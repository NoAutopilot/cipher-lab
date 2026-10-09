# TXP-AGREE (LANE TX-ENGINEER-2 round 0d: error map with reader agreement on errors; read-free; Opus 5.5; cap 4; box 50 min, 80% at 40)

For LANE TX-ENGINEER-2 (account 4, session_01NmaB9fhuaMSMYexV4NaVsR). Written 9 Oct 2026 15:1x UTC by date -u.
PREREG `benchmark-tx/PREREG-txeng2-0.md` section 0d. First: `git fetch origin && git checkout -B main origin/main`; `export
CIPHERLAB_ACCOUNT=account-4`; `python3 tools/room.py --start`; ROOM.md last 30 lines; claim with `python3 tools/room.py
"TXP-AGREE worker (account 4, Opus)" "claim ..." --push`. Read `tools/tx_taxonomy.py` (docstring + code), `tools/tests/
test_tx_taxonomy.py`, `research/TX-TAXONOMY-2026-10-09.md`, `research/TX-ENGINEER-2026-10-09.md` "Open" item and the close-out
lesson in STATUS.md "LANE TX-ENGINEER handoff" ("a round-1 taxonomy that measures reader agreement on errors ... would have
retired the compare, rendering and ordering families after one run each"). No vision call, no reader, no image: scripts only.

## Job
1. Extend `tools/tx_taxonomy.py` with an agreement measure per scored position, computed from the passes given with `--pass`
   (the first `--pass` is the baseline): new per-position columns `n_pass_wrong` (how many passes are wrong there), `n_same_wrong`
   (how many read the same wrong sign as the baseline, deleted counted as its own sign) and `agree_class` in {`all-same-wrong`
   (every pass wrong with the baseline's sign), `all-wrong-split` (every pass wrong, signs differ), `majority-wrong`,
   `baseline-only`, `right`}; and a summary table in the --md output: for the baseline's errors, the share in each agree_class,
   crossed with the existing error class (look-alike pair / crop / thin / other) and with the top (truth <- read) pairs. Keep
   every existing column and output byte-identical when the new columns are ignored (the existing test must still pass); add a
   test for the new columns in `tools/tests/test_tx_taxonomy.py` (a 3-pass toy with one all-same-wrong, one split, one
   baseline-only position). `--help` updated; SYSTEM.md row of tx_taxonomy.py amended (system_map_check passes); shelf row
   `evidence` cell amended.
2. Run it on every pool item with every pass on disk (baseline first, then the others; presentations count as passes):
   - birago1572-no87: baseline L = benchmark-tx/outputs/birago1572-no87/labels.tsv, then passA, passB, passC, passE_sheet,
     passF_fable, the views (outputs/birago1572-no87/views/*), passK2_sr4_dev_tune, passV_s0_dev_tune, passT_* (dev lines only
     for the dev_tune-restricted passes: tx_taxonomy scores only covered lines, so pass them as they are and say which lines
     each covers); `--boxes atlas/signs.tsv --box-token atlas/no87_box_token.tsv --harvest harvest` from
     ciphers/nevers-birago-fr3251-1572 as the taxonomy did (its docstring commands).
   - spinelli-c1519-confirm: baseline passZ_pipeline.tsv, then passA_txeq, passB_txeq (outputs/spinelli-c1519-confirm/), with
     `--label-map benchmark-tx/txeng/confirm/collapse_map.tsv`.
   - dint-f128-print: baseline passB, then passA, passF_fable, `--label-map benchmark-tx/dint128_label_map.tsv`.
   - ceppo-f87-S: baseline passC, then passA, passB, passF_fable; ceppo-f36v-gloss: baseline recon, then passA, passB, passD,
     passF_fable.
   Outputs to `benchmark-tx/txeng2/errormap/<item>_positions.tsv` and `<item>_summary.md`.
3. Write `benchmark-tx/txeng2/ERRORMAP-2026-10-09.md`: per pool (eval = eval_heldout lines of no.87 + spinelli; dev = dev_tune
   lines + dint + f87 + f36v) the baseline errors by agree_class (counts and shares), the top three error classes with mass,
   the top ten (truth <- read) pairs with their agree_class, and one paragraph: which classes are "every reader, every
   presentation" (not to be re-attacked by a presentation change) and which are reader-split (where a second look can help).
   State the pool's error count per split as the register's starting numbers.
4. Commit by path, push, ROOM done line "for LANE TX-ENGINEER-2": eval/dev pool errors, share all-same-wrong per pool, top
   three classes, "cost: the orchestrator get_session reading".

Stop at 80% of cap or box with what exists committed. Never a vision call; never AskUserQuestion. + `.claude/briefs/README.md`
common tail.
