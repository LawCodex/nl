# Netherlands — LawCodex

The national legislation of the Kingdom of the Netherlands **in force on {{DATE}}**, as plain
Markdown: one file per regeling, current consolidated text (*geconsolideerde tekst*) taken from
the official **Basiswettenbestand (BWB)** that also powers [wetten.overheid.nl](https://wetten.overheid.nl).

Part of [LawCodex](https://github.com/LawCodex) — the laws of every country as Markdown in git.

## Contents

| Directory | Contents | Files |
|---|---|---:|
{{TABLE}}
| | **Total** | **{{TOTAL}}** |

Each file is named `<BWB-ID>-<slug-of-title>.md`, e.g.
{{LINK:BWBR0001840}}. The BWB-ID is the
stable official identifier (`BWBR…`); the same text is at `https://wetten.overheid.nl/<BWB-ID>`.

Key codes, for orientation:

| Regeling | File |
|---|---|
| Grondwet | {{LINK:BWBR0001840}} |
| Statuut voor het Koninkrijk | {{LINK:BWBR0002154}} |
| Burgerlijk Wetboek | Boek 1 {{SHORT:BWBR0002656}}, 2 {{SHORT:BWBR0003045}}, 3 {{SHORT:BWBR0005291}}, 4 {{SHORT:BWBR0002761}}, 5 {{SHORT:BWBR0005288}}, 6 {{SHORT:BWBR0005289}}, 7 {{SHORT:BWBR0005290}}, 7A {{SHORT:BWBR0006000}}, 8 {{SHORT:BWBR0005034}}, 10 {{SHORT:BWBR0030068}} |
| Wetboek van Strafrecht | {{LINK:BWBR0001854}} |
| Wetboek van Strafvordering | {{LINK:BWBR0001903}} |
| Wetboek van Burgerlijke Rechtsvordering | {{LINK:BWBR0001827}} |
| Wetboek van Koophandel | {{LINK:BWBR0001838}} |
| Algemene wet bestuursrecht | {{LINK:BWBR0005537}} |

## File format

YAML front matter followed by the text:

```yaml
title: "Grondwet"                 # citeertitel (or opschrift when there is none)
identifier: "BWBR0001840"         # BWB-ID
type: constitution                # constitution | act | decree | regulation
bwb_type: "wet"                   # original BWB soort: wet, rijkswet, AMvB, rijksAMvB, ministeriele-regeling, *-BES
jurisdiction: nl
language: nl
date: 1840-09-04                  # date of signature (ondertekening) of the original act
last_amended: 2023-02-22          # start of validity of the consolidated version used
status: in_force
source: "https://wetten.overheid.nl/BWBR0001840/2023-02-22"
source_xml: "https://repository.officiele-overheidspublicaties.nl/bwb/…/BWBR0001840_2023-02-22_0.xml"
authority: "…"                    # responsible ministry
rechtsgebied: [...]               # BWB subject classification
retrieved: 2026-10-11
```

- H1 is the title; the full *opschrift* (intitulé) follows in italics.
- The preamble (*aanhef*: "Wij Willem-Alexander…", considerans) and the closing formula /
  signatures (*wetsluiting*) are kept.
- The internal hierarchy (Boek, Deel, Titel, Hoofdstuk, Afdeling, Paragraaf, Artikel, Bijlage …)
  becomes nested headings (`##` … `######`); deeper levels fall back to **bold** labels.
- Leden are rendered as `1. …` paragraphs, opsommingen as nested bullet lists keeping their
  official labels (`a.`, `1°`, …).
- Tables become Markdown tables when simple, otherwise HTML tables (with row/column spans).
- Images (formulas, maps, forms) are linked to the official repository, not copied.
- Repealed articles that the consolidation still lists are kept with their editorial note
  (e.g. `[Vervallen per 01-01-2013]`), exactly as on wetten.overheid.nl.
- Footnotes become Markdown footnotes.

## What is not covered

- **Treaties** (*verdragen*, ~3,600 in the BWB) — they live in the separate Treaty database
  structure and are mostly not Dutch legislation proper.
- Other BWB categories, skipped as secondary/administrative or mass-volume: *koninklijke
  besluiten* (KB, rijks-KB), *zelfstandige bestuursorganen* rules (zbo), *publiekrechtelijke
  bedrijfsorganisatie* (pbo), *beleidsregels*, *circulaires*, *reglementen*, and the ~1,100
  *archiefselectielijsten* (ministerial archive selection lists).
- Decentralised regulations (provinces, municipalities, water boards — CVDR) and the
  legislation of Aruba, Curaçao and Sint Maarten (separate countries within the Kingdom).
- Historical versions: only the version in force on the retrieval date is kept; git history will
  record later changes when the corpus is refreshed. Future versions already published but not
  yet in force are not included.
- Explanatory memoranda (*memorie van toelichting*), except where the BWB text itself includes a
  *toelichting* (some ministerial regulations do).

## Sources

- List of regelingen: KOOP SRU search service, connection `BWB`
  (`https://zoekservice.overheid.nl/sru/Search?x-connection=BWB`), queried per type with
  `overheidbwb.geldigheidsdatum=<date>` to obtain exactly the version in force on that date.
- Texts: BWB toestand XML (schema `toestand_2016-1`) from
  `https://repository.officiele-overheidspublicaties.nl/bwb/<BWB-ID>/<date>_<n>/xml/…`.
- Both are official open-data services of the Dutch government, maintained by KOOP
  (Kennis- en Exploitatiecentrum Officiële Overheidspublicaties).

## Licence / copyright

Under Article 11 of the Dutch Auteurswet (Copyright Act) there is no copyright in laws, decrees
and ordinances issued by public authorities. The BWB data is made available by the Dutch
government as open data, free of restrictions on reuse (see
[wetten.overheid.nl — Hergebruik](https://wetten.overheid.nl/) and the KOOP open data
documentation). The Markdown conversion in this repository is likewise free to reuse.

This is **not** an official publication: only the publications in the Staatsblad and
Staatscourant are authentic. Conversion errors are possible — always check the source link.

## Regenerating

```sh
pip install -r scripts/requirements.txt
cd scripts
python list_bwb.py 2026-10-11   # SRU → ../_raw/nl/index.json (one entry per BWB-ID)
python fetch.py                 # toestand XML → ../_raw/nl/xml/ (cached, ≤4 parallel requests)
python convert.py               # XML → Markdown into the repo directories
python build_readme.py          # refresh the counts above
```

Raw data goes to `../_raw/nl/` (override with `LAWCODEX_RAW`), never into this repository.
When refreshing, delete the output directories first so that regelingen that ceased to be in
force (or were renamed) disappear.

Retrieved: {{DATE}}.
