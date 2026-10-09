# LANE DEFAULT-account-4-20261009-1340 -- jobs (written 9 Oct 2026, ~13:5x UTC by date -u)

Lane orchestrator: session_01ALo565sPeiKLJT5UrYLMkv (account 4, `CIPHERLAB_ACCOUNT=account-4`). Standing brief
`.claude/briefs/default-lane.md`; common rules `.claude/briefs/lane-common-blast.md` and `.claude/briefs/README.md` common tail.
Selection: VERIFY-BACKLOG.tsv actionable rows are Birago (off limits) and Manteuffel 0436 (account-2 FAMILY-A2i live). Jobs are from
`tools/next_steps.py --hot-only` runnable rows, each folder's latest Escalation/Verdict read before briefing (lesson 1 of the 1051 lane),
skipping ROOM claims < 6 h, live lane briefs (account-2 FAMILY-A2i: Manteuffel, Brochado, Heinsius, es132; account-1 LEDGER: eckert-1864;
account-1 SIG-6) and anything needing Gallica (probed once 13:47 UTC: 403). The 1051 lane's jobs are not repeated; these are its named next steps.

## Common to every job (read before the first action)

1. `git fetch origin && git checkout -B main origin/main`; `export CIPHERLAB_ACCOUNT=account-4`; `python3 tools/room.py --start`;
   `date -u`. Read CLAUDE.md, the target's NOTES.md (status lines, Remaining gaps, Escalation, While waiting) and the last 30 ROOM lines.
2. ROOM claim with `tools/room.py` (role "<JOB> worker (account 4, <model>)", box end time), "for LANE DEFAULT-account-4-20261009-1340".
   A halfway line at 50% of the box; a `done` line at the end. Cost in ROOM lines is "the orchestrator's get_session reading", never your own.
3. Prior-work step: `.claude/briefs/prior-work-step.md` by reference -- run `tools/prior_work.py <slug> --item <id> --step-type <type> --fetch`
   and paste the output into your NOTES section before the first priced step; obey its exit code.
