target: armstrong-madison-1808
goal: a verified reading of the Armstrong-to-Madison, 20 February 1808 letter at N3 or better after two audits
started: 2026-09-27 20:31 UTC
daily_budget_usd: 40
spent_today_usd: 2.50
spent_day: 2026-09-27
closed:

## Attempts already made

In-house lane (LANE ARM/ARM2/ARM3, 26 Sept 2026, all logged in HYPOTHESES.md "Summary, cycle 1/2/3"):

- ARM-CODES: built `tools/data/uscodes-1800/` (WE028 1600-entry table; THE=972 in three renderings) -- no
  sibling table's own usage reproduces the target's last-digit skew or 900-1099 value gap.
- ARM-EN18: built the era/register-matched judge corpus `en18` (six 1794-1819 diplomatic-correspondence
  IA sources) -- leave-one-file-out false-negative 14.2/15.1%, fold spread 0.27/0.26, above the 0.05 gate;
  usable but not decisive on its own.
- ARM-A2: direct sibling-table transfer, offline, both rule-3 controls run (200 permuted-table, 200
  shuffled-target-order) -- all four tables FAIL the language judge outright; stopped, non-transfer on file.
- ARM-DESIGN: plaintext-free family B verdict -- two-level nomenclator (particle block 1-99, book >=100
  with units digit = fixed member slot), target at percentile 100 against every contiguous design and
  every real THE=972 letter; one-part/two-part/blockwise not decidable at this length.
- ARM-IMG / ARM-POOL / ARM-POOL2: fetched manuscript frames 0029-0033 and surveyed 111 frames of NARA M34
  roll 14 (keyless IIIF route); two numeral-code hits (frames 0025, 0643-44) and docket 0645 (4 of 6 items
  located) all screened and identified as ordinary THE=972 usage -- no pool candidate.
- ARM-TR / ARM-TR2: two independent manuscript transcriptions vs `ciphertext.txt`, reconciled --
  match_ratio 0.884 -> 0.957 after a crop-margin fix; one confirmed digit substitution (line 7: ms "200"
  vs ciphertext.txt "203"); page-1 lines 12-13 (dense shorthand) still do not resolve at any crop margin
  tried.
- ARM-C1: family C nomenclator solver built and controlled (`tools/families/nomenclator.py`) -- matched
  control (held-out Jefferson Vol IX letter) read 0.135 vs the 0.6 gate; CONTROL BELOW GATE, target never
  run; non-test at N=369 (139 singleton book values).
- ARM3-LOOP: family D model-in-the-loop crib rounds on the same design -- three matched controls, best
  gain mean 9.2 pts, under the 10-pt gate and inside the controls' own 13.3-pt blind spread; gate not met,
  target not run.
- ARM3-ADJ: family S2 run-adjacency structural test -- 1 of 6 statistics beyond the shuffled-position
  null's p95; positive control not subsampled to the target's 28 events; non-test at this N.
- ARM3-DICT: family G dictionary-code design excluded at U1 (fresh en18 pocket-dictionary control, ~12 sd
  separation on units-digit flatness).
