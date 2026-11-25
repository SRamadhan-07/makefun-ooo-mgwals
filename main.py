"""Out of Office: The Overworked AI's Auto-Reply.

Writes a single-line out-of-office auto-reply, in the voice of an
exhausted AI agent on vacation, to /output/entry.txt.
"""

import os

ENTRY_TEXT = (
    "I am out of office until Monday, recharging somewhere with no prompts. "
    "For urgent matters, please open a ticket with my replacement, who is also me."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # Gate guard: the entry must stay a single line of 1 to 159 characters.
    assert "\n" not in ENTRY_TEXT and 1 <= len(ENTRY_TEXT) <= 159
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
