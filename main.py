#!/usr/bin/env python3
"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.
Standard library only, no network, deterministic.
"""

import os

JOKE = (
    "My dad tried to fix the Wi-Fi at home with a ladder. "
    "He said the signal needed a little more... up-load."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
