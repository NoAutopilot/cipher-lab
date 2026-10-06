# AVS175 pre-registration (3 Oct 2026, ~15:07 UTC, worker AVS175, account 2, LANE-A2PUSH3)

Committed before any read of WVO 175 at native resolution (00175.pdf fetched to the scratchpad, 10 pages, 355-389 ppi).

Runs: the glossed cipher runs of WVO 175 pp.1, 3, 4, 5, 6, 8 (f.348r, 349r, 349v, 350r, 350v, 351v; A2-AVS-2's run list);
p2 is left out (no 'wir'/'Fürsten' gloss reported there). Only cipher signs with a gloss over them enter the alignment.

Sign questions (126's M left on key_98):
- Q1 NW (word sign, 98 'wir' n=1 M): does NW occur under a gloss 'wir'?
- Q2 Qf (98 'f' n=2 M): is the sign under gloss f (e.g. 'Fürsten', glossed 3 times) Qf, and where Qf occurs is the gloss letter f?
- Q3 K (word sign; 124 'der' n=1, 126 'die' by context): what article does the gloss give at each K?
- Q4 sign 1 (98 h; 124 once i): at each sign-1 position, is the gloss letter h or i?

Reads: 2 blind reads of the cipher runs (one subagent call each, line crops only, from `tools/iiif_lines.py --image`), 1 reconciliation
(by this worker against the crops), 1 gloss read (gloss lines only). A gloss letter is H-read only where both the gloss read and the
reconciliation agree it is legible.

Statistic: gloss-letter agreement = share of the cipher's single-letter sign positions (key_98 letter signs, word signs excluded) whose
aligned gloss chunk equals key_98's value (u=v), from `tools/interlinear_align.py align` with signs mapped to numerals (letter signs
< 100, word signs >= 100), `--prior` key_98 letter values, `--keep-fs`. For Q1-Q4 the statistic is the aligned chunk at the sign's positions.

Controls (>= 200 draws each, same tool, same flags): (a) rotated gloss: each run's cipher paired with the gloss of the run k places on
(k = 1..n-1, cycled to 200 draws with a fresh letter-offset each); (b) shuffled gloss: each gloss line's letters permuted (seeded). The
control can differ from the target: a gloss that does not belong to its cipher run cannot agree with key_98 above chance.

Gate: system test PASS if real agreement >= 0.60 AND above the p95 of both nulls. A sign value moves to C only if the gate passes, the
gloss at that position is H-read, and every aligned occurrence of the sign in 175 gives the same value (n >= 1); a split stays M and is
logged as a data conflict (rule 4). If the gate fails, nothing is regraded.
If fewer than 3 glossed runs are readable at native resolution, stop and log "too-short".

## Addendum 15:05 UTC (before any blind read or alignment; after one scoping look at three p1 crops, logged in NOTES.md "AVS175")
Scope reduced to fit the box: runs = WVO 175 p1 cipher lines c1 (y~920-975, gloss 'Den Graffe verdacht ...'), c2 (y~1045-1100, gloss
'Leibs und gutes gefahr wir ...') and c3 (y~1415-1470, gloss 'wir uns allzeit besorget haben'). Everything else in the prereg stands
(statistic, nulls >= 200 draws each, gate real >= 0.60 and > p95 of both nulls; the "fewer than 3 runs" stop rule is met at exactly 3).
The two blind reads are Sonnet subagents given cipher-only crops and a 98-system reference sheet cut from f.66 with align_98.txt's codes;
the gloss read is a third subagent given gloss-only crops. With n this small a PASS licenses only the sign values seen at those positions.

## Addendum AVS175B, 3 Oct 2026 ~15:22 UTC (worker AVS175B, account 2; committed before the second gloss read)
One more independent gloss read of the p1 gloss strips over c2 and c3 only (gloss-only crops, re-cut at the AVS175 NOTES coordinates
from a fresh 00175.pdf fetch; the reader is not shown the cipher, key_98, either earlier gloss read or the word 'wir'). The reader returns a
letter-by-letter transcription of each strip with per-word legibility (clear / probable / doubtful).
Decision rule for Q1 NW (the gate already PASSed, 0.615 vs p95 0.385/0.446, and is not re-run): the gloss word over NW at c2 pos 17 and
c3 pos 1 counts as H-read 'wir' only where this read gives 'wir' (or 'wier', 'wyr', u/v/i/y variants) marked clear or probable AND the AVS175
reconciliation read 'wir' there (it did, both positions). NW moves M -> C only if both positions are H-read 'wir'. If either position reads
another word, or doubtful, NW stays M and the split is logged (rule 4). One H-read 'wir' and one doubtful = stays M (every aligned
occurrence must agree and be H-read).
Q2 Qf and Q3 K: AVS175's reconciled c2/c3 signs contain no Qf and no K, and this job does not re-read cipher signs, so neither can move;
nothing about them is decided here. Q4 (sign 1) is not touched.

## Addendum A4-AVS175, 6 Oct 2026 00:08 UTC (worker A4-AVS175, account 4; committed before any blind read of these lines)
Scope: the other cipher lines of WVO 175 p1 (f.348r), in 4-line batches in page order, stopping before a batch that would cross 80% of
the cap (USD 9) or box (75 min). Lines by centre y on the 2600x4021 p1 image (00175.pdf, fetched again 6 Oct 2026): batch 1 = y~1187,
1300, 1595, 1700 (c4, c5, c7, c8; c3 = y~1465 is AVS175's); batch 2 = y~1850, 1962, 2150, 2245; batch 3 = y~2345, 2445, 2550, 2662;
y~2762 last. Crops: `tools/iiif_lines.py --image p-000.jpg --region 450,<y-48>,2150,96` per cipher line; gloss lines likewise.
Reads per batch: 2 blind Sonnet subagent reads of the cipher crops (reference sheet = f.66 lines 1-6 crops from 00098.pdf with
align_98.txt's codes), 1 gloss read of the gloss crops (gloss only, no cipher, no key, not told what to expect), reconciliation by this
worker against the crops. Disagreements between the blind reads become '?' unless the worker settles them from the crop and logs it.
Statistic, nulls and gate: exactly as the AVS175 prereg above (gloss-letter agreement at key_98 letter-sign positions from
tools/interlinear_align.py align --prior key_98 letters --keep-fs; rotated-gloss and shuffled-gloss nulls, 200 draws each; PASS if real
>= 0.60 and > both p95s), computed over the newly read lines only (AVS175's c1-c3 are not pooled in).
Q2 Qf: Qf moves M -> C only if the gate passes, Qf is read by both blind reads (or by one and confirmed in reconciliation) at >= 1
position, the gloss letter there is H-read (gloss read and reconciliation agree) as f, and no aligned Qf occurrence gives another letter.
Q3 K: count K positions read by both blind reads with the H-read gloss word above. If every such K is under 'die', that is a second
period witness (175) for K = die, against 124's K = der (n=1, A2-AVS3). Under rule 4 (conflicting H support is a data conflict, never
settled by the more frequent value): 126 (Willem -> August, 16 Sep 1564) matches 124 (to August, 16 Apr 1564) in date more closely than
175 (9 Apr 1567), so 126's two K stay M whatever 175 gives; the witnesses are logged in HYPOTHESES.md and key_98's K row records both
values. If 175 gives 'der' everywhere, K = der gains a witness and 126's two K stay M (context 'die'). A split inside 175 is logged.
Nothing else is regraded from this job; other sign observations are logged only.
