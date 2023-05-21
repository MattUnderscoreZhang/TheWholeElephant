from dataclasses import dataclass
from dataclasses_json import dataclass_json
import datetime
from dotenv import load_dotenv
import os
import requests
from typing import Literal

from elephant_news.core.llm import llm_api
from elephant_news.core.log import Data, Log, Message


load_dotenv()  # .env file
API_KEY = os.getenv("CONGRESS_API_KEY")


@dataclass_json
@dataclass
class Bill:
    congress: int
    latestAction: dict[str, str]
    number: int
    originChamber: Literal["House", "Senate"]
    originChamberCode: Literal["H", "S"]
    title: str
    type: Literal["HR", "S", "HRES", "SRES", "HJRES", "SJRES", "HCONRES", "SCONRES"]
    updateDate: str
    updateDateIncludingText: str
    url: str


def today() -> str:
    date = datetime.date.today()
    return f"{date.year}-{date.month}-{date.day}"


class Scraper:
    def scrape(self) -> list[Bill]:
        url = f"https://api.congress.gov/v3/bill?api_key={API_KEY}"
        results = requests.get(url).json()
        bills = [
            Bill.from_dict(bill)
            for bill in results["bills"]
        ]
        bills = [
            bill
            for bill in bills
            if bill.latestAction['actionDate'] == today()
        ]
        return bills

    def query(self, bills: list[Bill]) -> str:
        log = Log(model="gpt-3.5-turbo")
        log.set_data(Data())
        log.add_message(
            Message(
                speaker="user",
                content="".join([bill.to_json() for bill in bills]),
            )
        )
        log.add_message(
            Message(
                speaker="user",
                content="This data contains information about several bills currently in the US Congress. Each bill is identified by its number, title, type, origin chamber, Congress number, and URL. The latest action taken on each bill is also provided, along with the subcommittee it was referred to. Summarize the bills and  latest actions.",
            )
        )
        response = llm_api(log)
        return response
