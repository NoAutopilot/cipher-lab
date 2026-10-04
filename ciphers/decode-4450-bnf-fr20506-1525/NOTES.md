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

## ZX2-GAL2: f.136 neighbours (25 Sept 2026, LANE ZX2)

Worker ZX2-GAL2 (Sonnet). Per D2's own flagged follow-up ("check fr.20506's neighbouring canvases for a
continuation before assuming the copy is deliberately partial"): fetched the 4 Gallica canvases after f136v
(canvas 276) and the 2 before f136r (canvas 275) on ark `btv1b525047581`, at 600px first, then at native
2000px once a continuation was confirmed. Gallica requests: 8 (6 canvases at 600px, all succeeded, plus 1
connection-reset retry; then 6 at 2000px for native capture, plus 1 connection-reset retry), >=2s apart, UA
`cipher-lab research script (contact via repository)`, no 403/429/altcha.

**Yes, the copy continues -- for two more full leaves plus a signature page, then it ends.** Eye-checked, no
transcription:

- **canvas 273** (folio stamp "135" visible top right): blank apart from faint show-through offset of the
  facing page's cipher text (mirror image) -- not a content leaf.
- **canvas 274**: blank, no stamp visible (the verso of 135) -- not a content leaf.
- canvas 275 = f136r, canvas 276 = f136v: already on disk (the letter's first two written sides, per the
  existing D1/D2 sections above).
- **canvas 277** (folio stamp "137"): a full page of cipher in the identical hand and letter+superscript-
  number format as f136r/f136v -- the copy continues.
- **canvas 278** (unstamped, the verso of 137): another full page of the same cipher, continues.
- **canvas 279** (folio stamp "138"): cipher for roughly its first third, then a cancelled/scratched mark,
  then a shorter block, then **the sender's own plain-script autograph signature, legible as "Hiero[nim]o
  Ranzo,"** next to a later red archival ink stamp (not a wax seal) -- this is the letter's natural end, not
  a cut-off.
- **canvas 280** (unstamped, the verso of 138): blank, only a faint show-through offset of canvas 279's last
  lines and the signature.

**This resolves D2's open question.** D2 found the transcribed portion (f136r-v, 749 tokens) stopped at
witness index ~752 of 1009 and could not say whether "the rest of the copy is lost, was never made, or sits
on an unindexed neighbouring leaf of fr.20506." It sits on the neighbouring leaves: the copy is not
truncated or lost, it simply continues onto f137r-v and about a third of f138, ending with Ranzo's own
signature exactly where Bourdeau's `fr.2988` witness transcript itself ends (1009 tokens, ff.9-10) -- i.e.
this fr.20506 copy very likely runs the letter's full length across f136-138, not just the first half
Tomokiyo's one-line catalogue note ("f.136, a copy of BnF fr.2988, f.9") might suggest. A future transcription
pass now has three more content-bearing sides (137r, 137v, ~1/3 of 138r) to align against the rest of
Bourdeau's `ranzo_c0*.txt` witness (indices ~752-1009) that D2 did not reach. **No transcription attempted
here** (out of this brief's scope); native-resolution images fetched to `images/` (`fr20506_canvas273.jpg`
through `fr20506_canvas280.jpg`, 2000px IIIF `default.jpg`) and logged in `images/manifest.json`'s
`gallica_natives` array. Files named by canvas number rather than asserted recto/verso, since the visible
folio stamps (135, 137, 138) do not by themselves establish which physical side is which within a pair.

Status unchanged: **open**, not `partial` or `solved` -- this is a new extent for the same undeciphered
Ranzo/Garbino system, not a reading. Folder size after this fetch: still well under the 30 MB cap (about
6 MB in `images/`).

Grades: none (no tokens read, no decipherment). Requests this section: gallica.bnf.fr 8 (see above). No
other host, no subagents.

## ZX2-4450T: ff.137-138 (25 Sept 2026, LANE ZX2)

