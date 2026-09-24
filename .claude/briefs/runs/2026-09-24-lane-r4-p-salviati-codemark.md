LANE R4 WORKER P -- M35 SALVIATI: how much text the code+mark model needs (Opus, cap $4; disk only; no subagents).
Target: ciphers/fr2933-salviati-1525. Common rules: .claude/briefs/runs/2026-09-24-lane-r4-common.md. Input: ciphertext_f54r.tsv (370 signs)
and ciphertext_f54v.tsv (349 signs, LANE R4 J), 36 base codes plus superscript marks; NOTES.md "Solver (LANE R4 I)" (simple homophonic over
base codes excluded with a control; code+mark as 94 distinct signs untested because its control failed at 370 tokens).
1. Control curve first: with tools/homophonic_anneal.py and the same held-out Italian as worker I, build matched controls of the
   code+mark design (the pooled type counts and mark frequencies of the two leaves, the plain/cipher interleaving) at N = 720 (the pool),
   1,400 and 2,800, and a marks-as-vowel-indicator design (sign = consonant, mark = following vowel) at the same N. Three seeds each.
   Record token accuracy per design and N: control_curve.tsv.
2. Run the target (pooled 719 tokens) ONLY under a design whose control reads > 60% at N = 720; report both numbers.
3. From the curve, say how many tokens each design needs to read reliably, which is how many more leaves (at ~350 signs a leaf) are worth
   transcribing. One line in NOTES.md with that number.
Report what was found and where it was not found; do not classify novelty. NOTES.md "Code+mark control curve (24 Sept 2026, LANE R4 P)".
ROOM done: the curve and whether the target was run.
