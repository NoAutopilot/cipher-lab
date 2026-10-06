# WVO 1111 -- Wilhelm IV of Hesse to Willem van Oranje, Kassel, 14 Oct 1564 (reply to 1109): transcription

Job R8-WVO1111 (LANE LANE-RUN8-account-4, 6 Oct 2026). Source: `raw/01111.pdf` (Huygens WVO, KHAG original A 11/XIV B/15-19
per WVO's record; already on disk from R7-WVOH, not refetched). The PDF's embedded page images are ~312 ppi native
(`pdfimages -list`), so they were extracted as-is rather than re-rendered: `images/01111_p0_native.jpg`,
`images/01111_p1_native.jpg` (p2 = outer address leaf, viewed whole, not cropped).

Crop step (pasted):
```
python3 tools/iiif_lines.py --image images/01111_p0_native.jpg --out images/crops1111 --region 700,130,1460,2700 --prefix w1111p0 --lines-per-crop 1 --debug
  -> 23 lines, pitch 104 (debug overlay checked: one band per manuscript line)
python3 tools/iiif_lines.py --image images/01111_p1_native.jpg --out images/crops1111 --region 700,120,1520,2300 --prefix w1111p1 --debug
  -> 18 lines, pitch 102 (debug overlay checked)
```
Passes: two blind Sonnet passes per page (4 calls, one page per call, crop paths only, no WVO summary or incipit given);
reconciliation by this worker against stacked crops of p0 L05-L23 and p1 L01-L13 (one unit). Raw pass outputs are
summarised in NOTES.md (R8-WVO1111). Pass agreement was poor on the body (both passes marked every p0 row uncertain,
56-61 doubt marks per pass on p0), good on the dating clause and subscription.

Grades: **clear** = both passes and the reconciliation agree on every word; **uncertain** = at least one word is a
reconciler's reading not shared by both passes, or marked [?]. A [?] follows the doubtful word. This is a reading aid for
crib-hunting, not an edition; WVO's own incipit ("Wir haben E. L.ten schreiben de dato Brussell den 16ten Septembris
vonn ...") and Inhoud ("Dankzegging voor de 'Zeittungen' en bericht over de pest in Hessen") agree with it.

## p0 (first page)

| line | text | grade |
|---|---|---|
| p0_L01 | Vnser freundtlich dienst vnnd was wir | clear |
| p0_L02 | mehr liebs vnnd guts vermögen zuuor | clear |
| p0_L03 | Hochgeborner furst, freundtlicher | clear |
| p0_L04 | lieber Vetter Schwager vnnd Bruder, Wir | uncertain (Vetter/Vatter split; Vetter fits the address leaf "Vettern Schwagern vnd Bruedern") |
| p0_L05 | haben E. L. schreiben de dato Bruss[ell] | uncertain (passes "der Datum"/"vf dato"; WVO incipit "de dato Brussell") |
| p0_L06 | den 16ten Septembris vom gegenwertigen | uncertain ("16" clear; the reply cites **16** Sept, WVO dates 1109 18 Sept) |
| p0_L07 | brieffzeiger zu vnsern handen entpfangen | uncertain (pass A "Christoff Zeiger" rejected: one word, "brieffzeiger" = the bearer) |
| p0_L08 | gelesen. Thun[?] vns der mitgeschickten | uncertain |
| p0_L09 | zeitungen freundlichen bedancken, | uncertain |
| p0_L10 | wöllen E. L. gern hinwidder was vom[?] | uncertain |
| p0_L11 | zeitungen mittheilen, so[?] wir[?] sein[?] wir der | uncertain |
| p0_L12 | zeitten[?] dismals gar nichts zuzuschreiben, | uncertain |
| p0_L13 | dann[?] das das Sterben an der vergifften | uncertain |
| p0_L14 | Plage der Pestilentz[?] im Lande allenth- | uncertain |
| p0_L15 | halben grassiert, wie es dan auch alhier | uncertain |
| p0_L16 | vmb[?] vns allbereit[?] angefangen vnd sich nicht | uncertain |
| p0_L17 | allein zu weitter[?] [...] angezeigt[?], | uncertain |
| p0_L18 | Sondern auch gegen vnder die Kurchtr[?] | uncertain |
| p0_L19 | vnd den Marck[?] geratten[?], das zu besorgen, | uncertain |
| p0_L20 | wo es der Almechtige nicht wendet, | uncertain (wendet: reconciler + pass A) |
| p0_L21 | vnd das Sterben auch[?] [...] werdt[?], | uncertain |
| p0_L22 | Immer[?] sein[?] vns angefangen[?], wie dann | uncertain |
| p0_L23 | [...] Zeit dennen[?] auch [...] | uncertain |

## p1 (second page)

| line | text | grade |
|---|---|---|
| p1_L01 | Wir haben auch mit sonderlichen gros[sen] frewden[?] | uncertain |
| p1_L02 | vernommen das Gott der all- | clear |
| p1_L03 | mechtige E. L. geliebte Gemahlin vnsere | uncertain (geliebte: pass A + reconciler) |
| p1_L04 | freundtliche liebe [Muhme/Nichte?], widderumb | uncertain (kinship word unread: passes "Swester"/"Zochter") |
| p1_L05 | mit leiblicher[?]/weiblicher[?] frucht des leibs ge- | uncertain (initial letter ambiguous; see crib note) |
| p1_L06 | segnet, Vnnd wunschen hierzu[?] beiden[?] | uncertain |
| p1_L07 | E. L. vom Gott dem almechtigen | clear |
| p1_L08 | viell glucks[?], heils[?] vnnd aller seliger | uncertain |
| p1_L09 | wolfart. | uncertain |
| p1_L10 | Welchs[?] wir E. L. dissmals[?] hinwidder[?] | uncertain |
| p1_L11 | freundtlichen nicht verhalten wollen, | uncertain (verhalten: pass B + reconciler) |
| p1_L12 | Vnnd sindt E. L. freundtlichen zu | clear |
| p1_L13 | dienen[?] jederzeit[?] willig. Datum | uncertain |
| p1_L14 | Cassel am 14 Octobris Anno [etc.] 64. | clear |
| p1_L15 | Vonn Gottes gnaden Landtgraue | clear |
| p1_L16 | zu Hessen, Graue zu Catzenelnbogen etc. | clear |
| p1_L17 | E. L. gutwilliger vetter vnd bruder. | clear |
| p1_L18 | Wilhelm L. zu Hessen (autograph) | clear |

p2 (outer leaf): address "Dem hochgebornen Fürsten herrn Wilhelmen Printzen zu Uranien, Grauen zu Nassaw,
Catzenelnbogen, Vianden, Dietz ... Stathaltern ... Burgundi, Holland, Seeland ... vnserm freundlichen lieben Vettern
Schwagern vnd Bruedern", docket below; seal. Read from the 60-dpi overview only, uncertain, not cropped (no crib value).

Line counts: 41 text lines; clear 13, uncertain 28.

## Crib candidates against the 1109 enclosure (f.23) -- listed, NOT tested

What 1111 says (summary of the table): thanks for 1109 and its "mitgeschickten zeitungen" (the enclosed news); nothing to
write in return this time; the plague ("Sterben", "Pestilentz") is spreading in Hesse and has begun at Kassel, also
"gegen ... vnd den Marck[?]"; congratulation that Orange's wife (Anna of Saxony) is "widderumb ... mit [leib/weib]licher
frucht des leibs gesegnet"; dated Cassel 14 Oct [15]64.

1111 does **not** restate, paraphrase or answer any specific item of the enclosure: no name, place or number from 1109's
news recurs (no August of Saxony, no France/Lorraine, no medical detail). The candidates below are therefore weak --
words the enclosure *might* share, not attested parallels:

| # | candidate | source in 1111 | why it could matter for f.23 | strength |
|---|---|---|---|---|
| 1 | zeitungen / zeittungen | p0 L09, L11 | 1111 calls 1109's enclosed matter "zeitungen" -- the enclosure is news, not a key or a private matter | context only |
| 2 | Gemahlin; frucht des leibs; gesegnet; widderumb; schwanger | p1 L03-L06 | f.23's clear words "adern zweimahl", "purgiren mussen" (NX-WVO174 pass A) are medical; Anna's pregnancy is the one bodily matter 1111 answers. If f.23 reports Anna's health/bloodletting, these words could occur in cipher | speculative |
| 3 | 16 (Septembris) | p0 L06 | 1111 dates 1109 to 16 Sept, matching 1109's own f.22r docket "1564. Sept. 16." against WVO's/the enclosure's 18 Sept: a dating fact, no cipher crib | none (dating) |
| 4 | Sterben, Pestilentz, Plage | p0 L13-L14, L21 | Wilhelm's news, not Orange's; would occur in f.23 only if Orange reported plague in Brabant | weak |
| 5 | Sachsen / Augustus; Franckreich; Lothringen | not in 1111 | the 1109 Inhoud (August of Saxony rumour) and the enclosure's clear "Franc[e]" (L08, L16) give cribs from 1109 itself, not from 1111 | from 1109, untested |

## Next step (named and costed, not run)

The reply gives no direct parallel text, so a crib-drag on f.23 would rest on 1109's own content (candidate 5) and on the
enclosure's clear-word frame (L10 "man ir d. adern zwei mahl", L12 "... vnd ... zwei mahl", L14 "... ren mussen
dermassen"), with 1111's candidate 2 as a secondary word list. The attack: a crib-placement test (a German word list of
the candidates above dragged across each cipher run between clear words, scoring consistent sign->letter assignments
across placements), with a matched control that can fail differently: the same word list dragged across a synthetic
cipher of the same run lengths and sign count built from a German news text under a random homophonic key, plus a
shuffled-crib-list control. Precondition: a settled sign inventory for f.23 (NX-WVO174's passes split 290 vs 335 tokens
and named a per-glyph atlas as the fix; TRANSCRIPTION.md hands an unsettled symbol inventory to the owner's sign sorter
first). Cost: sorter build ~$1.5 (Opus floor) + owner time; then the crib test with control ~$3, Opus, no vision.
