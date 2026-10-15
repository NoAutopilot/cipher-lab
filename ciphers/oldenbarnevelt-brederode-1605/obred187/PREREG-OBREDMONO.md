# PREREG-OBREDMONO (15 Oct 2026, 11:4x UTC by date -u; worker OBRED-MONO, account 2, for LANE DEFAULT-A2-1109-15)

Pushed in its own commit before any statistic is computed. Inputs as on origin/main at ec3230aea: OBRED-SEG's 20 word leads
(`obred187/seg/seg_92_187.tsv`, unchanged), its decoder `seg.decode`, `seg.lexicon`, `seg.target_subruns`, OBRED-BAND's pooled pairs
(`pairs556`, `leaf_pairs` 555 + 556, 41 pairs) and `interval()`, `synth_list()`. Disk/CPU only, 0 requests. Disclosure: this worker has
read seg_92_187.tsv, ctry_leads.tsv and the 41 pool pairs; no monotonicity count has been computed.

## Idea
The 1619 list is (OBRED-BAND's assumption) an alphabetical homophonic list: code order implies letter order. Each lead implies
code -> letter assignments; a set of leads that are right cannot contain two assignments with c1 < c2 and l1 > l2, nor one code read with
two letters. Leads come from LM-driven segmentation inside band intervals, which is blind to the order of codes inside a pool gap, so
wrong leads place letters inside a gap in random order.

## Units and statistic
- Slot = one lead token (code c, folded letter l, lead id). All 20 leads (>= 4 letters), every token, name codes are already outside.
- Gap key: c itself if c is a pool code; else the index of the pool gap (bisect over the distinct sorted pool codes).
- Discordant pair of slots: (c1 < c2 and l1 > l2) or (c1 == c2 and l1 != l2), letter order = ALPHA index. Every unordered slot pair
  counts, same lead or not.
- D = number of discordant slot pairs. Slot-vs-pool-anchor discordances (possible only through edge letters) are reported, not gated.

## Null (varies on the axis the statistic measures, rule 3)
Within each gap key, the letters of that key's slots are permuted among its slots (1,000 draws, seed 4562); codes, gap membership,
letter multiset per gap and every interval/edge property stay fixed; only the code-to-letter order inside a gap changes, which is
exactly what D measures. Target p = share of draws with D_null <= D_real. Target passes when p <= 0.05.

## Per-lead flag
A lead is testable if one of its slots shares a gap key with another slot (any lead) that has a different code, or the same code in a
different lead. A testable lead is clean if it is in no discordant pair, contradicted otherwise.

## Synthetic known-answer control (must pass before any target number counts)
OBRED-SEG's control generator unchanged in kind: alphabetical homophonic list on 1..587 (`synth_list`), 41 pool pairs drawn with
gloss error e (one alphabet step), the target's 13 sub-run lengths filled from held-out nl16 file coor001boev01, trie of the other four
nl16 files, leads = `seg.decode` words >= 4 letters, a lead is right if it equals the true word at its span. Real error level bracketed:
e = 0.5 (interval hit ~0.81) and e = 0.75 (~0.73), against the real held-out hit 0.73-0.80. 40 simulations per e, seed 1600; each sim
runs the same D and the same null (200 draws). Report per e: leads, testable, right/wrong clean rates, precision(testable),
precision(clean), share of sims with joint p <= 0.05.
CONTROL GATE, at both e: (i) joint p <= 0.05 in >= 0.70 of sims; (ii) right-lead clean rate >= 0.60; (iii) precision(clean) >=
precision(testable) + 0.10. Below gate -> the target result is a non-test at this N, whatever it reads.

## Grades and output
Every lead stays M. A clean lead of >= 5 letters is S only if the control gate passes, the target passes, and the control's
precision(clean) >= 0.80 at e = 0.75. Contradicted leads are reported as contradicted (still M leads, not refuted words: one
instrument). Nothing goes into key.tsv (none exists). `obred187/mono/mono.py` writes `mono_gate.json` and `mono_leads.tsv`;
`--check` exits 1 if stale.
