# PREREG PIS-275V -- f.275v head gloss, the words after "il desiroit", at native resolution (15 Oct 2026, pushed before any tile read or score)

Question (unchanged from PREREG-D4-PISA.md): does the period decipherment at the head of fr.16045 f.275v read "tenir si cachee" (Colbert 16 pt II
p.122) or another wording ("tenir tres secrete" was D1A-PISG's and D4-PISA's descriptive read)? D4-PISA's instrument ran on the 0.646x debug image and
its control gate failed (GC 5/8): a non-test. Its Next named this run: the same instrument on native tiles.

Source: openapi.bnf.fr IIIF v3, btv1b9060906j f563 (canvas 3925x5906), region 550,490,2475,1060 at max (2475x1060), fetched 15 Oct 2026 02:5x UTC,
HTTP 200; kept in the session scratchpad, not committed (regen URL in pisa/pisa_native.py's docstring).
Tiles: pisa/pisa_native.py -- D4-PISA's 9 boxes (pisa/pisa.py TILES, unchanged: target X + 8 controls communiquer, entendre, par lettres, personne,
neantmoings, perpetuel, dilligence, faisant; same options and decoys) scaled x 2475/1600 to native, upscaled 1.5x, grayscale. The boxes were checked
on a native overlay before any read and need no nudge (NUDGE empty). Caveat: the worker saw the overlay (to place boxes), as in D4-PISA.

Instrument: two blind Sonnet subagent calls (passes A and B), each seeing the 9 tiles in its own seeded order with its own option shuffle
(A seed 4, B seed 5), the same prompt text as D4-PISA (no copy, key, decode, neighbouring text, or which tile is the target).
Replies verbatim in pisa/reader_native_A.txt / _B.txt; `python3 pisa/pisa_native.py [--check]` -> pisa/pisa_native_result.json.

Gates (per pass, as D4-PISA): GC >= 7 of 8 controls correct; free-vs-choice agreement on X's distinguishing words (si/tres/bien/fort;
cachee/secret/couuert).
 GT: both passes GC PASS and agree free/choice, and choose the same X option -> that option is the reading of the phrase, letters graded S;
     both pass but choose different options -> split, M; only one pass qualifies -> reported, stays M; neither -> non-test, M.
Reconciliation (one unit, the worker, copy known): descriptive only, cannot change GT.
Outcome either way is a fact about the period gloss vs Colbert's copy, not about the cipher: key86.tsv, transcriptions, readings and kp86f grades
unchanged in every outcome. If GC fails on both passes the instrument is retired for this phrase (rule 3, third attempt at this instrument family
after D4-PISA's own run counts as the second); the next step is a person's look at the native tile.
