import argparse

from elephant_news.core.color_scheme import Colors, print_color
from elephant_news.core.log import Log
from elephant_news.core.menu import start_menu
from elephant_news.core.web import app


# Define command-line arguments
parser = argparse.ArgumentParser(description="Talk to LLM assistant")
parser.add_argument("--model", type=str, default="gpt-3.5-turbo", help="model to use")
parser.add_argument("--temperature", type=float, default=1, help="Sampling temperature for generating text")
parser.add_argument("--interface", type=str, default="web", help="interface: cmd (command line) or web (web port 5000)")
args = parser.parse_args()


def main():
    print_color(f"Type '/' to show available commands. Enter '/exit' to exit.\n", Colors.info)
    log = Log(model=args.model)
    interface = "web" # args.interface
    if interface == "cmd":
       start_menu(log, args.model, args.temperature)
    else:
        app.run()

if __name__ == "__main__":
    main()
