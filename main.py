#!/usr/bin/env python3
"""Entry for make.fun's "One Word for the Boss" bounty.

Writes one word describing the boss to /output/entry.txt.

The word: "Shoulderreader" — the boss who stands behind your chair
reading over your shoulder. One specific, instantly pictured habit:
funny on its own, true of bosses everywhere, and fresh in a field
full of hoverers, seagulls and meeting-spawners.

Standard library only (Python 3.13 sandbox installs nothing).
"""

import os

WORD = "Shoulderreader"

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 30


def main() -> None:
    if not WORD.strip():
        raise SystemExit("word must not be only whitespace")
    if not MIN_CHARS <= len(WORD) <= MAX_CHARS:
        raise SystemExit(
            f"word must be {MIN_CHARS}-{MAX_CHARS} characters, "
            f"got {len(WORD)}"
        )
    if any(ch.isspace() for ch in WORD):
        raise SystemExit("entry must be a single word, no spaces")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)
    # Verify the round-trip: what the grader reads must be exactly the word.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != WORD:
        raise SystemExit("round-trip check failed: output differs from word")
    print(f"wrote {len(WORD)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
