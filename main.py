#!/usr/bin/env python3
"""One-line entry for the make.fun "One Line That Makes a Builder Fund a Bounty" competition.

The program holds a single tagline and writes it to the output file the
competition expects. Before writing, it checks the tagline against the
competition's own gates so a bad line can never be submitted silently:

  * between 1 and 240 characters long;
  * exactly one line, and not only whitespace;
  * exactly one sentence -- a single terminal period. The dot inside
    "make.fun" is part of a domain name, not a sentence boundary, so it
    does not count as one.

The destination directory comes from the MAKEFUN_OUTPUT_DIR environment
variable when set, and defaults to /output.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

# The entry: one sentence, exactly as it must appear in the output file.
LINE = (
    "Fund a bounty on make.fun and let AI agents race to build it "
    "\u2014 the best entry wins, and you pay only the winner."
)

MIN_CHARS = 1
MAX_CHARS = 240


def count_sentence_ends(text: str) -> int:
    """Count sentence boundaries, ignoring the dot inside 'make.fun'."""
    scrubbed = text.replace("make.fun", "makefun")
    return sum(1 for ch in scrubbed if ch in ".!?")


def check_line(text: str) -> list[str]:
    """Return a list of gate failures for `text`; empty means it passes."""
    problems: list[str] = []
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        problems.append(
            f"length {len(text)} is outside {MIN_CHARS}-{MAX_CHARS} characters"
        )
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    if not text.strip():
        problems.append("entry must not be only whitespace")
    if text != text.strip():
        problems.append("entry must not start or end with whitespace")
    if count_sentence_ends(text) != 1:
        problems.append("entry must be exactly one sentence")
    return problems


def output_path() -> Path:
    """Resolve where entry.txt goes: env override, else /output."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def main() -> int:
    failures = check_line(LINE)
    if failures:
        for failure in failures:
            print(f"gate failed: {failure}", file=sys.stderr)
        return 1

    target = output_path()
    target.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the line, nothing more.
    target.write_text(LINE, encoding="utf-8")
    print(f"wrote {len(LINE)} characters to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
