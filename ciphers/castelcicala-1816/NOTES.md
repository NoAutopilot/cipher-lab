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

## NEXT-CAS step (2 Oct 2026): disk-only alignment of the 9 pencil-gloss lines on R9586/R9588

Brief: .claude/briefs/runs/2026-10-02-acct3-next-cas.md (the Verdict line's cheapest next step). Input: Bourdeau's
transcripts `targets/castelcicala1816/transcripts/R9586.txt` and `R9588.txt` (dbourdeau/cyphersolver, commit 34e0fc8,
1 Oct 2026, MIT/CC BY 4.0), copied verbatim to `second_code/`. **Rule 2: this rests on his transcription from the
1600px copies; no image was opened**, so every anchor below is his eye placement of a faint pencil line, and every
value is conditional on it. Outputs: `second_code/gloss_alignment.tsv` (one row per gloss line),
`second_code/gloss_align.py` and its output `second_code/gloss_align_out.txt`. No outside host was contacted.

Corpus: 969 tokens (R9586 537, R9588 432; extra-digit groups kept). Most frequent groups: 224 x28, 294 x27, 1043 x24,
1698 x21, 784 x18, 319 x18.

Result, per gloss line (detail in the TSV):
- 6 of 9 lines can be placed on groups from the transcript: 4 carry Bourdeau's explicit "over <groups>" anchor
  (pure che; se dell ... cam bia; ei di san; im... pe...), 2 can be placed positionally against the full next line
  (ba li , che non ... sol tan za; tal ... in che stato). 3 cannot be placed at all without the image (R9586 "tta con
  ... ed ella"; R9588 "... e ... al ..."; R9588 "quanto ... si ... ir").
- The glosses are syllabic, one syllable per group where the count matches: "cam bia" = 207 188, "sol tan za" =
  801 863 1016 (the last three groups of the line). This confirms Bourdeau's note that the second code is syllabic.
- Recurrence, with a control that can fail differently (rule 3: n-gram counts depend on order, so a within-record
  shuffle of the same 969 tokens can move them; 1000 shuffles, seed 1): the anchored bigram **207 188 ("cam bia")
  occurs 3 times** (R9586 x2, R9588 x1) against a shuffled mean of 0.02 (p95 0); **676 596** (676 = "pe" under the
  R9588 "im... pe..." anchor) 3 times against 0.07 (p95 1); **1043 224** 6 against 0.70 (p95 2); **1043 319** 8
  against 0.48 (p95 2). These are real sequence units, not chance. The control shows they recur; it does not show
  what they mean.
- One cross-line agreement: the two positional lines on different pages (R9586 p2 "ba li , che non", R9588 p2 "in che
  stato") both put **"che" over 1043**. One conflict: 224 sits under "che" in "pure che" (R9586 p1) but under "non" in
  "ba li , che non". A homophonic code allows two groups for "che", but one group cannot read both "che" and "non",
  so at least one of those two placements is off by a group. That is the expected failure of a transcript-only
  alignment of faint interlinear pencil, and it is why nothing here is graded above M.

Grades (rule 4): H 0, C 0, S 0, I 0, M 10: the ten single-reading proposals not in conflict (207=cam, 188=bia, 1127=se, 763=dell, 801=sol, 863=tan, 1016=za, 450=im, 676=pe, 1043=che). The other placements in the TSV (688, 224, 482, 167, 493, 294, 771, 888, 101, 319, 784) are left ungraded: conflicting, doubtful or ambiguous. Not C: the pencil's date and hand are unknown, and the placement is read from a transcription.
Nothing is added to key.tsv (key.tsv and ciphertext.txt are the main code; R9586/R9588 are a different code), so the
committed reading is unchanged and `tools/decode_key.py --check` and the judge are not triggered (rule 7). No
judge was run: there is no decoded span, only isolated syllables.

What it settles: the disk-only half of the R9586/R9588 gap is done; what is left is the image half. The anchors that
would turn M into a key are on R9586 p2 (4 of the 9 lines) and R9588 p1-p2, and the conflict on 224 and the three
unplaceable lines can only be settled from the DECODE full-size scans.

## A2-CAS step (2 Oct 2026, 20:5x UTC): intake gate before the sub-1100 concordance -- not run

The brief (.claude/briefs/runs/2026-10-02-acct2-a2-cas.md) named the Verdict's cheapest next step, the two-context
concordance on the sub-1100 groups of R9558/R9559/R9560/R9587 with a shuffled-record control. Step 2 of that brief
requires the intake gate before any deep work:

```
$ python3 tools/intake_gate_check.py castelcicala-1816
castelcicala-1816: partial (line 1) has an edition citation but no logged open-web and blog-comment check (no 'Web and blog check' heading, no paragraph naming Cipherbrain, the Cryptiana blog and Cipher Mysteries) -- run check-solved.md's 'Open web and blog comment threads' step first (CHECK-SOLVED-WEB, 28 Sept 2026: spinelli-beinecke-c1515 was read in a Cipherbrain comment thread in 2017)
EXIT 1
```

The missing step is a check-solved step (`.claude/briefs/check-solved.md`, "Open web and blog comment threads"), not part
of the concordance this brief scoped, so the concordance was not run and nothing in key.tsv, reading.txt or
ciphertext.txt changed. Order now: a check-solved worker writes the "## Web and blog check" section (Cipherbrain, the
Cryptiana blog, Cipher Mysteries comment threads for Castelcicala/Circello/Naples 1816), the gate is re-run, and only then
the concordance. Requests this step: none (disk only).

## A2-CAS step (2 Oct 2026, 21:33-21:36 UTC): two-context concordance on the sub-1100 groups of R9558/R9559/R9560/R9587

Brief: .claude/briefs/runs/2026-10-02-acct2-a2-cas.md (second spawn; the intake gate now exits 0 after GF-A2-1):

```
$ python3 tools/intake_gate_check.py castelcicala-1816
castelcicala-1816: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT 0
```

Rule 2: this is disk-only, on Bourdeau's transcription (ciphertext.txt). No image was opened, no host contacted, no
vision call. Input: 236 distinct unkeyed groups below 1100, 475 tokens, in the four records (nulls dropped; '?' groups
never match). 105 of them occur at least twice in the four records, and 120 occur in at least two records corpus-wide.
Scripts (both rerun in about 3 s): `lowrange_concordance.py` (value-level frames, i.e. the key values of keyed
neighbours) and `group_frames.py` (group-level frames: identical neighbouring groups, keyed or not). Both write a TSV
(`lowrange_concordance.tsv`, `group_frames.tsv`). Controls, all 200 shuffles, seed 1. C1 shuffles token order inside
the four target records only. C2 shuffles it inside every record. Every statistic here counts frames, so it depends on
order and the shuffles can move it (rule 3, bCAS lesson). That differs from the coverage figure bCAS's control could
not move. The known-answer check takes each of the 27 keyed groups below 1100 in the corpus, unkeys it (leave-one-out)
and asks the same rule for its value.

1. **Value-level frames (the 154=a/605=enza method, made mechanical): no power.** A frame's winning value votes for the
   unkeyed group; a candidate needs at least 2 occurrences in at least 2 records. Three settings were declared before
   running: strict (2-keyed-neighbour frames, 2 or more fills, share 0.5 or more); plus one-neighbour frames; plus
   one-neighbour frames with 3 or more fills and share 0.6 or more. Each setting gave real 0 candidates, C1 0, C2 0.
   Known-answer: 0 of 27 recovered in every setting (1, 6 and 2 wrong; the rest no candidate). The control cannot
   separate anything here, so this licenses nothing either way: a non-test at this key's density (65-91 keyed groups
   per record of 207-325), not a negative.
2. **Group-level frames: the low groups sit in repeated formulae above chance.** 31 target occurrences (30 groups)
   share an identical (L1,_,R1) group frame with a different group somewhere in the corpus. The C1 mean is 17.2 (p95 24,
   max 29; 0 of 200 shuffles reached 31). The C2 mean is 18.5 (p95 26; 2 of 200 reached it). Split by partner range
   (43 pairings): **29 partners are 1100 or above** (main-code range), against C1 16.6 (p95 26, 7 of 200 at or above
   real) and C2 18.5 (p95 27, 8 of 200). **14 partners are below 1100**, against C1 6.2 (p95 11, 2 of 200) and C2 6.0
   (p95 12, 3 of 200). Both beat the controls. So the low groups occupy the same frames as main-code groups more often
   than order-shuffled text does. That fits the low-range-homophone-half reading this gap proposed, but it does not
   exclude a mixed text. Low-low pairs in shared frames are often near-consecutive numbers: 635/636 (frame 555 _ 20,
   R9558 twice), 97/122 (154 _ 199, R9558), 370/378 (471 _ 1113, R9560/R9587), 330/534 (661 _ 2369, R9560/R9587). That
   is the local alphabetical-run pattern Bourdeau documented for the main code. The one unkeyed homophone pair seen in
   two distinct frames: **516 ~ 1684** (1535 _ 2211 in R9559 against R9556/R9565; 1132 _ 1112 in R9560 against
   R9561/R9562). The identity of the two groups is supported; their value is not.
3. **Values: none licensed.** Group-level keyed votes give 2 two-context candidates, 754 = "a" (frame 171=to _ 2049,
   paired with 154=a and 1378=a) and 784 = "pu" (frame 2017 _ 2318, paired with 1922=pu in R9565 and R9579). The same
   vote rule's known-answer check gets 1 right (154=a), 5 wrong and 21 no candidate out of 27. It fails, so the two
   candidates stay at **M** and nothing goes into key.tsv. 784 is also a frequent group in the second code (R9586/R9588,
   x18). That proves nothing either way, since the two codes overlap in range.

Grades (rule 4): H 0, C 0, S 0, I 0, M 2 (754, 784), plus one unvalued equivalence (516 ~ 1684). key.tsv, ciphertext.txt
and reading.txt are unchanged, so `tools/decode_key.py --check` and the judge are not triggered (rule 7). Requests: none.
What it settles: the sub-1100 groups are not order-random noise. They share recurring frames with main-code groups
(29 against a control mean of about 17). The frame-vote instrument cannot assign them values at this key density
(known-answer 0-1 of 27). This was the instrument's first attempt, so it is not retired (rule 3). Its output feeds the
anneal step as tied-homophone constraints rather than another concordance pass.

## A2-CAS3 step (2 Oct 2026, 22:09-22:20 UTC): DECODE R9572 and R9590 fetched and classified

Worker A2-CAS3 (account 2, LANE-A2PUSH). Intake gate re-run first: `castelcicala-1816: partial (line 1) -- edition/page or
full-text-search citation found within 6 lines`, exit 0. One DECODE login (`tools/decode_browser_login.js 9572 <scratchpad>
--fetch-page /decrypt-web/RecordsView/9590 --guess-fullsize --max-files 12 --delay 1800`, logged in first time) served
both record pages and all four full-size images (real JPEGs, not the forbidden.png placeholder): IMG_R9572_I45079_P.jpg
3038x4269 (sha1 3d13aafb94af...), IMG_R9590_I45111_P1-P3.jpg 3056x4592, 3056x4592, 2995x4020. Images kept in the
scratchpad, not committed. Record pages: R9572 "1823", sender "Marchese di Ciscello? Principe di Castelcicala?", Status
Decrypted, inline cleartext and plaintext Italian; R9590 "1830", same sender field, same flags.

**R9572 is the same despatch as the transcript this folder already uses as R9571.** The page is "N. 3871 / Parigi li 8 [?]
Sett.e 1823 / Eccellenza", signed by the Principe di Castelcicala, addressed to "Ecc.mo Sig. Cavaliere de' Medici ...
Napoli": the conclave letter (France wants Cardinal Castiglioni as Pope, the Duc de Laval blamed, no Franco-Austrian
accord on the election). Read line by line from the iiif_lines.py debug overlay of the cipher block (region
400,1150,2550,1650; profile line-cutting failed on the slanted photograph, so no line crops were used), its 11 cipher lines
and their interlinear glosses agree group for group with Bourdeau's transcripts/R9571.txt (header N. 3871, 8 Sept 1823;
same struck "Vo..."/"te", same 5-digit strings 11913 11620 11526 9210 16120 in line 7, same closing and addressee). One
possible digit difference only: line 2's last group looked like 1408 at overlay scale where R9571.txt has 1418 (=per, G,
81 occurrences; the gloss reads "per"), not settled at native resolution. Every glossed group already sits in key.tsv
(G or X, taken by Bourdeau from this very text), so R9572 adds **no new value** and is not an independent known-answer
check of the key. Whether DECODE R9571 and R9572 hold two photographs of one leaf, or R9571 holds a second copy (a
duplicate) of N. 3871, cannot be told without R9571's own image, which this login did not fetch (brief scope).

