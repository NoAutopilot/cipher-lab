# NEVBIR-87ALIGN application rule (fixed 2 Oct 2026, before any decode of nos.71/86/90 under the clerk values)

A clerk-sheet value enters the decode variant (harvest/key_1572_clerkvar.tsv) only if:
1. it comes from the real-sheet alignment (align87/key_real.tsv), the run that beat the shuffled-alignment control;
2. the sign is a letter sign of the printed table (Tnn) whose sheet majority differs from Tomokiyo's printed value,
   with n >= 3, agree >= 3 and agree/n >= 0.75 -- or a sign the printed table lacks, under the same thresholds;
3. per-tile off-sheet codes (1001-1025) are no.87-only: they are one tile each (n = 1), so they never transfer to other
   letters; they are recorded in keys/key_1572_clerk.tsv and used only for no.87 itself.
Signs below the thresholds (split majorities such as T52 o 7/11, T98 s 10 / d 7, T88 e 2/4, T46 1/4) stay at the
printed value and are listed as conflicts, never resolved by majority (rule 4).
Report per letter: S/M/U counts printed-key vs variant, and the changed fragments.
