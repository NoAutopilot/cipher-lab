# AUDIT: sachsstaatsarchiv-manteuffel-1712 (VERIFY-MANT, account-4, 3 Oct 2026)

Verifier session separate from the solvers (A2-SAX, A2-SAX2, GAPS151/154/158/162/166). Claim under audit (ROOM 16:26 and
16:45 UTC, 3 Oct 2026): "694/08 f.410 lower block, 216 tokens, decoded with Krauske's 1893 key (key.tsv, 157 codes) at H0 C144
M48 U24, reads French in stretches; fr18 judge -1.038 vs real_p05 -0.99, all 20 shuffled-key decodes lower (best -1.18);
the f.467 period gloss scores -1.417 under the same judge, so the judge is the limit -> reading ready", plus "f.468's
interlinear gloss (period hand) agrees with Krauske's key 17/17 (shuffled p99 5)".

## Verdict table

| item | what | class | key | safe sentence |
|---|---|---|---|---|
| 694/08 f.410 lower block (file 0511), 216 code tokens | Krauske's table applied to an unglossed P.S. (Manteuffel to Flemming, Berlin, Nov 1712, from f.409's own heading per A2-SAX2) | **N3** | `published` (see Key source) | "Applying Dr. Krauske's 1893 manuscript key table (SHStA Dresden, Loc. 694/10) to the unglossed cipher passage of Loc. 694/08 f.410 gives French in stretches (C 144, M 48, U 24 of 216 tokens); no prior plaintext or decipherment of this passage was located after the search logged in AUDIT.md, which covered Acta Borussica *Behördenorganisation* vol. 1 (1894) only by word counts." |
| 694/08 f.468, 20 code groups | groups carry a period interlinear decipherment on the leaf | **N0** | the leaf's own gloss; Krauske's table agrees 17/17 | "f.468's code groups are already deciphered between the lines in a hand that is probably period; Krauske's table reproduces those glosses." |
| 694/08 f.467 glosses | period interlinear decipherment (used as judge calibration) | **N0** | the leaf's own gloss | "f.467 carries its own interlinear decipherment." |

Unsafe sentences (never use): "first decipherment of Manteuffel's reports", "previously unread", "Krauske's key verified on f.410",
"reading confirmed by the judge". The judge FAILs the f.410 decode; what the record supports is that the key fits this leaf far
better than a shuffled key does.

## Key source (rule 10)

`published` in the rule-10 sense: someone else's non-period key, credited. That is **Dr. (Otto) Krauske's 1893 manuscript table**,
"Einige Chiffre-Auflösungen zu den Berichten Manteuffels an Flemming 1712 und 1713", SHStA Dresden 10026 Geheimes Kabinett
Loc. 694/10 ff.2-5. It is handwritten, filed in the archive and **not printed**. The brief's wording ("rebuilt from a printed
key table") is corrected here: the table is not printed, and it is not a 1712 key sheet. Krauske was co-editor (with G. Schmoller)
of Acta Borussica, *Die Behördenorganisation und die allgemeine Staatsverwaltung Preußens im 18. Jahrhundert* I (Berlin 1894).
That volume prints extracts of these very reports ("Urschrift. Dresden. Hauptstaatsarchiv. Vol. CXLV. Loc. 694") with notes
such as "Chiffre für Graf Christoph Dhona". So the 1893 table was most likely made for that edition (I). It agrees 17/17 with
period interlinear glosses on f.468, so for those codes it carries the period key's values. The table was most probably compiled
from such glosses (I), so `period` would also be defensible for the codes it shares with glossed leaves. It is not a key that we recovered.
DECODE lead, not used: record 4999, "Key of Jakob Heinrich von Flemming and Count Manteuffel, 1717, HStAD 10026, Loc. 03233/02, ca.
f. 76" (sources/decode/keys-all-2026-09-28-merged.tsv) is a period key sheet of the same pair, five years later. Comparing it with
Krauske's table would test whether the 1712 codes survived (next step, not done).

## 1. Re-derivation (rule 7)

- `python3 tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712 --check` returned "tokens 261: C 162, M 58, U 41 / reading
  up to date", exit 0. The f.410 subset is as claimed: 216 tokens, C 144, M 48, U 24.
- `python3 f410/judge_f410.py --check` returned "candidate up to date". A fresh judge call on f410/candidate.txt gave score -1.038,
  real_p05 -0.99, N 263, the same as judge.tsv.
