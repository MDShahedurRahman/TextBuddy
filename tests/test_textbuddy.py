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
