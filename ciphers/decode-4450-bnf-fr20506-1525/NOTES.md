open
DECODE RecordsView/4450 and DocumentsList read by this worker (no attached document, confirmed again); Tomokiyo's `venetian.htm` read in full by this worker (fresh fetch, not the local snapshot, which lacks this page); Bourdeau's `vasto1527/n20/ranzo_c017.txt`/`ranzo_c018.txt` witness grepped fresh in a new shallow clone — f.136 remains a copy of the still-undeciphered Ranzo letter fr.2988 f.9, no decipherment of that system has landed anywhere searched since the 24 Sept 2026 sweep below. Desjardins *Négociations diplomatiques de la France avec la Toscane* vol.2 and Molini *Documenti di storia italiana* (both job-brief-named editions, both read in full by this worker via archive.org djvu text) carry no occurrence of the fr.2988 f.9 / fr.20506 f.136 letter or its Ranzo/Garbino code; Molini does independently attest the covername "Garbino" for a *different* family's ciphered correspondence (Girolamo Centurione, not Girolamo/Hieronimo Ranzo) -- see follow-up section below.

# decode-4450-bnf-fr20506-1525

## Check-solved (LANE CX, 25 Sept 2026)

Re-verdict per `.claude/briefs/check-solved.md`. This target's NOTES.md did not follow CLAUDE.md rule 5 (bare status word alone on line 1) before this pass; fixed above. Extensive prior work exists below (24 Sept 2026 check-solved sweep, LANE N audit, DECODE image fetch, and a D1/D2 transcription+witness-alignment pass that independently confirmed Tomokiyo's identification token-for-token at 94.1% agreement against Bourdeau's own fr.2988 f.9 transcription) — this worker did not repeat that transcription work (out of this brief's scope: "No transcription... or cryptanalysis") but reran the six check-solved searches fresh to confirm nothing has changed since.

1. **Web (a).** WebSearch `Ranzo Garbino cipher fr.2988 OR fr.20506 "solves" Claude GPT decipherment 2026`: no third-party solve found. Results confirm the Ranzo-Garbino code (Bourdeau's own repo, ~3,900 groups now transcribed per his site, up from ~2,600 on 24 Sept) is still explicitly reported as **not solved** — "a word annealer validated on a held-out control recovers only function words, so no. 20 needs Ranzo's table or a clear copy" — consistent with, not a change from, the 24 Sept verdict below.
2. **Community lists / Tomokiyo (c).** `cryptiana.web.fc2.com/code/venetian.htm` fetched fresh by this worker (not read from the local snapshot for this pass, to confirm it has not been updated) and read in full: unchanged wording, f.136 "a copy of BnF fr.2988, f.9" — still listed among "several undeciphered letters of Hieronimo Ranzo."
3. **Bourdeau (e).** Fresh shallow clone (25 Sept 2026, shared with the other two targets in this batch), `vasto1527/n20/ranzo_c017.txt`/`ranzo_c018.txt` present and unchanged in content from what the 24 Sept D2 pass compared against; `CATALOGUE.md` entry 1.6 for R4450 unchanged.
4. **Aymeloglu (f).** Fresh clone's `catalogue/decode-catalog.csv` still carries id 4450 as a routine row, still absent from `decode-ranked.md` and `exclude.txt` — not attempted there.
5. **DECODE (d).** Cached `decode-catalog.csv` re-checked: record 4450 (BnF fr.20506 f.136) still `Non-decrypted`; the 18 sibling records in the same volume (ids 4434-4449, 4815-4816) still `Decrypted`, unchanged from 24 Sept. No fresh login run this pass (no new document expected; the prior LANE R2 fetch already confirmed `DocumentsList?showmaster=records&fk_id=4450` returns "No records found").
6. **Print/calendar (b).** Not applicable in the usual sense — no printed edition of this specific unsigned 1525-1550 despatch exists; the relevant "edition" is the manuscript archetype fr.2988 f.9 itself (Gallica) and Bourdeau's own transcription of it, both already checked in searches (c)/(e) above and in the existing D2 section below.

**Verdict: open**, unchanged from 24 Sept 2026. Status stays `open`, not `partial`: a copy relationship and a matched second-witness alignment are established (94.1%, see D2 below), but no decipherment of the underlying Ranzo/Garbino system exists anywhere searched, so there is no reading to grade. Not "new"; not "unpublished" (rule 10) — a search result, not a discovery. Requests this pass: `cryptiana.web.fc2.com` 1 (fresh fetch, curl -L browser UA, 200 after redirect, shared rate budget with bl-gualterio-1700's fetch in this same batch), WebSearch 1, github.com 0 (reused this batch's shared shallow clones), no DECODE login (cached catalogue sufficient).

### Standard-edition follow-up (LANE CX, 25 Sept 2026)

Job brief's two named printed sources, both fetched and read in full from archive.org djvu text (no browser
tool needed, no challenge on this host):

