blocked

**Edition check (LANE N3 csED2, 24 Sept 2026 16:17 UTC):** hold not lifted -- the named series (Nuntiaturberichte
aus Deutschland III. Abteilung; Acta Nuntiaturae Gallicae) is identified down to the specific volume but is a
modern critical edition, not digitised on this pass's granted hosts. Brief
`.claude/briefs/runs/2026-09-24-lane-n3-csED2.md`.

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

## Edition check, LANE N3 csED2, 24 September 2026 (IA + Gallica SRU slots)

**Nuntiaturberichte aus Deutschland, III. Abteilung (1572-85) -- the specific volume identified, and it is not
reachable.** WebSearch (24 Sept 2026) finds the Delfino/Portia nunciature at Rudolf II's Prague court
(1577-1578) is III. Abteilung **Band IX**, edited by Alexander Koller, published Tübingen, 2003 -- a 21st-century
critical edition. Not on archive.org: `advancedsearch.php?q=title:(acta nuntiaturae gallicae)` returns 0 hits
(the Gallicae series is the parallel French one, checked for the sibling row CS2-04 and equally absent); the
archive.org Nuntiaturberichte holdings found by WebSearch (`bub_gb_JjaxAAAAIAAJ`, `nuntiaturberich11romgoog`,
`bub_gb_IjWxAAAAIAAJ`, `bub_gb_5zKxAAAAIAAJ`, `bub_gb_yCqxAAAAIAAJ`) are all I. and II. Abteilung (1533-1572)
Google-Books-era scans, all predating this volume and out of date range; none is Band IX. No HathiTrust record
found by WebSearch either. **Not reached this pass; still the gate for this row.**

**Venetian dispatches from the Imperial court, 1577** (the softer lead this row's brief also names): not pursued
this pass beyond the WebSearch above -- a Calendar of State Papers Venice volume covering 1577 would report a
Venetian ambassador's own business, not print L'Abbé's (a French agent's) cipher passages even if it mentioned
him, so it could not itself answer "are the cipher passages printed" the way the primary series could. Flagged
as a lead only, not chased further (in-budget triage, not a search failure).

No change to the underlying verdict: Bourdeau's own two-session attempt (`labbe1582/`, `REASSESSMENT.md`) remains
the deepest source, and this row's own fr. 4695 no. 51 lead (a possibly-surviving earlier cipher enclosure) is
still unlocated.

Credit: unchanged from the check-solved pass (D. Bourdeau, cyphersolver, `labbe1582/`). Rule 10: no novelty claim
made.

## Solver-repo check (bourdeau, 2 Oct 2026)

Fresh shallow clone of github.com/dbourdeau/cyphersolver, HEAD 34e0fc89 (1 Oct 2026), diffed against this folder on 2 Oct 2026 (worker SOLVERDIFF-BOURDEAU, sources/solver-diffs/2026-10-02-bourdeau.tsv). Match class b (they attempted it and closed or explained it).
- Their page: https://github.com/dbourdeau/cyphersolver/blob/main/targets/labbe1582/NOTES.md ; targets/labbe1582/REASSESSMENT.md
- Their extent, in their words: attempted, open: cipher not read; renewed attempt 23 Sept with failed cryptanalytic tests and a passed synthetic control
- Their date: 23 Sept 2026
- Note: already cited in our NOTES.md
Credit: D. Bourdeau, cyphersolver (code MIT, text CC BY 4.0). Status line unchanged; the parent decides any status change from the ROOM flag.

## Web and blog check (CS-BATCH1, 3 Oct 2026)

Queries (WebSearch, standard, 3 Oct 2026): (1) `Desiderio l'Abbé Nevers Prague 1577 cipher Rudolf II "l'Abbé" lettres chiffrées Français 3198` -> HistoCrypt 2019/2021 papers on Nevers ciphers, Source Library items on Rudolf II's 1597 cipher tools: nothing on fr.3198 nos.30/37; (2) four Cryptiana/Cipherbrain/Cipher Mysteries variant searches: no page naming l'Abbé 1577. Local: grep of `sources/cryptiana/web/nevers.htm`, `league.htm` for "3198", "labb", "l'abb": only an unrelated "monsieur l'abbé d'Orbais" (nevers.htm no.62, f.126); no fr.3198 section. Not found. Blog comment threads not opened.

## Premise check (CS-BATCH1, 3 Oct 2026)

(a) Folder's own files: the 2 March letter cites the 24 Feb 1577 enclosure ("copie de la chiffre"); fr.4695 no.51 named as possible key/crib -- not located. No decipherment mentioned. Not found.
(b) Other solvers' working files: `sources/cyphersolver/` disk snapshots (2026-10-01..03) contain no labbe1582 folder (only Bourdeau's mercy1648 notes mention an unrelated "Desiderio" hit); recorded via 2 Oct diff, class b. Not found.
(c) Physical neighbours: not viewed (no vision calls). The second witness of the Breslau letter (no.38, f.76) is a neighbour to check for a clear copy.
(d) Recipient/edition side: Nuntiaturberichte III. Abt. Bd. IX (Koller, 2003) identified, not reachable online; Gomberville not read here. Unreachable. Verdict remains `blocked`.

## While waiting

The one action that depends on nobody: Tomokiyo's fr.4695 pages (bnf4715.htm and neighbours on disk) searched for the 5 Feb 1577 no.51 key, disk-only, ~USD 0.3; then a Gallica fr.4695 manifest lookup (1 request). Status stays `blocked`.

## Next step (NO-CRACKS, 5 Oct 2026)

next: search Tomokiyo's fr.4695 pages on disk (bnf4715.htm and neighbours) for the 5 Feb 1577 no.51 key, disk-only, ~$0.3; then one Gallica fr.4695 manifest lookup. Who acts: agent. Source: this file's "## While waiting"; written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.

