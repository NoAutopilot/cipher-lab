# NAF-SPLIT pre-registration (account 1 worker for LANE DEFAULT-A1-1140-15, 15 Oct 2026, written 12:1x UTC by date -u, pushed before any registered score)

Brief step (gap line): "the same anchored split on f.249/f.250 (501 or another count-matched f.206 C anchor, pins, 722 ti vs i on its
segment, own (s)/(g) controls)". That gap text was written by FT4s; FT4t (3 Oct, PREREG-FT4t.md, 49e1f5a9) then ran it with the only
count-matched anchors of that day (628 'hongrie', 279 'plus'; 501 and 581 absent from f.249): NON-INFORMATIVE for both 722 values,
and the one-edit family was logged [retired] for the 722 question on f.249 (untestable at that length, rule 3).

What is new since FT4t: two codes reached C after 3 Oct -- 121 's' (FT4z pooled pin gate) and 605 'republique' (R9-ROUSV2, 6 Oct, slip
known plaintext at all 7 slip-backed occurrences). Count check over every C row of key.tsv (`ft4t_seg.py --show`, no score):
605 is 2 groups (f.249 idx 29, 74) vs 2 whole slip words (idx 18, 49), cut orders consistent with 628 (38/26) and 279 (101/64). It is
the only new count-matched anchor (121 's' is 4 groups vs 0 words; 22 5 vs 6; 208 4 vs 2; the rest 0 or unmatched). This new anchor is
the only reason for this run; the instrument is FT4t's unchanged (ft4t_seg.py, now with `--anchors`/`--pins` options; defaults
reproduce FT4t; ft4s_seg solver, E, MAXLEN 12, <= 1 edit, sublimit 10 s, Pool(4)).

Segment S' (722 piece between consecutive cuts 605@74/49 and 279@101/64): **groups 75..100 (26 groups)**
`347 722 476 689 22 632 807 589 179 825 843 10 65 86 306 208 276 121 468 208 242 219 70 405 114 755`
and **slip words 50..63 (14 words, 77 letters)** "continuera de fournir secretement a cette princesse les secours qui se pourront derober le".

Variants (both registered, run in this order, each with X = ti and X = i):
- **P1 (primary, FT4s pin family unchanged):** pins 22 'de' (1 occurrence; 66 absent) + 722 = X.
- **P2 (secondary, every C code present in S'):** pins 22 'de', 208 'se' (2), 121 's' (1) + 722 = X.
Controls per variant per X: seed 3, n 40, (s) S' slip words shuffled vs S' groups; (g) S' group order shuffled vs S' slip; pins move with
tokens; unresolved counted E = 1. Gate per X (unchanged): PASS iff E_real(X) = 1 AND each control share <= 0.05 (<= 2/40);
E_real = 1 with a share > 0.05: NON-INFORMATIVE; E_real(X) = 0: FAIL for X (a proof, conditional on anchors, pins, slip expansion);
unresolved real: NOT SCORED. Controls are run only for an X with E_real(X) = 1, serially (no concurrent pools; FT4t's lesson).

Expectation stated before scoring: S' (77 letters / 26 groups) is about the length of f.266r S3 (75 / 31), which was NON-INFORMATIVE
(7/40, 3/40), and shorter than FT4t's S (193 / 62, NON-INFORMATIVE). NON-INFORMATIVE is the likely outcome; a FAIL (E 0) for one value
is the informative case this short segment can still give, since a proof needs no control.

Outcomes and what may move:
- Decisive = on P1, one value PASSes and the other has E_real = 0. Then a VERIFY flag line for a separate verifier and a rule-4 witness
  line in NOTES (f.206 ti; f.213 i as a ti-NOFIT; f.249 S' <value>). P2 alone (P1 not decisive) is reported, no flag.
- Grades: no key.tsv edit by this worker in any outcome. 722 is already C (f.206) under a logged rule-4 conflict; settling the conflict
  is a verifier's, not a count-level step (the brief's cap: count-level C at most, M otherwise; nothing here is count-level).
- Rule 3: if both values are NON-INFORMATIVE or both fit on P1, the [retired] entry for the one-edit family on the f.249 722 question
  stands, now with every count-matched C anchor in today's key used; it reopens only with a different instrument or new material.
Sizing: one UNREGISTERED draw (seed 99, (g), P1, X = ti) before the push, time only. Box 12:00-13:00 UTC, stop line 12:48.
Regression: `ft4t_seg.py --value ti --real` with defaults must still give FT4t's E 1 (checked after the push, reported).
