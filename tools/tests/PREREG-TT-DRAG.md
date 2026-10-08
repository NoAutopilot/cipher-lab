# PREREG TT-DRAG -- `tools/running_key.py --drag` known-answer controls (written before any control ran)

Written 8 Oct 2026 ~22:58 UTC (date -u), worker TT-DRAG for LANE TOOLS-TOMO (account 4). Pushed before the controls run.
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
