# LANE LANE-RUN9-account-4 jobs (account 4) -- 6 Oct 2026 05:4x UTC, lane orchestrator session_01S1eWrEhfTEUrnYjwb91iQ7

Lane brief: .claude/briefs/default-lane.md (cap 60, box 05:39-15:39 UTC 6 Oct). WORK-QUEUE row LANE-RUN9-account-4: RUN8's named next steps
for folders s-z first (STATUS.md "LANE LANE-RUN8-account-4 handoff", "Open for the next s-z lane" 1-5), then tools/next_steps.py runnable
rows and the `parallel` action of blocked rows, cost band S and M, folders s-z only. The row's other named items (nla-heinrich, rayburn,
rousseau) are i-r and LANE-RUN9-account-2 already ran them (ROOM 05:18-05:24); eckert-1864 is a-h. Gate 0a met in-session (no
SESSION-SWEEP-account-4 row). VERIFY-BACKLOG.tsv: no s-z row. Off limits: Birago, Armstrong, Debosnys; bne20211-ferdinand-1478 and
destaing-gerard-1779 (account-4 standing session); baluze103; anything in a private repository.
Every worker: one job, then stop. Each job first checks its named step is still undone (NEXT-STEPS.tsv lags the folders): if a dated NOTES.md
section already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's cap and box and is not a machine
transcription pass the TRANSCRIPTION.md / CLAUDE.md Usage 6 sorter rule hands to the owner; otherwise stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN9-account-4".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host.
- Rule 3: any gate is pre-registered (a PREREG file committed and pushed before the scored run), with a matched control that can vary on
  the statistic tested; report both numbers. Rule 4 grades with counts. Rule 7: `tools/decode_key.py <folder> --check` (or the folder's
  own decode script --check) exit 0 before push if the reading or key changed. A reading change after AUDIT.md: say so in NOTES.md and
  flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md); keep both facts on conflict. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion. Solver/lookup jobs: report what was found
  and where it was not found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR` or the --ark/--canvas form); give
  subagents only crop paths, one page/leaf per call, never a full-page image. Price: ~1.5 per Sonnet subagent pass, reconciliation = 1 unit.
- Sorters: any sorter meant for the owner must PASS `python3 tools/sorter_preflight.py` and have 5+ random tiles opened against the line
  image before it is handed on; it is handed to the account-3 orchestrator (ROOM flag line) to publish. Never publish an artifact or edit
  ASKS.md yourself.
- No private-repository access in these sessions: if a step needs one, stop and say so in ROOM (the lane hands it to the standing session).
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN9-account-4",
  then a five-line final report.


## Wave 1 (spawned 05:4x UTC 6 Oct). Intake gate output (05:40 UTC) pasted per job.

### R9-MANTPOOL -- sachsstaatsarchiv-manteuffel-1712, pooled multi-code-run aligner gate (Opus; cap 4, box 70 min; disk only, no vision)
Intake gate: `sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN8 named step 1 / folder Verdict "cheapest next": the U codes (U 137) sit only inside multi-code glossed runs, where the per-leaf aligner's
S_multi is 0 on every leaf. Build a pooled aligner across the 7 transcribed glossed leaves (0501, 0502, 0527, 0528, 0529, 0530, 0574/0575;
files under r8mant/, pooled_mantp/, n9mant/): for each multi-code run, segment its gloss string among its codes (DP over gloss word/
syllable boundaries, codes with a licensed key.tsv value fixed), iterate hard-EM so a code's chunk agrees across runs (`tools/interlinear_align.py`
is the shared tool -- extend it with an option rather than writing a private copy, Usage 8). Pre-register (PREREG-R9-MANTPOOL.md, pushed
before the scored run): statistic = number of codes whose chunk agrees across >= 2 runs; matched control = gloss strings shuffled across
multi-code runs of the same code count (it CAN vary on the statistic -- check); known-answer control = hide 5 licensed C codes and report
recovery. Gate: real > shuffle p95 AND known-answer >= 3/5. If PASS, codes clearing it go into key.tsv at M only (S needs a verifier);
decode --check exit 0; update U count. If FAIL/tie, log the instrument per rule 3 (third-attempt clause if it applies). Update Remaining
gaps / Escalation; gaps_check.py pass.

