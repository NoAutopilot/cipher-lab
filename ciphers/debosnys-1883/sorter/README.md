# Sign sorter (1 Oct 2026)

The owner's alphabet-settling page: https://claude.ai/artifact/3HcBvFdR7EJ17VFy8uE7sM (private to the owner).
1,315 sign crops from the PUBLIC page images (glyphs/crops/*.png, boxes glyphs/signs.tsv), piled by the pass-A label
(glyphs/box_labels.tsv); 16 c4a0 boxes have no page crop and are left out. The owner marks per pile: one sign / not a
letter / same sign as another pile, and sets aside tiles in the wrong pile. Choices live in the artifact's db
collection `piles` (one doc per pile: pile, verdict, merge_into, outliers[sid], note, updated); read them with
ArtifactData list. Rebuild: `python3 build_data.py` then substitute data.json into page_template.html at __DATA__.
Why: R3 C4HI showed resolution is not the bottleneck (readers disagree ~28 pct at museum resolution vs 29 pct
degraded); the undefined sign inventory is. No museum material is used here (RESTRICTED.md).
