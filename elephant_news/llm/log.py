from dataclasses import dataclass, field
import tiktoken

from elephant_news.llm.log_fn import LogFn, LogMessageType, no_print


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

    @property
    def messages_token_length(self) -> int:
        enc = tiktoken.encoding_for_model(self.model)
        length = sum([
            len(enc.encode(message.content))
            for message in self.messages
        ])
        return length

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

    def undo(self) -> None:
        while len(self.messages) > 0:
            message = self.messages.pop()
            if message.speaker == "user":
                break
        self.log_fn(f"Rewound to state of last message.\n", LogMessageType.info)

    def clear(self):
        self.messages = []
        self.log_fn("Messages cleared.\n", LogMessageType.info)
