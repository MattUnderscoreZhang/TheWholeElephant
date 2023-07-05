def remove_newlines(text: str) -> str:
    return text.replace("\n", "")


def break_into_list(list_text: str) -> list[str]:
    first_bracket = list_text.find("[")
    last_bracket = list_text.rfind("]")
    list_text = list_text[first_bracket + 2: last_bracket - 1]

    split_claims = list_text.split("\",\"")
    return split_claims
