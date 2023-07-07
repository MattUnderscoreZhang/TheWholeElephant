from pathlib import Path
import pytest

from elephant_news.collection.news_sites.fallback import parse


@pytest.mark.llm
def test_parse():
    html_file = Path(__file__).parent.parent.parent / "data" / "html" / "2023_07_05_fox_prigozhin.html"
    with open(html_file, "r") as f:
        article = parse(f.read())
    assert article.headline == "Mercenary warlord Prigozhin breaks silence following Belarus exile in message to Russian people: report"
    assert article.sub_headline == "Yevgeny Prigozhin has allegedly returned to Russia since his exile started."
    assert article.author == "Peter Aitken"
    assert "Russian mercenary warlord-turned-rebel Yevgeny Prigozhin appeared to call on the Russian public to join the Wagner Group" in article.text
    assert article.links == {}
    assert article.images == {}
    assert article.videos == {}
