#!/usr/bin/env python3
"""Deadpan Forecasts for Cities That Do Not Exist entry for make.fun.

Writes one original line - a deadpan weather forecast for the invented
city of Quillmarsh, where the rain falls upward - to entry.txt.
Deterministic, standard library only: the same bytes every run.
"""

import os

FORECAST = (
    "In Quillmarsh, expect 23 degrees with rain falling upward at "
    "14 kilometres an hour, so umbrellas are useless and hats are "
    "strongly discouraged."
)


def main() -> None:
    # The gate requires 1 to 160 characters, not only white space.
    assert 1 <= len(FORECAST) <= 160, "FORECAST must be 1-160 characters"
    assert FORECAST.strip(), "FORECAST must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(FORECAST)
    # Read back and verify the written bytes match exactly.
    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == FORECAST, "entry.txt bytes differ from FORECAST"


if __name__ == "__main__":
    main()
