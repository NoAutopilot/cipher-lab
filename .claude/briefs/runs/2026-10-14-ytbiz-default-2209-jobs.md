# LANE DEFAULT-account-2-20261014-2209 jobs (account 2, lane orchestrator session_01JajHGkXCRZ7LtJNFUSiJWU) -- 14 Oct 2026 22:2x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 22:09 UTC 14 Oct - 08:09 UTC 15 Oct. Gate 0a: SESSION-SWEEP-account-2 stale-claimed
since 5 Oct; proceeded, as earlier incarnations did. VERIFY-BACKLOG regenerated 22:1x UTC: high rows Birago/ceppo only (off limits), the
audit2 rows are N0/N1 (Outreach gate 2 n/a). `next_steps.py --hot-only` runnable rows are held by the live account-1 (DEFAULT-A1-1840-14)
and account-4 (DEFAULT-A4-2135-14) lanes (baluze167, colbert26, sforza-duke, fr4712, fr4735, clair571, fair-game, eckert-1864, thurloe),
already run (fr3993 f.104v, VILL-104V 13 Oct), or wait on an owner sort (Revol no.60, gramont, fr16045, fr3416); so this wave also takes
plain `next_steps.py` runnable rows nobody holds, plus one record-correction job for two stale Verdict lines. Guardrail fifth: CL1161-KA
(text known from Lasry's f163r paragraph; it tests our key) and GAPS-FIX (record correction).

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A2-2209-14 (account 2)"; the hosts named in your job replace that file's
hosts lines. Export `CIPHERLAB_ACCOUNT=ytbiz` before any tools/room.py call. `get_session` is not available to you: say "cost not visible
to this session" in the done line. Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before).
Check 1 before any unit: grep the folder's NOTES.md for a later section that already ran the unit; if it did, one ROOM line and stop.
Never the words solved, cracked, novel, first, new for anything this project did. Do not touch status.json, NEAR.md, STATUS.md or the
board (the lane orchestrator does). Birago, Armstrong and Debosnys folders are off limits. Report what was found and where it was not
found; do not classify novelty (solver jobs).

## Wave 1 (22:2x UTC 14 Oct)

### CL1161-KA (Opus, cap 2, box 50 min, disk only): clair1161-avis-flandre-1688, c186R token-level known-answer gate against the f163r paragraph
NOTES.md Remaining gaps item "digit-pair nomenclature 77/76/44/37/48 and the S-sign conflicts 7 (i vs b) and S (u vs n)" (line ~2471) and
the Verdict (line ~2516): align our V2 decode of c186R to the full f163r paragraph (George Lasry's reading, logged as prior work, LQ-C1161;
AUDIT.md's prior-work notice) token by token and count unit and letter agreements against a permuted null. Intake gate (22:19 UTC, pasted):
`clair1161-avis-flandre-1688: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0. Units: (1)
PREREG-CL1161-KA.md pushed in its own commit BEFORE any score (statistic, null with >= 1000 permutations, gate, and a power check: the
gate must be able to fail -- e.g. a known-wrong key variant scored the same way); (2) score; (3) per conflict class (7 i/b, S u/n, the
digit pairs) say which value the alignment supports and with what count; a key value changes only through `tools/decode_key.py --try`
at every occurrence, graded M unless --try's own control passed (CLAUDE.md MQS-CROSSWORD), and any decode script touched is re-run with
`--check`. Credit Lasry for every value his paragraph supplies (rule 8). Update Remaining gaps / Escalation, `tools/gaps_check.py`.

### MCC-WORD (Opus, cap 3.5, box 75 min, disk/CPU only): mccormick-1999, word-level code-word anneal, control sweep first
NOTES.md "## MCC-SWEEP" and its Remaining gaps / Escalation (lines ~602-656): next instrument is a word-level code-word anneal (whole-word
bigram objective over an English word corpus in tools/data, code types drawn from the word pool, total-scale temperature). Intake gate
(22:19 UTC, pasted): `mccormick-1999: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0. Units:
(1) prefer an option on an existing tool (tools/token_anneal.py or tools/family_run.py's wordcode family) over a private script (Usage 8);
offline test in tools/tests/ if you add an option; (2) PREREG-MCC-WORD.md pushed before any run: control lengths 132, 500, 2,000, 8,000
tokens x 3 seeds, the gate for "reads" at 132, and the rule that the target is run only if the control mean meets the gate at 132; (3)
the sweep, serialized (CLAUDE.md Usage 6, no concurrent background CPU); (4) target only if gated. Rows into HYPOTHESES.md (both numbers).
If the control fails at every N this is the instrument's second family-level negative on this target: log it per rule 3 (untestable by
this instrument at this N) and name a genuinely different instrument or "no-key-material" in the Verdict. Update gaps, `gaps_check.py`.

### TUSC-KEYS (Opus, cap 3.5, box 60 min, cryptiana.web.fc2.com <= 6 requests at >= 2 s): fr3982-nevers-toscana-1592, Tomokiyo's Tuscan keys
Verdict (line ~221): transcribe the published Tuscan reconstructions (Tomokiyo, guicciardini.htm: guicciardini1.png, guicciardini2.png) as
key TSVs while the sign check waits. `sources/cryptiana/web/guicciardini.htm` is on disk; fetch the two images once to
`sources/cryptiana/web/` (a source snapshot: never edit after) and record them in a manifest line. Intake gate (22:19 UTC, pasted):
`fr3982-nevers-toscana-1592: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0. Units at ~1.5 each:
(1) crop each table with `tools/iiif_lines.py --image <png> --out <dir>` (pasted) or a plain row crop if the table is small; two blind
reads of each table (one vision call per table per pass) + one reconciliation unit; (2) write `keys/tomokiyo_guicciardini1.tsv` and
`..._2.tsv` (value, meaning, source, grade H-published, credit Tomokiyo), and KEY-OFFICES.tsv / KEY-DESIGN.tsv rows via tools/key_design.py
(CLAUDE.md 8a). No screen against ciphertext_v2.tsv (BNF-Q7-ERR: v2 is not a measured transcription); a screen against the committed
ciphertext.tsv is allowed only as a pre-registered `tools/key_crossmatch.py` run with its shuffled control, logged as conditional on that
transcription's known 8-sign problem. Credit Tomokiyo in every file (rule 8). Update gaps, `gaps_check.py`.

### OLD-O5 (Opus, verifier, cap 3, box 60 min, disk only): na-oldenbarnevelt-2442-1605, re-grade of leaves 4/5/7 under OLD-O2's grades
CLAUDE.md "Verifier brief (template)" steps 1, 3a and 4 only (no novelty search: the claim under audit is the per-token grades, not
novelty), as named in NOTES.md section 25 (OLD-WB) "Next step: (o5) verifier re-grade of leaves 4/5/7 under OLD-O2's grades" (lines ~1699,
~1745). You are not the solver of OLD-O2 or OLD-WB. Intake gate (22:19 UTC, pasted): `na-oldenbarnevelt-2442-1605: open (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0. Re-derive each leaf's reading with its committed decode script and
`--check` (rule 7); compare against OLD-O2's grades and OLD-WB's numbers; correct any grade the evidence does not license (rule 4; S needs
a control that could have failed); write the depth line (rule 4a) per leaf with tools/depth_check.py into AUDIT.md (a dated section);
note that ASKS 161's open sign sort (section 26) bounds the S stretches and is not settled here. Do not edit status.json (the lane does).

### GAPS-FIX (Opus, cap 1.5, box 40 min, disk only): stale Verdict lines on sp105-paget-1693 and wvo-11008-certain-1572
(a) sp105-paget-1693: Verdict (line ~257, D2-PRINT4 8 Oct) still names "check SP 106 key templates ... ~$0.5" as cheapest next, but
"## SP106-KEY" (9 Oct, line ~223) ran it by catalogue and left an owner-side look at SP 106/10, /40, /42 (needs-physical-access). (b)
wvo-11008-certain-1572: next_steps reads "correct the R2 Groen span in w5194_gate.py, ~$0.5", but W11008-R2 did that on 8 Oct (ROOM 23:03;
"## 5194 known-plaintext check" area). For each: confirm from the files and git log, then rewrite "## Remaining gaps" / "## Escalation"
(dated, GAPS-FIX, 14-15 Oct 2026) so each gap carries its real blocker and the Verdict names the true next step or "parked" with outside
blockers; add the missing sections where absent; no reading, grade or status line changes. Intake gates (22:19 UTC, pasted):
`sp105-paget-1693: open (line 1) ...` exit 0; `wvo-11008-certain-1572: open (line 1) ...` exit 0. `gaps_check.py` both, and run
`python3 tools/next_steps.py` once to confirm both rows read the new Verdict (do not commit NEXT-STEPS.tsv unless the tool's own docstring
says to).

### OBRED-6018 (Opus, cap 4, box 90 min, NA (service.archief.nl / www.nationaalarchief.nl) <= 220 requests at >= 1.5 s, take/release):
oldenbarnevelt-brederode-1605, stride-3 screen of NA 1.01.02 inv. 6018 (1618, 577 scans) for a third text in the no. 92 / scan-187 table
Verdict (line ~1547) and Remaining gaps (line ~1535). Method and controls exactly as OBRED-S3 (inv. 6017, 10 Oct: 195 scans, controls 60/60,
LEDGER row ~4118, 1.73 on Sonnet) and OBRED-6017E; METS ids in `nl_brederode_lias.tsv`. Intake gate (22:19 UTC, pasted):
`oldenbarnevelt-brederode-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0. Units: one
contact sheet of ~12 thumbnails per vision call (~1.0 each on Opus), positive controls mixed in as OBRED-S3 did; stop before a unit that
would cross 80% of cap or box and hand the remainder on with the exact scan range. Any hit: one native look, then stop and report (no
decode in this job). Commit the screen TSV and controls. Update gaps, `gaps_check.py`.
