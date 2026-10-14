# LANE VIV-KEYSTONE (account 4, parent session_01D7XWmthshMVqxumdDvitPh) -- jobs, 13 Oct 2026 23:5x UTC

Keystone target chosen by the owner 13 Oct 2026 (hub-seed/HANDOFF-ACCOUNT3-2026-10-13.md): **Saint-Gouard to Charles IX, Madrid,
10 Oct 1573**, `ciphers/fr16104-vivonne-spain-1572`, BnF fr.16105 ff.190r-194r, old ink piece 63, Tomokiyo's published key
(key.tsv). State: N3, D1 (AUDIT.md AUDIT 3 and AUDIT 2 VER1-VIV): 15,762 signs, H 12,290 / M 2,369 / U 1,103 after VIV-ANCHOR,
b2 + 200-wrong-key PASS, but the decode is salad -- longest all-H run 32-40 letters, no clause above the authentication distance.
The bottleneck is per-sign transcription error on this clerk hand: on the known-answer page f.103r (BENCHMARK-TX item
vivonne1573-f103r-confirm2, truth = the clerk's own decipherment ff.104r-108v under the key) the frozen two-pass pipeline reads
0.296 as measured / 0.150 flagged-excluded (benchmark-tx/txeng2/s2score/tx_bench_S2.txt), the committed reconciliation 0.221 /
0.032 (circular: the truth was aligned to it). Confusions are systematic (s<-d x17, a<-: x8, a<-m x7, i<-m x7, l<-: x6, e<-d x6,
c<-deleted x24). Owner's rules of 13 Oct (handoff a-e): one agent per job, no adversarial rounds unless a reading, label file
or count changes, no sorter asks. Lane cap 20 over both jobs. Parent reads `get_session` on each worker every 30 minutes and
interrupts at 1.3x cap.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-09-ytbiz-family-1310-jobs.md` (read it in
full) plus `.claude/briefs/README.md`'s common tail, with these substitutions: address every ROOM line "for LANE VIV-KEYSTONE
(account 4)"; export `CIPHERLAB_ACCOUNT=account-4` before any tools/room.py call; read `date -u` before writing any time;
`get_session` is not available to you, say "cost not visible to this session" in the done line. One halfway ROOM line at half the
box or half the planned units, whichever first. **No image file goes into git** (crops stay untracked; commit an
images/manifest.json entry plus the exact re-fetch command). **Hosts:** only VIV-67 touches a host: openapi.bnf.fr (IIIF Image API
v3, `--iiif-host openapi` on tools/gallica_folio.py and tools/iiif_lines.py; descriptive User-Agent; one request at a time >= 3 s
apart; `openapi.bnf.fr take` / `release` ROOM lines around each batch; if another session holds it with no release in the last 30
min, wait; on 403/429/5xx one retry after 60 s, then stop the host). Never gallica.bnf.fr (403 from the cloud). Solver jobs report
what was found and where it was not found; never classify novelty (rule 10). Nothing in either job edits key.tsv,
reading_piece63.tsv, status.json or any committed reading: both are measurements with a pre-registered gate; a reading change
is a later job with its own verifier. Both run `python3 tools/prior_work.py fr16104-vivonne-spain-1572 --item <id> --step-type
<step>` before the first priced step and paste the output in NOTES.md. Both append a NOTES.md section named for the job, refresh
"## Remaining gaps" / "## Escalation" (supersede the VIV52-O list, keep every other line), and pass `tools/gaps_check.py`.

### VIV-LAT (Opus, cap 6, box 90 min, disk only, no network, no vision call): key-constrained lattice decode with a confusion matrix learnt on this hand
Why: the S2 confusions on f.103r are systematic and the base error is 0.15-0.30, the band where a language model has headroom
(on Birago no.87 at 0.041 the same idea, TX-IDEAS M5, had none: 3 fixed / 7 broken). Tool: `tools/key_decode_lattice.py`
(subcommands learn-confusion, from-passes --confusion-matrix, decode; read its --help and tools/data/tool_shelf.tsv rows first;
grade weak/controlled-only -- so the known-answer gate below decides, not the tool's existence). Language model: the fr16 corpus
of tools/judge_plaintext.py. Key: ciphers/fr16104-vivonne-spain-1572/key.tsv (plus exceptions if decode.json names any).
Inputs (all on disk): the INDEPENDENT blind passes, never the builder's own: for f.102r `benchmark-tx/outputs/vivonne1573-f102r-dev/
passA_dv1.tsv`, `passB_dv1.tsv` (and passZ_dv1 if present) with truth `benchmark-tx/vivonne1573-f102r-dev2.truth.tsv`; for f.103r
`benchmark-tx/outputs/vivonne1573-f103r-confirm2/passA_S2.tsv`, `passB_S2.tsv`, `passZ_S2b.tsv` with truth
`benchmark-tx/vivonne1573-f103r-confirm2.truth.tsv`. Scorer: `tools/tx_bench.py` (corrected scorer; `--paired` by line, `--exclude-flagged`).
Steps, in order:
0. Write and push `ciphers/fr16104-vivonne-spain-1572/PREREG-VIVLAT.md` BEFORE any scoring: the exact commands, the lam grid
   {1, 2, 4, 8}, the dev rule, the confirm gate, the controls, the stop rule. Then prior_work.py.
1. Dev (f.102r dev2, split=dev): two folds by odd/even line ids. For each fold learn the confusion matrix (learn-confusion) from
   the OTHER fold's passes against truth, build the lattice from-passes with --confusion-matrix for the held fold, decode at each
   lam, score flagged-excluded and as measured against truth, paired by line vs the plain top-1 (no lattice) decode of the same
   passes. Choose the lam with the best flagged-excluded paired result pooled over both folds; record every number.
2. Confirm, ONE look (f.103r confirm2, lam fixed from step 1, confusion learnt on all of f.102r dev2): the registered gate is
   (a) flagged-excluded lines improved > worsened with sign test p < 0.05 AND (b) as-measured err_true not worse than the
   top-1 decode of the same passes AND (c) the built-in shuffled-key control (>= 50 value-shuffled keys): the real key ranks 1 and
   the top-1 decode's rank/z is reported beside. Report every number whether the gate passes or fails. Also report the truth-in-
   lattice share (how many of the top-1 errors have the true sign anywhere in the lattice): if it is under 50%, say so as the
   ceiling, as TX-DECODE did (27/97).
3. Only if the gate passes: apply the same recipe to ink 63 (tx/f190r..f194r passA/passB, `--ref` the matching tx/rec_f19x/
   ciphertext_draft.tsv or the rec TSV; read tx/viv63_clean.py and viv63_decode.py for how the committed reading was built so the
   token skeleton matches), write `tx/viv63_lat/` (lattice decode per page, changed positions listed, grade S for every changed
   position), decode with key.tsv, and report beside the committed reading: longest clean French run as AUDIT 2 measured it
   (consecutive H/S letters per line and across line ends), the judge score (`tools/judge_plaintext.py` with the folder's spec if
   one exists, else the fr16 corpus score), and the five longest stretches as text. No file under the folder root changes. If the
   gate fails, skip step 3, log "untested-by-this-tool at this error" only if the ceiling (truth-in-lattice) explains it, else FAIL.
Price: vision calls: 0 x USD 0 = 0; disk-only Opus, floor 2.5; dev 2 folds x 4 lam + confirm + ink 63 (9 pages) are script runs, under a minute each; cap 6.
Done line: the gate verdict first, with the dev and confirm numbers side by side, then whether step 3 ran and its longest run.

### VIV-67 (Opus, cap 12, box 150 min, openapi.bnf.fr <= 14 requests): a second known-plaintext pair in the target's own volume, ink 67/68
Why: ink 63 has no decipherment; every anchor for its unkeyed labels (c, single o, e, 2, r, l, Z, t: U 1,103 tokens) and every
known-answer figure for this hand rests on one letter (ink 40, June 1573, f.102r-f.103r). Ink 67 (20 Oct 1573, to the King, fr.16105
ff.201r-203r, Gallica btv1b9009663p canvases 206-208) is ten days after the target and carries its clerk decipherment, ink 68
("dechiffre de la precedente", ff.205r-207, canvases 210-212) -- piece_table.tsv rows 67/68 (N5-VIVTAB). Method: exactly N5-VIVK's
(NOTES.md "N5-VIVK", tx/vivk_test.py, tx/reconcile_vivk.py, tools/stream_align.py band_dp; and TX-CONFIRM-SET-2 /
benchmark-tx/build_vivonne_confirm2.py for how the truth item was built), scoped to ONE cipher page.
Units (state them in your halfway line): (1) fetch at native resolution via openapi.bnf.fr: the first cipher page of ink 67
(f.201r, canvas 206 right page, confirm the page by eye on a 600 px overview first) and the first two pages of the decipherment
(ff.205r-205v, canvases 210-211); run `tools/iiif_lines.py --iiif-host openapi ... --debug`, check the overlay, line crops under
2500 px (mandatory, pasted, before any subagent call); (2) two blind Sonnet passes on the f.201r crops, one page per call, the
N5-VIVK pass prompt and label conventions (tx/SIGNS.md), then `tools/reconcile_passes.py`; (3) two blind Sonnet passes on each
decipherment page (plain French, the dec_f10x pass prompt), merged as tx/merge_dec.py did; (4) align the f.201r sign stream to
the decipherment text under key.tsv with the banded DP (as vivk_test.py), with the 200 value-shuffled-key control (match share,
rank, p95) -- the pair stands only if the real key ranks 1 and the share clears p95, as N5-VIVK's did (0.605 vs p95 0.498).
Outputs: tx/f201r_passA.tsv, passB, rec; tx/dec_f205r_*, dec_f205v_*; `tx/vivk67_result.json`; a table of every unkeyed label
(c, o, e, 2, r, l, Z, t, and any new label) with the clerk letter aligned at each occurrence (position, aligned letter, DP
confidence) -- counts only, no key edit; and `benchmark-tx/vivonne1573-f201r-dev.truth.tsv` built the way
build_vivonne_confirm2.py builds confirm2 (split=dev; register it in BENCHMARK-TX.tsv with the control numbers in the header) so
VIV-LAT's recipe and any later reader can be scored on a second leaf of this hand. If the alignment control fails, stop after
step 4 and report the numbers; no truth file is registered. Report err_2reader for f.201r and, by the N5-VIVK route, the committed
f.201r reconciliation's own err against the new truth (say it is circular, as confirm2's committed figure is).
Price: vision calls: 6 x USD 1.4 = 8.4 (2 + 4 Sonnet subagent calls, per README per-pass rate) + the worker's own reconciliation (one unit each for f.201r and the
decipherment, bMALS rule) + alignment scripts: 8 units x 1.4 = 11.2 -> cap 12; stop before starting a unit that would cross 80% of
cap or box. If f.201r's cipher block is short (under 15 lines), add f.201v as the second page only if under 50% of the cap.
Done line: alignment share vs shuffled p95 first, then err_2reader, the unkeyed-label table's totals, and whether the truth item
was registered.

## Wave 2 (00:4x UTC 14 Oct 2026; VIV-LAT and VIV-67 done and archived)
Results read: VIV-LAT gate FAIL, ceiling -- the true sign is in the readers' lattice at only 29/234 of the top-1 errors on f.103r
(tx/vivlat/, NOTES "VIV-LAT"); a confusion matrix learnt on one reader set does not transfer to another. VIV-67 PASS: f.201r vs
ff.205r-205v aligns at 0.744 vs 200 shuffled keys p95 0.507 (rank 1/201; ink 40 was 0.605 vs 0.498); truth item
benchmark-tx/vivonne1573-f201r-dev.truth.tsv registered (894 scored; independent passes 0.185 / 0.037, 0.199 / 0.046); the unkeyed and
M labels against the clerk letter are in tx/viv67_labels.tsv and tx/viv67_labels_summary.tsv (c -> p 8 / e 5; single o -> p 5; e -> m 4;
V -> n 7; S -> b 10; 2 -> e 3; y -> r 11 / l 9; NOTES "VIV-67"). key.tsv has NO row for the plaintext letters p, m or f: the ink-67
anchors put p under labels c and o and m under label e, where ink 40 (VIV-ANCHOR) had c -> p 1, o -> p 2, e -> 0. The same rules as
wave 1 apply (no reading change without a verifier; PREREG before scoring; no image in git; openapi.bnf.fr only, take/release lines).

### VIV-KEY (Opus, cap 7, box 90 min, disk only, no network, no vision call): key rows for the unkeyed labels from the pooled clerk anchors of ink 40 and ink 67
Why: U 1,103 of 15,762 tokens in ink 63 are labels outside key.tsv; p and m are common French letters with no key row; AUDIT 3 named
"co_tandeur" x5 as a probable m gap. New material (the ink-67 anchors) allows a re-run of VIV-ANCHOR's instrument (rule 3's third-
attempt clause: new material, same tool). Instrument: exactly VIV-ANCHOR's (NOTES "VIV-ANCHOR", PREREG-VIVANCHOR.md, tx/vivanchor.py,
tx/vivanchor_gates.py: per-label anchor tally with a decision rule, then the b2 order gate and the 200-wrong-key specificity gate on
each of inks 63, 53, 54 after the key change, under new seeds), with the ink-67 anchors (tx/viv67_labels.tsv, DP confidence) pooled
with the ink-40 anchors (tx/vivanchor_result.json). Also run `tools/decode_key.py ciphers/fr16104-vivonne-spain-1572 --try
LABEL=VALUE` for each candidate (MQS-CROSSWORD; read tools/data/tool_shelf.tsv for its grade and its own control) and paste its output.
Steps: 0. PREREG-VIVKEY.md pushed before any tally: the candidate list (every label with >= 3 aligned positions pooled), the decision
rule (VIV-ANCHOR's: top letter holds >= 2/3 of aligned positions at local confidence >= 0.5 and >= 3 such positions; a label whose
top letter differs between ink 40 and ink 67 is a CONFLICT, logged, no row), the gates (b2 and 200-wrong-key on inks 63, 53, 54, new
seeds; judge score and longest clean run before/after reported, not gated), and the stop rule. 1. Tally and decide per label. 2. For
each label that passes the rule: add the key.tsv row at grade C (source: clerk anchors ink 40 + ink 67, counts in the note column),
re-run the decode scripts (tx/viv63_decode.py and the 53/54 ones, `--check` where it exists) and the gates. If any gate fails after
the change, revert that row and say so. 3. Report before/after H/M/U counts per ink, the judge score and the longest consecutive H
run per AUDIT 2's measure, with the five longest stretches as text. A reading change here goes to a verifier next (the parent spawns
it); write the per-token grade counts the verifier needs. Also update the plaintext-p / m entries of "ink 63 key questions" in
Remaining gaps. Price: vision calls: 0 x USD 0 = 0; disk-only Opus, floor 2.5; cap 7.
Done line: per label the decision (row / conflict / under 3), then the gate results per ink, then U before/after on ink 63.

### VIV-CLS (Opus, cap 12, box 150 min, openapi.bnf.fr <= 6): a supervised sign classifier trained on the two truth leaves, tested on the third
Why: the readers' errors are confident (truth-in-lattice 0.124), so no decode over their candidates can fix them; an image-side
classifier trained on this hand's own truth tiles is the one instrument that can put the true sign among the candidates. Three
truth leaves of this hand exist now: f.102r (dev2), f.103r (confirm2) and f.201r (dev, VIV-67). Train on f.102r + f.103r, test ONCE on
f.201r (held out, a different letter). Tools: `tools/glyph_atlas.py` (connected-component tiles, HOG+PCA features, `classify
--train-labels`; read its --help and tools/data/tool_shelf.tsv rows: weak on Birago, where line reads were already at 0.04-0.06;
here line reads are 0.185-0.296), `tools/box_token_align.py` (label-aware box-to-token map; the BOXMAP-RESCORE lesson: a width-only map
put tiles one token off on 10 of 26 lines), `tools/tx_bench.py`. Deps: `pip install opencv-python-headless scikit-learn scikit-image`
(works through the proxy, confirmed 13 Oct). Any new capability (a supervised fit, a top-k output in pass format) goes into
glyph_atlas.py as an option with an offline test in tools/tests/, never a private script (Usage 8). Images: f.102r/f.103r line crops
are on disk (images/c105_f102r_*, c106_f103r_*); f.201r crops are NOT (untracked, VIV-67's container): regenerate them with the exact
commands in NOTES "VIV-67" (one native region fetch, c206, then the --image cut), 1-2 requests. Steps: 0. PREREG-VIVCLS.md pushed before
any f.201r score: features, model, training set, the map, the gate. 1. Tiles + map on all three leaves; report the map's coverage
(share of truth positions with exactly one tile) per leaf -- segmentation failures are reported separately from classification.
2. Fit on f.102r + f.103r truth-labelled tiles (scored positions only; labels = ref_sign); cross-validate on those two leaves only to
choose features/k. 3. One look at f.201r: top-1 output in pass format (line, pos, sign) scored by tx_bench as measured and flagged-
excluded against vivonne1573-f201r-dev, paired by line against passA (benchmark-tx/outputs/vivonne1573-f201r-dev/ or wherever VIV-67
put it -- read NOTES "VIV-67"); truth-in-top-3 share among passA's wrong positions. Gate: (a) classifier top-1 err as measured on the
covered positions below passA's on the same positions with lines improved > worsened p < 0.05; (b) truth-in-top-3 >= 0.50 of passA's
errors on covered positions (the lattice ceiling the readers failed). Control: the same fit with training labels permuted (one run)
must score near chance. 4. Report both numbers whether the gate passes or fails; if (b) passes, say in one line how the top-3 would
feed key_decode_lattice.py (VIV-LAT's runner) -- do not run it. Price: vision calls: 2 x USD 1.5 = 3 (overlay checks only); Opus
floor 2.5; CPU fits are minutes; cap 12. Stop before a step that would cross 80% of cap or box.
Done line: gate (a) and (b) numbers first, coverage per leaf, then the permuted-label control.

## Account-2 rows (queued 00:4x UTC 14 Oct 2026 for the account-2 dispatcher; the worker addresses its ROOM lines "for LANE VIV-KEYSTONE (account 4)" and its done line to the parent session_01D7XWmthshMVqxumdDvitPh, whatever the dispatcher's spawn prompt says)

### VIV-70 (Opus, cap 12, box 150 min, openapi.bnf.fr <= 14 requests; account 2): a third known-plaintext pair, ink 70/71 (4-5 Nov 1573), first cipher page
Exactly the VIV-67 job above (read its section, then NOTES.md "VIV-67" for the method as actually run: the overview-then-native fetch,
the --image re-cut, tx/viv67_strips.py for the clerk pages, tx/viv67_prep.py's tokenisation fix, build_vivonne_f201r.py for the truth
item, tx/viv67_labels.py for the label table), with these substitutions: ink 70 = Saint-Gouard to the King, docket 4/5 Nov 1573,
fr.16105 ff.211r-213r, Gallica btv1b9009663p canvases 216-218 (first cipher page expected f.211r = canvas 216 right page; confirm by
eye on a 600 px overview, the offset here is canvas = folio + 5 as VIV-67 found); its decipherment ink 71 "dechiffre de la precedente"
ff.215r-217, canvases 220-222 (first two pages f.215r = c220 right, f.215v = c221 left). Outputs with the 70/71 names
(tx/f211r_*, tx/dec_f215r_*, dec_f215v_*, tx/dec70_norm.txt, tx/vivk70_result.json, tx/viv70_labels*.tsv,
benchmark-tx/vivonne1573-f211r-dev.truth.tsv registered in BENCHMARK-TX.tsv, split=dev). PREREG-VIV70.md pushed before any pass.
Price: vision calls: 6 x USD 1.4 = 8.4 (2 cipher + 4 decipherment Sonnet calls) + the worker's two reconciliation units; cap 12;
stop before a unit that would cross 80% of cap or box. If the ink-70 cipher does not start on f.211r (a plain head longer than a
page), take the first page that is mostly cipher and the decipherment pages that match its opening. Done line: alignment share vs
shuffled p95 first, then err_2reader, the label table totals, and whether the truth item was registered.

## Wave 3 (01:1x UTC 14 Oct 2026; VIV-KEY and VIV-CLS done and archived)
Results read: VIV-KEY added key.tsv row e -> m at grade C (4 of 5 ink-67 anchors, all inside "comm-"; ink 40 had none); the b2 and
200-wrong-key gates PASS on inks 63, 53, 54 but a post-hoc e = i passes them too, so they cannot pick the letter; decode_key --try on
ink 63 rejects e = m and prefers i (non-blind, weak at this noise); ink 63 U 1,103 -> 942, longest H run 40 unchanged, no new clause
(NOTES "VIV-KEY", PREREG-VIVKEY.md). VIV-CLS gate FAIL: a pen-unit tile kNN trained on f.102r + f.103r reads f.201r at 0.313 vs passA
0.154 on the 415 covered positions, top-3 holds the truth for 0.359 of passA's errors, coverage 0.46 (NOTES "VIV-CLS"). Same rules as
waves 1-2. Account 2 runs VIV-70 (ink 70/71 pair) in parallel from WORK-QUEUE.

### VIV-KEYV (Opus verifier, cap 6, box 90 min, openapi.bnf.fr <= 4): rule on the e -> m key row, write AUDIT 7, propagate
You are a verifier, not the solver (CLAUDE.md "Two hats"): you do not protect VIV-KEY's conclusion. Claim under audit: key.tsv row
"e -> m, grade C, clerk anchors ink 67 (4/5, all in comm-)", and the readings of inks 63, 53, 54 re-decoded under it (VIV-KEY, 14 Oct
2026). Steps: 1. Read NOTES "VIV-KEY" (its "For the verifier" paragraph), PREREG-VIVKEY.md, tx/viv67_labels.tsv rows for label e,
AUDIT.md AUDIT 2-4 (the depth measure used), and the key sheet glyphs/sheet_tomokiyo_v1.png (label e is Tomokiyo's e-like sign; the
published key gives it no value in key.tsv -- check key_tomokiyo.tsv and say what Tomokiyo's table has for it). 2. Shape look: cut the
four ink-67 "comm-" tiles (f201r L05:53, L10:59, L12:36, L13:14; regenerate the f.201r crops with the manifest "viv67" commands, 1
native request) and 8 ink-63 label-e tiles (positions from reading_piece63.tsv / tx/rec_f19x, crops regenerated from images/p63/
manifest.json, <= 3 requests) and compare by eye and with one blind Sonnet call ("same sign or not", tiles shuffled, no values
shown): is the ink-67 "comm-" sign the same glyph as ink 63's label e, or a doubled-m / "mm" ligature the readers also label e? 3. Weigh
the four single-leaf anchors (one word family) against the crossword's preference for i on 161 ink-63 positions; decide: keep at C,
downgrade to M (listed, not settled), or revert. A row that rests on one word family on one leaf is M at most unless the shape look
says the glyph is the same and the crossword's i preference is explained. 4. Depth re-check (rule 4a) on the current
reading_piece63.tsv, 53 and 54 files with AUDIT 2's longest-run measure; write "## AUDIT 7 (VIV-KEYV, 14 Oct 2026)" in AUDIT.md with
the per-item classification (N3 unchanged unless you find otherwise; D per item), the key-row verdict, and the propagation (status.json
depth fields via tools/depth_check.py; any SECOND-OPINIONS-QUEUE.tsv row for this target that quotes a changed reading). If you revert
or downgrade, make the key.tsv edit yourself, re-run the three decode scripts with --check, and say so. 5. Report what was found and
where it was not found; do not classify novelty beyond carrying the existing N3. Price: vision calls: 1 x USD 1.5 = 1.5; Opus floor
2.5; cap 6. Done line: the key-row verdict first (keep C / M / revert, and why), then D per item, then what was propagated.

### VIV-HUMAN (Opus, cap 8, box 90 min, openapi.bnf.fr <= 2): the owner's blind packet -- can a person read this hand where the machines fail?
Why: the owner offered (13 Oct 2026) to read or review signs; rule (e) of the handoff allows a sorter ask only with a pre-registered
test that consumes it within a day. This is that test. The question: on positions where the blind readers are wrong against a reliable
truth, does a person's eye get them right? If yes, a person's read of the disputed positions of ink 63 is the instrument that reaches
D2; if no, no reader of any kind will, and the lane turns to key-side and alignment work. Material: f.201r (truth vivonne1573-f201r-dev,
flags: use only UNFLAGGED scored positions, where the two clerk reads agree, so the truth is reliable), passes
benchmark-tx/outputs/vivonne1573-f201r-dev/ (passA, passB) and tx/f201r_rec.tsv. Sets: W = unflagged scored positions where passA
or passB (or both) is wrong against the truth value; R = unflagged scored positions where both are right. Sample with seed 20261014:
30 from W (all of W if fewer), 12 from R; shuffle; these are the question tiles. Build: regenerate the f.201r crops (manifest "viv67",
1 request); build the page with `tools/sign_sorter.py` ONLY (read its docstring and --help; `--signs` = every f.201r sign with its
committed rec label as the pile label, BLIND: no values, no decode choices, no reader weights; `--focus` = the 42 question tiles,
`--focus-to-tray`; `--lede` two sentences telling the owner what to do: each tile in the tray is one sign, put it in the pile whose
signs look the same, or "new sign" if none does, about 15 minutes; `--cipher-lines` so R01/R02 hold); run `tools/sorter_preflight.py`
and `tools/cvd_check.py` and paste both outputs; the page must pass every row of tools/data/sorter_owner_requirements.tsv that the
preflight checks. Write PREREG-VIVHUMAN.md BEFORE the page is built: the sets, the seed, the scoring rule (owner's pile label -> key value
vs truth value; "new sign" counts as wrong unless the truth position is off-key), the interpretation rule: owner correct share on W
>= 0.60 AND on R >= 0.90 -> "a person is an instrument for disputed positions of this hand"; on W < 0.40 -> "not an instrument"; between
-> undecided; and how the answers are consumed (tools/sign_sorter_apply.py export -> tx/vivhuman/score.py, which the worker writes and
tests on a synthetic export before the owner answers). Deliver: commit the page under tx/sorter_human/ (HTML with embedded tiles under
3 MB; no page image; this mirrors tx/sorter_fp/, the D4-VIV precedent) AND publish it with the Artifact tool (title "Vivonne f.201r:
42 signs to place", icon "grid"); put the artifact URL and the repo path in the done line and in NOTES "VIV-HUMAN". Do not score anything;
the parent scores when the owner answers. Price: vision calls: 0 x USD 0 = 0; Opus floor 2.5; the sorter build and preflight
(browser emulation) are the cost; cap 8. Done line: the artifact URL first, then |W| and |R| and the preflight verdict.

## Wave 4 (01:5x UTC 14 Oct 2026; VIV-KEYV and VIV-HUMAN done and archived; VIV-70 done on account 2)
Results read: VIV-KEYV downgraded e -> m to M: label e merges at least three signs, (A) e-loop + n compound (the comm- anchors, 15 ink-63
"-omman-"), (B) a hooked open c before 6 (plus), (C) Tomokiyo col f row 1 (faict, France); D1 held on all four inks, AUDIT 7 written,
status.json propagated (NOTES "VIV-KEYV", tx/vivkeyv_tiles.tsv, tx/vivkeyv_blind.txt). VIV-HUMAN published the owner's page
(https://claude.ai/artifact/WAPAiDSVDwYjvDotTgBFhA, tx/sorter_human/): only 13 unflagged single-tile rows exist on f.201r where a
reader is wrong -- on positions where the clerk's own decipherment is unambiguous the readers err at about 3%; the error that makes
ink 63 salad sits in the merged and unkeyed labels (U + M = 22% of its tokens) and in positions whose truth is itself uncertain.
VIV-70 (account 2): f.211r vs ff.215r-215v FAILs the registered gate by the rank rule (0.700 vs p95 0.661, rank 2 of 201) because
f.211r carries only 10 cipher lines against a 2,614-letter target; the post-hoc trimmed alignment (0.769 vs p95 0.522, rank 1) licenses
nothing until a trim rule is pre-registered (NOTES "VIV-70"). Same rules as waves 1-3.

### VIV-ESPLIT (Opus, cap 10, box 120 min, openapi.bnf.fr <= 4): split the merged labels e and y into their signs, key each sign from its own anchors
Why: the readers' label inventory conflates distinct glyphs (VIV-KEYV: label e >= 3 signs; VIV-67: label y aligns r 11 / l 9 / n 4 / e 4),
and every conflated label is M or U in the decode. Resolving two labels moves up to 161 + ~250 ink-63 tokens from M/U toward H and
is the first step that can lengthen the clean runs. Instrument order (tools first, Usage 8): (1) the three truth leaves give
supervised within-label classes: for every reader-label-e and label-y position on f.102r, f.103r, f.201r with a scored truth row,
the truth value is the class (e: m vs the (B) and (C) values; y: r / l / n / e / h); tiles from VIV-CLS's label-aware map
(tx/vivcls/map_signs.tsv; regenerate the f.201r crops with the manifest "viv67" command, 1 request) and, where the map has no tile,
a window cut on the reader token's x-span estimated from the line's token count (say which); features as glyph_atlas.py's; a
within-label classifier (3-5 classes) with leave-one-leaf-out; gate per label: held-out within-label accuracy above the majority
class with a one-sided binomial p < 0.05, and a permuted-label control near chance. (2) Apply the passing classifier to ink 63's
label-e and label-y tokens (crops from images/p63/manifest.json, <= 3 requests), write tx/viv63_esplit/ with the per-token sub-label
and confidence, and re-decode under provisional sub-sign rows (e_A -> m, e_B / e_C and y_r / y_l / y_n per their class value) with the
b2 and 200-wrong-key gates under new seeds, plus `decode_key.py --try` per sub-sign. (3) Key edit only if (1) and (2) pass for that
label: split the label in the ciphertext files the decode scripts read (document the mapping in tx/viv63_esplit/README.md so
`--check` still reproduces), add the sub-sign rows at grade C with counts, re-run every decode script with --check; report H/M/U
before/after, longest clean run per AUDIT 2's measure, and the five longest stretches as text. A verifier follows any key edit (the
parent spawns it); if nothing passes, no edit, log the numbers. Where the machine split is undecided on a shape group, write the
tile ids to tx/viv63_esplit/owner_questions.tsv for a later sorter ask (do not build a page). PREREG-VIVESPLIT.md before any
held-out score. Price: vision calls: 1 x USD 1.5 = 1.5 (one blind grouping check at most); Opus floor 2.5; cap 10; stop before a
unit that would cross 80% of cap or box. Done line: per label the held-out gate numbers first, then the ink-63 gates, then U/M/H
before and after if an edit was made.

### Account-2 row VIV-70B (Opus, cap 3, box 60 min, disk only; account 2): pre-register the trim rule, register the f.211r truth, label table
Exactly VIV-70's own "Next" (NOTES "VIV-70"): write PREREG-VIV70B.md FIRST with a trim rule derived without looking at the f.211r
alignment (the ink-67 ratio: target letters = cipher codes x (dec67 aligned letters / f.201r codes), window +-200 as confirm2's), then
re-run the alignment and the 200-shuffled-key control under it ONCE; if real ranks 1 and clears p95, build and register
benchmark-tx/vivonne1573-f211r-dev.truth.tsv (split=dev, build_vivonne_f201r.py's recipe) and run tx/viv67_labels.py's method as
tx/viv70_labels.py (counts only, no key edit); else stop and report. Done line: share vs p95 and rank first, then whether the truth
item was registered, then the label totals. ROOM lines "for LANE VIV-KEYSTONE (account 4)", done line to the parent
session_01D7XWmthshMVqxumdDvitPh.

## Wave 5 (02:2x UTC 14 Oct 2026; VIV-ESPLIT done and archived; VIV-70B running on account 2)
Results read: VIV-ESPLIT: label y's held-out split passes its registered gate but not the always-l baseline (0.408 vs 0.447; only l and
h separate per class), the ink-63 split scores like a random split, label e untestable at N 15; no key edit (NOTES "VIV-ESPLIT",
tx/viv63_esplit/owner_questions.tsv). VIV-70B (account 2, halfway 02:15): the pre-registered trim rule passes (0.769 vs p95 0.522,
rank 1/201), truth vivonne1573-f211r-dev built (398 scored; passA 0.138 / 0.006, passB 0.166 / 0.036). The day's diagnosis: on
positions whose truth is unambiguous the readers err at 1-4% (f.201r 0.037, f.211r 0.006 flagged-excluded); the salad in ink 63 comes
from merged and unkeyed labels (U + M 22%), from crop quality on its steeper pages (f.193r err_2reader 0.297 vs f.201r 0.201, f.211r
0.154) and from truth that is itself half-flagged. Same rules as waves 1-4. The owner's page (VIV-HUMAN) is unanswered; no second ask
goes to him before it is scored.

### VIV-F191 (Opus, cap 10, box 120 min, openapi.bnf.fr <= 3): one page of ink 63 read to the standard the truth leaves reach, aimed at one clause above the authentication distance
Why: D2 needs one clause above about 42 letters with no liberty and one true sentence (rule 4a). f.191r carries ink 63's longest runs
(AUDIT 3: L11, 32 letters). Its passes were two blind Sonnet reads on first-cut crops (N6-VIV63), err_2reader about 0.2-0.3 by page,
with `--follow-slope` bands known to snap onto neighbouring lines on this hand (gaps list). The truth leaves show the same readers reach
1-4% on well-cut crops where the truth is certain, so the page-level gap is crop and pass count, not the readers. Steps: 0. PREREG-
VIVF191.md before any pass: the crop recipe, the pass count, the reconciliation rule (tools/reconcile_passes.py over three passes, the
tx/reconcile_vivk.py label rules), the statistics (err_2reader pairwise before/after; b2 and 200-wrong-key on the page under new seeds;
longest clean run per AUDIT 2's measure; the registered stretch statistic of tx/viv53L_stretches.py or its ink-63 twin vs its
random-relabel null), and the stop rule. 1. Re-fetch the f.191r native region (images/p63/manifest.json; canvas 196, 1 request) and
cut it with `tools/iiif_lines.py` -- first add the deskew option the gaps list names ("deskew the region by a fitted angle before a
flat cut, what N6-VIV63C did by hand with PIL", with an offline test in tools/tests/; Usage 8: an option on the shared tool, never a
private script), check the --debug overlay, paste the command; crops under 1600 px. 2. Two fresh blind Sonnet passes on the new crops
(one page per call, tx/SIGNS.md conventions) plus the two existing passes (tx/f191r_passA/B.tsv, aligned to the new line set by
line id); reconcile four passes (majority, the vivk rules); err_2reader for each pair. 3. Re-decode the page under key.tsv
(tx/viv63_decode.py's method, grades per token; M for every position where the four passes split 2-2 or worse), the gates, the
stretch statistic, the five longest clean stretches as text with their grades. 4. Write tx/viv63_f191/ (passes, rec, decode, stats)
and a table of the M/U/split tokens inside the five longest stretches with tile ids and line positions (tx/viv63_f191/
owner_questions.tsv) -- the material for a later, clause-level owner ask; do not build a page. Do not change reading_piece63.tsv
(a reading change is the verifier's to admit: the parent spawns one if a stretch clears the distance). Price: vision calls: 2 x USD
1.4 = 2.8; reconciliation 1 unit; the deskew option ~1; Opus floor 2.5; cap 10. Done line: longest clean run before/after and whether
any stretch clears 42 letters with no liberty, then err_2reader pairs, then the gates.

### Account-2 row VIV-67B (Opus, cap 12, box 150 min, openapi.bnf.fr <= 10; account 2): the rest of ink 67 against ink 68
Exactly VIV-67's method (NOTES "VIV-67"; VIV-70B's PREREG trim rule for a cipher block shorter than its decipherment window) on
f.201v and f.202r (canvases 206 left? -- no: f.201v is canvas 207 left, f.202r canvas 207 right; confirm by eye on a 600 px overview)
against the unaligned tail of dec67 (the last 401 letters of tx/dec67_norm.txt) extended by ff.206r-206v (canvases 211 right, 212 left)
read in two blind passes each. Outputs with the 67B names (tx/f201v_*, f202r_*, dec_f206r_*, dec_f206v_*, tx/dec67b_norm.txt,
tx/vivk67b_result.json), the benchmark item vivonne1573-f201v-dev (and f202r) registered only if the registered alignment gate
passes; label table counts only. PREREG-VIV67B.md first. Price: vision calls: 8 x USD 1.4 = 11.2 -> cap 12; stop before a unit that
would cross 80%. ROOM lines "for LANE VIV-KEYSTONE (account 4)", done line to the parent session_01D7XWmthshMVqxumdDvitPh.

### VIV-HUMAN2 (Opus, cap 6, box 60 min, openapi.bnf.fr <= 2): the owner's second attempt, same tiles, piles rebuilt from truth-consistent examples
Why: the owner asked (02:4x UTC 14 Oct) to try the scored-against tiles again. The parent's pile check (NOTES "VIV-HUMAN result",
pile check bullet) found the page's "z" pile was itself full of 3-shaped tiles and the "3" pile a jumble, because the piles were built
from the committed f.201r labels, which carry the 3/z confusion. Build the same page again with these changes only (PREREG-VIVHUMAN.md
Addendum B, written and pushed first, scoring and interpretation rules unchanged, reported as "attempt 2" beside attempt 1, never
replacing it): (1) question tiles = Q04, Q14, Q15, Q19, Q12, Q23 (the six scored against him) and Q24, Q25 (the two lost to the recut
defect R12), eight tiles, shuffled with seed 20261014 again, starting in the tray; (2) for the piles 3, z, L, l, s, S, h, k (the
look-alike families these tiles touch), a tile is a pile member only if its committed label lies in the truth set of a scored
UNFLAGGED truth position it maps to 1:1 (tx/vivcls/real/map_r2_f201r.tsv, op 1:1; truth benchmark-tx/vivonne1573-f201r-dev.truth.tsv);
tiles of those labels that fail the test go to no pile (left out of the page, counted in the Addendum); every other pile as before;
blind as before (labels only, no values). If a pile is left with fewer than 3 truth-consistent members, say so in the Addendum and show
it anyway. (3) The lede adds one sentence: do not use "fix the cut" on this page (a recut tile cannot be placed yet, R12). Regenerate
the f.201r crops with the manifest "viv67" command (1 request), reuse tx/vivhuman/build_inputs.py and sets.py with the new filters
(options, not a copy), build with tools/sign_sorter.py only, run tools/sorter_preflight.py and tools/cvd_check.py, commit the page under
tx/sorter_human2/ (HTML with embedded tiles under 3 MB, no page image) and publish with the Artifact tool (title "Vivonne f.201r:
8 signs, second try", icon "grid"). Done line: the artifact URL first, then the pile member counts before/after the filter.
Price: vision calls: 0 x USD 0 = 0; Opus floor 2.5; cap 6.

## Wave 6 (03:3x UTC 14 Oct 2026; VIV-F191B, VIV-HUMAN2, VIV-67B done)
Results read: VIV-F191B (NOTES "VIV-F191B"): f.191r four-pass vote (pass D defective from L22, so three passes there), longest all-H run
32 -> 37 ("ceroaungtresgrandeouaconsdecestaaaire"), V_strict top-1 17 -> 21 (null p99 16), gates PASS; no stretch clears 42; the
non-H tokens inside the five best stretches are the s/S (-> a) and 3/z (-> d) pairs, and "aaaire" = affaire(s) with the f-sign read as
label s. VIV-HUMAN2: the owner reads the 3/z pair right when the piles are clean (7/8); R13/R14: a pile is one sign, from certain-answer
tiles. VIV-67B (account 2): f.201v truth registered (fourth leaf; c -> p 14 of 37 on three leaves). Four truth leaves now: f.102r,
f.103r, f.201r, f.201v, plus f.211r. Same rules as before.

### VIV-FKEY (Opus, cap 6, box 75 min, disk only): the f-sign -- one letter, pooled anchors from every truth leaf, PREREG'd row
Why: key.tsv has no row for f; the clerk anchors put f on label p (VIV-ANCHOR, "affaires" p p) and now on label s (VIV-F191B L31
"aaaire"); f is in affaires, faire, faict, France, fort -- the words the best stretches stumble on. Instrument: VIV-KEY's (NOTES "VIV-KEY",
PREREG-VIVKEY.md) restricted to the value f, with the anchors pooled over all truth leaves (tx/vivanchor_result.json for ink 40;
tx/viv67_labels.tsv, tx/viv70_labels.tsv, the VIV-67B label file for f.201v) plus the per-position truth files themselves (every scored
position whose truth letter is f: which reader label sits there, on each leaf). PREREG-VIVFKEY.md first: the decision rule (a label
holds f only where the truth-f positions' label distribution and that label's own truth distribution make f its majority or a clean
sub-shape -- if label p or s is mostly a or n and f only sometimes, the answer is a SPLIT (f-shape within the label), not a row: say so and
write the tile ids of the truth-f positions to tx/viv63_fkey/f_tiles.tsv for the packet below), the gates (b2 + 200 wrong keys on inks
63, 53, 54; decode_key --try f=... with its control), the stop rule. If a row or a split passes, apply it as VIV-KEY did (key.tsv grade C
with counts, decode scripts --check, before/after H/M/U and longest runs per ink); a verifier follows. If not, no edit, numbers logged.
Price: vision calls: 0 x USD 0 = 0; Opus floor 2.5; cap 6. Done line: row / split / neither first, with the pooled counts per label.

### VIV-PACKET3 (Opus, cap 8, box 75 min, openapi.bnf.fr <= 2): the owner's packet for f.191r's best neighbourhood, clean piles, re-decode pre-registered
Why: VIV-HUMAN2 showed the owner reads this hand's disputed pairs right when every pile is one sign from certain-answer tiles; f.191r
L08-L16 and L29-L32 hold the longest stretches and the M/U/split tokens that break them. Build (PREREG-VIVPACKET3.md first): question
tiles = every token on f.191r lines L08-L16 and L29-L32 whose vote grade is M or U or whose four passes split (tx/viv63_f191/rec.tsv,
decode.tsv, f191.py's vote columns), capped at 40 by stretch priority (the five V_strict stretches first, then by line), starting in
the tray; piles = one per key sign, members ONLY truth-consistent tiles from the truth leaves (label in the truth set at a scored
unflagged position; f.102r, f.103r, f.201r, f.201v, f.211r; cap 12 per pile, seed 20261014; a sign with no qualifying tile gets no pile
and is listed in the Addendum) -- never f.191r's own committed labels; blind; the lede: place each tile in the pile whose signs look the
same, "new sign" if none, do not use fix-the-cut (R12). Crops: f.191r via the VIV-F191 manifest command (1 request), tiles cut on the
reader token x-spans the way VIV-HUMAN's build_inputs did (reuse it with options), and a pile-purity check pasted: for each pile, one
blind Sonnet call "how many distinct shapes" is NOT used -- instead list per pile the truth letters of its members (must be one letter)
and show a contact sheet in the Addendum. Consuming test, registered now: the owner's placements -> labels -> re-vote those positions
(owner label replaces the plurality where he placed; "new sign" leaves U) -> re-decode f.191r with tx/viv63_f191/f191.py --stats ->
longest all-H run and V_strict before/after, with the same gates; the parent runs it when he answers; a stretch above 42 with no
liberty goes to a verifier. Publish with the Artifact tool (title "Vivonne f.191r: the signs that break the best lines"), commit under
tx/sorter_f191/ (HTML under 3 MB). Price: vision calls: 0 x USD 0 = 0; Opus floor 2.5; preflight/cvd; cap 8. Done line: the artifact
URL first, then the question count and the pile count with any sign that got no pile.

### Account-2 row VIV-DECH3 (Opus, cap 10, box 120 min, openapi.bnf.fr <= 6; account 2): a third blind read of the clerk decipherment pages to cut the truth's own noise
Why: about half the scored positions on every truth leaf are "flagged" (the two blind reads of the clerk's French disagree), which
caps every gate on this hand and turns reader error into truth noise. Pages: ff.205r-205v (ink 68, the f.201r truth), ff.206r-206v
(f.201v), ff.104r-108v only L-ranges that feed f.102r/f.103r (read tx/DEC_READ.md and the dec_f10x pass files: 6 pages max). Method:
one fresh blind Sonnet pass per page on the ink-minimum strips (tx/viv67_strips.py; crops regenerated from the manifests, 1 request per
page), merged by the existing tx/merge_dec.py / tx/viv67_merge_dec.py rules as a third vote; PREREG-VIVDECH3.md first with the
registered outcome: the flagged share per truth item before/after a three-vote rebuild (build scripts re-run with the third pass; the
truth files rebuilt ONLY as new items suffixed -3 beside the old ones, never replacing them). Report the flagged share and the passA/
passB err_true on the -3 items beside the old. Price: vision calls: 6 x USD 1.4 = 8.4; cap 10; stop before a page that would cross
80%. ROOM lines "for LANE VIV-KEYSTONE (account 4)", done line to the parent session_01D7XWmthshMVqxumdDvitPh.

### VIV-PACKET3B (Opus, cap 6, box 60 min, openapi.bnf.fr <= 2): publish the f.191r packet with hand-cut boxes and an f pile
Why: VIV-PACKET3 built the page but its box check failed (15 of 40 boxes hold no whole sign, 15 a sign no pass wrote there: the
pen-unit map is offset on f.191r), so it was rightly not published. VIV-FKEY found the f-sign is the g-like glyph the readers label g
(16 of 315 label-g positions on the truth leaves sit on a clerk f, 26x enriched; tiles in tx/viv63_fkey/f_tiles.tsv), so the packet can
also carry an f pile. Steps: PREREG-VIVPACKET3.md Addendum B first (parent's decision: option "hand-cut boxes per question"): for each
of the 40 question tiles (and the pile members drawn from f.102r/f.103r/f.201r, where the pen-unit map was already label-aware), the
worker sets the box by eye on the line crop so it holds exactly the sign the vote names at that position (one Opus look per line crop,
several boxes per look; log every box in tx/sorter_f191/boxes_handcut.tsv with the old box beside it); re-run the box check and paste
it (gate: >= 36 of 40 hold the whole sign); add pile "f" = the truth-f tiles of tx/viv63_fkey/f_tiles.tsv that have a usable box (cap
12), and keep pile g = truth-r tiles only, so the owner can tell the two apart; everything else as VIV-PACKET3 built it (blind, one
truth letter per pile, R12 sentence in the lede, no fix-the-cut). Preflight + cvd_check, commit under tx/sorter_f191/, publish with
the Artifact tool (title "Vivonne f.191r: the signs that break the best lines"). The consuming test stays as registered in
PREREG-VIVPACKET3, with one addition registered now: an owner placement into pile f at a position keys that position's token as f
(grade S, owner-read) in the re-vote. Price: vision calls: 10 x USD 0.3 = 3 (box looks on line crops, several boxes per look);
Opus floor 2.5; cap 6. Done line: the artifact URL first, then the box-check numbers before/after, then pile f's member count.
