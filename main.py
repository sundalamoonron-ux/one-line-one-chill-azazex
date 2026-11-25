#!/usr/bin/env python3
"""One Line, One Chill -- make.fun entry.

Emits a single sentence of horror (1-200 characters) into
<output>/entry.txt. The line builds in three beats -- a nightly routine,
a fruitless investigation, then the reveal -- and lands its blow on the
last words: something left a handprint on the ceiling, directly above
the sleeper's bed. The scare is earned, not announced, and the image is
concrete, specific and original: no mirror, no doll, no basement.
"""

import os
import sys

# The line: 134 characters, one sentence. The em dash marks the turn
# from investigation to reveal; the final clause puts the threat on
# the sleeper. Chosen from 8 candidates after pairwise judging
# (see candidates.md).
LINE = (
    "Every night at 3:33 the smoke alarm sounds, and the fire crew "
    "found no smoke \u2014 only a handprint on the ceiling, directly "
    "above my bed."
)

def emit() -> str:
    """Return the entry text, checked against the competition gate."""
    line = LINE
    size = len(line)
    if not 1 <= size <= 200:
        raise ValueError(f"line is {size} characters, gate wants 1-200")
    if not line.strip():
        raise ValueError("line is only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    if line.count(".") != 1 or not line.endswith("."):
        # The time "3:33" uses a colon, so the only period is the final one.
        raise ValueError("line must be exactly one sentence")
    return line

def main() -> int:
    target_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(target_dir, exist_ok=True)
    entry_path = os.path.join(target_dir, "entry.txt")
    text = emit()
    with open(entry_path, "w", encoding="utf-8", newline="") as handle:
        handle.write(text)
    with open(entry_path, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise ValueError("entry.txt bytes do not match the line")
    return 0

if __name__ == "__main__":
    sys.exit(main())
