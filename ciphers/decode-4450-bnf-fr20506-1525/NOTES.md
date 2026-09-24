# decode-4450-bnf-fr20506-1525

Status: open

## What this is

DECODE R4450: unsigned letter, BnF Français 20506, f.136, 1525-1550, French envoy/despatch series
(Non-decrypted, 5 images, no attached document found on the record page). QUEUE.md row DC1 ("DECODE
non-decrypted records with images", LANE N diff of 24 Sept 2026) flagged it as a "recovery, finish-existing-key"
lead because 18 other DECODE records in the same volume (BnF fr.20506, ids 4434-4449 + 4815-4816) are already
Decrypted. Checked as part of LANE N check-solved batch DC1 (`.claude/briefs/runs/2026-09-24-lane-n-csDC1.md`).

## Check-solved sweep, 24 September 2026

1. **Tomokiyo.** `sources/cryptiana/web/venetian.htm` identifies this exact folio directly: "Several
   undeciphered letters of Hieronimo Ranzo use similar ciphers with superscript figures (BnF fr.2988 ... f.2,
   f.9-10; BnF fr.3019 ... f.73-74; BnF fr.20506, f.136 (a copy of BnF fr.2988, f.9, which Norbert Biermann
   pointed out to me))." This places f.136 as a copy of a specific, still-undeciphered Ranzo letter (fr.2988
   f.9) — Tomokiyo does not say the volume's 18 Decrypted siblings share Ranzo's system, and QUEUE.md's own
   "finish-existing-key" framing did not check this before scoring.
2. **Bourdeau.** dbourdeau/cyphersolver's `CATALOGUE.md` entry 1.6 (a scored row, not the solved list) is this
   exact item: "DECODE R4450 = BnF fr. 20506 f. 136, a copy of fr. 2988 f. 9 (the R1894 letter). No key,
   decipherment or transcription on the DECODE record (checked 21 Sept 2026). The fr. 2988 Ranzo letters were
   transcribed here in vasto1527/ (n20/ranzo_c0*.txt, ~2,600 groups) with the Garbino letter (fr. 3022 no. 20),
   which uses the same initial-letter + number code. The numbering is not alphabetical, and a word annealer
   recovers only function words. No clear copy, crib or base key was found. Needs Ranzo's table or a clear
   copy; see entry 7." Bourdeau has therefore already attempted the Ranzo cipher system this letter belongs to
   (via its fr.2988 archetype and the related Garbino letter) and stalled — R4450 is not new ground, and the
   "key almost certainly exists" hypothesis in QUEUE.md's DC1 row is not supported by either named source.
3. **Aymeloglu.** aaymeloglu/unsolved-ciphers's `catalogue/decode-catalog.csv` and `decode-records.jsonl`
   carry id 4450 (routine catalogue row) but it is absent from `decode-ranked.md`'s printed rows and from
   `exclude.txt`, consistent with a catalogue entry that has not been attempted there either.
4. **Web.** WebSearch `"Hieronimo Ranzo" OR "Girolamo Ranzo" Gattinara chiffre déchiffré 1525 fr.2988` returned
   only tangential hits (Wikipedia disambiguation pages, a snippet confirming from dbourdeau's own published
   site that Ranzo used "an initial-letter code" as Gattinara's kinsman) — no third-party solution located.
5. **DECODE.** A prior LANE N pass this session read R4450's RecordsView page directly (QUEUE.md DC1 row): no
   attached key/transcription/decryption document found.
6. **Community lists.** Tomokiyo's site is the list of record here (item 1); no separate forum thread found.

## Verdict

**Open**, not found-solved. But the "finish-existing-key" plan in QUEUE.md's DC1 row needs revision before any
transcription pass: this folio is a copy of a specific undeciphered Ranzo letter (fr.2988 f.9) in a system
Bourdeau has already tried and failed to break (function words only recovered, no base key), not a plain
sibling-alignment problem against the volume's 18 already-Decrypted records — nobody has shown those 18 share
Ranzo's cipher. If this target is promoted, the next step is to check the 18 Decrypted siblings' own system
against Ranzo's transcribed corpus (Bourdeau's `vasto1527/n20/`) before assuming either helps the other.

