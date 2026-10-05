# PREREG-ECK62-FLIP (D2-ECK62R, 5 Oct 2026, written and pushed before any number)

Question: D2-ECK62M aligned 57 dated print-free/print-q matches; a group agrees with the print at 0-10% with conflicts, which
its NOTES section reads as "book likely wrong, not tested". Test: decode those entries with the other book and re-align.

Instrument: `ec18_align.py DATA ORDIR --rows <file> --write|--check`, unchanged except that the output suffix follows the rows
file name and a `flip-*` source caps non-AGREE tokens at S. Same ORDIR (OR ser. I 32.1-49.2, 48 `_djvu.txt`, sha256 of
`or_volumes.tsv`), same vol18.json (sha256 in ../pilot1864/manifest.tsv), same anchors, same same-week control window.

1. Selection (mechanical, from `align_free_entries.tsv`, fixed before any flipped number): scored >= 5, agree_rate <= 0.10,
   conflict >= 1 -> 19 entries, `align_flip_rows.tsv` (book flipped, source `flip-<old source>`).
2. Negative control for the flip itself (rule 3, can fail differently): the 14 entries with scored >= 5 and agree_rate >= 0.75
   flipped the same way (`align_flipctl_rows.tsv`). If flipping a right book still gives agreement, the flip test proves
   nothing. Expected: their flipped AGREE rate falls to near their control-window rate.
3. Gate (the instrument): pooled flipped-control AGREE rate <= 0.15 (a wrong book does not align). If it fails, no book is
   changed, the step is logged untested-by-this-tool.
4. Per entry, a flip is accepted (book written as `1r`/`2r`, grade of the book S: aligned against print, not marker-known) when
   flipped AGREE >= 3, flipped rate >= 0.30, flipped rate >= original rate + 0.20 and flipped rate > its own control-window
   rate + 0.20. Otherwise the entry keeps its book and stays listed as unexplained (print, transcription or table date the
   remaining causes; not settled here).
5. Report both pooled numbers (selected 19: original vs flipped vs control window; control 14: original vs flipped), the
   accepted count, and rule-4 grades of accepted entries (AGREE -> C, others S).
