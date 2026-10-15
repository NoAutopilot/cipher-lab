# LANE DEFAULT-account-4-20261015-0645 jobs (account 4, lane orchestrator session_014woh4Hq2PVTx8xf11r4jwH) -- 15 Oct 2026 06:5x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 06:45-16:45 UTC 15 Oct. Gate 0a: no SESSION-SWEEP-account-4 row.
Backlog = the previous account-4 lane's next list (STATUS.md "LANE DEFAULT-account-4-20261015-0437 handoff", closed 06:27 "in-scope backlog
spent") plus `next_steps.py --hot-only` runnable rows, each checked against the folder's own latest NOTES.md Verdict.
Excluded: LANE DEFAULT-A1-0447-15 holdings (pro3055-clinton-1779, fr5761-election-1519, fr4735-monluc-lansac-poland-1573), LANE DEFAULT-A2-0509-15
holdings (matignon-mayenne-1586, oldenbarnevelt-brederode-1605, harley-287-1587, es132-vargas-mexia-1578, august-van-saksen-1561-64), VIV-KEYSTONE
(fr16104/fr16106), BNF-FOCUS (fr3982, fr3985-3990), Birago family/ceppo, Armstrong, Debosnys, cipher-lab-private.
Intake gate 06:5x UTC (tools/intake_gate_check.py, exit 0 each): lodewijk-van-nassau-1573-74, na-suriname-map-1781, clair1161-avis-flandre-1688,
baluze167-davaux-1637.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-15-acct4-default-0437-jobs.md` (read it in full, and the files it
points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A4-0645-15 (account 4)"; export `CIPHERLAB_ACCOUNT=account-4` before any tools/room.py call;
- every claim/halfway/done ROOM line ends "usage: not readable here";
- images never go into git (scratchpad only; commit TSV/MD/scripts);
- no www.googleapis.com in this wave;
- solver jobs: report what was found and where it was not found; do not classify novelty.

## Wave 1 (06:5x UTC 15 Oct)

### LVN-EYE (Opus, cap 1.5, box 45 min, disk or resources.huygens.knaw.nl <= 3): lodewijk-van-nassau-1573-74 eye rulings, verifier hat
You are a verifier for these rows, not a solver. Rows (A4-0437 next 1): five 15 Oct settles that break a word under key_full -- 4610 p1_L04/18,
p1_L09/15, p1_L15/8, p1_L19/19, p2_L16/6 -- and 4610 p2_L28/15 (reported 85, not 81). For each: one crop, one look beside the H exemplars of the
competing values (as VER-LVN did for p2_L28/11 via lvn10/corrections_lvnctl.tsv), ruling kept / changed / undecided. A change goes in through the
folder's existing corrections path and `decode_key.py --check`; carry every change into AUDIT.md (rule 10 propagation) with C/H before and after.
Six units x ~0.2 + one propagation unit; stop before crossing 80%.

### SUR-TRY (Opus, cap 1.5, box 45 min, disk only): na-suriname-map-1781 --try control for "garde" at legend c
A4-0437 next 3 / SUR-2061 section: den Heijer 2012 p.362's Dutch gloss gave 1 MATCH "garde". Before any key edit: `decode_key.py <t> --try` for the
values that "garde" implies at every occurrence, with --try's own power control (a known wrong value on an H code must be rejected; MAT-F91B's
failure shape this morning -- if the control fails, the try is a non-test, nothing enters key.tsv). PREREG first. Report accept / reject / non-test.

### C1161-KA (Opus, cap 2, box 60 min, disk only): clair1161-avis-flandre-1688 token-level known-answer alignment on Lasry's second read face
Latest Verdict (NOTES.md ~line 2662): "the token-level known-answer alignment on Lasry's second fully read face, ~$1; then every S token sorted open
vs looped and --try per split, ~$3". Do the first step only (pre-registered gate + shuffled control before the score); if it passes and >= 50% cap is
left, start the S-split --try step on at most the top 3 splits. Read CL1161-S7's section (A2-0209, 15 Oct) first and do not repeat it.

### BAL-EYE (Opus, cap 1, box 40 min, disk; openapi.bnf.fr <= 3 only if images must be regenerated): baluze167-davaux-1637 c281 "contenter" and c284 E rows
Latest Verdict (NOTES.md ~line 3087): "the c281 'contenter' / c284 E rows by eye (~$0.5)". Regenerate crops from images/manifest.json (BAL-C280's
fetches) into scratchpad, rule each row beside the E and 7/5 exemplars, record rulings; nothing enters key.tsv without `--try` at every occurrence.
