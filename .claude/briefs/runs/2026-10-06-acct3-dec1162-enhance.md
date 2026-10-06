# DEC1162-ENHANCE (written by account 3, 6 Oct 2026 23:2x UTC, for account 1). Opus 5.5. Cap $4, box 50 min.
The owner cannot read the 22 split clear-text words of DECODE R1162 (Modena, Amb. Ung. b.2/20 no.6, Italian 1492): "I don't speak the
language ... apply a darkened filter on them and then whiten the background". The person read is withdrawn; do it by image work.
Inputs: ciphers/decode-1162-modena-ambung-1492/clear/focus/ (focus-sheet.html, the 22 word crops and their line crops, the two blind
passes and the reconciliation that left them split).
1. Enhance each word crop at native resolution (no upscaling past native): greyscale, background flattening (large-kernel blur
   subtract or morphological top-hat), contrast stretch, then a light binarisation (Sauvola or Otsu) -- keep both the enhanced grey and
   the binarised version; paste the script and parameters; never alter the source images.
2. Two blind Opus reads per word on the enhanced crops plus its line context (letters only, with the abbreviation notation of the
   focus sheet: ^ superscript, ~ tilde/macron, ? doubtful, [?] unread), then one reconciliation unit (CLAUDE.md Usage 6: 2 reads +
   1 reconciliation, priced per call). Known-answer control first: run the same protocol on 5 already-settled words of the same
   hand (from the reconciled transcription) and report how many it gets right; if under 4/5, stop and log "untested-by-this-tool".
3. Settle a word only where both reads agree after enhancement; others stay [?] with both readings noted. Write the result into the
   clear-text transcription with grades, F19 (the month: February or September) called out explicitly.
4. NOTES.md section, ROOM done line for the account-3 orchestrator. No novelty words.
