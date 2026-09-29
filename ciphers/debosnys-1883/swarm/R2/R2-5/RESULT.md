# R2-5 FOLGER-SPLIT: result (29 Sept 2026, DEB-SWARM2-R2-5, for the orchestrator)

Pre-registration: `PREREG.md` (main test, committed 5cf97fca before any real score; addendum D2 committed dc1e269a
after the calibration and before any real score was read). Scripts: `r25.py` (split maps, Folger encipherment,
planted ligature text, calibration, controls, real scores), `boxnull.py` (D2), `bgap.py` (B's fit gap), `analyze.py`
(writes `result.json`), `run.sh` / `run2.sh` (regenerate every output), `d2_drivers.py` (diagnostic). Instrument
`swarm/G-D/dcore.py` and `scripts/base_mark_recount.py` imported unchanged. Public copies only; CPU only; no key
fitted to be scored, nothing read. Folger plaintext: Bennett's own Figure 3 decipherment (`folger_fig3.txt`, cited
in its header; `sources/folger/`). Rule 10 throughout.

## The main test (D's frozen pair score, split vs a split null) -- as registered

| text | split N | gate: bal. acc. at 0.20 (NULL-SPLIT vs 5 language designs) | threshold | score | verdict |
|---|---|---|---|---|---|
| folger control (FOLGER-LIG, 6.5 pct of boxes composite) | 151 + 774 | **0.843** | 17.5 | split median 35.0 (unsplit 25.8); 40 of 40 above | **pass** |
| planted French ligature control (24.0 pct composite, the real share) | 155 + 801 | **0.555** | 24.7 | split median 25.9 (unsplit 12.1); 25 of 40 above | **fail** (gate and 32-of-40 bar) |
| folgerW (every Folger cluster one box; descriptive) | 430 + 2407 | 0.50 | -- | split 99.4 vs NULL-SPLIT median 91.5; 8 of 40 above its p95 | -- |
| real-T (top-to-bottom split) | 157 + 816 | 0.505 (0.517 at 0.15, 0.502 at 0.25) | 44.3 | **36.8** (unsplit 0.86); 12 of 40 NULL-SPLIT as high | untestable; at shuffle level |
| real-N (name-order split) | 157 + 816 | 0.51 (0.52, 0.505) | 48.8 | **41.7** (unsplit 0.86); 4 of 40 NULL-SPLIT as high | untestable; at shuffle level |

Why the gate fails at the real share: splitting a composite writes its internal pair into the text every time, and
D's within-line shuffle breaks those pairs, so D's score reads the split itself as order. At 0.20 the iid-box null,
split, scores a median 34.6 (real-T map), **above** every language design (15.6-26.5). The Folger passes because its
figures, as boxed here, are only 6.5 pct composites; at the real 24 pct share the same instrument cannot tell a
ligature-language text from iid boxes (planted 0.555). The real split scores (36.8, 41.7) sit inside their own
NULL-SPLIT spread: the jump from 0.86 unsplit is what splitting alone produces.

**Kill test (as registered): MET.** A gating control fails (the planted ligature text at Debosnys's composite share
and noise), so D's frozen score on split text is not a usable test for this design at this N and noise, and both real
splits are at shuffle level anyway. This is "untestable by this instrument at this composite share", not a
negative on the ligature design.

## D2: the same order features against box-level shuffles (diagnostic, registered before the real was read)

Boxes permuted within their line, then split, so a composite's internal pair is in every shuffle; only order between
boxes counts. 40 NULL-SPLIT instances per map at 0.20; controls the same 40 instances as above.

| text | D2 score (sum of z over c1, c2) | vs NULL-SPLIT (p95 / max of 40) |
|---|---|---|
| NULL-SPLIT, real-T map | median -0.47 | p95 4.07, max 8.92 |
| NULL-SPLIT, real-N map | median -0.50 | p95 4.33, max 4.36 |
| folger control | median 19.4 | 40 of 40 above p95: **passes** |
| planted French ligature control | median 5.0 | 26 of 40 above p95: **fails** the 32-of-40 bar (power about 65 pct) |
| real unsplit (same features, no split; baseline) | median 1.70 | -- |
| real-T | median **3.51** (5 seeds 3.17-3.72) | 3 of 40 as high: at shuffle level |
| real-N | median **9.55** (9.15-9.86; c1 3.5, c2 6.0) | 0 of 40 as high (and 0 of the 40 real-T-map nulls; 1 of those reaches 8.9) |

D2's control fails its own power bar, so D2 cannot back a negative. It does return one positive: the name-order split
of c1+c2 carries between-box order that 80 iid-box nulls do not reach (nearest 8.9) and that the unsplit text does
not show (1.7). This is weak: D2 was added after the calibration, two split orders were tried (so p is about 2/81, not
1/81), and real-N's 9.55 is higher than the planted French ligature text gives at this noise (median 5.0), which fits
a drawing habit (what is written after a composite's right-hand part) as well as or better than ligated letters.
The largest pair excesses (`d2_drivers.py`) are few-count pairs plus the known WAVE-PCT bond (H48, 7 vs 1.1 expected,
present in both orders, i.e. box-level order already): TILDE -> PCT-SLASH 5 vs 1.7, DASH -> XX 3 vs 0.6, DOT -> PHI 3
vs 0.6, O-SLASH -> C 3 vs 0.2, X -> OX 6 vs 2.7. No key, no letter value, nothing read.

## B's fit-vs-shuffle gap (second instrument; secondary, does not decide the kill test)

B's annealer rebuilt from 14 of B's 21 corpus files (gutenberg.org reset 7 fetches; stopped under the good-citizen
rule), 20 restarts x 3M iterations (B used 60 x 5M). Gap = fit per 5-gram window, real order minus the mean of 2
order-shuffled copies, split c1+c2 pooled.

| text | gap per window |
|---|---|
| folger control (English, B's language), 2 instances at 0.20 | 0.224, 0.257: **pass** (both above the larger null) |
| NULL-SPLIT (real-T map), 2 instances | 0.086, 0.039 (the split's own internal pairs give a gap) |
| real-T | 0.059: at shuffle level |
| real-N | 0.077: at shuffle level (below the null's 0.086) |

With 2 null instances this bar is coarse; it says that in English neither split comes near the Folger's gap (0.22-0.26).

## For the orchestrator

1. **The registered answer:** the split test through D's frozen score is untestable at Debosnys's 24 pct composite
   share (planted ligature control fails, gate 0.555); both real splits are at shuffle level there and on B's English
   gap. Kill test met on the control clause.
2. **One lead, not a reading:** D2 (box-level null) puts the name-order split above 80 iid nulls (9.55 vs max 8.9;
   unsplit 1.7). What would settle it: a fresh session, fresh seeds, 500+ NULL-SPLIT draws plus a habit null
   (dcore's NULL-HABIT at box level), each composite's split order read from the image rather than from the name, and
   the stroke-class boxes (R2-2's sign-or-mark rule) settled first; a planted control with D2 power of at least 80 pct
   (longer text or lower noise) before any negative is drawn from D2.
3. **For the digest:** a composite-splitting test must carry the split into its null; D's within-line shuffle of a
   split text reads the split as order (NULL-SPLIT 34.6 vs language 16-27).
