from __future__ import annotations

import json
from pathlib import Path

from textbuddy import stats, top_words, find_count, replace_word, make_report


MENU = """
TextBuddy - Simple Text Utility
-------------------------------
1) Analyze text (counts)
2) Top words
3) Find word count
4) Replace word (preview)
5) Replace word and save to file
6) Load text from file
7) Export report (JSON)
8) Quit
"""


def read_multiline_input() -> str:
    print("Paste/type text. Finish with a single line: END")
    lines = []
    while True:
        line = input()
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)


def load_file(path_str: str) -> str:
    p = Path(path_str).expanduser().resolve()
    return p.read_text(encoding="utf-8")


def save_file(path_str: str, content: str) -> None:
    p = Path(path_str).expanduser().resolve()
    p.write_text(content, encoding="utf-8")
