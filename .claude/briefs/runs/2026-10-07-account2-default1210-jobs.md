# LANE DEFAULT-account-2-20261007-1210 jobs (account 2) -- 7 Oct 2026 12:1x UTC, lane orchestrator session_011LUSjgh3ctGxLUSQvqB2Nj

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 12:11-22:11 UTC 7 Oct. Gate 0a clear (SESSION-SWEEP-account-2 done 5 Oct).
Backlog a: VERIFY-BACKLOG regenerated 12:1x UTC: three eckert-1864 N3 rows (N2-M, N2-R, N2-T) need the second adversarial audit
(CLAUDE.md Outreach gate 2); Birago off limits; nla-heinrich N0 (gate 2 only above N1); the other eckert rows are N1 (no audit 2 needed).
Backlog b: `tools/next_steps.py --hot-only` (exit 0): eckert-1864's named next step is the 74 unread "(No 2)" entries of mssEC 19
(no2-candidates.tsv, ECK64-NO2 done 12:08 UTC). Excluded: XCAL (live, key_crossmatch), Birago, Armstrong, Debosnys, folders claimed < 6 h
without a done line.
Every worker: one job, then stop. First check the named step is still undone (a later ROOM done line or NOTES section may have run it).

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-2-20261007-1210". If --start
  fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host. Google Books API: `&country=US&key=$GOOGLE_BOOKS_KEY`.
- Rule 3/4/7 as CLAUDE.md. eckert-1864: `python3 ciphers/eckert-1864/decode_no2.py --check` exit 0 before any push that touches the No. 2
  files. A reading change after AUDIT.md: say so in NOTES.md and flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md, SECOND-OPINIONS-QUEUE.tsv, JSTOR-QUEUE.tsv); keep
  both facts on conflict. Several sessions of this lane write eckert-1864 at once: commit only your own paths, fetch+rebase right before
  every push, and append your own NOTES/AUDIT section rather than editing another worker's. Run `python3 tools/file_shrink_guard.py <every
  file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the owner; never
  print credentials (test presence with `test -n`). Never call AskUserQuestion. Solver jobs: report what was found and where it was not
  found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half done
  writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR ...`, ECK64-NO2's region/centres form); read
  strip crops, never a full page image; one page per subagent call if you use one. Price ~1.2 per entry read (AM-ECK64K, ECK64-NO2).
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE
  DEFAULT-account-2-20261007-1210", then a five-line final report.

## Wave 1 (spawned 12:2x UTC 7 Oct). Intake gate (12:1x UTC): `eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.

### D12-V2M / D12-V2R / D12-V2T -- eckert-1864 second adversarial audit of one N3 entry each (verifier, Opus; cap 3.5, box 50 min each)
You are a separate session from every solver of the entry and from its first auditor (AM-ECKV for N2-M; the ECK64-NO2 verifier agent
for N2-R and N2-T). Your one entry: D12-V2M = N2-M (p.90, Kimber 11 June 1864, QMG/Burglar to Canby, gauge of the Vicksburg & Shreveport
Rail-road); D12-V2R = N2-R (p.56, Augur to Meade, 26 Apr 1864, 11.30 AM, co-operation from Warrenton); D12-V2T = N2-T (Stanton to Dana,
6 June 1864, two French officers). Follow .claude/briefs/verifier.md and CLAUDE.md "Verifier brief (template)" scoped to that entry, and
CLAUDE.md Outreach gate 2: try to find it in print by every family the first audit did NOT cover (read AUDIT.md's search log for your
entry first and list the gaps), at least: The Papers of Ulysses S. Grant (vol. 10 Jan-May 1864, vol. 11 June-Aug 1864: the first audit of
N2-P/N2-Q found two "not located" entries printed there), the sender's/recipient's own papers (Meigs letter books and Canby for N2-M;
Meade's and Augur's for N2-R; Stanton/Dana for N2-T, incl. Dana's Recollections), every OR ser. I/III volume for the date window +/- 3
days by date and correspondent (not only phrase), the Huntington's own full text across the whole mssEC collection (CONTENTdm
CISOSEARCHALL, CLAUDE.md host table), IA full text, Google Books, HathiTrust EF where useful, the open-index scholarship pass (OpenAlex,
Semantic Scholar, CORE, CrossRef with the keys) and JSTOR-QUEUE.tsv rows in both families (i) and (ii) (CLAUDE.md verifier template 2g;
rows never block). Re-derive the entry with `decode_no2.py --check` (rule 7) and check its tokens on the strip crop (one IIIF image,
regenerable). Write "## AUDIT 2 (second adversarial, D12-V2<x>)" in AUDIT.md for your entry only: families searched/unreachable,
class (keep N3, raise to N4 only per rule 10 if the principal editions, catalogues and project pages are covered, or lower), key `period`,
depth line, safe/unsafe sentence. Update the entry's status.json result row (`audit_status` 'two audits') and PROGRESS.tsv if the entry has
a row (rebase first); if its SECOND-OPINIONS-QUEUE.tsv row quotes a count or class you changed, correct it. Do not decode other entries.

