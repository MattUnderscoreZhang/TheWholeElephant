from enum import Enum, auto
import glob
from pathlib import Path
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document
from prompt_toolkit import shortcuts

from elephant_news.core.color_scheme import Colors, prompt_style, print_color
from elephant_news.core.llm import llm_api
from elephant_news.core.log import Log, Message, read_article


commands = [
    ("/help", "end the conversation"),
    ("/exit", "end the conversation"),
    ("/set_model", "set LLM model to use"),
    ("/set_article", "set article to read"),
    ("/log", "show the conversation log"),
    ("/undo", "delete last user message"),
    ("/clear", "clear log"),
]


class CommandCompleter(Completer):
    def get_completions(self, document: Document, _: CompleteEvent):
        text_before_cursor = document.text_before_cursor
        words_before_cursor = text_before_cursor.split()
        current_word = document.get_word_under_cursor()

        # Suggest filepaths if "/set_article" is typed
        if (
            (
                (len(words_before_cursor) == 1 and current_word == "")
                or (len(words_before_cursor) == 2)
            )
            and words_before_cursor[0] == "/set_article"
        ):
            root = "elephant_news/articles/"
            path = "".join(words_before_cursor[1:])
            suggestions = [
                Completion(
                    suggestion,
                    start_position=-len(path),
                    display=suggestion,
                    display_meta="",
                ) for suggestion in glob.glob(root + path + "*")
            ]
            for suggestion in suggestions:
                yield suggestion

        # Suggest models if /set_model is typed
        elif (
            (
                (len(words_before_cursor) == 1 and current_word == "")
                or (len(words_before_cursor) == 2)
            )
            and words_before_cursor[0] == "/set_model"
        ):
            model = "".join(words_before_cursor[1:])
            suggestions = [
                Completion(
                    suggestion,
                    start_position=-len(model),
                    display=suggestion,
                    display_meta="",
                ) for suggestion in [
                    "gpt-3.5-turbo",
                    "gpt-4",
                    "gpt-4-32k",
                ]
            ]
            for suggestion in suggestions:
                yield suggestion

        # Command suggestions
        elif len(words_before_cursor) == 1 and words_before_cursor[0].startswith('/'):
            for command, description in [
                c for c in commands
                if c[0].startswith(words_before_cursor[-1])
            ]:
                yield Completion(
                    command,
                    start_position=-len(current_word)-1,
                    display=command,
                    display_meta=description,
                )


class LoopStatus(Enum):
    Break = auto()
    Continue = auto()
    NoAction = auto()


def parse_user_input(user_input: str, log: Log) -> LoopStatus:
    if user_input == "/exit":
        return LoopStatus.Break
    elif user_input.startswith("/set_model"):
        model = user_input.split()[1]
        log.set_model(model)
    elif user_input.startswith("/set_article"):
        article_path = Path(user_input.split()[1])
        log.set_article(read_article(article_path))
    elif user_input == "/log":
        log.print()
    elif user_input == "/undo":
        log.undo()
    elif user_input == "/clear":
        log.clear()
    elif user_input.startswith('/'):
        print_color(f"Invalid command.\n", Colors.info)
    else:
        log.add_message(
            Message(
                speaker="user",
                content=user_input.strip(),
            )
        )
        return LoopStatus.NoAction
    return LoopStatus.Continue


def start_menu(log: Log, model: str, temperature: float) -> None:
    while True:
        # no newline
        user_input = shortcuts.prompt("You: ", style=prompt_style, completer=CommandCompleter())
        loop_status = parse_user_input(user_input, log)
        if loop_status == LoopStatus.Break:
            break
        if loop_status == LoopStatus.Continue:
            continue
        response = llm_api(log, model, temperature)
        print_color(f"\nassistant: {response}\n", Colors.assistant)
        log.add_message(
            Message(
                speaker="assistant",
                content=response.strip(),
            )
        )
