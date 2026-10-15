# LANE DEFAULT-account-2-20261015-1410 jobs (account 2, lane orchestrator session_01G3YvfSwGyU4kTVGDbmqiF5) -- 15 Oct 2026 14:3x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 14:10 UTC 15 Oct - 00:10 UTC 16 Oct. Gate 0a: SESSION-SWEEP-account-2 claimed
since 5 Oct, stale far past 90 min, proceeded.
Backlog: VERIFY-BACKLOG (Birago/ceppo `counted` rows off limits; eckert-1864 and manteuffel audit2 need Google Books, googleapis 503 at 14:2x
UTC) -> step b, `next_steps.py --hot-only` runnable rows, checked by a read-only triage of 34 folders against each folder's latest sections
(most lines stale or waiting on a person), plus the named nexts of LANE DEFAULT-A1-1140-15 (STATUS.md handoff). HTRC EF API still MongoError
(rah-salazar stays blocked).
Excluded: live LANE DEFAULT-A4-1236-15 (baluze167, fr4735-monluc, fr5761-election, matignon, clair1161, lodewijk), VIV-KEYSTONE (fr16104,
fr16106, lodewijk LVN-NAMES, oldenbarnevelt HEID-1621, mercy, thurloe), BNF-FOCUS (fr3982, fr3985-3990; idle-standing on ASKS 163/169),
Birago family/ceppo/nevers-birago, Armstrong, Debosnys, cipher-lab-private.
Intake gate 14:3x UTC (tools/intake_gate_check.py, each PASS): decode-1162-modena-ambung-1492, fr3151-noailles-1558, bne20211-ferdinand-1478,
fr16045-pisany-rome-1585, fr16144-savary-lancosme-1588, pro3055-clinton-1779.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-15-ytbiz-default-0810-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A2-1410-15 (account 2)"; export `CIPHERLAB_ACCOUNT=account-2` before any tools/room.py call;
- a worker pays ~1 of start-up before its first unit: stop before a unit that would cross 80% of cap or box;
- still no www.googleapis.com in this lane;
- never the words solved, cracked, novel, first, new for anything this project did; never name the owner.

## Wave 1 (14:3x UTC 15 Oct)

### DEC1162-RK (Opus, cap 4, box 75 min, disk only): decode-1162-modena-ambung-1492 apply the owner's g/q sort
NOTES "## Owner's g/q sort (12 Oct 2026, ASKS 144)": the six piles (g, g-b, q, q-b, q-c, q-d) are applied in `sorter/settled_labels.tsv`;
"Next (a worker): split the labels in both ciphertext.tsv files by the new piles, re-key 1168 (`align/run_align.py`), re-run `score_g.py` and
`decode_key.py --check` (sorter/README.md), ~$3." Do exactly that, in this folder and ciphers/decode-1168 (its own ciphertext/key files).
PREREG first: which score (score_g.py's G and its control p99, as MOD1162/MOD1162B) must hold or rise for the split key to replace the merged
one; if it falls, the split stays in a scratch branch of files (`*_split.*`) and the committed reading is unchanged. Grades per rule 4; key
conflicts to HYPOTHESES.md with witnesses. Update Remaining gaps / Escalation key-rebuild line + Verdict, gaps_check, decode_key --check in
both folders. Units: scripts only, no vision.

### NOA-TAM (Sonnet, cap 1.5, box 45 min, archive.org / gallica.bnf.fr <= 6): fr3151-noailles-1558 Tamizey de Larroque 1865
D22-FTS2 named Tamizey de Larroque, *Lettres inédites de François de Noailles, évêque de Dax* (1865, Gallica bpt6k97359942) as an edition of
his letters, not opened. Find a text copy (IA search first: advancedsearch / be-api fts; Gallica texteBrut only if it answers, a 403 stops that
host), and grep it for the 1558 Venice letters (Nov 1558, the dates and phrases of this folder's cipher letter, NOTES head) and any clear
paraphrase of the enciphered news. Record every copy found, query, hit or no hit, with page/leaf where available. No reading or grade change;
tick or keep the print rung; gaps_check if the folder is `partial` (it is `open`: add a dated section only).

### BNE-PRES (Sonnet, cap 1.5, box 45 min, be-api.us.archive.org / archive.org <= 15): bne20211-ferdinand-1478 how much of the letter Paz y Meliá prints
BNE-DEC29 found "reposo al regno de navarra" as an exact phrase in Paz y Meliá, *El cronista Alonso de Palencia* (1914; IA
elcronistaalonso0000unse). Question left open: does that book print the whole letter or one sentence? Take 10-12 distinctive phrases spread
across `period_decipherment_reconciled.tsv` (beginning, middle, end; 3-5 words each, the reconciled spelling and one normalised variant) and
run each through be-api fts on that identifier (presence + snippet only; page_num is not a page locator). Report per phrase hit/no hit and
the snippet; conclude "whole / part / one passage" with the phrase map. No novelty class (a verifier's job); no reading change; Verdict line
updated, gaps_check.

### PIS-121B (Opus, cap 4, box 60 min, openapi.bnf.fr <= 6): fr16045-pisany-rome-1585 f.121 gloss re-read
LANE DEFAULT-A1-1140-15 next 1: "PIS-121's next -- two-pass line-per-call read of the 3 f.121 gloss blocks, re-run pis121/score.py
unchanged (~2)". PIS-121 registered FAIL 32 vs p99 33 with the note that its power control cannot vary with gloss-read error. PREREG addendum
first (score.py and its gate unchanged; only the gloss input changes; say in advance what result would count). iiif_lines.py crops command
pasted; 2 blind Sonnet passes, one gloss line per call, + 1 reconcile = 3 units. NOTES "## PIS-121B", gaps + Verdict, gaps_check.

### SAV-L29 (Opus, cap 3, box 50 min, openapi.bnf.fr <= 3): fr16144-savary-lancosme-1588 c251 gloss line 29 + firm 17-28
Verdict: "c251 gloss line 29 + firmer 17-28 on one-line crops, ~$2.5". SAV-GLOSS/SAV-GLOSS2 method; one-line crops (iiif_lines.py command
pasted), 2 blind Sonnet passes + 1 reconcile; append to savt/gloss_c251_c252_reconciled.tsv; no alignment (waits on the owner's sort). NOTES
"## SAV-L29", gaps + Verdict, gaps_check; take/release lines.

### CLIN-3502B (Opus, cap 4, box 60 min, image-uab.canadiana.ca <= 8): pro3055-clinton-1779 3502 Images 946-952
LANE DEFAULT-A1-1140-15 next 3: "3502 Images 946-952, then 3537, 4152, 4216 (text-known; keep under the guardrail share)". CLIN-3502's
method (PREREG B2 gate + page-permuted-key control registered before decoding; one blind pass + reconcile per page). Screen 946-952 at low
resolution first and read only the cipher pages, first two cipher pages at most. Text-known: no reading changes beyond what the gate licenses.
NOTES "## CLIN-3502B", Verdict, gaps_check.
