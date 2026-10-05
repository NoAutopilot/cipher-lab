# PREREG N9-GRA4 addendum to PREREG-N8-GRA2 / PREREG-N8-GRA3: fr.3040 no.6 f.18r L11-L21 vs Le Grand III pp.454-455 (5 Oct 2026, written 05:40 UTC, before any crop is cut or read and before any score)

Brief: `.claude/briefs/runs/2026-10-05-ytbiz-near9-wave2.md`, job N9-GRA4 (account 2, for LANE-NEAR9). **Same instrument and
gate as N8-GRA3, no knob changed**: statistic `agree`, decode, normalisation, NW aligner with free print-side end gaps, N1
(shuffled print) and N2 (shuffled key) at 200 reps p99, planted control at 13% token error, 20 seeds (nulls on 3 seeds, as
score3.py), control gate mean >= max(N1,N2 p99) + 0.15, target gate agree >= 0.50 and > max(N1,N2 p99). Key: key.tsv at
the commit that carries this file. Scorer: `n9gra4/score4.py`, importing N8-GRA2's registered functions unchanged.

## Lines (Gallica btv1b9059870w canvas 32 = f.18r; counted by eye on a 1000 px thumbnail, 05:39 UTC)
- The f.18r cipher block has **21** lines (the brief's "L11-L26, 16 lines" was an estimate from the Verdict line). N8-GRA2
  read L01-L10; its L11 crop sits at its region's bottom edge (partial) and was never read. This job reads **L11-L21**
  (11 lines; thumbnail y ~725 to ~1010, the last line ending in a double stroke before the clear "... Ehausser").
  The few cipher signs at the end of the clear line above L01 ("pensa faire ...") are out of scope (not read by anyone yet).
- Crop: `tools/iiif_lines.py --ark btv1b9059870w --canvas 32 --region 560,2960,3300,1360 --follow-slope 400 --overlap 0
  --prefix f18rB`, then non-overlapping _a/_b halves by N8-GRA3's halves method (`n9gra4/halves.py`). Lines numbered
  f18rB_L01.. = f.18r L11..; if the tool finds more or fewer than 11 bands, the band list is fixed by eye on its debug
  overlay before any pass, and recorded.
- Print: segment S1 = `n8gra2/print_span.txt` (Le Grand III p.454 "il luy dit qu'il laissast" .. p.455 end of the
  pre-"Vous entendrez assez" passage), free ends, as N8-GRA2/N8-GRA3. The whole 11-line block is one alignment.
- Planted control: S1 enciphered to the target's keyed N (S1 is 866 letters; if N exceeds that, the control uses the whole S1).

## Units (Usage 6, stated before the first call)
One batch of ~22 half-line crops: 2 blind Sonnet passes (N8-GRA3's PASS-BRIEF text, file list changed) + 1 reconciliation by
this worker = 3 units; eye checks of open-code occurrences are part of the reconciliation unit.

## Reconciliation (fixed before reading)
N8-GRA3's reconcile rules unchanged: agreements kept; reader-label aliases a -> A2, O -> null_o, n -> n6, NEW:v* -> v; a split
is settled only by this worker's eye on the crop for the two N8-GRA3 pairs ((H, HASH), (zb, mx)) and otherwise '?' (wildcard,
unscored). No z relabel: N9-GRAZ found the passes' `z` on this letter is mostly the barred z (K2); the gating `agree` uses
key.tsv as committed (z = A). A **secondary, non-gating** figure is also reported: `agree` with every `z` token as a wildcard.

## Open-code rule
N8-GRA3's open-code rule, unchanged, pooled over this job's tokens + N8-GRA2 f.18r L01-L10 + N8-GRA3 f.18v/f.19r (each block
against its own print segment). Listing (not gating): every HASH, A2, Mx and zb occurrence with its aligned print letter;
for this listing only, zb (key.tsv NULL, M) is decoded as a wildcard in a separate alignment so its slot is visible. zb is
keyed (NULL), so it is not eligible for a C row under this rule; a consistent zb alignment is listed, not keyed.
Any key.tsv change -> `decode.py --check` and `tools/decode_key.py ciphers/fr2980-gramont --check`; VERIFIER WANTED in ROOM.md.
