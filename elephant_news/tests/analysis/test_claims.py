import pytest

from elephant_news.analysis import claims
from elephant_news.tests.analysis.article import article


@pytest.mark.llm
def test_list_claims():
    article_text = article.title + "\n" + article.text + "\n" + "Related articles:\n" + "\n".join(article.related_articles)
    results = claims.list_claims(article_text)
    breakpoint()