### D12-E1 -- eckert-1864, unread "(No 2)" entries of mssEC 19 pages 4-18 (solver, Opus; cap 12, box 110 min)
Entries (no2-candidates.tsv pointer/page/entry_on_page, unread): 8896/4/1, 8900/8/0, 8900/8/1, 8901/9/0 (long, 112 k2 tokens), 8903/11/0,
8906/14/1, 8907/15/2 (header says "1": check whether it is No. 1 or No. 2 before reading), 8909/17/1, 8910/18/0, 8910/18/1. Order: short
entries first, the long 8901/9/0 last. Method exactly as ECK64-NO2 (NOTES.md "## ECK64-NO2"): 2400 px IIIF image to scratch, strip crops
(command pasted), read with key-no2.md, volunteer transcription (dmGetItemInfo `transc`) as second witness, grade per token H/C/I/M, add
each as the next N2 block in ciphertext-no2.txt / reading-no2.md after the last existing one (N2-U at the time of writing; fetch first:
D12-E2 is adding blocks too -- use the next free letter at your push and rebase, renaming your blocks if needed), `decode_no2.py --check`
exit 0, OR print check per entry by phrase AND by date/correspondent in the OR volume for its date (IA djvu, on disk if cached) and PUSG
vol. 10 where Grant is a party. Price ~1.2 per entry; stop before an entry that would cross 80% of cap. Log key conflicts/clerk forms in
key-no2.md section 8 style, not resolved. Append "## D12-E1" in NOTES.md, update Remaining gaps / Verdict (no2-candidates.tsv status
column: READ D12-E1), gaps_check, and one ROOM flag naming your blocks for a verifier. Report what was found and where it was not found.

### D12-E2 -- eckert-1864, unread "(No 2)" entries of mssEC 19 pages 21-34 (solver, Opus; cap 11, box 110 min)
Entries: 8913/21/1, 8913/21/2, 8914/22/2, 8915/23/2 (Louisville), 8916/24/0, 8916/24/1, 8916/24/2, 8917/25/1, 8926/34/0. Same method,
rules and write-up as D12-E1 (your section "## D12-E2", status READ D12-E2); D12-E1 writes the same files at the same time, so take the
next free block letter at your push and rebase. PUSG vol. 10 where Grant is a party.

### D12-E62H -- eckert-1862, the 7 M-graded Hurlbut-row tokens against another witness (solver, Opus; cap 4.5, box 60 min)
Intake gate: run `python3 tools/intake_gate_check.py eckert-1862` and paste it before work. Folder Verdict (AM-ECK62Q): "the 7 M-graded
Hurlbut-row tokens against another witness, ~$4". Find the seven in overrides.tsv / R12A-ECKV2's section, look for a second witness
(another sent or received copy in mssEC 18-19 or 04-14, the OR print, a later re-use of the same code word in a print-matched entry), and
grade each H/C/S/M with the witness named. No change without a witness; an override change re-runs the folder's decode --check. Update
NOTES.md section, Remaining gaps / Verdict, gaps_check. Report what was found and where it was not found.

Wave 1 sessions (12:16 UTC): D12-V2M session_01PugdoD1Sjk6HZnB5SXjDPi; D12-V2R session_01HwXefTYDLb82sruCuUhEQH; D12-V2T
session_01Lsy7bgiVTbeuQHNrggXhBp; D12-E1 session_01HybNY3c6889sZU8de9LeAE; D12-E2 session_019gxbpr5FVaBnraBBwvT9U5; D12-E62H
session_01LebTAsxigKvN3AuFJccvdn. Caps 38.

