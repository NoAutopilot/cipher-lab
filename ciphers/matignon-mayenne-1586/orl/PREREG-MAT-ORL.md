# PREREG-MAT-ORL (15 Oct 2026, 14:5x UTC by date -u (corrected from "15:0x", a typing slip; pushed 14:54); account-4 worker MAT-ORL, LANE DEFAULT-A4-1441-15)

Written and pushed before any --try of this job. Brief: `.claude/briefs/runs/2026-10-15-acct4-default-1441-jobs.md` job MAT-ORL
(MAT-R2 Verdict: re-label the 13 leaves' o by shape from MAT-O3X and MAT-R2's agreed labels, then `decode_key.py --try` oA=i / oB=a
at every occurrence with its power control; tokens not covered by the two readers' crops stay o, never guessed).

## Relabel (done before this PREREG; counts only, no score) -- `orl/make_orl.py coverage`
- Agreed labels = `osplit/sort_answers_r2cons.tsv` (both readers A -> oA 22, both B -> oB 32, else X -> o 24), on the 78 o tokens of the
  **f.91-92 margin blocks** (`osplit/sort_tokens.tsv`, drafts f91 / f91c / f91e).
- **13 target leaves (ciphertext.txt, 12,994 tokens, 662 o): 0 tokens covered.** None of the readers' crops is on f.110, ff.123-124,
  ff.143-201 or fr.15571 f.177, so all 662 stay o, per the brief. A `--try` of oA / oB on the 13 leaves has n = 0: it cannot be run
  and is logged as a non-test by construction, not as a result.
- f.91 blocks A-F (E from f91e only, as MAT-OSPLIT's secondary run, so block E's text is not duplicated; draft signs below H confidence
  -> '?'): 1,462 tokens, '?' 359 (24.6%), **oA 20, oB 28**, o 24 (unsorted/X and E's first-draft o's are not in this copy).

## Instrument (scope: the f.91 copy, the only scope where oA / oB occur)
`orl/make_orl.py build DIR` (a decode_key-ready copy: key.tsv and decode.json unchanged, oA / oB unkeyed), then
`tools/decode_key.py DIR --try CODE=VALUE --lm fr16 --window 8 --nulls 100`, default acceptance rule, one code per call.
This is the third use of the --try window score on this target (MAT-F91B whole text: power control FAILED; MAT-BOX f.110 + whole: passed)
and the first on the f.91 copy. Its 24.6% '?' is above f.110's unkeyed share; that is the risk the power control is there to catch.
- **Power control, run first (rule 3: it can differ on this axis -- a wrong value on an H code is accepted or rejected by the same
  statistic and rule as the candidates):** wrong letters on the four H single-letter codes nearest oA's and oB's counts in the copy,
  each given the alphabetically next letter of its class (vowel->vowel, consonant->consonant, wrapping): **n=m** (n=l, 25),
  **oo=f** (oo=d, 17), **c=q** (c=p, 29), **s=a** (s=u, 28; a vowel control with the candidate oB's own letter).
- **Gate:** if any of the four is `accept`ed, the scope is "non-test on the f.91 copy" and neither candidate is licensed; rule 3's
  third-attempt clause then retires the --try window score for the o shapes on this target (untested-by-this-tool, not refuted).
- **Candidates (gating):** oA=i, oB=a. **Swap, reported only:** oA=a, oB=i (should not both beat the candidates if the split is real).
- **Grade rule:** a candidate `accept`ed with the gate passed is recorded at S *for the f.91 tokens only*, in crossword_log.tsv,
  HYPOTHESES.md and NOTES.md. **No key.tsv edit in any outcome:** oA / oB occur on 0 tokens of ciphertext.txt, so a key row would read
  nothing; the 13 leaves' o stays o = i (H, Bourdeau) until their o tokens are themselves sorted by shape (images or the owner's sorter).
  Rejected / undecided -> M, logged.

## Judge before/after
No reading changes in any outcome (no key.tsv or ciphertext.txt edit), so `openings/leaf_judge.tsv` stands; `decode_key.py --check` run
on the target to confirm.

## Stop rules
Cap 6, box 14:52-16:07 UTC; no unit started past 80% (4.8 / 15:52 UTC). Disk only, 0 requests, 0 vision units.