1. **Desjardins, *Négociations diplomatiques de la France avec la Toscane*, vol. 2** (archive.org
   `gri_33125010469852`, 1886 printing, 54,636-line djvu text; internal date coverage late 1524-1527, confirmed
   by its own table of contents headings, "SOIXANTE-TROIS LETTRES, DU 19 NOVEMBRE 1524 AU 13 AVRIL 1525" and
   "QUARANTE-QUATRE DÉPÈCHES, DU 4 DÉCEMBRE 1526 AU 14 AOÛT 1527" -- squarely inside this target's own
   1525-1550 window). "Ranzo" 2 hits, both OCR false positives on the unrelated Italian verb *ranzonare*/
   *ranzoneranno* ("to ransom"), not the surname. "Garbino" 0 hits. No occurrence of the letter or its code.
2. **Molini, *Documenti di storia italiana*** (archive.org, 2 distinct physical volumes each scanned twice by
   Google Books: `documentidistor00moligoog`/`01moligoog` and `documentidistor02moligoog`/`03moligoog`, all four
   fetched; 00/01 are the same volume at two OCR passes, confirmed by identical "Garbino" hit contexts, likewise
   02/03). "Ranzo" hits in all four are OCR false positives on *ranzon*/*ranzonare* ("ransom"), as in Desjardins.
   **"Garbino" 3 hits each in 00/01 and 02/03 -- a real, non-false-positive occurrence of the covername**, but
   for a **different person**: document No. CLXIV, "Martino Centurione, da Burgos 17 Gen. 1528, a Girolamo suo
   figlio, a Genova," carries a marginal note explaining that Girolamo (Seronimo) **Centurione** of Genoa was to
   receive letters from the Imperial court in cipher, *"sono adrissate di corte di Cesare in Genova al predetto
   Ieron.° et da Genova per ditto Ieronimo inviate ad Martino suo padre"* under the covername **Garbino** --
   i.e. a Genoese banking-family correspondence (Centurione), 1528, structurally identical in shape (a son at
   the Imperial court ciphering news home to his father under the name "Garbino") to the Ranzo/Garbino system
   Bourdeau names for this target, but **a different Girolamo, a different family, three years later than this
   target's earliest possible date, and not naming Ranzo, fr.2988, fr.20506 or fr.3022 anywhere nearby**. This
   is not a match for the target letter and is not treated as one; flagged here only because "Garbino" is
   otherwise a rare enough string that an independent, non-Ranzo attestation of the same covername convention
   is worth a future worker's attention if the wider Garbino-code question (is "Garbino" a generic diplomatic
   covername reused by unrelated correspondents, or does Centurione's usage connect to Ranzo's some other way?)
   is ever picked up -- not run further here, out of this brief's scope (no cryptanalysis, no attribution work).
3. No occurrence of "fr.2988", "fr.20506", "fr.3022", "Vasto", "Gattinara" (Ranzo's patron, per Tomokiyo) tied
   to Ranzo by name in either edition.

Requests this section: archive.org 6 (1 advancedsearch for Desjardins, 1 `_djvu.txt` fetch; 1 advancedsearch
for Molini, 4 `_djvu.txt` fetches), all `-L` follow, >=1.6s apart, descriptive UA, all HTTP 200. No browser
tool, no github, no DECODE login (nothing new to fetch there this pass).

`python3 tools/intake_gate_check.py ciphers/decode-4450-bnf-fr20506-1525` output: see done line.

**Verdict: unchanged, stays open.** Both job-brief-named editions are now directly read with no hit for the
target's own letter; the Ranzo/Garbino system remains undeciphered everywhere searched across this and the
prior 24-25 Sept passes.

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

## D2: transcription and witnesses, 24 September 2026

Superseded the D1 blocker: LANE G2 fetched real 2000px IIIF images (`images/fr20506_f136r.jpg`, `f136v.jpg`,
`fr2988_f9r.jpg`, `f9v.jpg`, manifest entry `gallica_natives`), not the DECODE `TH_IMG_*` thumbnails D1 was
stuck on. At this resolution the letter+superscript-number system is fully legible (no more "unresolvable
blur" concern).

**Transcription.** `ciphertext_f136.tsv` (page, line, idx, token, doubt): one row per token as written, read
from local crops of the Gallica images (`tools`-style Lanczos-upscaled bands, no network beyond the one
already-cached image). 749 tokens total (f136r 344, f136v 405), 320 distinct code types (letter+number
groups), doubt flagged on 3 tokens (two cancelled/scratched marks and one digit run I could not resolve even
zoomed — see below). Base-letter distribution (t 80, s 64, m 62, n 57, p 54, c 53, d 50, L 49, z 49, a 40, i
36, f 27, b 20, e 20, y 19, ...) matches the shape Bourdeau's NOTES.md describes for this same code family
(no. 20/Garbino-Ranzo): a large set of per-letter lists (a-z plus a separate "L" glyph he reads as la/le, and
z-groups behaving as nulls/punctuation). No decipherment attempted (out of scope).

**Second witness.** Per brief, checked `dbourdeau/cyphersolver`'s `vasto1527/n20/ranzo_c0*.txt` (shallow clone,
grepped, not committed; MIT code / CC BY 4.0 text, cited not copied) before transcribing fr.2988 f.9 fresh.
`ranzo_c017.txt` is headed "fr.2988 view 17 (Ranzo)" and `ranzo_c018.txt` "view 18" — Bourdeau's own NOTES.md
states views 17-20 are ff. 9r-10v of fr.2988 (ark `btv1b9059908w`), so **c017 = f.9r, c018 = f.9v**, transcribed
by his "six subagents" from full-resolution scans. Its opening tokens (`b5 f3 c227 g72 p246 v212 t74 h57 s116
m9 t163 t30 p78 ...`) match fr20506 f.136r's first line token-for-token once his glyph vocabulary (g, v, z, L,
Q, D as distinct base letters/marks in this hand) is applied — direct confirmation of Tomokiyo's identification
that f.136 is a copy of f.9, independent of Tomokiyo's own say-so.

**Alignment** (`compare_f9.tsv`, `page/line/idx/our_token/witness_source/witness_token/type`, produced by
`difflib.SequenceMatcher` over the flat token sequences, script not committed — trivial and one-off): of our
749 tokens, **705 align as exact equal blocks with the witness (94.1%)**; 45 rows are single-token
replacements, 2 are tokens on our side with nothing to align (extra-in-ours), and 259 rows are witness tokens
past the point our text stops (see below, not real disagreements). The 45 replacements cluster almost
entirely on classic secretary-hand look-alike pairs in this specific hand: **b/h** (b7/h7, b51/h51, h10/b10,
b35/d35 — 10 rows), **b/v/d** (b78/d78, b114/v114 x3, b211/v211 — 5 rows), **c/e** (c25/e25, c7/e7 — 2 rows),
**k/t/r** (k10/t10 x2, r41/t41 x2 — 4 rows), **L/n/h** (L77/n77, L77/h27 — 2 rows), **i/y** (i100/y100), plus a
scatter of single-digit swaps consistent with this scribe's numeral shapes (p373/p363, m110/m100, m109/m104,
m172/m162, n95/n97, p153/p353 — 7/3, 1/0, 9/4, 7/6, 5/7, 1/3 confusions). None of these is settled here — per
rule 3/CLAUDE.md discipline on reproducibility, a next pass with a tighter per-token crop budget should check
each row against both images before treating any as a real copying variant rather than a transcription
uncertainty on one side or the other. Two rows land on marks, not ordinary tokens: `f136r` line 17 idx 6 and
`f136v` line 4 idx 13 are a visibly cancelled/scratched mark on the page (recorded as `X7`, doubt=1); Bourdeau's
own file independently flags the *same* two spots as uncertain (`[m?]` at the first, a bracketed `[c291 z9
c170]` at the second) — both transcribers stumbled on the same manuscript trouble spots, which is itself a
small corroboration that both are reading the real page and not each other.

**f136 is a partial copy, not a complete one.** Our 749 tokens end (compare_f9.tsv) at witness index ~752 of
1009 (c017 499 + c018 510) — i.e. f136r+f136v covers all of f.9r and roughly the first half of f.9v, then the
ink simply stops (`images/fr20506_f136v.jpg` bottom third is blank, eye-checked, not a cropping artefact). The
letter Ranzo sent (fr.2988 f.9-10, ~1009 groups incl. f.10r-v not touched here) runs longer than what this
particular copy transcribes. Whether the rest of the copy is lost, was never made, or sits on an unindexed
neighbouring leaf of fr.20506 is not established here (out of scope — a one-line suggestion, not run: check
fr.20506's neighbouring canvases for a continuation before assuming the copy is deliberately partial).

**Attribution.** Second-witness comparison rests entirely on Daniel Bourdeau's `dbourdeau/cyphersolver`
(`vasto1527/n20/ranzo_c017.txt`, `ranzo_c018.txt`, MIT code / CC BY 4.0 text) and his own identification of the
Garbino/Ranzo code's structure (`vasto1527/NOTES.md` "No. 20 / the Garbino–Ranzo code"). No decipherment,
key-recovery or novelty claim is made here.

Requests this pass: github.com 1 (shallow clone `dbourdeau/cyphersolver`, depth 1, grepped for `vasto1527/`,
not committed). No other hosts.
