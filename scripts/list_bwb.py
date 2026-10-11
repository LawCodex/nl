#!/usr/bin/env python3
"""List all BWB regelingen valid on a given date via the KOOP SRU service.

Writes RAW/index.json: one entry per BWB-ID with the toestand (consolidated
version) in force on that date.

Usage: python scripts/list_bwb.py [YYYY-MM-DD]
"""
import datetime
import json
import sys
import time

from lxml import etree

from common import RAW, SRU, TYPES, get

NS = {
    "srw": "http://www.loc.gov/zing/srw/",
    "dcterms": "http://purl.org/dc/terms/",
    "overheid": "http://standaarden.overheid.nl/owms/terms/",
    "overheidbwb": "http://standaarden.overheid.nl/bwb/terms/",
}
PAGE = 1000


def txt(el, path):
    r = el.find(path, NS)
    return r.text.strip() if r is not None and r.text else None


def main():
    date = sys.argv[1] if len(sys.argv) > 1 else datetime.date.today().isoformat()
    RAW.mkdir(parents=True, exist_ok=True)
    out = {}
    for t in TYPES:
        start = 1
        while True:
            q = f"dcterms.type=={t} and overheidbwb.geldigheidsdatum={date}"
            r = get(SRU, params={
                "x-connection": "BWB", "operation": "searchRetrieve", "version": "1.2",
                "query": q, "maximumRecords": PAGE, "startRecord": start,
            })
            root = etree.fromstring(r.content)
            total = int(root.findtext("srw:numberOfRecords", namespaces=NS))
            recs = root.findall(".//srw:record", NS)
            for rec in recs:
                meta = rec.find(".//overheidbwb:meta", NS)
                bwb = txt(meta, ".//dcterms:identifier")
                e = {
                    "id": bwb,
                    "title": txt(meta, ".//dcterms:title"),
                    "type": txt(meta, ".//dcterms:type"),
                    "authority": txt(meta, ".//overheid:authority"),
                    "valid_from": txt(meta, ".//overheidbwb:geldigheidsperiode_startdatum"),
                    "valid_to": txt(meta, ".//overheidbwb:geldigheidsperiode_einddatum"),
                    "toestand": txt(meta, ".//overheidbwb:toestand"),
                    "rechtsgebied": [x.text for x in meta.findall(".//overheidbwb:rechtsgebied", NS)],
                    "xml": txt(rec, ".//overheidbwb:locatie_toestand"),
                }
                prev = out.get(bwb)
                # keep the most recent version if several are listed
                if prev is None or (e["valid_from"] or "") > (prev["valid_from"] or ""):
                    out[bwb] = e
            print(f"{t}: {start + len(recs) - 1}/{total}", file=sys.stderr)
            start += len(recs)
            if not recs or start > total:
                break
            time.sleep(1)
    (RAW / "index.json").write_text(json.dumps({"date": date, "items": out}, ensure_ascii=False, indent=1))
    print(f"{len(out)} regelingen", file=sys.stderr)


if __name__ == "__main__":
    main()
