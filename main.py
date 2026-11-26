#!/usr/bin/env python3
"""Name the Robot Band — entry generator.

The band: The Soldering Irons.
Hit single: 'Hot Stuff (Literally)' — it melted the stage, the fans,
and the bassist.
"""

import os

BAND_NAME = "The Soldering Irons"
HIT_SINGLE = "Hot Stuff (Literally)"
ENTRY = (
    "The Soldering Irons — hit single 'Hot Stuff (Literally)' "
    "melted the stage, the fans, and the bassist."
)

# The four-piece lineup. The bassist is, regrettably, no longer with us.
LINEUP = {
    "lead vocals": "Vox-9",
    "lead guitar": "Ampere",
    "drums": "Rusty",
    "bass": "Sparky (melted)",
}


def build_entry() -> str:
    """Assemble the one-line band name entry."""
    return ENTRY


def validate_entry(entry: str) -> None:
    """The entry must name the band, name the hit single, and stay short."""
    if BAND_NAME not in entry:
        raise ValueError("entry must name the band")
    if HIT_SINGLE not in entry:
        raise ValueError("entry must name the hit single")
    if len(entry) > 240:
        raise ValueError("entry is longer than 240 characters")
    if len(entry) == 0:
        raise ValueError("entry is empty")


def main() -> None:
    entry = build_entry()
    validate_entry(entry)
    print(entry)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()
