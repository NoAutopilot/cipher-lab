# f.61r for the verifier (CAMPAIGN.md H274) -- runner 10's page, 29 Sept 2026

Compiled by campaign runner session_0148wt8Aokh6aZEdJsXzYiZX (account 3, runner 10) for the VERIFY-F61-V9 brief. It collects paths and
results already recorded in NOTES.md and HYPOTHESES.md; it adds no claim, no reading and no class. Nothing on f.61r is solved, new or
first. Key v6 (family/key_period_v6.tsv) is unchanged by this session; VERIFY-F61-V8's "what should merge" list is still unmerged.

> Status line (H301, runner 11 session_01RNzUvRTqBTAw7BukhKyKBU, 29 Sept 2026, 11:2x UTC): VERIFY-F61-V9 has ruled (AUDIT.md, 10:33 UTC): CA endorsed in
> part (letterform replicated, p 0.0013; null direct for the 4 in-span tokens), the C6 conflict endorsed with the word test (e breaks 4 of 5 of his words),
> the null band endorsed; meter 12 / 59 / 2 / 26 [null 17 + unread 9]. Key v7 exists (F61-FAMILY-11, 10:17) and F61-FAMILY-12 (11:15) wrote V9's notes into
> KEY.md, f61_null_band.tsv and HYPOTHESES.md's C6 row. The header below is runner 10's as written at 10:27; the sections after it are later additions.

## Claims put up for audit this session (runner 10, steps H256-H273)

| claim | evidence | controls | files |
|---|---|---|---|
| **CA (10 tokens) is a null drawn as the letter a**, not a cipher value and not a clear letter left among the signs | letterform: two blind free sorts put all 10 CA with the scribe's clear a (5/5 and 5/5; group criterion "cursive minuscule a" both times); hand: H63 (28 Sept) put 5 of 6 in the cipher hand by weight/baseline/spacing; markup: all 4 in-span CA pair with Tomokiyo's dash and the words around them are complete without an a (est ca[-]pable, trop[--]avancees, beau[-][-]pere); a reader with no atlas takes CA for the word "a" (H253/H257/H264) | text a's grouped 6/6 both calls (gate 1); non-a letters 0/6 in the a group (gate 2; 3 of 6 came back unclear, 2 in their own o group); cipher PHI/C43 0/12 in the a group; hypergeometric P 0.030 per call | family/h256_ca_text_result.txt, family/h260_ca_text_result.txt (+ items, passes/h256_sort.tsv, passes/h260_sort.tsv), family/h259_ca_span_result.txt, scripts/f61ca_result.txt |
| **C6 = e has no support on f.61** (rule-4 conflict) | pooled C6 = e rests on 3 glossed tokens (f.101r L42/L45, f.188r L04); on f.61 Tomokiyo's markup is a dash at all 5 in-span C6, the known-span score is identical with and without the cell, and H237's blind sort put f.61's plain 6 apart from the glossed delta-shaped C6 | H261: 50/55 raw (53/55 folded) both ways; H237 controls noisy (n = 2 glossed) | family/h261_c6_markup_result.txt, family/h237_c6_glyph_result.txt, HYPOTHESES.md row "campaign H261" |
| **Span S5 reads as French only as "me l'entendoit"**: L11 8 (4STEM) = n, **L11 9 (the 4-over-Pi) = d against the published n** | fr16 corpus (933k words): entendoit 6, entendoient 1, enten- forms 0 (the pronoun phrase l'entendoit itself is not attested: H278 corrected an earlier "l entendoit 5" that was the substring of "il entendoit"; contexts verbatim in family/h278_entendoit_contexts_result.txt); H85's blind judge (28 Sept) had resolved the span "melentendoit"; H139: L11 8 is the only Tomokiyo dash on a keyed sign | pre-stated rule (entend- >= 5, enten- = 0) met; H269 test keys: 4-over-Pi = d scores 52/55 on the published markup and 54/56 on the entendoit witness, a/n the reverse (53/55, 53/56), pooled a/d/n/q 53 and 54; 2000 permuted keys never reach any | family/h268_entendoit_result.txt, family/h269_4overpi_d_testkey_result.txt, HYPOTHESES.md row "campaign H268" |
| Positions for 95 of 99 signs (infrastructure) | H253 (57), H257 (25: the unmatched sign per line was the CA read as the word "a"), H264 (13, the L10 fragment; x stored at 2x the reply, checked against H63 at ratio 2.00) | joins by count only | scripts/f61_positions_all.tsv, scripts/f61_positions_L10.tsv |
| The scribe does not space words in the cipher | boundary gaps 260/320 (n = 2) inside the within-word range 210-410 (n = 34) | permutation p95 350 | family/h265_span_gaps_result.txt |
| The null band as one table | 25 unread-or-null + 4 wider tokens, evidence and files per class | -- | family/f61_null_band.tsv |

Non-tests logged, not evidence: H258 (LOOPBAR glyph link, n = 1 + 1), H263 (no CA on the overlaid f.108r rows), H266/H267 (by H265), H270 (superseded),
H271/H272 (a count-3 word list segments any lattice, control 200/200), H273 (no "ni mesme" in fr16).

## Added after the first version (H277-H283)

- `scripts/tomokiyo_spans_witness.tsv`: the five spans with S5 as the lexicon witness, beside the untouched published file; `f61crib.load_spans(path)`.
- `family/f61_dash_need.tsv` (H281): Tomokiyo's 16 span dashes -- 12 on null-band classes, 3 on keyed classes (L05 1 LOOPSTEM1 q/s, L05 2 CH e/m, L11 8
  4STEM a/n), 1 unpaired; his own phrase needs a letter at L11 8 only.
