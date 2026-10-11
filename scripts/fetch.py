#!/usr/bin/env python3
"""Download the toestand XML of every regeling in RAW/index.json (cached).

Usage: python scripts/fetch.py [--workers 4]
"""
import argparse
import json
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed

from common import RAW, get


def fetch(item):
    url = item["xml"]
    dest = RAW / "xml" / url.rsplit("/", 1)[-1]
    if dest.exists() and dest.stat().st_size > 0:
        return None
    r = get(url)
    tmp = dest.with_suffix(".part")
    tmp.write_bytes(r.content)
    tmp.rename(dest)
    return dest.name


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--workers", type=int, default=4)
    a = ap.parse_args()
    items = list(json.loads((RAW / "index.json").read_text())["items"].values())
    (RAW / "xml").mkdir(parents=True, exist_ok=True)
    done = errs = 0
    with ThreadPoolExecutor(max_workers=min(a.workers, 4)) as ex:
        futs = {ex.submit(fetch, it): it for it in items}
        for f in as_completed(futs):
            done += 1
            try:
                f.result()
            except Exception as e:  # noqa: BLE001
                errs += 1
                print(f"ERROR {futs[f]['id']}: {e}", file=sys.stderr)
            if done % 500 == 0:
                print(f"{done}/{len(items)} ({errs} errors)", file=sys.stderr)
    print(f"done {done}, errors {errs}", file=sys.stderr)


if __name__ == "__main__":
    main()
