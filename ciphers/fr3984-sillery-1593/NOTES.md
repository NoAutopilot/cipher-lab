found-solved
Tomokiyo, Cryptiana "Ciphers of the Catholic League" (league.htm, BnF fr.3984 section, entry no.98 fol.198) read by this worker on the repo snapshot and again live at https://cryptiana.web.fc2.com/code/league.htm on 3 Oct 2026: it prints the no.40 decoding of every cipher token on f.198r; the leaf itself (Gallica btv1b9060633d canvas 364) viewed by this worker.

# fr.3984 f.198 -- Nicolas Brulart de Sillery to the Duke of Nevers, 25 July 1593 (NEVERS-VEIN NV-04)

Folder made by NV04-CS (account-2 worker, LANE-A2PUSH3), 3 Oct 2026. Brief: `.claude/briefs/runs/2026-10-03-acct2-nv04-cs.md`.
No transcription and no key application in this job (brief).

## Leaf location (gallica_folio.py + eye check, 3 Oct 2026)

- Manifest btv1b9060633d: 515 canvases, all labelled 'NP'. `python3 tools/gallica_folio.py btv1b9060633d --folio 198
  --anchor 327=176r --anchor 329=177r --anchor 333=179r --anchor 343=184r --anchor 351=188r` (anchors eye-checked by the
  fr4715-f61 campaign) fits canvas = 2*folio - 25 exactly over ff.176-188 and estimates f.198r at canvas 371.
- Eye check of 900/700 px downscales: **the offset changes after f.188**. Canvas 371 carries the ink foliation 202 (printed
  pamphlet "Advis aux François sur la declaration faicte par le Roy en l'Eglise sainct Denys ... le xxv jour de Juillet 1593"),
  373 = 203 (same pamphlet). Canvas 361 = an address leaf ("A Monsieur Monsieur de [Rubis?] a Lyon", endorsed "Mr l'archevesque
  de Lyon 24 juillet 93"); 362 = **f.197r** (Italian, "Di Roma alli 24 luglio 1593", the "Coppie ... au Sieur de Maisses");
  363 = a small slip laid in (see Premise check (c)); **364 = f.198r**, ink folio "198", heading "25 de Juillet 1593",
  signed at foot; **365 = f.198v**, address "A Monseigneur Monseigneur le duc de Nivernois", two seals.
- Native URLs: https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060633d/f364/full/full/0/native.jpg,
  verso f365. Leaf page: https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f364.item
- Requests to gallica.bnf.fr this job: 9 image requests (canvases 361-365, 371-373 downscaled, one 363 crop, one 364 band crop),
  one connection reset on 372 (not retried), no challenge page.

## Cipher on the leaf (estimate, no transcription)

Numeric/sign cipher written inline in the clear French prose, about two-thirds down the page (band pct:22,42,68,15 at 1800 px).
Four runs, counted by eye from the band crop: about 22 + 13 + 10 + 1 = **~46 tokens** (two-digit figures, a few symbols:
barred o, a v-like sign, a filled triangle-like sign, T, an epsilon-like sign, "xx"). No interlinear decipherment visible at this
resolution, which matches Tomokiyo's "Undeciphered". The four runs and their token counts match Tomokiyo's league.htm listing
(22/13/10/1), so his reading covers the whole of the cipher on f.198r.

## Check-solved (NV04-CS, 3 Oct 2026; rule 1 order)

1. Search engine: four WebSearch queries (see Web and blog check) -- no hit naming this letter or its cipher.
2. Sender's printed correspondence: not opened (the item was found-solved at source 4 before this step mattered; the reading
   is cipher-to-plain, so a printed copy of the letter would add a plain witness, not change the status).
3. Calendars / state-paper series: not applicable (BnF fonds français, Nevers papers); not searched.
4. List-post pages: **Cryptiana, league.htm no.98 (fol.198): "Portions in cipher. Undeciphered. Cipher no.40 of the Nevers
   collection decodes them as follows."** followed by a token-by-token reading of all four runs. nevers.htm (no.40 entry) says
   only "This decodes the undeciphered portions in ... (BnF fr.3984, f.198)", which is why NEVERS-VEIN's ev_note said "prints
   no reading on nevers.htm" -- true of that page, but the reading is on league.htm.
5. DECODE: not searched (stopped at the find).
6. Solver repositories: `sources/cyphersolver*` grep for 3984 -- no file names fr.3984 f.198; aaymeloglu not searched (stopped).

