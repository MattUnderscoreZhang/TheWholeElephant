from elephant_news.core.log import Data


class Scraper:
    def __init__(self):
        ...

    def scrape(self) -> list[Data]:
        raise NotImplementedError
