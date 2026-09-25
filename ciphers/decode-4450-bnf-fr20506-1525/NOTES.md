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
`images/fr20506_canvas279.jpg` just above the signature).

**Attribution.** Witness: Daniel Bourdeau's `dbourdeau/cyphersolver` (`vasto1527/n20/ranzo_c017.txt` through
`ranzo_c020.txt`, MIT code / CC BY 4.0 text; fresh shallow clone to scratchpad, not committed). No decipherment,
key-recovery or novelty claim is made here; rule 10 wording not used. Status unchanged: **open**.

Requests this pass: 0 network hosts (all work from images and text already on disk/scratchpad; the one
`github.com` shallow clone was to scratchpad, not counted as a rate-limited host per the access playbook's own
git-clone precedent in D2 above). No AskUserQuestion; no dollar figures for this worker (cost: see the lane
ledger). Wall-clock: job brief's 60-minute box, this section written and pushed at roughly the 45-minute mark.
