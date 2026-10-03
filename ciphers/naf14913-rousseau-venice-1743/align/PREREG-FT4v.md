# FT4v pre-registration (account-4, 3 Oct 2026, written 13:3x UTC by the clock, pushed before any transcription pass and any score)

Step (FT4u's Verdict): f.252r (Gallica btv1b525174513 canvas f517), 15 numeral groups at the foot of Lorenzi's letter of 6 June
1744 with an interlinear clear gloss in a lighter hand. Crops: `tools/iiif_lines.py --image images/f252r/src_f517_698_2951_3956_2620.jpg
--out images/f252r --prefix f252r --centres 1190,1471` (L01 = gloss + first numeral line, L02 = second numeral line; two native
segments each, <= 2400 px, 150 px overlap). Two blind Opus 5.5 passes (one subagent call each, crops only, no key, no prior reading)
+ one reconciliation by this worker against the crops.

Facts known before this PREREG (counts, no solver run): FT4u's one-look M reading has 15 groups, all distinct, none with a C value
in key.tsv; three carry key.tsv M values (188 'lar', 121 'ons', 10 'a'); 527/253/767/369/213/807 occur elsewhere in the
transcribed ciphertexts without a key value. So the pair has NO C pin and NO repeated code: the FT4s/FT4u statistic E with C pins
alone is satisfiable by construction (15 free groups, MAXLEN 12) and is NOT run as a gate (rule 3: a control could not differ).

Text under test (fixed now): the reconciled gloss, letters only, lower case, accents dropped, with abbreviations expanded to the
full word the cipher would encode (PX-BRODEC lesson): a superscript-contracted 'Gnal' -> 'general', 'pl.s'/'p.s' -> 'plus', a
numeral -> its French word ('3' -> 'trois'). Primary = expanded text; the literal text (as written) is a secondary readout, reported,
licensing nothing on its own. Groups = the reconciled 15 (or however many the reconciliation settles), in reading order.

Statistic (registered): E from `align/ft4s_seg.py` solve_pins/E unchanged (<= 1 edit, MAXLEN 12, sublimit 10 s, Pool(4)), with
pins = one M value at a time, then all three together:
  P188 = {188: lar}, P121 = {121: ons}, P10 = {10: a}, PALL = all three.
Controls per pin set, seed 3, n 40: (s) gloss words shuffled / real groups; (g) group order shuffled / real gloss; unresolved = E 1.
Gate per pin set: PASS iff E_real = 1 AND each control's E=1 share <= 0.05 (<= 2 of 40) -- the M value is then supported by this
pair (an S-grade candidate needing a second word, rule 4; no grade moves here). E_real = 1 with a share > 0.05: NON-INFORMATIVE
(expected for 'a', a common substring). E_real = 0: the M value is proved inconsistent with this pair within one edit -- a rule-4
dispute noted against the M value (second such for 188/121 after FT4u S2), no key edit. Unresolved real: NOT SCORED.

C-grade readout (registered): a code gets a C candidate from this pair only if the alignment is unambiguous, i.e. exactly one
chunk is feasible for it across the real-pair solutions under PALL-or-no-pins with <= 0 edits, enumerated by forcing each
alternative; with 15 free groups over ~50 letters this is expected to fail for every interior group -- reported as counts. A C
candidate disagreeing with key.tsv is a rule-4 conflict logged in NOTES, not merged. key.tsv gains no row this step unless
unambiguous; never a grade change on an existing row.

Box 13:36-14:16 UTC, stop line 14:08. Cap USD 5; vision units 3 (2 passes + reconciliation), ~USD 0.5 each.
