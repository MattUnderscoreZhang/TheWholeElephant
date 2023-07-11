import pytest

from elephant_news.analysis import viewpoints
from elephant_news.tests.analysis.examples.article_1 import claims
from elephant_news.utils.health_check import get_rich_print, save_test_log


@pytest.mark.llm
def test_analyze_viewpoints():
    results = viewpoints.analyze_viewpoints(claims)
    log_info = (
        ">>> We analyze claims in order to extract viewpoints.\n\n" +
        ">>> Claims:\n" +
        get_rich_print(claims) + "\n" +
        ">>> Viewpoints:\n" +
        get_rich_print(results)
    )
    save_test_log('test_analyze_viewpoints', log_info)
