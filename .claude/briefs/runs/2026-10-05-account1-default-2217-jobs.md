# LANE DEFAULT-account-1-20261005-2217 jobs (account 1) -- 5 Oct 2026 22:4x UTC, lane orchestrator session_019Kz7yPGospqiXe5Jxz6ffm

Lane brief: .claude/briefs/default-lane.md (cap 60, box 22:43 UTC 5 Oct - 08:43 UTC 6 Oct). Backlog per the WORK-QUEUE row: VERIFY-BACKLOG.tsv
(regenerated 21:43 UTC) then plain `tools/next_steps.py` runnable rows (not --hot-only), folders a-l only (account 2 takes m-z). Off limits:
Birago, Armstrong, Debosnys. Every worker: Opus 5.5, one job, then stop. Each solver job first checks that its named step is still undone
(NEXT-STEPS.tsv lags the folders): if a dated NOTES.md section already ran it, take the folder's own Verdict "cheapest next" instead, if it
fits this job's cap and box and is not deep work on another folder; otherwise stop and report.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim
  line with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-1-20261005-2217".
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
  DEFAULT-account-1-20261005-2217", then a five-line final report.

## Verifier jobs (rules for D2-NOXA2)
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

### D2-NOXA2 -- fr16142-noailles-constantinople-1571, Audit 2 of c262 (25 Apr 1572) and c510-516 (7 Jul 1574) (cap 5, box 60 min; 2 items x ~2 + 1)
VERIFY-BACKLOG.tsv rows 1-2 (high) and 5-6: status.json results[120] and [121], PROGRESS.tsv rows 51 and 52. Audit 1 = AUDIT.md "## AUDIT 1
(VER1-NOX, 5 Oct 2026)" (both N0 D0; text known: c262 in Charriere III p.258, c510-516 in Dupuy 521 + Charriere III). Later revisions to carry:
AUDIT.md "## Revision after AUDIT" and NOTES.md DEF1-NOXG (gloss.tsv corrected at L01-L08, RUN6-NOXREAD 0.309 -> 0.3506) and DEF1-NOXB (a
non-test). Expected N0; the job is to try to break that (is there a prior *decipherment* of these very leaves -- Charriere's own note, Tomokiyo's
pages, Lasry/DECODE records -- as distinct from the plaintext in print) and to set the count (rule 4a depth via tools/depth_check.py). Also
check: Charriere vols. II-III notes, Testa Recueil des traites, Hammer, Dupuy 521 catalogue, the BnF fr.16142 catalogue record. PROGRESS.tsv
column `2` = x for rows 51-52; `C` as the depth tool decides. Do not touch gloss.tsv or the reading.

## Solver jobs (solver template .claude/briefs/solver.md; intake gate output pasted below; report what was found and where it was not
## found; do not classify novelty; rule 4 grades; rule 7 --check before push; partial targets keep Remaining gaps / Escalation and
## pass `python3 tools/gaps_check.py <target>`)

### D2-SEURE -- fr3151-seure-1558, score R2 under nom_test (cap 1.5, box 70 min)
Intake gate (22:4x UTC): `fr3151-seure-1558: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Escalation (RUN6-SEURE2): "re-run kp/nom_test.py (same args) with a >= 45 min background timeout to score R2 and write result_run6b.json".
Run it exactly as PREREG-RUN6B.md registers (read kp/nom_run6b.log for the args; no new thresholds), in the background (Bash
run_in_background, timeout >= 50 min). Report R2 beside R1 and the control numbers; update NOTES.md, Remaining gaps / Escalation.

### D2-PAGR7 -- clairambault1225-paget-1714, fresh rule-7 re-derivation of the RUN6-PAGET state (cap 3, box 50 min)
Intake gate (22:4x UTC): `clairambault1225-paget-1714: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Follow the shape of RD7-2026-10-04-near4.md exactly (scratch copy; committed reading.txt / reading_tokens.tsv moved aside; read only
decode.json, key.tsv, exceptions.tsv, ciphertext.tsv, the tool headers and RUN6-PAGET's own command list -- not NOTES.md prose or the
committed reading -- before the diff). RUN6-PAGET made settle7 multi-seed (20 seeds, >= 16/20): run what it ran. Write RD7-2026-10-05-def2.md
with commands, per-file byte comparison and token diff; a difference beyond the M-graded tokens sends the reading back (say so, do not fix
it). Update Remaining gaps / Escalation.

