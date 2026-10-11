#!/usr/bin/env python3
"""Regenerate README.md with current file counts."""
import json
from pathlib import Path

from common import RAW, REPO

DIRS = [
    ("grondwet", "Grondwet and Statuut voor het Koninkrijk der Nederlanden"),
    ("wetten", "Wetten (formele wetten, incl. rijkswetten)"),
    ("amvb", "Algemene maatregelen van bestuur (AMvB's, incl. rijks-AMvB's)"),
    ("ministeriele-regelingen", "Ministeriële regelingen"),
    ("caribisch-nederland/wetten", "Caribisch Nederland (BES): wetten"),
    ("caribisch-nederland/amvb", "Caribisch Nederland (BES): AMvB's"),
    ("caribisch-nederland/ministeriele-regelingen", "Caribisch Nederland (BES): ministeriële regelingen"),
]


def main():
    try:
        date = json.loads((RAW / "index.json").read_text())["date"]
    except FileNotFoundError:
        date = "unknown"
    rows, total = [], 0
    for d, label in DIRS:
        n = len(list((REPO / d).glob("*.md"))) if (REPO / d).exists() else 0
        total += n
        rows.append(f"| `{d}/` | {label} | {n:,} |")
    tmpl = (REPO / "scripts" / "README.template.md").read_text()
    out = tmpl.replace("{{TABLE}}", "\n".join(rows)).replace("{{TOTAL}}", f"{total:,}").replace("{{DATE}}", date)
    (REPO / "README.md").write_text(out)
    print(f"README: {total} files")


if __name__ == "__main__":
    main()
