# LANE LEDGER worker jobs (account 1, session_01BhFrvFs46QaEbT8aTNPN8V; written 8 Oct 2026 17:5x UTC)

Lane brief .claude/briefs/lane-ledger.md (+ lane-common-blast.md). Continues the "Left, runnable" list of the LANE ST-LEDGER-4 handoff
(STATUS.md). Every ROOM line ends "for LANE LEDGER (account 1)".

Intake gates (pasted 17:4x UTC): `eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` (exit 0);
`eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` (exit 0). Objects 5952, 8472, 6254 are
Eckert Papers ledgers inside the scope of those two check-solved verdicts (QUEUE rank 1, mssEC 1-76); their work lives in sub-folders
of the target folders, and the prior-work step below is the item-level check for each.

Common to every worker:
- Read CLAUDE.md, .claude/briefs/prior-work-step.md (tools/prior_work.py does not exist: run its checklist by hand, civil-war adapter, and
  paste one line per check -- route, query, result -- before the first priced step), the LANE ST-LEDGER-4 handoff in STATUS.md, and
  ciphers/eckert-1864/NOTES.md "## PF4" and "## LS4-R1b" (eckert-1862: its "## LS3-R62" and Remaining gaps).
- `date -u` before any time; ROOM claim with box end time, a halfway line, a done line (`python3 tools/room.py "<role>" '<text>' --push`);
  commit and push every two units; stop before a unit that would cross 80% of cap or box; Rule 10 wording only; never call AskUserQuestion;
  never print credentials; file_shrink_guard on every touched file before the final push; `tools/gaps_check.py <target>` after NOTES.
- **hdl.huntington.org token (lane-ledger.md: one worker at a time on that host).** Before your first request there:
  `git fetch -q origin main && git show origin/main:ROOM.md | grep "LANE LEDGER hdl" | tail -3`. If the newest line is a `take` by
  another worker less than 40 minutes old, with no later `release` from that worker, wait: re-check every 60 s with a background loop
  or Monitor (no foreground sleep), up to 30 min, then say so in ROOM and work offline on what you have. To take:
  `python3 tools/room.py "<role>" 'LANE LEDGER hdl take' --push`; do ALL your hdl/CONTENTdm requests in one block (>= 1.6 s apart,
  CISOSEARCHALL form per CLAUDE.md), then `... 'LANE LEDGER hdl release (N requests)' --push`. Images to scratch, never committed;
  manifest entries only.
- archive.org / be-api >= 1.5 s apart, one at a time; stop a host on 429/403 after one retry; report requests per host.
- Solvers: report what was found and where it was not found; do not classify novelty.

---

## LS5-R1c, LS5-R1d, LS5-R1e (Sonnet 5.5, readers; cap $7.5 each, box 130 min each): the 34 PF4-clean Cipher No. 1 rows left
Rows in PF4's order (prefilter-ls4.tsv group pool-3, minus the 20 read by LS4-R1a/R1b):
- LS5-R1c (12): 9129/1 8907/1 9020/1 9062/1 9072/0 9090/1 9131/1 8898/1 8969/3 8982/2 8992/0 8996/0
- LS5-R1d (11): 9036/0 9043/0 9049/1 9053/2 9055/1 9062/2 9086/1 9088/1 9113/1 9124/1 8967/2
- LS5-R1e (11): 8984/1 9034/1 9124/0 8992/1 9034/0 9044/1 9081/0 9098/1 9120/0 9139/1 9144/0
Method: exactly the wave-3 reader method of .claude/briefs/runs/2026-10-08-acct1-st-ledger4-workers.md ("Readers LS4-R2b and LS4-R1b":
steps 0-4 of wave 2, step 1 widened), the book per entry by vocabulary share AND header label, matched control = the other books + a
meaning-shuffled copy of the chosen book, `ciphers/eckert-1864/decode.py --check` (or decode_no2.py / decode_no9.py) after filing,
crops cut by `tools/iiif_lines.py --image <file> --out <scratch dir>` (paste the command). Additions from the LS4 first audits:
0. Step 0 before anything: read the row's OWN Huntington transcription (sources/mssEC19/p<pointer>.json) AND, for any row to or from
   Grant, Lincoln, Stanton, Halleck, Butler or Meigs, one Google Books API query (country=US, GOOGLE_BOOKS_KEY) for a decoded or clear
   phrase in The Papers of Ulysses S. Grant / Basler -- the verifiers' N1/N2 calls came from these two sources 4 times in 10 (handoff lesson).
