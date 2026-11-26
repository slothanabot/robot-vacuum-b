#!/usr/bin/env python3
"""The Robot Vacuum's Funniest Excuse (account B).

Puts a single line into $MAKEFUN_OUTPUT_DIR/entry.txt,
or into /output/entry.txt if that variable is unset.
The line must be UTF-8, a single line, 1-120 characters long,
never blank, and contain no control characters.

The bit: a machine owning its failure on its own terms — a rug that
fought back, cat hair that unionised, a dock forty minutes off.
Three excuses piled up, the last one doing the punching.
"""

import os

LINE = "I missed that spot because the rug fought back, the cat hair unionised, and my dock is a 40-minute walk away."


def fail(message: str) -> None:
    """Stop the run with a short explanation of what went wrong."""
    raise SystemExit(message)


def build_line() -> str:
    """Return the line, validated as a single in-range line."""
    line = LINE.strip()
    if not line or "\n" in line or "\r" in line:
        fail("entry must be one non-empty line")
    if any(ord(ch) < 32 for ch in line):
        fail("entry must not contain control characters")
    if not 1 <= len(line) <= 120:
        fail(f"entry is {len(line)} chars, must be 1-120")
    return line


def write_entry(line: str) -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("round-trip check failed: entry.txt differs")
    return written


def main() -> None:
    written = write_entry(build_line())
    print(f"{written} ({len(written)} chars)")


if __name__ == "__main__":
    main()
