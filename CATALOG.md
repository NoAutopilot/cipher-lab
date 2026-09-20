# Catalogue of unsolved historical ciphers

Derived from Cryptiana's "Unsolved Historical Ciphers" index page as of 19 September 2026
(`sources/cryptiana/web/unsolved.htm`). The page's author warns that many solutions arrived in
September 2026 that he has not yet recorded, mostly from Daniel Bourdeau. **Before working on
anything below, check https://dbourdeau.github.io/cyphersolver/ and Andrew Aymeloglu's
https://github.com/aaymeloglu/unsolved-ciphers.**

Status key: **Open** = no solution reported. **Partial** = key partly recovered or some letters in
a group solved. Items marked Solved on the index page are listed separately at the end so nobody
re-solves them.

"Page" is the file under `sources/cryptiana/web/` unless it says blog. "Folder" is a working folder
under `ciphers/` when one exists.

## Corrections from the solver repositories, 19 September 2026

Two AI-driven projects swept this list in the week before the snapshot: Daniel Bourdeau's cyphersolver
(99 targets) and Andrew Aymeloglu's unsolved-ciphers. Their trackers change the status of most rows below.
The full reconciliation is in `LANDSCAPE.md`; the short version:

- **Solved or read since the snapshot:** Charles I-Boswell 1643 (Pitt, Bourdeau), Henry of Navarre to Ségur 1585-86
  (Bourdeau; the sender is Navarre, not Henry III), Bordeaux 1653 (Bourdeau, with the English key sheet DECODE R7537),
  Ottobon 1589 (Aymeloglu), Vande Perre 1653 (Aymeloglu, not on the list), Davison 1584 (found in print).
- **Partial with a published key:** Moray 1568 (Aymeloglu, 119 of 134 glyphs), Starhemberg 1758 (Aymeloglu),
  royalist intercept 13 May 1646 (Aymeloglu, Digby key 129, 45 values), Isle of Wight 1648 (two keys excluded).
- **Closed-negative against matched controls, pending images or a key:** SP53/16 nos. 78-79, SP53/22 f.52,
  Birago 1571, Colbert 1665-75, Chaulnes 1690, Joyeuse 1594, du Croc 1567, Cocquet 1616, Thurloe pieces,
  Vatican Challenge 5, Beverning-Vande Perre to Boreel 1653.
- **Offline-only, the key or text is located but not online:** Hamilton 1650 (NRS GD406/1/2197), Stepney 1702,
  Maurice-Rupert 1645 and the 1646 intercepts (BL offline), Torcy and Villars 1710 (dead transcription links),
  d'Estaing 1779 (AAE), Berthier 1812 and Marmont 1807 (Vilcoq 1969 not digitised), Blancmesnil (fr. 3633 not digitised).
- **Not a cipher:** Hyde's superscriptions (nulls).

The tables below keep the statuses as Tomokiyo's page had them on 19 September 2026, so the two can be diffed.

## Open and partial items

### Italian and Latin, 1520s

| Item | Date | Status | Where | Page | Folder |
|---|---|---|---|---|---|
| Venetian? cipher with superscript digits, letter to Seigneur Garbino; also Hieronimo Ranzo letters and a Madrid memoire | 1528 | Open | BnF Clair.327 ff.279-280; BnF fr.2988 f.2, f.9; fr.3019 f.73; fr.3022 f.44 | venetian.htm, spanish2C.htm | |
| Serno Gilino's Latin letter with two-digit superscripts | 1527 | Open | (with Bishop of Worcester papers) | henryviii.htm | |

### English, Elizabethan

| Item | Date | Status | Where | Page | Folder |
|---|---|---|---|---|---|
| Throckmorton to Elizabeth, marginal ciphertext in unknown cipher (DECRYPT 2988) | 1559 | Open | BL Add MS 4136 | elizabeth.htm | |
| John Wood to Cecil, on same sheet as DECRYPT 2989 | 1568 | Open | BL Add MS 4136 | elizabeth.htm | |
| Moray-Wood cipher, Regent Moray to John Wood | 1568 | Open | BL Add MS 32091 f.213 | elizabeth.htm, elizabeth_moray.txt | moray-wood-1568 |
| Anonymous letter to Mr Tempest, Paris | 1585? | Open | TNA SP53/16 no.78 | mary.htm, SP53_16_78.txt | sp53-16-78 |
| Anonymous letter to Dr Barret, Rheims, same hand | 1585? | Open | TNA SP53/16 no.79 | mary.htm, SP53_16_79.txt | sp53-16-79 |
| "Cifer with Spanish Spye", short text; also verso of key f.40 | c.1586 | Open | TNA SP53/22 f.52 | mary.htm | sp53-22-f52 |
| Robert Bowes to Walsingham | 1583 | Open | see page | elizabeth.htm | |
| William Davison to Walsingham | 1584 | Open | see page | elizabeth.htm | |
| Short ciphertexts in Cotton MS Caligula B VIII | | Open | BL | elizabeth.htm | |

