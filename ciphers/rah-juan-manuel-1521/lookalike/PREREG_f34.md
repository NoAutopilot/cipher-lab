# Look-alike pass on R9501 f.34, R13-RJM34LA (6 Oct 2026) -- fixed before any re-read
Instrument: tools/lookalike_pass.py windows (label-hidden per-tile windows) on scripts/lookalike_tiles34.py's tiles: the 218
reader-split '~' tokens of ciphertext_f34_reconciled.tsv (the brief's "220" counts the 2 '~' both readers wrote, which are not
splits and are not tiled, as in R11-RJMLA) plus 24 'oot' tiles, the agreed out-of-table groups the brief names (y 8, g 6, rob 5,
ez 5), each offered with every table code at edit distance 1 (and K/Q/Z for the one-letter reads). Blind Sonnet re-reads, crops of
RUN1-SEG's command on the DECODE full-size image (sha1 b510ebe5..., re-fetched 6 Oct 2026), crop batches by line range.
Rule, unchanged: `lookalike_pass.py reconcile` -- a firm (H/M) re-read equal to reader A or B settles a split tile at 2-of-3;
anything else stays UNSETTLED, keeps the passC label and goes to focus. For an oot tile A = B = the group as both readers wrote it,
so a re-read can confirm it (settled, unchanged) but never overturn it (a third reader does not overturn two); a firm re-read of a
table code there is reported as a pointer and goes to focus.
What changes downstream: scripts/decode9501.py applies the settled split tiles (passD labels) as a third reader in place of '~'.
Grades stay within R12-RJMV's licence: a token settled by this pass is graded as a one-reader token would be -- a table code M,
a symbol M (never S: S needs both blind readers to agree, and the 2-of-3 figure is agreement, not error), an unvalued symbol or
an out-of-table group U. Nothing H or C.
Reported: settled / unsettled split tiles, residual = unsettled / all 753 tokens (agreement among three machine readers, not
reader error, not true error -- CLAUDE.md Usage 6); grade counts before and after; the oot confirmations; the two judge calls
(es1600, es17c) on the rerun decode with the shuffled-order control over 20 seeds (R13-RJMV's method, scripts/shuffle_spread9501.py).
No gate: no key, alphabet or held-out figure is tested here, so nothing passes or fails; the judge is reported as before.