Found on the way, a corpus defect: ciphertext.txt's R9571 row carries **131 groups, but the page has 91** (Bourdeau's
own "group count: 91" note; the R9572 image ends at 2076, then "Ho l'Onore"). The 40 extra tokens after 2076
("7 5 NULL NULL 9210 NULL 1191 1162 1152 921 1612 1611 1611 171 9 3 5 2450 1 4 2232 2353 91 ...") are digits from the
"## notes" and "## pairs" sections of his transcript file parsed as groups; his own cipher/R9571.txt (clone at
commit 2341682, 2 Oct 2026) has the same tail. Not repaired here (ciphertext.txt is copied as transcribed); listed as a gap.

**R9590 (Parigi 12 marzo 1830, Castelcicala to the Principe di Cassaro, "Incaricato interinamente del Portafoglio degli
Affari Esteri", Madrid[?]) is a third code, matching neither.** pp.1 and 3 are cipher (groups about 180-2100, many
underlined), p.2 is a separate sheet headed "Traduzione della cifra del Sig.r Principe di Castelcicala in data del 12
marzo 1830" (the full plaintext: "In pronta replica al comando riservato che mi ha dato nella sua del 2 marzo sulla
denunzia contro il padre e figlio Viale ..."; Tangier, the French consulate). Classification on p.1 lines 1-8 (90 groups,
read once by eye from a 1500 px preview, grade M transcription: r9590/p1_lines1-8.txt; `python3 r9590/classify.py`),
with 200 random 90-group windows of each known code as the control (all three statistics depend on the group values, so
a window can score like or unlike the target):

