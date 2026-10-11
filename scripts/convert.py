#!/usr/bin/env python3
"""Convert downloaded BWB toestand XML (RAW/xml) to Markdown in the repo.

Usage: python scripts/convert.py [--only BWBR...] [--retrieved YYYY-MM-DD]
"""
import argparse
import datetime
import json
import re
import sys
import unicodedata
from pathlib import Path

from lxml import etree

from common import CONSTITUTION, RAW, REPO, TYPES

YEAR_SPLIT = {"wetten", "amvb", "ministeriele-regelingen"}

SKIP = {
    "meta-data", "bwb-inputbestand", "bwb-wijzigingen", "redactionele-correcties", "jcis",
    "brondata", "officiele-inhoudsopgave", "colspec", "spanspec", "kop", "lidnr", "li.nr",
    "citeertitel", "intitule",
}
INLINE = {
    "nadruk", "intref", "extref", "redactie", "sup", "inf", "noot", "nootref", "tekstcorrectie",
    "naam", "voornaam", "achternaam", "functie", "datum", "plaats", "dossierref", "label", "nr",
    "titel", "subtitel", "br", "omissie", "unl", "ovl", "afk",
}
PARA = {
    "al", "considerans.al", "noot.al", "slotformulering", "afkondiging", "wij", "tussenkop",
    "al-groep", "aanhef.al", "bijschrift", "koning", "dagtekening", "structuurtekst",
}
TEXTISH = PARA | {"ondertekening"}


def clean(s):
    return re.sub(r"\s+", " ", s or "")


MD_SPECIAL = re.compile(r"([\\`*_<>\[\]])")


def esc(s):
    return MD_SPECIAL.sub(r"\\\1", s)


def esc_start(line):
    """Escape characters that would start a block construct at line start."""
    if re.match(r"^\s*(#|>|[-+=]\s|[-+=]$|\d+[.)](\s|$)|\|)", line):
        m = re.match(r"^(\s*)(\d+)([.)])(.*)$", line, re.S)
        if m:
            return f"{m.group(1)}{m.group(2)}\\{m.group(3)}{m.group(4)}"
        s = line.lstrip()
        return line[: len(line) - len(s)] + "\\" + s
    return line


