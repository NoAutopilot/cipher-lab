# BIR87-SORTER (account 3 worker) -- 4 Oct 2026 11:5x UTC (account-3 orchestrator)
Target: ciphers/nevers-birago-fr3251-1572. Job: build (do not publish) a small sign-sorter page that lets the owner put the no.87 tiles
(f.178r, f.178v, f.179r; atlas/topk/no87.tsv, atlas/pages.json) into HIS OWN piles from the 4 Oct sort
(sorter/owner-sort-2026-10-04/settled_labels.tsv: 105 piles over f.117/f.144r/f.168), so BIR-KEYFIT's named next step can run:
tools/interlinear_align.py on owner-labelled no.87 against the clerk sheet (harvest/keyfit/RESULTS.md "Next").
1. Scope it small ("mini"): only no.87 tiles whose atlas family is one the owner SPLIT or created a new pile in (compare
   labels_as_published.tsv vs settled_labels.tsv per family); other no.87 tiles keep their atlas label and stay off the page. State the
   tile count in ROOM before building; if it is over ~250, keep the families with the most no.87 occurrences up to ~250 and list the rest.
2. Piles = the owner's piles for those families, named exactly as in settled_labels.tsv. Each pile shows up to 6 of the owner's own tiles
   as reference examples (marked so they read as "already sorted by you", e.g. pre-approved/kept via the page's existing kept/checked
   state, never moved by the apply step) -- if tools/sign_sorter.py has no way to show locked reference tiles, add an option for it
   (Usage 8: an option on the shared tool + an offline test + a browser test in tools/sign_sorter/browser_tests, run_all.sh green).
3. Seed each no.87 tile into the owner pile whose reference tiles it is nearest to (atlas bitmaps.npz, the same distance glyph_atlas uses);
   put tiles whose top two owner piles are within a small margin in the focus box ("Check these first"), at most 30.
4. No sign values anywhere in the page or its inputs (sorter rule). No DECODE material. Gallica-derived crops only, already on disk; 0
   network requests expected.
5. Write inputs + a build.sh + README under ciphers/nevers-birago-fr3251-1572/sorter/no87/ (the README gives the exact build and apply
   commands, and how settled no.87 labels feed tools/interlinear_align.py); build the HTML into your scratchpad to check it renders with
   no script errors, but commit only inputs/scripts (the orchestrator builds and publishes). Pages over ~4 MB: shrink strips.
Model Opus 5.5. Cap USD 6, box 60 min (stop before a step that would cross 80% of either). ROOM claim/done via tools/room.py. Do not
run the alignment itself, do not change key files, do not touch other targets.
