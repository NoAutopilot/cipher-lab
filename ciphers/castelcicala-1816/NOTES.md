partial
Check-solved (LANE B5 worker bCAS, 26 Sept 2026): inherited from Bourdeau's dbourdeau/cyphersolver castelcicala1816/NOTES.md (commit fc0c9e8, 25 Sept 2026, CC BY 4.0) -- web search for a printed edition of the 1816-23 Castelcicala/Circello despatches, Treccani DBI (biography only, no cipher edition) and Tomokiyo's Cryptiana index, none found (21 Sept 2026). Re-run here, 26 Sept 2026: aaymeloglu/unsolved-ciphers catalogue snapshot (commit 2495c45, 23 Sept 2026) grepped for Castelcicala/Circello -- three DECODE records (R9586-R9588) all listed status "Non-decrypted", no decipherment recorded; Internet Archive be-api full-text search for "Castelcicala" returns only 19th-c. biographical/memoir hits (Colletta, diplomatic histories), no decipherment; OpenAlex works search "Castelcicala cipher despatches" (one hit, "Hugh Elliot at Naples 1803-1806", EHR 1889, unrelated); Semantic Scholar 429 twice (one retry per the good-citizen rule, not completed -- flagged, not blocking). Verdict: open/unsolved, consistent with Bourdeau's own finding.

```
$ python3 tools/intake_gate_check.py castelcicala-1816
castelcicala-1816: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT: 0
```

## Who and when

Sender: Fabrizio Ruffo, principe di Castelcicala, Neapolitan ambassador in London (1816) then Paris; recipient
Tommaso di Somma, Marchese di Circello (foreign minister, DECODE misreads "Ciscello"), later Cavaliere Luigi de'
Medici (1823 letters). See Bourdeau's castelcicala1816/NOTES.md for the full correspondent/date table (credited
below); reproduced here only where it bears on this session's test.

## Source and credit

Key (162 values, grades G/X/I), transcriptions and the code analysis (homophonic two-part numeric code, ~2,450
groups, local alphabetical runs, 5-digit nulls) are Bourdeau's: dbourdeau/cyphersolver, `castelcicala1816/`,
commit fc0c9e8be2d..., 25 Sept 2026, code MIT / text CC BY 4.0 (CLAUDE.md rule 8). Copied here: `key.tsv` (his
162 rows, unedited, plus 3 new rows added by this session, grade S, see below), `ciphertext.txt` (his
`transcripts/R*.txt`, all 25 main-code records, concatenated per record; groups of 5+ digits normalized to the
literal token `NULL` per his own `corpus.py` convention; R9586/R9588 excluded, different code, not attacked).
The crib is a contemporary interlinear decipherment on R9566 p.3 (1 Dec 1816, in the same busta) discussing
Decazes, the Floridas and Cuba, and on the 1823 siblings R9569/R9571/R9589 -- all found and aligned by Bourdeau,
not by this session.

## This session's test (LANE B5 bCAS, 26 Sept 2026): the "retry" step

Bourdeau's escalation log names one step not done: "hand-read the 1816 letters one at a time against the
Decazes/Florida crib themes with the extended runs" (his NOTES.md, "## Escalation", `[ ] retry`). This is that
attempt, scoped to a $4/40-minute breadth cap.

Target set: the un-glossed letters, 1816-era. 11 records dated 1816 (R9553, R9555-R9560, R9561, R9562, R9579,
R9587) plus 5 undated records profile.json places in "1816-20" (R9554, R9563, R9564, R9565, R9567) -- 16
records, 7,492 main-code groups (nulls excluded). The 4 glossed records (R9566, R9569, R9571, R9589 -- the
crib sources themselves) and the different-code R9586/R9588 are out of scope.

Method: built a concordance of every group not yet in key.tsv, ranked by frequency in the target set, and read
its immediate context (already-keyed neighbours shown, unread groups in brackets) across every occurrence in
the target set and, for cross-checking, the whole 25-record corpus including the glossed letters (script:
concordance.py / concordance_full.py, not committed -- scratch, reproducible from key.tsv + transcripts).
Proposed a value only where the same group sits in the identical short frame in >=2 independent letters (S
grade, CLAUDE.md rule 4) or is confirmed a second time inside the crib letter itself against its own glossed
value (also counted as an independent context, since it is a second occurrence of the same group in a
different sentence position from the glossed one).

