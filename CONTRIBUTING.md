# Add or repair a case

The catalogue is an index of source versions, not a claim that all published cases have been collected. Keep the original books intact.

1. Find an identifiable publisher, school, consulting club or official firm source. Record its title, edition, URL, access date and format in `catalogue/books.json`. A search snippet or an aggregator's edition label is discovery evidence only.
2. Check the whole case. Confirm the prompt, boundaries, clarifications, exhibits, solution and closing discussion. Use **physical PDF pages starting at 1**, not the slide numbers printed on the page. For PowerPoint, use slide positions. An unpaginated document needs a heading locator.
3. Add a record to `catalogue/cases.json`. Include source ID, exact title, range, prompt/solution/exhibit locations, evidence and limitations. Use `needs_review` until the mapping is supported. `source_mapped` establishes navigation to source answer material; it is not a claim that every calculation and exhibit is correct.
4. Compare title and content against existing versions. A matching title does not prove the same case; different filenames or years do not prove different cases. Preserve variants and record evidence before consolidating anything.
5. For a web case, link the publisher's prompt and answers. Label any original interviewer adaptation as an adaptation. Do not invent missing facts or present generated answers as the author's solution.
6. Add full source files only when you have a basis to redistribute them. Public availability alone is not redistribution permission. Otherwise add a publisher link and navigation metadata. Do not bypass a login, subscription or club membership restriction.
7. Run `python3 tools/build_catalogue.py`, then `python3 tools/build_catalogue.py --check`. Inspect the generated companion and source pages yourself. Test the local catalogue search. Keep scraped page captures and personal practice logs out of commits.

For a fully prepared peer session, copy [the packet template](resources/CASE-PACKET-TEMPLATE.md) privately and complete its release map and independent math check. Report source errors with the exact edition and physical page so a classmate can reproduce the issue.
