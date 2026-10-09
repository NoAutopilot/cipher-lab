# LANE-VERIFY-4 job briefs (account 3, session_01667XGk7THE9debemXAefTi), 8 Oct 2026 from 23:4x UTC (date -u)
Lane brief: .claude/briefs/lane-verify.md (+ lane-common-blast.md). Continues LANE VERIFY-3's handoff in STATUS.md.
**Common tail for every job: the "Common tail" of .claude/briefs/runs/2026-10-08-acct3-verify1-jobs.md (lines 3-17) verbatim, with the
changes at the top of .claude/briefs/runs/2026-10-08-acct3-verify2-jobs.md and .claude/briefs/runs/2026-10-08-acct3-verify3-jobs.md**
(prior_work.py --step-type second-audit --fetch first, then --reading <file> --network for G3; G3 covers the holder's transcription,
recipient-side and staff papers, same-day orders, the sender's same-week letters to other recipients and the press of the day). Also:
- Account 3 never read or first-audited any item below (readers/first auditors: accounts 1, 2, 4; account 3's V1-LS4B was E96's SECOND
  audit, so AUD3-E96 must run in a fresh session that has not seen V1-LS4B's reasoning beyond the file). If you find otherwise, stop and
  say so in ROOM.
- Rebase immediately before every write to a shared file (AUDIT.md, status.json, SECOND-OPINIONS-QUEUE.tsv, research/SIGNIFICANCE-*.md);
  append your own section, never rewrite another's; keep both facts on a conflict. Do not touch decode.py or keys.
- Hosts: Huntington CONTENTdm take/release lines in ROOM; IA one request at a time >= 1.5 s; Gallica answered 403 all day -- one probe at
  most, no retry. Google Books with &country=US and the key.
- Class may stay, rise or fall; depth keep-or-lower only (.claude/briefs/runs/2026-10-08-acct3-depth-bar.md). Carry any change into
  status.json (class, audit_status) and any SECOND-OPINIONS-QUEUE.tsv row (rule 10 propagation).
- Done line "for LANE-VERIFY-4 / acct3-orchestrator", with cost not guessed (the lane reads get_session). Stop at 80% of cap or box
  before starting a new item. Never print credentials; never AskUserQuestion; rule 10 and 4a wording only.

## AUD3-E96 (account 3), cap $3, box 45 min: eckert-1864 E96 -- the Horan check
research/SIGNIFICANCE-2026-10-08.md (significance reviewer, wf_380c48d5-955) says Colonel William Hamilton, named in E96, is already a
rebel agent in James D. Horan, *Confederate Agent: A Discovery in History* (1954), so E96 should fall N3 -> N2. Verify that claim in print
(IA full text / be-api fts on Horan 1954 and its reprints, Google Books snippet): quote the passage and page if found, and judge whether
what Horan prints is the SUBSTANCE of E96 (N2 means the plaintext's content is known elsewhere) or only the man's name (then N3 may stand,
with a caveat line). Read E96's own AUDIT sections (FV-LS4-R1b, V1-LS4B) first; do not repeat their search families. AUDIT.md heading
"## AUDIT 3 (AUD3-E96)". One item, ~$2 + reconciliation.

## AUD-SIG-CHAV (account 3), cap $5, box 75 min: the section "## AUD-SIG-CHAV" of .claude/briefs/runs/2026-10-08-acct1-sig1-jobs.md verbatim
baluze167-davaux-1637, Baluze 170 f.229, Chavigny to d'Avaux 25 Aug 1640 (N3 D2 after AUD1-B167 acct 2 + AUD2-B167 acct 1; reader
D4-B167 acct 4). Families owed: AAE Correspondance politique 1640 inventories/printed selections; the Hessian side (Rommel VIII,
Melander/Eberstein literature, Amalie Elisabeth editions). Note: SIG-B228/B228B (account 1) re-read the neighbouring f.228 this
evening -- f.228 is NOT this audit's item; read its NOTES only as context. AUDIT.md heading "## AUDIT 3 (AUD-SIG-CHAV)"; one line in
research/SIGNIFICANCE-2026-10-08.md "## Lane SIG additions" as the SIG-1 brief says. Units: 2 source families x ~$1.5 + reconciliation.

## AUD-SIG-E146 (account 3), cap $3, box 60 min: the section "## AUD-SIG-E146" of .claude/briefs/runs/2026-10-08-acct1-sig1-jobs.md verbatim
eckert-1864 E146, QMG office to Allen, Louisville 12 Dec 1864, Donaldson's L&N take-over proposal (N3 weak after FV-LS5-B acct 1 +
AUD2-LEDGER-2 acct 3 -- a different session; account 3 did not read or first-audit it). Owed: L&N histories (Herr 1943, Klein 1972,
Lee 2011), McCallum 1866 report, QMG annual report 1865 / OR ser. III vol. 5 (Donaldson's report). AUDIT.md heading
"## AUDIT 3 (AUD-SIG-E146)"; one line in "## Lane SIG additions". Runs in parallel with AUD3-E96 on the same AUDIT.md: rebase before writing.

## AUD2-MANTR8 (account 3), cap $5, box 75 min: sachsstaatsarchiv-manteuffel-1712 Loc. 694/08 frames 0214 (Jul 1712, N3 low D1) and
## 0375 (Sept 1712, N2 D1) -- VERIFY-BACKLOG high audit2 rows
First audit "## AUDIT (V-MANTR8)" (account 2, 23:03-23:14 UTC 8 Oct); reader MANT-R8 (account 2). V-MANTR8 already searched Acta
Borussica BO I, Droysen IV.1, Heinsius XIII-XIV: do not repeat; extend. For 0214 ("on n'attend que ma guérison pour achever l'ouvrage"):
Manteuffel's illness in summer 1712 in Saxon/Prussian scholarship (Haake on Manteuffel/Flemming, Ziekursch, Flemming biographies,
Sbornik RIO), and the press of Jul 1712; test whether N3 low should hold or fall. For 0375: test V-MANTR8's N2 basis (Arnold to
Stanislas, Eosander to Charles XII, Droysen IV.1 Anm. 511-512) -- could the Manteuffel report itself be quoted anywhere (N1)? Also check
V-MANTR8's reading "St[anislas]" for 51.28 against the key table (no image crops on disk; say so if you cannot eye-check). Update
status.json audit_status for both rows and PROGRESS.tsv per the backlog's action; the backlog flags REGISTERS DISAGREE for this folder:
correct the register that is wrong, say which. AUDIT.md heading "## AUDIT 2 (AUD2-MANTR8)". Units 2 x $1.8 + reconciliation.

