# LANE LANE-RUN8-account-4 jobs (account 4) -- 6 Oct 2026 03:4x UTC, lane orchestrator session_01WJDfJbsRjgvoazG3ivjfVQ

Lane brief: .claude/briefs/default-lane.md (cap 60, box 03:39-13:39 UTC 6 Oct). WORK-QUEUE row LANE-RUN8-account-4: RUN7's named next steps
for folders s-z first (thurloe verifier propagation; manteuffel 0527 zoom then 0530 -- see below), then tools/next_steps.py runnable rows and
the `parallel` action of blocked rows, cost band S and M, folders s-z only, ranked by PROGRESS.tsv closeness to a counted N3+/D2+ result,
BnF tie-break. Gate 0a met in-session (STATUS.md "Account-4 unfinished-work report (5 Oct 2026)"; no SESSION-SWEEP-account-4 row).
VERIFY-BACKLOG.tsv has no row in s-z. Off limits: Birago, Armstrong, Debosnys; bne20211-ferdinand-1478 and destaing-gerard-1779 (account-4
standing session); anything in a private repository (handed to the standing session, never run here).
Manteuffel (sachsstaatsarchiv-manteuffel-1712): folder initial s, but LANE-RUN8-account-2's 03:12 ROOM claim names "manteuffel 0527/0530";
not briefed here until that lane confirms it is not running it (send_message 03:4x).
Every worker: one job, then stop. Each job first checks its named step is still undone (NEXT-STEPS.tsv lags the folders): if a dated NOTES.md
section already ran it, take the folder's own Verdict "cheapest next" instead if it fits this job's cap and box and is not a machine
transcription pass the TRANSCRIPTION.md / CLAUDE.md Usage 6 sorter rule hands to the owner; otherwise stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE LANE-RUN8-account-4".
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
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE LANE-RUN8-account-4",
  then a five-line final report.

## Wave 1 (spawned 03:4x UTC 6 Oct). Intake gate output (03:40 UTC) pasted per job.

### R8-THURV -- thurloe-printed, verifier propagation of R7-THURP10 (Opus; cap 3, box 50 min; no vision)
Intake gate: `thurloe-printed: partial (line 2) -- edition/page or full-text-search citation found within 6 lines`.
You are a VERIFIER, a session separate from the solver (R7-THURP10, account 2). RUN7 named step: R7-THURP10 (6 Oct 01:18-01:2x, NOTES.md
section "R7-THURP10 -- P10 p.620 L10's 14 unglossed groups aligned to Powell 1937", PREREG-R7-THURP10.md commit 06f758dc) changed grades on
P10 L10 (14 groups C12 M2; code 67 s/o conflict logged) after AUDIT.md was written. Rule 10 / CLAUDE.md verifier step 4: (1) re-run the
alignment script and the folder's decode --check yourself and confirm the counts; check the Powell 1937 citation (page) against what is on
disk; (2) carry the revision into AUDIT.md as "## Revision after AUDIT (R8-THURV, 6 Oct 2026; rule 10 propagation)" (class N0 unchanged
unless your check finds otherwise -- say why), recount P10's per-token grades and depth (rule 4a; `tools/depth_check.py`), update
status.json depth fields only if the numbers moved, and update any SECOND-OPINIONS-QUEUE.tsv row filed for P10 (grep it); (3) log the
code-67 conflict per rule 4 in HYPOTHESES.md if R7-THURP10 did not. Do not decode anything new. Commit, push, ROOM done.

