# HYPOTHESES -- moray-wood-1568

## Conflict: triangles in R9257 (nulls) vs the postscript (letters) -- GAPS11, 2 Oct 2026, logged per rule 4, not settled
- Witness 1: BL Add MS 4136 f.172 (DECODE R9257), key of Sir Henry Percy to Sir William Cecil, Norham, 22 July 1559 (docket).
  Its "Nullae" block lists x, +, an asterisk, an inverted, an upright and a right-pointing triangle as nulls (native-res crop read, GAPS11).
  Its letter table gives a = V, y; c = M; d = o; e = a marked x; f = + (also listed among the nulls).
- Witness 2: Aymeloglu's cryptanalytic key of the postscript (aaymeloglu/unsolved-ciphers moray-1568/key.json, commit d2800bb; grade S,
  not a period key): A (triangle) = a, Ab (triangle with bar) = i, V = f, M = m, x = e, t-shaped cross (L3.26) = t (M).
- Direction/date: witness 1 is Percy -> Cecil, 1559, English Border office; the postscript is Moray -> Wood, 13 July 1568, Scottish regent's
  secretary. Different sender, office and decade.
- Status: the two disagree on every shared shape that carries a value (triangle, V, M, x, +). This is evidence that R9257 is not the
  postscript's key, so no R9257 value is H for the postscript; the triangle conflict is recorded, not resolved by either witness.

## Conflict: R4930 P3 = Randolph-Sussex f.277r (period key, f.278) vs the postscript key -- GAPS12, 2 Oct 2026, logged per rule 4, not settled
- Witness 1: the clerk's decipherment on BL Cotton Caligula C II f.278 (DECODE R4932) of Randolph to Sussex, Edinburgh 5 July 1570 (f.277r = DECODE R4930 P3),
  values as listed by Bourdeau (dbourdeau/cyphersolver randolph1570/NOTES.md, credited): barred x = o, 4 = d, 3 = f (tailed 3 = a), looped o with tail = o, delta = t, cup u = h.
- Witness 2: Aymeloglu's cryptanalytic key of the postscript (key.json d2800bb, grade S): X (crossed x) = u, 4 = c, Z3 = o, M (o with tail) = m, A (triangle) = a, U = [the].
- Direction/date: Randolph -> Sussex, English ambassador at Edinburgh, July 1570; the postscript is Moray -> Wood, 13 July 1568. Different sender, office and date.
- Numbers: 0 of 6 comparable shapes agree (r4930/r4930_test.py part A; shape matches from glyph descriptions, not images). The 4-gram key.tsv test on run 1
  (N=111 matched of 331): -1.988, rank 0.432 vs 1,000 shuffled keys, 0.235 vs 200 sign-order shuffles; positive control at matched sparsity (postscript reduced
  to the same 8 labels, N=49 < 111): -1.753, 0.906 / 0.740 -- does not separate, so test B is a non-test (rule 3).
- Status: evidence that R4930 P3 is in a different key; no Randolph value is H for the postscript; no key.tsv value moved.

## H-no804: Bain ii no.804's cipher phrase is in key.tsv (pre-registered GAPS15-moray-wood-1568, 2 Oct 2026; untested, no leaf image)
- Rule fixed in no804/PREREG.md before any image: S = max LCS(decode, 16 spelling variants of Bain's "and says he must neidis haif
  it be on meinis or uthir") / length; PASS = S > p99 of 200 letter-shuffled cribs AND of 200 shuffled keys AND S >= 0.60.
- Matched control at N = 39-42 signs (no804/control.tsv): positive 1.000/1.000/1.000/0.975 at 0/10/20/30 pct sign error; false-pass
  (same phrase, shuffled key) 0.000 at every level. Reference: the R2989 line scores S 0.452 vs p99 0.475/0.425, FAIL.
- Status: untested (waits on ASKS row 103); run `python3 ciphers/moray-wood-1568/no804/no804_crib.py --score <leaf.tsv>`.
