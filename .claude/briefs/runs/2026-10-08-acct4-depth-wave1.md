# LANE DEPTH (account 4, DEFAULT-account-4-20261008-1748) wave 1 -- three jobs (written 18:4x UTC 8 Oct 2026 by date -u)

Common tail for every job below: read CLAUDE.md, `.claude/briefs/lane-common-blast.md`, `.claude/briefs/prior-work-step.md`
(run `tools/prior_work.py` for your item and paste its output before the first priced step; LEAD rows naming our own audited
reading are expected -- this lane extends that reading -- answer them with `--record <row> 'KNOWN: our reading, extended here'`),
and the last 30 ROOM.md lines. Claim in ROOM.md with `python3 tools/room.py "<ROLE> (account 4, LANE DEPTH)" '<text>' --push`
(single quotes) before work; halfway line; done line with start-end times read from `date -u`. Disk only: Gallica answered 403 at
18:40 UTC (one probe by the lane); no Gallica request in this wave. Other hosts: good-citizen rule, one request at a time.
Depth rulings follow `.claude/briefs/runs/2026-10-08-acct3-depth-bar.md` literally (copy it into a PREREG before computing).
Rule 4 grades, rule 7 `--check`, rule 10 wording (never new/first/solved/unpublished). Stop at 80% of cap or box; the orchestrator
reads cost with get_session. Never AskUserQuestion; never print credentials; never name the owner. Commit by explicit path to
main, `tools/file_shrink_guard.py` on every touched tracked file before the final push (paste output in the done line).
Solver jobs end: "report what was found and where it was not found; do not classify novelty".

## DV-MERCY -- depth verifier (Opus), cap $5, box 75 min
VERIFIER (depth re-rule, step type `upgrade-audit`): ciphers/espagnol142-mercy-1648, BnF Espagnol 144 f.22r-v (instruction to Mercy).
Status on file (AUDIT.md "## Depth (DEPTH-REGRADE, 4 Oct 2026)"): D2, 92.2% (S 488 of 529); "no external check and no AD computed on
file, so D3 withheld". You are a separate session from every solver of this folder.
1. Re-derive the current reading with the folder's decode script and `--check` (exit 0 expected); recount H/C/S/M/U and nulls.
2. Compute the authentication distance for this design (code+mark / nomenclator as NOTES.md describes it: H(K) = key space of the
   38-value design plus every liberty the reading takes -- M tokens, U, repairs; R from the fr17/es corpus as NOTES.md's judge uses),
   per the depth bar; find the longest contiguous H/C/S stretch in letters and say whether it exceeds AD. Matched control is on file
   (anneal beats it by 167-181); confirm it is the design-matched control rule 3 asks for, or say why not.
3. Classify the residue (the ~41 non-S tokens): names/codes vs ordinary text, token by token, from the reading and the code table.
4. External check: look for one non-statistical check of the content (a period summary, the recipient's reply, a printed account of
   Mercy's 1648 Brandenburg mission) -- AUDIT.md's print searches are the starting point; log every source tried. None found is fine.
5. Rule D2/D3 (D4 only if every 4a element is met) per item; write "## Depth re-rule (DV-MERCY, 8 Oct 2026)" in AUDIT.md and
   update status.json's depth fields for that results row (depth, depth_pct, depth_check, depth_sentence, depth_by, depth_date,
   decode_status) -- fetch/rebase immediately before editing status.json, edit only that row. Run `tools/depth_check.py` after.
   Do not decode beyond the re-derivation; N-class untouched. Report the ruling with its numbers and a one-line postmortem.

## D3-BLA -- residue re-grade (Opus), cap $5, box 75 min
Target ciphers/huntington-blathwayt-madrid-1728, depth item BLA 184 + 186 + 191(a) (D2, 75.0% C 129/172 at DEPTH-REGRADE; NOTES
now says C 130, M 21, U 21). Intake gate: `python3 tools/intake_gate_check.py huntington-blathwayt-madrid-1728` pasted first.
Goal: the SIBLINGS rows "re-grade BLA187/191(a) residue with key.tsv --check + shuffled control" (~$2) and "resolve BLA 190 p7
anomaly then re-grade" (~$1), applied to the 42 M/U tokens of the three depth items only.
1. Decode with the folder's decode.json `--check`; list the 42 M/U tokens with their codes, contexts and why each is M/U.
2. For each, test whether key.tsv (now 388 rows), the deciphered siblings BLA 188/189/190/194/179/185 (period glosses on file, C)
   or a settled image re-read (images and crops already on disk only; crop command pasted; one blind pass + your reconciliation,
   priced as 2 units) gives a value; a value counts as C only when a period gloss gives it; a context-only value is M.
   Shuffled-code control: the same promotion rule applied to the 42 positions with codes permuted must promote clearly fewer
   (report both counts). Pre-register the rule in PREREG-D3BLA.md and push it before scoring.
3. Re-decode, `--check`, recount per item and pooled; classify what is left as names/codes vs ordinary text.
4. NOTES.md section + updated Remaining gaps/Escalation (`tools/gaps_check.py`). Do not touch AUDIT.md depth lines (the verifier does).

## D3-5551 -- WVO 5551 residue under key_full (Opus), cap $4, box 60 min
Target ciphers/jan-van-nassau-1572-75, WVO 5551 p3 cipher lines (reading_5551.txt: 32 tokens, C 23, M 1, I 2, U 6; D2 71.9%).
Fact found by the lane (check it): decode_5551.json uses ../lodewijk-van-nassau-1573-74/key.tsv; that folder's key_full.tsv
(AX-NAMES2 re-gate) grades 126, 127 and 137 NULL at C (empty in 8/8, 31/31, 8/8 aligned observations); 140, 145, 146 are in neither.
1. Intake gate pasted. Run the current decode `--check`. Add a second job (or decode.json variant) with key_full.tsv; regenerate,
   `--check`, recount (nulls out of the denominator as decode_key.py does).
2. The three `?` tokens (L1 after WILL x2, L2 after [140] and at line end): re-read from the image crops already on disk
   (`images/`, the TX-WV5551D crops; crop command pasted if you cut new ones from a local page file); two blind Sonnet passes on
   crops only + your reconciliation (3 units, ~$0.8 each). A read sign that maps to a key_full value is C; otherwise U.
3. Codes 140, 145, 146: check key_5801/key_7206/key_4614 and names.tsv in the Lodewijk folder for any C/H value with direction and
   date matching Jan to Willem, Apr 1574 (rule 4's conflict paragraph); an M value stays M.
4. Recount; classify the residue (name codes vs letters). Notes section + Remaining gaps/Escalation. Do not touch AUDIT.md depth lines.
