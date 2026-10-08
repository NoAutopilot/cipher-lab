# LANE DEFAULT-account-2-20261008-0710 jobs (account 2) -- 8 Oct 2026 07:2x UTC, lane orchestrator session_01DmKMLEo17qiXvRU7NGoG7g

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 07:11-17:11 UTC. Gate 0a clear (SESSION-SWEEP-account-2 done 5 Oct, ROOM 9073).
Backlog a: VERIFY-BACKLOG regenerated 07:14 UTC: top row eckert-1864 E74 (LS-V7 one-audit N3, D1) is not in AUD2-LS-H's scope (E66 E68
E70 N2-BN) and ST-LEDGER-2 closed 05:46, so D2V-E74 takes it; Birago off limits; nla-heinrich and colbert26 are N0 (gate 2 applies above N1).
Backlog b: `tools/next_steps.py --hot-only` (exit 0) runnable rows and blocked rows' parallel actions, filtered against ROOM claims < 6 h
and 7-8 Oct live briefs. Excluded: Birago, Armstrong, Debosnys; every folder LANE DEFAULT-account-1-20261008-0540 touched (fr5160,
decode-1411, fr16045, fr4715-vieuville-pool, pro3055, na-suriname, clairambault296/1225, maurice-rupert, fr5761, fr3975, rah-juan-manuel,
baluze167, clair1161, fr16142); the Nevers no.41/no.60 pool held by LANE BNF-FOCUS (fr3613/3622/3983-3990); sforza-*, na-oldenbarnevelt.
Every worker: one job, then stop. First check the named step is still undone (a later ROOM done line or NOTES section may have run it);
if it was, write one ROOM line saying so and stop.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-2-20261008-0710". If --start
  fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host. Prefer files already on disk.
- Rule 3 (matched control first; a control that cannot differ from the target on the statistic is a non-test), rule 4 grading, rule 7
  (`--check` scripts). Pre-register any new gate in a PREREG-<JOB>.md pushed before the score is computed. A reading change after AUDIT.md:
  say so in NOTES.md and flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md, NEXT-STEPS.tsv); keep both facts on conflict.
  Commit only your own paths. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with
  `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the owner; never
  print credentials (test presence with `test -n`). Never call AskUserQuestion. Solver jobs: report what was found and where it was not
  found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half done
  writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR ...` or the `--ark/--canvas` form, or the
  folder's existing crops); read line or strip crops, never a full page image; one page (or half page) per subagent call. Price ~1.5 per
  vision call, reconciliation one more unit.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE
  DEFAULT-account-2-20261008-0710", then a five-line final report.

