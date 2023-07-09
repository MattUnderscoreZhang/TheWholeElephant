import pytest

from elephant_news.analysis import claims
from elephant_news.tests.analysis.examples.article_3 import article_text
from elephant_news.utils.health_check import get_rich_print, save_test_log


@pytest.mark.llm
def test_list_claims():
    results = claims.list_claims(article_text)
    log_info = (
        ">>> We analyze article text to extract claims.\n\n" +
        ">>> Article text:\n" +
        get_rich_print(article_text) + "\n" +
        ">>> Claims:\n" +
        get_rich_print(results)
    )
    save_test_log('test_list_claims', log_info)
