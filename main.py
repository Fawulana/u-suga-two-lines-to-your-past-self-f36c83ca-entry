# SPDX-License-Identifier: MIT
"""Two Lines to Your Past Self.

Writes exactly two lines to /output/entry.txt (or $OUTPUT_PATH):
a warning to the writer's past self about one specific moment, and
one sentence on why that moment mattered.

Deterministic: the same fixed text on every run, no input, no
network, no randomness, stdlib only.
"""

import os

TEXT = (
    "When your brother calls from the payphone at the bus station "
    "at 11 p.m. on a Tuesday, pick up \u2014 it's the last time he'll "
    "ask for help.\n"
    "You let it ring, still angry about the money, and that "
    "unanswered call is why you answer every unknown number now, "
    "just in case it's him.\n"
)


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
