# strips50 (7 Oct 2026, account-3 orchestrator)
The sorter's line strips rebuilt 50 px taller above and below from the full NARA frames (images/M34-014-00xx.jpg):
each original line crop was located in its frame by template match (all at scale 1.0, score >= 0.998;
line_locations.json), recut with +-50 px, and every tile's y shifted by +50 (../signs_strips50.tsv). Tile sids are
unchanged, so the owner's saved db choices (keyed by sid) carry over. 40 of 997 tiles had touched the old strip edge.
Strip images are not committed (regenerate from line_locations.json and the frames). Published 7 Oct 2026 with
Tomokiyo's 38-type sheet embedded as a reference panel (tools/sign_sorter.py --ref-image).
