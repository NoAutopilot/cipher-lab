# Research director, wave 49 (24 Oct 2026, 09:2x UTC by date -u): SP 106/6 no. 32 key as key.tsv; promote the Wickfort/De Bacquoy pool with its copy request

Common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Done line addressed for the account-4 parent. Gallica is not involved.

## JOB KEY32-TSV-PROMOTE (account 4; Sonnet 5; cap USD 6; box 50 minutes; hosts: de-crypt.org (ONE browser login, <=10 fetches, >=2 s apart: RecordsView 509 and 506 and their three attached text documents only), discovery.nationalarchives.gov.uk details endpoint (<=4); Price: vision calls: 0 x USD 0 = 0)

Read first: ciphers/sp84-fuente-1662/NOTES.md sections "## DECODE fetch (DECODE-KEY32 ...)", "## DECODE fetch, second pass" and the two
parent notes after them; sources/decode/2026-10-24-sp106-6-keys/{509,506}/README.md; ciphers/_triage/sp84-wickfort-bacquoy-1660-63.md;
harvest/C-FOLLOW-2026-10-24-sp84-gloss.tsv; sources/cryptiana/web/chauran.htm (on disk); tools/decode_key.py --help and one of
tools/tests/decode_configs/ for the key.tsv columns.
Part 1, the key (route priority 1, grade H: read from a key source).
1. One login (tools/decode_browser_login.js, as DECODE-KEY32B did) to re-fetch the three attached transcription documents of 509 and 506
   (DOC_R509_D2952, DOC_R509_D2953, DOC_R506_D2951) into your scratchpad; raw documents and images are not committed
   (sources/decode/NOTES.md); record their sha256 in the two manifest.json files if missing.
2. Parse them with a script you commit (ciphers/sp84-wickfort-bacquoy-1660-63/build_key_no32.py) into
   ciphers/sp84-wickfort-bacquoy-1660-63/key.tsv: columns code, mark (DECODE's mark name, verbatim), meaning (French, as transcribed,
   abbreviations kept), class (letter | person | ville | royaume | word | syllable | other), source (509 p1 / 509 p2-3 / 506), grade H.
   Where 509 and 506 disagree on a value, keep both rows and flag `conflict` (rule 4: a data conflict, not a majority vote). Append a
   provenance header: TNA SP 106/6 no. 32 (Tomokiyo's numbering, chauran.htm), DECODE records 509 and 506, transcriber initials and
   date as DECODE gives them, fetched 24 Oct 2026; the script re-derives key.tsv from the documents and exits non-zero if the
   committed file differs (rule 7); since the documents are not committed, the script also accepts `--check-hash` against the
   manifest sha256 so a later session can verify it fetched the same text.
3. Cross-check against chauran.htm's structural description (class ranges 20-76 / 61-89 / 90-108, the 23-letter alphabet): write the
   counts per class and any range that disagrees into NOTES.md; do not "fix" the key to match Tomokiyo.
Part 2, the folder (promotion after check-solved: the triage note's verdict is `open` with the editions named).
4. Create ciphers/sp84-wickfort-bacquoy-1660-63/ with NOTES.md whose first line is `blocked` (rule 5 vocabulary: every unread piece
   waits on the TNA images) followed by: the check-solved sentence copied from the triage note (with its date and worker), "## Premise
   check" copied, the pool table (Group A controls, Group B targets, with the key question per item: Wickfort = no. 32 expected;
   De Bacquoy = numerical cipher, key unidentified), "## Key" (what key.tsv is and is not), "## Remaining gaps" and "## Escalation"
   ending in a Verdict "parked" (the gap is needs-physical-access / copy order), and "## While waiting" naming the one action that
   depends on nobody (none remains inside the session once key.tsv exists; say so). Run `python3 tools/dup_check.py
   sp84-wickfort-bacquoy-1660-63`, `python3 tools/prior_work.py sp84-wickfort-bacquoy-1660-63`, `python3 tools/intake_gate_check.py
   sp84-wickfort-bacquoy-1660-63` and `python3 tools/gaps_check.py sp84-wickfort-bacquoy-1660-63`; paste each output into NOTES.md
   and fix what they flag.
5. REQUEST.md: the exact TNA copy request in the folder's own words, no money figure (SPRINT P12 carries the money side): minimum
   order SP 84/166 f.85 (Wickfort, 10 Aug 1662, entire letter in cipher) + SP 84/165 f.106 (Wickfort, 5 Mar 1662, PRO-decoded with
   no. 32, the known-plaintext control, both recto and verso and the PRO's decode sheet if filed with it); full order the other
   nine Group B folios; Discovery ids beside each; the known TNA tariff route (Discovery "request a copy" per item). Mark the target
   "waiting on you" in your report. Never decode anything; key.tsv is applied to nothing in this job.
Report: key.tsv row count by class, conflicts, the four gate outputs in one line each, the REQUEST.md minimum order, five lines.
