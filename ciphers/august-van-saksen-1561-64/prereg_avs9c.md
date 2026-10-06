# PREREG R11A-AVS9C: a count-2 control for sign 9 = f in 53 (6 Oct 2026, worker R11A-AVS9C, account 1)

Written and pushed before any scored run. Follows R11A-AVSK (prereg_avsk.md), whose control had no count-2 sign, so its gate L
could not speak to sign 9 (count 2; R11A-AVSK: 4 of 6 target restarts converge, all give 9 = f; shuffle null 0 of 6).

Control design (`anneal_53n.py control2 SEED`, seeds 1-10): the tool's standard matched control (`make_control`, K = 21, N = 364,
homophones by frequency; S1's and R11A-AVSK's design) on a seed-varied 364-letter window of tools/data/de1600/briefedespfalzgr01joha
(Bezold, Briefe des Pfalzgrafen Johann Casimir I, letters 1575-82: the nearest-era German princely correspondence on disk, mixed
with the 1882 editor's own German; not part of the anneal's language model, which is de16/composed_enhg + plaintext_98).
Windows are drawn by rng(5000 + seed) and kept only if (a) <= 21 distinct letters and (b) the enciphered window has at least one
sign of count 2. The filter reads only letter and sign counts, never a score. A dry run of the filter alone (no anneal) gave 12
count-2 control signs over the 10 windows (k x5, p x3, m, q, x, z); windows 7 and 8 overlap (starts 152132, 152329).
Anneal settings unchanged (order 3, w as uu, 200000 iters, 6 restarts, uni-weight 1.0).
An exact-profile control (`make_profile_control`) was tried first on this 192k-letter text and, like align_74's, admits no
window (seeds 1-10, 5000 tries each): with 21 signs the profile forces almost one sign per letter. Not used.

Gates (R11A-AVSK's, plus the count-2 sub-gate this job exists for):
- **C**: mean best-key letter share over seeds 1-10 >= 0.90. Fail -> non-test, sign 9 stays M.
- **L**: pooled over seeds 1-10, control signs with count <= 3 read right by the best key, share >= 0.80.
- **L2**: pooled control signs with count exactly 2 read right, share >= 0.80, with at least 10 such signs pooled (12 expected).
- **T** and **S**: taken from R11A-AVSK's runs on the same ciphertext_53.tsv (avsk/target_s1.json: T PASS, 4 of 6 converge,
  all 9 = f; avsk/shuffle_s1.json: S PASS, 0 of 6). Not re-run: the input file and the script's target/shuffle modes are unchanged.
  Can the control vary on the statistic? Yes: per-sign recovery of rare signs differs window to window (R11A-AVSK's one
  control already missed its count-3 sign).

Decision: if C, L and L2 all pass, sign 9 enters key_53.tsv as f at grade S (source R11A-AVS9C + R11A-AVSK), its two
exceptions_53.tsv M rows are dropped (settle_53n.py), decode_key --check re-run, NOTES + ROOM verifier flag (a grade change after
AUDIT.md). If L2 fails, or fewer than 10 count-2 signs are pooled, sign 9 stays M ("untestable at N 364 by this design" if under
10, otherwise "the control does not read count-2 signs reliably"); if C or L fails, likewise no change. G4 (count 2, already S = p
in key_53) is reported only: no other key change is allowed by this run.