- H280: a standalone pronoun before entendoit occurs once in fr16 ("s'il l'entendoit") and never in the later corpora; "me l'entendoit" is possible,
  rare French in these texts. H278 corrected H268's phrase count (see above).
- H282: "comme" + majesty formula 0 of 2,108 in fr16: L04's OTHER is not "S.M." by the corpus; stays OTHER.
- H283 (lead, grade M read by the runner, blind pass pending as H288): L04 ends "croys aussi que les" and L05 opens "[LOOPSTEM1] [CH] trop avancees",
  so the two keyed signs before "trop" cannot be letters there (French wants a noun and a verb; fr16 "les W1 W2 trop": choses allaient, pretentions
  etaient); word codes outside Tomokiyo's que/qui/pour, or a misread "les".

## WITHDRAWN: the word-code lead on L05 1-2 (H283-H291; NOTES "Correction")

The runner took L05's run to open the line; the span sheet drops the first native segment, and sheet B shows the line beginning "choses sont a" in
clear. The text is "Je croys aussi que les choses sont a [LOOPSTEM1] [CH] trop avancees": complete French with the two signs (and the edge a) as nulls,
which is what Tomokiyo's three dashes say. What survives for the verifier: on the family leaves the two classes are letters inside words (H288/H291,
25 of 30), on f.61 his dashes and the French agree they carry nothing -- a leaf-level difference of the C6 kind; and the CH e/m cell is two leaves'
letters merged (HYPOTHESES.md H289). No word-code claim.

## Meter variants the verifier chooses between (verify_v8/meter_v8.py bands, key v6 f.61 reading)

