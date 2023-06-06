from elephant_news.llm.llm import llm_api
from elephant_news.llm.log import Log, Message
from elephant_news.utils.text_parsing import break_into_list


def list_claims(article: str) -> list[str]:
    log = Log("gpt-3.5-turbo")
    claims_query = f"""
The article is delimited with triple backticks.
Answer questions about the article by following these steps:

- First, identify all claims in the article text.
Each claim should be a single sentence, as short as possible.
Break complex claims into multiple smaller claims.

- Next, remove any empty claims.
Format claims by escaping quotes, removing extra whitespace, and correcting capitalization.

- Finally, format the claims as a Python list of strings.

Article: '''{article}'''
"""
    message = Message("user", claims_query)
    log.add_message(message)
    claims_list_text = llm_api(log)
    claims_list = break_into_list(claims_list_text)
    return claims_list
