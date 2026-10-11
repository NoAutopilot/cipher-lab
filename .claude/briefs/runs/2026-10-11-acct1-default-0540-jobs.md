# LANE DEFAULT-account-1-20261011-0540 jobs (account 1, lane orchestrator session_018mrAo3nwi1htD6CzT9gyWE) -- 11 Oct 2026 05:5x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 05:40-15:40 UTC 11 Oct (80% line 13:40). five_hour `allowed` at start.
Gate 0a: SESSION-SWEEP-account-1 stale-claimed since 5 Oct, proceeded (as every incarnation since). Backlog read 05:4x-05:5x UTC:
VERIFY-BACKLOG.tsv (05:20 run): high rows are Birago (off limits), manteuffel (LANE DEFAULT-A2-0509 holds it), eckert-1864 -- of the
13 eckert high rows only results[401-404] are N3 (the rest are N1: Outreach gate 2 does not apply); "none" rows need no verifier
action. `next_steps.py --hot-only`: most runnable/parallel cells are stale on reading the folders (fr3987 read, JVN-104 run, vieuville
print check run, wallis Thurloe grep run, harley ff.70r-72v read, heinsius Deel 2 done, ormond report read); Gallica answers 403
(probe 05:5x UTC, 1 request) and the HTRC EF API still MongoError (1 request), so every Gallica/EF step is out. Exclusions: Birago,
Armstrong, Debosnys; pisany, baluze167, fr3985-nevers, manteuffel, thurloe-printed (LANE DEFAULT-A2-0509); wvo-hessen-1564 and
fr16104-vivonne (account 3, < 6 h).

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in full), with
these substitutions: address every ROOM line "for LANE DEFAULT-A1-0540 (account 1)"; the hosts bullet below replaces the one there.
Halfway line: one ROOM line at half the box or half the cap, whichever first (skip if done before). `get_session` is not available to
you: say "cost not visible to this session" in the done line.
Hosts this wave: MAT-F179 disk only (no network at all). AUD2-FM16e: hdl.huntington.org (CONTENTdm, >= 3 s), googleapis (key +
country=US), archive.org be-api/IA full text, OpenAlex/S2/CORE (keys per CLAUDE.md item 3), <= 60 requests per host; post "IA take" /
"IA release" lines (LANE DEFAULT-A2-0509's workers also use archive.org this morning: if one of theirs holds an IA take with no release
in the last 30 min, work another host meanwhile). CAST-G7: searcharchives.bl.uk (`?format=json`, <= 5), the ASNa and BL contact pages
(<= 5 each), nothing else. No Gallica, no HTRC.

## Wave 1 (05:5x UTC 11 Oct)

### AUD2-FM16e (Opus, second verifier, cap 5, box 120 min): eckert-1864, Audit 2 for results[401]-[404]
status.json results titled "Eckert 1864 (Fort Monroe ledger): Sheldon, Fort Monroe, to John Horner ..." (E443, p.241 ptr 5785),
"... Butler's headquarters (R. O'Brien) to Sheldon ..." (E445, p.272 ptr 5816), "... Sheldon, Fort Monroe, to Maj. Eckert, 12 Mar
1864 ..." (E446, p.39 ptr 5583), "... Eckert, Washington, to Dealy, Fort Monroe, 15 Oct 1864 ..." (E448, p.249 ptr 5793): all N3 D1,
key period, first audit "## AUDIT (FV-L16e)" in AUDIT.md (l.19285 on). AUD2-LEDGER16-5 left these four out of its scope; you are a
session separate from FV-L16e, AUD2-LEDGER16-5 and every reader (FM-S1, FM-S2, FM-S3, FM-F1). CLAUDE.md "Verifier brief (template)"
steps 1-5, per item: extract (step 1), then try to find each telegram's plaintext in print -- OR (on disk: the cached print-check volumes
FV-L16e used, read its `fortmonroe/fv_l16e_*.py` outputs first and do not repeat its queries), ORN, Butler's Private and Official
Correspondence IV-V, Grant Papers vols 10-12 (Google Books snippets, country=US + key), IA full text (be-api), the holder's own
CONTENTdm text (CISOSEARCHALL per CLAUDE.md, fresh phrases, not FV-L16e's 27), OpenAlex/S2/CORE; a phrase search on each decoded span;
JSTOR-QUEUE rows in both families (i) and (ii) for the owner's runner (never blocking). Upheld or lowered class per item, depth unchanged
unless wrong (rule 4a; `python3 tools/depth_check.py` after). Write "## AUDIT 2 (second adversarial, AUD2-FM16e)" in AUDIT.md; set
audit_status 'two audits' and append to audit_refs in status.json for each item; any item kept at N3+ gets its SECOND-OPINIONS-QUEUE.tsv
row if one is not already there (grep first). Item 5, small: NOTES.md FM-S65B gap "E550 (5897/0): its clear copy is 8561, which FM65-D
did not find" -- as a verifier, check it against `sources/fortmonroe/` and correct E550's per-row line in AUDIT.md (one line). Do not
decode. Units: 4 items x ~1 + E550 0.2.

### CAST-G7 (Opus, gate-7 fact check, cap 2, box 60 min): castelcicala-1816, REQUEST.md (two drafts)
ASKS row 149 waits on "a gate-7 fact check of ciphers/castelcicala-1816/REQUEST.md (not yet run)". You are not its drafter (D4-CASTREQ,
account 4). CLAUDE.md Outreach gate (7): read both drafted requests (BL Add MS 41525 f.38; ASNa Esteri busta 2337) against every file
and source they cite and try to falsify each factual sentence: shelfmarks, folio, the BL catalogue record 040-002085178 and its quoted
Access text (re-read the record once with `?format=json`), dates, sender/recipient, the DECODE record numbers against the folder's own
files, what was and was not checked, the Premise check (d) claim in NOTES.md, and the recipient address read from each institution's
own contact page with the date (an institutional address only, never a private person's). Also the voice check (outreach/README.md rule
1a) and the AI-disclosure sentence (rule 1) if the draft is an outward note. Correct the draft in place, then write the header line
`checked: <date> by CAST-G7 (account 1, separate session from D4-CASTREQ); corrected: <what>` (or `checked: ... ; no corrections`). If a
claim cannot be verified from here, say so in the checked line rather than guess. Update ASKS row 149's cell to say the check ran (keep
both facts on conflict). Do not add a CONTRIBUTIONS.md or SEND-QUEUE.tsv row; sending stays the owner's. Units: 1 read pass + 1 fix.

