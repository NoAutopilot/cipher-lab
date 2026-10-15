# PREREG-JAV-COLLET (LANE DEFAULT-A4-0235-15, account 4) -- written 15 Oct 2026 03:06 UTC by date -u, before any --try run

Job: test Collet 1910's printed sentences (AUDIT.md "Found, not applied") as crib values on leaf 188 with
`tools/decode_key.py ciphers/na-janssens-java-1811 --try CODE=VALUE` (fr1810 corpus model, window 8, 100 nulls),
at every occurrence in the pool. Pool = leaf 188 ciphertext.tsv (inv26 is a copy of the same dispatch, not an
independent occurrence; no other transcribed leaf carries these codes: grep of leaf187/192/201/no4 files, 0 hits).
Occurrences: 853 n=1, 1121 n=2 (l.1, l.9), 1173 n=1, 381 n=1 (keyed 'chargent' C, p.191), 125 n=2 (l.4, l.11),
1065 n=1, 72 n=1; also 573 n=?, 1027 n=? (same Collet sentence, beyond the brief's list; logged only).

Crib alignment (Collet: "L'ancien gouverneur général présentera les choses bien différemment ... Il part, chargé de
trésors et de la malédiction"; cipher l.1 "[853] [1121] l' état des [1173] [573] [1027]", l.10-11 "par [381] de [125]
[1065] et de la mal é [72]"):

Hypotheses tried, all and only these:
- H1 853/1121 split of "présentera": (a) 853=pré,1121=sentera; (b) 853=présen,1121=tera; (c) 853=présente,1121=ra.
  1121's l.9 occurrence ("i [824] [1121] [449]") is the only independent test.
- H2 1173=choses (Collet abridges "l'état des choses" to "les choses").
- H3 573=bien, 1027=différemment (logged only, not in the brief's list).
- H4 381=chargé against the keyed 'chargent' (period decipherment p.191, C): a conflict to log, never a key edit.
- H5 "trésors": (a) 125=tré,1065=sors; (b) 125=tre,1065=sors; (c) 125=trésors with 1065 left unread.
  125's l.4 occurrence ("ns [125] A [206] ché") is the only independent test.
- H6 72=diction; alternative 72=dic.

Gate (brief, fixed before scoring): a value enters key.tsv as C only where --try's own known-answer control passes for
that value class AND no occurrence contradicts it. Every hypothesis above is a word or multi-letter syllable; the
word-class control K2 (Blathwayt, tools/tests/PREREG-MQS-CROSSWORD.md) FAILED (58/116 first vs 70% gate; false accepts
17/70 vs 10%). Letter-class K3 passed but no hypothesis is a single letter. So, decided now: no key.tsv edit from this
job whatever the verdicts; each value is logged in HYPOTHESES.md as M (crib from print, Collet paraphrases), with its
--try statistic, both null p95s and verdict; a 'reject' verdict at a second occurrence is recorded as a contradiction
of that alternative. n=1 codes are 'undecided' by construction and are reported as such, not as support.
