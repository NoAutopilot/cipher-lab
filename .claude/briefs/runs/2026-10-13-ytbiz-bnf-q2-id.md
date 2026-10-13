# BNF-Q2-ID (Sonnet worker for LANE BNF-FOCUS, account 2 / ytbiz), 13 Oct 2026

Job: check-solved + premise check + key identification by sign shape for ONE letter, nothing else:
BnF Français 3985 no.53, fol. 89, the duc de Nevers to M. de Gièvre, Nevers, 21 August 1593, "some portions in cipher
(undeciphered)" (Tomokiyo, sources/cryptiana/web/league.htm, fr.3985 section). Do not transcribe the cipher in full and
do not decode. Cap USD 2.5 of usage, box 60 min from your claim; stop before a step that would cross 80% of either.
Units: leaf location (~0.3), 2 leaf images read (~0.3), check-solved sources (~1.0), write-up (~0.4). Model: Sonnet.

Read first: CLAUDE.md (rules 1, 2, 5, 6, 10; good-citizen rule), `.claude/briefs/check-solved.md` (whole file),
`.claude/briefs/prior-work-step.md` (run it and paste its result before step 2), `ciphers/fr3985-nevers-revol-1593/NOTES.md`
(same volume, same day: Nevers to Revol, f.88, key no.60), `ciphers/fr3986-nevers-revol-1593/key.tsv` and its
`sign_guide.md` (key no.60 tags), BNF-VALUE.md row Q2, last 30 lines of ROOM.md.

## Route (Gallica images only through BnF's API host; never gallica.bnf.fr, which answers 403)
Manifest (fetched once by the lane 13 Oct, 200): `https://openapi.bnf.fr/iiif/presentation/v3/ark:/12148/btv1b90606498/manifest.json`
(485 canvases, every label "NP"). Bourdeau places f.88r at canvases 176-177 (cyphersolver targets/nevers1593/NOTES.md),
so f.89 is about canvas 178-180: confirm by the pencil foliation on the image. Images:
`https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b90606498/f<N>/full/1600,/0/default.jpg`. Descriptive User-Agent
`cipher-lab research script (contact via repository)`, one request at a time, >= 3 s apart, at most 12 requests to
openapi.bnf.fr. Fetch once to `ciphers/fr3985-gievre-1593/images/` with a manifest.json. On 403/429/challenge stop.

## Steps
1. ROOM claim (tools/room.py, single quotes) with box end time and cap. Create `ciphers/fr3985-gievre-1593/` with
   NOTES.md (status word alone on line 1).
2. Locate f.89 (recto and verso if it continues). Record canvas, the clear text around the cipher (opening, date,
   address), how many lines/signs are in cipher, and the SIGN TYPE: symbols of key no.60's kind (compare by eye to the
   sign_guide/tag set), two-digit figures, letters, or other. Name the key family you think it is and how sure (H/M/U by
   shape only), and whether any interlinear or marginal decipherment is on the leaf (premise c).
3. Check-solved per `.claude/briefs/check-solved.md` for this letter: web + the three blogs' comment threads; Tomokiyo's
   pages (local mirror sources/cryptiana/web/: league.htm, nevers.htm, henryiv2.htm, any page naming Gièvre/Givry 1593);
   Bourdeau and Aymeloglu (shallow clone, grep only: Gievre, Gièvre, Givry, 3985, "f. 89"); DECODE listing
   (`tools/decode_list.py` or sources/decode/); the edition: Gomberville, *Memoires de M. de Nevers* seconde partie (1665,
   Gallica bpt6k64451005; read views through the same openapi image route, at most 10 views, located by the 1593 letters'
   printed pages) and any edition of Nevers's 1593 correspondence you can open. Open or full-text search each edition
   yourself; if you cannot, the item is `blocked` and say what blocked it. Identify "M. de Gièvre" if you can (name +
   source), graded as a lead.
4. Premise check (check-solved.md section): (a) decipherments the folder/Tomokiyo mention; (b) other solvers' files;
   (c) neighbouring leaves (the notice's next items; a "Double"/"Déchiffrement"; f.88 Revol same day); (d) recipient side.
5. NOTES.md: line 1 verdict (open / found-solved / blocked), line 2 the edition read and pages; sections for leaf look,
   key-family call, check-solved, premise check, requests per host; "## While waiting" with one action. Run
   `python3 tools/intake_gate_check.py fr3985-gievre-1593` and paste its output.
6. Commit by explicit path, `tools/file_shrink_guard.py` on every touched file, push (`tools/room.py --push <paths>`),
   ROOM done line "for LANE BNF-FOCUS (account 2)" with verdict, key-family call, sign count, gate exit, requests per host.

Report what was found and where it was not found; do not classify novelty (rule 10). Never print credentials. Never the
words solved, cracked, novel, first, new for anything this project did. Never call AskUserQuestion. If
`tools/room.py --start` fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
