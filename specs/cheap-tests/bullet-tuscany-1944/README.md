# Cheap test 1: bullet-tuscany-1944

Tests whether any key of a named family (Vigenere, Beaufort, variant Beaufort, simple
substitution) maps the 44-letter cipher body `CBFUKYYEVOZILOOZVNCWJKQRSAWBYZUGYTZWYBATRSUA` to
the forum-claimed plaintext `THEYTHROWGRENADESWEPULLPINSANDTHROWBACK`, with a matched control
(the same claimed plaintext enciphered under a real random key of each family, same checks run
on the result). Script: `run_test1.py`. Full numbers: `test1_output.json`.

## Length check (decisive)

Cipher body: 44 letters. Claimed plaintext: 39 letters. Mismatch: 5.

Implication: Vigenere, Beaufort, variant Beaufort and simple substitution are all
length-preserving (one ciphertext letter per plaintext letter). With 5 more cipher letters than
claimed plaintext letters, **no key of any of these families can map the full 44-letter body
onto this 39-letter plaintext under any of them** -- 5 cipher letters have no plaintext
counterpart at all. This confirms Schmeh's prose rejection mechanically, not just on
plausibility grounds; strictly speaking the forum "solution" fails before any key search even
starts.

## Fallback probe: does a 39-letter window of the body fit anyway?

In case the poster silently dropped 5 cipher letters (treated as extra metadata), the script
scans all 6 contiguous 39-letter windows of the 44-letter body against the claimed plaintext,
for each family: derives the per-position key letter, scores periods 1-20 by majority-vote
consistency per residue class, and (for MASC) checks whether the cipher-to-plaintext letter
mapping is consistent and injective.

**Matched control**: for each of 3 seeds, the same 39-letter claimed plaintext was enciphered
under a real random key (period 3-7 for the three polyalphabetic families, a random bijection
for MASC), and the identical script run on the result.

| family | target best score, any of 6 offsets | control recovered score (3 seeds) | control finds true period? |
|---|---|---|---|
| vigenere | 0.590 | 1.0, 1.0, 1.0 | yes, all 3 |
| beaufort | 0.564 | 1.0, 1.0, 1.0 | yes, all 3 |
| variant_beaufort | 0.590 | 1.0, 1.0, 1.0 | yes, all 3 |

MASC: target minimum violations (any of 6 offsets) = 37 of 39 cipher-plaintext pairs; control
violations (3 seeds) = 0, 0, 0.

Calibration note: the target's best scores above (0.56-0.59) come from period **20**, not from a
short period -- at short periods (1-7, where the control's true keys sit and where a real WW2
hand cipher would plausibly sit), the target scores only 0.08-0.31 across all 6 offsets, close to
chance. The rise near period 20 is an artifact of small residue-class sizes (39 samples over 20
classes leaves ~2 samples per class, so a same-by-chance "majority" is common) -- exactly why the
control matters: a real periodic key is recovered near 1.0 *at its true (short) period*, and the
target never comes close to that at any period or any offset.

## Verdict

Target and control side by side, per family, above: control cleanly recovers its planted key
(period found in all 3 seeds, score 1.0; MASC 0 violations) under the identical script: the
method works. The target shows no comparable consistency at any of the 6 possible 39-letter
alignments, in any of the four families, at any period 1-20 (best 0.564-0.590, all from the
degenerate high-period end, vs control's clean 1.0; MASC 37-39 violations of 39 pairs vs
control's 0). Combined with the decisive length mismatch (44 vs 39) that rules out a full-body
mapping outright: **no key of any of these families maps the 44-letter cipher body to the
claimed plaintext**. This closes the rejected forum claim mechanically rather than leaving
Schmeh's rejection as prose-only, per the brief. This does not test other cipher families
(candidates named in the spec: M-209, M-94/M-138) against a *different*, undetermined plaintext
-- only the specific rejected claim against this specific ciphertext.

M-209-style check: subsumed by the Beaufort-family periodicity scan above (an M-209 keystream is
Beaufort-like; testing for any fixed period 1-20 is the "at minimum" bar named in the brief). Not
pursued further for cost: 39-44 derived-keystream letters are far too few to show the M-209's own
pin/lug periodic structure (which needs a much longer stream to distinguish from noise), so no
stronger claim is made either way.

25 Sept 2026, LANE B2 worker bBUL (Sonnet). No network, no subagents.
