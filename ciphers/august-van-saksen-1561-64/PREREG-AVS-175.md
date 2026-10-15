# PREREG AVS-175 (15 Oct 2026, worker AVS-175, account 2, LANE DEFAULT-A2-0509-15)

Written and pushed before any image of WVO 124 or 126 is fetched or looked at in this session.

## Scope
The brief names two units: (1) WVO 175 pp.3-8 for a hand that separates Qf, and (2) a native look at WVO 124 f.134's one K = 'der'.
Unit 1 is NOT run: NOTES.md "R12A-AVS175" (6 Oct 2026) already ran 175 pp.3-8 under a prereg (S2 = 1, no second f-shape), and
"SIG-AVS" (8 Oct 2026) ran the follow-on shape sort on 126 itself; both leave Qf at M. The brief's stop rule ("the folder's NOTES.md
shows the step already done") applies to that unit. Only unit 2 runs.

## Question (unit 2)
align_124.txt f134 l.10 reads '... Td 3 Z 8 3 Z L | deiweil ;; K | der ;; 8 3 L Td 9 | weldt ...' (f.135 'dieweil der Weldt'), the one
period witness for K = der against 175's K under gloss 'die' (A4-AVS175, A4-AVS175B). Is that f.134 sign the same shape as 126 f.139's
two K (ciphertext_126.tsv l.4 pos 26, l.6 pos 1), or a different sign (for example B, which A2-AVS4 records once as 'der' before PAPE)?

## Material
00124.pdf (page 6 = f.134) and 00126.pdf (page 4 = f.139) from resources.huygens.knaw.nl, 2 requests, scratchpad only, nothing committed.
Single-sign crops at native size, cut by a script (avs175/cut_k124.py, boxes in avs175/boxes_k124.json) under neutral shuffled ids:
- T: f.134 l.10, the sign between 'deiweil' and 'weldt';
- K1, K2: 126 f.139 l.4 pos 26 and l.6 pos 1 (K);
- B1: f.134's B (= der before PAPE), if locatable on the page; if not located, the sort runs without it and this is logged;
- R1, R2: two f.134 R (E.L.); M1, M2: two f.134 M (und) -- known-answer exemplars whose identity f.135 supplies.

## Read
One blind Sonnet subagent call: the crops only, neutral ids, no key, no plaintext, no sign names; task: sort into piles of the same
written sign. Then one look by this worker (Opus) at native size, logged separately (not blind: this worker knows the question).

## Gates and decision (fixed now)
- G (known answer): R1, R2 in one pile; M1, M2 in one pile; that R pile differs from that M pile. G FAIL -> non-test, nothing moves.
- If G PASS and T is in the same pile as both K1 and K2 (and not with B1 if B1 is in the sort) -> T is K: 124's K = der witness
  stands, the K conflict (der 1 / die 2 by reads) holds, 126's two K stay M (prereg_avs175.md's date-proximity rule).
- If G PASS and T is in a pile with neither K1 nor K2, AND this worker's native look agrees T is not K -> 124's 'der' token is
  recoded off K in align_124.txt (to the sign it matches, or 'K?' if it matches nothing named); K's period witnesses are then 175's
  'die' only, and that is reported as licensing a lane decision on 126's two K. This job does NOT regrade 126's K itself in that case
  (175's two K are one aligner-clean and one slid, A4-AVS175B); it reruns build_pairs/build_key/decode_key --check and reports.
- Any split (T with one K only; sorter and own look disagree) -> unresolved, nothing moves.
- Qf (126 L1 pos 20) is not touched by this job.

## Cost
2 requests; 1 Sonnet vision call (~0.6) + 1 own look (~1) + write-up. Cap 5, box 90 min (05:21-06:52 UTC).
