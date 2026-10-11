"""Shared helpers for the LawCodex NL scripts."""
import os
import time
from pathlib import Path

import requests

UA = "LawCodex/1.0 (+https://github.com/LawCodex)"
REPO = Path(__file__).resolve().parent.parent
RAW = Path(os.environ.get("LAWCODEX_RAW", REPO.parent / "_raw" / "nl"))
SRU = "https://zoekservice.overheid.nl/sru/Search"

# BWB regeling types collected, mapped to (output dir, front-matter type)
TYPES = {
    "wet": ("wetten", "act"),
    "rijkswet": ("wetten", "act"),
    "AMvB": ("amvb", "decree"),
    "rijksAMvB": ("amvb", "decree"),
    "ministeriele-regeling": ("ministeriele-regelingen", "regulation"),
    "wet-BES": ("caribisch-nederland/wetten", "act"),
    "AMvB-BES": ("caribisch-nederland/amvb", "decree"),
    "ministeriele-regeling-BES": ("caribisch-nederland/ministeriele-regelingen", "regulation"),
}

# Constitutional texts go to grondwet/
CONSTITUTION = {
    "BWBR0001840": "grondwet",  # Grondwet
    "BWBR0002154": "grondwet",  # Statuut voor het Koninkrijk der Nederlanden
}

_session = None


def session():
    global _session
    if _session is None:
        _session = requests.Session()
        _session.headers["User-Agent"] = UA
    return _session


def get(url, params=None, tries=6, timeout=120):
    delay = 2
    for i in range(tries):
        try:
            r = session().get(url, params=params, timeout=timeout)
            if r.status_code == 200:
                return r
            if r.status_code == 404:
                r.raise_for_status()
            if r.status_code not in (429, 500, 502, 503, 504):
                r.raise_for_status()
        except requests.HTTPError:
            if i == tries - 1 or (r is not None and r.status_code == 404):
                raise
        except requests.RequestException:
            if i == tries - 1:
                raise
        time.sleep(delay)
        delay = min(delay * 2, 60)
    raise RuntimeError(f"failed: {url}")
