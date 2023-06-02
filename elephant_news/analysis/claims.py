from elephant_news.llm.llm import llm_api
from elephant_news.llm.log import Log, Message


def break_into_list(list_text: str) -> list[str]:
    first_bracket = list_text.find("[")
    last_bracket = list_text.rfind("]")
    list_text = list_text[first_bracket + 1: last_bracket - 1]

    split_claims = list_text.split("'")
    split_claims = [s for s in split_claims if s != "" and s != ", "]
    return split_claims


def list_claims(article: str) -> list[str]:
    log = Log("gpt-3.5-turbo")
    message = Message(
        "user",
        "Summarize the claims in the following article.",
    )
    log.add_message(message)
    message = Message(
        "user",
        article,
    )
    log.add_message(message)
    claims = llm_api(log)

    log.clear()
    message = Message(
        "user",
        "Break these claims into a logical list of individual claims, like ['claim 1', 'claim 2', etc.]. Each claim should be as small as possible. Break complex claims into multiple smaller claims. Make sure any single quotes in claims are escaped with a backslash. Format claims into coherent sentences, and remove any extraneous markup like newlines, extra whitespace, odd capitalization, etc.",
    )
    log.add_message(message)
    message = Message(
        "user",
        claims,
    )
    log.add_message(message)
    claims_list_text = llm_api(log)
    breakpoint()

    claims_list = break_into_list(claims_list_text)
    return claims_list
