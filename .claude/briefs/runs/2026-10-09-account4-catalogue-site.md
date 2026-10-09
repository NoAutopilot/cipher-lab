# CATALOGUE-SITE-1: a public catalogue of our readings, generated for GitHub Pages (account 4, Opus 5.5, cap USD 10, box 90 min)

Written 9 Oct 2026 22:1x UTC by date -u by the orchestrator (account-4), session_012sGNgiddCpz4QUhQsMyoPU, on the owner's direction at
22:0x UTC (3:0x pm PT): "take what we've solved that are only discoverable within GitHub and make it more accessible to those who are
interested in the topic", with dbourdeau.github.io/cyphersolver/catalogue.html as the shape he liked (its text is CC BY 4.0: cite, do not
copy; its layout: an index by outcome, one page per item, links a reader can verify from their desk).

What exists: `docs/index.html` is the internal board (tools/build_dashboard.py, 5 MB, worker names and costs: NOT the public page; leave
it alone). GitHub Pages is not yet enabled on the repository (noautopilot.github.io/cipher-lab answers 404); the owner enables it from
Settings > Pages (branch main, folder /docs) after the fact check below. Nothing this job writes is live until then.

Read first: CLAUDE.md rules 4a, 8, 9, 10 and the Outreach section (gates 3, 4, 6 apply to every sentence on a public page: the audit's
safe sentence, any prior print it rests on, a link to AUDIT.md, the primary-source image, the printed edition at the page cited; rule-10
wording only -- never first/new/unpublished/never printed; "no prior decipherment located" is allowed only at N4); research/DECIPHERMENT-
STANDARDS-2026-10-04.md (depth words: D1 "fragments read", D2 "partially deciphered (about N%)", D3 "largely deciphered", D4
"deciphered"); README.md "What counts as a result"; tools/build_dashboard.py (how status.json is read; reuse its loaders, never its page).

Build, in order:
1. ROOM claim via `python3 tools/room.py "CATALOGUE-SITE-1 worker (account 4, Opus)" "claim ..." --push`.
2. `tools/build_catalogue.py` (offline test in tools/tests/, `--help`, SYSTEM.md line, system_map_check ok): reads status.json (every
   result row with an N-class and a depth, not superseded), each target's AUDIT.md (the verdict's safe sentence, key source ours/period/
   published, text known/not, the audits' dates and the search families logged) and NOTES.md head (status, holder, shelfmark, image ark);
   writes `docs/catalogue.html` (index: counts by outcome in the board's own classes -- recovered-passage documents, completed readings,
   fragments read, keys to known text, contributions -- then one row per item: date, sender -> recipient, holder + shelfmark, language,
   class N0-N5 in words, depth in words, key source, the one-line English gist from `depth_sentence` marked "(interpretation)") and
   `docs/items/<slug>.html` per item (the safe sentence verbatim; the gist; the cipher's design in one line; the key's source and credit
   -- "read with Tomokiyo's published 1572 key", "Bourdeau's verified key", "a period key rebuilt by us"; links: the primary image (Gallica
   ark / IIIF / holder viewer from the folder's manifest), the printed edition at the page cited, the repository folder, AUDIT.md, the
   reading file and the decode script; what was searched and where it was not found, as the audit logs it; the audits' dates; "verified
   by a separate session" per audit). Credits page: Tomokiyo (Cryptiana), Bourdeau (cyphersolver, MIT/CC BY), Aymeloglu (unsolved-ciphers),
   Lasry/Biermann/Tomokiyo 2023, and every published key by name. A short "How to read this" page: the N-classes and depth words in plain
   language, the two-audit rule, what "ours/period/published" means, and that every page is generated from the audit files.
3. Content rules: plain language, no internal job names, session ids, costs or account numbers; no personal data (rule 9); dates
   absolute; nothing about targets that are `open` or `blocked` beyond a count ("N targets in work"); restricted material never (check
   RESTRICTED.md and skip anything it names, Debosnys included); images: link, never embed a holder's image whose licence the folder
   does not record as public domain or CC. Colours pass `tools/cvd_check.py`; the page works at phone width.
4. Run the builder; `tools/file_shrink_guard.py` on docs/ paths; paste the item count and the class counts in the done line; the counts
   must equal the board's (python3 tools/build_dashboard.py x prints them) or the done line says why.
5. Done line "for orchestrator (account-4)": what was built, counts, the three items whose pages a fact-checker should read first, and
   the follow-up row the orchestrator queues (CATALOGUE-CHECK: a separate session reads every item page against its AUDIT.md and
   falsifies each factual sentence before the owner enables Pages). Stage by path; never force-push; never AskUserQuestion; never print
   credentials; no ciphers/ file edited.

## Amendment 1 (orchestrator, 22:2x UTC 9 Oct by date -u; the owner at 22:1x UTC: "don't post anything publicly like that; if you do mock-ups I can look it over")
Nothing public. (1) Write nothing under docs/ (the GitHub Pages folder): no docs/catalogue.html, no docs/items/. (2) tools/build_catalogue.py
takes an output directory (default research/mockups/catalogue/) and that is what is committed: the generated index and per-item pages,
self-contained HTML, no external scripts. (3) One single-file mock-up research/mockups/catalogue-2026-10-09.html shows the index and three
complete item pages inline (Gramont 1530 to Montmorency, Manteuffel 1712 f.410, Lodewijk 5797) for the owner to judge look and wording.
(4) Every content rule above stands. (5) Step 5's "the owner enables Pages" is withdrawn: the owner decides after the mock-up; the
CATALOGUE-CHECK fact-check row is queued only if he says go.
