# harry-caroline-1863 cheap test 1 (25 Sept 2026, LANE B2 worker bHAR2)

Test: MASC with word boundaries on the Harry+Caroline ads jointly, single-letter words (`t` Harry,
`U`/`G` Caroline) fixed to a/I, `Ebcvgfm` tried as a name (also run excluding it from scoring).
Solver: `tools/subst_hillclimb.py` (library import), corpus `tools/data/pg2701_mobydick.txt`,
restarts=15, iters=1500, seed=1, max_homo=2 (needed to satisfy all 3 fixed symbols at once, see
below). Script: `run_test1.py`; raw output `test1_main.json`, `test1_control.json`.

Letter-count note: the spec's `harry_letters`/`caroline_letters` (44/27, 71 total) do not match a
direct extraction of the message bodies from `ciphertext_source` (address label and signature
stripped): Harry's message is 43 letters, Caroline's is 31, 74 total. Recorded, not corrected here
(out of this brief's scope).

Homophone note: `t`, `u`, `g` are three distinct cipher symbols, each standing alone as a
single-letter word at least once. English single-letter words are only "a"/"I", so a strict
one-to-one MASC cannot map all three into {a,i} without a collision. Ran with `max_homo=2` to make
the fix satisfiable at all — itself a mild negative sign against a plain 1:1 MASC on the
single-letter words specifically.

## Main test result

Best of the 8 fixed combinations of (t,u,g) in {a,i}^3 by solver score:
`{'t': 'a', 'u': 'i', 'g': 'i'}`, score_per_token=-1.005.

Reading: `ie ore tidinterea oun as leshing oth dthera a iisher i anddin rs i hate un ssten rods ho hsse`

`tools/judge_plaintext.py specs/harry-caroline-1863.json --file <reading>` (full output in
`judge_output.txt`):
```
ok   length: got=74, min=60, max=80
FAIL language: score=-1.442, null_p99=-1.848, real_p05=-0.919, real_median=-0.811, mode=both, N=74
ok   words: cover=0.662, min=0.6, real_text_median_cover=0.946
FAIL - harry-caroline-1863
```
Language FAILs (above the null but well below real English); words check clears the 0.6 floor only
because many 1-2 letter fragments are cheap to "cover" — not itself evidence of English.

Excluding `ebcvgfm` from the scored fragments (name variant), same fixed combo: score_per_token
worsens to -1.049 (not an improvement; the tool doesn't re-search combos for this variant given the
$3/30 min cap, so this is indicative, not exhaustive).

## Matched control (target vs control side by side)

Control: real English words of the identical 20-word length pattern (2,3,10,3,2,7,3,6,1,6,
1,6,2,1,4,2,5,4,2,4; 74 letters), drawn from `tools/data/pg1661_holmes.txt` (a source not in the
solver's own corpus, `pg2701_mobydick.txt`, avoiding circularity), enciphered with a random 1:1
MASC, decoded blind with the same solver/restarts, no fixed symbols, max_homo=1, 3 seeds:

| | target (this test) | control seed 1 | control seed 2 | control seed 3 |
|---|---|---|---|---|
| result | FAIL (language + not real English) | 33.8% letters correct | 31.1% letters correct | 16.2% letters correct |

The target reading fails the language judge outright (not just "low percent correct" — it never
resembles English at all); the control, run blind with no crib and no fixed letters, recovers
16-34% of letters per seed on a real English MASC of the same design. Different metrics (the
control's is percent-letters-correct against known plaintext; the target has no known plaintext),
so this is a design-validity check that the solver/corpus setup works on real data of this shape,
not a strict apples-to-apples score comparison. cheap_test_done records both numbers per rule 3.
