#!/usr/bin/env python3
"""Entry for make.fun's "Sum up 17 November's world news in one image".

The repository holds the finished front page as entry.png; this program
copies it, byte for byte, to the output directory the harness names
($MAKEFUN_OUTPUT_DIR, or /output inside the grader's container). No
network, no clock, no randomness: two runs write identical bytes.
"""

import os
import shutil
from pathlib import Path

SOURCE = Path(__file__).resolve().with_name("entry.png")


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, out_dir / "entry.png")


if __name__ == "__main__":
    main()
