# BNF-Q7-KEY (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: put on disk, as transcriptions, the two things a later key test needs for `ciphers/fr3982-nevers-toscana-1592`
(BnF fr.3982 f.25, Nevers to the Grand Duke of Tuscany, 26 Aug 1592; status open, intake gate exit 0): (A) the Nevers
key no.62 table, BnF fr.3995 fol.114-115v (Gallica ark btv1b525085665), and (B) the cipher digit string of f.25. No
decode, no segmentation attempt, no test: those come next, on Opus, with a control.
Why no.62: Tomokiyo (sources/cryptiana/web/nevers.htm, fr.3995 section): "no.62 (fol.114) (January 1594) ... Bologna ...
Substitution by figures. Polyphonic (see another article). Nulls. Figures 201-297 represent names and words (in Italian).
On fol.115v, a note says the subscription (sender) is 263227, which is 'Nivers' (227 being null) and the superscription
(addressee) is 297295, which is 'Gran duca' ... used in a letter (in Italian) from Sr Vinta to the Duke of Nevers dated 29
January 1593 (BnF fr.3983, fol.53)". BNF-Q7-ID named no.62 a candidate by shape (M).

Cap USD 4, box 90 min; stop before a unit that would cross 80% of either. Units (per call, CLAUDE.md Usage 6): leaf
location + fetch (~0.4); A: table transcription, 2 blind passes + 1 reconciliation over crops (~0.5 each = 1.5); B: f.25
digit lines, 2 blind passes + 1 reconciliation (~0.5 each = 1.5); write-up (~0.4). Model: Sonnet.

Read first: CLAUDE.md (rules 2, 4, 6, 8; Usage 6 crop paragraph), TRANSCRIPTION.md, `ciphers/fr3982-nevers-toscana-1592/
NOTES.md`, Tomokiyo's article that nevers.htm links for no.62's polyphony (find it in sources/cryptiana/web/; if it
prints a reconstruction of no.62, record it as a published source and credit it), last 30 lines of ROOM.md.

Route: images only via `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<N>/full/max/0/default.jpg` (native) and
the presentation v3 manifest at `https://openapi.bnf.fr/iiif/presentation/v3/ark:/12148/<ark>/manifest.json`; never
gallica.bnf.fr (403). UA `cipher-lab research script (contact via repository)`, one request at a time, >= 3 s apart, at
most 10 requests. Locate fol.114-115v of fr.3995 by pencil foliation (check `ciphers/birago-fr3252-1571-72/NOTES.md`, which
used this ark, for its canvas/folio offset). f.25 of fr.3982: the native image may already be on disk from BNF-Q7-ID
(`images/`); fetch only what is missing. Keep the folder under 30 MB (crops can be JPEG).

Steps
1. ROOM claim (tools/room.py, single quotes) with box end and cap.
2. Crop step, mandatory and pasted before any subagent call: `python3 tools/iiif_lines.py --image <native file> --out
   <dir> --debug` for the key table region(s) and for the f.25 cipher block; check the overlay. Subagents get only crops.
3. A: `ciphers/fr3982-nevers-toscana-1592/key_no62.tsv` -- one row per table entry: `value<TAB>meaning<TAB>grade<TAB>source`
   (grade H = both passes agree and the reconciliation sees it; M otherwise; a polyphonic value gets one row per meaning;
   nulls as meaning `NULL`; source = "BnF fr.3995 f.114r/v / 115r/v, Nevers key no.62 (numbering Tomokiyo)"). Include the
   fol.115v note (263227 = Nivers, 297295 = Gran duca) as rows with its own source line. Header comment credits Tomokiyo for
   the numbering and identification.
4. B: `ciphertext.tsv` for f.25 (one line per crop, digits exactly as written, spaces only where the writer left gaps,
   `?` after an uncertain digit, `[clear: ...]` for clear words), passA.tsv, passB.tsv, reconcile.tsv; report digit-level
   agreement.
5. NOTES.md section "## BNF-Q7-KEY (13 Oct 2026, account 2)": key rows (H/M counts, value range, nulls), f.25 digit count
   and agreement, whether the digit string's figures fall inside the key's ranges (a count, not a decode), requests per host.
6. Commit by explicit path, `tools/file_shrink_guard.py` on touched files, push (`tools/room.py --push <paths>`), ROOM done
   line "for LANE BNF-FOCUS (account 2)": key rows, H share, f.25 digits, agreement.

Do not decode or claim any reading; do not classify novelty (rule 10). Never print credentials. Never the words solved,
cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If `tools/room.py --start` fails to
push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
