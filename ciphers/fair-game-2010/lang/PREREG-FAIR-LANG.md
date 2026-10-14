# PREREG-FAIR-LANG (account 4, LANE DEFAULT-A4-2135-14, 14 Oct 2026, written 22:1x UTC before any score)

Question: FAIR-TRANS's G0 put the 67 marks' letter counts below p01 of English 67-letter windows. Is there a
language with a corpus in tools/data (every `LANG_CORPORA` key in tools/judge_plaintext.py, 34 keys) whose letter
counts the marks fit, and does a pure transposition of that language read?

L0 (letter-count rank, `lang_rank.py`, `--check`): per language key, the target's mean log unigram probability
(letters folded to a-z by NFKD, add-0.5 smoothing over 26) ranked among 2000 word-start windows of N=67 from that
key's corpus (tools/families/transposition.word_window, seeds 1-2000). Target = test2/order_scroll.txt (as G0).
Order does not matter for L0 (column order is a permutation). Recorded: pct_rank, p01, p05, median.
  - pct_rank < 0.01: letter counts exclude a pure transposition of that language at p01; no family run.
  - pct_rank >= 0.01: the language goes to L1.
L1 (transposition --langs): `tools/family_run.py specs/fair-game-2010.json --family transposition --langs <L1 set>`
on trans/scroll68.txt and trans/column68.txt (the FAIR-TRANS inputs, N=68 with the ? masked), same settings as
FAIR-TRANS's standard search (restarts 4, gate 0.80, 28 control designs per language from that language's corpus).
A language whose control misses 0.80 is CONTROL BELOW GATE (not a negative). A target decode counts only if the
judge in its own language PASSes (margin >= 0 and above null_p99) AND its quadgram score sits above its own
shuffle floor (5 shuffles of scroll68 in that language, same search); otherwise negative for that language.
If more than 8 languages qualify for L1, run the 8 with the highest L0 pct_rank first and log the rest as next
step (box 45 min, cap 2.5).
