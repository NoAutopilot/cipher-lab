# IMG-GALLICA1: two Gallica image surveys (3 Oct 2026, written by LANE-IMAGES, account 2)

Model: Opus 5.5. Cap USD 5; box 60 min from your claim. Units: 2 (clair1161 ~USD 3 incl. up to 5 contact-sheet vision calls;
fr3151 ~USD 2 incl. up to 2 vision calls). Stop before a unit that would cross 80% of cap or box. No transcription, no decoding.
You are the only Gallica worker in this lane: one request at a time, >=2 s apart, on altcha/challenge/SSL reset one pause and one
retry, then stop that host and log it.

Start: `python3 tools/room.py --start` (detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`); `date -u`; claim
`python3 tools/room.py "IMG-GALLICA1 (account 2 worker, for LANE-IMAGES)" 'claim: clair1161-avis-flandre-1688 canvas sweep + fr3151-noailles-1558 fr.10773 survey (Gallica IIIF); box ends <HH:MM> UTC'`.
Read both NOTES.md (last sections, "While waiting", the canvas_sweep.tsv) and the CLAUDE.md Gallica host row first.
1. clair1161-avis-flandre-1688: close the ~65 unsampled canvases of ark btv1b90010063 (c1-14 and the gaps in
   images/canvas_sweep.tsv) at 300 px via the IIIF image API (`tools/gallica_folio.py` for labels/offsets). Build contact sheets
   locally (PIL, 16 per sheet, canvas index printed under each), look at them (<=5 vision calls) and extend canvas_sweep.tsv with one
   row per canvas: folio number if legible, content class (cipher / clear / blank / print). If the "Avis de Flandre" cipher leaf is
   found, fetch it once at native resolution, cut line crops with `tools/iiif_lines.py --ark ... --canvas N --region ... --debug`
   (check the overlay), manifest entries, and flip the leaf-locator blocker. Thumbnails are scratch: commit the TSV and contact
   sheets only (<1 MB each), not the 65 thumbnails.
2. fr3151-noailles-1558: survey Gallica fr. 10773 (btv1b52527305r, copies of Noailles's Venice/Constantinople dispatches): canvas
   labels first, then <=2 vision calls on contact sheets at <=1000 px, looking only for a copied cipher alphabet/key table or a
   deciphered copy of the Nov 1558 letters (dates in the folder). Record per-canvas classes in a TSV; fetch native + crops only for a
   key table or a cipher/decipherment page of Nov 1558.
NOTES.md per target: catalogue/availability flag quoted (ark + manifest), route that worked, request count per host, what was and
was not found. Keep folders under 30 MB. Grades: none. gaps_check on any partial folder. Rule 10 wording; "report what was found and
where it was not found; do not classify novelty". Never call AskUserQuestion.
End: commit by explicit path, `python3 tools/file_shrink_guard.py <paths>`, `python3 tools/room.py --push <paths>`, confirm on
origin/main, one done line for LANE-IMAGES (account 2): per target result, requests per host, vision calls used.
