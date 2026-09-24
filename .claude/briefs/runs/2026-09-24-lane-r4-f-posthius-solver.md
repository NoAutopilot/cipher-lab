LANE R4 WORKER F -- POSTHIUS 1614/1618 SOLVER: read both cipher passages with the keys on the leaves (Opus, cap $6; disk only).
Target: ciphers/trew-posthius-1614-18. Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md.
Input (revised 15:28 UTC: worker A was stopped at 2.3x its cap after both passes, before reconciling): passA.tsv, passB.tsv
(long format, lines 1614_note1-3, 1614_c1-c4 = the cipher block, 1614_key_top/_bot, 1614_crib1-2, 1618_left_top/_bot with
glyph codes G1-G9 from glyphs/atlas.tsv, 1618_right_top/_bot, 1618_spec1-8) and the orchestrator's scripted reconciliation in
recon/ (tools/reconcile_passes.py: 299/330 = 90.6% agree; recon/disagreements.tsv lists the 31 columns, crops in images/crops/).
Step 0: settle only the recon/disagreements.tsv columns from the crops (Opus looks at crops only for those), write ciphertext.tsv
and key_leaf_*.tsv from recon/ciphertext_draft.tsv, commit and push before any decoding.
1. 1614: decide the key's design from the leaf itself, testing both: (a) a keyword-mixed alphabet (plain a..z -> SALUTEM... order),
   (b) a two-row reciprocal table (each top letter swaps with the letter under it; 12 pairs). The design that reads the 4-line block
   as Latin (or German) is the one; show both outputs. Check the reading against the clear notes on the leaf (the "Fridericus
   Henricus ... recens natus Princeps" line and the "Eandem descriptionem ... Camerario" note) and say whether the clear line is the
   plaintext, a gloss, or unrelated.
2. 1618: which of the two key blocks reads the specimen lines; apply it; say which block is complete (letters covered) and which
   is struck through. The drawn-glyph block: map glyph codes to letters from its own top row; apply only if a passage uses glyphs.
3. key.tsv, decode.json (tools/decode_key.py; examples tools/tests/decode_configs/), reading files; grade every token: H where the
   leaf's own key gives the value, I for repairs, M uncertain. `python3 tools/decode_key.py ciphers/trew-posthius-1614-18 --check`
   exits 0. Give the counts.
4. Search log: note where you looked for a prior reading or print of these passages (NOTES.md check-solved list; add a phrase
   search of the decoded text on archive.org full text, at most 4 requests, >= 3 s apart). Report what was found and where it was
   not found; do not classify novelty.
NOTES.md section "Reading (24 Sept 2026, LANE R4 F)". ROOM done line: grade counts and "for LANE V4: ciphers/trew-posthius-1614-18
reading ready".