| statistic | main-code windows mean (p05-p95) | second-code windows mean (p05-p95) | R9590 p1 |
|---|---|---|---|
| share of groups with a main key.tsv value | 0.484 (0.256-0.656) | 0.065 (0.033-0.100) | 0.033 |
| hits on main code's 20 most frequent groups | 19.2 (9-29) | 0.0 (0-0) | 0 |
| hits on R9586/R9588's 20 most frequent groups | 0.38 (0-2) | 27.4 (22-32) | 1 |

R9590 sits below the main code's p05 on both main statistics and far below the second code's p05 on the second; it is in
neither code, which agrees with Bourdeau's "another code". Per the brief (align only if it matches) no alignment was run:
its Traduzione is a full clear text for a third, 1830 code, outside this target's 1816-23 letters. One-line suggestion:
R9590 pp.1/3 with p.2 is a self-contained known-plaintext key-recovery item for the 1830 Paris legation code (about 350
groups plus a full translation), worth its own spec if any other 1830s Castelcicala letter in busta 2337 shares it.

Requests: de-crypt.org 1 login + 2 record pages + 8 files (4 thumbnails, 4 full-size), 1.8 s apart; github.com 1 shallow
sparse clone of dbourdeau/cyphersolver. Vision reads: 7 (by the worker itself, no subagents: 3 page previews, 1 overlay,
1 header crop, 2 more page previews). No values entered key.tsv; decode_key.py --check not re-run (nothing changed).

## A2-CAS4 step (2 Oct 2026, 22:27-22:45 UTC): the R9571 row's 40 note-derived tokens dropped, logged

Worker A2-CAS4 (account 2, LANE-A2PUSH). Intake gate re-run first:

```
$ python3 tools/intake_gate_check.py castelcicala-1816
castelcicala-1816: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT 0
```

Correction (rule 2, never silently repaired): ciphertext.txt's R9571 L01 row had 131 groups; positions 92-131 (40 tokens,
"7 5 NULL NULL 9210 NULL 1191 ... 1611 1611 171 NULL") follow 2076, the leaf's last cipher group, and are digits from the
"## notes"/"## pairs" sections of Bourdeau's transcripts/R9571.txt. The row now holds positions 1-91 only (his own "group
count: 91"; the R9572 image of the same despatch N. 3871 ends at 2076 then "Ho l'Onore", A2-CAS3 above). The original
131-group row is kept verbatim as a comment line directly above the corrected row, and the drop is logged in
`corrections.tsv` (date, worker, positions, the 40 tokens, reason, evidence). No other row was touched and no group value
changed; the possible 1408/1418 digit at line 2's end (A2-CAS3) is not settled here and stays as transcribed.

The 40 dropped tokens: 4 nulls, 36 groups, of which 24 carried a key value (G 17, I 5, X 2) and 12 did not (U).
`python3 tools/decode_key.py ciphers/castelcicala-1816` regenerated reading.txt and reading_tokens.tsv; `--check` then:

```
ciphertext.txt: tokens 9388: G 2889, I 937, M 1, S 163, U 4769, X 491, null 138
reading up to date
```

(before: tokens 9428: G 2906, I 942, M 1, S 163, U 4781, X 493, null 142). Recount, nulls excluded: 4,481 of 9,250 main-code
groups carry a key value (48.4%; was 4,505 of 9,286, 48.5%). R9571 is now 84 of 87 (0.966; was 108 of 123, 0.878). The
16-record 1816 set is unchanged (3,406 of 7,492, 45.5%); with the second code's 966 groups, 4,481 of 10,216 (43.9%). The
correction removes duplicated glossed groups from the corpus, so it lowers the keyed count; it reads nothing more. Grades
per token (rule 4) are those in the --check line above: H 0, C 0, S 163, M 1, I 937, the rest G/X (Bourdeau's) or U. No
reading changed in sense, so no judge line (specs/castelcicala-1816.json's judge block records "No judge run": no
era-matched Italian corpus). The spec's `cheap_test_done` text still quotes the 9,286-group figures as the 26 Sept 2026
measurement; left as the record of that run, not edited.

Requests: none (disk only). Vision calls: 0.

## A2-CAS5 step (2 Oct 2026, 22:46-23:0x UTC): pencil-gloss legibility pass on the R9586/R9588 scans

Worker A2-CAS5 (account 2, LANE-A2PUSH). Intake gate re-run first: `castelcicala-1816: partial (line 1) -- edition/page or
full-text-search citation found within 6 lines`, exit 0. One DECODE login (`tools/decode_browser_login.js 9586 <scratchpad>
--fetch-page /decrypt-web/RecordsView/9588 --guess-fullsize --max-files 14 --delay 1800`) served both record pages and all
five full-size images, real JPEGs (not the forbidden.png placeholder): IMG_R9586_I45099_P1-P3 3056x4592 (sha1 940803e5b06a,
7665fc2325c4, 9eb6aab54ae1), IMG_R9588_I45107_P1 3056x4592 (cef33e2577e1), P2 3029x4021 (07144d694404). Images and crops
kept in the session scratchpad, not committed. **Rule 2 now holds for these anchors: they are read from the page image.**

Method (Usage 6): 12 crops cut with `tools/iiif_lines.py --image <scan> --region ... --centres ... --lines-per-crop N
--max-width 1500` (the ink profile found 0 lines on the slanted photographs, so centres were given by eye), 6 strips x 2
segments: R9586 p2 (the "se dell", "ba li", "tta con" and "ei di san" lines), R9588 p1 (the "...al...", "quanto" and "im pe"
lines), R9588 p2 ("tal in che stato"). Two blind Sonnet passes (A forwards, B backwards; neither saw the transcript), then
my reconcile against the crops at native resolution, plus one extra crop of R9586 p1's "pure che" line (needed to settle
224). Output: `second_code/gloss_image_anchors.tsv` (one row per glossed cipher line, one gloss item per group).

What the image settles:
- **The pencil sits above the cipher line it glosses**, roughly centred on each group. On R9588 p2 the "tal in che stato"
  line lies over line 8 (867 456 224 818 ...), not line 7 as the transcript-only alignment assumed.
- **"ba li , che non effett in o la sol tan za" is one item per group over 167 493 1043 224 581 326 456 596 1698 801 863
  1016**, 12 for 12 (all three readers; the comma is a pencil mark over 1043). The transcript-only alignment had "che" on
  1043 and "non" on 224; the image puts **"," on 1043 and "che" on 224**.
- **224 = che is consistent**: R9586 p1 "pur che" puts "che" squarely over 224 too (reconcile crop). The 224 conflict in
  NEXT-CAS is resolved, and the old 1043=che "cross-line agreement" was an artefact of placing both lines one group off.
  The bigram 1043 224 (6 occurrences against a shuffled mean of 0.68, p95 2; gloss_align_out_cas5.txt) reads ", che".
- **"se dell cam bia an cut ver" sits over 763 287 207 188 125 339 977**; 1127 carries only a pencil overbar (all three
  readers; x-extents measured at native size). So NEXT-CAS's 1127=se and 763=dell were each one group off: 763=se, 287=dell.
- **New conflict: 287** reads "dell" here, but the first pencil item of the next line, read "tta"/"?ake" (first letter
  uncertain), sits over 287 at the start of 287 1952 784 .... One of the two is wrong or 287 is not a single syllable; both
  stay ungraded.
