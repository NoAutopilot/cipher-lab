# PREREG-BAL22-SHAPE (BAL22-SHAPE worker, LANE DEFAULT-A2-0911-14, account 2), written 14 Oct 2026 09:27 UTC by date -u (header first said 09:4x, a typing error corrected after the push; the commit time is the record),
# pushed in its own commit BEFORE any tile read for this job

Target: the 7 letter-sign tokens of Baluze 169 f.22r (reading_tokens_b169f22r.tsv: L01/8 f, L03/4 r, L03/7 m, L03/9 n, L03/12 a,
L04/1 n, L04/3 u; all grade M, settled from context by BAL169-F22; VER-BAL22 / AUDIT 7 says f and a are context fits, I not M).
Question: does each tile carry the value the reading gives it, judged blind against exemplars? Brief: .claude/briefs/runs/
2026-10-14-ytbiz-default-0911-jobs.md "BAL22-SHAPE". Method: BAL-WL (PREREG-BAL-WL.md), the same-key wrong-label negative that passed on f.228.

## Design (balshape/f22/tiles_f22.py; disk only; tiles placed by eye on the BAL169-F22 debug overlay, location only: balshape/f22/locate.py)
- T (7): each f.22r tile captioned with its CURRENT value ("Xnn: E-f?").
- P+ / P-: the same 23 gloss-fixed f.258r/f.233r tiles as BAL-WL (balshape/gloss_labels.tsv), split by seed; P+ with the TRUE gloss label,
  P- with a WRONG label drawn from the f.22r value pool {a f m n r u} minus the true letter (so the wrong labels are the letters under test).
- Exemplar sheet (balshape/f22/sheet_exemplars.png): the 12 gloss-fixed BAL-SHAPE exemplars (a b c e g l n p r s t w), E-m (m4) and E-u
  (gam) from f.229 (published-key values, b167228/sig_tiles.py), and E-f = the f column of Tomokiyo's table (images/louisxiii_davaux.png;
  no glossed f exists in this folder). Limit stated now: P+ never proposes f, m or u (no gloss-fixed P tile has those letters), so the
  positive arm does not check that those three exemplars are recognisable; P- does use them as wrong labels.
- Two blind reads (two fresh Sonnet subagents), each told nothing about arms, leaves or which tiles are glossed:
  read A = seed 20261014 half 0 (P+ 12, P- 11); read B = seed 20261015 half 1 (P+ 11, P- 12; the other P half becomes P+).
  Per tile: yes/no "same sign as the proposed exemplar (allowing for hand variation)", high/low confidence, best exemplar or NONE.

## Gates (per read; a read's T answers count only if that read passes both)
G1 positive: P+ yes-rate >= 0.75.  G2 negative: P- yes-rate <= 0.25 AND <= (P+ yes-rate - 0.50).
No third read. If either read fails a gate: no grade moves to S on this job (logged non-test for that read).

## Target statistic and adoption
A T tile is CONFIRMED only if both reads pass both gates and both answer yes. CONFIRMED tile: M -> S (exception row read by
tools/decode_key.py via decode.json, never by hand; values unchanged). Not confirmed: f (L01/8) and a (L03/12) -> I (VER-BAL22's
correction, applied because the shape check did not license them); r, m, n, u stay M. A tile answered no in both reads is logged in
HYPOTHESES.md as a conflict (value unchanged; stays M or I). Then `python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check`.
Numerals, marks and the name after "commandement" are not tested here.
Caps: USD 3 job cap, box 09:24-10:24 UTC (80% 10:12). Units: 2 reads (~0.8 each), reconciliation/scoring (~0.5), re-derivation (~0.5).
