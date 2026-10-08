# PREREG TT-MATRIX (key_design.py --matrix), written 22:58 UTC 8 Oct 2026 by date -u, before any control run

Instrument: `tools/key_design.py --matrix KEY.tsv` (Tomokiyo, matrix.htm "Vatican Substitution Ciphers Designed on
Alphabetical Matrices", 2018; practices 3 and 4 of LESSONS-TOMOKIYO.md).

Known-answer control keys (text on disk, transcribed into tools/tests/fixtures/matrix/ from the pages named):
- manetti   matrix.htm (Meister 1906 p.211)            expected label: one-part
- nevers25  matrix.htm (Nevers Collection no.25)        expected label: one-part (homophones)
- despes    matrix.htm (Devos 1950 Cp.25)               expected label: one-part (homophones)
- commendone matrix.htm (Meister 1906 p.235, Leighton)  expected label: two-dimensional; paired first digits; vowel-headed
- ormonde   ormonde.htm (letter codes as decoded on the page)  expected label: one-part, two series
- schiner   schiner.htm (letter codes as decoded on the page)  expected label: one-part
The Spanish blocked-square keys (matrix.htm matrix3.png, spanish3cp37.png, phelippes1.png) are images not on disk:
not in the control; a synthetic blocked/reversed fixture covers the label in the offline test only.

Pass lines (fixed before running):
1. Labels: >= 5 of 6 control keys get the expected label.
2. Null: each key with letters randomly permuted over its codes, 20 permutations per key (seed 0): >= 95% of the
   120 null runs labelled `none`. (The null can fail differently: permuting letters over codes changes exactly the
   code-order adjacency the label is computed from.)
3. Prediction: from 3 anchor letters drawn at random (20 draws per key, seed 0), using the language's period
   alphabet preset (not the key's own letter set), pooled correct / total over the six keys' non-anchor letter codes
   >= 0.50; the same on the permuted null keys <= 0.15.
A key whose label passes but prediction fails is reported as such; the shelf grade follows the brief
(`proven` only if 1-3 all pass on Tomokiyo-solved cases; else `weak` with the failing number).
