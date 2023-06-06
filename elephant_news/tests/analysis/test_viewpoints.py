import pytest
from pprint import pprint

from elephant_news.analysis import viewpoints
from elephant_news.tests.analysis.article import claims


@pytest.mark.llm
def test_analyze_viewpoints():
    results = viewpoints.analyze_viewpoints(claims)
    pprint(results)
    breakpoint()
