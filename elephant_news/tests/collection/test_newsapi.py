from elephant_news.collection import newsapi


def test_scraper():
    scraper = newsapi.Scraper()
    articles = scraper.scrape()
    assert len(articles) > 0
    assert type(articles[0]) == newsapi.Data
