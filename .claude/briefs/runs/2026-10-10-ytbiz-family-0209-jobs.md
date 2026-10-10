# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261010-0209, "FAMILY-A2n") -- 10 Oct 2026 02:3x UTC, lane orchestrator session_01JchHuak89yQ8Ac1iDRfMRY

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 02:09-12:09 UTC 10 Oct (80% 10:09). Started from STATUS.md
"LANE FAMILY handoff (incarnation DEFAULT-account-2-20261009-2312)" (cheap supply reported spent) and a fresh `next_steps.py --hot-only` /
NEXT-STEPS read at 02:1x UTC: in-scope runnable rows not yet worked are jan-van-nassau-1572-75 (the 104 glyphs, JVN-104's named next) and
na-oldenbarnevelt-2442-1605 step (o2) (V-OLD10 did (o3'); D2 for the leaves waits on (o2)). Supply (c)/(d) (KEY-OFFICES pools, design_prior)
goes to a survey job (POOLS) whose table feeds wave 2. Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct (prior incarnations
proceeded; so do we). Exclusions: eckert-* and Huntington ledgers (LANE LEDGER-N2, account 1, live), Gallica fetches, Armstrong/Debosnys/Birago,
any folder with a ROOM claim < 6 h and no done; no live claim on either wave-1 folder at 02:2x UTC.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with these
substitutions: address every ROOM line "for LANE FAMILY-A2n (account 2)"; hosts this wave: resources.huygens.knaw.nl ("huygens": JVN-GLY only,
<= 3 requests), service.archief.nl / www.nationaalarchief.nl ("NA": OLD-O2 only, <= 10 requests), data.htrc.illinois.edu (POOLS, 1 probe);
no other external host unless the job names it. No Gallica. Halfway line: one ROOM line at half the box or half the cap, whichever first (skip
if done before). Lessons carried: read only the NOTES sections named (an Opus worker spends ~$2 reading a large folder); count tokens on the
image before planning vision calls; push every PREREG in its own commit and check `git log origin/main -1 -- <PREREG>` before scoring.

## Wave 1 (02:3x UTC 10 Oct)

### JVN-GLY (Opus, cap 2.5, box 60 min, huygens <= 3 requests): jan-van-nassau-1572-75, WVO 5551 p3 L2, the glyphs around code 104
The Verdict's cheapest next (NOTES "## JVN-104", ~lines 1617-1705; read only that section and the D3-5551 lines it cites). JVN-104's Sonnet
reader failed both same-hand "ſich" positive controls, so its pass was a non-test. This job: one control-first read by YOU (Opus, reading the
crops directly, no subagent), with the identical pre-registered question and gate as JVN-104 (copy them into PREREG-JVN-GLY.md, pushed in its
own commit before you look at X3), plus two more same-hand controls from the body (another "ſich" or "ich"/"ch" word and another long-s word
without ch) so the control set is X1, X2, X5 positive and X4, X6 negative. Re-fetch 05551.pdf once (huygens take/release), render p3 at 300 dpi,
cut with the pasted `tools/iiif_lines.py --image` command JVN-104 used; commit the detail crops this time (images/jvn_gly/, small JPEGs) so a
person can re-check. Look at the controls first, shuffled, and write your control calls in NOTES before looking at X3; if any positive control
fails, stop: non-test, record it, the instrument for this word moves to the owner's sign sorter (name it in the Escalation line). If the gate
passes, apply the result to ciphertext_5551.tsv only as the gate allows (M grade unless the gate says otherwise), re-run the folder's decode
`--check`, and update Remaining gaps / Escalation / Verdict. Also report the 140-vs-110 reading on the same crop (not gated). NOTES
"## JVN-GLY", gaps_check.py after. Report what was found and where it was not found; do not classify novelty.

### OLD-O2 (Opus worker, Sonnet subagents, cap 9.5, box 120 min, NA <= 10 requests): na-oldenbarnevelt-2442-1605 step (o2), L4/L7 masked re-cut
Read NOTES sections 22 (OLD-SIBS), 23 (OLD-S10, including the OLD-O4 normaliser paragraph and the V-OLD10 verifier note) and AUDIT.md "AUDIT 3"
and "AUDIT 5" only. Step (o2): leaves 4 and 7 (the L4/L7 blocks read by OLD-SIBS) re-cut with `tools/iiif_lines.py --mask-neighbours`
(pasted command; images from disk if committed, else NA IIIF with take/release), then two blind Sonnet passes on the masked crops (one page or
half page per call, crops only, not told the key or the reading, told to write the cursive r as r per OLD-O4) and one reconciliation unit.
Price: about 4 crop sets x 2 passes x ~1.0 + 1.5 reconciliation; stop before a unit that would cross 80% of cap or box. Pre-register in
PREREG-OLD-O2.md (own commit, before scoring): the S rule (OLD-O4 normaliser from the start), the matched control (the same permuted-key /
lexicon-hit controls OLD-S10 used, which can differ from the target on the S statistic), and what moves D1 -> D2 under
.claude/briefs/runs/2026-10-08-acct3-depth-bar.md (a stretch above the authentication distance, or a code value reading in two contexts) --
the verifier decides depth, you report the numbers. Decode under the fixed B/C1 key with the folder's script and `--check`. Also apply the two
eye-check suggestions OLD-SIBS-V and V-OLD10 left (`f28ss8` L5_1 "fuesse", `q24nd7` L4a_05 "quando", L16 `h4237` -> `h4b3t7` "habito") only if
your masked passes support them; otherwise list them as still open. NOTES "## 24. OLD-O2", gaps_check-style Remaining gaps/Escalation if the
folder has them, reading files regenerated. If the S share rises, end with one line asking the lane for a verifier (do not verify yourself).
Report what was found and where it was not found; do not classify novelty.

### POOLS (Sonnet, cap 3, box 75 min, disk only except 1 HTRC probe): supply survey for wave 2 -- key pools with unread letters, in-scope families
No decoding, no fetches beyond the one probe. (1) From KEY-OFFICES.tsv take every row in this lane's families (Dutch/WVO/Huygens/NA, German,
Iberian, British/Irish incl. Thurloe and Huntington Blathwayt/Stowe, DECODE-held, Scandinavian; skip eckert-*, Huntington ledgers, Gallica-only
items, Armstrong/Debosnys/Birago). For each key family, list unread letters that the repo already knows of on the same host (grep the owning
folders' NOTES "siblings"/"Remaining gaps"/"While waiting" sections, siblings*.tsv, discovery*.tsv, SIBLINGS-2026-10-08.tsv, LOOSE-ENDS*,
NEXT-STEPS.tsv), with: folder, letter id, host, images on disk (y/n, path), signs estimate, glossed (y/n/?), key in hand (path), last step and
date, blocker (from the folder's own words), and a ROOM.md claim < 6 h (y/n). Mark a row `done-already` when the folder's dated sections show
it read, glossed (N0 by construction) or retired. (2) For each family with >= 1 runnable unread letter, run `python3 tools/design_prior.py`
on it (paste the command and the top line). (3) Probe the HTRC EF API once for rah-salazar-soria-sanchez-1524-28 (the folder's own command,
NOTES last section); if it answers 200 with data, run the rerun (~$0.2) and record it in that folder's NOTES; if not, one ROOM line, no retry.
Output: `research/POOLS-FAMILY-2026-10-10.tsv` (one row per unread letter, ranked by: key in hand, images on disk, signs, cost) and a 10-line
summary at the top of a sibling .md naming the top 5 runnable rows with a one-line cheap step and cost each. Push. Report the top 5 in the
final paragraph.