- ARM-S1/ARM-S2/ARM-S3: shorthand mark inventory + symbol-by-symbol match against ten period systems
  (Taylor, Byrom, Gurney, Mavor, Weston, Macaulay, Blanchard, Annet, Holdsworth, Lewis) plus a Pitman
  control -- none identified; a fresh Taylor recalibration drifted 0.211 on freq_score between sessions
  (over the brief's own 0.1 tolerance), so ARM-S3's own four results are retired "untested-by-this-tool",
  not exclusions. Annet's own design (a two-digit numbered word/syllable index) makes the frequency half
  of the test unscoreable; its named next step (a positional/structural test) was not run.
- ARM-REC / ARM-REC2 / ARM-REC3 / ARM-LIV / ARM-JEF / ARM3-COR / ARM3-LIVCODE: searched Founders Online's
  own apparatus, and built/screened LOC pools for Livingston (5 letters 1807-09, all clear; 5 of 9 "in
  cipher" 1803-04 Livingston items screened directly, digit signature does not match), Pinkney (0
  direct hits), the Armstrong-Jefferson private channel (14 items, page-1 only, all clear), and six named
  "other correspondent" candidates (Bowdoin, Warden, Skipwith, Barlow, Mason, Parker -- nearest-date
  letters read in full, all clear) -- no second letter in this code, no key, no decode, no editorial note
  found anywhere reached. WE027 (Livingston's own nomenclator) has no table on file anywhere searched.
- ARM-BRANT: located Irving Brant Papers (LOC), Box 37, item "Official cipher used by Robert R.
  Livingston, copy, 1801-1804" (Weber 1979's own named source for a partial WE027 reconstruction) -- not
  digitised; ASKS row 77.
- Outreach to the Papers of James Madison editors (U.Va.) sent 26 Sept 2026 18:01 UTC via the project
  mailbox (ASKS row 66) -- waiting for a reply as of this write-up.
- Lane state: HYPOTHESES.md's cycle-2 summary records LANE ARM2 as idle-standing -- every cheap step
  reachable without a person or new material had been taken as of 26 Sept 2026.

Owner-directed Codex sessions, 27 Sept 2026 (folders `codex-2026-09-27{,b,c,d,e}`; ROOM.md lines 14:49-19:55
UTC), all reported UNSOLVED, none redone by this seed:

- codex-2026-09-27 (ARM-REATTACK): fresh Bourdeau inventory reconciliation; three renumbering families
  calibrated on synthetic THE972 (100% exact recovery); target sits within the optimized shuffle ranges on
  all three; no family exclusion reached.
- codex-2026-09-27b (ARM-GLYPHS): provisional glyph inventory N=257/K=36; three English controls
  99.22/100/99.22%; target not read at this stage.
- codex-2026-09-27c (ARM-PIECES): Annet 1752/1770 manuals inspected directly; bounded variable-length
  glyph-substitution surrogate (257 tokens/36 types/28 fragments) tuned to 85.21%/97.67% on held-out
  controls; target score -294.031441 against three shuffle nulls (-300.03/-297.18/-301.15) -- three nulls
  only, not treated as significance evidence by the worker itself.
- codex-2026-09-27d (ARM-GLYPH-ALT): ten local binary shape-label alternatives audited against image
  crops; joint alphabet/label search corrected 4/5 and 5/5 planted errors on fresh controls (256/257,
  257/257 recovered); target still incoherent (-299.499256129); two unconfirmed optimizer digit swaps.
- codex-2026-09-27e (ARM-PRIVATE): historical-source pivot; found two untested image leads -- a 1803
  Livingston cipher key indexed in the Monroe Papers (1963 index p.11/PDF p.27, reel 3, exact frame
  unresolved) and a private 1803 Livingston letter, CBH 1974.002 Box 1 Folder 25, catalogued with cipher
  content (Brooklyn, finding aid only) -- both logged as ASKS row 80, neither image retrieved.
- ARM-KEYIMAGE (claimed 17:43 UTC, folder `codex-2026-09-27f`): claimed to inspect/retrieve the Livingston
  key before any target transfer, but that folder is absent from the repository as landed
  (PR-LAND-15's flag, ROOM.md 18:49 UTC) -- an unreconciled discrepancy, not confirmed either way.
- Four second-opinion checkpoints landed as PRs into `second-opinions/` (chatgpt-resume, chatgpt-space,
  chatgpt-components, chatgpt-livingston-witnesses, all 27 Sept 2026): name further leads -- the Wouves
  numeric-table cipher's complete key (Wellcome-catalogued ECCO item CB0131087164, table not retrieved);
  a 20-null homophonic glyph model whose target output outranks all 20 of its own shuffles, explicitly
  flagged by its own worker as "not proof ... a small, exploratory comparison among multiple tried
  models"; a 19-entry provisional Livingston base-reading table with only 2 literal group overlaps against
  the target's 366 groups, too sparse to transfer.

## Hypotheses

| id | rank | hypothesis | needs | est_usd | status | result |
|---|---|---|---|---|---|---|
| H1 | 1 | Reconcile the ARM-KEYIMAGE / codex-2026-09-27f discrepancy: `git log --all` / `git fsck --unreachable` / re-read every PR and ROOM.md line touching that path to establish whether the claimed Livingston-key retrieval exists anywhere, before treating it as lost or as evidence for anything | nobody | 1 | done | no `codex-2026-09-27f` anywhere (every ref incl. 15 armstrong SO branches, fsck unreachable: 0 hits); the 17:43 line is a claim with no done line; the key was located instead by the ChatGPT runner (PR 50, reel 3 fr.127-128, hashes, images not on disk) |
| H2 | 2 | Formalize SO-ARMSTRONG-COMPONENTS' glyph-20-null finding (target outranks all 20 of its own shuffles) into a rule-3-sized control: rerun `codex-2026-09-27b/glyph_solve.cpp`'s model with >=200 shuffles (matching this repo's own ARM-A2/ARM3-DICT convention) and report the real percentile, PASS or FAIL | nobody | 2 | open |  |
| H3 | 3 | Run the positional/structural test ARM-S3 named as Annet's own next step (do the target's shorthand marks group in twos, the way a two-digit numbered sign index would) against the shuffled-position null already built in `adj/adj_test.py` | nobody | 1.5 | open |  |
| H4 | 4 | Re-derive the keyless NARA IIIF route for frame M34-014-0025 (Armstrong's known 15 Feb 1808 THE=972 letter, ARM-S2's flagged failure -- HTML app shell instead of an image) and run the superscript-tick-vs-baseline-dash check ARM-S2 left undone | nobody | 1 | open |  |
| H5 | 5 | A third independent blind transcription pass, with a further-widened top-margin crop, over manuscript page-1 lines 12-13 (frame 0030) -- the one span ARM-TR2 could not resolve at any margin tried -- to check whether Bourdeau's minimal "2, **, 44" notation is really an undercount there | nobody | 1.5 | open |  |
| H6 | 6 | Retrieve the Wouves numeric-table cipher's complete key from the Wellcome-catalogued ECCO item CB0131087164 (SO-ARMSTRONG-COMPONENTS) and screen it against the target's own particle/book value distribution the way ARM3-LIVCODE screened Livingston's despatches | doc: ECCO/Gale access to CB0131087164 (no ASKS row filed yet -- open one if a cloud route is tried and blocked) | 3 | open |  |
| H7 | 1 | Fetch the 1803 Livingston compact key images the ChatGPT runner located (PR 50, `second-opinions/chatgpt-checkpoint-2026-09-27-2117.md`): Monroe Papers reel 3 frames 127-128 and the undated table reel 9 frame 954, via the file URLs in `https://www.loc.gov/item/mss33217003/?fo=json` (answers 200 from the cloud, 22:13 UTC); verify SHA-256 against the checkpoint's three hashes, write images/manifest.json entries, and screen the key's readable value ranges (15/17/24/26/48/71/75, 234-284; nulls 100..9000) against the target's 366 groups vs a shuffled-value control | nobody | 1.5 | done | images fetched, all three SHA-256 match PR 50; frame 127 is the compact key (plus a 334-897 vocabulary column the fixture omitted); value-range screen: target 0.257 producible vs digit-permuted null mean 0.249 (p95 0.266) and same-length uniform null mean 0.244 (target at the 74-79th pct), en18 prose encoded with the key 1.000; 75/369 groups strip to values above 899 the key cannot produce -- this leaf is not the target's key, control-backed (livkey1803/screen.tsv, NOTES.md step H7) |
| H8 | 9 | Obtain images of the private 1803 Livingston letter, CBH 1974.002 Box 1 Folder 25 (Brooklyn), catalogued with cipher content, and any decipherment already on file with it | doc: Brooklyn CBH finding-aid images, ASKS row 80 | 0 | open |  |
| H9 | 10 | Visit or request a copy of Irving Brant Papers Box 37 (LOC Manuscript Reading Room), the one witness that could supply a WE027 reconstruction to test directly against family E | person: the owner (Reading Room visit or copy request), ASKS row 77 | 0 | open |  |
| H10 | 11 | Await and act on any reply from the Papers of James Madison editors (U.Va.) naming a second letter in this code, its correspondent, or its shorthand system | person: the owner / editors' reply, ASKS row 66 (sent 26 Sept 2026 18:01 UTC) | 0 | open |  |
| H11 | 7 | Two blind transcription passes (Sonnet subagents, line crops via `tools/iiif_lines.py --image`, one frame per call) of the reel-3 frame-127 compact key, reconciled with `tools/reconcile_passes.py`, into `key_livingston1803.tsv` graded per token; then decode the target with `tools/decode_key.py` and score through the en18 judge against a 200-shuffled-key control -- the same shape as ARM3-LIVCODE, now with the key itself rather than despatch usage | nobody -- but only worth its cost if H12 or H13 gives this leaf a role: H7 screened it out as the target's key, so a graded key TSV is for the record and for the alphabet-mark test, not for a decode | 4 | open |  |
| H12 | 1 | Screen the undated large numbered table at reel 9 frame 954 (PR 50: its 911 reads "ven", 967 "trade"; distinct from frame 127 and from PR 43's despatch witnesses) the way ARM3-LIVCODE screened Livingston usage: digit signature and the 900-1099 gap of its readable entries against the target's, before any transcription pass | nobody (H7 done: image on disk, images/monroe/mss33217-009-0954.jpg) | 1.5 | open |  |
| H13 | 8 | Compact-key design test without the key's values: under a frame-127-style design the letter alphabets are single digits 1-9 distinguished by a mark, so the target's superscript ticks (`ciphertext_ms.txt` `^`, ARM-S1) would sit on single-digit groups -- they sit on 38, 1640 and 1276 (3 ticks, no single-digit group), so first re-read the three tick crops and the single-digit groups' crops for any mark (one Sonnet vision pass, line crops via `tools/iiif_lines.py --image`), then count marked vs unmarked by group length against a shuffled-position null | nobody | 1.5 | open |  |

## Log

2026-09-27 20:31 UTC | session_01QwdzD6zYzkhzTviz7QhF4M | seed | 0 | CAMPAIGN.md written, 10 hypotheses.
2026-09-27 22:15 UTC | session_013E5jUS9GV1AsxLeUcwgbf6 | H1 | 1 | done: codex-2026-09-27f never reached GitHub in any form (all refs, 15 armstrong SO branches, fsck unreachable), the 17:43 line is a claim with no done line, not evidence; the key it aimed at was located by the ChatGPT runner (PR 50, reel 3 fr.127-128). Re-rank: H7 to rank 1 with needs nobody (locator answered, LOC item JSON reachable); H11/H12 added behind it; H2-H6 each down one.
2026-09-27 22:35 UTC | session_01H27tXgYoK6tVYXUGAN1h5T | H7 | 1.5 | done: three Monroe Papers frames fetched from tile.loc.gov IIIF, SHA-256 all match PR 50; frame 127 compact key screened by value range -- target 0.257 producible, inside both nulls (0.249 / 0.244, target 74-79th pct), en18 prose encoded with the key 1.000, 75/369 groups above 899: not the target's key, control-backed. Re-rank: H12 (screen the reel-9 frame-954 table, now on disk) to 1 since it is the remaining unexamined key image and its values run into the 900s the target uses; H11 down to 7 and re-scoped (the frame-127 key is for the record, not a decode); H13 added at 8 (alphabet-mark test, weakly grounded: 3 ticks, none on a single-digit group); H2-H6 each up one.
