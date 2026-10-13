# BNF-Q7-ID (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: check-solved + premise check + key-family call by sign shape for ONE item, nothing else: BnF Français 3982, fol. 25
(BNF-VALUE.md row Q7): the duc de Nevers to the Grand Duke of Tuscany (Ferdinando I de' Medici), 26 Aug 1592, a minute in
Italian marked as in cipher ("chiffrée"). Do not transcribe in full, do not decode. No Tomokiyo entry was found for it
by the lane (13 Oct, local mirror grep for 3982 + Tuscany/Grand Duke); Bourdeau's repository has fr.3982 only for no.22
(Pelissier to Jeannin, ff.46-50, his catalogue item 16) -- confirm both yourself.
Cap USD 2.5, box 60 min; stop before a unit that would cross 80% of either. Units: leaf location (~0.3), 2-3 leaf
reads (~0.3), check-solved sources (~1.2), write-up (~0.4). Model: Sonnet.

Read first: CLAUDE.md (rules 1, 2, 5, 6, 10; good-citizen rule), `.claude/briefs/check-solved.md` (whole file),
`.claude/briefs/prior-work-step.md` (run it, paste its result before step 2), BNF-VALUE.md row Q7, KEY-OFFICES.tsv rows
for Nevers and for Tuscany/Florence, last 30 lines of ROOM.md.

Route (Gallica images only through BnF's API host; never gallica.bnf.fr, which answers 403):
the fr.3982 ark is in KEYHUNT-2026-10-07.tsv or the fr4715-f61-mayenne-1592 / fr2751-dediou-mayenne folders (search
for 3982). Manifest: `https://openapi.bnf.fr/iiif/presentation/v3/ark:/12148/<ark>/manifest.json`; images
`https://openapi.bnf.fr/iiif/image/v3/ark:/12148/<ark>/f<N>/full/1600,/0/default.jpg`. Labels may all be "NP": locate
f.25 by the pencil foliation (canvas is about 2 x folio in these volumes; read one canvas, then step). UA
`cipher-lab research script (contact via repository)`, one request at a time, >= 3 s apart, at most 12 requests.
Save to `ciphers/fr3982-nevers-toscana-1592/images/` with a manifest.json (keep the folder under 30 MB).

Steps
1. ROOM claim (tools/room.py, single quotes) with box end and cap. Create `ciphers/fr3982-nevers-toscana-1592/` with
   NOTES.md (status word alone on line 1).
2. Leaf look: canvas, clear text (opening, date, address), language, extent of cipher (lines, rough sign count), SIGN
   TYPE (figures, symbols, letters; one- or two-digit groups; dots/marks), any interlinear or marginal decipherment or a
   clear copy nearby (premise c). Key-family call by shape with grade (H/M/U) against KEY-OFFICES rows (Nevers keys of
   1592, e.g. no.70 for Gonzague-Clèves; Tuscan keys if any).
3. Check-solved per `.claude/briefs/check-solved.md`: web + the three blogs' comment threads; Tomokiyo (sources/cryptiana
   /web/: nevers.htm, league.htm, any page naming Toscana/Tuscany/Ferdinand 1592); Bourdeau and Aymeloglu (shallow clone,
   grep only: 3982, Toscan, Tuscany, Ferdinand, Medici, Granduca); DECODE listing (`tools/decode_list.py` or
   sources/decode/). The standard edition: Canestrini and Desjardins, *Négociations diplomatiques de la France avec la
   Toscane*, vol. V (1875; covers 1589 onward) -- find it on archive.org (advancedsearch, then the `_djvu.txt` full text)
   and full-text search it for "Nevers"/"Nivers" and "1592" around August; open it yourself. Gomberville's Memoires de
   M. de Nevers seconde partie pp.660-697 (1591-1594) were read in full on 13 Oct for another letter
   (`ciphers/fr3985-gievre-1593/gomb_views.tsv`): no Tuscany letter there -- cite that file, do not re-read it. If an
   edition cannot be opened, the item is `blocked` and say what blocked it.
4. Premise check (check-solved.md section): (a) decipherments the record/Tomokiyo mention; (b) other solvers' files;
   (c) neighbouring leaves (notice items next to f.25; a reply from Florence); (d) recipient side (Florentine archives'
   Mediceo del Principato is not online: say so; the Canestrini volume is the recipient-side print).
5. NOTES.md: line 1 verdict (open / found-solved / blocked), line 2 the edition read and pages; sections for leaf look,
   key-family call, check-solved, premise check, requests per host; "## While waiting" with one action. Paste
   `python3 tools/intake_gate_check.py fr3982-nevers-toscana-1592`.
6. Commit by explicit path, `tools/file_shrink_guard.py` on touched files, push (`tools/room.py --push <paths>`), ROOM
   done line "for LANE BNF-FOCUS (account 2)": verdict, key-family call, sign count, gate exit, requests per host.

Report what was found and where it was not found; do not classify novelty (rule 10). Never print credentials. Never the
words solved, cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If
`tools/room.py --start` fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
