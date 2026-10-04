partial
CSP Foreign Elizabeth vol.21 pt.3 pp.197-217 and pt.4 pp.199-212 (British History Online) read by this worker today, with a control name confirmed present on each page, and DECODE's own record pages fetched directly (RecordsView/8477 etc.): no decipherment of the Cobham/Needham cipher passages found in print and DECODE still marks every record Non-decrypted/Partially decrypted; unchanged from the 23 Sept 2026 sweep below.

# BL Harley MS 287 cipher letters 1587-88: Cobham to Walsingham (4), Needham, unsigned (7) — DECODE R8477-R8496

- Source: QUEUE.md rank 13 (score 33), scored 20 September 2026; catalogued from the DECODE record range
  (de-crypt.org/decrypt-web/RecordsView/8477 through 8496) via Bourdeau's `cyphersolver` catalogue harvest.

## Check-solved (LANE CX2, 25 September 2026)

Fresh sweep by this worker (session CX2-BRIT2), independent of the 23 Sept pass below (its findings are not
quoted, only cross-checked).

1. **Web search.** `Harley MS 287 Cobham Walsingham cipher 1587 1588 deciphered solved` and `Harley 287 cipher
   "solves" Claude GPT Vals AI` (WebSearch) — no page reports this volume solved; hits are the Babington Plot
   (unrelated Mary Stuart ciphers), a Cambridge Core article on Nicholas's correspondence, and the unrelated
   Cyphral Distich (Urquhart 1653) model-solve story. One snippet paraphrased Bourdeau's own `harley287`/
   `cobham1588` pages (see item 5) without adding a new source. found=false.
2. **Print, own read.** CSP Foreign Elizabeth vol.21 pt.3 (British-History-Online, `cal-state-papers/foreign/
   vol21/no3`, HTTP 200) is dated April-December 1587; fetched `pp197-217` ("Elizabeth: July 1587, 26-31") and
   found the Francis Needham letter dated "Flushing, 28 July, 1587" calendared as an ordinary English narrative
   of the Sluys relief attempt, with no "in cipher"/"deciphered" marker on it; control: the same page also
   calendars "Sir William Pelham to Walsingham" and "The Same to Walsingham" for the same date, confirming real
   page content, not a stale fetch. CSP Foreign vol.21 pt.4 (`cal-state-papers/foreign/vol21/no4/pp199-212`,
   "Elizabeth: March 1588, 16-20") read the same way: no entry names "Cobham" on this page; two entries
   mentioning "Ostend" (Remarks touching Ostend; De Loo to Burghley) are plaintext with no cipher notation;
   control: "Sir James Crofte" (20 March) and "Dr. Rogers" (18 March) both present on the page, confirming it
   is being read, not a blank/error page. Neither page reproduces or notes a decipherment of the Harley 287
   cipher runs. Google Books: `GOOGLE_BOOKS_KEY` is set in this environment (unlike the 23 Sept pass, which
   found it unset) but not used this pass — the calendar pages above already answer the "is it printed
   deciphered" question with a control, and CLAUDE.md's usage rule against redundant fetches applies once one
   source has answered with a control.
3. **Community lists.** `sources/cryptiana/web/elizabeth.htm` re-grepped (on disk, not edited): still documents
   Cobham's 1588 ciphers with Burghley/Walsingham only in general terms, no mention of Harley MS 287 or these
   DECODE records, no decipherment printed. Cipherbrain/scienceblogs.de: WebSearch snippets only, as
   23 Sept (full-page fetch of that host is not attempted here; not re-tested for reachability this pass).
   found=false in Cryptiana; unread/unreachable on Cipherbrain (unchanged).
4. **DECODE.** de-crypt.org answers HTTP 200 from this container today (egress unblocked since 23 Sept, when it
   was `connect_rejected`). Fetched `RecordsView/8477`, `8479`, `8482`, `8490`, `8496` directly (no login,
   1.6s apart): R8477 Non-decrypted, R8479 Partially decrypted, R8482 Non-decrypted, R8490 Non-decrypted, R8496
   Non-decrypted — DECODE's own status field, read by this worker, matches Bourdeau's off-platform findings
   below and shows no one has posted a decipherment to the platform itself. found=false (own read, not a
   citation of the 23 Sept "unreachable" note, now superseded).
5. **Bourdeau (`github.com/dbourdeau/cyphersolver`, fresh shallow clone 25 Sept 2026, MIT code / CC BY 4.0
   text).** Re-confirms the 23 Sept finding, dated in this clone's own commit (25 Sept 2026 11:19): `needham1587/`
   (R8479, "read", 227/261 tokens measured, three-grid pigpen, Wilkes-Walsingham key per CSP Foreign 21/3 n.4,
   key itself in BL Add MS 5935, not consulted); `harley287/` (R8477+R8482-R8487, "read in part", reclassified
   from "read" on 22 Sept because no token-level fraction was ever computed — open items still code 42, sign
   `.7.`, one Jesuit's surname, one verb, scattered words; R8477/f.11 confirmed a different, shorter, unrelated
   code, not read); `cobham1588/` (R8490+R8492+R8495+R8496, "read in part", key rebuilt from the same cipher's
   glossed siblings, no fraction measured). No other DECODE record in the R8477-R8496 range belongs to a
   different BL volume (checked profile.json shelfmarks for every neighbouring folder — harley1582r8499/r8500/
   r8504, harley286, r8356/r8358/r8361/r8362/r8364, stafford1586, walsingham1572/1572nov/1585, wotton1585 — all
   are Harley MS 260, 1582 or 286, or Add MS 32657, not Harley MS 287). Write-ups unchanged:
   https://dbourdeau.github.io/cyphersolver/harley287.html, /cobham1588.html.
6. **Aymeloglu (`github.com/aaymeloglu/unsolved-ciphers`, fresh shallow clone 25 Sept 2026; no licence, cite
   only).** `grep -rli` for "cobham", "walsingham", "needham", "harley" (any Harley shelfmark) across the whole
   repository: zero matches beyond the unrelated `forster-1644` and `royalist-1646` folders (different targets,
   different shelfmarks). found=false (not attempted in this repository).

Intake verdict: open (this worker's own CSP Foreign read, with a control on each page, satisfies the gate's
citation requirement; `tools/intake_gate_check.py` exits 0 below).

## Check-solved sweep (23 September 2026)

1. **Web search.** "Harley MS 287 Cobham Walsingham cipher 1587 1588 solved decrypted" — no page reports this
   volume decrypted; results are about the unrelated Babington Plot and Mary Stuart ciphers. found=false from
   open web search.

2. **Print.** The 20 September 2026 search-print pass already recorded in QUEUE.md checked CSP Foreign Elizabeth
   vol. 21 pt 4 (Jan-June 1588, british-history.ac.uk) in detail: the index and text around pp.442-460 give only
   English abstracts and a postscript note ("Sent the cipher by Spritwold"), never a reproduced or "deciphered"
   cipher passage, and "Needham" indexes to a single unrelated entry. Vol. 22 (July-Dec 1588) is on HathiTrust
   (htid `msu.31293027027295`, full view) but Cloudflare-blocks curl and the browser tool; the HTRC Extracted
   Features API located a candidate page (scan 62, adjacent to a Cobham mention, with both "cipher" and
   "decipher" tokens) but it remains unread. Not re-run this sweep; status unchanged: NOT FOUND in print,
   vol. 22 inconclusive. Google Books: not available in this account's environment (no key set here).

3. **Community lists.** `sources/cryptiana/web/elizabeth.htm` (grepped locally, never edited) documents Lord
   Cobham's separate 1588 ciphers with Burghley and Walsingham in general terms (Burghley providing a cipher in
   April 1588, Cobham sending one to Walsingham in June 1588) but does not mention Harley MS 287 or these DECODE
   records specifically, and prints no decipherment. Cipherbrain/scienceblogs.de site search for this item
   returned no matching post (see full log method in ciphers/charles-rupert-1645/NOTES.md item 3); full-page
   fetches of scienceblogs.de are blocked by this environment's egress policy, so only WebSearch snippets could
   be checked. found=false in Cryptiana; unread/unreachable on Cipherbrain.

4. **DECODE.** `curl -A "Mozilla/5.0" https://de-crypt.org/decrypt-web/RecordsView/R8477` — connection refused
   at the egress proxy (`CONNECT tunnel failed, response 403`, HTTP code 000; `connect_rejected — organization
   policy`). de-crypt.org is unreachable at all from this account's environment; no login attempted
   (DECODE_USER/DECODE_PASS unset here). Source: **unreachable**.

