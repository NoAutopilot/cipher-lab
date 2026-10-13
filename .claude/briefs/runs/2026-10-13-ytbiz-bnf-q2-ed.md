# BNF-Q2-ED (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: the one missing edition step for `ciphers/fr3985-gievre-1593` (BnF fr.3985 no.53 f.89, Nevers to M. de Gièvre,
Nevers, 21 Aug 1593): is this letter printed in Gomberville, *Memoires de M. de Nevers*, seconde partie (1665, Gallica
bpt6k64451005)? Nothing else: no transcription, no decode, no classification.
Cap USD 1.5, box 45 min from your claim; stop before a step that would cross 80% of either. Units: ~15 page reads at
~0.06 each (BNF-RONDI2 rate) + write-up. Model: Sonnet.

Read first: CLAUDE.md (rules 1, 5, 6, 10; good-citizen rule), the folder's NOTES.md, `ciphers/fr3613-rondinelli-1590/
gomb_views.tsv` (views 263-273, 387-393, 443-452 already read: printed pp.213-224, 338-344, 394-403, with their letter
dates -- use them to place 1593), last 30 lines of ROOM.md.

Route: images only through BnF's API host, never gallica.bnf.fr (403):
`https://openapi.bnf.fr/iiif/image/v3/ark:/12148/bpt6k64451005/f<N>/full/1600,/0/default.jpg`; manifest
`https://openapi.bnf.fr/iiif/presentation/v3/ark:/12148/bpt6k64451005/manifest.json` (one request, gives the view count).
Descriptive UA `cipher-lab research script (contact via repository)`, one request at a time, >= 3 s apart, at most 18
requests. Fetch once to `ciphers/fr3985-gievre-1593/images/gomb/` with a manifest.json; on 403/429/challenge stop.

Steps
1. ROOM claim (tools/room.py, single quotes) with box end and cap.
2. Find the volume's table of contents (usually the last views; the manifest gives the count) -- read 2-4 views. Locate
   from it the letters of August-September 1593 and any letter to Gièvre/Givry/"M. de Gievre". If there is no usable
   table, bisect by printed date using gomb_views.tsv as anchors.
3. Read the views covering 15 Aug - 10 Sept 1593 (or the table's hit) as images; one TSV row per view in
   `ciphers/fr3985-gievre-1593/gomb_views.tsv` (view, printed page, letter headings with dates, Gièvre? yes/no).
4. NOTES.md section "## BNF-Q2-ED (13 Oct 2026, account 2)": found / not found, edition + pages read. Line 1 per
   `.claude/briefs/check-solved.md`: if the letter is printed (deciphered or in clear) -> found-solved with the page; if not
   found and the other sources are complete (they were, per BNF-Q2-ID) -> open, line 2 citing Gomberville seconde partie
   and the pages read. Paste `python3 tools/intake_gate_check.py fr3985-gievre-1593`.
5. Commit by explicit path, `tools/file_shrink_guard.py` on touched files, push (`tools/room.py --push <paths>`), ROOM done
   line "for LANE BNF-FOCUS (account 2)" with verdict, pages read, gate exit, requests per host.

Report what was found and where it was not found; do not classify novelty (rule 10). Never print credentials. Never the
words solved, cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If
`tools/room.py --start` fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
