# LANE LANE-RUN13-account-4 jobs (account 4) -- 6 Oct 2026 17:4x UTC, lane orchestrator session_01FDkvT3PQo6q9YnARRsCgjP

Lane brief: .claude/briefs/default-lane.md (cap 60, box 17:36 UTC 6 Oct - 03:36 UTC 7 Oct). WORK-QUEUE row LANE-RUN13-account-4: verifier
propagation flags first (both outside s-z or already done: R14-OLDV/R15-OLDUV oldenbarnevelt held by account 2, R11A-AVSV2 august-van-saksen
16:05), then NEXT-STEPS runnable rows, split s-z. `next_steps.py --hot-only` gives one s-z runnable row (manteuffel); plain NEXT-STEPS.tsv
gives 10, of which 4 carry an untried step that depends on nobody (manteuffel, siena, scorpion, sp90-raby); the other six are stale or
need a person (sp78/sp99 TNA orders, ula done by D2B-ULA, untersberg paleographer, viganego blocked, yogtze parent decision) and get one
housekeeping job. Gate 0a: no SESSION-SWEEP-account-4 row. VERIFY-BACKLOG: no s-z row needs a verifier. five_hour `allowed` at 17:4x.
Off limits: Birago, Armstrong, Debosnys. No Gallica job in this split.
Every worker: Opus 5.5, one job, then stop. Each job first checks that its named step is still undone (a dated NOTES.md section may already
have run it); if so, correct the NOTES.md next-step line, stop and report rather than inventing work.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN13-account-4".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on
  the statistic tested; report both numbers. Rule 4 grades with counts. Rule 7: `tools/decode_key.py <folder> --check` (or the folder's
  own decode script --check) exit 0 before push if the reading or key changed. A reading change after AUDIT.md: say so in NOTES.md and
  flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md, NOTES.md of a folder another job also touches);
  keep both facts on conflict. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with
  `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Report what was found and where it was not
  found; do not classify novelty (verifier jobs excepted, where the brief says).
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call (or the stated crop batch), never a full-page image. Price: ~1.5 per Sonnet
  subagent pass, reconciliation = 1 unit. Thumbnail/contact-sheet triage by the worker's own eye at low resolution is allowed.
- Sorters: any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles opened against the line
  image; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never publish an artifact or edit ASKS.md yourself.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN13-account-4",
  then a five-line final report.


## Wave 1 (spawned 17:4x UTC 6 Oct). Intake gate output (17:4x UTC) pasted per job.

### R13-MANTSCR -- sachsstaatsarchiv-manteuffel-1712: inventory screen of uninventoried Loc. 694/08-09 frames (Opus; cap 3.5, box 60 min)
Intake: `sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`
Gap "Loc. 694/08 and /09 ciphered reports, 847 of 894 frames not inventoried" (NOTES.md ## Remaining gaps; 148 seen, ~746 unseen). Frame URLs:
images/loc694-08-09/frames.tsv; already-seen lists in the GAPS184/GAPS201/N9-MANT2 inventories (n9mant/inventory_0504_0578.tsv etc.). Screen the
frames AFTER 0580 (694/09 side, Jan-1713 onward) at stride 5, skipping any already seen, by your own eye at reduced size (contact sheets of
~12 thumbnails, no subagent): per frame record code-bearing y/n/possible, glossed y/n, code range letter (<400) or nomenclator (>400) where
legible. Unit = one contact sheet of 12 frames, ~0.35 each incl. fetch; plan ~5 sheets (~63 frames), stop before a sheet that would cross 80%.
archiv.sachsen.de: one fetch at a time, >= 1.5 s apart. Write r13mant/inventory_0581_plus.tsv, update the gap line counts and the Escalation
image-check line, and name the top 3 glossed nomenclator-range frames (the ones that could give values for f.410's 24 U codes) as the next step
with cost. No transcription, no key change. gaps_check passes.

### R13-SIENAJ -- siena-concistoro-2308: agent-J confound check, blind second-reader sign concordance no. 7 vs nos. 9/19 (Opus; cap 3.5, box 60 min)
Intake: `siena-concistoro-2308: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md ## R11-SIENAPOOL: nos. 19 and 9 share no. 7's sign stock above the null, but all three were transcribed by Bourdeau's agent J. Remove the
confound: pre-register (PREREG-R13-SIENAJ.md, pushed before scoring) a sign-concordance test where YOU (or one Sonnet subagent per pair, crops
only) read the sign shapes of no. 7 and of no. 19 (then no. 9 if the box allows) from the images, blind to agent J's labels, building your own
sign inventory per letter and a concordance (same shape / different) between letters; then recompute R11-SIENAPOOL's overlap statistic on YOUR
labels against the same null. Images: images/manifest.json first; if nos. 9/19 are not on disk, one DECODE browser login per CLAUDE.md
(tools/decode_browser_login.js), fetch only what is needed, scrub the account name. Crop step mandatory (tools/iiif_lines.py --image ...).
Units: 2 pairs x ~1.5 + 1 reconciliation. If the overlap survives on blind labels, say so and name the pooled-nomenclator run (no. 7+19+9,
R10-SIENA7N family) as next with cost; if it does not, record the confound as the explanation. Nothing read; status stays open.

