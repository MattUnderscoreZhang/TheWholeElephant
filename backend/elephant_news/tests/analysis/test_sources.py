import pytest

from elephant_news.analysis import sources
from elephant_news.tests.analysis.examples.article_2 import article_text
from elephant_news.utils.health_check import get_rich_print, save_test_log


@pytest.mark.llm
def test_list_sources():
    results = sources.list_sources(article_text)
    log_info = (
        ">>> We analyze article text to extract sources.\n\n" +
        ">>> Article text:\n" +
        get_rich_print(article_text) + "\n" +
        ">>> Sources:\n" +
        get_rich_print(results)
    )
    save_test_log('test_list_sources', log_info)