### R8-WVO1111 -- wvo-hessen-1564, native-resolution read of WVO 1111 (Wilhelm's reply to 1109) for cribs (Opus; cap 5, box 70 min;
### 2 Sonnet passes + 1 reconciliation)
Intake gate: `wvo-hessen-1564: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN7 named step (R7-WVOH, NOTES.md "Hessen -> Oranje reply search"): 1111 (Kassel, 14 Oct 1564, "Antwoord op nr. 1109") was opened at 80 dpi
only; body unread. Fetch `raw/01111.pdf` once (if not on disk; Huygens WVO, >= 2 s, descriptive UA), render pp.1-2 at 300 dpi, cut line crops
with tools/iiif_lines.py --image (paste command), two blind Sonnet passes on crops (one page per call), reconcile (one unit). Write the
German transcription (grade per line: clear / uncertain) to `wvo1111_transcription.md`, then list every name, place, number and news item
that could be a crib against the 1109 enclosure (f.23) -- do NOT run a crib attack; name the attack and its control as the next step, costed.
Also: Demandt II nr. 292 (pp.109-110) -- one IA/Google Books (country=US, key) search for a scan; record found/not found.

### R8-WHIT -- whitworth-1707, the three S lookups that resolve the intake gate's unread edition (Sonnet; cap 2.5, box 45 min)
Intake gate: `whitworth-1707: open (line 3) names an edition not read ('unread' within 6 lines) -- CLAUDE.md's Pipeline intake gate says
this must read `blocked` instead`. This is a lookup job, not deep work. Run the NOTES.md tail's three S steps: (1) tools/htrc_ef_headwords.py
for 'Whitworth'/'Harley'/'Boyle' against Hartley 2002 and Rothstein 1986 (HathiTrust bibliographic API -> EF API; if neither book has an htid,
say so); (2) re-grep HMC Portland vols 3-6 (on disk if fetched; else IA djvu text) for 'Boyle', 'Moscow', 'Whitworth' near 1707-08 and the
SP 91/5/108 date (30 July/10 Aug 1707); (3) skip the DECODE re-search unless steps 1-2 finish under half the cap (one browser login only,
tools/decode_browser_login.js; scrub the account name). Then fix the status line so the intake gate passes honestly: if an edition is still
unread, status `blocked` with the unread edition named; if all are read, say which pages. Run intake_gate_check.py and paste its output.

### R8-SPLOOK -- three s-z `parallel` lookups that depend on nobody (Sonnet; cap 2.5, box 45 min)
Intake gates: `sp53-22-f52: open (line 1) -- ... found within 6 lines`; `sp81-roe-1638: open (line 1) -- ... found within 6 lines`;
`wallis-emus203-undeciphered: blocked (line 1) -- already terminal, nothing to gate`.
(a) sp53-22-f52: re-read Tomokiyo's live `unsolved.htm` and `mary.htm` entries for f.52 and diff against the 24 Sept snapshots in sources/
(zero edits to sources/; save the live copy under the folder), check for an image reference (092.jpg/093.jpg). (b) sp81-roe-1638: fetch
SP 81/44/88's full TNA Discovery record detail (API; note field) to see whether its "decipher" names the cipher. (c) wallis-emus203-
undeciphered: grep Thurloe vols 2-5 djvu text (`collectionofstat02thur`..`05thur`, IA, once each) for "Brasset", "Buckingham", "Townesend"
and the Scotland 1651 window. Each result goes into the folder's NOTES.md as a dated section, and the `## While waiting` / next-step line
is ticked. Search results only.

