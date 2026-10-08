# BNF-Q14-CS (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 8 Oct 2026

Job: check-solved + premise check only, for a pool of Nevers-Mantua cipher letters of 1590 in BnF Français 4698
(online; finding aid in sources/bnf-findingaids/2026-10-07/, parse with `python3 tools/bnf_findingaid.py --html`).
Cap USD 4, box 50 min. Do not transcribe, decode or class. Read CLAUDE.md (rules 1, 5, 6, 8 credit, 10),
.claude/briefs/check-solved.md (whole: six sources, Web and blog check, line-2 citation, Premise check), BNF-VALUE.md
"Wave 14" section.

Create `ciphers/fr4698-nevers-mantua-1590/` (status word alone on NOTES.md line 1; per-item verdicts as in
fr3984-sega-1593 when mixed). Items (all "Chiffre", no decipherment in the BnF record):
- no.47 f.108, Nevers to Cardinal Scipione Gonzaga, Decize, 28 Feb 1590 (copy); no.92 f.177, Nevers to the Duke of
  Mantua, Nevers, 17 Apr 1590 (minute); no.93 f.179, to Scipione Gonzaga, 9 Jul 1590; no.94 f.181, to the Duke of
  Mantua, 27 Jul 1590 (copy); nos.2-5 and 12-16, Scipione Gonzaga to Nevers, 1590; no.43 (key note "Con la lettera di
  16 febraro 1590", f.104).
FIRST, D. Bourdeau (fresh shallow clone of github.com/dbourdeau/cyphersolver, grep only): his CATALOGUE.md entry 331
lists fr.4698 nos.2-5, 47, 92 as a candidate and his targets/gonzaga1590 read the sibling fr.3979 ff.92-93 with Nevers
key no.35 ("Per Cavare 1590", fr.3995 f.64). Establish for each item whether he (or anyone) has read it: README rows,
targets/*, issues/PRs on the repository page (web), his site dbourdeau.github.io/cyphersolver. Then Tomokiyo
(sources/cryptiana/web/mantua.htm, nevers.htm, and the live site), DECODE (sources/decode dumps; fr.4698 records),
Aymeloglu, web + the three blogs, and print: Gomberville *Mémoires de Nevers* seconde partie (Gallica bpt6k64451005
full text) for Feb-Jul 1590 and any edition of Scipione Gonzaga's or Vincenzo Gonzaga's 1590 letters.
Gallica: one low-res look per letter (cipher present? any gloss = premise (c)); fr.4698's ark from the BnF notice's
Gallica link; at most 20 gallica.bnf.fr requests, 1.5 s apart.
Close: verdict per item, line 2 citing what this worker read, `python3 tools/intake_gate_check.py
fr4698-nevers-mantua-1590` pasted. If Bourdeau has a reading or work in progress on an item, it is found-solved (or
"his live candidate") -- say so plainly; the lane will not compete with his open work. Commit by explicit path including
the new folder, push with tools/room.py --push, tools/file_shrink_guard.py, ROOM done line "for LANE BNF-FOCUS" with
verdicts, gate exit code, requests per host. Report what was found and where it was not found; do not classify
novelty. Never print credentials. Never call AskUserQuestion. Never the words solved, cracked, novel, first, new for
anything this project did. If tools/room.py --start fails to push from a detached HEAD: git push origin HEAD:main;
git checkout -B main HEAD.
