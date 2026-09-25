LANE KX job 3f: KX-LATHCT1, breadth-lane first cheap test on specs/colbert26-lathuillerie-1644.json. Sonnet. Cap $3 (CLAUDE.md
pipeline 3a; the orchestrator interrupts at $5). Parent: LANE KX orchestrator session_01JPoYAFvVfraJibxQdQfrqp. Read
.claude/briefs/runs/2026-09-25-lane-kx-COMMON.md first; it binds. ROOM role: "LANE KX worker KX-LATHCT1 (Sonnet, <your session id>)".

Run only the spec's cheap test 1, nothing else: no transcription, no crib test, no anneal. No network.
Question it answers for this lane: is the La Thuillerie cipher (canvases 20, 21, 27, 30 in ciphertext.tsv) the same key family
as a key we hold, and is it one alphabet or two?

1. Use only tokens the two passes agree on (ciphertext.tsv vs passB.tsv; state the count used and the count dropped).
2. Profiles for: (a) canvases 20+21+27 (mixed digits and letter-codes), (b) canvas 30 (2-digit only), and for each of our keys'
   own ciphertexts of the same office: ciphers/clair1067-brienne-poland-1646 (key_1646 and key_brienne_1647 texts) and
   ciphers/fr5160-letellier-1653 (key_1659 text). Profile = sign classes (1/2/3-digit numbers, bare letters, letters with
   marks), share of each, distinct signs per 100 tokens, repeat rate, index of coincidence on the sign stream, and the
   overlap of the sign inventories (Jaccard) with each key's own code set.
3. Matched control (rule 3, match the design): for each pair compared, draw 200 synthetic texts of the same N from a mixed
   nomenclator of the same K and class shares (random code->value assignment, French plaintext from tools/data/fr16 encoded
   through it); report where the observed overlap/IC sits in that distribution (percentile). Also: two disjoint synthetic
   texts from ONE synthetic key vs from TWO keys, same N and K, to calibrate what "same key" overlap looks like at this N.
4. Verdicts, each with its two numbers (observed vs control): (a) vs (b) same alphabet or not; (a)/(b) vs each held key:
   same key family / different / cannot tell at this N. Write them into the spec's cheap_test_done (target number, control
   number, verdict, date) and a short NOTES.md section "KX-LATHCT1 (25 Sept 2026)". Script under
   ciphers/colbert26-lathuillerie-1644/ct1_profile.py, deterministic (fixed seed), re-runnable.
Files: specs/colbert26-lathuillerie-1644.json (cheap_test_done only), ciphers/colbert26-lathuillerie-1644/{ct1_profile.py,
ct1_results.tsv,NOTES.md}, ROOM.md. Push with `python3 tools/room.py --push <paths>` without committing first; confirm on
origin/main. Final paragraph first line: the verdicts with their numbers.
