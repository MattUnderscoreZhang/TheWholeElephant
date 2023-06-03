from elephant_news.collection import congress


def test_scraper():
    scraper = congress.Scraper()
    bills = scraper.scrape(from_today=False)
    assert len(bills) > 0
    assert type(bills[0]) == congress.Data
