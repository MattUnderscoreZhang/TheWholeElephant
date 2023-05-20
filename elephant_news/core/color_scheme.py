import builtins
from prompt_toolkit.styles import Style
from termcolor import colored
from typing import Any, NamedTuple


class Colors(NamedTuple):
    info = "blue"
    article = "yellow"
    user = "cyan"
    assistant = "magenta"
    warning = "red"


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


def print_color(content: Any = "", color: str = Colors.info):
    builtins.print(colored(str(content), color))
