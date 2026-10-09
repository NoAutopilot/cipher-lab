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

## Amendment 2 (orchestrator, 22:2x UTC 9 Oct by date -u; the owner's four model pages, 22:2x UTC)
Models (CC BY 4.0: structure and voice, never a copied sentence): dbourdeau.github.io/cyphersolver/dinteville1592.html (a full item page
for a target we also hold), hesse1824.html#method ("Method": how the key was found, plain words), highlights.html#method ("Highlights":
favourites as one-paragraph stories -- the owner's "Hall of Fame"), mercy1648.html#the-cipher ("The cipher": the design and the key's
shape for a reader). Each mock-up item page carries "The letter", "The cipher", "Method" plus the gist and the safe sentence; the
single-file mock-up adds a "Hall of Fame" page of 5-8 favourites as one-paragraph stories (Gramont 1530, Manteuffel 1712, the Lodewijk
blanks, Birago 1572, the Suriname fort map, Mercy 1648 if its safe sentence allows). Where Bourdeau or Tomokiyo read an item first, the
page says so and links theirs. Cap unchanged: index and three item pages first, the Hall of Fame next if the cap allows.

## Amendment 3 (orchestrator, 22:3x UTC 9 Oct by date -u; the owner at 22:3x UTC: not a copy of Bourdeau; discoverable, clear, with the rigour behind it)
Amendment 2's "in his shape" is withdrawn: Bourdeau's pages are examples of a working public page, not a template; no mirrored sections,
names or layout. Ours is built around one idea -- a plain claim on top, its proof directly underneath, every link verifiable from a
reader's desk. Per item: the safe sentence as the claim with the gist marked interpretation; a proof panel with the per-token grade counts
(rule 4) and a one-line key to the letters, how the reading regenerates (decode script and --check, transcription and key files, linked),
the matched control where one was run (both numbers), the two independent audits with dates, the search families logged as searched and
as unreachable, the N-class and depth with their definitions one click away, whose key with the credit, the primary image at the leaf and
the printed edition at the page. Progressive disclosure: plain language first, the evidence expandable, nothing hidden. Index: one row per
item a search engine and a historian can both read, filterable by century, archive and outcome. The favourites page is "Readings worth a
historian's attention", each story limited to what its audit licenses.
