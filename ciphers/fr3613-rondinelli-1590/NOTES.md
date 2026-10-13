blocked
Gomberville 1665 seconde partie (Gallica bpt6k64451005) read as page images by this worker: printed pp.213-224, 338-344 and 394-403 (views 262-273, 387-393, 443-452), letter absent, no Rondinelli, no cifra, no Italian letter there; status stays blocked because the individual blog-site searches and the fr.3995 recipient-side tables are still unread (see BNF-RONDI2).

# Hercole Rondinelli to the duc de Nevers, Paris, 11 Nov 1590 -- BnF Français 3613 no.33, fol. 62

Job BNF-Q13-CS for LANE BNF-FOCUS (account 2), 8 Oct 2026. Status `blocked` (edition unread), not a negative.
BnF notice (cc50063m.html): "Lettre, avec chiffre, du Sr HERCOLE RONDINELLI au duc de Nevers. Di Parigi, il di XImo di 9bre 1590. En italien." No decipherment flag.

## Leaf look (Gallica btv1b90582263, canvas 69 = f.61v/62r, 900 px)
f.62r: a full page of about 17 lines of dense symbol cipher (letter-like forms with diacritics and strokes), headed "Ser. Principe Sig. et Padrone Col.mo", then three clear Italian lines at the foot ("Io sarei partito un pezzo fa se havesti trovato il modo di pagare ..."). Left page is the verso of the preceding leaf, no gloss. Canvas 70 (f.62v/63r): a clear letter from Rondinelli dated Paris, October 1590 (signature visible), not the cipher letter. No interlinear decipherment, slip or clear copy seen at 900 px. Symbol cipher, about 17 full lines, so the length is workable; the key is unknown.
Note: the clear letters from the same hand dated Oct 1590 neighbour it (f.61v, f.62v) and may give context/cribs; not read.

## Prior-art search (8 Oct 2026)
Bourdeau repo: no hit "Rondinelli". Tomokiyo: no hit. Meister 1906 whole-volume grep: "Rondinelli" appears once in an index/name list (djvu line 9359), no key. Gomberville search-within: Rondinelli no hit, Gondy hits at pp.346, 426, 467 (not this letter). WebSearch "Rondinelli duc de Nevers lettre chiffrée 1590 Français 3613 déchiffrement": nothing on Rondinelli; only Desenclos and Lasry 2024 (BnF fr.3995 holds 68 cipher tables used by Nevers, a key source to check; fr.3615 f.52 interlinear for a 1591 letter).

## Web and blog check (BNF-Q13-CS, 8 Oct 2026)
One query above plus the combined blog query in fr3613-sega-caetani-1591's NOTES; no hit. Blog site searches not run individually.

## Premise check (BNF-Q13-CS, 8 Oct 2026)
(a) none: not found. (b) Bourdeau none: not found. (c) f.61v-63r viewed at 900 px: no gloss, not found. (d) recipient side: Nevers papers' own cipher tables in fr.3995 not opened: unreached.

## While waiting
Open fr.3995's table list (finding aid cc504266) for tables addressed to Italian correspondents of 1590 and screen on Gallica, ~3 requests.

## BNF-GOMB (8 Oct 2026, account 2, different instrument: Gallica ContentSearch + page images, not Google Books search-within)
Edition: Gomberville, Memoires de M. de Nevers, seconde partie (1665), Gallica bpt6k64451005 (view n = Gallica PAG_n; printed page = view - 49 near v.255, - 63 near v.754).
ContentSearch (`gallica.bnf.fr/services/ContentSearch?ark=bpt6k64451005&query=`), whole volume: Rondinelli 0, Rondinel 0, Rondin 0, Hercole 0, Ercole 0, Cifra 0, Parigi 1 and Illustriss 1 (both view 255 only). View 255 (printed p.206, read as image) is Cardinal Caetani to Cardinal Montalto, Di Parigi 15 Feb 1590, the only Italian letter in the volume: not Rondinelli, not the 11 Nov 1590 letter. "Nouembre 1590" hits at views 262-273, 452, 670 are royal/Champagne dated pieces (snippets only). Pages for Oct-Dec 1590 were NOT read as images, so blocked stays: no instrument here tested a French rendering of an Italian private letter beyond name search.
Premise (d) update: recipient-side edition searched by OCR for the sender's name, 0 hits; not found.
Next: read views 262-273 and 387-393, 443-452 as images (about 20 requests) or park.
Gallica requests this job (shared with unit 2): about 39 incl. 1 reset+1 retry.

## BNF-RONDI (8 Oct 2026, 10:27-10:40 UTC by date -u, account 2)
Instrument: Gallica `ark:/12148/bpt6k64451005/f<N>.highres`. View 262 fetched and read as image: printed p.213, "Autre lettre de S. M. au mesme", Henri IV to Nevers, Camp de Coeures 10 Nov 1590, French, no cipher, no Rondinelli. Rest of the page is the bleed-through of p.214. Views 263 (HTML challenge page, 48 KB), 264 and 265 (HTTP 503 maintenance, 299 B) and one retry of 263 after a 100 s pause (60 s timeout, 0 bytes) all failed; stopped per brief. Not read as images: 263-273, 387-393, 443-452 (28 views). Verdict: blocked (pages cannot be read now), not a negative. Next: re-run views 263-273 first (printed pp.214-224, the 11 Nov 1590 neighbourhood) when Gallica answers, ~11 requests; 387-393 and 443-452 after.
Requests this job: gallica.bnf.fr 7 (1 reset, 1 HTTP 500 on an IIIF path, 262 ok, 263 challenge, 264-265 503, 263 retry timeout); no other host.

## Gate
```
fr3613-rondinelli-1590: blocked (line 1) -- already terminal, nothing to gate
exit 0
```


## BNF-RONDI2 (13 Oct 2026, account 2)
Window 06:21-06:5x UTC by `date -u`. Route: `openapi.bnf.fr/iiif/image/v3/ark:/12148/bpt6k64451005/f<N>/full/1600,/0/default.jpg`, descriptive User-Agent, 2 s apart; no contact with gallica.bnf.fr. Request log: `images/gomb/request.log` (28 requests, all HTTP 200, 533-685 KB each; sha256 in `images/gomb/manifest.json`).
Views read as images (one read each): 263-273 (printed pp.214-224), 387-393 (pp.338-344; view 392's header is misprinted "341"), 443-452 (pp.394-403). Per-view rows: `gomb_views.tsv`.
Content: 263-273 Henri IV to Nevers, 15 Nov-29 Dec 1590, all French; 387-393 Flamenville's letter from Sedan 12 Oct 1590 and Nevers's reply to the King, Châteauthierry 15 Dec 1590; 443-452 d'Aumont, La Chère, de Gèvre, Chabouille and d'O letters and Nevers's "Articles et faits" with the King's answers (Attichy 18 Nov 1590).
Result: not found in the views named. Rondinelli, any cifra, and any Italian letter from Paris of Nov 1590 do not appear on any of the 28 views (reading by this worker, 1600 px images; body text read at heading level, not word by word on every line). Together with BNF-GOMB's whole-volume ContentSearch (Rondinelli 0, Cifra 0), the edition shows no sign of this letter in the named views.
Still unread for the check-solved sources: the three blogs individually (Cipherbrain, Cryptiana blog, Cipher Mysteries) and the recipient-side cipher tables in fr.3995; line 1 stays `blocked`.
Requests this job: openapi.bnf.fr 28; no other host.

### Gate
```
fr3613-rondinelli-1590: blocked (line 1) -- already terminal, nothing to gate
exit 0
```