- V8 as endorsed: **12 / 58 / 2 / 27** (4PI split, f.61's two 4-over-Pi held unread).
- V8 variant, L11 9 a/n at grade M on Tomokiyo alone: 12 / 59 / 2 / 26.
- This session's lead, L11 9 = d at grade I (lexicon witness, HYPOTHESES.md H268): the count does not move unless a grade-I one-letter candidate is
  admitted to the firm band, which is the verifier's rule to set, not the runner's; L01 12 stays unread either way. CA's 10 tokens stay in the
  unread-or-null band whatever wording is chosen ("null" rather than "unread" on the evidence above changes no count).

## What is not claimed

No plaintext beyond Tomokiyo's five published spans is read. "me l'entendoit" is his own span with one letter corrected by the lexicon, a
candidate (grade I) that stands against his printed n; the safe sentence is "the corpus admits only entendoit at that place, which would put d
at L11 9 where the published reading prints n". Rule 10 wording only; novelty is not the runner's to assess.

## Added after the withdrawal (H295-H300, runner 10; carried in by H301, runner 11): a second letter-shaped null, at n = 1

Not audited by V9 (its brief closed at H262); for the next verifier.

- **H297** (one blind Opus positional read of sheet B's L05 from the true line start, `scripts/h297_reply.tsv`, `scripts/f61positions_L05B_result.txt`):
  "choses sont a" precede the run, so the Correction's premise has a blind witness; the reader lists the CH sign as the clear letter "h" between the
  LOOPSTEM1 loop and the VBAR_A, as readers take CA for "a". **H299** joins the line 18/18 once the bare "h" is taken as CH (`scripts/f61_positions_L05B.tsv`).
- **H298** (H256's design on CH, `family/h298_ch_text.py`, key `family/h298_items.tsv`, one Opus free sort, `family/passes/h298_sort.tsv`, result
  `family/h298_ca_text_result.txt`): the one CH tile (L05 2) sorts with all 3 clear h's (group "a cursive h, tall looped ascender, arched shoulder"),
  PHI/C43 0/4, the l of les in its own group, 2 non-h unclear. Pre-stated read-out met: **CH has the clear h's letterform -- at n = 1 on the CH side,
  flagged.** With Tomokiyo's dash (H281), the French complete without it (Correction, H295), a letter inside words on the family leaves (H288/H291) and
  the CH cell being two leaves' letters merged (H289): on f.61 the sign is an h-shaped mark reading as nothing, the CA pattern at n = 1. No cell change;
  CH stays keyed e/m in the meter (two-way band) until a verifier rules; `family/f61_null_band.tsv` carries it as a `note` row outside the 25 + 4.
- **H300** (`family/f61_nulls_as_letters.tsv`): of the null-band and dash classes, CA (a), CH (h), C6 (6), LL (ll) and partly LOOPSTEM1 (q-like) are
  shaped like clear letters or digits by the atlas and the readers' own words; CROSS, LOOPBAR, the 4-over-Pi and OTHER are not. LL's test is H302 (open);
  C6 has no clear-text digit control on the leaf (H303, open).
- **H295/H296**: "sont trop" needs no filler in fr16 (bare 1, one-word 2, "est trop" 5), so the null reading of L05's edge a + LOOPSTEM1 + CH is unforced;
  `scripts/f61_sheet_edges.tsv` flags which positioned "edges" are sheet edges (L05 1, L03 15, L08 14), a guard against the H283 error.

Meter variant this adds (not computed as a band change, because CH is keyed): if a verifier moved CH to null on f.61, the two-way band would lose one
token and the last band gain one: 12 / 58 / 2 / 27 [null 18 + unread 9]. Nothing moves until then.

## Added by runner 12 (H302-H306): LL's letterform, and L02's opening mark

- **H302** (one blind Opus sort, `family/h302_ll_text_result.txt`): LL against clear 'ella' and two clear 'Il' -- **CONTROL FAIL** (the two 'Il' sort
  together by the capital I's diagonal lead-in, 'ella' unclear), no read-out on LL.
- **H304** (fresh reader, capital-I control explicit, `family/h304_ll_pair_result.txt`): **CONTROL FAIL** again (one clear I unclear), nothing scored.
- **Descriptive, in no gate, both times:** f.61's LL (L05 16) and L02's opening mark were put together in a group of their own ("two tall long-s-like
  stems side by side"), apart from every clear I, every single l and PHI/C43. read_call_U pass 1 coded that mark LL, pass 2 read it as the handwritten
  'Il', and the decode follows pass 2. If a verifier took it as LL, the null band's LL would count 2, not 1 -- a recount for the verifier, not applied.
- **H305** (`family/h305_ll_census.tsv`): no ll-only control in f.61's hand can be cut from material on disk (one clear ll, 'ella'; every other ll word on
  file is de Diou's hand). A second LL token in this hand: f.108v L06 29 (pass B only, confidence l).
- **H306**: a `note` row `L02 0 LL?` in `family/f61_null_band.tsv` (counts unchanged: 25 + 4; note rows 2) and the LL row of
  `family/f61_nulls_as_letters.tsv` carry the above.
- **H309-H311** (added 29 Sept by runner 12): the free sort was retired for LL after a third failed gate (H309 NON-TEST; HYPOTHESES.md,
  untested-by-this-tool). A different instrument, a forced choice ONE / TWO / NEITHER, passed its known-answer gate 14/14 with four doubled l's from a
  clear chancery page (fr.3983 f.211r) and put **LL = TWO, like the clear ll** (H310, n = 1, flagged). A second forced choice (capital I lead-in vs
  upright l, known answers 7/7 + 4/4) got **unclear** on both LL and L02's opening mark (H311): whether that mark is LL (pass 1) or a clear 'Il'
  (pass 2) is for the verifier's eye; counts unchanged.

**C6, the digit-shaped null (H303).** f.61's eight C6 tokens are shaped like the digit 6 (atlas; the blind readers write "6", "6-shaped sign", once "b / 6 shape", H253/H264/H297). On f.61 every in-span C6 (L01 2, L03 11, L07 6, L08 3, L08 9) carries Tomokiyo's dash (H261), the French of his spans is complete without a letter there (H281), the pooled C6 = e cell (three glossed tokens on f.101r/f.188r) gains and loses no span letter (H261), and f.61's plain 6 showed no glyph link to the glossed, delta-shaped C6 of those leaves (H237) -- so f.61's C6 reads as nothing, the rule-4 conflict row in HYPOTHESES.md standing. Unlike CA (a), CH (h) and LL (ll), a letterform test cannot be run on it here: f.61's clear text holds no digits, and the only same-hand clear page on disk, fr.3983 f.211r (H308), is prose with no numerals seen at 1600 px (its date is in the docket, another hand). What a real test would need: clear numerals written by Mayenne's secretary (dates, sums or counts on a leaf of fr.3982-3984 in the hand of f.61/f.108/f.211r), used as known answers in H310's forced-choice format ('the digit 6 / some other shape'), with PHI/C43 as neither-controls; until then the C6 argument rests on the markup and the missing link to the glossed C6, not on letterform. C43 is not in this paragraph: it is keyed a/n and reads letters in the spans.

- **Correction (H312):** the "second LL token in this hand" at f.108v L06 29 named under H305 above is not supported (pass B only, confidence l, on a 720-px band cut through the line's lower half; pass A reads OTHER; the native H59 draft of f.108v codes no LL). LL stays n = 1.

## Added by runner 12 (H325/H328): a held-leaf check of key v7's cells on fr.3982 f.124r

f.124r's gloss (HELD, never loaded into a key): 165 words both model gloss passes read identically, 651 letters over 266 signs. Letters falling in
key v7's cells, one-to-one: **148**, against shuffled cells p95 140 (H325), a binned frequency-matched permutation p95 143 (7/1000 >= real) and a
frequency-only key 132 (H328). Lead stands as pre-stated; grade M gloss letters, a 5-letter margin; not a reading, f.124r stays HELD.

- INSTRUMENTS (29 Sept 2026, runner 12, H302-H329): a blind FREE letterform sort failed its own gate three times on LL (H302, H304 CONTROL FAIL; H309 NON-TEST) and is retired for that question (HYPOTHESES.md, untested-by-this-tool). A per-tile FORCED CHOICE with known answers passed where the free sort could not (H310 ONE/TWO/NEITHER 14/14; H311 LEADIN/UPRIGHT 11/11) and failed only where the known-answer tiles themselves were poor or confusable (H324: f.101r's dense page, both known tiles unclear; H322: VBAR_A and EBR confusable on f.211r's run). So: prefer the forced-choice design, check the known-answer tiles' centring on a placement sheet first, and never take known answers from a dense leaf without hand-set centres. For held-leaf checks of the key, the H325/H328 count (two-pass agreed gloss letters matched one-to-one into v7's cells) must be run against a frequency-matched control (binned permutation and a frequency-only key), not cells shuffled across all classes alone.
- **H330/H331:** the f.124r lead is **fragile** under a 200-word bootstrap (beats the frequency-only key in 90% of resamples, pre-stated bar 95%); it is carried by PHI and C43, and VBAR_A's g/t scores below its binned mean on f.124r (HYPOTHESES.md row). Treat H328 as a lead only.
- **H332-H341 (runner 13, 29 Sept 2026):** f.106r rows 7-12 read by the model gloss passes at 0.252 word agreement (rows 1-6: 0.339) -- the model gloss readers are retired for this hand (untested-by-this-tool; a person's read, ASKS 99, now 42 arrows on twelve sheets). A gloss-free check (key v7 on the sign draft, fr16 4-gram beam, against binned-permuted keys) passed on the held leaves f.124r, f.97r and f.108v, but its own shuffled-order control VOIDED that arm on f.106r, f.124r, f.108v and even in-sample f.101r (H341): there it measures frequency matching, not sequence. **Those beam passes are not evidence for v7**; f.97r survives on its own leaf only and is fragile. The f.124r gloss-count lead (H325/H328, fragile per H330) is a different instrument and is unaffected. A within-run order statistic (H342) is being tested against its in-sample control.
- **Order checks of key v7 (runner 13, 29 Sept 2026, H335-H354; one current paragraph).** A within-run ORDER GAIN (v7's fr16 4-gram beam score in real order minus within-run shuffles, against 100 frequency-matched permuted keys; now `tools/partial_key_test.py --cells`) passes in-sample on f.101r and f.188r and passes its shuffled-target control. On leaves v7 was not built from it shows an order signal on **f.124r (0/100) and f.97r (0/100)**, and on **f.108v (f.61's own hand) only on the 180 signs both drafts read alike (5/100; 8 runs, a splice caveat)**. **f.106r (the secretary's hand, rows 1-18, 51 runs): no signal, untestable at this N** -- held leaves with the signal pass only 0.10/0.53 of 51-run subsets (H351; H350's in-sample power had overstated it). Per class with size-matched alternatives (H349): **HASH4 d/q supported on both held leaves**; C43 a/n, H24 i/x, ZBAR f/s on one each; EBR_B l/y weakest (0.46/0.08), but the per-class test is underpowered in-sample (H355: f.101r 4/10), so misses carry no information; only the passes stand. On f.124r, widening 4TRI by a/n beats all 30 random widenings (H358): the readers' 4TRI there likely mixes the no-bowl a/n sign (H218/H231's finding elsewhere) -- a transcription pointer, not a cell change. Void and not evidence: the earlier plain beam-vs-permuted-key passes (H335/H338/H340; voided by their own shuffled-order control, H341). v6 vs v7 differ only in 4PI; split (H347). Evidence about v7's cells as a set; not a reading, no token graded.
- **f.124r's 4TRI is mostly the no-bowl sign (runner 13, H358-H361, 29 Sept 2026).** An order pointer (H358: widening 4TRI by a/n beats all 30 random widenings) was tested by shape: a bowl forced choice with H193's known-answer strips in every call (gates 18-19/20, five calls) finds **202 of 270 agreed 4TRI tokens on de Diou's f.124r have no stem-foot bowl** (C43 20/20 no-bowl). Relabelling them C43 **doubles v7's order gain** (0.034 -> 0.071, shuffled targets clean; H360) and **raises the held-gloss count 148 -> 156** (binned p95 148, 1/1000; H361). A transcription correction for the f.124r draft, supported by two independent instruments; no cell change, not a reading; earlier f.124r counts saw two signs under one code.
- **The same on f.101r, checked against period letters (H362/H364).** f.101r's agreed 4TRI: 77% no-bowl (gate 17/20); joined to f.101r's own period alignment, **no-bowl 4TRI pairs with a/n 23 times vs c/p/t 6, bowl-letter agreement 44/56 = 0.79**. The readers' 4TRI code is two signs (c/p/t with the bowl, a/n without) on the leaf that built v7's 4TRI cell; v7's 4TRI tally mixes them. A resplit proposal is H366 (verifier's call; nothing changed).
- **f.101r in full (H365/H366):** 241 answered 4TRI: no-bowl 155, bowl 67; by f.101r's own period letters **no-bowl -> a 62, n 56 (118 of 130 a/n-or-c/p/t)**, bowl -> p 17, c 15 (n/a 19); agreement 0.83; the split raises f.101r's order gain too. Proposal for the verifier:  (read the no-bowl '4TRI' as the a/n sign; nothing applied). f.61's own 4TRI tokens not yet bowl-read (H367).