## Wave 1 (spawned 07:2x UTC 8 Oct)
Intake gate 07:2x UTC (tools/intake_gate_check.py, each exit 0):
`fr4712-nevers-duchesse: open (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`colbert26-lathuillerie-1644: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`fr16106-vivonne-longlee-1579: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`heinsius-vanhaersolte-1703: open (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`bl-gualterio-1700: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.

### D2V-E74 -- eckert-1864 E74 second adversarial audit (VERIFIER, Opus; cap 4.5, box 90 min)
Claim under audit: status.json results[179], "Eckert 1864: Stanton (Brutus) to Chas Armond, 11 Sept 1864, the publication of Sanders'
despatch an enormous blunder (E74; clear text, signature in cipher)", N3, D1, audit_status one audit (AUDIT.md "## AUDIT (LS-V7)", l.~2823).
You are a separate session from the solver and from LS-V7; do not protect either. CLAUDE.md "Verifier brief (template)" steps 1-5, with the
second-audit emphasis of Outreach gate 2: search to disprove novelty. Pointers the first audit left open: identify "Sanders" (the
George N. Sanders / Niagara Falls "Tycoon" correspondence of July-Sept 1864 is the obvious candidate -- test it against the date) and the
addressee "Chas Armond"; search the 1864 press pages LS-V7 listed as unread (Chronicling America / LOC JSON API, loc.gov is reachable),
Lincoln Collected Works (Basler) and Stanton's printed papers, OR ser. I vols 39/42/43 and ser. III vol. 4 (IA; record if unreachable),
and the Huntington CONTENTdm route with `CISOSEARCHALL` on addressee/subject names for same-date sibling copies (lesson of AUD2-LS-H,
which lowered E70 to N2 that way). Open-index pass (OpenAlex, S2 with keys), Google Books (country=US), one JSTOR-QUEUE.tsv row per family
(i) and (ii) if not already queued. Depth stays as set unless you find cause (it is D1: only the signature is in cipher). Write
"## AUDIT 2 (second adversarial, D2V-E74)" to ciphers/eckert-1864/AUDIT.md; set results[179] audit_status 'two audits' (and lower the
class if print is found); update SO-ECKERT-E74 in SECOND-OPINIONS-QUEUE.tsv if the class or safe sentence changes. Do not decode. Do not
touch other eckert items. Note the account-3 orchestrator's AUD2-LS series works in the same AUDIT.md: rebase before every write.

### D2-F4712 -- fr4712-nevers-duchesse: apply ASKS 113's answer to the six f.13r carries (solver, Opus; cap 3, box 60 min)
NOTES.md "## Owner eye check, ASKS 113 (5 Oct 2026 04:01 UTC)" and "## Next step (FRESH-0914, 7 Oct 2026)": the owner's eye check said
same writer ("I think the same"); ASKS row 113 states the pre-registered rule: then f.13r's six H glosses (82 "D. n.", 21 "Berry",
12 "b. Pal.") carry to six of f.10r's 37 tokens at grade C. Read PREREG_duchf13.md and f13_carry.py first and apply exactly what was
pre-registered (no new gate); R11A-F4712's blind digit-hand NON-TEST (6 Oct) does not override a person's eye check, but record both side by
side. Re-run the decode with `--check` (tools/decode_key.py or the folder's script), update grades and counts (rule 4), NOTES.md Remaining
gaps/Escalation if partial, HYPOTHESES.md row, and if a status.json result exists for this folder, update it; flag in ROOM for a verifier if
a reading changes after an AUDIT.md. No network. Report the six tokens and the new H/C/S/M/I counts.

### D2-HEIN -- heinsius-vanhaersolte-1703: Deel 2 small-number re-grep (worker, Opus; cap 2.5, box 60 min)
NOTES.md "## Next step (cheap, depends on no one; updated R12A-HEIN, 6 Oct 2026)" item 1: re-grep the ~70 Deel 2 pages A2P4-HAER read
(section l.139ff) for small-number runs of letter 1017's kind (numbers 1-70 inside running text, not footnote or page numbers), which
A2P4's 140-199 grep could not catch. Route: Huygens retroboeken (CLAUDE.md host table: >= 2-2.1 s apart, descriptive UA, ~95-128 per
session); script only, save the fetched page text under the folder (or scratch with a manifest) once. Define in the script, before running,
what counts as a candidate run (e.g. >= 3 numerals 1-70 within 40 characters, excluding dates, page refs, money and ordinals) and test it on
letter 1017's own page as a positive control (it must fire) and on 3 Deel 2 pages with no cipher as a negative. Report every hit with page
and letter number; eye-read only hits, from text. Update NOTES.md (section + Next step list), no status change unless cipher is found.

### D2-GUALT -- bl-gualterio-1700: HMC Stuart Papers calendar, "Vernon" grep (worker, Opus; cap 2, box 45 min)
NOTES.md "## D4-GUALT (6 Oct 2026)" last bullet and "## Next step (costed, CS-BATCH5)": the Stuart Papers calendar entries for the Vernon
group (Count F. de Vernon, Sardinian minister in France 1719-1723, BL Add MS 20554-20556 "many in cipher", key at Add MS 20582 f.74b) were
not on disk. Fetch the `_djvu.txt` of the seven HMC *Calendar of the Stuart Papers* volumes once (archive.org advancedsearch to get the
identifiers -- vol. I is `calendarofstuart01grea`; 1.5 s apart) and grep for Vernon / "Comte de Vernon" / Gualterio + cipher / "cypher"
/ "deciphered" in the 1713-1727 window. Report hits with volume, page (from the djvu page markers where present) and the surrounding line;
in particular any calendared letter whose text is printed in clear and that matches a Vernon cipher letter by date (a possible crib). No
reading, no key. Update NOTES.md and the Next step; status stays open.

### D2-COL26 -- colbert26-lathuillerie-1644: value-independent test of the M-lowered codes + canvases 11/29 retry (solver, Opus; cap 6.5, box 110 min)
Known-text target (N0, AUDIT 1 DA1-COLV): allowed because the step builds the key for the unglossed Jan-Feb 1648 La Haye siblings.
Verdict line (NOTES.md l.~2020) and AUDIT.md AUDIT 1 l.39-50: DA1-COLV lowered 20 (i), 30 (s), 67, 81, 85 (na), 96 (que) to M because
their values were chosen on the R10-COL26B value-choice units (IN). Step: pick the glossed sibling unit(s) OUTSIDE every value-choice unit
(read AUDIT.md's IN/OUT list first; canvases 30/32/50/51 are candidates only if OUT -- canvas 50 and 30/32 reconciled transcriptions are
on disk in siblings/, so prefer a unit already transcribed and use no vision call if possible), pre-register in PREREG-D2-COL26.md (the
six codes, the word-grain ordered-walk statistic as in verify_colv.py, the shuffled-gloss and length-matched controls, gate P < 0.05/6
per code or pooled as you register, n floor) and push it before scoring. If no OUT unit carries enough of these codes, say TOO-SHORT and
stop that unit (no new transcription unless one canvas of <= 8 line crops would do it: 2 blind passes + reconciliation = 3 units ~4.5).
Then the loose-ends retry: Gallica canvases 11 and 29 of Part I (HTTP 500 before), one request each (one retry after a pause), note
whether either carries cipher. Rule 3 per-unit merge clause applies to any key change; `tools/decode_key.py ... --check`. Update
NOTES.md, HYPOTHESES.md, gaps sections; flag in ROOM for a verifier if any grade moves.

### D2-VIVX -- fr16106-vivonne-longlee-1579: apply D4-VIVV's crosswalk fixes and re-score (solver, Opus; cap 4, box 75 min)
NOTES.md "## D4-VIVV" item 4: three crosswalk misses found by eye against the Mousset 1912 table (key/mousset1912_plviii_table.jpg,
plix_w500.jpg): 'o' marked "no glyph" where the readers' adjacent '1 o' / 'ı o' is the table's x = "10"; cc = '8' missing from the '8'
row; 'H' omitting b.g2 (boxed H); plus the 'z' label mixing the Ze ligature with 3. Apply these fixes to the crosswalk only (no relabelling
of the transcription), pre-register in PREREG-D2-VIVX.md that the gate, statistic, nulls and control are those of PREREG_vivmous.md /
PREREG_vivv.md unchanged (no new knob), push, then re-run vivmous.py and the vivv contamination checks. Report old vs new (0.45 vs p99
0.398) and whether every number moves together. If it does not move, that is the second attempt of this instrument: log it in HYPOTHESES.md
and the Escalation as rule 3 would require; do not tune further. Grades stay M/I unless a clause reads (rule 4, rule 4a). Disk only.