class Doc:
    def __init__(self, bwb, toestand_dir_url):
        self.bwb = bwb
        self.img_base = toestand_dir_url
        self.notes = []

    # ---- inline -------------------------------------------------------
    def inline(self, el, top=True):
        out = [esc(clean(el.text))] if top else []
        if not top:
            out.append(self.inline_el(el))
            out.append(esc(clean(el.tail)))
            return "".join(out)
        for c in el:
            if not isinstance(c.tag, str):
                out.append(esc(clean(c.tail)))
                continue
            out.append(self.inline(c, top=False))
        return "".join(out)

    def inner(self, el):
        parts = [esc(clean(el.text))]
        for c in el:
            if isinstance(c.tag, str):
                parts.append(self.inline(c, top=False))
            else:
                parts.append(esc(clean(c.tail)))
        return "".join(parts)

    def inline_el(self, el):
        t = el.tag
        if t in ("meta-data", "jcis"):
            return ""
        if t == "nadruk":
            s = self.inner(el)
            if not s.strip():
                return s
            typ = el.get("type", "")
            lead = s[: len(s) - len(s.lstrip())]
            trail = s[len(s.rstrip()):]
            core = s.strip()
            if typ in ("vet", "halfvet"):
                return f"{lead}**{core}**{trail}"
            if typ == "cur":
                return f"{lead}*{core}*{trail}"
            if typ == "ondlijn":
                return f"{lead}<u>{core}</u>{trail}"
            return s
        if t == "sup":
            return f"<sup>{self.inner(el)}</sup>"
        if t == "inf":
            return f"<sub>{self.inner(el)}</sub>"
        if t == "br":
            return "<br>"
        if t == "noot":
            nr = clean(el.findtext("noot.nr") or str(len(self.notes) + 1)).strip()
            body = " ".join(
                b.strip() for a in el if isinstance(a.tag, str) and a.tag != "noot.nr"
                for b in (self.para(a) if a.tag == "noot.al" else self.block(a, 0)))
            body = re.sub(r"\s*\n\s*", " ", body)
            label = f"n{len(self.notes) + 1}"
            self.notes.append((label, nr, body))
            return f"[^{label}]"
        if t in ("noot.nr", "noot.al"):
            return ""
        if t == "illustratie":
            return self.image(el)
        if t in ("lijst", "table", "tgroup"):
            # block-level element in an inline context: flatten
            return " " + " ".join(b.strip() for b in self.blocks(el)) + " "
        return self.inner(el)

    def image(self, el):
        naam = el.get("naam", "")
        alt = el.get("alt") or "Afbeelding"
        return f"![{esc(alt)}]({self.img_base}{naam})"

    # ---- blocks -------------------------------------------------------
    def para(self, el, prefix=""):
        s = (prefix + self.inline(el)).strip()
        return [esc_start(s)] if s else []

    def kop_text(self, kop):
        parts = []
        head = " ".join(x for x in (clean("".join(k.itertext())).strip()
                                     for k in kop if k.tag in ("label", "nr")) if x)
        tit = kop.find("titel")
        titel = self.inline(tit).strip() if tit is not None else ""
        sub = kop.find("subtitel")
        if sub is not None:
            st = self.inline(sub).strip()
            if st:
                titel = f"{titel} {st}".strip()
        if head and titel:
            parts.append(f"{esc(head)} — {titel}" if not head.endswith(".") else f"{esc(head)} {titel}")
        else:
            parts.append(esc(head) or titel)
        return parts[0]

    def blocks(self, el, depth=0):
        """Return list of Markdown blocks for the children of el."""
        out = []
        for c in el:
            if not isinstance(c.tag, str):
                continue
            out.extend(self.block(c, depth))
        return out

    def block(self, c, depth):
        t = c.tag
        if t in SKIP:
            return []
        kop = c.find("kop")
        if kop is not None and t not in ("li",):
            return self.section(c, kop, depth)
        if t in PARA:
            return self.para(c)
        if t == "lid":
            nr = clean(c.findtext("lidnr")).strip()
            bl = self.blocks(c, depth)
            lab = (f"{nr}\\." if re.fullmatch(r"\d+[a-z]*", nr) else esc(nr)) if nr else ""
            if lab and bl and not bl[0].startswith(("- ", "|", "<table", "![", "#", "**")):
                bl[0] = f"{lab} {bl[0]}"
            elif lab:
                bl.insert(0, lab)
            return bl
        if t == "lijst":
            return [self.lijst(c, 0)]
        if t == "table":
            return [self.table(c)]
        if t in ("definitielijst", "specificatielijst"):
            return [self.pairlist(c)]
        if t == "plaatje":
            res = []
            for x in c:
                if x.tag == "illustratie":
                    res.append(self.image(x))
                elif x.tag == "bijschrift":
                    res.extend(self.para(x))
                elif isinstance(x.tag, str):
                    res.extend(self.block(x, depth))
            return res
        if t == "illustratie":
            return [self.image(c)]
        if t == "ondertekening":
            parts = [esc(clean(c.text))]
            for x in c:
                if not isinstance(x.tag, str) or x.tag in SKIP:
                    if not isinstance(x.tag, str):
                        parts.append(esc(clean(x.tail)))
                    continue
                if x.tag == "naam":
                    if "".join(parts).strip():
                        parts.append("\x00")
                    nm = " ".join(self.inner(n).strip() for n in x if isinstance(n.tag, str))
                    parts.append(nm or self.inner(x).strip())
                    parts.append(esc(clean(x.tail)))
                else:
                    parts.append(self.inline(x, top=False))
            lines = [ln.strip() for ln in "".join(parts).split("\x00")]
            lines = [esc_start(ln) for ln in lines if ln]
            return ["\\\n".join(lines)] if lines else []
        # generic container: recurse; keep stray text
        res = []
        tx = clean(c.text).strip()
        if tx:
            res.append(esc_start(esc(tx)))
        has_el = False
        for x in c:
            if not isinstance(x.tag, str):
                continue
            has_el = True
            if x.tag in INLINE and x.tag not in ("noot",):
                s = self.inline(x, top=False).strip()
                if s:
                    res.append(esc_start(s))
            else:
                res.extend(self.block(x, depth))
                tl = clean(x.tail).strip()
                if tl:
                    res.append(esc_start(esc(tl)))
        return res

    def section(self, c, kop, depth):
        level = depth + 2
        title = self.kop_text(kop)
        out = []
        if title:
            if level <= 6:
                out.append("#" * level + " " + title)
            else:
                out.append(f"**{title}**")
        out.extend(self.blocks(c, depth + 1))
        return out

    def lijst(self, el, level):
        lines = []
        ind = "  " * level
        for li in el:
            if li.tag != "li":
                if isinstance(li.tag, str) and li.tag not in SKIP:
                    for b in self.block(li, 0):
                        lines.append(ind + b.replace("\n", "\n" + ind))
                continue
            nr = clean(li.findtext("li.nr")).strip()
            first = True
            item_lines = []
            for x in li:
                if not isinstance(x.tag, str) or x.tag in SKIP:
                    continue
                if x.tag == "lijst":
                    item_lines.append(("sub", self.lijst(x, level + 1)))
                else:
                    for b in self.block(x, 0):
                        item_lines.append(("txt", b))
            tx = clean(li.text).strip()
            if tx:
                item_lines.insert(0, ("txt", esc(tx)))
            if not item_lines:
                lines.append(f"{ind}- {esc(nr)}".rstrip())
                continue
            for kind, b in item_lines:
                if kind == "sub":
                    if first:
                        lines.append(f"{ind}- {esc(nr)}".rstrip())
                        first = False
                    lines.append(b)
                    continue
                b = b.lstrip("\\") if re.match(r"^\\[#>+=\-|]", b) else b
                body = re.sub(r"\n(?=.)", "\n" + ind + "  ", b)
                if first:
                    lines.append(f"{ind}- {esc(nr) + ' ' if nr else ''}{body}")
                    first = False
                else:
                    lines.append("")
                    lines.append(f"{ind}  {body}")
        return "\n".join(lines)

    def pairlist(self, el):
        """definitielijst (term/definitie) and specificatielijst (specificatie/waarde)."""
        lines = []
        for item in el:
            if not isinstance(item.tag, str) or item.tag in SKIP:
                continue
            parts = []
            for x in item:
                if not isinstance(x.tag, str) or x.tag in SKIP:
                    continue
                bl = self.block(x, 0) if len(x) and x.find("al") is not None else [self.inner(x).strip()]
                parts.extend(b for b in bl if b.strip())
            if not parts:
                continue
            first = parts[0].lstrip("\\") if re.match(r"^\\[#>+=\-|]", parts[0]) else parts[0]
            line = "- " + first
            if len(parts) > 1 and not parts[1].startswith(("- ", "|", "<table")):
                line += " " + parts[1]
                rest = parts[2:]
            else:
                rest = parts[1:]
            lines.append(line)
            for b in rest:
                lines.append("")
                lines.append("  " + re.sub(r"\n(?=.)", "\n  ", b))
        return "\n".join(lines)

    # ---- tables -------------------------------------------------------
    def table(self, tbl):
        out = []
        title = tbl.find("title")
        if title is not None and clean(title.text).strip():
            out.append(f"**{self.inline(title).strip()}**")
        for x in tbl:
            if x.tag == "tgroup":
                out.append(self.tgroup(x))
            elif isinstance(x.tag, str) and x.tag not in SKIP and x.tag != "title":
                out.extend(self.block(x, 0))
        return "\n\n".join(out)

    def cell(self, entry):
        bl = []
        for x in entry:
            if not isinstance(x.tag, str) or x.tag in SKIP:
                continue
            if x.tag in INLINE:
                bl.append(self.inline(x, top=False).strip())
            else:
                bl.extend(self.block(x, 0))
        tx = clean(entry.text).strip()
        if tx:
            bl.insert(0, esc(tx))
        return [b for b in bl if b.strip()]

    def tgroup(self, tg):
        rows = []
        complex_ = False
        for part in ("thead", "tbody", "tfoot"):
            for p in tg.findall(part):
                for row in p.findall("row"):
                    cells = []
                    for e in row.findall("entry"):
                        if (e.get("namest") or "") != (e.get("nameend") or "") or \
                                (e.get("morerows") or "0") != "0" or e.get("spanname"):
                            complex_ = True
                        bl = self.cell(e)
                        if len(bl) > 1 or any("\n" in b for b in bl):
                            complex_ = True
                        cells.append((e, bl))
                    rows.append((part, cells))
        ncols = int(tg.get("cols") or 0) or max((len(c) for _, c in rows), default=0)
        if any(len(c) != ncols for _, c in rows):
            complex_ = True
        if not rows:
            return ""
        if not complex_:
            def fmt(cells):
                return "| " + " | ".join((b[0] if b else "").replace("|", "\\|") for _, b in cells) + " |"
            md = []
            head = [r for r in rows if r[0] == "thead"]
            body = [r for r in rows if r[0] != "thead"]
            if head:
                md.append(fmt(head[0][1]))
                rest = head[1:] + body
            else:
                md.append("| " + " | ".join([" "] * ncols) + " |")
                rest = body
            md.append("| " + " | ".join(["---"] * ncols) + " |")
            for _, cells in rest:
                md.append(fmt(cells))
            return "\n".join(md)
        # HTML fallback
        names = [cs.get("colname") for cs in tg.findall("colspec")]
        spans = {sp.get("spanname"): (sp.get("namest"), sp.get("nameend")) for sp in tg.findall("spanspec")}

        def colspan(e):
            st, en = e.get("namest"), e.get("nameend")
            if e.get("spanname") in spans:
                st, en = spans[e.get("spanname")]
            if st and en and st in names and en in names:
                return names.index(en) - names.index(st) + 1
            return 1

        h = ["<table>"]
        for part, cells in rows:
            tag = "th" if part == "thead" else "td"
            cells_html = []
            for e, bl in cells:
                attrs = ""
                cs = colspan(e)
                if cs > 1:
                    attrs += f' colspan="{cs}"'
                if (e.get("morerows") or "0") != "0":
                    attrs += f' rowspan="{int(e.get("morerows")) + 1}"'
                content = "<br>".join(md_to_html(b).replace("\n", "<br>") for b in bl)
                cells_html.append(f"<{tag}{attrs}>{content}</{tag}>")
            h.append("<tr>" + "".join(cells_html) + "</tr>")
        h.append("</table>")
        return "\n".join(h)


