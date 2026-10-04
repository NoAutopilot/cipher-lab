# LANE-NEAR4 wave 1 (4 Oct 2026, written 04:1x UTC by LANE-NEAR4, account 2 / ytbiz, session_01LRQBWNfFKjoMQfG9LHoUuz)

Lane brief: `.claude/briefs/runs/2026-10-04-acct3-lane-near4.md`. Intake gates pasted 04:13 UTC (all exit 0, "partial (line 1) --
edition/page or full-text-search citation found within 6 lines"): clair1161-avis-flandre-1688, hellen-frederick-1752,
clairambault1225-paget-1714, es132-vargas-mexia-1578, august-van-saksen-1561-64, fr16142-noailles-constantinople-1571.

## Common to every job below
- Read `.claude/briefs/README.md` "Common tail" and follow it; CLAUDE.md; last 20 lines of UPDATES.md; last 30 of ROOM.md.
- Start: `python3 tools/room.py --start` (if it cannot push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`);
  `date -u`; claim with `python3 tools/room.py "<JOB> (account 2 worker, for LANE-NEAR4)" 'claim: <target> <job>; box ends <HH:MM> UTC' --push`.
- Stop and push at the cap or the box, whichever first; before starting a unit that would cross 80% of either, stop. Never write a dollar
  figure for yourself: "cost: see the lane ledger". Never call AskUserQuestion. Never print or commit credentials or the DECODE account name.
- Rule 10 wording only (never new/first/unpublished/solved/cracked/novel); "report what was found and where it was not found; do not
  classify novelty". Never name the owner.
- Transcription steps follow TRANSCRIPTION.md: crop command run and pasted before the first subagent call (`tools/iiif_lines.py`, with
  `--follow-slope` for sloped lines), one subagent call per page/leaf, two blind passes + one reconciliation priced as 3 units.
- Rule 3: every gate pre-registered in a PREREG file pushed before the statistic is computed; a control that can differ on the statistic.
- If the target stays `partial`, refresh "## Remaining gaps" / "## Escalation" at the end of NOTES.md and paste `python3 tools/gaps_check.py
  <target>`'s OK line; if your result bears on a NEAR.md row, update its Evidence and Last-touched cells and run `python3 tools/near_check.py`.
- End: commit by explicit path, `python3 tools/file_shrink_guard.py <paths>`, `python3 tools/room.py --push <paths>` (or plain
  push after rebase), confirm on origin/main, one done line for LANE-NEAR4 (account 2) with the numbers (target and control side by side),
  requests per host, subagent calls used.

## N4-C1 -- clair1161-avis-flandre-1688: finish the leaves, pooled two-instrument reading, judge, audit handoff (Opus; cap USD 14; box 110 min)
Only job on this folder this wave: you may edit NOTES.md, NEAR.md row, status.json `near`, spec, key.tsv, ciphertext.tsv, reading.
Read first: NOTES.md sections IMG-GALLICA1, READ2-C1161, READ2-C1161B, every NEAR3-* section (C1RD, C1LOOSE, C1SPLIT, C1TX-*, C1POOL), the
"Remaining gaps (NEAR3-C1POOL)" and Escalation at the end. Note: IMG-GALLICA1 dates the group to the Noailles bundle (c188R is the clear
letter "Noailles e. d'Acqs", Paris, [20?] Dec 1570); the slug's "1688" is a catalogue artefact unless NOTES says otherwise -- check.
1. (a) Leaves. c188R is a clear letter (IMG-GALLICA1): confirm by eye on the committed 1200 px grid (`images/contact_sheets/c185-188_1200px_grid.jpg`)
   that c188R and c185L carry no cipher run, and look at c184 and c189 thumbnails (one Gallica request each, 1200 px) for a continuation;
   any cipher run found -> transcribe it (2 blind passes + reconciliation). (b) c187R slope check: 3 lines level vs `--follow-slope` crops,
   one subagent call; if framing differs, re-pass c187R with slope crops. (c) c188L (err_2reader 0.181): two fresh blind passes on the
   committed slope crops (`tx/c188L_slopecrop.py`), reconcile against its focus.tsv; target err_2reader <= 0.10. Merge changed rows into
   ciphertext.tsv (as transcribed, never repaired). Keep folder <= 30 MB (`du -sh`).
2. Pooled reading with grades "S only where two instruments agree" (pre-register in `tx/PREREG_two_instr.md` before computing): instrument 1
   = current key.tsv (fitted on c185R+c186R, held-out PASS on the other leaves); instrument 2 = an independent one you name (e.g. the best
   of seeds 1-5 pooled re-anneal key from NEAR3-C1POOL re-run on the merged stream, or a homophonic anneal on the four non-training leaves
   only). Per token: both instruments give the same letter -> S; differ -> M; C stays for the 6 gloss-attested signs; unkeyed -> U. Report
   the agreement rate against the same agreement on order-shuffled ciphertext (a control that can differ). Update key.tsv grades /
   exceptions so `python3 tools/decode_key.py ciphers/clair1161-avis-flandre-1688` regenerates reading.txt; `--check` exit 0; update the spec's
   stream to the merged signs (gap "spec stream").
3. Judge: fr16 if the 1570 dating holds (rule 3 era note: say why), else fr17; `python3 tools/judge_plaintext.py <spec> --file reading.txt`
   pasted, plus the c186R contemporary gloss scored through the same judge (rule 3 period-gloss paragraph) beside the shuffled nulls.
4. Known keys (gap "known-keys", ~2): `python3 tools/key_crossmatch.py --help`, then run this ciphertext against KEY-OFFICES keys of the
   same office/era, specifically fr16142-noailles-constantinople-1571's keys (same Noailles, bishop of Dax, 1571) and any fr.3151/Noailles
   key on disk; report stat vs gate per key.
5. NOTES.md section "N4-C1 (4 Oct 2026)": reading by leaf, an English gist of the S spans marked "interpretation", grade counts. Refresh
   Remaining gaps / Escalation, gaps_check OK, NEAR.md + status.json `near`, near_check. Then the ROOM line, exactly:
   `python3 tools/room.py "N4-C1 (account 2 worker, for LANE-NEAR4)" 'for LANE-A3V / the account-3 orchestrator: clair1161 ready for audit 1 (rule-7 re-derivation of the merged reading owed first, LANE-NEAR4 briefs it)' --push`.

## N4-HEL5 -- hellen-frederick-1752: NA Fagel inv. 5177, Hellen 1751 decipherments as known plaintext (Opus; cap USD 10; box 90 min)
Read: NOTES.md (the 5206 sections, the VHEL/VHEL2 bracketed notes, NEAR3-HEL3/HEL4, Remaining gaps), AUDIT.md section 3d and AUDIT 2.
De Leeuw 2000 ch.8 n.32: English-deciphered copies of Hellen's letters No 1-37 (30 Oct-28 Dec 1751) are in NA Fagel inv. 5177.
1. Catalogue first (CLAUDE.md Access playbook): the NA finding aid record for 2.21.006.?? Fagel inv. 5177, availability flag quoted with URL;
   then the scans via the Nationaal Archief route in the CLAUDE.md host table (item page `drupal-settings-json` -> scans -> service.archief.nl
   IIIF). A3V-VHEL2 already opened 5177 scan 108 -- reuse its route (its ROOM line 03:11 and AUDIT 2). >= 1.5 s between requests, <= 60.
2. Locate the Hellen 1751 letters in the volume (contact sheets at low res; at most 6 vision calls). For each: is it plain only, or cipher
   groups beside/above the decipherment (interlinear or facing)? language? numbered? Write `fagel5177/letters.tsv` (scan, No, date, form).
3. If no cipher survives in 5177: search for the 1751 ciphertexts elsewhere login-free (`tools/decode_list.py` for Hellen/Ellen records
   dated Oct-Dec 1751; BL Add MS 32xxx Newcastle intercepts via the DECODE listing; NA 5177 neighbouring volumes) and record. If both
   cipher and plain of the same letters exist on disk-reachable images: pre-register (`fagel5177/PREREG.md`) a held-out gate (fit codes on
   letters A, predict codes 1-800 tokens of letter B against a shuffled-pair control), then transcribe the cipher of ONE letter (2 blind
   passes + reconciliation) and run `tools/interlinear_align.py`; recovered values graded C. Stop at the cap; one letter done well beats three.
4. If plain-only and no ciphertext found: say so, and test whether the plaintexts can still serve as cribs for R1953 (same weeks? same
   topics?) in one paragraph -- no cryptanalysis this job. NOTES.md section "N4-HEL5", gaps refresh, NEAR row.

## N4-XM -- key_crossmatch leads of 4 Oct 02:50 (Opus; cap USD 4; box 50 min)
Read: ROOM.md lines 2026-10-04 02:53-02:55 (key_crossmatch nightly), `tools/data/key_crossmatch_gate.json`, `python3 tools/key_crossmatch.py --help`.
1. fr3993-villeroy-1595 `keys/key_f159_letters.tsv` vs august-van-saksen-1561-64 ct58_sample/ct74/ct57 (stat 8.66/7.22/6.48, gate 3.29; AVS's
   own key reads ct74 at 7.49). Pre-register (`ciphers/august-van-saksen-1561-64/xmatch/PREREG.md`): matched control = two or three OTHER
   letter-alphabet keys of about the same size (count of letter values) from other targets on disk, run through the same tool on the same three
   ciphertexts; the lead is "generic letter-frequency artefact" if a control key of the same size reaches the gate too. Then read by eye: decode
   30 tokens of ct74 under villeroy f159 and under AVS's own key side by side -- how many tokens agree letter for letter? Is f159 a plain
   letter alphabet whose symbols overlap AVS's notation? Verdict in one paragraph in both folders' NOTES.md (append, section "N4-XM").
2. fr3416-nevers-fils-1589 `keys/key_no25.tsv` vs fr3993-gonzague-nevers-1595 (stat 6.0, cov 0.963, repeat of 3 Oct): one line confirming
   same key family (A3V-VNV01 03:18: Gonzague read by key no.70, period interlinear gloss) -- is no.25 the same table as no.70 or a relative?
   One line in fr3993-gonzague NOTES.md.
3. The short one (hellen R4370 key on rah-morillo rederiv, n=21): one line why it is below min_tokens (100) and not a lead.
No claim beyond "the tool's statistic reaches/does not reach the gate and the control does/does not"; no reading.

## N4-NXS -- fr16142-noailles-constantinople-1571: sign-sorter page for c510-516 (Opus; cap USD 5; box 60 min)
LANE-RUN2 (account 1) closed 04:02 UTC and asked account 3 to publish `run2/nxatl/sheets` + `run2/nxta|nxtb/focus.tsv`: read its ROOM
lines 02:59-04:02 and `run2/nxatl/REPORT.md`, `run2/nxaln` report, and post a ROOM line naming RUN2's claim before you start.
1. `python3 tools/sign_sorter.py --help`, `tools/sign_sorter_apply.py --help`, and one prior sorter page in the repo as a pattern
   (`grep -rl sign_sorter ciphers/*/NOTES.md | head`). Build ONE page for c510-516 (9,904 tiles): `--atlas run2/nxatl/atlas.tsv`, clusters from
   `run2/nxatl/clusters.tsv`, `--focus` merged from nxta + nxtb focus.tsv (c510, c515, c516), `--rank` if the tool supports a rank that does not
   need a key (else none). Build in your scratchpad first; report the page size.
2. If the page (and its data) keeps the folder under 30 MB, commit it under `ciphers/fr16142-noailles-constantinople-1571/sorter/` with the exact
   build command in a README.md; else commit only the build command + any small data file, and say the page must be rebuilt on the publishing
   side. Run the sorter tool's offline test if it has one. ROOM line: "for the account-3 orchestrator: Noailles c510-516 sorter page at <path>
   (<N> tiles, <MB>), publish for the owner's sort; RUN2-NXALN re-runs on its settled labels".

## N4-PAG65 -- clairambault1225-paget-1714: codes 65 and 116 (Opus; cap USD 2; box 35 min)
NOTES.md "Remaining gaps (RUN2-PAG)" names it: the same per-token reading as RUN2-PAG's settle7 for code 65 ("ab" over "Labbe") and the 116
g/ge neighbour conflict, ~$1. Use align/settle7.py's method (or extend it by option, no private copy), per-token S/M rulings, key.tsv /
exceptions.tsv, `decode_key.py --check` exit 0. A3V-VPAG/A3V-RD117P audited and re-derived the RUN2 state: if any token changes, say in the
done line that a rule-7 re-derivation of the new state is owed (do not do it yourself).

## N4-ES132 -- es132-vargas-mexia-1578: f.119v upper + f.120r under test 2 (Opus; cap USD 6; box 70 min)
NOTES.md "Test 2 (LANE-RUN2 RUN2-ES132)" and its Remaining gaps: same pipeline per page (`test2.py`, shape-notation passes, the
pre-registered gate (b) in PREREG_test2), ~$2.5 per page. Two pages: f.119v upper, then f.120r; stop before a page that would cross 80% of cap.
Only letters NOT in el-descifrador/cabinet-noir's list (`cabinet_noir_map.tsv`) -- check first. Crop commands pasted (they are in NOTES.md
for f.89r/v). Per page: err_2reader, gate numbers target vs controls, grades, a few phrases read by eye (Spanish), `test2.py --check`.
