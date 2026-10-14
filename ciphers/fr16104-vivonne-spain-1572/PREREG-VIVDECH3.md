# PREREG-VIVDECH3 (14 Oct 2026, 04:3x UTC by date -u; VIV-DECH3, account-2 dispatched worker for LANE VIV-KEYSTONE, account 4)

Brief: .claude/briefs/runs/2026-10-13-acct4-keystone-viv-jobs.md, "Account-2 row VIV-DECH3". Written and pushed before any third pass is
read, merged or scored. Measurement only: key.tsv, every reading, status.json and every existing truth item stay untouched.

## Question
About half the scored positions on each truth leaf of this hand carry the flag `clerk-split` (the two blind reads of the clerk's French
disagree at that letter). Does a third blind read of the clerk pages, used as a vote, cut that flagged share?

## Pages (6, the brief's maximum)
| page | canvas, region (openapi.bnf.fr, native) | strips | feeds item |
|---|---|---|---|
| f.205r | c210, 4300,350,3600,5500 | 8 | vivonne1573-f201r-dev (and f201v-dev via the last 401 letters of dec67) |
| f.205v | c211, 150,100,3750,5750 | 7 | vivonne1573-f201r-dev, vivonne1573-f201v-dev |
| f.206r | c211, 4050,300,3800,5600 | 8 | vivonne1573-f201v-dev |
| f.206v | c212, 150,100,3750,5750 | 7 | vivonne1573-f201v-dev |
| f.108r | c111, 4200,150,3950,5650 | 8 | vivonne1573-f103r-confirm2 |
| f.108v | c112, 700,150,3600,5650 | 7 | vivonne1573-f103r-confirm2 |

Why these two ink-41 pages: under the frozen confirm2 alignment (`build_vivonne_confirm2.py --offsets`), the 1,068 scored f.103r positions sit
on dec_norm letters 6865-9553 = f.107v 29, f.108r 422, f.108v 617. f.102r (dev2, window dec_norm 550-3250) needs ff.105v-106v, three more
pages, which the six-page limit does not allow; vivonne1573-f102r-dev2 is NOT rebuilt (its 2-vote figure is reported unchanged).
f.211r (ink 71 pages ff.215r-215v) is not in the brief's page list and is not touched.

## Pass C
One fresh blind Sonnet subagent call per page, on ink-minimum strips cut by `tx/viv67_strips.py` from the native region (halves sharing
400 px), with the prompt of `tx/DEC_READ.md` unchanged. Blind: the reader sees no earlier pass, no truth, no cipher, no decode. The reader
returns its text in its reply; this worker writes `tx/dec_<page>_passC.txt` (refusal rule of 14 Oct: no subagent writes a file). No image
goes into git; images/manifest.json gains a "vivdech3" entry with the exact regenerate commands.

## Three-vote rule (tx/vote3.py, written before pass C is read)
Per page, words of A and B are aligned as tx/merge_dec.py does (difflib on `merge_dec.norm`). C is aligned separately to A and to B the same
way; a word of A (or B) is "supported by C" when it lies in an `equal` block of the A-C (B-C) alignment.
- `equal` A=B block: words of A kept, agreed (as before; C dissent does not unflag or flag: 2 of 3 already agree).
- `replace` block: the side with more C-supported words wins (tie: merge_dec's doubt rule, ties to A); each kept word is agreed iff it is
  C-supported.
- `delete` (A only) / `insert` (B only) block: the words are kept (as merge_dec does); each is agreed iff C-supported.
- A word with a doubt mark ('?' or '<?>') is never agreed (as before).
- A page with no pass C: the old two-vote rule, unchanged.
The merged text of each page becomes `tx/dec_<page>_merged3.txt`; the letter streams `tx/dec_norm3.txt`, `tx/dec67_norm3.txt`,
`tx/dec67b_norm3.txt` (the existing streams with the three-vote pages substituted). The mask is mapped onto the stream letter by letter as
the builders' clerk_mask does.

## Rebuild
`benchmark-tx/build_vivonne_vote3.py` re-runs the three existing builders (build_vivonne_f201r.py, build_vivonne_f201v.py,
build_vivonne_confirm2.py, imported, code unchanged) with the three-vote text and mask swapped in, and writes NEW items
`vivonne1573-f201r-dev-3`, `vivonne1573-f201v-dev-3`, `vivonne1573-f103r-confirm2-3` (truth, sha256, outputs dir) beside the old ones,
never replacing them; `--check` exits 1 if stale. Each builder's own alignment control is re-run on the new text and printed in the header.

## Registered outcome (reported whatever it shows)
Per item, old (committed) vs -3: (1) the flagged share on scored positions (any flag; and clerk-split alone); (2) scored count; (3) passA and
passB err_true from tools/tx_bench.py, as measured and flagged-excluded; (4) the alignment control (real share, p95, rank).
Also per page: C's word agreement with A and with B, C's agreement on the A=B words (a competence check), and how many A/B disputes C
settled to A, to B, or to neither.
Interpretation (pre-registered): a drop of >= 0.10 in the clerk-split share on an item, with the null below, counts as "the third vote cuts
the truth's noise materially" for that item; a drop < 0.05 counts as "no material change".

## Null (rule 3: a control that can differ from the target)
The same rebuild with each page's pass C replaced by the pass C of a DIFFERENT page (rotation: f205r<-f206v, f205v<-f205r, f206r<-f205v,
f206v<-f206r, f108r<-f108v, f108v<-f108r). A wrong-page C can support A or B only by chance word overlap, so its clerk-split drop measures
what the three-vote rule gives with no real third reading; the real drop is reported beside it. The null writes nothing to git.

## Stop rule
Stop before starting a page whose subagent call would cross 80% of the cap (10) or of the box (04:12-06:12 UTC; 80% at 05:48). If fewer than
six pages are read, items whose pages all have C are rebuilt; an item with a page missing C is rebuilt only if at least one of its pages has
C, and the report says which pages voted three ways.
