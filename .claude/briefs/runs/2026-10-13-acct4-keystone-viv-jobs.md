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

## JOB VIV-GSPLIT (wave 7, 15 Oct 2026 01:5x UTC by date -u; account-4 parent) -- split label g into the r-sign and the f-sign, machine side

Model: Opus 5.5. Cap USD 6 (Opus floor 2.5). Box 60 minutes from the claim; stop before any unit that would cross 80% of cap or box.
Context: VIV-FKEY (NOTES.md, 14 Oct 2026) showed plaintext f has no key row: it is a sub-shape hidden under reader label g (key r; 16 of the
60 counting truth-f positions across the five truth leaves, 26x enrichment, p 1e-18), with smaller shares under p, single o and y. VIV-PACKET3B
eyed three of the truth-f g tiles as "a looped-top stem with a lower loop, visibly unlike the truth-r g tiles (g with a descender)". The owner's
f.191r packet (NOTES "VIV-PACKET3 result", 15 Oct 2026) returned a negative on the run gate and left f.191r at D1; the one key change in sight
that lengthens runs is this split. This job is measurement only: no key.tsv edit, no reading edit, no status change; a verifier decides any key row.

Steps, in order:
1. `tools/room.py --start`, read the last 30 ROOM.md lines, claim. Write `ciphers/fr16104-vivonne-spain-1572/PREREG-VIVGSPLIT.md` and push it
   BEFORE any tile is classified: the instrument, the held-out design, the gates below, the seed, and what is reported either way.
2. Material (disk first). The label-g tiles of the three truth leaves with crops on disk (f.102r dev2, f.103r confirm2, f.201r), boxed by the
   label-aware VIV-CLS map at op 1:1 (`tx/vivcls/map_signs.tsv`; Addendum B used the same source), with the clerk's letter at each position from
   the truth items (f = the 16 anchors in `tx/viv63_fkey/f_tiles.tsv`, split_label yes; r = the rest at scored, unflagged rows). If a truth leaf's
   crops are missing, regenerate them with the committed command in its own NOTES section (openapi.bnf.fr: take/release lines in ROOM.md, one
   request at a time >= 3 s apart, at most 4 requests in the whole job, disk first).
3. Instrument: `tools/glyph_atlas.py classify --boxes` (the shared tool; rule 8 -- an option added to it, not a private copy, if something is
   missing), kNN in the atlas feature space over the g tiles, binary f vs r. Design: leave-one-leaf-out (train on two leaves, predict the third),
   all three folds, per-fold and pooled. Gates (registered): pooled held-out f recall >= 0.60 AND precision >= 0.60 (per-class breakdown printed,
   the r class too -- AX-NAMES lesson: never the blended accuracy alone), AND F1 above the 99th percentile of 200 label-shuffled nulls (the same
   tiles, f/r labels permuted within each training leaf). Report the per-fold spread beside the pooled number; a fold with N_f < 4 is reported
   as untestable at that N, not as a pass or a fail.
4. If the gate PASSes: apply the two-leaf model to every g token of f.191r (the VIV-F191 line crops; regenerate with the committed command if
   gone, within the 4-request budget), writing `tx/sorter_f191/gsplit_override_2026-10-15.tsv` in the owner_override format (line, pos, sid,
   qid='', pile='gsplit', new_sign='gf', action='classifier-f', rec_sign, rec_flag, q_code) for the predicted-f positions only. Then run
   `tx/viv63_f191/f191.py --override <that file> --tag gsplit --stats` TWICE as registered here: (a) as is (gf is outside the key -> U, so the
   strict all-H run can only shorten or hold: this is the registered decision number); (b) with a `letter` column read by a small extension of
   `apply_override` (new_sign not in key + letter given -> that letter, grade 'S'), reporting the longest H-or-S run beside the strict all-H
   run. Decision rule (registered): the lane's D2 gate stays "no liberty = all H"; (b) is reported as what a verified key row WOULD give, never
   as the result. If the gate FAILs: log the numbers, no f.191r run, verdict "untested-by-this-instrument at N_f=16".
