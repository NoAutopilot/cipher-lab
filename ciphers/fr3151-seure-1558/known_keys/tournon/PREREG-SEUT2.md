# PREREG-SEUT2: held-out-half alignment gate for the Tournon 1556 fo. 22r transcription (R12A-SEUT2, 6 Oct 2026, written before any target score)

Why: PREREG-SEUT's self-scored statistic (learn the key on the slip, score on the same text) was a NON-TEST at control (0/3): at N ~500 a
key fitted to a text fits wrong texts as well. This gate learns on one half of the cipher and scores the other half.

## Inputs
- `passR.tsv`: a reconciliation of `passA.tsv`/`passB.tsv` made against the fo. 22r crops and `exemplar_sheet.png` ONLY. The reconciler is
  NOT given the slip or any decipherment, so the scored half (L07-L13) carries no slip knowledge. (The brief named "the slip as known
  plaintext"; the slip enters here only through the alignment of the build half, which is where known plaintext belongs without making
  the held-out half circular.)
- `passA.tsv`, `passB.tsv` unchanged, scored the same way as secondary rows (reported, not gating).
- `slip_read.txt` (M, 524 letters), letters a-z kept, as in PREREG-SEUT.
Symbol stream as in PREREG-SEUT ('NONE' dropped, each '??' a fresh id). Build half = crops L01-L06, scored half = L07-L13.

## Statistic
H = `tools/stream_align.py` nw_score( decode(learn(build_syms, slip)) applied to scored_syms , slip ): identical aligned pairs / scored
symbols; a scored symbol unseen in the build half decodes to unknown (a miss). Settings fixed as PREREG-SEUT (band 80, step 100, iters 3,
slope = letters/symbols, tool defaults otherwise).

## Null (can differ from the target: H depends on which letters follow which in the text)
Same learn+score with the slip replaced by (a) 20 random 524-letter fr16 passages (seed 12), (b) 20 word-order shuffles of the slip
(seed 13). Null p95 = 95th percentile of the 40.

## Power control, run first
PREREG-SEUT's synthetic design (slip text, 40 homophones + 11 word codes, N 485) at sign error 0.32 (brackets the A/B disagreement
0.318, the upper bound of either pass's own error), seeds 21, 22, 23, split at the same symbol fraction as passR's L06/L07 boundary.
Power: H > null p95 in >= 2 of 3 seeds, else NON-TEST and stop.
(Disclosed: an exploratory run of this control before writing, at err 0.32/0.20/0.10, 2 seeds, 20-text nulls, read H 0.66-0.86 vs
null p95 0.42-0.45. No pass stream was scored before this file was pushed.)

## Target gate
PASS if passR's H > its null p95. PASS licenses a key TSV (symbol -> letter from learn() on the whole passR stream, grade C only where
the symbol's top letter holds >= 2 aligned pairs and >= 2/3 of its pairs; else M), and only then the items 43/44 key test.
FAIL: no key from this transcription; the fo. 22r key waits on a person's sign sort, not a third machine pass (rule 3 third-attempt clause).
A PASS is not a reading of anything; it says only that the transcription carries the slip's text in order.
