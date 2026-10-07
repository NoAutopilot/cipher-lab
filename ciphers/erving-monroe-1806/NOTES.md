Status: open

# George W. Erving to James Monroe, Lisbon 23 May 1806 -- coded passage in WE028

Status `open` until a check-solved verdict (`.claude/workflows/check-solved.js`) and `tools/intake_gate_check.py
erving-monroe-1806` (with its "## Premise check") are run; both are the **next step before any deep work** (CLAUDE.md
Pipeline 2). Found 7 Oct 2026 by KH4-D (LANE KH-4, account 4, KEYHUNT row 68, key `tools/data/uscodes-1800/WE028.tsv`).

## Source (image over transcription: read from the image)
- Library of Congress, James Monroe Papers (mss33217), Series 1, reel 3 (item mss33217003), frames 0828-0830:
  `https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0800:0828` (p.1, headed "Lisbon 23 May 1806"),
  `...:0829` (pp.2-3; signed "George W Erving"; coded lines 1-5 of the right page), `...:0830` (not looked at beyond the
  contact sheet). Native 4234x2824 for frame 0829.
- 1904 LOC *Calendar of the Papers of James Monroe* (IA cu31924029594037, OCR line "23. George William Erving to Monroe."
  under May 1806) lists it; the calendar does not flag cipher.
- Context (from the clear text, read by this worker at pct:30, not transcribed): Erving had embarked at Falmouth on the
  13th and reached Lisbon on the 21st; news from the United States to 3 April; the Randolph schism; the Massachusetts
  election (Sullivan, Strong, district of Maine).

## Ciphertext and reading
`ciphertext.txt` (34 groups, five lines), two blind Sonnet passes on the line crops in `images/` (`tools/iiif_lines.py`
command below), `passA.tsv`/`passB.tsv`, agreement 33/33 on the groups both read (`tools/reconcile_passes.py`,
`agreement.tsv`). `decode.py [--check]` (rule 7) writes `reading.txt` and `reading_letters.txt`. Grades: H 0, C 0, S 29,
M 4, I 1 of 34 -- a **cryptanalytic result** in rule 4's sense (no H or C): WE028 is a modern transcription of the period
table (Tomokiyo's `WE028.txt`), and no period gloss for this letter was found.

Clear words in the manuscript between the runs are given in brackets; the decoded groups are in capitals:
> [Randolph asked] WHEN MISTER MONROE WOULD RETURN HOME -- THE PRESIDENT [answered] NOT UNTIL HIS SUCCESSOR ARRIVES.
> [the other bluntly observed that he] MISTER MON[ROE] WOULD BE THE NEXT PRESIDENT.

(L04's middle group is overwritten in the manuscript with "137" interlined; read 1379 = ter, grade I. Its last group 146
is at the crop edge, grade M. L05 runs on from L04: "mon | ro E would be ...".) The left page of frame 0829 carries two more
groups in running text, "a conversation of Randolph with 78" with "1385" interlined above (= "with the president", M, one
reader) -- not transcribed by the passes, not counted.

Crop command (pasted, Usage 6):
`python3 tools/iiif_lines.py 'https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0800:0829' --out <scratch>/crop --region 2120,80,2060,580 --prefix f829 --debug`
-> 6 lines, pitch 97; L01-L05 used.

## Matched control (rule 3) and judge (rule 7)
`control.py` (output `control.json`): the same 34 groups under 200 shuffled WE028 keys (plaintext values permuted over the
1600 codes). A shuffled key changes both statistics, so the control can fail differently from the target.
- en18 4-gram score: **real -0.723 vs shuffle mean -1.296, p95 -1.087, max -0.971** (0 of 200 reach the real score).
- greedy word cover: real 0.971 vs shuffle mean 0.865, p95 0.941, max 0.972 -- this statistic barely separates at 105
  letters (1 of 200 shuffles reaches it); reported, not relied on.

`python3 tools/judge_plaintext.py specs/erving-monroe-1806.json --file ciphers/erving-monroe-1806/reading_letters.txt`:
```
ok   length: got=105, min=50, max=400
ok   language: score=-0.723, null_p99=-1.986, real_p05=-0.877, real_median=-0.738, mode=both, N=105
PASS - erving-monroe-1806 (a PASS is a gate for a verifier, not a reading; rule 10)
```
en18's fold spread was measured at N=1000/1500, not at 105 letters: a PASS of unknown reliability at this length (rule 3);
the shuffled-key control above is the stronger evidence.

## What was searched (7 Oct 2026) and where it was not found -- not a check-solved verdict
- Founders Online (headless Chromium): the Madison Papers print the WE028 passages of Erving's and Monroe's letters **to
  Madison** decoded by the editors; this letter is to Monroe and is not in the Madison Papers. Not searched: Founders for
  this letter's date by name (it would only appear in a Monroe edition).
- `sources/cryptiana/web/state.htm` (Tomokiyo's WE028 page): lists Madison-Monroe letters only; no Erving-Monroe item.
- `sources/cyphersolver/`, `sources/decode/`, `sources/solver-diffs/`: no Erving item (grep "erving").
- Not reached: *The Papers of James Monroe* vol. 5 (Preston, 2014; Google Books NO_PAGES and Rotunda subscription per
  armstrong-madison-1808 ARM-KEYHUNT-2) -- the edition most likely to print or calendar this letter; Aymeloglu's
  repository (not cloned here); a phrase search. These are check-solved's job.
- Related known item: Erving to Monroe, Madrid 5 Feb 1806 (reel 3 frames 740-744, WE028 with a period interlinear
  decode), read in ciphers/armstrong-madison-1808 H25/H29 -- the same channel; not this letter.

Report what was found and where it was not found; novelty is a verifier's call (rule 10).
