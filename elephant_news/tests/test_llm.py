import pytest

from elephant_news.llm import Message, llm_api


@pytest.fixture
def messages():
    return [
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


def test_llm_api(messages: list[Message]):
    reply = llm_api(messages, "gpt-3.5-turbo", 0.7)
    assert type(reply) == str
    assert len(reply) > 0


def test_unknown_model(messages: list[Message]):
    reply = llm_api(messages, "unknown", 0.7)
    assert reply == "Specified unknown model unknown."
