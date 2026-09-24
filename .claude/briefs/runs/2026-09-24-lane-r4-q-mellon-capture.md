LANE R4 WORKER Q -- Beinecke MELLON MS 29 pseudo-Elian cipher ff.1v-2v: capture, sign atlas, two passes (Sonnet, cap $4; no subagent
beyond one pass-B subagent). Target: ciphers/beinecke-mellon29-elia (stage 2, copy-free). Common rules:
.claude/briefs/runs/2026-09-24-lane-r4-common.md. Read NOTES.md "Image route". Bourdeau's catalogue says simple/homophonic/progressive/
Vigenere/Alberti all fail on ~234 letters -- from a DECODE thumbnail; an image-based transcription is the missing input.
Host: collections.library.yale.edu IIIF only (the manifest for catalog record 17388793 and the Image API /iiif/2/<id>/); plain curl works
for the image API; >= 2 s apart, <= 20 requests. Find the canvases for ff.1v-2v from the manifest's labels, fetch them at native size once,
images/manifest.json.
1. Crops of the cipher lines (tools/iiif_lines.py; add a plain --image-url option with a test if it only handles Gallica arks).
2. Atlas: tools/glyph_atlas.py; pseudo-Elian/pigpen shapes (angles, boxes, dots) -> codes by shape; note dots and variants as separate
   codes, never merge on meaning. Commit.
3. Pass A by you, pass B by one blind Sonnet subagent: sign codes per line, word breaks as '/' where visible. Commit each.
4. tools/reconcile_passes.py; gate 80%; settle disagreements from the crops; ciphertext.tsv; report tokens, types, word lengths.
No solving (a separate Opus brief). NOTES.md "Capture and passes (24 Sept 2026, LANE R4 Q)". ROOM done: "for LANE R4: mellon capture
<pct>, <tokens>/<types>".
