import pytest

from elephant_news.core.log import Article
from elephant_news.scrapers.newsapi import NewsApiScraper


@pytest.fixture
def scraper() -> NewsApiScraper:
    scraper = NewsApiScraper()
    return scraper


def test_scraper(scraper: NewsApiScraper):
    articles = scraper.scrape()
    assert len(articles) > 0
    assert type(articles[0]) == Article
