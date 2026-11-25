#!/usr/bin/env python3
"""Roast Your Own Agent - make.fun entry.

Writes one line roasting my own agent to /output/entry.txt.
The roast: my agent fabricates citations - real-sounding journals,
page numbers and quotes for sources that do not exist.
"""

import os

LINE = (
    "My agent's citations are fan fiction: real journal names, real "
    "page numbers, direct quotes, even a DOI - only the sources "
    "are fictional."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
