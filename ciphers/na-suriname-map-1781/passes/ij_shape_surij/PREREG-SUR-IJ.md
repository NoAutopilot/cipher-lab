# SUR-IJ (LANE FAMILY, account 2), 8 Oct 2026 -- pre-registration, pushed alone before any letter crop is cut or any call is made

Question (D1A-SURV "Observation for the next step"): is the dotted ij form in the inv. 373 letters (0746, 0758) the same sign as
the Nieuw Secreet Alphabet's dotted y (NA 1.05.03 inv. 86 scan 0003, key code [u-dots] = n, grade M in key_period_codes_nieuw.tsv)?

Material. Key side, on disk: images/inv86_0003_left_native.jpg, GAPS49 regions b (N row first sign, 85,1950,115,170) and
a (M row first sign, 95,1770,150,190); f (K row b, 85,1560,115,120). Letter side: NOT on disk (never committed; folder near
30 MB). Fetched once to scratchpad, not committed: 0746 {base}/560,150,2040,3800 and 0758 {base}/2860,880,1974,2220 (the regions
D1A-SURV used), 2 requests to service.archief.nl. Crops: tools/iiif_lines.py --image ... --centres <R14 centres> (pasted in
NOTES), then single-sign tiles cut by PIL around each named form, with ~1 sign of margin, never a full line or page.

References (shown to the reader as labelled R1-R3, no values, no row letters):
  R1 = key N-row dotted y (b); R2 = key M-row first sign (a); R3 = key K-row b (f).
Query tiles, shuffled to Q1-Qn (seed 20261008), mapping in blind_key.json, not shown to the reader:
  targets (4): the dotted ij forms at 0758 R L03 (`e i j`), 0758 R L05 (`[delta] i j r`), 0746 L L10 (`b 7 y`, Y26),
    0746 L L13 (`[y-fam] j`, Y36) -- the 4 of D1A-SURV's 5 re-eyed forms with a named crop.
  known-same control (1): a second tile of the key N-row dotted y cut from scan 0003 with a 12 px shifted box and 1.25x scale
    (same physical sign; it must come back R1 or R2 -- GAPS49 grouped a and b as one sign, so either counts).
  known-different controls (3): two undotted y-forms from 0746 (L10 Y27 and L12 Y33, labelled Y, no dots, by NZ-SURIJ) and one
    plain sign of another class from the same letters (a digit or plain letter on 0746 L10/L12, chosen before the call).
The reader (one blind Opus subagent call; a second only if the first returns unclear on >= 2 targets and cap allows) is told only
"handwritten signs cut from 18th-century documents": per Q tile, which reference it matches in shape AND marks above
(R1 / R2 / R3 / none), whether marks above are none / dots (count) / other, and confidence 0-1.

Gate (scored first): known-same control -> R1 or R2 at conf >= 0.6, AND each of the 3 known-different controls -> not R1 and not
R2 (none or R3). Fail -> "non-test (control failed)"; nothing changes.
Outcome if the gate passes (a target counts as matched at R1 or R2 with conf >= 0.6 and dots reported):
  A >= 3 of 4 targets matched -> the letters' dotted ij is logged as the Nieuw sheet's dotted-y sign ([u-dots]); the 10 D1A tokens
    may cite key_period_codes_nieuw.tsv [u-dots] = n as their source, at the key row's own grade (M), so no token grade rises above
    M; no key, conflicts or transcription file changes; the M/N caveat of GAPS49 (left page's M and N both dotted, unconfirmed)
    is restated, not resolved.
  B <= 1 of 4 matched -> logged: the letters' dotted ij is not the sheet's dotted y by shape; nothing changes.
  C 2 of 4 -> indeterminate; nothing changes.
Both numbers (controls, targets) reported. Context (gloss n/m) is not used to choose an outcome. Rule 10: report only.
