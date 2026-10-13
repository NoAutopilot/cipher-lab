# BNF-RONDI-TX (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: transcribe the cipher of BnF fr.3613 no.33 f.62r (Hercole Rondinelli to the duc de Nevers, Paris, 11 Nov 1590;
`ciphers/fr3613-rondinelli-1590`, status open, intake gate exit 0) into sign tags, nothing else: no decode, no key work.
Purpose: a measured transcription that a later controlled test of the period partial key `keys/block_no34.tsv` (fr.3995 f.63r,
heading "Rondinelli al S. D. ... di parigi", vowel marks written over consonants) can use.
Cap USD 4, box 90 min; stop before a unit that would cross 80% of either. Units (per call, CLAUDE.md Usage 6): fetch + crop
(~0.3); TWO blind Sonnet passes over the line crops (~17 lines; split into 2-3 calls per pass if needed, ~0.4 each);
one reconciliation call (~0.6); eye comparison of sign shapes with the no.34 block (~0.3); write-up (~0.4). Model: Sonnet.

Read first: CLAUDE.md (rules 2, 4, 6; Usage 6 crop paragraph), TRANSCRIPTION.md, the folder's NOTES.md (leaf look, BNF-RONDI3,
BNF-RONDI-KEY), `keys/sign_guide.md` and `keys/blocks_rules.md` (the tag convention and the vowel-mark rule), last 30 lines
of ROOM.md.

Route: fr.3613 is Gallica ark btv1b90582263; f.62r is on canvas 69 (f.61v/62r opening, per the leaf look) -- confirm by the
pencil foliation. Native image via `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90582263/f69/full/max/0/default.jpg`
(and one neighbouring canvas only if 69 is wrong); never gallica.bnf.fr; <= 3 requests, 3 s apart. Keep the folder under
30 MB (JPEG crops; delete the native after cropping, keep its URL in images/manifest.json).

Steps
1. ROOM claim (tools/room.py, single quotes) with box end and cap.
2. Crop step, mandatory and pasted before any subagent call: `python3 tools/iiif_lines.py --image <native> --out
   images/f62 --debug` (region = the cipher block, excluding the clear heading and the three clear Italian lines at the foot);
   check the overlay; one crop per line, order checked.
3. Extend `keys/sign_guide.md` only where f.62 shows a sign the guide lacks (name it neutrally, never by a guessed value).
   Subagents get ONLY the crops and sign_guide.md -- not the key blocks, not any guessed plaintext. Vowel marks above a
   sign are written as the base sign + `^` + the mark's own neutral name, as the guide defines.
4. passA.tsv, passB.tsv (one line per crop, `f62_L01<TAB>tags...`, `?` after an uncertain sign), then
   `python3 tools/reconcile_passes.py passA.tsv passB.tsv --crops images/f62` (if it mis-parses the tag format, say so and
   align with difflib instead), one reconciliation call that settles only the disagreements against the crops ->
   reconcile.tsv, ciphertext.tsv. Report agreement as agreement, never as accuracy (TRANSCRIPTION.md).
5. Eye comparison (M): for each base sign in f.62, does the no.34 block contain it? Count covered / not covered.
6. NOTES.md section "## BNF-RONDI-TX (13 Oct 2026, account 2)": tokens, lines, agreement, signs not in the guide, coverage by
   no.34, the clear lines at the foot transcribed as text (they may be a crib: "Io sarei partito un pezzo fa se havesti trovat..."),
   requests per host. Next step named: a blind third pass to measure error before any key test (as BNF-Q7-ERR did).
7. Commit by explicit path, `tools/file_shrink_guard.py` on touched files, push (`tools/room.py --push <paths>`), ROOM done line
   "for LANE BNF-FOCUS (account 2)": tokens, agreement, coverage by no.34.

Do not decode; do not classify novelty (rule 10). Never print credentials. Never the words solved, cracked, novel, first, new
for anything this project did. Never call AskUserQuestion. If `tools/room.py --start` fails to push from a detached HEAD:
`git push origin HEAD:main; git checkout -B main HEAD`.
