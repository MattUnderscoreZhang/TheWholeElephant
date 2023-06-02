import argparse
import glob
from prompt_toolkit.completion import CompleteEvent, Completer, Completion
from prompt_toolkit.document import Document
from prompt_toolkit.shortcuts import prompt
from prompt_toolkit.styles import Style

from elephant_news.llm.llm import llm_api
from elephant_news.llm.log import Log, LogMessageType, Message


# TODO: integrate command completion and functions into commands list
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


def start_conversation(log: Log):
    log.log_fn(f"Type '/' to show available commands. Enter '/exit' to exit.\n", LogMessageType.info)
    prompt_style = Style.from_dict(
        {
            # default style
            "": "#ffdaac",
            # prompt
            "username": "#884444 italic",
            "at": "#00aa00",
            "colon": "#00aa00",
            "pound": "#00aa00",
            "host": "#000088 bg:#aaaaff",
            "path": "#884444 underline",
            # make a selection reverse/underlined
            # (use control+space to select)
            "selected-text": "reverse underline",
        }
    )
    while True:
        user_input = prompt("You: ", style=prompt_style, completer=CommandCompleter())
        if user_input == "/exit":
            break
        elif user_input.startswith("/set_model"):
            model = user_input.split()[1]
            log.set_model(model)
        elif user_input == "/log":
            log.print()
        elif user_input == "/undo":
            log.undo()
        elif user_input == "/clear":
            log.clear()
        elif user_input.startswith('/'):
            log.log_fn(f"Invalid command.\n", LogMessageType.info)
        else:
            log.add_message(
                Message(
                    speaker="user",
                    content=user_input.strip(),
                )
            )
            response = llm_api(log)
            log.log_fn(f"\nassistant: {response}\n", LogMessageType.assistant)
            log.add_message(
                Message(
                    speaker="assistant",
                    content=response.strip(),
                )
            )


def main():
    # set up log using command line arguments
    parser = argparse.ArgumentParser(description="Talk to LLM assistant")
    parser.add_argument("--model", type=str, default="gpt-3.5-turbo", help="model to use")
    parser.add_argument("--temperature", type=float, default=1, help="Sampling temperature for generating text")
    args = parser.parse_args()
    log = Log(model=args.model, temperature=args.temperature)

    # start conversation
    start_conversation(log)


if __name__ == "__main__":
    main()
