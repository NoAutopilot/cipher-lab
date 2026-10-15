# PREREG-VIVLOOKALIKE (15 Oct 2026, 02:1x UTC by date -u; worker VIV-LOOKALIKE, account 2, for LANE VIV-KEYSTONE, account 4)

Brief: .claude/briefs/runs/2026-10-15-acct4-for-acct2-jobs.md "JOB VIV-LOOKALIKE". Pushed before any dedup or lookalike count is computed.
Disk only, no network, no readers. No committed reading, key.tsv, rec file or status.json changes: every output goes to tx/viv_lookalike/.

## Part 1 -- overlap-dedup rule (fixed here, before any scan)

Shape: a line is cut into s1/s2 (s3) crops whose boxes overlap (ink 63: s1 [x0, x0+1600], s2 [x0+1120, x0+2720], about 480 px shared);
a reader who writes both crops in full writes the shared signs twice, back to back. Named instances: f.192r L06, L34; f.193r L07.

Rule DEDUP (applied per pass, per line, to the cleaned token row tx/<page>_pass{A,B}_c.tsv, i.e. after tx/viv63_clean.py's own steps):
1. Find every immediately repeated block X X in the token row: X a run of k consecutive tokens, the next k tokens identical, token for token,
   with 4 <= k <= 12 (exact match only; no near-repeats).
2. The junction (index of the first token of the second copy, as a fraction of the row's length) must lie in [0.20, 0.80] -- the band that
   holds every crop junction for 2- and 3-segment lines.
3. Among qualifying blocks take the longest k (ties: leftmost); delete the second copy (k tokens); repeat on the shortened row until none
   qualifies (so a block written three times loses two copies, never the first).
4. Nothing else changes. DUP rows, [PLAIN:], '[...]', 'Il non', π->P handling stay as tx/viv63_clean.py does them.
The scratch build is tx/viv_lookalike/viv63_clean_dedup.py (a copy of tx/viv63_clean.py plus DEDUP behind --dedup, writing to
tx/viv_lookalike/, never over tx/<page>_pass?_c.tsv). The parent decides whether DEDUP enters the build.

## Known-answer check (truth leaves of the same hand with the same crop/overlap shape)

Leaves: f.201r, f.201v (ink 67), f.211r (ink 70) -- benchmark-tx/vivonne1573-{f201r,f201v,f211r}-dev.truth.tsv, whose ref_sign stream equals
tx/<leaf>_rec.tsv line for line (checked before this file: 25/25, 32/32, 10/10 lines identical).
DEDUP is run on tx/<leaf>_pass{A,B}_c.tsv. For each block it removes, find the same 2k-token sequence X X in the committed line of
tx/<leaf>_rec.tsv (nearest occurrence to the pass index). Then, from the truth file's status column over those 2k positions:
- **violation** = more than k of the 2k positions are `scored` (the clerk decipherment aligns letters to both copies: the truth keeps the
  repeat, so removing a copy removes a kept position);
- strict count (descriptive, not the gate): `scored` positions inside the second copy itself;
- a block whose X X is absent from the committed line (one reader only wrote it twice and the reconciler did not keep both) is listed as
  "not in committed stream" and cannot violate (the committed stream never held the duplicate).
If DEDUP removes no block on any truth leaf, the known-answer check is vacuous and is reported as a non-test, not a pass.

## Gate

PASS iff (G1) zero violations on the three truth leaves AND (G2) err_2reader on f.193r after DEDUP <= before (0.297, tools/reconcile_passes.py
default settings, 1 - sum(agree)/sum(columns) over rec_f193r/agreement.tsv). G1 vacuous -> verdict "G1 non-test", whatever G2 says.
Reported beside the gate (descriptive): per ink-63 leaf (ff.190r-194r) err_2reader before/after, H/M/U counts and the longest all-H run
(longest run of consecutive H grades within a line in the tx/viv63_decode.py build, letters and line) before/after, blocks removed per pass.
Control for the count: the same DEDUP on the truth leaves' passes is the matched control (same hand, crop shape and readers); a removal count
there with zero violations is the evidence the rule does not eat real text.

## Part 2 -- lookalike pairs (r/z, 2/z on f.193v; c/e, 6/b on f.192r)

`tools/lookalike_pass.py confusion` on two-reader splits converted from tx/rec_<page>/ciphertext_draft.tsv (why=differ rows -> idA, idB,
status=split, passage=line, posA=position), ink 63 ff.190r-194r and tx/viv63_f191 passes C/D where on disk. The 2-of-3 `packet/windows/
reconcile` steps need a third read of crop windows; the ink-63 crops are not on disk (untracked) and this job has no readers and no network,
so the settlement step is not run here: reported as not-attempted with its next step and cost. The lookalike pass's 2-of-3 residual is
agreement, not accuracy (CLAUDE.md Usage 6) -- no such figure is produced or quoted here.
Descriptive known-answer lead (not a rule, not a key edit): on the three truth leaves, for every two-reader split on one of the four named
pairs at a `scored` position, which reader's label the truth's accepted set contains (A only / B only / both / neither).
