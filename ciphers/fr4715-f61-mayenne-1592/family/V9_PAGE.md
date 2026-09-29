# f.61r for the verifier (CAMPAIGN.md H274) -- runner 10's page, 29 Sept 2026

Compiled by campaign runner session_0148wt8Aokh6aZEdJsXzYiZX (account 3, runner 10) for the VERIFY-F61-V9 brief. It collects paths and
results already recorded in NOTES.md and HYPOTHESES.md; it adds no claim, no reading and no class. Nothing on f.61r is solved, new or
first. Key v6 (family/key_period_v6.tsv) is unchanged by this session; VERIFY-F61-V8's "what should merge" list is still unmerged.

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
