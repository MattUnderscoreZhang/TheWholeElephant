import pytest

from elephant_news.analysis import sources
from elephant_news.tests.analysis.article import article


# @pytest.mark.llm
def test_list_sources():
    article_text = article.title + "\n" + article.text + "\n" + "Related articles:\n" + "\n".join(article.related_articles)
    results = sources.list_sources(article_text)
    breakpoint()
