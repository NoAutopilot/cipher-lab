LANE KX job 1b: KX-XMATCH2, fix tools/key_crossmatch.py until its positive controls pass, then re-run. Sonnet. Stall alarm $8.
Parent: LANE KX orchestrator session_01JPoYAFvVfraJibxQdQfrqp. Read .claude/briefs/runs/2026-09-25-lane-kx-COMMON.md first; it binds.
ROOM role: "LANE KX worker KX-XMATCH2 (Sonnet, <your session id>)". Predecessor: KX-XMATCH (session_019EFB6xfyrrFXaJMkNuh5Gu),
read KEY-CROSSMATCH.md, the tool, and its test first. Do not start over; repair.

Files you may write: tools/key_crossmatch.py, tools/tests/test_key_crossmatch.py, KEY-CROSSMATCH.tsv, KEY-CROSSMATCH.md,
tools/data/*_repo/, ROOM.md. Nothing else.

Why it failed: only 1 of 56 keys passed its own positive control. Two causes, fix both:
A. 29 keys could not cover their own ciphertext (coverage < 0.5 on the text they were built from). That is a tokeniser or
   key-adapter bug every time, not a property of the key. For each such key: print 20 of its own ciphertext tokens next to
   20 key codes, find the mismatch (leading zeros, dots/dashes, ranges like `12-13`, `a|b` alternates, symbol names,
   decode.json layouts not honoured, "code" column that is really the value), fix the adapter or tokeniser, re-check.
   Target: every key whose folder has a committed reading covers its own text at >= 0.8, or a one-line reason why not
   (e.g. key is a partial table by design). Where the folder has decode.json, tools/decode_key.py's own decoding is the
   reference: your decoded stream for (own key, own text) should match its output.
B. The "unrelated key of the same design" z is unmeasurable with 2-5 keys per design. Replace it as the second control
   with the calibrated test judge_plaintext.py already implements for language: score the decoded letter stream against
   (i) real-text windows of the same length from the key's language corpus (pass needs >= that distribution's 5th
   percentile) and (ii) letter-shuffled windows (pass needs > the null's 99th percentile). Keep z against the
   shuffled-key control (it works: z_sh >= 4 on 13 keys). Also report the decoded share of the letter stream that
   falls into dictionary words of the corpus (a cheap second signal).
New verdicts: `own`; `hit` = coverage >= 0.7 AND z_sh >= 4 AND passes (i) and (ii); `weak` = coverage >= 0.5 AND z_sh >= 3
AND passes (ii); `none`.

Positive controls, all three must pass before any other row is reported:
1. Own text: every usable key (after A) gets verdict `own`-quality numbers on its own text (z_sh >= 4, passes (i),(ii)).
   Report K of N; any key still failing is `unusable` with its reason.
2. Known reuse: the tool must flag as `hit` (or at least `weak`) the key-reuse pairs already established in the repo:
   ciphers/jan-van-nassau-1572-75/key_5549.tsv on the Lodewijk letters (4610 etc.), Lodewijk's key.tsv on
   jan-van-nassau-1572-75/ciphertext_5549_ps.tsv (J5S), and Brienne's key_brienne_1647/1651 across
   clair1067-brienne-poland-1646 and fr5160-letellier-1653 (the same tables in both folders). Grep NOTES.md for any other
   stated "reads under the X key" pair and add it. Report each known pair's numbers.
3. Negative: keys scored against ciphertexts of a different language or century (e.g. a 1570s Nassau key on the 1869
   RAH or 1781 Huntington texts) must come out `none`. Report the false-positive rate over all such pairs.
Then: KEY-CROSSMATCH.tsv (same columns plus pass_real, pass_null, dictword_share, known_pair yes/no), and KEY-CROSSMATCH.md
rewritten (<= 50 lines): controls table, then hits and weak rows EXCLUDING known pairs, each with its ciphertext's folder
status. Explicitly list these pairs' numbers even if `none`: rah-canada-1869 key vs the RAH N1 Morillo texts if on disk
(and reverse); willem-van-hessen-1567/siblings/ciphertext_1069 vs jan-van-nassau key_1572; la-garde-1577 vs the Nevers keys.
No network. Do not decode further or write in target folders. A hit is a candidate for the orchestrator, not a reading.
Push after controls pass and at the end. Final paragraph: first line "own K/N, known pairs P/Q flagged, false-positive
rate F; H hits, W weak (excluding known)", then hit rows, files touched, cost.
