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
