# LANE-VERIFY-2 job briefs (account 3, session_01KGRk2s5FgW1PSCfQe5WCT7), 8 Oct 2026 from 19:5x UTC
Lane brief: .claude/briefs/lane-verify.md (+ lane-common-blast.md). Continues LANE VERIFY-1's handoff in STATUS.md.
**Common tail for every job: the "Common tail" of .claude/briefs/runs/2026-10-08-acct3-verify1-jobs.md (lines 3-17) verbatim**, with
these changes:
- Prior work: the FIRST step per item is `python3 tools/prior_work.py <slug> --item <item_id> --step-type second-audit --fetch` (or
  `--item-spec 'shelfmark=..;folio=..;date=..;sender=..;recipient=..'` if the item has no items.tsv row), then after reading the
  decoded body `--reading <file> --network` for G3; paste both outputs. Where v1 does not reach, run the hand checklist in
  .claude/briefs/prior-work-step.md and paste one line per check. Log all of it in your AUDIT.md section under "Prior-work checks 3-5".
- Lesson carried from VERIFY-1 (6 items lowered): G3 must cover the holder's own transcription (Huntington CONTENTdm full text for
  eckert), recipient-side and staff papers, same-day orders in the destination department, the sender's same-week letters to OTHER
  recipients, and the press of the day.
- Duplicate diff first (FV-LS4-R2b lesson): diff each entry's pointer, date and addressee against every already-filed ID in
  NOTES.md/status.json; a duplicate is reported as such (status.json note) and not audited further.
- Done line "for LANE-VERIFY-2 / acct3-orchestrator". Stop at 80% of cap or box before starting a new item.
- Never print credentials; never AskUserQuestion; rule 10 and 4a wording only.

## AUD2-LS4C (account 3), cap $8, box 80 min: eckert-1864 N2-CE (D3), N2-CK (D3), N2-CJ (D2)
First audit FV-LS4-R2b (account 4), reader account 1. Shape exactly as "## V1-LS4B" in the verify1 jobs file. AUDIT.md heading
"## AUDIT 2 (AUD2-LS4C)". Update the three status.json rows (audit_status "two audits" if held) and SO rows if a class moves.
Units 3 x $2.5 + 1 reconciliation.

## AUD2-LEDGER-1 (account 3), cap $10, box 90 min: eckert-1864 E106, E122, E104, E103
First audit FV-LS5-A (account 1), readers LS5-R1c/R1d (account 1). Shape as V1-LS4B; start with Papers of U. S. Grant vols 10 and 12
(Google Books snippet search, country=US). AUDIT.md heading "## AUDIT 2 (AUD2-LEDGER-1)". Cap 2.5 per entry.

## AUD2-LEDGER-2 (account 3), cap $10, box 100 min: eckert-1864 E123, E143 (D3), E145, E146 (D2), N3 weak each
First audit FV-LS5-B (account 1), readers LS5-R1d/R1e (account 1). Shape as V1-LS4B. E123 includes its reply. AUDIT.md heading
"## AUDIT 2 (AUD2-LEDGER-2)". Cap 2.5 per entry.

## AUD2-LEDGER-3 (account 3), cap $10, box 100 min: eckert-1864 E162, E160 (N3 D3), E163, E164 (N3 D2, weak: frame largely clear)
First audit FV-FM1 (account 1), reader FM-R1 (account 1), Fort Monroe ledger mssEC 25. Start with Plum 1882 (E164 route), Butler's Book
pp.754ff (E160/E162), OR I/42 pt 3 by page; Butler's Private and Official Correspondence vols III-V by phrase (IA ids in NOTES
"## FM-PRE"); the sender's copy in mssEC 19/18 (sources/mssEC19, sources/mssEC18). AUDIT.md heading "## AUDIT 2 (AUD2-LEDGER-3)".
Cap 2.5 per entry.

## AUD2-MANT8 (account 3), cap $6, box 75 min: sachsstaatsarchiv-manteuffel-1712 Loc. 694/09 f.8-8v (frames 0015+0016), Gersdorff
relation of 3 Jan 1713 forwarded to Manteuffel 13 Jan (VERIFY-BACKLOG high audit2 row, status.json results[194])
Reader FAM-MANT15 (account 2), first audit "## AUDIT (FAM-MANTV)" (account 2). Account 3 ran only a G3 check on f.410 (V1-G3D), never
read or audited f.8. FAM-MANTV itself names the unchecked family: Gersdorff's relation printed in Sbornik RIO or a Saxon-Polish
edition (would lower to N1) -- start there, then the Dutch side (Gersdorff at The Hague: Lamberty, Mémoires; the Heinsius
correspondence via Huygens retroboeken full-text search), Droysen IV.2, the press of the day (Europäische Fama, Mercure historique
Jan-Feb 1713), G3 on the French fragments. AUDIT.md heading "## AUDIT 2 (AUD2-MANT8)". Depth keep or lower only.

## V2-G3GAPS (account 3), cap $5, box 70 min: the cheap open G3 gaps from LANE VERIFY-1 handoff next item 4
(a) huntington-blathwayt-madrid-1728 BLA 186 vs the London Gazette of 13 Sept 1728 (and +-1 issue); (b) august-van-saksen-1561-64 WVO 56
vs the Dresden Zeittung pp.10-13 named in V1-G3C (candidate external check for WVO 53 depth: report it, do not re-rule depth); (c)
jan-van-nassau-1572-75 WVO 5551 vs Kluckhohn, Briefe Friedrich des Frommen II (IA `bub_gb_3N1SAAAAcAAJ`, Fraktur OCR: search by
names/dates, read the hit pages). Read each item's existing G3 section first. One section "## G3 check (V2-G3GAPS)" per AUDIT.md;
class moves only on a print hit. loc.gov: one probe at most, log unreachable if 403. Units 3 x $1.2 + 1 reconciliation.
