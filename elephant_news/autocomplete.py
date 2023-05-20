import glob
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document
from prompt_toolkit import shortcuts

from elephant_news.color_scheme import prompt_style


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
    def get_completions(self, document: Document, complete_event: CompleteEvent):
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


def prompt(prompt_str: str) -> str:
    return shortcuts.prompt(prompt_str, style=prompt_style, completer=CommandCompleter())