4. Hosts: one request at a time, >= 1.5 s apart (stricter where CLAUDE.md's host table says so); post "<host> take" / "<host> release"
   ROOM lines and wait for another worker's release on the same host. Gallica: do not call it (403). On 429/403/challenge: stop that host,
   log it, one retry after a pause at most. Report requests per host in the done line.
5. **Images never go into the public repository.** Fetch and crop into your scratchpad (or a git-ignored path); commit TSV/MD/scripts only.
   Images already committed in a folder may be read from disk.
6. Subagents: at most 4 at once; a transcription call gets line crops only (`tools/iiif_lines.py --image <file> --out <scratch dir>`, the
   command pasted in NOTES before the first call), never a full page. Price: about USD 1.5 per Sonnet blind pass, and one more unit for
   your own reconciliation. Stop before starting a unit that would cross 80% of cap or box.
7. Grades per CLAUDE.md rule 4; any accepted nomenclature value goes through `tools/decode_key.py <t> --try` and stays M unless its
   control passed; never a direct key.tsv edit for a guessed value. Rule 3: every gate has its matched control, both numbers reported.
8. A target left `partial`: NOTES.md ends with "## Remaining gaps" and "## Escalation" (Verdict) and `python3 tools/gaps_check.py <t>`
   passes. Do not change the status line beyond rule 5. Run `python3 tools/file_shrink_guard.py <every path you touched>` before your
   final push; push with `tools/room.py --push <paths>` (or stage by explicit path, rebase, push).
9. Report what was found and where it was not found; do not classify novelty. Never the words solved, cracked, novel, first or new for
   anything this project did. Never name the owner. Never print credentials. Never call AskUserQuestion. Stop when the brief is met;
   follow-ups go in NOTES.md as one-line suggestions.
10. Final message: five lines max (what ran, numbers with controls, files/commit, requests per host, what is left).

## Jobs

### J1 F5160-POOL -- fr5160-letellier-1653, Opus, cap USD 4.5, box 90 min
Intake gate: `fr5160-letellier-1653: open (line 3)` passes. Disk only. NOTES "## Remaining gaps (D4-F5160B)" gap 3 / Escalation key-rebuild:
rerun the nomenclator_anneal.py matched control with all four 1653 letters pooled (f.1-2, f.9, c11, c32, ~970 tokens; the earlier
control read 25.7% against a ~60% bar at a smaller N). Control first (`tools/family_run.py` if the family is registered there, else the
folder's own script, same N, K, design and language -- rule 3); run the target only if the control meets its pre-registered bar.
Pre-register the bar in a PREREG file pushed before any score. If the pooled control is still below bar, log it in HYPOTHESES.md as the
second attempt (rule 3 third-attempt clause: one more failure retires the instrument) and name the word-level solver step. ~3 compute units.

### J2 PISA-275R -- fr16045-pisany-rome-1585, Opus, cap USD 3, box 75 min
Intake gate: `fr16045-pisany-rome-1585: partial (line 1)` passes. Disk only. The Verdict's cheapest next: the UNA-PISA tile compare on f.275r's
17 T45/T47/T57 tokens (`una_pisa/windows.py f275r` ready), the same instrument and controls UNA-PISA and UNA2-PISA used on f.301v/f.302v.
Pre-register; any relabel is committed only on a gate PASS with its controls, grades per rule 4. Units: tile build + blind compare
(<= 2 Sonnet calls on tiles only) + your reconciliation.

### J3 SFZ-LOOK -- sforza-pusterla-1447-f13 (NEAR row), Opus, cap USD 3, box 75 min
Intake gate: `sforza-pusterla-1447-f13: partial (line 1)` passes. Disk only. Gap 2: f.13 lookalike pass on the T=/b-, d/g, q/V pairs
(`tools/lookalike_pass.py`, CLAUDE.md Usage 6: its 2-of-3 residual is agreement, not accuracy). What machines still split goes to a
focus.tsv for the owner's sorter (do not publish it; name it in NOTES). Re-run the lattice decode + judge only if labels change; report
both corpora and the shuffled-key null. Do not touch f.81/f.42 labels.

### J4 BLA-TRY -- huntington-blathwayt-madrid-1728, Opus, cap USD 1.5, box 45 min
Intake gate: `huntington-blathwayt-madrid-1728: partial (line 3)` passes. Disk only. The Verdict's cheapest next: `tools/decode_key.py
<t> --try` on the 7 key-tie tokens (BLA184 p1 L02/L03/L04; BLA191 p5 L01 pos 8 665, L04 pos 4 1250, L11 pos 1 46, L12 pos 2 1018; NOTES
line ~696), each candidate at every occurrence, with --try's own control; accepted values stay M unless the control passed. No key.tsv edit
by hand. Report the tie each token resolves to (or not) with the numbers.

### J5 MONLUC-F86 -- fr4735-monluc-lansac-poland-1573, Opus, cap USD 3, box 60 min
Intake gate: `fr4735-monluc-lansac-poland-1573: partial (line 1)` passes. Disk only (crops already in the folder or scratch from
MONLUC-BLIND; if they are not on disk and need Gallica, stop and say so). Gap: f.86 K07 Z vs 2 split -- a blind sort of the f.86 K07
crops alone at one scale with the f.86 K38 exemplars beside them (value-blind, no key values on the sheet), one Sonnet call plus your
reconciliation. Relabel only if the sort splits and a --try with control supports it; otherwise log the non-split.

### J6 BNE-1180 -- bne20211-ferdinand-1478, Sonnet, cap USD 1.5, box 45 min
Intake gate: `bne20211-ferdinand-1478: partial (line 1)` passes. NOTES line ~510: one DECODE browser login
(`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js` per CLAUDE.md DECODE row; one login only, scrub the account name from saved
pages) to fetch R1180 `DocumentsList` and its full-size pages to scratch (images never committed); compare dimensions against
images-123-shots and record what R1180 holds (manifest TSV only). No transcription pass. de-crypt.org take/release lines.