### R8-NICH2 -- sp77-nicholas-1659, Cal. Clar. iv pp.310-316 (Sonnet; cap 2, box 40 min)
Intake gate: `sp77-nicholas-1659: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
RUN7 named step (R7-NICH, account 2): read Calendar of the Clarendon State Papers vol. iv pp.310-316 (IA djvu text) for Bennet's Aug 1659
letters and any report from St Sebastian / Sir L.R. that would identify the cipher letter SP 77/32/289's writer or content. Record the
entries read (page, date, writer, one-line summary) and whether any names the cipher or quotes the letter.

### R8-UNTB -- untersberg-code, symA same-scribe concordance (Opus; cap 5, box 75 min; per-leaf units)
Intake gate: `untersberg-code: open (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Folder's named next step (NOTES.md "Next step for symA (one line, not run)"): the same-scribe concordance across the IIIF leaves on disk, with
every crossed-descender p and every symA-like sign, to settle F4 (crossbar or curl). Unit = one leaf: crop candidate signs with a script
(locate from existing transcriptions/coordinates where possible; tools/iiif_lines.py --image), one vision call per leaf on crops only
(~1.5 each). Plan at most 6 leaves (choose the ones with most crossed-descender p's, listed with counts first), stop before a leaf that would
cross 80% of cap or box. Pre-register the F4 decision rule before viewing (PREREG file, pushed). Report the tally and whether F4 is settled.

Wave 1 sessions (03:42 UTC): R8-THURV session_01GgJJf1MigeMBNFeBRkxYGr (Opus, cap 3); R8-WVO1111 session_01QFm9LTr4x56CMCu7H6jNhv (Opus, cap 5);
R8-WHIT session_01JeUgzgaQmCos6MDLrCVXyL (Sonnet, cap 2.5); R8-SPLOOK session_01LYh1suS99H4vCAR4Von4Ej (Sonnet, cap 2.5); R8-NICH2
session_01SENqzw9fekTByY5gMRHBRR (Sonnet, cap 2); R8-UNTB session_01W3wKtZZXqPj8GC4Z9btLAL (Opus, cap 5). Caps 20.0.

## Wave 2 (written 03:4x UTC 6 Oct, spawned as wave-1 slots free). Intake gate output (03:43 UTC) pasted per job.

### R8-ZESCH -- zeschau-seebach-1841, crib test on R5008 (Opus; cap 5, box 75 min; no vision)
Intake gate: `zeschau-seebach-1841: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder's "While waiting" / Verdict cheapest next: first check Bourdeau's stated next step for this item (dbourdeau/cyphersolver, fresh shallow
clone, grep only; GAPS185 duplicate-effort risk) and stop if he has run it. Then rerun crib_test.py on R5008 (German, 260 digits): re-check
the test's power at this N on a matched synthetic control FIRST (same N, symbol count, design per HYPOTHESES.md); only if the control reads
above its pre-registered gate, run the target; then, budget permitting, the crib-anchored key search on R5008's sentence frame with its own
control first. Note rule 3's third-attempt clause: GAPS202's 4-gram syllabary annealer is retired for the key rebuild (failed control
twice); this job is a different instrument (crib test), so it is allowed -- do not re-run the annealer. Both numbers into HYPOTHESES.md.

### R8-YOG3 -- yogtze-1984, spec test 3: 720-anagram enumeration (Opus; cap 2.5, box 40 min)
Intake gate: `yogtze-1984: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
specs/yogtze-1984.json test 3, last untried in the lexical family: enumerate the orderings of the six signs (with the folder's look-alike
reading set) against German and English word lists (tools/data corpora or a public list fetched once), pre-register the scoring and a
shuffled-letter control that can differ (random 6-letter draws from the same letter frequency), report target hits vs control rate.
Write cheap_test result into the spec and NOTES.md. If non-discriminating, the lexical family is logged exhausted; say so.

### R8-TAUR -- taurello-roma-1527, Sanuto vol. 46 mapping + vol. XLII Taurello passage (Sonnet; cap 2, box 40 min)
Intake gate: `taurello-roma-1527: blocked (line 3) -- already terminal, nothing to gate`.
"While waiting" action: map Sanuto vol. 46's archive.org identifier (scan 22 or 01 heads) and read vol. XLII's Taurello passage (id 05,
line 41313 of its djvu) to see whether it ties him to Pietro Antonio. Keep be-api requests to a few dozen (the last pass used about 400).
If vol. 46 is mapped, full-text search it for Taurello/Torello/Vetralla with a positive-control term. Search results only.

### R8-RABY -- sp90-raby-1704, Preuss 1897 (Sonnet; cap 2, box 40 min)
Intake gate: `sp90-raby-1704: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
The folder's last section closes Riezler; "Preuss 1897 is still unread": locate Preuß, *Die preußische Mediation zwischen Bayern u.
Österreich 1704* (1897) on IA / Google Books (keyed, country=US) / HathiTrust EF; if a full text is reachable, read pp.20-30 and p.61 for
Raby, Reichard/Reichart, Berlepsch and any mention of intercepted or ciphered letters; record found/not found and the identifiers.

### R8-SIENA7 -- siena-concistoro-2308 no. 7, native crop of the cipher block glosses (Opus; cap 3, box 50 min)
Intake gate: `siena-concistoro-2308: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder's named step for piece 7: crop the cipher block at native size (images/manifest.json; one DECODE browser login only if the image is
not on disk, tools/decode_browser_login.js, scrub the account name; test full-size per record) to read the faint glosses Bourdeau used (nine
values) and look for more. Crop step pasted; one vision pass on crops, then a second blind pass if any gloss value is new; reconcile.
Grade every gloss value (C if a period gloss, M if uncertain). No key rebuild in this job.

Wave 1 closed 04:0x UTC: THURV 1.43, WVO1111 3.81, WHIT 1.21, SPLOOK 1.23, NICH2 0.85, UNTB 2.83 = 11.36 (all D).
Wave 2 sessions (04:02 UTC): R8-ZESCH session_01YMesMZvJYF4uVjuKGH9Z2P (Opus, cap 5); R8-YOG3 session_017To169azKsJGb28EHb6azE (Opus, cap 2.5);
R8-TAUR session_018VGEHgXyA7wrha6pfRK4xz (Sonnet, cap 2); R8-RABY session_018zvrxKT6onjgbBbtFRPUaA (Sonnet, cap 2); R8-SIENA7
session_01Y1WNnXGknvYihADmNofDuG (Opus, cap 3). Caps 14.5.

Wave 2 closed 04:1x UTC: ZESCH 1.37, YOG3 1.38, TAUR 0.79, RABY 0.63, SIENA7 2.56 = 6.73 (all D). Workers so far 18.09.

## Wave 3 (written 04:17 UTC 6 Oct). Intake gate output (04:16 UTC) pasted per job.
Manteuffel: no answer from LANE-RUN8-account-2 in 35 min and no manteuffel worker in its waves 1-3 (ROOM to 04:16); taken here, ROOM line 04:1x.

### R8-MANT -- sachsstaatsarchiv-manteuffel-1712, 0527 run-7 zoom, then frame 0530 (Opus; cap 7, box 90 min; 1 zoom + 2 Sonnet passes + 1 reconciliation)
Intake gate: `sachsstaatsarchiv-manteuffel-1712: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Verdict cheapest next (NOTES.md line ~1106): (1) re-read 0527 run 7 on the image -- is the code over "Ilgen" 898 or 98? One native-resolution
zoom crop (paste command), read by you plus one blind Sonnet read; record both. If 98, re-run the folder's registered pooled gate
(pooled_mantp / pooled_gate, rule as already pre-registered) and apply the per-unit rule for 898 (M or C). (2) Then, only if under 50% of cap,
transcribe frame 0530 (ff.425v-426, same letter as 0529): folio check first, line crops (paste), 2 blind passes one page per call +
reconciliation, per-leaf gate and pooled gate re-run (rule 3: per-unit gate before anything enters key.tsv). decode --check exit 0 before push;
a reading change after AUDIT.md (N4 AUDIT2-MANT) -> flag a verifier in ROOM. Update Remaining gaps / Escalation; gaps_check.py passes.

### R8-THUR25 -- thurloe-printed P25-P28, page images to replace OCR-line pairs (Opus; cap 5, box 75 min; per-page units)
Intake gate: `thurloe-printed: partial (line 2) -- edition/page or full-text-search citation found within 6 lines`.
NOTES.md escalation S item (section 23, not run): fetch page images for P25-P28 (Manning/Lockhart/Burton/Johnson letters in Birch's Thurloe,
IA) and re-pair cipher groups with printed decipherments from the image rather than OCR lines. Unit = one printed page: IA page image once
(manifest), crops with tools/iiif_lines.py --image (paste), one vision pass per page on crops. List pages first with counts; stop before a
page that would cross 80% of cap/box. Report C-rate before/after per letter; any grade change after AUDIT.md -> say so in NOTES.md and flag
a verifier in ROOM (do not edit AUDIT.md yourself). If budget allows, the third Johnson letter search (P27/P28 sub-key mismatch) in the
already-fetched Birch OCR text.

### R8-SIENA19 -- siena-concistoro-2308 no. 19 vs the no. 13/16 alignment (Opus; cap 3, box 50 min)
Intake gate: `siena-concistoro-2308: open (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Folder's named step for piece 19: compare its run signs with the no. 13/16 alignment (Bourdeau's) as a known-key fit. Pre-register the fit
statistic and its controls BEFORE scoring; check (rule 3) that each control can vary on that statistic -- a value-shuffled key can; an
order-shuffled text cannot change a per-token coverage figure, so use it only if the statistic depends on order (e.g. word/bigram fit).
Disk plus at most one crop. Both numbers into HYPOTHESES.md. No key rebuild.

### R8-SPS1 -- three s-z `parallel` lookups (Sonnet; cap 2.5, box 45 min)
Intake gates: sp36-ball-1745, sp8-ehrenstein-1689, vanspaen-vandergoes-1808 all `open (line 1) -- ... found within 6 lines`.
(a) sp36-ball-1745: TNA Discovery API search of SP 106 (Deciphering Branch) for Nov 1745 items (Marischal, Dunkirk, 6000), record hits.
(b) sp8-ehrenstein-1689: read the remaining 29 rows of the Arcinsys `Bernstorff` 1688-1690 list (pages 2-3) and log any Ehrenstein/cipher
item. (c) vanspaen-vandergoes-1808: grep the public EAD of the NA Kabinet des Konings (1806-1810) for code/sleutel/cijfer/chiffre and Van
Spaen/Van der Goes; record inventory numbers. Dated NOTES.md section per folder, tick the While-waiting line. Search results only.

### R8-SPS2 -- three more s-z `parallel` lookups (Sonnet; cap 2.5, box 45 min)
Intake gates: `sp87-brunswick-1759: open (line 1) ...`; `salvago-caraffa-1691: blocked (line 3) -- already terminal`;
`sp90-raby-whitworth-1705: open (line 1) ...`.
(a) sp87-brunswick-1759: Westphalen 1871 (Google Books CUoSqn-TycQC, full view) at the "composition secrète" hit -- Books API only
(keyed, country=US); books.google.com page view is blocked from the cloud (host table), so if the API gives no page text, say so and leave
the LOCAL-QUEUE row as is. (b) salvago-caraffa-1691: memoriedigitaliliguri.it full-text search of Atti della Società Ligure di Storia
Patria for "Caraffa" 1691 and "Coysis/Coisis/Coissy". (c) sp90-raby-whitworth-1705: BL searcharchives JSON record for Add MS 31128-31152
(1705 volume) for a draft of 1 Aug 1705, and IA full-text search of HMC Portland vols 4 and 8 for "Raby" 1705. Search results only.
