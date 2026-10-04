# LANE-POOLS2 check-solved + premise check (account 1), 4 Oct 2026 05:4x UTC -- four pools, one worker each

Why: the account-3 orchestrator's brief `.claude/briefs/runs/2026-10-04-acct3-lane-pools2-a3v2.md` (LANE-POOLS2 item 1) sends
the four untested pools from LANE-POOLS's scout (QUEUE.md "LANE-POOLS scout, 3 Oct 2026 (account 1)" rows 7, 9, 10, 11; raw rows in
`sources/pools-scout/2026-10-03/`) to check-solved. A pool is checked as a whole: the verdict says which letters of it are
found-solved (printed in clear, period decipherment on the leaf or beside it, read by Bourdeau/Aymeloglu/Tomokiyo/Lasry/
cabinet-noir) and which are open, with counts. The pool bar for sending a pool on is >= 2,000 open cipher signs.

Templates: `.claude/briefs/check-solved.md` in full (six sources, the "Web and blog check" section, the whole-volume grep rule,
the duplicate/copy rule, the stated-next-step rule, the editor's-note sweep) **and** its "Premise check" section (a)-(d), in the
same job, plus the common tail in `.claude/briefs/README.md`. Model Sonnet. Cap USD 6, box 60 minutes from your own `date -u`: at
48 minutes push what you have and stop. At most 2 subagents (Sonnet). No transcription, no decoding, no key application -- a
found decipherment or key is recorded, not used. Rule 4a (depth) does not apply: nothing is read.

Survey pricing (LANE-POOLS lesson, STATUS.md "LANE POOLS handoff"): a whole-volume canvas survey is priced as contact-sheet
units, not a step inside one box. Do NOT survey every canvas. Count cipher letters from the printed edition, Tomokiyo's page and
the BnF/BL catalogue first; open canvases only to sample (<= 40 Gallica requests in this job, contact sheets at 600 px, each
canvas at most once). Estimated open signs = sampled signs/page x open cipher pages, stated as an estimate with its sample size.

Output, in your target's folder `ciphers/<slug>/` (create it unless the target says otherwise; check `ls ciphers` and the last
6 h of ROOM.md first; if a folder or a ROOM claim under 6 h already covers the same shelfmark, stop and flag):
- `NOTES.md`: line 1 the bare status word (`open` / `partial` / `found-solved` / `blocked`), line 2 the one sentence naming the
  edition or calendar *you* read and the pages or full-text search (CLAUDE.md Pipeline 2 intake gate); then QUEUE row pointer,
  a per-letter table of the pool (shelfmark/folio or record, date, est. signs, status: printed / period decipherment / solver
  read / open, with the source), totals (open letters, open est. signs), "## Web and blog check (<worker>, <date>)",
  "## Premise check (<worker>, <date>)" (a)-(d), and "## While waiting" if the verdict waits on anything. A `partial` verdict
  also ends with "## Remaining gaps" and "## Escalation" (rule 5; `python3 tools/gaps_check.py <slug>` passes; format in its
  docstring).
- `python3 tools/intake_gate_check.py <slug>` must exit 0 for an `open`/`partial` verdict: paste its output in NOTES.md and in
  your done line. A nonzero exit you cannot fix within the box: status `blocked`, saying what blocked it.
- One line at the end of NOTES.md: "Pool bar: PASS|FAIL (<open est signs> open est. signs, >= 2,000 needed)" and, if PASS, the
  cheapest first test you would name (one sentence: data, key/table, statistic, matched control, est. cost).
- Do not touch QUEUE.md, POOLS.tsv, status.json, NEAR.md -- the lane orchestrator does.

Targets (your prompt names one):

