# BIRAGO-NUM (account-3 orchestrator, 2 Oct 2026): the Nov 1571 numerical system, pooled with a second letter

Targets ciphers/birago-nevers-1571 (fr.3251 f.119, 13 Nov 1571, 483 digits, Tomokiyo transcription) and
ciphers/birago-fr3252-1571-72 (fr.3252 f.100r, 8 Jan 1572, ~800 digits; NEVBIR-3252 340ddeae: same inventory -- digits
with m/n/h/f, the divide sign and superscript crosses). Model Opus 5.5. Cap $10, box 80 min.
Credit and prior work: D. Bourdeau attempted f.119 on 16 Sept 2026 (cyphersolver targets/birago/NOTES.md, MIT/CC BY
4.0), glyph-level re-transcription, variable-length designs excluded against controls, "structure narrowed, not
read". Read his NOTES first (grep a fresh shallow clone; cite, do not re-derive his exclusions). Rule 3: the new
material (a second letter in the same system, ~1,300 digits pooled) is what justifies a new attempt.
1. Transcribe f.100r from native Gallica crops (btv1b9060232m canvas 101; tools/iiif_lines.py command pasted; check
   --follow-slope line assignment by the debug overlay -- NEVBIR-3252 found it merged L02 into line 1), 2 blind passes
   + 1 reconciliation, superscripts and diacritics placed per Tomokiyo's/Bourdeau's convention for f.119 so the two
   letters are in one notation (rule 3 transcription-convention paragraph). Report two-reader error.
2. Design analysis on the pool, not yet an attack: digit-pair/triple statistics per Bourdeau's surviving design(s),
   repeats shared across the two letters (a repeat of length >=6 across letters is a strong signal of shared codes),
   modifier-letter distribution, and the period's Nevers-network numerical codes (Tomokiyo nevers.htm nos.19-20 use
   figures up to 99/136 for words: check whether either table's structure fits). tools/design_prior.py on KEY-DESIGN.
3. If one design survives with a matched control at the pooled N and measured error (tools/family_run.py where the
   family exists), run it; otherwise write the design note with the numbers and the named next test.
HYPOTHESES rows, NOTES in both folders, gaps_check, PROGRESS row "Birago numerical (f.119 + f.100)". Report what was
found and where it was not found; do not classify novelty. Done line "for the account-3 orchestrator".
