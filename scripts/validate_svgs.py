#!/usr/bin/env python3
"""
Parse every SVG passed on argv with an XML parser. Exit non-zero if any fail.

Used by .github/workflows/validate.yml to guarantee that the profile banner /
snake SVGs are well-formed XML before they can land on main.
"""
from __future__ import annotations

import sys
import xml.etree.ElementTree as ET


def main(argv: list[str]) -> int:
    paths = argv[1:]
    if not paths:
        print("no SVG paths supplied; nothing to validate")
        return 0

    failures = 0
    for p in paths:
        try:
            ET.parse(p)
            print(f"OK   {p}")
        except ET.ParseError as e:
            failures += 1
            print(f"FAIL {p}: {e}", file=sys.stderr)
        except FileNotFoundError:
            failures += 1
            print(f"FAIL {p}: file not found", file=sys.stderr)

    if failures:
        print(f"\n{failures} SVG(s) failed to parse.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
