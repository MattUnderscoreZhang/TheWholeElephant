from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from dotenv import load_dotenv
import os
import requests

from elephant_news.collection.core import Scraper


load_dotenv()  # .env file
API_KEY = os.getenv("NEWSAPI_KEY")


@dataclass_json
@dataclass
class Article:
    author: str = ""
    content: str = ""
    description: str = ""
    publishedAt: str = ""
    source: dict[str, str] = field(default_factory=dict)
    title: str = ""
    url: str = ""
    urlToImage: str = ""


class NewsApiScraper(Scraper):
    def scrape(self) -> list[Article]:
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
        results = requests.get(url).json()
        assert results["status"] == "ok"
        # total_results = results["totalResults"]
        articles = [
            Article.from_dict(article)
            for article in results["articles"]
        ]
        return articles
