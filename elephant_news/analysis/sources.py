import json

from elephant_news.llm.llm import llm_api
from elephant_news.llm.log import Log, Message
from elephant_news.utils.text_parsing import break_into_list


def list_sources(article: str) -> list[str]:
    log = Log("gpt-3.5-turbo")
    sources_query = f"""
The article is delimited with triple backticks.
List all sources cited to support the sources in the article.
Format your response as a JSON list, with the following keys: SourceDescription (str), IsPrimarySource (bool), IsAvailableOnline (bool).

Article: '''{article}'''
"""
# TODO: include type of source
    message = Message("user", sources_query)
    log.add_message(message)
    sources_text = llm_api(log)
    sources = json.loads(sources_text)
    breakpoint()
    return sources
