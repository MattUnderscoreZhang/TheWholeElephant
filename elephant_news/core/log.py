from dataclasses import dataclass, field
from dataclasses_json import dataclass_json
from pathlib import Path
import tiktoken
from typing import Optional

from elephant_news.core.color_scheme import Colors, print_color


@dataclass
class Message:
    speaker: str
    content: str

    def __str__(self) -> str:
        return f"{self.speaker}: {self.content}"


@dataclass_json
@dataclass
class Article:
    author: str = ""
    content: str = ""
    description: str = ""
    publishedAt: str = ""
    source: dict[str, str] = field(default_factory=dict)
    title: str = ""
    url: str = ""
    urlToImage: str = ""


def read_article(filepath: Path) -> Article:
    try:
        with open(filepath) as f:
            article = Article.from_json(f.read())
            return article
    except IsADirectoryError:
        print_color(f"Path is a directory: {filepath}\n", Colors.info)
    except FileNotFoundError:
        print_color(f"File not found: {filepath}\n", Colors.info)
    return Article()


@dataclass
class Log:
    model: str
    article: Optional[Article] = None
    messages: list[Message] = field(default_factory=list)

    def set_model(self, new_model: str) -> None:
        self.model = new_model
        print_color(f"You are now talking to the {self.model} model.\n")

    def set_article(self, article: Article) -> None:
        self.article = article
        self.messages = []
        print_color(f"You have pinned article \"{self.article.title}\".\n")

    @property
    def messages_token_length(self) -> int:
        enc = tiktoken.encoding_for_model(self.model)
        length = sum([
            len(enc.encode(message.content))
            for message in self.messages
        ])
        return length

    def print(self) -> None:
        if self.article is None:
            print_color("No article pinned.\n", Colors.info)
            return
        print_color(self.article, Colors.article)
        for message in self.messages:
            color = Colors.user if message.speaker == "user" else Colors.assistant
            print_color(message.content, color)
        print()

    def add_message(self, message: Message) -> None:
        self.messages.append(message)

    def undo(self) -> None:
        while len(self.messages) > 0:
            message = self.messages.pop()
            if message.speaker == "user":
                break
        print_color(f"Rewound to state of last message.", Colors.info)
        print()

    def clear(self):
        self.messages = []
        print_color("Messages cleared.", Colors.info)
        print()
