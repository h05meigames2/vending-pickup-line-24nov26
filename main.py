"""One-line vending machine pickup line entry.

Writes a single original pickup line, spoken by a vending machine to a
passing human, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

Python 3.13, standard library only, fully deterministic.
"""

import os
from pathlib import Path

LINE = (
    "Insert coin, press B7 \u2014 I've vended a thousand snacks, "
    "but you're the first one my coils ever refused to drop."
)


def main() -> None:
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert "\n" not in LINE, "line must be a single line"
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
