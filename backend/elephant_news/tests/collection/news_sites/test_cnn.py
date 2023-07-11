from pathlib import Path

from elephant_news.collection.news_sites.cnn import parse


def test_parse():
    html_file = Path(__file__).parent.parent.parent / "data" / "html" / "2023_07_06_cnn_financially_secure.html"
    raise NotImplementedError("TODO: add test")
    with open(html_file, "r") as f:
        article = parse(f.read())
    assert article.headline == ""
    assert article.sub_headline == ""
    assert article.author == ""
    assert "" in article.text
    assert article.links == {
    }
    assert article.images == {
    }
    assert article.videos == {
    }
