from pathlib import Path

# from elephant_news.collection.news_sites.fox_news import parse
from elephant_news.collection.news_sites.general import parse


def test_parse():
    html_file = Path(__file__).parent.parent.parent / "data" / "html" / "2023_07_05_fox_prigozhin.html"
    with open(html_file, "r") as f:
        parse(f.read())
