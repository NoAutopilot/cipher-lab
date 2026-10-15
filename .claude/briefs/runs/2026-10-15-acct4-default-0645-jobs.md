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

## Wave 1 result (07:2x UTC): LVN-EYE 2.55 Q, SUR-TRY 1.86 N, C1161-KA 1.12 F (brief error: disk-only for material not on disk), BAL-EYE 1.71 D.
Pricing lesson: every job pays ~1.0 of fixed start-up (CLAUDE.md + notes reading) before its first unit; caps below include it.

## Wave 2 (07:2x UTC 15 Oct)

### LVN-4611P2 (Opus, cap 9, box 100 min, disk; resources.huygens.knaw.nl <= 4): lodewijk-van-nassau-1573-74 4611 p2 per page-half
NOTES.md ~line 4769 "4611 p2 (252 M rows) per page-half, ~$8". Same protocol, control and gate as LVN-4611 / LVN-L1 (their PREREG addenda);
write a PREREG addendum for 4611 p2 and push it before any read. Two units (top half, bottom half), each: placement + Sonnet reads incl. control
(~0.6 a call) + 1 reconcile; per-unit estimate ~3.5 incl. Opus placement (lodewijk runs ~1.4x a vision-call price). Apply only tokens the half's
own control licenses (rule 3 per-unit merge). Stop before starting a half that would cross 80% of cap or box. decode_key --check after; carry
changes into AUDIT.md; report C/H before and after.

### C1161-LASRY (Opus, cap 2.5, box 60 min, github.com / raw.githubusercontent.com <= 10): clair1161-avis-flandre-1688 Lasry second face
C1161-KA section (NOTES.md ~line 2670). Find Lasry's plaintext for the second face he read in full, in github.com/dbourdeau/cyphersolver (MIT
code / CC BY text, cite it; clone shallow or fetch raw only the `clair1161` paths; Bourdeau's repo, not Aymeloglu's). If found: snapshot the text
(not images) into sources/cyphersolver/2026-10-15-lasry2/clair1161/ with source URL + commit, then the token-level known-answer alignment
(PREREG gate + shuffled control first). If not found: log what was searched and stop.

### BAL-C286 (Opus, cap 3, box 60 min, openapi.bnf.fr <= 8, ROOM take/release): baluze167-davaux-1637 c286 onward for a glossed 7/5
NOTES.md Verdict ~line 3105: "Baluze 167 c286 onward for a glossed 7/5 (~$2)". Same PREREG as BAL-C275G/BAL-C280 (unchanged); Sonnet reader calls
on native regions, eye check only on glossed 7/5/E rows; --try at every occurrence before anything enters key.tsv.

## Wave 2 result (07:5x UTC): LVN-4611P2 7.13 D (p2a only, stopped on its PREREG spend line), C1161-LASRY 1.31 N, BAL-C286 2.03 N.

## Wave 3 (07:5x UTC 15 Oct)

### LVN-P2RETX (Opus, cap 6.5, box 90 min, disk; resources.huygens.knaw.nl <= 3): lodewijk-van-nassau-1573-74 re-transcription of 4611 p2 mixed lines
LVN-4611P2 section (NOTES.md ~line 4851): the 150-dpi boxes mix physical lines p2_L13-L33 (35 physical vs 33 transcribed; runs of ink in no row).
Re-transcribe those lines as LVN-L1 did for p3_L00: deskew, cut one crop per physical line with tools/iiif_lines.py --image (paste the command),
two blind Sonnet passes per line batch (~0.6 a call) + 1 reconcile, insert the missing runs as new rows, keep the old rows' ids mapped in a
TSV. PREREG addendum first. This is a transcription repair (grade unchanged until a settle); do NOT run the p2b per-token settle in this job.
Stop before a batch that would cross 80% of cap or box. decode_key --check after; report rows added/changed and the residual for p2b.

### C1161-SSPLIT (Opus, cap 4, box 75 min, disk only): clair1161-avis-flandre-1688 S tokens open vs looped, --try per split
Verdict NOTES.md ~line 2738: "every S token sorted open vs looped and --try per split, ~$3". Read CL1161-S7 first (do not repeat its exemplar
check). PREREG first; sort by crops in scratchpad (regen from images/manifest.json); --try each split at every occurrence with --try's own power
control (a known wrong value on an H/C code must be rejected AND a hidden right value accepted; if either fails the try is a non-test). Nothing
enters key.tsv on a non-test.

### BAL-E293 (Opus, cap 3, box 60 min, disk; openapi.bnf.fr <= 6 for 169 only): baluze167-davaux-1637 c293 E sign identity, then 169 glossed 13:/65
Verdict NOTES.md ~line 3150: (a) the c293 E beside the c268 ball-foot E exemplars and the c275 E -- same sign or not; if the same, run --try with
"E = null" as the hypothesis against E = e, power control first (~0.8). (b) then, if >= 50% cap left, a glossed 13: and plain 65 on Baluze 169
f.36-38 / f.208-209 (~2), same PREREG family as BAL-C275G. Nothing into key.tsv without --try at every occurrence.