### D2-BAL103 -- baluze103-letellier-marca-1644, DECODE record R2742 (cap 2, box 35 min)
Intake gate (22:4x UTC): `baluze103-letellier-marca-1644: blocked (line 3) -- already terminal, nothing to gate` (an access step).
One browser login: `NODE_PATH=$(npm root -g) node tools/decode_browser_login.js 2742 <scratch dir>` (try `--guess-fullsize` per the CLAUDE.md
DECODE row if images are listed). One login, fetch everything in that session, scrub the account name from any saved page before committing;
never print credentials. Record what R2742 holds (status, documents, images, any plaintext of f.50) in NOTES.md with what was and was not
served. If a plaintext or decipherment is served, do not decode or claim anything beyond recording it and its source (credit DECODE and the
uploader). If the login fails once, stop (one attempt). Status line changes only per rule 5.

### D2-ECK62M -- eckert-1862, --print-free matcher on the 113 '?' entries, then align dated matches (cap 3, box 45 min)
Intake gate (22:4x UTC): `eckert-1862: partial (line 3) -- edition/page or full-text-search citation found within 6 lines`.
Verdict: "--print-free matcher on the 113 '?' entries with both books, ~$1; then align the 25 dated print-free matches, ~$2". Scripts read,
models judge (Usage 2): run the folder's matcher, then align; grade per rule 4; any key-vs-print conflict is a rule-4 data conflict with
witnesses. decode --check before push. Update Remaining gaps / Escalation; gaps_check passes.

### D2-F3198 -- fr3198-labbe-1577, locate the 5 Feb 1577 no.51 leaf in fr.4695 (cap 2, box 45 min)
Intake gate (22:4x UTC): `fr3198-labbe-1577: blocked (line 1) -- already terminal, nothing to gate` (a lookup step).
NOTES.md tail: (1) search Tomokiyo's fr.4695 pages already on disk (sources/cryptiana/, bnf4715.htm and neighbours) for the no.51 key;
(2) the BnF archivesetmanuscrits record for fr.4695 (piece list: is no.51 a piece number, folio range, 5 Feb 1577) to give
`tools/gallica_folio.py btv1b90582923 --anchor canvas=folio` pairs; (3) one native-resolution view of the candidate leaf with
tools/iiif_lines.py (mandatory crop step, paste the command) to confirm date and cipher. Record in NOTES.md; no decoding. If the leaf is
found and in cipher, write the next step (transcription cost) and leave status per rule 5.

# Wave 2 (spawned as wave-1 slots free; same rules)

### D2-NOXB2 -- fr16142-noailles-constantinople-1571, blind read of c262 gloss with a valid control (cap 3, box 35 min) -- D2-NOXA2 done 23:09
Previous lane handoff item 1: one blind read whose control lines are lines commit 4ef591e8c's diff leaves unchanged (L07 plus another glossed
line of the same hand). Must NOT open Charriere, gloss.tsv, reading files, NOTES.md after line 1000, AUDIT.md or commit 4ef591e8c's diff
before finishing the read -- except that the orchestrator states the control lines here: check `git show 4ef591e8c --stat` only for which
gloss lines changed (do not view the diff text) and use the unchanged glossed lines as the control. Pre-register PREREG-D2NOXB2.md (gate:
control word agreement >= 0.80 after PX-BRODEC normalisation). Then compare the target lines with DEF1-NOXG's leaf readings. No gloss edit.