5. Side table, report only (no gate): classify the owner's 13 new-pile tiles from `tx/sorter_f191/owner_override_2026-10-15.tsv` (action
   new-sign, by sid; the page's crops are embedded in tx/sorter_f191/sorter_viv_f191.html DATA, or recut from the line crops) with the same
   model, and say for each whether it falls nearer f, r, or neither; the three reader-r tiles of one new pile (L08:20, L08:31, L12:37) first.
6. Two Opus eye checks at most (contact sheets of the predicted-f and predicted-r exemplars, one each), pasted as a sentence each; no subagent
   writes a file (readers return text, the worker saves it). Price: vision calls: 2 x USD 0.5 = 1; Opus floor 2.5; cap 6.
7. NOTES.md section "## VIV-GSPLIT (<date -u>)": material counts per leaf, per-fold and pooled numbers with the null, the verdict, the f.191r
   numbers (a) and (b) if run, the side table, requests per host (<= 4 openapi.bnf.fr), cost "not visible to this session". `f191.py --check`
   must still pass. HYPOTHESES.md: one row (family "g-split f/r classifier", control = the shuffled-label null, both numbers). file_shrink_guard
   on every touched file; commit by explicit path; pull --rebase; push to main; ROOM.md done line: verdict first, then recall/precision/F1 vs
   null p99, then the f.191r strict run before/after, then (b). Stop. Report what was found and where it was not found; do not classify novelty,
   do not edit key.tsv, do not touch status.json, do not start VIV-F191C or any owner page.

## JOB VIV-GSPLIT2 (wave 8, 15 Oct 2026 04:5x UTC by date -u; account-4 parent) -- the g-split re-run at N_f >= 12 (new material: f.202r, f.211v)

