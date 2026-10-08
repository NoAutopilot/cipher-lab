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

## Addendum, 8 Oct 2026 ~23:00 UTC (date -u), before the run: a REAL two-copy case on disk

After the Servien control above had run (result: all four items held, both designs), a real two-copy ciphertext with a
known answer was found on disk: BnF Espagnol 132, Philip II to Vargas Mexia, 19 Sept 1578, f.89r-f.91r and its duplicate
cipher copy f.93r-f.95r (`ciphers/es132-vargas-mexia-1578/`, both transcribed, key Cp.30 from Tomokiyo's cp30.png in
`key.tsv`). One key, two encipherments by the clerk; about 4% of aligned pairs are homophone/notation variants, the rest
identical tokens, and the two readings carry ~9% reader error each (dup_align_summary.json). Harness:
`python3 tools/tests/cipher_pair_es132.py --out tools/tests/fixtures/tt_pair_es132.tsv` (no key given to the tool).
Pass line, all must hold, for shelf grade `proven` (else the grade stays `controlled-only` from Servien, with this case's
numbers in evidence):
1. precision of accepted equivalences (both symbols decode the same under Cp.30) >= 0.80;
2. at least 10 accepted NON-identical pairs (a symbol in one copy equated with a different symbol in the other: the
   homophone identification practice 7 is for), with precision >= 0.60;
3. null (copy B = the other Cipher 3 letters on disk, same key and hand, different text, cut to the same length):
   precision at least 0.30 below the real case's;
4. column agreement with align_dup.py's key-assisted alignment (dup_align.tsv) >= 0.80.
Caveat stated now: the two copies here are mostly the same tokens, so items 1 and 4 are easier than on independently
enciphered copies; item 2 is the one that tests homophone discovery.