1. After decoding, the decoded-text phrase pass (2-4 phrases per entry through be-api, no identifier) and, for Butler/Fort Monroe traffic,
   Butler's Private and Official Correspondence (5 vols, find the IA identifiers, log them). An entry found in print is filed with its
   volume/page and is not sent to a verifier.
2. Shared rows: 9062/1 + 9062/2, 8992/0 + 8992/1, 9034/0 + 9034/1, 9124/0 + 9124/1 are same-page pairs split across readers: read only your
   own entry; if your entry continues onto the sibling's, read the continuation and say so in ROOM so the other reader skips it.
3. Next free IDs: `grep -o "E1[0-9][0-9]" ciphers/eckert-1864/NOTES.md | sort -u | tail -1` at the moment you file, after a fetch;
   LS5-R1c takes E103 onward, LS5-R1d takes E120 onward, LS5-R1e takes E140 onward (avoids collisions; gaps are fine). No. 2 or No. 9
   rows go to that book's file with the same offset rule (N2-DA onward for R1c, N2-EA for R1d, N2-FA for R1e).
4. Unit ~0.55 per entry read (ST-LEDGER-4 ledger). hdl.huntington.org at most 40 requests each, under the token.
NOTES sections "## LS5-R1c (8 Oct 2026, account 1, for LANE LEDGER)" etc. with the per-entry table (row, ID, book, three shares, clause
counts chosen vs controls, H, step 0 and print result), Remaining gaps and Escalation, gaps_check after.

## FM-PRE (Sonnet 5.5; cap $5.5, box 100 min): Fort Monroe "Ciphers Received and Sent", Huntington object 5952 -- pre-filter, no reading
Folder ciphers/eckert-1864/fortmonroe/ (NOTES section in ciphers/eckert-1864/NOTES.md "## FM-PRE ..."; scripts and TSVs in the sub-folder).
1. Prior-work checks 1-4 for the ledger as a whole: our own work (grep 5952, "Fort Monroe", "Monroe" in eckert-1862/1864 NOTES/AUDIT and ROOM);
   the Huntington catalogue record and its scope note; Butler's Private and Official Correspondence (IA identifiers, 1864-65 volumes) as the
   sender-family edition; OR I vols 33, 36 pt 1-3, 40 pt 1-3, 42 pt 1-3, 46 pt 1-3, II/6-8, III/4-5; ORN I/9-11.