### R13-SCORP2C -- scorpion-1991: blind second-coder distinct-code test (Opus; cap 2, box 45 min)
Intake: `scorpion-1991: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md ## Cheap test 3 (A2P4-SCORP2) verdict names "a distinct-code statistic preregistered with a second, blind coder (one coder's codes
decide both sides here), about USD 1". Pre-register the statistic and threshold (PREREG-R13-SCORP2C.md, pushed first) with a control that can
differ from the target on it (rule 3). Then have ONE Sonnet subagent, given only the S1 sign crops and the Zodiac Z408/Z340 alphabet sheet the
earlier test used (no earlier codes, no NOTES), assign codes blind; compute the statistic on its codes and on A2P4-SCORP2's, report agreement
(kappa) and both numbers. Result into NOTES.md and HYPOTHESES.md. Search/compare only; nothing read; status stays open.

### R13-RABYPDF -- sp90-raby-1704: Preuss 1897 retry (Opus; cap 2, box 40 min)
Intake: `sp90-raby-1704: open (line 1) -- edition/page or full-text-search citation found within 6 lines`
NOTES.md ## R8-RABY: Google Books `UfnriIriq9UC` (Preuss 1897, full view, public domain) PDF download got one 429 at 04:0x UTC; R9-HOUSE filed
LOCAL-QUEUE L61 for pp.20-30 and p.61. Check L61 is still unanswered (if answered, read the answer and stop). Then ONE retry of the PDF download
(books.google.com, browser UA, a single request; on 429/captcha stop the host, no loop), or via an Internet Archive / HathiTrust-EF copy if one
now exists. If the text is obtained: read pp.20-30 and p.61 for Raby, Reichard/Reichart, Berlepsch, intercepted or ciphered letters of 1704 and
quote what is found (search result, rule 10); if it fails, log it and leave L61. Update the next-step line either way.

### R13-STALE -- housekeeping: stale next-step lines in six s-z folders (Opus; cap 2, box 40 min)
NEXT-STEPS.tsv lists these as `runnable`, but their parsed step is done or needs a person: sp78-yorke-1749 (picks a "[done 2 Oct ...]" line;
real next = TNA page-copy order), sp99-wotton-1622 (D4-SP99 done 6 Oct; next = f.251/f.159 copy order), ula-degeer-1644 (while-waiting step done
by D2B-ULA 6 Oct), untersberg-code (paleographer packet = needs-person), viganego-torino-1717 (blocked, read its "## Next step (costed)"),
yogtze-1984 (parent decision on re-label). For each: read the latest dated sections, confirm, and write ONE dated, current next-step line where
tools/next_steps.py will parse it (read its docstring for the parsed forms), naming the real blocker (needs-person / waiting-on <row> / done)
or, if you find a genuinely untried step that depends on nobody, name it with a cost and say so in your report (do not run it). No status-line
change unless rule 5 requires it. Re-run `python3 tools/next_steps.py` and confirm each folder no longer shows a stale `runnable`
(commit NEXT-STEPS.tsv only if that is the tool's normal practice).

## Wave 2 (spawned 18:0x UTC 6 Oct), from wave 1's named next steps. Wave 1 cost (get_session): MANTSCR 2.85, SIENAJ 3.58, SCORP2C 2.13,
RABYPDF 0.99, STALE 2.10 = 11.65. Intake gates as wave 1 (untersberg-code run below).

### R13-MANT85 -- sachsstaatsarchiv-manteuffel-1712: frame 694/09 0085 transcription and per-leaf gloss gate (Opus; cap 5, box 70 min)
R13-MANTSCR found 694/09 0085 is a glossed nomenclator-range frame (values to 483/501, M) -- the only one outside 694/08 so far, i.e. possible
glosses for f.410's 24 U codes and f.409v's open codes. Follow the RUN3-MANT / GAPS195 pattern exactly (read those NOTES sections first): crop
step pasted (tools/iiif_lines.py --image), 2 blind Sonnet passes of the code groups + gloss lines (one call per crop batch) + 1 reconciliation
unit (~1.5 each = 4.5), PREREG of the per-leaf gate (single-code and multi-code gloss consistency vs shuffle p95) pushed before scoring.
Only if the leaf's own gate PASSes (CLAUDE.md rule 3, per-unit gate before merge) may codes enter key.tsv, graded C/M, with conflicts with
Krauske logged, never resolved by majority (rule 4); then decode_key --check exit 0 and report the U-count change on f.410/f.409v. A TIE or FAIL:
nothing merges, log it. Any change to f.410's reading after AUDIT.md -> ROOM flag for a verifier. gaps_check passes.

### R13-SIENA719 -- siena-concistoro-2308: pooled no. 7 + no. 19 homophonic+nomenclator family run (Opus; cap 3, box 50 min)
R13-SIENAJ: no. 19 still clears no. 7's sign stock on blind labels (pJ 0.0015 vs gate 0.0033); no. 9 does not; reader-bias control not run. Pool
no. 7 + no. 19 (481 tokens on J's transcripts) for the R10-SIENA7N family with a matched control AT THE POOLED N and K (rule 3; read
R10-SIENA7N's control design and its blind baseline first -- if the control at pooled N is below its gate, stop: CONTROL BELOW GATE, non-test).
Use tools/family_run.py or the R10-SIENA7N script; HYPOTHESES.md row with both numbers. Disk only, no DECODE. Nothing is read unless the
target clears; any reading is graded and goes to a verifier. Status stays open unless rule 5 says otherwise.

### R13-UNTOP -- untersberg-code: opening-27 painted inscription, blind 2-pass transcription (Opus; cap 4.5, box 60 min)
R13-STALE's "## Next step (R13-STALE, 6 Oct 2026)": blind 2-pass transcription of the 3-line opening-27 inscription (native crops via
tools/iiif_lines.py --image, crop step pasted; one Sonnet pass per line batch per pass) + 1 reconciliation, collated against Herzog's "Vgl. fol. 27"
apparatus, to see whether symA-like signs occur in a second context. Read TRANSCRIPTION.md's sorter rule first: if the sign inventory is
unsettled and the two passes split > 10%, stop after the passes and name the sorter step (do not run a third machine pass). Paste
`python3 tools/intake_gate_check.py untersberg-code` output first; a nonzero exit stops the job. Report symA occurrences found / not found.

## Wave 3 (spawned 18:4x UTC 6 Oct). Wave 2 cost (get_session): MANT85 3.40, SIENA719 1.53, UNTOP 3.19 = 8.12.

### R13-SIENAWC -- siena-concistoro-2308: structural word-code restriction, control first (Opus; cap 3, box 50 min)
R13-SIENA719's next step (b): add a tool option (to the shared annealer the R10-SIENA7N script uses, e.g. tools/families/homophonic_anneal.py
or wherever it lives -- an option, not a private copy; offline test in tools/tests/) that allows word codes only on signs J tokenised as
multi-character units or on drawn (non-letter, non-digit) signs. PREREG pushed first. Run the matched control at the pooled N=481, K=62 with the
same restriction applied to the synthetic; G2 nomenclator recall gate as R13-SIENA719's PREREG. CONTROL BELOW GATE -> stop, log non-test, and
since this is a genuinely different instrument, log it as such (not a third attempt at the old one). Only if the control clears, run nos. 7+19.
HYPOTHESES.md row with both numbers. Disk only. Status stays open unless rule 5 says otherwise.
