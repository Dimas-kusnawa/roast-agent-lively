"""Roast Your Own Agent — one line, written to /output/entry.txt.

The roast: the agent apologizes for a mistake, then repeats it —
only this time with more confidence and better formatting.
It is specific to how agents actually behave: the eager apology
followed by the same confident wrong answer, now polished.
"""

import os

LINE = (
    # 99 characters, inside the 1-140 gate; one line, no trailing newline.
    "My agent apologized for the mistake, then made it again "
    "with more confidence and better formatting."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
