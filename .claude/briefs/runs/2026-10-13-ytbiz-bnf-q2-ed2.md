# BNF-Q2-ED2 (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: finish the Gomberville sweep for `ciphers/fr3985-gievre-1593` (Nevers to M. de Gièvre, Nevers, 21 Aug 1593),
nothing else. Gomberville seconde partie (bpt6k64451005) is chronological (BNF-Q2-ED's gomb_views.tsv: p.659 = 1591,
pp.671-692 = an instruction of 1593 and a Sept 1593 letter, p.737 = 1597), so the Aug 1593 letters fall in pp.660-691.
Read EXACTLY these 24 unread views, every one, in order: 721-731, 733-739, 741-743, 745-747. No sampling.
Cap USD 1.5, box 45 min; stop before a step that would cross 80% of either. Units: 24 page reads at ~0.05 + write-up.
Model: Sonnet.

Route: `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/bpt6k64451005/f<N>/full/1600,/0/default.jpg` only (never
gallica.bnf.fr). UA `cipher-lab research script (contact via repository)`, one at a time, >= 3 s apart, 24 requests (+1
retry max). Save to `ciphers/fr3985-gievre-1593/images/gomb/`, add to its manifest.json. On 403/429/challenge stop.

Steps
1. ROOM claim (tools/room.py, single quotes) with box end and cap.
2. Fetch and read each view; append one row per view to `ciphers/fr3985-gievre-1593/gomb_views.tsv` (same columns):
   printed page, every letter or document heading with sender, recipient, place and date, and Gièvre/Givry? yes/no.
   Also note any letter dated 15-31 Aug 1593 from Nevers, whoever it is to.
3. NOTES.md section "## BNF-Q2-ED2 (13 Oct 2026, account 2)". If the letter is printed (in clear or deciphered):
   line 1 `found-solved`, with page. If not, and all views 721-760 are now read: line 1 `open`, line 2 "Gomberville,
   Memoires de M. de Nevers, seconde partie (1665), pp.660-699 read as images (views 721-760, openapi.bnf.fr), letter not
   printed; Tomokiyo, Bourdeau, Aymeloglu, DECODE: no decipherment (BNF-Q2-ID)". Paste
   `python3 tools/intake_gate_check.py fr3985-gievre-1593` (must exit 0 for `open`).
4. Commit by explicit path, `tools/file_shrink_guard.py` on touched files, push (`tools/room.py --push <paths>`), ROOM done
   line "for LANE BNF-FOCUS (account 2)": verdict, views read, gate exit, requests per host.

Report what was found and where it was not found; do not classify novelty (rule 10). Never print credentials. Never the
words solved, cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If
`tools/room.py --start` fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
