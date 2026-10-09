# UNA-BIR3252 pre-registration (9 Oct 2026, 06:2x UTC by date -u; written and pushed BEFORE any tile is cut or read)

Brief `.claude/briefs/runs/2026-10-09-account4-orch-unassigned-jobs.md` (UNA-BIR3252), for the account-4 orchestrator.
Instrument: per-sign 4x tiles cut from the NATIVE bands (`../../../ceppo-nevers-fr3251-1570s/harvest/witness_f36/c37_f36r_cipher.jpg`,
`c38_f36v_top.jpg`, `c38_f36v_mid.jpg`, `c38_f37r_cipher.jpg`), each sign located by its neighbour context (passD_v3 / recon.tsv
sequence) on the band, not by "pos k of n". Reader: this worker's own eye (no subagent), one tile sheet per unit. Line-segment
reconciliation calls stay [retired] (RUN6-BIR3637, BKLOG-0507) and are not used.

## Rules (reused from files on disk, not re-derived)
- R-8 (witness_pairs/PREREG.md, CEPPO-WITNESS-PAIRS): 8 with a bar through the waist past BOTH sides -> S80 (a); no bar -> S65 (et).
- R-hash (same file): stem SLANTED across two horizontals -> S88 (t); stem UPRIGHT -> S24 (o).
- R-6 (same file): flat crossbar on top of the 6 -> S54 (null); blob/teardrop top, no crossbar -> S74 (m). Weak side both ways.
- R-bar (D07-CEP21 PREREG-S13S69): loop crossed by ONE bar past both sides -> S69 (f, unglossed side); TWO bars -> X_THETA2 (r, glossed).
- R-dot (CEPPO-SPLITS): caret/A-form with a dot inside or beside -> S23 (n); curled-top lambda, no dot -> S97 (a).
- A tile whose deciding feature cannot be seen at 4x is UNDECIDED and keeps its passD_v3 label ('?' stays '?').
- Pairs with no glossed rule on disk (S73/S88, S73/X_THETA2, S88/X_THETA2, S80/X_NEW, S30/S73, S16/S42, S17/S66, S13/S45, and every
  other pair of adjudicate_in.tsv not listed above): NOT tiled, counted as untested ("no rule").

## Units (in this order; stop before a sheet that would cross 80% of the cap or of the box)
Targets: the 35 rows of `adjudicate_in.tsv` whose two candidates form one of the five rule pairs above, minus r37_L01 pos 9
(already settled in passD_v3). Order: R-8 (4), R-hash (5), R-6 (7), R-bar (10, of which v36top_L01 pos 18 is glossed r and becomes a
known-answer tile, see below), R-dot (5). Tiles: 4x, autocontrast, about 150 x 110 native px around the sign; sheets of up to 8.

## Gate 1: known answer FIRST (instrument check)
At least 6 known-answer tiles of the rule families, located from files on disk, shuffled (seeded permutation, mapping written to a
file not opened until the read is written) among the first target sheets, read by the same rule: v36top_L01 idx 3 (double-barred
oval, gloss r -> X_THETA2, C), v36top_L01 idx 5 (S80, gloss a, C), v36top_L01 pos 18 (barred oval, gloss r, M), r36_L12 S24 (gloss o,
M), and the witness_pairs glossed hash-t / barred-8 / plain-8 instances on f.36v top (L2 x~1100, L3 x~1080, L3 x~2290) as far as
they can be located. Score: rule label == gloss-implied label; UNDECIDED counts as wrong. **Gate: >= 80% correct (>= 5 of 6, or the
same share if more are used). If the gate fails: stop, log a non-test for this instrument, apply nothing.**
Caveat fixed now: the rules were derived from glossed instances on this same leaf; the known-answer gate tests whether this reader
sees the deciding feature on a native 4x tile, not the rules themselves.

## Apply (only if Gate 1 passes)
`passD_v4.tsv` = passD_v3 with every DECIDED target set to the rule's label. UNDECIDED rows unchanged. Reads first written to
`reads_una.tsv` (tile id, line, pos, candidates, feature seen, rule label or UNDECIDED) before any decode or score is run.
Grades: no C from this job; ciphertext_f36_v2.tsv and the decode inputs are not changed; decided rows are S-candidates for a verifier.

## Measures and controls (rule 3)
1. E figure, as before: E = (one-sided 40 + splits not decided) / 700. E before (BKLOG-0507) 0.321 ((40 + 185) / 700). A residual,
   not an error rate (TRANSCRIPTION.md).
2. Key control: `../../../ceppo-nevers-fr3251-1570s/harvest/decode_control.py passD_v4.tsv --shuffles 200 --windows 20 --err 0.286
   --extra X_THETA2=r --seed 1,2,3` (0.286 = the last measured whole-letter two-reader figure; the E residual is not used as --err).
   Gate 2: the printed key ranks 1/201 on every seed. Reported beside passD_v3 (z 6.44 / 6.54 / 7.90, real -1.3799).
3. Placement control (can vary on the statistic, the real-key score per letter): the same number of changed rows, drawn at random
   from the same rule-pair rows of adjudicate_in.tsv and set to a random member of their pair, n = 500; p = share of draws whose
   real-key score >= passD_v4's. Reported beside the real number. A real score that does not beat most draws reads "the shape
   choices do not read better under the printed key than random choices among the same pairs" and is reported as such.
