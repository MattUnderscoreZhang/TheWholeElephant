import pytest

from elephant_news.core.llm import llm_api
from elephant_news.core.log import Article, Message, Log


@pytest.fixture
def log():
    messages = [
        Message(
            speaker="user",
            content="Hello, how are you?",
        ),
        Message(
            speaker="assistant",
            content="I'm doing well, how about you?",
        ),
        Message(
            speaker="user",
            content="I'm doing well too.",
        ),
    ]
    log = Log(
        model="gpt-3.5-turbo",
        article=Article(),
        messages=messages,
    )
    return log


def test_llm_api(log: Log):
    reply = llm_api(log, "gpt-3.5-turbo", 0.7)
    assert type(reply) == str
    assert len(reply) > 0


def test_unknown_model(log: Log):
    reply = llm_api(log, "unknown", 0.7)
    assert reply == "Specified unknown model unknown."
