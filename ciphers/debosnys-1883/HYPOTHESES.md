# Debosnys cryptograms -- hypotheses and prior attempts

Working file for the four Debosnys cryptograms (1883, Essex County jail; NOTES.md holds the check-solved verdict, the
image manifest, and the GOLD-0D/B2/4A/4B/4C/4E sections this summary rests on). Everything below the first `##` is
append-only, dated and signed by the job that wrote it; `tools/family_run.py` appends its rows under its own
marker at the end. This top block is rewritten once per cycle by the lane's consolidator and by nobody else.

**Summary, cycle 1** (GOLD-CONS1, Fable, session_017PRh6MAX17rgp5ayuycZ6c, 25 Sept 2026 19:35 UTC)

**Where the target stands.** Six page images on disk (c1, c2a, c2b, c3, c4a, c4b; 6 scienceblogs.de requests in all),
segmented into 1315 boxes; after GOLD-4C's by-eye split, 1251 signs over **160 ids** (29 `_` noise and 35 `MULTI`
boxes excluded), pooled IC 0.0391 against uniform-at-K 0.0063, French 0.0697, English 0.1022. Per cryptogram
(N, K, IC): c1 132/58/0.040, c2a 520/104/0.046, c2b 214/67/0.049, c3 116/59/0.035, c4a 201/68/0.035, c4b 68/49/0.015.
The sign X is 201 of 1251 (16.1 pct), self-adjacent 28 times; without X the pool reads N 1050, K 159, IC 0.019
(X alone contributes 0.026 of the pooled 0.039). 73 ids occur fewer than three times, 50 once; twenty of the
singletons are pictograms (horse, eagle, anchor, house ...), eight are plain Latin letters. 36 composite ids
(a base sign with strokes stacked over or under it: O-TILDE, OX-TILDE, O-DASH2, II-DASH, CC-DASH, ARCH-DASH,
C-BAR-X, II-O ...) cover 267 boxes, 20 pct of all signs. No ciphertext.txt at the gate yet: the file still holds
LANE B2's single-pass k=90 draft for c1-c3; `ciphertext_draft.tsv` is GOLD-4C's single pass A on the 160-id
inventory, `ciphertext_c1_draft.tsv` the c1 reconciliation.