### Spanish

| Item | Date | Status | Where | Page | Folder |
|---|---|---|---|---|---|
| Last ten lines of Ferdinand's letter to Garcilaso de la Vega, Rome | 1498 | Open | see Parisi (2004) p.115 | spanish.htm; blog 2019_01_two-more | |
| Viceroy of Sicily to Ferdinand (no.94) | 1503 | Open | BnF Esp.318 ff.120-121 | spanish.htm; blog 2019_01_unsolved-spanish | |
| Lorenzo Suarez to Ferdinand and Isabella, Venice (no.93) | 1504 | Open | BnF Esp.318 f.118 | spanish.htm | |
| Letter of 8 Jan 1497 (no.95) | 1497 | Partial (Lasry 2022, approximate) | BnF Esp.318 f.122 | GL.htm | |
| Charles V letter of 26 December | 1521? | Open | see page | spanish2.htm (SEC5b) | |
| Two Juan Manuel letters lacking plaintext (key otherwise reconstructed) | 1521-22 | Partial | BRAH R9499-R9529 in DECODE | AlonsoSanchez.htm | |
| Report to Charles V, and Gasto's second cipher | 1527 | Partial (Lasry 2026, three-letter codes unidentified) | BnF fr.3022 f.16 etc. | GL.htm (SEC3), spanish2.htm | |
| Matheo de Segura to Constable of Castile, short passage | 1596 | Open | BnF es.336 f.196 no.99 | GL.htm | |

### French, to 1610

| Item | Date | Status | Where | Page | Folder |
|---|---|---|---|---|---|
| Earliest French ciphers of Francis I's reign, remaining unsolved ones | 1526-30 | Partial (four solved) | see page | francis.htm | |
| Catherine de Medicis to Philibert du Croc | 1567 | Open | Destray (1924) p.53 and plate | henryiii.htm | |
| Lodovico Birago to Duke of Nevers, numerical paragraph | 1571 | Open | BnF fr.3251 f.119 | nevers.htm | birago-nevers-1571 |
| Blancmesnil to Duke of Nevers, phrases in cipher | | Open | BnF fr.3633 f.24 | nevers.htm | |
| Guise? letter f.151, short, different key | c.1581 | Open (probably too short) | BnF fr.15564 f.151 | henryiii.htm, GL.htm | |
| Henry III to Segur, ff.143, 233, 239, 288v | 1583-86 | Open | BnF 500 de Colbert 401 | henryiii.htm (SEC1) | |
| Henry IV to Savary de Breves | 1610 | Partial (Lasry 2021, significant part) | see page | louisxiii.htm | |
| Marie de Medici to de Breves, short passages | 1610 | Open | see page | louisxiii.htm | |

### Vatican and Italian

| Item | Date | Status | Where | Page | Folder |
|---|---|---|---|---|---|
| Vatican Challenge Part 5, Cardinal Farnese to nuncio | 1542 | Open | MTC3 level X | vatican.htm; blog 2019_08 | |
| BnF fr.4715 no.62 (f.85) | c.1590 | Partial (Lasry 2022, interim) | BnF fr.4715 | bnf4715.htm | |
| Undeciphered letters in BnF fr.4712 | c.1590 | Open | BnF fr.4712 | nevers.htm | |
| Cardinal de Joyeuse to Villars, left undeciphered by Viète | 1594 | Open | Cinq Cents de Colbert 33 f.539 | viete.htm | |
| Cocquet to Mangot, Rome | 1616 | Open | BnF Clair.369 f.316 | louisxiii.htm | |
| Fragments in Sertori's "novel cipher" solved by Valle de la Cerda | c.1590s | Partial (Caballero 2012 close) | BN Madrid Ms.994 | valle.htm | |
| Fra Guglielmo Vizani | 1637 | Open | see page | louisxiii.htm | |

### German and Habsburg

| Item | Date | Status | Where | Page | Folder |
|---|---|---|---|---|---|
| Future Ferdinand III to Trauttmansdorff | 1634 | Open | SOA Pilsen, Trauttmansdorff archive, carton 6 no.68 | (Mírka 2012) | |
| Other sheets in DECODE R1579 (images I7060, I7066, I7068) | c.1640 | Open | DECODE R1579 | habsburg.htm | |
| Ferdinand III to Cardinal-Infante, old-style cipher with graphic symbols | 1634 | Open (R1889 and R1890 solved by Aymeloglu Sept 2026) | DECODE R1887 | | |
| Third of three variable-length figure codes | 1627/1644 | Open (R2159 and one other solved by Bourdeau Sept 2026) | DECODE R1408 or R2179 | variable2.htm | |
| Georg Adam Starhemberg's variable-length code | 1758 | Open | see page | variable2.htm (Starhemberg) | |

