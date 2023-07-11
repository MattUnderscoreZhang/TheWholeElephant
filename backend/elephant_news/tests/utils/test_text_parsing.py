import pytest
from elephant_news.utils.text_parsing import remove_newlines, break_into_list, batch_strings_into_max_encoding_length_batches


@pytest.fixture
def text() -> str:
    return '''["The NAACP issued a travel advisory for Florida due to Governor Ron DeSantis\' attempts to erase Black history and restrict diversity, equity, and inclusion programs in Florida schools.","The travel advisory warns that Florida is openly hostile towards African Americans, people of color, and LGBTQ+ individuals.","The League of United Latin American Citizens (LULAC) also issued a travel advisory for Florida after DeSantis signed a new immigration law.","DeSantis has banned the teaching of critical race theory in Florida schools and supported legislation barring instruction that suggests anyone is privileged or oppressed based on their race or skin color.","The NAACP distributed 10,000 books to predominantly Black communities across Florida after DeSantis\' administration rejected an Advanced Placement course on African American studies.","The NAACP decried Florida\'s new concealed weapon law, which allows gun owners to carry a concealed weapon without a permit or training.","The NAACP urged members to consider holding conventions outside of Florida due to DeSantis\' harmful policies.","The NAACP previously issued a travel advisory for Missouri in 2017 after the state passed a law making it more difficult for employees to prove discrimination."]'''


def test_remove_newlines():
    text = "This is a test.\nThis is another test."
    assert remove_newlines(text) == "This is a test.This is another test."


def test_break_into_list(text: str):
    my_list = break_into_list(text)
    assert len(my_list) == 8
    assert my_list[0] == "The NAACP issued a travel advisory for Florida due to Governor Ron DeSantis' attempts to erase Black history and restrict diversity, equity, and inclusion programs in Florida schools."
    assert my_list[1] == "The travel advisory warns that Florida is openly hostile towards African Americans, people of color, and LGBTQ+ individuals."
    assert my_list[2] == "The League of United Latin American Citizens (LULAC) also issued a travel advisory for Florida after DeSantis signed a new immigration law."
    assert my_list[3] == "DeSantis has banned the teaching of critical race theory in Florida schools and supported legislation barring instruction that suggests anyone is privileged or oppressed based on their race or skin color."
    assert my_list[4] == "The NAACP distributed 10,000 books to predominantly Black communities across Florida after DeSantis\' administration rejected an Advanced Placement course on African American studies."
    assert my_list[5] == "The NAACP decried Florida\'s new concealed weapon law, which allows gun owners to carry a concealed weapon without a permit or training."
    assert my_list[6] == "The NAACP urged members to consider holding conventions outside of Florida due to DeSantis\' harmful policies."
    assert my_list[7] == "The NAACP previously issued a travel advisory for Missouri in 2017 after the state passed a law making it more difficult for employees to prove discrimination."


def test_batch_strings_into_max_encoding_length_batches():
    for strings, max_encoding_length, expected_batches in [
        (["a", "b", "c", "d"], 2, [["a", "b"], ["c", "d"]]),
        (["a", "bc", "de", "f"], 3, [["a", "bc"], ["de", "f"]]),
        (["a", "bc", "de", "f"], 4, [["a", "bc"], ["de", "f"]]),
        (["a", "bc", "de", "f"], 5, [["a", "bc", "de"], ["f"]]),
        (["a", "bc", "def", "g"], 2, [["a"], ["bc"], ["g"]]),
    ]:
        string_encoding_lengths = [len(string) for string in strings]
        batches = batch_strings_into_max_encoding_length_batches(strings, string_encoding_lengths, max_encoding_length)
        assert batches == expected_batches
