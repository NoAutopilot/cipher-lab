# Unassigned-target jobs (account 4, orchestrator) -- written 9 Oct 2026 05:0x UTC (date -u 05:05)

Eight folders that nobody had assigned. Each job is the folder's own named cheapest next step, read from its NOTES.md tail (Remaining gaps /
Escalation / Verdict / newest dated section), HYPOTHESES.md and its NEXT-STEPS.tsv row. Where the register row was stale, the newer NOTES
section was followed, and the section below says so. ROOM.md check at writing: no live claim (< 6 h, no done line) on any of the eight
folders (pro3055-clinton-1779's CLIN-RG and CLIN-EYE claims both have done lines, 00:20 and 02:50 UTC 9 Oct). Gallica answered 403 on
9 Oct 2026 (LANE SIG-5 probe, ROOM 04:45 UTC): **no job below touches gallica.bnf.fr.**

## Common rules for every job
- First commands: `python3 tools/room.py --start`, `date -u`, then a ROOM claim line written with `tools/room.py` naming your job id, the
  folder, the cap and the box end time, addressed "for orchestrator (account-4)". No hand `git checkout/reset/pull` (README common tail).
  After one classifier denial: one `flag` ROOM line and stop.
- Prior work (`.claude/briefs/prior-work-step.md`): before the first priced step run the `tools/prior_work.py` command given in your
  section and paste its output and exit code. Exit 3 (DONE) or 2 (KNOWN with no `--known-answer` consumer): ROOM flag and stop. Exit 4: do
  the listed LOOK/LEAD/UNCHECKED first, then `--record <row_id> 'CLEAR: ...'` or `'KNOWN: ...'`. Then do hand checks 1-4 where v1 does not
  reach, one line each (route, query, result) in your NOTES section. A check that did not run is "unchecked". If check 1 shows the step
  is already done, write one ROOM line and stop.
- Read the folder's NOTES.md tail, HYPOTHESES.md and the AUDIT.md section list before acting. Read the last 30 ROOM lines and the last 20
  UPDATES.md lines.
- Rule 3: run the matched control first. A control that cannot differ from the target on the statistic is a non-test. Pre-register every
  gate in the PREREG file your section names, commit and push it (`git add <paths> && git commit && git push origin HEAD:main`; check that
  `git log -1 --stat` shows it) BEFORE any score is computed. Rule 3 third-attempt clause: never re-tune an instrument the folder marks
  [retired].
- Rule 4: grade per token (H/C/S/M/I) and give the counts. Rule 7: run `--check` on every decode script you touch and paste its exit code.
  For a target with a spec, paste the `tools/judge_plaintext.py` output whenever a reading changes.
- Vision: the crop step is mandatory and the command is pasted (`tools/iiif_lines.py --image FILE --out DIR ...` or the folder's own cut
  script). Use line, strip or tile crops only, never a full page to a subagent, one page or less per subagent call. Price about 1.5 per
  vision call, and count your own reconciliation as one more unit. Trial crops go in the scratchpad. Commit every crop a later eye check
  would need (folder under 30 MB).
- Good-citizen rule: one request at a time per host, >= 1.5 s apart. On a 403, 429 or challenge, stop using that host (at most one retry
  after a pause). Report request counts per host. No Gallica.
- Rebase before writing shared files and keep both facts on a conflict. Commit only your own paths. Run
  `python3 tools/file_shrink_guard.py <every file you touched>` before the final push. Push with `python3 tools/room.py --push <paths>`
  (that commits ROOM.md only; commit content files with git as above).
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and paste the OK line of `python3 tools/gaps_check.py
  <target>`. If the target has a NEAR.md row, update it in the same push when your result bears on its next step.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did. Use rule 10 wording only. Solver jobs report
  what was found and where it was not found and do not classify novelty. Never name the owner, never print credentials, never call
  AskUserQuestion. Never write a dollar figure for yourself; write "cost: see the lane ledger".
- Stop at the cap or at 80% of the box, whichever comes first. Do not start a unit that would cross 80% of either. Opus session floor
  ~1.5 (brief_price_check FLOOR Opus 2.5).
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap|stopped at box): <result, target vs control numbers
  side by side, commit>` "for orchestrator (account-4)", then a five-line final report (first line: the answer).

### UNA-CEPPO (Opus 5.5, cap 4.5, box 90 min, disk only): ceppo-nevers-fr3251-1570s, the next f.21v split pairs by count, for coverage only
Folder `ciphers/ceppo-nevers-fr3251-1570s/`. The step is named in the Verdict and the Remaining gaps f.21v row: "the remaining split pairs
in `harvest/f21v/lookalike/confusion.tsv` for coverage only, ~$3". D2-CEP21M (8 Oct) showed that no f.21v passage (max 39 letters) can
reach AD 165, so this job cannot lift depth and must not claim it. The f.21v pairs with count > 1 are all done (S65/S80 D22-CEPPO21; S10/S26 and
S13/S69 D07-CEP21; S23/S97 and S49/S73 CEPPO-SPLITS). What is left are the count-1 f.21v rows: S61/S94 L01.11 and S32/S40 L05.13 first,
then S26/X_NEW L07.34 (D07 UNDECIDED, value-neutral) and S25/X_NEW L11.2 (D07: not an oval, label kept). Skip S13/X_NEW L09.3 and
S60/S69 L06.2.12, which D07-CEP21 already decided.
- Prior work: `python3 tools/prior_work.py ceppo-nevers-fr3251-1570s --item-spec 'shelfmark=BnF fr.3251;folio=21v' --step-type transcribe
  --fetch`.
- Steps: (1) For each pair, find a shape rule from files already on disk: the printed sheet `nevers_add1.png` with
  `harvest/sign_id_map.json`, and the fr.3252 f.36 witness `harvest/witness_f36/alignment_pairs.tsv`. If a pair has no glossed witness
  (S32 has none: the looped family is [retired] for blind model reads), write "no rule" and skip it. Do not invent a rule. (2) Write
  PREREG-S61S94.md (or one PREREG for all pairs with a rule) under `harvest/f21v/lookalike/` and push it before any tile is opened. (3)
  Cut 4x tiles from `harvest/f21v/c23_cipher_w.jpg` the way D07-CEP21 did, and paste the `iiif_lines.py --groups 8 --group-upscale 3`
  command. Locate each token by its passD neighbours. Use the L09.5 x 720 correction from D4V-CEPPO if you re-use `cut_r8_tiles.py`.
- Control (rule 3): the placement control in D07-CEP21's shape (`s13s69_control.py`-type, n >= 500), which can vary on the score, plus
  `harvest/decode_control.py <seq> --shuffles 200 --windows 20 --err 0.15 --extra X_THETA2=r` on 3 seeds, before and after.
- Gate (pre-registered): change a label only where the shape rule decides it AND the decode score does not prefer the other value (the
  strict rule of D22/D07). Otherwise the token stays M.
- Write: `harvest/f21v/lookalike/<pair>_reads_f21v.tsv`; passD.tsv and `ciphertext_f21v.tsv` via `build_decode_inputs.py f21v --seq
  f21v/passD.tsv`. Paste `tools/decode_key.py ciphers/ceppo-nevers-fr3251-1570s --check`. Add a HYPOTHESES.md row per pair (target vs
  control). Add a NOTES section "UNA-CEPPO (9 Oct 2026)", update the Remaining gaps f.21v row and the Verdict, run gaps_check. Any changed
  token gets "VERIFIER WANTED" in an AUDIT.md grade note. Units: worker eye on <= 10 tiles plus CPU, ~$3.

### UNA-CLIN (Opus 5.5, cap 5, box 100 min): pro3055-clinton-1779, B.148 p.124 (the continuation of the p.123 cipher) on the 1778 key
Folder `ciphers/pro3055-clinton-1779/`. **The step named in the brief request (the p.123 re-gate, ~$1.5) is already done.** CLIN-RG (9 Oct
00:17 UTC) returned a NON-TEST at its floor and retired the alignment design under rule 3's third-attempt clause. CLIN-EYE (02:45 UTC) did
the eye check. NEXT-STEPS.tsv is stale on this row. The folder's current cheapest next (Verdict and Remaining gaps, 9 Oct) is "p.124 (the
continuation, ~$3.5), the one step that adds material". This job is that step. It is a key-consistency check on a text read at H from p.102,
not a reading.
- Prior work: `python3 tools/prior_work.py pro3055-clinton-1779 --item-spec 'shelfmark=BL Add MS 21808 (B.148);folio=p.124;date=1782-09-25'
  --step-type align --known-answer gate:UNA-CLIN --fetch` (p.102 is the known answer, KNOWN is its input).
- Steps: (1) Find p.124's IIIF id (Image 1206, the canvas after 1205 `c0ft8dg56944`) in the h1649 frame list on disk (images/,
  regen_images.sh, images_manifest_full.tsv). If it is not on disk, make ONE manifest GET. Fetch it with ONE `full/max` GET from
  image-uab.canadiana.ca (browser UA + Referer as in D4-CLIN), to the scratchpad. Commit a w1600 copy and the manifest row. (2) Cut columns with
  `SHEAR=0.012 PAD=0 python3 passes/cut_2380_p121_122.py IMGDIR OUT 1206` (add a box for 1206, paste the command) and COMMIT the column
  crops (D4-CLIN's crops were lost in scratch). (3) Make two blind Sonnet passes (column crops only, no key, no p.102), then do your own
  reconciliation as one unit.
- Gate: write PREREG-UNA-CLIN.md and push it before decoding. Use a design that has not been retired, for example B2's decode-run statistic
  on the 1778 key against a page-permuted-key control (>= 1000 seeds), with hits > control max as the gate, and the share threshold fixed in
  advance. No whole-page alignment (that design is retired). Write down beforehand how a full pair inside an un-underlined letter run is
  classed.
- Write: `passes/p124_*.tsv`, a scorer with `--check`, a HYPOTHESES/NOTES section "UNA-CLIN (9 Oct 2026)" with both numbers side by side,
  and update the Remaining gaps p.123 row and the Verdict. Run gaps_check. Units: 2 vision passes plus 1 reconciliation (~1.5 each) plus CPU,
  ~$3.5.

### UNA-NEVBIR (Opus 5.5, cap 2.5, box 60 min, disk only): nevers-birago-fr3251-1572, the three atlas-mix re-tests (no.73, no.85, fr3252-no77)
Folder `ciphers/nevers-birago-fr3251-1572/`. Verdict "cheapest next" (loose-ends 8 Oct, Remaining gaps last row, Escalation retry
sub-item): "run the three disk-only re-tests with the atlas/topk files beside a shuffled-text decode of the same length, sign count and
mix, ~$1". The source is NOTES.md TX-DECODE (around line 2153), next (1).
- Prior work: `python3 tools/prior_work.py nevers-birago-fr3251-1572 --item-spec 'shelfmark=BnF fr.3251;folio=144r' --step-type decode
  --fetch`, then the same for `folio=168r` and for `shelfmark=BnF fr.3252;folio=117r`.
- Steps: rerun TX-DECODE's re-test (lam 4, printed key, 200 value-shuffled keys, seed 1; f.144r and f.168 it16dip, f.117r fr16) with the
  lattice built as two-pass 0.8 + atlas 0.2 (`harvest/tx_decode/atlas_mix.py`, weight fixed at 0.8/0.2 as before) from `atlas/topk/no73.tsv`,
  `no85.tsv` and `fr3252-no77.tsv`.
- Control (rule 3): the same pipeline on a position-shuffled lattice of the same length, sign count and mix (5 seeds per letter). This
  control could fail and did on the two-pass lattices, so it can differ from the target.
- Gate (write PREREG-UNA-NEVBIR.md and push it before running): rank 1/201 on the real order AND shuffled-target best rank > 1 on every
  seed. Record "rank 1 holds / does not hold" per letter, next to the two-pass figures (1/3.10, 1/2.77, 1/3.66).
- Write: `harvest/tx_decode/<letter>_mix_lam4.*` and a HYPOTHESES row per letter (target vs control). Add a NOTES section "UNA-NEVBIR
  (9 Oct 2026)" and tick the loose-ends sub-item in Escalation. Run gaps_check. No grade moves: changed positions are S at best and only a
  verifier lifts them. CPU only, ~$1.

### UNA-BIR3252 (Opus 5.5, cap 4.5, box 90 min, disk only): birago-fr3252-1571-72, per-sign 4x tiles of the kept f.36-37 splits
Folder `ciphers/birago-fr3252-1571-72/`. Verdict "cheapest next" (BKLOG-0507, 7 Oct): "per-sign 4x tiles of the kept f.36-37 splits
(look-alike pairs first, ~$3, disk only)". Line-segment reconciliation calls are [retired] (RUN6-BIR3637, BKLOG-0507). This is the different
instrument they named: the D22-CEPPO21 tile shape.
- Prior work: `python3 tools/prior_work.py birago-fr3252-1571-72 --item-spec 'shelfmark=BnF fr.3252;folio=36r-37r;date=1571-04-05'
  --step-type transcribe --fetch`.
- Inputs: `harvest/f3637/adjudicate_in.tsv` (185 splits remain after the 8 r37 settles in passD_v3, which is a candidate only), and the
  native bands `../ceppo-nevers-fr3251-1570s/harvest/witness_f36/c37_f36r_cipher.jpg`, `c38_f36v_top.jpg`, `c38_f36v_mid.jpg` and
  `c38_f37r_cipher.jpg`. Locate each split sign by its neighbour context on the native band, not by "pos k of n" (that mismatch is why the
  old instrument failed). Cut 4x tiles and paste the cut command. Work the look-alike pairs first: S80/S65 by R-8, S24/S73, S73/S49.
- Gate (write `harvest/f3637/PREREG-UNA.md` and push it before any tile is read): known-answer tiles first. Use the f.36v glossed tokens
  already at C (10 C) or R-8's glossed instances, at least 5 tiles shuffled among the targets, gate >= 4/5. If the gate fails, stop and log
  a non-test. If it passes, apply only where the shape rule decides.
- Control (rule 3): `decode_control.py harvest/f3637/<new seq> --shuffles 200 --windows 20 --err <measured> --extra X_THETA2=r` on 3 seeds,
  side by side with passD_v3 (z 6.44/6.54/7.90), plus a placement control (random relabels of the same count, n >= 500).
- Write: `harvest/f3637/tiles/`, `reads_una.tsv`, and the new E figure ((one-sided + splits) / 700, a residual and not an error rate).
  Add a HYPOTHESES row, a NOTES section "UNA-BIR3252 (9 Oct 2026)", update the Remaining gaps / Escalation retry rows and the Verdict, and
  run gaps_check. Units: worker eye per tile sheet; stop before a sheet that would cross 80% of the cap. ~$3.

### UNA-NEVF27 (Opus 5.5, cap 4.5, box 60 min, disk only): fr3416-nevers-fils-1589, the f.27r L09 gloss crops to one blind Opus pass
Folder `ciphers/fr3416-nevers-fils-1589/`. Verdict "cheapest next": "the f.27r L09 gloss crops (sibling_f27/gloss/) to one blind Opus pass
under PREREG-AMNEVF27 (~$3; Sonnet passes were a non-test at K1 3/14, AM-NEVF27)". It uses a different reader, not a re-tune. By the PREREG
grade rule it cannot move f.35r tokens 45/79 by itself.
- Prior work: `python3 tools/prior_work.py fr3416-nevers-fils-1589 --item-spec 'shelfmark=BnF fr.4715;folio=27r;date=1589-12-02'
  --step-type read --known-answer gate:AMNEVF27 --fetch`.
- Steps: append an amendment to PREREG-AMNEVF27.md (the reader changes to one blind Opus 5.5 subagent; everything else is word for word)
  and push it before the call. ONE Opus subagent call on `sibling_f27/gloss/f27g_L01_s1.jpg` and `_s2.jpg` only, with the crop paths only:
  no key, no figures, no passes.tsv, and not told the question. Score it with `sibling_f27/gloss/score_gloss.py` unchanged.
- Control and gate (as registered): K1 (gloss over the frame-1 span vs "onnehorscestes") >= 10/14 and above its shuffle p95. K2 vs
  "aumoins" above its shuffle p95. If either control fails, it is a NON-TEST and S is not scored. If both pass, score S (the junction
  `43 18 [1] 32`) as the PREREG says.
- Write: an Opus row in `sibling_f27/gloss/passes.tsv`, `score_out.txt`, a NOTES section "UNA-NEVF27 (9 Oct 2026)" with K1/K2 target vs
  shuffle p95 side by side, and a re-judge of token 79 under the PREREG grade rule (expected: no change). Run `decode_f35.py --check` and
  update the Remaining gaps L05 row and the Verdict. If this attempt also fails, mark blind model reads of this gloss [retired] (the third
  reader after two Sonnet passes) and name a person's read as the next step. Run gaps_check. Units: 1 Opus vision call (~2-3) plus CPU.

### UNA-GRAM (Opus 5.5, cap 3, box 60 min, disk only): fr2980-gramont, per-sign-box shape check of the 6 R-aligned plain z on fr.3040 f.18v/f.19r
Folder `ciphers/fr2980-gramont/`. Verdict "cheapest next" (after D4-GRA, 8 Oct; NEXT-STEPS truncates it): "per-sign-box shape check of those
6 R-aligned z with R12D-GRAZB2's method and decoy control (one vision call), ~$1.5". These are the 6 plain z left as z that still align R
(OFF in both sorts or where the sorts disagree), listed in `relabel_zh.tsv`. The step closes or keeps the plain-z A (f.30) vs R (fr.3040)
conflict in HYPOTHESES.md. Running R12D-GRAZB2's passed instrument on tokens it did not box is not a re-tune.
- Prior work: `python3 tools/prior_work.py fr2980-gramont --item-spec 'shelfmark=BnF fr.3040;folio=18v-19r;date=1530-03-28' --step-type
  transcribe --fetch`.
- Steps: write PREREG-UNA-GRAM.md (R12D-GRAZB2's instrument and gate word for word; only the token set changes to the 6, plus the same
  decoy sets fh/n6, the plain-z references and >= 5 known barred-z (C1) tiles) and push it before any box is cut. Cut per-sign boxes with
  `r12zb2/seg.py` / `cut.py` from the fr.3040 half-line images on disk (images/fr3040_f18). Eye-check every overlay for box position only and
  log fixes. Then ONE blind Sonnet sort of the unlabelled tile sheets (the same reader as R12D-GRAZB2, so the instrument is unchanged), scored
  by `r12zb2/score.py` with only the paths changed.
- Gate (registered): decoy control G1 PASS first, G0 OFF <= 0.2. Then each of the 6 is classed C1 (barred, relabel `zh` via
  `relabel_zh.py`'s rule) or plain (stays z, an R-aligned plain z kept as a listed conflict).
- Write: `unagram/` (tiles, sheets, sort answer, score.out). If any token is relabelled, run `relabel_zh.py --check` and re-score with the
  registered `n8gra3/score3.py` (paste both numbers beside 0.889 on 696). Run `decode.py --check` and `tools/decode_key.py . --check`. Add
  a HYPOTHESES row (z A-vs-R entry), a NOTES section "UNA-GRAM (9 Oct 2026)", update the Verdict, and run gaps_check. key.tsv is changed
  only by its own registered open-code rule. Units: 1 Sonnet sort plus worker overlay checks plus CPU, ~$1.5.

### UNA-PISA (Opus 5.5, cap 3.5, box 75 min, disk only): fr16045-pisany-rome-1585, per-token crop compare of the key86 T45/T47/T57 tokens
Folder `ciphers/fr16045-pisany-rome-1585/`. **The named cheapest next (f.275v head L04 end, the D4-PISA tiles re-cut at native resolution)
needs the Gallica region c563, and Gallica answers 403 today (9 Oct 2026). It is not run.** The folder's best disk-only step with a named
price is in the Remaining gaps key86 T45/T47/T49/T57 row: "a different instrument is open; next: per-token crop compare of the
T45/T47/T57 tokens on f.275r/f.301v/f.302v against the table cells, disk only, ~$2". The nw_score remap is [retired] for this hypothesis.
The blind crop compare against the 688 px table copy failed its control for T40 (D07-PIST40, 1/5), so the known-answer control below gates
everything.
- Prior work: `python3 tools/prior_work.py fr16045-pisany-rome-1585 --item-spec 'shelfmark=BnF fr.16045;folio=275r' --step-type transcribe
  --fetch`, then the same for `folio=301v` and `folio=302v`.
- Steps: write PREREG-UNA-PISA.md and push it before any tile is shown. Cut per-token tiles of every T45/T47/T57 token from the committed
  line crops (`images/f275r_*`, `f301v_*`, `f302v_*`) and table-cell tiles from the key image on disk. Paste the cut command. Mix in >= 5
  known-answer tiles (tokens whose cell is settled at C on these pages, e.g. the 4 R12A-PISRS T36 labels) in seeded order. Use one blind
  Opus call per page (tiles only, no copy text, no key values).
- Gate: known-answer >= 4/5 (the D07-PIST40 control shape). If it fails, the run is a NON-TEST and the crop compare against the 688 px copy
  is logged as not discriminating for these cells too, with a higher-resolution key witness as the only reopener. If it passes, a cell
  correction is a candidate. Re-run kp86.py on the corrected key as its own pre-registered test with its shuffled-key control, and record
  both numbers.
- Write: `una_pisa/` (tiles, prompt, answers, scorer with `--check`), a HYPOTHESES row, a NOTES section "UNA-PISA (9 Oct 2026)", the
  Remaining gaps T45 row and the Verdict (keep the Gallica step as "next when Gallica answers"). Run gaps_check. Units: <= 3 Opus vision
  calls (~1.5 each); stop before a call that would cross 80% of the cap.
  Alternative (same price, also disk only, if the T45 tiles cannot be located): a third blind reader on the 14 UNSETTLED f.275r T31 tokens
  (same Remaining gaps T31 row).

### UNA-HELLEN (Opus 5.5, cap 3, box 60 min, disk only): hellen-frederick-1752, adopt the R7A-HEL53 image-check + R8-HEL 0/8 corrections into key_r4369/
Folder `ciphers/hellen-frederick-1752/`. The Verdict's first option (the 1-800 key rebuild on the full Fagel scans 5-93, ~$30-35, low
prior) is campaign-sized and is **HELD: campaign-sized, orchestrator decision**. It is not briefed here. The Verdict's second option is
this job: "adopting the image-check + 0/8 corrections into key_r4369/ (orchestrator's call, changes a counted reading)".
**DISPATCH ONLY ON THE ORCHESTRATOR'S EXPLICIT GO.** The job changes a counted reading, so rule 10 propagation applies.
- Prior work: `python3 tools/prior_work.py hellen-frederick-1752 --item-spec 'shelfmark=DECODE R1953;date=1752' --step-type decode --fetch`,
  then `... --step-type propagate-revision` before touching AUDIT.md.
- Steps: (1) apply `image_check_r1953/corrections.tsv` (high + medium, as reading_R1953_all.txt) and `zero_eight/corrections.tsv` (pos 2
  820 -> 828, pos 133 990? -> 998; pos 272 stays as transcribed, ambiguous) as an exceptions/input layer read by key_r4369's decode config.
  Leave ciphertext_R1953.txt as transcribed (never silently repaired). (2) Run `tools/decode_key.py ciphers/hellen-frederick-1752/key_r4369`,
  then `--check` (exit 0). The counts must reproduce zero_eight's H 154 / S 306 / M 15 / U 372 of 847. If they do not, stop and report the
  diff. (3) Paste `tools/judge_plaintext.py specs/hellen-frederick-1752.json --file <new reading>` (expected FAIL near the gate, -0.978).
  (4) Rule 10 propagation: carry the reading change into AUDIT.md (grade note, safe sentence re-checked), into any SECOND-OPINIONS-QUEUE.tsv
  row for this target, and into status.json depth fields. Mark VERIFIER WANTED for a rule-7 fresh re-derivation.
- Control: none needed for adoption. The corrections were each made on the image under R8-HEL's PREREG and R7A-HEL53's reconciliation, and
  no new gate is introduced. State that in NOTES.
- Write: a NOTES section "UNA-HELLEN (9 Oct 2026)" with the before/after counts table, a HYPOTHESES line if a key value's reading changes
  ("soin" -> "suis", M "le" -> H "d"), and the Verdict (1 internal gap remains: codes 1-800, no-key-material, the campaign HELD). Run
  gaps_check. CPU plus file edits, ~$1.5.

## Not briefed
- None BLOCKED outright. UNA-PISA replaces its Gallica step with the folder's named disk-only T45 step.
- HELD: hellen-frederick-1752's 1-800 key rebuild (~$30-35, campaign-sized, orchestrator decision). UNA-HELLEN is the sub-$6 alternative,
  dispatch on the orchestrator's go.

## Summary
| job_id | folder | cap | box | model | account-suggestion |
|---|---|---|---|---|---|
| UNA-CEPPO | ceppo-nevers-fr3251-1570s | 4.5 | 90 | Opus 5.5 | any |
| UNA-CLIN | pro3055-clinton-1779 | 5 | 100 | Opus 5.5 | any |
| UNA-NEVBIR | nevers-birago-fr3251-1572 | 2.5 | 60 | Opus 5.5 | any |
| UNA-BIR3252 | birago-fr3252-1571-72 | 4.5 | 90 | Opus 5.5 | any |
| UNA-NEVF27 | fr3416-nevers-fils-1589 | 4.5 | 60 | Opus 5.5 | any |
| UNA-GRAM | fr2980-gramont | 3 | 60 | Opus 5.5 | any |
| UNA-PISA | fr16045-pisany-rome-1585 | 3.5 | 75 | Opus 5.5 | any |
| UNA-HELLEN | hellen-frederick-1752 | 3 | 60 | Opus 5.5 | any (orchestrator go first) |
