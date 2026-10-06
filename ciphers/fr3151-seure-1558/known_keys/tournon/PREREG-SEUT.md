# PREREG-SEUT: do the two blind Tournon 1556 passes align with the slip decipherment into a key? (R12A-SEUT, 6 Oct 2026, written before any score)

Inputs: `passA.tsv`, `passB.tsv` (blind Sonnet reads of fr. 3138 fo. 22r against `exemplar_sheet.png`; A/B err 0.318, `pass_err.json`);
`slip_read.txt` (this worker's M-grade read of the canvas-25 slip; brackets and '?' dropped, letters a-z kept, 524 letters).
Symbol stream: crops in order L01_s1 .. L13_s1, 'NONE' dropped; every '??' token gets its own fresh id (cannot match anything).

## Statistic
S = `tools/stream_align.py` nw_score(decode(learn(sym, let)), let): identical aligned pairs / symbols, the RUN2-NXALN statistic.
Fixed settings (not tuned after scoring): band 80, step 100, iters 3, slope = letters/symbols, all other parameters at the tool defaults.

## Null (wrong text; S depends on which letters sit where, so it CAN differ from the target)
For each pass: the same learn+score against (a) 20 random 524-letter passages of `tools/data/fr16` (fixed seed 12), (b) 20 word-order
shuffles of the slip text (same unigrams, seed 13). Null p95 = 95th percentile of the 40.

## Power control, run first (design-matched: homophonic letters + short-word codes, same N, same symbol count, same error)
The slip text enciphered with a random homophonic key (40 letter symbols, homophones by letter frequency) where each occurrence of
de/le/la/que/qui/et/du/par/il/a/est is one word-code symbol (11 codes), then sign error injected at 0.32 (a token replaced by a random
other symbol), 3 seeds (21, 22, 23), each vs its own null built the same way. Power condition: S > null p95 in >= 2 of 3 seeds.
If it fails: NON-TEST, the passes are not scored as a key-alignment negative; stop.

## Target gate
PASS for a pass if S > its null p95. Both pass: the transcription supports a key rebuild (key TSV written, values supported by both passes
graded C, others M). Either fails: no key from this transcription; next pass is the owner's sorter / a reconciliation, not a third machine pass.
A PASS licenses no reading of items 43/44 (the R1/R2 key test is a separate pre-registered step).
