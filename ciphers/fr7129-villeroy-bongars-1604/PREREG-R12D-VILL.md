# PREREG R12D-VILL (6 Oct 2026, written before any scored run; account 4, LANE LANE-RUN12-account-4)

Job: decode f.268 (`ciphertext.txt`, the transcription of record, 13 lines; and `ciphertext_v2.txt`, verso only,
blind glyph-matched) using ONLY key v3's high-confidence cells; every other token `[MARK]`.

**High-confidence set (fixed now):** rows of `keys/key_f275_v3.tsv` with flag `confirmed` or `confirmed-unclear`
(the f.275 period-key value of record agrees with the clerk-alignment majority, two independent witnesses) and
count >= 2. Nulls and the doubling sign are not in it (no row carries those flags). Secondary set, reported beside:
the same plus every row with unclear=0 and count >= 2 (k=n, Z=s, x=a, a=s, 20=e, 5=o, 61 la, 76 mil, ^16 sa).

**Grades (rule 4), per decoded token:** H only where the cell's clerk agreement >= 0.6 AND both blind passes saw the
token (`agree` = AB in ciphertext.txt); every other decoded token M; `[MARK]` tokens ungraded (U). No C or S is
claimed (the clerk lines are siblings, not this letter; no control-backed cryptanalysis of this letter).

**Statistic:** letters decoded from the set form runs between `[MARK]`s (a word code is its own run). Score =
length-weighted mean log10 4-gram probability per letter (tools/judge_plaintext.py NgramModel) over runs of >= 4
letters. Corpora: fr16 (`LANG_CORPORA["fr"]`, c.1560-1615, nearest in era) primary; fr17 (1617-1644, diplomatic
register) reported beside.
**Control (can vary on this statistic):** 200 class-shuffled restricted keys, seed 20261006 -- the restricted set's
letter values permuted among its letter signs, word values among its word signs. Coverage and run positions are
identical by construction; only the letters in the runs change, which is exactly what the score measures.
**Gate:** "restricted decode carries language signal" only if z >= 3 AND rank 1 of 201 on fr16, and the fr17 z has the
same sign. Otherwise logged "no signal at this coverage" -- a non-reading, not a key negative (the transcription is
the known weak leg, VB-KEY).
**Expected-precision figure (descriptive, not a gate):** sum(count x agree)/sum(count) over the set's cells as used
in f.268, i.e. how often the clerk alignment says these cells' values are right.
**Rule 7 judge:** `tools/judge_plaintext.py` on the run text (runs joined by spaces) with a scratch spec, fr16 and
fr17; reported whatever it says. Expected FAIL (fragmentary runs); a FAIL here is not evidence either way.
Status stays `blocked` unless rule 5 says otherwise.