### R9-SIENA7 -- siena-concistoro-2308 no. 7, anchored homophonic fit (Opus; cap 4.5, box 80 min; disk only)
Intake gate: `siena-concistoro-2308: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN8 named step 3a (R8-SIENA7 "Next step for no. 7"): homophonic fit of no. 7's 363 tokens (Bourdeau transcript, CC BY 4.0; sparse clone
of dbourdeau/cyphersolver targets/siena1421 if not on disk, read only) with the 7 C gloss values in glosses_no07.tsv fixed, Italian corpus
from tools/data (check era: 1421 Sienese; say which corpus and whether era-matched). Rule 3 first: matched control = synthetic Italian
plaintext of N=363, K=45 homophonic design with the same 7 fixed values (as count of fixed tokens, ~24%), same solver, >= 3 seeds; if the
control mean is below gate (e.g. 0.6 letter accuracy, pre-registered in PREREG-R9-SIENA7.md, pushed before scoring), stop: "non-test at
this N", do not score the target. If the control reads, run the target, report the plaintext candidate, judge it (`tools/judge_plaintext.py`
with an it-medieval corpus if one exists; paste output) and the shuffled-target decode through the same judge (rule 3 ARM-C1). No key.tsv
change beyond M without a verifier. Status stays `open` unless rule 5 says otherwise.

### R9-SIENA15 -- siena-concistoro-2308 no. 15, R4764 shape concordance (Opus; cap 4, box 70 min)
Intake gate: as R9-SIENA7. RUN8 named step 3b. Read READ2-SIENA's section on no. 15 and R4764 in NOTES.md for what the concordance is meant
to test; do it from images/transcripts on disk (if an image fetch is needed, one DECODE login with tools/decode_browser_login.js, scrub
the account name, images stay in the scratchpad; crop step pasted). Pre-register the concordance statistic and a control that can vary on
it before scoring. Do not overlap with R9-SIENA7 (no. 7 only there): write only a "## R9-SIENA15" NOTES.md section and its own files.
If the step is already done or undefined in NOTES.md, stop and report.

### R9-WVOSORT -- wvo-hessen-1564, f.23 enclosure owner sign sorter (Opus; cap 3.5, box 60 min)
Intake gate: `wvo-hessen-1564: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN8 named step 4 (R8-WVO1111 "Next"): f.23's sign inventory is unsettled (NX-WVO174 passes split 290 vs 335 tokens), so the next pass is the
owner's sorter, not a third machine pass (CLAUDE.md Usage 6). Build it with tools/sign_sorter.py from the image on disk (raw/ PDFs; crop step
pasted; focus.tsv = every pass split), run `python3 tools/sorter_preflight.py` to PASS, open 5+ random tiles against the line image, then
one ROOM flag line to the account-3 orchestrator to publish (db capability) with the path. Do not publish, do not edit ASKS.md. The
crib-placement test waits on the settled labels; do not run it.

### R9-HOUSE -- thurloe-printed index cells + sp90-raby-1704 LOCAL-QUEUE row (Sonnet; cap 2, box 40 min)
(a) thurloe-printed: R8-THURV2 flag -- index.tsv P27/P28 `cipher_system` cells still carry the OCR-era "different sub-key" note; R8-THUR25
showed it was an OCR shift (same Manning key). Correct the two cells to what NOTES.md R8-THUR25 / AUDIT.md revision now say, nothing else.
(b) sp90-raby-1704: RUN8 named step 5 -- Preuss 1897 (Google Books UfnriIriq9UC) pp.20-30 and 61 cannot be read from the cloud (page view
blocked). Append one LOCAL-QUEUE.tsv row in the file's existing column format (read tools/local_runner_brief.md and the last 5 rows first)
asking for those pages' text relevant to the folder's question (state it from NOTES.md), only if no existing row already asks it (grep).
Run `python3 tools/key_livecheck.py` first and quote its Google Books line in the row (CLAUDE.md Access playbook). Both: rebase before
writing; file_shrink_guard on both files.