HTML_KEEP = re.compile(r"(</?(?:sup|sub|u|br)>)")


def md_to_html(md):
    """Turn the small Markdown subset we emit into HTML (for HTML tables)."""
    out = []
    for part in HTML_KEEP.split(md):
        if HTML_KEEP.fullmatch(part):
            out.append(part)
            continue
        part = re.sub(r"!\[((?:\\.|[^\]])*)\]\(([^)]*)\)", lambda m: "\x00IMG" + m.group(2) + "\x01" + m.group(1) + "\x02", part)
        part = re.sub(r"\\(.)", lambda m: "\x03" + str(ord(m.group(1))) + "\x04", part)
        part = part.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        part = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", part)
        part = re.sub(r"\*(.+?)\*", r"<i>\1</i>", part)
        part = re.sub(r"\x03(\d+)\x04", lambda m: {"<": "&lt;", ">": "&gt;", "&": "&amp;"}.get(chr(int(m.group(1))), chr(int(m.group(1)))), part)
        part = re.sub(r"\x00IMG([^\x01]*)\x01([^\x02]*)\x02", lambda m: f'<img src="{m.group(1)}" alt="{m.group(2)}">', part)
        out.append(part)
    return "".join(out)


def slugify(s, maxlen=80):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rsplit("-", 1)[0]
    return s or "regeling"


