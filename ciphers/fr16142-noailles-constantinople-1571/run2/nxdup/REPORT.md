# RUN2-NXDUP: Dupuy 521 221R-226R clear text (LANE-RUN2 wave 1, account 1, 4 Oct 2026, 02:47-03:0x UTC)

Brief: `.claude/briefs/runs/2026-10-04-acct1-run2-wave1.md` RUN2-NXDUP. No decode, no alignment, key.tsv/gloss.tsv untouched.
Intake gate (02:47 UTC): `fr16142-noailles-constantinople-1571: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

## What was done
1. Gallica `btv1b100339270` canvases 221-226 fetched once at IIIF `full/4800,` (native 7358 px; 6 requests, HTTP 200, 2 s apart),
   scratchpad only. `tools/iiif_lines.py --image ... --follow-slope 400 --debug` per page (regions in `regen.sh`): 221R 7 lines
   (from "Au Roy", below Merillon's letter of x mars 1574), 222L-225R 27 bands each, 226L 27, 226R 23 (to the date line);
   277 crops. Overlays checked for 221R and 222L (bands on the lines, catchword in the last L band). Crops not committed; `regen.sh` re-cuts them.
2. Two blind Sonnet passes per page, one call per page per pass, crop paths only (`pass_prompt.md`): 22 calls, `passA/`, `passB/`.
   Pass B on 222L drifted one row (its L07 text is L08's) -- row labels are not reliable, so agreement is measured on the whole page text.
3. Reconciliation (this worker, Opus): each page read from two half-page images of the 4800 px fetch with both passes beside it;
   `reconciled/<page>.txt`, one manuscript line per line. 21 tokens left [?].
4. `build_texts.py` writes `dupuy221_226_diplomatic.txt` (page.line markers) and `dupuy221_226_norm.txt` (rule 3 PX-BRODEC:
   abbreviations expanded -- Ma^te -> maieste, dupp^tas -> duplicatas, & -> et --, lower case, apostrophes -> word break,
   diacritics stripped, letters/digits + word spaces; **u/v and i/j kept as written**, no mapping applied; catchwords, the
   heading "Au Roy", the dittography and the copyist's "&c." dropped). `--check` exits 1 when stale (rule 7).

## Numbers (`err_2reader.tsv`)
| | value |
|---|---|
| normalised text | 2,088 words, 9,425 letters (FT-D/RUN1-NX estimate for c510-516: ~9,750 cipher signs) |
| err_2reader, raw (Levenshtein / mean length, whole page) | 0.218 pooled (0.119-0.382 per page) |
| err_2reader, loose ([?]/markers stripped, lower case) | 0.129 pooled (0.096-0.197) |
| pass A vs reconciled, loose | 0.184 |
| pass B vs reconciled, loose | 0.202 |

The two passes agree with each other better (0.129) than either agrees with the reconciled text (0.18-0.20): they share
errors (both read this copyist's r as v, e as c), so err_2reader understates reader error here. The reconciled text is one
further reader's reading, not ground truth; no benchmark item exists for this hand (TRANSCRIPTION.md: err_true not measured).

## Observations (not tested here)
- **Extent.** The letter is 221R.03 ("Sire.") to 226R.23 ("des Vignes de Pera les Constantinople ce vj Juillet 1574"); 226R then
  opens "A la Royne". The date is **vj**, as the RUN1-NX index read (fr.16142's heading has 7).
- **"&c." before the date (226R.21).** The text breaks off "... que toutes choses vous succedent mal &c." and goes straight to the
  place and date: no courtesy close, no signature. This is the copyist's truncation mark (Dupuy 521 calls itself "Extraits"); the
  enciphered original may continue after this point (closing formula at least, possibly more). **Possible omission.**
- **Dittography 223L.14-15**: "en quoy j'ay esté bien / en quoy j'ay esté bien apropos" (kept in the diplomatic text as
  `{DITTO: ...}`, dropped in the normalised text).
- **The c516 clear lead-in is at 226R.03-.06** ("Sire quelques jours avant recepvoir vostredicte depesche du dix huictiesme d'avril
  j'avois entendu ce qu'il plaist a Vostre Ma^te me mander"); the print-crib for c516's cipher is therefore 226R.07-.21 ("des
  conspirations ... succedent mal"), about 90 words. The rest of the clear copy (221R.03-226R.02) stands against c510-515.
- **225L.09-.13** carries the passage Charrière III pp.551-552 prints from the same despatch ("Quant a l'opposition que Vostre Ma^te
  me commande faire aux recherches qu'aucuns princes & Estatz d'Italie font pour avoir intelligence en ceste porte ...").
- Where the copy is continuous across a page turn the catchwords match (222L Dudict, 223L ladicte, 224L Maistre, 225L est,
  226L denommee); 225R -> 226L joins "Je ne[?] / doubte point" without a catchword (R pages carry none).
- Uncertain names: "Mouillon[?]" (226L, 2x; the Marseille correspondent of 220R-221R is indexed "Merillon"), "Jazlowiezky"
  (223R), "Caidramadan" (226L), "Ferrals" (225R).

Requests: gallica.bnf.fr 7 (1 info.json + 6 images). Subagent calls: 22 (Sonnet), 0 failed. Own image reads: 24 (overlays, crops, half pages).
