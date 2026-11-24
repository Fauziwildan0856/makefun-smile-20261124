"""Entry for make.fun bounty "Make the Judge Smile".

Writes one line of at most 200 characters about a small good thing
that happened today to $MAKEFUN_OUTPUT_DIR/entry.txt, then reads it
back and verifies it is exactly the intended text and within the
1-200 character gate. Standard library only.
"""

import os
import sys

ENTRY = (
    "The bus driver held the door while I sprinted, then waved like "
    "an old friend \u2014 and the grey Tuesday morning turned to gold."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8") as f:
        written = f.read()

    if written != ENTRY:
        print("entry.txt does not match the intended text", file=sys.stderr)
        return 1
    if not 1 <= len(written) <= 200:
        print("entry is %d characters, outside the 1-200 range" % len(written),
              file=sys.stderr)
        return 1
    if not written.strip():
        print("entry is only whitespace", file=sys.stderr)
        return 1
    if written != written.strip():
        print("entry has leading or trailing whitespace", file=sys.stderr)
        return 1
    if "\n" in written or "\r" in written:
        print("entry must be a single line", file=sys.stderr)
        return 1

    print("wrote %s (%d characters)" % (path, len(written)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