### R9-SRCH -- s-z printed-source greps (Sonnet; cap 3, box 60 min; archive.org / be-api / Google Books API only)
Four free crib/identification searches named as each folder's `parallel` action; for each, first check the folder's NOTES.md that it was not
already run, then run it and write a dated "## R9-SRCH" section in that folder's NOTES.md (what was searched, ids, hits with quoted lines,
"not found in <source>, searched by <method> on 6 Oct 2026"): (1) sp87-chesterfield-1747: Coxe, Pelham Administration (1829) for
July-Aug 1747 Waldeck/Cronstrom despatches to Cumberland; (2) sp78-doncaster-1621: CSP Venice vol. 17 for Doncaster's Sept 1621
audiences; (3) sp87-newcastle-1743: be-api "Munchberg" across HMC reports and Yorke's Life of Hardwicke; (4) sp36-stquentin-pretender-1743:
be-api "St. Quentin" + "Chevalier" across published Stuart Papers selections (HMC Stuart Papers). Search results only; no decode.

## Wave 2 (spawned as wave-1 slots free, from 06:0x UTC 6 Oct). Intake gate output (05:40 UTC) pasted per job.

### R9-UNTB2 -- untersberg-code symA reference class from the illustrated openings (Opus; cap 3.5, box 70 min)
Intake gate: `untersberg-code: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder's named next step (R8-UNTB, NOTES.md end): find a crossed-descender p (the F4 reference class) in Latin-script words and painted
captions on openings 12-28 (opening 27's tablets first, 1225 px on disk, then native). Screen with 400 px thumbnails first; crop only leaves
with Latin script (crop step pasted; Salzburg Museum IIIF, >= 2 s apart, descriptive UA). Reuse R8-UNTB's PREREG resolution control (3
R instances required); if it now passes, run the symA tally exactly as pre-registered and keep L6 tok3 apart (R8-UNTB observation 1). If
no crossed-descender p exists in the manuscript, log F4 untestable within this manuscript and add it to the paleographer crop packet
(SO-UNTERSBERG-LEADS item 2) as a NOTES.md line; nothing else. Rule 4 counts.

### R9-ZESCH -- zeschau-seebach-1841 word-segmentation objective on pooled R5005-R5007 (Opus; cap 4, box 70 min; disk only)
Intake gate: `zeschau-seebach-1841: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder's Verdict cheapest next (RUN4-WAITBF): first check Bourdeau's stated next step for this item (dbourdeau/cyphersolver, sparse clone,
grep only; GAPS185 duplicate-effort risk) -- if he has run or published it, stop and report. Otherwise: a word-segmentation objective
(French, era-matched corpus from tools/data if one exists -- say which) on the pooled R5005-R5007 syllabary ciphertext, with the matched
control FIRST (synthetic French, same N, same symbol inventory size and syllabary design, >= 3 seeds; gate pre-registered in
PREREG-R9-ZESCH.md, pushed before scoring; check the control is not already at ceiling and CAN fail). Control below gate: stop, "non-test
at this N", target not run. GAPS202's 4-gram annealer is retired (rule 3 third-attempt clause): this must be a genuinely different
objective, say how. Update Remaining gaps / Escalation; gaps_check.py pass.

### R9-LIPP -- ss-radio-lippert-1944 Wayback CDX retry (Sonnet; cap 1.5, box 30 min)
Folder's named next step: test `curl -sS -o /dev/null -w "%{http_code}" https://web.archive.org/` first; if it answers, run the CDX search
for `ebay.de/itm/*284276746819*` and the seller's other items (one request at a time, >= 2 s apart, stop on reset/429; one retry after a
pause), fetch any capture with the `if_` form, and record what the listing shows (images, text, date) in a dated NOTES.md section. If
web.archive.org still resets, append one LOCAL-QUEUE.tsv row for it in the file's format (grep for an existing row first). Search results
only.

