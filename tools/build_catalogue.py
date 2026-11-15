#!/usr/bin/env python3
"""Build portable navigation and interviewer companions from reviewed metadata."""
import argparse
import hashlib
import json
import re
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]


def slug(text):
    return re.sub(r'[^a-z0-9]+', '-', text.lower()).strip('-')[:90]


def identity(case):
    value = f"{case['source_id']}|{case['title']}|{case.get('start_page')}"
    return slug(case['title']) + '-' + hashlib.sha256(value.encode()).hexdigest()[:10]


def pages_label(pages):
    if not pages:
        return 'Not separately identified'
    runs = []
    for page in sorted(set(pages)):
        if runs and page == runs[-1][-1] + 1:
            runs[-1].append(page)
        else:
            runs.append([page])
    return ', '.join(str(r[0]) if len(r) == 1 else f'{r[0]}–{r[-1]}' for r in runs)


def source_link(book, page=None, prefix='../'):
    url = book.get('url') or prefix + quote(book['file'])
    if page and book.get('format') == 'pdf':
        url += f'#page={page}'
    return url


def validate(books, cases):
    by_id = {b['id']: b for b in books}
    assert len(by_id) == len(books), 'Duplicate source IDs'
    seen = set()
    for book in books:
        assert re.fullmatch(r'[a-z0-9-]+', book['id']), 'Unsafe source ID'
        assert bool(book.get('file')) != bool(book.get('url')), 'One source target required'
        if book.get('file'):
            path = (ROOT / book['file']).resolve()
            assert path.is_relative_to(ROOT) and path.is_file(), f'Missing source: {book}'
        else:
            assert book['url'].startswith('https://'), 'Expected HTTPS publisher URL'
    for case in cases:
        assert case['source_id'] in by_id
        assert case['title'].strip() and '\n' not in case['title']
        cid = identity(case)
        assert cid not in seen, f'Duplicate case: {cid}'
        seen.add(cid)
        book = by_id[case['source_id']]
        lo, hi = case.get('start_page'), case.get('end_page')
        if lo is not None:
            assert isinstance(lo, int) and isinstance(hi, int) and 1 <= lo <= hi
            assert hi <= book['pages'], f'Page outside source: {case["title"]}'
        for field in ('prompt_pages', 'interviewer_pages', 'exhibit_pages'):
            for p in case.get(field, []):
                assert lo is not None and lo <= p <= hi, f'{field} out of range'
        assert case['review_status'] in ('source_mapped', 'needs_review', 'publisher_web_case')
        if case['review_status'] == 'source_mapped':
            assert case.get('interviewer_pages') or (case.get('locator', {}).get('heading') and case['locator'].get('solution_heading')), 'Mapped entry needs answer-material locations'


def md(text):
    return str(text).replace('|', '\\|').replace('\n', ' ')


