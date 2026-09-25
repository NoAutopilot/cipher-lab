LANE R6 Y10 -- rah-xiquena-1868: fetch the file, find the cipher, try the sibling key (Sonnet, cap $5, box 45 minutes). Common: 2026-09-25-lane-r6-common.md.
Intake gate (live, 25 Sept 18:22 UTC): "rah-xiquena-1868: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
Read NOTES.md, and ciphers/rah-canada-1869/NOTES.md for the RAH route (OAI-PMH DIDL record -> imagen_id.do URLs -> tools/browser_fetch.js --binary)
and for its key (same archive, Isabel II's papers, 1869). Job: (1) fetch the item's 8 page images once (OAI record 15711; <= 16 requests to
bibliotecadigital.rah.es, >= 3 s apart, stop on a challenge page after one retry) into images/ with manifest.json; (2) describe each page: which
carries the ciphered telegram copy, whether a plain version, decipherment or interlinear text sits in the same file (lead classes 1-3 first:
if the file carries the clear text, align it and stop -- that is the reading); (3) transcribe the cipher (you pass A, ONE blind Sonnet subagent
pass B, tools/reconcile_passes.py, settle); (4) lead class 4: apply ciphers/rah-canada-1869's key (key.tsv + decode.json) with a script and a
random-draw control (1000 draws over the same code range), report coverage and whether covered words read; if it reads, decode_key --check and
route "for LANE V6". NOTES.md section "## Y10: capture and sibling-key trial (25 Sept 2026, LANE R6)". Hosts: bibliotecadigital.rah.es only.
ROOM done: "for LANE R6: xiquena <tokens> tokens, sibling key <target>% vs control <c>%". Report what was found; do not classify novelty.
