# TXP-GLOSS jobs (LANE TX-ENGINEER-2 round 0b item 1: BENCHMARK-TX items from the glossed Nevers-office 1590s leaves; Opus 5.5; one leaf per worker)

For LANE TX-ENGINEER-2 (account 4, session_01NmaB9fhuaMSMYexV4NaVsR). Written 9 Oct 2026 15:5x UTC by date -u. PREREG
`benchmark-tx/PREREG-txeng2-0.md` 0b + Amendment 1 (binding: split, truth recipe, gloss masking). First: `git fetch origin &&
git checkout -B main origin/main`; `export CIPHERLAB_ACCOUNT=account-4`; `python3 tools/room.py --start`; ROOM.md last 30 lines;
claim with `python3 tools/room.py "<JOB> worker (account 4, Opus)" "claim ..." --push`. Read TRANSCRIPTION.md, CLAUDE.md Usage 6,
`benchmark-tx/txeng2/decode-scout-2026-10-09.md` (your leaf's row), `benchmark-tx/txeng2/f152r/RESULTS.md` (the order of
operations, worked example), `benchmark-tx/build_dint128.py` + `benchmark-tx/PREREG-dint128.md` (the recipe), `ciphers/fr3621-
dinteville-1592/f128/pass_instructions.md` (the Dinteville reader vocabulary) and `f128/print_align/` (key_print.tsv, align_print.py).

| job | item id | leaf | page file (sources/decode/nevers-1590s-2026-10-09/) | lines (scout) | split | key check | cap | box |
|---|---|---|---|---|---|---|---|---|
| TXP-D89 | dint-f89-gloss | fr.3619 f.89 (DECODE 9440, Dinteville, Nov 1591) | IMG_R9440_I44624_P.jpg | ~17 cipher lines + PS, ~750 signs | dev | key_print.tsv | 15 | 120 min |
| TXP-D98 | dint-f98v-gloss | fr.3619 f.98v (DECODE 9441 P2) | IMG_R9441_I44625_P2.jpg | 6 lines, ~270 signs | dev | key_print.tsv | 9 | 90 min |
| TXP-D113 | dint-f113-gloss | fr.3619 f.113 (DECODE 9443) | IMG_R9443_I44629_P.jpg | 4 lines, ~180 signs | dev | key_print.tsv | 8 | 90 min |
| TXP-B23 | bir1591-f23r-gloss | fr.3623 f.23r (DECODE 9452, Italian, Birago-style symbols, signed Dinteville) | IMG_R9452_I44643_P.jpg (crops already on disk: ciphers/fr3621-dinteville-1592/f3623/f23r_L??_s?.jpg, check their source and resolution first) | 9 lines, ~400 signs | eval | none (rebuild only) | 10 | 100 min |

Images: the DECODE copies on disk (Gallica is 403 today; fr.3619 is 1653 px wide, near-native for DECODE's copy; the manifest
says how to refetch). Record in the item's notes the pixel size used.

## Order (binding; the cipher reads are committed BEFORE any gloss is read or any truth built)
1. **Crops, pasted.** `python3 tools/iiif_lines.py --image <page file> --out benchmark-tx/txeng2/<item>/crops --prefix <leaf>
   --max-width 1250 --overlap 300 --band-extent 0.1 --mask-neighbours --overlap-note --debug` (tune `--distance`/`--prominence`
   or give `--centres` so that EVERY gloss row is detected as its own line and every cipher line as its own; then cut ONLY the
   cipher lines (`--only-lines`), so the interlinear gloss is masked out as a neighbour line). Open the debug overlay and two
   crops yourself: if gloss letters remain legible inside a cipher crop, re-cut with a tighter band; if they cannot be removed,
   write `gloss-visible` in the BENCHMARK-TX notes (Amendment 1) and say so in the done line. Paste the final command and
   crops_note.md in RESULTS.md. One subagent call per <= 8 cipher lines (Usage 6: never a whole 750-sign page in one call).
