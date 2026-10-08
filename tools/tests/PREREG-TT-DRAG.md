# PREREG TT-DRAG -- `tools/running_key.py --drag` known-answer controls (written before any control ran)

Written 8 Oct 2026 22:48 UTC (date -u), worker TT-DRAG for LANE TOOLS-TOMO (account 4). Pushed before the controls run.
Method: Tomokiyo, runningkey.htm ("Tips"; "Running Key Challenge" / "Solution": Matthew Brown's dictionary attack, words of
length >= 10, quadgram fitness on the revealed other side, then manual extension). A row is a TRUE placement when the dragged
word equals the true plaintext or the true key at exactly that offset (either side: under vig the two are symmetric).

## Control A -- synthetic, matched to hessen-1824 (N=164, German, de19, vig, book key)
Build: word-aligned windows of 164 letters, plaintext from one de19 book and key from a DIFFERENT de19 book (random start per seed),
vig. Scoring LM: order 4 (quadgram), trained on de19 books other than the two used (book held out). Dictionary: de19 word types of
>= 10 letters (all three books -- a dictionary is assumed to contain the words). Seeds 1-8 (>= 5 required).
- PASS line: a true placement in the top 10 in >= 5 of 8 seeds AND mean hits@10 >= 1.0.
- NULL A: identical plaintext windows enciphered with a uniform RANDOM key (no language on the key side), same drag. The planted
  plaintext words still sit at the same offsets, so the statistic (rank of the true word) can move only through the key side's
  language structure -- the null can fail differently from the control. NULL passes (i.e. collapses as required) if a true
  placement reaches the top 10 in <= 2 of 8 seeds and mean hits@10 <= 0.3.

## Control B -- Tomokiyo's own case: Brown's 2026 running-key challenge (runningkey.htm, 1000 letters, English, vig)
Ciphertext and Brown's 207-letter partial plaintext + key copied from sources/cryptiana/web/runningkey.htm (read, not edited).
Dictionary: English word types >= 10 letters from tools/data en sources (pg1661, pg2701, tools/data/en/*); LM order 4 on the same.
Truth known only inside Brown's 207-letter window; rows outside it are unknown, not false.
- PASS line: at least one true placement inside the window ranks in the overall top 20 (run as if unsolved, all 1000 letters).
- NULL B: the same ciphertext with its letter ORDER shuffled (seeds 1-5) scored against the same truth window. Shuffling changes
  which fragment each offset yields, so the true-word ranks can collapse -- this null can differ. NULL collapses if no seed puts a
  true placement in the top 20.

Grade on the shelf: `proven` only if A and B both pass and both nulls collapse; `controlled-only` if A passes and B fails or B is
not runnable; `weak` ("controlled-only: failed ...") if A fails.

## Addendum, 8 Oct 2026 22:55 UTC (date -u) -- written after Control B ran, before B2 runs
Control B result (pre-registered line above): FAIL -- the first true in-window placement ranks 272 (pass line: top 20); the
shuffled null collapses (no true placement in any kept list, seeds 1-5). Diagnosis: only ONE word of the English dictionary
(4,910 types of >= 10 letters from five novels) occurs anywhere in Brown's 207-letter truth window ("calculated", plaintext
offset 328, at the window's end) -- B tested the dictionary's coverage as much as the drag. This FAIL stands as B's result.
Observation not pre-registered, reported as such: rank 1 overall is communicating / yinterviewwit at offset 7, one of the four
pairs Brown published (runningkey.htm "Solution"); it lies outside the 207-letter window, so it is not counted as a hit.
- B2 (pre-registered here, before it runs): identical to B except the dictionary adds the word types of tools/data/en18
  (Madison/Jefferson/Gallatin writings, period diplomatic register). LM unchanged (en only). PASS line: a true in-window
  placement in the top 20. NULL: shuffled order, seeds 1-5, collapses if none in the top 20. The shelf grade follows B2 only if
  it passes; otherwise B's FAIL decides and the grade is `controlled-only`.

## Results (8 Oct 2026, 23:00 UTC by date -u; files tools/tests/ttdrag/controlA.tsv, controlB.tsv, controlB2.tsv)
- A: PASS. True word in top 10 in 7/8 seeds (seed 7: first true rank 31), mean hits@10 3.75 (30/80). NULL A collapses: 0/8, mean 0.
- B: FAIL (first true in-window rank 272 > 20). NULL B collapses: 0/5.
- B2: FAIL (first true in-window rank 381; three window words now in the dictionary: correcting@136, ambassador@273 (key),
  calculated@328). NULL collapses: 0/5. Not pre-registered, reported only: Brown's published pairs communicating/yinterviewwit
  (rank 1 in B, 3 in B2) and transmission/hatitwasesse (rank 16 in B2) come out at the top; both lie outside the 207-letter window.
- Grade: `controlled-only` (A passes, the Tomokiyo case's pre-registered line fails).
