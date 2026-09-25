LANE R7 BBER -- berthier-napoleon-1812: spec and first cheap test through the breadth rule (Sonnet, cap $3, box 40 minutes; archive.org only).
Common: 2026-09-25-lane-r7-common.md and `.claude/briefs/breadth.md` (its common tail and intake step apply). No cryptanalysis, no subagents.
Intake gate (live, 25 Sept 20:03 UTC): "berthier-napoleon-1812: open (line 1) -- edition/page or full-text-search citation found within 6 lines" (exit 0).
State (NOTES.md "Y9"): 325 groups, 207 distinct, 136 hapax, range 2-1388, from Vilcoq 1969's plate (ciphertext_full.tsv, two-pass settled; use it, not
ciphertext.txt); Chuquet's 22 Dec 1812 letters XIX and XXIII do not fit against a 34-letter control; no petit-chiffre key in Cryptiana or Bourdeau.
A 1,200-entry nomenclator at N=325 is not a solver target (rule 3 ladder would fail its control), so the spec's tests are lead tests.
Job:
(1) Write specs/berthier-napoleon-1812.json in the house format (specs/README.md; copy the shape of an existing spec such as specs/antt-linhares-chave.json):
    ciphertext from ciphertext_full.tsv with source and date, alphabet (numeric groups 2-1388), constraints (nomenclator, one- or two-part unknown,
    French 1812, sender Berthier to Napoleon 22 Dec 1812), judge block for French (fr18 or fr19 corpus, whichever tools/judge_plaintext.py wires; say
    which), and cheap_tests_in_order: [0] letter XXIX (28 Dec 1812, best length fit 0.028) scored on all three Y9 metrics against the same 34-letter
    control; [1] Correspondance de Napoléon Ier vol. XXIV "votre note chiffrée" lead: find the letter on IA full text and read whether it quotes or
    answers the 22 Dec cipher; [2] one-part vs two-part code test: do the code numbers of high-frequency French function words (if any crib ever
    lands) ascend with alphabet order -- stated only, not run; [3] William Urban's Russian State Military Historical Archive find (Cryptiana napoleon2.htm),
    a print lead.
(2) Run test [0] only, with its control, reusing scripts/crib_test.py and scripts/letters.json (disk only). Write both numbers (XXIX's rank on each of
    the three metrics out of 34, and whether it beats the control on a majority) into cheap_test_done with date, method.
    If archive.org time remains inside the box, run test [1] as a print check only (IA advancedsearch + be-api fts; <=20 requests, >=1.5 s) and record it
    as cheap_test_done[1] -- this is the one exception to breadth.md's "do not run test 2", granted because [0] is disk-only.
(3) Append a section "## BBER: spec and first test (25 Sept 2026, LANE R7)" to ciphers/berthier-napoleon-1812/NOTES.md.
ROOM done: "done: for LANE R7: berthier spec written; test0 XXIX ranks <a>/<b>/<c> of 34 (control: the 33 other letters); test1 <found/not found, where>".
Report what was found and where it was not found; do not classify novelty.
