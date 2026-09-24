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

## csDA2: edition lead (24 September 2026, close-out pass)

Closing the Waldburg family edition lead flagged above (brief named it as "Vochezer, Geschichte des
fürstlichen Hauses Waldburg"). Vochezer's 3-volume *Geschichte des fürstlichen Hauses Waldburg in Schwaben*
(Kempten, 1888-1907) is on archive.org; volume 3 (identifier `GeschichteDesFuerstlichenHausesWaldburgInSchwaben3`,
Vochezer_Waldburg_3_djvu.txt, 67,235 lines) is the one that reaches the 17th century — confirmed by nine "1653"
hits in the narrative (e.g. line 54725 "erftatteten am 23. Januar 1653", line 58984 "23. September 1653"), and
one hit for "Trauchburg" (line 20214, "Christoph, Erbtruchsess, Freiherr zu Waldburg... zu Trauchburg" — a
different Christoph, not Christoph Karl).

Fetched the full djvu.txt and grepped for the correspondents and the cipher terms (with loose substrings
"iffr"/"eheim" against the same Fraktur-OCR noise seen in the Havemann volume): no occurrence of "Chiffre",
"Geheimschrift" (only "Geheimer/Geheimen Rat", the privy-council sense, appears — 15 hits total for "eheim"),
"Christoph Karl", "Walburga" (the two "Walburgen" hits at lines 16078-16582 are the saint, S. Walburga, not the
person), or "Essen"/"Pröpstin". The correspondence (StA Sigmaringen Dep. 30/1 T 3 Nr. 702) is not named.

**Verdict: open, edition lead closed.** Vochezer's volume covers the right decade and the Trauchburg line of
the family but never names either correspondent, the letters, or a cipher. The genuine caveat: 19th-century
Fraktur OCR on this scan is noisy (many common words misrecognised, e.g. "Sriefe" for "Briefe"), so a rare
proper name could in principle be missed; the negative is on the same footing as the Havemann one, not
stronger. Posting `confirm` to ROOM.

Host requests this section: archive.org 3 (advancedsearch + metadata + djvu.txt fetch for
`GeschichteDesFuerstlichenHausesWaldburgInSchwaben3`, >=3s apart, IA slot); WebSearch 1 (to confirm which
archive.org identifier is volume 3 and its year range).