def build():
    data = ROOT / 'catalogue'
    books = json.loads((data / 'books.json').read_text())
    cases = json.loads((data / 'cases.json').read_text())
    validate(books, cases)
    by_id = {b['id']: b for b in books}
    out = ROOT / 'interviewer'
    out.mkdir(exist_ok=True)
    groups = {b['id']: [] for b in books}
    for case in cases:
        groups[case['source_id']].append(case)
        cid = identity(case)
        book = by_id[case['source_id']]
        link = source_link(book, case.get('start_page'))
        page_range = f"{case.get('start_page')}–{case.get('end_page')}" if case.get('start_page') else 'Web sections / unpaginated source'
        body = f'''# {case['title']} — interviewer companion

**Source:** {book['title']}

**Case ID:** `{cid}`

**Review status:** `{case['review_status']}`

**Open the source:** [Publisher / existing source]({link})

This companion is an original navigation aid. Use the source for the actual prompt and available answer material. This file does not invent a replacement solution or claim an independently checked answer key. A `needs_review` entry is not ready to give; resolve its mapping and answer gaps first.

| Material | Physical PDF pages / slides |
|---|---|
| Complete case range | {page_range} |
| Prompt locations (may also contain answers) | {pages_label(case.get('prompt_pages', []))} |
| Interviewer / solution locations | {pages_label(case.get('interviewer_pages', []))} |
| Exhibit mentions (not certified candidate-safe pages) | {pages_label(case.get('exhibit_pages', []))} |

**Mapping evidence:** {case.get('evidence_note', 'See the source and catalogue review status.')}

**Limitations:** {case.get('limitations', 'Page navigation is not an arithmetic or visual exhibit audit. Confirm exact case boundaries and release instructions before a live session.')}

## Prepare and give this case

1. Open the complete source range. Locate the exact prompt, clarifications, exhibit triggers, worked calculations and closing discussion. If any required part is missing, repair it before the session or select another case.
2. Recalculate the quantitative steps. Record any discrepancy; distinguish the author’s inputs from any explicit assumption agreed with your partner.
3. Read only the prompt aloud. Share only visually inspected candidate exhibits, individually. Prompt and exhibit pages may contain solutions; never share the full book or this companion with a cold candidate.
4. Follow the source's question sequence or candidate-led release logic. Accept alternative sound structures; use the agreed hint policy.
5. Give specific feedback using the [scorecard](../resources/SCORECARD.md), then redo one weak step. Log the exact case ID privately.

See [Run a case](../resources/RUN-A-CASE.md), [source catalogue](../catalogue/README.md), and [coverage and limitations](../COVERAGE.md).
'''
        if case.get('locator'):
            body += '\n## Word-document locator\n\nFind the exact heading **' + case['locator']['heading'] + '** in the source document. '
            body += ('The answer material is under **' + case['locator']['solution_heading'] + '** within that case. ' if case['locator'].get('solution_heading') else 'No worked solution was located in this case block. ')
            body += 'Pagination depends on your Word viewer; no physical page numbers are asserted.\n'
        if case.get('interviewer_note'):
            body += '\n## Case-specific interviewer note\n\n' + case['interviewer_note'] + '\n'
        body = '\n'.join(line.rstrip() for line in body.splitlines()) + '\n'
        (out / (cid + '.md')).write_text(body)
    lines = ['# Case catalogue', '', 'Browse the [searchable local catalogue](index.html) after downloading the repository, or use the tables below on GitHub.', '',
             'Every entry links to an interviewer navigation companion and the original source. `source_mapped` means title/range mapping with solution cues; it does not mean a complete mathematical or visual audit. `needs_review` is a discovery entry, not a ready-to-give case. Titles repeated across editions are not automatically different cases. Full casebooks contain spoilers.', '',
             f'{len(books)} source records; {len(cases)} indexed case/version records. These are not a count of unique cases in the world.', '']
    browser_rows = []
    (data / 'books').mkdir(exist_ok=True)
    lines += ['| Source | Indexed records | Case list |', '|---|---:|---|']
    for book in books:
        rows = groups[book['id']]
        lines.append(f"| {md(book['title'])} | {len(rows)} | [Browse](books/{book['id']}.md) |")
        book_lines = [f"# {book['title']}", '', f"[Open source]({source_link(book, prefix='../../')}) · {book.get('coverage_note', 'Case-level completeness not certified.')}", '', 'Physical PDF page numbers start at 1. They may differ from printed slide numbers. Read the review status and limitations in each companion before use.', '', '| Case | Start page | Status | Interviewer companion |', '|---|---:|---|---|']
        for c in rows:
            cid = identity(c)
            location = c.get('start_page') or ('Heading' if c.get('locator') else 'Web')
            status_label = '**REVIEW REQUIRED — not ready**' if c['review_status'] == 'needs_review' else c['review_status']
            book_lines.append(f"| {md(c['title'])} | {location} | {status_label} | [Open](../../interviewer/{cid}.md) |")
            browser_rows.append({'title': c['title'], 'book': book['title'], 'status': c['review_status'], 'pages': location, 'guide': '../interviewer/' + cid + '.md', 'source': source_link(book, c.get('start_page'))})
        if not rows:
            book_lines.append('| Case-level index pending; open source for contents | — | needs_review | See source |')
        book_lines += ['', '[All sources](../README.md) · [Coverage and gaps](../../COVERAGE.md)', '']
        (data / 'books' / (book['id'] + '.md')).write_text('\n'.join(book_lines))
    (data / 'README.md').write_text('\n'.join(lines))
    payload = json.dumps(browser_rows, ensure_ascii=False).replace('<', '\\u003c')
    page = '''<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Case trade catalogue</title>
<style>body{font:17px system-ui,sans-serif;line-height:1.5;max-width:1150px;margin:32px auto;padding:0 20px;color:#172b3a;background:#f8fafb}h1{font-size:36px}input,select{font:inherit;padding:10px;border:1px solid #8194a3;border-radius:5px;margin:4px}input{width:min(560px,90%)}table{width:100%;border-collapse:collapse;background:white}th,td{text-align:left;padding:12px;border-bottom:1px solid #dde4e8}a{color:#045ea8}th{background:#e5eef4}small{display:block} .notice{padding:16px;background:#fff2d4;border-left:4px solid #c18d11} @media(max-width:700px){table{font-size:14px}td,th{padding:7px}}</style>
<h1>Case trade catalogue</h1><p>Choose a case to give. Open the interviewer companion, then read the complete linked source and verify the math before the session.</p>
<p class="notice">This is a dated, incomplete coverage audit. Page mappings are not a guarantee of a complete answer key. Full source books contain spoilers. Keep classmates' feedback in private copies of the logs.</p>
<p><a href="../resources/RUN-A-CASE.md">Run a case</a> · <a href="../resources/SCORECARD.md">Scorecard</a> · <a href="../COVERAGE.md">Coverage and gaps</a> · <a href="README.md">GitHub-friendly catalogue</a></p>
<label for="query">Search case or book</label><br><input id="query" type="search" placeholder="e.g. Wharton, Coffee"><label for="status">Status</label><select id="status"><option value="mapped">Mapped sources</option><option value="">All, including review queue</option><option>source_mapped</option><option>publisher_web_case</option><option>needs_review</option></select>
<p id="count" aria-live="polite"></p><table><thead><tr><th>Case / source</th><th>Start page</th><th>Status</th><th>Open</th></tr></thead><tbody id="rows"></tbody></table>
<script>const data=PAYLOAD;const query=document.querySelector('#query'),status=document.querySelector('#status'),rows=document.querySelector('#rows');
function render(){const q=query.value.toLocaleLowerCase();const found=data.filter(x=>(!status.value||(status.value==='mapped'?x.status!=='needs_review':x.status===status.value))&&(x.title+' '+x.book).toLocaleLowerCase().includes(q));rows.replaceChildren();for(const x of found){const tr=document.createElement('tr');const td=document.createElement('td');td.textContent=x.title;const small=document.createElement('small');small.textContent=x.book;td.append(small);tr.append(td);for(const value of [x.pages,x.status]){const t=document.createElement('td');t.textContent=value;tr.append(t)}const t=document.createElement('td');for(const [name,url]of [['Interviewer',x.guide],['Source',x.source]]){const a=document.createElement('a');a.textContent=name;a.href=url;t.append(a,document.createTextNode(' '))}tr.append(t);rows.append(tr)}document.querySelector('#count').textContent=found.length+' of '+data.length+' case/version records';}query.addEventListener('input',render);status.addEventListener('change',render);render();</script></html>'''.replace('PAYLOAD', payload)
    (data / 'index.html').write_text(page)
    return len(books), len(cases)