Model: Opus 5.5. Cap USD 6 (Opus floor 2.5). Box 60 minutes from the claim; stop before any unit that would cross 80% of cap or box.
Why: VIV-GSPLIT (NOTES, 01:59 UTC) passed its registered gate at N_f = 6 only (every fold untestable alone) and its own next line asks for
N_f >= 12 before any key row. Since then VIV-67C registered f.202r (4 more truth-f positions under label g, pooled 6 -> 10) and VIV-70C2
registered f.211v (its label table: check it for label-g truth-f positions). This is new material, so a re-run of the same registered
instrument is licensed (CLAUDE.md rule 3's third-attempt clause does not apply to new material). Measurement only: no key.tsv, reading or
status.json edit; a verifier decides any key row.
Steps: 1. room --start, claim; PREREG-VIVGSPLIT2.md pushed before any tile is cut: same instrument and gates as PREREG-VIVGSPLIT (1-NN over
glyph_atlas features, leave-one-leaf-out now over FIVE leaves where tiles exist, pooled f recall >= 0.60 and precision >= 0.60 and F1 > the
99th pct of 200 label-shuffled nulls, per-fold spread reported, a fold with N_f < 4 untestable alone), plus the registered minimum N_f >= 12
before the f.191r step runs at all. 2. Material: the VIV-GSPLIT material.tsv (6 f / 34 r tiles) + the f.202r label-g positions from
tx/viv67c (its truth item vivonne1573-f202r-dev: 4 truth-f, up to 50 truth-r, cap r at 20 per leaf by seed 20261015) + f.211v's if any +
the 5 untiled label-g f anchors of VIV-FKEY hand-cut by eye on the line crops (one Opus look per line crop, boxes logged in
tx/vivgsplit2/boxes_handcut.tsv with a whole/unsure/none verdict, only `whole` used). Crops: regenerate f.202r and f.211v line crops with
the committed commands in NOTES "VIV-67C" / "VIV-70C2" (openapi.bnf.fr: take/release lines, one at a time >= 3 s, at most 4 requests in
the job; disk first). 3. Run `tx/vivgsplit/gsplit.py` (extend it in place, never a private copy) with the enlarged material; report per
fold and pooled with the null. 4. If N_f >= 12 AND the gate PASSes: f.191r step exactly as VIV-GSPLIT Addendum A (28 tileable g tiles,
plus any newly tileable ones; `f191.py --override ... --tag gsplit2 --stats`, (a) strict and (b) letter-S variants as registered there).
Otherwise: log the numbers and verdict "untested at N_f = <n>" and stop. 5. Two Opus eye checks at most (contact sheets of predicted-f and
predicted-r), no subagent writes a file. Price: vision calls: 3 x USD 0.5 = 1.5 (two contact sheets + the hand-cut look); Opus floor 2.5;
cap 6. 6. NOTES "## VIV-GSPLIT2 (<date -u>)", HYPOTHESES.md row with the control, requests per host, `f191.py --check` passes, shrink
guard, commit by path, pull --rebase, push; done line verdict first (N_f, recall/precision/F1 vs null p99, f.191r strict run before/after).

## JOB VIV-F191D (wave 8, 15 Oct 2026 04:5x UTC by date -u; account-4 parent) -- a 5-pass reconciliation rule for f.191r L22-L36, registered then run

Model: Opus 5.5. Cap USD 3 (Opus floor 2.5). Box 45 minutes from the claim. Disk only: no network, no readers.
Why: VIV-F191C (NOTES, 02:2x UTC) added blind pass E on L22-L36 (drift check 15/15; noisier than A-C: agreement 0.24 vs 0.12-0.17); as a
fourth usable vote on the 123 flagged columns it settles 52 the same way, flips 7 (five via the 3/z RULES pair) and leaves 64 flagged. The
reconciliation in tx/viv63_f191/f191.py is 3-of-4 over A-D; D is the drifted pass on these lines.
Steps: 1. room --start, claim; PREREG-VIVF191D.md pushed before any run: the rule (on L22-L36 only: votes A, B, C, E, with D kept but E
weighted no higher than D -- the registered rule is "settled when >= 3 of the 5 agree; a 2-2-1 falls to the existing decide() on A-D with
E as tie-breaker only when it agrees with C"; write the exact decision table), the gates (longest all-H run on f.191r and V_strict top-1/
top-3 with the 200-shuffle null and the same controls C1/C2, before = committed rec.tsv, after = the 5-pass build; the decision stays
s.5-of-PREREG-VIVPACKET3's: a stretch >= 42 all-H with no liberty goes to a verifier, else logged), and the no-liberty clause (no position
may be settled by E alone). 2. Implement as an option on f191.py (`--five-pass`, output rec_5pass.tsv / decode_5pass.tsv / stats_5pass.json,
rec.tsv and decode.tsv untouched, `--check` still passes). 3. Run; report before/after; count positions settled, flipped, still flagged, and
list every flip with its five votes. 4. NOTES "## VIV-F191D (<date -u>)", HYPOTHESES.md row (control = the shuffle null + C1/C2), shrink
guard, commit by path, pull --rebase, push; done line: longest all-H run before/after first, then V_strict, then flips. Price: vision calls:
0 x USD 0 = 0. No key, reading or status.json edit; do not start any other job.

## JOB VIV-GSPLIT3 (wave 9, 15 Oct 2026 05:5x UTC by date -u; account-4 parent) -- the g-split with every label-g truth tile hand-cut (a different instrument)

Model: Opus 5.5. Cap USD 6 (Opus floor 2.5). Box 60 minutes from the claim; stop before any unit that would cross 80% of cap or box.
Why: VIV-GSPLIT2 (NOTES) was untested at N_f = 11 and showed the auto map, not the classifier, is the limit (2 of 2 new f tiles and 3 of 22
sampled r tiles mis-cut; the re-cut alone cost one of GSPLIT's four hits). Rule 3's third-attempt clause allows this only as a different
instrument: every tile in this run is cut by eye, none by the map. Measurement only: no key.tsv, reading or status.json edit.
Steps: 1. room --start, claim; PREREG-VIVGSPLIT3.md pushed first: same classifier and gates as PREREG-VIVGSPLIT (pooled f recall >= 0.60,
precision >= 0.60, F1 > null p99 over 200 label shuffles; per-fold spread; folds with N_f < 4 untestable alone), registered minimum N_f >= 12
CHECKED AGAINST THE MATERIAL COUNT before the run (list the anchors by leaf: VIV-FKEY's 16 label-g truth-f positions on f.102r/f.103r/f.201r/
f.201v/f.211r + f.202r's 4 + f.211v's if any; if fewer than 12 can be boxed `whole`, stop after the count and log "untestable at N_f = <n>").
2. Hand-cut every label-g truth-f tile and a seeded sample of 20 truth-r tiles per leaf (seed 20261015) on the line crops by eye: one Opus look
per line crop, several boxes per look, each logged in tx/vivgsplit3/boxes_handcut.tsv with a whole/unsure/none verdict; only `whole` enters.
Crops: regenerate with the committed commands (NOTES "VIV-F191", "VIV-67", "VIV-67B", "VIV-70B", "VIV-67C", "VIV-70C2"; openapi.bnf.fr
take/release lines, one at a time >= 3 s, at most 6 requests in the job; disk first). 3. `tx/vivgsplit/gsplit.py` extended in place for
hand-cut boxes (glyph_atlas classify --boxes); leave-one-leaf-out over every leaf with tiles. 4. Gate PASS at N_f >= 12 -> the f.191r step
as VIV-GSPLIT Addendum A, but on HAND-CUT f.191r g tiles too (the 28 tileable + any the map missed, cut by eye, same log), then
`f191.py --override ... --tag gsplit3 --stats`, (a) strict and (b) letter-S. Otherwise log and stop. 5. Price: vision calls: 8 x USD 0.5 = 4
(about six line-crop looks for boxes + two contact sheets); Opus floor 2.5; cap 6. 6. NOTES "## VIV-GSPLIT3 (<date -u>)", HYPOTHESES row,
requests per host, `f191.py --check` passes, shrink guard, commit by path, pull --rebase, push; done line: N_f and verdict first.

## JOB VIV-GSPLIT3B (wave 9b, 15 Oct 2026 06:5x UTC by date -u; account-4 parent) -- finish VIV-GSPLIT3's r sample; same registered test, not a new attempt

Model: Opus 5.5. Cap USD 5 (Opus floor 2.5). Box 50 minutes from the claim; stop before any unit that would cross 80% of cap or box.
Why: VIV-GSPLIT3 (NOTES, 06:09 UTC) reached N_f = 18 hand-cut and a gate PASS on an incomplete r sample (29 of 138 r tiles cut; recall 0.889,
precision 0.727); its own projection puts precision near 0.36 at the full r sample, so the test is unfinished, not passed. This job completes
the SAME registered test (PREREG-VIVGSPLIT3.md, unchanged; add an Addendum A naming this continuation and the per-tile price before any
cut). Measurement only: no key.tsv, reading or status.json edit.
Steps: 1. room --start, claim; PREREG-VIVGSPLIT3.md Addendum A pushed first. 2. Hand-cut the remaining 106 planned r tiles the same way
(one Opus look per line crop, about 15 tiles per look, boxes logged in tx/vivgsplit3/boxes_handcut.tsv with whole/unsure/none; crops
regenerated by the committed commands, openapi.bnf.fr take/release, one at a time >= 3 s, at most 6 requests). Unit = one look; stop before
a look that would cross 80% of cap or box and report the r count reached. 3. Recompute the registered gate on the full hand-cut material
(leave-one-leaf-out, pooled recall/precision/F1 vs 200 label-shuffled nulls, per-fold spread). 4. PASS -> the f.191r step as VIV-GSPLIT
Addendum A on hand-cut f.191r g tiles (cut by eye, same log), `f191.py --override ... --tag gsplit3 --stats`, (a) strict and (b) letter-S;
FAIL -> log; the g-split family is then [retired] for this instrument absent new material. 5. Price: vision calls: 9 x USD 0.45 = 4.05
(about 7 looks for 106 tiles + 2 contact sheets); Opus floor 2.5; cap 5. 6. NOTES "## VIV-GSPLIT3B (<date -u>)", HYPOTHESES row updated,
requests per host, `f191.py --check` passes, shrink guard, commit by path, pull --rebase, push; done line: N_r reached, gate numbers, verdict,
f.191r strict run before/after if run.

## JOB VIV-GSPLIT3C (wave 9c, 15 Oct 2026 08:0x UTC by date -u; account-4 parent) -- the last 66 r tiles, then the registered verdict and the f.191r step

Model: Opus 5.5. Cap USD 4.5 (Opus floor 2.5). Box 45 minutes from the claim; stop before any unit that would cross 80% of cap or box.
Why: VIV-GSPLIT3B (NOTES, 07:12 UTC) reached N_r = 59 of 138 with every registered number above its gate (recall 0.889, precision 0.842, F1
0.865 vs null p99 0.571) but Addendum A rightly withholds PASS until the r sample is complete. This job completes the SAME registered test
(PREREG-VIVGSPLIT3.md; add Addendum B naming this continuation and the price 2 looks per 20 tiles before any cut). Measurement only.
Steps: 1. room --start, claim; Addendum B pushed. 2. Cut the last 66 r targets with `panels.py sheets --rest` (sheets 01-04 after the
3B log), 2 looks per 20 (cut + check), boxes logged in tx/vivgsplit3/boxes_handcut.tsv (whole/unsure/none); crops regenerated by the
committed commands if gone (openapi.bnf.fr take/release, one at a time >= 3 s, at most 6 requests). Unit = one look. 3. `gsplit.py check3`
on the full material: pooled recall/precision/F1 vs 200 label-shuffled nulls, per-fold spread; the registered verdict (PASS only with the
r sample complete, i.e. every target cut whole or logged unsure/none). 4. PASS -> the f.191r step as VIV-GSPLIT Addendum A on HAND-CUT
f.191r g tiles (the 28 tileable + any the map missed; cut by eye, same log, within the remaining looks), `f191.py --override ... --tag
gsplit3 --stats`, (a) strict and (b) letter-S; if the looks run out before f.191r, stop and say so (the f.191r step is then its own job).
FAIL -> log; the family is [retired] for this instrument absent new material. 5. Price: vision calls: 9 x USD 0.45 = 4.05 (about 7 looks for
66 tiles with checks + 2 for f.191r/contact sheets); cap 4.5. 6. NOTES "## VIV-GSPLIT3C (<date -u>)", HYPOTHESES row, requests per host,
`f191.py --check` passes, shrink guard, commit by path, pull --rebase, push; done line: N_r reached, gate numbers, verdict, f.191r strict run
before/after if run.

## JOB VIV-GSPLIT3D (wave 9d, 15 Oct 2026 09:0x UTC by date -u; account-4 parent) -- the f.191r step of the hand-cut g-split (licensed by VIV-GSPLIT3C's registered PASS)

Model: Opus 5.5. Cap USD 3.5 (Opus floor 2.5). Box 40 minutes from the claim; stop before any unit that would cross 80% of cap or box.
Why: PREREG-VIVGSPLIT3 (+ Addenda A, B) passed on the complete hand-cut sample (NOTES "VIV-GSPLIT3C": recall 0.833, precision 0.750, F1 0.789
vs null 0.400). Its step 4 -- apply the five-leaf model to f.191r's g tokens -- is licensed and was not run (looks exhausted). This is that
step only. Measurement only: no key.tsv, reading or status.json edit; the verifier decides any row.
Steps: 1. room --start, claim; PREREG-VIVGSPLIT3 Addendum C pushed first: this job runs step 4 exactly as VIV-GSPLIT Addendum A registered it,
on HAND-CUT f.191r g tiles; the decision stays s.5 of PREREG-VIVPACKET3 (a stretch >= 42 all-H with no liberty -> verifier; else logged); (b)
letter-S is reported as what a verified key row WOULD give, never as the result. 2. Hand-cut the f.191r g tiles: the 116 g tokens of
tx/viv63_f191/rec.tsv (the 28 the map tiled + the rest), by eye on the VIV-F191 line crops (regenerate with the committed command; openapi
take/release, <= 3 requests), 2 looks per 20 tiles with check, logged in tx/vivgsplit3/boxes_handcut_f191r.tsv (whole/unsure/none); cut as
many as the looks allow, g tokens on L08-L16 and L29-L32 FIRST (the lines that carry the best runs), and say how many were cut. 3. Classify
with the full five-leaf hand-cut model (gsplit.py, the 3C material); write tx/sorter_f191/gsplit_override_2026-10-15.tsv (owner_override
format, new_sign 'gf', action classifier-f, plus a `letter` column = f) for predicted-f positions; `f191.py --override ... --tag gsplit3
--stats` (a) strict (gf outside the key -> U) and (b) with the letter column (extend apply_override minimally: new_sign not in key + letter
given -> that letter, grade 'S'; report the longest H-or-S run beside the strict one). 4. Price: vision calls: 7 x USD 0.45 = 3.15 (about 6
looks for 60 tiles with checks + 1 contact sheet); cap 3.5. 5. NOTES "## VIV-GSPLIT3D (<date -u>)": tiles cut, positions predicted f (list by
line:pos with the current sign and letter), (a) and (b) tables with the controls, requests per host; HYPOTHESES row; `f191.py --check`
passes; shrink guard; commit by path, pull --rebase, push; done line: predicted-f count first, then strict run before/after, then (b).

## JOB VIV-GSPLIT3E (wave 9e, 15 Oct 2026 10:1x UTC by date -u; account-4 parent) -- classify the hand-cut f.191r g tiles with the registered five-leaf model (no looks)

Model: Opus 5.5. Cap USD 3 (Opus floor 2.5). Box 35 minutes from the claim. No vision looks: the tiles are already cut (VIV-GSPLIT3D:
tx/vivgsplit3/boxes_handcut_f191r.tsv, 63 whole). Price: vision calls: 0 x USD 0 = 0.
Why: VIV-GSPLIT3D cut the tiles but could not classify them because the five-leaf training crops and the vivcls atlas live in no container
(4 canvases over its request cap). This job rebuilds them and runs the registered step 4 (PREREG-VIVGSPLIT3 Addendum C stands; add Addendum
D naming this run and the request budget before any fetch). Measurement only.
Steps: 1. room --start, claim; Addendum D pushed. 2. Rebuild: regenerate the five-leaf line crops and the vivcls atlas with the committed
commands (NOTES "VIV-GSPLIT3C" / "VIV-CLS" / images manifest "vivcls"; openapi.bnf.fr take/release lines, one at a time >= 3 s, at most 6
requests: f206, f207, f216, f217 + the f.191r canvas c196 and one spare); verify material.tsv byte-identical to 3C's where it overlaps.
3. `gsplit.py` step 4 on the 63 whole f.191r tiles (and the 9 unsure reported separately): write tx/sorter_f191/gsplit_override_2026-10-15.tsv
(owner_override format, new_sign 'gf', action classifier-f, column letter = f) for predicted-f positions; list them by line:pos with the
committed sign and letter and their nearest training tiles. 4. `f191.py --override ... --tag gsplit3 --stats` (a) strict and (b) letter-S
(extend apply_override minimally: new_sign not in key + letter -> that letter, grade 'S'; report the longest H-or-S run beside the strict
one); controls C1/C2 as the script runs them. 5. NOTES "## VIV-GSPLIT3E (<date -u>)", HYPOTHESES row, requests per host, `f191.py --check`
passes, shrink guard, commit by path, pull --rebase, push; done line: predicted-f count first, strict run before/after, then (b).
