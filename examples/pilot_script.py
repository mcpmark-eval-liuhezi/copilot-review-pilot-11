#!/usr/bin/env python3
"""Example script for the GitHub Copilot code review pilot.

This small script computes the SHA-256 checksum of a given string and
prints a short usage report. It is intentionally simple so that an
automated Copilot code review has a clear, low-risk diff to comment on.
"""

import hashlib


def sha256_of(text: str) -> str:
    """Return the hex SHA-256 digest of *text* (UTF-8 encoded)."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def main() -> None:
    sample = "pilot-change branch demo"
    digest = sha256_of(sample)
    print(f"input   : {sample}")
    print(f"sha256  : {digest}")
    print("status  : ok")


if __name__ == "__main__":
    main()
