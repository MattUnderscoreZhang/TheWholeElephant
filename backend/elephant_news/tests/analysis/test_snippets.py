import pytest

from elephant_news.analysis import snippets
from elephant_news.tests.analysis.examples.article_2 import article_text, claims, sources
from elephant_news.utils.health_check import get_rich_print, save_test_log


@pytest.mark.llm
def test_list_snippets():
    results = snippets.list_snippets(article_text, claims, sources)
    log_info = (
        ">>> We analyze article text and claims to extract snippets.\n\n" +
        ">>> Article text:\n" +
        get_rich_print(article_text) + "\n" +
        ">>> Claims:\n" +
        get_rich_print(claims) + "\n" +
        ">>> Snippets:\n" +
        get_rich_print(results)
    )
    save_test_log('test_list_snippets', log_info)
