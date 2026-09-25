LANE R6 MJ and MR -- espagnol142-mercy-1648: a register-matched judge corpus, and a fresh-instance re-derivation. Common: 2026-09-25-lane-r6-common.md.
Intake gate (live, 25 Sept 18:18 UTC): "espagnol142-mercy-1648: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
State (M2, NOTES.md "M2: graded reading"): key.tsv, exceptions.tsv, decode.json, reading.txt; S 494 M 27 of 521 codes; decode_key --check 0.
Judge on es17 (Cervantes + Quevedo) FAILs the reading (-1.034 vs real_p05 -0.875) AND the letter's own clear words (-0.892 vs -0.888):
the corpus is the wrong register (CLAUDE.md rule 3, V6-PTCORP lesson).
MJ (Sonnet, cap $4, box 40 minutes; hosts archive.org only): build tools/data/es17c/ -- Spanish diplomatic/chancery prose of c.1630-1660,
>= 200k letters, from archive.org djvu text (e.g. Coleccion de documentos ineditos para la historia de Espana volumes printing the Spanish
plenipotentiaries' correspondence at Munster 1643-1648, or other printed Spanish state letters of the 1640s). HOLD-OUT RULE: grep every
candidate volume for "Mercy", "Mercij", "Barneton", "Sumiller" and "Brandenburg" near 1648; exclude any page that could hold this letter or
its reply from the corpus, and if the letter itself appears in print, stop, flag it in ROOM ("flag: possible print of the Mercy letter at
<identifier> p.<n>") and say so in NOTES.md -- that is a verifier's lead, not yours to classify. Add es17c to LANG_CORPORA as a named option
(keep es17 the default), selftest, and report: real-prose false-negative rate on held-out es17c text, then judge the clear words alone and the
reading with a spec variant naming es17c (paste both outputs). NOTES.md section "## MJ: register-matched judge (25 Sept 2026, LANE R6)".
MR (Sonnet, cap $2, box 25 minutes; disk only): the rule-7 re-derivation. Read ONLY specs/espagnol142-mercy-1648.json, ciphertext.tsv,
key.tsv, exceptions.tsv and decode.json (not reading.txt, NOTES.md's M2 section, m2/ or corrections.tsv). Regenerate the reading with
`tools/decode_key.py ciphers/espagnol142-mercy-1648` into rederive/reading_fresh.txt, diff it against the committed reading.txt, and report
the number of differing tokens against the M-graded count (27). Then run --check. NOTES.md section "## MR: fresh re-derivation (25 Sept 2026,
LANE R6)". Both: ROOM done "for LANE R6: mercy <MJ judge result | MR diff n vs M 27>". Do not classify novelty.
