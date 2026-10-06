# Look-alike pass, R11-RJMLA (6 Oct 2026) -- fixed before any re-read
Instrument: tools/lookalike_pass.py windows (label-hidden per-tile windows) on the 88 (f.194) + 114 (f.199) reader splits
of test 1 (scripts/lookalike_tiles.py), one blind Sonnet re-read per page, then `lookalike_pass.py reconcile` unchanged:
a firm (H/M) re-read equal to reader A or B settles the tile at 2-of-3; anything else stays UNSETTLED and goes to focus.tsv.
Reported: settled / unsettled counts per page and residual = unsettled / all reconciled tokens. That residual is
agreement among three machine readers, NOT reader error or true error (no BENCHMARK-TX row for this hand); it licenses no
S grade and does not change ciphertext_*_reconciled.tsv, alphabet.tsv or the held-out gate (witness/gate_alpha.txt).
Known limit, stated before the run: the label inventory is not settled (f.199 pass B used its own ?1/?2, mapped here to
Hb/Tri), which tools/lookalike_pass.py says is the owner's sorter's job; unsettled tiles go to the sorter's focus list.
