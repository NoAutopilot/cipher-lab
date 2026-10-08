# PREREG-D1A-F68 (8 Oct 2026, 06:2x UTC by date -u; worker D1A-F68, LANE DEFAULT-account-1-20261008-0540)

Written and pushed before any score is computed.

Question: do key_1659's rows (key_1659.tsv as committed at ab0a80f3a, built from the f.86/f.88 + f.87 pair only) read the f.67
cipher (ciphertext_f67.tsv, 24 Sept passes) in agreement with its clear text on f.68r (dechiffre_f68.txt, pass A reconciled
with blind pass B, 24 Sept)? A second-letter test of the key, independent of align_f67.py (whose EM keeps key_1659 counts as
pseudo-counts and so cannot test the key).

Material: already on disk. The f.68r second blind pass already exists (dechiffre_f68_B.txt, 24 Sept, 179/199 words agree,
differences settled on the image), so no new transcription call is made.

Statistic (per-aligned-token agreement): each of f.67's three cipher stretches (cut at its clear words, as align_f67.segments)
is decoded token by token with key_1659's modal value (codes absent from key_1659 and the null 0 contribute no letters and are
not scored). The decoded letter string is globally aligned (Needleman-Wunsch, match +2, mismatch -1, gap -1) to the matching
f.68r stretch, normalised as align_f86.norm. A scored token agrees when every one of its letters is aligned to an identical
clear letter. S = agreeing scored tokens / scored tokens, pooled over the three stretches.

Control: the same decode aligned to the f.68r text with its words shuffled within each manuscript line (and within each
stretch where a cut falls mid-line), same letters, same length, same symbol count; 1000 shuffles, seed 20261008. Word order
changes the alignment, so the control can differ from the target on S (rule 3 orthogonality paragraph).

Gate: PASS if S(target) > p99 of the control. PASS licenses "key_1659 reads a second letter (f.67/f.68r) above a
shuffled-order null"; it changes no key row and no grade (align_f67's C grades stand on their own). Per-code agree/total is
reported descriptively only; no row is revised from it. FAIL: logged in HYPOTHESES.md as a FAIL of this instrument at this N.
