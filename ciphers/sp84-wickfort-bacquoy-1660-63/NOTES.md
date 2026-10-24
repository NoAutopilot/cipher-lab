blocked

Promoted from `ciphers/_triage/sp84-wickfort-bacquoy-1660-63.md` (worker CHECK-SP84POOL, 24 Oct 2026) by job
KEY32-TSV-PROMOTE (`.claude/briefs/runs/2026-10-24-acct4-research-director-49.md`), account 4, 24 Oct 2026. Every
unread piece in this folder waits on the TNA copy order in `REQUEST.md`: this is why the folder opens `blocked`
(CLAUDE.md rule 5), not `open` -- the key is now in hand (grade H), but there is nothing here yet to apply it to.

## Check-solved sentence (copied from the triage note, CHECK-SP84POOL, 24 Oct 2026)

Calendar of State Papers Domestic, Charles II, May 1660-May 1661 (archive.org
`sim_great-britain-public-record-papers-domestic-charles-ii_may-29-1660-may-1661`, whole-volume djvu text read
by this worker), June 1661-December 1662 (`..._june-1661-december-1662`) and January 1663-August 1664
(`..._january-1663-august-1664`) were each fetched once and whole-volume grepped (Wickfort/Wiquefort/
Wicquefort, Bacquoy/Bacquoij/Bacquoi, "undecoded", "in cipher", "cipher" bare, and the index's own "Cipher"
heading) by this worker: none of the 18 items below is printed, summarised, or indexed in any of the three
volumes under its own date/folio. The only name hits are unrelated items (three "[De Wiquefort's despatch]"
entries on the chimney tax and the Queen's landing, June-61/Dec-62 vol., pp.324/371 per its index; two "M. De
Bacquoy" letters in the Jan-63/Aug-64 vol. dated Sept. 2-3 [1663], pp.265/276 per its index, about Downing's
arrival at the Hague and thanks for money sent — neither date matches any pool item, and neither is marked
"cipher" or "French" beyond the ordinary language tag). No CSP Foreign series covers Holland for this period
(established for the same SP 84/165 piece in `ciphers/sp84-fuente-1662/NOTES.md`, citing `ciphers/
sp84-chauran-1662/NOTES.md`; not re-verified fresh this pass — the printed CSP Foreign series stops in
Elizabeth I's reign, which is why this project reads CSP Domestic for SP 84 letters at all). CSP Venetian
covers Venice, not Holland, and was not searched (out of scope by definition, not a coverage gap). Cryptiana's
`sources/cryptiana/web/chauran.htm` (on disk, read in full by this worker) is the decisive hit: see below.

## Premise check (copied from the triage note, CHECK-SP84POOL, 24 Oct 2026)

(a) Folder's own files: no `ciphers/<slug>/` folder existed yet for this pool at the time of that check; the two
neighbouring folders in the same piece network — `ciphers/sp84-chauran-1662/` (Chauran's own letters, verdict
`not-a-cipher`: letters *about* ciphers, not ciphertext) and `ciphers/sp84-fuente-1662/` (the Marqués de la
Fuente Spanish intercepts in the same SP 84/165 piece, key SP 106/6 no. 34, still `open`) — were both read;
neither names any Wickfort/De Bacquoy item in Group A or B, and neither's key (no. 34, Spanish) is the same key
as Group A's (no. 32/no. 31+35, French).
(b) Other solvers' working files: Aymeloglu's `unsolved-ciphers` (fresh shallow clone, grepped only), Bourdeau's
on-disk snapshots, and the DECODE listing cache — no hit, no rendered/applied key found for either group.
(c) Physical neighbours: not checked — none of the 18 items is digitised (Group B confirmed `digitised: false`;
Group A's digitisation status was not re-checked since they are already known-text, not a cryptanalysis target),
so there is no image to view a facing page or pasted slip on.
(d) Recipient's side: Wickfort and De Bacquoy are Orangist informants writing *to* the English Secretaries of
State, not foreign-government correspondents with their own state archive; there is no "recipient country"
documentary edition distinct from the CSP Domestic calendar already read.

## Pool

Harvest row: `harvest/C-FOLLOW-2026-10-24-sp84-gloss.tsv` (worker C-FOLLOW, 24 Oct 2026). Two groups, same
correspondent network (Wickfort and De Bacquoy, Orangist informants to Joseph Williamson/Sir Edward Nicholas/
Sir Henry Bennet), same piece series (SP 84, State Papers Foreign, Holland).

### Group A — SP 84/165, PRO-decoded siblings (8 items, key SP 106/6 no. 32, f.213 also nos. 31/35) — known-plaintext controls

| Discovery id | Reference | Folio | Date | Correspondents | PRO-decoded |
|---|---|---|---|---|---|
| C7306600 | SP 84/165/8 | 13 | 1662 nd | [Chauran] to [Williamson] | yes (SP 106/6 no. 32) |
| C7306657 | SP 84/165/65 | 106 | 1662 Mar 5 | Wickfort to [Williamson] | yes (no. 32; chauran.htm "5 March") |
| C7306656 | SP 84/165/64 | 105 | 1662 May 3 | Wickfort to [Williamson] | yes (no. 32; chauran.htm "3 May") |
| C7306701 | SP 84/165/109 | 184 | 1662 Apr 19 | Wickfort to [Williamson?] | yes (no. 32; chauran.htm "19 April") |
| C7306706 | SP 84/165/114 | 190 | 1662 May 7 | [Chauran?] to [Williamson?] | yes (no. 32) |
| C7306707 | SP 84/165/115 | 192 | 1662 Apr 26 | Wickfort to [Williamson?] | yes (no. 32; chauran.htm "26 April") |
| C7306718 | SP 84/165/126 | 213 | 1662 May 5 | Wickfort to [Williamson?] | yes (**nos. 31 and 35** — the *second*, numbers-to-999 cipher, not no. 32) |
| C7306719 | SP 84/165/127 | 214 | 1662 May 14 | Wickfort to [Williamson?] | yes (no. 32; chauran.htm "14 May") — carries Wickfort's own "nouveau chiffre" remark |

Tomokiyo's chauran.htm independently names five of these exact dates (5 March, 19 April, 26 April, 3 May, 14
May 1662) as Wickfort letters using "the same cipher as Chauran's" = SP 106/6 no. 32 (encoding table, this
folder's key.tsv) / no. 33 (decoding table, not needed once no. 32 is in hand), and separately names Wickfort's
letter of 5 May 1662 as using the *different*, numbers-to-999 cipher, SP 106/6 no. 31 (decoding) + no. 35
(encoding) — an exact match to f.213. This is prior structural/key work by Tomokiyo (2012), not a plaintext
reading; it does not itself decipher any letter but independently confirms the harvest row's key citations.

### Group B — undecoded candidates (10 items, no key cited in their own Discovery note) — targets

| Discovery id | Reference | Folio | Date | Correspondents | Note (verbatim) | Digitised |
|---|---|---|---|---|---|---|
| C7306789 | SP 84/166/7 | 19 | 1662 Jul 7 | [Wickfort] to Williamson | Part in undecoded cipher. Copy. | False |
| C7306823 | SP 84/166/41 | 85 | 1662 Aug 10 | Wickfort to [Williamson] | Undecoded cipher. | False |
| C7306833 | SP 84/166/51 | 106 | 1662 Sep 1 | De Bacquoy to Nicholas | Part in undecoded cipher. | False |
| C7306834 | SP 84/166/52 | 108 | 1662 Sep 18 | De Bacquoy to Nicholas | Small part in undecoded cipher. | False |
| C7306853 | SP 84/166/71 | 167 | 1662 Oct 15 | De Bacquoy to [Williamson] | Part in undecoded cipher. | False |
| C7306863 | SP 84/166/81 | 184 | 1662 Nov 4 | De Bacquoy to Bennet | Part in undecoded cipher. | False |
| C7306866 | SP 84/166/84 | 188 | 1662 Nov 10 | De Bacquoy to Williamson | Part in undecoded cipher. | False |
| C7306880 | SP 84/166/98 | 213 | 1662 nd | Wickfort to [Williamson] | Undecoded cipher. | False |
| C7307065 | SP 84/168/26 | 60 | 1663 Oct 28 | De Bacquoy to [Williamson] | Part in undecoded cipher. | False |
| C7307408 | SP 84/171/55 | 123 | 1660 Aug 9 [OS/NS] | De Bacquoy to Williamson | Part in undecoded cipher. | False |

Key question per item: Wickfort items (ff.19, 85, 213) — expected no. 32, unconfirmed (the PRO itself did not
decode them with a key it otherwise held, the open question this pool exists to resolve; SP 84/166 f.213 is a
second, separate Wickfort item from Group A's f.213 in SP 84/165, different piece). De Bacquoy items (the other
seven, ff.106, 108, 167, 184, 188, 60, 123) — a different, numerical cipher per chauran.htm's own loose
description (low numbers = single letters, numbers above ~50 = two alphabetically-ordered word/syllable series;
11 value/meaning pairs given, e.g. 51=accord, 270=France, 939=vo); no PRO key is named for De Bacquoy anywhere
in chauran.htm or in the Discovery/archive.org/solver-repo search above — key unidentified.

## Key

`key.tsv` (this folder) is DECODE's own 2020 text transcription of TNA SP 106/6 no. 32 — the Chauran/Wickfort
French encoding table (chauran.htm: "alphabetical by word/syllable, persons/towns/countries as separate
sequences") — read from two DECODE records that both carry the full table: 509 (`TNA_SP106/6_CharlesII_
(0099-0101)`, pages 3711-3713, transcriber AP, 13 Aug 2020) and 506 (`TNA_SP106/6_CharlesII_(0096)`, page 3705,
transcriber AP, 10 Aug 2020). **Correction to the prior pass's note** (`ciphers/sp84-fuente-1662/NOTES.md`
"## DECODE fetch, second pass"): that pass described 506 as "the shorter, overlapping copy" duplicating only
509's first section (the letter alphabet and person codes). Re-reading 506's full attached text this pass shows
it is not shorter in content — it carries its own complete Villes, Royaulmes and word/syllable homophone lists
through to Z and the null row, the same sections 509 spreads across three page-images. 506 is one physical page
(3705.png) of very dense writing, not a partial table; the "shorter" description in the prior pass's README
(`sources/decode/2026-10-24-sp106-6-keys/506/README.md`) is superseded by this reading and should be read with
that correction. No key.tsv edit was needed to the prior pass's own verdict ("match no. 32") — that holds — only
to the claim about 506's completeness.

**key.tsv is applied to nothing in this job** (no decode, per brief). It is reproducible from the two source
documents by `build_key_no32.py` (CLAUDE.md rule 7): the documents themselves are not committed
(`sources/decode/NOTES.md`: raw DECODE text/images stay out of the repository) — re-fetch them with
`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 509 OUT --fetch
"https://de-crypt.org/decrypt-custom/filesrv/?file=DOC_R509_D2952_2952.txt,https://de-crypt.org/decrypt-custom/filesrv/?file=DOC_R509_D2953_2953.txt,https://de-crypt.org/decrypt-custom/filesrv/?file=DOC_R506_D2951_2951.txt"
--max-files 3` (one login), then run `python3 build_key_no32.py build --doc2952 OUT/DOC_R509_D2952_2952.txt
--doc2953 OUT/DOC_R509_D2953_2953.txt --doc2951 OUT/DOC_R506_D2951_2951.txt --check` to verify the committed
key.tsv is still current, or `--check-hash` (same three paths) to confirm a fresh fetch is byte-identical to this
pass's without needing to re-run the parse.

**Row counts by class** (1,692 rows total; `note` column carries "conflict: ..." where 509 and 506 disagree on
the same code's value, per rule 4 — kept as separate rows, not resolved by majority):

| class | rows | numeric code range | unique meanings |
|---|---|---|---|
| letter | 144 | 10-33 (plus named-mark forms, no numeric range) | 24 |
| person | 216 | 9-76 (double-underscore block 20-76 plus a separate primed block 9'-60' for foreign dignitaries — two numbering systems sharing the "person" class, not one continuous 20-76 range) | 201 |
| ville | 58 | 61-89 | 42 |
| royaume | 38 | 90-108 | 30 |
| word | 934 | 1-100 | 448 |
| syllable | 188 | 1-100 | 74 |
| other (null) | 114 | 1-47 | 1 (`<NULL>`) |

**Cross-check against chauran.htm** (`sources/cryptiana/web/chauran.htm`, quoted in full above): "the words and
syllables are arranged in the alphabetical order in the encoding table ... persons/towns/countries as separate
sequences", "a structure of two-part code." chauran.htm gives no exact numeric ranges for no. 32/33 itself (the
20-76/61-89/90-108 ranges came from this pass's own reading of the transcriptions, not from chauran.htm); the
ranges above are internally consistent across 509 and 506 and with the letter-alphabet/Villes/Royaulmes
structure chauran.htm describes qualitatively. No range disagrees with chauran.htm's description. The
`word`/`syllable` split in the table above is this script's own closed-list heuristic over short French
fragments (`build_key_no32.py`'s docstring) — descriptive bookkeeping for this key.tsv, not part of DECODE's or
Tomokiyo's own classification, and not a graded distinction; read the two rows together as one homophone pool.

**Conflicts**: of 549 (class, code, mark) keys attested in both 509 and 506, 210 (38%) carry a different
`meaning` string between the two sources (429 rows total flagged, two per disagreeing key) — mostly small
spelling/reading variants on the same person name (e.g. code 21: "le Duc Danjou" in 509 vs "M^r le d. Danine" in
506; code 33: "De Meaufort" vs "D. Bev*ufort") rather than wholesale different identifications. Per rule 4 this
is logged as a data conflict between two H-grade transcriptions, not adjudicated by majority: a future worker
applying this key to a Group A or Group B letter should expect a code's exact spelling to vary by which sheet is
closer to that letter's own hand, and should check both rows before treating a mismatch as a transcription
error on the letter side.

Note: SP 106/6 nos. 31 and 35 (the second, numbers-to-999 cipher for SP 84/165 f.213) and DECODE id 497 are
still unlocated on DECODE, but that is a gap in the *key-identification* work tracked in
`ciphers/sp84-fuente-1662/NOTES.md`, not in this pool's own folder (dropped from this job's scope per the
account-4 parent's check-in 148 decision, a separate job) — not listed as a gap of this target below.

## Remaining gaps (finish-or-blocker pass, 24 Oct 2026)
Read so far: unmeasured: no digitised image exists yet for any of the 18 pool letters to measure a read fraction against
- Group A letters (8 items), unread against key.tsv as a known-plaintext control - blocker: needs-physical-access; none of the 8 PRO-decoded letters is digitised beyond DECODE's own transcription of the key itself, not the letters; next: TNA copy order, see REQUEST.md
- Group B letters (10 items), unread - blocker: needs-physical-access; all ten carry `digitised: false` in their own Discovery record (checked by CHECK-SP84POOL and reconfirmed this pass); next: TNA copy order, see REQUEST.md
- De Bacquoy's own numerical cipher key (the 7 De Bacquoy items in Group B) - blocker: needs-physical-access; chauran.htm's 11 value/meaning pairs are a lead, not a PRO key citation, and no De Bacquoy letter or key sheet is digitised to test them against; next: TNA copy order, see REQUEST.md

## Escalation (24 Oct 2026)
- [x] siblings: Group A's 8 PRO-decoded letters are already identified and tabulated above as the known-plaintext control pool; no further sibling search is needed before the TNA order
- [n/a] clear-pages: no clear or plain-text facing page exists for any of the 18 items; every Discovery note marks each as wholly or partly in cipher
- [x] known-keys: SP 106/6 no. 32 recovered from DECODE this pass as key.tsv, grade H; no. 31/35 and De Bacquoy's own cipher remain unidentified but belong to a different target's gap, noted above
- [x] print: CSP Domestic Charles II (3 volumes, whole-text read) checked by CHECK-SP84POOL; no print of any of the 18 items found
- [n/a] key-rebuild: no cipher text is on disk yet for any of the 18 items, so there is nothing to rebuild a key against until an image arrives
- [x] image-check: Discovery's own digitised flag was checked for all ten Group B items (false) by CHECK-SP84POOL and reconfirmed this pass
- [n/a] retry: no image exists yet for any of the 18 items, so there is nothing to retry reading

Verdict: parked: every gap has an outside blocker (needs-physical-access; see REQUEST.md)

## While waiting

No action in this pool depends on nobody once key.tsv exists: the only things left to do (read Group A against
the key; acquire Group B's images) both need the TNA order placed first. `python3 tools/next_steps.py
--wait-only | grep sp84-wickfort-bacquoy-1660-63` is empty (confirmed below) — this folder correctly names no
wait-only row of its own, since every remaining gap above is an outside blocker (needs-physical-access), not an
internal step someone could run while waiting. SP 106/6 nos. 31/35 and DECODE id 497 remain open leads for a
future DECODE pass, but that is a different target's gap (see the note above "## Remaining gaps"), not this
folder's own wait-only action.

## Gate outputs

### `python3 tools/dup_check.py sp84-wickfort-bacquoy-1660-63`
```
ok: sp84-wickfort-bacquoy-1660-63 has no outstanding claim in the last 24h (no claim line, or the latest claim has a later done)
```

### `python3 tools/prior_work.py sp84-wickfort-bacquoy-1660-63`
The tool now requires one of `--item/--item-spec/--derive/--register/--brief/--interceptor/--record` (the
brief's bare invocation errors with "one of the arguments ... is required" on this version); run both the
closest equivalents:
```
$ python3 tools/prior_work.py sp84-wickfort-bacquoy-1660-63 --derive --step-type lookup --offline
derive sp84-wickfort-bacquoy-1660-63: 0 proposed row(s) -> ciphers/sp84-wickfort-bacquoy-1660-63/items.pending.tsv (items.tsv untouched)
exit: 0
```
```
$ python3 tools/prior_work.py sp84-wickfort-bacquoy-1660-63 --brief .claude/briefs/runs/2026-10-24-acct4-research-director-49.md --offline
[two adhoc items auto-extracted from the brief's own folio citations, SP 84/166 f.85 and SP 84/165 f.106]
verdict step: LEAD (both items; the only "lead" found is this job's own live ROOM.md claim line, a false-
positive self-match, not a prior-work hit)
verdict plaintext: LOOK (both items; look.tsv lists 7 crop(s) owed, 0 on disk -- i.e. no image exists yet,
which is exactly this folder's own `needs-physical-access` finding, not a block on building key.tsv or
writing REQUEST.md)
exit: 4 (owed before a *read* step on those two items specifically; this job never reads or decodes them, so
nothing here is owed before this job's own steps)
```
No ciphertext/decode.json exists for this target (it is a promoted pool awaiting TNA images, not a cryptanalysis
target yet), so `--derive`'s normal item-seeding has nothing to seed from; recorded as 0, not a failure.

### `python3 tools/intake_gate_check.py sp84-wickfort-bacquoy-1660-63`
```
sp84-wickfort-bacquoy-1660-63: blocked (line 1) -- already terminal, nothing to gate
exit: 0
```

### `python3 tools/gaps_check.py sp84-wickfort-bacquoy-1660-63`
```
OK parked sp84-wickfort-bacquoy-1660-63: parked: 3 gap(s), all outside blockers
gaps_check: 1 checked: 1 parked, 0 keep-going, 0 FAIL, 0 skipped
exit: 0
```

### `python3 tools/next_steps.py --wait-only | grep sp84-wickfort-bacquoy-1660-63`
```
(empty)
```
