# PREREG-JVN-GLY (10 Oct 2026, 02:2x UTC by date -u; worker JVN-GLY, LANE FAMILY-A2n, account 2)

Written and pushed before the target crop X3 is looked at. Copied from JVN-104 (NOTES.md "## JVN-104", 9 Oct 2026),
with the control set widened per the JVN-GLY brief.

Material: WVO 5551 (resources.huygens.knaw.nl/media/wvo/images/05000-05999/05551.pdf), p3 rendered at 300 dpi with
pdftoppm; line crops with `tools/iiif_lines.py --image <p3> --region 530,190,1770,220 --out ... --prefix p3 --debug`
(JVN-104's command); detail crops at JVN-104's boxes (X1, X2, X3, X4) plus two more same-hand body controls chosen
from the body before X3 is viewed: X5 (positive: another "ſich", or an "ich"/"ch" word) and X6 (negative: another
long-s word without ch). Reader: the Opus worker itself, reading the crops directly (no subagent). Controls are
viewed first, in a shuffled order, and their calls written to NOTES.md before X3 is opened.

**Question:** does L2 read "offentlich ſich" -- i.e. the glyph pair after 103 is Kurrent "ch" (completing
"offentli-ch"), the glyph before 104 is long-s, and the glyph between 104 and 146 is Kurrent "ch" (so "ſ[104=i]ch")?

**Gate:** YES only if the reader (i) reads all positive controls X1, X2 and X5 with their "ch" (X1, X2 as "ſich";
X5 as its ch word), (ii) does not read "ch" in either negative control X4 or X6, and (iii) on X3 reads long-s
before 104 AND "ch" between 104 and 146. If (i) or (ii) fails, the pass is a non-test (stop; the instrument moves to
the owner's sign sorter). If (i)-(ii) pass and (iii) fails: NO for this pass. The glyph after 103 is reported but
not part of the gate. 140 vs 110 on the same crop is reported, not gated.

Caveat stated in advance: the reader (this worker) has read JVN-104's notes and so knows the proposal and which crop
is which; "shuffled" here guards order only, not knowledge. A YES under this gate is therefore graded M at most in
ciphertext_5551.tsv (the brief: M unless the gate says otherwise), never S.