### French, 17th century

| Item | Date | Status | Where | Page | Folder |
|---|---|---|---|---|---|
| Sabran, passages in letter to "Mr de ch.gr" | 1630s | Open | see page | servien.htm, louisxiii.htm | |
| Antoine de Bordeaux, ambassador in England | 1653 | Open | BL Add MS 4200 f.88; DECODE R8390 | louisxiv0.htm (SEC3) | |
| Prince of Condé to Barrière; also f.101 | 1654 | Open | BL Add MS 4200 f.98, f.101; DECODE R8395, R8398 | louisxiv0.htm (SEC4) | |
| Duke of Charost, short paragraph | 1673 | Open | Mélanges de Colbert 172 f.23 | louisxiv0.htm | |
| Abbé de Gravel to Maulevrier | 1674 | Open | Mélanges de Colbert 168bis f.553 | louisxiv0.htm | |
| A few words in cipher | 1665 | Open | Mélanges de Colbert 127 f.349 | louisxiv0.htm | |

### English Civil War and Restoration

| Item | Date | Status | Where | Page | Folder |
|---|---|---|---|---|---|
| Charles I to Boswell, and Nicholas to Boswell | 1643 | Open | TNA | blog 2021_09_charles-i-boswell | |
| Charles I and Henrietta Maria private cipher, passage of 8 April | 1645 | Open | see page | charlesi.htm | |
| Charles I in the Isle of Wight, two of four letters | 1648 | Partial (two solved 2021) | see page | charlesii.htm (SEC1), charlesi2.htm | |
| Prince Maurice to Prince Rupert, Worcester | 1645 | Open | Warburton, Memoirs p.133 | charlesi.htm | maurice-rupert-1645 |
| Intercepted royalist letter | 1646 | Open | BL Add MS 72438 f.9r; DECODE R8623 | | intercepted-royalist-1646 |
| Intercepted letter to Charles I | 1646 | Open | BL Add MS 72438 f.10; DECODE R8624 | | |
| Baron Craven to Prince Rupert, The Hague | 1648 | Open | BL Add MS 18982 ff.134-135; DECODE R8447 | | |
| Charles II to Duke of Hamilton, passages | 1650 | Open (key may be in Wallis papers, Bodleian) | see page | charlesii.htm (SEC2) | |
| Intercepted letter of Hyde | 1659 | Open | BL Add MS 4166 ff.92-93; DECODE R4886 | thurloe.htm | |
| Short intercepted letter in Thurloe vol.7 | c.1659 | Open | Thurloe State Papers vol.7 pp.860-869 | | |
| Ormond to Arran, short segments | 1678 | Open | Ormonde MSS vol.4 p.93 | charlesii2.htm | ormond-arran-1678 |

### Commonwealth intercepts

| Item | Date | Status | Where | Page | Folder |
|---|---|---|---|---|---|
| Dutch letters, e.g. Beverning and Vande Perre to Boreel | 1653 | Open | Thurloe State Papers | dutch.htm | |
| Intercepted letters: du Gard to White (10 June), Brussels (12 Aug), Jo. Waddall (22 Aug) | 1656 | Open | Thurloe State Papers vol.5 | | |

### French, Louis XIV to the Revolution

| Item | Date | Status | Where | Page | Folder |
|---|---|---|---|---|---|
| Louis XIV's instructions to Castaignère, Constantinople | 1690 | Partial (Tomokiyo) | Rycaut, History of the Turks p.453 ff. | louisxiv2.htm, davys_e.htm | |
| Louis XIV's instructions to Duke of Chaulnes, Rome | 1690 | Open | see page | louisxiv.htm (SEC4B) | |
| Marshal Catinat's despatch of 15 September | 1702 | Open | see page | louisxiv.htm (SEC9) | |
| Torcy to French ministers at Geertruidenberg, "Blencow cannot decypher" | 1710 | Open | BL Add MS 61575 ff.38-41; DECODE R8755 | blencowe2.htm (Torcy) | |
| Marshal Villars to Abbé de Polignac | 1710 | Open | BL Add MS 61575 f.44; DECODE R8756 | blencowe2.htm (Villars) | |
| Admiral d'Estaing to Gérard, intercepted | 1779 | Open | Clements Library, Clinton Papers 64:14 | marbois.htm | destaing-gerard-1779 |

### Miscellaneous and Napoleonic

