# D2B-MATF110 pre-registration (written 5 Oct 2026 ~23:58 UTC, before any blind pass; committed before the passes run)

Job: NOTES.md gap 2 / Escalation image-check -- f.110 line-crop sample, testing whether Bourdeau's unkeyed f.110
labels (BOX, z, w, T, 4, U, p; also v/y/1 if present) are unmarked variants of keyed labels.

Material: BnF fr.15572 f.110 = Gallica btv1b9061879d canvas 116 right page (Bourdeau's folio table). Native region
4780,300,3330,560 cut by tools/iiif_lines.py into 6 lines x 2 segments (images/f110/f110_L0{1..6}_s{1,2}.jpg).
Sample = image lines 1-6 = Bourdeau f110-1..f110-6 (358 tokens; unkeyed: BOX 22, z 22, w 7, T 7, 4 6, U 5, p 4).

Passes: two blind Sonnet passes (A, B), 3 calls each (lines 1-2, 3-4, 5-6), bMAT1F's protocol
(align1f/PASS_BRIEF.md) with the f.78v reference sheet (Bourdeau's labels, lines 1-5, crops images/f78v_79r/ref/).
The passes never see ciphertext.txt's f110 lines or key.tsv values. Reconciliation: script alignment
(f110crops/score.py) of each pass against Bourdeau's f110 line (Needleman-Wunsch, unit costs), then by-eye check of
the crops only for the label-collapse candidates.

Gates (all must hold before any key.tsv/ciphertext change):
- G0 known-answer control: on aligned positions where Bourdeau's label is keyed (key.tsv, value not '+'), each pass
  reproduces Bourdeau's label (exact) at >= 50%. If either pass is below, the sample is a NON-TEST for label
  collapse at this protocol (passes cannot reproduce the labeller's own keyed labels), and no label moves.
- G1 per unkeyed label L with >= 4 aligned instances: L -> K (K a keyed label) is supported only if BOTH passes give
  the same K on >= 60% of L's aligned instances, and K's share on L instances is >= 3x K's share of that pass's
  output over all other aligned positions (specificity against a pass that just writes K often).
- G2 crib consistency: where openings/openings_alignment.tsv (align_openings.py, Tomokiyo's f.111 opening) places a
  letter on an L instance in f110-1..6, K's key value must equal that letter on a majority of such instances (if
  there are none, G2 is "no data" and does not block, but the collapse is then graded M, not H).
- A collapse passing G0-G2 enters ciphertext/key only as an M-grade exception for f110 (never H), followed by
  tools/decode_key.py --check. A label failing G1 stays absent; outcome logged per label.
Shuffle reference for G1: the specificity ratio is the control that can fail differently (a pass that writes K
everywhere fails it; a shuffled-position control would not vary with label identity and is not used).
