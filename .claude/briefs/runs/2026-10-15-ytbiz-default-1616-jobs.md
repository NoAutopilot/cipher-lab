# LANE DEFAULT-account-2-20261015-1616 jobs (account 2, lane orchestrator session_01RJVk5rvjZN3Afx7NbPXjqu) -- 15 Oct 2026 16:3x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 16:16 UTC 15 Oct - 02:16 UTC 16 Oct. Gate 0a: SESSION-SWEEP-account-2 claimed
since 5 Oct, stale, proceeded (as the five earlier account-2 lanes today).
Backlog: VERIFY-BACKLOG rows are Birago/ceppo (off limits) or eckert-1864/manteuffel audit2 at N1 (gate 2 asks a second audit only above
N1): not run. Step b: `next_steps.py --hot-only`, 71 runnable/parallel rows after exclusions, checked by one read-only Sonnet triage against
each folder's latest sections; 9 survived, 2 of those were already done on re-check (matignon f.179 = MAT-F179 9 Oct; naf14913 code 605 = C
since R9-ROUSV2 6 Oct), and na-suriname / thurloe were left (instrument churn; P25-P28 already done by R8-THUR25).
Excluded: live LANE DEFAULT-A1-1426-15 (baluze167, fr5761, na-janssens), VIV-KEYSTONE (fr16104, fr16106, mercy), SAV-L29's claim
(fr16144), Birago family/ceppo/nevers-birago, Armstrong, Debosnys, BNF-FOCUS holdings (fr3982, fr3985-3990).
Intake gate 16:3x UTC (tools/intake_gate_check.py, each PASS): clair1161-avis-flandre-1688, harley-287-1587, august-van-saksen-1561-64,
antt-msliv0638-brochado-1712, fr4715-f61-mayenne-1592.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-15-ytbiz-default-0810-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A2-1616-15 (account 2)"; export `CIPHERLAB_ACCOUNT=account-2` before any tools/room.py call;
- a worker pays ~1 of start-up before its first unit: stop before a unit that would cross 80% of cap or box;
- www.googleapis.com only in job F61-GB2, and only as that job says;
- images never go into git (scratchpad only); commit TSV/MD/scripts by explicit path;
- never the words solved, cracked, novel, first, new for anything this project did; never name the owner; never AskUserQuestion.

## Wave 1 (16:3x UTC 15 Oct)

### C1161-G1 (Opus, cap 3.5, box 70 min, disk only; Sonnet reader calls ~0.6): clair1161-avis-flandre-1688 group 1 re-pass + registered --try
C1161-EXC's Verdict "cheapest next" (NOTES "## Remaining gaps (C1161-EXC, 15 Oct 2026)"): (1) a fresh blind pass B on the group 1 labels
(d, psi, rot, s, th, tri) with a new seed, same protocol and controls as C1161-EXC, plus a fourth reader on f/dia (2 Sonnet calls); (2) one
registered `tools/decode_key.py ciphers/clair1161-avis-flandre-1688 --try` per exemplar-matched conflict (vdash d, 2 s, eloop a, ls e, K h,
6 in 76, iii '###' et, blot, x null) at every occurrence, with the power controls of C1161-S275. PREREG-C1161-G1.md pushed before any score.
No key.tsv edit (MQS-CROSSWORD rule: accepted values M unless --try's own control passes). Known text (AUDIT N0, Lasry key published): this
corrects the record of the concordance with his key; say so. NOTES "## C1161-G1", gaps + Verdict, gaps_check.

### HAR-41R (Opus, cap 4.5, box 80 min, de-crypt.org one browser login, ROOM take/release): harley-287-1587 R8480 f.41r cipher vs margin
HAR-37R's named alternative (NOTES Verdict "cheapest next", and HAR-37R's lesson): fetch DECODE R8480 P1 (f.41r; HAR-37R's copy had sha1
0f4896606b21, scratch only) with `tools/decode_browser_login.js` (one login, `--guess-fullsize` if needed), cut tight crops of the cipher block
(box-sign rows only, gloss out of view) and of the margin clear text with `tools/iiif_lines.py --image` (command pasted before the first
reader call). Readers: one Opus call per run (HAR-39V's reliable method), not Sonnet batches; the margin text read separately. PREREG first:
gate = the needham1587 key (Bourdeau's, as used in HAR-37R) applied to the read cipher vs the margin text, against a value-shuffled key null
(p95), and a second statistic that can differ under the shuffle. Units: ~4 cipher calls + 1 margin call + 1 reconcile ~ 6 x 0.6-1.0. If
f.41r's cipher block is longer than 4 runs, read the first 4 and say so. NOTES "## HAR-41R", gaps + Verdict, gaps_check.

### AVS-W1 (Opus, cap 2.5, box 50 min, resources.huygens.knaw.nl <= 3): august-van-saksen-1561-64 W1 native read + the '6~' tokens
AVS-153's "Next (not done here)": a native read of witness W1 (p7/f.5) for a rule-4 W1/W2 check on WVO 153 cipher lines 10-20 (1 Opus look,
~1), and a look at the lines 2/6 '6~' tokens against 6f (~0.5). PREREG the decision rule first. Text on the leaf is known (light guardrail:
it firms key_153 for the unread letters of that key family; name them). key_153.tsv grades change only by the registered rule;
decode_key --check (or the folder's own check script) exit 0. NOTES "## AVS-W1", gaps + Verdict, gaps_check.

### BRO-KK (Opus, cap 2.5, box 50 min, cryptiana.web.fc2.com <= 4, digitarq.arquivos.pt <= 3 at >= 3 s): antt-msliv0638-brochado-1712
Two cheap internal steps the Escalation names as never run: (a) known-keys: a dedicated search of Tomokiyo/Cryptiana for a Portuguese cipher
table of 1700-1720 (sources/cryptiana on disk first, grep; then at most 4 cryptiana requests for index pages) -- compare any hit's design with
key.tsv (homophonic letters inside clear Portuguese); (b) the m0264 inline 3-4 token string (page 130, BRO-SWEEP): fetch m0264 once with
tools/digitarq_fetch.py, crop the string, one Opus read, decode under key.tsv with the grade it earns. No letter-134 change unless (a) yields a
key that passes a matched control. NOTES "## BRO-KK", gaps + Verdict, gaps_check.

### F61-GB2 (Sonnet, cap 1, box 30 min, www.googleapis.com <= 8, api.semanticscholar.org <= 3): fr4715-f61-mayenne-1592 the unsent phrases
F61-GB's table: the five phrases not searched (503) and the 429'd Semantic Scholar queries. ROOM "googleapis take/release" lines. Control query
first (any phrase with a known hit, as F61-GB); on a 503 one retry after 60 s, then stop the host and report. `&country=US` and the key from the
environment (never printed). Record every query, status, hit / no hit in NOTES "## F61-GB2" and print-check-f61 rows. No reading change.
