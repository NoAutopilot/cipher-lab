# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261008-1909) -- 8 Oct 2026 19:3x UTC, lane orchestrator session_01HZSAviBovfWXJQzF9mwEg8

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 19:12 UTC 8 Oct - 05:12 UTC 9 Oct. Second incarnation:
started from STATUS.md "LANE FAMILY handoff" (DEFAULT-account-2-20261008-1613). Gate 0a clear (SESSION-SWEEP-account-2 done 5 Oct per
that handoff). Exclusions: eckert-* (LANE LEDGER), Gallica fetches, Birago/Armstrong/Debosnys, every folder with a ROOM claim < 6 h and no
done line, the account-4 LANE DEPTH folders of 18:4x (espagnol142-mercy, jan-van-nassau 5551, huntington-blathwayt).
Register rows re-checked (prior-work check 1, orchestrator, 19:2x): handoff next 1 (Rusdorff NAD) and 2 (WVO 11106 Dutch) live; next 3
(Manteuffel 694/08) lower value after N2; next 4-6 person/sorter/unlocated. NEXT-STEPS "oldenbarnevelt-brederode: read the 1598 slip
and fit no.92" is STALE as worded: R10-OBRED98 (6 Oct) already excluded that key from no.92 by design; its live part is the Van Aerssen
1598-1609 glossed pool (inv. 2016-2025), taken here as a pool (supply c). pro3055-clinton p.123 re-gate skipped (all 20 items
text-known; known-text spend only).

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE FAMILY (account 2)". If --start fails to push
  from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Prior work (`.claude/briefs/prior-work-step.md`): run `python3 tools/prior_work.py <slug> --item-spec '...' --step-type <type> --fetch` first and paste its output and exit code (the orchestrator's offline run is pasted under each job; exit 4 = the LOOK/UNCHECKED rows it lists are owed by you, then `--record` them); then run checks 1-4 by hand where v1 does not reach and paste one line per check (route, query, result) into your
  NOTES.md section BEFORE the first priced step; check 5 after any decode. A check that did not run is "unchecked". If check 1 shows the
  step already done, write one ROOM line saying so and stop.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host. Prefer files already on disk. No Gallica.
- Rule 3 (matched control first; a control that cannot differ from the target on the statistic is a non-test), rule 4 grading, rule 7
  (`--check` scripts). Pre-register any new gate in a PREREG-<JOB>.md pushed before the score is computed.
- Rebase before writing shared files; keep both facts on conflict. Commit only your own paths. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the owner; never
  print credentials. Never call AskUserQuestion. Solver jobs: report what was found and where it was not found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. Opus session floor ~1.5.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR ...`); line or strip crops only, never a full
  page image to a subagent; one page (or half page) per subagent call; ~1.5 per vision call, reconciliation one more unit.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE FAMILY (account 2)",
  then a five-line final report.

- Shared hosts in this wave: post `host take` / `host release` ROOM lines (e.g. "NA take", "huygens take", "IA take") around each batch of
  requests to service.archief.nl / www.nationaalarchief.nl ("NA"), resources.huygens.knaw.nl ("huygens") and archive.org ("IA"); if
  another worker of this lane holds the host (a take with no release in the last 30 min), work from disk meanwhile and wait.

## Wave 1 (19:3x UTC 8 Oct)
Intake gate 19:2x UTC (tools/intake_gate_check.py):
`wvo-11106-bergh-1572: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0);
`na-oldenbarnevelt-2442-1605: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0);
`craven-rupert-1648: open (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0);
`decode-4333-rusdorff-oxenstierna-1628: blocked (line 1) -- already terminal` (so RUS-CS below is a check-solved job, not deep work).
prior_work.py (offline, 19:2x): every item exit 4 (LOOK 2-leaf + UNCHECKED solver/tomokiyo/editions rows owed by the job; no DONE, no
KNOWN). Each worker re-runs it with --fetch and answers its owed rows.

