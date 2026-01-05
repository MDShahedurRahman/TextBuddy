import pytest
from textbuddy import stats, top_words, find_count, replace_word, tokenize


def test_tokenize_basic():
    text = "Hello, hello! It's 2026."
    assert tokenize(text) == ["hello", "hello", "it's", "2026"]
