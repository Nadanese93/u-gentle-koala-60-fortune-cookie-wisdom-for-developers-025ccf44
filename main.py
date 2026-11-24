#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).

Deterministic, no network, no reads outside this file. The output file is
written as UTF-8 with mode 0644; the output directory itself is never
chmodded, moved or removed.
"""

import os
import sys

ENTRY = "Your lucky numbers are the line numbers of the bug you have not found yet."
MAX_CHARS = 120


def validate(text):
    """Reject anything the gate would refuse: empty, whitespace-only,
    over 120 characters, or containing a newline / carriage return.
    Also reject leading/trailing whitespace (wasted bytes on the
    size tie-break) and any control character, which would garble
    the line for the judge."""
    if not text or not text.strip():
        raise ValueError("entry is empty or whitespace-only")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d characters, over the 120 limit" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry has leading or trailing whitespace")
    if any(ord(ch) < 0x20 or ord(ch) == 0x7F for ch in text):
        raise ValueError("entry contains a control character")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = validate(ENTRY)
    data = text.encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
