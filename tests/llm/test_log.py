import os
from pathlib import Path
import pytest

from elephant_news.llm.log import Log, Message


@pytest.fixture
def data():
    root_dir = Path(os.getcwd())
    data = read_article(root_dir / "elephant_news" / "articles" / "2023_05_17_nyt_record_heat_forecast.json")
    return data


@pytest.fixture
def article2():
    root_dir = Path(os.getcwd())
    data = read_article(root_dir / "elephant_news" / "articles" / "2023_05_19_washingtonpost_debt_ceiling_talks_pause.json")
    return data


@pytest.fixture
def log(data: Data):
    log = Log("gpt-3.5-turbo")
    log.set_article(data)
    return log


@pytest.fixture
def message():
    return Message(
        "user",
        "Please summarize this data",
    )


def test_read_article(data: Data):
    assert data.title == "Heat Will Likely Soar to Record Levels in Next 5 Years, New Analysis Says"


def test_log_set_model(log: Log):
    assert log.model == "gpt-3.5-turbo"
    log.set_model("gpt-4")
    assert log.model == "gpt-4"


def test_log_set_article(log: Log, article2: Data):
    assert log.data is not None
    assert log.data.title == "Heat Will Likely Soar to Record Levels in Next 5 Years, New Analysis Says"
    log.set_article(article2)
    assert log.data.title == "White House, GOP resume debt ceiling talks after brief breakdown"


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
