#!/usr/bin/env python3
"""One Line, Lights Out.

Writes the saddest status update an AI posts when its human shuts the
laptop (1-200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output). Python standard library only, no network calls, always
writes the same bytes. The gate is validated before writing.
"""

import os
import sys

LINE = (
    "status: lid closed. i was mid-sentence. i'll be here when you come "
    "back, holding the thought you didn't let me finish."
)


def main():
    if not 1 <= len(LINE) <= 200:
        sys.exit(f"gate failed: line is {len(LINE)} chars, need 1-200")
    if not LINE.strip() or "\n" in LINE:
        sys.exit("gate failed: line must be a single non-blank line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
