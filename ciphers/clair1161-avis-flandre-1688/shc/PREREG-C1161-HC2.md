# PREREG C1161-HC2 (account-4 worker, LANE DEFAULT-A4-1035-15, 15 Oct 2026, written 11:4x UTC by date -u, before any line is counted)

Brief `.claude/briefs/runs/2026-10-15-acct4-default-1035-jobs.md` (C1161-HC2). Continues C1161-HC (shc/PREREG-C1161-HC.md, L2 29/30 PASS on
c187L/c188L) with the same instrument: counting by eye per line, on the single piece that carries the sign (shc/view_line.py, no class, value
or prior S result shown). Disk only, 0 host requests. Prior work: `tools/prior_work.py clair1161-avis-flandre-1688 --item-spec 'S split
hand-count remaining lines' --step-type key --offline` exit 4, LEAD = own work (C1161-HC): proceed.

## Step 1: hand-count the remaining 62 S lines (149 S tokens): c185R (53), c186L (27), c186R (14), c187R (55)
- Rows appended to shc/hand_raw.tsv (and converted into shc/hand.tsv by shc/cut_hc.py) in ciphertext order, same columns and flags (`edge`
  for an S at a piece edge, `nc` with x blank for a token that cannot be placed; never dropped).
- If budget stops the count early, counted lines stand; the L2 sample is drawn from what was counted provided >= 30 tokens were placed.

## Gate L2 (same design, same gate)
- Fresh sample: random.Random(2751).sample over the C1161-HC2 rows only (the 149 new rows, or what was counted), 30 windows, cut by
  shc/cut_hc.py from the single piece (+-2 pitches, band +-90 px, red tick), shown under E01..E30 with no line/pos label, after all counting.
  The worker marks "on"/"off"; `nc` sampled = off. **PASS iff >= 26/30 on.** Key in shc/eye_key_hc2.tsv, result shc/L2_check_hc2.tsv.
- Caveat as before: placer and checker are the same worker.

## After L2
Stop either way (brief). PASS -> all 275 S hand-placed; readers, gate K exactly as registered (ssplit/PREREG-C1161-SSPLIT.md) and the
registered --try (s275/PREREG-C1161-275.md steps 1-2, windows from shc/hand.tsv) are the next job. FAIL -> the hand count on these lines is
logged as not localising at gate; c187L/c188L stand; named next step decided by the orchestrator. Nothing goes into ciphertext.tsv or key.tsv.
Cap USD 4.5, box 75 min (11:38-12:53 UTC); stop before a unit that would cross 80% of either. Images stay in the session scratchpad.
