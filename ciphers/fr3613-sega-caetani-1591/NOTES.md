blocked
Meister 1906 (archive.org diegeheimschrift00meis, full text) read by this worker pp.420-421 and grepped whole-volume for Sega/Caetani/Rondinelli; no printed edition of Sega's 1590-91 letters could be opened (Acta Nuntiaturae Gallicae not on archive.org, searched 8 Oct 2026), so the verdict is blocked, not open.

# Sega (bishop of Piacenza) to Cardinal Caetani, Paris, 9 January 1591 -- BnF Français 3613 no.88, fol. 148

Job BNF-Q13-CS for LANE BNF-FOCUS (account 2), 8 Oct 2026, 00:02-~00:40 UTC. Status word: `blocked` (edition unread), not a negative.
BnF notice (sources/bnf-findingaids/2026-10-07/cc50063m.html, via tools/bnf_findingaid.py): "Lettre, avec chiffre, de FILIPPO SEGA, vescovo di Piacenza ... all' illmo ... Sor cardinale Caetano ... Di Parigi, li 9 di gennaro 1591. En italien." No decipherment flag.

## Leaf look (Gallica btv1b90582263, canvases unlabeled; canvas = folio + 9 here)
Canvas 157 = f.148r (clear Italian, addressed "Illmo et Rmo ... Cardinale"); canvas 158 = f.148v: the letter's last lines carry a block of about four lines of digits (single digits and two-digit groups, ~200 digits) inside the clear text, then "Di Parigi li 9 di Gennaro 1591", signed Sega. No interlinear or marginal decipherment, no slip, facing page (f.149r) blank. Viewed at 700-900 px only, not native.
Which cipher: not decoded. The digit repertoire (single digits for some letters, two-digit numbers in the 20s-40s) is the same kind as the Caetani table Meister prints, but that is a visual impression at low resolution, not a match. Tomokiyo's Jan 1591 Mayenne-Sega cipher: not compared.

## Key availability (unit 4)
Meister 1906 is on archive.org in full text (identifiers diegeheimschrift00meis, diegeheimschrift00meisgoog). pp.420-421 print "Cifra con Ill.mo signor cardinal Caetano legato in Francia, 28 Settembre 1589": five alphabets (1-5) with nulls 1, 5, 0, 10, 50, 11, 15, 51, 55, 00 and a word list (et, con, non, che, chi, per, perche ... V.S. Illma = 99), two-digit values 22-49 plus single digits for some vowels. The table prints in full in the OCR (djvu line ~92890). Meister footnote: Caetani, sent by Sixtus V 1589 to support the League (Ehses, Nuntiaturberichte I,2, p.LX). Meister p.~71 text (djvu line 6771) also mentions a cipher usage with "cardinal Sega legato in Francia". Whether Sega's letter to Caetani in Jan 1591 uses this 1589 table is untested; the cipher given to Caetani was for correspondence with Caetani, which fits the addressee.

## Prior-art search (what was checked, 8 Oct 2026)
- Bourdeau cyphersolver (shallow clone, grep of md/tsv/json): no hit for Sega, Caetani, Rondinelli, fr.3613. Existing folder ciphers/fr3984-sega-1593 concerns other Sega-era items (Baudouin-Desportes, 1593), blocked on Acta Nuntiaturae Gallicae too.
- Tomokiyo (sources/cryptiana/web, grep): polyalphabetic.htm line 126 names Caetani's cipher "four substitution tables numbered 1-5 (Meister (1906), p.420)", possibly broken by Chorrin; no mention of this letter.
- Meister whole-volume grep: no letter of Sega's printed, only keys.
- Desenclos and Lasry 2024 (NEALT 53): cited for fr.3615 f.52 interlinear (Henri IV, 19 Apr 1591); different volume.
- Not reached: Acta Nuntiaturae Gallicae / Nuntiaturberichte for the Sega legation; DECODE; Aymeloglu repo; HathiTrust; JSTOR.

## Web and blog check (BNF-Q13-CS, 8 Oct 2026)
Queries (WebSearch standard): "Filippo Sega Caetani 1591 lettera cifra Parigi decifrata"; "Cipher Mysteries OR Cipherbrain OR Cryptiana Sega legate France 1591 cipher Caetani Meister BnF". Hits: Penzi on Sega (Classiques Garnier, La Sainte Union, pp.157-173: Sega came with the Caetani legation), Desenclos and Lasry 2024, Lasry HistoCrypt Colbert 500/33. None mentions this letter. Blog site searches (Cipherbrain, Cryptiana blog, Cipher Mysteries) were not run as site searches; only the combined query above.

## Premise check (BNF-Q13-CS, 8 Oct 2026)
(a) folder: none existed before; BnF record names no decipherment: not found. (b) other solvers' files: Bourdeau none, Aymeloglu not checked: not found/unreached. (c) neighbours: f.148r-149r viewed at 700-900 px, no clear copy: not found. (d) recipient side (Caetani papers, Rome): unreachable.

## While waiting
Next step needing nobody: view canvas 158 native (iiif_lines.py) and see whether the digit groups fit the 1589 table's value set.

## Gate
```
ciphers/fr3613-sega-caetani-1591: blocked (line 1) -- already terminal, nothing to gate
exit 0
```