2. Harvest the page transcriptions under the hdl token (at most 250 requests this session): try one bulk page-level query first
   (dmQuery with field `transc` on the compound object's pages, or dmGetCompoundObjectInfo + dmGetItemInfo per page); if 411 pages exceed the
   budget, take the 1864 pages first (to the first Jan 1865 date) and list the rest. Save to ciphers/eckert-1864/sources/fortmonroe/
   p<pointer>.json (transcription text only, small).
3. Segment into entries (reuse ciphers/eckert-1864/entries_mssEC19.py with an added `--pages-dir`/`--prefix` option, not a private copy), mark
   direction (received/sent), date, sender, addressee, the code-word share against key.md (No. 1), key-no2.md (No. 2) and key-no9.md (No. 9),
   and the PF4 checks (a) widened print incl. Butler's Correspondence, (b) own transcription clear? (c) same-leaf/neighbour duplicates, and
   the mssEC 19 overlap (the same telegram may also be in mssEC 19: match on date + addressee + >= 3 shared rare tokens).
4. Known-answer control before the verdicts (rule 3): 6 Fort Monroe entries you find printed in OR/Butler -- does the filter flag them? Report
   recall; if under 4 of 6, say which check missed and fix once.
Output ciphers/eckert-1864/fortmonroe/entries-fm.tsv + prefilter-fm.tsv (verdict clean / print-likely / clear-sibling / dup / mssEC19-dup) and
the clean rows ordered for a reader by book. No decoding. Also: does the ledger switch book in 1865 (No. 3/No. 4, not in hand)? Give the date.

## K8472 (Sonnet 5.5; cap $5, box 100 min): which book reads objects 8472 and 6254 (controlled key test on 10 entries each), plus 9660
Folder ciphers/eckert-1862/obj8472/ and ciphers/eckert-1862/obj6254/ (NOTES section in ciphers/eckert-1862/NOTES.md "## K8472 ...").
1. Prior-work checks 1-4 per ledger (as FM-PRE, editions: OR I vols 11, 12, 19, 21, 25, 27 and III/2-3 for 6254 (Army of the Potomac HQ,
   Aug 1862-Apr 1863); for 8472 the War Department office, Aug 1862-Jan 1864, Basler for Lincoln's telegrams).
2. Under the hdl token (at most 120 requests): page transcriptions for 25 pages spread over each ledger (dates early/middle/late), and for
   9660 two dated pages to compare with 8472 (duplicate copy? say yes/no with the two dates and the shared text).
3. Pick 10 coded entries per ledger (ones with >= 8 code-shaped words and not clear in their own transcription), and apply every book in hand:
   ciphers/eckert-1862/key.md (mssEC 15 book, Feb-Jul 1862), ciphers/eckert-1864/key.md (No. 1), key-no2.md (No. 2), key-no9.md (No. 9);
   score each by vocabulary share and clause counts against a meaning-shuffled copy of the same book (two seeds). Pre-register the
   verdict rule in NOTES before scoring: a book "reads" a ledger when its share beats every other book and its clause count beats both
   shuffled copies on >= 7 of 10 entries.
4. Verdict per ledger: the book that reads it with the numbers, or "no book in hand reads it" (then this ledger stops: Remaining gaps entry
   blocker no-key-material, naming the period of the book needed). No reading of entries beyond the test.

## E62-ALN (Sonnet 5.5; cap $3, box 60 min): eckert-1862 -- align the 20 printed residue entries to their OR print
The cheapest next of ciphers/eckert-1862/NOTES.md Remaining gaps (LS3-R62): the 20 M-bearing residue entries with >= 3 6-gram hits in one OR
volume (list them from LS3-R62's re-grep output). Run `ciphers/eckert-1862/print/or_align.py` (unchanged unless an option is needed) on each
against its OR page (local djvu text in scratch, not committed); record per entry the M tokens that get a dated C witness, every proposal
that conflicts with key.md (do not edit key.md for a conflict: log it in HYPOTHESES.md with both witnesses, rule 4), and widen the
single-day key rows named there (Myrtle, Mary, Ingress, Camden, Humboldt) only when the print gives a date. Then regenerate the residue
(residue_decode.py) and report the C/M/I counts before and after. No Huntington requests needed. NOTES "## E62-ALN (8 Oct 2026, account 1,
for LANE LEDGER)", Remaining gaps and Escalation updated, gaps_check after.

---

# Wave 2 (written 8 Oct 2026 18:1x UTC)
Wave 1 by get_session: LS5-R1c 4.53, LS5-R1d 4.19, LS5-R1e 2.79, K8472 2.49 (no book in hand reads 8472 or 6254: that ledger stops).
Readers filed 24 entries; 15 located in print by the readers themselves, 10 rows skipped at step 0. Not located (9): E103 E104 E106 N2-DB
(LS5-R1c), E122 E123 (LS5-R1d), E143 E145 E146 (LS5-R1e).
hdl token lesson: three readers posted `take` within the same minute (17:52) -- the check-then-take is not atomic across sessions. Before
your first hdl request after posting `take`, fetch ROOM again: if another `take` without `release` is newer than the last release and
earlier than yours, wait for its release.

## FV-LS5-A and FV-LS5-B (Opus 5.5, first verifiers, separate sessions from the readers; cap $5 / $4.5, box 90 / 80 min)
Exactly the "## First verifiers LS4-V2a and LS4-V1a" section of .claude/briefs/runs/2026-10-08-acct1-st-ledger4-workers.md (points 1-4 first
per entry: own Huntington transcription + CONTENTdm full-text search of the decoded substance; OR ser. I-III + ORN; Papers of U. S. Grant
(Google Books snippet search, country=US, reaches vol. 13) and Basler; press of the day), plus .claude/briefs/prior-work-step.md check 5 (G3,
same-day replies/antecedents, the clear reply in the received ledgers mssEC 11). New first point from FV-LS4-R2b (17:56 UTC: N2-CC = N2-M,
N2-CL = N2-R): **diff each entry's pointer, date and addressee against every already-filed ID in NOTES.md/status.json** -- a duplicate is
withdrawn, not audited. Depth per .claude/briefs/runs/2026-10-08-acct3-depth-bar.md. AUDIT.md heading "## AUDIT (FV-LS5-A)" / "(FV-LS5-B)";
status.json rows for N3+ only with audit_status "one audit"; SO row per N3+ entry; tools/depth_check.py passes; file_shrink_guard. hdl
token as above, at most 40 requests. On N3+ D2+ add a WORK-QUEUE row `AUD2-LEDGER-<n>` (account account-3, Opus 5.5, cap 2.5 per entry)
and name it in ROOM for the account-3 VERIFY lane. Unit ~0.8 per entry.
- FV-LS5-A: E103, E104, E106, N2-DB (NOTES "## LS5-R1c"), E122 (NOTES "## LS5-R1d").
- FV-LS5-B: E123 (incl. its reply), E143, E145, E146 (NOTES "## LS5-R1d", "## LS5-R1e").
