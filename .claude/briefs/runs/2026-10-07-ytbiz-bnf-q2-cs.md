# BNF-Q2-CS (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 7 Oct 2026

Job: check-solved + premise check only, three BnF items (three units, ~$1.8 each; cap USD 6, box 70 min from your
claim; stop before starting a unit that would cross 80% of either). Do not transcribe, decode or class (rule 10).

Read first: CLAUDE.md (rules 1, 5, 6, 9, 10; Access playbook), `.claude/briefs/check-solved.md` (whole file: six
sources, "## Web and blog check", the line-2 citation rule, "## Premise check"), `.claude/briefs/README.md` common
tail, BNF-VALUE.md section 3 (rows Q2b, Q9, Q10), ROOM.md last 30 lines.

The BnF record text for each item is in `sources/bnf-findingaids/2026-10-07/` (parse with
`python3 tools/bnf_findingaid.py --html <file>`; grep the parsed TSV for the folio). Lesson from BNF-Q1-CS (same day):
the previous queue row was already read by D. Bourdeau -- search his README.md, CATALOGUE.md and targets/ (fresh
shallow clone of github.com/dbourdeau/cyphersolver, grep only) and Tomokiyo's pages FIRST, before any print search.

## Units (one folder each, status word alone on NOTES.md line 1)
1. `ciphers/fr3631-dinteville-1593/` -- BnF Français 3631 no.27, fol. 28: "Lettre, avec chiffre, du Sr DE DINTEVILLE
   ... à monseigneur le duc de Nyvernoys ... Au camp de Collaverde, ce 14e juin 1593". Sibling project folder
   `ciphers/fr3621-dinteville-1592/` (Dinteville 1592 key rebuilt from the printed f.128; its Web and blog check and
   Premise check sections list sources already searched -- reuse, do not repeat blindly). Editions: Gomberville,
   *Mémoires de Nevers* (1665) seconde partie (Google Books H2eV4wAmIr0C) for June 1593; the 1882 *Revue de
   Champagne* Dinteville letters the sibling folder used.
2. `ciphers/fr3624-marchant-1593/` -- BnF Français 3624 nos.47, 51, 67 (ff.53, 57, 78), "Lettre, avec chiffre, du Sr
   MARCHANT ... au duc de Nevers", 6, 11 and 26 Jan 1593. Identify who Marchant is if the sources say; Gomberville
   seconde partie for Jan 1593.
3. `ciphers/fr3620-henri4-nevers-1592/` -- BnF Français 3620 no.64, fol. 70: "Lettre, avec chiffre, de HENRY [IV] ... à
   mon cousin le duc de Nyvernoys ... Escrit à Noyon, le XIIe jour de septembre 1592". Desenclos and Lasry, "An early
   French digit cipher" (Henri IV to Nevers, 1592) may be exactly this letter: find it (OpenAlex/S2/CrossRef with the
   keys, per CLAUDE.md) and say which letter it reads. Also *Recueil des lettres missives de Henri IV* (Berger de
   Xivrey) tome III for 12 Sept 1592 (Internet Archive full text).
For each: Gallica ark + canvas via Gallica SRU / `tools/gallica_folio.py` and one low-res look (cipher present? any
interlinear or marginal decipherment = premise (c)); at most 20 gallica.bnf.fr requests in total, 1.5 s apart. If a
volume is not on Gallica, quote the BnF record's availability flag and mark the unit blocked (needs-image).

## Close
Per unit: verdict on line 1, the line-2 citation of the edition this worker read, `python3 tools/intake_gate_check.py
<folder>` output pasted into NOTES.md. Commit by explicit path (include the new folders -- BNF-Q1-CS's first push
missed an untracked folder), push with tools/room.py --push, tools/file_shrink_guard.py on touched files, one ROOM
done line "for LANE BNF-FOCUS" with verdicts, gate exit codes and requests per host.

Report what was found and where it was not found; do not classify novelty. Never print credentials. Never the words
solved, cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If tools/room.py --start
fails to push from a detached HEAD: git push origin HEAD:main; git checkout -B main HEAD.
