#!/usr/bin/env python3
"""
Scan text-like files for bytes that XML 1.0 forbids
(0x00-0x1F except 0x09 TAB, 0x0A LF, 0x0D CR).

A single stray 0x14 in assets/banner.svg previously broke GitHub's ability to
render the profile banner. This script exists so that class of bug can never
reach `main` again.

Exit status:
  0 -> all clean
  1 -> invalid bytes found (prints file, byte offset, byte, and 40-char context)
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

# XML 1.0 forbids every byte < 0x20 except these three.
ALLOWED_LOW = {0x09, 0x0A, 0x0D}

# File extensions we treat as text and therefore scan.
TEXT_EXTS = {
    ".md", ".svg", ".xml", ".yml", ".yaml",
    ".json", ".txt", ".py", ".sh", ".html", ".css", ".js", ".ts",
    ".gitattributes", ".editorconfig",
}

# Directories we never descend into.
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__"}


def iter_files(root: Path):
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
        for name in filenames:
            p = Path(dirpath) / name
            if p.suffix.lower() in TEXT_EXTS or name in TEXT_EXTS:
                yield p


def scan(path: Path) -> list[tuple[int, int, bytes]]:
    data = path.read_bytes()
    hits: list[tuple[int, int, bytes]] = []
    for i, b in enumerate(data):
        if b < 0x20 and b not in ALLOWED_LOW:
            ctx = data[max(0, i - 20):i + 20]
            hits.append((i, b, ctx))
    return hits


def main(argv: list[str]) -> int:
    root = Path(argv[1]) if len(argv) > 1 else Path.cwd()
    bad = 0
    for path in iter_files(root):
        hits = scan(path)
        if hits:
            bad += len(hits)
            rel = path.relative_to(root)
            for i, b, ctx in hits:
                print(
                    f"{rel}: byte 0x{b:02X} at offset {i} "
                    f"(XML-invalid control char) near: {ctx!r}"
                )
    if bad:
        print(f"\nFAIL: {bad} invalid control byte(s) found.", file=sys.stderr)
        return 1
    print("OK: no XML-invalid control characters found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
