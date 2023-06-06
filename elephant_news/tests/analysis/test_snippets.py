import pytest
from pprint import pprint

from elephant_news.analysis import snippets
from elephant_news.tests.analysis.article import article_text, claims, sources


# @pytest.mark.llm
def test_list_snippets():
    results = snippets.list_snippets(article_text, claims, sources)
    pprint(results)
    breakpoint()
