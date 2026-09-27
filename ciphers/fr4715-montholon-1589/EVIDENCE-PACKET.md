# Evidence packet: f.81r digit-stream calibration (fr4715-montholon-1589)

Written 27 Sept 2026 by parent worker MONT-LATTICE. It fixes the material, the known answer, the gates, the
controls and the held-out rule, so that any reader or decoder, including an outside prototype, can be scored on the
same four lines by the same rule and compared row for row with the results below. The statistic is a calibration
against a known answer. It is not a reading of the letter, and passing it does not make a reading.

## The item

BnF fr.4715, no.58, f.81r (Gallica ark `btv1b52509819x`, canvas 177, IIIF label '81r'). Montholon, Tours, 8 Nov 1589.
It is a numeric homophonic cipher with dotted word-codes. Four calibration lines: **L03, L08, L13, L15** (folio line
numbers as used in `NOTES.md`).

## Inputs (path, last commit, sha256 first 12)

| role | path | commit | sha256[:12] |
|---|---|---|---|
| known answer (grade H), codes only | `witness/aligned_dump_codes.txt` | 01b22a3 | 85bd27e017e1 |
| known answer with Tomokiyo's glosses | `aligned_dump.txt` | 01b22a3 | 42897f34109f |
| letter key (Tomokiyo's table) | `keys/key_vieuville_nevers.tsv` | 01b22a3 | 21ec8c6cb3f2 |
| line images (slope-following sheets, what a reader sees) | `images/f81rslope_L03.jpg`, `_L08`, `_L13`, `_L15` | 36fdd7c | 9ef73ea5ad11, bfd8074c3c2c, 2fc03c581535, 9dea0ce8716e |
| reader stream, call C (Opus, sloped sheets; best so far) | `witness/read_digits/call_C.tsv` | 36fdd7c | 5df0631d2731 |
| reader stream, call B (Sonnet, sloped sheets, no dots) | `witness/read_digits/call_B.tsv` | 60c8550 | a1d17efd9483 |
| reader stream, call A (Opus, old fixed-y sheets, truncated) | `witness/read_digits/call_A.tsv` | 3edcd58 | b80c28e47864 |
| blind passes (old sheets) | `witness/pass_a.tsv`, `witness/pass_b.tsv` | 01b22a3 | aefed749f224, dc0c812ffec2 |
| settled v2 digits on these lines | `witness/read_digits/ref_v2.tsv` | a69f67e | f99c9cef8e03 |
| the dump as a stream (scorer check, should read 1.0/0.99/1.0) | `witness/read_digits/ref_dump.tsv` | a69f67e | 8fdd9c857d11 |
| scorer | `scripts/mont4715c.py` (`digscore`) | 3edcd58 | 0dcf2c2513f8 |
| lattice decoder (this job) | `scripts/mont_lattice.py` | this commit | 5c4df60b15cf |

## The known answer

Tomokiyo's group dump of L02-L17 (959 groups, cryptiana.web.fc2.com, page bnf4715.htm section no58), grade H, is the
reference. It is itself a transcription, not the manuscript. It carries no line breaks. Each line's reference span
is assigned through our v2 anchors (`mont4715c.py dump_spans`): L03 dump groups 22-84, L08 339-395, L13 698-759, L15
825-888 (0-based). The spans are approximate by about four groups, which is why the scorer lets each window's ends
move by up to 8 groups (below).

## Submission format

A TSV with header `line<TAB>digits_with_marks<TAB>confidence`, one row per line (L03, L08, L13, L15). The stream is
the line's digits left to right, with no group boundaries. `'` goes immediately before a digit that carries a dot or
stroke above it (a dotted word-code marks its first digit). `?` stands for an undecided digit. Everything else is
ignored. Segmentation is not the reader's job: the scorer parses the stream with the key's code inventory. That
parse restores 0.99 of the dump's own groups from a boundary-free stream (MONT-CAL).

## Scoring rule (unchanged since MONT-READ-DIGITS, pre-registered there)

`python3 scripts/mont4715c.py digscore SUBMISSION.tsv L13,L15` (and `L03,L08`, and all four). Per line the reference
is the contiguous dump window whose start and end each lie within 8 groups of the anchored span, chosen to maximise
(matched digits - unmatched reference digits); every control gets the same free choice.
- **G0** digit LCS / reference digits >= **0.92**
- **G1** letter-group (undotted) recall after the key parse >= **0.85**
- **G2** dotted-group recall, dot required, >= **0.70**

All three must be met. Built-in controls: a within-line digit-order shuffle (G0) and a within-line shuffle of the
parsed groups (G1, G2), 20 each, seed 1.

## Held-out rule

The **tuned pair is L03 + L08** and the **held-out pair is L13 + L15**. A method may set anything it likes on the
tuned pair: weights, thresholds, prompts, and which voters to use. Its verdict is read on the held-out pair, scored
once, with nothing changed after the score has been seen. A gain that appears only on the tuned pair is not a gain.
The pooled four-line score is reported beside the verdict and does not decide it. Any model trained on the dump (a
dotted word-code table, for example) must exclude the dump groups inside all four lines' windows (span plus or minus
8). That is 310 groups, which leaves 89 dotted groups over 27 codes.

## Reader confusion matrix (MONT-CAL, our v2 transcription vs the dump, L02-L17; row = dump digit, column = ours)

```
   ours: 0 1 2 3 4 5 6 7 8 9
 dump 0  - 0 0 3 0 3 0 1 0 0
 dump 1  1 - 2 0 1 6 0 0 0 2
 dump 2  0 1 - 7 1 5 5 1 0 1
 dump 3  9 4 4 - 2 14 3 10 0 5
 dump 4  1 0 0 0 - 0 3 1 0 2
 dump 5  8 1 0 9 1 - 5 2 0 4
 dump 6  2 0 3 4 2 2 - 1 0 2
 dump 7  0 0 1 1 0 0 0 - 1 0
 dump 8  8 7 1 4 1 6 4 2 - 1
 dump 9  3 2 4 2 1 3 5 3 1 -
```
(`python3 scripts/mont4715c.py anatomy`.) The matrix is from the old transcription, read on fixed-y sheets. Call C's
own errors on the sloped sheets are far fewer: 8 unmatched digits in 475.

## Results on file (same rule)

| stream | tuned L03+L08 G0 / G1 / G2 | held-out L13+L15 G0 / G1 / G2 | held-out verdict |
|---|---|---|---|
| call C alone (Opus reader) | 0.983 / 0.910 / 0.737 | 0.984 / 0.964 / 0.562 | G2 missed |
| MONT-LATTICE (C + B + neighbours + dotted prior) | 0.965 / 0.910 / 0.789 | 0.947 / 0.883 / 0.600 | G2 missed |
| lattice with shuffled weights (5, mean) | 0.961 / 0.902 / 0.789 | 0.905 / 0.795 / 0.600 | G2 missed |
| call B alone (Sonnet), pooled four lines only | 0.886 / 0.657 / 0.000 (pooled) | -- | -- |
| the dump itself (scorer check) | 1.000 / 0.990 / 1.000 (pooled) | -- | reference |

The number to beat is **G2 on the held-out pair**: 9 of 16 dotted groups with call C, where 12 are needed for 0.70.
Digits and letters already clear their gates.

## Controls a submission should report beside its own number

1. digscore's built-in shuffles (printed automatically).
2. Call C alone on the same pair (the row above).
3. If the method weights readers, the same method with weights shuffled across positions. This control must also
   scramble or remove the dot evidence. Otherwise it cannot fail differently from the target on G2, which is what
   happened to MONT-LATTICE's control (i) (NOTES.md "MONT-LATTICE").
