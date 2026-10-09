# TX-POOL-LEAF candidates (9 Oct 2026, 20:4x UTC by date -u; account 1, brief .claude/briefs/runs/2026-10-09-account4-tx-pool-leaf.md)

Read-free screen (no cipher image read by a reader; the builder looked at one page image for legibility and gloss only).
Excluded hands: Birago 1572/1571, Ceppo, Dinteville, Spinelli, Vivonne/Saint-Gouard (confirm2), and the Nevers-office 1590s
DECODE cluster fr.3619/3621/3623 (LANE TX-ENGINEER-2's own 0b material). Gallica not probed (403 all of 9 Oct).
Screen: every KEY-DESIGN.tsv `usable=yes` folder x sign inventory (symbol/mixed/glyph over digits) x C-graded token files x
images on disk; then NOTES/AUDIT for the known-text source. Per-sign error assumed 8-25% (today's symbol range); expected baseline
errors = scored signs x 0.08-0.25.

| rank | candidate | hand | key source | known-text source | signs (scorable est.) | image source | exp. errors | verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | gunther-van-schwarzburg-1561, WVO 8246 p.2 (Staatsarchiv Rudolstadt, Kanzlei Sondershausen 693) | Willem van Oranje's German secretary, Brussels, 2 May 1561 (new hand/office/language/decade) | key.tsv, 79 signs, grade C, rebuilt from sibling WVO 5109 against Japikse no.236 pp.232-233 (H. Koot's decipherment, printed 1934; published modern key, as spinelli's Domnina table); zero conflicts among C pairs | Japikse, Correspondentie van Willem den Eerste I (1934) no.316 pp.343-344, spaced type = the cipher passage deciphered (AUDIT.md N0, two audits); page images on disk (images/japikse_p343.png, p344.png) | p.2 371 committed signs, 329 keyed C (whole letter 953 / 817) | on disk, Huygens WVO PDF (non-Gallica), 1241x1754, no interlinear gloss, signs widely spaced | 26-82 on p.2 | **BUILD** (p.2 only, cost) |
| 2 | clair349-este-guise-1556, Clairambault 349 f.3 | Este/Ferrara chancery 1557 | period key BnF fr.20974 no.15 (Tomokiyo) | interlinear gloss on the leaf + Guise Memoires-journaux t.6 pp.238-239 | ~1000 tokens but C 260, M 611 | Gallica crops on disk | ~20-65 on C only | passed over: M 611 of 1000 (key application uncertain), gloss on the leaf (masking, gloss-visible risk) |
| 3 | clair1067-brienne-poland-1646, Clairambault 1067 ff.226r-227r | Brienne secretariat 1646 | key_1646 rebuilt from the leaf's own gloss (C, no outside key); key_brienne_1647/1651 siblings | interlinear gloss on every cipher line | 338 tokens, C 307 | Gallica crops on disk | 25-75 but digit syllabary (expect <8%) | passed over: digit groups read at ~1-5%, gloss-visible, key rebuilt from the same gloss (f23r caveat) |
| 4 | rah-canada-1869, RAH 9/6958 | Cañada 1869 | key.tsv C 28 (from the leaf) | clear Spanish line above every cipher line, same hand | 667 signs | RAH, on disk | low: digits plus pen marks | passed over: digits, clear text touching every line (gloss-visible) |
| 5 | august-van-saksen-1561-64 no.57 | Saxon court 1561-64 | key_74/key_98 C | Demandt 1988 clear text of 57 (Google Books snippets only) | 294 C tokens | Huygens on disk | 24-70 | passed over: known text from snippets only, not a full print on disk |
| 6 | fr5160-letellier-1653 f.67 | Le Tellier 1653-61 | key_1659 (period) | align_f67 C 454 | ~450 | Gallica on disk | digits syllabary | passed over: digit groups (low headroom), status open |
| - | fr16045-pisany-rome-1585 | Pisany 1585 | C 355 | Colbert witness | - | Gallica | - | passed over: UNA3-PISA / V-PISA-T32 live on it today (collision) |
| - | na-suriname-map-1781 | Suriname 1781 | period alphabet | legend | - | NA | - | passed over: SUR-0745 (account 2) live on it today |

prior_work.py (offline, --step-type transcribe --known-answer item:txpool) on 1-4: every one exit 0 `KNOWN` (known-answer work).
LEADs answered: gunther `2-leaf LOOK` "no gloss/clear-copy check recorded for this leaf" -- checked by eye on images/08246_p2.jpg
this session: no interlinear gloss, no clear text on p.2 (C1 inventory agrees: "cipher, full page, no clear-text breaks"); the
known text is the 1934 print, not a leaf gloss. gunther `UNCHECKED` 3-tomokiyo/3-solver/4-editions (Gachard t.1-6): not
prior-work holds for a known-answer build (the item is already N0; the print is the answer). Others not built.

Choice: candidate 1, page 2 only (25 lines, the one page with no clear-text break): 2 blind passes x 1 page + 1 adjudication
fits the USD 8 cap; pp.1 and 3 stay available for a later extension (same build script, `--pages`).
