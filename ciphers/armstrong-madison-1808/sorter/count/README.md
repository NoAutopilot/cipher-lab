# Armstrong 1808 mark count (4 Oct 2026, account-3 orchestrator)

Owner's ask, 4 Oct 2026: the mark sorter is hard ("many signs look very similar"); a counting-only page instead.
Published https://claude.ai/artifact/TMbzp2zyengn2XufZRJSXP (private, db; board card arm-marks-count).
27 cards, one per passage in `../passages.tsv` (15 where ciphertext_ms.txt and codex glyphs.tsv disagree first), each
run shown in place on its NARA frame with the run box in red. The owner gives a count, "can't tell", or a note; the two
transcriptions' counts are not shown (blind third reader).

Build: `python3 ciphers/armstrong-madison-1808/sorter/count/build_count_page.py OUT.html` (disk only).
Read answers: ArtifactData list, collection `counts` (doc id = passage: count, unsure, note, updated); compare with
`ms_marks` / `glyph_tokens` in passages.tsv. The owner's count is a third reader, not ground truth.
