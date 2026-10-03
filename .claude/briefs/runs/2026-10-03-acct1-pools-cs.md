# LANE-POOLS check-solved + premise check (account 1), 3 Oct 2026 22:1x UTC -- six pools, one worker each

Why: LANE-POOLS's scout (QUEUE.md "LANE-POOLS scout, 3 Oct 2026 (account 1)", raw rows in `sources/pools-scout/2026-10-03/`)
ranked eleven candidate one-sender cipher-letter pools; the top six go to check-solved before anything is called stage 2.
A pool is checked as a whole: the verdict says which letters of it are found-solved (printed in clear, period decipherment on
the leaf or beside it, read by Bourdeau/Aymeloglu/Tomokiyo/Lasry) and which are open, with counts.

Templates: `.claude/briefs/check-solved.md` in full (six sources, the "Web and blog check" section, the whole-volume grep rule,
the duplicate/copy rule, the stated-next-step rule, the editor's-note sweep) **and** its "Premise check" section (a)-(d),
in the same job, plus the common tail in `.claude/briefs/README.md`. Model Sonnet. Cap USD 6, box 60 minutes from your own
`date -u`: at 48 minutes push what you have and stop. At most 2 subagents (Sonnet). No transcription, no decoding, no key
application -- a found decipherment is recorded, not used.

Output, in your target's folder `ciphers/<slug>/` (create it; it does not exist yet -- check `ls ciphers` and ROOM.md first;
if a folder or a ROOM claim under 6 h already covers the same shelfmark, stop and flag):
- `NOTES.md`: line 1 the bare status word (`open` / `partial` / `found-solved` / `blocked`), line 2 the one sentence naming the
  edition or calendar *you* read and the pages or full-text search (CLAUDE.md Pipeline 2 intake gate); then QUEUE row pointer,
  a per-letter table of the pool (shelfmark/folio or record, date, est. signs, status: printed / period decipherment / solver
  read / open, with the source), totals (open letters, open est. signs), "## Web and blog check (<worker>, <date>)",
  "## Premise check (<worker>, <date>)" (a)-(d), and "## While waiting" if the verdict waits on anything.
- `python3 tools/intake_gate_check.py <slug>` must exit 0 for an `open`/`partial` verdict: paste its output in NOTES.md and
  in your done line. A nonzero exit you cannot fix within the box: status `blocked`, saying what blocked it.
- Do not touch QUEUE.md, POOLS.tsv or status.json -- the lane orchestrator does.

Targets (your prompt names one):

1. **es132-vargas-mexia-1578** -- BnF Espagnol 132 (Gallica btv1b10032556x), Philip II / Antonio Perez to Juan de Vargas Mexia,
   ambassador in Paris, 1577-80, ~55-60 letters in "Cipher 3" plus ~8 in "Cipher 4" (scout rows P1-01, P1-03). Key printed by
   Devos 1950 (Cp.30) and rebuilt by Tomokiyo (spanish3D.htm). Must answer: why DECODE marks records 1960-2025 "Decrypted"
   (open the listing metadata: a period decipherment? a modern one? whose?); whether CODOIN / Archivo documental español /
   Gachard / Mignet (Antonio Perez et Philippe II) print these despatches; the AGS Estado K series duplicates (recipient side);
   BL Add MS 28421. Bourdeau lists es.132 in research/gallica_sweep/bnf_candidates.txt (no target folder) -- grep his planning
   text for it.
2. **fr16144-savary-lancosme-1588** -- BnF fr.16144 (btv1b9060974c) ff.75-206, Jacques Savary de Lancosme, ambassador at
   Constantinople, to Henry III, 1588 (scout P2-D). Tomokiyo henryiii.htm gives the table. Must read: Charrière, Négociations de
   la France dans le Levant (vol. IV, IA full text: whole-volume grep for Lancosme/Savary/1588), Lettres de Henri III, the
   marginal decipherments on the leaves themselves (premise (c): count how many letters carry one).
3. **rah-juan-manuel-1521** -- DECODE R9499-R9529 (RAH Salazar 9/23-9/24), Juan Manuel, imperial ambassador in Rome, to
   Charles V, 1521-22 (scout P4-JMANUEL). Tomokiyo 2025 key on disk (`sources/cryptiana/keys/AlonsoSanchez_2.tsv`). Must read:
   Bergenroth, Calendar of State Papers Spain vol. II (1509-25) and its Supplement (Gayangos) -- whole-volume grep for Juan
   Manuel with dates; Bourdeau sanchez1522/ and lopehurtado/ (lopehurtado NOTES ~line 704 names "Juan Manuel's table still
   untested": state-next-step rule); which records carry a contemporary decipherment (R9528 does).
4. **fr16142-noailles-constantinople-1571** -- BnF fr.16142 (btv1b9060927q) ff.109-275, François then Gilles de Noailles at
   Constantinople, 1571-76 (scout P2-C). High edition risk: Charrière, Négociations dans le Levant vol. III prints Noailles'
   dispatches -- whole-volume grep and per-letter match (which are printed, which in clear, which with "[chiffre]" notes);
   Lettres de Catherine de Médicis (recipient side). Note `ciphers/fr3151-noailles-1558` is a different Noailles (Antoine,
   London 1558) -- do not merge.
5. **fr16104-vivonne-spain-1572** -- BnF fr.16104 (btv1b9009609w), fr.16105 (btv1b9009663p), fr.16106 to f.198
   (btv1b90096628): Jean de Vivonne, sr de Saint-Gouard, ambassador in Spain, 1572-74 (scout P2-A). In-volume clerk's
   "dechifré de la precedente" leaves seen (16105 canvases 48, 200): count them. Must read: any printed Saint-Gouard
   correspondence (search: "Saint-Gouard" "Vivonne" dépêches 1572 édition), Mousset's Longlée intro pp.xlviii-li on misplaced
   decipherments, Lettres de Catherine de Médicis vols 4-5, Gachard (Bibliothèque nationale à Paris, notices).
6. **baluze167-davaux-1637** -- BnF Baluze 167-171 (167 btv1b9001489r, 168 btv1b9001503k, 169 btv1b9001488b, 170
   btv1b90015040; 171 Gallica ark not found), Chavigny / Bouthillier / La Barde / Louis XIII to Claude de Mesmes comte d'Avaux,
   1637-41, ~68 letters with short cipher passages (scout P1-02). Contemporary interlinear decipherments seen (168 f.131).
   Must answer: how many passages carry an interlinear decipherment (premise (c)); printed d'Avaux correspondence (e.g. the
   Acta Pacis Westphalicae series, "Correspondance diplomatique" d'Avaux) for 1637-41; Tomokiyo louisxiii.htm; Bourdeau
   SOLVED_CATALOGUE.md line ~239 "Read in part". Note `ciphers/davaux-1633` (Baluze 188, found-solved) is a different letter.

Good-citizen rule: one request at a time per host, >= 1.5 s apart; Gallica with a browser UA; stop a host on 429/403/challenge.
Google Books calls carry `&country=US&key=$GOOGLE_BOOKS_KEY`; OpenAlex/S2 keys as headers (CLAUDE.md item 3). Never print
credentials. Report request count per host.

Done line (tools/room.py, role "LANE-POOLS CS-<n> (account-1 worker)"): `done (<start>-<end> UTC, brief met|box|cap): commit
<sha>. <slug>: <status>; <k> of <n> letters open, est <signs> open signs; read <edition pp.>; intake gate <exit>; requests per
host ...; cost: see the lane ledger`. Report what was found and where it was not found; do not classify novelty.
