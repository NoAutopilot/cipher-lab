# PREREG-MAT-BOX (15 Oct 2026, 11:1x UTC by date -u; account-4 worker MAT-BOX, LANE DEFAULT-A4-1035-15)

Written and pushed before any --try, judge score or image look of this job.
Brief: `.claude/briefs/runs/2026-10-15-acct4-default-1035-jobs.md` job MAT-BOX (A2-0810 handoff next step).

## Hypothesis
Bourdeau's `BOX` (key value `+`, grade U; 125 of its 137 tokens on f.110) is the BOX2 shape (MAT-EYE: 5/5 eyed on f.110)
and so carries BOX2's value **u** (S, MAT-KA/MAT-KEY).

## Instrument (second use on this target; MAT-F91B's first use failed its power control, whole text)
`tools/decode_key.py <dir> --try CODE=VALUE --lm fr16 --window 8 --nulls 100`, default acceptance rule, one code per call.
- **Scope A (primary): f.110 alone.** A scratch copy of the folder (decode.json, key.tsv, the f110-* lines of ciphertext.txt
  only; script `box/make_f110.py`, committed) so that occurrences and windows are f.110's.
- **Scope B (reported): whole text** (`ciphers/matignon-mayenne-1586`), logged to crossword_log.tsv.
- **Power control, run first in each scope:** wrong letters on the three H single-letter codes nearest BOX's f.110 count
  (h=e 126, o=i 128, e=r 163), each given the alphabetically next letter of its class (vowel->vowel, consonant->consonant):
  **h=i, o=u, e=s**. (o=i -> next vowel is o, the same letter's own sign is no test, so u.) Plus, as a vowel-class control
  matched to the candidate, BOX=a and BOX=o are run beside BOX=u and reported (not gates).
- **Gate:** if any of the three wrong-value controls is `accept`ed in a scope, that scope's BOX=u verdict is "non-test at
  this target/scope" and nothing is licensed from it. BOX=u counts as licensed only if, in scope A, all three controls are
  rejected/undecided AND BOX=u is `accept`. Even then: grade M, recorded in crossword_log.tsv, HYPOTHESES.md and NOTES.md;
  **no key.tsv edit in this job** (a later key row needs the f.110 image agreement too).
- Rule 3 third-attempt clause: if the control fails again here, the --try window score is logged in HYPOTHESES.md as
  untestable on this target at its current reading after two attempts; a third use needs a different instrument or a
  reading with fewer unkeyed codes (f.110 carries z 158, w 73, 4 58, v 35 unkeyed tokens beside BOX).

## Judge before/after
`ciphers/matignon-mayenne-1586/judge_leaves.py` (per leaf, fr16 spec judge, within-line shuffle control) before; after only
if a value were applied, which this job does not do -- so "after" = unchanged, stated, not re-run.

## o / c label image check (~1)
o (i, H) and c (p, H) on f.110: openapi.bnf.fr c116 region (<= 2 requests, scratch only), crop step via tools/iiif_lines.py,
the worker eyes up to 6 tokens of each against Bourdeau's label; report matched/mismatched/not-eyed per label, no regrade
unless a mismatch, and then downgrade only.

## Stop rules
Cap 3, box 60 min from 11:10 UTC; no unit started past 80% (2.4 / 11:58 UTC). openapi.bnf.fr <= 4.
