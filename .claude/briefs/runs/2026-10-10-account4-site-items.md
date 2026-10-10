# SITE-ITEMS-1/2/3: every item page gets the display's structure and rigour, with only as much story as the reading supports (account 4, Opus 5.5)

Written 10 Oct 2026 02:1x UTC by date -u by the orchestrator (account-4), session_012sGNgiddCpz4QUhQsMyoPU, on the owner's decision at
02:1x UTC ("Sure let's do it") after his question "when they click into one, can we give them the same care we did the three displays?".
The orchestrator's answer, which binds these jobs: the same STRUCTURE and RIGOUR on every item page, only as much STORY as the audited
reading itself supports -- a quartermaster telegram gets an honest short page, never a hook ("we don't make stuff up; if it's not
interesting, don't act like it's interesting", owner 9 Oct 22:5x). Parent briefs, all still binding: 2026-10-09-account4-catalogue-site.md
(+ Amendments), -catalogue-v2b.md (three-layer lines), -exhibit-1.md and -exhibit-2.md (display anatomy, CURATOR.md, SELECTION.md, image
and licence rules, portraits from the manifest only, no Wikimedia calls), 2026-10-10-account4-site-ship-1.md (one site, one builder,
research/mockups/site/build_site.py + tools/tests/test_build_site.py, private, never docs/, rule-10 wording, footer). The site is on
main at research/mockups/site/ and published private; the orchestrator republishes after each job.

## Job 1: SITE-ITEMS-1 -- the item-page template (cap USD 10, box 90 min; spawned by the orchestrator)
Every one of the 165 item pages gets, in the display's order, from data already on disk (status.json, AUDIT.md, SELECTION.md, the
folder's decode output and key, portraits/manifest.tsv):
1. **What it says** -- one plain sentence drawn from the audited reading: SELECTION.md's "the one thing the reading says" cell where it
   exists (139 items), else the status.json depth_sentence, else "A <kind> read at grade <N>; the reading is below the content bar" --
   never a sentence written from the letter's context.
2. **The reading, three layers** -- the slot for cipher crop / original language with grades / English, filled where a crop and an
   English line exist (the three v2b sample pages and the three displays' items), and otherwise the two layers that exist (the graded
   original from decode_key.py output) with the English slot marked "English line: pending (SITE-ITEMS-2)". The crop is cut by the
   same recipe the displays used (tools/iiif_lines.py from the folder's own images, never a network fetch; if no image is on disk, no crop).
3. **Who, where, when** -- sender, recipient, place, date from status.json; named persons and places from the reading's own name/code
   list (decode output), each a link to a per-person index page (people/<slug>.html) listing every item that names them; portrait from
   the manifest where on file, placeholder otherwise.
4. **How we know** -- the badges as the displays have them (N-class with the verifier's safe sentence, depth and %, key source
   ours/period/published, two audits yes/no) plus links to AUDIT.md, the decode script, key.tsv and the image source on GitHub main.
5. **Interest tier** recorded in the page's data attribute (SELECTION score 0-3, "thin" flag) and nothing else -- the tier chooses the
   length of the page, never a different tone: score >= 2 pages carry a "Context" section placeholder for Job 3; others do not.
Build it in build_site.py (one template function, data-driven), keep the link test green, add a test that every item page carries the
four sections and the pending marker count is reported. Push, done line with the pending-English count and the people-index size.

## Job 2: SITE-ITEMS-2 -- the English reading line for every item (cap USD 25, box 150 min; queued on Job 1's done line)
For each item without an English line: pick the reading's best stretch (the displays' rule: the clause the audit's depth_sentence
rests on, else the longest H/C-graded run), take its graded original from the decode output, and write the English line by the v2b
convention (translation, interpretation in square brackets, names and codes left as read, grades carried; "[unread]" where the token
is M or U). Unit = one item = one Opus call with the graded line and the key's gloss column only (no image, no context): about USD
0.12 a call, 165 units, stop before a unit that would cross 80% of the cap. Write the lines to research/mockups/site/data/english_lines.tsv
(item, line id, original, english, grade string, date) so the builder reads them; never edit a reading or a key. A second blind Opus call
checks every tenth line for added content (anything in the English not in the original or the gloss is a defect; fix and re-check).
Push, rebuild, done line with the count written and the spot-check result.

## Job 3: SITE-ITEMS-3 -- curator paragraphs for the dozen (cap USD 8, box 60 min; queued on Job 2's done line)
For every item with SELECTION score >= 2 (about a dozen; list them in the done line), write the "Context" section by CURATOR.md's rules:
the hook from the reading's own words, context labelled context and never supplying the hook, people and events named only where a
printed source on file names them (cite it), portraits as above, no sentence the audit does not support. One Opus call per item from
the item's AUDIT.md, NOTES.md head and SELECTION.md row; the orchestrator reads every paragraph before it is republished. Push, rebuild,
done line listing the items and one sentence per paragraph's source.

All jobs: run tools/restricted_guard.py --outgoing and tools/file_shrink_guard.py on every touched path before the final push and paste
the lines; rule-10 wording (never first/new/unpublished/previously unread for our work; "no prior decipherment located" at N4 only);
done line "for orchestrator (account-4)"; cost by get_session is the orchestrator's; stage by path; never force-push; never AskUserQuestion;
never print credentials; no network; ROOM claim before the first write.
