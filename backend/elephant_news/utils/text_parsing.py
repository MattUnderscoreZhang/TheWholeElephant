def remove_newlines(text: str) -> str:
    return text.replace("\n", "")


def break_into_list(list_text: str) -> list[str]:
    first_bracket = list_text.find("[")
    last_bracket = list_text.rfind("]")
    list_text = list_text[first_bracket + 2: last_bracket - 1]

    split_claims = list_text.split("\",\"")
    return split_claims


def batch_strings_into_max_encoding_length_batches(strings: list[str], string_encoding_lengths: list[int], max_encoding_length: int) -> list[list[str]]:
    batches = []
    current_batch = []
    current_batch_length = 0
    skipped_indices = []
    for i, length in enumerate(string_encoding_lengths):
        if length > max_encoding_length:
            # TODO: handle this case
            # raise ValueError(f"String too long to be processed: {length} > {max_comment_batch_encoding_length}")
            skipped_indices.append(i)
            continue
        if length + current_batch_length > max_encoding_length:
            batches.append(current_batch)
            current_batch = [strings[i]]
            current_batch_length = length
        else:
            current_batch.append(strings[i])
            current_batch_length += length
    if current_batch:
        batches.append(current_batch)
    return batches
