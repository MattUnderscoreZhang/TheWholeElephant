import pytest
from pprint import pprint

from elephant_news.analysis import sources
from elephant_news.tests.analysis.examples.article_2 import article_text


@pytest.mark.llm
def test_list_sources():
    results = sources.list_sources(article_text)
    pprint(results)
    breakpoint()
