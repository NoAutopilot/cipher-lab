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
Price: disk-only Opus, floor 2.5; dev 2 folds x 4 lam + confirm + ink 63 (9 pages) are script runs, under a minute each; cap 6.
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
Price: 2 + 4 Sonnet subagent calls (~1.4 each per README) + the worker's own reconciliation (one unit each for f.201r and the
decipherment, bMALS rule) + alignment scripts: 8 units x 1.4 = 11.2 -> cap 12; stop before starting a unit that would cross 80% of
cap or box. If f.201r's cipher block is short (under 15 lines), add f.201v as the second page only if under 50% of the cap.
Done line: alignment share vs shuffled p95 first, then err_2reader, the unkeyed-label table's totals, and whether the truth item
was registered.
