LANE KX job 3c: KX-LATHKEY, native-resolution gloss check and transcription for ciphers/colbert26-lathuillerie-1644. Sonnet.
Stall alarm $8. Parent: LANE KX orchestrator session_01JPoYAFvVfraJibxQdQfrqp. Read .claude/briefs/runs/2026-09-25-lane-kx-COMMON.md
first; it binds. Also .claude/briefs/transcription.md. ROOM role: "LANE KX worker KX-LATHKEY (Sonnet, <your session id>)".

Intake gate: the folder's check-solved verdict is `open` (Négociations secrètes 1725-26 vols 1-4 full text and APW online
full-text search read); accepted by the orchestrator 25 Sept 2026 08:25 UTC. Read the folder's NOTES.md and leaves.tsv first.

Files you may write: ciphers/colbert26-lathuillerie-1644/ only (new files; NOTES.md new section "KX-LATHKEY (25 Sept 2026)";
update leaves.tsv's gloss column), ROOM.md. Only you fetch from Gallica in this lane now: one request at a time, >= 1.8 s,
<= 200 requests; keep the folder under 30 MB (shrink your own reference copies, keep crops of cipher lines).

1. Gloss check. For each of the 11 enciphered leaves (canvas 20-21, 26, 27, 30-32, 33, 35-36, 39-40, 47-51, 54-56, 62-63),
   fetch the cipher-bearing regions at native resolution (tools/iiif_lines.py or IIIF region crops) and record whether a
   second hand has written a decipherment (interlinear, marginal, or on a separate leaf). Update leaves.tsv.
2. Transcription, two independent passes (two Sonnet subagents, each sees only the crops, never the other's output), of
   every cipher group on every enciphered leaf, with its clear-text context (the few clear words before and after) and,
   where present, the gloss text over it. Tokens: numerals, letters with marks (e.g. zz, w'), and any symbol, as seen;
   never repair. Reconcile with tools/reconcile_passes.py; settle disagreements from the image yourself. Output
   ciphertext.tsv (leaf, line, token_index, token, context_before, context_after, gloss_over) and disagreements.tsv.
3. Period key from the gloss: align glossed groups with their gloss words (canvas 20-21 and any other glossed leaf) into
   key_period.tsv (code, value, grade C, source canvas/line, note). A code whose gloss is ambiguous is M. Report how many
   distinct codes the gloss fixes and what share of all tokens on the 11 leaves those codes cover.
4. Stop there: no key applied to the unglossed leaves, no reading. The orchestrator briefs the key test (key_period.tsv,
   clair1067's key_1646.tsv, key_brienne_1647.tsv, with a shuffled-key control) from your files.
Report what was found and where it was not found; do not classify novelty. Finish per COMMON: final paragraph first line
"G of 11 leaves glossed; T tokens transcribed (agreement A%); key_period.tsv K codes covering S% of tokens".
