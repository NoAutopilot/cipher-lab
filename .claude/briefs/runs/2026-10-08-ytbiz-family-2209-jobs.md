# LANE FAMILY jobs (account 2, incarnation DEFAULT-account-2-20261008-2209, "FAMILY-A2c") -- 8 Oct 2026 22:2x UTC, lane orchestrator session_01NLigWQpxoYPadEgdJpwQW8

Lane brief: .claude/briefs/lane-family.md (+ lane-common-blast.md). Cap 60, box 22:09 UTC 8 Oct - 08:09 UTC 9 Oct. Third incarnation:
started from STATUS.md "LANE FAMILY handoff" (DEFAULT-account-2-20261008-1909) next list, then next_steps.py --hot-only runnable rows in
scope. Gate 0a clear (SESSION-SWEEP-account-2 done 5 Oct, ROOM 9073). Exclusions: eckert-* (LANE LEDGER, account 1), Gallica fetches,
Birago/Armstrong/Debosnys, huntington-blathwayt and ceppo-nevers (account-4 LANE DEPTH, 21:4x), every folder with a ROOM claim < 6 h and
no done line. Register rows re-checked by hand (prior-work check 1, orchestrator 22:2x): Manteuffel V-MANT08 fixes still unapplied
(AUD2-MANT0391 22:02 added four missing name codes); wvo-11008 "5194 known-plaintext" step not run (grep 5194: no artefact);
la-garde "transcription-error check" not run; wvo-11106 strip reads not run; na-suriname 0743-0745/0701/0703 blind transcription not run.
Intake gate 22:2x (tools/intake_gate_check.py): manteuffel partial, wvo-11008 open, la-garde-1577 open, wvo-11106 open, na-suriname partial
-- each "edition/page or full-text-search citation found within 6 lines" (exit 0).
prior_work.py (offline, 22:2x) wvo-11008 item 5194 (--step-type key): exit 0, UNCHECKED 3 + UNCHECKED-NET 1 (Groen IV/Gachard windows, no
positive control) -- KNOWN is the input for a key step, never a stop.

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE FAMILY (account 2)". If --start fails to push
  from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Prior work (`.claude/briefs/prior-work-step.md`): run `python3 tools/prior_work.py <slug> --item-spec '...' --step-type <type> --fetch`
  first and paste its output and exit code (exit 4 = the LOOK/UNCHECKED rows it lists are owed by you, then `--record` them); then checks
  1-4 by hand where v1 does not reach, one line per check (route, query, result) in your NOTES.md section BEFORE the first priced step;
  check 5 after any decode. A check that did not run is "unchecked". If check 1 shows the step already done, one ROOM line and stop.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table (one request per host at a time, >= 1.5 s apart; stop a host on 429/403/challenge, one
  retry after a pause at most). Report request counts per host. Prefer files already on disk. No Gallica.
- Shared hosts: post `<host> take` / `<host> release` ROOM lines around each batch to www.archiv.sachsen.de ("sachsen"),
  resources.huygens.knaw.nl ("huygens"), service.archief.nl / www.nationaalarchief.nl ("NA"), archive.org ("IA"); if another worker of
  this lane holds the host (a take with no release in the last 30 min), work from disk meanwhile and wait.
- Rule 3 (matched control first; a control that cannot differ from the target on the statistic is a non-test), rule 4 grading, rule 7
  (`--check` scripts). Pre-register any new gate in a PREREG-<JOB>.md pushed before the score is computed.