Verdict: **found-solved, F0** (README's grades): the specialist list keeper who catalogues these ciphers (Tomokiyo) has already
linked this manuscript leaf to its key and printed the decoding; the only party that did not know was this project's own
NEVERS-VEIN row, which read nevers.htm and not league.htm. What it leaves to hand on: nothing to Tomokiyo; for this project,
the leaf is a ready known-answer control under key no.40 (Tomokiyo's reading as the answer, grade C for us only after our own
transcription agrees with his token list).

Tomokiyo's reading as printed (his token values; "(Symbols other than figures are approximate substitutes.)"), quoted for the
record, not re-derived here:
- run 1: 46 u, 32 n, 35 r, 18 e, 22 g, 26 i, 30 m, 18 e, 32 n, 16 d, U e, 42 s, 46 u, 26 i, 42 s, 25 s, 23 e, 25 s, [sym] a,
  46 u, xx "D: de Mant[u]a", 61 "soldats" -> "un regiment de suisses a u D. de Mantua soldats" (spacing his);
- run 2: 37 u, 32 n, 18 e, [sym] n, 91 "Prouance", U e, 44 t, [sym] u, 32 n, 18 e, T n, 90 "Daulfine", 47 - ;
- run 3: 28 l, 18 e, 37 u, 31 i, 36 p, [sym] a, 42 s, 25 s, 10 a, 22 g, 23 e -> "le u i passage" (as his values give);
- run 4: "23" (his comment block lists it on its own line).
Note for any later transcription: his run 3 has 31, where this worker's downscaled band crop reads the fourth figure as "35";
not settled here (no transcription in this job).

## Premise check (NV04-CS, 3 Oct 2026)

(a) Folder's own mentions of a decipherment: the folder is fresh; NEVERS-VEIN NV-04 and QUEUE.md row NV-04 cite Tomokiyo's
    "This decodes the undeciphered portions" -- opened: **found** (league.htm no.98, above).
(b) Other solvers' working files: Tomokiyo's league.htm is his working output for this very text under key no.40 -- **found**.
    Bourdeau / sources/cyphersolver: grep for 3984 finds no file for f.198 -- not found. Our own key: no.40 letter strip is on
    disk at `ciphers/fr3993-villeroy-1595/keys/key_f74r_letters.tsv` (fr.3995 no.40 f.74v, canvas f148, read by VILL-STRIPS
    3 Oct 2026, 72 lines) -- a key we would borrow; not run on f.198 by anyone in this repo.
(c) Physical neighbours: f.197r (canvas 362) is the Italian "Coppie" of 24 July 1593, clear; 361 an address leaf of another
    letter; **canvas 363 is a small slip laid in between f.197 and f.198 carrying six lines of a different, letter-symbol cipher
    with a lighter interlinear (clear letters) and the note "avec la [lettre?] du 20 Aoust 9[3?]"** -- not this letter's cipher
    (f.198's is figures), not a decipherment of f.198; flagged for the vein as a separate glossed item. f.198v (365) address
    only; no clear copy or decipherment of f.198 bound beside it. Found: nothing for f.198 beyond (a)/(b).
(d) Recipient's side: Nevers is the recipient; the Nevers papers are this very fonds. No printed edition of Sillery's 1593
    Swiss-embassy letters to Nevers searched (stopped at the find) -- not searched.

## Web and blog check (NV04-CS, 3 Oct 2026)

WebSearch (standard), 3 Oct 2026:
1. `Sillery Nevers 25 juillet 1593 chiffre fr.3984` -- Wikipedia "1593 in France", BnF CCFR records on Sillery's Swiss embassy;
   nothing on this letter's cipher.
2. `"fr.3984" "f.198" cipher Sillery` -- no relevant hit.
3. `Brulart de Sillery duc de Nevers 1593 lettre chiffrée` -- Lasry et al. (dspace.ut.ee) on Henri IV to Nevers 1592, a
   different letter; nothing on f.198.
4. `cryptiana Sillery Nevers 1593 cipher no.40 Donchery` -- same 1592 paper; Cryptiana not indexed for this page.
Blogs: Cryptiana (Tomokiyo's pages) read on disk and live -- **hit, league.htm no.98** (live fetch 3 Oct 2026, HTTP 200 after
a 302 to https). Cipherbrain and Cipher Mysteries not searched (stopped at the find, which is already decisive).

## Intake gate

```
$ python3 tools/intake_gate_check.py fr3984-sillery-1593
fr3984-sillery-1593: found-solved (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Verdict

found-solved (F0, Tomokiyo, league.htm no.98). No first test on this letter as a target. The leaf's use for the vein: a
**known-answer control for key no.40** -- ~46 tokens, Tomokiyo's token-level reading as the answer. Next step (if the lane wants
the control): one transcription pass of the f.198r cipher band (`tools/iiif_lines.py --ark btv1b9060633d --canvas 364
--region <band> --out ciphers/fr3984-sillery-1593/images`, crops pasted first; 2 independent passes x 1 crop batch at about
USD 1.5 per Opus vision call + 1 reconciliation unit = ~USD 4.5), then `tools/decode_key.py` with the VILL-STRIPS no.40 strip,
scored token-by-token against Tomokiyo's list (grade C only where our transcription and his agree). Also worth a vein row:
the laid-in slip at canvas 363 (glossed letter-symbol cipher, "du 20 Aoust 9?").
