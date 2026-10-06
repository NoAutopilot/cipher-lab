# PREREG D4-VIVV (verifier, 6 Oct 2026, written before the scored run of vivv_contam.py at nshuf 1000 / nw 100)

Question: does D4-VIVMOUS's 0.454 need the copy f.105r's own text in its own order, or only French letter statistics?
The value-permutation null (vivmous.py) changes the decoded stream's letter frequencies as well as its order, so it cannot
separate the two. A 3-draw smoke run (not scored) showed the real decode reading 0.42 mean against unrelated French.
Nulls (same statistic, stream_align.nw_score, same window length W): (e) 100 random windows of
tools/data/fr16/lettresdecatheri01cathuoft (period French, Catherine de Medicis), real decode unchanged, seed 7;
(f) 100 shuffles of pass A's token order, real map unchanged. Both can vary on the statistic (text identity / order).
Matched control: vivmous.py's control construction, seed 0, at e=0.576, scored vs the copy and vs (e)'s windows.
Text-specific PASS iff real_vs_copy > (e) p99 AND > (f) p99, and the control seed 0 clears its own (e) max. Otherwise
"French-statistics only; no text-specific alignment shown at this transcription". Not gated (reported): contamination
variants a-d of vivv_contam.py.
