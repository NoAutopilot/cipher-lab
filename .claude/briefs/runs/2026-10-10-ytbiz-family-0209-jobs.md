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

## Wave 2 (02:5x UTC 10 Oct)
Wave 1 results: JVN-GLY gate YES at M (blind check to the sign sorter); OLD-O2 S 87->165 words, longest S stretch 13 < AD floor 24.2;
POOLS research/POOLS-FAMILY-2026-10-10.tsv (rows 1-4 stale on check: thurloe P25-28 done R8-THUR25, wvo-11008 R2 done W11008-R2, wvo-hessen
waits on the owner's sorter; heinsius-hermitage already listed the deciphered letters -> REQUEST.md). Intake gate 02:5x UTC exit 0:
oldenbarnevelt-brederode-1605 open, decode-1411-hhsta-vienna-1600 open. Hosts this wave: service.archief.nl / www.nationaalarchief.nl ("NA":
OBRED-6016 only, <= 120 requests, >= 1.9 s); de-crypt.org (D1411-P6 only, ONE browser login, tools/decode_browser_login.js). OLD-WB disk only.

### OLD-WB (Opus, cap 2, box 50 min, disk only): na-oldenbarnevelt-2442-1605, word-boundary-insensitive S test (OLD-O2's named instrument)
Read NOTES section 24 (OLD-O2) and its PREREG only. OLD-O2: "the stretch is held down by word-level M on short function words where one pass
splits or joins tokens, not by sign disagreement alone -- a pre-registered word-boundary-insensitive S test (match the sign string across token
boundaries) would be the next instrument, ~$1". Write PREREG-OLD-WB.md (own commit, pushed and checked on origin/main before scoring): the S
rule on the concatenated sign string per line (both passes agree on the sign and the fixed key decodes it into a lexicon word or a run that a
lexicon segmentation covers, define it exactly), the longest contiguous S stretch statistic, and the SAME 120 permuted-key control OLD-O2 used,
which CAN differ from the target on this statistic (state why). Report the target's longest stretch and S share against the control's
distribution and against the AD floor 24.2 digits; no new vision, no third pass (the 10% rule). The verifier decides depth; you report numbers.
NOTES "## 25. OLD-WB", reading files only if a grade changes under the registered rule (then `--check`). Report what was found and where it was
not found; do not classify novelty.

### OBRED-6016 (Sonnet, cap 2, box 70 min, NA take/release, <= 120 requests, >= 1.9 s): oldenbarnevelt-brederode-1605, inv. 6016 sibling screen
The Verdict's cheapest next (NOTES ~lines 781-846; read only those). Contact sheets of NA 1.01.02 inv. 6016 from image order 261 onward at
~400 px (IIIF via service.archief.nl; read the item page's drupal-settings-json for the scan list, CLAUDE.md NA row), looking for a
Brederode-side cipher letter with a period gloss or decipherment (three-digit unmarked groups as in no. 92). Seed every contact sheet with one
known cipher scan of this folder (positive control) and one plain scan; a sheet whose control is missed is a non-test, re-look it. Every hit:
one scan at >= 1200 px, say glossed yes/no, date/sender if legible. Write images/6016_screen.tsv (scan, call, control) and NOTES
"## OBRED-6016" with counts and the hits; no transcription. Stop the scan at the end of the Brederode run or at 80% of the cap/box. Remaining
gaps / Escalation / Verdict, gaps_check.py after.

### D1411-P6 (Opus worker, Sonnet subagents, cap 6.5, box 110 min, ONE DECODE login): decode-1411-hhsta-vienna-1600 p.6 numerals
The Verdict's cheapest next. Read NOTES "## AM-D1411P5", "## AM-D1411V" and the Remaining gaps/Escalation only (~lines 656-833). Exactly the
AM-D1411P5 method on p.6 (IMG_R1411_I6600_P6.png): PREREG-D1411P6.md + score_p6.py (a copy of d1411p5's scorer, paths changed) pushed in their
own commit and checked on origin/main BEFORE the image is opened, registering T21r primary with h12/h22 beside, the permuted controls p.5 used,
and the copy mask (d1411v/rescore_v.py copy_mask: numbers aligning to already-read pages are excluded before scoring; state the alignment rule).
Re-run the scorer on p.5 first and reproduce AM-D1411V's numbers (independent p.5 0.588) before touching p.6. One DECODE browser login
(`tools/decode_browser_login.js 1411 --fetch IMG_R1411_I6600_P6.png --max-files 1`), sha1 against images/manifest.json, image not committed.
Crops as AM-D1411P5 (pasted commands, crops committed), two blind Sonnet passes (one call each, crops only, opposite orders),
tools/reconcile_passes.py, one reconciliation unit. Score; an S grade only on a registered PASS on independent (unmasked) numerals that also
reaches the leaf's own gloss coverage (the AM-D1411V bar). NOTES "## D1411-P6", Remaining gaps/Escalation, gaps_check.py. If p.6 PASSes, end
with one line asking the lane for a verifier. Report what was found and where it was not found; do not classify novelty.

## Wave 3 (03:1x UTC 10 Oct)
Wave 2: OLD-WB WB S share 0.448 rank 1/120, longest stretch 17 = sign-agreement ceiling < 24.2; OBRED-6016 0 cipher in 92 scans (orders
351-624, stride 3); D1411-P6 stopped on the orchestrator's brief error (relative --fetch name -> 404), PREREG + score_p6.py on main (b42c67c7d).
Hosts this wave: de-crypt.org (D1411-P6b only, ONE browser login). V-OLD-O5 disk only.

### D1411-P6b (Opus worker, Sonnet subagents, cap 5.5, box 100 min, ONE DECODE login): decode-1411-hhsta-vienna-1600 p.6 numerals, resumed
As "### D1411-P6" above, resumed from NOTES "## D1411-P6 step" (~line 817): the PREREG (d1411p6/PREREG-D1411P6.md) and score_p6.py are
already on main -- do NOT rewrite them; re-run the scorer on p.5 and reproduce 0.5882 first. Fetch with the ABSOLUTE filesrv URL:
`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 1411 <scratch> --fetch 'https://de-crypt.org/decrypt-custom/filesrv/?file=IMG_R1411_I6600_P6.png' --max-files 1`
and check the saved file is a real PNG (not the forbidden.png placeholder, sha1 035489a0...; compare images/manifest.json's sha1 for P6 if
listed). If that one login does not yield the image, stop: one ROOM flag, no second login. Then crops, two blind Sonnet passes, reconcile,
score exactly as registered. NOTES "## D1411-P6b", Remaining gaps/Escalation, gaps_check.py. A PASS that also reaches the gloss coverage bar ->
one line asking the lane for a verifier. Report what was found and where it was not found; do not classify novelty.

### V-OLD-O5 (Opus, verifier, cap 3.5, box 60 min, disk only): na-oldenbarnevelt-2442-1605 leaves 4/5/7 re-grade after OLD-O2 and OLD-WB
Step (o5). A verifier session: you did not produce these readings. CLAUDE.md "Verifier brief (template)" steps 3a-5 only (the novelty search for
this letter is on file in AUDIT 3/4; do not redo it unless a reading changed in a way that adds a phrase -- then a phrase search on the new
words). Read AUDIT.md "AUDIT 3", "AUDIT 4", NOTES sections 24 (OLD-O2) and 25 (OLD-WB) and both PREREGs. (1) Re-derive: run the folder's
decode `--check` and OLD-WB's scorer; confirm the S shares and the 17-digit stretch independently (your own short script is fine). (2) Eye-check
20 S-graded words on the masked crops, chosen by a fixed rule you write down first (e.g. every 8th S word). (3) Depth under
.claude/briefs/runs/2026-10-08-acct3-depth-bar.md: does any clause (a stretch above the AD, a code value reading in two contexts) now hold?
Give depth_pct and D-level with the check used. (4) Write AUDIT.md "## AUDIT 6 (V-OLD-O5)" with N-class carried (or changed, with reason), key
`ours`, depth, one safe and one unsafe sentence, and carry any change into status.json's row and the SO-OLDEN-2442-L457 SECOND-OPINIONS-QUEUE
row (rule 10 propagation). If N3+ and D2+, add the WORK-QUEUE row AUD2-FAMILYA2N-1 for a second audit on account 3 (lane-common-blast
"Results"). Rule 10 wording only.
