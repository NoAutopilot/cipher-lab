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

## Other solvers' items (TX-POOL-LEAF-2)

9 Oct 2026, 21:5x UTC by date -u; account 1, brief .claude/briefs/runs/2026-10-09-account4-tx-pool-leaf-2.md (= Amendment 1 of the
TX-POOL-LEAF brief). Read-free screen over the solver sources only: sources/cryptiana/READABLE.tsv (13 rows), CRYPTO-INDEX.tsv and
cryptiana/keys/ (Tomokiyo); sources/cyphersolver/2026-10-0{1,2,3}/ and sources/cyphersolver-site/ (Bourdeau: mercy1648, catokwacopa,
matignon1586, spaen1808, zeschau1841, armstrong); KEY-DESIGN.tsv rows whose key is Tomokiyo's or Bourdeau's; LANDSCAPE.md /
Aymeloglu's DECODE catalogue (cite only, nothing copied). Same exclusions as above (Birago, Ceppo, Dinteville, Spinelli,
Vivonne/Saint-Gouard incl. fr16104, the fr.3619/3621/3623 cluster, gunther). Gallica 403 until 10 Oct 00:00 UTC: listed, not fetched.
Independence rule: pool-grade only where the plaintext has a witness independent of any transcription (period decipherment on the
leaf or elsewhere, clerk clear copy, printed edition of that letter) AND the key is period or published.

### Pool-grade (independent plaintext witness)

| rank | candidate | solver credited | hand | key source | independent witness | signs (est.) | image source | verdict |
|---|---|---|---|---|---|---|---|---|
| 1 | huntington-luzerne-destouches-1781, Huntington mssDE 108(A) pp.1-6 (La Luzerne to Destouches, Philadelphia 16 Jan 1781) | Tomokiyo (Cryptiana blog 23 Sept 2021, "Decoded but not Identified Code of Luzerne": the Jan 1781 Luzerne code, Beinecke sibling); Bourdeau's destaing/NOTES.md l.13 on the same 1199-figure code | La Luzerne's legation secretary, 1781 (new century, office, language family, numeric code) | key.tsv grade C from the contemporary interlinear decipherments of siblings mssDE 68/37/55 (period, Destouches's office) + Tomokiyo's Yale 8 Jan 1781 table (key_tomokiyo.tsv); the 31 figures key.tsv took from 108(B) are DROPPED for the truth (independence) | mssDE 108(B), the "Duplicata" of the same letter, a separate document deciphered in ink under every group by Destouches (catalogue note, AUDIT.md N0); gloss transcribed in pairs_108B.tsv (R19, 24 Sept 2026; a reading of clear French, not of the cipher) | 719 committed groups (~2,100 digits), scored = groups whose 108(B) gloss word has a keyed figure | Huntington CONTENTdm IIIF, on disk (images/mssDE108A_p1-p8.jpg, 1200 px), non-Gallica | **BUILD** |
| 2 | rah-juan-manuel-1521 (Juan Manuel to Charles V, RAH Salazar, DECODE R9499-R9529) | Tomokiyo (AlonsoSanchez.htm: "the first page of contemporary decipherment is visible in most of these records") | Juan Manuel's Rome embassy 1521 | Tomokiyo's published alphabet (key_tomokiyo_alpha.tsv) | contemporary decipherment page of p.1 inside 26 of 28 DECODE records | p.1 per letter | DECODE full-size images not on disk (manifests only; account-gated per record) | listed: images not on disk; DECODE fetch per record first |
| 3 | matignon-mayenne-1586, fr.15572 f.18 (deciphered on f.19), f.14v (f.15r), ff.91-92 (margin) | Bourdeau (matignon1586, key verified against these decipherments); Tomokiyo henryiii.htm | Mayenne/Forget 1586 | Bourdeau key.json (published, MIT) | period decipherments on f.15r, f.19, f.91-92 margin | f.18 3 lines on disk only as text | Gallica only, never imaged | listed, not fetched (Gallica 403); f.78v/79r crib closed by rule 3(b) |
| 4 | Bayonne 1529 (Clair.330 f.85, "deciphered on the previous pdf page") | Tomokiyo; Bourdeau dubellay/ | du Bellay 1529 | Bayonne's Cipher (1529), Tomokiyo/Bourdeau | period decipherment on the previous page | unmeasured | Gallica only, no folder | listed, not fetched |
| 5 | beinecke-manchester-1699-1700 (Beinecke OSB MSS fc37) | Bourdeau (published reading); HMC 8th Report App. II prints the letters | Vernon/Yard to Manchester | THE=454 key preserved with the papers | HMC 8th Report (1881) + Memoirs of Affairs of State (1733) print the letters | word code | Beinecke, not on disk (folder holds NOTES only) | listed: images not on disk; word-code digits |

### Key-only (solver-truth), not pooled

| candidate | solver | why not pooled |
|---|---|---|
| fr4715-montholon-1589 f.81r (Vieuville-Nevers) | Tomokiyo (bnf4715.htm no.58 L01-L17); Descifrado, Cabinet Noir v1.0 (L18-L40) | plaintext only from the solvers' own decodes; no period gloss or print of the letter |
| clair331-rangone-montmorency-1530 f.15, f.156 | Bourdeau (rangone1530, joachim1530) | solver decode only |
| fr4715-f61-mayenne-1592 | Tomokiyo (mayenne.htm key; interlinear markup on his specimen is his own) | solver markup only |
| fr3985-nevers-revol-1593 | Tomokiyo (no.60 style) | no gloss on the leaves; solver key only |
| decode-2678-bnf-colbert127-gravel-1665 | Tomokiyo (Colbert-Gravel 1672 key); Bourdeau WIP | our own S/H decode only (N3) |
| espagnol142-mercy-1648, zeschau-seebach-1841, vanspaen-vandergoes-1808, catokwacopa-1875 | Bourdeau | no independent plaintext (partial/open) |
| stepney-manchester-1702 | Bourdeau (Yale transcription) | key not found; offline-only |

prior_work.py (offline, --step-type transcribe --known-answer item:txpool, --item-spec): huntington 108(A) exit 4 -- plaintext
KNOWN; step LEAD 1-own NOTES.md:277 (our own R10/R16 partial reading of 108(A)): answered -- that reading is a READER (C/M/U decode,
not used for truth); the truth is the 108(B) period gloss under the sibling-built key, and the baseline is two fresh blind passes,
so the earlier passA/passB in the folder are neither truth nor baseline; 2-leaf LOOK: 108(A) carries no decipherment (inventory.tsv
p1/p2/p6 viewed, catalogue "entire letter in numerical code except closing"); the one pencil "835" in the p.1 margin is a figure,
not a gloss. matignon exit 0 KNOWN; rah-juan-manuel, montholon, beinecke-manchester exit 4 LOOK/UNCHECKED (not built).

Choice: candidate 1, scope by cost (Usage 6): two blind Sonnet passes x one page per call, pages taken in order p1..p6 while the
80% box line (23:18 UTC) allows, + one reconciliation unit. Digits: TRANSCRIPTION.md target <= 1%; at 1-3% per group over ~720
groups the >= 8 rule is expected to be met only with most of the letter read.
