# SEURE-DEC (account 3 worker) -- 4 Oct 2026 18:4x UTC (account-3 orchestrator)
Target: ciphers/fr3151-seure-1558 (now found-solved, SEURE-WEB). Potter 2014 cites BnF fr.3151 fo. 84-87 "in cipher, with decipher".
Job: locate the period decipher on the leaves, nothing more.
1. tools/gallica_folio.py on the fr.3151 ark (in NOTES/images manifest) with eye-checked --anchor canvas=folio pairs to pin fos 84-87
   (labels are all NP). Fetch native views of those canvases once (tools/iiif_lines.py or the image API, manifest entries), <=12 requests.
2. Say where the decipher is: interlinear, margin, separate sheet, or the clear prose of item 44 being a deciphered copy of item 43.
   Test that last one cheaply: does the clear text's length/structure track the cipher block (line count, paragraphing, a few names)?
   No cryptanalysis and no key rebuild in this job.
3. If a decipher is located, write the one named next step ("period key rebuild from cipher+decipher, ~$X"; then apply to items 40/41
   of 27 Dec) into Remaining gaps; if not, say which canvases were viewed and that none carries it.
Good-citizen rule on Gallica (1.5 s apart). Model Opus 5.5. Cap USD 2.5, box 30 min. ROOM claim/done via tools/room.py.
