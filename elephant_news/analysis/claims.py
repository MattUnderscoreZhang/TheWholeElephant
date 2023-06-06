from dataclasses import dataclass
import json

from elephant_news.llm.llm import llm_api
from elephant_news.llm.log import Log, Message


@dataclass
class Claim:
    id: int
    claim: str


def list_claims(article: str) -> list[Claim]:
    log = Log("gpt-3.5-turbo")
    claims_query = f"""
The article is delimited with triple backticks.
Answer questions about the article by following these steps:

- First, identify all claims in the article text.
Each claim should be a single sentence, as short as possible.
Break complex claims into multiple smaller claims.

- Next, remove any empty claims.
Format claims by escaping quotes, removing extra whitespace, and correcting capitalization.

- Finally, format your response as a JSON list, with the following keys:
- id (int): an integer ID, with numbering starting from 0
- claim (str): a sentence summarizing the claim

Article: '''{article}'''
"""
    message = Message("user", claims_query)
    log.add_message(message)
    claims_text = llm_api(log)
    claims = json.loads(claims_text)
    claims = [Claim(**claim) for claim in claims]
    return claims
