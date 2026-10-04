# PREREG-MANT-WORD (4 Oct 2026, written 10:5x UTC by the clock, RUN4-MANT, account 1), before any statistic is computed

Instrument (different from interlinear_align.py's letter chunks, as the RUN3-MANT verdict asked): **whole-word code pairing**.
Material: frame 0501's glossed multi-code runs C3 C4 C7 C9 C10 C12 (f0501/pairs.tsv), C9 trimmed to 553 716 417 646 (84.406.108
carry no gloss on the image, RUN3-MANT reconciled.tsv run 9). Single-code glosses (C1 C2 C5 C6) are not part of this test.
f.409v adds no gloss, so it adds no positions (cross-witness = run-level identity only).

- Pairing model: per run, k = min(#codes, #words); codes and words are each cut into k contiguous non-empty blocks, block i of codes
  carries block i of words (one-to-many either way, monotone). A code occurrence's label = the word tuple of its block.
- S_word = max over the joint choice of cuts in all runs of (codes with >= 2 occurrences across these runs whose label is identical at
  every occurrence) / (number of such recurring codes). Exhaustive enumeration (script f0501/word_pairing.py).
- Control: gloss strings permuted across the six runs, same model, same max, 200 draws, seed 409. The permutation changes which words
  can sit over which codes, so S_word can differ under it (it is the pairing S measures, not order or value alone).
- Gate: N_recurring >= 3 AND S_word > p95(shuffle) strictly. Anything else = HELD: values to f0501/word_values.tsv at grade M,
  nothing into key.tsv (rule 3 Szembek / third-attempt paragraphs). Even on a pass, only codes whose label is a single word, identical
  at >= 2 occurrences, would be C; nothing else.
- Expected in advance: 4 recurring codes (612, 115, 402, 515); 612 and 115 cannot share a word under any cut (no repeated word that
  fits their positions), so S_word <= 0.5 by construction; a tie with the control is likely.
Also reported, not a gate: the gloss placement as written over the codes on the 0501 zoom (scribe's position), per word.