### New values (3, grade S)

- **1378 = "a"** (preposition "to/at"). Four occurrences of `<verb ending in -to> 1378 V.E.` across three
  different un-glossed letters: R9559 twice ("...ca to 1378 V.E....", "...por ta to 1378 V.E....", i.e.
  "[re]cato/portato a V.E." -- "brought/conveyed to Your Excellency", a standard despatch-opening formula),
  R9567 once, and R9583 once (`...NULL 1378 V.E.`). No occurrence anywhere in the corpus contradicts this
  (1378 never appears immediately before/after another already-keyed preposition in a way that would double
  up).
- **154 = "a"** (homophone of 1378 for the same preposition; the code is documented homophonic, e.g. di =
  1112/2211, del = 2082, ere = 1836/2381). Same `X 154 V.E.` frame in three different un-glossed letters:
  R9557, R9558 (twice), R9587.
- **605 = "enza"** (homophone of the already-glossed 1606 = "enza", completing "conferenza" after the
  already-keyed stem "confer", group 2403). `confer` (2403) is followed by 605 seven times across five
  different records (R9556 x2, R9561 x2, R9566 x1, R9579 x1, R9587 x1) and by the glossed 1606 once, inside
  the crib letter R9566 itself (line "presso del Re di Fra ha avuto una confer.za col", where 1606 is the
  aligned gloss value) -- i.e. the crib letter uses BOTH codes for the same word in different sentences,
  which is the strongest form of the two-context test available here (one occurrence is the gloss itself,
  the other six are the same stem in other letters).

No group meeting the two-context bar was found among the Decazes/Florida *content* words specifically (Cuba,
Isola, Cattolica, Onis, cessione are already keyed or too rare in the un-glossed set to recur); the three new
values are function words/syllables, not new thematic vocabulary. One candidate lead not resolved at this
cap: group 2261 followed immediately by the already-keyed syllable "do" recurs 8 times across 6 different
un-glossed letters (R9554, R9556x2 as [412]/[1599] variants, R9561, R9562, R9564x2, R9567), twice in the
near-identical frame `[[1424]] [412] 2261 do Inghil` (R9554, R9561) -- a repeated bigram, but no crib word
fits both the alphabetical-run position (2261 sits between 2232=la and 2290=lan, i.e. after "la" before "lan")
and the "Inghil" (Inghilterra) collocation confidently enough to propose a value; left open, M-grade at most,
not committed to key.tsv.

### Coverage (main-code groups, nulls excluded; `tools/decode_key.py ciphers/castelcicala-1816`)

