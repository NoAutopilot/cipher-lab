# DEB-SWARM-G: Portuguese, Spanish or Latin plaintext, homophonic letter substitution

Worker DEB-SWARM-G, 29 Sept 2026. Hypothesis: c1 and c2 are homophonic letter substitution over Portuguese (he is
reported born in Lisbon), Spanish or Latin. The attempts, controls and numbers are in `LOG.md`; this file says what
the tools are.

- `hsa.c` -- the annealer core (C; no numpy in the container). Score = sum of log P(x_i | three letters before), minus
  a KL term keeping the letter distribution near the corpus. Moves: re-key one sign, or swap two signs' letters.
  `HSA_PERTURB=p` makes every restart after the first start from the best key so far with a share p re-drawn
  (iterated local search; 0.2 is the setting used from 03:31 on). Build: `gcc -O3 -o /tmp/claude-0/hsa hsa.c -lm`.
- `gg.py` -- front end. `model LANG [--floor F]` builds `models/LANG.bin` (conditional quadgrams interpolated down to
  unigrams, a-z; `--floor` clips log P from below, a bounded loss that tolerates transcription noise; `models/` is
  regenerable and not committed). `solve LANG TEXT` fits a key on ONE text (`S:c1`, `S:c2` = the frozen scorer's own
  token stream, via a read-only import of `../score.py`; `--keep-x` keeps X as a sign, otherwise X is keyed null;
  `--nulls X,PICT,PUNCT` adds more null classes; `--shuffle S` fits an order-shuffled copy). `hcontrol LANG --model M`
  plants a LANG text on the real pooled sign curve with noise, fits the c2-shaped part, and runs the frozen scorer's own
  `evaluate()` on the c1-shaped part. `control` is the simpler hand-planted control used before the scorer was frozen.
- Corpora (`corpus/`, `corpus/MANIFEST.tsv`): Camilo Castelo Branco (1868, 1882), Eca de Queiros (1866-67), Almeida
  Garrett's verse (1853), Galdos (1876, 1892); Latin from `tools/data/la18` (Zaluski, c.1709, no 1850-1900 Latin at
  hand). None contains Camoes, the PT-HOMO plaintext.
- Scripts that produced the rows: `phase2_fit.sh` + `phase2_score.sh` (12 keys, both directions),
  `phase2_seeds.sh` + `phase2_seeds_score.sh` (c2 -> c1, 4 seeds, control beside target), `controls_hand.sh`,
  `fitgap.sh`, `phase2_xp.sh` + `phase2_xp_score.sh`. Every key was committed before it was scored.
- `summ.py` -- one line per score.py JSON.

Nothing here is a reading. No key passed the bar (LOG.md).
