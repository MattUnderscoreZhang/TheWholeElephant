import builtins
from dataclasses import dataclass, field
import json
from pathlib import Path
from termcolor import colored
import tiktoken
from typing import Optional

from elephant_news.color_scheme import Colors
from elephant_news.llm import Message


@dataclass
class Article:
    title: str = ""
    subtitle: str = ""
    author: str = ""
    date: str = ""
    updated: str = ""
    url: str = ""
    contents: str = ""


def read_article(filepath: Path) -> Article:
    try:
        with open(filepath) as f:
            file_contents = json.loads(f.read())
            article = Article(
                title=file_contents["title"],
                subtitle=file_contents["subtitle"],
                author=file_contents["author"],
                date=file_contents["date"],
                updated=file_contents["updated"],
                url=file_contents["url"],
                contents=file_contents["contents"],
            )
            return article
    except IsADirectoryError:
        print(f"Path is a directory: {filepath}\n", Colors.info)
    except FileNotFoundError:
        print(f"File not found: {filepath}\n", Colors.info)
    return Article()


@dataclass
class Log:
    model: str
    article: Optional[Article] = None
    messages: list[Message] = field(default_factory=list)

    def set_model(self, new_model: str) -> None:
        self.model = new_model
        print(f"You are now talking to the {self.model} model.\n")

    def set_article(self, article: Article) -> None:
        self.article = article
        print(f"You have pinned article \"{self.article.title}\".\n")

    @property
    def messages_token_length(self) -> int:
        enc = tiktoken.encoding_for_model(self.model)
        length = sum([
            len(enc.encode(message.content))
            for message in self.messages
        ])
        return length

    def print(self) -> None:
        for message in self.messages:
            color = Colors.user if message.speaker == "user" else Colors.assistant
            builtins.print(colored(message.content, color))
        print()

    def add_message(self, message: Message) -> None:
        self.messages.append(message)

    def undo(self) -> None:
        while len(self.messages) > 0:
            message = self.messages.pop()
            if message.speaker == "user":
                break
        print(f"Rewound to state of last message.", Colors.info)
        print()

    def clear(self):
        self.messages = []
        print("Messages cleared.", Colors.info)
        print()
