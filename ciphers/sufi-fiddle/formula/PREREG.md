# GAPS104 formula test: pre-registration (3 Oct 2026, account-4; written and pushed before any result)

Question: do the two formula candidates the GAPS98 vision reader raised fit ciphertext_fig1.txt's sign sequence better
than random Arabic text of the same length does?

Candidates (fixed here, no others scored):
- F1 `على كل شيء قدير` ('ala kulli shay'in qadir), claimed at L06 g13-15 (vision numbering; ours may sit 1-2 off)
- F2 `محمد رسول الله` (shahada tail), claimed at the L06 tail; F2b `لا إله إلا الله محمد رسول الله` (full shahada) as the
  wider variant -- the vision reader wrote "la ... Muhammad?" for the L06 tail

Representation: rasm (dotless) classes on both sides, so dot misreads (most of the 18.5 pct two-reader split, GAPS87) do
not count: b/t/th/n/y/tooth -> B, j/h/kh -> H, d/dh -> D, r/z -> R, s/sh -> S, sad/dad -> C, ta'/za' -> T, ain/ghayn/nga ->
E, f/q -> F, k -> K, l -> L, m -> M, ha/ta marbuta -> O, waw -> W, alif -> A, lamalif -> LA; hamza dropped both sides;
OBSCURED and '|' dropped (groups concatenated per line; a match may cross a gap).

Statistic: d = minimum Levenshtein distance between the candidate's rasm string and any substring of the sign string,
divided by the candidate's length. Two scopes: (a) LINE = L06 only (the claimed line), (b) ALL = any line.
Null (matched, varies on the same axis): 2000 random contiguous spans from the Tanzil Quran (simple-clean, sha1 979b7902,
GAPS93 manifest) with the same rasm length as the candidate, scored identically; p = share of null spans with d <= the
candidate's. Positive control (power at this length and noise): the candidate planted at a random position in a copy of
L06 (scope LINE) with each sign substituted at 18.5 pct by a random class, 500 trials; power = share with p < 0.05.

Gate: a candidate is "fits beyond chance" only if p < 0.05 AND the positive control's power >= 0.8. p < 0.05 with power
< 0.8 is still reported as a fit; p >= 0.05 with power >= 0.8 is a control-backed negative for that candidate at this copy;
p >= 0.05 with power < 0.8 is a non-test. No reading is changed by this test; grades stay as GAPS98 left them unless a
candidate passes, and even then the locus is I->M at most (one copy, script fit, no key).