1. **fr16106-vivonne-longlee-1579** (create) -- BnF fr.16106 FROM f.207 (btv1b90096628), fr.16107 (btv1b9009661v), fr.16108
   (btv1b9009660f), fr.16109 (btv1b9060954m), fr.16110 (btv1b90609536): Jean de Vivonne, sr de Saint-Gouard, 1579-82, then Pierre
   de Segusson, sr de Longlée, 1582-88, ambassadors in Spain, to Henry III (scout row 7). HIGH edition risk: Albert Mousset,
   *Dépêches diplomatiques de M. de Longlée, résident de France en Espagne (1582-1590)*, Paris 1912 -- find it on IA/HathiTrust/
   Gallica, whole-volume grep, and match every Longlée cipher letter to a printed number (printed in clear = found-solved for
   that letter; Mousset's intro pp.lviii-lix prints his reconstruction of the Longlée table -- record it, it is a published key).
   Vivonne 1579-82: any print (Lettres de Catherine de Médicis vols 7-8; Gachard; "Saint-Gouard" dépêches édition). Tomokiyo
   `sources/cryptiana/web/henryiii.htm` on disk: grep it for Vivonne/Saint-Gouard/Longlée. In-volume clerk decipherments
   ("dechiffré") seen on any sampled leaf count as period decipherments. **Off limits:** `ciphers/fr16104-vivonne-spain-1572`
   (LANE-NEAR4 claim < 6 h; also fr.16106 up to f.198 belongs to it) -- read its NOTES.md for routes, never write to it.
2. **throckmorton-add4136-1559** (create) -- BL Add MS 4136 ff.100-155, Nicholas Throckmorton (ambassador in Paris, then
   Edinburgh) to Elizabeth I / Cecil / the Council, 1559-63; DECODE R9220-R9255 (+R3026); key records R9260-R9262 (ff.177-190,
   "Sr Nicholas Throckmorton's Third Cipher") (scout row 9). **Prior finding to test first:** QUEUE.md line ~1498 marked this pool
   found-solved on 20 Sept 2026 from Patrick Forbes, *A Full View of the Public Transactions in the Reign of Q. Elizabeth*
   (2 vols, 1740-41), "prints Throckmorton's despatches in full from deciphered MSS"; the per-item match was never done. Do it:
   find Forbes on IA/Google Books, and for each DECODE record (date + addressee from the login-free listing,
   `tools/decode_list.py` or `sources/decode/*.tsv` on disk -- no login needed for this job) find the Forbes page or say none;
   then CSP Foreign Elizabeth vols 1-6 (IA full text) for the remaining dates and whether they say "deciphered" or "in cipher,
   not deciphered". Also Bourdeau `targets/throckmorton/` (clone github.com/dbourdeau/cyphersolver shallow, grep only): what he
   read, with which key, and his stated next step (stated-next-step rule). QUEUE.md rows 7/20/31 and `ciphers/moray-wood-1568`
   touch the same manuscript -- read, do not merge.
3. **fr16045-pisany-rome-1585** (create) -- BnF fr.16045 (btv1b9060906j), fr.16046 (btv1b90609054): Jean de Vivonne, marquis de
   Pisany, ambassador in Rome, to Henry III, 1585-88 (scout row 10). Tomokiyo henryiii.htm lists 9 (1585) + 5 (1586-87) letters
   and quotes a 17 Sept 1586 specimen; Anticona's thesis (2012-13) prints one marginal transcription -- locate it (theses.fr/HAL/
   Sorbonne) and say which letter. Check Lettres de Catherine de Médicis vols 8-9, and any edition of Pisany's Rome dispatches.
   Count leaves carrying a marginal/interlinear period decipherment (premise (c)) from Tomokiyo + sampled canvases.
   `ciphers/fr3983-pisany-nevers-1593` is a different letter (Pisany to Nevers 1593, found-solved) -- read, do not merge.
   **Gallica timing:** worker 1 also uses Gallica; this worker is started only after worker 1 stops (good-citizen rule).
4. **costabili-modena-1491** (create) -- State Archives of Modena, Amb. Ung. b.2/20 (DECODE R1162-R1167), b.2/22 (R1095-R1097):
   Beltrame Costabili, Ferrarese envoy in Hungary, to Eleonora d'Aragona (1491-92) and Ercole I d'Este (1493) (scout row 11).
   Our two folders `ciphers/decode-1162-modena-ambung-1492` (partial; AUDIT N0, plaintext = period gloss) and
   `ciphers/decode-1168-modena-costabili-1492` (found-solved, Berzeviczy 1914 no. CLV) are read first and not rewritten -- the
   pool folder covers the OTHER eight records. HIGH edition risk: Albert Berzeviczy, *Acta vitam Beatricis reginae Hungariae
   illustrantia* (MHH Diplomataria 39, 1914) already printed R1168 in clear -- grep the whole volume (IA/HathiTrust/REAL-EOD/
   MEK) for every Costabili letter 1491-93 and match each record by date; then Nyáry / the Magyar diplomacziai emlékek
   Mátyás/Ulászló series (Ambassador reports, "Ferrarai követ") for 1491-93. DECODE: login-free listing metadata only (status
   field, documents attached, page counts), from the on-disk `sources/decode/` TSVs first, `tools/decode_list.py` only if a record
   is missing there (<= 10 requests). A2-COS2 (period key by alignment) was parked by the owner on 3 Oct: do not run it.

Good-citizen rule: one request at a time per host, >= 1.5 s apart (Gallica >= 2 s, browser UA); stop a host on 429/403/challenge,
one retry after a pause at most. Google Books calls carry `&country=US&key=$GOOGLE_BOOKS_KEY`; OpenAlex/S2 keys as headers
(CLAUDE.md item 3). Never print credentials. Report request count per host.

Done line (tools/room.py, role "LANE-POOLS2 CS-<n> (account-1 worker)"): `done (<start>-<end> UTC, brief met|box|cap): commit
<sha>. <slug>: <status>; <k> of <n> letters open, est <signs> open signs; pool bar PASS|FAIL; read <edition pp.>; intake gate
<exit>; gaps_check <result>; requests per host ...; cost: see the lane ledger`. Report what was found and where it was not found;
do not classify novelty.
