import pytest
from pprint import pprint

from elephant_news.analysis import claims
from elephant_news.tests.analysis.examples.article_1 import article_text


@pytest.mark.llm
def test_list_claims():
    results = claims.list_claims(article_text)
    pprint(results)
    breakpoint()
