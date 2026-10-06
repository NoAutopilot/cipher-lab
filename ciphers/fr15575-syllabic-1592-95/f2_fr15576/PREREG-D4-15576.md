# D4-15576 pre-registration, fr.15576 f.2 (canvas f8 of btv1b9063777v), 6 Oct 2026 13:3x UTC (by date -u)

Written and pushed before any alignment run and before the worker has seen any pass output (the four blind Sonnet passes
were launched at 13:30 UTC and had not returned when this file was written). What the worker had seen: the 1600 px
overview of canvas f8, the --debug overlay of the body region (21 cipher lines with light-ink interlining), and four
crops opened to check the cut (f2i_L13_s1, f2i_L23_s2 gloss; f2c_L07_s1 cipher; f2g_L12_s2 superseded cut).

Material
- Body region 5650,1700,3230,3100 (native px), 21 cipher lines C01-C21, each with one gloss line G01-G21 directly above it.
  The 5-line letter-sign block above the body (and its own gloss) is out of scope.
- Crops: `tools/iiif_lines.py --centres` alternating gloss/cipher centres, `--mask-neighbours --mask-margin 45`; odd bands
  (f2i_L01, L03 ... L41) = gloss G01-G21, even bands (f2i_L02 ... L42) = cipher C01-C21.
- Reads: gloss 2 blind Sonnet passes (A plain crops, B contrast views); cipher 2 blind Sonnet passes; one reconciliation
  per text by the worker on the crops (tools/reconcile_passes.py for the cipher). A token the reconciliation cannot settle
  stays doubtful ('?' in the group). If the cipher passes split on > 10% of groups, no third pass: the lines whose groups
  agree after reconciliation are aligned, the rest go to a sorter focus list.
- Gloss gaps: an unread gloss word [..] is written as '???' and run with `--wildcard ?` (positions, never evidence).
- Cipher letter/sign tokens (y, p, q, k, V, sh, uu, +): kept in cipher_raw as written (the tool treats them as clear,
  taking no plain letters). Marks above groups are dropped from the value (¨128 -> 128) for the alignment only.

Alignment (primary, the only gated run)
    python3 tools/interlinear_align.py align f2_fr15576/pairs.tsv f2_fr15576/align.tsv f2_fr15576/key_f15576.tsv \
        --floor 0 --max-chunk 14 --seg-bonus 1.0 --len-prior 0.5 --wildcard '?' \
        --shuffle 200 --seed 1595 --min-share 0.6 --shuffle-out f2_fr15576/shuffle.json
(the Manteuffel syllabic-code settings, PREREG-MANT4, unchanged; pairs = one per line, G_n over C_n.)

Statistic and control (rule 3): CONSISTENT = code values whose top chunk is non-empty, occurs >= 2 times on >= 2
different cipher lines and is >= 0.6 of the value's aligned occurrences (the tool's own definition). Control: the same
run with the gloss lines dealt to the wrong cipher lines (200 derangements, seed 1595). A gloss over the wrong line gives
chunks that disagree across lines, so the control can move the statistic (it is not orthogonal to it).

Gate: PASS iff real CONSISTENT >= 5 AND the empirical p <= 0.01 (real exceeds the control at its 99th percentile).

Grades: on PASS, a value is C only if it is in the CONSISTENT set; every other glossed value is M (one occurrence, or
inconsistent); tokens with no chunk are U. On FAIL, no value is C (all glossed values M). Exploratory variants (e.g.
--clear-consumes for the clear letter tokens, other chunk settings) may be reported afterwards, labelled ungated, and
cannot license a C.
