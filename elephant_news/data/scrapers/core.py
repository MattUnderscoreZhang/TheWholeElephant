from elephant_news.cli.log import Data


class Scraper:
    def __init__(self):
        ...

    def scrape(self) -> list[Data]:
        raise NotImplementedError
