# BNF-Q1-CS (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 7 Oct 2026

Job: check-solved + premise check, nothing else, on three BnF cipher letters of the "no.54" pool (Tomokiyo's Nevers
collection no.54, the Spanish syllabic numerical cipher of 1592). Cap USD 4 of usage, box 50 min from your claim;
stop before starting a step that would cross 80% of either. Model: Sonnet. Do not transcribe, decode, or class.

Read first: CLAUDE.md (rules 1, 5, 6, 9, 10; Access playbook), `.claude/briefs/check-solved.md` (whole file: the six
sources, the required "## Web and blog check" section, the line-2 citation rule, the "## Premise check" section),
`.claude/briefs/README.md` common tail, BNF-VALUE.md section 3 row Q1, the last 30 lines of ROOM.md.

## Targets (one new folder for the pool)

Create `ciphers/fr3983-no54-pool-1593/` with NOTES.md (status word alone on line 1). Items, all BnF Département des
Manuscrits, Collection "Mémoires de la Ligue" (finding aid ark:/12148/cc504266, snapshot
`sources/bnf-findingaids/2026-10-07/cc504266.html`; parse it with `python3 tools/bnf_findingaid.py --html <file>`):
1. Français 3983 no.45, fol. 98: "Lettre, avec chiffre, d'el conde DE MIRANDA ... al duque de Feria ... De Napoles, a
   25 de hebrero 1593. En espagnol." Tomokiyo (sources/cryptiana/web/league.htm, fr.3983 section): "(undeciphered)",
   lists it among letters that "use cipher no.54 of the Nevers collection".
2. Français 3983 no.79, fol. 162: "Lettre, avec chiffre, d'el duque DE SESSO ... a don Diego de Ibarra ... De Roma,
   11 de março 1593". Same Tomokiyo list.
3. Français 3984 no.68, fol. 145: "Lettre, avec chiffre, de D. DIEGO DE IBARRA ... De Paris, a 10 de julio 1593".
   Not in Tomokiyo's no.54 list -- record what his pages say about it, if anything.
Glossed siblings in the same volumes (catalogue: "avec chiffre et déchiffrement"): fr.3983 ff.198, 199, 205, 207, 209
(nos.102, 103, 107, 108, 109) and fr.3984 f.108 (no.47, "commencement de déchiffrement"). Do NOT read them as targets;
list them in NOTES.md as the known-answer pool for a later first test.
Key in this repository: `ciphers/fr15575-syllabic-1592-95/key_no54.tsv` (syllabary only; nomenclator not transcribed)
and that folder's NOTES.md/AUDIT.md (read its check-solved and its own search list; reuse its sources, do not redo them
blindly).

## Steps
1. ROOM claim (tools/room.py, single quotes) with box end time and cap.
2. Gallica: confirm each leaf exists and carries cipher at low resolution (fr.3983 and fr.3984 arks: find them in
   KEYHUNT-2026-10-07.tsv or the fr3984-sega-1593 / fr3983-pisany-nevers-1593 folders; `tools/gallica_folio.py ARK
   --folio N` for the canvas). One thumbnail per leaf, no native fetch. Record ark, canvas, and whether any interlinear
   or marginal decipherment is visible (premise (c)). Requests to gallica.bnf.fr: at most 15, 1.5 s apart.
3. Check-solved per `.claude/briefs/check-solved.md` for each of the three letters: web + three blogs (comment threads),
   Tomokiyo's pages (league.htm, spanish3.htm, nevers.htm, any page naming Miranda, Sessa, Ibarra, Feria in 1593 --
   local mirror sources/cryptiana/web/), Bourdeau and Aymeloglu (shallow clone, grep only: Miranda, Sessa, Ibarra,
   Feria, 3983, 3984), DECODE listing (`tools/decode_list.py` or the dumps under sources/decode/), and print: the
   standard edition for Spanish 1593 correspondence on French affairs -- at least *Archivo General de Simancas, Estado K
   (Papeles de Estado: Francia)* calendars (Daumet / Paz *Catálogo IV*), Lefèvre *Correspondance de Philippe II sur les
   affaires des Pays-Bas* 2e partie t.IV (Google Books API with key + country=US), and any CODOIN volume on Feria's
   1593 embassy (the Estates of 1593). Open or full-text search each named edition yourself; if you cannot, the item is
   `blocked`, and say what blocked it.
4. Premise check (check-solved.md section): (a) decipherments the folder or Tomokiyo already mention; (b) other solvers'
   working files; (c) neighbouring leaves (the catalogue's own next items, e.g. a "Double" or "Deschiffrement" nearby);
   (d) recipient-side editions (Feria's, Ibarra's papers; Philip II's).
5. Verdict per item on NOTES.md line 1 (one of open / found-solved / blocked; a pool folder with mixed results uses the
   per-item form other folders use, e.g. fr3984-sega-1593), line 2 the edition actually read and pages. Run
   `python3 tools/intake_gate_check.py fr3983-no54-pool-1593` and paste its output in NOTES.md.
6. Commit by explicit path, push (`tools/room.py --push <paths>`), run `tools/file_shrink_guard.py` on every file you
   touched, ROOM done line "for LANE BNF-FOCUS" with the verdicts, the intake gate exit code, requests per host.

Report what was found and where it was not found; do not classify novelty (rule 10). Never print credentials. Never
the words solved, cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If
`tools/room.py --start` fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
