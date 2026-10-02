# NEVBIR-OFFSHEET (account-3 orchestrator, 2 Oct 2026): fill the fragments -- value fits for off-sheet signs, 1572 key

Target ciphers/nevers-birago-fr3251-1572. Model Opus 5.5. Cap $7, box 60 min. Disk only.
Why: nos.71/86/90 read as fragments; about 10% of signs are off Tomokiyo's sheet (X_NEW and subtypes, T83-like r
sign of NEVBIR-185B) and drop whole words. Pool every 1572 reading on disk (nos.71, 86, 87, 90; ~2,700 signs).
1. Method check on the known answer FIRST: on no.87 (clerk's clear sheet, canvas 182; GAPS4), hide the sheet, fit each
   recurring off-sheet sign by maximising the 1572 judge corpus score of the pooled decode, then compare with the
   sheet. Pre-register the rule (min occurrences, min gain, shuffled-sign control: the same fit on a randomly chosen
   in-key sign's occurrences relabelled must not gain as much). If the method gets <70% of no.87's off-sheet values
   right, stop: log "untested-by-this-tool" and report.
2. If it passes: fit the recurring off-sheet signs across nos.71/86/90 (>=3 occurrences each), each with its own
   shuffled control; accept only fits that beat their control; grade accepted values M (fitted by us), never S.
   Write an exceptions/fit file read by decode_key (no private decoder), re-run decode_key --check, report the change
   in S/M/U per letter and the newly readable word fragments in English (gloss style of harvest/gloss_no90.md).
3. HYPOTHESES.md rows (both numbers), NOTES.md section, gaps_check, PROGRESS rows' notes only (firm counts move only
   if a verifier later endorses). Do not classify novelty. Done line "for the account-3 orchestrator".