Wave 1 results (12:3x UTC): D12-V2M N2-M N3 -> N4 (4.02, D- 1.15x); D12-V2T N2-T N3 -> N4 (3.53); D12-V2R N2-R kept N3 (3.46; the Supplement
to the OR is not full-text searchable from the cloud -- lane leaves the verifier's N3 as written, no raise by the orchestrator);
D12-E2 N2-V..AC 8 entries pp.21-34, all located in print (5 OR, 3 PUSG 10 page not established), H 115 C 11 I 2 (4.82).

## Wave 2 (spawned 12:3x UTC 7 Oct). Intake gate as wave 1 (eckert-1864 partial, citation found). E2 ran ~0.6 per entry.

### D12-E3 -- eckert-1864, unread "(No 2)" entries of mssEC 19 pages 40-54 (solver, Opus; cap 6, box 90 min)
Entries: 8932/40/0, 8935/43/1, 8936/44/0, 8942/50/2, 8944/52/0, 8946/54/2, then 8945/53/0 (long) last. Same method, rules and write-up as
D12-E1 (section "## D12-E3", status READ D12-E3, next free block letter at your push; D12-E1 and D12-E4 write the same files). OR for the date
by phrase and by date/correspondent, PUSG vol. 10 where Grant is a party. If archive.org answers 502, one retry after a pause, then log the
entry's print check as unreachable (not as "not located").

### D12-E4 -- eckert-1864, unread "(No 2)" entries of mssEC 19 pages 56-74 (solver, Opus; cap 6, box 90 min)
Entries: 8948/56/0, 8951/59/2, 8956/64/0, 8961/69/2, 8965/73/0, 8966/74/0, then 8964/72/1 (long) last. Same as D12-E3 (section "## D12-E4",
status READ D12-E4). PUSG vol. 10 (to May) / vol. 11 (June on) where Grant is a party.
Wave 2 sessions (12:34 UTC): D12-E3 session_014UAgDp1xLqVrhj1oS83wcY; D12-E4 session_01P4LyLzaZCVox5oC7XKgXUm. Archived 12:34: D12-V2M, V2R, V2T, E2.

Wave 2 results (12:5x UTC): D12-E1 N2-AD..AK 8 entries pp.4-18 (7.42; 8900/8/0 and 8907/15/2 are Cipher No. 1, not read), 6 in print, 2 not
located (Howell, Augur); D12-E62H eckert-1862 6 Hurlbut M -> C + mssEC 19 9174 x2 C, 9877 stays M (4.95, 1.10x); D12-E3 N2-AL..AR pp.40-55,
all 7 in OR (3.87); D12-E4 N2-AS..AY pp.56-74, 6 OR + 1 PUSG 10 (6.22, 1.04x). Lane spend 43.3 of 60 (workers 38.3, orchestrator 5.0).

## Wave 3 (last; spawned 12:5x UTC 7 Oct)

### D12-VP -- eckert-1864 AUDIT propagation for N2-V..AY (verifier, Opus; cap 5, box 60 min)
You are a separate session from D12-E1..E4 and every earlier eckert-1864 solver. CLAUDE.md "Verifier brief (template)" scoped to the 30
blocks reading-no2.md gained after AUDIT.md: N2-V..AC (D12-E2), N2-AD..AK (D12-E1), N2-AL..AR (D12-E3), N2-AS..AY (D12-E4). Price: the 28
"located in print" entries are a check, not a search -- re-derive all with `decode_no2.py --check`, spot-check one strip crop per worker
(4 IIIF images), confirm each cited print page by a script (IA djvu full text on disk/fetched once per volume; PUSG vol. 10 snippet
entries: establish the page where possible, else say "page not established") and class N1 with one table row each. Spend the rest on the
two not located (D12-E1's Howell and Augur entries): full verifier search per entry (OR by date and correspondent +/- 3 days, PUSG 10,
sender/recipient papers, Huntington whole-collection full text, IA, Google Books, open indexes, JSTOR-QUEUE rows in both families) and an
N-class; for N3+, the SECOND-OPINIONS-QUEUE.tsv row in this session. Depth line per entry (D3/D4 rule 4a). Also record the key-no2.md
section 8 conflicts the solvers logged (Religion/Slumber = Operations; Nuptial = Steele in N2-AQ; N2-AT yawl) as logged, not resolved.
Append "## AUDIT (propagation, D12-VP)" to AUDIT.md; status.json result rows for N3+ entries only (one row per N3+ entry, as earlier
ones; rebase first). Do not decode other entries.

### D12-V62 -- eckert-1862 grade-change check (verifier, Opus; cap 3, box 45 min)
Separate session from D12-E62H. D12-E62H moved 6 Hurlbut-row tokens M -> C (overrides.tsv) and mssEC 19 9174 lehigh+leopard M -> C, citing
OR 33, PUSG 11, OR 49.1 (commit b5a795fe6). Check each C against its cited print page (script, the IA djvu text) and the image crop if
needed; keep, drop to M, or correct; rerun ec18.py --check. D12-E62H also flagged pre-existing staleness: `ec18.py --book 2 --check` stale
since key-no2.md changed (ECK64-NO2 and today's section 8 rows) and `ec18_align.py --check` stale: regenerate both with their own scripts if
the change is only the key-no2 rows, report the diff counts, and say if any committed reading changes. Write "## D12-V62 verifier" in
NOTES.md and, if AUDIT.md quotes the changed counts, an AUDIT propagation section; gaps_check.
Wave 3 sessions (12:52 UTC): D12-VP session_01Q6FAeqaULVdZY4x3K9Huwk; D12-V62 session_01MomWz5Aeez9vHpAnQ7ZRnK. Archived 12:52: D12-E1, E62H, E3, E4.