### D2-DAVEX -- baluze167-davaux-1637, exemplar-sheet labeller for f.247 (cap 4, box 50 min)
Verdict: "the exemplar-sheet labeller for f.247, ~$3" (untried: exemplar-sheet labelling from gloss-fixed sign crops; DEF1-DAV's table
labelling failed its control 0/15). Pre-register (control = known-answer crops of the same hand, gate >= 0.80) before the target; one
subagent call per canvas + 1 reconciliation. Rule 3 order.

### D2-ECK64S -- eckert-1864, the Spit/men conflict in Cipher No. 2 (cap 2.5, box 30 min)
Verdict: "re-read mssEC 47 p.22 l.26 and mssEC 48, ~$1". Crop step mandatory; rule-4 data conflict, witnesses named, never by majority.

### D2-BACON -- lambeth-bacon-649, Baconiana Jan 1897 pp.23-29 OCR check (cap 2.5, box 30 min)
Next step: read the page images (IA leaves 26-32, free item) to check the OCR of the printed cipher values, ~$1.

### D2-VIEU -- fr3975-vieuville-1587, print_check on the clear phrases (cap 2, box 30 min)
`tools/print_check.py` with "eschevins et maire de ville", "St Aignen", 30 Sept 1587; search result only (rule 10).

### D2-LINK -- antt-linhares-chave, ink-profile comparison of the 329011 first glyph (cap 4, box 45 min)
Verdict: "a script ink-profile comparison of the 329011 first glyph against every 3 and 8 on m0002, ~$3". Pre-register, script not model.

### D2-1162 -- decode-1162-modena-ambung-1492, native tiles of g/q/sigma (cap 3.5, box 45 min)
Verdict: native tiles of the three g/q/sigma shapes from 1162 p.1 and 1168 f.12r into the sign sorter, then re-key and re-score, ~$3.

Cap note (23:2x UTC): wave-1 workers cost 1.4-3.1 each, with ~1.3 of fixed start-up (CLAUDE.md + brief + --start); wave-2 caps above raised to
cover that. A worker still stops at its cap.

# Wave 3 (written 23:2x UTC from wave-1 results)

### D2-BAL103T -- baluze103-letellier-marca-1644, R2742 TranscriptionsList + check-solved re-verdict (cap 3, box 40 min)
D2-BAL103 (23:07, NOTES.md) found R2742 holds f.50r-51v full-size images and Tomokiyo's key table, Inline Plaintext No, and four
TranscriptionsList entries not opened. One DECODE browser login (same tool and rules as D2-BAL103): open the four transcriptions, record
what each is (ciphertext only, plaintext, who, date), scrub the account name. Then write the check-solved verdict per
.claude/briefs/check-solved.md into NOTES.md (is a decipherment of f.50 published or posted? Tomokiyo's page for the key, DECODE, the two
solver repos, Mazarin/Marca editions per the folder's own log). Status per rule 5 only from that verdict. No decoding in this job; if the
verdict is open, name the next step (transcribe f.50 against the key, with cost).

### D2-ECK62R -- eckert-1862, re-line the ~14 zero-agreement aligned entries under the other book (cap 2.5, box 35 min)
D2-ECK62M (23:13): 57 dated matches aligned, AGREE 316/817 = 0.387 vs control 0.073; about 14 entries 0-agree, book likely wrong. Pre-register
(gate: same control as D2-ECK62M), decode those entries with the other book, report both numbers, grade per rule 4, --check.

### D2-F3198B -- fr3198-labbe-1577, native view of fr.4695 no.55 f.125 (Prague 20 Apr 1577) (cap 2.5, box 35 min)
D2-F3198 (23:06): no.51 = ff.116r-117v, clear, "Je vous envoye presentement la chiffre", no key sheet bound there. Next named: no.55 f.125
(canvas = folio + 9 for rectos per D2-F3198). Mandatory crop step; record what the leaf is (cipher? key? date) in NOTES.md; no decoding.
