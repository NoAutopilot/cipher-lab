# PREREG-TT-PAIR -- pass line for the --cipher-pair known-answer control (pushed before the control runs)

Written 8 Oct 2026, 22:5x UTC (date -u), by TT-PAIR (LANE TOOLS-TOMO, account 4), before
`tools/tests/cipher_pair_control.py` was run on the Servien fixture. Development so far used only fr17 corpus passages
(synthetic word drops/insertions), never the Servien text.

Instrument: `tools/interlinear_align.py --cipher-pair A B --out DIR` (Tomokiyo practice 7, servien.htm).
Case: Servien to Sabran 1632, BnF Baluze 155 f.123 / f.127, Tomokiyo's own break (servien.htm). Semi-synthetic: his two
printed plaintexts (fixture `tools/tests/fixtures/servien_1632_parallel.tsv`), his clear words left clear, each copy
enciphered with a homophonic key of his recovered key's shape (per-letter homophone counts of
`ciphers/decode-2754-bnf-baluze156-1636/key_servien_1632_letters.tsv`, 3 nulls, 3% null rate). No transcription of the two
real ciphertexts is on disk, so the shelf grade cannot be `proven` from this control: `controlled-only` at best.

Command: `python3 tools/tests/cipher_pair_control.py --seeds 10 --design both --null --out tools/tests/fixtures/tt_pair_control.tsv`
(seeds 1632-1641, default tool parameters, nothing tuned after this file).

Pass line (all must hold, for BOTH designs `same` = one key two encipherments, `indep` = two keys):
1. Servien mean precision of accepted A<->B equivalences >= 0.80.
2. Servien mean recall of true same-letter A<->B pairs >= 0.20.
3. Null (copy B = a different fr17 passage, same length and clear-word rate) mean precision <= 0.35, and the Servien
   MINIMUM precision over the 10 seeds is above the null MAXIMUM.
4. Servien mean crib accuracy (cipher token vs the other copy's clear letter, truly that letter) >= 0.85, and the
   opening (first 16 columns: "De cete sorte l'on" vs "{De ceste sorte} on", Tomokiyo's one-place shift) mean >= 0.85.
Why the null can fail differently (rule 3): the statistic is which A symbol aligns to which B symbol; with an unrelated
B text the co-alignment carries no letter identity, so precision falls toward chance (about 0.07), unlike a
shuffled-order null of the same text, which this is not.
Outcome wording: all four hold -> shelf grade `controlled-only` (semi-synthetic, passes); any fails -> `weak`, evidence
"controlled-only: failed <item>".
