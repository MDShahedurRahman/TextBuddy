from __future__ import annotations

import re
from dataclasses import dataclass
from collections import Counter
from typing import List, Tuple, Dict


_WORD_RE = re.compile(r"[A-Za-z0-9']+")


@dataclass(frozen=True)
class TextStats:
    characters: int
    characters_no_spaces: int
    words: int
    lines: int
    unique_words: int


def normalize_word(word: str) -> str:
    return word.lower().strip()


def tokenize(text: str) -> List[str]:
    # Extract words like: don't, it's, 2026, etc.
    return [normalize_word(w) for w in _WORD_RE.findall(text)]


def stats(text: str) -> TextStats:
    chars = len(text)
    chars_no_spaces = len("".join(text.split()))
    lines = 0 if text == "" else text.count("\n") + 1

    words_list = tokenize(text)
    words = len(words_list)
    unique_words = len(set(words_list))

    return TextStats(
        characters=chars,
        characters_no_spaces=chars_no_spaces,
        words=words,
        lines=lines,
        unique_words=unique_words,
    )


def top_words(text: str, n: int = 10) -> List[Tuple[str, int]]:
    if n <= 0:
        raise ValueError("n must be > 0")

    words_list = tokenize(text)
    counts = Counter(words_list)
    return counts.most_common(n)


def find_count(text: str, needle: str) -> int:
    needle_norm = normalize_word(needle)
    if not needle_norm:
        return 0
    return sum(1 for w in tokenize(text) if w == needle_norm)
