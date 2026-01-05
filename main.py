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


def run():
    text = ""

    while True:
        print(MENU)
        choice = input("Choose (1-8): ").strip()

        if choice == "8":
            print("Bye!")
            break

        if choice == "6":
            try:
                path = input("Enter text file path: ").strip()
                text = load_file(path)
                print(f"Loaded {len(text)} characters.\n")
            except Exception as e:
                print(f"Error loading file: {e}\n")
            continue

        # For other options, ensure we have text
        if choice in {"1", "2", "3", "4", "5", "7"} and not text:
            print("No text loaded. Choose one:")
            print("A) Paste text now")
            print("B) Load from file (option 6)")
            pick = input("Pick A/B: ").strip().upper()
            if pick == "A":
                text = read_multiline_input()
                print("\nText loaded.\n")
            else:
                print("Use option 6 to load from file.\n")
                continue

        if choice == "1":
            s = stats(text)
            print(f"Lines: {s.lines}")
            print(f"Words: {s.words}")
            print(f"Unique words: {s.unique_words}")
            print(f"Characters: {s.characters}")
            print(f"Characters (no spaces): {s.characters_no_spaces}\n")

        elif choice == "2":
            try:
                n = int(input("Top how many words? (default 10): ").strip() or "10")
                for w, c in top_words(text, n):
                    print(f"{w}: {c}")
                print()
            except ValueError:
                print("Invalid number.\n")

        elif choice == "3":
            needle = input("Word to find: ").strip()
            count = find_count(text, needle)
            print(f"Occurrences of '{needle}': {count}\n")

        elif choice == "4":
            old = input("Replace word: ").strip()
            new = input("With: ").strip()
            preview, count = replace_word(text, old, new)
            print(f"Replacements: {count}")
            print("----- Preview (first 500 chars) -----")
            print(preview[:500])
            print()

        elif choice == "5":
            old = input("Replace word: ").strip()
            new = input("With: ").strip()
            out_path = input("Save to file path: ").strip()
            updated, count = replace_word(text, old, new)
            save_file(out_path, updated)
            print(f"Saved. Replacements: {count}\n")

        elif choice == "7":
            try:
                n = int(
                    input("Top N words in report? (default 10): ").strip() or "10")
                out_path = input("Save report JSON path: ").strip()
                report = make_report(text, top_n=n)
                save_file(out_path, json.dumps(report, indent=2))
                print(f"Report saved to {out_path}\n")
            except ValueError:
                print("Invalid number.\n")
            except Exception as e:
                print(f"Error saving report: {e}\n")

        else:
            print("Invalid option.\n")


if __name__ == "__main__":
    run()