def self_test():
    assert slug('Penn & Teller') == 'penn-teller'
    assert pages_label([5, 2, 3, 3, 8, 9]) == '2–3, 5, 8–9'
    assert source_link({'file': 'Book A.pdf', 'format': 'pdf'}, 3) == '../Book%20A.pdf#page=3'
    c = {'source_id': 'x', 'title': 'Case', 'start_page': 1, 'end_page': 3, 'prompt_pages': [1], 'interviewer_pages': [2, 3], 'exhibit_pages': [], 'review_status': 'source_mapped'}
    b = [{'id': 'x', 'title': 'Test', 'url': 'https://example.com/book.pdf', 'format': 'pdf', 'pages': 3}]
    validate(b, [c])
    unpaged = dict(c, start_page=None, end_page=None, prompt_pages=[], interviewer_pages=[], locator={'heading':'Case No. 1 – Test','solution_heading':'Possible Solution'})
    validate(b, [unpaged])
    for bad in ([c, c], [dict(c, end_page=4)], [dict(c, prompt_pages=[0])], [dict(unpaged, locator={'heading':'No answer location'})]):
        try:
            validate(b, bad)
        except AssertionError:
            pass
        else:
            raise AssertionError('Invalid fixture accepted')
    for bad_book in (dict(b[0], id='../escape'), dict(b[0], url='javascript:alert(1)')):
        try:
            validate([bad_book], [])
        except AssertionError:
            pass
        else:
            raise AssertionError('Unsafe source fixture accepted')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    self_test()
    if args.check:
        books = json.loads((ROOT / 'catalogue/books.json').read_text())
        cases = json.loads((ROOT / 'catalogue/cases.json').read_text())
        validate(books, cases)
        expected = {identity(c) + '.md' for c in cases}
        actual = {p.name for p in (ROOT / 'interviewer').glob('*.md')}
        assert expected == actual, 'Missing or stale generated companions; rebuild and reconcile removed records'
        assert all((ROOT / 'catalogue/books' / (b['id'] + '.md')).is_file() for b in books)
        readme=(ROOT/'README.md').read_text()
        mapped=sum(c['review_status']!='needs_review' for c in cases)
        review=len(cases)-mapped
        for label, count in [('Source catalogue',len(books)),('Mapped navigation entries',mapped),('Review queue',review)]:
            assert re.search(r'\| '+re.escape(label)+r' \| \*\*'+str(count)+r'(?:\*\*|\s)',readme), 'README counts are stale: '+label
        for b in books:
            if b.get('file') and b.get('sha256'):
                assert hashlib.sha256((ROOT / b['file']).read_bytes()).hexdigest() == b['sha256'], 'Source file changed'
        print('Metadata, generated-file inventory, source hashes and negative-fixture checks passed')
    else:
        print('Built sources / case companions:', build())
