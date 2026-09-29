# H65 pre-registration (29 Sept 2026, DEBOSNYS-RUNNER-3b; pushed before any classifier score)

Row: CAMPAIGN.md H65 (orchestrator, 29 Sept 12:47 UTC) -- a per-glyph classifier on glyphs/bitmaps.npz over the six
pixel-limited class groups, gated on R2-2's known-answer page.
Groups: EIGHT/VENUS/THREE, C-BAR-X/ARCH-DASH, CIRC-O/BLOB, O-SLASH/PHI, II-DASH/CC-DASH, S-CURL/DOUBLE-LOOP.
Training data: 48x48 sign bitmaps (glyphs/bitmaps.npz 'signs', rows of glyphs/signs.tsv) of boxes settled agree-AB, or
settled-majority at H, in the three settled drafts, whose id is in a group; every box used as a target or neighbour-
source on R2-2's page (swarm/R2/R2-2/control/truth.tsv) or on H63's page (h63/truth.tsv) is excluded from training.
Classifier: per group, k-nearest-neighbour (k 3, distance-weighted) on the bitmap pixels scaled to 0-1 (no tuning);
a second arm with a linear SVM on the same pixels is reported alongside, not used for the kill.
Controls first: (a) leave-one-out accuracy on the training boxes of each group against its majority-class baseline;
the classifier must beat the pooled majority baseline or the row stops ("no passable control").
Use on the pages: for each reader's read that falls in a group (after R2-2's folds and RULE.md marks), replace it with
the classifier's call among that group's members for that box's bitmap (both readers therefore agree wherever both
read inside the same group). Score: two-reader error (unsettled + agreed-wrong) / 96 after arbitration.
Kill: R2-2 page two-reader error at or above 15.6 pct after arbitration (no gain over the readers). H63's page is a
second held-out page, reported, not gating. A pass says the classifier resolves those pairs better than readers at
the public pixels -- a transcription tool, not a reading.
