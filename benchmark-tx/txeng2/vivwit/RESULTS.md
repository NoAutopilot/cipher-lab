# WIT-VIV: printed second witness for the Saint-Gouard June 1573 dispatch (TXE2-VIVWIT, 10 Oct 2026)

PREREG: benchmark-tx/PREREG-txeng2-16.md section WIT-VIV. Brief row: .claude/briefs/runs/2026-10-10-account4-txe2-round16.md
TXE2-VIVWIT. Worker: account 4, Opus 5.5, for LANE TX-ENGINEER-2 incarnation 3. Clock (date -u): 00:12-00:1x UTC 10 Oct 2026.
Scripts: `grep.py` (run from the repo root: `python3 -I benchmark-tx/txeng2/vivwit/grep.py <phrase file>`; lower-cases, strips
accents and non-letters, folds v->u, j->i, y->i, k->c on both sides, so OCR line-break hyphens and word spacing do not matter),
phrase files `phr.txt` (phrases from dec_norm + controls) and `phr2.txt` (Gachard's own wording, after the first hit).

Openings of eval truth: 0. No benchmark-tx/*.truth.tsv and no outputs/ file was opened. Phrases were taken from
ciphers/fr16104-vivonne-spain-1572/tx/dec_norm.txt offsets 500-3200 (the folder's clerk reading, not the benchmark truth).

## Editions searched

On disk (sources/ia-fulltext/print-check/<id>_djvu.txt.gz, whole volume, letter-normalised grep):

| IA identifier | edition |
|---|---|
| labibliothquen02gachuoft | Gachard, *La Bibliothèque nationale à Paris* II (1875) |
| lepredemadamede00dargoog | Brémond d'Ars, *Jean de Vivonne* (1884) |
| archivesoucorre03housgoog | Groen van Prinsterer, *Archives ... d'Orange-Nassau* 1re sér. IV |
| archivesoucorre04housgoog | Groen van Prinsterer, *Archives* (the volume after; checked in case the 03/04 numbering is off) |
| lettresdecatheri04cathuoft | La Ferrière, *Lettres de Catherine de Médicis* IV |
| leshuguenotsetle03kerv | Kervyn de Lettenhove, *Les Huguenots et les Gueux* III |
| correspondancede02phil | Gachard, *Correspondance de Philippe II* II |

Internet Archive full text, all items: be-api.us.archive.org/fts/v1/search, quoted phrases, no identifier filter (5 queries)
plus 1 query restricted to labibliothquen02gachuoft.

## Phrases and results

On-disk, dec_norm-derived (f.102r stretch) and controls (`phr.txt`), 7 editions each:

| label | phrase (normalised pattern; "+" = both within 400 letters) | hits |
|---|---|---|
| P1 | nouvelles forces aux rebelles | 0 |
| P2 | portugal en flandres | 0 |
| P3 | secours pris par le conte de Montgommery | 0 |
| P4 | Montgommery + belle isle | 0 |
| P5 | prince d'Orange se deffendra (dec_norm 2730) | 0 (Gachard's wording differs: "ilz s'en deffendent bien", G1) |
| P6 | tant que le roy vivra (dec_norm 2781) | 0 (Gachard: "tant que ce roy vivra", G2) |
| P7 | la paix de(u) Turc | 0 as a string |
| P8 | reconciliation + orange | Gachard II 7, Kervyn III 8, Philippe II vol. II 2, Groen IV 1 -- all other letters or Gachard's own French paraphrase (below), none a quotation of f.102r |
| P9 | flamans + pardon | **Gachard II 3, the quotation below**; 0 elsewhere |
| P10 | la rochelle + montgommery | Groen IV 3, Catherine IV 8, Philippe II 1 -- other letters (Rochelle news), not this dispatch |
| CTL | le dernier de may feut juré (Gachard quotes it under XXXVIII; plain French on f.100) | 0 on-disk as a string because the OCR reads "feut iure ash..." (spacing/accents) -- see CTL2 |
| CTL2 | hieronime + castille (same passage) | **Gachard II 1** (positive control passes) |

On-disk, Gachard's own wording (`phr2.txt`), 7 editions each:

| label | phrase | hits |
|---|---|---|
| G1 | ilz s'en deffendent bien | Gachard II 1 only |
| G2 | tant que ce roy vivra | 0 (OCR "ceroiuiura" vs fold; G1's hit shows the line) |
| G3 | du pardon general + flamans | Gachard II 1 only |
| G4 | Harlem sera pris | Gachard II 1 only |
| G5 | remedier par la force (the letter's closing passage, f.103r / clerk f.108v; control) | Gachard II 2 (p.429 + another letter), **Groen IV 2 (letter 63, pp.90*-91*)** |

be-api (all of IA unless an identifier is named):

| # | query | total | items |
|---|---|---|---|
| be1 | "diversité d'opinions entre les Flamans" | 0 | (the one witness's OCR reads "<:ntre", so the exact phrase breaks -- a measured OCR miss, see be3) |
| be2 | "Harlem sera pris" pardon, identifier=labibliothquen02gachuoft | 1 | Gachard II (positive control) |
| be3 | "Flamans qui sont icy apellez" | 1 | labibliothquen02gachuoft only |
| be4 | "tant que ce roy vivra" Oranges | 1 | labibliothquen02gachuoft only |
| be5 | "s'aider plus que jamais du pardon" | 1 | labibliothquen02gachuoft only |
| be6 | "Le dernier de may feut juré" (control, plain passage) | 1 | labibliothquen02gachuoft only |

be-api `page_num` is 640 for every Gachard hit = not a page locator (CLAUDE.md IA row); the printed pages below are from the
running heads in the djvu text ("428 DÉPÊCHES DES AMBASSADEURS" before XXXVIII; "PHILIPPE II. 429" before "L'empereur").

## The witness found

**Gachard II (1875), p.428**, entry "XL, XLI. -- Au roi, Madrid, 8 juin 1573. (Presque entièrement chiffrée, avec le
déchiffrement.) Cette lettre est un duplicata de celle du 4". After a French paraphrase (audience; the duc d'Albe's arrangement
with the English; the reconciliation with the prince d'Orange "de laquelle il était bruit", the king "fit semblant de n'en avoir
jamais ouï parler", hoped the two kings "auraient bientôt la raison de leurs ennemis et rebelles"; nothing said to Saint-Gouard
of the Venetians' peace with the Turk), Gachard prints verbatim (OCR as on disk):

> Quant à la paix que l'on dit qu'ilz veullent faire avecques le prince d'Oranges, ilz s'en deffendent bien, el me disent tous
> que je ne la verray jamais tant que ce roy vivra ; ilz m'en disoient tout autant au faict des Anglois .... Je sçay
> asscurément qu'ilz sont aprèz pour s'aider plus que jamais du pardon général : mais il y a diversité d'opinions <:ntre les
> Flamans qui sont icy apellez à ces affaires et les Espaignolz, estans d'advis lesdicts Flamans qu'au plus tost, ou pour le
> moins aussi tost que Harlem sera pris, ledict pardon se publie, et les autres veullent que premièrement toutes choses soient
> appaisées par la force ....

and on **p.429** the closing passage ("L'empereur faict tout ce qu'il peult de réconcillier le prince d'Oranges ... Mais l'on
m'asseure qu'il n'a donné nulle espérance ..."), which the folder already places at the end of the letter (f.103r / clerk f.108v).

Placement in dec_norm (the folder's reading; offsets by plain string search): "quantalapaixcequelondict" 2669, "sedeffendrabien"
2730, "tantqueleroyuiura" 2781, "opinions" 3000, "flamans" 3014/3089, "pardon" 3145, "premierement" 3177 -- the quotation spans
about dec_norm 2669-3230, i.e. the tail of the 500-3200 window. The paraphrase above covers about dec_norm 1100-1300
("reconciliation" 1123, "semblantdauoirouyparler" 1259) and 2550 ("lapaixdeturc"), but paraphrase is not a letter-level witness.
Whether 2669-3230 falls on f.102r or crosses into f.102v depends on the j0/bounds question DV1c left "not confirmed"; this worker
did not decide it.

Two cautions for the lane: (1) Gachard's XL-XLI is "avec le déchiffrement", so his quotation is very likely his reading of the
same clerk decipherment (ff.104-108v) that dec_norm transcribes -- an independent transcription of the same source, not an
independent decipherment of the cipher; (2) "...." marks Gachard's own omissions (one inside the quote, after "Anglois").

Other witness noted (outside the f.102r stretch): **Groen van Prinsterer, Archives 1re sér. IV (IA archivesoucorre03housgoog),
letter 63, pp.90*-91***, "St. Goard au Roi Charles IX: Madrid, 8 juin (MS. P. Sup. G. H. 228, vol. 79a)", prints only the
closing Emperor passage ("....L'Empereur fait asseurément tout ce qu'il peult de réconcillier le Prince d'Oranges ... je ne
scay enfin ce qu'il feroit pour remédier ses affaires"), from a different manuscript copy than BnF fr.16105.
d'Ars 1884, Catherine IV, Kervyn III, Philippe II vol. II, Groen 04: no hit for any f.102r phrase.

## Requests per host

be-api.us.archive.org 6 (all HTTP 200, >= 1.6 s apart); archive.org downloads 0 (all full texts already on disk);
gallica.bnf.fr 0. Subagent calls: 0.

Verdict: measured: witness found at Gachard, La Bibliothèque nationale à Paris II (1875, IA labibliothquen02gachuoft) p.428
(about 530 letters, dec_norm ~2669-3230, plus the closing passage p.429 and Groen IV pp.90*-91* outside the stretch); no other
printed witness of the f.102r stretch located in 7 on-disk editions by 17 phrases and in IA full text by 5 corpus-wide phrase
queries (a search result, never a novelty verdict). Handed to the lane as anchor material; nothing applied.