| Item | Date | Status | Where | Page | Folder |
|---|---|---|---|---|---|
| George Stepney to Earl of Manchester, Vienna | 1702 | Open | Manchester Papers | | stepney-manchester-1702 |
| Encoded letter to Marshal Marmont | 1807 | Open | Vilcoq (1969) | napoleon2.htm | |
| Berthier to Napoleon, duplicate in Neufchâtel cipher | 1812 | Open (contemporary decipherment likely exists) | Vilcoq (1969) | napoleon2.htm | berthier-napoleon-1812 |
| Armstrong to Madison, unique code, 20 February | 1808 | Open (a claimed solution is disputed) | see page | madison_armstrong.htm | |

### Telegraphic age and Enigma

| Item | Date | Status | Where | Page | Folder |
|---|---|---|---|---|---|
| British consulate at Lüderitz to Foreign Office, 43 five-figure groups | 1911 | Open | Klaus Schmeh's blog, 15 Jan 2016 | | |
| Japanese diplomatic telegram printed by Yardley, p.251 | c.1920 | Open (solved by Cipher Bureau at the time; solution not public) | The American Black Chamber | meiji.htm (SEC7), yardley.htm | |
| Telegrams from the sunken warship Zhongshan, 539 of 891 unsolved as of 2009 | c.1938 | Open (primary sources not located) | Zhongshan Warship Museum | chinesecrypto_e.htm | |
| Two telegrams Switzerland to London, "BLUME SALAMANCA" | 1937 | Open (IC matches English, maybe transposition) | Schmeh's Facebook | blog 2023_09 | |
| Enigma message from Oberbefehlshaber Oberrhein deputy | 10 Jan 1945 | Open | Schmeh's blog, 7 Jan 2019 | | |

## Solved, per the index page (do not re-solve)

Recent wave, September 2026, so not yet widely known:

- Richelieu to Rancé (1629), Bourdeau. See richelieu1629.txt.
- Ormonde-Maltravers (1634-35), Bourdeau.
- Richard Forster, possibly to Henrietta Maria (1644): Lasry, then Biermann, then Pitt, Aymeloglu and Bourdeau independently. Simple homophonic substitution.
- Le Tellier-Castelnau (1657), Pitt. See LeTellier_Castelnau1657.txt.
- Hyde's superscriptions (1659-60) are nulls, not a cipher, per the printed edition. Bourdeau.
- Catinat despatch (1691), Bourdeau. See catinat1691.htm.
- Two of three variable-length figure codes (R2159 "Lucca" and "Warsaw"), Bourdeau.
- Cardinal-Infante correspondence R1889 and R1890 (1635, 1640), Aymeloglu.
- Ottobon to Mocenigo (1589), Aymeloglu. Key is "Ziffra prima", DECODE R1789.
- Armstrong to Madison postscript (30 Aug 1808), Bourdeau.
- Sun Yat-sen telegram (1916) and Huang Xing telegram (1916), Bourdeau.
- Confederate Navy dictionary code (1863): dictionary identified as Webster's Primary School Dictionary, 1850 printing, by Reddit user offgramercy, August 2026.
- Bishop of Worcester's superscript cipher (1526, 1529): decryption published, per Aymeloglu.
- Milroy telegrams (1862), Richard Bean, 2026.

Earlier: Mary Queen of Scots collections (2023), SP53/11 no.50, SP53/16 nos.28(3), 29(2), 29(3), SP53/18 no.64, Mary-Grange (1571), misplaced English cipher in BnF fr.2988, Catherine of Aragon (1509), the 1504 "Spanish" letter (actually English, John Stile 1514), Perez to Charles V (1527), Figueroa (1529), Charles V to Saint-Mauris (1547), Simancas 1551 letters, Idiaquez (1577), Vargas Mexia keys, most BnF items in GL.htm, Hurault, Guise 1556 and 1581, Charles IX to du Croc, Danzay (1574), Villeroi (1577), Duke of Lorraine (1592), Schiner (1520), papal ciphers, Vatican Challenges 1-4, Bellaso, Viète f.555, D'Estrades (1647), Trithemius, Wallenstein, Ferdinand III and Leopold, imperial ministers, Rabenhaupt, Frederick I transposition, Sabran (mostly), Richelieu (1641), Brasset to Mazarin (1649), Mazarin to Bordeaux (1654), Ormonde-Clanricarde (1644), Maurice to Digby (1645), Charles II pseudonym (1655), Chesterfield memoirs (1659), Louvois to Lauzun (1690), Perwich (1670), Euler (1744), Madison-Mazzei (1780), Patterson (1802), Poe's Tyler cryptograms, Johnston to Lee (1862), Macdonald telegrams, Enigma 1942, Zodiac Z340, running key challenge.
