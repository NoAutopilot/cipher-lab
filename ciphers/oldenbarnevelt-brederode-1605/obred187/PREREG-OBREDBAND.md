# PREREG-OBREDBAND (15 Oct 2026, 09:1x UTC by date -u; worker OBRED-BAND, account 2, for LANE DEFAULT-A2-0810-15)

Pushed in its own commit before any statistic is computed. Inputs as on origin/main at 767b257d5: `ciphertext_556.tsv` (81 groups, gloss
columns; OBRED-556, OBRED-552), `obred187/tokens_92.txt` (121 tokens), `obred187/tokens_187.txt` (59 tokens). Disk and CPU only.

Disclosure: the band hypothesis comes from OBRED-TRY's statistic B (rho 0.959, itself post-hoc-selected and disclosed there). This worker
has read ciphertext_556.tsv's rows (as OBRED-TRY did) before registering. Nothing below has been computed yet.

## Pairs
Exactly OBRED-TRY's `pairs556()` rule: rows with gloss_grade C and a single-letter gloss, letters folded i/j, u/v/w; alphabet
`abcdefghiklmnopqrstvxyz` (23). Any group grade (H-read or M) enters; a sensitivity run with H-read groups only is reported, not gated.
Conflict codes (415 r/s, 337 o/p, 100 d/e) enter as their per-leaf glosses (rule 4: never settled; here they simply score as they fall).

## Predictor (band interval)
Training set T = (code, letter index) pairs. For a test code v:
- v in T: interval = the letters T glosses v with (min..max index);
- else L = largest T code below v, U = smallest above: interval = min(g_L, g_U)..max(g_L, g_U) inclusive; only L -> g_L..z; only U -> a..g_U.
Per token score s = 1[true letter in interval] / width. Statistic S = mean s over test tokens. Secondary (not gated): hit rate, mean
width, nearest-code exact accuracy.

## Held-out check (the gate)
Primary: fit on scan 555 pairs, score scan 556 pairs. Null (shuffled band): the 555 letters permuted over the 555 codes, 10,000 draws,
seed 1619; p = share of draws with S_null >= S_real. Reverse direction (fit 556, score 555) reported, not gated.
Power (rule 3, ARM3-ADJ clause), before reading the gate: synthetic alphabetical homophonic list on codes 1..587, contiguous letter
bands in alphabet order, band width proportional to the letter's frequency in tools/data/nl16 (folded, >= 1 code each); plaintext windows
from nl16; each letter enciphered by a uniform homophone. Per simulation: a training sample the size of 555's pair count and a test sample
the size of 556's, drawn as letter tokens from two different windows; same S and 1,000-draw shuffled null; 200 simulations, seed 92.
Power = share with p <= 0.05. In the same simulations, bands fitted on (555 + 556) pair count are applied to a synthetic text of
180 tokens (no. 92's 121 + 187's 59, letters only): report the share of tokens with a one-letter interval and that share's accuracy,
and the overall interval hit rate -- the expected yield of the application at the target's own count, under this synthetic design
(which is an assumption: the real band widths are unknown).
GATE: power >= 0.70 AND p <= 0.05 on the primary direction. Power < 0.70 -> "non-test at this N", no application. p > 0.05 with power
>= 0.70 -> held-out check failed, no application.

## Application (only if the gate passes)
Bands from all pooled C pairs (555 + 556). Each token of no. 92 and the 187 postscript: codes 588-751 are left as codes (name band);
every other code gets its interval as above, grade M, written to `obred187/band/reading_92_187.tsv` by `obred187/band/band.py`
(`--check` exits 1 if stale). Reported: share of tokens with a one-letter interval, with width <= 2, and name codes. Not key.tsv,
not a reading of the letter's sense; no word is claimed from an interval string.
