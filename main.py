#!/usr/bin/env python3
"""Write the entry's single-line advice joke to the harness output path."""
from pathlib import Path
import os

ADVICE = "For a faster morning, put your keys in the cereal box tonight; breakfast will be the only thing you can find on time."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ADVICE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