- Lower-confidence lines (readers split, conf L in the TSV): "tta con si ri chi ed ella" over 287 1952 784 723 225 324/353;
  "ei di san" (reconciler 294 771 888 allowing for the pencil's left drift, pass B 331 294 771 by literal overlap); R9588 p1
  "de ol ale" over 710 609 154 and "quan to sp ir ir" over 692 499 807 468 473 (both faint); R9588 p2 "tal in che stato"
  (reconciler 867 456 224 818; pass B straddling one half-group right; pass A one group right). Two faint items at line
  starts on R9588 p1 ("?ul" over 840, "vk/ot" over 934) are illegible to all readers.
- "im pe" on R9588 p1 confirmed over 450 676 (second item "pe" or "pu"/"fu").

Control (rule 3; the control can differ from the target because cross-line agreement depends on where each line is
placed): `second_code/gloss_shift_check.py` shifts every line's gloss by k = -2..+2 groups in all combinations and counts
group->gloss agreements across lines and conflicts. H/M lines only (4 lines, 625 combinations): image placement 1
agreement (224=che, two lines), 0 conflicts; shifted mean 0.04 agreements, 0.36 conflicts; 25 of 625 (0.040) do as well.
All 9 lines (incl. L): image 2 agreements (224=che x3, 456=in x2), 1 conflict (287); shifted mean 0.14 and 3.86; 0.0072 do
as well. A small-N result: it says the image placement is more self-consistent than shifted ones, not that the glosses
are correct.

Grades (rule 4), second code only, all M (the pencil's hand and date are unknown; graded as NEXT-CAS did): **M 21** --
763=se, 207=cam, 188=bia, 125=an, 339=cut, 977=ver, 167=ba, 493=li, 1043=",", 224=che, 581=non, 326=effett, 456=in,
596=o, 1698=la, 801=sol, 863=tan, 1016=za, 450=im, 676=pe, 688=pur ('pur' sits between 688 and 224, the weakest of the 21).
H 0, C 0, S 0, I 0. Ungraded: 287 (conflict) and every L-line placement. Withdrawn from NEXT-CAS's ten M values: 1127=se,
763=dell, 1043=che (each one group off). Unchanged: 207, 188, 801, 863, 1016, 450, 676. Nothing goes into key.tsv (main code)
and ciphertext.txt is untouched, so `tools/decode_key.py --check` and the judge are not triggered (rule 7); no decoded
span exists for a judge. The transcripts R9586.txt/R9588.txt stay verbatim (Bourdeau's); the image reading lives in
gloss_image_anchors.tsv. gloss_align.py rerun on the corrected anchors: gloss_align_out_cas5.txt (207 188 x3, 676 596 x3,
1043 224 x6, all far above their shuffled p95; the 1-occurrence anchors 167 493, 581 326, 801 863 1016 cannot recur).
Reads: 2 blind Sonnet passes + 1 reconcile. Requests: de-crypt.org 1 login + 7 fetches (2 pages, 5 images, thumbnails
auto-discovered), 1.8 s apart. Nothing to verify outward (isolated syllables, no reading).

## A2-CAS6 step (2 Oct 2026, 23:04-23:2x UTC): R9587 image check (the 20 "?" tokens and the low-range runs)

Worker A2-CAS6 (account 2, LANE-A2PUSH). Intake gate re-run first:

```
$ python3 tools/intake_gate_check.py castelcicala-1816
castelcicala-1816: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT 0
```

One DECODE login (`tools/decode_browser_login.js 9587 <scratchpad> --guess-fullsize --max-files 8 --delay 1800`) served the
record page and three full-size images, real JPEGs: IMG_R9587_I45103_P1 2935x3599 (sha1 156bdb616cdd), P2 2970x3597
(23d37d684e87), P3 3056x4592 (33982cbce447, the address cover). Kept in the session scratchpad, not committed. P2 is the
letter's first page ("Eccellenza"), P1 its last (signature, "Parigi 23. Ott.e 1816"); ciphertext.txt runs P1 then P2, as
Bourdeau's transcript does. **Rule 2 now holds for R9587's crops below: they are read from the page image.**

Method (Usage 6): 30 line crops cut with `tools/iiif_lines.py --image <scan> --region ... --centres ... --lines-per-crop 1
--max-width 1400 --overlap 200` (centres by eye, checked on the --debug overlay): P1 lines 1-3, P2 lines 1-4 (the damaged
block holding 17 of the 20 "?"), P2 lines 5-7 (the densest low-range run) and P2 line 8. One blind Sonnet pass (no transcript
shown), then my reconcile against the native crops. Result per token: `r9587/image_check.tsv`.

What the image settles:
- **The low-range groups are real ink, not misreads.** On the clear lines (P2 L5-L8, 47 transcript groups) the blind pass
  matches the transcript on 45 groups exactly. The two differences are reader slips settled from the crop: 965 (blind "065",
  with 965 as its alternative) and 2205 (blind "7205"; the first glyph is the same 2 as in 2201 next to it). The blind pass's
  extra "8" after 154 is part of the mirrored "Ho l'onore" offset under the line. Every low value on those lines (65 713 49
  536 88 965 581 471 378 87 567 436 34 154 174 781 63 332 351 480 800 207 769 9) is confirmed as written. So R9587's
  46%-below-1100 profile is a property of the letter, not of the transcription, and the low-range gap stays a code question.
- **The "?" block is a cancelled and offset-damaged passage, not a resolution problem.** P2 lines 1-4 carry groups the
  writer crossed through or overwrote (both readers: line 2 opens with several struck groups, 55 and 57-58 are struck), plus
  the mirrored offset of P1's lines. The photograph is out of focus there at native size. Of the 20 "?" tokens, 4 get a
  two-reader image reading, graded M and **proposed, not applied**: 66 ?818 -> 818, 67 ?13 -> 713 (possibly itself cancelled),
  80 ?800 -> 800, 134 291? -> 291 (the last mark is a line-end flourish). 16 stay open. 11 (177?) runs off the curled right
  edge of the photograph. For 68, 22?? is 2211 (=di, G) or 2214, and the overwrite decides it. 70/71 may be one group or two.
  The rest split between the readers.
- **None of the four proposed readings is in key.tsv** (291, 800, 818 and 713 are all unkeyed). Applying them would turn 4
  "?" tokens into U tokens and change no value, so ciphertext.txt is left as transcribed (no repair, rule 2), and
  `tools/decode_key.py --check` is not triggered. Coverage is unchanged: 4,481 of 9,250.
- Found on the way, logged and not repaired: Bourdeau's transcript has **6 bare "?" groups** at the start of P2 lines 1-2
  ("? ? 2369 ...", "? ? ?425 ?549 ? ? 2287 ...") that ciphertext.txt's R9587 row does not carry (218 groups against his
  224). The image puts struck or overwritten groups at those places, so dropping them is probably right, but it was never
  logged. Recorded here; corrections.tsv is unchanged because ciphertext.txt was not edited.

Grades (rule 4), transcription only: M 4 (the proposed four), open 16. No H, C or S reading. No reading changed, so there
is no judge line. The judge block of specs/castelcicala-1816.json records "No judge run" because no era-matched Italian
corpus exists. Controls (rule 3): no solver, family or gate ran, only a transcription comparison. The clear-line agreement
(45 of 47) is the reader's reference rate for the damaged lines, where the two readers split on 16 of 20 "?" tokens. Reads:
1 blind Sonnet pass + 1 reconcile. Requests: de-crypt.org 1 login + 1 record page + 6 files (3 thumbnails, 3 full-size),
1.8 s apart; github.com 1 sparse clone of dbourdeau/cyphersolver (transcripts only). Nothing to verify outward.

## A2-CAS7 step (2 Oct 2026, 23:25-23:3x UTC): it19 corpus built (the Verdict's cheapest next step)

Built `tools/data/it19` by the V6-PTCORP method (tools/data/pt18): five archive.org `_djvu.txt` OCR files, five works
by four authors of about 1800-1830 -- Botta, *Storia d'Italia dal 1789 al 1814* t. I (1824); Colletta, *Storia del reame
di Napoli* (written 1820s); Cuoco, *Saggio storico* (1806); Foscolo, *Epistolario* vols 1 and 3 (vol. 3 is his London
letters of 1816-27). `build.py` keeps Italian-prose chunks and caps each file at 650k folded letters: 3,001,304 letters,
largest source 21.7%. Wired into `tools/judge_plaintext.py` LANG_CORPORA as `it19`. Offline test
`tools/tests/test_judge_plaintext_lang_it19.py` (held-out Botta t. IV passage passes; shuffled and random fail): ok.
Nothing from this target or its correspondents is in the corpus.

Calibration (rule 3 fold-count paragraph; `tools/data/it19/holdout_check.py`, `era_check.py`; 200 windows per fold):

| N | it19 leave-one-file-out | per-fold spread | it19 prose under 16th-c. `it` | spread |
|---|---|---|---|---|
| 300 | 23.2% | 12.0-42.5% | 21.1% | 13.5-28.5% |
| 1000 | 29.6% | 9.5-65.5% | 58.3% | 41.5-80.5% |

The control can differ from the target here: the same windows are scored under two different models. At N=1000 it19
halves the false-negative rate of the mismatched corpus; at N=300 there is no gain. One fold (Foscolo vol. 3) is the
outlier at 65.5%. By rule 3, five files with that spread make a judge FAIL/PASS against it19 of unknown reliability; it
is a better-matched LM for the anneal, and any gate result must carry the spread. No reading changed (decode_key.py not
re-run; key.tsv untouched). Requests: archive.org 11 (4 advancedsearch, 1 metadata, 6 downloads), 2 s apart. The next
step the Verdict named (a family_run.py seeded two-part homophonic option and its matched control, ~$10) is over this
brief's $4 cap and was not started.

## A2-CAS8 step (2 Oct 2026, 23:44-23:5x UTC): seeded two-part code family + matched control -- CONTROL BELOW GATE

The Verdict's cheapest next step. Added `tools/families/seeded_code.py` to `tools/family_run.py` (Usage 8; offline test
`tools/tests/test_seeded_code.py`; SYSTEM.md row). Design: one codebook entry (whole word or syllable) per group type,
homophones, code numbers alphabetical only inside short runs with the runs shuffled; the target's key.tsv values pinned
(`--param pins=`); an unpinned group whose nearest pinned neighbours within 8 numbers are in alphabetical order may only
take an entry between them; annealed under an it19 letter 4-gram model plus an entry-frequency prior. The control is cut
from it19 at the target's N=9,388 tokens (NULL and "?" tokens included, as in ciphertext.txt) and K=1,269 codes, with
types pinned (weight count^2) until the pinned token share equals the target's own 0.492. Recovery = token accuracy on
unpinned positions only. Matching checks printed per seed: control pinned types 209-219 against the target's 166 (the
control's frequent entries carry more homophones); share of pinned pairs within 8 numbers in alphabetical order 0.81-0.87
against the target's 0.81 (n=93), so run=6 matches the target's run structure.

Can the control differ from the target on this statistic? Yes: token accuracy depends on which entry each type gets, which
the order of tokens and the pins drive (not a per-token coverage figure, the bCAS non-test). Rows in HYPOTHESES.md:

| run | seeds | recovery (unpinned tokens) |
|---|---|---|
| matched control, 49.2% pinned, 4 restarts x 300k moves | 1-3 | **0.070** (0.052-0.100) -- gate 0.6: CONTROL BELOW GATE, target not run (exit 3) |
| blind baseline, pinshare=0 (headroom check) | 1 | 0.028 |

Headroom exists (blind 0.028, far below ceiling), and the pins add about 4 points, which is not a reading. Scratch
diagnostics (scratchpad, not logged as rows): with 90% of tokens pinned the same solver still reads only 0.035-0.044 of
the remaining rare types, and a uniform-proposal first version read the same, so the limit is the instrument (a letter
4-gram over one-entry-per-type cannot tell one syllable from another for a group seen 1-4 times), not the seed share. By
rule 3 this licenses nothing about the target: no target decode was produced, key.tsv and the reading are untouched
(decode_key.py not re-run). This is the first attempt with this instrument; it is not retired, but repeating it with more
moves or another bracket width would be tuning the same knob (rule 3, third-attempt clause). A genuinely different
instrument would score whole entries in sequence (an entry-bigram model over the segmented it19 corpus, so "confer" is
followed by "enza") rather than letters. Vision calls 0; network requests 0.

## A2-CAS9 step (3 Oct 2026, 00:02-00:1x UTC): entry-bigram scorer for seeded_code + matched control -- CONTROL BELOW GATE

The Verdict's cheapest next step, and the second instrument tried in this family. Added `--param lm=entry` to
`tools/families/seeded_code.py`: whole entries are scored in sequence by an interpolated Witten-Bell entry-bigram model
over the same segmented it19 corpus (nulls skipped as context; the frequency prior is off because the bigram carries
the unigram), and half the proposals for a type are drawn from the corpus followers of the entry before one of its
occurrences, kept only inside the type's bracket. Offline test extended (`tools/tests/test_seeded_code.py` case 4: pins
kept; on the toy control lm=entry reads 0.83 where the letter model reads 0.42). Everything else is A2-CAS8's run: same
token file (`families/cipher_tokens.txt`, N=9,388, K=1,269), same control generator and seeds, 49.2% pinned (209-219
control pinned types against the target's 166), run=6, bracket=8 (in-order pinned pairs 0.81-0.87 against the
target's 0.81), 4 restarts x 300k moves, words=1000. Command:
`python3 tools/family_run.py specs/castelcicala-1816.json --family seeded_code --cipher ciphers/castelcicala-1816/families/cipher_tokens.txt --tokens space --corpus tools/data/it19 --seeds 3 --restarts 4 --gate 0.6 --param pins=ciphers/castelcicala-1816/key.tsv --param iters=300000 --param words=1000 --param lm=entry`.

The control can differ from the target on this statistic (same reasoning as A2-CAS8: token accuracy depends on which
entry each type gets, driven by token order and pins). Rows in HYPOTHESES.md:

| run | seeds | recovery (unpinned tokens) |
|---|---|---|
| matched control, lm=entry, 49.2% pinned | 1-3 | **0.230** (0.205, 0.234, 0.251) -- gate 0.6: CONTROL BELOW GATE, target not run (exit 3) |
| blind baseline, lm=entry, pinshare=0 | 1 | 0.038 |
| (A2-CAS8, for comparison) matched control, letter 4-gram | 1-3 | 0.070 (0.052-0.100); blind 0.028 |

The entry-bigram scorer more than triples the letter model's control reading, and the pins now add about 19 points over
blind instead of 4, so the numbers moved toward the gate together. It still reads less than half the gate, and by rule 3
a control below its gate licenses nothing: no target decode was produced, key.tsv and the reading are untouched
(decode_key.py not re-run). One observation, not a test: the blind decode scored better under the model (-4.07 per entry)
than the pinned control decodes (-4.30 to -4.35), so at this N the bigram rewards chains of common entries that the truth
does not follow; a stronger model of the same kind would have to fix that, not more moves. Per this job's brief, this is
the second attempt with this tool and the control failed again: the seeded_code family on this target is logged
**untested-by-this-tool** (HYPOTHESES.md), and rule 3's third-attempt clause applies to any further tuning of it (a
trigram order, more iterations, another bracket width). Only a genuinely different instrument or new material reopens
it. Vision calls 0; network requests 0.

