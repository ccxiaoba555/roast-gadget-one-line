#!/usr/bin/env python3
"""One-Line Roast: the gadget you use every day.

Roasts the smartwatch. First draft applauded the bare minimum; the
tighter cut keeps the contrast that does the work -- eight hours of
surveillance, one second of applause -- and drops the price tag, which
was a second joke competing with the first. One gadget, one absurdity,
one line.
"""

import os

ROAST = (
    "My smartwatch watched me sit for eight hours, then buzzed to "
    "congratulate me for standing up -- eight hours of surveillance, "
    "one second of applause."
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
    # Read it back: the file must hold exactly the roast, one line.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("entry.txt does not hold exactly the roast")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
