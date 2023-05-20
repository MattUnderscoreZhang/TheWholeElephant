from elephant_news.scrapers.primary import congress


def test_scraper():
    scraper = congress.Scraper()
    bills = scraper.scrape()
    assert len(bills) > 0
    assert type(bills[0]) == congress.Bill

    result = scraper.query(bills)
    assert type(result) == str
