# RUN2-NXALN pre-registration (committed before any alignment output is printed)

Written 4 Oct 2026, 03:23 UTC (`date -u`), account 1 worker RUN2-NXALN for LANE-RUN2. Brief:
`.claude/briefs/runs/2026-10-04-acct1-run2-wave1.md` (RUN2-NXALN). Nothing in this folder aligns or decodes anything before
this file is pushed.

## Material
- Cipher: `run2/nxatl/sequences.tsv`, leaves c510-c516, column `cluster` (k-means id, k=120), in leaf/line/pos order. Tiles,
  not signs (c262 ratio 1.05). c510 already starts at L05 tile 23 (cipher start); c516 holds only its cipher lines
  (L01-L03, L06-L19).
- Clear text: `run2/nxdup/dupuy221_226_norm.txt` (RUN2-NXDUP reconciled, PX-BRODEC normalised), letters only (spaces and
  digits dropped), with the two clear lead-ins removed because they are clear on the cipher leaves too: the c510 lead-in
  (221R from "sire le dernier" through "la reception d icelle que") and the c516 lead-in (226R "sire quelques jours ... me
  mander"). The stream thus runs "les espagnolz pour ce coup ..." to "... succedent mal".
- Instrument 1 (atlas, this job's priority): train = c510-c513, held-out = c514-c516.
- Instrument 2 (line reads): train = c510 (`run2/nxta/reconciled.tsv`), held-out = c516 + c515 L01-L20 (`run2/nxtb/`).
  Run only if the box allows after instrument 1 (brief: "if only one instrument fits, do the atlas instrument").

## Aligner (the same pipeline for control, nulls and target)
A shared option `--stream` added to `tools/interlinear_align.py` (offline test in `tools/tests/`): anchored, progressively
grown, banded monotone dynamic programming of a long symbol stream against a long letter stream. Moves: symbol emits one
letter (score = smoothed log P(letter|symbol) - log P(letter)); symbol emits nothing (cipher-side gap: null, nomenclator
remainder, tile split); letter skipped (clear-side gap: Dupuy abridgement, merged tiles). Start anchored at stream starts,
free end on the clear side. Hard EM: align, re-estimate P(letter|symbol) from the matched pairs, repeat; the aligned prefix
grows in steps. The key learned on train = argmax letter per symbol (symbols never matched on train decode as '?').
Second aligner: `tools/gibbs_align.py` on (line-sized symbol run, aligned span +- slack) pairs cut from the stream
alignment's anchors; its per-symbol modal value is compared with the stream key ("agreement between the two aligners").
Gibbs agreement is descriptive; the gate is computed on the stream aligner alone.

## Statistic
Held-out letter accuracy: decode the held-out symbols with the train key; align the decoded string to the clear text that
follows the train alignment's end (to the stream end), semi-global Needleman-Wunsch, match +2, mismatch -1, gap -1 on either
side, free leading/trailing gaps on the clear side only; accuracy = identical aligned pairs / number of held-out symbols.

## Nulls (200 draws each) and why each can differ from the target on this statistic
(a) Shuffled key: the learned values permuted among the symbols (multiset kept), held-out decoded and scored identically.
    Destroys the symbol-to-letter link while keeping the decode's letter frequencies, so it can only match the target if the
    statistic reflects letter frequencies plus NW slack, not the key.
(b) Shuffled text: train aligned (whole pipeline) to a word-shuffled copy of the train-side clear text; the key so learned
    decodes the held-out symbols, scored against the REAL held-out text. It keeps the training text's letters and word forms
    but breaks their order, so it can differ from the target only if order-dependent alignment is what carries the key.
    200 draws if one training run on the control is <= 6 s; otherwise 40 draws and the gate uses the null's MAXIMUM (stricter
    than p99 at that N). The count actually run is reported.
(c) Wrong text: the held-out decode scored against a same-length French span from a different letter. Dupuy 219-220 is not
    transcribed in this repository, so the spans are drawn (200 random offsets) from `tools/data/fr16` (Lettres de Catherine
    de Medicis, letters of the same court and decade), normalised the same way. Keeps the decode fixed and changes only the
    text, so it can differ from the target only if the decode carries this letter's content.

## Gate
Target passes iff held-out accuracy > p99 of each of (a), (b), (c) (or > max of (b) under the 40-draw fallback).

## Matched control (run before the target)
Synthetic homophonic + nomenclator cipher: fr16 text (a span disjoint from null (c)'s draws where possible, same letter count
as the target's clear stream); key with ~41 true symbols (the c262 reconciled label count): letters with 1-3 homophones by
frequency, ~8 nomenclator codes for frequent words (a code replaces the whole word), a null rate of 3%; the cipher symbol count
matched to the target's tile count per leaf (train/held-out split at the same proportion, 4 of 7 leaves by tiles). Atlas noise:
each true symbol over-split at random into clusters (120 clusters total, as the atlas), then impurity: a fraction p of tiles
relabelled to a random other cluster, p in {10, 25, 40}%; segmentation: tile insertions 8% and deletions 3% (c262 per-line
tile/sign ratio 0.84-1.14, mean 1.05). Line-read control (instrument 2): 41 symbols, 40% label noise, no over-split.
The control is scored with the identical statistic, nulls (a)-(c) (fewer draws allowed for the control: 50 each, gate on p99/
max as above) and gate.
**Which control licenses the target:** the atlas cluster->label purity on c262 is 0.593 (RUN2-NXATL), i.e. ~40% impurity, so
the 40% bracket is the matched one. If the control fails its gate at 40%, the atlas target is a non-test at this noise (not a
negative), whatever it scores; 10% and 25% are reported as the curve.

## Grades
Learned values grade C only if the target passes the gate AND both aligners agree on the value; else M. Comparison with
key.tsv (Tomokiyo, published) via `run2/nxatl/cluster_provisional_names.tsv`: agree/disagree counts only, no edit to key.tsv.
