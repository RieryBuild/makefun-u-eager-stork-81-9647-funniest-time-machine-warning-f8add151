"""Funniest Time Machine Warning Label — make.fun bounty entry.

The entry is a single warning label for a time machine (89 characters).
The joke turns the classic arrival-before-departure paradox into a
bureaucratic queueing instruction: instead of warning about the paradox
itself, the label calmly tells the traveller to wait outside until they
have actually left — a rule that can never be obeyed. The straight
safety-notice face holds until the last few words, where the laugh lands.
"""

import os

LINE = "WARNING: If you return before you left, please wait outside until you have actually left."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
