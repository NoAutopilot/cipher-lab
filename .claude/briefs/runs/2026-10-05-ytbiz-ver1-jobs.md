# LANE-VER1 jobs (account 2 / ytbiz) -- 5 Oct 2026 18:2x UTC, lane orchestrator session_01PhSoTvEMEhYjg6A5A6tRvA

Lane brief: .claude/briefs/runs/2026-10-05-acct3-lane-ver1.md. Every job below is a VERIFIER job: you are a fresh session, never
the solver of the reading. Use the CLAUDE.md "Verifier brief (template)" (steps 1-5, including 3a depth per rule 4a and step 4
postmortem). Do not decode, do not re-solve, do not touch other folders' readings.

Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, then `python3 tools/room.py --start`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder and box end time (date -u). If --start fails to push from a detached HEAD:
  `git push origin HEAD:main; git checkout -B main HEAD`.
- Audit 2 = the second adversarial audit (CLAUDE.md Outreach gate 2): a separate session from Audit 1's, trying to find the
  plaintext or the decipherment in print and failing. Cover: canonical/series editions, sender- and recipient-specific printed
  correspondence, the holding archive catalogue, IA full text (be-api fts), Google Books API (`&country=US&key=$GOOGLE_BOOKS_KEY`),
  HathiTrust EF where useful, OpenAlex (Bearer header), Semantic Scholar (x-api-key), Persee, HAL, CrossRef, solver repos
  (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers -- grep, cite, never copy Aymeloglu code), cipher blogs. Phrase searches on
  the decoded text. JSTOR: append rows to JSTOR-QUEUE.tsv in both families (i) names+date+cipher keyword and (ii) a bare quoted
  phrase, no cipher keyword; a queued row never blocks the class. `tools/print_check.py ciphers/<t>` is the scripted pass.
- Log every family searched and every one unreachable, with the date. Good-citizen rule: one request per host at a time, >=1.5 s.
- Append your audit to the folder's AUDIT.md as a new section "## AUDIT 2 (<job id>, 5 Oct 2026)" (never rewrite Audit 1's text;
  correct over-claims by a dated correction note). Per item: N-class (rule 10), key source ours/period/published, text known/not,
  depth D0-D4 with % H/C/S tokens and for D2+ one true content sentence (rule 4a), safe sentence, unsafe sentence.
- Then: status.json fields for the result row(s) (audit_status 'two audits' when audit 2 is done; depth, depth_pct,
  depth_sentence, depth_check, decode_status) and run `python3 tools/depth_check.py` (paste output in AUDIT.md);
  PROGRESS.tsv column `2` = x for each leaf row you audited (and `C` per the count rule: C = x only at N3+ and D2+, per
  depth_check), `source` column naming AUDIT.md. Rebase before editing shared files; keep both facts on conflict.
- At N3 or better: append the SECOND-OPINIONS-QUEUE.tsv row in the same session (CLAUDE.md Operating model).
- Run `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the
  owner; never print credentials.
- Stop at the cap or at 80% of the box, whichever first; a stop with the audit half done writes what was searched so far into
  AUDIT.md as "AUDIT 2 (partial)" and names the remaining families.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <class per item, depth, commit>` addressed
  "for LANE-VER1", then a five-line final report. Report what was found and where it was not found.

## VER1-PIS -- fr16045-pisany-rome-1585, three known-answer pages (cap 7, box 75 min)
Pages f.247r (17 Sept 1586), f.275v (4 Nov 1586), f.302v (24 Mar 1587): key86 known-answer PASS 4-5 Oct 2026 against the clear
copies in Colbert 16 pt II (see NOTES.md "Remaining gaps" and the kp86* folders). The text is in Colbert by design, so the expected
class is N0 or N1: this is AUDIT 1 for these three pages (the folder has no AUDIT.md yet). Establish for each page: is the plaintext
in print anywhere (Colbert is a manuscript copy -- also check printed editions of Pisany's Rome dispatches, e.g. any edition of the
Pisany/Vivonne correspondence, Lettres de Henri III, Negociations, the Bulletin/Annuaire-Bulletin SHF), is the period decipherment
on the leaf, key source (period? ours?), depth. Write ciphers/fr16045-pisany-rome-1585/AUDIT.md. PROGRESS.tsv already has rows
"Pisany 17 Sept 1586 f.244v-245r", "Pisany 4 Nov 1586 f.275r", "Pisany 24 Mar 1587 f.301v": add one row per audited page
(f.247r, f.275v, f.302v) using the existing columns, `1` = x, and do not collapse rows (one row per leaf). Expect `C` = '.'.

