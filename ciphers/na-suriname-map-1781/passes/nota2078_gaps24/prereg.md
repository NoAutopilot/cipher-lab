# GAPS24 pre-registration: secondary pairs of the other 2077 cipher entries vs nota2078.tsv (3 Oct 2026, account-4)

Written 3 Oct 2026 about 05:06 UTC (clock read 05:04 before writing), committed and pushed before any secondary score is
computed. Follows passes/nota2078_gaps23/prereg.md ("Any further pairing found after transcription is SECONDARY: reported,
never gating") and its regrade rule. Script: `score_secondary.py` (this folder), which imports GAPS23's `score.py` unchanged
(same entry extraction, normalisation, alignment and statistic A).

## Pairing (fixed now, before any A for these pairs is computed)

Basis: the 2077 entry's word-level M segmentation already committed by GAPS20 (reading_2077_legend_nieuw.txt, as quoted in
AUDIT.md item 4 step 1) and 2077's own plain words, matched to the 2078 Nota entry whose head noun is the unique 2078
counterpart. One-to-one; 2078 entries used by the GAPS23 gating pairs (b, c, d, k, n) are not reused; an entry whose head noun
has several or no 2078 candidates is excluded, not guessed. **Caveat, stated before scoring:** this choice is not letter-blind
(it reads the decoded words), so a pair's A is biased upward against a label-shuffle control; for that reason the regrade rule
below needs both controls per pair, and no pooled secondary figure gates anything.

| 2077 entry | GAPS20 segmentation (M) | 2078 entry | 2078 text |
|---|---|---|---|
| a | t[g/l]opeernenent ~ "envelopement" | B | Envelopement van aerdewerken |
| e (first run) | nee[g/l]trpieysen ~ "neeger...huysen" | h | gebouw waarin ... d Neeger gevangenhuysen, & ... Geweer kamer ... |
| k | d.toeannateeria[g/l].en ~ "dito ... materialen" | s | Magaçyn van Materialien |
| l | waqternoo[g/l]e ~ "water(koorn)molen" | t | Waer Koornmolle |

Excluded (reason): b, i, x, gamma (magazyn: several 2078 magazyn entries g, i, o, q, r, s); c (secretarye: no 2078 entry);
d (paardestal en koetshuys: none); m (wooning: several, k v w); o (sluys/water...molen: competes with l for t; l is the
unambiguous one); y-umlaut entry (arsenaal / geweermakers winkel: none unique); delta (brandspuiten: none); eta L20 (dispositie
der batteryen: heading, not an entry of the Nota); the title lines (not legend entries).

## Statistic and controls (per pair; GAPS23's two controls)

A = H tokens aligned to the identical 2078 letter / H tokens (GAPS23 score.py `stat`). Per pair, 2000 draws each, seed 20261003:
- N1 label shuffle: the 2077 entry aligned to a 2078 entry drawn uniformly from all 27 transcribed entries other than its partner.
- N2 value-shuffled key: a random permutation of the 26 letters applied to the entry's token values, aligned to the true partner.
Both can move A (N1 changes the text, N2 the letters).

## Rule

A pair is **supported** when its A > its own N1 p99 AND > its own N2 p99. Pooled A over the four pairs and pooled controls are
reported, descriptive only. Regrade (GAPS23 rule, applied only within supported pairs): an M or U token placed on a 2078 letter L
(not a gap) becomes C with value L when (i) for M, L is one of its listed values (an outside letter changes nothing and is
logged), and (ii) the nearest three H tokens on each side inside the entry (fewer at an entry boundary, at least two in all) each
align to an identical 2078 letter. Written to exceptions_nieuw_image.tsv (grade C, reason naming GAPS24 and the 2078 entry);
`tools/decode_key.py ciphers/na-suriname-map-1781 --check` must exit 0. New H/C/M/U and M+U reported. AUDIT.md class untouched.
An unsupported pair regrades nothing and is logged with both control numbers.