- **New shuffle seeds** (verifier script, seeds 5000-5099, not the solver's 0-19), 100 draws each:
  - (a) all key values permuted over all codes, as the solver did: best -1.121, median -1.361, **0/100 >= candidate**; best margin
    (score - its own real_p05) -0.162, against the candidate's -0.048.
  - (b) a stricter control the solver did not run. Only the letter codes (1-120) were permuted among themselves, and every
    nomenclator value was kept, so names cannot drive the gap: best -1.608, median -1.822, **0/100 >= candidate**.
- Verdict: **reproduces**. The reading and the scores are the same. The control claim holds and is stronger under (b).
  The empirical p for "a random letter assignment fits this well" is below 0.01 at both levels.

## 2. Control audit (rule 3)

- **Can the shuffled-key control differ on the statistic?** Yes. Permuting values changes the decoded letters, which the n-gram
  score measures directly. This is not the CAS/AX-5799 orthogonal shape. The shuffled decodes' N varies with the names, so
  margins were compared as well as raw scores, and the result is the same.
- **Gloss and decode at matched N, one normalisation?** The judge folds case and accents and keeps a-z only (judge_plaintext.py
  l.224-225), and it does this for every text. GAPS166 windowed the 263-letter candidate to G's 128 letters, so N is matched.
  **Register is not matched.** G is almost all names and titles ("le Roy de Prusse", "Stanislas", "Stenbock"), while the f.410
  candidate is mostly spelled words. So G's low score (-1.417) mostly measures how fr18 handles a list of names. It shows that
  fr18 cannot certify genuine material of this series at 128 letters. It does not show that a prose decode at the candidate's
  margin is genuine. The prose-side calibration, C2 (f.467 clear text, 877 letters, +0.011), is one unreconciled pass. Reading:
  the judge cannot decide. The "reading ready" flag rests on the shuffled-key controls, not on the gloss calibration.
  fr18's leave-one-file-out spread (0.18-0.19, six files) is under the ~5-file caution only narrowly. Treat a FAIL/PASS as of
  limited reliability (rule 3, es17c paragraph).
- **Is the f.468 gloss independent of Krauske?** One vision look by this verifier (montage of hand_crops f468g_L01 and L06 above
  k694f4R_L01, all cut with tools/iiif_lines.py --image by GAPS158) concurs with GAPS158. The glosses ("Welling" over
  3.35.44.12.34.21.7, "Stenbock", and an interlinear "Stenbock et qu'il desapprouve sa conduite") are a small, steep Latin cursive
  in the letter's own pen weight. Krauske writes the same names (130 Welling, 155 Flemming, 160 Manteuffel) in large upright
  Kurrent. **Independent in hand (M)**, but **not independent in origin**: Krauske most probably built his table from glosses
  like these. So 17/17 shows that his table faithfully carries the period glosses' values. It does not separately test his
  cryptanalysis. That still licenses the key for the glossed codes. What it cannot license is any code the table gives that
  no gloss covers. The f.410 test of the table is the shuffled-key control above, not the gloss agreement.
- **26/4 conflicts (rule 4):** see HYPOTHESES.md. 26 = "R." is not a conflict: a lone letter code is used as a person's initial,
  as with 39/9 Ilgen, 44 Lol. and 66 Arn on f.468. 4 = "Ilgen" against Krauske's 4 = x is open (M). It is most likely a 9 read
  as 4 (the writer's 4/9 glyph), seen in one witness. f.410 contains no lone 4, so the reading is unaffected. The one look spent
  on f467_L11 showed lines 21-22's upper part ("178 luy avoit que 257") but not the "Ilgen" group, so that digit was not re-read.

## 3. Transcription spot check

Three lines drawn by script (`random.Random(20261003).sample` over the 17 real line crops): L01, M5, L06, 20 tokens. One blind Opus
subagent read the crops copied to scratch under neutral names (no expected values, no repo access):

| line | committed | blind | differences |
|---|---|---|---|
| L01 | 59:low 60 35 28 16 32 \| 57:low | 53?(59) 60 35 28 16 32 \| 51 | 59/53 (its alt = 59), 57/51 |
| M5 | 536:low 399 | 530?(536) 399 | 536/530 (its alt = 536) |
| L06 | 381 66 48:low 39 99 35 27:low 42 54 51 10 16 14 28 26 | 381?(281) 66 48?(43) 39 99 35 23?(28) 42 54 51 10?(15) 16 14 28 26 | 27/23 |

Exact first-reading agreement is 16/20. **All 4 splits fall on tokens the committed transcription already marks low (M)**, and
2 of them have the committed value as the blind reader's own alternative. Nothing differs beyond the M tokens, so under rule 7
this does not send the reading back. The blind reader also noted a "w3." mark before L01's final group, which the committed
transcription does not show. Not settled.

## 4. Novelty search log (3 Oct 2026)

| family | searched | result |
|---|---|---|
| (a) canonical/edition series | Acta Borussica, *Behördenorganisation* I (1894, Schmoller & Krauske). Found via Google Books API snippets (country=US, key): Nr. 82 "Bericht ... Manteuffel an ... Flemming. Berlin 23. November 1712. Urschrift. Dresden HStA Vol. CXLV. Loc. 694", on Graf Dhona and the Prince Royal; further extracts of 3, 9 and 12 Dec 1712 and Jan-Feb 1713. Volume read **by word counts only**: HathiTrust njp.32101065980920 v.1 (full view; pages Cloudflare-blocked from cloud) through the HTRC Extracted Features API. Positive control: Manteuffel, Dhona, Ilgen, Grumbkow and Flemming all present on seq 354-469. **"Angleterre", "d'Angleterre", "contentement", "Suédois", "Danemarc" occur on no page of the volume**; Nr. 82 (seq 435-436) has no Stettin, reine or paix | **f.410's passage not printed here** (OCR- and bag-of-words-conditioned; f.410 names "la reine d'Angleterre" three times) |
| (a) | NASG vols 14-19 (1893-98), full OCR grep (A2-SAX, 24 Sept and 3 Oct 2026; not re-run) | none |
| (b) sender/recipient papers | Haake's Flemming studies: no IA item (GAPS158); the Wackerbarth "Société des antisobres" paper (OpenAlex hit, 2016) was not read | **unread, gap** |
| (c) documentary editions | J. G. Droysen, *Geschichte der preußischen Politik* IV (cited on Acta Borussica I seq 436 beside the Dhona/Ilgen conflict) was not searched; other Acta Borussica series were not searched | **gap** |
| (d) holding archive | archiv.sachsen.de records for Loc. 694/08, /09 and /10 (quoted by A2-SAX/A2-SAX2): no transcription or edition named | none |
| (e) full text | Google Books API phrase queries: "ne donne contentement" + reine Angleterre prince 1712 (0); Manteuffel Flemming "contentement" 1712 (0); Manteuffel Flemming Stettin 1712 Chiffre (0); Manteuffel Flemming "Suedois" paix 1712 (0); Dhona Manteuffel "reine d'Angleterre"/"contentement"/"rien pour lui" (0); Dhona Manteuffel "Stettin" (5 hits, 1758-1902 Prussian histories, none on the passage). IA: the 9 *Behördenorganisation* copies on archive.org are later volumes (no Manteuffel report text) | none on the f.410 passage |
| (f) solver repos, blogs, DECODE | DECODE keys listing: record 4999 (1717 Flemming-Manteuffel key, Loc. 03233/02), a lead and not a decipherment of f.410. Repos and blogs: GAPS158/24 Sept passes (zero hits), not re-run by this verifier | none |
| (g) scholarship | OpenAlex (key): 3 queries returned "Geheime Netzwerke im Militär" (2016), the Société des antisobres paper (2016), "Anna von Cosel" (2020) and "Multiple Loyalitäten" (2024), titles only and none on the cipher. Semantic Scholar (key): 0 on all 3. JSTOR: 3 rows appended to JSTOR-QUEUE.tsv (family (i) metadata+cipher, family (ii) quoted phrase without a cipher word) | none; JSTOR queued |

Unreachable: HathiTrust page images (Cloudflare; EF used instead); books.google.com page view (captcha). Requests: googleapis.com
~20, archive.org 10, catalog.hathitrust.org 4, data.htrc.illinois.edu 1, openalex 3, semanticscholar 3, openlibrary 1.

**Why N3 and not N4:** Krauske, who made the key, co-edited a volume that prints decoded extracts from this same Loc. 694 file.
That volume was read only as word counts, not page by page. Droysen, Haake and the Wackerbarth paper are unread. A person reading
Acta Borussica I pp. around Nr. 82-85 (HathiTrust njp.32101065980920, seq 434-440) is the cheapest way to N4. It would also show
whether Nr. 82 is the letter whose P.S. is f.409v-410.

## Postmortem and corrections

- The brief and GAPS151 called Krauske's table "printed"/"published". It is an unprinted 1893 manuscript. The `published` key
  class is right only in rule 10's "someone else's modern key" sense. NOTES.md now says so.
- GAPS158/GAPS154 treated the 17/17 gloss agreement as "an independent check" of Krauske's table. It is independent in hand,
  not in origin, because Krauske likely compiled the table from these glosses. Corrected in NOTES.md.
- "The judge is the limit" is supported only weakly by G, which is a names list and not register-matched. The reading-ready
  basis is the shuffled-key control, confirmed here at 0/100 under two shuffle designs.
- No over-claim of novelty was found in the folder. Every solver section says "a search result, not a novelty verdict".
