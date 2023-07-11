from dataclasses import dataclass, field
from dotenv import load_dotenv
import os
import requests


load_dotenv()  # .env file
API_KEY = os.getenv("NEWSAPI_KEY")


@dataclass
class Data:
    author: str = ""
    content: str = ""
    description: str = ""
    publishedAt: str = ""
    source: dict[str, str] = field(default_factory=dict)
    title: str = ""
    url: str = ""
    urlToImage: str = ""


class Scraper:
    def scrape(self) -> list[Data]:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
        results = requests.get(url).json()
        assert results["status"] == "ok"
        # total_results = results["totalResults"]
        articles = [
            Data(**article)
            for article in results["articles"]
        ]
        return articles
