partial

# Vincenzo Amidani's 1447 cipher: key rebuilt from his slips and their clear copies (BnF italien 1584) -- SFZ-1, 7 Oct 2026

Worker SFZ-1 for LANE ST-REBUILD (account 2), brief `.claude/briefs/runs/2026-10-07-acct2-st-rebuild-workers.md`.
Times by `date -u`: 21:18-21:4x UTC, 7 Oct 2026. Parent pool folder: `../NOTES.md` (SFZ-0). Lead: KH2-E / KH2-E2
(`ciphers/sforza-maino-1446/NOTES.md`, last two sections; `keyhunt/2026-10-07-KH2E.tsv`, `-KH2E2.tsv`).

Status meaning here: `partial` = a known-plaintext key (grade C) exists and passed a held-out gate. Every letter it was
built from already has a later-hand decipherment beside it, and no unglossed letter has been read with it. The f.70 test
(step 6) FAILed.

## Source

BnF italien 1584 (Archivio Sforzesco, 1447). Gallica ark:/12148/btv1b100373864 is from microfilm, with two pages per canvas
and no folio labels. Folio numbers were read on the images. The regions were fetched once at native resolution with
`tools/iiif_lines.py` (commands below) and are kept in `images/` with `images/manifest.json`.

| unit | cipher slip | clear copy | canvases | slip signs (our read) | copy letters (cipher part) |
|---|---|---|---|---|---|
| U1 | f.366 (opens in clear: "S. per quanto io posso comprendere fundamentalm[en]te") | f.365 "Del Sig.r Amidani 9bre 1447" | 360 / 359 | 353 | 331 |
| U2 | f.367 | f.368 "del Sig.r Vincenzo Amidani 9bre 1447" (two blanks where the copyist left names) | 360 / 361 | 590 | 609 |
| U4 | f.148 (opens "Scripsi ad li 14 del presente a la S.V. de quello havia inteso"; closes in clear from "Niente...") | f.147 "copia 15 maggio 1447" (one gap ".......") | 141 / 140 | 675 | ~1,000 |

U3 (f.371 / f.370) and U5 (f.206 / f.205) were not done (see Remaining gaps). The f.370 copy is visibly partial: it has a
dotted gap and "Desunt..."-type notes.

Commands (pasted):
```
python3 tools/iiif_lines.py --ark btv1b100373864 --canvas 360 --region 4170,960,2960,1110 --out ciphers/sforza-italien1584-1447/amidani/images --prefix f366 --overlap 0 --max-width 1500
python3 tools/iiif_lines.py --ark btv1b100373864 --canvas 359 --region 4780,330,2700,1300 --out ... --prefix f365 --overlap 0 --max-width 2400 --debug
python3 tools/iiif_lines.py --ark btv1b100373864 --canvas 360 --region 4080,2690,3020,1130 --out ... --prefix f367 --overlap 0 --max-width 1500 --debug
python3 tools/iiif_lines.py --ark btv1b100373864 --canvas 361 --region 5900,250,1560,2300 --out ... --prefix f368 --overlap 0 --max-width 2400 --debug
python3 tools/iiif_lines.py --ark btv1b100373864 --canvas 141 --region 4100,300,3300,1380 --out ... --prefix f148 --overlap 0 --max-width 1700 --debug
python3 tools/iiif_lines.py --ark btv1b100373864 --canvas 140 --region 5700,250,1850,3800 --out ... --prefix f147 --overlap 0 --max-width 2400
```
The debug overlays were checked: 8, 10 and 13 cipher lines were found, matching the slips.

## Method and deviations from the brief

- **Sign reading.** `tools/glyph_atlas.py` was not available: it needs opencv, which is not installed. Two blind Sonnet
  passes were started on f.366 with the label sheet `labels.md`:
  - Pass A finished (341 tokens) and called itself low-confidence. It also read the letter-shaped cipher groups as clear
    words.
  - Pass B's file write was refused by the session's auto-mode permission check, so it produced no file. It was not
    re-routed through another tool.
  - SFZ-1 (Opus) therefore read all three slips itself, sign by sign, from 1.3-1.5x enlargements of the native crops.
    Each slip was read before it was aligned to its copy.
  - f.367 and f.148 were read after the f.366 key had been printed. Label choices could therefore lean toward
    consistency with that key (a possible bias, unmeasured). The f.366 read itself was blind to any key.
  - `err_2reader` for f.366 (pass A vs SFZ-1, `tools/reconcile_passes.py`): 231/367 aligned columns agree (62.9%), so
    37.1% disagree. Most of this is pass A's weakness (its own words, and its w: words). This is not a reconciled
    figure. f.367 and f.148 are single-reader.
  - `err_true` is not measurable: no benchmark item exists for this hand.
  - What the gate does show: held-out letter accuracy of 74-78% (below), which bounds the combined reading error and
    key error from above.
