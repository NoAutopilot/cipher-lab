# PREREG -- GAPS90-sufi-fiddle (account-4), 3 Oct 2026 11:1x UTC, committed before any scoring

Hypothesis (NOTES.md, Remaining gaps): the 7 lines of ciphertext_fig1.txt are Tausug written in Jawi-style Arabic
script (Kawashima via Bulliet 2021). Test: does a Tausug word list cover the transcription's consonant skeletons
better than the same transcription with its sign identities scrambled?

Lists (none committed; manifest.json only):
- L_PD (primary): Cowie, *English-Sulu-Malay Vocabulary* (1893, public domain), archive.org
  englishsulumala00cowigoog_djvu.txt. Every lowercase token of the vocabulary section (Sulu and Malay columns are
  not separable in the OCR, so Malay rides along; capitalised English headwords filtered). Noise in this list
  affects target and null equally; the positive control measures what it costs in power.
- L_NT (secondary): word types of the Tausug New Testament (Wycliffe 1998/2018, eBible tsg, **all rights reserved**:
  used locally for statistics only, never committed), with Revelation held out.
  Wiktionary's Category:Tausug_lemmas (CC BY-SA) was tried first: HTTP 429 twice, host left alone.

Skeleton: both sides reduced to strong-consonant classes b t d k(g,q) N(ng) n m l r s h j p; vowels, alif, hamza,
ain, waw, ya, w, y dropped. Cipher map: ha/ha2/kha=h, sin/shin/sad/tha=s, fa=p (Jawi pa), nga/ghayn=N, lamalif=l,
tooth = any of {b,t,n,s,nothing}; '?' suffixes stripped; groups containing OBSCURED excluded.

Statistic C3 (primary): per line, a dynamic-programming tiling of spans of 1-3 consecutive visible groups (a word
boundary must fall at a visible gap); a span scores its skeleton length L if L>=3 and the skeleton is in the list;
C3 = max covered consonants / all consonants. C2 (secondary): same with L>=2. Per-length breakdown: spans chosen
with L=2, 3, 4+, and singleton-group matches by L.

Null (can differ on the statistic): 1000 random permutations of the 13 consonant classes applied to the cipher
signs (sign identities scrambled, group structure and lengths kept). p = share of nulls with C3 >= target.
Not a shuffled-group-order control: order cannot change a bag-of-spans match much, and identities can.

Positive control (power): 20 chunks of held-out Tausug (Revelation, eBible tsg) rendered into Jawi-like groups
(break after alif/dal/ra/waw), each with the target's consonant count over 7 lines, at 0, 10 and 20 pct random
class substitution (bracketing the transcription's 18.5 pct err_2reader and 3.3 pct residual); each chunk scored
against its own 200-permutation null. Power = share of chunks with p<0.05.

Gate: target PASS for a list only if p<0.05 AND that list's power at 20 pct noise >= 0.8. Power < 0.8 at the
noise level that brackets the transcription = non-test for that list, whatever p is (rule 3). A PASS is "worth a
reader", never a reading (no tokens are graded by this test).
