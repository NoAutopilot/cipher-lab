# Pre-registration 3: fr.4712 f.7r period interlinear pair as NEW MATERIAL (GAPS-fr4715-vieuville-pool-16, account-4)
Written 3 Oct 2026 04:0x UTC (clock read), committed and pushed BEFORE the native image of f.7r is fetched or read.
GAPS-14 (PREREG.md) and GAPS-15 (PREREG2.md) FAILed as registered and stay on record. The retired instrument was
"our key71 transcription scored by token-subset match against a printed answer list"; this registration changes the
material (period glosses on a leaf enciphered with key no.71, read blind by us) and the match rule (notation-normalized,
fixed below). No further re-gate of key no.71 follows this one whatever the result.

## Disclosure (seen by the worker before writing this)
- Cabinet Noir README section 2 bis (sources clone 47b6db9): f.7r is a letter of 6 Mar 1589 to Nevers, about 20 lines,
  and they list 18 word-codes and 2 names confirmed by its gloss ('40 ou, '99 vous, '20 est, '42 pour, '12 bon, '22 je,
  '46 que, '19 et, '26 le, '87 Ligue, '21 fort, '16 de, '47 qui, '27 les, '52 si, '11 au, '33 mon?, '23 j'ay?; ~7 Roy,
  ''12 Chasteau), letters 8 = s, 17 = r, 62 = m, 52 = d, 31 = e, 77 = n, and '15 glossed "M...s". None of no.44's six
  open slots (.03 x2, .07, .49, .57, .6) is in their list; their f.7r transcription is partial (about 12 of 20 segments).
- key71_reconciled.tsv rows for numbers 3, 6/7/8, 49, 57 in every layer (grepped this session), and the cells PREREG2
  discloses. The vision subagents get crops only: no key, no Cabinet Noir list, no expected values.
- The 1000 px view (images/f4712_7r/view15_1000.jpg): the right page of view 15 is f.7r, clear French with numeral
  lines and small interlinear writing above them.

## Reading protocol
Native region of the right page (one fetch), `tools/iiif_lines.py --image`; line crops; two blind Opus passes on the
crops (one call each), then one reconciliation (a third call or the worker's own comparison on the disputed crops
only). Output witness/f4712_7r_pairs.tsv (plain_line, plain_raw = gloss as written, cipher_line, cipher_raw with marks:
'N one dot, ''N two dots, ~N bar). Only cipher lines with a gloss above them are paired.

## G1 -- the leaf's own control (rule 3 per-unit, before ANY merge)
`tools/interlinear_align.py align` from a flat start (no --prior), --floor 100 (letters and word-codes alike may take a
chunk), marked groups mapped to distinct code names. Statistic A = number of distinct UNMARKED codes 1-99 whose aligned
modal letter equals a value Tomokiyo's table (../fr4715-montholon-1589/keys/key_vieuville_nevers.tsv) gives that code;
S = scored codes (unmarked codes with a single-letter modal chunk that the table lists). Control: the table's values
permuted over its codes, 10,000 draws, seed 4712 (it varies which value meets which code, the statistic's own axis).
PASS: S >= 12, A/S >= 0.70 and A > the control's p99. Otherwise the leaf is held: nothing from it merges, stop.

## G2 -- key no.71 on the f.7r glosses (only if G1 PASSes)
Items: every marked group on f.7r whose gloss (word or name above it) the reconciliation reads at M or better and whose
mark is read the same by both passes. Layer by mark: one dot -> mots, bar -> persons, two dots -> places. Key cell from
key71_reconciled.tsv, loaded as scripts/key71_control.py loads it. match / conflict / absent as in PREREG2.
Notation-normalized match (fixed now): both sides through key71_control.norm_tokens, PLUS (i) a token-subset match
either way; (ii) else the two sides' concatenations (stop words kept, apostrophes and spaces removed) equal after
dropping one leading elided consonant (l d j n s m t c qu) from either side; (iii) else equal after removing every s
that precedes a consonant and collapsing doubled letters. Period abbreviations already in ALIAS (Mr, Card, Cal, C, D).
Controls: label permutation over the items (exact if <= 8 items, else 10,000 draws, seed 4712) and random code in the
layer's range (mots 11-99, persons 1-89, places 1-99), 10,000 draws, seed 71.
PASS: scorable >= 8, SHARE = match/(match+conflict) >= 0.80, REAL > p95 of both controls (strictly).

## What follows
- A slot code (.03, .07, .49, .57, .6) glossed directly on f.7r with a mark both passes read the same: grade C on
  no.44 if G1 PASSes; a value that conflicts with an existing C/H value goes to HYPOTHESES.md, never by majority.
- G2 PASS: no.44's slots not glossed on f.7r are read from key no.71 in the layer their mark selects, grade M (the
  slots' own marks are L/M), then decode_key --check must exit 0. G2 FAIL or NON-TEST: no slot read from the key.
- Every f.7r word-code or name gloss that conflicts with our existing values is logged in HYPOTHESES.md.
