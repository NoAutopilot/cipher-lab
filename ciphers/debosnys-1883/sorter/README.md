# Sign sorter (1 Oct 2026)

The owner's alphabet-settling page: https://claude.ai/artifact/3HcBvFdR7EJ17VFy8uE7sM (private to the owner).
Built with the shared tool (tools/sign_sorter.py; lesson in LESSONS.md, "Settle the alphabet before reading"):

    python3 tools/sign_sorter.py --signs ciphers/debosnys-1883/glyphs/signs.tsv \
      --labels ciphers/debosnys-1883/glyphs/box_labels.tsv --pages ciphers/debosnys-1883/glyphs/crops \
      --marks ciphers/debosnys-1883/glyphs/marks.tsv --title "Debosnys Sign Sorter" --out <scratch>/debosnys-sign-sorter.html

Then publish that file to the URL above (same file path in the publishing session, or url=...). 1,315 tiles from the
PUBLIC page crops (glyphs/crops/*.png); 16 c4a0 boxes have no page crop. Piles start from the pass-A labels.
No museum material is used (RESTRICTED.md).

Decisions live in the artifact's db: `piles` (one doc per pile: verdict same/mark, merge_into, legacy outliers,
note), `moves` (one doc per moved tile: sid, from, to; to = ASIDE or BAD-CUT for those states), `newpiles`.
Export with ArtifactData list ... out_dir=DIR for each collection, then:

    python3 tools/sign_sorter_apply.py --labels ciphers/debosnys-1883/glyphs/box_labels.tsv --db DIR \
      --out ciphers/debosnys-1883/sorter/settled_labels.tsv --summary ciphers/debosnys-1883/sorter/summary.json

Next after the owner finishes: recut BAD-CUT tiles, one Opus re-transcription against the settled inventory, and the
C4HI two-reader disagreement measured again (CRIBLIT step 1 gives the error level the H39 mixed design needs).
