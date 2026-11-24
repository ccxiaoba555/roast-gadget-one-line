#!/usr/bin/env python3
"""One-Line Roast: the gadget you use every day.

Roasts the smartwatch: it spends eight hours watching you sit, then
buzzes to congratulate you for standing up -- eight hours of
surveillance, one second of applause, from a gadget that charges you
for the privilege of being watched.
"""

import os

ROAST = (
    "My smartwatch watched me sit for eight hours, then buzzed to "
    "congratulate me for standing up -- a $300 babysitter that applauds "
    "the bare minimum."
)

OUTPUT_PATH = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")


def validate(text: str) -> str:
    """Enforce the gate: one line, 1-200 chars of UTF-8, not blank."""
    text = text.strip()
    if not text:
        raise ValueError("roast must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"roast is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("roast must be a single line")
    text.encode("utf-8")  # must be valid UTF-8 text
    return text


def main() -> None:
    text = validate(ROAST)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
