import pytest

from elephant_news.llm.llm import llm_api, Message, Log
from elephant_news.llm.log_fn import no_print


@pytest.fixture
def log():
    log = Log("gpt-3.5-turbo", log_fn=no_print)
    return log


@pytest.fixture
def message():
    return Message(
        "user",
        "Please summarize this data",
    )


def test_log_set_model(log: Log):
    assert log.model == "gpt-3.5-turbo"
    log.set_model("gpt-4")
    assert log.model == "gpt-4"


def test_log_messages_token_length(log: Log, message: Message):
    assert log.messages_token_length == 0
    log.add_message(message)
    assert log.messages_token_length > 0


def test_log_add_and_undo_message(log: Log, message: Message):
    log.add_message(message)
    log.add_message(message)
    assert len(log.messages) == 2
    log.undo()
    assert len(log.messages) == 1
    log.undo()
    assert len(log.messages) == 0


def test_log_clear_messages(log: Log, message: Message):
    log.add_message(message)
    assert log.messages_token_length > 0
    log.clear()
    assert log.messages_token_length == 0


def test_llm_api(log: Log):
    log.messages = [
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
    reply = llm_api(log)
    assert type(reply) == str
    assert len(reply) > 0


def test_unknown_model(log: Log):
    log.set_model("unknown")
    reply = llm_api(log)
    assert reply == "Specified unknown model unknown."
