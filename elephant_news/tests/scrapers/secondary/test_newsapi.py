import pytest

from elephant_news.core.log import Data
from elephant_news.scrapers.secondary.newsapi import NewsApiScraper


@pytest.fixture
def scraper() -> NewsApiScraper:
    scraper = NewsApiScraper()
    return scraper


def test_scraper(scraper: NewsApiScraper):
    articles = scraper.scrape()
    assert len(articles) > 0
    assert type(articles[0]) == Data