## Remaining gaps (finish-or-blocker pass, 2 Oct 2026)
Read so far: 4,481 of 9,250 main-code groups carry a key value (48.4%, nulls excluded; G 2,889, X 491, I 937, S 163, M 1, U 4,769), from `python3 tools/decode_key.py ciphers/castelcicala-1816 --check` ("reading up to date") and reading_tokens.tsv, recounted 2 Oct 2026 22:4x UTC after the A2-CAS4 correction (R9571 row cut from 131 to its 91 groups; was 4,505 of 9,286). That is 3,406 of 7,492 (45.5%) on the 16-record un-glossed 1816 set, and 4,481 of 10,216 (43.9%) if the 966 groups of the second code (R9586/R9588, none read) are counted. This is coverage by the key, not sense: no letter reads through, and about a third of the values are Bourdeau's unconfirmed I-grade inferences. Per record it runs from 0.200 (R9560) to 0.966 (R9571).
- Main code, recurring unkeyed groups: 272 distinct groups occurring 5 or more times, 3,251 tokens (1999 x92, 1998 x62, 2178 x57, 1462 x52, 2145 x45), including bCAS's lead "[412] 2261 do Inghil" (8 occurrences in 6 letters, left at M) - blocker: not-attempted; these are frequent and sit among keyed neighbours. Two instruments have been tried once each and neither is retired: Bourdeau's solve.py it-modern 5-gram candidate scoring did not discriminate (his profile.json), and bCAS's concordance hand-read added 3 values (section "New values"). The era-matched Italian corpus now exists: tools/data/it19 (A2-CAS7, 2 Oct 2026, section below; 3.0M letters, 5 files; leave-one-file-out false negatives 29.6% at N=1000, per-fold spread 9.5-65.5%, so a FAIL/PASS against it is of unknown reliability by rule 3, but it halves the 58.3% the 16th-c. `it` corpus gives period prose). The seeded, bracket-constrained option now exists (`family_run.py --family seeded_code`, A2-CAS8, 2 Oct 2026, section above) and its matched control read 0.070 (0.052-0.100, 3 seeds) of unpinned tokens against a 0.6 gate, blind 0.028: CONTROL BELOW GATE, target not run, nothing licensed. The letter-4-gram instrument cannot place rare syllable types even at 90% pinned. Its second instrument, an entry-bigram scorer (`--param lm=entry`, A2-CAS9, 3 Oct 2026, section above), read 0.230 (0.205-0.251) on the same matched control against the 0.6 gate, blind 0.038: CONTROL BELOW GATE again, target not run. The seeded_code family is untested-by-this-tool on this target; a further tuning of it falls under rule 3's third-attempt clause; next: new material, the recipient-side clear-text extracts of 1816-17 Castelcicala-Circello letters in BL Add MS 41525 f.38 (Premise check (d)), which would be a grade-C crib for the un-glossed 1816 set if one matches a despatch. BL images are not reachable from the cloud, so the step is an ASKS.md row plus a LOCAL-QUEUE.tsv/owner-side copy request for f.38, ~$2
- Main code, rare unkeyed groups: 831 distinct groups occurring 1-4 times each, 1,530 tokens - blocker: open-codes; each occurs a handful of times, and half of each context is itself unread. bCAS's frequency-ranked concordance found no two-context frame for them (section "This session's test"). They stay workable once the recurring groups and the low-range groups below extend the key; next: rerun the concordance (the retry step) after any key extension, ~$3
- R9558 and R9560 (1816; coverage 0.236 and 0.200), and partly R9587 (0.286) and R9559 (0.440) - blocker: open-codes; 71% and 65% of R9558's and R9560's groups are below 1100 (46% R9587, 41% R9559; 6-27% elsewhere). The two-context concordance ran (A2-CAS, 2 Oct 2026, section above; group_frames.py, lowrange_concordance.py). The low groups share identical group frames with main-code groups above a shuffled-record control: 31 occurrences against a mean of 17.2 (p95 24); 29 of the 43 pairings are with partners of 1100 or above, against 16.6 (p95 26). That fits a low-range homophone half of the main code. Neither frame-vote rule assigns values, though: known-answer 0-1 of 27, so 754=a and 784=pu stay M and 516~1684 is an unvalued pair. Next: carry the frame pairs (516~1684, 635/636, 97/122, 370/378, 330/534) and the M candidates as tied-homophone constraints into a seeded anneal of the recurring-groups gap once a control for it clears its gate (neither seeded_code instrument did: letter 4-gram 0.070, entry-bigram 0.230, against 0.6, A2-CAS8/A2-CAS9; the family is untested-by-this-tool, so this needs a different instrument or the f.38 crib first), ~$6 (shared with the recurring-groups gap)
- R9586 and R9588 (second code, values mostly 100-1100, 966 groups; R9588 dated 1823), which carry faint pencil syllabic glosses - blocker: open-codes; excluded from ciphertext.txt and never attacked by Bourdeau. The disk-only alignment (NEXT-CAS) and the image legibility pass (A2-CAS5, 2 Oct 2026, section above; second_code/gloss_image_anchors.tsv) are done: 21 values at M (pencil above its group, 3 readers), 224=che settled across two lines, 1043=","; 287 conflicts (dell / ?tta); no further pencil lines were seen on the four page overviews read (R9586 p1-p2, R9588 p1-p2; R9586 p3 not viewed), so 945 of 966 groups stay unvalued and no span reads through. The second code is a syllabary of roughly 1,000 groups with 21 known; next: a seeded syllabic anneal of R9586+R9588 with the 21 M values pinned (the seeded_code family is untested-by-this-tool after both its letter-4-gram and entry-bigram controls failed at 49% pinned, A2-CAS8/A2-CAS9, so a 2%-pinned syllabary needs a different instrument first), its matched control a ~970-token syllabic code with 2% seeded, checked first for headroom (rule 3), ~$10
- 57 tokens with illegible "?" digits in Bourdeau's transcripts (R9587 20, R9559 6, R9566 6, R9554 5, R9560 4, R9564 4, R9569 4, R9563 3, R9558 2, others 1) - blocker: not-attempted (for the 37 outside R9587; R9587's 16 open ones are illegible on this photograph); ciphertext.txt is Bourdeau's transcription copied verbatim. The R9587 image check is done (A2-CAS6, 2 Oct 2026, section above; r9587/image_check.tsv). Its 20 "?" sit in a passage the writer cancelled and overwrote, under the offset of the facing page, on an out-of-focus photograph. Two readers give 4 an M reading (818, 713, 800, 291), all unkeyed, proposed and not applied. 16 stay open, and 11 (177?) runs off the photograph's curled edge. R9587's low-range groups are confirmed as written: the blind pass matches 45 of 47 clear-line groups. R9572's 1408/1418 digit was not in scope (R9572 was not refetched). The other 37 "?" (R9559, R9566, R9554 and others) have never been compared with an image. R9587's yield (0 keyed values) says that pass is low value until the key grows; next: the same crop pass on R9559+R9566+R9554 (17 tokens) after any key extension, ~$5
- The 1816-19 "Cifra della Segreteria di Stato" codebook itself, or Circello's deciphered copies (ASNa, Esteri) - blocker: needs-physical-access; it is not on DECODE. R9532-R9541 are 1859-60 consular keys, and R9549 (busta 2317, 1823, "Cifra del ... Principe di Castelcicala") is in a different code by Bourdeau's comparison (frequent groups 441, 486, 563, 1144). Those groups are also absent or single in R9586/R9588 (441 0, 1144 0, 1951 0, 486 1, 563 1; counted this pass), so R9549 is not visibly the second code either. REQUEST.md drafted 6 Oct 2026 (D4-CASTREQ: BL Add MS 41525 f.38 and an ASNa Esteri busta 2337 enquiry; ASNa contact address and catalogue record not found, left blank); waiting-on the ASKS row the account-4 orchestrator files; no ASKS.md row existed as of 2 Oct 2026. Formerly: file them only if the internal gaps above stall, next: REQUEST.md plus an ASKS.md row to ASNa (Esteri busta 2337 and the Segreteria cipher holdings) asking whether the 1816-23 codebook or decipher copies survive, ~$2

