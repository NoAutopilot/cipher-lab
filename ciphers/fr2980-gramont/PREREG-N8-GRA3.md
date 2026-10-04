# PREREG N8-GRA3 addendum to PREREG-N8-GRA2: the rest of fr.3040 no.6 (f.18v, f.19r top) vs Le Grand III pp.455-457 (4 Oct 2026, written 17:1x UTC, before any crop is read or any score)

Brief: `.claude/briefs/runs/2026-10-04-ytbiz-near8-wave3.md`, job N8-GRA3 (account 2, for LANE-NEAR8). Everything in
PREREG-N8-GRA2.md holds (statistic `agree`, decode rules, normalisation, NW scoring and free print-side end gaps, N1/N2 at
200 reps p99, planted control at 13% token error, 20 seeds, control gate mean >= max(N1,N2 p99) + 0.15, target gate
agree >= 0.50 and > max(N1,N2 p99)) except as below. Key: key.tsv at the commit that carries this file.

## New lines (Gallica btv1b9059870w; located by eye on 1000 px thumbnails, 17:1x UTC)
- f.18v (canvas 33) L01-L03: the three cipher lines at the top of the leaf, the end of the f.18r block.
  Print segment S1 = the N8-GRA2 span `n8gra2/print_span.txt` (free ends: the f.18r L12 onward lines are not read here,
  so these three lines align to wherever they fall in that span).
- f.18v L04-L08: the 5-line block after the clear "selon le project et desseing qu'ilz font".
  Print segment S2 = p.455 "car puisque luy qui est Pere" through p.456 "que l'on luy ait depuis fait entendre".
- f.18v L09-L27 and f.19r (canvas 34) L01-L02: the block after the clear "plus proffitable pour le service du ...",
  running over the page to the two cipher lines above "Monseigneur je presuppose".
  Print segment S3 = p.456 "dudit Seigneur. Monsieur l'Evesque de Vvigorne" through "pour s'en valloir de luy ailleurs".
- Each block is aligned to its own segment (three alignments); `agree` is pooled over all keyed tokens of the three.
  N1 shuffles each segment's letters separately; N2 permutes key values once per rep for all three; the planted control
  enciphers S1+S2+S3 (S1 cut to its last 120 letters, the expected length of three lines) to the target's keyed N.
- The marginal notes beside the blocks are not read (third witness, out of scope).

## Units (Usage 6, stated before the first call)
Unit 1 = f.18v L01-L08 + f.19r L01-L02 (10 lines, about 20 half-line crops): 2 blind Sonnet passes + my reconciliation.
Unit 2 = f.18v L09-L27 (19 lines, about 38 crops): 2 blind Sonnet passes + my reconciliation. 4 subagent calls in all;
the brief's rate is about USD 1.2 per unit. Unit 2 is not started if the job is past 80% of cap or box.

## Open-code rule (registered here, replaces PREREG-N8-GRA2's "what a PASS licenses" for open codes)
Open codes = HASH, A2, INF, TRI, ST, BOX, B8, ev and any key.tsv value '?' or unkeyed NEW: shape. Only if the gate
PASSes, an open code gets a key.tsv row at grade C iff all of:
1. it occurs >= 2 times among the reconciled tokens of this job plus N8-GRA2's f.18r L01-L10 (recon.tsv, re-aligned
   with its own GRA2 print span; open codes there were wildcards and are read out of that alignment unchanged);
2. every occurrence aligns to the same print letter (or the same letter pair, for a code that takes two print letters
   by gap structure; the aligner gives a wildcard one slot, so a one-letter value is the expected case), no gap;
3. a per-occurrence eye check by this worker on the occurrence's crop agrees the token is that shape (an occurrence
   whose shape the eye check rejects is dropped from the count; any rejection is listed);
4. per-code shuffled-print null: over 200 shuffles of the relevant print segments (the same decode, open codes still
   wildcards), the share of shuffles in which all of that code's occurrences align to one and the same letter is
   <= 0.01.
A code meeting 1-3 but not 4, or seen once, is listed in NOTES, not keyed. A keyed code whose aligned letter disagrees
in >= 2 occurrences is listed as a conflict (rule 4), not changed. Any key.tsv change -> `decode.py --check`; VERIFIER
WANTED flagged in ROOM.md naming the codes.
