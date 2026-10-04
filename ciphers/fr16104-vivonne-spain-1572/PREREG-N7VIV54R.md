# PREREG-N7VIV54R (4 Oct 2026, N7-VIV54R, LANE-NEAR7 worker, account 2) -- ink 54: the col-u row-3 sign as its own label

Target: ink piece 54, BnF fr.16104 f.173r-v (7 Sept 1572). Written and pushed BEFORE any relabel, any per-position judgement and any
re-decode under the new label. Inputs frozen at this commit: tx/lookalike54/viv54L_<page>_passD.tsv (N7-VIV54L's settled sequence),
tx/lookalike54/align/<page>/passC.tsv, images/c187_f173r_* and c188_f173v_* (native line crops, images/manifest.json), key.tsv,
sources/cryptiana/web/henryiii_Vivonne1.png. Seen before this file: N7-VIV54Q's 7-occurrence montage (tx/viv54Q/to_sign_evidence.jpg)
and the committed reading_piece54_L.tsv, so the "to"+sign contexts are known to this worker; that is why the per-position judge below is
a value-blind subagent, not this worker's eye.

## New label and key cell
- **Label `Zu`** = Tomokiyo's column u, row 3 entry: a Sigma/I-shaped sign (top bar, near-upright stem that may bend back, bottom bar,
  no diagonal). Read from henryiii_Vivonne1.png at 3x by this worker before this file: the cell sits plainly under "a" in column u and
  is legible -> **key.tsv row `Zu` -> u, grade C (published key; H at token level by the usual rule)**, source "published key (Tomokiyo,
  henryiii_Vivonne1.png) col u row 3; no clerk-alignment support (n_aligned 0)". Also added to key_tomokiyo.tsv. Inks 53 and 63 are
  NOT relabelled here; their "to z"/"to x" contexts are noted as the next step.

## Positions judged (every position, not only after "to")
Every token of ink 54 whose settled label (passD) is one of the labels a reader could have merged this glyph into: **z, x, R, 3, 2**
(169 positions: f.173r z 54, x 15, 3 10, 2 2, R 1; f.173v z 55, x 24, R 6, 3 2). Other labels (P, S, tz, # ...) are distinct shapes
and are not judged. No position is chosen or skipped by its neighbours.

## Shape criterion and instrument
One value-blind Sonnet call: per-position windows cut from the native line crops by the N7-VIV53L/54L window instrument
(tx/viv53L_windows.py window/montage, imported; red tick = estimated x, may be 1-3 signs off), 6 per montage, plus a reference image
holding (a) the key cell col u row 3 and (b) the key cell col a row 3 (flat z) cut from henryiii_Vivonne1.png. The prompt shows NO
decoded text, no key values, no word "u", no hypothesis; per position it gives the 3 labels before/after (keyboard ids, to find the
sign) and asks for one class:
- **SIGMA** = two horizontal bars joined by a near-upright or back-bent stem, no diagonal stroke from upper right to lower left (ref a);
- **ZED** = top bar and bottom bar joined by a diagonal (ref b), incl. crossed z and 2-shaped z;
- **OTHER** = a round-topped 3, an x, an r-like loop, a 2, anything else; **UNSURE** = cannot find or cannot tell.
with conf H/M/L and the stroke feature seen.
**Decision rule:** SIGMA at conf H or M -> label `Zu` (token grade by the usual rule: M if conf M, else H); SIGMA at L, ZED, OTHER,
UNSURE -> label unchanged. Nothing settled by what decodes better; this worker does not override any answer.
**Built-in check (reported, can fail):** the 13 "to"+sign positions N7-VIV54Q saw by eye are a known-positive subset; if fewer than
7 of them come back SIGMA at H/M, or if more than 50% of all non-"to" positions come back SIGMA (the reader is not separating
shapes), the relabel is a NON-TEST: it is not applied, reading_piece54_L.tsv is left as N7-VIV54L wrote it, and the finding goes to
NOTES as such.

## Re-decode and gates (rule unchanged from PREREG-N6VIV53B / PREREG-N7VIV54L (iv))
tx/viv54L_decode.py gains an overlay (tx/lookalike54/viv54R_relabel.tsv, applied to passD before L1) and regenerates
reading_piece54_L.tsv (--check). b2 (s vs 200 letter-order shuffles, p99) with positive controls C1 f.103r and C2 ink 53 first; (c) 200
wrong keys (key.tsv values permuted across its codes, now incl. Zu); pass iff real margin > wrong-key margin p99. Seed base
"20261054R". Written to tx/viv54R_result.json. Repair-free stretches: re-listed by eye with liberties as AUDIT 2 4a counts them, the
three longest, and PREREG-N7VIV54L (ii)'s mechanical listing re-run beside its shuffle control (descriptive). print_check only on a
stretch >= 20 letters with no letter repair.

## Units (cap USD 2.5, box 13:45-14:30 UTC)
Scripts: windows, overlay, decode, test. 1 Sonnet judge call (~USD 1.2); this worker's tally of the answers (script). Stop before a
unit crossing 80% of cap or box.
