LANE R6 Y3 -- clair1161-avis-flandre-1688: transcription of the cipher leaf (Sonnet, cap $6, box 45 minutes). Common: 2026-09-25-lane-r6-common.md.
Intake gate (live, 25 Sept 15:42 UTC): "clair1161-avis-flandre-1688: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
Read NOTES.md in full. Disk only: images/f106_full.png and images/manifest.json (no Gallica fetch; if the image is too coarse to read, say
so, give the crop that shows it, and stop). Job: (1) first look for any decipherment on the leaf (interlinear words, a marginal gloss, a
facing plain version) -- if present it is the lead and you align the cipher against it instead of two blind passes (R4 common); (2) otherwise
cut line crops (tools/iiif_lines.py works on a local file only if it accepts one; else a small script with the same output layout, crops
under 2500 px), two blind passes (you = pass A, ONE Sonnet subagent = pass B, never opens pass A, writes to disk), tools/reconcile_passes.py,
gate >= 80 percent token agreement, settle disagreements.tsv on the image, write ciphertext.tsv plus a one-paragraph description of the
system (numbers? groups? symbol count? plain words mixed in?) and token/type counts. No cryptanalysis, no spec (the orchestrator decides
the next step). NOTES.md section "## Y3: transcription (25 Sept 2026, LANE R6)". Hosts: none. ROOM done: "for LANE R6: clair1161 <tokens>
tokens, <types> types, agreement <x>%".
