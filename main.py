import argparse

from elephant_news.color_scheme import Colors, print_color
from elephant_news.log import Log
from elephant_news.menu import start_menu


# Define command-line arguments
parser = argparse.ArgumentParser(description="Talk to LLM assistant")
parser.add_argument("--model", type=str, default="gpt-3.5-turbo", help="model to use")
parser.add_argument("--temperature", type=float, default=1, help="Sampling temperature for generating text")
args = parser.parse_args()


def main():
    print_color(f"Type '/' to show available commands. Enter '/exit' to exit.\n", Colors.info)
    log = Log(model=args.model)
    start_menu(log, args.model, args.temperature)


if __name__ == "__main__":
    main()
