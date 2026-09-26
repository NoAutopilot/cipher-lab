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
