# PREREG-OBREDCTRY (15 Oct 2026, 11:2x UTC by date -u; worker OBRED-CTRY, account 2, for LANE DEFAULT-A2-1109-15)

Pushed in its own commit before any statistic is computed. Inputs as on origin/main at cae642f7c: OBRED-SEG's 20 word leads
(`obred187/seg/seg_92_187.tsv`, unchanged), its decoder `seg.decode` and lexicon, OBRED-BAND's pooled pairs and `interval()`,
`obred187/structure.json` (runs, clear context before/after), `tools/data/nl16`, the letter's clear prose (ciphertext.txt pp.110-111,
numerals and editor's lines removed). Disk/CPU only, 0 requests. Disclosure: this worker has read seg_92_187.tsv and the run contexts
(as OBRED-SEG did); nothing has been scored.

`decode_key.py --try` does not apply: the target has no key.tsv / decode.json (letters are band intervals, not key values). The brief's
fallback, a lattice scorer, is used: one fixed decoder, identical on target, nulls and control.

## Context model and lattice scorer
Character 4-gram over ALPHA (`abcdefghiklmnopqrstvxyz`, i/j and u/v/w folded) + space, interpolated orders 4/3/2/1 with weights
0.4/0.3/0.2/0.1, add-0.1 smoothing per order, log2. Target corpus: the five nl16 files + the letter's own clear prose.
Viterbi over a letter sub-run (OBRED-SEG's 13 sub-runs, split at name codes 588-751): emission 0 bits for a letter inside the token's
interval, 3 bits one alphabet step outside, 7 bits any other letter; an optional single space between tokens (scored by the LM);
the sub-run is word-aligned at both ends. Context: prefix = the last 12 folded characters of the clear text before the run (first
sub-run of a run) or a space (after a name code); suffix = space + the first 12 folded characters of the clear text after (last
sub-run) or a space. F(pins) = best log2 score with pinned tokens restricted to their pinned letter (emission 0).

## Lead tests
- Self (context score, reported, not gated): dself = F(free) - F(lead span pinned to the lead word), bits per letter.
- Every occurrence (the gated test): for lead L (codes c_i, letters l_i), other occurrences = every token in the 92/187 letter
  sub-runs carrying one of L's codes, outside L's own span. A code read with two different letters inside L = break. For each
  sub-run with >= 1 other occurrence, pin all of them to L's letters: d = F(free) - F(pinned); the sub-run holds if d <= 3.0 x
  n_pinned bits. L holds if every affected sub-run holds; L is testable if it has >= 1 other occurrence; untestable otherwise.
- Per-lead random-assignment null (reported, not gated): 200 draws (seed 187) of in-interval random letters for L's codes; share
  that hold.

## Target gate (null a, shuffled band)
100 draws, seed 1605: pool letters permuted over pool codes, intervals recomputed, OBRED-SEG's decoder run (same trie) to give the
null's own leads (>= 4 letters), then the same every-occurrence test. Statistic h = share of testable leads that hold.
Target passes when h_real > p95(h_null). The null can change h (different intervals, leads and pins).

## Synthetic control (must pass before any target lead counts)
OBRED-SEG's control generator (alphabetical homophonic list on 1..587, 41 pool pairs, the target's 13 sub-run lengths, held-out
nl16 file coor001boev01, seed 1600), at the real error level bracketed: e = 0.5 (interval hit ~0.81) and e = 0.75 (~0.71); 20
simulations each. Control trie: the four other nl16 files (as OBRED-SEG). Control LM: those four files + a held-out excerpt of the
same word count as the letter's clear prose, taken from the 40 words before and after each span (spans themselves excluded).
Context = the held-out words before/after each span. Leads from `seg.decode`; a lead is right if it equals the true word at that span.
Report per e: leads, testable, right-lead hold rate, wrong-lead hold rate, precision of testable leads, precision of holding leads.
CONTROL GATE, at both e = 0.5 and e = 0.75: right-lead hold rate >= 0.60 AND precision(holders) >= precision(testable) + 0.10.
Below gate -> the target result is a non-test at this N, whatever it reads.

## Grades and output
Every lead stays M. A holding lead of >= 5 letters is S only if the control gate passes, the target passes null (a), and the
control's precision(holders) >= 0.80 at e = 0.75. Leads that break are reported as breaking (still M leads, not refuted words: one
instrument). Nothing goes into key.tsv (none exists). `obred187/ctry/ctry.py` writes `ctry_gate.json` and `ctry_leads.tsv`;
`--check` exits 1 if stale.
