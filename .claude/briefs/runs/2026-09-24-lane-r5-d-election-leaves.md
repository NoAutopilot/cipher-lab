LANE R5 WORKER D -- M36 fr5761 1519 KEY f.105-f.110: extend key.tsv as a dataset, then look for letters it opens (Sonnet, cap $5; disk only).
Target: ciphers/fr5761-election-1519. Common rules: .claude/briefs/runs/2026-09-24-lane-r5-common.md. Read NOTES.md "Atlas and key f.104
(LANE R4 D)", "Pass B and key f.104 (LANE R4 H)", "Pass C and key f.104 (LANE R4 L)". Natives of all seven key leaves are on disk
(images/canvas104-110_*.jpg, manifest.json); key_passB.tsv already holds one blind pass over f105-f110 (made before the atlas).
1. Extend the atlas to f105-f110 with `tools/glyph_atlas.py segment/classify` (reuse glyphs/, do not rebuild f104's codes; new codes only
   from the contact sheet). Coverage by script: share of f105-f110 sign boxes with a confident atlas code. Commit.
2. Two atlas passes per leaf, as L's method: pass A (you) and pass C (you, blind order: do leaves in reverse and never look at pass A's
   rows while doing C), plus the existing key_passB.tsv as the third vote. Majority per row (script) -> append to key.tsv
   (correspondent, section, plain, sign_code, grade H where 2 of 3 agree, M otherwise). Commit after every two leaves.
   At 70% of cap stop adding leaves and write what is done.
3. Then (<= $1): grep QUEUE.md, CATALOG.md, sources/solver-diffs/*.tsv and any fr.5761 finding-aid text on disk for 1519-20 letters of
   the election embassy (Bonnivet, Orval, Jean d'Albret, Guillart, Louise of Savoy, Francis I to the electors) in cipher, including
   fr.5761's neighbours in the same series (fr.2994, fr.3005, fr.3060, Dupuy, Clairambault 1519-20 volumes as named on disk). No fetches.
   List candidates with shelfmark and source line; do not capture.
NOTES.md section "Key f.105-f.110 and letters to try (24 Sept 2026, LANE R5 D)". ROOM done: "for LANE R5: M36 key rows <n> (H <h> M <m>),
leaves <list>, candidate letters <k>, cost $<c>". A key is a dataset result even with no letter read. No solving.
