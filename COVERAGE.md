# Coverage audit — 15 November 2026

## Finding

**The repository is not exhaustive.** There is no finite, authoritative public list of every consulting practice case, and new, private, member-only and paid cases continue to exist. This audit checks a documented public source universe; it cannot establish universal completeness or that every indexed case is ready to give.

All 144 original casebook files are preserved. The source catalogue now contains 158 records. It contains 1561 mapped case/version navigation entries and 2429 review candidates. Review candidates may still contain duplicate titles, subsections, missing cases or inaccurate boundaries; they are excluded from the default local search. Even mapped entries need a source read and a math/exhibit check before a live trade.

## Search and comparison method

Firecrawl was used to search and retrieve public casebook directories, original school resources and official firm preparation pages. The initial 144-file inventory was compared with every school/edition listing extracted from [StrategyCase](https://strategycase.com/free-mba-casebooks/) and [MasterTheCase](https://www.masterthecase.com/case-interview-casebooks-top-mba). The result is **135 directory entries** (some overlap): 97 filename/edition matches, 19 missing listed editions, 5 uncertain near-year matches, 5 source-reported access restrictions, 3 entries whose access is unverified, and 6 publicly linked primary-source entries. These are initial-inventory comparison statuses, before this update's linked additions; they are not distinct-case counts.

See [the full comparison](catalogue/source-coverage.json). A directory label is not proof that a local file is byte-identical to that edition. Search-result snippets were used for discovery, not as evidence of a complete case or an answer key. Firecrawl's ability to retrieve a page is not evidence of redistribution rights.

## Publisher-linked additions

| Source | Addition | Important qualification |
|---|---|---|
| [Notre Dame Consulting Connect](https://consultingconnect.nd.edu/assets/658111/university_of_notre_dame_case_book.pdf) | 22 cases; physical case ranges mapped in the 340-page book | Some contents labels/links differ from actual case pages. Sports Bar lacks a sample final recommendation. Penn & Teller includes exhibits explicitly not to be shown to the candidate. |
| [Penn Career Services](https://cdn.uconnectlabs.com/wp-content/uploads/sites/74/2019/09/Penn-Case-Book-with-Practice-Cases.pdf) | 10 cases in a 194-page preparation guide | Distinguishes interviewer and interviewee pages; share only inspected candidate material. |
| [FMS Delhi consulting club archive](https://sites.google.com/fms.edu/conclubfms/casebook/casebook-archive) | 268 case/version records and 120 drill/version entries across the 2020–21, 2021–22, 2023–24, 2024–25 and 2025–26 books | Student interview recollections and model approaches, not firm-authenticated interviewer packets. The cover identifies 2025–26 despite stale embedded PDF metadata. |
| [McKinsey sample cases](https://www.mckinsey.com/careers/interviewing) | Beautify, Diconsa, Electro-Light, National Education, Talbot Trucks | Public guided samples with original interviewer adaptation notes; answers are on the publisher's page. |
| [Bain case preparation](https://www.bain.com/careers/hiring-process/case-interview/) | Coffee Shop Co. and FashionCo. | Some worked material is image-based. Revenue improvement is not automatically profit improvement. |

The [BCG preparation page](https://careers.bcg.com/global/en/case-interview-preparation) was also checked. No case PDF link was found on that page; this is not a claim that BCG has no public cases elsewhere. [Soreno's directory](https://soreno.ai/articles/consulting-casebooks) helped locate original school sources.

## Known acquisition gaps

- The directories list newer **Darden 2025–26, NYU Stern 2025–26, Columbia 2025 and Fuqua 2025–26** editions. Their full source/permission/access status is not resolved in this update; they are not claimed as added. The public [Fuqua documents page](https://fuquaconnect.duke.edu/organization/the-duke-mba-consulting-club/documents) did not expose a casebook download in the retrieved view. Columbia Graduate Consulting Club's public resource page is a different club and does not verify the MBA edition.
- Nineteen historical listings lack a local filename match: Booth 2007/2009/2010/2012; Columbia 2017; Fuqua 2015/2017/2022; Stern 2017/2021; Darden 2015/2021; UCLA 2010/2016; INSEAD 2007/2020; ESADE 2018; IIM Calcutta 2022; IIM Lucknow 2022. A missing edition may reuse cases already held.
- Five near-year matches need edition verification: HBS 2012, Darden 2009 and 2013, Tuck 2000, McGill 2014.
- All five consulting editions visibly linked on FMS's public archive were retrieved and indexed as separate versions. Cases and drills repeat across editions; these totals are not unique-problem counts. Other Indian-school editions remain acquisition leads.
- Member-only, paid, inaccessible, unindexed and newly published material is outside any completeness claim. No login or payment restriction was bypassed.

## Indexing limits

All original PDFs were inventoried and text-extracted; office documents were extracted separately. Image/font-encoded MIT Sloan, Duke Fuqua and Michigan Ross books required OCR; an older FMS edition also required OCR. Untitled Stern practice questions use explicitly editorial navigation labels. Contents tables, case headings and answer-material cues supported the page mappings, with targeted manual repairs and independent spot checks. Extraction is not a full semantic review of more than 20,000 pages. The review queue is explicit; no generic generated answer is substituted for a missing source solution.

Original sources without a case-level index in this release:

- Dartmouth Tuck Casebook-2006.pdf — this 22-page file ends in framework guidance; the cases advertised in its contents are absent.

Page numbers mean physical PDF positions starting at 1; slides use slide positions. They can differ from printed page labels. Browser/GitHub PDF viewers may ignore page fragments; download the source and enter the stated page manually. Word files have no stable extracted pagination.

## Duplicate and quality findings

Ten pairs have identical normalized extracted text. [Their hashes and filenames](catalogue/text-duplicate-candidates.json) are recorded; images, layouts, metadata and pagination may still differ. Nothing was deleted or relabelled as the same edition based only on page counts. Matching case titles are also only duplicate candidates.

Some source tables of contents disagree with actual case titles or page boundaries. Corrected navigation follows the case pages. An older Notre Dame Coffee Shop case contains inconsistent arithmetic; its companion flags the issue. The seven official firm-case notes contain targeted arithmetic checks, but there has been no blanket mathematical verification of the library.

## Material and privacy boundaries

This update adds original navigation/teaching resources and short metadata, plus links to new publisher sources. It does not rehost the newly discovered books or reproduce their full solutions. The existing collection's files are unchanged. A future source upload needs a basis for redistribution. Keep classmates' names, scores, recordings and feedback outside this public repository; the log files supplied here are blank templates.
