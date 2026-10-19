# Two-day research report, account 4 (17 Oct 00:45 UTC to 19 Oct 01:1x UTC)

Owner's request, 17 Oct 2026: "check in in a couple days on your progress and only iterate with data". Written from records only:
status.json, AUDIT.md, HYPOTHESES.md, PREREG files, QUEUE.md, learning/, and the LEDGER.md rows of 17-19 Oct. No proposals.

## 1. Readings (N3+ / D2+ changes)
- **One new result.** sherwood-cossit-1781: the Cossit/Sumner cypher messages to Justus Sherwood, February 1783 (Haldimand Papers, BL
  Add MS 21838 pp.345-347), are partially deciphered as a page-and-printed-line code into Entick's *New Spelling Dictionary* (1781).
  Class N3 with depth D2 (72.7% H/C/S; 216 rows H 8, C 4, S 145, M 57, I 2). Key: ours (we identified the code book); the design,
  Entick as a Haldimand-service code book, was already published. One audit, and a rule-7 send-back fixed before the class. Not N4
  while Leighton and Matyas 1985 is unread (ASKS 174). status.json row added 18 Oct.
- No other status.json result changed class or depth (diff of status.json against the 17 Oct 00:45 commit: 1 row added, 0 changed).
- **Mercy 1648, D2 ceiling (PREREG-MERCY-CEIL.md):** the clause route is reachable only in principle. Longest H/C/S run: 89 committed
  and 89 with every reader-settlable M, against an AD of 125.9; the ceiling with every M as transcribed is 393. The smallest crossing set
  is r20:6-7 plus code 25 at r19:10 (run 132), and neither is a legibility question. MERCY-GAP (pixel gap statistic) FAILed its own gate
  (LOO 5/6 positives, negatives 0.940; label-shuffle control 20/20), so it is a non-test. D2 for Mercy waits on new key evidence for
  code 25 (the Brussels sibling, ASKS 60 / SEND-QUEUE S3). Mercy stays at D1.
- Lope Hurtado 1522 (LOPE-KEYAPP): Kolosova's published Cifrario 7 passes its known-answer gate but adds 2 tokens. The table is
  confirmed; no depth change.

## 2. Flagship fr16104-vivonne-spain-1572
Hypotheses map: RESEARCH.md s.2 (K1-K3 key, T1-T5 transcription, L1 language, A1 AD bar). Experiments since 17 Oct, all in
HYPOTHESES.md rows 15-18 with their PREREGs:
| experiment | control and gate | result | decision and the evidence line |
|---|---|---|---|
| VIV-SYNTH (synthesis) | known-leaf error split | reader error about 0.14 on clean truth; clerk doubt explains 0.00-0.035 | pivot: from more reading passes to an error-matched synthetic (EVIDENCE-DECISIONS 17 Oct 01:1x) |
| ERR-SIM | zero-error synthetic of ink 63 on key.tsv, 5 seeds | the control itself reads only 54 letters against an AD of 94.6; 143 with p and m coded | pivot: the key caps the run, not the readers; key cells p, m, f next (17 Oct 02:2x) |
| VIV-KCELLS | LOO known answer 12/14 vs chunk-shuffle mean 2.95, max 5 | gate PASS; trial labels c = p, 2 = m | continue to a crossword test |
| VIV-KCELLS2 | value-shuffle null, 20 draws | hrunV 26 ties p99 26; crossover below 0.05 reader error (measured 0.14) | FAIL, branch (c): split the merged labels first (17 Oct 04:3x) |
| VIV-KSPLIT | frequency-matched null; tiles | s rank 1/21, but hrunV ties, so FAIL by the both-statistics rule; 36 usable tiles (c: 12 p / 3 other; 2: all m) | under 30 tiles per side, so no model read; the owner's blind sort became the only instrument (ASKS 173) |
| VIV-TILES6770 | n/a (tile cutting) | ink 67/70 tiles added to the packet | feeds ASKS 173 |
The flagship was not changed. The program is blocked since 17 Oct about 07:00 UTC on the owner's 10-minute blind sort (ASKS 173,
sorter artifact; no piles saved as of 19 Oct 01:00 UTC). Flat result: no reading moved; the diagnosis moved from "transcription" to
"the key caps the run, and two labels are merged".

