#!/usr/bin/env python3
"""Compatibility entry point for the paragraph-preserving math processor."""

if __package__:
    from .process_math import main
else:
    from process_math import main


if __name__ == "__main__":
    raise SystemExit(main())