2. **Two blind cipher passes**, two Opus 5.5 subagents (`model: opus`), given ONLY the crop paths, the vocabulary block of
   `f128/pass_instructions.md` (its sign label table; drop every sentence about the gloss) for the Dinteville leaves, or for
   TXP-B23 a value-blind instruction to label signs by shape with a short NEW:<description> for anything not in a seed list
   you draw from the scout's row (∓ Δ ∇ ψ # o □ ¢ z 3 ...), and the output path `benchmark-tx/txeng2/<item>/passA.tsv` /
   `passB.tsv` (header passage pos sign_id alt conf note). They open nothing else. Commit each pass as it lands.
3. `tools/reconcile_passes.py passA.tsv passB.tsv --crops <crops>`; settle disagreements.tsv + uncertain.tsv with ONE Sonnet
   subagent from the crops (the folder's third-reader protocol, `benchmark-tx/txeng/confirm/adjud_task.txt` as the worked
   example); write `passZ_pipeline.tsv` (line pos sign; line ids <leaf>_L01..). Commit passZ BEFORE step 4.
4. **Gloss read**: cut gloss-row crops the same way (`--only-lines` on the gloss rows, a wider band), two blind Opus passes of the
   clear text (one line of letters per cipher line, words separated, `+`/`|`/`?` where the decipherer left a sign unexpanded or
   the word is unreadable), reconciled by difflib + one Sonnet look at the splits; `gloss.tsv` (line, text, conf). Commit.
5. **Truth build** `benchmark-tx/build_<item>.py` (`--check`): align gloss.tsv to passZ's sign sequence per line with
   `tools/interlinear_align.py` (the settings of `f128/print_align/align_print.py`); from the alignment rebuild the leaf's key
   (sign -> letter, count, agree share); a position is `scored` only when its aligned chunk is one letter, that letter is the
   sign's majority value with count >= 2 and agree >= 0.75 on this leaf, and (Dinteville leaves) agrees with key_print.tsv when
   the sign is in it; everything else excluded with its class (unaligned, multi-letter, low-agree, key-conflict, gloss-unread,
   off-sheet NEW/?); a `flag` column `align-conflict` where interlinear_align's own uncertainty says so. Control: the GAPS4
   statistic against 200 value-shuffled keys (as build_birago152.py prints). Write `benchmark-tx/<item>.truth.tsv` + `.sha256`, the
   BENCHMARK-TX.tsv row (split per the table; truth_source "period interlinear decipherment on the leaf (DECODE <rec>), key
   rebuilt from this leaf's alignment at agree >= 2 [+ key_print check]"; truth_grade C; notes: reference = passZ, home
   advantage; px size; gloss-visible or not), `benchmark-tx/outputs/<item>/{passA,passB,passZ_pipeline}.tsv`.
6. **Score** passZ, passA, passB with `tools/tx_bench.py ... --item <item>` (passZ scores 0 by construction on segmentation
   but NOT on identity: the truth is the gloss, so passZ's wrong-sign positions count -- state that); `tools/tx_power.py
   --unit <item>=<item>:...passZ_pipeline.tsv` for the unit's E; RESULTS.md with every count (positions, scored, excluded by
   class, err_true per output with CI, pair agreement, alignment control, key rows rebuilt and how many agree with key_print).
7. Commit by path, push; ROOM done line "for LANE TX-ENGINEER-2": scored / excluded, baseline errors (= the pool gain), gloss
   visible y/n, vision calls, "cost: the orchestrator get_session reading".

Price (per pass call ~1.5, Sonnet ~0.7): D89 = 2 passes x 3 calls + gloss 2 x 2 + adjudication 2 = 12 calls -> cap 15; D98 /
D113 = 2x1 + 2x1 + 1 = 5 calls -> cap 8-9; B23 = 2x2 + 2x2 + 1 = 9 -> cap 10. Stop before a unit that would cross 80% of cap or
box; commit what exists and say what is missing. Readers never see the gloss, the truth, another pass or any decode; never edit
a truth file by hand; never AskUserQuestion; stage by path; no Gallica fetch today. + `.claude/briefs/README.md` common tail.
