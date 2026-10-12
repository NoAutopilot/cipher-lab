# PREREG-MANT-NAMES (12 Oct 2026, 18:5x UTC by date -u; LANE DEFAULT-A2-1810, account 2)

Brief: .claude/briefs/runs/2026-10-12-ytbiz-default-1810-jobs.md "### MANT-NAMES". Disk only. Written and pushed in its own commit BEFORE
any score is computed (the script fnames/names_gate.py is written after this file lands on origin/main).

## Question
Does key.tsv, applied to the never-glossed MANT-POOLU pool, give letter-spelled name runs that agree ACROSS leaves (or with key.tsv's own
glossed name codes) more often than a key with the same value multiset but permuted assignments? This is the cross-leaf consistency gate
MANT-POOLU named (13 alone x5, 103.34.26 'le pr' across 0483/0491, Stettin as 57.28.35.59 / 51.28 / 390 across 0088/0247).

## Data (frozen on disk at 325a05e91)
- Target set S: fpoolu/ciphertext.tsv (frames 0088 0247 0426 0442 0483 0489, 94 tokens) + f0491_08/ciphertext.tsv (38 tokens). Runs = the
  files' `line` field.
- Key: key.tsv. A code's value = the first option of its `value` cell (before `|`). A code is LETTER-LIKE if that first option, letters only,
  has length 1-3 (letters, syllables, 'le'/'la'); codes absent from key.tsv decode to '?', which never matches anything.
- Name list L: every key.tsv row graded C whose first-option value, normalised (lower case, accents stripped, a leading 'le '/'la '/"l'"/'der '
  removed, non-letters removed), has length >= 4 (390 Stettin, 155 Flemming, 252 roideprusse, 299 angleterre, 312 berlin, ...).
- A letter run = a maximal stretch of letter-like codes inside one `line`; its decode = concatenated values. Only runs with decode length >= 3
  enter.

## Statistic T = T_a + T_b (computed identically for target and every null draw)
- T_a: unordered pairs of runs on DIFFERENT frames whose decodes share a common prefix of length >= 4 with no '?', counted only if the two
  CIPHER sequences differ in at least one position inside that prefix (identical cipher prefixes agree under every key, so they are excluded).
- T_b: runs whose decode shares a prefix of length >= 4 with some normalised name in L.

## Why the null can vary on T (CLAUDE.md rule 3, "control that cannot vary")
Null = key-permuted: the multiset of letter-like first-option values is shuffled over the letter-like codes (1000 draws, seed 20261012).
Every run's decode changes under a draw, so both prefix agreements between DIFFERENT cipher sequences (T_a) and matches to the fixed name
list (T_b) can rise or fall; only identical-cipher agreement is invariant, and T_a excludes it by construction.
Items that CANNOT vary under any key and are therefore logged as non-tests, not scored: 13 alone (same single code each time); 103.34.26(.27)
on 0483 and 0491 (identical cipher sequence on both leaves); 390 / 252 / 150 / 187 / 217 / 257 (nomenclator singletons, value fixed by key.tsv).

## Gate
p = (1 + #{null T >= real T}) / 1001. PASS if p <= 0.01. A second null (frame labels shuffled over runs, 1000 draws) is reported only.

## Power check (run BEFORE the target score; stop on fail)
Power pool: every other folder's reading_tokens.tsv (on disk at 325a05e91) whose `grade` column is >= 60% H/C/S (key-validated leaves; their
readings come from the same key, so the key is the known answer there). 200 subsamples: draw min(7, available) frames at random, keep their
runs of decode length >= 3, then subsample runs at random to the target's own count of such runs (if a draw has fewer, redraw). Per subsample,
p from 200 key-permuted draws. Power = share of subsamples with p <= 0.01. If power < 0.80: stop, log "non-test at this N", do not score the
target (the script exits 3 before touching S).

## Outputs
fnames/names_gate.py (with --check), fnames/power.out, fnames/gate.out, fnames/per_code.tsv (each contributing pair/match and each non-test
item). Grades rise from M only on a PASS; key.tsv unchanged unless two independent glossed witnesses support a value (rule 4).