Requests this pass: WebSearch 1, github.com 0 (reused this session's shared shallow clones, logged in
ROOM.md). No fresh DECODE login (reused the prior worker's RecordsView read). No promotion, no decoding.

flag for LANE N orchestrator: DC1's QUEUE.md rationale over-states the strength of the "finish-existing-key"
lead; recommend the row be corrected or the nomination carry this caveat.

## LANE N audit, 24 September 2026

DocumentsList check (`DocumentsList?showmaster=records&fk_id=4450`, read in the same login as DC2/DC4/DC5/
DC8/DC9 below): **"No records found"** — no attached document of any kind. RecordsView confirms `Inline
Cleartext: No`, `Inline Plaintext: No`, `Available Documents:` (empty). This adds nothing to the check-solved
verdict above: still **open**, still the weaker "copy of a stalled Ranzo attempt" framing, not
"finish-existing-key". Status word unchanged.

`sources/decode/records-non-decrypted-2026-09-24-diff.tsv` was regenerated this session (normaliser fix, see
`tools/decode_neighbours_exclude.py`); R4450's `held_by` is now `ours:decode-4450-bnf-fr20506-1525` (was
`none`, because this folder did not exist when the stale diff was generated) — an artifact of the pipeline
having since caught up to this record, not a new finding about the Ranzo system.

## DECODE fetch, 24 Sept 2026

For LANE R2 (ROOM 08:50 flag). One login (`tools/decode_browser_login.js`), `--fetch-page RecordsView/4450`
plus auto-discovery of its `/decrypt-custom/filesrv` links, `--delay 1600`. 8 images fetched into `images/`
(`TH_IMG_R4450_I26869_P1`-`P8`, .jpg/.jpeg, 6-17 KB each), manifest at `images/manifest.json` (file, source
URL, bytes, sha1, date). Note: the record page's own "Pages: 5" field undercounts — 8 distinct image files
are linked from the page, all 8 fetched. Confirmed again (per this folder's existing LANE N audit) that
`DocumentsList?showmaster=records&fk_id=4450` has no attached document. No transcription, no decoding.
Folder now 120 KB, well under the 30 MB cap.

## D1: transcription, 24 September 2026

**Blocked on image resolution, no blind passes run.** All 8 files are `TH_IMG_*` ("thumbnail image")
thumbnails, 200px wide (200x293/254/290/253/293/285/279/241, confirmed with `file`). Same test as run for
decode-1162 (this worker's other target, same session): 6-10x Lanczos upscales of line- and word-sized crops
of pages 2/4/6/7/8 (the four/five full-text pages) leave individual letterforms as an unresolvable blur --
the Ranzo system's diagnostic feature per Tomokiyo (superscript figures over an initial-letter code, see
`sources/cryptiana/web/venetian.htm`) would need to be visibly a *superscript*, which is not recoverable at
this resolution even in principle. Bourdeau's own CATALOGUE.md entry 1.6 (cited in this folder's check-solved
section) confirms he worked from BnF's own images for the related fr.2988/fr.3022 Ranzo letters, not a 200px
thumbnail -- this record's own attachment set is comparatively degraded.

Per CLAUDE.md rule 2 (image over transcription) and rule 7 (reproducible from the image), a blind pass at
this resolution would not be a real transcription. No `ciphertext.tsv`, no comparison against Bourdeau's
fr.2988 f.9 transcription (that step needs an actual token sequence to compare, which this pass could not
produce). Wrote `inventory.tsv` instead, page level only: pages 1/3/5 are mostly blank docket/address leaves
with small illegible marks; pages 2/4/6/7/8 are full pages of continuous handwriting (roughly 15-21 lines
each) that cannot be classified cipher-vs-clear or counted into tokens from what's on disk. Page 8 carries a
probable subscription line and a wax-seal-or-ink mark bottom-left.

**Follow-up (one-line suggestion, not run here):** same as decode-1162 -- a networked worker should check
whether DECODE's viewer for record 4450 offers anything larger than these `TH_IMG_*` thumbnails before this
target is written off as needing a fresh BnF Gallica capture of fr.20506 f.136 instead (LANE G2 already has
live Gallica fetchers this session and may be a faster route to a real image than re-querying DECODE).

Grades: none (no tokens read). No fr.2988 f.9 comparison possible (needs a real transcription first).
Requests this pass: 0 (no network, per brief).
