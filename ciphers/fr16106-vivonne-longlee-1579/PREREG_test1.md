# PREREG test 1 -- fr16106-vivonne-longlee-1579, held-out known-answer test of a stream-aligned key (VIV-T)

Written and pushed 4 Oct 2026 before any key is fitted (git log orders it before test1.py's first output).

**Pair.** Cipher: BnF fr.16107, canvas 107, left page (f.101v by the foliation run 102, 103, 104 on the facing rectos;
headed "Du s. de St Goard au Roy, 2 mars 1580, Madrid"), the first page of a ciphered letter running c107-c109 left
(f.101v-103v) and closing in clear "Sire, Je supplie le Createur ... 2 Mars 1580". Plain: the clerk's copy headed
"2 mars 1580 / Dechiffré de la precedente / 10 & 30" on c110 right (f.105r; f.104r on c109 right carries the same
heading over a blank page). Its subscription reads "Madame ..." although the cipher's reads "Sire" (observed, not
explained). Cipher alphabet: the letter-form mark system (as fr.16107/16108 c80/c102), not the digit-and-mark one.

**Inputs (frozen now).** Cipher symbols: `tx/passA.tsv` (blind Sonnet pass A, 32 lines, 1,307 signs, labels of
`tx/SIGNS.md`, s2 overlap brackets stripped) is PRIMARY; `tx/passB.tsv` (1,273 signs) is SECONDARY, reported, not gating.
Two-reader agreement (reconcile_passes nw): 618/1458 = 42.4%, err_2reader 0.576 -- far above TRANSCRIPTION.md's
10% line; no reconciliation pass is run (840 disagreement columns; by Usage 6 the next pass is the owner's sorter,
not a third machine pass). Signs `?`, `?{..}` and `A/B` doubles are kept as their own symbol ids. Clear text:
`tx/plain_c110_f105r.txt` (VIV-T's read of f.105r, made before looking at either pass), letters a-z after removing
comment lines and the markers `{?}` (dropped), `[` `]` `?` (the doubtful word kept); accents folded.

**Split (by line).** Fit half = cipher lines L01-L20; held-out half = L21-L32. Plain is not split by hand: the fit
alignment's end column `jend` on the clear side defines the boundary.

**Fit.** `tools/stream_align.learn(sym_fit, plain_all, K)` with the module defaults; key = `decode(counts)` (argmax,
symbols unseen in the fit -> unknown). Grade C (every value from the clerk's copy).

**Statistic.** `nw_score(decode(heldout), REF)`: identical aligned pairs / held-out length, REF = plain[jend+1 :
jend+1+W], W = min(len(plain) - jend - 1, round(len(heldout) * (jend+1)/len(sym_fit))).

**Nulls (computed first, in the script's order).** (a) value shuffle: the fitted key's values permuted among the
symbols that have a value, 1,000 permutations, same REF; p99. (b) wrong window: the real key's held-out decode scored
against every window plain[o : o+W] with o + W <= jend + 1 - 20 (windows inside the fit-side text, disjoint from REF
by at least 20 letters), step 1; p99. If (b) has fewer than 200 windows, (b) is computed from the 200 evenly spaced
offsets with replacement allowed and the shortfall is reported.
Orthogonality: (a) changes which letter each held-out symbol decodes to, so the agreement with a fixed REF can differ;
(b) keeps the decode and changes the reference text, so agreement can differ if and only if the decode tracks REF's
specific content rather than French letter frequencies.

**Gate.** PASS iff real > null (a) p99 AND real > null (b) p99. NON-TEST if the held-out half has fewer signs than
3 x the key's symbol count with a value, or W < 150.

**Power control (pre-registered; licenses reading a FAIL).** Synthetic pair of matched design: the same clear letters
enciphered by a random homophonic key with the same number of symbol ids as pass A (symbols allotted to letters in
proportion to letter frequency, at least one each), then: (i) symbol noise -- each sign replaced by a random symbol id
with probability e = 0.576 (the measured err_2reader) and, as reference, e = 0.10; (ii) clear-copy noise -- the fitter
sees the clear text with 20% of its words deleted at random (mimicking this read's dropped `{?}` words), while the
cipher encodes the full text. Split at the same 20/32 line proportion; same fit, statistic, nulls and gate; 5 seeds per
e. If the control passes its gate in fewer than 4 of 5 seeds at e = 0.576, a target FAIL is reported as NON-TEST
(untestable at this transcription error), not as a negative; a target PASS is reported regardless, with the control.

**What a PASS licenses.** Only "the pass-A labels of this page carry a reproducible letter key against the clerk's
copy" -- the next test is the fitted key on one unglossed letter, judged by fr16 vs a shuffled-key null.