## AUD3-E97 (account 3), cap $2.5, box 40 min: eckert-1864 E97 -- the Horan check, carried from AUD3-E96 (added 23:5x UTC)
AUD3-E96 found Horan, *Confederate Agent* (1954) p.226 (IA dli.ernet.157117, leaf 267) prints Holt's 23 Nov 1864 summary of the Francis
Jones confession, which lists Baltimore agents (E96 -> N2), and p.227 names St Louis agents. E97 (St Louis, same affair; first audit
FV-LS4-R1b acct 2, second V1-LS4B acct 3 in another session) needs the same test: read AUD3-E96's section first, read Horan pp.226-228
for E97's people and substance, and judge N2 (substance in print) vs N3 (name only, or nothing). Also check E100 against the same pages
if it belongs to the same confession affair (V1-LS4B audited E96 E97 E100 together). AUDIT.md heading "## AUDIT 3 (AUD3-E97)"; propagate
class to status.json and any SO row. Units 1-2 items x ~$1 + reconciliation.

## AUD2-SIG-228 (account 3), cap $5, box 60 min: baluze167-davaux-1637 Baluze 170 f.228r-v (added 00:1x UTC 9 Oct)
The WORK-QUEUE row's note is the brief: first audit "## AUDIT 1 f.228 (SIG-V228)" (account 1; readers SIG-B228/SIG-B228B account 1):
N3 D2 (36%). Check the verifier-corrected grades (15 sig_marks regrades -> I) by re-running decode_key.py --check and comparing counts;
the B228B changes (4 u4/4u signs -> a) landed after or before SIG-V228? -- say which reading was audited and carry any difference. Google
Books phrase search (it answered 429 to every account-3 worker 8 Oct 23:4x-23:5x: one probe, and if still 429 log it, no retry loop).
Do NOT repeat the f.229 families AUD-SIG-CHAV just covered (its "## AUDIT 3 (AUD-SIG-CHAV)": Rommel VIII, Eberstein 1865, Bougeant II,
Siri VIII, Mercure XXIII-XXIV, Caillet 1912) except to search them for f.228's own phrases (la langrave, etc.). AUDIT.md heading
"## AUDIT 2 f.228 (AUD2-SIG-228)". Units: 1 item x ~$3 + reconciliation.

## AUD2-LEDGER-8 (account 3), cap $5, box 100 min: eckert-1864 E193, E194 (added 00:1x UTC 9 Oct)
The WORK-QUEUE row's note is the brief (first audit FV-FM4, account 1; reader FM-R2b account 1, Fort Monroe ledger mssEC 25). Cap 2.5 per
entry; Huntington hdl take/release lines (LANE LEDGER account 1 works the same host: at most one holder at a time). Google Books: one
probe, no loop on 429. AUDIT.md heading "## AUDIT 2 (AUD2-LEDGER-8)".