- Rebase before writing shared files; keep both facts on conflict. Commit only your own paths. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial/open targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the owner; never
  print credentials. Never call AskUserQuestion. Solver jobs: report what was found and where it was not found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. Opus session floor ~1.5.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR ...`); line or strip crops only, never a full
  page image to a subagent; one page (or half page) per subagent call; ~1.5 per vision call, reconciliation one more unit.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE FAMILY (account 2)",
  then a five-line final report.

## Wave 1 (22:2x UTC 8 Oct)

### MANT-FIX (Sonnet, cap 1.5, box 45 min): sachsstaatsarchiv-manteuffel-1712, apply the owed transcription fixes in f0390_08/
Handoff next 1. Apply exactly what the two audits list, no other change: V-MANT08 (AUDIT.md "AUDIT (V-MANT08)" item 2 / NOTES "V-MANT08"):
0391 r4 tok5 = 39 (y-glyph 9; "Bullinbroug" as written), 0390 r9 tok3 = 9 not 4, 0391 r5 tok1 = 160 by shape graded M (100 by sense noted),
code 217 twice more on 0391 (lines 8 and 14; line 14 doubtful per AUD2 -> M); AUD2-MANT0391 (AUDIT.md "AUDIT 2 (AUD2-MANT0391)"): add
the four missing name codes 217 (line 19), 266 (line 20), 227 (line 23), 257 (line 27) at their positions. Locate positions from the
audits' own row/token references and the crops already on disk (f0390_08/, no fetch). Then `python3 tools/decode_key.py
ciphers/sachsstaatsarchiv-manteuffel-1712/f0390_08` (regenerate) and `--check`, rerun shuffle_gate_0390.py (same seeds/shuffles) and paste
both before/after numbers into a NOTES.md section "MANT-FIX (8 Oct 2026)". Carry any reading change into AUDIT.md (one dated line under
each audit noting the fix applied, rule 10 propagation) and into SECOND-OPINIONS-QUEUE.tsv row SO-MANT-0839 if it quotes a changed word.
Rule 4 counts after the fix. No novelty or depth change.

### MANT-0609X (Opus, cap 4, box 90 min): sachsstaatsarchiv-manteuffel-1712, Loc. 694/09 frame inventory for heavy cipher frames
SIBS-PREMISE "Next sibling round" row 6. 694/09 has 302 frames (URLs in images/loc694-08-09/frames.tsv; mant0609/inventory_sample.tsv is
what is already seen). Goal: find the 694/09 frames with the most code groups (a frame with >= 60 tokens, glossed or not, is what the
key-in-hand reading needs to reach a clause). Method: "sachsen take"; fetch at a small size (<= 800 px long side, >= 2 s apart) every
uninventoried frame at stride 3 (about 85 requests; stop the host at 403/429), build contact sheets of 12 frames each locally (PIL), one
Sonnet vision call per sheet asking only "which frames show numeral code groups, light/moderate/heavy"; then native crops (iiif_lines.py)
of the top <= 6 candidates for one Opus look each: glossed?, code range (Krauske 1-401 vs nomenclator), est. tokens. Positive control: two
already-known cipher frames (0015, 0052) placed blind on the sheets -- if the sheet pass misses either, the sheet size is too small; say so
and halve stride for the rest. Write mant0609/inventory_stride3.tsv and append ranked rows to mant0609/rank_unglossed.tsv (or a glossed
list), a NOTES section, and update "## Remaining gaps" (694/09 inventory line). No transcription, no decoding.

### W11008-KP (Opus, cap 3.5, box 90 min): wvo-11008-certain-1572, the 5194 known-plaintext check and run 1/3 native look
NOTES "Remaining gaps" items 2 and 3. (a) Page 1 native look at run 1 code 120 and run 3's damaged start (images on disk, crops only;
~0.5). (b) WVO 5194 (Willem as Certain to Lodewijk, 24 June 1572, KHA A 3 895/I; WVO: "in cijferschrift"; Groen III pp. 448-449 prints
it entire in clear French): get the WVO page image (resources.huygens.knaw.nl, "huygens take", the same PDF route the 11008 images used --
see sources.tsv), crop its cipher runs, two blind passes + reconciliation, decode with key_nepveu.tsv (the table used for 11008), and diff
the decoded runs against Groen's clear text (the IA/DBNL copy already read by KHF-2). Gate, pre-registered in PREREG-W11008KP.md before the
diff: letters agreeing with Groen vs the same decode under 1000 shuffled keys (p95), per-run. A PASS = the Certain letters use this table
(a key-family confirmation for 11008, C on the agreeing values); a MISS says which runs differ. If 5194 shows no numeral runs at all
(Groen's clear text is the whole letter), say so -- that is the answer. Known text used as key input (guardrail: known-text share). Report
what was found and where it was not found.

### LAG-ERR (Sonnet, cap 1.5, box 45 min): la-garde-1577, the transcription-error re-measure (CPU only)
NOTES "Next cheapest step" (after R15-LAGMI): re-measure the base-code disagreement between ciphertext_6179_v2.tsv / ciphertext_6467_v2.tsv
and the transcription passes on disk, with marks stripped and with marks kept, and list the sign pairs that cause most of it (top 10, with
counts). If the stripped base-code disagreement is well below 0.23 (say < 0.15), name it and state that the homophonic prereg
(families/homophonic_prereg.md) should be re-run at that figure (do not run it -- a separate job); otherwise write that the target waits for
the image or pooled siblings, and hand the top pairs to `tools/lookalike_pass.py` inputs (a focus.tsv for the owner's sorter). No network,
no vision. NOTES section, gaps/escalation, gaps_check.

### BERGH-STRIP (Opus, cap 7.5, box 150 min): wvo-11106-bergh-1572, box-numbered strip reads to fix the atlas mapping
Handoff next 2 / NOTES Verdict cheapest next. GLY-11106's atlas (atlas/: 875 boxes, 60 clusters) maps box -> transcription position right
only 5/19. Cut strip crops with each box's number drawn under it (local PIL from atlas/ boxes and the page images on disk; one line per
strip, <= 2500 px), and have two blind Sonnet passes read each strip as "box number -> sign" (one call per strip group of <= 4 lines);
reconcile against tx/ (one Opus unit). Measure box->position agreement on the 19 checked positions first (gate: >= 17/19, pre-registered
in PREREG-BERGH-STRIP.md), and only then on all boxes. Output: atlas/box_sign.tsv; if the gate passes, the per-box sorter piles for the
owner (sorter/ inputs; do not publish -- the account-3 orchestrator publishes). Stop at the gate if it fails, with the reason. Unit price
~1.5 per call; state the planned call count in your claim line.

### SUR-BLIND (Opus, cap 7, box 150 min): na-suriname-map-1781, blind transcription of 0743-0745 and 0701/0703 as held-out units
NOTES Verdict cheapest next (SUR-IJ / FAM-SUR729 / FAM-SUR373). Fetch the five scans once ("NA take", service.archief.nl IIIF, read the
folder's sources.tsv/manifest for the route; native size, >= 1.5 s) to images/ with manifest entries; crop per line; two blind Sonnet
passes per page + one reconciliation, readers not told the key; mark every [ij]/[y-fam] position. Then score the held-out units under the
current key (decode script --check) against its shuffled control, as the folder's prior held-out tests did (match their gate; name it in
PREREG-SUR-BLIND.md before scoring). Report what reads and where it does not; a gate PASS goes to the lane for a separate verifier.