### RUS-CS (Sonnet, cap 3, box 75 min): decode-4333-rusdorff-oxenstierna-1628, check-solved by the cloud routes not yet tried
Follow `.claude/briefs/check-solved.md` (with its Premise check) for the Rusdorff -> Oxenstierna letters on DECODE R4333-R4337 (dated on the
leaves 12 Mar 1624, 10 Apr 1624, 10 Nov 1624, 15/25 Feb 1625, 26 Feb 1625 o.s.; NOTES.md "Leaf check" table). The blocker is the
edition check: Cuhn's *Mémoires et négociations secrètes de Rusdorf* (Leipzig 1789, 2 vols) and *Consilia et negotia politica* (1725)
were not opened as text (FAM-CS4333; LOCAL-QUEUE L67 queued for the owner's runner). Routes not yet tried from the cloud: (1) HathiTrust
Bibliographic API for both titles (record/OCLC via Open Library search, CLAUDE.md "HathiTrust without a browser"), then HTRC Extracted
Features per-page token counts (`tools/htrc_ef_headwords.py` or a short script; data.htrc.illinois.edu, >= 1.6 s) for pages carrying
"Oxenstiern*" with "1624"/"1625", "Februarii"/"Martii"/"Aprilis"/"Novembris" -- a page with both is a candidate printed letter of that
date; positive control: a letter you can show is in the edition (e.g. any page that EF and the Google Books API snippet agree on);
(2) Google Books API (`country=US`, key) `q=` searches with the volume ids for snippets on those dates; (3) Riksarkivet NAD
(sok.riksarkivet.se) note for "E 701 Ser. B." / Oxenstiernska samlingen, Rusdorff letters (one or two requests; report reachability);
(4) AOSB ser. I Bd 3 footnote name codes in the 7xx range (746 Regi Daniae etc.) from the IA OCR already used by riksarkivet-r4282-1628
(its NOTES "IA-DESK-ALT" section; disk first), tabled against the 7xx codes seen in R4336/R4337 (NOTES table) -- a table, no decoding.
Write the verdict line(s) at the top of NOTES.md per check-solved.md: if the edition check is now done (pages read or full-text-searched,
named), say open/found-solved accordingly; if EF only shows that letters to Oxenstierna of those dates are printed but no text could be
read, say so and keep `blocked` naming L67. Update Remaining gaps/Escalation and pass gaps_check. No transcription, no decoding.

### NL16-11106 (Opus, cap 5, box 100 min): wvo-11106-bergh-1572, an era-matched 16th-c. Dutch corpus and the Dutch homophonic run
Next 2 of the handoff. (a) Build `tools/data/nl16/` (README.md with sources, dates, licence, sizes): 1560s-1580s Dutch prose, letters and
pamphlets preferred (e.g. DBNL plain-text downloads of Marnix, Coornhert, Van Vloten's Nederlandsche geschiedzangen prose notes, Bor's
*Oorsprongk* or Groen's Dutch letters; IA djvu text only with an "IA take"), normalised the way `tools/judge_plaintext.py`'s other
corpora are (read how `LANG_CORPORA` is built, add `nl16` the same way, with an offline test). At least 5 source files; report the
leave-one-file-out false-negative rate PER FOLD with the blended rate (CLAUDE.md rule 3, es17c/EN-FOLDS lessons). (b) Then
`tools/family_run.py` on the folder's spec, `--family homophonic`, corpus nl16, matched control at the target's measured noise (0.10;
the control must bracket it, rule 3 SALV-DIAG lesson), the same K and N as FAM-11106L's fr16/de1600/la17 rows, 6 seeds; both numbers to
HYPOTHESES.md. Control below gate = non-test, say so. (c) Only if under 60% of cap: the six WVO Opmerkingen of Bergh's letters 5628-5631,
9663, 9666 (resources.huygens.knaw.nl/wvo/app/brief?nr=N, "huygens take", 6 requests >= 2 s) for a cipher or key mention. NOTES section,
gaps/escalation, gaps_check. A PASS (target above its gate) goes to the lane for a separate verifier; do not classify.

### OLD-S10 (Opus, cap 6, box 100 min): na-oldenbarnevelt-2442-1605, step (o1): scan 10's cipher block under the fixed key
NOTES.md "Verdict: open ... Next steps: (o1) scan 10's cipher block (ff.63v/64r right page, ~25 lines): masked crops, two blind passes +
one reconciliation, fixed key, ~$4.5". Read AUDIT.md "AUDIT 3" (OLD-SIBS-V: leaves 4/5/7 N3 D1, key ours) and the latest sections on how
the key and the transcription convention work (key file, decode script). Prior-work check 2: scan 10's own left page and scans 9/11 for an
interlinear decipherment or clear copy (scan 11 is f.64v; NOTES l.1346) before any pass. Image: from disk if present; else one fetch
(NA host, "NA take"/"NA release", >= 1.9 s; release as soon as the image is on disk -- AERS-POOL waits on it). Units: `tools/iiif_lines.py
--image ... --mask-neighbours` crops (paste the command), 2 blind Sonnet passes (~1.5 each) + 1 reconciliation, decode with the fixed key
and `--check`, grade per token (rule 4); matched control: the same decode under shuffled/permuted keys (the folder's existing control
design), both numbers. Report the S share and the longest S stretch against the folder's AD figure (depth bar,
.claude/briefs/runs/2026-10-08-acct3-depth-bar.md) -- report the numbers, the verifier sets depth. Run check 5 (`tools/prior_work.py
... --reading <file> --network`) after decode. Do not classify novelty; do not touch AUDIT.md. Also note in one line whether the NOTES.md
tail is duplicated (the "Verdict: open ... While waiting" block appears twice) -- do not rewrite it.

### AERS-POOL (Opus, cap 4.5, box 100 min): Van Aerssen 1598-1609 to Oldenbarnevelt, NA 3.01.14 inv. 2016-2025, pool inventory + check-solved
From oldenbarnevelt-brederode-1605 NOTES.md "The 10 Aug 1598 sleutel ... (R10-OBRED98)": inv. 2016 carries partly deciphered originals
(scans 31/32, 43, 64) and per-letter gloss sheets (scans 7, 16, 31 slip); inv. 2017-2025 (1599-1609) are catalogued "Gedeeltelijk
gedecodeerd". Job: (1) wait for OLD-S10's "NA release" if it holds the host; METS for inv. 2017-2025 (one request each; the inv. 2016 list
is on disk, na_301_14_2016_scans.tsv), 400 px contact sheets of every third scan by your own eye, 1400 px only for candidates; <= 150 NA
requests total, >= 1.9 s. (2) Table every cipher-bearing scan: inv., scan, date on thumbnail, design (syllabary marked 1-2 digit numbers /
phrase letters / other), glossed interlinear (all / part / none), gloss sheet present, rough sign count -> `ciphers/vanaerssen-1598-1609/
pool.tsv` (new folder; NOTES.md first line `open` only if (3) supports it, else `blocked` naming what was not read). (3) Check-solved per
`.claude/briefs/check-solved.md` for the pool: Veenendaal's *Bescheiden ... Oldenbarnevelt* (Huygens retroboeken, "huygens take"; its own
full-text search for "Aerssen" and "cijfer"), *Lettres et négociations* / Van Deventer's *Gedenkstukken* (IA), the two solver repos,
DECODE listing (login-free, `tools/decode_list.py`), Cipherbrain/Cryptiana. (4) Name the best two unglossed (or partly glossed) letters
with sign counts and the key source in hand (the glossed letters of the same years), and the next read with a per-unit cost. No
transcription, no decoding. Correct oldenbarnevelt-brederode-1605's loose-ends gap line in place (the slip was excluded for no.92 by design
on 6 Oct; the live part is this pool) and re-run gaps_check on it.

### CRAV-49 (Opus, cap 4, box 90 min): craven-rupert-1648, the 1649 siblings DECODE R8451-R8454
Next step of D2-CRAV (NOTES.md "Remaining gaps (D2-CRAV)"): one DECODE browser login (`NODE_PATH=$(npm root -g) node
tools/decode_browser_login.js ... --guess-fullsize`, the D2-CRAV route), fetch R8451-R8454 (ff.185-195) full-size images, look for
cipher/decipherment pairs (interlinear glosses), table the pairs, and run the SAME pre-registered A1 coverage test (test2/, amendment A1)
on each sibling table against the target's 40 legible groups, with its key-true and random-code controls; if a table is not EXCLUDED, a
decode of the target under it with --check and a shuffled-key control. Prior-work check 2: the leaves either side of each record for a
clear copy. Scrub the account name from any saved page. One login, <= 40 de-crypt.org requests >= 2 s. Report both numbers per table.
