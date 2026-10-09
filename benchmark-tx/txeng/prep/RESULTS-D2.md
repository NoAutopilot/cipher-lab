# TXE-D2: one blind read at 4x (LANE TX-ENGINEER, idea M4 read; 9 Oct 2026, account 4, Opus 5.5)

**Verdict: FAIL on dev, so no eval look was spent.** On dev_tune (343 scored signs) the 4x read scores err_true 0.067
(23/343). Against pass A (0.070, 23/343) it fixed 9 signs and broke 8: the sign test gives p = 1.0, and the registered gate
is p < 0.01. Against L (0.041) it fixed 3 and broke 11, p = 0.057. TXE-D's proxy near-miss (atlas top-1 9/1, p 0.02) does
not carry over to the reader. Looks taken by this instrument on eval_heldout: 0.

PREREG: `benchmark-tx/txeng/prep/PREREG-D2.md`, commit b4e6a3edd, pushed 07:44 UTC by date -u, before any read. Raw reads
were committed before scoring: f69282796 (L01-03, L07-09, L10-12) and 97e124e6e (L04-06).

## Rendering
    python3 tools/tx_prep.py lines --crops ciphers/nevers-birago-fr3251-1572/harvest/f178v --setting sr4 --segments 4 \
        --overlap 200 --only f178v_L01_ ... --only f178v_L12_ --out <scratch>/sr4dev
That makes 144 crops of 1400 px, at LANCZOS 4x of the 36 dev_tune line crops. Each 5000 px crop was cut into four q-segments
that share 200 px (50 native). The crops are regenerable, so they were not committed. `--segments` is a new option with a
test in tools/tests/test_tx_prep.py.

The brief asked for 1250 px segments; they are 1400 px instead, logged in the PREREG before the read, because four 1250 px
pieces sharing 200 px would cover only 4400 of the 5000 px. Two things changed at once: the scale went from 2x to 4x, and the
segments per line went from 3 to 12. A null result cannot be pinned on the scale alone.

## Score (tx_bench)
```
birago1572-no87 [eval] err_true 0.067 (23/343) 95% 0.045-0.099 | wrong 22 deleted 0 inserted 1 | excluded 11 | lines missing 17
  top confusions (truth value <- read): e<-T76 x3, l<-T65 x2, s<-X_NEW x2, s<-T50 x2, d<-T98 x1, g<-T42 x1, e<-T36 x1, t<-T90 x1
paired passK2_sr4_dev_tune.tsv vs passA_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 23, output wrong 22; fixed 9, broken 8; sign test p = 1.0000
paired passK2_sr4_dev_tune.tsv vs labels_dev_tune.tsv on birago1572-no87: 343 common scored signs; base wrong 14, output wrong 22; fixed 3, broken 11; sign test p = 0.0574
```

## Joins
The readers de-duplicated the overlaps themselves, as pass A's reader did. Line lengths match pass A on 11 of 12 lines. The
exception is L06, with 29 signs against A's 30. No reader row's note flags an overlap or duplicate doubt, so the count of
ambiguous joins is 0. tx_bench counts 0 deletions and 1 insertion over the unit.

## Taxonomy (`tools/tx_taxonomy.py`, A vs K2 vs L; `taxonomy_D2.tsv`, `taxonomy_D2.md`)
| stroke tercile | A wrong | K2 wrong | L wrong |
|---|---|---|---|
| thin | 12 | 10 | 6 |
| mid | 4 | 3 | 4 |
| heavy | 7 | 9 | 4 |

TXE-D predicted that the thin tercile would not move. It moved slightly the right way (12 -> 10), and heavy moved the wrong
way (7 -> 9). The proxy had found the opposite pattern, with its gains in heavy and mid. Both movements are within noise at
these counts. Band-cut positions got worse (5 -> 8 wrong) and in-band positions got better (18 -> 12). Overlap-zone errors
went from 4 to 5.

## Reader task text
The task text is in full in `reader_task_D2_L01-03.md`; the other three calls differ only in line numbers and paths. It is the
unchanged `harvest/blind_pass_brief_1572.md`, followed by the generated `crops_note_D2.md`, the sheet path, 36 crop paths and
the output path. Each subagent was told only to read that task file and follow it.

## Calls and cost
4 blind Opus 5.5 vision calls on dev and 0 on eval, run 07:43-07:49 UTC by date -u. For cost, see the lane's get_session.

## Follow-up (one line, not started)
- To separate scale from segmentation, a 4x read at 3 segments per line would need crops of about 2000 px each. That is
  allowed under 2500 px, but it is a new instrument run, and at p = 1.0 it is unlikely to be worth a read.
