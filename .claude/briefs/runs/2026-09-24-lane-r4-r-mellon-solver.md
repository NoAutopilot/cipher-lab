LANE R4 WORKER R -- Beinecke MELLON MS 29 pseudo-Elian cipher: control-first solve (Opus, cap $4; disk only; no subagents).
Target: ciphers/beinecke-mellon29-elia. Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md. Input: ciphertext.tsv (LANE R4 Q:
248 signs, 32 types, 58 words, word breaks kept) and NOTES.md (Bourdeau: simple/homophonic/progressive/Vigenere/Alberti failed on a
thumbnail transcription; the codex is Latin/Italian alchemy c.1525, "Lumen luminum").
1. Controls first (rule 3): synthetic ciphers of 248 signs, 32 types, the same word-length profile, in Latin, Italian and German
   (alchemical prose where a corpus is on disk, else general), for monoalphabetic substitution (with homophones up to 32 types) and for
   a pigpen reading order variant; the solver (tools/homophonic_anneal.py or an existing word-aware solver in tools/) must read them.
   Record control_results.tsv.
2. Run the target under every design whose control reads > 60%. A reading must be continuous language across the word breaks; grade
   per token S (cryptanalytic with a control) or M; decode.json + key.tsv + tools/decode_key.py --check exits 0 if a reading exists.
3. Search log: phrase-search any reading on archive.org full text (<= 4 requests) and name what was not searched. Report what was found
   and where it was not found; do not classify novelty. NOTES.md "Solver (24 Sept 2026, LANE R4 R)". ROOM done: control and target numbers,
   and "for LANE V4: ciphers/beinecke-mellon29-elia reading ready" only if a reading exists.