## RUN6-LABBE (5 Oct 2026, 05:39-05:42 UTC by date -u)

Disk grep, sources/cryptiana (web/*.htm, blog, keys, CRYPTO-INDEX/READABLE/PAPERS tsv, md): "4695" 0 hits in Tomokiyo's pages
(bnf4715.htm is fr.4715, a different Nevers volume, not 4695; nevers.htm's volume list has fr.4715 but no fr.4695). Also no Prague/Rudolf/Desiderio hit
in nevers.htm. So Tomokiyo carries nothing on fr.4695 no.51 or a 5 Feb 1577 key. Not found in the local snapshots (a search result, not a novelty verdict).
Gallica: 1 SRU query (`gallica all "Français 4695"` and `dc.type all "manuscrit"`, 3 hits) gave fr.4695 =
https://gallica.bnf.fr/ark:/12148/btv1b90582923, "Recueil de pièces originales et de copies concernant l'histoire des années 1574 à 1590"
(digitised). 1 manifest read (tools/gallica_folio.py): 209 canvases, all labelled 'NP', 0 folio labels, so "no.51" cannot be mapped to a canvas
from the manifest; canvas 1 is 8400x5896 and ~7800x5600 after. Re-fetch: `python3 tools/gallica_folio.py btv1b90582923 --list`.
No decoding, no images viewed. Requests: gallica.bnf.fr 2 (SRU 1, manifest 1), both 200.
Next (agent, ~USD 1.5): fetch the BnF archivesetmanuscrits record for fr.4695 (item list: does "no.51" = a piece number, with folio range and
5 Feb 1577 date) to give --anchor canvas=folio pairs; then view the candidate leaf at native resolution via tools/iiif_lines.py. Status stays `blocked`.

## D2-F3198 (5 Oct 2026, 23:02-23:08 UTC by date -u) -- fr.4695 no.51 located; it announces the cipher, but the key sheet is not bound with it

Step 1 (Tomokiyo on disk) had already run (RUN6-LABBE, 0 hits); not repeated.
Step 2, catalogue: the Gallica manifest's Relation field gives the BnF record, https://archivesetmanuscrits.bnf.fr/ark:/12148/cc57745v
(curl, 200). Piece list: **"Fol. 116 . 51 Lettre de « D. LABBE » au duc de Nevers. Prague, 5 février 1577."** [FRBNFEAD000057745_d0e491].
The record does not mention cipher. Neighbours: nos.47-50 Guazzo (ff.108ff), no.52-53 Guazzo (ff.118, 120), and a later l'Abbé sibling,
**no.55, fol.125, "De Prague, ce 20 d'apvril 1577"** (also nos.40, f.94, Vienna 1 Apr 1576; 42-44, ff.98ff, Ratisbon Jul-Aug 1576).
Canvas mapping (eye-checked folio stamps, 1000-px views): canvases are two-page spreads; canvas 118 = ff.108v/109r, canvas 125 =
ff.115v/116r, 126 = 116v/117r, 127 = 117v/118r. So recto f.N sits on canvas N+9 in this range (anchor pairs 118=109r, 125=116r, 127=118r).
Step 3, native crops (mandatory crop step, commands run):
`python3 tools/iiif_lines.py --ark btv1b90582923 --canvas 125 --region 3780,0,3500,5400 --lines-per-crop 6 --prefix f116r --out ciphers/fr3198-labbe-1577/images`
`python3 tools/iiif_lines.py --ark btv1b90582923 --canvas 127 --region 600,1900,3200,700 --lines-per-crop 8 --prefix f117v_date --out ciphers/fr3198-labbe-1577/images`
(the line finder caught only 16 of ~45 lines on f.116r; the fetched native region was read in four strips instead).

What the leaf is: no.51 runs ff.116r-117v, four pages of clear French in l'Abbé's hand. f.116r opens with receipt of Nevers's letters of
14 November via "le s.r Ancel secretaire du Roy", the condolences for the late emperor, and the s.r Barquin. Read at native resolution on
f.116r, line ~22: **"Je vous envoye presentement la chiffre affin que ie vous puisse escripre plus librement."** f.117v ends "... de Prague
ce 5.e de febvrier 1577", a postscript naming "s.r Rina", the subscription "D. L'Abbé", and the address "A Monseigneur ... le duc de Nevers"
with a dorse endorsement. f.118r is Guazzo's Italian letter (no.52).
Cipher: no numeral cipher groups seen on f.116r (native strips) or on ff.116v-117v (1000-px views only, not native -- small inserted groups
there are not excluded). **No key sheet / cipher table is bound at ff.116-117**: the enclosure the letter announces is not with it in fr.4695.
So this letter confirms that a key went from l'Abbé to Nevers with the 5 Feb 1577 dispatch (consistent with the 2 March letter's "copie de
la chiffre que je vous envoyay avec mesdictes dernieres"), but it is not itself a crib or key source.
Not decoded; no transcription. Not found: the key sheet, in fr.4695 ff.115v-118r.
Requests: gallica.bnf.fr 7 (manifest 1, 1000-px views 4 [canvases 118, 125, 126, 127], native regions 2 via iiif_lines), archivesetmanuscrits.bnf.fr 1; all 200.

Next steps (one-line suggestions, not run): (a) no.55, f.125 (canvas 134 by the +9 offset, Prague 20 Apr 1577, after the key arrived):
one native view for inserted numeral groups -- a third cipher letter in the same key, ~USD 1; (b) the detached key sheet may be in another
Nevers volume: search the archivesetmanuscrits fr.3198-3200 / fr.4695-4715 piece lists for "chiffre" with l'Abbé's name, ~USD 1.
Status stays `blocked` (line 1).
