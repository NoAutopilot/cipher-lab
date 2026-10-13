# PREREG-BAL-WL (BAL-WL worker, LANE DEFAULT-A1-0640, owner account), written 13 Oct 2026 07:4x UTC by date -u,
# pushed in its own commit BEFORE any tile read for this job

Target: Baluze 170 f.228r-v (Chavigny to d'Avaux, 25 Aug 1640, bare cipher), the same question as PREREG-BAL-SHAPE.md: do the f.228
letter-sign shape classes carry the values the reading gives them (all grade M)? Brief: .claude/briefs/runs/2026-10-13-acct1-default-0640-jobs.md
"BAL-WL". This is the SECOND control design on the BAL-SHAPE test (BAL-CROP: G1 0.870 PASS, G2 other-key negative 0.625 FAIL twice on
Saint-Chamond look-alikes -> non-test). If this design also fails its gates, the shape test is logged untested-by-this-tool for f.228.

## Why a new read, not BAL-CROP's reads
BAL-CROP's reads were exemplar-choice reads ("which exemplar, or NONE"), and this worker has seen their per-tile results (score1/2.out).
This design asks a different question per tile (verify ONE proposed label), so the reads are not reusable; one fresh blind read is made.

## Design (balshape/wl/tiles_wl.py, seed 20261013, half 0; disk only)
- Same tile() geometry, same 12-letter exemplar sheet (balshape/tiles/sheet_exemplars.png: E-a b c e g l n p r s t w, gloss-fixed
  f.258r/f.233r signs), same 23 gloss-fixed tiles P and 29 f.228 tiles T as BAL-SHAPE (balshape/tiles.py).
- Each unknown tile is captioned "Xnn: E-<letter>?" -- one proposed label. Arms, shuffled together into one blind id order:
  T  (27): every f.228 tile with its CURRENT value proposed (the 2 'gam=u' tiles dropped: no u exemplar exists).
  P+ (12): a seeded half of P with its TRUE gloss label proposed.
  P- (11): the other half of P with a WRONG label proposed: a seeded draw from the T value pool {a c l n r s t} minus the true letter.
  Same key, same hand, same leaves as P+; no other-key material at all (the BAL-CROP look-alike failure cannot recur by construction).
- Reader (one blind Sonnet subagent): per tile, yes/no "is this the same sign as the proposed exemplar (allowing for hand variation)",
  high/low confidence, and the best exemplar or NONE. It is not told the arms exist, nor which tiles are glossed or from which leaf.

## Why the negative's number can differ from the target's (rule 3, AX-5799)
The statistic is the yes-rate on the proposed label. The manipulation (true vs wrong proposed label on the SAME kind of tile) acts on the
exact input the yes/no depends on, so it is not orthogonal: a reader that anchors on the proposed label, or says yes to anything
letter-like, gives a high P- yes-rate (G2 FAIL); a reader that checks shape gives a low one. T's yes-rate is free to sit anywhere: its
labels are this project's own values, which may be right or wrong.

## Gates (both must pass, on the same read)
G1 positive: P+ yes-rate >= 0.75.
G2 negative: P- yes-rate <= 0.25 AND <= (P+ yes-rate - 0.50).
If either fails on read 1: ONE second blind read (fresh subagent, seed 20261014, half 1 -- the other P half becomes P+), gates on read 2
alone, only if the job's cap and box allow it (80% rule). If still failing (or no read 2): BAL-SHAPE logged untested-by-this-tool for
f.228 (two control designs failed), no grade or value changes.

## Target statistic (only if both gates pass)
Per f.228 shape class: share of its tiles answered yes. CONFIRMED if >= 2/3 yes (the one tile of a 1-tile class: yes) and no tile of
the class answered "no" with high confidence. Overall T yes-rate reported beside the P+ and P- rates (not gating).

## Adoption
Tokens of a CONFIRMED class on f.228 move M -> S through an exceptions/grade file read by tools/decode_key.py, never by hand; values never
change (only grades), so the fr17 judge is not re-run; then `python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check`.
A class answered "no" by the majority is logged as a conflict in HYPOTHESES.md (stays M). Every other class unchanged.
Caps: USD 3.5 job cap, box 07:39-08:49 UTC (80% 08:35). Units: 1 tile read (~1.5) (+1 only if under gate and within 80%).
