# PREREG-txeng3-5 BOXES: do the owner's corrected boxes lower err_true against the machine's boxes? (TXE3-5; account 3; Fable worker session_014KPMCN7x6L5GsRgRFKMCLr; written 06:2x UTC 11 Oct 2026 by date -u, before any arm was classified or scored)

Brief: one of ten TXE3 experiments (account-3 parent session_0198Cv8ypBfBVfRToKVWx33M, owner's ask 11 Oct 2026). Cap USD 15, box
05:47-07:47 UTC, 80% line 07:23 / 12.00. Nearest prior: OL1-BOXES / OL1-PAGE (benchmark-tx/txeng2/oracle1/: the machine boxes the
owner's L74 pages were built from, boxes/boxes_recut_all.tsv, 343 Birago + 445 Luzerne + 541 Vivonne), the owner's answers
(oracle1/answers/{birago,luzerne,vivonne}/settled.tsv, recuts.tsv; vivonne/merges.tsv), TX-ATLAS-B72 (the Birago 1572 family atlas
and `glyph_atlas.py classify`; atlas top-1 on no.87 held-out lines err_true 0.162). What is different: the owner's cuts are scored
against truth for the first time, with the cut as the ONLY change (same atlas, same classifier, same scorer).

## Overlap with benchmark truth (found before scoring)
| oracle hand (12/12/11 lines) | benchmark item with truth on those lines | split | pipeline available |
|---|---|---|---|
| birago1572-no87 f178v L01-L12 | birago1572-no87 (343 scored of 354 positions on these lines) | eval, BUT these 12 lines are the atlas's own TUNE lines (atlas/no87_map.py `TUNE`: cluster names and the 309 per-tile overrides in labels.json were set from them) | yes: the family atlas, `classify --boxes` (added this job) |
| vivonne1573-f102r L03,06,09,11,12,15,17,21,22,23,26,27 | vivonne1573-f102r-dev (302 scored on these lines) and -dev2 (447) | dev | none: no atlas for the Saint-Gouard hand; building one needs box-to-truth alignment, the thing under test |
| luzerne108a-p1 L01-L11 | luzerne108a-p1 (64 scored of 115, truth at the digit-GROUP level) | dev | none: a digit hand, no atlas, no digit-level truth |

So the full pipeline test runs on Birago only; Vivonne and Luzerne get the brief's proxy. On Birago the absolute figures are optimistic
(tune-line contamination of the atlas labels, which no classification here can undo); the endpoint is therefore the PAIRED difference
between two arms classified under one and the same atlas, which the contamination affects equally.

## Hypothesis
H1: replacing the machine boxes by the owner's corrected boxes (11 trashed page-edge shadows, 3 re-cuts) lowers the atlas-top-1 err_true
on f178v L01-L12. H0: no change beyond what the same number of random edits produces.

## Arms (Birago; all from oracle1/boxes/boxes_recut_all.tsv rows hand=birago1572-no87, the 343 tiles of the owner's page)
- **machine**: the 343 boxes as built; kind=mark boxes (3) are excluded from the scored sequence in EVERY arm (the atlas treats a mark as
  an attribute, the no.87 truth has no mark sign); reported beside with marks included.
- **owner**: machine minus the 11 `not-letter` tiles (settled.tsv), the 3 `recuts.tsv` rows applied (new_x,new_y,new_w,new_h in the
  crop's own pixels, same frame as the box list). Decomposition reported: trash-only and recut-only.
- **control** (CLAUDE.md rule 3): the owner's edits applied to randomly chosen boxes of the same size distribution, 20 seeds: for each
  trashed box, delete a random untrashed box whose area is among the 10 nearest to it (without replacement); for each re-cut, apply the
  same (dx, dy, dw, dh) to a random untouched box among the 10 nearest in area (clipped to the crop). Proof it can vary on the statistic:
  deleting a box that carries a true sign adds a deletion to the edit-distance score, so the control's err_true can go UP where the
  owner's goes down (the owner's 11 trashes are last-of-line boxes the line readers never read as signs: passC on these lines has I 0);
  the same shuffling cannot, by construction, leave the sequence identical to the owner's unless it picks the same boxes, probability
  ~0 over 343 choose 11.
- Classification: `python3 tools/glyph_atlas.py classify --out ciphers/nevers-birago-fr3251-1572/atlas --labels <atlas>/labels.json
  --boxes ARM.tsv --tsv ARM.k.tsv --topk 3 --boxes-median-h 68` (68 = pages.json median_h of the atlas's f178v page, so the size features
  of every arm sit on the atlas's own scale; the same value in every arm). The output sequence per line = kind=sign boxes in reading
  order (box_id order), sign = k1. Nothing else differs between arms.

## Endpoint, scorer, gate
- `python3 tools/tx_bench.py ARM.out.tsv --item birago1572-no87 --coverage-diagnostic` (12 of 27 lines: the diagnostic mode lists the
  15 missing lines and does not score them as deleted), as measured AND `--exclude-flagged`, Wilson 95%; `--paired machine.out.tsv`
  for the owner arm.
- Gate: PASS if owner err_true < machine err_true AND the owner's paired improvement (fixed - broken) exceeds the control's at 19 of 20
  seeds (p <= 0.05 one-sided against the control distribution) AND the control's mean is not below the machine's (a control that
  improves on its own would say the segmenter, not the owner, is the cause). Else FAIL or NON-TEST (if the control cannot vary: it can,
  see above). A null is a result.
- Stop rule: Birago classified once per arm (23 classify calls, all scripted, no reader, no vision call); no re-tuning of knn, median_h or
  the mark rule after a number is seen; if the machine arm itself fails to classify (tool error) the job stops and says so.

## Proxy for the hands without a pipeline (brief: "where nothing overlaps, say so, then measure the nearest proxy")
1. Cut-error share: S / D / I of the existing benchmark outputs on exactly the oracle lines (tx_bench --coverage-diagnostic), already
   read before this PREREG as part of finding the overlap -- Vivonne dev 12 lines: committed S120 D0 I0, passA S117 D4 I0, passB S123 D2
   I0, passZ_dv1 S130 D3 I14; Luzerne: every output S6 D0 I0 on 64 scored groups. Reported as the share of errors that are cuts.
2. Count proxy per line (scripted, blind to values): machine box count vs owner box count vs the reference count of units on the line
   (Vivonne: the truth file's positions per line, all statuses, i.e. the committed read's tokens, marks included since ':' is a sign of
   this hand; Luzerne: digits in the committed read per line, since boxes are digits and truth positions are groups). Statistic: sum
   over lines of |boxes - reference|; owner edits = trash (not-letter) + aside + Vivonne merges (-17); BAD-CUT is "could not judge" by
   the owner's own rule and is kept as a machine box. Control: the same number of random deletions per line, 200 seeds, same statistic.
   Reported as numbers; it is a count-agreement proxy, NOT accuracy (LESSONS.md "Look-alike pass"), and said so.
3. The 11 Vivonne merges: Vivonne has dev truth but no pipeline, so their effect is reported through proxy 2 only (count moves toward the
   reference or away), never as err_true.
Position-level "do the owner's re-cuts sit at cut-error positions" needs a box-to-truth-position alignment on Vivonne and Luzerne that
does not exist; it is named as the next step with its cost in RESULTS.md, not improvised here.

## Blind rules
The oracle pages and answers are read, never written; no truth value or label is written near them; nothing is published; the owner is
not contacted. Openings of eval truth: tx_bench reads birago1572-no87.truth.tsv (eval) on 12 tune-contaminated lines -- declared here
as a scorer opening for a paired cut comparison, not a look at a frozen confirm item (none is touched: vivonne1573-f103r-confirm2 is not
read).
