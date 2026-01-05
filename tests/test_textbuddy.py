import pytest
from textbuddy import stats, top_words, find_count, replace_word, tokenize


def test_tokenize_basic():
    text = "Hello, hello! It's 2026."
    assert tokenize(text) == ["hello", "hello", "it's", "2026"]


def test_stats_counts():
    text = "Hi\nThere"
    s = stats(text)
    assert s.lines == 2
    assert s.words == 2
    assert s.unique_words == 2


def test_top_words():
    text = "a a a b b c"
    tops = top_words(text, 2)
    assert tops[0] == ("a", 3)
    assert tops[1] == ("b", 2)


def test_top_words_invalid_n():
    with pytest.raises(ValueError):
        top_words("x", 0)


def test_find_count_case_insensitive():
    text = "Cat cat CAT dog"
    assert find_count(text, "cat") == 3
    assert find_count(text, "dog") == 1


def test_replace_word_whole_word_only():
    text = "cat category Cat."
    updated, count = replace_word(text, "cat", "pet")
    # "category" should not change
    assert updated == "pet category pet."
    assert count == 2
