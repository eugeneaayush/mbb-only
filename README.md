# Case-trade library

A practical library for giving and receiving consulting cases with a partner. **This collection is broad, but it is not exhaustive, and not every original case has a verified interviewer packet yet.** The audit is dated **15 November 2026**. Open issues are visible rather than silently treated as complete.

## Start here

1. **[Browse by school/source](catalogue/README.md)** on GitHub. Choose a case and open its interviewer companion.
2. For fast title/source search, download or clone this repository and open **[catalogue/index.html](catalogue/index.html)** in a browser. GitHub displays the HTML source rather than running the search page. The page runs locally without installing anything or uploading your data.
3. Open the original case at the companion's page reference. Read the full source, recalculate the math and prepare the candidate exhibits. **Full books contain answers.**
4. Use **[Run a case](resources/RUN-A-CASE.md)**, the **[pre-case checklist](resources/PRE-CASE-CHECKLIST.md)** and **[scorecard](resources/SCORECARD.md)**. Keep completed logs and classmates' feedback private.

## What is here

| Material | Current scope |
|---|---|
| Original library | All **144 original files** preserved: 140 PDFs, 2 PowerPoint files, 2 Word documents |
| Source catalogue | **158 sources**, including the original library and publisher-linked additions |
| Mapped navigation entries | **1561** case/version and short-question records with source answer-material mappings or official web-case adaptations |
| Review queue | **2429** additional extraction records requiring identity, boundary or solution review; not a count of verified cases |
| New publisher-linked material | 22 Notre Dame cases, 10 Penn cases, 268 FMS interview recollection/version records across five editions and 7 official McKinsey/Bain guided cases; **307 case/version records**, with readiness stated individually |
| Additional practice | [120 market-sizing drill/version entries](resources/DRILLS.md), session/error log templates, a scorecard and a blank packet-authoring template |

An **interviewer companion** is an original navigation layer over the actual source material: prompt locations, available solution locations, exhibit references, limitations and giving instructions. It is not a fabricated answer key. Existing books often already contain interviewer instructions and solutions; the companion helps you find them. New books are linked at their publisher rather than mirrored here.

`source_mapped` means the case title/range and source answer-material cues have been mapped. It does **not** certify every calculation or exhibit. `publisher_web_case` is an original peer-practice adaptation of an official guided sample. `needs_review` is a discovery/review entry and **must not be used as a ready-to-give packet**. The local search defaults to mapped entries.

The same case can recur across editions, schools or publisher pages. Counts above describe records and versions, not unique cases. Some older sources contain short practice questions; their companions identify that format. Ask your partner about prior exposure.

## Useful files

- [Coverage, known gaps and evidence](COVERAGE.md)
- [Source-by-source directory comparison](catalogue/source-coverage.json)
- [Text-duplicate candidates](catalogue/text-duplicate-candidates.json) — original files retained
- [Blank session log](resources/SESSION-LOG.csv) and [error log](resources/ERROR-LOG.csv) — copy privately
- [Case packet template](resources/CASE-PACKET-TEMPLATE.md) — complete and validate it before use
- [Contributing and repair process](CONTRIBUTING.md)

The generated catalogue and companions are built from `catalogue/books.json` and `catalogue/cases.json`. Edit metadata there, then run `python3 tools/build_catalogue.py` and `python3 tools/build_catalogue.py --check`. No external Python packages are needed. Existing casebook files and coaching instructions are preserved.
