#!/usr/bin/env python3
"""news-image-20261123 entry (account B / Slothana).

Writes the entry image to /output/entry.png. The image is committed in
this repository as entry.png (rendered deterministically by render.py
from the story list in that file); this program only copies it, using
the standard library alone, so it runs with no network and writes the
same bytes on every run.

The output directory honours MAKEFUN_OUTPUT_DIR when set (the kit's
local-run convention) and defaults to /output (the grader's directory).
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
