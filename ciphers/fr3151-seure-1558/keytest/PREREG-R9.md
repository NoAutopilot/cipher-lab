# PREREG-R9: Henri II-era French key vs the reconciled f81R reads (R9-SEURE, 6 Oct 2026, written 06:1x UTC by date -u, before any score)

## Candidate keys (on disk, no new key transcription)
- K1 **Danzay 1557** (BnF fr.20140; Tomokiyo's reconstruction, `ciphers/fr20140-danzay-1557/key.tsv`, glyph descriptions + values).
  The only Henri II-era French symbol key transcribed in this repository. Other Henri II-era keys named on Tomokiyo's GL page
  (Marillac 1550, La Guiche 1551, Babou) exist only as images in sources/cryptiana and are not transcribed; the Lasry GL tables
  on disk (`sources/cryptiana/web/GL/`) are fr.3071 (1530s, Francis I) and fr.15564 (1580s, Guise): wrong era. Not tried here.

## Fixed label map (Seure reader-A labels -> Danzay glyph code), chosen from the glyph descriptions and one look at
## danzay_1557.png and f81R_L02_s1.jpg, before any decode. Not tuned afterwards.
| Seure label | Danzay glyph | value |
|---|---|---|
| 2 | r2 | r |
| 4 | q4 | q |
| 6 | b6 | p |
| 7 | g7 | g |
| 8 | g8 | g |
| 9 | h9 | h |
| 3 | le | le |
| = and =/ | eq | i |
| * | st | i |
| x and x/ | x | e |
| y | ven | y |
| m | sha | m |
| p | hp | h |
| t and t/ | pd | t |
| # and #/ | pp | m |
| s | ls | s |
| f and f/ | fd | d |
| o | O | null |
| oo | xinf | null |
Every other label is unmapped (a gap). Numerals >= 10 are unmapped (Danzay has no numeral word codes; that design difference is
itself noted, not scored).

## Statistic
Decode R1 and R2 (`kp/f81R_recon_R1.tsv`, `_R2.tsv`) with the map; nulls dropped; a word value expands to its letters; an unmapped
sign breaks the run. F = mean log10 P(c3|c1c2) over every letter trigram lying wholly inside a run, under a letter-trigram model
(add-0.5 smoothing, a-z, j->i, v->u, w->u, k kept) trained on `tools/data/fr16` (16th-century French letters).

## Control (can differ from the target: F depends on the values at fixed positions)
Shuffled key: permute the value column across the mapped glyph codes (same positions, same coverage, same run structure), 1000 draws.
Gate per reader: F_target > shuffled p95. Positive control (power), run first: Danzay's own ciphertext (`ciphertext.txt`, first 461
tokens of R1..), decoded with the TRUE Danzay key restricted to the same 19 glyph codes the map uses (others gaps), with injected
sign error 0 / 0.095 / 0.242 (a token replaced by a random other Danzay code), 3 seeds each, vs its own 1000-draw shuffled-key null.
Power condition: pass (F > own p95) in >= 2/3 seeds at 0.095 AND at 0.242. If the power condition fails, the target result is a
non-test and is reported as such. If it holds and the target fails for both readers: a negative for K1 under this label map only
(the map is one shape judgement; not a negative for the key family or for other maps). A target pass licenses only "worth a
second, blind shape-mapping and a fuller decode", no reading, no grades.
