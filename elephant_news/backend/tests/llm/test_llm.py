import pytest

from elephant_news.llm.llm import llm_api
from elephant_news.llm.log import Message, Log
from elephant_news.llm.log_fn import no_print


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
        messages=messages,
        log_fn=no_print,
    )
    return log


def test_llm_api(log: Log):
    reply = llm_api(log)
    assert type(reply) == str
    assert len(reply) > 0


def test_unknown_model(log: Log):
    log.set_model("unknown")
    reply = llm_api(log)
    assert reply == "Specified unknown model unknown."