### R9-WVOALIGN -- wvo-hessen-1564 f.23 interlinear alignment (Opus; cap 6, box 90 min; 2 Sonnet passes + 1 reconciliation, row-pair crops)
Intake gate: `wvo-hessen-1564: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
R9-WVOSORT's observation (NOTES.md "f.23 owner sign sorter", grade M by eye): f.23 is 20 alternating rows, German clear rows over 10 cipher
rows, apparently a letter-over-sign interlinear decipherment. Test it: (1) cut 10 row-pair crops (clear row + the cipher row under it;
crop step pasted, from the image on disk, reuse sorter/ geometry where it helps); (2) transcribe clear rows (German, letter-spaced) and
cipher rows: 2 blind Sonnet passes, one row-pair crop group per call (price 1.5 per call; at most 2 calls per pass), sign labels = the
sorter's provisional pile ids where possible so the owner's later sort can relabel mechanically; reconcile (1 unit); (3) PREREG-R9-WVOALIGN.md
pushed before scoring: statistic = number of cipher signs whose letter value is consistent across >= 2 rows (and the "worden sei"/"zweimahl"
checks named in NOTES.md); control = the same alignment against row-shuffled gloss/cipher pairs (can vary on the statistic -- check),
>= 200 draws; gate real > control p95; (4) run `tools/interlinear_align.py` (extend it with an option, never a private copy). If PASS, write
key.tsv (grade C only where the gloss letter sits over a single sign and recurs consistently; M otherwise), a decode with the folder's
decode config and `--check` exit 0, rule 4 counts, and correct the folder's "no interlinear gloss" statements (Verdict, Premise check,
"Images opened") with a dated note -- do not delete them. A reading change after AUDIT.md (if any): flag for a verifier. If FAIL/tie,
log it; status stays `open`. Report what was found and where it was not found; do not classify novelty.

### R9-MANTPC -- sachsstaatsarchiv-manteuffel-1712 per-code shuffle test on R9-MANTPOOL's 24 codes (Opus; cap 2.5, box 50 min; disk only)
Intake gate: `sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder Verdict cheapest next (R9-MANTPOOL): the blended PASS (24 vs p95 19, mean 14.9) cannot say which codes carry the 5-10 codes of signal.
Pre-register (PREREG-R9-MANTPC.md, pushed before scoring) a per-code test on r9mant/codes_r9.tsv: for each of the 24 codes, its agreement
share against the same code's share under the 1000 within-bin gloss shuffles (r9mant/shuffle draws; regenerate if not stored), with a
multiple-comparison correction stated in advance (e.g. Benjamini-Hochberg q 0.10), plus a per-class breakdown (letter / syllable / word
codes; rule 3 AX-NAMES lesson). Codes that clear: note "per-code PASS" in key.tsv's note at M (no S without a verifier); codes that fail:
key.tsv note "per-code FAIL", and if a code's value is no better than chance remove it from key.tsv (decode --check exit 0, recount U).
Update NOTES.md, HYPOTHESES.md, Remaining gaps / Escalation; gaps_check.py pass; ROOM flag for a verifier (reading changed after AUDIT.md).

## Wave 3 (spawned 06:2x UTC 6 Oct). Intake gate output (05:40 UTC) pasted per job.

