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
