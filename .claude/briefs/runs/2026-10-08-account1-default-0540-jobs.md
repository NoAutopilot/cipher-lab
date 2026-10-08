# LANE DEFAULT-account-1-20261008-0540 jobs (account 1) -- 8 Oct 2026 05:4x UTC, lane orchestrator session_01RR9DYMbpvFjP1tVfVsp2Ho

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 05:40-15:40 UTC. Gate 0a: SESSION-SWEEP-account-1 row still `claimed` since
5 Oct 22:40 but its TSV is on disk; proceeding (as RUN8-12 and the 7 Oct DEFAULT lanes did), 0 exclusions from it.
Backlog a: VERIFY-BACKLOG regenerated 05:42 UTC: eckert-1864 rows held by LANE ST-LEDGER-2 / the account-3 orchestrator (AUD2-LS-*);
Birago off limits; nla-heinrich and colbert26 are N0 (Outreach gate 2 applies above N1 only); the rest `counted` rows with priority none.
No verifier job taken. Backlog b: `tools/next_steps.py --hot-only` (exit 0) runnable rows and blocked rows' parallel actions, filtered
against ROOM claims < 6 h and 8 Oct live briefs. Excluded: Birago, Armstrong, Debosnys; eckert-1864, na-oldenbarnevelt-2442-1605,
es132, fr16104, fr2980, fr3416, hellen, manteuffel, decode-2754, sforza-*, fr3613/3622/3983/3984/3985-3990 (BNF-FOCUS), ceppo.
Every worker: one job, then stop. First check the named step is still undone (a later ROOM done line or NOTES section may have run it);
if it was, write one ROOM line saying so and stop. A LOOSE-ENDS worker (account 2, box to 06:42 UTC) may be writing Escalation lines in
many NOTES.md files: fetch and rebase immediately before every NOTES.md edit and keep both facts.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-1-20261008-0540". If --start
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
  DEFAULT-account-1-20261008-0540", then a five-line final report.

