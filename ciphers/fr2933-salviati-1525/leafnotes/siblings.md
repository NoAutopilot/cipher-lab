# Sibling search, 25 Sept 2026 (LANE R7 SSIB)

Brief: `.claude/briefs/runs/2026-09-25-lane-r7-ssib-salviati-siblings.md`. Pools-first search (CLAUDE.md
selection rule) for another letter enciphered in the same invented-sign design as fr.2933 no.11
(`glyphs/atlas_part1.png`/`atlas_part2.png`: cursive a, e, g, y, m, w, wd, nt, bh, ch forms with superscript
marks), since the atlas re-pass (R7-AT55V/AT57V) cut the pooled type count only to 198-205 against a gate of
178, and CM2's own suggestion is that more observations per type (i.e. more sibling text) is the remaining
lever, not further merging.

## Method

`archivesetmanuscrits.bnf.fr` plain POST search (`resultatRechercheSimple.html`, field `TEXTE_LIBRE_INPUT`,
cookie jar, page 1 only, per the CLAUDE.md host table and the LANE G2/G3 precedent in QUEUE.md's "Fourth
pass"). No CSRF token; a connection reset on one item-page fetch recovered on the single allowed retry
(`ws_closed_mid_exchange`, proxy-side, confirmed transient not a block).

Queries run (each a separate request, >=2s apart, UA `cipher-lab research script (contact via repository)`):
1. `Salviati chiffre` -- 1 result (an unrelated Latin ms, Giorgio Benigno dei Salviati, `Latin 3620`)
2. `Salviati chiffres` -- 3 results (the target itself, `cc493855`=Français 2933 item 11; plus two
   false-positive co-occurrences within the same finding-aid page, see below)
3. `Salviati en chiffre` -- 1 result (same unrelated Latin 3620 hit as query 1)
4. `Salviati dechiffrement` (no accent) -- ambiguous render, re-run with accent
5. `Salviati déchiffrement` -- **0 results** (confirmed via "Aucun résultat")
6. `Salviati chiffrée` -- 0 results
7. `Salviati cifra` -- 0 results
8. `Salviati cifre` -- 0 results
9. `Salviati` scoped to `DATE_DEBUT_INPUT=1524&DATE_FIN_INPUT=1530` (`DATE_CATEGORIE=DATE_DE`) -- 32 results
   (page 1), giving the fullest list of Cardinal Giovanni Salviati's own correspondence held in the BnF's
   "Français 2754-3068"/"3069-3380" Ancien fonds "Recueil de lettres et de pièces originales" run (the same
   fonds and item-list convention as fr.2933 itself) -- 11 distinct Salviati items besides the target, listed
   in `siblings.tsv`, plus one different Salviati ("chevalier Salviati", Français 3226, not the cardinal) and
   one Jacopo-Salviati-linked recueil (Italien 2101, the cardinal's father, matching the Strozziane lead
   already logged in NOTES.md's check-solved section).
10. `Salviati Clairambault` -- 0 results (brief asked to check this fonds explicitly)
11. `Salviati Béthune` -- 2 results, both volume-level (Dupuy 28, Français 6635-6643), no item-level Salviati
    + cipher co-occurrence found on inspection
12. `lettre en chiffres italien` scoped 1524-1528 -- 0 results (too many ANDed words; the site's search is
    AND, not OR, confirmed again here)
13. `en chiffre` scoped 1524-1528 (unscoped by sender, to probe the broader pool) -- 1187 reported, far beyond
    what this brief's budget or the site's own pagination cap can review (consistent with QUEUE.md's Fourth/
    Fifth-pass finding that the four broad chiffre-family terms are not sweepable this way); not pursued
    further, a documented gap not a negative for that broader question.

Requests: archivesetmanuscrits.bnf.fr 16 (1 reachability check, 13 search POSTs, 2 item-page GETs — the second
a retry of a `ws_closed_mid_exchange` reset on the first). gallica.bnf.fr: 0 (no candidate reached step 2).

## Result

**No sibling found.** Of Cardinal Giovanni Salviati's ~11 other letters catalogued in this exact fonds run
(1524-1530, `Français 2754-3068`/`3069-3380`, the same "Recueil de lettres et de pièces originales" series as
the target), **none is catalogued as ciphered** ("en chiffre"/"chiffres"/"déchiffrement"/"cifra" all return
zero additional hits when combined with "Salviati"). This absence is meaningful, not a search-method gap: the
same fonds run demonstrably flags cipher status at the individual-item level where it applies (Français 3034,
in the same list, separately catalogues its own items 68 and 69 as "Lettre, en chiffre," while leaving item 3,
a plain Salviati letter in the same volume, unflagged) — so a cataloguer did look at each item and Salviati's
other letters were judged plain. The closest in date, Français 3087 item 90 ("Da Toledo, a di III di ottobre
1525", 13 days before the target's 16 October 1525), is plain per the same convention.

Two catalogued-cipher items surfaced incidentally in the same fonds range (Français 3034 items 68/69, and
Français 5761's "voiage d'Allemagne" office cipher) but belong to different correspondents/offices (an
anonymous despatch and Ambrosio Bizzolla writing to Maximilian Sforza; a Palatine-embassy cipher) — not
Salviati's own hand, not image-checked this pass (out of the brief's Salviati-specific scope and budget); left
in `siblings.tsv` as an unresolved design-comparison lead for whoever next works this fonds run, since "same
office, different sender" pools are exactly the CLAUDE.md pools-first target if the design turns out to match.

**No image comparison was run** (step 2 of the brief): with zero genuinely cipher-catalogued Salviati items
found, there was no candidate to fetch a Gallica reference image for. `signs_compared` is 0 throughout
`siblings.tsv`.

## Where not found

Web search / QUEUE.md / STATUS.md were not re-checked this pass (NOTES.md's 24 Sept check-solved sweep and key
search already covered web search, Cryptiana/Cipherbrain, DECODE, both solver repos, Meister 1906, the
Strozziane inventory and Pieper 1894 -- per the brief, "do not repeat them"). This pass is archivesetmanuscrits
and Gallica only, as briefed.

## Suggested follow-up (not attempted, out of this brief's scope)

- Image-check Français 3034 items 68/69 and Français 5761's cipher against `glyphs/atlas_part1.png`/
  `atlas_part2.png` -- a design match would identify a same-office (not same-sender) pool, which is still a
  pool per CLAUDE.md's pools-first rule.
- The `en chiffre` 1524-1528 broad sweep (1187 results, page 1 only) is an open gap; bucketing by a narrower
  date range or fonds (as QUEUE.md's Fifth pass did for the 17th-18th century sweeps) could make it tractable
  for a future worker with more budget.
- The pagination-past-page-1 limitation noted in QUEUE.md's Fifth pass was not re-tested this pass; all
  counts above are page-1 samples where the reported total exceeds ~50.
