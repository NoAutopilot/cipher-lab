# BNF-Q7-TAB (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: transcribe two Nevers key tables from BnF fr.3995 (Gallica ark btv1b525085665) into key files that
`ciphers/fr3982-nevers-toscana-1592/q7test/screen.py` can read, nothing else: no decode, no screening run.
In priority order:
1. **no.45 (fol.84-85, endorsement "Camp Provin", August 1592)** -- Tomokiyo (sources/cryptiana/web/nevers.htm):
   "Substitution by two-digit figures. Homophones. Nulls (1, 89, 35, 28, 0). Instructions advise that '1' and '0' as
   nulls should be put in the middle of a two-figure code number as 7831452807, which is parsed as 78(u) 314(o) 52(u)
   807(s) ('87' is 's' and '0' is null)". Transcribe the alphabet, the nulls, any word/name entries, AND the
   instruction text about the intercalary nulls verbatim (it fixes the parsing rule the screen must use).
2. **no.47 (fol.88-89, "Cifra col Sr Cau re Giac[om]o Graty?", 1592, Italian)** -- alphabet, x = et, homophones, and the
   dotted-figure nomenclator (names: Don Giouanni di Jacquez, Re di Nauarra, Duca di Guisa ...).
Stop after no.45 if 80% of cap or box would be crossed by starting no.47.

Cap USD 4, box 90 min. Units (per call): locate + fetch (~0.4); per table 2 blind Sonnet passes over crops + 1
reconciliation (~0.5 each = 1.5); write-up (~0.4). Model: Sonnet.

Read first: CLAUDE.md (rules 2, 4, 6, 8; Usage 6 crop paragraph), TRANSCRIPTION.md, `ciphers/fr3982-nevers-toscana-1592/
NOTES.md` (BNF-Q7-KEY: how no.62 was located and transcribed in this same volume -- reuse its canvas offset; key_no62.tsv
is the 4-column format), `q7test/screen.py --help` (key file formats), last 30 lines of ROOM.md.

Route: `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b525085665/f<N>/full/max/0/default.jpg`, manifest
`https://openapi.bnf.fr/iiif/presentation/v3/ark:/12148/btv1b525085665/manifest.json`; never gallica.bnf.fr. UA
`cipher-lab research script (contact via repository)`, one request at a time, >= 3 s apart, at most 10 requests. Images
into `ciphers/fr3982-nevers-toscana-1592/images/fr3995/` with a manifest.json; keep the folder under 30 MB (store JPEG
crops, delete natives you no longer need after cropping, keep their URLs).

Steps
1. ROOM claim (tools/room.py, single quotes) with box end and cap.
2. Crop step, mandatory and pasted before any subagent call (`tools/iiif_lines.py --image <native> --out <dir> --debug`,
   region around each table column); subagents get only crops.
3. For each table write `q7test/key_no45.tsv` / `q7test/key_no47.tsv` in key_no62.tsv's 4-column format
   (value, meaning, grade H/M, source "BnF fr.3995 f.84r, Nevers key no.45 (numbering Tomokiyo)"), nulls as NULL,
   polyphones/homophones one row per pair, dotted or barred figures with a mark prefix you define in the header. For
   no.45 add `q7test/key_no45_rules.md`: the instruction text as read (grade each line), and the parsing rule it implies.
4. NOTES.md section "## BNF-Q7-TAB (13 Oct 2026, account 2)": rows per table, H share, value ranges, digit profile of each
   key's codes vs f.25's (q7test/digit_profile.out: f.25 has no 8, few 9s) -- a count, not a test; requests per host.
5. Commit by explicit path, `tools/file_shrink_guard.py` on touched files, push (`tools/room.py --push <paths>`), ROOM done
   line "for LANE BNF-FOCUS (account 2)": tables done, rows, H share, the no.45 rule as read.

Do not decode or run the screen; do not classify novelty (rule 10). Never print credentials. Never the words solved,
cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If `tools/room.py --start` fails to
push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
