#!/usr/bin/env python3
"""One Word for Your Wi-Fi — make.fun entry.

Writes a single word describing the entrant's home Wi-Fi to
/output/entry.txt. Deterministic: the same word on every run.

The word is "liar": the Wi-Fi icon shows full bars and the router
blinks happily, yet no page ever loads. The signal promises the
internet and delivers nothing. The network is not slow, it is
lying to your face.
"""

import os

WORD = "liar"
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate self-check: UTF-8 text, 1-20 characters, not only whitespace.
    if not (1 <= len(WORD) <= 20) or not WORD.strip():
        raise ValueError("entry word fails the gate: %r" % WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
