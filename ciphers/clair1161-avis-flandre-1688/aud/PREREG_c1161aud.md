# PREREG D2-C1161AUD (account-1 worker for LANE-D2PUSH), written 5 Oct 2026 19:0x UTC by date -u, before any re-read or score

Brief: .claude/briefs/runs/2026-10-05-acct1-d2-c1161aud.md. Target: planted agreed-token audit on th/z/S/4 (TX-AGREEAUDIT).
Question: how many th/z/S/4 tokens that BOTH blind readers agreed on (invisible to D2-C1161LA's split-tile pass) does a
value-blind reader relabel, with planted known-wrong labels as the positive control.

## Items (aud/run_audit.py, fixed: seed 51)
- Pool: la/align_abc.tsv status 'agree' with merged label th/z/S/4 (D2-C1161LA's alignment; about 829 tokens: 4 222, S 266,
  th 197, z 144). `lookalike_pass.audit` (the tool's code; the wrapper only narrows its agreed pool) with --sample 120,
  --plant 0.17 (= 20 plants), --k 3, --hide-passc. A plant swaps the shown label to the label's most frequent confusion
  partner in la/confusion.tsv (z->tz, S->s, th->dia, 4->qb). Hidden answers in aud/c1161aud_audit_items.tsv.
- Instrument: `tools/lookalike_pass.py windows --items aud/c1161aud_audit_items.tsv --passc la/passC.tsv --manifest
  la/crops/manifest.json --crop-pattern '{line}_s*' --out aud --run c1161aud_win --per 10 --scale 1 --desc la/desc.tsv`
  (label hidden, candidates alphabetical, shapes from tx/labels_v2.md via la/desc.tsv). Per-item windows cut from the
  existing native line crops (made by the iiif_lines.py commands in NOTES.md / la/PREREG_c1161la.md); never a full page.
  Note: the reader never sees the shown label, so "flag" = picks a candidate other than the shown one.

## Pricing (Usage 6, per pass)
- 3 Sonnet subagent calls of 40 windows (4 montages each), est. USD 0.6 per call = 1.8; one value-blind reader; scoring is
  the script (audit-score). Cap 4; stop before a call that would cross 80% (3.2).

## Control gate (fixed; rule 3)
`python3 tools/lookalike_pass.py audit-score --items aud/c1161aud_audit_items.tsv --reread aud/reread.tsv` (tool rule: flag =
re-read label != shown at H or M; planted catch = flagged AND re-read == original). Gate: catch >= 0.80 (the tool's own
gate; stricter than the brief's 0.70, so it satisfies both). Below it the audit is a NON-TEST and no unplanted figure is
interpreted. Rule-3 check: plants and unplanted items are read by the same reader in the same montages; the catch rate can
differ from the unplanted flag rate (it is a different statistic on different positions), so the control can fail.

## Reported (if the gate passes)
- Unplanted flag rate (flags / unplanted items) with a binomial 95% interval, per label, and extrapolated to the ~829 pool.
- Relabel classes: (shown -> re-read) pairs among unplanted flags.
- Systematic class = >= 10 unplanted flags of the same pair in this sample. Only then: ONE run of D2-C1161LA's
  registered relabel test (la/la_test.py logic: dG and dJ under unchanged key.tsv vs 50 random same-label relabel seeds,
  gate real > null p95 on both, longest C/S run reported) on that class's flagged positions; applied to ciphertext.tsv only
  on PASS. Otherwise nothing is applied; the flags go to a focus list for the owner's sign sorter.
- One test, no re-tuning after scores; no second reader, no re-sample.