## Escalation (2 Oct 2026)
- [x] siblings: Bourdeau (21 Sept 2026) opened DECODE R9550-R9591 and R9549 (his NOTES.md Escalation; profile.json). He found the glossed 1823 letters R9569, R9571 and R9589 in this code (R9570 is unglossed), and found R9590 (1830) and the 1850s-60s telegrams (R9550-R9552, R9568, R9573-R9581) to be other codes. R9572 and R9590 fetched and classified (A2-CAS3, 2 Oct 2026): R9572 is the same despatch N. 3871 as the R9571 transcript, no new values; R9590 (1830) is a third code, matching neither the main nor the second code (control-backed, r9590/classify.py), with its own "Traduzione" sheet. The R9571 row's 40 note-derived tokens were then dropped with a logged correction (A2-CAS4, 2 Oct 2026; corrections.tsv).
- [x] clear-pages: the contemporary interlinear decipherments on R9566 p.3, R9569, R9571 and R9589 were Bourdeau's crib, the source of the G grade (2,906 tokens). Residual, listed as a gap: the 9 pencil-gloss lines on R9586/R9588 were aligned on disk by NEXT-CAS (2 Oct 2026): 6 of 9 placed, 10 candidate values at M, 207 188 ("cam bia") and 676 596 recur 3 times each against shuffled means of 0.02 and 0.07, 1043=che agrees across two lines, 224 conflicts; the image pass on R9586 p2 and R9588 p1-p2 is done (A2-CAS5, 2 Oct 2026): 21 values at M, 224=che and 1043="," settled, 287 a new conflict; no further pencil lines seen on R9586 p1-p2 or R9588 p1-p2 (R9586 p3 not viewed).
- [x] known-keys: Bourdeau found that DECODE R9532-R9541 (1859-60 Borbone consular keys) and R9549 (busta 2317) are different codes, and Tomokiyo's Cryptiana index has no Castelcicala entry. In KEY-CROSSMATCH.tsv, 43 rows test this ciphertext and none reaches more than 0.068 coverage. design_prior.py (KEY-DESIGN-PRIORS.tsv) puts it nearest the nomenclator family, with no same-office key on file. This pass also checked R9549's frequent groups against R9586/R9588: no match. Close-out omission, not a reading gap: there is no KEY-OFFICES.tsv row for this key.
- [x] print: Bourdeau (21 Sept 2026) searched the web, Treccani DBI and Cryptiana. bCAS (26 Sept 2026) searched the aay catalogue (R9586-R9588 listed Non-decrypted), IA be-api fts for "Castelcicala" (biography and memoir hits only) and OpenAlex (one unrelated hit); Semantic Scholar answered 429 twice. No printed decipherment was found, and QA/2026-09-26-0142.md passed the search. tools/print_check.py has not been run, because no span reads through to give phrases.
- [x] key-rebuild: Bourdeau bracketed the alphabetical runs (942 I-grade tokens) and ran solve.py it-modern 5-gram candidate scoring, which did not discriminate. bCAS's concordance (26 Sept 2026) added 3 S values (1378=a, 154=a, 605=enza). Each instrument has been run once, so neither is retired. A2-CAS (2 Oct 2026) ran the low-range concordance: frames beat the shuffled-record control (31 against 17.2, p95 24), but the value-vote rule fails its known-answer check (0-1 of 27), so no values. The it19 LM is built (A2-CAS7, 2 Oct 2026). A2-CAS8 (2 Oct 2026) ran that LM as a letter 4-gram in a seeded, bracket-constrained anneal (`family_run.py --family seeded_code`): matched control 0.070 against a 0.6 gate, blind 0.028, CONTROL BELOW GATE, target not run. A2-CAS9 (3 Oct 2026) ran the second instrument, an entry-bigram scorer (`--param lm=entry`): matched control 0.230 against 0.6, blind 0.038, CONTROL BELOW GATE, target not run; the family is untested-by-this-tool here (rule 3 third-attempt clause for any further tuning). Untried, listed as gaps: the A2-CAS frame pairs as tied-homophone constraints, which need an instrument whose control clears its gate.
- [x] image-check: R9587 done (A2-CAS6, 2 Oct 2026). The DECODE full-size scans, 30 iiif_lines.py crops, one blind pass and a reconcile confirm the low-range groups as written (45 of 47 clear-line groups match), and give 4 of 20 "?" an M reading, all unkeyed and not applied. The other 16 sit in a cancelled, offset-damaged passage and stay open. Still open, gap above: the 37 "?" in other records, after a key extension. Earlier: R9572 confirms the R9571 transcript line for line (A2-CAS3), with one 1408/1418 digit unsettled.
- [x] retry: bCAS (26 Sept 2026) ran Bourdeau's "[ ] retry" item, re-reading the un-glossed 1816 letters with the extended key. It added 3 values and left the 2261+do lead at M. Coverage went from 3,268 to 3,406 of 7,492 on the 1816 set and from 4,342 to 4,505 of 9,286 on the corpus. It must be rerun after any key extension or image-check correction.
Verdict: keep going: 5 internal gaps; cheapest next: file an ASKS.md row and an owner-side (LOCAL-QUEUE.tsv) request for a reading or copy of BL Add MS 41525 f.38, the 1816-17 Castelcicala-Circello clear-text extracts (Premise check (d)), as a possible grade-C crib for the un-glossed 1816 set; the seeded_code family is untested-by-this-tool after both its controls failed (letter 4-gram 0.070, entry-bigram 0.230, gate 0.6, A2-CAS8/A2-CAS9), ~$2.

