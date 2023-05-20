from elephant_news.core.log import Article


class Scraper:
    def __init__(self):
        ...

    def scrape(self) -> list[Article]:
        raise NotImplementedError