## 3. Discovery (program C)
New QUEUE.md sections: "Key-beside-cipher candidates (17 Oct)" (SCOUT-KEYS, K1-K10), "Haldimand-service cypher pool (18 Oct)",
"Book-code candidates (18 Oct)". Rows promoted to a first test, with results:
| row | first test | result |
|---|---|---|
| K1 Haga, NA inv. 6896 | check-solved + 2 leaf hunts | open; leaf not located (the lias interleaves correspondents); stopped at USD 11.4 |
| K2 Aitzema, NA inv. 6025 | check-solved + 2 sheet passes | open; Feb 1618 run not located; stopped |
| K3 Berck, NA inv. 6897 | check-solved | open; one pair, already deciphered at the time; parked, no leaf hunt |
| K4 Fuente intercepts, TNA SP 84/165 | check-solved + DECODE key-image test | open; 11 undigitised intercepts; the 3 DECODE Spanish key pages are not Tomokiyo's no. 34; TNA copy held (SPRINT P12) |
| K9 Sherwood/Cossit, LAC reels | check-solved, then 7 more jobs | **read: N3/D2** (section 1) |
| K10 C11A despatches | calendar grep | no undeciphered candidate (all 8 show a decipherment reduction) |
| Haldimand pool rank 1, B.149 p.286 | check-solved + page fetch | found-solved by premise: no cipher on the page; ranks 2-3 not pursued |
| Book-code B1 Jay-Deane 1780, B2 Livingston-Jay 1781 | check-solved / record | both found-solved in the modern Selected Papers of John Jay |
Yield: 1 reading from 13 promoted rows. Lessons written into QUEUE.md: a calendar "in cypher" line locates a covering letter, not
necessarily ciphertext; a catalogue's "not deciphered in <old edition>" note is not a check of the modern edition.

## 4. Assumptions the system caught itself
- learning/EVIDENCE-DECISIONS.md entries since 17 Oct: VIV-SYNTH (the transcription assumption), MERCY-CEIL (readers cannot reach the
  bar), ERR-SIM (the key, not the readers), VIV-KCELLS2 (merged labels first), and SHERWOOD-PAGES (the 1778 key excluded; switch to
  book identification). Separately, SHERWOOD-VERIFY's blind rule-7 re-read caught a line-grid error of the solver's own instrument (9
  cells, 4 pages) before any class was given, and the re-issue fixed its cause.
- learning/ASSUMPTION-CASES-2026-10-17.md (CASES-TX): in all four named owner-caught cases (Debosnys, Mercy, Salviati, Vivonne) the
  number showing the problem was on disk 1-10 days before the outside catch, and a check under about USD 3 on disk files would have
  found it. In two (Debosnys, Mercy) the folder had written the right conclusion down and kept working on the opposite assumption.
  The outside contribution was narrow: the owner's perceptual sorting and Bourdeau's split reading.

## 5. Interventions
- learning/INTERVENTIONS.tsv since 17 Oct: one row, the owner's 17 Oct directive (strategy, not avoidable).
- Required the owner (money, email, physical, or a person's eye): the FDR follow-up email and phone payment (SPRINT P1); the two ILL
  scans (Fontaine 1972, Kolosova 2024), read on 17 Oct; the BnF order DEV-2610-010032; the NRS permission reply; and the open asks
  ASKS 173 (the Vivonne sort) and ASKS 174 (the Leighton and Matyas ILL). Money items are collected in SPRINT.md (P1-P12).
- Did not require the owner: the whole Sherwood chain (locate, transcribe, identify the book, read, two verifications, fix), every
  check-solved, the Vivonne diagnosis chain, and the Mercy ceiling and gap tests.

## 6. Spend (account 4, LEDGER.md rows 17-19 Oct, cost from get_session)
| program | jobs | USD | share | starting split |
|---|---|---|---|---|
| A recovery (Mercy, Lope, FUENTE-KEY, Sherwood from SHERWOOD-BOOK on) | 10 | 35.65 | 33% | 40% |
| B flagship (Vivonne) | 6 | 16.88 | 16% | 30% |
| C discovery (check-solveds, leaf hunts, scouts, SHERWOOD-PAGES) | 15 | 55.52 | 51% | 30% |
| total | 31 | 108.05 | | |
Not included: SCOUT-KEYS and CASES-TX, run for account 4 by account 2 and not yet ledgered there. Orchestrator overhead is not
ledgered per check-in. Program B ran under its share because it has been gated on ASKS 173 since about 07:00 UTC 17 Oct. Program C ran
over because its single success needed seven follow-on jobs and four promoted rows returned nothing.
Per-account usage (tools/usage_watch.py, 19 Oct 01:0x UTC): account 1 allowed; account 2 allowed; account 3 allowed_warning
(seven-day); account 4 allowed_warning, seven-day, resets 20:00 UTC 19 Oct. Live workers: 0 on every account.