### R9-WVOV -- wvo-hessen-1564 f.23, VERIFIER (Opus; cap 4, box 70 min)
Intake gate: `wvo-hessen-1564: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (now `partial`, R9-WVOALIGN).
You are a VERIFIER, separate from the solver (R9-WVOALIGN, session_018jdurbcUgRBMVtqcdMv3yV). Claim under audit: NOTES.md section "f.23
interlinear alignment" (R9-WVOALIGN, 6 Oct 2026): f.23 of WVO 1109 (Orange to Wilhelm of Hesse, 18 Sept 1564, HSAM) carries its own
letter-over-sign interlinear decipherment; PREREG-R9-WVOALIGN gate PASS (pile ids 10 vs row-shuffle p95 3); key.tsv 10 C / 18 M; decode
C 102 M 155. Follow CLAUDE.md "Verifier brief (template)" steps 1-5 in full, plus: (a) re-run the alignment and `tools/decode_key.py
ciphers/wvo-hessen-1564 --check` yourself; check 10 random gloss-over-sign pairs against the row-pair crops by eye; check the
row-shuffle control can vary on the statistic; (b) is the German gloss a period decipherment (grade H/C per rule 4 -- say which and why)
and does it read as continuous text (paste it); (c) novelty search per the template, with phrase searches on the gloss text (Groen van
Prinsterer 1e serie I, WVO's own Opmerkingen, Demandt's Nassau-oranische Korrespondenzen if reachable, Google Books / IA / HathiTrust EF);
JSTOR rows to JSTOR-QUEUE.tsv in both families; (d) depth per rule 4a with `tools/depth_check.py`; (e) write AUDIT.md (N-class, key
source per rule 10, depth, safe/unsafe sentence); if N3+, append the SECOND-OPINIONS-QUEUE.tsv row in the same session; (f) status.json:
wvo-hessen-1564 has no entry -- add the result fields the way other targets' entries are shaped (read two first) and run
`tools/near_check.py` if you touch NEAR.md. Do not decode beyond re-running the solver's scripts; do not touch other targets.

### R9-WVOX -- wvo-hessen-1564 f.23 key vs the 1069 and 174 keys of willem-van-hessen-1567 (Opus; cap 3, box 60 min; disk only)
Intake gate: as R9-WVOV; `willem-van-hessen-1567: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Same two correspondents, 1564 / 1567 / 1069's date: does f.23's interlinear key (wvo-hessen-1564/r9align/, key.tsv) share sign->letter values
with willem-van-hessen-1567/siblings/key_1069.tsv and key_174_nomenclator.tsv? Build a shape concordance between the three sign inventories
(by sign description/crop, from files on disk; crop step pasted if you cut any), pre-register (PREREG-R9-WVOX.md in wvo-hessen-1564, pushed
before scoring) the statistic = number of concordant shapes carrying the same letter, control = letter labels permuted within each key
(>= 1000 draws; it can vary on the statistic -- check). If PASS, apply f.23's C values to the 174 letter body's transcribed spans that have
no value yet (willem-van-hessen-1567 files; M grade only), decode --check where a decode config exists, and say what reads. If FAIL, log it
in both folders' HYPOTHESES.md. Coordinate with R9-WVOV (it writes AUDIT.md/status.json of wvo-hessen-1564; you do not).

### R9-SIENA7B -- siena-concistoro-2308 no. 7, second blind line-crop pass for an error figure (Opus; cap 4, box 70 min)
Intake gate: `siena-concistoro-2308: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
R9-SIENA7 named next: the anchored-fit negative is conditional on transcription (control falls to gate at ~10% injected error; no. 7 error
unmeasured). One DECODE login (tools/decode_browser_login.js 4796, as R8-SIENA7 did; scrub account name; image in scratchpad, sha1 vs
manifest), R8-SIENA7's iiif_lines.py crop command (pasted), one blind Sonnet pass over the cipher lines (Bourdeau's sign labels supplied as
the reference sheet, not his transcript; <= 3 calls, crops only), then measure per-sign disagreement vs Bourdeau's no07.tok (aligned; report
substitution/insertion/deletion rates) as the error figure. If the error is below ~8%, say the R9-SIENA7 negative stands as control-backed at
that error; if above, say it is a non-test and name the next step. No key change. Price: 3 passes x 1.5 + 1 reconciliation.

### R9-ZESCH2 -- zeschau-seebach-1841 same word-parse objective, stronger search (Opus; cap 4, box 70 min; disk only)
Intake gate: `zeschau-seebach-1841: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
R9-ZESCH named next: control was below gate (0.0026 vs 0.60) but the true key scores 1181.7 > annealer best 957.4, so the search is the limit.
Same objective (wordseg_syllabary.py, unchanged), a genuinely stronger search (parallel tempering or many-restart + crib-free greedy
initialisation; say how it differs), PREREG-R9-ZESCH2.md pushed before scoring, matched control FIRST at the same N/inventory (>= 3 seeds,
gate 0.60 unchanged). Control below gate: stop, log "non-test at this N" -- and since this is the second attempt at this objective, say
explicitly whether a third would be rule 3's third-attempt case. Control at gate: run the target, judge the decode with a French corpus
(say era) and the shuffled-target decode through the same judge (ARM-C1). Status partial; gaps_check pass.
