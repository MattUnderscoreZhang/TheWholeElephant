from dataclasses import dataclass
import json

from elephant_news.analysis.claims import Claim
from elephant_news.analysis.sources import Source
from elephant_news.llm.llm import llm_api, Log, Message


@dataclass
class Snippet:
    id: int
    snippet: str
    claim_ids: list[int]
    source_ids: list[int]


def list_snippets(article: str, claims: list[Claim], sources: list[Source]) -> list[Snippet]:
    log = Log("gpt-3.5-turbo")
    claims_text = "\n".join([f"{claim.id}: {claim.claim}" for claim in claims])
    sources_text = "\n".join([f"{source.id}: {source.description}" for source in sources])
    snippets_query = f"""
The article, claims made by the article, and sources cited by those claims are given below in triple backticks.
Divide the article text into snippets, where snippets should cover the entire article without overlap.
Format your response as a JSON list, with the following keys:
- id (int): an integer ID, with numbering starting from 0
- snippet (str): the text of the snippet
- claim_ids (list[int]): a list of IDs of claims made by the snippet (this list may be empty)
- source_ids (list[int]): a list of IDs of sources cited by the snippet (this list may be empty)

Article: '''{article}'''

Claims: '''{claims_text}'''

Sources: '''{sources_text}'''
"""
    message = Message("user", snippets_query)
    log.add_message(message)
    snippets_text = llm_api(log)
    snippets = json.loads(snippets_text)
    snippets = [Snippet(**snippet) for snippet in snippets]
    return snippets
