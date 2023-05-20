from dotenv import load_dotenv
import os
import requests

from elephant_news.core.log import Article
from elephant_news.scrapers.core import Scraper


load_dotenv()  # .env file
API_KEY = os.getenv("NEWSAPI_KEY")


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
