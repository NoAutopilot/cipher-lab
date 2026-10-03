# PREREG3 reconciliation rule for the image pass (GAPS-fr4715-vieuville-pool-17, account-4, 3 Oct 2026)
Written and pushed before the vision call. PREREG3.md and scripts/f4712_7r_gates.py are unchanged; this only fixes how
the reconciled pairs file is made, replacing GAPS-16's mechanical rule (scripts/f4712_7r_reconcile.py, kept as history).

- One Opus vision call (subagent) gets the 20 crops in images/f4712_7r/ (paths only), the crop offsets, and the two
  blind passes' readings of each run (witness/f4712_7r_pass_A.tsv, pass_B.tsv). It gets no key, no Cabinet Noir list,
  no Tomokiyo table and no expected value. It settles from the image: the digit grouping as the scribe spaces it, the
  mark above each group (one dot, two dots, bar, none; a dot that belongs to the gloss is not a mark), the looped glyph
  (written 8, as both passes read it), and the gloss words over the run.
- Its output is written verbatim to witness/f4712_7r_pairs_img.tsv in the PREREG3 schema (plain_line, plain_raw,
  cipher_line, cipher_raw; tokens N / dN / tN / bN; non-digit glyphs omitted; only runs with a gloss; struck gloss
  words dropped). No hand edit after the call, except dropping a token the schema cannot parse (logged).
- That file is committed and pushed, then `python3 scripts/f4712_7r_gates.py --pairs witness/f4712_7r_pairs_img.tsv
  --out witness/f4712_7r_img` runs once; its output is pasted unedited into NOTES.md. G2 and no.44's slots follow only
  on G1 PASS, then only on G2 PASS, as PREREG3 says. No second run with any other file.
