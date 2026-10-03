# Pre-registration 6: G2 (key no.71) on f.7r marked codes, located by fixed-key LCS anchors (GAPS91-fr4715-vieuville-pool, account-4)
Written 3 Oct 2026 (clock read 11:27 UTC), committed and pushed BEFORE scripts/f7r_g2anchor.py is written or run, and
before any key71_reconciled.tsv cell for an f.7r marked code is looked at this session.

## Why this is not a third attempt with a retired instrument (rule 3)
GAPS-14 and GAPS-15 retired "our key71 transcription scored by token-subset match against a printed answer list" and
named the f.7r period pair as the new material; PREREG3 (GAPS-16) registered G2 on that material, never run because G1
(flat-start aligner) FAILed. GAPS83 showed G1's gate reachable; GAPS88 (PREREG5) PASSed fixed-key scoring and named this
step: PREREG3's G2 with the marked codes located by the fixed-key LCS anchors instead of the flat-start aligner. This is
PREREG3's own G2, run once. PREREG3's "no further re-gate of key no.71 follows this one whatever the result" binds: after
this run, key no.71 is not re-gated again on any material with this match rule.

## Material (fixed)
witness/f4712_7r_pairs_img.tsv (GAPS82, unchanged). Tomokiyo letter table as scripts/f4712_7r_gates.tomokiyo().

## Locating each marked code's gloss
Per run: tokens = cipher_raw split; an unmarked N decodes to Tomokiyo's letter (N not in the table -> '?'); a marked
token (dN, tN, bN) is a sentinel that matches nothing. Gloss letters = plain_raw normalized exactly as f7r_fixedkey.py's
gl() (letters in the table's value set), with each letter's source word index kept (plain_raw split on whitespace).
LCS by full DP with traceback from the end, tie order: diagonal match first, then drop the token, then drop the gloss
letter. Anchors = matched (token index, gloss index) pairs. For a marked token at index i: left = gloss index of the last
anchor with token index < i (else -1), right = the first anchor with token index > i (else len(gloss)). The located text
is the plain_raw words all of whose gloss letters lie strictly between left and right, joined by spaces. Not located:
empty text, or another marked token lies between the same two anchors (shared interval).

## Items (fixed)
Every marked token, EXCEPT those whose mark the reconciliation NOTE lines call undecided: L01.1.1 d20 (the run's dots
flagged), L02.1.1 t12, L05.2.1 d16, L06.3.1 d87, L09.1.2 d47 and d20, L10.1.1 b85. That leaves 10 primary items:
L01.3.2 d41, L02.1.1 d16, L03.1.1 d11, L03.2.1 t11, L03.3.1 b65, L05.2.1 d12, L05.3.1 d42 and d99, L07.1.1 d33,
L09.1.1 b7. Layer by mark (one dot mots, bar persons, two dots places); key cell from key71_reconciled.tsv via
key71_control.load_key; match / conflict / absent by f4712_7r_gates.judge (PREREG3's notation-normalized nmatch,
unchanged). Located-but-absent and not-located items are reported, not scored.

## Gate (PREREG3's, unchanged)
Controls: label permutation of located texts over the scorable+absent located items (exact if <= 8, else 10,000 draws,
seed 4712) and random code in the layer's range (mots 11-99, persons 1-89, places 1-99), 10,000 draws, seed 71. Both
can differ from REAL: each changes which key cell meets which located text, the statistic's own axis.
PASS: scorable >= 8, SHARE = match/(match+conflict) >= 0.80, REAL match > p95 of both controls (strictly).
scorable < 8: NON-TEST. Otherwise FAIL.
Descriptive only (does not change the verdict): the same run over all 17 marked tokens.

## What follows (fixed)
- PASS: key no.71 qualifies on f.7r for the marked layers; no.44's open slots may then be read from key no.71 in the
  layer their mark selects at grade M, as a SEPARATE next step (not this job), with decode_key --check after.
- FAIL: key no.71 does not match f.7r's period glosses as located; the conflicts are logged (rule 4, data, not merged);
  no slot read; key no.71 [retired] as an instrument for no.44's slots.
- NON-TEST: f.7r carries too few located marked codes to test key no.71 with this locator; no slot read; key no.71
  re-gating closed by PREREG3's clause; the slot step needs new material (another key-71 leaf with marked-code glosses).
