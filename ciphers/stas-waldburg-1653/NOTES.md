open

# Maria Walburga Eusebia von Waldburg to Christoph Karl von Waldburg, partly ciphered — StA Sigmaringen

QUEUE row: DA9 (sources/solver-diffs/2026-09-24-lane-n2-dea.tsv, "German state archives, online finding aids
(LANE N2 scout of 24 September 2026)").

## Source

Staatsarchiv Sigmaringen, **Dep. 30/1 T 3 Nr. 702**: "Korrespondenz der Truchsessin Maria Walburga Eusebia von
Waldburg, Pröpstin zu Essen, an ihren Bruder Truchseß Christoph Karl (?) z.T. in Geheimschrift", 1653-1654.

Identified persons (WebSearch, 24 Sept 2026): **Maria Walburga (Eusebia) Truchsess von Waldburg-Trauchburg**
was Pröpstin (provost) of the Essen women's abbey until 1668 (Wikipedia/BLKÖ). Her likely brother
**Christoph Karl (Karl Christoph) Graf von Waldburg-Trauchburg** (24 Aug 1613 - 28 Mar 1672), Reichserbtruchsess,
married to Maria Elisabeth von Sulz (kaiserhof.geschichte.lmu.de/16378) — the catalogue's own "(?)" on the
brother's identity is not resolved by this pass, just corroborated as plausible.

## Check-solved sweep (24 September 2026)

1. **Editions.** No dedicated edition of Waldburg family correspondence covering this pair or these years was
   located. The Deutsche Digitale Bibliothek holds several *unpublished* Waldburg family correspondence
   bundles at item level (Waldburg-Wolfegg'sches Gesamtarchiv material, e.g. items
   4Q6VGO4AFOYYMBS43B3TQHXXUTFNTJJO and E65VUJJ63AAMXORAELJDFFRHUAAAWZTP, both catalogue descriptions, not
   editions) — none of these DDB item descriptions names either correspondent by this date range or mentions a
   cipher. A dedicated printed *Zeitschrift für Hohenzollerische Geschichte* or Waldburg-archive Regesten
   series was not reached this pass.
2. **Printed decipherment / catalogue note.** The finding-aid title gives no indication of an attached key or
   contemporary decipherment.
3. **Community lists.** `sources/cryptiana/` grepped for "Waldburg": no hits.
4. **DECODE.** `sources/decode/` grepped for "Waldburg", "Walburga", "Trauchburg", "Sigmaringen": no hits.
5. **Solver repositories.** Fresh shallow clones, 24 Sept 2026. No target folder for Waldburg in either repo;
   `grep -rli waldburg` across both trees: zero matches.
6. **General web search.** As (1). No result names an attempt to read this correspondence's cipher passages.

**Copy status.** Not independently re-tested this pass against LABW's viewer (StA Sigmaringen's finding aids
are served through the same LABW OFS21 system as GLA Karlsruhe and HStA Stuttgart). Scout's original sweep
(sources/solver-diffs/2026-09-24-lane-n2-dea.tsv) recorded "none tested (no digitisation link)" for this row.
**Copy-order**, pending a direct re-check. See REQUEST.md.

**Host requests this pass:** WebSearch 1, github.com 1 shallow clone each of both repos (shared across this
run's six targets); no direct LABW request this pass.

## Verdict

**Status: open, stage 2 (verified unsolved).** No edition, catalogue gloss, community list, DECODE record, or
solver-repository entry names this correspondence. Convent/family correspondence "z.T. in Geheimschrift" between
a Reichsstift provost and her brother is a plausible small nomenclator or letter-substitution system, likely
short given it is only "z.T." (partly) enciphered within otherwise plain letters — those plain portions, once
copied, may themselves be a crib for the ciphered portions per the same letter (LESSONS.md "structure before
search" / verify-against-the-world pattern).

**Recommended next steps (not run this pass):** (1) search for a Waldburg-Trauchburg family archive Regesten
or Zeitschrift für Hohenzollerische Geschichte covering 1653-54; (2) resolve the catalogue's "(?)" on
Christoph Karl's identity against Waldburg genealogies before any solving; (3) re-test LABW's viewer for
Dep. 30/1 T 3 Nr. 702 directly.
