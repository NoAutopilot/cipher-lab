# SIG-AVS pre-registration (8 Oct 2026, account 1, for LANE SIG-1)

Committed before any blind read. Sources: 00126.pdf p4 (f.139, 3840x6040), 00098.pdf p2 (f.66, 3868x2990), 00074.pdf p3 (f.18,
3800x6144) and p5 (f.19, 3600x5922), resources.huygens.knaw.nl, 8 Oct 2026, embedded JPEGs extracted with pdfimages to the
scratchpad (not committed). Crop boxes (x0,y0,x1,y1 native px): boxes_qf.json, boxes_74.json; crop scripts cut.py, cut74.py
(single-sign crops, ink-trimmed vertically, 7-9 px edge strips whitened, enlarged 2x, neutral shuffled ids; id -> crop maps
key_qf_read{1,2}.json, key_read74_{1,2}.json, never shown to a reader). Readers: Sonnet subagents, each blind to labels,
to the plaintext and to the other read.

## Test A: 126 L1 pos 20 (Qf) shape sort

Crops (11): T = 126 L1 pos 20 (Qf, the target); 126 Pf L5 pos 6 and L8 pos 6 (C, AVS-SPOT); 126 Dp L3 pos 4 and L7 pos 1;
126 Qg L5 pos 9; 126 digit 9 L5 pos 7; f.66 Qf L5 idx 15 (the only other Qf on the 98 sheet); f.66 Pf L3 idx 2 and L2 idx 13;
f.66 Dp L2 idx 26. Reader task: sort all crops into piles so that each pile holds one intended character (ignore size, ink, slant).

Gates (all must hold in BOTH reads):
- K (known-answer discrimination, can fail independently of the target): the four Pf crops share one pile; no Dp crop, the
  Qg crop or the 9 crop is in that pile.
- C (the brief's control pair, f.66 Qf vs f.66 Pf): read literally, as the R21 labels give them: the f.66 Qf crop is NOT in the
  Pf pile. (Ambiguity logged before reading: R12A-AVS175 thought f.66's Qf looks like its Pf, so the labels themselves may be
  the split; there is no independent known answer for this pair. A merge of f.66 Qf with Pf in both reads will be logged as
  evidence for the label-split hypothesis but, under this brief, does not license a grade change: Qf stays M.)
Decision: if K and C hold in both reads and T is in the Pf pile in both reads -> 126 L1 pos 20 relabelled Pf, f at C (key_98 Pf
n=18, C). If K and C hold and T sorts with f.66 Qf (not Pf) in both reads -> label Qf confirmed, value f stays M. Any other outcome
(K or C fails in either read, or T splits) -> Qf stays M, no file change except NOTES.

## Test B: 74 p3 l.10 idx 6 (T? : T = s or 7 = n)

Crops (6): X = p3 l.10 idx 6; T exemplars l.10 idx 1, l.9 idx 8; 7 exemplars l.10 idx 4, l.9 idx 7; J (l.11) as a distractor.
Same pile task. Gate K74 (both reads): the two T crops share a pile, the two 7 crops share a different pile, J in neither.
Decision: K74 holds and X with the 7s in both reads -> ciphertext_74.tsv sign 7 (n, C; agrees with f.19 and Rachfahl 'noch');
with the Ts in both reads -> sign T (as written, a writer's s for n), conf cleared; anything else -> T? stays, M.
Reading files of 53/57/126 are not affected (74 is a key source); key_74 is rebuilt only if build_key.py reads ciphertext_74.

## Test C: f.19 l.13 (plaintext_74.txt line 'mit glimpf abgeschlagen und machen sich keinem')

Two line-half crops at native size; two blind Sonnet reads, each asked to transcribe the German as written. Decision: the words
after 'und' are corrected in plaintext_74.txt to the alternative ('machen sich keinem' vs 'mochten/möchten wohl leiden') only
if both reads give the corrected words' three content tokens matching one alternative (letter-level variants such as o/ö, ch/ck
allowed); otherwise the line keeps its [?] status and gets a note. No control applies (a palaeographic read, not a statistic);
the prior state is a single 100 dpi R14 read, so two native reads agreeing is the bar.
