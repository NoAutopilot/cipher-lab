# Independent re-derivation of the substitution key (L01-L14) and a decode attempt for L18/L19

## Method

Every (group, gloss) pair in lines L01-L14 of ciphertext.tsv was tallied by code. Empty
gloss cells and the stray punctuation artifacts (",", "=", "+") were dropped before
tallying; a two-letter gloss ("en", on code 60) and capitalised glosses that look like
proper-noun initials (M, N, P, A, L, K, T, E) were kept as literal tallied values, not
normalised. Bracketed shape codes ([triangle], [tilde], [blot], [X], [Z], [T], [circle],
[square]) were tallied exactly like numeric/prime codes. For each code the letter with
the most votes was taken as its value; a code whose top count is shared by two or more
letters was recorded as a genuine tie, value "[?]".

## Results

87 distinct codes appear across L01-L14.

- **38 unanimous** -- every occurrence of the code glossed the same single letter
  (includes codes seen only once, e.g. )10=e, )4=y, 18=g, 22=M, 8)=P, as well as codes
  seen several times with total agreement: 3=o (5/5), 13=b (2/2), 21=L (2/2),
  35=b (2/2), 43=l (2/2), 68=o (2/2), 81=a (2/2), 93=r (2/2)).
- **27 clear-majority-but-mixed** -- more than one gloss letter occurs, but one is
  ahead, e.g. 56 -> a (7/10, vs r=2, v=1), 60 -> e (7/11, vs en=1, a=1, s=1, n=1),
  89 -> n (5/7, vs e=1, t=1).
- **22 genuine ties**, no majority letter, value set to "[?]": )3 (t/o), 11 (a/s),
  14 (l/e), 24 (o/i/l), 25 (a/u/p), 26 (q/u), 29 (a/t), 31 (d/x), 33 (z/n),
  34 (s/d/a), 36 (c/r/e), 45 (n=2/e=2, with N=1 a minority third value), 49 (r/n/u),
  5 (e/s/d), 51 (t/a/e), 65 (y/a), 82 (e/d), 94 (q/i/s/r/e, 5-way), 95 (e/a),
  96 (o/n), 98 (y/a), [blot] (M/E).

Full key: `rederivation_key.tsv`.

## L18 / L19 decode attempt

L18 (codes 61, 68, 2), 88, )8) decodes to **`?orma`** -- code 61 never occurs in
L01-L14, so it is unresolved; the other four codes are covered (68=o unanimous,
2)=r majority 3/4, 88=m unanimous, )8=a majority 2/5, itself a weak plurality over
l/c/m). "?orma" is one letter short of plausible Spanish (forma, norma).

L19 (23 codes) decodes to **`ad???An?o?yadea?banyP??`**. Five positions resolve to
"?": code [n] never occurs in L01-L14 at all; codes 24, 34, 51, 65 (twice) and 11 are
genuine ties in the key. The result does not read as coherent Spanish to me -- it is
dominated by gaps and isolated letters rather than recognisable words, so I would treat
this as an inconclusive reconstruction from the L01-L14 sample alone, not a reading.
