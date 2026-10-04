# ARM-SORTER (account 3 worker) -- 4 Oct 2026 16:0x UTC (account-3 orchestrator; owner: "let's do the transcription of Tomokiyo's target, give me that link")
Target: ciphers/armstrong-madison-1808 (Armstrong to Madison, 20 Feb 1808; NARA M34 roll 14 frames 0030-0033, public IIIF images on disk
in images/, manifest.json). The numeral groups are manuscript-checked (ARM-TR/ARM-TR2); the weak part is the SHORTHAND MARKS between them:
two one-reader transcriptions disagree by about 16% in mark count (ciphertext_ms.txt 218 marks in 28 runs vs codex-2026-09-27b/glyphs.tsv
257 tokens in 28 fragments; NOTES "Campaign step H3"). The owner will settle the marks by eye in the sign sorter, as on Birago (his piles
beat the machines 98/108). Build (do NOT publish) a sign-sorter page for the marks.
1. Locate every shorthand-mark run on frames 0030, 0031 (and 0033 if it holds the letter's end; 0032 is a duplicate scan of 0031 -- use
   the cleaner copy, say which) from ciphertext_ms.txt / layout.md / ARM-TR crops. Cut line strips with tools/iiif_lines.py --image (disk
   only) and segment marks into tiles with tools/glyph_atlas.py segment (try --cursive; check the debug overlay; a mark is often one
   connected stroke but may touch a neighbour -- prefer over-splitting, the owner merges). Numerals stay OFF the page.
2. Initial piles: cluster the tiles by shape (glyph_atlas atlas/cluster), value-blind, arbitrary names (M01, M02, ...); no shorthand
   system values anywhere on the page (sorter rule). Focus box ("Check these first", <= 30): tiles that sit between two clusters, and
   tiles where ciphertext_ms.txt and glyphs.tsv disagree on the count at that spot.
3. Inputs + build.sh + README under ciphers/armstrong-madison-1808/sorter/ (README: exact build and apply commands; how settled labels
   replace ciphertext_ms.txt's mark tokens; the 16% figure and what the owner's sort is meant to settle). Build the HTML in your scratchpad,
   render it headless with no script errors (tools/sign_sorter/browser_tests/test_qa.js on the built page), commit inputs only; the
   orchestrator publishes. Page under ~4 MB.
Disk only, no network (images on disk). Model Opus 5.5; at most 2 Sonnet vision calls for checking the segmentation overlay. Cap USD 6,
box 60 min (stop before a step that would cross 80% of either). ROOM claim/done via tools/room.py. Do not change ciphertext files or
any reading.