def yq(s):
    return '"' + (s or "").replace("\\", "\\\\").replace('"', '\\"') + '"'


def convert(item, retrieved):
    url = item["xml"]
    src = RAW / "xml" / url.rsplit("/", 1)[-1]
    tree = etree.parse(str(src))
    root = tree.getroot()
    bwb = item["id"]
    doc = Doc(bwb, url.rsplit("/", 1)[0] + "/")
    wg = root.find("wetgeving") if root.tag == "toestand" else root
    if wg is None:
        wg = root
    title = clean(item["title"]).strip()
    intit = wg.find("intitule")
    intitule = doc.inline(intit).strip() if intit is not None else ""
    date = intit.get("ondertekening_bron") if intit is not None else None
    if not date and intit is not None:
        date = intit.get("inwerking")
    valid_from = root.get("inwerkingtreding") or item.get("valid_from")
    if bwb in CONSTITUTION:
        outdir, ftype = CONSTITUTION[bwb], "constitution"
    else:
        outdir, ftype = TYPES[item["type"]]
    fm = [
        "---",
        f"title: {yq(title)}",
        f"identifier: {yq(bwb)}",
        f"type: {ftype}",
        f"bwb_type: {yq(item['type'])}",
        "jurisdiction: nl",
        "language: nl",
    ]
    if date and re.fullmatch(r"\d{4}-\d{2}-\d{2}", date):
        fm.append(f"date: {date}")
    if valid_from:
        fm.append(f"last_amended: {valid_from}")
    fm += [
        "status: in_force",
        f"source: {yq(f'https://wetten.overheid.nl/{bwb}/{valid_from}' if valid_from else f'https://wetten.overheid.nl/{bwb}')}",
        f"source_xml: {yq(url)}",
    ]
    if item.get("authority"):
        fm.append(f"authority: {yq(item['authority'])}")
    if item.get("rechtsgebied"):
        fm.append("rechtsgebied: [" + ", ".join(yq(x) for x in item["rechtsgebied"]) + "]")
    fm += [f"retrieved: {retrieved}", "---", ""]
    body = [f"# {esc(title)}"]
    if intitule and intitule.rstrip(". ").lower() != title.rstrip(". ").lower():
        body.append(f"*{intitule}*")
    for c in wg:
        if not isinstance(c.tag, str) or c.tag in SKIP:
            continue
        body.extend(doc.block(c, 0))
    if doc.notes:
        for label, nr, text in doc.notes:
            body.append(f"[^{label}]: {esc(nr)} {text}".rstrip())
    text = "\n".join(fm) + "\n" + "\n\n".join(b for b in body if b.strip()) + "\n"
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"(?<=\S) {2,}", " ", text)
    fname = f"{bwb}-{slugify(title)}.md"
    if outdir in YEAR_SPLIT:
        # GitHub lists max 1,000 entries per directory: split by year of the original act
        yr = (date or "")[:4]
        if not (yr.isdigit() and yr > "1000"):
            yr = (intit.get("inwerking") or "")[:4] if intit is not None else ""
        outdir = f"{outdir}/{yr if yr.isdigit() else 'onbekend'}"
    dest = REPO / outdir / fname
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(text, encoding="utf-8")
    return dest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", nargs="*")
    ap.add_argument("--types", nargs="*", help="only these BWB types")
    ap.add_argument("--retrieved", default=datetime.date.today().isoformat())
    a = ap.parse_args()
    idx = json.loads((RAW / "index.json").read_text())
    items = idx["items"]
    ids = a.only or sorted(items)
    if a.types:
        ids = [k for k in ids if items[k]["type"] in a.types]
    missing = [k for k in ids if not (RAW / "xml" / items[k]["xml"].rsplit("/", 1)[-1]).exists()]
    if missing:
        print(f"skipping {len(missing)} not yet downloaded", file=sys.stderr)
        ids = [k for k in ids if k not in set(missing)]
    errs = 0
    for i, k in enumerate(ids, 1):
        try:
            convert(items[k], a.retrieved)
        except Exception as e:  # noqa: BLE001
            errs += 1
            print(f"ERROR {k}: {e!r}", file=sys.stderr)
        if i % 1000 == 0:
            print(f"{i}/{len(ids)} ({errs} errors)", file=sys.stderr)
    print(f"converted {len(ids) - errs}, errors {errs}", file=sys.stderr)


if __name__ == "__main__":
    main()