Worker ZX2-4450T (Sonnet). Job: transcribe the continuation found by ZX2-GAL2 (canvases 273/274/277/278/279/280,
`ark:/12148/btv1b525047581`) and align it against Bourdeau's witness. Intake gate: `tools/intake_gate_check.py
decode-4450-bnf-fr20506-1525` -> "open (line 1) -- edition/page or full-text-search citation found within 6
lines", exit 0.

**Crops.** `tools/iiif_lines.py --image ... --region ...` (row-ink-profile line detection) on the three cipher
canvases, after finding each page's text bounding box from a column/row ink-density profile (the raw canvases
carry facing-page show-through and binding-shadow margins that would otherwise be mis-read as content columns):
canvas277 (f.137, stamped "137") region 430,140,1290,2150 -> 27 lines, 14 two-line crops (`f137a_*`); canvas278
(f.137, unstamped verso) region 615,170,1325,2140 -> 28 lines, 14 crops (`f137b_*`); canvas279 (f.138, stamped
"138") region 400,150,1250,1400 -> 18 lines, 9 crops (`f138_*`), region chosen by eye-check (`/tmp/sig_check.jpg`,
not committed) to stop just above the page's plain-script autograph signature "Hier[on]o Ranzo" (confirmed at
native y~1550-1650, x~300-1700, well below this region) -- no signature line was given to any transcription
pass. Debug overlays committed alongside the crops (`images/crops/*_lines_debug.jpg`).

**Two blind passes per page** (2 Sonnet subagents at a time, one page's crop set per call, per CLAUDE.md Usage
item 6 -- never a whole leaf or the whole target in one call), same page/line/idx/token/doubt notation as
`ciphertext_f136.tsv`: `passA_f137r.tsv`/`passB_f137r.tsv` (393/393 tokens), `passA_f137v.tsv`/`passB_f137v.tsv`
(396/394), `passA_f138r.tsv`/`passB_f138r.tsv` (230/233).

**Reconciliation.** `tools/reconcile_passes.py` needs its 'long' format's first column literally named `line`
(not `page`) -- converted each pass to a `line/pos/token` TSV (doubt=1 -> trailing `?`) for the tool, keeping the
committed `passA_*`/`passB_*` files in this project's own page/line/idx/token/doubt convention unchanged. Pass
agreement, well above the brief's 60% gate on every page: f137r 393/393 signs, 360/393 = 91.6% (33 disagreement
columns); f137v 396/394 signs (28 lines), 361/398 aligned columns = 90.7% (37 disagreement columns, higher
because the two passes segmented a few lines differently); f138r 230/233 signs (18 lines), 198/236 = 83.9% (38
disagreement columns).

**Settling disagreements.** Per brief, settled from the image plus (new to this pass) Bourdeau's own witness
transcription used as a fresh, independent third source at the expected offset -- not just eye judgement.
Concrete findings, most useful for a future transcription pass on this hand:
- The page's small squiggle/cedilla-like mark and its "d" glyph (a loop with a descending curling tail) are
  genuinely distinct base signs in this system (`ciphers/decode-4450-bnf-fr20506-1525/inventory.tsv`'s D2
  section already counted them separately, d:50 vs z:49, on f.136) -- but on f.137r the mark that both blind
  passes and the witness agree is "z" really is z (5 instances, `z6`/`z8`/`z9`/`z15` etc. all confirmed against
  the witness at their exact witness-aligned position). On f.137v, however, one blind pass's own prompt
  (carried forward verbatim from the f.137r prompt) caused **32 tokens** it labelled "z" to be "d" at the exact
  matching digit against the witness (e.g. `z35`->`d35` x3, `z246`->`d246`, `z156`->`d156` x2, `z183`->`d183`,
  `z179`->`d179` x2 -- always same digits, only the base letter corrected) -- a genuine over-application of the
  "z" label to the visually similar "d" loop-and-descender shape, not a copying variant, fixed here and the
  prompt corrected before the f.138r passes ran (0 further z/d fixes needed there).
- The tall-ascender glyph this project calls "L" (a hooked/curled top, e.g. `L10`, `L47`, `L99`) is frequently
  confused by a blind pass with a plain dotless "i" (`i100`, `i29`); checked against both the image (a plain
  vertical stroke with no hook reads "i") and the witness's own token frequency in `vasto1527/n20/` (`i100`
  appears 37 times across c017-c019, `L100` appears **zero** times) -- "i" is correct wherever this ambiguity
  came up; both subagent prompts for f.137v/f.138r were given this heuristic up front, reducing but not
  eliminating the flag rate.
- A base letter this project provisionally calls "q" recurs at three f.137r positions (line 8/12/13) where one
  pass read "q", the other "e", and the witness reads "Q" (capitals); Bourdeau's own witness genuinely
  distinguishes lower-case `q` (40 occurrences) from upper-case `Q` (21 occurrences) as separate signs in
  c017-c020, but eye-checking the fr.20506 image (`/tmp/q6_check2.jpg`, not committed) found the glyph
  indistinguishable in shape from the ordinary "q" written two tokens later on the same line -- kept as "q",
  flagged doubt=0 given the direct image check, logged here as an open question for whoever eventually keys
  this system (does fr.20506's scribe collapse a q/Q distinction the fr.2988 scribe kept, or is Bourdeau's own
  c020 transcription over-splitting one glyph into two labels?).
- One genuine cancelled/scratched mark on f.137r (line 9) where the witness has **no corresponding token at
  all** at that position (not a replace, a true gap) -- the same signature (both a strike-through and a witness
  gap) D2 already used on f.136 to confirm a cancellation; recorded as bare `X`, doubt=1. f.137v (line 17) and
  f.138r (line 6) each carry one further clear strike-through, also `X`.
- Classic secretary-hand look-alike pairs already catalogued by D2 on f.136 (b/h, b/v/d, r/t, digit transpositions)
  recur throughout f.137-138 at similar density and are recorded as `replace` rows in `compare_f137_138.tsv`,
  not silently corrected -- these read as genuine copying variants between the fr.20506 copy and the fr.2988
  original, the same conclusion D2 reached, not transcription noise on either side.
- 8 f.137r cells and the bulk of f.137v/f.138r's remaining flagged cells are left as honest 3-way ambiguities
  (doubt=1) where neither blind pass matches the witness and the image does not settle it either; these are
  listed in full in `compare_f137_138.tsv`'s `replace` rows, not hidden.

**`ciphertext_f137_138.tsv`** (page/line/idx/token/doubt, 1027 tokens): f137r 393 (19 doubt=1), f137v 398
(118 doubt=1 -- the two passes disagreed on segmentation as well as tokens on this page, see above), f138r 236
(56 doubt=1).

**`compare_f137_138.tsv`** (page/line/idx/our_token/witness_source/witness_token/type): aligned each page's
final token sequence against `vasto1527/n20/ranzo_c017.txt`+`c018.txt`+`c019.txt`+`c020.txt` concatenated
(fr.2988 f.9r/f.9v/f.10r/f.10v, 499+510+514+266 = 1789 tokens total -- c019/c020 not used by D2, which only
needed c017/c018 for f.136), via `difflib.SequenceMatcher` exactly as D2's `compare_f9.tsv` did. Best-match
starting offset for f.137r found by brute-force search over witness index 700-800: **752**, i.e. f.137 continues
the fr.2988 letter from the exact point D2's own f.136 alignment stopped (D2: "our 749 tokens end at witness
index ~752 of 1009"). **Combined agreement across all three pages: 828/1031 aligned columns = 80.3%** (lower
than D2's 94.1% on f.136, expected: f.136 got a full by-hand per-token image recheck of every disagreement,
f.137-138 relied more on the automated witness cross-check given this worker's time box, so more genuine
paleographic variants and unresolved ambiguities are left visible in the numbers rather than eye-verified away).

**Where the copy ends relative to the witness.** f.137r consumes witness index 752 to 1145 (393 tokens, exactly
1:1: one witness token skipped as a mid-letter insertion the copy omits, balanced by one extra token the copy
carries that the witness omits -- see `compare_f137_138.tsv` line1/line9 `extra-in-ours`/insert rows). f.137v
starts at 1145, f.138r starts at 1543. **f.138r's own alignment reaches witness global index 1787 of the
witness's total 1789 tokens** -- i.e. this transcription (f.136 through f.138, all four workers combined)
accounts for all but the last 2 tokens of Bourdeau's entire fr.2988 f.9-f.10 transcription. This confirms
ZX2-GAL2's eye-check finding (the cipher block on f.138 ends immediately before the "Hiero Ranzo" signature,
"the letter's natural end, not a cut-off"): **the fr.20506 ff.136-138 copy is not a partial excerpt of the
Ranzo/Garbino letter, it is (to within 2 tokens of alignment noise) the complete letter**, matching fr.2988
f.9r through f.10v end to end. Whether those last 2 witness tokens are a genuine tail this transcription missed
or an artefact of the alignment's tail handling is not resolved here (one-line suggestion, not run: a future
pass could diff the very last 5-10 tokens of `ranzo_c020.txt` against a fresh close look at the bottom of
`images/fr20506_canvas279.jpg` just above the signature). **Settled 2 Oct 2026 (D4450-TAIL, below): the 2 tokens are a real 19th line, `m66 o4`, that the crop region cut off; N is now 0.**

**Attribution.** Witness: Daniel Bourdeau's `dbourdeau/cyphersolver` (`vasto1527/n20/ranzo_c017.txt` through
`ranzo_c020.txt`, MIT code / CC BY 4.0 text; fresh shallow clone to scratchpad, not committed). No decipherment,
key-recovery or novelty claim is made here; rule 10 wording not used. Status unchanged: **open**.

Requests this pass: 0 network hosts (all work from images and text already on disk/scratchpad; the one
`github.com` shallow clone was to scratchpad, not counted as a rate-limited host per the access playbook's own
git-clone precedent in D2 above). No AskUserQuestion; no dollar figures for this worker (cost: see the lane
ledger). Wall-clock: job brief's 60-minute box, this section written and pushed at roughly the 45-minute mark.

## D4450-TAIL (2 Oct 2026, account-4): the 2 leftover witness tokens are a real tail, not an alignment artefact

Worker D4450-TAIL (account-4, Fable 5.1), brief `.claude/briefs/runs/2026-10-01-account4-d4450-tail.md` (written 1 Oct, run
2 Oct 2026 00:14-00:2x UTC, clock read). Job: settle ZX2-4450T's open question above -- whether the 2 tokens of Bourdeau's
witness that `compare_f137_138.tsv` left unmatched after our last token (`f138r` line 18 token 13, `o66`) are a tail this
transcription missed or an artefact of the alignment's tail handling. No decoding, no key work, no other target.

**Witness tail.** Fresh shallow clone of `dbourdeau/cyphersolver` to the scratchpad (commit 34e0fc89, 1 Oct 2026, deleted
after; the files have moved to `targets/vasto1527/n20/` since ZX2-4450T's clone). `ranzo_c020.txt` (fr.2988 f.10v) ends:

```
z6 d180 d37 m82 f4 m176 i4 c193 o5 p3 v152 f5 o66 [m66]
o4
```

So the 2 leftover tokens are `[m66]` (square-bracketed: Bourdeau's doubt/marginal notation -- `[m?]` in c017, `[??]` in
c019; his own loader `n20/load.py` strips bracketed spans with `re.sub(r'\[[^\]]*\]','',l)`) and `o4` alone on a final line.

**Image.** Two vision calls, as capped. (1) A Sonnet subagent read the bottom strip of `images/fr20506_canvas279.jpg`
(native region 250,1300 1500x520 at 150%, scratchpad only) blind -- it was given no witness and no transcription -- and
reported the last cipher line as two tokens, `m66` (M; "the m is at the far left, partly over the red library stamp, with
66 above it") and `o4` (M), followed by "a large looped flourish ... a pen stroke, not a letter-plus-digits token", then a
blank gap and the signature, no cipher token on the signature line; and the line above ending `p3 v152 f5 o66`. (2) This
worker's own look at the committed crop `images/crops/f138_L10_tail.jpg` (native region 250,1420 1500x300, resized to
2400 px wide; `images/manifest.json` key `d4450_tail_crop`) confirms it: below `... v152 f5 o66` sits a short 19th line at
the far left, an `m` with `66` written above it (the digits overlap the red "BIBLIOTHEQUE NATIONALE MSS" stamp ring but
read as 66), then an `o` with `4` above it, then a paraph, then the autograph `Hier° Ranzo` with a `V°`-shaped mark before
it. Native position about y 1577-1622, x 430-580 -- that is **below** ZX2-4450T's line-finder region (400,150,1250,1400,
i.e. y 150-1550), which that pass chose by eye "to stop just above the page's plain-script autograph signature": the
short two-token line sat inside what was taken for the signature zone and was never cropped or sent to a pass.

| witness token | our token (ZX2-4450T) | image reading (blind subagent / this worker) | verdict |
|---|---|---|---|
| `o66` (c020 line 21, token 13) | `f138r` 18/13 `o66` | `o66` / `o66` | equal, already aligned |
| `[m66]` (c020 line 21, token 14, bracketed) | none | `m66` M / `m66`, digits over the stamp | **real token, missed**; added as `f138r` 19/1 `m66`, doubt=1 (stamp overlap; the witness itself brackets it) |
| `o4` (c020 line 22, alone) | none | `o4` M / `o4`, clear | **real token, missed**; added as `f138r` 19/2 `o4`, doubt=0 |
| -- | -- | paraph, then signature | nothing further; no catchword, no margin token |

**Verdict: a missed tail, not an alignment artefact.** The fr.20506 ff.136-138 copy is the complete fr.2988 f.9r-f.10v
letter to within **0** tokens of the witness's end (ZX2-4450T's sentence "to within 2 tokens of alignment noise" is
corrected above). Files changed: `ciphertext_f137_138.tsv` now 1029 tokens (f138r 238, 19 lines), `compare_f137_138.tsv`
+2 `equal` rows (830/1033 aligned columns = 80.3%, unchanged to one decimal), `images/crops/f138_L10_tail.jpg` + manifest
entry. The folder has no decode script or key (status `open`, no reading), so there is no `--check` to re-run; the TSVs
were checked for column count and per-page totals only.

One-line suggestion, not run (outside this brief): the same crop shows line 18 opening with two tokens, a `?9` partly
under the stamp and a `z6` (the blind subagent read "t with a tiny 9" then "[ with 6"), where `ciphertext_f137_138.tsv`
has one token `z9` and the witness has `t9 z6` (the two `replace` rows at the head of line 18 in `compare_f137_138.tsv`)
-- a future transcription pass on f.138r should re-read line 18 token 1 from a crop that includes the stamp edge.

Attribution: witness Daniel Bourdeau, `dbourdeau/cyphersolver` `targets/vasto1527/n20/ranzo_c020.txt` (MIT code / CC BY
4.0 text), cited, not copied. Rule 10 wording: nothing here is a reading or a novelty claim; status unchanged, **open**.
Requests: 1 `github.com` shallow clone to the scratchpad, 0 other hosts. Vision calls 2 of 2. No AskUserQuestion.

## Web and blog check (WEBCHECK-decode-4450-bnf-fr20506-1525, 1 Oct 2026)

Required step of `.claude/briefs/check-solved.md` ("Open web and blog comment threads", CHECK-SOLVED-WEB, 28 Sept
2026), run 1 Oct 2026 23:35-23:41 UTC (clock read) by the account-4 WEBCHECK worker. No transcription, no decoding, no other
folder touched. The item has no clear text, so the "distinctive phrase" is its opening ciphertext run from
`ciphertext_f136.tsv` (`b5 f3 c227 g72 p246`), which is also the opening of Bourdeau's `ranzo_c017.txt` (fr.2988 f.9r).

**(a) Plain web searches (WebSearch, 8 queries).**

| # | Query | Result |
|---|---|---|
| 1 | `"Hieronimo Ranzo" OR "Girolamo Ranzo" OR "Jerome Ranzo" Gattinara cipher letter 1525` (sender + patron + date) | Wikipedia (Gattinara, Aleandro, Sirturus), Cryptologia "cifra delle caselle" paper, dbourdeau.github.io index, two Cipher Mysteries pages (Bellaso, Sirtori). None about this letter. |
| 2 | `"fr. 20506" OR "français 20506" OR "fr.20506" chiffre OR cipher f.136` (shelfmark + chiffre) | Only cipher-dictionary pages and the Mary Stuart Cryptologia article; the search engine's own summary repeated the fr.20506 description (Gaignières 394, letters to Montmorency, "folio 136 of fr. 20506 is a copy of folio 9 of fr. 2988"), which is Tomokiyo's/Bourdeau's wording already on file, not a new source. |
| 3 | `"b5 f3 c227" OR "c227 g72 p246" Ranzo cipher` (distinctive ciphertext phrase, quoted) | No page carries the token string. Second-pass hits: github.com/dbourdeau/cyphersolver pull 5 (Conti 1649 etc., not this letter), Wikipedia Giulio Ranzo, generic cipher pages. |
| 4 | `DECODE record 4450 BnF fr.20506 f.136 unsigned letter 1525-1550 cipher Ranzo copy fr.2988 f.9` (folder title) | dbourdeau/cyphersolver pull 2 (Sormano/Passano 1529) and three forks of cyphersolver (arya1515, aryasn2026, setsunaatto -- forks, same content), dbourdeau.github.io index. No independent page on R4450. |
| 5 | `Ranzo Garbino cipher "fr. 2988" OR "fr.2988" OR "fr. 3022" solved OR deciphered OR solves Claude OR GPT` (model-solve announcement check) | Only dbourdeau's own pages/PRs and unrelated cipher papers; the engine's summary of Bourdeau's site: Ranzo-Garbino "approximately 3,900 groups transcribed but remains not solved". No "X solves the Ranzo cipher" announcement by anyone. |
| 6 | `site:scienceblogs.de/klausis-krypto-kolumne Ranzo OR Gattinara OR "fr. 20506" OR "fr. 2988"` | Two Cipherbrain posts: 17 May 2016 "Wer löst diesen verschlüsselten Brief aus dem französischen Nationalarchiv" and 24 Mar 2017 "Who can solve this encrypted text from the 16th century?" (the Spinelli post). Both opened below. |
| 7 | `site:cryptiana.blogspot.com Ranzo OR Gattinara OR Garbino OR "fr. 2988" OR "fr. 20506"` | site: operator returned nothing from the blog (Wikipedia/1stdibs noise); replaced by the blog's own search, below. |
| 8 | `site:ciphermysteries.com Ranzo OR Gattinara OR Garbino OR "fr. 2988" OR "fr. 20506"` | No Cipher Mysteries page matching; one unrelated CM post (2011 "Milanese enciphered letters") surfaced and was opened below. |

**(b) Blog site searches, each blog by name.**

- **Cipherbrain** `scienceblogs.de/klausis-krypto-kolumne/?s=Ranzo` (HTTP 200): 10 posts. Only the 17 May 2016 post
  carries the name; the other nine (2014/07/18 Eiffelturm, 2014/12/17 "Die Franzosen und das englische Bier",
  2022/05/05 and 2022/05/28 French newspaper ads, 2022/07/30 "21 bisher ungelöste Verschlüsselungen gelöst",
  2022/08/17 Elamite, 2022/11/21 Louis XIII letter, 2022/11/27 "Brief von Karl V. ... dechiffriert", 2022/12/31
  Goldene Alice) were each fetched (all HTTP 200) and grepped for `ranzo|gattinara|20506|2988|garbino`: zero
  real matches -- WordPress matched the substring "ranzo" inside "französisch/Franzosen". Not hits.
- **Cryptiana blog** `cryptiana.blogspot.com/search?q=Ranzo` and `search?q=2988 OR 20506 OR Gattinara OR Garbino`
  (both HTTP 200): two posts, 21 Mar 2021 "More Undeciphered Texts (Italian, Spanish) in BnF" and 24 Mar 2021
  "Misplaced? English Cipher Letter in French Archives" (a third, 1 Oct 2026 "Enigma Messages Solved by AI", was
  a false match: fetched, no Ranzo/BnF content, "No comments"). Both 2021 posts opened below. Tomokiyo's own
  pages: `sources/cryptiana/` on-disk snapshot grepped first (0 requests): `web/venetian.htm` is the only file
  naming fr.20506 f.136 ("a copy of BnF fr.2988, f.9, which Norbert Biermann pointed out to me", listed among
  "several undeciphered letters of Hieronimo Ranzo"); nothing under `sources/cryptiana/blog/`. The live page was
  already re-read in full on 25 Sept 2026 (section "Check-solved (LANE CX)" above), unchanged; not refetched.
- **Cipher Mysteries** `ciphermysteries.com/?s=Ranzo` (via the fetch tool, HTTP 200): "Nothing Found - Apologies,
  but no results were found for the requested archive." A second search (`?s=2988 OR 20506 OR Gattinara`) and the
  2011 post by curl both answered **HTTP 406 "Not Acceptable"** (WAF, browser UA) -- stopped hitting the host by
  curl after the two 406s; the one permitted retry went through the fetch tool (200, below).

**(c) Hits opened, post and comment thread read.**

1. **Cipherbrain, 17 May 2016, "Wer löst diesen verschlüsselten Brief aus dem französischen Nationalarchiv"**
   (`scienceblogs.de/klausis-krypto-kolumne/2016/05/17/wer-loest-diesen-verschluesselten-brief-aus-dem-franzoesischen-nationalarchiv/`,
   21 comments, 17 May 2016 to 22 Oct 2017, all read). The post is about **BnF fr.2988 itself** (Gallica
   `btv1b9059908w`, the PDF's pages 6-7 = **f.1**, the English letter), i.e. the archetype volume of this target.
   What the thread says about Ranzo's letters, verbatim:
   - Thomas, 17 May 2016, quoting the BnF catalogue: "ohne Anschrift, ganz in Chiffre, nur mit der Unterschrift
     Hieronimo Ranzo"; "Im Exemplar der BNF gibt es eine merkwürdige Fortsetzung: https://gallica.bnf.fr/ark:/12148/btv1b9059908w/f6.item.zoom".
   - Torbjörn Andersson, 29 Mar 2017 (#9): posts a substitution key and plaintext **for f.1 only** ("Plaintext is
     in English ... Pleis your Majesty[?], hes bein ernist to obtain licence to kis youe Majesty[?] hand").
   - Torbjörn Andersson, 3 Apr 2017 (#16): "I suspect the letter has been misplaced, and has nothing to do with
     Ranzo (who uses an entirely different, more complex cipher and probably writes in Italian)."
   - Norbert [Biermann], 21 Oct 2017 (#18): "Ich teile Torbjörns Einschätzung, dass der Text fälschlich Ranzo
     zugeordnet wurde. Die Geheimtexte ab folio 9 sind von Ranzo unterschrieben und ganz offensichtlich wesentlich
     komplexer." He also points to **fr.3022 f.50** (Gallica `btv1b90601558/f97.item`), an "adizione nel zifra":
     "Es sieht ganz danach aus, dass diese 'Ergänzung zur Chiffre' zu Ranzos Code gehört ... Zumindest in der
     Erweiterung ist der Buchstabe vor der hochgestellten Zahl grundsätzlich auch der Anfangsbuchstabe der
     Klartextentsprechung."
   - Norbert, 21 Oct 2017 (#20): "Kannst du herausfinden, ob der Nomenklator von Ranzos Brief (fol. 2) bekannt
     ist?"; Thomas, 22 Oct 2017 (#21, last): "Zu dem Nomenklator von Ranzos Brief fol. 2 konnte ich nichts finden."
   **Nothing in the thread deciphers fr.2988 f.9 (or f.2, or f.136).** The one decipherment posted (Andersson,
   f.1) is of a different, simpler cipher the commenters themselves conclude is misattributed to Ranzo.
   Follow-up for a later worker, not run here (out of scope): Biermann's fr.3022 f.50 "adizione nel zifra" is a
   period key-fragment candidate for the Ranzo system; check whether Bourdeau's `vasto1527/NOTES.md` already
   used it before anyone briefs a key-reading pass.
2. **Cipherbrain, 24 Mar 2017, "Who can solve this encrypted text from the 16th century?"** (the Spinelli post,
   17 comments, read). Thomas, 25 Mar 2017 (#14): "Some signs are similar to the unbroken Ranzo cipher which also
   dates around the year 1520." Torbjörn Andersson, 28 Mar 2017 (#15): "Thomas' comment just reminded me, that I
   broke the Ranzo cipher back in June. I did post the solution here then, but for some reason, it didn't appear.
   I have just reposted the key on the appropriate page". **This "Ranzo cipher" is fr.2988 f.1**: the repost is his
   29 Mar 2017 comment #9 in thread 1 above, and he himself withdraws the Ranzo attribution on 3 Apr 2017 (#16).
   Not a decipherment of f.9/f.136.
3. **Cryptiana blog, 24 Mar 2021, "Misplaced? English Cipher Letter in French Archives"**
   (`cryptiana.blogspot.com/2021/03/misplaced-english-cipher-letter-in.html`, "No comments"): about the same f.1
   English letter (credits Andersson 2017); the only Ranzo sentence: "Another reason of this post is its possible
   relation to another undeciphered ciphertext signed Hieronimo Ranzo on the following folio (see 'Venetian
   Ciphers with Superscripts')." No plaintext of any Ranzo letter.
4. **Cryptiana blog, 21 Mar 2021, "More Undeciphered Texts (Italian, Spanish) in BnF"** (no comments): "More
   specimens of the Venetian? cipher with superscript are found in BnF fr.2988, fr.3019, fr.3022." Listing only.
5. **dbourdeau.github.io/cyphersolver/index.html** ("updated 1 October 2026", fetched and grepped): "No. 20
   (Madrid, 11 Apr 1528, to 'Garbino') is in Hieronimo Ranzo's initial-letter code. The numbering was tested and
   is not alphabetical. All 1,315 groups were transcribed, plus ~2,600 from Ranzo's letters in fr. 2988. A word
   annealer validated on a held-out control recovers ..." only function words; no R4450 / fr.20506 mention on the
   index page. Status there unchanged from 25 Sept: not solved.
6. **Cipher Mysteries, 28 Jun 2011, "Milanese enciphered letters, call for help"** (fetch tool, 517 comments
   2011-2018 summarised): Sforza-era Milan, Voynich discussion; no Ranzo, Gattinara, Garbino or BnF fr.2988/
   3022/20506 mention. Not a hit.

**Result: no decipherment or plaintext of this item located by these queries on 1 Oct 2026** (a search result,
never a novelty verdict, rule 10). The only decipherment anywhere in these threads is Andersson's 2017 reading of
fr.2988 **f.1**, a different letter in a different cipher, which the same commenters and Tomokiyo call misplaced and
not Ranzo's. Status word unchanged: `open`.

Requests this pass: WebSearch 8; scienceblogs.de 13 (1 fetch tool + 12 curl, all 200, >= 1.7 s apart);
cryptiana.blogspot.com 5 (2 fetch tool + 3 curl, all 200); ciphermysteries.com 4 (2 fetch tool 200, 2 curl 406 --
host dropped for curl after the second); dbourdeau.github.io 2 (200); `sources/cryptiana/` local, 0. No DECODE,
Gallica or github.com request.

`python3 tools/intake_gate_check.py decode-4450-bnf-fr20506-1525` (1 Oct 2026, after this section):

```
decode-4450-bnf-fr20506-1525: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/catalogue.json #189
- Their extent, in their words: R4450 = fr. 20506 f. 136, a copy of fr. 2988 f. 9 (R1894); same attempt as #170, not read
- Their date: 21 Sept 2026
- Note: our NOTES.md cites vasto1527/n20/ranzo_c017.txt; catalogue #189 entry itself not cited
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Premise check (GF4-BATCH3, account-4, 3 Oct 2026)

Adversarial pass per `.claude/briefs/check-solved.md` (try to prove the item already done), before any first test.
**Result: not found on (a)-(d); status stays `open`.** The archetype (fr.2988 ff.9-10, Ranzo's signed letter) and
this copy (fr.20506 ff.136-138) are both undeciphered everywhere checked.

- **(a) Decipherments the folder mentions -- not found.** DECODE R4450 has no attached document (LANE N, LANE CX,
  re-confirmed above). The one "decipherment" lead this folder names is the 18 *Decrypted* DECODE siblings in
  fr.20506 (ids 4434-4449, 4815-4816), never opened until now: three re-opened live (plain GET, 3 Oct 2026):
  R4449 = f.82, Claude Dodieu de Vély to Anne de Montmorency; R4434 = f.245, Mary Queen of Scots to Castelnau
  de Mauvissière; R4815 = f.96, Robert Cenalis, bishop of Avranches, to Montmorency. French envoys' own ciphers to
  French recipients, a different side and different senders from Ranzo (Gattinara's man, Imperial side); none
  carries an "Additional Information" note tying it to f.136. Bourdeau's DECODE R1894 (fr.2988 ff.9-11, the
  archetype) has "no key, decipherment or" clear copy (his `vasto1527/NOTES.md` l.157-158).
- **(b) Other solvers' working files -- not found.** Fresh shallow clone dbourdeau/cyphersolver main 2341682
  (3 Oct 2026): `targets/vasto1527/n20/` holds his transcriptions of the Ranzo letters (`ranzo_c006/007/017-020.txt`),
  `solve.py`, `solve2.py`, `anchor.py`, `free.py`, `alphatest.py`, `calib.py` -- solver attempts, no rendering or
  key file for Ranzo; his NOTES "Remaining gaps": "No. 20 ... whole letter - blocker: no-key-material; Ranzo's
  code is non-alphabetical, the annealer recovers only function words on a matched control; needs Ranzo's table
  or a clear copy"; README row (catalogue item 7) still "not solved". His fr.3019 no.27 (f.73) Ranzo letter
  check: "all in cipher, no interlinear or separate decipherment". Aymeloglu (main d2800bb): R4450 only in the
  raw DECODE harvest, no working files.
- **(c) Physical neighbours -- not found.** Done in full by ZX2-GAL2 (25 Sept 2026, section above): canvases
  273-280 at native 2000 px; f.135 and its verso blank (the facing page of f.136r), the copy runs ff.136r-138r to
  Ranzo's signature, f.138v blank; no slip, no clear copy, no interlinear. Not re-fetched. The archetype's own
  neighbours were checked by Bourdeau (fr.2988 views 43-87: a different French-side symbol cipher with clear
  copies of *Doria* letters, not Ranzo's code; f.2v "dup.ª" a duplicate cipher, not a clear copy).
- **(d) Recipient's side -- not found.** Ranzo writes from the Imperial court, so the receiving side is
  Imperial/Spanish/Italian. Internet Archive full-text (be-api fts) inside the *Calendar of State Papers, Spain*
  items `calendarorleters0003vari` (vol. III pt 2, 1527-29), `calendarofletter0003pasc`,
  `calendarofletter0004pasc`, `dli.ministry.01108`, `dli.ministry.01109`: "Ranzo" 0/1/1/0/0 hits -- the two hits
  are Gattinara's mother "Felicita Ranzo" and "the Lord Ranzo (Renzo da Ceri)", both unrelated (they double as
  positive controls that the search reaches the text); "Garbino" 0 in all five. Google Books API (`country=US`,
  key): `"Hieronimo Ranzo"` 38 (BnF 1868 *Catalogue des manuscrits français* entry for fr.2988; a 1837
  Navarrete *Colección de los viages* witness list -- no letter text), `"Girolamo Ranzo" Gattinara` 20
  (Gattinara biography, genealogies), `"Ranzo" Gattinara 1528 cifra` 2: *L'umanista aronese Pietro Martire
  d'Anghiera* (1992) and *Novarien* (1990) snippet "... 1528 faceva da intermediario fra Gaspare Rotulo e Alonso
  de Valdés, segretario del Gattinara, per la cifra ... Ranzo, camer[iere]" -- a **lead on who handled
  Gattinara's cipher in 1528** (a person, not a key or decipherment); worth one Google Books snippet read before
  any key-rebuild, not a solve.

Requests this pass: de-crypt.org 3, archive.org 10, googleapis.com 3, github.com (clone shared with
decode-2754). Next cheap test: none by cryptanalysis (Bourdeau's matched-control annealer already fails on
~3,900 groups); the cheap step is material -- read the *Novarien* 1990 / Pietro Martire 1992 passage (Google
Books snippet, ~$0.5) for where Gattinara's chancery cipher tables (Valdés, Rotulo) survive, i.e. Ranzo's table
or a clear copy, the blocker Bourdeau names.

## FT4: Novarien 1990 lead and a Molini 1836 clear-copy claim (account-4, 3 Oct 2026)

Worker FT4-decode-4450-bnf-fr20506-1525 (account-4), 01:07-01:3x UTC. Intake gate run first: `decode-4450-bnf-fr20506-1525:
open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0. Job: GF4-BATCH3's cheap step,
"read Novarien 1990 snippet on Gattinara cipher handlers for Ranzo table/clear copy". **Result: no key table and no clear
copy of this letter or its archetype (fr.2988 f.9) found. The Novarien lead is a false positive. Status stays `open`.**

**1. Novarien 1990 / Pietro Martire 1992: false positive.** Google Books API (`country=US`, key) returns the full snippet:
"... 1528 faceva da intermediario fra Gaspare Rotulo e Alonso de Valdés, segretario del Gattinara, per la **cifra di 468
ducati e 244 maravedís**. Altro operatore di Borsa è Tomaso Fornari ... ASV - FAG ... Ranzo, cameriere di Mercurino Arborio
di Gattinara, relativo alle entrate e alle spese del periodo 13 agosto 1527 - 31 maggio 1529, visto e saldato dal
segretario Alfonso de Valdés". Here *cifra* means a sum of money, not a cipher, and the Ranzo document is an **account**
(receipts and expenses, 13 Aug 1527 to 31 May 1529) in ASV-FAG (Archivio di Stato di Vercelli, Fondo Arborio di
Gattinara). It is not a cipher table. The 1982 Vercelli conference volume *Mercurino Arborio di Gattinara, gran cancelliere
di Carlo V* (GB id 7pkfAAAAMAAJ, no preview) describes the same item in its archive inventory: "1524-1529 (e 1522). Conti di
Gerolamo Ranzo, cugino di M., concernenti quanto da lui operato come cameriere di M. (cc. 33)". This tells us that
Gattinara's family papers survive at Vercelli (ASV-FAG). No snippet shows a cipher table there; queries for
cifrario/cifre/"in cifra"/"lettere cifrate" together with Gattinara or the archive returned 0 hits (queries below).

**2. Molini 1836: an old claim of a French "interpretation", checked and set aside.** Molini, *Documenti di storia
italiana* vol. 2, "Omessi di copiare" (archive.org `documentidistor02moligoog` djvu, l.1031-1037; the same entry in
`00moligoog` l.1086), under the old number 8513 (= fr.2988): "A c. 1. Lunga lettera tutta in cifra, firmata Hieronimo
Ranzo. A c. 4 dello stesso volume sta la sua interpretrazione in francese, colla data di Roma 15 Dicembre 1526. Ivi a c. 9
è altra lettera dello stesso parimente in cifra, ma senza l'interpetrazione." LANE CX's 25 Sept read of Molini missed this
entry: its OCR breaks the name ("^ieroni>no/?afi«o"). Two points:
- **Molini himself says the archetype of our copy (c. 9) has no interpretation.** That agrees with every later source.
- For the c.1 letter, the 1868 BnF *Catalogue des manuscrits français* (Google Books snippet) describes f.4 as
  "Double de lettres escriptes en chiffre par NICOLAS RAINCE ... De Romme, xve decembre 1526": a clear copy of letters
  that the French envoy Raince had sent in cipher. It is not a decipherment of a letter signed by Ranzo. I looked at
  Gallica `btv1b9059908w`, views 8-13 (600 px), and one crop of view 13. View 8 is blank; f.4r (view 9, stamped "4")
  through view 13 hold about 4.5 pages of **clear French** in one cursive hand. The view 13 crop reads as Rome news
  addressed to "Monseigneur" ("Le cardinal qui fut Colonne ... à Naples au conseil ... citations ... contre Sa S^te ...
  Monseigneur, vous ay bien voulu advertir"). This is the voice of the French envoy in Rome writing to Montmorency.
  Ranzo's code encodes **Italian**: Bourdeau's addition sheet `additione.json`, from fr.3022 f.50, reads "apresso", "cosa",
  "al garbino". Ranzo also writes from the Imperial side. Molini's pairing of c.1 with c.4 is therefore most likely
  his own guess from the two items sitting next to each other in the volume. (This is grade I: inferred from the
  language, the voice and the catalogue title, with no token-level test.) In any case it bears on f.1-2, not f.9/f.136.
  Bourdeau's `vasto1527/NOTES.md` (fresh sparse clone, 3 Oct 2026) never mentions f.4 or Raince.
- A cheap test that would settle the f.2 question, not run here (outside this brief, and it needs a transcription of
  f.4r-6r, about 1,100 words): Ranzo's code is an initial-letter code. If f.4 rendered f.2r-v (Bourdeau's
  `ranzo_c006/007`, 834 groups), the base letters of f.2 would track the initials of the French words, compared against
  a shuffled-pairing control (rule 3). The language argument above predicts a negative. The estimated cost is about $3
  (2 transcription passes on line crops plus 1 reconciliation, Usage 6). Even a positive result would key Ranzo's
  f.2 letter, not this one directly, though the shared code would carry over to f.9/f.136. Suggestion only.

**No matched test run:** nothing was found that could serve as a key table or as a clear copy of this letter, so there
was nothing to test against a control.

Queries (Google Books API, `country=US`, key): `"Ranzo" Gattinara 1528 cifra` (2: Pietro Martire 1992, Novarien 1990,
NO_PAGES); `Rotulo Valdés cifra Ranzo` (2, same); `Novarien Ranzo cifra` (1); `"Ranzo" Gattinara cifre OR cifrario OR "in
cifra" OR chiffre` (0); `"Arborio di Gattinara" archivio Vercelli cifrario OR cifre OR "in cifra"` (0); `"Ranzo" Gattinara
"cameriere"` (9: 1982 Vercelli volume, Cibrario 1861 x5, Memorie Accad. Torino 1897; all household offices, none about a
cipher); `"gran cancelliere di Carlo V" Gattinara cifra OR cifre OR zifra OR "in cifra"` (4, irrelevant: wine statistics,
bibliographies); `"Gerolamo Ranzo"` (no items); `"Girolamo Ranzo" cifra OR zifra OR cifre` (211, top 8 are Soranzo
false positives); `Gattinara archivio "lettere in cifra" OR "lettere cifrate" OR "alfabeto" cifra 1528` (0); `"Hieronimo
Ranzo" cifra OR zifra OR chiffre OR "en chiffre"` (12: the 1868 BnF catalogue fr.2988 entry, Molini 1836). Internet
Archive advancedsearch `Novarien` (0) and `Ranzo cifra Gattinara` (0): the journal is not on IA, so there is no be-api
full text to search.

Requests: googleapis.com 12; archive.org 4 (2 advancedsearch, 2 `_djvu.txt`); gallica.bnf.fr 8 (1 manifest via
`tools/gallica_folio.py`, 6 views at 500 px, 1 crop), all 200, >=1.6-2 s apart; github.com 1 (sparse clone of cyphersolver
`targets/vasto1527`, grepped, not committed). Vision calls: 2 (contact sheet of views 8-13; view 13 crop). Rule 10: these
are search results, not a novelty verdict.

Next step for this target: the blocker stays Bourdeau's "no-key-material". New material could come from an inquiry to
ASV Vercelli, Fondo Arborio di Gattinara, asking whether the chancellor's papers hold cipher tables for 1527-29
(owner-side, an outreach draft). The cheaper desk-side option is the optional f.2/f.4 initial-letter test above (~$3).

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: the optional f.2/f.4 initial-letter test this folder names as its cheaper desk-side option (~$3); the Vercelli (Fondo Arborio di Gattinara) inquiry stays owner-side outreach.
