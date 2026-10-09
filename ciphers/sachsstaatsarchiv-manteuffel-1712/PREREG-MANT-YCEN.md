# PREREG-MANT-YCEN (9 Oct 2026, written before any score; LANE FAMILY-A2k account 2)

Question: in the 694/08-09 transcriptions, is the y-shaped digit (open top, long descender, no crossbar, no closed loop;
MANT-EYE63R) a 9 or a 4?

Census (ycen/census.tsv, built from committed files only, disk only, no vision): every token whose committed note calls
a digit y-shaped / y-glyph / y-tailed on a 694/08 or 694/09 leaf, with leaf, line, token id, hand (as recorded on disk;
"unrecorded" where no file names the hand), the code if the y is a 4 and if it is a 9, and key.tsv's value for each.

Known answers (ycen/known.tsv): a y-slot gets a known answer only from a source independent of the digit reading:
tier P = a printed clear text at that slot (Acta Borussica BO I print spans already committed); tier G = a blind gloss
pass letter/word at that slot whose neighbouring keyed tokens agree with the gloss letters on both sides (alignment
anchor); tier K = a known word from the keyed neighbours alone (e.g. Bullinbroug, Ferdinand); tier W = weak (gloss read
only by a worker's eye or one blind pass). Slots whose shape is disputed (0398/0410 code 19, read 19 by two blind reads,
y-shape asserted only by V-MANTC) are tier D and scored separately, never pooled with the y-slots.

Rule under test, R9: "a y-shaped digit is 9". Alternative R4: "a y-shaped digit is 4". A slot is a hit for a rule if
key.tsv's value of the code under that rule equals the known answer (letter, or name per key note: 9/39/46 Ilgen,
259 Ilgen M). Score: hits / known slots, for tiers P+G+K (primary) and P+G+K+W (secondary), per volume (694/08, 694/09)
and pooled; per-hand only where the hand is recorded.

Control (can differ from the target by construction): the known answers are replaced by labels drawn uniformly from
the pool of every gloss/print letter at aligned positions of the same spans (letter base rate; the Ilgen name label
counted once per printed/glossed Ilgen slot in those spans), 10,000 draws, seed 1712; report the null mean and p99 of
R9 hits. Gate: R9 PASS if R9 primary hits > null p99 AND R9 hits > R4 hits AND R9 accuracy >= 0.80. R4 symmetric.

Consequence: no transcription edit unless the gate passes AND this worker's own eye (committed crop) agrees at that
slot; with no vision in this job, the expected outcome is no edit, the rule recorded, readings unchanged.