- **Letter-shaped signs.** The slips mix in signs drawn as cursive minuscules, which run together into apparent words:
  "to tamd", "adusse", "primu", "maxie", "tanno", "lano", "mea". KH2-E took "fundamentalm[en]te" and these groups for
  clear words. Only the openings and closings named above are clear. The groups are cipher: f.366's "adusse" aligns to
  "sonno" and "primu" to "che". Each letter-shape is labelled `cX` (`labels.md`, additions).
- **Clear copies** (`clear_f365.txt`, `clear_f368.txt`, `clear_f147.txt`) were read by SFZ-1 in one pass from the native
  crops. Accents are dropped and copyist blanks are marked `[ ]`.
- **Alignment.** `tools/stream_align.py`, reached through `tools/interlinear_align.py stream` (banded hard-EM, band 40,
  step 60, default gap costs 1.5), is run per unit. Signs aligned to nothing (nulls, names the copyist left blank, or
  read errors): f.366 41/353, f.367 57/590, f.148 61/675. The degenerate "all null" optimum did not occur.

## Gate G1 (pre-registered; `g1.py`, output `gate_g1.tsv`)

Leave-one-letter-out. For each unit, the key is learned from the other units' slip/copy pairs and used to decode the
held-out slip. Its letter accuracy is scored against the held-out unit's own copy: identical aligned pairs, the
held-out slip's own null positions excluded, and signs absent from the training key counted as wrong. The control is
200 shuffles of the training key's sign -> value map. The shuffle changes the decoded letters, so it can change the
statistic.

| held out | signs | nulls | trained signs | unseen | real | shuffle mean | shuffle p95 |
|---|---|---|---|---|---|---|---|
| f.366 | 353 | 41 | 60 | 7 | **0.776** | 0.342 | 0.378 |
| f.367 | 590 | 57 | 60 | 6 | **0.775** | 0.353 | 0.390 |
| f.148 | 675 | 61 | 61 | 9 | **0.739** | 0.386 | 0.420 |

Mean 0.763 >= 0.60, and every unit is above its shuffle p95: **PASS**. With U1+U2 only (first run), the result was
0.814 / 0.771 against p95 0.372 / 0.372, also PASS. The shuffle mean is high (0.34-0.39) because the alignment is
free to slide and the commonest values (a, e, i, o) match often. The margin over p95 is 0.32-0.40.

**One key or several?** Across the three unit pairs there are 105 (sign, unit-pair) cases with at least 2 counts in both
keys. 88 give the same value and 17 conflict. The conflicts concentrate in signs SFZ-1 found hard to tell apart (H vs h,
q, 3, S, m) and in the `cX` letter-shapes. That pattern looks like reader label-merging (two signs under one label) or
homophones, not a different key. It is consistent with one key for all three 1447 letters (Nov 1447 and 15 May 1447).

**Key** (`key.tsv`, pooled over the three units): 65 sign labels, 35 at C (count >= 2, share >= 0.6), the rest M. The
values come from the later-hand clear copies, so the grade is C at best (brief item 2). Per-unit keys: `key_f366.tsv`,
`key_f367.tsv`, `key_f148.tsv`. Per-sign alignments: `align_*.tsv`. Main values (C): + a, 7 e, O e, g e, D i, T i,
F r, R s, Q s, x o, P o, o t, z t, A t, a d, h d, d n, J n, K l, f l, l a, Y m, W p, 8 c, c c, # g, n u, t p, b b, e m; H (40 counts, split between i in ff.366/367 and r in f.148; pooled top value r at 0.44) and q (a, 0.56) are among the commonest labels but fall below C: most likely two signs read under one label (above).
This is a homophonic letter substitution: at least three signs for a, e and i each, two for o, t, d, n, l and s.

Reproduce: `python3 ciphers/sforza-italien1584-1447/amidani/g1.py --check` (exit 1 if gate_g1.tsv or key.tsv is stale).

## Step 6: f.70 (BnF italien 1583, Amidani to Sforza, Milan 4 May 1446) -- test FAILed

`f70_test.py`, output `f70_test.out`. Bourdeau's f.70 codes (draft transcription from DECODE image IMG_R7899_I35638_P1,
`ciphers/sforza-maino-1446/ciphertext_f70.txt`, credit dbourdeau/cyphersolver, CC BY 4.0) were mapped to our labels
**by his written descriptions only** (`MAP` in the script; several mappings are marked weak). Codes with no counterpart:
W (ab-ligature), O (reversed c), K (hatched sign), P (barred p), 13 tokens in all. The remaining 377 signs were decoded with
the pooled key and compared with 200 shuffled keys:

