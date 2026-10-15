# PREREG-LVNNAMES -- name and null codes above 120 in WVO 4610/4611/4616 (pushed before any scoring)

Written 15 Oct 2026, 14:1x UTC (date -u), by worker LVN-NAMES (owner account, for LANE VIV-KEYSTONE, account 4).
Brief: `.claude/briefs/runs/2026-10-15-acct4-depth-steps.md`, JOB LVN-NAMES. No key.tsv / key_full.tsv / names.tsv /
reading / AUDIT.md / status.json edit; every value this job proposes is grade M at most and goes to a verifier.

## What was counted before this file (inventory only, no scoring)

Codes above 120 in `reading_461{0,1,6}_full_tokens.tsv` (key_full.tsv, AX-NAMES2): 608 tokens, 67 distinct codes.
Unread (value '?', grade U), by frequency: **150 x77, 125 x34, 148 x25, 145 x24, 149 x21, 140 x19, 142 x17, 147 x16,
139 x15, 146 x11** (the ten of this job; 249 tokens). Other period keys give these codes conflicting single letters or
NULL at low counts (key_4614/5801/7205-7208/names.tsv: e.g. 150 NULL H x3 in one key, 'd' M in another; 140 NULL H x6 /
's' M; 142 NULL H x2+2) -- AX2-172's rule: a code with conflicting H support stays M whatever this job finds.
Observation recorded before scoring: the ten codes sit in the 121-150 block, which names.tsv and key_full already value
as NULLs (15 C-graded NULL codes there) plus 123 'l' and 136 'uingt'; whole-name codes in this system start above 150
(153, 161, 192, 200, 221 ...). A whole-name reading of a code seen 77 times inside letter runs is a priori unlikely, so
both a name test and a letter/NULL test are registered.

## Frozen inputs (sha256)

| file | sha256 |
|---|---|
| key_full.tsv (unchanged) | 994d507975db00f5609bcc96003cde4cd196e7deecb5b87890ae248908b55629 |
| lvnnames/groen_IV_CDXLIV-CDLXXXV_ia.txt (Groen, Archives 1re s. IV, IA archivesoucorre11pringoog djvu, lines 12251-18282 = Lettres CDXLIV 22 Oct 1573 to CDLXXXV, Apr 1574) | 796646478bd85b205c674accd332b565041403e49b782597d6e30b1e787541f2 |
| lvnnames/pool_frozen.tsv (name_candidates --freeze-only: that index + KEY-OFFICES.tsv; Wikidata cache empty, not queried) | db275631b35cf62a21c6a2e45f9cc78ba5d901df5d57e6382e10e3c9ab143671 |
| lvnnames/pool_period.tsv (= pool_frozen + 27 H/C name values above 120 from the period sheets: key_full, key_4614, key_5801, key_7205-7208, names.tsv) | 48591920928582ce10d9725f63891ad8aef9713bed62f821f82234b643005b22 |
| lvnnames/key_holdout.tsv (key_full with 19 control codes set '?') | 0b08bdf2174d0c09a35d55c38af835a4dcb0dfac99bb5554e2ae7d653b6bdbfb |
| lvnnames/decode_three.json / decode_three_holdout.json (4610+4611+4616 jobs, scratch outputs) | db6f1d75... / 0c6d41b5... |

Disclosure: the period-name rows put the control's true answers (192 roidespagne, 200 herzogvonalba, 221 hollande,
153 pfaltzgraf) in the pool by construction, as the brief asks (the sheets' own name values); coverage is therefore not
evidence, rank is. Pool built from the Oct 1573-Apr 1574 window the brief names; 4610 (3 Jun) and 4611 (2 Jul 1573) are
before it.

## Test A: name_candidates.py (whole-name class)

Known-answer control, run FIRST: codes 192 (x6), 200 (x6), 221 (x4), 153 (x2) -- every code above 150 with a period H/C
name value that occurs in the three letters -- held out (contexts from decode_three_holdout.json, the tool never reads the
held-out key value), `--pool lvnnames/pool_period.tsv`, `--truth` = the period value and its spelling variants
(roidespagne|roi d'espagne|roy d'espagne|philippe; herzogvonalba|duc d'albe|alba|albe; hollande|holland|hollandt;
pfaltzgraf|palatin|pfalzgraf), `--nulls 200 --seed 1`, sender Lodewijk van Nassau, recipient Willem van Oranje, date
the letter's own (1573-06-03 / 1573-07-02 / 1574-04-12; one run per code with the date of its majority letter).
**Gate A: at least 3 of the 4 true values rank in the top 5 AND above their own context-null p95.**
If gate A fails, name_candidates is not run on the ten target codes (ARM-S3 rule: the calibration is a gate, not a
caveat); the job logs "name class: non-test at this pool/N" and goes to test B. Expected: FAIL (tool_shelf grade weak;
MQS-NAMES control (a) on this folder, 9 Oct 2026, ranked 202 at 13 and 223 at 11, each = own null p95).
If gate A passes, the ten codes are run with the same settings and the top candidate per code goes to test B as a
`--try CODE=<value>` word hypothesis.

## Test B: decode_key.py --try (letter / NULL class, the instrument's controlled-only use)

Language model fr16 (default), window 8, nulls 100. Statistic and verdict exactly as the tool defines them (accept /
reject / undecided; null 1 shuffled positions, null 2 random values of the class; breakage rule).
Known-answer control, run FIRST on decode_three_holdout.json: the 15 C-graded NULL codes above 120 with n >= 7 in the
three letters (127, 124, 135, 122, 138, 130, 141, 134, 121, 137, 144, 126, 133, 131, 143) held out. For each, the 24
hypotheses (23 letters a-z without j/k/w, as the tool's letter class, + NULL) are tried one at a time; per code record
the top hypothesis by statistic and the verdict of the true value (NULL) and of the best wrong value.
**Gate B (both):** (B1) NULL is the top hypothesis AND accepted for >= 10 of 15 held-out codes (about 2/3, the tool's
K3 Danzay rate was 19/23); (B2) a wrong value is accepted for <= 2 of 15 (false accept <= ~13%). B1 is not near ceiling
by construction: a NULL in this block is removed text, and a letter can fit a gap as well as nothing does.
Rule 3 "can the control vary": the statistic depends on each occurrence's neighbours, the true value is fixed by the
period sheets, and a wrong letter or NULL can each win -- so the control can fail differently from the target.
If gate B fails: test B on the ten is still run once (cheap, no key edit) but every result is logged "non-test (control
below gate)" and no value is reported as a candidate. If it passes: per target code, the top hypothesis and its verdict
are reported, grade M.

## What is reported

Per code: occurrences, name_candidates top (or "not run: gate A FAIL"), --try top value, statistic, both p95s, verdict,
grade M. The H/C/S share if a verifier accepted every accepted value: (current H+C over non-null cipher tokens of the
three letters) vs (same + accepted tokens, a NULL counted as removed from the denominator and a letter added to the
numerator). Both control numbers beside the target numbers (rule 3). No novelty wording (rule 10).
