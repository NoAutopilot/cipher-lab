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

## Wave 2 (added ~13:5x UTC by date -u; spawned as wave-1 slots free)

### J7 SALAZ-HTRC -- rah-salazar-soria-sanchez-1524-28, Sonnet, cap USD 1, box 30 min
HTRC EF API answered 200 at 13:47 UTC. Rerun NOTES line ~503's exact command (`python3 tools/htrc_ef_headwords.py osu.32435013919725 --words
cifra,cifras,salazar,sanchez,sánchez,soria,mirandola,descifrar,descifrado,cifrada,cifrado --target '' --json`), once; on error one retry after
60 s, then stop. Record the page locations of the Soria catalogue entries in NOTES (TSV beside it). data.htrc.illinois.edu take/release.

### J8 COS-SPAN -- costabili-modena-1491, Opus, cap USD 3.5, box 75 min
Intake gate before briefing: run `python3 tools/intake_gate_check.py costabili-modena-1491` and paste it; stop on nonzero. The Verdict's cheapest
next: short-span boxes on the R1163/R1165 slips cut at each clear word and at line ends (pairs of one to three groups; NOTES lines ~281-284, 322),
then the anchor-span scoring with the same matched control as N9-COS2. Images from disk or DECODE per the CLAUDE.md DECODE row (one login),
to scratch only. Units: crop + 2 Sonnet reader calls + your reconciliation.

### J9 COS-ASMO -- costabili-modena-1491 / decode-1162-modena-ambung-1492 key lead, Sonnet, cap USD 1.5, box 45 min
Catalogue search only (no solving). Lead: Archivio di Stato di Modena, Cancelleria, Cifrario 'Cifre con Ambasciatori e Agenti estensi all'estero,
sec. XV' (B.4), cited in Lang 2018 p.156 (STATUS.md line ~5034; costabili NOTES line 3). Establish: (a) the full Lang 2018 citation and whether
an open copy exists (OpenAlex, Semantic Scholar, CORE, Google Books with country=US, IA be-api); (b) whether ASMo B.4 is digitised anywhere
(ASMo site, Archivi di Stato portals, DECODE records by holding "Modena" and date 1480-1500 via tools/decode_list.py); (c) whether any DECODE
record already holds a Costabili/Este 1490s key. Write a "## Key lead ASMo B.4 (COS-ASMO)" section in costabili-modena-1491/NOTES.md with every
host searched and the result; if an owner-side request is needed, name it in one line (do not file ASKS). Good-citizen rule on every host.

## Wave 3 (added ~14:2x UTC by date -u; the named next steps of wave 1/2). J8 COS-SPAN above is spawned with this wave.
Intake gates re-run 14:2x: costabili-modena-1491 partial (line 1), fr16045-pisany-rome-1585 partial (line 1), fr4735-monluc-lansac-poland-1573
partial (line 1), fr5160-letellier-1653 open (line 3): all pass.

### J10 PISA-T32 -- fr16045-pisany-rome-1585, Opus, cap USD 2, box 45 min
PISA-275R (ba567ff57) settled 4 f.275r T57 tokens as T32 candidates. Run the UNA2-PISA re-score shape on f.275r for those 4 (pre-registered
before any score, same gates G1-G3 and controls as una2_pisa; key86 unchanged). Commit the relabel only on a PASS, keeping pre-edit files
byte-identical as *_preT32; grades per rule 4; carry any reading change into AUDIT.md as a facts-only carry-over (rule 10 propagation). Disk only.

### J11 MONLUC-CURL -- fr4735-monluc-lansac-poland-1573, Opus, cap USD 2.5, box 50 min
MONLUC-F86's named next (bcab4a936): a binary curl-present / curl-absent blind sort of the 17 f.86 K07 tokens on wider crops (from images on
disk; if wider crops need Gallica, stop and say so), value-blind, pre-registered gate, one Sonnet call plus reconciliation. Relabel only on a
gate PASS plus a `decode_key.py --try` with its control; otherwise log. This is the second blind sort of f.86 K07: a fail is logged under rule 3.

### J12 F5160-WORD -- fr5160-letellier-1653, Opus, cap USD 5, box 100 min
The Verdict's cheapest next (F5160-POOL): a word-level (dictionary-constrained) solver for the 1653 syllabic table, a different instrument
from nomenclator_anneal.py. Use a shared tool if one fits (`tools/family_run.py` families, `tools/segmenter.py`, `--param lock=`); a private
script only if none does, and say why in NOTES. Matched control first on control_pool.txt (same N 972, K, design, fr17 language); pre-register
the bar and push it before any score; run the four real letters only if the control meets it. Both numbers in HYPOTHESES.md.

### J13 COS-CREM -- costabili-modena-1491 key lead, Sonnet, cap USD 1.5, box 40 min
COS-ASMO (da488a051) named Cremonini 2017 (RSU 16, pp.117-145, EPA pdf) as the next read. Fetch it once (EPA / epa.oszk.hu; good-citizen rule),
grep it for b.4-7, Ungheria/Hungary, Costabili, cifra/cifrario, 1490-1492, and record what it says about a surviving Este-Hungary cipher key of
the 1480s-90s (page cited, quote <= 2 lines). Do not commit the pdf. If it is unreachable, log it and stop. Section "## COS-CREM" in NOTES.md.

## Wave 4 (added 14:4x UTC by date -u). Intake gates re-run 14:45: fr4735 partial (line 1), costabili partial (line 1), harley-287 partial
(line 1), fr16144 partial (line 1), decode-1162 partial (line 3): all pass. Two jobs use DECODE (J15, J16): one login each, take/release
lines on de-crypt.org, the second waits for the first's release.

### J14 MONLUC-K38 -- fr4735-monluc-lansac-poland-1573, Opus, cap USD 1.5, box 35 min
MONLUC-CURL (9a7fe7147) passed its pre-registered curl gate (p 0.0086); its --try was a non-test (known-answer control 1/6). Decide, per the
folder's PREREG and rule 4, whether the 10 f.86 curl-Y tokens can take K38 (= t) graded from f.86's own period gloss (C where the gloss reads t at
that position, M otherwise), without --try licensing anything. Commit only what the gloss supports, old labels kept; decode --check; judge rerun.

### J15 COS-BOX2 -- costabili-modena-1491, Opus, cap USD 4.5, box 90 min
COS-SPAN step 2 (not run, cap): fresh short-box reads of the R1163/R1165 slips -- boxes cut at each clear word and line end (1-3 groups), two blind
Sonnet passes on crops only + your reconciliation (3 units at ~1.5), scored under PREREG-COS-SPAN unchanged (fdd8bbe51) with its matched control.
A FAIL is the second attempt of this design: log it under rule 3. Images: one DECODE login to scratch (never committed).

### J16 HAR-GLOSS -- harley-287-1587, Opus, cap USD 2.5, box 50 min
While waiting (WAIT-PASS-5): view the DECODE ff.70r-72v and ff.96-97 images (R8482-R8487, R8496; fetched 5 Oct, never read; re-fetch to scratch with one
DECODE login if not on disk) for interlinear glosses. Leaf census only: per leaf, glossed yes/no, how many glossed groups, crop coordinates for any
glossed span, in a TSV. No transcription pass; no sign labels (the f.88r owner sort stays the owner's).

### J17 SAV-BOUCHER -- fr16144-savary-lancosme-1588, Sonnet, cap USD 1.5, box 40 min
While waiting: grep Boucher's Lettres de Henri III (1587-88 volumes; IA be-api full text, Google Books API with country=US and the key) for a reply
quoting or naming Savary de Lancosme's 29 Apr 1587 duplicata (Lancosme, Savary, Constantinople, duplicata, chiffre, April-June 1587). Log every
volume/query and hits with page where the host gives one. Search result only.

### J18 D1162-F19 -- decode-1162-modena-ambung-1492, Opus, cap USD 1.5, box 35 min
While waiting: the key-constrained check of the F19 month (febr~?, p.2 l.6) against the docket '27 febb^o' (p.1 l.2) and the dating evidence already
in NOTES (DEC1162-ENHANCE's named next). Disk only. Pre-register what would settle F19 before looking; the clear_text.tsv word changes only if the
check passes with its control; otherwise log.
