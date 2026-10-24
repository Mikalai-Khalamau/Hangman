from src.non_interactive import compare_words

def test_non_interactive_exact_match():
    result = compare_words("окно", "окно")
    assert result == "окно;POS"

def test_non_interactive_partial_match():
    result = compare_words("волокно", "толокно")
    assert result == "*олокно;NEG"

def test_non_interactive_no_match():
    result = compare_words("привет", "яблоко")
    assert result == "******;NEG"

def test_non_interactive_one_letter_match():
    result = compare_words("футбол", "форсаж")
    assert result == "ф*****;NEG"