| statistic | real | shuffle mean | shuffle p95 |
|---|---|---|---|
| it16dip 4-gram log10/letter (era mismatch: 16th-c. corpus for a 1446 letter, flagged) | -1.779 | -2.016 | -1.812 |
| fraction of 4-grams found in the three clear copies | 0.029 | 0.016 | 0.032 |

**FAIL**: the 4-gram statistic is narrowly above p95, the copy statistic is below it, and the decode is not Italian
("iresenoeraosaneresegalnso..."). No reading file was written and no f.70 token is graded above M.
**What the FAIL does and does not mean.**
- It is conditional on three things: (a) Bourdeau's draft transcription; (b) a description-only label mapping;
  (c) the two inventories not matching. Several of our most frequent signs have no counterpart in Bourdeau's f.70
  inventory: our o (σ, = t), l (⊢, = a), T (π, = i), K (ß, = l), a (= d), h (= d), and the `cX` letter-shapes.
  Conversely, his E70 (11.8% of f.70) has no clear counterpart in ours.
- So the test cannot separate "f.70 uses a different (1446) key" from "the two transcriptions do not map".
- It is a weak negative on mapping grounds. It is not evidence about the 1446 key.
- The decisive next step is to re-transcribe f.70 from an image in our labels. Italien 1583 is not on Gallica; the
  route is DECODE R7899 or a BnF order (see `ciphers/sforza-maino-1446/NOTES.md`, "Image gate").

## Grading (rule 4)

- Key values: C (from later-hand copies) or M (`key.tsv` grade column). No H.
- The three slips are N0 by construction: a decipherment sits beside each (rule 10 is for a verifier; nothing here is
  claimed as a reading).
- f.70: no reading; the test failed.
- `tools/judge_plaintext.py` was not run on a reading: none exists.

## Where it was not found

Not searched for print in this job (the brief asked for no novelty or print work). KH2-E found these items absent from the
DECODE listings of 24 Sept, Bourdeau's it1583 folder, `sources/` and `ciphers/`.

## Remaining gaps (SFZ-1, 7 Oct 2026)
Read so far: 0 unglossed letters read; key passes held-out G1 at 0.763 mean letter accuracy over 3 glossed units (1,618 slip signs)
- f.70 (italien 1583, 1446) under the 1447 key - blocker: not-attempted; the description-mapped test failed and cannot separate key from mapping, so it needs f.70 re-read from an image in our labels; next: fetch DECODE R7899 image via tools/decode_browser_login.js (one login) and transcribe f.70 in labels.md labels, then rerun f70_test.py with an identity map, ~$4
- f.371/f.370 (U3) and f.206/f.205 (U5) slips - blocker: not-attempted; would add key coverage for the uncertain signs (H/h, q, 3, S, m, cX); next: same per-unit procedure (native crops, read, add to g1.py UNITS), ~$3 each
- second blind reader for the three slips - blocker: not-attempted; err_2reader is only measured on f.366 against a weak pass; next: one Sonnet pass per slip with the extended labels.md and the cX convention, reconcile with tools/reconcile_passes.py, ~$1.5 per slip
- the four 1447 cipher items without a clear copy (f.13 Pusterla, f.15 Duke, f.143 Marcolino, f.259 Guarna; SFZ-0) - blocker: not-attempted; different senders may share this key family; next: after SFZ-0's check-solved and intake gate pass, decode one with key.tsv plus a 200-shuffle language control (lane's call), ~$3

## Escalation (SFZ-1, 7 Oct 2026)
- [x] siblings: three glossed Amidani 1447 slips used (ff.366, 367, 148); f.369, 371 and 206 remain
- [x] clear-pages: the later-hand clear copies ff.365, 368, 147 used as known plaintext
- [ ] known-keys: not checked against Cerioni 1970 / ASMi Sforzesco cipher registers; planned for the lane
- [n/a] print: brief excluded print and novelty work; a verifier session does this
- [x] key-rebuild: key.tsv rebuilt from three pairs and gated G1 PASS
- [ ] image-check: f.70 needs an image read in our labels (DECODE R7899) before the 1446 question is a real test
- [ ] retry: f.70 test to be rerun once f.70 is re-transcribed
Verdict: keep going: 4 internal gaps; cheapest next: second blind reader on f.366/367/148, ~$1.5 per slip (or U3, ~$3)

## Requests

gallica.bnf.fr: 14 (7 overview canvases at 1400 px, 1 info.json, 6 native regions), one at a
time, at least 2 s apart, no errors. No other host.

## f.70 re-read (SFZ-70, 7 Oct 2026)
f.70 was re-read from the DECODE R7899 image in our labels. The key test FAILs under the identity map and under a best-case
nearest-label map: 1446 key differs from 1447 at this transcription. See ciphers/sforza-maino-1446/NOTES.md, last section, and
f70_test_sfz70.out. This closes the "image-check" and "retry" escalation steps above for f.70.
