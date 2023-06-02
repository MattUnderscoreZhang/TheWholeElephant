from dataclasses import dataclass
from dataclasses_json import dataclass_json
from uuid import UUID


@dataclass_json
@dataclass
class Data:
    uuid: UUID
    title: str
    content: str
    summary: str = ""
    publishedAt: str = ""


# to be added to log.py when ready
"""
    def read_article(self, filepath: Path) -> Data:
        try:
            with open(filepath) as f:
                return Data.from_json(f.read())
        except IsADirectoryError:
            self.log_fn(f"Path is a directory: {filepath}\n", Colors.info)
        except FileNotFoundError:
            self.log_fn(f"File not found: {filepath}\n", Colors.info)
        return Data()

    def set_data(self, data: Data) -> None:
        self.data = data
        self.messages = []
        self.log_fn(f"You are now discussing \"{self.data.title}\".\n")
"""


# to be added to test_log.py
"""
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


def test_read_article(data: Data):
    assert data.title == "Heat Will Likely Soar to Record Levels in Next 5 Years, New Analysis Says"


def test_log_set_article(log: Log, article2: Data):
    assert log.data is not None
    assert log.data.title == "Heat Will Likely Soar to Record Levels in Next 5 Years, New Analysis Says"
    log.set_article(article2)
    assert log.data.title == "White House, GOP resume debt ceiling talks after brief breakdown"
"""


# to be added to llm.py
"""
def llm_api(log: Log) -> str:
    global last_call
    if time() - last_call < 1:
        sleep(1)
        last_call = time()
    model = log.model
    temperature = log.temperature
    try:
        if model in [
            "gpt-4",
            "gpt-4-0314",
            "gpt-4-32k",
            "gpt-4-32k-0314",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-0301",
        ]:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {
                        "role": "user",
                        "content": log.article.to_json(),
                    }
                ] + [
                    {
                        "role": m.speaker,
                        "content": m.content
                    }
                    for m in log.messages
                ],
                temperature=temperature,
                frequency_penalty=0,
                presence_penalty=0
            )
            return response.choices[0].message.content
        elif model in [
            "text-davinci-003",
            "text-davinci-002",
            "text-curie-001",
            "text-babbage-001",
            "text-ada-001",
            "davinci",
            "curie",
            "babbage",
            "ada",
        ]:
            response = openai.Completion.create(
                model=model,
                prompt=log.article.to_json() + "\n".join([f"{m.speaker}: {m.content}" for m in log.messages]) + "assistant: ",
                temperature=temperature,
                max_tokens=100,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
            )
            return response.choices[0].text
        else:
            return str(f"Specified unknown model {model}.")
    except error.APIConnectionError as e:
        return str(e.user_message)
"""