### MAT-F179 (Opus, cap 8, box 150 min): matignon-mayenne-1586 folder, BnF fr.15571 f.179 (Matignon's Cipher-3) under Tomokiyo's table
The folder's own escalation line (NOTES.md l.1574): "Cipher-3 f.179: ... crop images/f179_gallica_native.jpg with tools/iiif_lines.py
--image, two passes + decode". Intake gate (05:5x UTC, pasted): `matignon-mayenne-1586: partial (line 1) -- edition/page or
full-text-search citation found within 6 lines`, exit 0. NEAR.md row: the target stays `partial` whatever happens (rule 5). Disk only:
the leaf is `images/f179_gallica_native.jpg` (1600x2221, already rotated 180 degrees, no overlay); the table is
`sources/cryptiana/keys/henryiii_Matignon3.png` (Tomokiyo's reconstruction of Cipher-3 from the period decipherments of fr.15572 f.189/190,
f.277-280, f.282; cite Tomokiyo, key source `published`). PRIOR WORK, read before anything: Tomokiyo's own composite
`images/BnFfr15571f179.jpg` carries his modern magenta labels on some glyphs and the words "front", "pour", "que", "entre" (NOTES.md l.212-
260, bMAT3) -- a published partial reading. Your blind passes and their subagents must never see that file or its labels; it is used only
afterwards, as an external agreement check (count where our decode and his labels agree / differ), never to settle a sign. Run
`python3 tools/prior_work.py matignon-mayenne-1586 --item-spec 'shelfmark=BnF fr.15571;folio=179' --step-type read` and paste it.
Steps: (1) transcribe the table into `cipher3/key_tomokiyo.tsv` (sign label -> value, homophones and nulls as he shows them; one Opus
look at the png, then a second independent look by a subagent; disagreements settled from the png and listed). (2) PREREG-MAT-F179.md
pushed in its own commit BEFORE any decode: crop step pasted (`tools/iiif_lines.py --image images/f179_gallica_native.jpg --out
cipher3/crops --debug`, check the overlay), sign labels from the table's own label set (with an `?` and a `new:<desc>` escape for signs
the table lacks -- Tomokiyo notes f.179 has extra variants), two blind Sonnet passes (line crops only, at most ~8 lines per call),
`tools/reconcile_passes.py`, reader-disagreement rate reported; gate: decode under the table scored by `tools/judge_plaintext.py` with
the most era-matched French corpus in tools/data (say which; the fr16 fold-spread caveat in CLAUDE.md applies) above the p95 of >= 200
value-shuffled tables (shuffle values among signs, nulls kept) AND above the shuffled decode of the shuffled ciphertext (CLAUDE.md rule 3,
ARM-C1); plus the Tomokiyo-label agreement count as a separate, non-gating check. If reader disagreement exceeds 10% of signs, stop after
step 2's passes: write the disagreements to `cipher3/focus.tsv` for the owner's sign sorter (TRANSCRIPTION.md) and do not decode. (3) If
the gate passes: `decode.json` layer + `tools/decode_key.py ciphers/matignon-mayenne-1586 --check` route for f.179 (do not disturb the
Cipher-1 reading), grade per token (rule 4: S at most for table values not confirmed by a period gloss on this leaf; M for uncertain),
judge output pasted into NOTES.md (rule 7). Write "## MAT-F179 (11 Oct 2026)" in NOTES.md, refresh Remaining gaps / Escalation /
Verdict, gaps_check passes. Report what was found and where it was not found; do not classify novelty. Units: table 2 looks (~1.5 each)
+ 2 pass units (~1.5 each; a pass over > 8 lines is 2 calls, price it) + 1 reconciliation + CPU = ~7.5; stop before a unit that would
cross 80% of cap or box.