1816 un-glossed target set (16 records, 7,492 groups):
- before this session: 3,268/7,492 = 0.4362 (Bourdeau's 162 values only)
- after (+3 S values): 3,406/7,492 = 0.4546 -- **+138 tokens, +1.84 points**

Whole corpus (25 main-code records, 9,286 groups, nulls excluded):
- before: 4,342/9,286 = 0.4676; after: 4,505/9,286 = 0.4851

Grade breakdown after (whole corpus, `reading_tokens.tsv`): G 2,906, X 493, I 942, S 163, M 1, U 4,781, plus
142 null tokens excluded from the denominator above. No letter reads through; this remains a partial key, not
a reading.

### Shuffled-order control (rule 3), 3 seeds

Required by the brief; the honest result is that it is **uninformative by construction** for this metric.
`tools/decode_key.py` (like Bourdeau's own `apply.py`) is a pure per-token substitution: each group's value
depends only on the key, never on its neighbours, so the *coverage fraction* (share of groups with a value)
is mathematically identical for any re-ordering of the same multiset of groups within a record. Confirmed:
shuffling group order within each of the 16 target records, 3 seeds, gives 3,406/7,492 = 0.4546 every time --
exactly the "after" number above, not a lower one. This shows the coverage number is not an artifact of
*this session's* read (it would be the same whoever assigned these 3 values), but it cannot show whether the
resulting text reads coherently -- that is judged by eye, per the two-context rule above, not by a coverage
statistic. A control that would actually test coherence would need a language-model judge scoring the decoded
*word sequence* in original order against the same sequence shuffled; not run here (no it16-era corpus applies
to an 1816-23 Italian target per QUEUE.md's own flag, and building an 1816-Italian corpus is out of this
cap's scope -- left as the natural next step for a campaign-tier follow-up, not a breadth test).

### Files

- `ciphertext.txt` -- Bourdeau's `transcripts/R*.txt` for the 25 main-code records, concatenated, copied
  verbatim (nulls normalized per his own convention); `key.tsv` -- his 162 rows plus 3 new S-grade rows;
  `decode.json` -- job config for `tools/decode_key.py`; `reading.txt`, `reading_tokens.tsv` -- generated,
  regenerate with `python3 tools/decode_key.py ciphers/castelcicala-1816`.
- Bourdeau's own `reading_partial.txt`, `apply.py`, `solve.py`, `corpus.py`, `profile.json` are not copied
  (not needed for this test; re-clone `dbourdeau/cyphersolver` to consult them, per CLAUDE.md rule 8).

## Escalation (from Bourdeau, plus this session's line)

- [x] siblings, clear-pages, known-keys, print, key-rebuild -- Bourdeau, 21 Sept 2026 (see his NOTES.md)
- [x] retry -- this session, 26 Sept 2026: 3 new S values (+1.84 points on the 1816 un-glossed target set);
      the Decazes/Florida *content* words themselves did not yield a second confirmable group; one lead
      (2261+do, "Inghil" collocation) named above, not resolved
- [ ] R9586/R9588 (different code, values ~100-1100) -- not attempted, this session or Bourdeau's
- [ ] the 1816-19 Cifra della Segreteria di Stato codebook itself, or Circello's deciphered copies, in ASNa --
      needs physical archive access

## Remaining gaps (finish-or-blocker pass, 2 Oct 2026)
Read so far: 4,505 of 9,286 main-code groups carry a key value (48.5%, nulls excluded; G 2,906, X 493, I 942, S 163, M 1, U 4,781), from `python3 tools/decode_key.py ciphers/castelcicala-1816 --check` ("reading up to date") and reading_tokens.tsv, recounted 2 Oct 2026 00:25 UTC. That is 3,406 of 7,492 (45.5%) on the 16-record un-glossed 1816 set, and 4,505 of 10,252 (43.9%) if the 966 groups of the second code (R9586/R9588, none read) are counted. This is coverage by the key, not sense: no letter reads through, and about a third of the values are Bourdeau's unconfirmed I-grade inferences. Per record it runs from 0.200 (R9560) to 0.878 (R9571).
- Main code, recurring unkeyed groups: 272 distinct groups occurring 5 or more times, 3,251 tokens (1999 x92, 1998 x62, 2178 x57, 1462 x52, 2145 x45), including bCAS's lead "[412] 2261 do Inghil" (8 occurrences in 6 letters, left at M) - blocker: not-attempted; these are frequent and sit among keyed neighbours. Two instruments have been tried once each and neither is retired: Bourdeau's solve.py it-modern 5-gram candidate scoring did not discriminate (his profile.json), and bCAS's concordance hand-read added 3 values (section "New values"). There is no era-matched Italian corpus: tools/data has only it16 and it16dip (specs/castelcicala-1816.json judge note; QUEUE.md). tools/family_run.py has no pinned-seed two-part homophonic family, so it needs an option added (Usage 8) rather than a private script; next: build an it19 corpus of 1810-1830 Italian diplomatic and political prose the way pt18 was built (V6-PTCORP). Add a seeded, bracket-constrained option to family_run.py with the 165 key.tsv values pinned and the alphabetical-run bounds as constraints. Run its matched control first: a two-part homophonic code at N=9,286, K about 1,268, 48% pre-seeded, with its blind baseline checked for headroom (rule 3, Salviati). Then run the target, judged by word-sequence order against a shuffled sequence, ~$10
- Main code, rare unkeyed groups: 831 distinct groups occurring 1-4 times each, 1,530 tokens - blocker: open-codes; each occurs a handful of times, and half of each context is itself unread. bCAS's frequency-ranked concordance found no two-context frame for them (section "This session's test"). They stay workable once the recurring groups and the low-range groups below extend the key; next: rerun the concordance (the retry step) after any key extension, ~$3
- R9558 and R9560 (1816; coverage 0.236 and 0.200), and partly R9587 (0.286) and R9559 (0.440) - blocker: not-attempted; recounted 2 Oct 2026 from reading_tokens.tsv. 71% and 65% of R9558's and R9560's groups are below 1100 (medians 694 and 769), as are 46% of R9587's and 41% of R9559's. In the other 21 main-code records the share is 6-27% (medians about 1,710-1,900). An uncontrolled look this pass does not support a separate code here. R9558's low groups are interleaved with keyed main-code groups (its first groups read 553 2232=la 2205=ci 2352 1112=di 63 ...), and S-grade 154=a is itself a low group found in R9558. Only 27% (R9558) and 26% (R9560) of their sub-1100 tokens fall in the R9586/R9588 group set, against 22% (R9561) and 16% (R9566). The likelier reading is a low-range homophone half of the main code that is under-represented in the four glossed letters. That is untested; next: run a two-context concordance restricted to sub-1100 groups in R9558/R9559/R9560/R9587, pairing each with keyed high-range homophones in identical frames (the 154=a and 605=enza method), with a shuffled-record control that can fail differently (frame matches counted across records, not coverage), ~$2
- R9572 (busta 2337_23, 1823, DECODE "Decrypted", 1 page, cleartext and plaintext Italian, sender "Castelcicala?") and R9590 (2337_41, 12 Mar 1830, "Decrypted", "With deciphered plaintext", 3 pages) - blocker: not-attempted; R9572 sits directly after the 1823 main-code letters R9569-R9571 (2337_20-22). It is not among Bourdeau's 27 transcripts. Neither his NOTES.md nor his profile.json names it: his profile names only R9569/R9571/R9589 as sharing the code and R9590 as "another code". In the clone of dbourdeau/cyphersolver at commit 34e0fc8 (2 Oct 2026), decode/views_9532_9591.jsonl gives the metadata above. R9590 was compared only against the main code, never against the second code of R9586/R9588 (R9588 is also 1823). Either record could be a glossed crib, for the main code or for the second; next: one DECODE login (tools/decode_browser_login.js --listen) to fetch R9572's single full-size image and R9590's three, images kept in the scratchpad. Classify each one's code by value range and frequent groups against the main code and against R9586/R9588 (frequent 224, 294, 1043, 1698, 784, 319). If either matches, align its decipherment group by group for G values, ~$3
- R9586 and R9588 (second code, values mostly 100-1100, 966 groups; R9588 dated 1823), which carry faint pencil syllabic glosses - blocker: not-attempted; excluded from ciphertext.txt and never attacked by bCAS or by Bourdeau. Bourdeau's transcripts (targets/castelcicala1816/transcripts/R9586.txt and R9588.txt, commit 34e0fc8) already record 9 pencil-gloss lines, several anchored to named groups: "over 688 224 482" = "pure che"; "over 294 771 888" = "ei di san"; "over 1127 763 287 207 188 125 339 977" = "se dell ... cam bia ..."; "over 450 676" = "im... pe...". DECODE full-size images have been reachable since 28 Sept 2026 (sources/decode/NOTES.md, DECODE-OPEN: R9586 3 images at 3056x4592, R9588 2 images); next: first a disk-only alignment of the 9 transcribed gloss lines to their groups, and check whether the values recur consistently elsewhere in R9586/R9588 (~$1.5). Then a legibility pass on R9586's first page: crops cut with tools/iiif_lines.py --image from the full-size scan, two blind passes and a reconcile, to read the glosses Bourdeau marked "..." (~$5)
- 57 tokens with illegible "?" digits in Bourdeau's transcripts (R9587 20, R9559 6, R9566 6, R9554 5, R9560 4, R9564 4, R9569 4, R9563 3, R9558 2, others 1) - blocker: not-attempted; ciphertext.txt is Bourdeau's two-subagent transcription copied verbatim, and we have never compared it with the page images. The bCAS brief (.claude/briefs/runs/2026-09-26-lane-b5-castelcicala.md) said "no DECODE login, no image hosts", so under rule 2 this rests on a transcription. R9587 also carries the low-range anomaly above (46% below 1100), so the same crops test whether some of those groups are misreads; next: in the same DECODE login as the R9572 step, fetch R9587's 3 full-size images (2935x3599). Cut crops around the 20 "?" tokens and the low-range runs with tools/iiif_lines.py --image, do one blind pass and one reconcile (priced as 3 units), and regrade with decode_key.py. Keep the images out of the repo, ~$6
- The 1816-19 "Cifra della Segreteria di Stato" codebook itself, or Circello's deciphered copies (ASNa, Esteri) - blocker: needs-physical-access; it is not on DECODE. R9532-R9541 are 1859-60 consular keys, and R9549 (busta 2317, 1823, "Cifra del ... Principe di Castelcicala") is in a different code by Bourdeau's comparison (frequent groups 441, 486, 563, 1144). Those groups are also absent or single in R9586/R9588 (441 0, 1144 0, 1951 0, 486 1, 563 1; counted this pass), so R9549 is not visibly the second code either. No REQUEST.md and no ASKS.md row exists for this target (grepped 2 Oct 2026); file them only if the internal gaps above stall, next: REQUEST.md plus an ASKS.md row to ASNa (Esteri busta 2337 and the Segreteria cipher holdings) asking whether the 1816-23 codebook or decipher copies survive, ~$2

## Escalation (2 Oct 2026)
- [x] siblings: Bourdeau (21 Sept 2026) opened DECODE R9550-R9591 and R9549 (his NOTES.md Escalation; profile.json). He found the glossed 1823 letters R9569, R9571 and R9589 in this code (R9570 is unglossed), and found R9590 (1830) and the 1850s-60s telegrams (R9550-R9552, R9568, R9573-R9581) to be other codes. Residual, listed as a gap: R9572 (1823, Decrypted, 2337_23) is recorded nowhere, and no sibling was ever compared against the second code of R9586/R9588.
- [x] clear-pages: the contemporary interlinear decipherments on R9566 p.3, R9569, R9571 and R9589 were Bourdeau's crib, the source of the G grade (2,906 tokens). Residual, listed as a gap: the 9 pencil-gloss lines on R9586/R9588 are transcribed in Bourdeau's files but have never been aligned.
- [x] known-keys: Bourdeau found that DECODE R9532-R9541 (1859-60 Borbone consular keys) and R9549 (busta 2317) are different codes, and Tomokiyo's Cryptiana index has no Castelcicala entry. In KEY-CROSSMATCH.tsv, 43 rows test this ciphertext and none reaches more than 0.068 coverage. design_prior.py (KEY-DESIGN-PRIORS.tsv) puts it nearest the nomenclator family, with no same-office key on file. This pass also checked R9549's frequent groups against R9586/R9588: no match. Close-out omission, not a reading gap: there is no KEY-OFFICES.tsv row for this key.
- [x] print: Bourdeau (21 Sept 2026) searched the web, Treccani DBI and Cryptiana. bCAS (26 Sept 2026) searched the aay catalogue (R9586-R9588 listed Non-decrypted), IA be-api fts for "Castelcicala" (biography and memoir hits only) and OpenAlex (one unrelated hit); Semantic Scholar answered 429 twice. No printed decipherment was found, and QA/2026-09-26-0142.md passed the search. tools/print_check.py has not been run, because no span reads through to give phrases.
- [x] key-rebuild: Bourdeau bracketed the alphabetical runs (942 I-grade tokens) and ran solve.py it-modern 5-gram candidate scoring, which did not discriminate. bCAS's concordance (26 Sept 2026) added 3 S values (1378=a, 154=a, 605=enza). Each instrument has been run once, so neither is retired. Untried, listed as gaps: an era-matched it19 LM driving a seeded, bracket-constrained anneal, and a concordance on the low-range groups.
- [ ] image-check: we have never done one. ciphertext.txt is Bourdeau's transcription copied verbatim, and the bCAS brief barred image hosts. The plan is to crop-read the 57 "?" tokens and R9587's low-range runs on the DECODE full-size scans (reachable since 28 Sept 2026), starting with R9587's 3 images, in one login with the R9572/R9590 fetch, ~$6.
- [x] retry: bCAS (26 Sept 2026) ran Bourdeau's "[ ] retry" item, re-reading the un-glossed 1816 letters with the extended key. It added 3 values and left the 2261+do lead at M. Coverage went from 3,268 to 3,406 of 7,492 on the 1816 set and from 4,342 to 4,505 of 9,286 on the corpus. It must be rerun after any key extension or image-check correction.
Verdict: keep going: 6 internal gaps; cheapest next: disk-only alignment of the 9 pencil-gloss lines on R9586/R9588 already in Bourdeau's transcripts (commit 34e0fc8), ~$1.5
