# copenhagen-1835 cheap test 1: monoalphabetic anneal vs Danish/German/English

Run 25 Sept 2026 by LANE B2 worker bCPH (`.claude/briefs/runs/2026-09-25-lane-b2-copenhagen-1835.md`).
Reproduces with `sh specs/cheap-tests/copenhagen-1835/rerun.sh`.

Tool: `tools/homophonic_anneal.py` (1:1 MASC anneal; K=23 signs at N=98 letters is at most a simple
substitution, no homophones needed). Pelling's 98-letter interpretive transcription (rule 2: conditional on
it; see spec's `ciphertext_source` for the transcription-vs-image discrepancy). Default settings throughout:
order=3, restarts=8, iters=40000, uni-weight=1.0.

No Danish corpus existed anywhere in this repo before this test; built `tools/data/da19/` (see its README)
from one Internet Archive `_djvu.txt`, *Historisk Tidsskrift* 1845 (1.04M letters after fold), after two
other 19th-c. Danish candidates were rejected for unusably garbled Fraktur OCR. `da` is **not** wired into
`tools/judge_plaintext.py`'s `LANG_CORPORA` (per the brief's fallback for an unwired language): this test
reports the anneal's own score against a same-script Danish control distribution instead of a judge
PASS/FAIL. `de` and `en` are wired, but the judge's `language` check compares a *candidate plaintext* against
a corpus at the candidate's own length; the object of this test is which corpus best explains the ciphertext
as-is (an anneal score comparison), not a claimed reading to run through the judge -- none of the three
decodes below is offered as a candidate plaintext (all three are near-nonsense).

## Target: anneal score by corpus (higher / less negative = better fit)

| corpus | best score (8 restarts) | decode (best restart) |
|---|---|---|
| da (tools/data/da19, 1.04M letters) | **-221.9** | aenendeblerelsmedestoueeueroratniereuiderftesfuluddeligddelsernetilskiederenfeldererereenneolgruer |
| de (tools/data/de16, period German) | -233.3 | felelundsernsdenunddieenengigenlangeeauerinediesettnsacutnsderlndasdmanuereliestehnherenlanischeng |
| en (tools/data/pg1661+pg2701, ~1.9M letters) | -236.4 | yininressinestherethauieuerarponeeriueringoitgusullesearlestinnehestheeriningierningislidedinienceasaduer |

None of the three decodes is legible in its language (expected: this is only a corpus-fit test, not a
crib-checked reading). Danish scores best among the three, consistent with Bonavoglia's presence-function
hint (25/107 distinct symbols in the image count is closer to a 29-letter Danish-style alphabet than a
26-letter one).

## Matched control: same tool, same N=98/K=23, real plaintext of that language enciphered and solved blind, 3 seeds

| corpus | seed 1 | seed 2 | seed 3 | score range |
|---|---|---|---|---|
| da | 63.3% (score -213.1) | **0.0%** (score -222.0) | 73.5% (score -207.1) | -207.1 to -222.0 |
| de | 80.6% (score -200.3) | 85.7% (score -202.3) | 85.7% (score -198.2) | -198.2 to -202.3 |
| en | 93.9% (score -200.0) | 93.9% (score -200.0) | 93.9% (score -200.0) | -200.0 (identical every seed) |

## Reading the two tables together

The target's score under the **Danish** corpus (-221.9) falls *inside* the Danish control's own real-plaintext
score range (-207.1 to -222.0) -- i.e. the ciphertext, decoded with the Danish model, scores about as well as
a genuine 98-letter Danish plaintext decoded blind with the same weak model. Under German and English the gap
is much larger: the target's German score (-233.3) sits well below the German control's real-plaintext range
(-198.2 to -202.3), and likewise for English (-236.4 vs -200.0). Read as weak positive evidence for Danish
over German/English, **not** as a solved or even a crib-checked reading -- the Danish control's own recovery
rate is low and erratic (0% to 73.5% letters correct across 3 seeds, one seed landing on a completely wrong
permutation), which means the Danish corpus/model is a much weaker solver than the German or English ones,
so this comparison is asymmetric evidence, not a clean apples-to-apples solve-rate comparison. Two caveats
worth flagging for whoever takes the next step: (1) the da19 corpus is ~1M letters vs ~1.9-2.5M for de/en,
smaller and noisier (OCR quirks, see its README); a bigger/cleaner Danish corpus would let this comparison
be trusted more. (2) The English control's identical 93.9%/93.9%/93.9% across all 3 seeds is a corpus
artifact: `tools/data/pg1661_holmes.txt` opens with repetitive Project Gutenberg boilerplate ("the project
gutenberg etext of the adventures of sherlock holmes...") that the anneal solves almost perfectly every time
-- this pre-existing corpus file is not this worker's to strip (out of this brief's scope), but it means the
English control's ~94% is closer to a ceiling effect on that specific 98-letter window than a real measure of
how hard English MASC recovery is at N=98 in general.

## Status

Cheap test 1 run; not a moved spec by this test's own numbers (no legible decode in any language, and the
Danish signal is weak/asymmetric per the caveats above). rule 10: no novelty wording, nothing to classify.
Per the brief, test 2 (IC/frequency-profile pass) was not run.
