# LANE SIG-4 worker jobs (account 1, lane orchestrator session_01TCCyHP5FPpBbTnQY6Z9JDp; written 9 Oct 2026 02:5x UTC by date -u)

Lane brief .claude/briefs/lane-significance.md (+ lane-common-blast.md); starts from STATUS.md "LANE SIG handoff" (SIG-1, with SIG-2/SIG-3 lines).
Gallica probe 02:43 UTC 9 Oct: 403 (IIIF manifest, Baluze 170 btv1b90015040) -- handoff items 1-2 (Baluze 170, Gramont f.30) skipped this
incarnation per the WORK-QUEUE SIG-4 orchestrator amendment; items 3-5 checked:
- august-van-saksen: no further cipher enclosures exist (KH1-D); the only open steps are the Qf label-split re-brief (1 M token, low value)
  and ASKS 67 / the Dresden reply. Not worked this wave (judged by what it adds: ~0).
- lodewijk 4612: needs new material or a different instrument (handoff item 4). The folder's own siblings step names that material:
  **WVO 7208** (Orange to Lodewijk, Vlissingen, 21 Feb 1574, pp.1-3 cipher "Duplicata", ARAB; WVO "solved on leaf" but AX-GLOSS found no
  interlinear gloss; p5 a separate same-date clear letter), the letter 4612 says it answers ("vostre lettre du xxime de febvrier"). Its
  reading is both a letter-level result in its own right (Orange's own cipher despatch to his brother six weeks before Mook, no
  decipherment located by the folder's searches) and a topical crib for 4612.
- code 146 (5797): band tests retired, open-codes; not worked.

Every ROOM line ends "for LANE SIG-4 (account 1)". Judge every result by what it adds to the letter's content, not by count.

Intake gate (pasted 02:4x UTC, exit 0): `lodewijk-van-nassau-1573-74: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`.
Prior-work pre-run by the orchestrator (02:4x UTC, `--item-spec 'shelfmark=WVO 7208;date=1574-02-21;sender=Willem van Oranje;recipient=Lodewijk van Nassau;place=Vlissingen' --step-type transcribe --fetch`): exit 4 -- owed LEAD 1-own (SIG-4612B's claim, which has a done line 23:36 8 Oct: record it), LOOK 2-leaf (AX-GLOSS's 7208 look, NOTES table row "7208 | 5 |": record it), UNCHECKED 3-tomokiyo, 3-solver, 4-editions Groen IV and Gachard (do these by hand, below).

**Common to every worker**
- Read CLAUDE.md, .claude/briefs/prior-work-step.md and the NOTES.md sections named below. `date -u` before any time; ROOM claim with box end
  time, a halfway line, a done line (`python3 tools/room.py "<role>" '<text>' --push`, single quotes); commit and push every two units; stop
  before a unit that would cross 80% of cap or box (Usage 6: units x per-unit rate below; a transcription subagent call gets line crops only,
  never a full page -- the crop command is run and pasted before the first call). Rule 10 and rule 4a wording only; never "new", "first",
  "solved". Never call AskUserQuestion; never print credentials; never name the owner.
- Hosts: resources.huygens.knaw.nl only, one worker at a time, >= 2 s apart, descriptive UA; fetch once to disk. No Gallica request.
- Rule 3: every gate pre-registered in a committed file BEFORE the target is scored, with a control that can fail differently from the target on
  the statistic computed. Rule 7: decode with `tools/decode_key.py ... --check`, exit 0, pasted.
- file_shrink_guard on every touched file before the final push; `python3 tools/gaps_check.py lodewijk-van-nassau-1573-74` after NOTES (paste).
- Solvers: report what was found and where it was not found; do not classify novelty.

---

## SIG-7208 (Opus 5.5 with Sonnet reader subagents; cap $15, box 150 min): WVO 7208 pp.1-3 -- prior work, transcription, decode under the list-B keys, controls
Target lodewijk-van-nassau-1573-74. Read NOTES: the AX-GLOSS table (row "7208 | 5 |"), "## Escalation" siblings bullet, AX-COMP2 (7205: transcription
protocol, key_7205 from pp.8-10), AX2-BLANKS (7206, key_7206), HYPOTHESES.md "Key conflict: code 172" and the direction rule (name codes above 145
split by direction: Orange -> brothers is list B), "## SIG-4612" / "## SIG-4612B" (why 4612 needs a crib).
0. Prior work (before any priced step). Re-run the orchestrator's prior_work command; `--record` the LEAD and LOOK rows from the files named above;
   then by hand, one pasted line each: (a) Groen van Prinsterer IV (dbnl text in `groen/` and DBNL full text) and the Supplément for any letter of
   Orange to Lodewijk dated 20-23 Feb 1574 or from Vlissingen/Middelburg in Feb 1574 (also Orange's reply-dates cited in 4612's printed context);
   (b) Gachard, Correspondance de Guillaume le Taciturne III (1851; IA full text) for 21 Feb 1574; (c) the WVO record's own fields for 7208
   (print status "none named" in sources/wvo/print-status-2026-09-24.tsv:82 -- re-read the WVO detail page once); (d) Tomokiyo dutch.htm (on disk);
   (e) both solver repositories by grep (shallow clone, 7208 / "21 feb" / "Vlissingen 1574"). If the plaintext is in print, 7208 becomes KNOWN:
   proceed only as a known-answer key source (`--known-answer item:WVO 4612`) -- align it with tools/interlinear_align.py, do not report it as a reading.
1. Fetch `https://resources.huygens.knaw.nl/media/wvo/images/07000-07999/07208.pdf` once (1 request), render pp.1-3 and p5 with `pdftoppm -png -r 300`
   to the scratchpad (folder is over 30 MB: commit no full page; add a `regen_images.sh` line instead), log sha1s.
2. Pre-register (`sig7208/PREREG.md`, committed before any decode): (i) transcription protocol as AX-COMP2 (two blind Sonnet passes per page on
   line crops from `tools/iiif_lines.py --image ... --debug`, + your reconciliation from the crops; `tools/reconcile_passes.py`); transcription
   control: re-read 2 crop lines of 7205 p1 (known transcription + its decipherment) through the same protocol, gate >= 0.90 code agreement;
   (ii) key: which table (table_check against key_full / key_7205 / key_7206), the list-B values with their per-direction grades (a value attested
   only in Lodewijk -> Orange letters is M here); (iii) reading gate: French-word share of the decode vs a 200-draw value-permuted key null
   (same code frequencies, permuted values -- this changes the statistic) AND a held-out control: key_7206 alone decoding 7205 p1-2 against 7205's
   own decipherment (letter agreement), which shows what a sibling key reads on an unseen list-B letter; (iv) the p5 test: is p5 a clear copy of
   pp.1-3 (aligned-word overlap of the decode with p5 vs with 7205's decipherment as an off-topic null).
3. Units: 3 pages x 2 blind passes + 3 reconciliations = 9 units at ~$1.1 (AX-COMP2's 1.46/call at 6 pages; 7208 pages are denser -- recompute after
   page 1 and stop if the per-unit rate would cross 80% of cap) + transcription control 2 calls + decode/controls ~$1.5.
4. Decode: ciphertext_7208.tsv + decode_7208.json; `python3 tools/decode_key.py ciphers/lodewijk-van-nassau-1573-74 --config ...decode_7208.json --check`
   (exit 0); per-token grades H (period key value on a list-B leaf), S (key_full table value with control), M, I, U; counts. Run
   `tools/judge_plaintext.py` with the folder's spec/fr16 if a spec exists (paste the output, FAIL included) and the shuffled-target decode through
   the same judge (rule 3 ARM-C1 clause).
5. Then and only if 7208 reads past its gate: list every passage that bears on 4612 (dates, places, names, the 21 Feb arrangements 4612 replies to) as
   candidate cribs in `sig7208/cribs_4612.tsv` -- do not run a 4612 crib attack in this job (that is the next job, priced separately).
6. NOTES "## SIG-7208 (9 Oct 2026, account 1, for LANE SIG-4)": prior-work lines, route and request counts, control numbers beside target numbers,
   grade counts, the reading with M words marked, what the passage says in one paragraph (rule 4a wording), where it was not found; update the
   Escalation siblings bullet and Remaining gaps; HYPOTHESES.md row. Do not classify; the lane sends a reading that clears its gate to a separate
   verifier. Done line with cost by your own estimate (the orchestrator ledgers from get_session).

---

# Wave 2 (written 9 Oct 2026 03:2x UTC by date -u)

SIG-7208 (done 03:08, 9.35): 7208 is KNOWN on its own leaf (period decipherment f.223r), key source only; cribs for 4612 in
`ciphers/lodewijk-van-nassau-1573-74/sig7208/cribs_4612.tsv`. NOTES Remaining gaps "4612 cipher body" now names this job.

## SIG-4612C (Opus 5.5, solver; cap $7, box 100 min, no network, no vision calls): Lodewijk 4612 v3 -- pre-registered crib-placement test from 7208
Target lodewijk-van-nassau-1573-74. Read NOTES "## SIG-7208", "## SIG-4612", "## SIG-4612B", the Remaining gaps "4612 cipher body" item, HYPOTHESES.md
rows for 4612 (H-S: 4612 is key_full's table with some codes reassigned), `sig7208/cribs_4612.tsv`, `ciphertext_4612_v3.tsv`, `decode_4612_v3.json`.
The global LM-anneal, key_repair and word-segmentation instruments are [retired] for 4612 and are NOT reopened: this job is a different instrument
(crib placement), justified by new material (7208's known text), per rule 3's third-attempt clause.
0. Prior work: `python3 tools/prior_work.py lodewijk-van-nassau-1573-74 --item-spec 'shelfmark=KHA A 11;wvo=4612;date=1574-03-06;sender=Lodewijk van Nassau;recipient=Willem van Oranje' --step-type key --fetch`;
   paste; a DONE on "known-keys" is the false DONE SIG-4612 flagged (a different step) -- note it and proceed.
1. Pre-register (`sig4612c/PREREG.md`, committed and pushed before any 4612 score) the whole test, e.g.: for each crib word (the topical list
   from cribs_4612.tsv, spelled in the period variants you fix in advance, >= 6 letters) slide it over every position of the 4612 v3 numeral
   stream (1-120 codes, nulls 121-138 skipped as key_full does) and record placements where key_full's decode agrees on >= a pre-fixed share
   of letters; each placement implies code reassignments for the disagreeing positions. Statistic: the number of implied reassignments that
   are CONSISTENT across >= 2 independent placements (same code -> same letter, no contradiction with C-graded codes elsewhere), or the gain in
   French-word share of the full 4612 decode after applying only the consistent reassignments.
   Controls that can fail differently from the target on that statistic (rule 3, AX-5799 lesson):
   (a) positive/known-answer: the 5811 cut (N=833, printed in Groen, under key_full) with a synthetic H-S perturbation at the reassignment rate
       the 4612 70.7% share implies, and cribs taken from 5811's own Groen text at matched topical strength (same count, same lengths) -- the
       procedure must recover >= a pre-fixed share of the planted reassignments with <= a pre-fixed false-reassignment count;
   (b) off-topic null on 4612 itself: the same number of crib words of matched length drawn from 7205's or 4614's decipherment vocabulary that do
       not appear in 7208's topics (fix the list in PREREG) -- 200 draws if cheap; the topical cribs must beat the off-topic p95;
   (c) shuffled-order 4612 (token order permuted, so placements cannot line up) through the same procedure.
   Gate: (a) passes AND topical > (b) p95 AND topical > (c) p95. If (a) fails: stop, log CONTROL BELOW GATE, target not scored.
2. Units: implement in `sig4612c/crib_place.py` with an offline test (~$2), control (a) (~$1.5), target + (b)+(c) (~$1.5), NOTES (~$1). Serial CPU.
3. Only on a PASS: apply the consistent reassignments through a decode config / exceptions file (never hand-edit), `python3 tools/decode_key.py
   ciphers/lodewijk-van-nassau-1573-74 --config ... --check` exit 0; grade per token (reassigned codes S at most, crib-only placements M); quote
   the stretches that now read, with M marked. The 276 slots (p1_r05, p1_r21) as "Mastrecht" are a direction-rule lead only, never a value.
4. NOTES "## SIG-4612C (9 Oct 2026, account 1, for LANE SIG-4)": numbers for (a)/(b)/(c)/target side by side, HYPOTHESES.md row, Remaining gaps
   item updated (on a FAIL the crib instrument is logged with its attempt count, not retired after one attempt unless its own control failed),
   gaps_check. Report what was found and where it was not found; do not classify novelty.

---

# Wave 3 (written 9 Oct 2026 04:0x UTC by date -u)

SIG-4612C (done 03:29, 2.95): control (a) recall 0.512 (pass), mean G +0.107 (pass), mean false reassignments 2.5 vs <= 2.0 (FAIL);
4612 not scored. Crib instrument attempt 1 of 3.

## SIG-4612D (Opus 5.5, solver; cap $4, box 60 min, no network, no vision calls): 4612 crib placement, attempt 2 -- a changed DESIGN, control first
Target lodewijk-van-nassau-1573-74. Read NOTES "## SIG-4612C", `sig4612c/PREREG.md`, `sig4612c/crib_place.py`, `sig4612c/control.json`.
Rule 3's third-attempt clause: this attempt must change the design, not one threshold. The named change (SIG-4612C's own next step): a
reassignment is admitted only with (i) support from >= 2 independent kept placements (different cribs or non-overlapping windows), OR
(ii) one placement plus a whole-stream per-code check fixed in advance: applying c -> L alone raises the fr16 word share over ALL other
occurrences of code c outside the placement window (state the margin and the minimum count of outside occurrences in PREREG).
1. `sig4612d/PREREG.md` committed and pushed before any new control run. The SAME 25 cribs, 0.60 placement share, f calibration, seeds,
   pools (b)/(c) and the SAME false bar (mean false <= 2.0 per seed) and G > 0 as SIG-4612C -- do not relax them. The recall bar may be
   re-fixed in PREREG with a reason written before the run (fewer, better-supported reassignments are the point), but not below 0.30.
2. Control (a) first. If it fails any bar: stop, CONTROL BELOW GATE, attempt 2 of 3 logged, 4612 not scored.
3. If (a) passes: (b) and (c) and the 4612 target exactly as SIG-4612C's PREREG; gate G_topical > p95(b) AND > p95(c). On PASS apply
   through a decode config (never hand-edit key_full.tsv), grades S at most / M in crib windows, `tools/decode_key.py ... --check` exit 0,
   and quote the stretches that now read with M marked. Run `tools/judge_plaintext.py` on the resulting 4612 decode and on the shuffled
   control's decode through the same judge (rule 3 ARM-C1 clause), paste both.
4. NOTES "## SIG-4612D (9 Oct 2026, account 1, for LANE SIG-4)", HYPOTHESES.md row with both numbers, Remaining gaps item, gaps_check.
   Report what was found and where it was not found; do not classify novelty.