## VER1-VIV -- fr16104-vivonne-spain-1572, ink 53 / 54 / 63 (cap 9, box 100 min)
Audit 2 for the three Saint-Gouard (Vivonne) letters: ink 53 (5 Sept 1572, to Anjou, fr.16104 ff.170r-171v), ink 54 (7 Sept 1572,
f.173r-v), ink 63 (10 Oct 1573, to Charles IX, fr.16105 ff.190r-194r). Audit 1 in AUDIT.md (VIV54-A1 and later). Also a depth
re-check: they sit at D1 ("fragments read"); state whether the current committed reading supports D2 under rule 4a (one stretch above
the authentication distance and one true specific content sentence), with the evidence; lower or hold, never raise without it.
Key printed sources to rule out: the Saint-Gouard dispatches printed in e.g. Douais, Depeches de M. de Fourquevaux / Lettres de
Charles IX a M. de Fourquevaux, and any edition of Saint-Gouard's correspondence; the Archivo de Simancas K-series calendars.

## VER1-C1161 -- clair1161-avis-flandre-1688 (cap 7, box 80 min)
Audit 2 + count. Audit 1 = A3V2-C1161A1 (4 Oct). The reading is the merged 3,389-sign reading; check NEAR.md row and NOTES.md for
any reading change after Audit 1 (rule 10 propagation) and carry it. Then count per rule 4/4a with depth_check.py. Folder is absent
from status.json results (SYS1-VBL): add a results row following the existing schema of neighbouring rows, and say so in ROOM.

## VER1-PAG -- clairambault1225-paget-1714 (cap 7, box 80 min)
Audit 2 + count. Audit 1 = A3V-VPAG (4 Oct). Check RD7-* files and NOTES.md for any reading revision after Audit 1 (RUN2-PAG etc.)
and carry it. Two status.json results rows reference this folder (results[4] and the PROGRESS row): reconcile them, keep both facts.

## VER1-GRA -- fr2980-gramont: f.18r L11-L21 and fr.3040 no.6 (cap 7, box 80 min)
The N8/N9 pre-registered PASS readings (PREREG-N8-GRA*, PREREG-N9-GRA*, NOTES.md 4-5 Oct). AUDIT.md currently covers f.29r only.
Audit 1 for these two items (N-class, key source, depth); if a prior audit section exists for either, make yours Audit 2. Look
especially for printed editions of Gramont's Rome dispatches 1529-1531 (e.g. Le Grand, Histoire du divorce de Henry VIII, vol. 3
preuves; Pocock, Records of the Reformation; Calendar of State Papers Spanish/Venetian; L&P Henry VIII). Add PROGRESS.tsv rows for
the items you audit if absent (one row per leaf).

## VER1-COS -- costabili-modena-1491 (and decode-1168-modena-costabili-1492 if it is the same reading) (cap 6, box 70 min)
"11 C confirmed" (N9-COSV, 5 Oct; VER-GRACOS 4 Oct key-grade check). Novelty audit (Audit 1 if none in AUDIT.md assigns an N-class,
else Audit 2), depth, PROGRESS.tsv row if absent. Sources: Este ambassadors' dispatches editions (Dispacci degli ambasciatori
estensi, Carteggio degli oratori), Archivio di Stato di Modena inventories, DECODE record pages (login-free listing only).

# Wave 2 (written 18:2x UTC; spawned only as wave-1 spend allows)

## VER1-NOX -- fr16142-noailles-constantinople-1571, the basin reading (cap 5, box 60 min)
No AUDIT.md yet. Readings: N8-NOX basin, N8-NOX2 key tie, RUN6-NOXREAD reader-sign decode (PASS, thin) -- NOTES.md "Remaining
gaps". Audit 1: N-class for what is actually read (Charriere, Negociations dans le Levant III, prints much of this correspondence --
NOTES.md top -- so check whether the c262 plaintext is in Charriere), key source, depth (expect D0/D1 unless a clause above the AD
reads). Write AUDIT.md; status.json row if absent; PROGRESS.tsv row (one per letter/leaf actually read).

## VER1-REG -- register fixes + Janssens audit 2 (cap 5, box 60 min)
(a) na-schonenberg-1678-1716: AUDIT.md (2 Oct) classes the leaf N0, but PROGRESS.tsv col `1` = '.': set it from AUDIT.md,
source = AUDIT.md; depth_check fields in status.json if missing. (b) na-janssens-java-1811: Audit 2 on Audit 1 (A3V-VJAN, N1).
(c) fr3993-gonzague-nevers-1595: Audit 2 on A3V-VNV01. Each a separate AUDIT 2 section; stop at cap with what is done.

## VER1-SYNC -- register reconciliation, no new searching (cap 3, box 40 min)
VERIFY-BACKLOG.tsv note "REGISTERS DISAGREE" rows: bowes-walsingham-1583 (results[17]), thurloe-printed (results[43], [50]),
rah-morillo-1817 (results[99]): PROGRESS.tsv says Audit 2 done, status.json does not. For each, read the folder's AUDIT.md: if it
holds a second audit by a separate session, set status.json audit_status 'two audits' (and depth fields via depth_check.py if
missing), citing the AUDIT.md section; if it does not, set PROGRESS.tsv `2` back to '.' with source AUDIT.md. Do not audit anew.
Then re-run `python3 tools/verify_backlog.py` (regenerates VERIFY-BACKLOG.tsv) and push both registers + the backlog.
