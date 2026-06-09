#!/usr/bin/env python3
"""Compute MAME-style CRC32 and SHA1 hashes for ROM dump files.

This helper is intentionally limited to hashes used by MAME ROM definitions:
CRC32 and SHA1 per dumped ROM file.

Example:
    python tools/hash_mame_roms.py dumps/
    python tools/hash_mame_roms.py dumps/*.bin

The script does not combine files and does not compare against copyrighted ROM
content. It only reports hashes for files already dumped locally.
"""

from __future__ import annotations

import argparse
import hashlib
import sys
import zlib
from pathlib import Path
from typing import Iterable


EXPECTED_SIZE = 0x2000


def iter_input_files(paths: Iterable[str]) -> list[Path]:
    files: list[Path] = []

    for raw_path in paths:
        path = Path(raw_path)
        if path.is_dir():
            files.extend(sorted(p for p in path.iterdir() if p.is_file()))
        elif path.is_file():
            files.append(path)
        else:
            print(f"warning: skipping missing path: {path}", file=sys.stderr)

    return sorted(files)


def hash_file(path: Path) -> tuple[int, str, str]:
    data = path.read_bytes()
    crc32 = zlib.crc32(data) & 0xFFFFFFFF
    sha1 = hashlib.sha1(data).hexdigest()
    size_note = ""
    if len(data) != EXPECTED_SIZE:
        size_note = f"  # expected {EXPECTED_SIZE} bytes for VS. SMB EPROMs"

    return len(data), f"{crc32:08x}", sha1 + size_note


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Compute MAME-style CRC32 and SHA1 hashes per ROM dump file."
    )
    parser.add_argument(
        "paths",
        nargs="+",
        help="ROM dump file(s) or directory/directories containing dump files.",
    )
    args = parser.parse_args()

    files = iter_input_files(args.paths)
    if not files:
        print("error: no files to hash", file=sys.stderr)
        return 1

    for path in files:
        size, crc32, sha1 = hash_file(path)
        print(f"{path.name:28} {size:5d} CRC({crc32}) SHA1({sha1})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