## Wave 1 (spawned 05:5x UTC 8 Oct)
Intake gate 05:4x UTC (tools/intake_gate_check.py, each exit 0):
`decode-1411-hhsta-vienna-1600: open (line 3) -- edition/page or full-text-search citation found within 6 lines`;
`fr16045-pisany-rome-1585: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`fr5160-letellier-1653: open (line 3) -- edition/page or full-text-search citation found within 6 lines`;
`fr4715-vieuville-pool: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`pro3055-clinton-1779: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.

### D1A-D1411 -- decode-1411-hhsta-vienna-1600 p.2/p.5 copy differences (solver, Opus; cap 4, box 75 min)
Escalation line (NOTES.md l.788) and gap l.776: settle the 13 differing numbers (12 substitutions; look-alikes 53/93, 19/29, 7/4, 81/61,
95/45, 46/96) between p5L_L11_b-L31_a and def1411's p2Lb_L01-p2R_L02 (NOTES.md l.705-711) by a side-by-side per-number comparison of the
two copies' images: cut per-number tiles of each differing pair from the existing native crops (images/, def1411/, d1411p5/) into one
montage per pair (both copies side by side, plus 2-3 undisputed same-hand exemplars of each candidate numeral as references). Units: one
blind Opus subagent call on all montages (shapes only, no key, no context) + your own reconciliation = 2 units. Pre-register in
PREREG-D1A-D1411.md before reading: what counts as settled (both copies show one numeral on the tile, or one copy's reading is legible and
the other's is the look-alike) and the exemplar control (the reader must name the exemplars correctly, >= 80%, else the comparison is a
non-test). Then re-score p.2+p.5 on the settled copy text as DESCRIPTIVE only (the AM-D1411V ruling: in-sample for T21r, no S grades).
Note the p.4 4/5 look-alike machine re-read is retired; do not reopen it. Update NOTES.md, HYPOTHESES.md, gaps sections.

### D1A-PIS -- fr16045-pisany-rome-1585 key86 T40 witness from the letters (solver, Opus; cap 5, box 80 min)
Verdict (NOTES.md l.992): "key86 T40 witness from the letters themselves ... ~$1". Unit 1: list every T40 token on the leaves already
paired with their Colbert 16 pt II clear copies (f.244r, f.244v/f.245r, f.247r, f.275r, f.275v, f.301v, f.302v) from the folder's own
aligned files; for each, read what the clear copy carries at that position by script (the alignments on disk), and register before scoring
(PREREG-D1A-PIS.md) the gate for assigning T40 a value: one value at >= 70% of aligned T40 tokens with N >= 5, beside a null of the same
count drawn from random non-T40 positions (its top-value share must stay below the gate) -- a control that can differ on the statistic.
Note the two blind crop-compare instruments are retired for T40 (D07-PIST40, D07-PISSD); this is the alignment instrument, not a crop
compare. Unit 2, only if unit 1 finished under 50% of cap and box: the f.275v period gloss as a second witness (gap at NOTES.md: "read the
gloss at native resolution, normalise to one convention with the copy (rule 3 PX-BRODEC), score agreement, ~$2"), one blind subagent read
of the gloss line crops + reconciliation. key.tsv changes only through a passed gate; run the decode --check. Update NOTES/HYPOTHESES/gaps.

### D1A-CAN -- fr5160-letellier-1653 canvas refetch + fr4715-vieuville-pool f.67v (solver, Opus; cap 4, box 70 min)
Two small fetch-and-look units, each its own folder's own step. Unit 1 (fr5160, Verdict "refetch canvas 45 (and any of 55/58/74 still
missing) once each and look for cipher groups; add a cipher leaf to trial_1653, ~$0.5"): Gallica IIIF, one request per canvas, >= 1.5 s
apart; look at a downscaled view first, cut line crops (tools/iiif_lines.py) only if cipher groups are present. If a cipher leaf is found,
add it to trial_1653 as the folder's notes describe and stop there (the f.68 clear-pages step is a separate job; name it in the Verdict).
Unit 2 (fr4715-vieuville-pool, Verdict "fetch the f.67v canvas once and look for a continuation or cipher, ~$0.3"): locate f.67v with
tools/gallica_folio.py on the fr.4715 ark (read NOTES.md for it), fetch once, look, record what is there (clear continuation, cipher, blank)
with the canvas and URL. If cipher: crops only, no reading. Update both folders' NOTES.md, gaps sections and Verdicts; gaps_check both.

### D1A-CLIN -- pro3055-clinton-1779 f.381 period decipherment line (solver, Opus; cap 3, box 60 min)
Verdict (NOTES.md, R15-CLINGAP): "read the f.381 period decipherment line (B.147 p.381) for 'and pains', ~$1.5". The text is known (N0);
this job corrects a record (whether the period decipherment or the 1920 edition drops "and pains" / "up"). Fetch the H-1649 frame for B.147
p.381 once from image-uab.canadiana.ca with the route the folder already used (browser UA + Referer; NOTES.md R15-CLIN407 names the Image
number pattern; check images/ first), crop the one line plus its neighbours, one blind subagent read of the crop (no context given) + your
reconciliation. Record what the period decipherment carries for the "all your Trouble ..." and "give ..." passages, with the frame number.
No status change; update the gap line and Verdict; gaps_check.

## Wave 2 (spawned 05:5x UTC 8 Oct)
Intake gate 05:5x UTC: `na-suriname-map-1781: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`sp77-nicholas-1659: open (line 1) -- edition/page or full-text-search citation found within 6 lines`;
`naf14913-rousseau-venice-1743: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.

### D1A-SUR -- na-suriname-map-1781 [ij] test with a control off ceiling + step-2 tile (solver, Opus; cap 4, box 75 min)
Verdict (NOTES.md l.3067, NZ-SURIJ 7 Oct): "open: an IJ test with a control not at ceiling over more scans (~$2) and a cleanly cut
same-hand step-2 look with [d-loop][s-loop] as one tile (~$1)". Unit 1: pool the image-dotted ij forms from the inv. 373 scans already on
disk (0693, 0702, 0730, 0746, 0758; NZ-SURIJ found 6 on 0746) to n >= 10 if they exist; write PREREG-D1A-SUR.md first with a C1 control
whose p99 at that n sits below the gate (if no available n gets the control off ceiling, stop and log "untestable at this n" -- rule 3
third-attempt clause applies: this is the second IJ attempt, so change the n, not the gate). Unit 2 only if unit 1 finished under 50% of
cap and box: the [d-loop][s-loop] one-tile step-2 look with a known-same control that answers SAME (NZ-SURIJ's was UNSURE). No key row
changes without a passed gate. Update NOTES/HYPOTHESES/gaps.

### D1A-SRCH -- two print searches (search worker, Sonnet; cap 3, box 60 min)
Unit 1 (sp77-nicholas-1659, NOTES.md l.150): grep the IA full text (`_djvu.txt`) of CSPD 1659-60 and Calendar of the Clarendon State
Papers vol. iv -- find the identifiers with advancedsearch first; indexes first, then body -- for royalist aliases/agents at St Sebastian in
Aug 1659 (Holder, Bennet, Peter Wilson's house) and anything that identifies "Sir L.R."; quote each hit with identifier and djvu line.
Unit 2 (naf14913-rousseau-venice-1743, NOTES.md l.226 and l.228): phrase-search f.206r's own quote ("venitiens en faveur de la Reine de
Hongrie" and one or two other exact phrases from slip_f206r.txt) via archive.org be-api fts and the Google Books API (`&country=US`,
`&key=$GOOGLE_BOOKS_KEY`), and full-text search Souchon 1915 (Gallica bpt6k935116v; Gallica SRU or the volume's own search) for the
1743-44 passage. Log every query with hit counts, by host; "no hits" is a search result, never a novelty verdict. Append findings as a dated
section in each NOTES.md and tick the matching lines; gaps_check where the folder is partial. Scripts read, the model judges the hits.