5. **Bourdeau (`github.com/dbourdeau/cyphersolver`, shallow clone 23 Sept 2026, MIT code / CC BY 4.0 text).**
   **found=true, substantial.** Bourdeau's project has already worked most of this DECODE range, in three
   folders, all dated 21-22 September 2026 (i.e. after our own 20 September 2026 search-print pass):
   - `needham1587/` (DECODE R8479, Francis Needham to Walsingham, 28 July 1587, ff.39-40): **read**,
     `fraction_read: 0.978` (182/186 unglossed signs; grades H:44, M:1), one word on one line unresolved. Cipher
     identified as a three-grid pigpen keyed to Thomas Wilkes (per CSP Foreign vol. 21 pt 3's editorial note on
     BL Add MS 5935, not itself online). CATALOGUE.md does not list a public write-up URL for this one.
   - `harley287/` (catalogue item 132: R8477 f.11 + R8482-R8487, Lord Cobham at Ostend to Walsingham, 20 and 22
     March 1587/8): **read in part**. Every cipher run of ff.70r-72v is read in sense (crib-based: "commaunded
     to attend", "that bearer hath", "under colour thereof" etc. fixed most letter values, confirmed
     independently by the `cobham1588` session against contemporary glosses on f.89/R8493); open items are code
     number 42, code sign ".7.", one Jesuit's surname, one verb, and scattered words, with the share of tokens
     read explicitly **not measured** (the 22 Sept 2026 entry in that folder's own profile.json downgrades it
     from "read" to "read in part" precisely because no token-level fraction was ever computed — note that the
     top-level `CATALOGUE.md` line still says "read" for this item, unreconciled with the folder's own later
     correction; we report the folder's own current, more conservative status). R8477 (f.11) is confirmed a
     different letter and code (about eight groups), not read, too short for a key. Write-up:
     https://dbourdeau.github.io/cyphersolver/harley287.html.
   - `cobham1588/` (catalogue item 131: R8490, R8492, R8495, R8496, Cobham to Walsingham, 5 May - 9 June 1588):
     **read in part**, `fraction_read: 0.35` (estimated, "about a third of the cipher words," not token-counted
     against a full sign transcription). Key partly rebuilt from the glossed sibling letters in the same volume;
     several signs remain unglossed or polyphonic (K, upsilon, rho, W; wedge s/t/a, gamma r/y). Write-up:
     https://dbourdeau.github.io/cyphersolver/cobham1588.html.
   DECODE key record R8497 (f.187, Bodley's cipher, December 1590) was checked by Bourdeau's project and
   confirmed a different, unrelated system, consistent with our own 20 September 2026 note. No print source was
   found by that project either (same CSP Foreign vol. 21 pt 4 negative result independently reached).

6. **Aymeloglu (`github.com/aaymeloglu/unsolved-ciphers`, shallow clone 23 Sept 2026; no licence, cite only, no
   code copied).** No target folder and no catalogue-file mention for Harley MS 287 or any R848x/R849x record
   (`grep -rli` across the repository returned zero matches). found=false (not attempted in this repository).

## Verdict

**Partial**, not open. This is not a single undisturbed target: Bourdeau's project has already produced real,
publicly committed partial-to-near-complete readings covering most of the named DECODE range (needham1587 ~98%
read; harley287/R8477+R8482-R8487 read in sense throughout with named gaps; cobham1588/R8490+R8492+R8495+R8496
about a third read), all dated 21-22 September 2026, citing Lasry-style key-recovery from contemporary glosses
rather than a printed source (none was found by their project or by this sweep). No fully "found-solved" claim
applies because none of the three sub-items is complete and cobham1588 in particular is far from it. This
project should not restart this item as an unattempted cryptanalysis target; any further work here is a
finishing/verification job on Bourdeau's existing partial key and transcriptions (MIT code, CC BY 4.0 text —
cite, do not silently duplicate). No Stage 2 line applies (verdict is not "open"). QUEUE.md row 13 has been
annotated with this finding rather than moved to Dropped, since the item is not fully solved.

## Step NEXT-HAR, 2 Oct 2026: solve.py rerun on the third-pass strings, with controls

Brief: `.claude/briefs/runs/2026-10-02-acct3-next-har.md` (the Verdict's cheapest next step). Disk only: one shallow
clone of github.com/dbourdeau/cyphersolver (commit 34e0fc8), no other outside request, no image seen (rule 2: every
figure below is conditional on Bourdeau's transcription, read by him from DECODE full-size crops).

- What was run. Bourdeau's `solve.py` and `wordfreq.tsv` (MIT; vendored unchanged with credit in `solver/SOURCE.md`)
  over `solver/runs_nexthar.txt`: his third-pass sign strings for f.80r, f.81r top, f.92r lines 1-10 and f.96v
  (`reading_ff80_92_96_full.md`), put into his `runs.txt` ASCII code, 109 groups, 45 of them unread by him. Loop-1
  values are already in his SETS (L=e, c=o/a/e, d=o/d, ϕ=l/t/p); `run_nexthar.py` adds `-` = b. Correction to the
  finish-or-blocker classifier: `runs.txt` did hold f.80 runs a-i and f.92 runs a-f, but in the first-pass strings;
  the third-pass corrections, f.81r, f.92r lines 3-10 and f.96v were the parts missing.
- Target. Unread groups with any exact candidate: 19 of 45 (0.42); exact or near: 34 of 45. Split by length, 1-4 signs:
  16 of 21 (0.762) against a shuffled-sign null of 0.572; 5+ signs: 3 of 24 (0.125) against a null of 0.114. The three
  long hits (ApLcA "appease", +lcAA "bless/blast", Ap77l "spell") fit no context. No unread group is read.
- Controls (rule 3, matched to the unread groups' lengths, same sign inventory and solver). Known answer: words of
  Cobham's own clear text on ff.70r-72v (Bourdeau, harley287/READING.md) enciphered with this inventory, true word
  rank-1 exact 0.896 at 0 % sign error, 0.681 at 10 %, 0.415 at 20 % (all lengths, n=135); for 5+ signs (n=480) any
  exact 0.954 / 0.542 / 0.312 / 0.208 / 0.142 and true rank-1 0.877 / 0.458 / 0.221 / 0.123 / 0.065 at 0/10/20/30/40 %.
  Null: the same unread groups with their signs shuffled, any exact 0.304, exact or near 0.738 (450 strings).
- Reading. The solver passes its known-answer control, and the long unread groups score at the shuffled null (0.125
  vs 0.114), which the control reaches only at about 40 % sign error. So the long groups behave as noise to this word
  list: either the strings carry about that much transcription error, or the unglossed and polyphonic signs (K, the
  lone dots, ŧ read e or a, ϸ read c) are wrongly valued. A further rerun of the same solver on the same strings will
  not move them (rule 3 third-attempt clause: this is the second solve.py pass after Bourdeau's loop 1, not yet
  retired, but no third pass on these strings is proposed). The different instrument is the one the Escalation
  already names: a blind sign-by-sign transcription from DECODE full-size crops and the R8491/R8494 glosses.
- □ = the States on f.80 line 1. Tested at no image cost: "hoping theym in the □ lUn87A for what chaunces so ever you
  bestowe" reads as "in the [States] ..." with the clear "the" before the code, which is how Cobham writes the
  States in clear on f.72r ("delivered over to the States") and how □ stands for them on ff.70r/72r (Bourdeau,
  harley287/NOTES.md l.83-84, grade C there). Syntactically compatible, not confirmed: the next group lUn87A gives
  only "lances" exact ("lance", "glances", "paces" near), and "the States' lances" is not a convincing phrase. Grade
  of □ = the States on f.80: M (context carried from a sibling letter of the same sender and volume, March 1588).
- No reading changed, so there is no decode script or judge output to regenerate (rule 7); `run_nexthar.py --check`
  regenerates `solver/out_nexthar.txt` and exits 1 if it is stale.
- Files: `solver/` (SOURCE.md, solve.py, wordfreq.tsv, runs_bourdeau.txt, runs_nexthar.txt, run_nexthar.py,
  control_cobham_clear.txt, out_nexthar.txt). The control text still carries a few editorial words of Bourdeau's
  page header; they are in the lexicon and do not change the comparison.

## Step A2-HAR, 2 Oct 2026: intake gate failed, DECODE step not run

Brief: .claude/briefs/runs/2026-10-02-acct2-a2-har.md (LANE-A2PUSH, account 2). Before the DECODE fetch I ran the intake gate, and it exits nonzero:

    $ python3 tools/intake_gate_check.py harley-287-1587
    harley-287-1587: partial (line 1) has an edition citation but no logged open-web and blog-comment check (no 'Web and blog check' heading, no paragraph naming Cipherbrain, the Cryptiana blog and Cipher Mysteries) -- run check-solved.md's 'Open web and blog comment threads' step first (CHECK-SOLVED-WEB, 28 Sept 2026: spinelli-beinecke-c1515 was read in a Cipherbrain comment thread in 2017)
    EXIT 1

The two check-solved sweeps above (23 and 25 Sept 2026) logged Cryptiana's elizabeth.htm and Cipherbrain only from search snippets ("unread/unreachable"). They did not check Cipher Mysteries, and they did not read any comment threads. The brief allows fixing a gate failure only when the fix is inside its own step, and this fix is a check-solved job. So I made no DECODE login, fetched no records and checked no codes. Hosts contacted: none.

## Remaining gaps (finish-or-blocker pass, 2 Oct 2026)
Read so far: unmeasured for the target as a whole: this folder holds no transcription, key or reading of its own, so every figure is Bourdeau's (cyphersolver commit 34e0fc8, 1 Oct 2026, local clone; only mercy1648 is snapshotted under sources/cyphersolver/2026-10-01/). needham1587: 182 of 186 unglossed signs (97.8%), measured against cipher.txt (profile.json). harley287 (ff.70r-72v): never measured (profile.json fraction_read "unknown"). cobham1588: 0.35 is an estimate (profile.json fraction_read_method "estimated"). The only per-leaf counts are in reading_ff80_92_96_full.md: f.92r lines 3-10, 15 of 37 cipher groups read (H2 M11 I2); f.96v, 15 of 23 (H3 M8 I4). Coded by NEXT-HAR (2 Oct 2026, solver/runs_nexthar.txt) for f.80r, f.81r top, f.92r lines 1-10 and f.96v together: 64 of 109 groups read by Bourdeau at H/M/I, 45 unread.
- ff.39-40 (R8479, Needham to Walsingham, 28 July 1587), f.39v line G word 3, `U ? ? ? ? O C` = b????ed - blocker: not-attempted; was filed "illegible", but Bourdeau's needham1587/NOTES.md l.75-76 says only one of the four cramped signs is blotted, and the three-grid pigpen alphabet is closed (a-i, k-s, t-z). The legible signs have never been tested against seven-letter candidates: "blocked" and "bridged" both fit b+4+ed, while "barred", Bourdeau's guess, does not fit the count. DECODE R8478 (f.37-38, 1587) and R8480 (f.41-42, 1587) are marked Decrypted, sit on either side of this letter, and nobody has opened them (records-decrypted-2026-09-24.tsv; no mention in any of Bourdeau's three folders); next: in the shared DECODE login, eye-check the three unblotted signs of f.39v line G on the full-size R8479 image against the closed alphabet and the candidate list, and look in R8478/R8480 for the same pigpen and word, ~$1.5
- f.11 (R8477): about eight code groups (80, wh24, a circled cross, a square, Nrp54) - blocker: not-attempted; was filed "too-short". Too short to rebuild a key, but nobody has compared it with an existing key. DECODE catalogues Elizabethan English keys of this decade that this project has never opened: R337 (TNA SP 106/1 f.74, 1588), R330 (SP 106/1 f.50, 1587), R8367 (BL Harley MS 290 f.256, 1588), R1819/R3822/R3823 (SP 12/193 no.54, 1586), R338/R328/R933 (SP 106/1, undated Elizabethan) and R9260-R9262 (Add MS 4136 ff.177-185, 1560-1587) (sources/decode/keys-all-2026-09-28-merged.tsv; none is cited anywhere in the repo or in Bourdeau's folders). Whether DECODE holds images for each is untested (R4282 had none); R337 (Croft, 1588) and R8367 (Harley 290 f.256) were fetched full-size on 2 Oct 2026 (A2-HAR, second spawn) and hold none of 80, wh24, Nrp54, the circled cross or the square; next: the other catalogued keys R330, R1819/R3822/R3823, R338/R328/R933 and R9260-R9262 in one DECODE login, same check, ~$2.5
- ff.70r-72v, code number 42 on f.70r ("15 will never yield to send 42 hither") - blocker: open-codes; it occurs once and context allows commissioners or forces (Bourdeau harley287/NOTES.md l.84-85). It is not among the glossed codes 7, 10, 15 and 16 in cobham1588/signs.tsv l.33. Cobham's 25 May 1588 list is a code-WORD list (sources/cryptiana/web/elizabeth.htm l.539: "Beware" for the Pope, "ferret" for Parsons), so it is unlikely to hold numbers; checked 2 Oct 2026 (A2-HAR, second spawn): absent from R337, R8491 and R8494; R8367 has 42 = "puritanes" (struck), but in a different code (60 = Parma there, 15 = Parma in Cobham's), so no value transfers; next: the remaining catalogued keys with the f.11 check above (same login), ~$0.5
- f.71r (R8484, Middelburg enclosure): the Jesuit's surname `+∪∧∧..#7`, read "Bastune?" - blocker: not-attempted; Bourdeau files it not-attempted himself (harley287/NOTES.md "Remaining gaps"). Under harley287/key.tsv the signs give b-a-[s/t]-[s/t]-[u/v/w]-[n/i]-e: ǂǂ is i or n and ".." is u/v/w. The classifier's [m/n] is wrong, because m is ∝. No print search for a Jesuit sent post into Italy in March 1588 has been done; next: read CSP Foreign vol.21 pt.4 (March-April 1588) and CSP Spanish vol.4 on British History Online and test each Jesuit's name against the pattern, ~$3
- ff.70r-72v (R8482-R8487, 6 pages): one verb on f.70r ("will not [keep them] from"), the words marked "..." or "(?)" on ff.70v, 71r, 72r and 72v, and the share of tokens read - blocker: not-attempted; the reading was made word by word from crops with no sign-by-sign transcription (harley287 profile.json gaps; his Escalation "[ ] retry"). Full-size DECODE images have been open to the project account since 28 Sept 2026 (ASKS 42; sources/decode/NOTES.md "access after the PI's extension"). DECODE marks R8486 (f.72r) "Partially decrypted" although Bourdeau found no decipherment on the leaf, so its RecordsView documents should be read in the same login; next: fetch R8482-R8487 at full size in one login (tools/decode_browser_login.js --listen, images in the scratchpad only), cut crops with tools/iiif_lines.py --image, run 2 blind passes per page (12 calls) plus 1 reconciliation at ~$1.5 per call, decode with harley287/key.tsv, regrade, measure, ~$22
- f.80r-81r (R8490): codes 22, 27 and the square sign - blocker: open-codes; none of them is glossed on R8481/R8488/R8489/R8493 (cobham1588/signs.tsv l.33-34). The square has a candidate nobody has tried: Bourdeau's own merged key reads □ as "the States" twice on ff.70r/72r (harley287/NOTES.md l.83-84, grade C). Code 22 recurs on f.81r ("22 hath a desire to retourne"). □ = the States tested on f.80 line 1 (NEXT-HAR, 2 Oct 2026): compatible ("in the □"), not confirmed, grade M; checked 2 Oct 2026 (A2-HAR, second spawn): 22, 27 and a square are absent from R337, R8367, R8491 and R8494 (R8491/R8494 spell names out and carry no number codes); next: the remaining catalogued keys with the f.11 check above (same login), ~$0.5
- f.80r-81r (R8490): the unread letter groups Xd+c:87, AcdD7p#cI, A:VAI, Ac-D:XL and `V z L ### A l c c A`, and f.81r "restrain[ed]?" (I) - blocker: not-attempted; correction to the classifier and to Bourdeau's own gap list: f.80g (HcVwUVd7) is already read "forwarde" (H) in his solver loop 1 and third pass (cobham1588/NOTES.md l.181, reading_ff80_92_96_full.md L5). solve.py was rerun on them with the loop-1 values and -=b (NEXT-HAR, 2 Oct 2026, solver/out_nexthar.txt): no group read; groups of 5+ signs hit the word list at the shuffled-null rate (0.125 vs 0.114) while the known-answer control reads 0.877 rank-1 clean, so the strings act as noise to the solver; next: blind sign-by-sign transcription of f.80r-81r from DECODE full-size crops (2 passes + 1 reconciliation, ~$4.5) after the R8491/R8494 glosses, then rerun run_nexthar.py
- f.88r (R8492): the name after "captain", the word after "haven of", lines 3-6 and the seven cipher words of lines 12-20 (the recurring "Tnn") - blocker: not-attempted; filed open-codes by Bourdeau, but these are letter runs blocked by the unglossed signs K, upsilon, rho and W and by polyphonic signs (cobham1588/NOTES.md "Remaining gaps"). DECODE R8491 (f.84, 1588) and R8494 (ff.90-91) are marked Decrypted in the same volume, and nobody has opened them (records-decrypted-2026-09-24.tsv; grep of Bourdeau's three folders finds neither); next: fetch R8491 and R8494 at full size and align their interlinear glosses sign by sign against cobham1588/signs.tsv (2 pages x 2 passes + 1 reconciliation), ~$8. A2-HAR3 (2 Oct 2026) did this mapping but its pairs were never pushed (A2-HAR4 step below); next: redo it, commit gloss_pairs.tsv before any analysis, then interlinear_align.py with a shuffled control, ~$7.5. Done 3 Oct 2026 (A2-HAR7): f.84r/f.90r glosses aligned with gloss_pairs.tsv committed first, consistency 0.819 vs nulls max 0.305/0.226, 19/20 signs agree with signs.tsv; K, Q, L, upsilon, rho and W are not glossed there at this transcription, so no new value reaches f.88r; next: rerun solver/run_nexthar.py with 8 = c/d added (the only value the glosses add), no vision, ~$0.5; then a gloss-masked cipher-only pass of f.84r to rule out reader projection, ~$3
- f.92r (R8495): of runs 92a-d, 92a is read "Portugals?" (I) and 92d "Bridges" (M) in reading_ff80_92_96_full.md, so the classifier's "92a-d unread" is out of date. Still unread: 92b, 92c and 22 groups of lines 3-10, including the surname -cX8L - blocker: not-attempted; the same unglossed and polyphonic signs; solve.py rerun on lines 1-10 (NEXT-HAR, 2 Oct 2026): no unread group read, same null-level result as f.80r-81r; next: blind sign-by-sign transcription of f.92r from DECODE full-size crops (2 passes + 1 reconciliation, ~$4.5) after the R8491/R8494 glosses, then rerun run_nexthar.py
- ff.96r-97r (R8496): f.96v, 8 unread groups (reading_ff80_92_96_full.md "f.96v counts"); f.96r and the f.97r runs have no sign transcription at all (not in runs.txt) - blocker: not-attempted; the f.96v strings went through solve.py on 2 Oct 2026 (NEXT-HAR) with no group read; Bourdeau's own retry step says to add f.97r and rerun (cobham1588/NOTES.md Escalation); next: two blind sign-by-sign passes of f.96r, f.96v and f.97r on DECODE full-size crops (6 calls + 1 reconciliation at ~$1.5), then solve.py, ~$11

## Escalation (2 Oct 2026)
- [ ] siblings: Done by Bourdeau: the glossed R8481 (f.63), R8488 (f.75), R8489 (f.78-79) and R8493 (f.89) were aligned sign by sign (cobham1588/signs.tsv), the harley287 and cobham1588 keys were merged, and R8497 (Bodley 1590) was checked and found to be a different system. Those glosses already settle one harley287 gap: ·7· is glossed "her Maties" (signs.tsv l.33, READING.md l.4), so the .7. before "ships" on f.70r is her Majesty from a period gloss of the same key and sender, 1588, not a context guess. Upgrade it from C on the next decode of our own and drop it from the open codes. Not tried: four DECODE records in the same volume that are marked Decrypted and that nobody has opened. R8491 (f.84, 1588) and R8494 (ff.90-91) could gloss K, upsilon, rho and W. R8478 (f.37-38, 1587) and R8480 (f.41-42, 1587) flank Needham's ff.39-40. R8491 and R8494 fetched full-size 2 Oct 2026 (A2-HAR, second spawn): both are glossed interlinearly in the Cobham alphabet (f.84r about 16 cipher lines, peace-treaty letter; f.90r about 13, Ostend, 14 Mar. 1587/8), with no number codes. Planned: align their glosses against cobham1588/signs.tsv, ~$8, plus ~$1 for the Needham pair R8478/R8480 (not fetched). Done 3 Oct 2026 (A2-HAR7) for R8491/R8494: aligned, 0.819 vs nulls max 0.305; confirms signs.tsv on 19/20 signs, adds only 8 = d (M); K, Q, L, upsilon, rho and W not glossed there
- [x] clear-pages: no interlinear, marginal or separate decipherment on ff.70r-72v (Bourdeau harley287/NOTES.md Escalation). The f.39r/40r runs were glossed at the time (needham1587/profile.json). The CSP Foreign 21/4 check for clear duplicates of the 5 May, 27 May and 9 June 1588 letters found none (cobham1588/NOTES.md "Clear-duplicate check", commit 95d37d2f). One residual check rides on the ff.70r-72v fetch: what DECODE's "Partially decrypted" status for R8486 (f.72r) refers to
- [ ] known-keys: Done: Bodley's R8497 key was tried and is a different alphabet. KEY-OFFICES.tsv and KEY-DESIGN.tsv have no row for this target (their only Walsingham row is bowes-walsingham-1583), and design_prior.py has not been run. Not tried: the Elizabethan English keys DECODE catalogues for 1586-88, which no one in this repo has opened (R337 SP 106/1 f.74, 1588; R330 SP 106/1 f.50, 1587; R8367 Harley 290 f.256, 1588; R1819/R3822/R3823 SP 12/193 no.54, 1586; R338/R328/R933 SP 106/1, undated; R9260-R9262 Add MS 4136, 1560-1587; keys-all-2026-09-28-merged.tsv). One of them could be Burghley's April 1588 cipher for Cobham (Cryptiana elizabeth.htm l.536). Cobham's 25 May 1588 code-word list is word-for-word (l.539) and is unlikely to give numeric codes. The Wilkes key (BL Add MS 5935) for Needham was not consulted. Done 2 Oct 2026 (A2-HAR, second spawn): R337 (TNA SP 106/1 f.74, Croft's 1588 key: different alphabet, codes 100/60/20/50 for persons) and R8367 (Harley 290 f.256, a Davison-era code list: 42 = puritanes, 60 = Parma) give no value for 42, 22, 27, the square or the f.11 groups. Planned: the remaining catalogued keys (R330, R1819/R3822/R3823, R338/R328/R933, R9260-R9262) in one login, ~$2.5, then run design_prior.py
- [x] print: no printed decipherment and no clear duplicate found. Searched: CSP Foreign vol.21 pt.3 pp.197-217 and pt.4 pp.199-212, read by us with a control name on each page (this NOTES.md, 25 Sept 2026); CSP Foreign vol.21 pt.4 March and May-June 1588 (Bourdeau); web, Cryptiana, DECODE status fields and Aymeloglu (23 and 25 Sept 2026). The vol.22 HTRC candidate page (scan 62) is unread, but vol.22 covers July-Dec 1588, after the latest letter (9 June). The print search for the Jesuit's name is a separate gap above
- [ ] key-rebuild: Done by Bourdeau: the harley287 key was built by hand from clear-text cribs; for cobham1588, solve.py (word candidate sets, CSP 1588 word list, up to 2 edits) was run with loop 1 on f.88 only (cobham1588/NOTES.md l.175-190, Escalation). Done 2 Oct 2026 (NEXT-HAR): solve.py on the third-pass f.80r-81r, f.92r 1-10 and f.96v strings with the loop-1 values and -=b: 0 of 45 unread groups read; 5+ sign groups hit at the shuffled-null rate (0.125 vs 0.114) against a known-answer control of 0.877 rank-1 clean, 0.065 at 40 % sign error, so the bottleneck is the transcription or the sign values, not the word list. Done 2 Oct 2026 (A2-HAR4): rerun with A2-HAR3's reported constraints 8 in {c,d} and chi(X) = y: 0 of 45 unread groups changed (12 contain X or 8); 5+ sign groups 0.125 vs null 0.116, control 0.898 rank-1 clean; X = y is a non-test because solve.norm folds y into i. A third value-only pass is not proposed (rule 3); the next solve.py run waits on a sign-by-sign transcription. Not tried: a joint search over all runs with tools/homophonic_anneal.py, fixing the values from signs.tsv, after the R8491/R8494 glosses. tools/data has no Elizabethan English corpus (en16_repo is Thurloe, 1650s), so one would have to be built first (rule 3 era lesson). That search needs a matched control, and any negative from it is conditional on Bourdeau's transcription (rule 2), ~$5
- [ ] image-check: this project has never seen a Harley 287 image; the folder holds no images and no transcription. Bourdeau read from DECODE full-resolution crops but kept no glyph-level transcription of ff.70r-72v, and f.96r/f.97r have none in runs.txt. Full-size DECODE access has been open to the project account since 28 Sept 2026 (ASKS 42). Planned: a two-pass sign-by-sign transcription of ff.70r-72v (~$22) and of f.96r/96v/97r (~$11), plus the line-G eye-check on f.39v (~$1.5), all from one login, with images kept in the scratchpad only Update A2-HAR6 (3 Oct 2026): R8491 f.84r and R8494 f.90r pair crops are now in images/f84r, images/f90r (the glossed leaves, not the unread ones); the unread leaves still have none. A2-HAR7 (3 Oct 2026): f.90r recut per run (images/f90r_runs), both glossed leaves transcribed in two blind passes and reconciled (gloss/gloss_pairs.tsv).
- [ ] retry: Bourdeau's word-by-word full-resolution re-reading was done once for ff.80r, 81r, 92r and 96v and up to three times for f.88. Evidence: first pass; second pass at commit a3159f02; third pass at commit dcf0b032 (reading_ff80_92_96_full.md). His Escalation line "[ ] retry: not done" is out of date for that re-read. No gate was set, so rule 3's third-attempt clause does not retire it formally, but a fourth word-by-word re-read of f.88 is not proposed. What is untried is a different instrument: a blind sign-by-sign two-pass transcription (tools/reconcile_passes.py) and a rerun of solve.py with the key extended by the sibling glosses. Planned: rerun every unread run that way once the R8491/R8494 glosses and the transcriptions are in, then regrade
Verdict: keep going: 10 internal gaps; 8 = c/d rerun and the gloss-masked f.84r control done (RUN1-HAR, 4 Oct 2026: no token changed; G1 PASS, G2 FAIL, so 8 = d and the values the masked read did not reproduce are graded M); cheapest next: a two-pass blind sign-by-sign transcription of f.88r (R8492) from DECODE full-size crops, one login, crop step pasted, scored against the gloss-confirmed core values only (#,+,7,8=c,A,D,G,H,U,z,d,y), ~$4.

## Web and blog check (GF-A2-2, 2 Oct 2026)

Worker GF-A2-2 (account 2, LANE-A2PUSH), 2 Oct 2026 21:14-21:18 UTC (clock read). WebSearch standard mode; WebFetch for opened hits.

| # | Query / page | Hits |
|---|---|---|
| 1 | `Lord Cobham Walsingham 1588 Ostend cipher letter deciphered` (sender + recipient + date) | BHO CSP Foreign Feb and Aug 1588 nodes (66430, 65383, 66436, 66438): the 1 Aug 1588 Calais letter with a Beale decipher is a State Papers item outside this volume; a Camden treatise on Calais; BL searcharchives 040-002046115 (Harley MS 287 record, opened, see row 5). No reading of the Harley 287 cipher passages. |
| 2 | `"Harley MS 287" cipher` (shelfmark + cipher) | BL searcharchives records for Harley 286/288 items (Harley 286 ff.80-87 "Walsinghams Characters or Cyphers") and the Harley 287 record; ciphermysteries.com tag pages (augusto-buonafalce, tony-gaffney/page/2, ?p=1463), all on other subjects. No reading. |
| 3 | `"in all armadas" OR "to these termes" Cobham 1588 Parma Walsingham cipher` (two distinctive decoded spans from Bourdeau's cobham1588 READING.md) | BHO nodes 66458, 94873, 65383, 66467; popular history pages. Neither phrase found. |
| 4 | `Harley 287 cipher letters 1587-88 Cobham Needham Walsingham unsolved DECODE` (folder title) | BL records; news items on the 2023 Mary Queen of Scots decipherment (Lasry, Biermann, Tomokiyo), unrelated letters. No reading. |
| 5 | WebFetch searcharchives.bl.uk/catalog/040-002046115 and its .json (the volume record) | Item list for the volume, with cipher items at f.11r, ff.37-42 (Needham, three letters), 63, 70-79, 80-81, **84 ("Part of a letter from Cobham, in cypher")**, **86r-87v ("Copy of Cobham's letter, deciphered, giving an account of Spanish naval preparations in the Low Countries")**, 88, 89, 90, 187. The ff.86-87 entry is a deciphered copy bound two leaves from f.84 and one leaf from f.88. See the Premise check below. |
| 6 | `site:scienceblogs.de klausis-krypto-kolumne Walsingham Cobham Harley 1588` (Cipherbrain) | No scienceblogs.de result returned; the hits are general Walsingham/Mary pages. Nothing on this volume. |
| 7 | `site:cryptiana.blogspot.com Walsingham Cobham Harley cipher` (Cryptiana blog) | No cryptiana.blogspot.com post returned. Tomokiyo's `elizabeth.htm` (on disk, `sources/cryptiana/web/`) was already grepped twice above and prints no decipherment. Nothing on this volume. |
| 8 | `site:ciphermysteries.com Walsingham Cobham cipher Harley 1588` (Cipher Mysteries) | No ciphermysteries.com post on this volume; general Walsingham pages only. |

Comment threads: none of the hits is a blog post about this volume, so there was no relevant comment thread to read. The three Cipher Mysteries tag pages in row 2 are about other ciphers. **Result: no decipherment or plaintext of the Harley 287 cipher passages found on the open web or in these three blogs.** The ff.86-87 catalogue entry is a lead inside the volume, not a web publication.

## Premise check (GF-A2-2, 2 Oct 2026)

- (a) **Decipherments the folder already mentions.** Found, already known: Bourdeau's `cobham1588` and `harley287` readings (read in part, key rebuilt from the glossed siblings R8481 f.63, R8488 f.75, R8489 ff.78-79 and R8493 f.89), and DECODE's "Decrypted" flag on R8491 (f.84) and R8494 (ff.90-91), which the Remaining gaps section already lists as unopened. Nothing in these goes beyond the partial status.
- (b) **Other solvers' working files.** Found, already known: shallow clones today (Bourdeau HEAD dated 2 Oct 2026 15:12 -0500; Aymeloglu HEAD). Bourdeau `targets/harley287/` (NOTES, READING, key.tsv, profile) and `targets/cobham1588/` (READING.md, reading_f88*.md, reading_f96v.md, reading_ff80_92_96_full.md, solve.py, signs.tsv) and `targets/needham1587/` have no file dated after 25 Sept 2026 and match what this folder already cites. `targets/harley1582r8499` etc. are Harley MS 1582, a different volume. Aymeloglu's repository (cited, not copied) has only the DECODE catalogue rows for this volume (`catalogue/decode-records.jsonl`: R8477, 8479, 8482-8487, 8490, 8492, 8495, 8496, with DECODE statuses), no working files or renderings.
- (c) **Physical neighbours.** **Found (a lead, not yet checked):** the BL volume record (searcharchives.bl.uk/catalog/040-002046115, fetched today) describes **ff.86r-87v as "Copy of Cobham's letter, deciphered, giving an account of Spanish naval preparations in the Low Countries"**. It sits between f.84 ("Part of a letter from Cobham, in cypher", DECODE R8491, marked Decrypted, `sources/decode/records-decrypted-2026-09-24.tsv`) and f.88 ("News from Cobham, 1588, on the Spanish preparations, written in a slightly different cipher", R8492, one of this folder's targets). ff.86-87 is not a DECODE record of its own and is not mentioned anywhere in this folder or in Bourdeau's harley287/cobham1588 files. The subject ("Spanish preparations") matches f.88's catalogue line, and f.88's reading on file (Montgomery, Scottishmen, Italians, "80 sayles ... with saddelles") is about Spanish preparations. It is unknown whether ff.86-87 deciphers f.84, f.88 or another letter. That needs the page images. BL images are unreachable from the cloud (iiif.bl.uk dead since 2023), and DECODE's full-size images are account-blocked, so the leaves were not viewed. Next step: view ff.84, 86-87 and 88, by a DECODE R8491 thumbnail/document check or a BL reproduction request. If ff.86-87 deciphers f.88 or any of R8490/R8495/R8496, that item is found-solved before more is spent on it, and it is a known-answer control for the rest.
- (d) **Recipient-side editions.** Not found: the recipient is Walsingham, whose side is CSP Foreign Elizabeth vol.21 pts 3-4, already read page by page on 25 Sept 2026 (line 2 of this file). That read was not repeated today. The Spanish/Parma side is the subject of the intelligence, not a recipient.

## Step A2-HAR (second spawn), 2 Oct 2026: one DECODE login, R8491/R8494/R337/R8367 vs codes 42, 22, 27, the square and the f.11 groups

Brief: .claude/briefs/runs/2026-10-02-acct2-a2-har.md (LANE-A2PUSH, account 2). Intake gate output, pasted before the work:

    $ python3 tools/intake_gate_check.py harley-287-1587
    harley-287-1587: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
    EXIT 0

Route. One real-browser login (`tools/decode_browser_login.js 8491 <scratchpad> --max-files 0 --listen`, `loggedIn: true`,
21:34 UTC), then 14 listener requests 1.5 s apart: RecordsView 8494, 337, 8367, DocumentsList for 337, and the full-size
images of all four records. Every full-size file came back as a real image, not the `forbidden.png` placeholder (sha1
prefixes: R8491 5b328092f5ef/4c4ad3bc8d1c, R8494 67e1d4f3eeaa/f1f2983d539f/31b5dbcc2e0f/e1206230bbc6, R337 626a80d46605,
R8367 10631647c8c7/5f9ee8f7dbd4). The images stay in the session scratchpad, not in this repository. No saved page is
committed, so no account name had to be scrubbed. DECODE documents: R8491, R8494 and R8367 list 0; R337 lists 1, but its
DocumentsList page rendered only the site-wide bibliography, and the record's own file was not retrieved. Read by eye from
downscaled whole-page views and region crops (about 12 image reads by this worker, no subagent).

What the four records are (image over catalogue, rule 2):

| record | leaf | what the image shows |
|---|---|---|
| R8491 | Harley 287 f.84r (+ f.84v endorsement) | A cipher letter in the Cobham alphabet (7 = e, ∧ = t, U = a, ǂǂ = n, ∞ = d: "U ǂǂ ∞" = "and"), glossed interlinearly in full, line by line. It concerns the 1588 peace treaty: "The answers brought us by [Norris?] after three days attendance do shew small hope of any good success in the great cause ... we must go from hence ... either to Dover or Calais and there to press them resolutely whether they will condescend to the three points propounded, which being refused her Ma[jes]tie may with honour break off and we return home"; then "the Dukes commission", "cessation of arms for the time of the treaty and twenty days after", "honourable security for our persons". The f.84v endorsement mentions the treaty of peace, the Commissioners and "my Lord Cobham" (read at grade M from a small crop). |
| R8494 | Harley 287 f.90r-91r (4 images: f.90r, f.90v blank, f.91r, f.91v blank) | f.90r is headed "... fro Ostend 14 Mar. 1587" with "E: Darby" written above, so probably from the Earl of Derby at Ostend in March 1587/8 (header grade M). It is a mixed clear/cipher letter in the same alphabet, glossed interlinearly: the dislike between the governor and captains of Ostend, the soldiers grown insolent, Lord Willoughby or one of the Council of the Low Countries to come and reform the disorders. f.91r is wholly in clear (Ostend, Bergen, the King of Spain, Richardot, Champagny, "Julio Romero, Christopher Mondragon"). |
| R337 | TNA SP 106/1 f.74 (folio "28"/"74") | A 1588 key, receiver Sir James Croft (DECODE metadata). Croft sat with Cobham on the 1588 peace commission. It has a full alphabet with nulls 2, 7, 9, 6 and abbreviation signs (at, with, for, from, to, by, and, that, they, which), and a nomenclator: number and letter codes for persons (100, 60 = E. Leycester, 20 = Sec. Walsingham, 50 = L. Cobham, then letter codes for Sir J. Croft, Dale, Willoughby, Russell, Killigrew and others), symbol codes (Pope, Holy League, K. of Spain, D. of Parma, D. of Guise, Montigny, Mondragon, Verdugo, Stanley, La Motte, Aremberg, Champagny, Richardot, ships, mariners, horsemen, footmen ...) and plain-word cover names for places (Vlissingen = Hector, Middelburg = Ajax, Ostend = Xerxes ...). |
| R8367 | Harley 290 f.256 (+ verso, "For Mr F. Dobson"?) | A one-page "Characters" list in a later-looking hand: a = K. of Spain, d = D. of Guise, 33 = Low Countries, 96 = Italy, 60 = D. of Parma, 65 = K. of Scots, 20 = the Papists, 48 = England, a sign = "Mr Secretary Davison", A = Earl of Leicester, and struck through at the foot "58 the French king", "42 puritanes", "72 the ..." (grade M from the image). Several codes have no value. |

The check the brief asked for:

- **Code 42 (f.70r, "15 will never yield to send 42 hither").** It is absent from R337, R8491 and R8494. R8367 has 42 = "puritanes",
  struck through, but that list is a different code: there 60 = the Duke of Parma and 33 = the Low Countries, while
  Cobham's glossed code has 15 = the Duke of Parma (cobham1588/signs.tsv). It names Davison as Secretary (1586-87) and
  the Queen of Scots, so it belongs to another office and another year. "Parma will never yield to send puritans hither"
  also makes no sense. No value transfers. 42 stays open.
- **Codes 22, 27 (f.80r-81r).** Absent from all four records. R337's numeric codes are round numbers (100, 60, 20, 50) in a
  different alphabet (Croft's a = ":I:", e = ∞, against Cobham's a = ∪, d = ∞, e = 7). R8491 and R8494 spell their names out
  ("the Dukes", "her Ma[jes]tie", "the Lord Willoughby") and carry no number code at all (the only digits are the clear
  "29" date on f.90r). Still open.
- **The square sign (f.80r).** No square in R337 or R8367, and none in the R8491/R8494 cipher text. The NEXT-HAR candidate
  (□ = the States, grade M) is neither confirmed nor refuted. R337 codes "States general" with a dotted P-like sign, not a
  square.
- **f.11 groups (80, wh24, ⊕, □, Nrp54).** None appears in R337 or R8367. R337's ⊙ (dotted circle) = La Motte is not the
  f.11 circled cross. No match. The f.11 code is still unidentified.
- **Matched control (rule 3).** Not applicable: this was a lookup of glossed values in period keys, not a solver, family or
  judge run, and no statistic was computed. Nothing here is a negative about the cipher. It records only that these
  four records hold no value for these codes.
- **No reading changed** (rule 7: no decode script to regenerate). Token grades: no new token read, so H 0, C 0, S 0, M 0, I 0.

What the step did settle:

1. **R8491 and R8494 are usable gloss sources** for the same alphabet. Both are interlinear-glossed throughout their
   cipher lines (f.84r about 16 cipher lines, f.90r about 13), so the planned alignment (~$8) has real material,
   including several words Cobham's own letters use. Whether they gloss the unglossed signs K, upsilon, rho and W
   is not yet known; that is the alignment's job.
2. **Bearing on the ff.86r-87v lead (GF-A2-2 Premise check (c)).** ff.86-87, the BL's "Copy of Cobham's letter, deciphered,
   giving an account of Spanish naval preparations", is **not** the decipherment of f.84. f.84 is glossed in place, and
   its subject is the peace-treaty negotiation, not Spanish naval preparations. That leaves f.88 (R8492, "News from Cobham
   ... on the Spanish preparations") as the likeliest match, but ff.86-87 is not a DECODE record and remains unviewed. The
   lead is unchanged apart from ruling out f.84.
3. **R337 (Croft's 1588 key) is a different system** from Cobham's (alphabet and code numbers both differ). It is
   not the Burghley cipher for Cobham (Cryptiana elizabeth.htm l.536) under another receiver's name. It is the key of a
   fellow commissioner, useful only if a Croft letter turns up in this volume.

Requests: de-crypt.org 1 login + 1 RecordsView (8491, in the login call) + 14 listener requests = 16, 1.5 s apart, no 403/429.
github.com: 1 sparse shallow clone of dbourdeau/cyphersolver (HEAD 2341682, 2 Oct 2026) to read harley287/key.tsv and
cobham1588/signs.tsv. No other host.

## Step A2-HAR4, 2 Oct 2026: gloss alignment (not runnable) and constrained solve.py rerun

Brief: .claude/briefs/runs/2026-10-02-acct2-a2-har4.md (LANE-A2PUSH, account 2). Intake gate output, pasted before the work:

    $ python3 tools/intake_gate_check.py harley-287-1587
    harley-287-1587: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
    EXIT 0

**Precondition missing.** The brief's Verdict line cites A2-HAR3 (session_01KLfk1EnuwELanBdc7AY5Zw, LEDGER row "done ~22:21",
cost 5.95): it reported mapping the R8491 f.84r and R8494 f.90r interlinear glosses to glyphs (grade C, f.90r single eye) and
the constraints chi = y, delta/8 in {c,d}, L = e, - = b. None of its work is on main: no NOTES.md section, no pairs or glyph
table, no ROOM done line. `git grep A2-HAR3 origin/main` finds only its brief, this brief, LEDGER.md and ROOM.md; the session
is archived with `staged_files: true` in its handoff, so its files were staged and never pushed, and its scratchpad images
are gone with the container. The four constraints above survive only as one line of its session summary.

1. **tools/interlinear_align.py: not run.** There is no (gloss, cipher) pair file to align, and none can be rebuilt from the
   repository. No shuffled-alignment control was run either: with no target run, a control would test nothing.
2. **Constrained solve.py rerun: run** (`solver/run_har4.py`, wrapping NEXT-HAR's `run_nexthar.py` unchanged; outputs
   `solver/out_har4_replace.txt` and `solver/out_har4_add.txt`, both `--check: ok`; `run_nexthar.py --check` also ok before
   the change). L = e and - = b were already in NEXT-HAR's sets, so the changes are only `8` -> {c,d} and the chi sign -> y.
   The chi sign is taken to be Bourdeau's ASCII `X` (his i, also j); that identification is ours and is not checked against
   A2-HAR3's lost table. Variants: replace (X = y) and add (X = i or y). Grade of the constraints themselves here: I (from a
   summary line, no evidence on disk), not C.

| run | unread groups (of 45) with any exact candidate | 5+ sign unread: target vs shuffled null | known-answer, 5+ signs, rank-1 at 0 / 10 / 20 % sign error |
|---|---|---|---|
| NEXT-HAR baseline | 19 | 0.125 vs 0.114 | 0.877 / 0.458 / 0.221 |
| A2-HAR4 replace (X=y, 8=c/d) | 19 | 0.125 vs 0.116 | 0.898 / 0.450 / 0.250 |
| A2-HAR4 add (X=i/y, 8=c/d) | 19 | 0.125 vs 0.116 | 0.898 / 0.452 / 0.252 |

- **The unread groups' candidate lists are identical in all three runs** (line-by-line diff of every `unread` line). 12 of
  the 45 unread groups contain X or 8 (Xd+c:87, Ac-D:XL, IXpp7#, 8-l:Vd, l7XA, w+Ap::Xcl, Al7VLAT8:, nXcH, V?XAT, -cX8L, lIX,
  wU::8T); none gained or lost an exact candidate. Read groups: three near-lists changed (lUn87A gains "landed", "lands";
  one captain-type list gains "detain"; one gains "beside", "bride"), no exact read changed.
- **chi = y is a non-test with this solver, by construction (rule 3).** `solve.norm()` folds y into i before every lookup, so
  X = i and X = y give the same keys for every string, target, null and control alike. The control could not differ from
  the target on this statistic; the identical result says nothing about the constraint. Logged untested-by-this-tool, not
  refuted.
- **delta/8 in {c,d}: no effect.** The known-answer control stays well above the target (0.898 rank-1 clean), the target's
  5+ sign groups stay at the shuffled-null rate (0.125 vs 0.116), and no unread group reads. This is the same finding as
  NEXT-HAR: the bottleneck is the transcription of the unread strings or the unglossed signs (K, upsilon, rho, W), not these
  two values. This was the second solve.py pass with only the sign values changed; under rule 3's third-attempt clause a
  third value-only pass is not proposed. The next pass needs new material: a sign-by-sign transcription.
- **No reading changed.** Token grades for this step: H 0, C 0, S 0, M 0, I 0 (no token read). No judge run (no reading).

Requests: none to any external host (offline run on vendored files). Vision calls: 0. Read-only `get_session` on A2-HAR3 to
establish why its output is missing.
Next (the cheapest step that restores the lost input): redo A2-HAR3 and push it. One DECODE login, R8491 f.84r and R8494 f.90r
full-size into the scratchpad, `tools/iiif_lines.py --image` line crops, gloss and cipher pairs written to
`ciphers/harley-287-1587/gloss_pairs.tsv` and **committed before any analysis**, then interlinear_align.py with a
shuffled-alignment control. About 5 calls at ~$1.5 (A2-HAR3 spent 5.95), ~$7.5.

## Step A2-HAR6, 3 Oct 2026: pair crops and pipeline pushed; both blind passes refused at the file write

Brief: .claude/briefs/runs/2026-10-03-acct2-a2-har6.md (LANE-A2PUSH2, account 2). Intake gate output, pasted before the work:

    $ python3 tools/intake_gate_check.py harley-287-1587
    harley-287-1587: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
    EXIT 0

Done and on origin/main (each push checked with git log origin/main):
- **Images.** One DECODE browser login (`tools/decode_browser_login.js 8491 images/decode --fetch-page RecordsView/8494
  --guess-fullsize --max-files 20`, loggedIn true). All six full-size images came back real, with the same sha1s as A2-HAR
  and A2-HAR5 (`images/decode_sha1.txt`). The 73 MB of full-size images are not committed; `images/README.md` says how to
  re-fetch them. The saved RecordsView pages were deleted before the commit, so nothing carried the account name.
- **Crops (commit 791beeec).** `images/f84r/` holds 15 gloss+cipher pair bands x 2 segments, cut with `tools/iiif_lines.py
  --centres` set by eye, because the auto profile merged lines 6-7. `images/f90r/` holds 7 auto-detected three-line bands
  x 2 segments, overlapping. The exact commands are in `images/README.md`.
- **Pipeline (commit a6442f53).** `gloss/run_align.py`'s sign table was changed from A2-HAR5's undocumented shape code to
  Bourdeau's documented code (the `solver/runs_bourdeau.txt` legend). A second, length-preserving control was added: each
  pair keeps its own gloss, with the letters shuffled. That control can differ from the target on the consistency
  statistic, because shuffling changes which letter sits over which sign.
  `gloss/known_answer.py` checks the pipeline on a known answer: 11 synthetic pairs of the same shape (the f.84r gloss
  wording, a random 28-sign key, 10% sign error). They read consistency **0.919**, against the pair-shuffled null at
  mean 0.271, max 0.309, and the letter-shuffled null at mean 0.233, max 0.246. The tool can separate a real gloss from
  both nulls at this size.
- `gloss/PASS_PROMPT.md` is the blind-pass instruction.

Not done: **`gloss_pairs.tsv` does not exist.** Two blind Sonnet passes (A and B) read every crop (44 images each) and
drafted 46 and 35 rows. In both, the session's auto-mode safety check refused the one command that would have written
the TSV, with the message that the check "could not evaluate" the action and that a retry or a reworked attempt would be
refused the same way. Neither pass tried another route. I did not re-spawn the passes or write their drafts into the
repository myself, since that would route around the refusal. So there is no reconciliation and no interlinear_align run
on real data. Both passes reported low confidence:
- On f.90r, the gloss-to-run pairing was ambiguous, because glosses sit above, below or between the cipher rows and the
  three-line bands overlap.
- On f.84r, several first signs and the s1/s2 overlap zones were unclear.

Changes to the next attempt from that report:
- Cut f.90r per cipher run (`--region` per run, gloss included), not in three-line bands.
- Run the passes in a session where the write is allowed, outside auto mode or in a fresh session as the passes
  suggested.

Token grades: no token read (H 0, C 0, S 0, M 0, I 0). No reading changed, no judge run.
Requests: de-crypt.org 1 login + 1 RecordsView (in the login call) + 13 fetches (1 RecordsView page, 12 images), 1.5 s
apart, no 403/429. No other host. Vision calls: 2 blind passes (no output kept) + about 8 single-image reads by this worker
to set crop centres.

## Step A2-HAR7, 3 Oct 2026: R8491 f.84r / R8494 f.90r gloss pairs transcribed, reconciled and aligned, with controls

Brief: .claude/briefs/runs/2026-10-03-acct2-a2-har7.md (LANE-A2PUSH2, account 2). Intake gate output, pasted before the work:

    $ python3 tools/intake_gate_check.py harley-287-1587
    harley-287-1587: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
    EXIT 0

- **f.90r recut per cipher run (commit 7a0dea80), no DECODE login.** The full-size images are not on disk in a fresh
  container. The committed f.90r band crops are native resolution and together cover the whole region, so I pasted them
  back at their manifest boxes into a page-coordinate canvas (scratchpad only). From that canvas
  `tools/iiif_lines.py --image` cut 18 runs (gloss + cipher) into 22 crops in `images/f90r_runs/`. The per-run
  `--region` values are in `regions.txt`, and the boxes in `manifest.json` are native IMG_R8494_I39202_P1.jpg
  coordinates. R18's cipher row is clipped at the bottom edge of the A2-HAR6 region (y 3650).
- **Two blind Sonnet passes (vision calls 2).** Each pass read 30 f.84r crops + 22 f.90r crops and returned its TSV as
  reply text. I wrote the replies to `gloss/passA.tsv` (af264753) and `gloss/passB.tsv` (31f555f2), unchanged.
  - Raw sign agreement is **697 / 814 = 85.6%**.
  - 41 of the 117 splits are one systematic naming split: A wrote l where B wrote p. The sign behind most of them is
    the looped, crossed-stem sign under gloss "h". On f84r L03_s1 and L07_s1 it is distinct from the phi in the cipher
    line above. Most of the rest are the true p sign, judging by the key below.
  - With that split counted as agreement, agreement is 738 / 814 = 90.7%.
- **Reconciliation (my own pass over the crops; `gloss/reconcile_gloss.py`, regenerates `gloss_pairs.tsv` with
  `--check`; commit b0ef9801, pushed before any alignment).**
  - Cipher signs: agreed tokens are kept; the l/p split goes to p; every other split becomes the wildcard ?. The result
    is 67 signs wildcarded, so no sign is settled by guess.
  - Gloss words: 18 rows where the passes differ are settled from the crops and the cipher word lengths. Example: R04
    reads "no dyuyne seruyce" on the image (2/6/7 signs), which neither pass had.
- **Alignment (`python3 gloss/run_align.py`; `--check` ok).** Controls first, both able to differ from the target on
  this statistic, because re-pairing or letter-shuffling changes which letter sits over which sign (rule 3). The
  known-answer check stands from A2-HAR6 (0.919 on synthetic pairs of this shape).

      real consistency 0.819 concordance 0.950 (20 signs n>=3)
      shuffled consistency mean 0.257 p95 0.289; concordance mean 0.097 p95 0.200
      letter-shuffled consistency mean 0.201 max 0.226; concordance mean 0.150 max 0.250
      pair-shuffled max consistency 0.305 concordance 0.250

  The real alignment beats both nulls by more than 0.5 on consistency (564 of 689 sign occurrences, n>=2, carry their
  sign's majority letter). It agrees with Bourdeau's independent cobham1588/signs.tsv values on 19 of 20 signs (n>=3).
  The one miss is a naming difference, not a value conflict: our code p reads h (35/40), and Bourdeau codes the h sign
  `h` (runs_bourdeau.txt legend: "h stem+bowl (h)"), so the passes named it with a different code letter.
- **What the glosses give (`gloss/key_f84_f90.tsv`, 22 codes).** Grade C (a period interlinear gloss), with grade M
  where the reader's sign naming may be at fault.
  - Confirmed from these two leaves: Bourdeau's polyphony for A (t 63, s 48), y (y 7, r 6), G (g 12, y 6) and
    I (i 21, e 4).
  - Also confirmed: + b, 7 e, : u, D d, H f, U a, V r, w w, z o, # n, k k.
  - One value Bourdeau does not list: 8 reads d 6 times beside c 20 (M: may be readers taking the D ∞ sign for 8 in
    "dyuyne"/"desiren").
  - l splits l 16 / p 8, so the passes' l merges Bourdeau's l and p.
  - **Not glossed here:** K, Q, L, and every sign the passes left as ? (upsilon, rho and W have no code of their own in
    the pass alphabet). So these two leaves, at this transcription, do not supply the values f.88r's unread runs need.
- Caveat: the passes read the cipher with the gloss in view, so a reader could project gloss letters into sign names.
  The 19-of-20 agreement with Bourdeau's values, made from other leaves, argues against wholesale projection, but a
  gloss-masked, cipher-only pass would be the clean test.
- Token grades: no ciphertext token of an unread leaf was read in this step (H 0, C 0, S 0, M 0, I 0). The output is a
  sign-value table at grade C from glossed leaves, which confirms existing values and adds none for the unglossed signs.
  No reading changed, so no judge was run (no spec).
- Requests: none to any host (no DECODE login; crops on disk sufficed). Vision calls: 2 blind passes + 1 reconciliation
  (this worker's own crop checks, 4 image reads).

## Interrupted (account 2 usage limit, 3 Oct 2026)

- A2-HAR8 (account 2, LANE-A2PUSH2, session_01F5vxGtQzEEETwsViBGh25G), spawned 05:30 UTC 3 Oct 2026; brief
  .claude/briefs/runs/2026-10-03-acct2-a2-har8.md (2d73ce47). No claim or done line in ROOM.md. Committed: none (no
  commit in this folder after A2-HAR7's 587ad9a2 at 05:27 UTC, checked 09:25 UTC); no orphaned pre-registration.
  Unfinished step: rerun solver/run_nexthar.py with 8 = c/d (gloss/key_f84_f90.tsv) on the f.80r-81r, f.92r and f.96v
  strings, control beside target (the Verdict line above is still this step).
- A2-HAR3 (account 2, LANE-A2PUSH, session_01KLfk1EnuwELanBdc7AY5Zw), claim 22:10 UTC 2 Oct 2026, no done line;
  LEDGER row D. Committed: none (its gloss pairs never landed, see A2-HAR4 above). Step since done by A2-HAR6/A2-HAR7
  (791beeec, a6442f53, b0ef9801, 587ad9a2); nothing left to re-run under this role.
- A2-HAR5 (account 2, LANE-A2PUSH, session_01S3oNgVLh7vdgCgtgyPVk7U), claim 23:04 UTC 2 Oct 2026, halfway 23:12, no
  done line; LEDGER row X. Committed: eb8b231bc (gloss/run_align.py, "not yet run") -- a pre-registration without its
  result at the time; the script was revised in a6442f53 (A2-HAR6) and run by A2-HAR7 (587ad9a2), so the orphan is
  resolved. Nothing left to re-run under this role.
- May still push if account 2's session resumes; check git (`git log origin/main -- <this folder>`) and ROOM.md before re-running. Recorded by CLOSEOUT-A2 (account-3 in-session worker) from git and ROOM.md only; no reading, grade, status line or key was changed.

## Step RUN1-HAR, 4 Oct 2026: 8 = c/d solver rerun, and the gloss-masked f.84r known-answer control

Brief: .claude/briefs/runs/2026-10-04-acct1-run1-wave2.md (LANE-RUN1, account 1). Intake gate, pasted before the work:

    $ python3 tools/intake_gate_check.py harley-287-1587
    harley-287-1587: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
    exit 0

**1. Solver rerun with 8 = c/d (no vision).** `solver/run_nexthar.py` gained `--set SIGN=LETTERS`. With no option the
output is unchanged (`--check` ok). `python3 solver/run_nexthar.py --set 8=cd --out solver/out_har_8cd.txt` (`--check` ok):
- No token changed. The exact candidate lists of all 109 groups are identical to `out_nexthar.txt`.
- Counts are unchanged: unread 19/45 any exact and 34/45 exact or near; read 45/64 and 63/64.
- Only three near lists change, and no rank-1:
  - `lUn87A` (read[I] "lances") gains landed/lands.
  - `8clA7In` (read[M]) gains detain.
  - unread `-cX8L` gains beside/bride. Its exact list is still empty.
- Regression check: every H token Bourdeau read keeps its exact candidates and its rank-1, so the key still reproduces
  them.
- Controls move only within noise:
  - Null: 0.307 vs 0.304.
  - Known-answer rank-1 at 0/10/20 % sign error: 0.889/0.667/0.400 vs 0.896/0.681/0.415.
  - 5+ signs, target vs null: 0.125 vs null 0.116.
- Token grades unchanged: H 0, C 0, S 0, M 0, I 0 changed.

**2. Gloss-masked, cipher-only pass of f.84r (known-answer control).** Pre-registered in `gloss/PREREG_masked.md`
(commit 8933b99a), before either pass ran.
- **Crops.** No DECODE login was needed: the committed f.84r crops are native resolution. I pasted them back at their
  manifest boxes into a page canvas (scratchpad), then:

      python3 tools/iiif_lines.py --image <scratchpad>/f84r_canvas.png --region 1950,500,4700,4600 \
        --centres 369,647,921,1218,1460,1775,1994,2290,2570,2887,3202,3490,3936,4164,4410 --lines-per-crop 1 \
        --max-width 2450 --overlap 120 --follow-slope 400 --slope-local --out images/f84r_masked --prefix f84rM
      python3 gloss/mask_f84r.py     # rows outside [peak-78, peak+36] painted white

  - The cipher centres for L06-L09 were corrected by eye: A2-HAR6's list paired gloss/cipher centres off by one there.
  - `--follow-slope` was needed because the lines drift up to 70 px across the leaf.
- **Deviation from the pre-registration.** It says L10_s2 (no cipher, gloss only) was blanked. It was not blanked
  until after the passes ran. Both readers saw L11's gloss words "proofe of the sufficiency" on that crop. Both said
  so, and both coded no cipher from it.
  - The leak touches one band (L11).
  - The sensitivity run below excludes L11. The crop is now blank.
- **Two blind Sonnet passes.**
  - Prompt: `gloss/PASS_PROMPT_masked.md`.
  - Replies are kept unchanged in `gloss/passA_masked.tsv` and `gloss/passB_masked.tsv`.
- **Mechanical reconciliation, no eye arbitration.** `gloss/reconcile_masked.py` (`--check`) writes
  `gloss_pairs_masked.tsv`. I did not arbitrate by eye because I had already read the gloss pairs.
- **err_2reader (masked) = 292 / 686 = 0.426**, against the gloss-in-view passes' 117/814 = 0.144. This is agreement
  between two runs of one model, not accuracy. Most of the gap is not sign-shape reading:
  - Pass B slipped bands from L06 to L09: its L07-L09 rows hold the next line's signs. Those four bands carry 180 of
    the 292 disagreements.
  - B wrote the two-dot sign as two tokens ": :".
  - B wrote ":" for the dot+stroke sign w, and X for the barred x G.
- **Scores.** Statistic, nulls and seeds are as in `gloss/run_align.py` (new `--pairs/--page/--suffix` options; the
  default run is unchanged, `--check` ok). f.84r only:

      gloss-in-view (gloss_pairs.tsv, f84r rows)   S_v 0.827  C_v 0.947 (19 signs n>=3)   control_f84r_view.tsv
      masked (gloss_pairs_masked.tsv)              S_m 0.672  C_m 0.875 (16 signs n>=3)   control_f84r_masked.tsv
      masked nulls: pair-shuffled max 0.257 (mean 0.232), letter-shuffled max 0.241 (mean 0.222)
      sensitivity, not pre-registered (drop B's slipped bands L06-L09 and the leaked L11): masked 0.689 vs view 0.805

- **Gate.**
  - **G1 PASS:** 0.672 > 0.257, so the masked read can read.
  - **G2 FAIL:** S_m 0.672 < S_v - 0.10 = 0.727. C_m 0.875 does clear C_v - 0.15 = 0.797. The sensitivity gap is also
    over 0.10 (0.116).
  - Per the pre-registration this shows a drop of that size, from projection or masking cost. At this err_2reader the
    two cannot be separated.
- **What the masked read reproduces (`gloss/key_f84r_masked.tsv`).** These values stand on both reads, grade C:
  - # n, + b, 7 e, 8 c, A t/s, D d, G g, H f, U a, z o, d o, y r/y.
  - The pass sign coded T by both masked readers ("crossed caret") reads h 16/19. That is the sign the gloss-in-view
    passes named p (h 35/40), so it is a naming difference, not a new value. It also costs C_m one concordance point
    against Bourdeau's T = d/t.
- **What it does not reproduce.** These drop to grade M under the pre-registered rule until a further unmasked read
  supports them:
  - **8 = d** (gloss-in-view 3-6 occurrences; masked 0 of 9, where 8 reads c 6, o 2, u 1). This supports A2-HAR7's own
    suspicion that the readers took the D ∞ sign for 8 in "dyuyne"/"desiren". So 8 = d is no longer carried into
    solver runs, and step 1's 8 = c/d run is moot: nothing changed anyway.
  - I = i (masked 5/16).
  - : = u (3/8).
  - l (masked 4/12, l/p merged).
  - w, k, X, c and V = r: the masked readers coded V mostly as y, and w as ":" (pass B), so these have n<3 under their
    own codes.
- Token grades: no ciphertext token of an unread leaf was read (H 0, C 0, S 0, M 0, I 0). No reading changed, so no
  judge was run.
- Credit: the sign code, the signs.tsv values and solve.py are D. Bourdeau's (github.com/dbourdeau/cyphersolver, code MIT,
  text CC BY 4.0).
- Work done: 0 host requests (no DECODE login); 2 Sonnet vision passes; reconciliation mechanical; my own image checks
  were limited to mask verification at half size.
- Suggestion (one line, not done): a masked pass whose prompt fixes the band count per crop and the ":"/w and T naming
  would separate projection from masking cost.

gaps_check (RUN1-HAR, 4 Oct 2026): `OK keep-going harley-287-1587: keep going: 10 internal gap(s), 5 step(s) untried`.
