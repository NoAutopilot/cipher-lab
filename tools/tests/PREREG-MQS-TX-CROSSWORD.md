# PREREG MQS-TX-CROSSWORD (9 Oct 2026, 06:5x UTC by date -u; LANE MQS-2, account 4)

Brief `.claude/briefs/runs/2026-10-09-ytbiz-mqs-next-tx-crossword.md` (research/MARY-STUART-TALK-2026-10-09.tsv row M33, "an
iterative transcribe-and-decode loop in which the decipherment corrects the transcription"; Lasry, Biermann and Tomokiyo 2023,
Cryptologia 47:2). Written and pushed **before any crop is shown to any reader and before any score**. Files:
`benchmark-tx/txcross/` (flag.py, score.py, positions.tsv, blind_G1/G2.tsv, orient_G1/G2.txt; later answers, RESULTS.md).

## Why this is not a fourth tuning of the same knob (rule 3, third-attempt clause)
TX-DECODE, TXD-HOLDOUT and TX-ALTS re-picked among signs some reader had already proposed; they are capped by truth-in-lattice
(27/97, 12/35). TX-AGREEAUDIT (4 Oct) re-read with k=3 confusion partners and was capped the same way (8/26 agreed-wrong signs had
the truth among the candidates). This job changes the instrument on both ends:
1. **Flags come from the decipherment, not from reader disagreement.** `flag.py` decodes the base reading (labels.tsv, err_true
   0.045) through the printed 1572 key and flags the 60 positions where the it16dip LM most prefers some other one-sign letter
   (gain over current, (n-1) left + 4 right chars). An agreed-wrong sign that no reader doubted can be flagged.
2. **The re-read is open-choice per sign against the whole printed-key sign sheet** (`harvest/sign_sheet_blind_1572.png`, ids
   only), the BIR-OPEN instrument (3 Oct, f.117r/f.168/f.144r, never run against a known answer). The reader is shown no
   candidate, no value, no key, no flag reason; it can return any sheet id, OTHER or U. So a value no reader ever proposed is
   reachable. No.87's truth file is not read by flag.py, the packets or the reader.
3. The two signals are ANDed (score.py): a T position changes only if the reader names a different single-letter key sign at
   conf H/M **and** that sign's letter scores above the current one in the LM window. Key values are never changed, so
   `decode_key.py --try` (letter values only, per MQS-CROSSWORD) has nothing to test here and is not run; no word value is used.

## Arms (seed 20261009, fixed in positions.tsv before any read)
T 60 crossword flags; D 30 calibration decoys (LM gain <= 0); R 20 random unflagged positions (null arm, same reader and same
rule). All 110 interleaved, masked alike as [qid] in the orientation (base labels elsewhere). Why R can fail differently from T:
the statistic is truth-fixing changes per arm, and R differs from T exactly in the flagging step under test.

## Reader (2 vision calls, Sonnet subagents, scratchpad crops only)
Crops cut before the first call by `tools/iiif_lines.py --image` from the committed native regions (boxes reproduce the committed
crop manifests exactly after the region offset; commands in RESULTS.md). G1 = f178r, f179r, f178v L01-10 (59 questions); G2 = f178v
L11-23 (51). Each call gets crop paths, the sign sheet, its blind_*.tsv and orient_*.txt only. Price: 2 reader units + 1
reconciliation/eye-check unit (me).

## Gate (all on tools/tx_bench.py, BENCHMARK-TX eval item birago1572-no87, 803 scored signs)
- G0 calibration: D answered == current sign >= 0.80 (24/30). Miss -> NON-TEST, nothing applied.
- G1 err_true(applied_T) < 0.045 strictly, i.e. at most 35/803 wrong (base labels.tsv 36/803).
- G2 `tx_bench --paired labels.tsv applied_T.tsv`: fixed > broken and sign test p < 0.05.
- G3 eye check: I look at the crop of every changed sign before scoring and list agree/disagree in RESULTS.md; a change I
  disagree with is reverted before tx_bench runs (logged with its qid). Done before any tx_bench call on applied files.
- G4 second held-out item: **none exists on disk** -- BENCHMARK-TX.tsv's only eval item is no.87; the other items are dev and
  other key families (Ceppo, Dinteville) and their S truths are not independent of their committed reads. So G4 cannot be met in
  this job: a G0-G3 pass ships the method on tools/data/tool_shelf.tsv as `weak` ("no.87 only"), names the second item as the
  next step, and is not adopted into any reading. A G0-G3 miss ships `weak` with both numbers and is logged
  "untested-by-this-tool / not supported" per rule 3; not re-briefed against no.87.
- Reported, not gated: applied_R (null arm) fixed/broken; applied_Timg (image only, no LM AND) fixed/broken; per-arm change
  rates; truth-in-reach is not computed (truth stays unread until tx_bench).
- Ceiling check: base 0.045 is not near ceiling (95.5% right; 36 errors of headroom).

No status, key, reading or AUDIT.md change; Birago 1572 family: nothing value-bearing rendered for the owner (ASKS 118); no host.
