# GAPS19-na-suriname-map-1781 (account-4), 3 Oct 2026 -- pre-registration for the 4.VEL 2077 text block (Plan van de fortress
# Zelandia, 1781), written and committed BEFORE either blind pass was run or merged and before any 2077 token was decoded
# (no ciphertext_2077_legend.tsv exists at this commit). Same shape as GAPS18's 2046 pre-registration (ebfcc3d3).

Material: one native IIIF region 6650,150,2450,2050 of 10711x5110 (images/2077_legend_native.jpg): title cartouche 3 lines, the
plain heading "Explicatie der Signatuuren", the mixed plain/cipher legend a-z (about 15 rows), and the line below it. Crops
images/crops_2077_leg (tools/iiif_lines.py, command in NOTES.md GAPS19). Not covered: the No.1-3 lines below the region, the
left inset's "Explicatie" list and Nota/Remarque, river and land labels.

Key: key_period_codes_nieuw.tsv as committed (Nieuw Secreet Alphabet, NA 1.05.03 inv. 86 scan 0003), plus
exceptions_nieuw_image.tsv only for the tokens it already names (none on 2077). No key row is added from 2077 in this job.

Control 1 (primary, unchanged from GAPS14/16/18): control_prereg_vocab.py, vocab_prereg.txt unchanged, statistic unchanged, seed
14, 1000 draws, on the 2077 file ALONE: `python3 control_prereg_vocab.py 1000 key_period_codes_nieuw.tsv ciphertext_2077_legend.tsv`.
Pass rule: real > max of BOTH nulls (shuffled-value, shuffled-order) with 0/1000 null draws >= real. Either null reaching real = FAIL.

Control 2 (headroom, rule 3 gain-gate clause; new, committed here): GAPS18's 2046 result (real 3 vs shuffled-order max 3) shows
the statistic can sit at its floor on one legend. Before the primary result is read as a negative, control_headroom_2077.py
scores the sheet's OWN plain legend words (w: tokens) with the same vocabulary, statistic, seed and shuffled-order null, at the
target's cipher-token N (or whole, if shorter). If that genuine 1781 plain text does not clear its own null (real > max, 0/1000),
the gate has no headroom here and a primary FAIL is logged as a NON-TEST, not a negative. A primary PASS stands either way.
Pre-decode expectation from data on file: 2039+2061 gave 13 hits in ~750 tokens vs null max 4; 2046 gave 3 in 362 vs max 3.

Judge: specs/na-suriname-map-1781.json names nl; tools/judge_plaintext.py has no nl corpus wired, so the judge is expected not
to run; output pasted either way, no PASS claimed. Building an era-matched nl18 corpus is named as a step, not done here.
Grading: decode_key.py's own (H sheet's own sign, M shape name or two-valued, U unkeyed); transcription H/M in the note. No S.
Vision calls: 2 blind passes + 1 blind reconciliation (Opus subagents), at most 3.