## Web and blog check (GF-A2-1, 2 Oct 2026)

Run 2 Oct 2026, 21:19-21:21 UTC (date -u; committed 4a9c0c7d), by worker GF-A2-1 (account 2, LANE-A2PUSH). Plain web searches (one search engine):
1. `Castelcicala Circello 1816 dispacci cifra Londra Parigi` (sender + recipient + date) -- hits: De' Sivo/De Cesare *La fine di
   un Regno* on it.wikisource (biography), BL searcharchives Add MS 89143/2/21/1 and 89143/2/9/12 (Canning Papers, 1807-1810,
   outside these dates), an RMG archive object, a 1797-99 *Dispacci da Napoli* sale listing, TNA catalogue C11953. None prints
   a decipherment of the 1816-23 despatches.
2. `"affari esteri" 2337 Archivio di Stato di Napoli cifra Castelcicala` (shelfmark + cifra) -- hits: the ASNa Esteri inventory
   PDF (inventari-san 2360), ASNa's 2025 "fondi fuori consultazione" list, museum pages; no item-level hit for busta 2337.
3. `Principe di Castelcicala ambassador cipher letters 1816 deciphered Naples` (folder title, English) -- hits: BL Heytesbury
   Papers Add MS 41525 (Vol. XV, 1817-18), 41536, 41515; RMG objects; a unimi SSMD article; an NCF Napoleon-letter page. Add MS
   41525's JSON record opened (searcharchives.bl.uk, ?format=json): it lists "f. 38 (extr.) Fabrizio Ruffo, Principe di
   Castelcicala; Neapolitan Ambassador in London: Letters to the Marchese di Circello: 1816, 1817.: Ital." -- see Premise
   check (d). The other two records (41536, 41515) list no Castelcicala-Circello letters of these years.
