# PREREG MERCY-CEIL (17 Oct 2026, written before the scenario numbers were computed)

Worker MERCY-CEIL (account 4), brief `.claude/briefs/runs/2026-10-17-acct4-research-director-1.md` "## JOB MERCY-CEIL".
Question: is a D2 cipher clause (an H/C/S stretch longer than the authentication distance) reachable on Espagnol 144 f.22 by
settling the 28 remaining M positions, before anyone pays for readers? Disk only; no reading, key or AUDIT.md edit.

## Instrument
Scratch copy of `mercym33/runs.py` (longest run of letters with every token H/C/S inside one cipher segment) on a scratch
reading_tokens.tsv in which the named positions are set to S, letter values unchanged (run length counts letters, so the
value chosen for a 1-letter token does not change it; r10:8 counts 2 letters, r10:14 counts 0 as committed).

## Scenarios (positions fixed here, before running)
- (a) committed: 28 M as on disk.
- (b) every M that DV-MERCY2's rule could grant S: out-of-range one-parse clusters (none left) and the companion rule (two gated
  blind readers reading the glyph identically, own group). Split in two:
  - (b0) licensed now from files on disk: positions where `mercyimg/readA_tokens.tsv` and `readB_tokens.tsv` already agree, own group,
    and the key code read is itself S in key.tsv.
  - (b1) b0 plus every legibility-only M (key code S, no in-range glue, no sense re-cut) that a gated re-read could settle:
    r04:17, r06:14, r14:7, r16:3, r16:6, v01:15, v07:15-16 (if readers confirm two own groups).
  Never grantable by readers (stay M in b): key-level M codes (25 at r09:7 r16:9 r17:4 r19:10; 9 at r06:7; 15 at v04:9 v04:19;
  [MARK:frac] v01:6; [MARK:box] r07:5 r09:6) and in-range segmentation / sense re-cuts (r18:5-6, r20:6-7, r24:14-15, r10:8,
  r10:13-14).
- (c) ceiling: every M as transcribed (all 28 set to S).

## Gate
The brief's bar, AD = 125.9 letters (es17c, DV-MERCY2, 28 liberties). Beside it I report the AD recounted for each scenario's own
residual liberties (AD = 1.5 x (149.3 + M_left) / 2.114, DV-MERCY2's figures); if the decision differs between the two bars I say so
and the verifier decides, I do not.

## Decision
- (b1) >= 126: name the exact positions whose gated re-read licenses the clause, price it from MERCY-IMG's ledger row, as MERCY-IMG2; stop.
- (b1) < 126 and (c) >= 126: name the in-range clusters / key-level codes in the way and what instrument other than sense could cut
  them (spacing statistics across the letter with a control; the writer's habit on out-of-range clusters; code 25's value test).
- (c) < 126: the clause route is closed for this item; D2 needs a different route (new material, the code clause).

## Results (17 Oct 2026, 00:5x UTC by date -u; computed after the block above was pushed, commit 84bb874c6)

Scratch copy of `mercym33/runs.py`, positions set to S on the command line; on-disk files read only.

| scenario | positions set S | M left | longest H/C/S run (letters, span) | vs 125.9 | recounted AD (es17c) |
|---|---|---|---|---|---|
| (a) committed | 0 | 28 | **89** (r20:8-r24:13) | below | 125.9 |
| (b0) licensed now | 1 (r17:5) | 27 | **89** (r20:8-r24:13) | below | 125.1 |
| (b1) + every legibility M a gated re-read could settle | 9 | 19 | **89** (r20:8-r24:13); next 77 (v05:1-v09:6) | below | 119.4 |
| (c) ceiling, all 28 as transcribed | 28 | 0 | **393** (r13:14-v09:6) | above | 105.9 |

Finding on file evidence (b0): r17:5 is already settled by the companion rule -- both MERCY-IMG gated readers read 14, own group
(`mercyimg/readA_tokens.tsv`, `readB_tokens.tsv`: reader_digits 14, own_group 1), and 14 = c is S in key.tsv. DV-MERCY2's 13 did not
list it. It lies outside every candidate run, so it moves no number; for the verifier/parent, not applied here.
Conflict found (not settled): r16:3 and r16:6 carry exceptions.tsv value c (open 14, Bourdeau 1 Oct 2026), but both gated readers read
19 (own group) at both positions. Two gated readers against an image re-read: an M either way, logged, not resolved.

Sensitivities (what the 89-run is waiting on; its bounds are r20:6-7 on the left, r24:14-15 on the right):
| settled | run |
|---|---|
| r24:14-15 (26 vs 2 6) | 103 |
| r20:6-7 (23 vs 2 3) | 106 |
| both in-range clusters r20:6-7 + r24:14-15 | 120 (stopped by r19:10, code 25) |
| r20:6-7 + r19:10 (code 25) | **132** (r18:7-r24:13) |
| r20:6-7 + r19:10 + r18:5-6 | 156 |
| all three in-range clusters + r19:10 | 170 (DV-MERCY2's figure, reproduced) |
| b1 + code 25 only (no in-range cluster) | 94 |

## Decision (as pre-registered)
(b) < 126 and (c) >= 126: **the clause is reachable in principle but no reader job can license it.** Paying readers is not the next
step: every legibility-only M lies outside the 89-run or adds nothing to it (b1 = 89). The smallest set that crosses the bar is two
items, neither a legibility question: **r20:6-7** (an in-range cluster, 23 = o vs 2 3 = o p; the two gated readers already split, A two
groups, B one; if 23 the run is 131, still above) and **r19:10** (code 25's value, key-level M; MERCY-M33's K25 test rejected u at n = 4,
non-decisive). Without code 25 the ceiling on this side is 120, under 125.9 and under its own recounted AD (about 121).
Instruments other than sense:
1. r20:6-7 -- a spacing statistic across the whole letter with a control: measure the gap inside the six known glued clusters (72, 52,
   48, 48, 186, 65; S by the out-of-range rule, the positive class) against ordinary between-token gaps (the negative class) on the
   existing crops, gate it on held-out known pairs (it must separate them before it is read on r20:6-7, r18:5-6, r24:14-15), then read
   the three in-range clusters. Disk only, crops exist (mercyimg/crops), no reader calls if done by pixel measurement.
   The writer's habit is weak evidence on its own: every glued pair on file is code + single digit, which fits 2|3 and 2|6 as well as 23/26.
2. r19:10 -- code 25's value is a key question, not a reading: a sibling in the same key (the 15 April 1648 Brussels letter, ASKS row
   60 / SEND-QUEUE S3) or a period key; a re-run of the K25 value test at larger n is not possible on this letter (4 occurrences, one of
   them the r10:8 re-cut). A licence for 25 = u at this one position would itself be a liberty the AD already counts.
So D2 by the cipher clause needs (1) a gated spacing instrument for r20:6-7 **and** (2) new key evidence for code 25. Next job named:
MERCY-GAP (pixel gap statistic with the glued-cluster control, disk only, no vision calls, about USD 2); code 25 waits on ASKS 60.
