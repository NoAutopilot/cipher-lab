# TXP-SCOUT2 results: Birago 1572 leaves with a period decipherment witness (9 Oct 2026, 19:13-19:2x UTC by date -u)

LANE TX-ENGINEER-2 incarnation 2, PREREG `benchmark-tx/PREREG-txeng2-6.md` section SC1 (binding), brief
`.claude/briefs/runs/2026-10-09-account4-txe2-round6.md` row TXP-SCOUT2. Read-free scout of what is already on disk:
`ciphers/nevers-birago-fr3251-1572/` NOTES.md (every slip / clerk / interlinear / gloss / decipherment mention, the GAPS4
section, the Premise check (c) neighbour table, the per-letter slip checks), `harvest/` (gloss_no71/86/90.md,
f152r/ and f162r/ decipherment_slip.tsv, ciphertext_*.tsv, pass files), `images/manifest.json`, `BIRAGO-POOL.tsv`, and the
sibling folders NOTES.md names (`birago-fr3252-1571-72`, `birago-nevers-1571`, `ceppo-nevers-fr3251-1570s`). No reader, no
transcription, no decode, no truth built, no image opened as a read.

Pool rule applied (PREREG-txeng2-0 0b, Amendments 1-4): an item enters only if its truth comes from an independent key and a
known text -- a period decipherment slip, clerk sheet or interlinear gloss through the printed 1572 key -- never from a reader.
The `harvest/gloss_no71.md`, `gloss_no86.md`, `gloss_no90.md` files are **not** witnesses: each says so itself ("the whole
of this file is grade I (interpretation)", TRANSLATE-NEVBIR, 2 Oct 2026, a modern rendering of our own decode). They are
listed below as "no witness" for that reason.

## Ranked table (1572 key family, Birago's hand)

Baseline errors = scorable signs x 0.07-0.09 (today's pipeline rate, f152r 0.082 / flagged-excluded 0.043). Cost of a build
is scaled from TXP-152 (LEDGER: 6.20 for 97 signs, 20 crops, 2 Opus passes + 1 Sonnet adjudication + truth build).

| rank | leaf / letter | witness (kind, where) | est. cipher signs (scorable) | committed transcription | witness image on disk | est. baseline errors at 0.07-0.09 (flagged-excl.) | in a benchmark unit | first build step, est. cost | flagged-excl. errors per $ |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **f.162r, no.82** (27 June 1572) | later-hand decipherment slip pasted on f.161v, canvas 164 left: `harvest/f162r/slip_f161v_c164_1400_3450_2100_800.jpg`, read into `f162r/decipherment_slip.tsv` (2 lines: "monsignore di S. Andre" / "M. di Bellaguarda") | 25 (L01.1 21 + L01.2 4); about **17 scorable** (L01.1 pos 4-18, 20-21); excluded: pos 1-2 writer-struck, pos 3 X_NEW, pos 19 X_EQ off-sheet, L01.2 a name code with two digit-like off-sheet signs | yes: `harvest/ciphertext_f162r.tsv` = `f162r/passC.tsv` (NEVBIR-162, 2 Oct 2026: 2 Sonnet value-blind passes 22/25 agreed + 1 Sonnet adjudicator on the 3 struck-sign splits) | yes (slip crop and the cipher region `f162r/src_ark_12148_btv1b9060248g_f164_4700_2200_3050_450.jpg`, 3 line crops `f162r_L01_s1-3.jpg` + debug overlay) | 1.2-1.5 (about 0.7 flagged-excluded); one known candidate already visible: L01.1 pos 12 T81 (b) where the slip has r (T81/T83 look-alike or a cipher-clerk slip -- flag-worthy) | no (not in eval_heldout, dev_tune, f178r, f152r, or any BENCHMARK-TX row) | re-cut crops from the on-disk region with `tools/iiif_lines.py --image .../src_ark_..._f164_....jpg` (no Gallica), then the f152r recipe: 2 blind Opus passes, adjudicate, truth from the slip through the printed 1572 key with `align_sheet.py` / interlinear_align `--wildcard .`, score; about **2.0-2.5** (1 line, 3 crops, about a quarter of f152r's reading volume plus the fixed truth-build overhead) | about 0.3 |
| -- | no.87 f.178r L01-03 / f.178v L01-23 / f.179r L01-03 | clerk clear sheet laid in, canvas 182 right (`harvest/f179r_sheet/`) | 853 | yes | yes | -- | **taken**: f178r unit, dev_tune (f178v L01-12), eval_heldout (f178v L13-23 + f179r L01-03) | not re-scouted | -- |
| -- | f.152r, no.77 | slip on f.151v, canvas 154 left | 97 | yes | yes | -- | **taken**: birago1572-f152r | not re-scouted | -- |

No other leaf of the 1572 hand carries a period witness on any image on disk or named in the manifest:

| leaf / letter | signs (committed) | witness search on record (all by eye, no witness found) |
|---|---|---|
| f.139v, no.71 (7 Feb 1572) | 161 | VERIFY-NEVBIR-139V: no slip on the canvases; gloss_no71.md is our own grade-I rendering, not a witness |
| f.144r + f.144v, no.73 (27 Mar 1572) | 90 + about 24 untranscribed | Premise check (c): not found on canvases 146-147 |
| f.152v onward, no.77 rest | -- | not located (NOTES gap "not-attempted") |
| f.168r + f.168v, no.85 (29 July 1572) | -- (two short runs) | NEVBIR-168 / A3V-VNB1: no slip on canvases 171-172 |
| f.174r-175v, no.86 (27 Aug 1572) | 758 | canvases 173-180 at 1000 px and canvas 178 at native: no slip, squared paper, interlinear or marginal decipherment; gloss_no86.md is grade I |
| f.184r-185v, no.90 (2 Oct 1572) | 966 | canvases 188-190 at 1000 px: nothing laid in; f.185r L19 faint marks are show-through, not a gloss; gloss_no90.md is grade I |
| fr.3252 f.100r, no.67 (8 Jan 1572) | about 800 digits, untranscribed | BIRAGO-POOL / NEVBIR-3252: no slip, facing page show-through and a docket only; key family untested (1571 numerical or 1572) |
| fr.3252 f.117r, no.77 (13 Mar 1572) | about 330, French, symbol set unlike the 1572 key | NEVBIR-3252: no slip, no clear copy |

## Outside the 1572 family (listed, not ranked: their truth cannot run through the printed 1572 key)

- Ceppo-Nevers key (Birago's 1570-71 letters): fr.3252 f.36v interlinear gloss -- **taken** (`ceppo-f36v-gloss`); fr.3251 f.27
  interlinear gloss -- illegible at Gallica's native resolution, 6 clerk letters (ceppo-nevers-fr3251-1570s NOTES); fr.4702 f.37
  "yes" per BIRAGO-POOL, not on disk in this folder. A Ceppo unit would be its own key family's pool, not this one's.
- 1571 numerical cipher (birago-nevers-1571, fr.3251 f.119): no witness recorded.
- Birago's 1591-92 letters in the Nevers-office 1590s key (DECODE 9438, 9445-9447, interlinear, legible): already scouted by
  TXP-DEC (`benchmark-tx/txeng2/decode-scout-2026-10-09.md`); 9446 and 9447 "too short alone".

## Reading of the table

The 1572 hand is exhausted as a witness source except for **one line, f.162r (no.82)**: about 17 scorable signs, about 1-1.5
baseline errors, under one flagged-excluded error expected. It adds little power to the eval pool (f152r's 5 errors alone had
none; this item is a fifth of that) and costs about 2-2.5. Everything else in the hand has been eye-checked for a slip, sheet or
gloss and none was found; growing the pool further from this hand needs new material (a reply-side clear copy, a clerk register),
not a further scout of these folders.

## Requests per host
gallica.bnf.fr 0 (not contacted, per brief); de-crypt.org 0 (the folder's own files answered; tools/decode_list.py not run);
all other hosts 0. Subagents: 0. Images opened: 0.

Openings of eval truth: 0

## Integrity
sha256 of this file before the hash line was added, and the commit: see the done line in ROOM.md (`sha256sum` of the committed
file is recorded there beside the commit hash, since a file cannot carry its own final hash).
