blocked

# Desiderio l'Abbé to Nevers, Prague and Breslau, 2 March & 2 May 1577 — BnF fr. 3198 nos. 30, 37

QUEUE row: CS2-28 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 284 at dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September
2026 by LANE N3 csCS2b (session_01711qcbvcwvGDsSAtVXwfJB), brief `.claude/briefs/runs/2026-09-24-lane-n3-csCS2b.md`.

## What it is

Two dispatches from Desiderio l'Abbé (Nevers's agent at Rudolf II's imperial court) to the duc de Nevers: from
Prague, 2 March 1577 (no. 30, ff.62–66, canvas f63 onward), and from Breslau/Wratislavie, 2 May 1577 (no. 37,
f.75, canvas f77; a second witness of the same letter is no. 38, f.76). Both are mostly legible clear French
reporting on the imperial court, Báthory, Polish and Silesian affairs, Ottoman rumours, and Nevers's Mantua
business, with cipher numeral insertions at the sensitive points. D. Bourdeau's own working folder
(`labbe1582/`, sessions of 21–23 September 2026, including a renewed attempt) measured 834 draft digits in the
Prague letter and 77 in the Breslau letter, tested over 1,500 prefix/pairing/null configurations and validated
his solver on a synthetic control (538/538 letters recovered) — the real cipher does not yield continuous
French under any tested key. The March letter itself references an earlier cipher dispatch of 24 February 1577
("copie de la chiffre que je vous envoyay avec mesdictes dernieres"), pointing to a possibly-surviving earlier
enclosure (BnF fr. 4695 no. 51, not yet inspected) as the best lead for a crib or key — not located this pass.

## Six-source search log (24 September 2026)

1. **Tomokiyo (sources/cryptiana/ on disk).** No sentence in the local snapshot names fr. 3198, Desiderio
   l'Abbé, or the Prague/Breslau 1577 letters (grep across `sources/cryptiana/web/*.htm` for "3198",
   "Desiderio", "Prague", "Breslau": only unrelated hits — a different Prague cipher in `venetian.htm`/
   `german.htm`, San Clemente's Prague letters in `viete.htm`, l'Abbé d'Orléans (a different "l'Abbé") in
   `viete.htm`). Bourdeau's own search log records the same: no relevant published transcription or key found
   in Cryptiana.
2. **Standard printed edition — this lane's own instruction is explicit.** Per this lane's brief: "for CS2-28
   ... the Nevers papers editions and Imperial-court nunciature/Venetian series -- read the volume's text for
   the date on archive.org (IA slot), or the verdict is `blocked` with the volume named." archive.org is held
   by csED this pass and was not available to this worker. Bourdeau's own search ("renewed searches for
   L'Abbé, Nevers, Prague/Breslau 1577 ... found catalogue leads, not a key or reading. This is not a claim to
   have searched every printed edition") likewise did not read Gomberville's *Mémoires du duc de Nevers* (1665)
   or the Imperial-court nunciature/Venetian series (e.g. the *Nuntiaturberichte aus Deutschland* / *Acta
   Nuntiaturae* volumes for Rudolf II's Prague court, 1576–78) for these dates. WebSearch/WebFetch located only
   a private catalogue mirror pointing to a possibly-related earlier letter (fr. 4695 no. 51, 5 Feb 1577), not
   an edition text.
3. **DECODE (sources/decode/) + both solver-repo clones.** No DECODE record found for fr. 3198 nos. 30 or 37 in
   the local snapshot (grep for "3198": no hit in either records TSV). dbourdeau/cyphersolver (shallow clone,
   24 Sept 2026): `labbe1582/NOTES.md` and `labbe1582/REASSESSMENT.md` give by far the fullest account (above);
   verdict "attempted, open — cipher not read... Move on pending better evidence." Escalation checklist run
   twice (siblings, clear-pages, known-keys, print, key-rebuild, retry all [x], each explicitly caveated as
   bounded, not exhaustive). aaymeloglu/unsolved-ciphers: fresh shallow clone, no hit for "3198", "Desiderio",
   or "l'Abbé".
4. **Web search** (Desiderio l'Abbé Nevers Prague 1577 chiffre BnF fr.3198): only the BnF catalogue record and
   generic Wikipedia results (unrelated people named "Abbé"/"Desideri") surface; no solution, key or edition
   text found.
5. **Ciphertext confirmed present on the Gallica leaf.** IIIF fetch, gallica.bnf.fr, 24 Sept 2026, 1 request:
   `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060073v/f63/full/500,/0/native.jpg` (f.63, opening of no. 30).
   Image shows a two-page spread of dense French cursive prose with numeral cipher groups inserted mid-line on
   both pages, matching Bourdeau's description of the Prague letter's dispersed cipher insertions. Leaf:
   https://gallica.bnf.fr/ark:/12148/btv1b9060073v/f63.item

## Verdict

**Blocked, not open — per this lane's own brief for this target.** No source of the six claims a decipherment
or a validated key; Bourdeau's own attempt (by far the deepest single source, two full sessions) explicitly
declines to claim exhaustive coverage of the printed record. The brief for this row names the specific
condition: the Nevers-papers editions and the imperial-court nunciature/Venetian series must be read for the
date on archive.org, which is not available to this worker this pass (csED holds the slot). Unblocks when:
archive.org access lets Gomberville's *Mémoires du duc de Nevers* (1665) and the *Nuntiaturberichte aus
Deutschland*/*Acta Nuntiaturae Gallicae*-type series for 1576–78 be searched for these dates and for L'Abbé,
Báthory, Weber and Vieheuser (named in the clear text); and BnF fr. 4695 no. 51 (5 Feb 1577, the letter the
March dispatch says carried an earlier copy of the cipher) is inspected as a possible crib source.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 284; `labbe1582/`
working folder and `REASSESSMENT.md` — clear-text reading, digit inventories, 1,500+ key-configuration tests,
matched synthetic-control validation, the fr. 4695 no. 51 lead), CC BY 4.0 — prior attempt, substantial clear-text
research, cipher not read (not a solution).

Not decoded, not transcribed here (out of scope for check-solved). Rule 10: no novelty claim made; this is a
search result, not a verifier's classification.
