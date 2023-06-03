import pytest

from elephant_news.analysis import claims
from elephant_news.tests.analysis.article import article


def test_break_into_list():
    claims_list_text = "['claim 1', 'claim 2', 'claim 3']"
    claims_list = claims.break_into_list(claims_list_text)
    assert claims_list == ["claim 1", "claim 2", "claim 3"]


@pytest.mark.llm
def test_list_claims():
    article_text = article.title + "\n" + article.text + "\n" + "Related articles:\n" + "\n".join(article.related_articles)
    results = claims.list_claims(article_text)
    breakpoint()
