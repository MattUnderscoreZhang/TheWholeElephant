# TODO: fix tests
"""
import pytest

from elephant_news.cli.log import Data
from elephant_news.collection.newsapi import NewsApiScraper


@pytest.fixture
def scraper() -> NewsApiScraper:
    scraper = NewsApiScraper()
    return scraper


def test_scraper(scraper: NewsApiScraper):
    articles = scraper.scrape()
    assert len(articles) > 0
    assert type(articles[0]) == Data
"""
