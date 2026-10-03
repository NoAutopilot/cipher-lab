# fr.3623 f.23r one-line pilot: pre-registration (DIN-23P, account 1, 3 Oct 2026, written ~10:15 UTC)

Brief: `.claude/briefs/runs/2026-10-03-acct1-din-23p.md`. Committed before any image of f.23r is viewed by this worker.

## Line choice
The brief says "the line with most 0' on DIN-3623's inventory pass". That pass (`f3623/inventory_passA.md`) gives only
whole-slip counts (0' about 10), no per-line split, so the line cannot be read off it. Substitute rule, fixed here:
one selection look (vision call 1) at a contact sheet of the existing two-line band crops L02-L07 (s1+s2, 60% scale,
`pilot/select_sheet.jpg`), counting ONLY stemmed zeros (0': a zero with a stroke rising from it) per cipher row, no other
sign and no gloss read. The cipher row with the highest count is the pilot line; tie -> the row with more total
signs (longer); if every count is 0 the pilot reports "no 0' visible at sheet scale" and uses the middle cipher row (L04).

## Question
On that one line: (Q1) do the 0' tokens sit under s or p of the interlinear Italian gloss? (Q2) do the v' tokens sit
under a or t?

## Method
- Native line crop of the chosen cipher row + its gloss row, cut with `tools/iiif_lines.py --image` from the native region
  already on disk (`f3623/src_ark_12148_btv1b525245007_f55_560_1780_2950_1560.jpg`); command pasted in NOTES.md.
- Two blind sign passes (vision calls 2, 3; Sonnet subagents) on the cipher row only (gloss row masked white), with the
  f.128 label list of `f128/pass_instructions.md` (+ v'), no values, no gloss.
- One gloss read (vision call 4) of the gloss row alone (cipher row masked), letters only, period spelling.
- Consensus sign string: positions where A and B agree after a DP alignment of the two passes; disagreements kept as
  "?" (wildcard).
- Alignment: global DP of the consensus sign string against the gloss letter string (spaces dropped), one sign = one
  letter, gaps allowed (cost 1), match score +2 when the sign's f.128 key_print value (`f128/print_align/key_print.tsv`,
  the meaning column) equals the gloss letter, -1 otherwise; 0', v', NEW signs and ? score 0 against any letter.
  (Italian u/v and i/j are folded.)
- Null: the same DP against every cyclic rotation of the gloss letter string by k letters, |k| >= 5 (rule 3: rotation
  moves which letters sit opposite 0'/v', so the null can differ from the real on both the key-fit and the s/p count).

## Decision rule
- G1 (does the alignment hold at all): fraction of key-valued signs whose aligned gloss letter equals their key_print
  value, real vs rotations. Pass = real fraction > the maximum over rotations. G1 fail -> Q1/Q2 "undecided", no reading.
- Q1: with G1 passed, let n0 = consensus 0' tokens aligned to a letter. "0' sits under s/p" is SUPPORTED if n0 >= 2,
  at least 2/3 of them are s or p, and the real s/p count exceeds the 95th percentile of the rotation null's s/p count.
  REFUTED if n0 >= 2 and at most 1/3 are s/p. Otherwise undecided.
- Q2: same rule for v' and {a, t}.
- Key change: only if Q1 (or Q2) is SUPPORTED with n >= 3; then 0' (v') enters as a separate f.130 key row at grade M
  (one-line evidence, Italian text) and `tools/decode_key.py --check` / the f.130 regeneration is re-run. Otherwise no
  file under f128/, f130/ or firm/ changes.
- Cost: price of the full 6-line alignment job is stated from this pilot's per-call cost (session total / vision calls).