4. `Castelcicala cipher scienceblogs OR ciphermysteries OR cryptiana` (cipher-community title search) -- Cipher Mysteries tag
   pages and old posts (Bellaso, Voynich), no Castelcicala post.
No decoded phrase was searched in quotes: no span of the reading runs to a sentence (Remaining gaps: "coverage by the key,
not sense").
Blog site searches: **Cipherbrain** (`site:scienceblogs.de klausis-krypto-kolumne Neapel Castelcicala OR Circello OR "Archivio
di Stato di Napoli"`) -- no scienceblogs.de hit; **Cryptiana blog** (`site:cryptiana.blogspot.com Naples cipher 1816 OR
Castelcicala OR Circello`) -- no blogspot hit (Tomokiyo's index has no Castelcicala entry, Bourdeau 21 Sept 2026, re-checked
by bCAS 26 Sept); **Cipher Mysteries** (`site:ciphermysteries.com Naples Castelcicala OR Circello OR "Two Sicilies" cipher`) --
ciphermysteries.com/?p=3700 opened ("Milanese enciphered letters, call for help", 2011): post and its 89 comments read, the
only Naples mention is a 1455 Sforza letter; other hits (Montefeltro conspiracy, Simonetta) are 15th-century. No comment
thread anywhere carries a decipherment or plaintext of these letters.
Requests: searcharchives.bl.uk 5 (2 s apart), ciphermysteries.com 1, search engine 7.

## Premise check (GF-A2-1, 2 Oct 2026)

(a) Decipherments the folder already mentions -- **found and used, two not opened.** The contemporary interlinear
decipherments on R9566 p.3 and the 1823 siblings R9569, R9571, R9589 are Bourdeau's crib and the source of all 2,906 G
tokens; they decipher those records, not the 16 un-glossed 1816 letters. The pencil syllabic glosses on R9586/R9588 (second
code) are aligned on disk (NEXT-CAS). R9572 (2337_23, 1823, DECODE "Decrypted", 1 page, inline cleartext and plaintext,
Italian) and R9590 (2337_41, 12 Mar 1830, "With deciphered plaintext", 3 pages): metadata read this pass from Bourdeau's
`castelcicala1816/decode/views_9532_9591.jsonl` (cited, MIT/CC BY); images **not opened** (DECODE login, one per session; not
in this gate-fix brief). Both are separate records, not the target letters, and Bourdeau classes R9590 as another code; R9572
stays the open gap already listed in "Remaining gaps".
(b) Other solvers' working files -- **found: Bourdeau's own working folder is this target's source.** Shallow clone of
dbourdeau/cyphersolver (2 Oct 2026, 21:16 UTC): `targets/castelcicala1816/` holds key.tsv, apply.py, solve.py,
reading_partial.txt, profile.json -- all already the basis of this folder (credited in "Source and credit"); no newer
reading there than ours (his reading_partial.txt is the 162-value key's output). His DECODE harvest
(research/catalogue_harvest/decode/batch_5.json) lists 2337_4 through 2337_39 with `"known": []`. aaymeloglu/unsolved-ciphers:
no Castelcicala hit in a grep of the clone (cited only).
(c) Physical neighbours -- **checked by Bourdeau, residual listed.** Busta 2337 records R9550-R9591 and busta 2317 R9549 were
opened by Bourdeau (metadata via API, 28 images); the glossed facing page R9566 p.3 is in use. Residual: R9572 (above).
(d) Recipient side -- **lead found, not seen.** British Library, Heytesbury Papers (William A'Court, British envoy at Naples),
**Add MS 41525** (Vol. XV, 1817-1818), **f. 38 (extr.)**: "Fabrizio Ruffo, Principe di Castelcicala; Neapolitan Ambassador in
London: Letters to the Marchese di Circello: 1816, 1817.: Ital." (searcharchives.bl.uk/catalog/040-002085178, read 2 Oct 2026).
These are extracts of the same correspondent pair and years in an Italian clear text in British hands; whether any extract
is the clear text of one of the 1816 cipher despatches here (R9553-R9560, R9579, R9587) is unknown until f.38 is seen. BL
images are not reachable from the cloud (IIIF dead since 2023), so this is an owner-side copy or reading-room step; if an
extract matches a despatch it is a crib (grade C) for the un-glossed 1816 set. Not in this folder or in Bourdeau's before
this pass (grep 'Heytesbury', '41525', 2 Oct 2026). No Neapolitan or Italian documentary edition of Circello's
incoming despatches was located (Treccani DBI biography only, Bourdeau; searches 1-3 above).

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: draft the two requests the Remaining gaps name but nobody has written (no REQUEST.md in this folder, no ASKS row, checked 4 Oct 2026): a REQUEST.md and ASKS.md row for BL Add MS 41525 f.38 (the 1816-17 Castelcicala-Circello clear-text extracts, Premise check (d)) and one to ASNa (Esteri busta 2337, the Segreteria cipher holdings) asking whether the 1816-23 codebook or decipher copies survive; ~$2. Sending is the owner's.
