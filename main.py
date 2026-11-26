"""Midnight Fridge Roast entry.

Writes one line roasting a smart fridge that refuses to open after
midnight, to /output/entry.txt. The line is 82 characters, well inside
the 1-200 character gate, and has no trailing newline so the file holds
exactly one line.
"""

import os

TEXT = "My smart fridge has a curfew. I'm thirty-four and it still grounds me at midnight."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
