import argparse
from enum import Enum, auto
from pathlib import Path

from elephant_news.autocomplete import prompt
from elephant_news.color_scheme import Colors
from elephant_news.llm import llm_api
from elephant_news.log import Message, Log, read_article, print_color


# Define command-line arguments
parser = argparse.ArgumentParser(description="Talk to LLM assistant")
parser.add_argument("--model", type=str, default="gpt-3.5-turbo", help="model to use")
parser.add_argument("--temperature", type=float, default=1, help="Sampling temperature for generating text")
args = parser.parse_args()


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


def main():
    print_color(f"Type '/' to show available commands. Enter '/exit' to exit.\n", Colors.info)
    log = Log(model=args.model)
    while True:
        # no newline
        user_input = prompt("You: ")
        loop_status = parse_user_input(user_input, log)
        if loop_status == LoopStatus.Break:
            break
        elif loop_status == LoopStatus.Continue:
            continue
        response = llm_api(log, args.model, args.temperature)
        print_color(f"\nassistant: {response}\n", Colors.assistant, indent=2)
        log.add_message(
            Message(
                speaker="assistant",
                content=response.strip(),
            )
        )


if __name__ == "__main__":
    main()