**The bottleneck is the transcription, and the number that prices it.** Blind pass agreement: c4 22.4 pct at 68 ids
(GOLD-4A, of which three quarters was inventory confusion, not legibility, once settled on the image: reading-error
floor 9 pct); c1 62.3 pct full-id, 66.4 pct family-level, at 160 ids (GOLD-4E, 52 disagreements not settled on the
image). GOLD-4D (all four cryptograms through one subagent) was stopped at 3.3x its cap with nothing pushed. If two
independent passes each misread a share e of signs, agreement is about (1-e)^2 plus chance, so 62 pct agreement is
roughly e = 0.2 per single pass; a settled two-pass transcription sits near the 9 pct floor GOLD-4C measured on c4.
The only matched-control curve on file for what noise does to a large-alphabet anneal is Salviati's (NEAR.md,
LANE R6 CM, 25 Sept 17:54): code+mark at N 2820, K 223 reads 87-94 pct clean, 27-43 pct at 10 pct type noise,
24-27 pct at 20 pct. Debosnys is shorter and has a larger alphabet per sign (K/N 0.128 against Salviati's 0.079),
so the curve here can only be worse. Read: **a single pass (about 20 pct noise) is not a usable input to any
anneal; a settled two-pass (about 10 pct) is borderline; and whether even a clean transcription reads at this N
and K has not been measured.** That measurement costs nothing in transcription and comes first (D1 below).

| family | status | CONTROL | TARGET | what it rests on / what is left |
|---|---|---|---|---|
| T transcription (the input to every family) | **partial, below gate** | GOLD-4C's settled c4 columns: 9 pct reading-error floor | c4 22.4 pct at 68 ids; c1 62.3 / 66.4 pct at 160 ids; no cryptogram at the 80 pct gate | next transcription spend only after D1 says which K the solver needs; the cheapest path to one gated cryptogram is settling c1's 52 columns on the image (136 signs), not another blind pass |
| H homophonic French, sign = letter (`tools/family_run.py --family homophonic`, fr19 corpus) | **open, no control run yet** | owed: N 1251, K 160, fr19, seeds 1-3, at type noise 0 / 0.1 / 0.2 (D1) | not run; must not run on a single-pass draft | structural objection to weigh with the control: X at 16.1 pct exceeds any French letter's share once that letter is split across homophones, so under H either X is a null or divider (but it is self-adjacent 28 times) or e has a single sign; the control is built with the target's own sorted profile so it faces the same shape |
| BM base + mark (composites read as a base sign plus a modifier class; Sektu's N-glyph = nasalisation is one such mark) | **open, recount owed** | same control at (N, K_base) (D1) | a crude first-token fold of the 160 names gives K 85, IC 0.061 -- an upper bound, since it also folds the twenty pictograms into one and BAR-THIN with BAR-SOLID; the proper fold from GOLD-4C's 36-id composite list is D1's first step | the fold is mechanical (names carry their parts), so this family's K is a lookup, not a re-read; two passes also agree better at base level (66.4 vs 62.3 pct on c1) |
| NC nomenclator or code (sign = syllable, rhyme group or word; Sektu 2017's phonetic-syllable hypothesis) | **open, parked until T is gated** | none defined; a synthetic syllable cipher at N 1251 is the control if ever run | the long tail (73 ids under three occurrences, twenty pictograms), the 2.1 letters-per-sign estimate from GOLD-4B, the author's Latin/Greek/English/French/"Portuguese" | no ciphertext-only attack for a word code at this N; a syllable code needs an exact type identity, which T does not yet give |
| V verse form (a clear poem as crib) | **parked with numbers** (GOLD-4B; Sektu 2017) | shuffle null of 1000 line-length permutations | c4a vs the c3 clear poem r 0.44 at the 93.6th percentile (not significant; the 14-line match is an artefact of counting one of c4's two pages); Sektu rejected alexandrines against Baudelaire | the Greek poem on the reverse of the c4 leaf (Cipher Foundation scans, not on disk) is the one untested host text |
| L language (fr / en / pt / la) | **open** | fr19 exists (2.66M letters); en16_repo exists; la and pt corpora not wired | -- | the anneal control is French first; en second; la and pt only if H reads clean French at gate |

**Decisions, cycle 1.** T: no new blind pass this cycle; settle c1 on the image only after D1 (if D1 says a clean
transcription reads at this K, that settlement is the next job, c1 then c3, c4, c2, one cryptogram per worker, no
subagent, cost read at 15 minutes). H: continue, control only (D1). BM: continue, mechanical recount inside D1.
NC: park. V: park. L: French first.

**What transcription standard is good enough, per family** (to be replaced by D1's measured curve):

| family | K the solver sees | tolerable type-noise (working assumption from the Salviati curve) | which transcription reaches it |
|---|---|---|---|
| H at K 160 | 160 | under 10 pct, and only if the clean control reads at gate | settled two-pass, all four cryptograms (about 1250 signs, four Sonnet boxes) |
| BM at K_base | about 90-120 | under 10 pct at base level | settled two-pass at base level: fewer confusable ids, so cheaper |
| NC | exact | under 5 pct | out of reach this cycle |

**Decision rule for cycle 2, written before the numbers exist.** From D1's control table (mean plaintext letters
recovered, 3 seeds): (a) clean at or above 0.6 and 10 pct noise at or above 0.4 at K 160 -- H has headroom; buy the
settled transcription, c1 first, then run H on the gated cryptograms pooled. (b) clean at or above 0.6 only at K_base --
BM has headroom, H does not; the settlement pass is briefed at base level. (c) clean below 0.4 at both -- neither
letter family is a test at this N and K; the target is parked as "transcription-limited at K 160, no letter-substitution
control reads at N 1251" in the spec's `cheap_test_done`, NEAR.md keeps the row, and only NC (with a gated
transcription) or the museum's key sheet (ASKS 52) remain. Rule 10: nothing in this file is a reading; status stays
`open`; the lane never writes solved, new, first or unpublished.

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
