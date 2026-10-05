# LANE DEFAULT-account-1-20261005-2039 jobs (account 1) -- 5 Oct 2026 20:5x UTC, lane orchestrator session_0129JoekeRPRo9Fsfv9XdQQi

Lane brief: .claude/briefs/default-lane.md (cap 60, box to 6 Oct 06:41 UTC). Backlog: VERIFY-BACKLOG.tsv (regenerated 20:42 UTC)
rows LANE-VER1 left open (its STATUS.md handoff "Open for the next verifier or solver lane"), then `tools/next_steps.py --hot-only`
runnable rows. Every worker: Opus 5.5, one job, then stop.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-1-20261005-2039".
  If --start fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections) and AUDIT.md section list before acting.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge). Report request counts per host.
- Rebase before writing shared files (status.json, PROGRESS.tsv, VERIFY-BACKLOG.tsv, SECOND-OPINIONS-QUEUE.tsv, JSTOR-QUEUE.tsv,
  ROOM.md); keep both facts on conflict. Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push;
  push with `python3 tools/room.py --push <paths>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials (test presence with `test -n`). Never call AskUserQuestion.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half
  done writes what was done and what remains into the folder's files.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE
  DEFAULT-account-1-20261005-2039", then a five-line final report.

## Verifier jobs (rules for DEF1-THUR, DEF1-LVN, DEF1-PIS, DEF1-GRACOS)
You are a fresh session, never the solver of the reading and never the session that wrote Audit 1. CLAUDE.md "Verifier brief
(template)" steps 1-5 including 3a (depth, rule 4a) and 4 (postmortem). Do not decode, do not re-solve.
- Audit 2 = the second adversarial audit (CLAUDE.md Outreach gate 2): try to find the plaintext or the decipherment in print and
  fail. Cover: canonical/series editions, sender- and recipient-specific printed correspondence, the holding archive catalogue, IA
  full text (be-api fts), Google Books API (`&country=US&key=$GOOGLE_BOOKS_KEY`), OpenAlex (Bearer header), Semantic Scholar
  (x-api-key, 1.1 s), Persee, HAL, CrossRef, CORE (Bearer, `v3/search/works/`), solver repos (dbourdeau/cyphersolver,
  aaymeloglu/unsolved-ciphers -- grep, cite, never copy Aymeloglu code), cipher blogs. Phrase searches on the decoded text
  (`tools/print_check.py ciphers/<t>` is the scripted pass). JSTOR: append rows to JSTOR-QUEUE.tsv in both families (i)
  names+date+cipher keyword and (ii) a bare quoted phrase with no cipher keyword; a queued row never blocks the class.
- Log every family searched and every one unreachable, with the date.
- Append "## AUDIT 2 (<job id>, 5 Oct 2026)" (or 6 Oct if the clock says so) to the folder's AUDIT.md; never rewrite earlier audit
  text; correct over-claims with a dated correction note. Per item: N-class, key source ours/period/published, text known/not,
  depth D0-D4 with % H/C/S tokens and for D2+ one true content sentence, safe sentence, unsafe sentence.
- If the reading was revised after Audit 1 (dated NOTES.md sections after the audit), carry the revision into your audit and into
  any SECOND-OPINIONS-QUEUE.tsv row already filed for the target (rule 10 propagation).
- Registers: status.json results row(s) named below (audit_status 'two audits'; depth, depth_pct, depth_sentence, depth_check,
  decode_status per tools/depth_check.py), then `python3 tools/depth_check.py` (paste the line for your rows into AUDIT.md);
  PROGRESS.tsv column `2` = x for each leaf row audited (`C` = x only at N3+ and D2+), `source` naming AUDIT.md. Then
  `python3 tools/verify_backlog.py` and commit the regenerated VERIFY-BACKLOG.tsv.
- At N3 or better: append the SECOND-OPINIONS-QUEUE.tsv row in the same session.
- Report what was searched and where the text was and was not found.

### DEF1-THUR -- thurloe-printed, status.json results[43] and results[50] (cap 5, box 60 min; 2 items x ~2 + 1 reconciliation)
Audit 2 for two result rows that carry one audit each: [43] "14 cipher letters whose decipherment Birch printed" (Audit 1 = AUDIT.md
"## P2, P3, P5+P6, P7, P8, P16-P24"), [50] "Blake 4 and 6 July 1655 ... Mountagu 16 Sept 1656" (Audit 1 = "## P9, P10, P14, P15").
Birch 1742 prints these decipherments, so the expected class is N0/N1: the job is to confirm or correct that, check the later
revisions (AUDIT.md "Revision after AUDIT (N8-THUR, N8-THUR2)", "Depth (DEPTH-REGRADE)") are reflected, and set depth. Also check
the calendars (CSP Domestic 1655-56, CSP Venetian) and Firth/Clarke Papers, Corbett/Navy Records Society (Blake, Mountagu) for prior
print of the same letters. No PROGRESS.tsv leaf rows exist for these: add one row per result row only if the register's own schema
for multi-letter results allows it (read tools/progress_block.py); otherwise say so.

### DEF1-LVN -- lodewijk-van-nassau-1573-74, status.json results[64] (cap 5, box 60 min)
Audit 2 for "William of Orange to Louis of Nassau, 1574 (WVO 5811, 5810, 4503): partial readings under the letter table" (Audit 1 =
AUDIT.md "## WV2 letters (V7): WVO 5811 and 4503"). Later revisions are in AUDIT.md "Revision log" (26 Sept), "Revision log v3",
"VERIFY-LVN-173" (2 Oct) and "Depth (DEPTH-REGRADE)": check which touch 5811/5810/4503 and carry them. Printed sources to rule out
beyond what Audit 1 logged: Groen van Prinsterer, Archives ou correspondance ... de la maison d'Orange-Nassau ser. 1 vol. IV-V
(1574); Gachard, Correspondance de Guillaume le Taciturne vol. III; Japikse; the Huygens WVO detail pages for 5811, 5810, 4503
(`wvo/app/brief?nr=<n>`, >= 2 s apart). Note: 5810 is named in the result title but not in Audit 1's heading -- establish whether
it was ever audited and say so.

### DEF1-PIS -- fr16045-pisany-rome-1585, f.247r / f.275v / f.302v (cap 6, box 70 min; 3 pages x ~1.7 + 1)
Audit 2 for the three pages VER1-PIS audited as Audit 1 (N0 D1 each, key published Tomokiyo, text known; AUDIT.md "AUDIT 1"). Audit 1
found Aubery 1654 prints f.275v and one f.247r sentence, and f.302v (24 Mar 1587) "not located in print". The open question that
matters: is f.302v's plaintext printed anywhere (Aubery 1654 Memoires pour l'histoire du cardinal de Joyeuse / Mémoires de
Pisany? Lettres de Henri III, ed. Société de l'histoire de France; Négociations diplomatiques avec la Toscane (Desjardins) vol. IV;
L'Épinois; Hübner, Sixte-Quint vol. III pièces justificatives; Bulletin/Annuaire-Bulletin SHF). Does the f.302v text sit in the
Colbert 16 pt II clear copy only (manuscript; N0 by the period copy regardless)? State per page whether N0 holds and on which
witness. PROGRESS.tsv rows 42-44.

### DEF1-GRACOS -- fr2980-gramont fr.3040 no.6 and costabili-modena-1491 R1166 (cap 5, box 60 min; 2 items x ~2 + 1)
Audit 2 for: (a) Gramont to Montmorency, Boulogne [Bologna] 28 March 1530 (BnF fr.3040 no.6, ff.18-19), status.json results[114],
PROGRESS.tsv rows 47-49 (f.18r, f.18v, f.19r); Audit 1 (VER1-GRA) N0 via the period marginal decipherment on f.18r + Le Grand,
Histoire du divorce III pp.454-457. (b) Costabili to Eleonora d'Aragona, Esztergom 21 June 1491 (ASMo Amb. Ung. b.2/20 no.16),
status.json results[115], PROGRESS.tsv row 50; Audit 1 (VER1-COS) N0 D0, key period, text known on the leaf. For (a) check Pocock,
L&P Henry VIII vol. IV pt 3, CSP Spanish IV, Ehses (Römische Dokumente). For (b) check Berzeviczy (Monumenta Hungariae Historica,
Acta extera: Aragoniai Beatrix magyar királyné életére vonatkozó okiratok, 1914), Nyáry, the Dispacci estensi editions. Expected:
N0 holds; the job is to try to break it and to log the families. Do not touch fr16142-noailles (a solver job runs there now).

## Solver jobs (solver template .claude/briefs/solver.md; intake gate output pasted below; report what was found and where it was not
## found; do not classify novelty; rule 4 grades; rule 7 --check before push; partial targets keep Remaining gaps / Escalation and
## pass `python3 tools/gaps_check.py <target>`)

### DEF1-NOXG -- fr16142-noailles-constantinople-1571, c262 gloss vs Charriere III p.258 (cap 4, box 50 min)
Intake gate (20:5x UTC): `fr16142-noailles-constantinople-1571: partial (line 1) -- edition/page or full-text-search citation found
within 6 lines`.
VER1-NOX (NOTES.md "Correction note (VER1-NOX verifier, 5 Oct 2026)") found gloss.tsv differs from Charrière III p.258 at L01
"bruslent"/"veullent", L04 "le bestial"/"l'antienne liberté", L06 "la faim se trouva"/"la farce se jouera", L08 "sendormir de
ca"/"s'endorme de deçà". Job: (1) get Charrière III p.258 page text (IA full text; record identifier + page), (2) cut native crops of
the c262 interlinear gloss at those four spots (fr.16142 ark btv1b9060927q canvas per NOTES.md; `tools/iiif_lines.py` with
`--region`; crops < 2500 px; this is the mandatory crop step -- paste the command), (3) one blind read of each crop by you (no
subagent needed; 4 crops), recording what the leaf says, (4) normalise both texts (CLAUDE.md rule 3, PX-BRODEC lesson: one case,
expand abbreviations, one spelling convention) and record per word: leaf reads X, print reads Y, gloss.tsv had Z, (5) correct
gloss.tsv only where the leaf supports it (never from the print alone; a print-only correction is grade C at most and marked so),
(6) if gloss.tsv changes, re-run RUN6-NOXREAD's pre-registered gate exactly as registered (no new thresholds) and report both
numbers beside the old ones; if the instrument's script needs more than a re-run, stop and name it. Write a dated NOTES.md section and
update Remaining gaps / Escalation. Do not touch AUDIT.md beyond a one-line pointer under a "Revision after AUDIT" heading (rule 10
propagation) if gloss.tsv changes.

### DEF1-ECK62I -- eckert-1862, image check of the six collision/conflict mssEC 18 entries (cap 5, box 60 min; 6 entries x ~0.7 + 1)
Intake gate (20:5x UTC): `eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
NOTES.md Remaining gaps: "the 26 print-matched mssEC 18 entries were not [image-reconciled]; first the 3 unguarded collisions
(white, animals, Hotel) and the Lehigh (9947.505 "general Canby", 10020.609 "can be") and weigh (9965.539 "on the way")
conflicts; next: image-reconcile with the eckert-1864 method, ~$4". Job: find those six entries' page images (Huntington mssEC 18;
check images/manifest.json and NOTES.md for the route used for mssEC 15 -- Huntington CONTENTdm, CLAUDE.md host notes, CISOSEARCHALL
form), fetch only the pages needed, crop each entry (mandatory crop step, paste the command), read each code word from the crop
blind to the decode first, then compare with the text-derived ciphertext and decide each collision/conflict from the image. Grade
per rule 4; update decode/ec18 inputs only where the image disagrees with the transcription, re-run `decode.py`/ec18 with its
check, record per entry: transcription, image read, decision, grade. If the images are not reachable from the cloud, stop, log the
route tried and add the LOCAL-QUEUE.tsv/ASKS row per the Access playbook (after `python3 tools/key_livecheck.py` if a key is
involved). Update Remaining gaps / Escalation; gaps_check passes.
