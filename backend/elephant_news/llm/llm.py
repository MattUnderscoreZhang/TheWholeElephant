from dataclasses import dataclass, field
from dotenv import load_dotenv
import tiktoken
from time import sleep, time
import openai
from openai import error
import os

from elephant_news.llm.log_fn import LogFn, LogMessageType, no_print


load_dotenv()  # load the OpenAI API key from a .env file
openai.api_key = os.getenv("OPENAI_API_KEY")


# rate limiter
last_call: float = time()


@dataclass
class Message:
    speaker: str
    content: str

    def __str__(self) -> str:
        return f"{self.speaker}: {self.content}"


@dataclass
class Log:
    model: str
    temperature: float = 0.0
    messages: list[Message] = field(default_factory=list)
    log_fn: LogFn = no_print

    def get_encoding_length(self, text: str) -> int:
        enc = tiktoken.encoding_for_model(self.model)
        return len(enc.encode(text))

    def get_model_max_encoding_length(self) -> int:
        match self.model:
            case "gpt-3.5-turbo":
                return 4097
            case "gpt-3.5-turbo-16k":
                return 16358
            case _:
                raise Exception(f"Unknown model: {self.model}")

    @property
    def messages_token_length(self) -> int:
        return sum([
            self.get_encoding_length(message.content)
            for message in self.messages
        ])

    def set_model(self, new_model: str) -> None:
        self.model = new_model
        self.log_fn(f"You are now talking to the {self.model} model.\n", LogMessageType.info)

    def print(self) -> None:
        for message in self.messages:
            self.log_fn(
                message.content,
                LogMessageType.user if message.speaker == "user" else LogMessageType.assistant
            )
        self.log_fn("\n", LogMessageType.info)

    def add_message(self, message: Message) -> None:
        self.messages.append(message)

    def ask(self, question: str) -> str:
        saved_messages = self.messages
        self.messages = [
            Message(
                speaker="user",
                content=question,
            ),
        ]
        reply = llm_api(self)
        self.messages = saved_messages
        return reply

    def undo(self) -> None:
        while len(self.messages) > 0:
            message = self.messages.pop()
            if message.speaker == "user":
                break
        self.log_fn(f"Rewound to state of last message.\n", LogMessageType.info)

    def clear(self):
        self.messages = []
        self.log_fn("Messages cleared.\n", LogMessageType.info)


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
                prompt="\n".join([f"{m.speaker}: {m.content}" for m in log.messages]) + "assistant: ",
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
