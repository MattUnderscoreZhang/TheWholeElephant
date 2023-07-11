from dataclasses import dataclass
import json

from elephant_news.analysis.claims import Claim
from elephant_news.llm.llm import llm_api, Log, Message


@dataclass
class ClaimAnalysis:
    id: int
    support_ids: list[int]
    refute_ids: list[int]
    is_opinion: bool


def analyze_viewpoints(claims: list[Claim]) -> list[ClaimAnalysis]:
    log = Log("gpt-3.5-turbo")
    claims_text = "\n".join([f"{claim.id}: {claim.claim}" for claim in claims])
    snippets_query = f"""
A list of claims from a news article are listed in triple quotes.
For each claim, analyze whether the claim supports one or more other claims, refutes one or more other claims, or stands alone.
Also analyze whether each claim expresses someone's opinion or an objective fact.
Format your response as a JSON list, with the following keys:
- id (int): claim ID
- support_ids (list[int]): a list of IDs of claims made by the snippet (this list may be empty)
- refute_ids (list[int]): a list of IDs of sources cited by the snippet (this list may be empty)
- is_opinion (bool): whether the claim expresses an opinion or an objective fact
Remember that in JSON, 'true' and 'false' are lowercase.

Claims: '''{claims_text}'''
"""
    message = Message("user", snippets_query)
    log.add_message(message)
    viewpoints_text = llm_api(log)
    viewpoints = json.loads(viewpoints_text)
    viewpoints = [ClaimAnalysis(**viewpoint) for viewpoint in viewpoints]
    return viewpoints
