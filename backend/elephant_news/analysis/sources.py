from dataclasses import dataclass
import json

from elephant_news.llm.llm import llm_api, Log, Message


@dataclass
class Source:
    id: int
    description: str
    source_type: str
    is_primary_source: bool
    is_available_online: bool


def list_sources(article: str) -> list[Source]:
    log = Log("gpt-3.5-turbo")
    sources_query = f"""
The article is delimited with triple backticks.
List all sources cited to support the sources in the article.
Format your response as a JSON list, with the following keys:
- id (int): an integer ID, with numbering starting from 0
- description (str): a sentence describing what the source contains and where it's from
- source_type (str): one of the following words: interview, speech, transcript, article, press_release, other
- is_primary_source (bool)
- is_available_online (bool): whether a copy of the original cited source can reasonably be expected to be found online

Article: '''{article}'''
"""
    message = Message("user", sources_query)
    log.add_message(message)
    sources_text = llm_api(log)
    sources = json.loads(sources_text)
    sources = [Source(**source) for source in sources]
    return sources
