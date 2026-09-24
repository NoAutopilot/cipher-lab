# konstanz-talleyrand-sieyes-1798

Status: open

## What this is

Talleyrand (French Foreign Minister) and Sieyès (French envoy to Berlin), correspondence around Prussian
neutrality, the Repnin mission and Rhine troop movements during the Congress of Rastatt: Stadtarchiv Konstanz,
"Korrespondenz Ignaz Heinrich von Wessenberg – N-Q" (fonds `DE-611-BF-42689`), items P 1839/5 (17 Jul 1798,
Berlin, Sieyès probably to Talleyrand, cipher in a postscript), P 1839/21 (26 Oct 1798, Paris, Talleyrand to
Sieyès, "Chiffrierter Brief" outright), P 1839/28 and P 1839/41 (Dec 1798, Feb 1799, further items in the same
run). Scored as K2 by LANE S scout, 24 Sept 2026 (QUEUE.md). No image seen; the Wessenberg-fonds provenance for
Directory-era Foreign Ministry traffic is unexplained and unresolved (QUEUE.md caveat 4). No ciphertext.txt
exists yet.

## Check-solved sweep, 24 Sept 2026

Six sources, run directly (no subagents).

1. **Web.** WebSearch: `Talleyrand Sieyès Rastatt 1798 chiffre lettre Konstanz Stadtarchiv`. Returns general
   pages on the Congress of Rastatt, the Stadtarchiv Konstanz itself, and a Google Books listing for
   *Correspondance Diplomatique de Talleyrand*, but nothing naming these specific items, this shelfmark or a
   decipherment/attempt. Nothing found.
2. **Print.** Bailleu, *Preussen und Frankreich von 1795 bis 1807* (1881-87), vol. 1 (1795-1800, archive.org
   `preussenundfran01bailgoog`, public): full-text search (be-api fts) for "Sieyès" returns one matching volume
   with several snippets, all Prussian foreign-ministry correspondence *about* or *with* Sieyès at Berlin in the
   same window — e.g. "Alvensleben. 1798 Juli 5. Sieyes bei dem König", "Berlin 1798 August 7... Sieyès s'est
   rendu il y a quelques jours chez moi", "Graf Haugwitz an den Grafen Finckenstein. Berlin 1798 August 25.
   Sieyès..." — but these are Prussian ministers' own despatches referencing meetings with Sieyès, not the
   Talleyrand-Sieyès letters themselves, and none of the dates matches P 1839/5, /21, /28 or /41 exactly.
   Inconclusive: this edition covers the same milieu closely (within a fortnight of P 1839/5's 17 July date)
   but no direct match confirmed. Pallain and Guyot, *Le Directoire et la paix de l'Europe*, not checked this
   session (budget) — flagged as the next print-check step in any future pass on this target.
3. **Lists.** `sources/cryptiana/web/`: grep for Talleyrand/Sieyès/Rastatt hits only `napoleon2.htm` (Takagi's
   *Napoleon and Talleyrand*, 1814 context) and `madison.htm` (Livingston-Talleyrand bribe reference, 1802-04,
   US legation cipher) — both a different Talleyrand cipher, a different period, unrelated to this 1798 Rastatt
   correspondence. No hit in `sources/cryptiana/blog/`. Live Cipherbrain/Cipher Mysteries not fetched (budget).
4. **DECODE.** Cannot log in (ASKS row 1). Cached catalogue snapshot (`aaymeloglu/unsolved-ciphers/catalogue/
   decode-catalog.csv`, 10,107 rows): zero hits for Talleyrand, Sieyès/Sieyes, Rastatt, Konstanz or Wessenberg.
5. **Bourdeau.** Fresh shallow clone, 24 Sept 2026. `grep -ril -iE` for the same terms: the only "Talleyrand"
   hits are `napoleon/` corpus files (Napoleon-era, different period) and `soglia1848/blog.txt` and
   `fagel1804/NOTES.md` (both name Talleyrand as a subject mentioned inside a different cipher's nomenclator or
   correspondence, not as sender/recipient of this item). No Sieyès, Rastatt, Konstanz or Wessenberg hit.
6. **Aymeloglu.** Fresh shallow clone, 24 Sept 2026. Same grep, no hit beyond the cached DECODE catalogue
   already covered under source 4.

**Verdict: open**, stage 2 verified unsolved (conditional — catalogue-metadata match only, no image seen; the
Bailleu print check is inconclusive rather than negative and should be redone with the exact three dates before
this target is treated as fully clear). Copy-order target: no digitisation found at Stadtarchiv Konstanz. See
`REQUEST.md`.

Requests this pass: archive.org 2 (advancedsearch + be-api fts on `preussenundfran01bailgoog`), github.com 2
(shallow clones, shared with K1/K3/K4). No TNA Discovery, no Google Books.
