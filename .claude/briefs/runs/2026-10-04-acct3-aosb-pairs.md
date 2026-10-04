# AOSB-PAIRS (account 3 worker) -- 4 Oct 2026 20:2x UTC (account-3 orchestrator)
Target: ciphers/riksarkivet-r4282-1628 (+ sibling R4284 in the same folder). Lead (NOTES.md "Lead: AOSB I:4 prints Oxenstierna cipher
passages WITH their cipher numbers"): AOSB ser. I Band 4 (1909) letter 231, Oxenstierna to Paul Strasburg, Elbing 24 Jan 1629,
pp. 341-342: the cipher passages printed in clear between asterisks, footnotes 2-11 printing the cipher numbers per passage; the editors
deciphered with the "chifferklaven" in Riksarkivet (fn 10 on p.342 names a code: "Siculi" (szekler) per the key, "Hungarorum" in the
copy, "enligt klaven betecknadt med 1782"). Original Uppsala UB E 388 c; copy by Schilher in Riksarkivet, Transsylvanica; printed earlier
by Szilágyi. Owner's screenshots (p341, p342, p343, p344, p715) are in the PRIVATE repo cipher-lab-private,
riksarkivet-r4282-1628/aosb-I4-screens-2026-10-04/ (clone it read-only; never commit the images to this public repo).
1. Transcribe the footnote cipher numbers and the matching asterisked clear passages into ciphers/riksarkivet-r4282-1628/aosb/pairs.tsv
   (fn, passage clear text, cipher tokens in order): two independent blind subagent reads of per-footnote crops (PIL crop locally,
   one call per footnote block), then one reconciliation pass (price it as N reads + 1). Mark any digit the two reads split as '?'.
   If the screenshot resolution makes more than ~5% of tokens '?', stop after step 1 and write the exact zoomed crops the owner should
   take (page, footnote numbers) as a LOCAL-QUEUE row -- do not guess digits.
2. Align plaintext to cipher (tools/interlinear_align.py, the general known-plaintext aligner): learn the system's design (homophones for
   letters? 2-digit letters + 3-4 digit word/name codes? letter signs like λ H II Q O γ as nulls/specials?) and write a partial key
   ciphers/riksarkivet-r4282-1628/aosb/key_aosb1629.tsv, grade C (period key via the 1909 editors), with counts.
3. Rule 3 order, pre-registered before scoring (PREREG file pushed first): does this key family fit R4284's numeric body or R4282?
   Statistic: coverage + decode language score (Latin) of R4284/R4282 under the partial key vs a matched control of 200 shuffled keys
   (same value set); a key-family crossmatch like tools/ crossmatch scripts the folder already uses (see scripts/ and keys*_overlap.json).
   Control first: the same statistic on the AOSB passages themselves held out (leave-one-footnote-out) must pass, else stop and log
   "untested-by-this-tool".
4. NOTES.md section + HYPOTHESES.md row with both numbers; Remaining gaps/Escalation updated; gaps_check; file_shrink_guard; ROOM done.
Report what was found and where it was not found; do not classify novelty. Disk only (no HathiTrust: Cloudflare-blocked from the cloud).
Model Opus 5.5. Cap USD 6, box 50 min. ROOM claim/done via tools/room.py.
