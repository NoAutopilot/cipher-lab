# PREREG C1161-HC (account-4 worker, LANE DEFAULT-A4-1035-15, 15 Oct 2026, written 11:1x UTC by date -u, before any line is counted)

Brief `.claude/briefs/runs/2026-10-15-acct4-default-1035-jobs.md` (C1161-HC). Disk only (line pieces under images/, regenerable from the
folder's own crop scripts; nothing fetched), 0 host requests. Prior work: `tools/prior_work.py clair1161-avis-flandre-1688 --item-spec
'S split hand-count' --step-type key --offline` exit 4, LEAD = own work (C1161-SSPLIT/SORT2/RECUT/275): proceed. n/u hypothesis: George
Lasry's key sheet (credit, rule 8).

## Not a third attempt of the same instrument (rule 3)
Localisation of the 275 S ticks has had two instruments: (1) SSPLIT's ink-segment placement (tick on the sign 8/12 on sign 4) and (2) C1161-275's
automatic counting localiser (ink blobs aligned to ciphertext.tsv by DP; L2 18/30 FAIL). This job uses a different instrument: **counting by
eye per line** (the worker views each line's pieces, unstitched, with an x ruler, beside the line's ciphertext.tsv sequence, and places each S
token's tick by counting signs from the line start), the method RECUT used for three windows. The c188L stitching shift that C1161-275 found is
avoided by placing every tick in the coordinates of the single piece (s1/s2/s3) that carries the sign, never on a stitched strip.

## Step 0: hand-count c187L and c188L (53 lines, 126 S tokens)
- `shc/view_line.py` renders a line's pieces with an x ruler (no class, value or prior S result shown); the worker writes `shc/hand.tsv`
  (line, pos, piece, x, y) per S token. Lines in ciphertext order, c187L then c188L. A token the worker cannot place (sign under a blot,
  count lost) is written with x blank and flag `nc` (counts as a placement failure in L2 if sampled; never dropped).
- If budget stops the count before both blocks are done, the counted lines stand and L2 samples from what was counted, provided >= 30
  tokens were placed; under 30 -> no gate, logged as not reached.

## Gate L2 (same design as C1161-275, same gate)
- `shc/cut_hc.py` cuts RECUT/275-format windows (+-2 sign pitches, band +-90 px, upscaled, red tick top and bottom) from the piece at the hand
  position; 30 random hand-placed tokens (random.Random(2750).sample over hand.tsv rows in file order; all of them if exactly 30), shown under
  E01..E30 with no line/pos label. The worker marks each "on" (tick on an S-shaped sign, either form) or "off"; no O/L class written.
  **PASS iff >= 26/30 on.** `nc` rows sampled count as off.
- Caveat stated now: the placer and the checker are the same worker (as in C1161-275's L2); the check is done after all counting, on shuffled
  unlabelled windows.

## After L2
- **L2 FAIL** -> stop; the localisation step is logged [retired] with both instruments named (automatic counting localiser C1161-275; hand count
  C1161-HC), per rule 3's third-attempt clause (three localisers tried: ink-segment, counting DP, hand count); the S split stays as RECUT left it.
- **L2 PASS** -> extend the hand count to the remaining 62 S lines (c185R, c186L, c186R, c187R) only as far as this job's cap and box allow
  (stop before a unit crossing 80%); the blind readers, gate K exactly as registered in ssplit/PREREG-C1161-SSPLIT.md, A, T, reconciliation and
  the registered --try run only once all 275 are hand-placed (s275/PREREG-C1161-275.md steps 1-2 unchanged, windows from hand.tsv). Whatever is
  not reached is handed on as the named next step. Nothing goes into ciphertext.tsv or key.tsv in this job unless step 2 of that PREREG is reached.
Cap USD 5, box 90 min (11:08-12:38 UTC); stop before a unit that would cross 80% of either. Images stay in the session scratchpad.

## Addendum A (11:1x UTC 15 Oct by date -u; written after L2 was scored)
- Hand count done for all 126 S tokens on c187L (69) and c188L (57), pushed (059468e26) before the eye montages were looked at; 2 flagged
  `edge` (S at a piece edge), none `nc`. **L2 29/30 PASS** (gate 26; shc/L2_check.tsv; the one off is E25 = c188L_L11/30, an `edge` row
  whose S is clipped by the s3 piece edge). Caveat as registered: placer and checker are the same worker.
- Extension to the other 62 S lines: not started. The worker cannot read its own cost; its estimate of the context spent on 53 line views
  plus the eye check puts it near 80% of the USD 5 cap, so per the PREREG it stops before that unit. Handed on as the next step.
