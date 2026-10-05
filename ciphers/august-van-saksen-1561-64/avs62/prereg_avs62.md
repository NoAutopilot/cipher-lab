# RUN6-AVS62 pre-registration (5 Oct 2026, written before any score was computed)

Target: WVO 74 (Willem -> August, Brussel 13 Aug 1562, SAD; sources/wvo/cipher-letters-2026-09-24.tsv row 74) = Rachfahl II.1
p.209 n.1 "Dresdner Archiv Locat 8510 (chiffrierter Zettel, d. Brüssel 13. August 1562)". Cipher on disk: ciphertext_74.tsv
(R21 native read). Key: key_74.tsv (C from f.19, the leaf's own decipherment). Rachfahl is an independent printed witness.

Crib (quoted span only, Rachfahl's paraphrase outside the quotation marks excluded): "Wir aber in diesen Niederlanden sind noch
still; zwar sind wir darum ersucht worden, haben's aber mit Glimpf abgeschlagen und möchten wohl leiden, daß unser König in
Hispania desgleichen auch tue". Cipher span: p3 l.9 idx 22 .. p3 l.13 idx 31 (located by the f.19-aligned word units in
pairs_74.tsv, i.e. located with the period decipherment, not with Rachfahl).

Normalisation (both sides identically; CLAUDE.md rule 3 notation lesson): lowercase; ä ö ü -> a o u; ß -> ss; y -> i; v -> u;
drop h; dt -> t; final d -> t (per word, before joining); ie -> i; collapse doubled letters; drop non-letters and spaces.
Word signs decode to their key_74 value (NL niderland, VmV konig, HISP hispanien, Wm frankreich, ZZ zu).

Statistic S: difflib.SequenceMatcher(None, decode, crib, autojunk=False).ratio() on the normalised strings.
Nulls (1000 draws each, seed 62):
  N1 shuffled key: key_74 values permuted across all 38 rows, decode the same span, S against the crib.
  N2 shuffled crib: the crib's words permuted, S of the real decode against it.
  N3 wrong span: every other window of 74's cipher (p3+p4) with the same sign count, S of its key_74 decode against the crib.
Gate PASS: S_real > p99(N1) AND S_real > p99(N2) AND S_real > max(N3).
Known-answer control (run first): the same S with the f.19 units of pairs_74.tsv over the same span as "decode" must exceed all
three gates too (it is the period text; if it fails, the statistic is a non-test and the target is not scored).
On PASS: each sign in the span whose key_74 value is matched letter-for-letter in the difflib alignment against Rachfahl gets
a second, printed witness (C, printed) -- counted per sign, beside its existing C from f.19. Signs not matched are listed, not
regraded. No grade on 53/57/126 changes from this job.
