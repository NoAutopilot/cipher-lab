# AUDIT: sachsstaatsarchiv-manteuffel-1712 (VERIFY-MANT, account-4, 3 Oct 2026)

Verifier session separate from the solvers (A2-SAX, A2-SAX2, GAPS151/154/158/162/166). Claim under audit (ROOM 16:26 and
16:45 UTC, 3 Oct 2026): "694/08 f.410 lower block, 216 tokens, decoded with Krauske's 1893 key (key.tsv, 157 codes) at H0 C144
M48 U24, reads French in stretches; fr18 judge -1.038 vs real_p05 -0.99, all 20 shuffled-key decodes lower (best -1.18);
the f.467 period gloss scores -1.417 under the same judge, so the judge is the limit -> reading ready", plus "f.468's
interlinear gloss (period hand) agrees with Krauske's key 17/17 (shuffled p99 5)".

## Verdict table

| item | what | class | key | safe sentence |
|---|---|---|---|---|
| 694/08 f.410 lower block (file 0511), 216 code tokens | Krauske's table applied to an unglossed P.S. (Manteuffel to Flemming, Berlin, Nov 1712, from f.409's own heading per A2-SAX2) | **N4** (AUDIT2-MANT, 3 Oct 2026; was N3, VERIFY-MANT; superseded safe sentence on the right, current one in "Second adversarial audit" below) | `published` (see Key source) | "Applying Dr. Krauske's 1893 manuscript key table (SHStA Dresden, Loc. 694/10) to the unglossed cipher passage of Loc. 694/08 f.410 gives French in stretches (C 144, M 48, U 24 of 216 tokens); no prior plaintext or decipherment of this passage was located after the search logged in AUDIT.md, which covered Acta Borussica *Behördenorganisation* vol. 1 (1894) only by word counts." |
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

## Second adversarial audit (AUDIT2-MANT, account-4, 3 Oct 2026, 17:11-17:25 UTC)

A session separate from the solvers and from VERIFY-MANT. The job was to find the f.410 plaintext in print, starting from the
N4 step VERIFY-MANT named (Acta Borussica *Behördenorganisation* I read page by page, not only by word counts). No decoding was done.

| family | searched | result |
|---|---|---|
| (a) Acta Borussica *Behördenorganisation* I (1894, Schmoller & Krauske), the step VERIFY-MANT named | Internet Archive: nine `bub_gb_*` copies of the series, all djvu text fetched and identified. None is vol. I. `bub_gb_fnM5AQAAIAAJ` is vol. II (1714-20, printed 1898), and the others are vols. IV-IX. Google Books has **vol. I in full view** (`ESf8fHFG9ngC`, `IHM5AQAAIAAJ`, `wu-EWEtCN9sC`, `BlqBSdWlfOMC`, `H8WZD9dm0NQC`, `-y4jtRT_qxAC`). It was searched with the viewer's own search-inside endpoint (`books.google.com/books?id=ESf8fHFG9ngC&jscmd=SearchWithinVolume2&q=...`, JSON at HTTP 200, no captcha), which covers the whole volume's OCR. **Positive controls**: Manteuffel 20+ hits, and every report heading came back with its page: p. 204 (4 June 1712), 256-258 (19 Sept, 4, 7 and 23 Oct 1712), **285 (Nr. 82, Nov 1712, "Graf Dhona"; Nr. 83, 3 and 9 Dec 1712)**, 286, 307, 310 (Nr. 91, the *Nachschrift* of 26 Feb 1713), 321, 357, 359, 381 and 396. Other controls: "Prince Royal" 8 hits, Dhona 20+, Grumbkow 20+, "Chiffre" 4 (pp. 286, 287, 311, including Krauske's notes "Chiffre für Graf Christoph Dhona" and "Chiffre versehentlich statt 10 (= Blaspil)"). **Target terms**: Angleterre, d'Angleterre, Anglois, Anglais, Suedois, Suédois, Suède, Stettin, Stetin, contentement, Danemarc, Dannemarc, Whitworth and Witworth each gave **0**. "reine" gave 2 (p. 137, German "reine"; p. 312, the queen at a 1713 ceremony). "la paix" gave 1 (p. 258, "vivre en paix avec lui", Oct 1712, Krautt/Grumbkow). "son fils" gave 1 (p. 310, Friedrich I's deathbed "mon fils", 1713). "contraire" gave 3, of which p. 285 is Nr. 82 on Dhona's complaisance and does not match f.410. | **f.410's passage is not printed in vol. I.** The volume quotes Manteuffel only on court and administrative matters (Dhona, Ilgen, Grumbkow, Blaspil, Krautt, the King's household). The f.410 subjects (the Queen of England, the Swedes, peace, Stettin) do not occur in it at all. Nr. 91, the one printed *Nachschrift*, is Feb 1713 and on another subject. OCR-conditioned, but the controls hit every relevant report page. |
| (a) Krauske's other prints | Google Books `inauthor:Krauske` returned 0 items. "Krauske Manteuffel Chiffre" returned only Acta Borussica I and unrelated newspapers. NASG 14-19 had already been grepped (A2-SAX) and was not re-run. | no other Krauske print on these reports or their cipher found |
| (c) J. G. Droysen, *Geschichte der preußischen Politik* IV.1 (cited on Acta Borussica I p. 286 beside Nr. 82-83) | IA `droysen-geschichte-der-preussischen-politik-v-4-no-1` djvu text read by grep and by eye over the endnotes (Anmerkungen nos. 431-520). Manteuffel is quoted for 9 Feb 1712 (n. 431), 21 May 1712 (n. 485), July 1712 (n. 505), a memoir to Manteuffel on Stettin, mid-1712 (n. 510), 27 Jan 1713 (n. 518, "la reine" = the Prussian queen's illness), and 4, 8 and 19 Feb 1713 (nn. 519-520). The Toronto copy `p1geschichtederpre04droyuoft` was also checked (no Manteuffel; print_check no hits). | **no quotation from a Nov 1712 report and nothing matching f.410**. The Stettin memoir (n. 510) is the same topic, but its text differs. |
| (e) print_check.py (5 phrases in `phrases.txt`, sources in `sources.tsv`) | IA global full text, Google Books, OpenAlex, CrossRef, HTRC on njp.32101065980920, and Droysen IV.1 | no hit on any phrase in a relevant source. The ia-global and gbooks "hits" are loose word-AND matches in unrelated books (Nevers 1665, Mazarin, Marie Stuart, Scandinavian histories). Semantic Scholar answered 429 after 2 phrases and was not retried. |
| (b) scholarship on Flemming/Manteuffel | Google Books `inauthor:Haake Manteuffel Flemming` returned 0. "Manteuffel 'reine d'Angleterre' 1712 Berlin Flemming" returned 0. OpenAlex keywords returned the same titles VERIFY-MANT logged. | none. Haake's monographs and the 2016 Wackerbarth paper were still **not read in full**. |
| JSTOR | VERIFY-MANT's 3 rows stand. No new row: they cover both families. | queued, non-blocking (rule 10 template) |

No LOCAL-QUEUE row was written: vol. I was reachable in full view from the cloud, so the HathiTrust seq 434-440 read is not needed for this question.

**Class: N4** (revised from N3). The principal edition that prints decoded Loc. 694 extracts, the edition made by the man who made
the key, was searched in full text with passing controls, and it does not carry this passage. The standard narrative history,
which quotes these reports, was read at its endnotes. NASG, the holding archive's records, DECODE, the solver repositories
and the open indexes were covered by VERIFY-MANT and here. Not excluded: internal or unpublished work, Haake's Flemming
monographs and the Wackerbarth paper (scholarship read only through search APIs), and the unanswered JSTOR rows. The key source
stays `published` (Krauske's 1893 manuscript table, unprinted). It is not `ours`, so the "nearest equivalent of a first" wording does not apply.

**Safe sentence (current):** "Applying Dr. Krauske's 1893 manuscript key table (SHStA Dresden, Loc. 694/10) to the unglossed
cipher passage of Loc. 694/08 f.410 (Manteuffel to Flemming, Berlin, November 1712) gives French in stretches (C 144, M 48, U 24
of 216 tokens); no prior decipherment located: the passage is not among the extracts of these reports printed in Acta Borussica,
*Behördenorganisation* I (1894) or quoted in Droysen's *Geschichte der preußischen Politik* IV.1, searched in full text on
3 Oct 2026 (log in AUDIT.md)."

**Unsafe:** "first decipherment", "previously unread", "Krauske's key confirmed", "the reading is certain". The decode is partial
(M 48, U 24), and the fr18 judge FAILs it (-1.038 vs real_p05 -0.99). Only the shuffled-key controls support it.

Postmortem: VERIFY-MANT's note that "the 9 *Behördenorganisation* copies on archive.org are later volumes" holds, since vol. II and vols. IV-IX
are there and vol. I is not. Its date "Nr. 82, Berlin 23 Nov 1712" was not re-read at the heading itself: the search snippet shows
"... November 1712 ... Loc. 694. Graf Dhona" on p. 285, and the day number was cut off. The note is otherwise correct. Fixed `tools/print_check.py`
l. 303, which crashed on an OpenAlex work with a null `display_name`.
Requests: archive.org 24 (advancedsearch 3, metadata 7, djvu 13, print_check 1), books.google.com 37 (search-inside
JSON, 1.6 s apart, no challenge), www.googleapis.com 12, be-api.us.archive.org 10, api.openalex.org 6, api.semanticscholar.org 4
(429), api.crossref.org 1.

## Addendum GAPS180 (account-4, 3 Oct 2026): Haake and the Wackerbarth paper

The two items AUDIT2-MANT listed as "not excluded" under (b). Searched by word lists and search-inside, not read page by page.

| family | searched | result |
|---|---|---|
| (b) Paul Haake | IA advancedsearch `creator:Haake` (+August/Flemming/Sachsen) and titles "August der Starke"/Flemming: no Haake title on this subject. Google Books API (key, country=US) `inauthor:Haake "August der Starke"`: 9 titles 1902-1939, all NO_PAGES; books.google.com search-inside on 5 (jMU9AAAAIAAJ, CywIAAAAIAAJ, Mx_rcQAACAAJ, VCzSAAAAMAAJ, 780rHAAACAAJ) returned 0 even for the control "Flemming" (non-test). HathiTrust bibliographic API via Open Library OCLC numbers, then HTRC Extracted Features word counts: *August der Starke* (1926, mdp.39015033271936, full view), *König August der Starke* (1902, uc1.$b191675, 42 tokenised pp.), *Kursachsen oder Brandenburg-Preussen?* (1939, inu.30000055055671, search-only). Positive controls: Flemming 56 / 6 / 13; Manteuffel (OCR "Manteussel"/"Manteufsel") on 9 pages of 1926; Wackerbarth 8 / 0 / 1. Targets: Angleterre, d'Angleterre, Suédois, Suedois, contentement, Chiffre, Chiffren, chiffriert, Dhona, Whitworth = 0 in all three; Stettin 0 (1926), 9 (1939, no page with Manteuffel). 1926 seq 139-141 (Manteuffel, 1712 nearby) are character sketches (Paykull, Sidney, Engländer), not a report. 1939 seq 233 cites Krauske for 1722-26 Prussian matters. | no print of the f.410 passage or of Krauske's decipherment found (bag-of-words, OCR-conditioned). The 1929/1930/1934 titles and the 1922 essay were not readable (NO_PAGES, not in HathiTrust under the OCLC numbers tried). |
| (b) Rous 2016, "Der Weinkeller als Schlachtfeld" (in Gahlen et al., *Geheime Netzwerke im Militär 1700-1945*, doi:10.30965/9783657777815_004, OA) | Brill PDF: HTTP 202 challenge; BORIS (boris.unibe.ch/78675): Anubis wall; CORE: metadata only. Read through Google Books search-inside on RuHvEQAAQBAJ (PARTIAL). Controls: Wackerbarth 10, Manteuffel 10, Flemming 8, Krauske 2 (pp. 38-39, his 1905 edition, not the cipher). Targets: "Loc. 694", 694, 1712, Angleterre, reine, Stettin, dechiffriert = 0. | footnote 48 (p. 44) cites "SächsHStAD, 10026, Geheimes Kabinett, Chiffren de S. Exc. Mgr. le C. de Flemming, **Loc. 3234/5**; Chiffre, **Loc. 3233/4**": the Flemming cipher series beside DECODE record 4999 (Loc. 03233/02), **not Loc. 694**, used for the 1720s Société, not the 1712-13 reports. Not a print of this passage. |

**Class unchanged: N4.** No prior print found, so nothing to propagate to status.json or SECOND-OPINIONS-QUEUE.tsv. Haake's
volumes now count as searched (word counts, with controls) and Rous 2016 as searched (search-inside, with controls). Still
not excluded: internal or unpublished work, Haake's NO_PAGES titles, page-by-page reading of any of these, and the JSTOR rows.
Side lead for the key gap, not a novelty fact: Loc. 3233/4 and 3234/5 are Flemming cipher volumes, possible homes of a key
for the f.409v codes above Krauske's table.

Requests: archive.org 2, www.googleapis.com 4, books.google.com 23 (search-inside JSON, 1.6-1.7 s apart, a few empty
responses, no challenge page), openlibrary.org 1, catalog.hathitrust.org 5, data.htrc.illinois.edu 3, api.openalex.org 1,
api.core.ac.uk 3, brill.com 1 (202), boris.unibe.ch 1 (Anubis), library.oapen.org 1 (refused).

## Depth (DEPTH-REGRADE, 4 Oct 2026)

Verifier DEPTH-REGRADE (account 3, session_015eezFKYThEoRKoeamyhxSD), rule 4a / verifier step 3a; nothing decoded or changed. % = cipher tokens graded H/C/S (clear text excluded; counts as the cited reading file or audit gives them, nulls excluded where the file marks them); when evidence for a level is not on file the level below is given.
- **SHStA Dresden, 10026 Geheimes Kabinett, Loc. 694/08 f.410 lower block (frame 0511), P.S. o**: **D1** (Non-decrypted; outward "fragments read"), 66.7% (C 144 of 216). Check: Krauske 1893 table (17/17 with period glosses on f.468); f.410 decode gives fragments ('les Schvedois la paix', 'ne donne contentement'); fr18 judge FAIL. Class without a reading: not counted as a unique solve.

## Revision after AUDIT (R9-MANTV, 6 Oct 2026)

Verifier R9-MANTV (account 4, LANE LANE-RUN9-account-4, session_012DnG74vFmLJ3eycAh3zYRA), separate from the solvers R9-MANTPOOL
(session_01VrWrGx5EfmDVNbJiRwSHGM) and R9-MANTPC (session_018HJAXS5gcf5p5wVsdG2wjc). Rule 10 propagation / verifier step 4 of two
key changes made after this AUDIT.md was written. Nothing decoded; no key value added or changed.

**1. Re-derivation (06:46-07:05 UTC by date -u).**
- `r9mant/pooled_multi.py` re-run in a scratch copy with key.tsv as it stood when R9-MANTPOOL scored (commit 4452e2bfc): 101 runs,
  S 24 of 87 recurring free codes, shuffle mean 14.93, p95 19, max 23, known-answer 5/5, gate PASS. runs_r9.tsv, codes_r9.tsv,
  shuffle_r9.tsv and known_answer_r9.tsv byte-identical to the committed files (current `tools/interlinear_align.py`, which changed
  at 06:10 for R9-MANTPC, gives the same result).
- `r9mant/per_code.py` re-run in a scratch copy with key.tsv at commit 712239bc7 (R9-MANTPOOL's 24 rows, which the script strips):
  per_code_r9pc.tsv and per_code_ka_r9pc.tsv byte-identical. 7/24 BH PASS, power control 5/5.
- `tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712 --check`: exit 0, 423 tokens, C 202, M 98, U 123 -- matches the
  solvers' counts.

**2. Pre-registration order (git log, shallow clone deepened to 05:00 UTC).** PREREG-R9-MANTPOOL.md and pooled_multi.py added in
5d92dfc32 (05:47:11), header fixed in 4452e2bfc (05:47:27); scored outputs and key rows first committed in 712239bc7 (05:54:17).
PREREG-R9-MANTPC.md added in 633b7436e (06:03:36), header fixed 922f423e4 (06:03:43); per_code.py and its outputs first committed
in 45d3e9965 (06:18:44). Both PREREG files are unchanged since. Both predate their scored runs. (The commit hashes the solvers cite
are real; a shallow checkout shows only the 06:23 graft commit, which is why `git log` on the folder looked flat.)

**3. Controls (rule 3).**
- The matched control can vary on both statistics: the blended shuffle S ranges up to 23 (1000 draws), and every one of the 24
  per-code nulls has 2-7 distinct values (null_distinct column), so neither control is identical to the target by construction.
- BH applied as registered (q 0.10 over 24): sorted p 0.001, 0.003, 0.007, 0.008, 0.013, 0.014, 0.018 clear r q/24 (largest
  0.018 <= 0.0292 at r 7); the 8th, 0.037 (515), misses 0.0333; no later rank clears. 7 PASS, confirmed.
- One correction to NOTES.md's gloss: "roughly 2.4 expected false discoveries" is q x m (0.10 x 24). BH bounds the expected share
  of false discoveries among the 7 passes at 10%, i.e. under about 0.7 codes. The solvers' figure was the cautious one; it is not
  changed in NOTES.md, only noted here.
- Power control (5 known-answer C codes at n 10-15) does not subsample to the 24 codes' n 2-21 (rule 3, ARM3-ADJ). The removals at
  n 2-4 (295 e 2/2 p 0.135, 513, 613, 737) are therefore "untestable at this n", not shown wrong; R9-MANTPC's own text says so.

**4. The three codes kept at raw p < 0.10 (285, 515, 636).** Within the PREREG: PREREG-R9-MANTPC's "Actions (fixed in advance)"
says in so many words "per-code FAIL with raw p_v < 0.10: kept at M, note 'per-code FAIL ...'", and only raw p >= 0.10 is removed.
key.tsv follows that rule exactly (513 at p 0.1009 removed). No correction to key.tsv. The verifier's reading: these three are M on
the weakest footing in the key (not BH-significant, and two of them carry rule-4 conflicts, item 6), and none should be cited as a
reading of its own.

**5. Effect on the audited item (f.410 lower block, 216 tokens).** Only one f.410 token changed: L16 pos 2, code 402, U -> M 'la'
(per-code PASS). Item counts C 144, M 48 -> **49**, U 24 -> **23**. f.409v (154 tokens, not an audited item) moved M 24 -> 36, U 92 -> 80.
- **N-class: N4, unchanged** (the plaintext added is one M-graded article; nothing in the search log is affected).
- **Depth: D1, unchanged** (rule 4a; H/C/S = C 144 of 216 = 66.7%, unchanged, since every added value is M). `tools/depth_check.py`
  run 06:58 UTC: exit 0, f.410 listed as "class without a reading, not counted (D1)". status.json: depth and depth_pct unchanged;
  depth_unread updated to 23 U / 49 M, and the row's count fields brought into line.
- Safe sentence: the AUDIT2-MANT sentence stands with the counts updated to "C 144, M 49, U 23 of 216 tokens (one further code read
  at M from a pooled alignment of the leaves' interlinear glosses, 6 Oct 2026)". Unsafe: "the gloss alignment deciphered the
  nomenclator codes", "24 codes recovered" (14 of the 24 did not survive their own per-code test).
- SECOND-OPINIONS-QUEUE.tsv row SO-MANT-F410 (queued, not yet answered): its prompt quotes "C 144, M 48, U 24"; prompt updated to the
  new counts with a dated note.

**6. Per-code conflicts (rule 4), logged in HYPOTHESES.md.** 714: aligner chunk 'u' (3 runs) vs 'une' (2 runs) vs 0529's single-code
gloss 'un' (leaf_values_0529.tsv, M); 515: 'e' (3) vs 'p' (2) vs f0501 word_values 'Pr | propose' (the RUN5-MANT5 flag); 402 and 341
are corroborated by 0574's recurring pair 402.341 'la guerre' and by f0501's 402 'la', but that pair is one of the runs feeding the
aligner, so it is not an independent witness.

Requests: none (disk only). Vision: 0. Subagents: 0.

## AUDIT (depth re-check, DEPTH-MH)

Verifier DEPTH-MH (account 1, session_01LMs2EyN5RhSA1321cqQrnZ), 8 Oct 2026 02:43-03:0x UTC by date -u; separate from every
solver of this item and from DEPTH-REGRADE and R9-MANTV. Brief: .claude/briefs/runs/2026-10-08-acct3-scout-jobs.md "## DEPTH-MH";
bar: .claude/briefs/runs/2026-10-08-acct3-depth-bar.md, copied into PREREG-DEPTH-MH.md and pushed (fdab0b7b) before any
statistic. Nothing decoded; key, ciphertext, reading and N-class (N4) untouched.

**Rule 7.** `python3 tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712 --check`: tokens 423, C 202, M 98, U 123,
"reading up to date", exit 0. Item = the 216 `694-08_0511_f410_` tokens (C 144, M 49, U 23); the 8 `f410u` tokens are outside
the audited count.

**Statistics** (`python3 tools/depth_stats.py --tokens ciphers/sachsstaatsarchiv-manteuffel-1712/reading_tokens.tsv --key
ciphers/sachsstaatsarchiv-manteuffel-1712/key.tsv --line-prefix 694-08_0511_f410_ --cipher-class 'code<=120' --shuffle classes
--seeds 8100-8299 --out ciphers/sachsstaatsarchiv-manteuffel-1712/depth_mh`; outputs in depth_mh/):

| statistic | target | control (200 value-shuffled keys, classes kept, seeds 8100-8299) | result |
|---|---|---|---|
| longest H/C/S run, cipher codes 1-120 only (M/U/code break it) | 11 letters ('n t r e le s sch v', M1) | none (key-independent) | -- |
| same, C nomenclator tokens let through | 21 letters ('s e a la reine d'Angleterre', M2) | none | -- |
| AD = 1.5 x H(K)/R | H(K) = 60 distinct cipher codes x log2(35) = 307.8 + liberties 175.7 (49 M, 23 U) = 483.5 bits; R = 1.908 (fr18 5-gram held-out H 2.792); unicity 253, **AD 380 letters** (213 at R = 3.4) | -- | **cipher clause fails** (11 vs 380) |
| (i) longest decoded stretch segmenting into fr18 words | **55** | p95 43, max 54 | **item control passes** |
| (ii) code 217 'la reine d'Angleterre' (C), 3 occurrences, 3 independent contexts: 8+value+8 window, mean log2 P/letter | -2.806 / -2.533 / -2.815 | p95 -3.764 / -3.746 / -3.705; max -3.136 / -3.300 / -3.021 | **3/3 above p95** |
| (ii) flanks only (value gapped out) | -3.589 / -2.878 / -3.476 | p95 -4.468 / -4.308 / -4.373 | 3/3 above p95 |

390 Stettin occurs once in the item (no second context); no other code-class value recurs in f.410.

**Code clause, (c) the verifier's reading of each context** (liberties listed):
1. M2: `r|re|ro q u e l ? s e c|ch o|ou|ous s e a [217] ? ?` -> "... quel[?]se chose à la reine d'Angleterre ..." -- reads as
   "quelque chose à la reine d'Angleterre" only if the unkeyed group is taken as 'que' and the 'se' before 'chose' is left
   over: one U, three M, one repair. Weak; not relied on.
2. L13: `? ? a ? [217] ? t o u ch a n t le|la p r i n c e` -> "... à [?] la reine d'Angleterre [?] touchant le prince". Two U
   outside the phrase, M le|la and M c. Reads sensibly.
3. L14 -> M4 (M4 is the band between L14 and L16, NOTES.md (2), so the order is the leaf's): `f i l s|sa ? [217] ? ? n e f e |
   r|re|ro a r i e n p o|ou|ous u r|re|ro l u i m a i s l u y` -> "... fils [?] la reine d'Angleterre [? ?] ne fera rien pour lui,
   mais luy ...". Three U, four M. Reads sensibly.
Contexts 2 and 3 are independent (different codes on both sides, different lines) and both read with 217's meaning, so the code
clause is met. The C grade on 217 (Krauske's table, 17/17 with the f.468 glosses) is not what meets it; under the bar that
agreement is a D3/D4 external-check element only.

**Verifier's sentence (written from the reading, no edition used):** "In this postscript the Queen of England is named three
times: once in a phrase reading 'touchant le prince', and once followed, after two unread groups, by 'ne fera rien pour lui,
mais luy ...'."

**Ruling: D2** (was D1, DEPTH-REGRADE 4 Oct 2026). Code clause met (217, two sensible independent contexts, 3/3 windows above
the 200-shuffle p95, flanks-only too) + item control (i) passed (55 vs p95 43, max 54) + the sentence above. Cipher clause not
met (longest letter run 11 against AD 380). depth_pct 66.7 (C 144 of 216). Outward words: "partially deciphered (about 67% of the
cipher text)"; DECODE mapping "Partially decrypted". The fr18 judge FAIL near its gate is the ZX-DEC349 shape and was not used.
Limits: (i) beats the shuffle maximum by one letter only; the ruling rests on one code value; D3 would need >= 80% H/C/S.
Not changed: SO-MANT-F410 (its prompt quotes no depth and the counts are unchanged).

## AUDIT (FAM-MANTV)

Verifier FAM-MANTV (account 2, LANE FAMILY, 8 Oct 2026, 16:54-17:1x UTC by date -u); a separate session from the solver FAM-MANT15
and from every earlier verifier of this target. Brief: .claude/briefs/runs/2026-10-08-ytbiz-family-1613-jobs.md "### FAM-MANTV".
Depth bar copied into PREREG-FAM-MANTV.md and pushed (c253ff720) before any depth statistic. Nothing decoded beyond the re-derivation;
key.tsv, the ciphertexts and the readings are untouched.

**Items.** A = SHStA Dresden 10026 Geheimes Kabinett Loc. 694/09, URL files 0015+0016 (f.8-8v): "Extrait de la relation de M. de
Gersdorf du 3 Janv. 1713" (Gersdorff, Saxon envoy at The Hague; clear first page 0014, f.7), sent with Manteuffel's letter of 13 Jan
1713; 69 cipher tokens in 8 runs inside clear French (f0015_09/). B = Loc. 694/09 0052 (slip beside the extract sent with Manteuffel's
letter of 11 Feb 1713), 43 tokens in 3 runs (f0052_09/). Solver's reading of A (key application of Krauske's 1893 table, C 47 M 21
U 1): "le dit C. ne desesperoit pas d'en empecher les suites"; "Celui [deser?] qui m'en a fait ce recit"; "comme si la Porte vouloit
reconnoitre Stanislas pour [r]oy"; "que [159] avoit fait garder ses papiers ches Colliers"; f.8v "quelqu'un de la part de Stanislas
y est recu comme l'envoye"; "il feroit tout son mieux pour empecher les suites de cette resolution prise a la Porte".

**1. Re-derivation (rule 7).** `python3 tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712[/f0015_09|/f0052_09] --check`:
exit 0 all three ("reading up to date"; A C 47 M 21 U 1; B C 29 M 11 U 3). Shuffle gates re-run unchanged except the seed
(scratch copies of shuffle_gate_0015.py / _0052.py): A seed 77113, real -1.010 vs 1000 shuffled keys mean -2.016, p99 -1.597,
max -1.443, 0/1000 at or above -> PASS (solver: seed 15, 0/1000, p99 -1.608); power control 0085 r9+r10 1/1000 PASS. B seed 77152:
real -1.394 vs p99 -1.553, max -1.311, 1/1000 -> PASS (solver 2/1000). Reproduces. The gate says the Krauske table is the right
key family for these leaves; it is not a reading.

**2. Transcription spot check.** Frames 0015, 0016, 0052 fetched once from www.archiv.sachsen.de (3 requests, 1.6 s apart, 200;
sha256 prefixes 97842410, 5496f00b, 1ba248b1, identical to the solver's), cropped at the solver's regions and read by me at native
scale. 0015 r1 (16 groups), r2 (5), r3 (8), r5 (21), 0016 r1 198, r2 376, r3 (16) and 0052 r1/r3 all agree group for group with
ciphertext.tsv; 0015 r1 tok15 reads 66 (the solver's low flag stands); 0052 r1's first group is overwritten (465/405) as flagged.
No disagreement found in 4 spot runs (A: 0015 r1, r3, r5; 0016 r3) beyond the solver's own low-confidence flags.

**3. Prior-work checks 1-5 (by hand; tools/prior_work.py absent).**
1. Our own work: the solver's check (grep of NOTES/AUDIT/HYPOTHESES/mant0609/ROOM) re-read; only MANT-0609's rank and R13-MANTSCR's
   screen line precede FAM-MANT15. CLEAR.
2. Leaf and neighbours: solver fetched and eye-read 0013-0018, 0051-0053, no gloss/clear copy; I re-read 0015/0016/0052 at the crop
   regions: no interlinear or marginal decipherment over A's runs. 0052 carries small interlinear numerals over run 1 (role unsettled,
   solver's note stands). CLEAR for A.
3. Holder/portal/solver repositories: offline, as the solver; no item-level catalogue note. CLEAR offline.
4. Edition and calendar identity (left "unchecked" by the solver): no edition of Gersdorff's Hague relations is known to this repo;
   Google Books API (country=US, key) 5 queries ('"Gersdorf" relation 1713 Stanislas Porte Colyer' 0; 'Gersdorff Manteuffel 1713
   "Stanislas" Haye relation' 0; 'Goltz papiers Colyer 1712 Stanislas envoyé Porte' 0; '"ne desesperoit pas d'en empecher"' 214, first 6 unrelated (Varillas,
   Saint-Simon, Louis XIII); 'Colyer Goltz Adrianopel 1712 Stanuslaus' 4, all Feldzüge des Prinzen Eugen von Savoyen (1891) on the
   1712-13 Porte crisis, a secondary account of the same events, not of this relation); IA full text (be-api) '"relation de M. de
   Gersdorf"' 0, '"Stanislas pour roy" Gersdorf' 0 (control '"graaf Colyer"' 1 hit, so the route answers). Acta Borussica BO I,
   Droysen IV.1 and NASG 14-19 were searched by earlier verifiers for Manteuffel's reports, not for Gersdorff's; Sbornik RIO and the
   Leszczynski literature: UNCHECKED (not reached in this box).
5. After decode, other correspondents' versions of the same news (the leaf's own clear text says "Ces lettres sont du 12 & du 18 Nov"
   and "Et comme Mr de Colier mande"): **SUBSTANCE FOUND.** Huygens retroboeken, Briefwisseling van Anthonie Heinsius Deel 14
   (RGP GS 226), full-text search 'Colyer' within Deel 14 (35 hits, 2 requests), then the OCR pages read (4 requests,
   retroapp/service_heinsius/14_226/html/heinsius_14_GS226_{214,215,236,237}.html):
   - **no. 336, Colyer to Heinsius, Pera, 12 Nov 1712 (H.A. 1686), pp.213-214**: "Den heer generael-majoor Goltz, internuntius van
     Polen alhier, bevreest wesende dat insgelijx gevangen geset mogte worden, heeft alle sijne schrifturen elders doen verbergen
     ... de Turcken den coning Augustus ... niet begeeren t'erkennen, maer Stanislaus (van wien gister een envoyé over Bender alhier
     is aengelant) op den troon van Polen sullen tragten te herstellen"; P.S. "den envoyé Crispin van Stanuslaus hier gecaresseert
     wert".
   - **no. 367, Colyer to Heinsius, 18 Nov 1712, p.236**: confirms the 12 Nov news ("het armement van een envoyé extr. van den
     gecroonden Stanuslaus alhier, ende dat den G. Heer voorgenomen soude hebben opgem. Stanuslaus op den troon van Polen te doen
     herstellen"); the mufti "zich verlegen vint" (the leaf's clear text: "puisque le Mufti etoit absolument contraire").
   Diff against A's cipher spans: "comme si la Porte vouloit reconnoitre Stanislas pour roy" = Colyer's Stanislaus "op den troon ...
   te herstellen" (agree); "quelqu'un de la part de Stanislas y est recu comme l'envoye" = Colyer's envoy of Stanislaus arrived and
   "gecaresseert" (agree); "[159] avoit fait garder ses papiers ches Colliers" = Goltz "heeft alle sijne schrifturen elders doen
   verbergen" (agree in substance, Gersdorff names the place as Colyer's; 159 = Goltz is an identification I, not a key value, and
   is not entered in key.tsv); "le dit C. ne desesperoit pas d'en empecher les suites" / "feroit tout son mieux pour empecher les
   suites de cette resolution" and "deser": not in nos. 336/367 (Colyer's wish to mediate and be excused from following the court is
   close but not the same sentence). So three of the five readable cipher spans relay news already printed from Colyer's own letters;
   the agreement is also a non-statistical external check of the key application on this leaf (three specific facts, none supplied
   to the solver). Gersdorff's own French text was not found in print.

**4. Depth (rule 4a, depth bar of 8 Oct; PREREG-FAM-MANTV.md).** `tools/depth_stats.py --cipher-class 'code<=120' --shuffle classes
--seeds 8100-8299` on each item (outputs f0015_09/depth_mantv/, f0052_09/depth_mantv/):
| | A (0015+0016) | B (0052) |
|---|---|---|
| H/C/S % | 68.1 (C 47 of 69) | 67.4 (C 29 of 43) |
| longest H/C/S run, cipher codes only | 8 letters ('e s p a p i e r') | 8 ('n u d e v a n t') |
| AD (H(K) = distinct codes x log2 35 + liberties; R 1.908) | 137.9 (77.4 at R 3.4) | 127.0 (71.3) |
| cipher clause | fails (8 vs 138) | fails |
| control (i) word-segmenting stretch | 53 vs p95 50, max 72: passes p95, below max | 25 vs p95 31: fails |
| code clause, 198 Stanislas (C), 2 contexts | windows -4.104 / -3.474 vs p95 -3.973 / -3.280: **both below** (flanks-only above) | no recurring code |
Pre-registered rule: the code clause needs both windows above p95; both are below, so **the code clause is not met** for A. Note for
the next verifier: depth_stats.py builds its 8+value+8 window from cipher tokens only, so on a leaf where each cipher run is an island
in clear French the flanks splice letters from the neighbouring runs (here 'e s|sa e r' from the 'deser' run, 'i e r s|sa' from the
end of 0015 r5), not 198's real context ("reconnoitre [198] pour roy", "de la part de [198] y est recu"). That makes the window
statistic a poor test on this shape of leaf; it is recorded, not overridden (ROOM flag for the parent). The external check of step 3.5
is a D3/D4 element under the bar and does not replace the clause at D2; D3 is out anyway (68.1% < 80%).
**Ruling: A D1** ("fragments read"; DECODE mapping Non-decrypted), depth_pct 68.1. **B D0** (the key ranks first, 1/1000 and 2/1000,
but nothing reads: 'un pour', 'devant', 'elle'; control (i) below p95). No D2 sentence is written.

**5. Classification (rule 10).**
- **A: N2** -- the news carried by its cipher spans is known in print elsewhere (Colyer to Heinsius, 12 and 18 Nov 1712, Briefwisseling
  van Anthonie Heinsius Deel 14 nos. 336 and 367, pp.213-214, 236), and no prior mapping of this ciphertext (Gersdorff's relation of
  3 Jan 1713 as forwarded to Manteuffel, Loc. 694/09 f.8-8v) to it was found. Key: published (Krauske's 1893 manuscript table, someone
  else's non-period key, credited). Prior plaintext: in substance yes (Colyer, printed; earliest citation found Heinsius Deel 14, RGP Grote
  Serie 226) -- Gersdorff's own wording no. Prior decipherment: none located. Evidence quality: re-derivation clean, transcription
  spot check clean, key family gate 0/1000, external agreement on three facts. Confidence: medium-high on N2 (the class could only
  fall to N1 if Gersdorff's relation itself is printed, e.g. in Sbornik RIO or a Saxon-Polish edition, unchecked).
  Safe sentence: "Applying Dr. Krauske's 1893 manuscript key table to the unglossed cipher spans of an extract of Gersdorff's Hague
  relation of 3 January 1713 (SHStA Dresden, Loc. 694/09 f.8-8v) gives French fragments -- the Porte recognising Stanislas as king, his
  envoy received, papers kept at the Dutch ambassador Colyer's -- whose news is already printed in Colyer's own letters to Heinsius of
  12 and 18 November 1712 (Briefwisseling van Anthonie Heinsius XIV, nos. 336, 367)."
  Unsafe sentence: "A previously unread report on the Porte and Stanislas has been deciphered."
- **B: no class** -- nothing reads (D0); a class needs a reading. The slip's key family is confirmed (gate 1/1000); the next step is
  the solver's own (native re-read of 4 groups), not an audit.
- Not queued: no SECOND-OPINIONS-QUEUE row and no AUD2-FAMILY-1 WORK-QUEUE row (the brief gates both on N3+ and D2+; neither item
  qualifies).

**6. Postmortem and corrections.** Failure caught: the solver's check 4/5 searched only the decoded French phrases and left the
other-correspondent route unchecked, although the leaf's clear text names the source ("Mr de Colier mande", letters of "12 & 18 Nov")
-- one search of the printed Heinsius edition by sender and date found the same news (the "other correspondents' versions of the same
news" clause of prior-work check 5, the Eckert shape). Over-claim found: none outward (the solver wrote "no novelty class" and "Not
located in what was searched (a search result, not a novelty statement)"); NOTES.md's FAM-MANT15 line 'Next: (3) a verifier ...' is
now done -- noted under Remaining gaps. Requests this audit: www.archiv.sachsen.de 3, resources.huygens.knaw.nl 6, www.googleapis.com
5, be-api.us.archive.org 4; no 403/429/challenge.
## G3 check (V1-G3D)

Verifier V1-G3D (account 3, session_01B3GbNMSz6kStoU6DvctLBF, for LANE-VERIFY-1), 8 Oct 2026, 16:56-17:0x UTC by `date -u`.
This is the prior-work-step.md check 5 on the 694/08 f.410 lower block (N4, two audits, D1 per DEPTH-MH). It is not a third full audit,
and nothing was decoded. Account check: VERIFY-MANT, AUDIT2-MANT and the f.410 readers were not account 3. MANT-0609 (account 4 for the
account-3 orchestrator) was a frame inventory, not a reading or an audit of f.410. 694/09 (FAM-MANT15/FAM-MANTV, live today on account
2) was not touched.

Prior-work checks 3-5:
- **Check 5, decoded phrases:** AUDIT2-MANT's print_check run on the five `phrases.txt` stretches (3 Oct) stands and was not repeated.
- **Other correspondents' and later quotations of the same reports.** IA full text (be-api) `"Manteuffel" Stettin 1712 Flemming` ->
  6,225 loose matches. Its relevant new hit is Droysen, *Geschichte der preußischen Politik* IV.2 (1886, IA
  `droysen-geschichte-der-preussischen-politik-v-4-no-2`). AUDIT2-MANT had read only IV.1. The djvu text was fetched once and grepped.
  IV.2 quotes Manteuffel's Berlin reports from 1713 on (Friedrich Wilhelm I's accession, 18 April, 20 May, 18 Oct, 1718), and none of
  November 1712. It has no "reine d'Angleterre", "ne fera rien" or matching "contentement" passage. **Negative.** A second fts
  query (Berlin Novembre 1712 Stettin "Reine d'Angleterre") failed on a malformed response and was not retried.
- **Press of the day** (November-December 1712). Google Books (key, country=US) gave 0 on all three of:
  - `"Mercure historique" 1712 Stettin "reine d'Angleterre" Berlin Danemarck`
  - `Fama 1712 Stettin Sequestration Berlin Manteuffel`
  - `Berlin novembre 1712 Stettin Suedois Danemarc "reine d'Angleterre" prince`

  IA advancedsearch found no dated 1712-13 *Mercure historique et politique* items. *Europäische Fama* volumes are on IA
  (`bub_gb_*`) but undated in the metadata, so the November 1712 issues were not identified. **Partly searched**; the issue-level
  read is unchecked. A monthly would not share the P.S.'s specific content (the Queen of England's displeasure touching the prince,
  Stettin), only the public news of the Pomeranian campaign.

Result: no print hit. **Class kept: N4.** D1 stands (not re-examined). status.json and SO-MANT-F410 are unchanged. Requests:
archive.org 4 (advancedsearch 2, metadata 1, djvu 1, plus one 404 on a guessed filename), be-api.us.archive.org 2,
www.googleapis.com 3.

## AUDIT 2 (AUD2-MANT8)

Verifier AUD2-MANT8 (account 3, session_014k9UgQiKu87EKCZt1gq2eA, for LANE-VERIFY-2), 8 Oct 2026, 19:58-20:2x UTC by `date -u`.
Second adversarial audit of item A only: Loc. 694/09 f.8-8v (URL files 0015+0016), the extract of Gersdorff's Hague relation of
3 Jan 1713 sent with Manteuffel's letter of 13 Jan 1713 (status.json results[194]). Account check: the reader (FAM-MANT15) and the
first auditor (FAM-MANTV) were account 2. Account 3 had only run a G3 check on 694/08 f.410 (V1-G3D), never on f.8. Item B (0052)
has no class and was not audited. Nothing decoded.

**Duplicate diff.** status.json results[194] is the only filed entry for 694/09 f.8-8v / Gersdorff 3 Jan 1713. No other ID in
NOTES.md or status.json has this pointer, date or addressee. Not a duplicate.

**Re-derivation.** `python3 tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712/f0015_09 --check` gave "reading up to date",
C 47, M 21, U 1, exit 0. This matches FAM-MANTV. The shuffle gate was not re-run, since FAM-MANTV already re-ran it on a new seed.

**Prior-work checks 3-5.**
- `tools/prior_work.py ... --item-spec 'shelfmark=SHStA Dresden 10026 Loc. 694/09;folio=8-8v;date=1713-01-03;sender=Gersdorff;recipient=Manteuffel' --step-type second-audit --fetch`
  exited 4 with these holds:
  - LEAD 1-own: FAM-MANTV's claim (it is the first audit, already written above), this session's own claim, and MANT-08 (its claim is
    for 694/08 frames). All three were recorded CLEAR.
  - UNCHECKED-NET 3-solver: aaymeloglu, no clone. Bourdeau caches: CLEAR.
  - UNCHECKED-NET 4-editions: no prior_editions.tsv row. Checked by hand (below) and recorded CLEAR.
  - CONTEXT 3-tomokiyo: spanish.htm "ff.7-9", which is the Reyes Católicos cipher and unrelated.
- `--reading <scratch>/reading_A.txt --network` (G3, the five readable spans) gave two LEADs, both recorded CLEAR after the snippets
  were read:
  - 'de la part de Stanislas': ia-global, 57 items. This is a generic phrase and the items are other texts.
  - 'la Porte vouloit reconnoitre Stanislas': gbooks, 82 volumes, all loose matches. Nordberg's *Leben Carl des Zwölften* (1751)
    prints other documents of the same 1712-13 Porte crisis ("la Porte ne veut pas admettre l'Envoïé de Sa Majesté à l'audience").
    The exact form "reconnoître STANISLAS pour Roi" is Lamberty's text on the 1704 election. There is also the Rákóczi
    correspondence. None of them carries Gersdorff's sentence.
- **Families FAM-MANTV left unchecked:**
  1. **Gersdorff's own Hague letters (Heinsius edition).** Huygens retroboeken `heinsius/search_in_text`, source_id=14 (Deel 14,
     1 Sept 1712 - 30 Apr 1713, RGP GS 226). 'Gersdorff' gave 23 hits. The edition prints Gersdorff's letters to Heinsius of 12 Sept,
     12 Oct and 14 Nov 1712, and of 2, 15, 16, 19, 23 and 26 Jan, 1 and 5 Feb, 26 Mar and 14 Apr 1713. **No. 531, 2 Jan 1713 (H.A. 1780),
     pp.344-345**, written one day before the relation, was read in full (OCR pages). It contains New Year wishes and the arrears of the
     Saxon troops in English pay, and has nothing on the Porte, Stanislas, Goltz or Colyer. The other Jan 1713 letters were seen only as
     search snippets (Mainz, troops), which is weaker than a full read. 'Gersdorf' across all 19 volumes gave 10 hits, none in Deel 14.
     'Goltz' in Deel 14 gave 12 hits; the new hit is **no. 453, Colyer to Heinsius, Pera, 12 Dec 1712, pp.294-295**, with a copy of
     Goltz's letter to Colyer, Adrianople, 20 Nov 1712. Colyer and Sutton cannot follow the court without orders, but "in hope leefden"
     that Goltz could undeceive the Sultan, and "de saake wel een anderen tour soude connen nemen". This is close in substance to the
     cipher's "le dit C. ne desesperoit pas d'en empecher les suites", but it is a later letter than the 12 and 18 Nov letters the leaf
     cites, and it is not the same sentence. 'papieren' in Deel 14: 6 hits, none about Goltz. 'Stanislaus Goltz': 2 hits (pp.214 and
     655), both already known.
     Gersdorff's relation itself is **not in the Heinsius edition**, because it was sent to Dresden and not to Heinsius.
  2. **Lamberty, *Mémoires pour servir à l'histoire du XVIII siècle* VII and VIII** (IA `memoirespourserv07lamb`, `...08lamb`, be-api
     fts per identifier). 'Colyer', 'Colier' and 'Goltz' gave 0 in both volumes. 'Gersdorf' gave 0 in VII and 1 in VIII: a resolution
     on a memorial of 18 Feb 1713 about the troops, which is unrelated. As a control, 'Stanislas' and '"Grand Seigneur" Stanislas
     Pologne' each answered, so the route works. Negative.
  3. **Droysen IV.2** (IA `droysen-geschichte-der-preussischen-politik-v-4-no-2`). 'Gersdorf' and 'Gersdorff' gave 0. 'Stanislaus
     Pforte' gave 1 hit, a general narrative of the Porte and Charles XII. Negative.
  4. **Sbornik RIO / a Saxon-Polish edition.** The IA advancedsearch lists Sbornik volumes but none indexed by subject. Searches:
     - Google Books 'Sbornik "Gersdorf" 1713 Haye Stanislas': 0.
     - IA fts '"Gersdorf" "Colyer"': loose noise.
     - IA fts '"Goltz" "Colyer" 1712 Adrianople' turned up two sources on the same crisis that do not carry Gersdorff's text:
       - *The despatches of Sir Robert Sutton, ambassador in Constantinople 1710-1714* (Camden 3rd ser., IA `despatchesofsirr0000unse`).
         In-item fts: 'Gersdorf' 0, 'Goltz papers' 0. 'Stanislaus envoy' 1 hit, which reads "the Polish Embt and Mons? Crispin, King
         Stanislaus his Envoy equally under confinement". Crispin as Stanislas's envoy is the same fact as the cipher's "l'envoye";
         be-api gives no page.
       - Feldman, *Polska a sprawa wschodnia 1709-1714* (KPBC). 'Gersdorf' 0.

     A volume-by-volume read of Sbornik RIO was not done, so the family is **partly searched**. Sbornik prints Russian diplomats'
     papers, which is not where a Saxon envoy's relation to Dresden would appear.
  5. **Press of the day.**
     - Google Books: '"Mercure historique" 1713 Stanislas Porte "Colyer"' 0; '"Mercure historique et politique" janvier 1713 Stanislas
       Porte envoyé Mufti' 0; '"Europäische Fama" 1713 Stanislaus Pforte Goltz' 0.
     - IA: advancedsearch finds no dated 1712-13 Mercure items. The Europäische Fama items (`bub_gb_*`) are undated in their metadata,
       so the issues were not identified.

     **Partly searched** (V1-G3D's finding repeated). Issue-level reads are unchecked.
  6. **G3, exact phrases.**
     - IA fts: '"tout son mieux pour empecher les suites"' 0; '"ne desesperoit pas d en empecher les suites"' 0; '"papiers chez"
       Colyer Goltz' 0; '"ses papiers chez le comte Colyer"' 0; '"Stanislas pour roi" Porte 1713 Colyer' 0.
     - Google Books: '"empecher les suites de cette resolution"' gave 354 loose hits (law treatises), none relevant; '"Gersdorf"
       "3 janvier 1713"' gave 71 loose hits (genealogy), none relevant; '"tout son mieux pour empecher les suites"' got HTTP 503
       twice (one retry after 20 s, then stopped, per the good-citizen rule) and was run on IA instead (0).

**Correction to the safe sentence (over-claim found).** FAM-MANTV's sentence says "papers kept at the Dutch ambassador Colyer's" is
news "already printed in Colyer's own letters". Colyer's no. 336 says only that Goltz "heeft alle sijne schrifturen **elders** doen
verbergen" ("had all his papers hidden elsewhere"). The detail that they were kept at Colyer's comes from the cipher alone, at grade C,
and is not in the print. FAM-MANTV's own step 5 said this correctly ("agree in substance, Gersdorff names the place as Colyer's"), but
the safe sentence and status.json `line` dropped the distinction. Corrected sentence below.

**Depth (rule 4a, keep or lower).** D1 kept. Nothing new bears on it:
- 68.1% C, so D3 is out.
- The cipher clause fails (longest run 8 vs AD 138).
- The code clause is not met, with FAM-MANTV's flag on the window tool for a leaf where the cipher runs sit inside clear text.
- The printed agreements, now Colyer 12 Nov, 18 Nov and 12 Dec and Sutton on Crispin, are an external check on the key application,
  not a depth clause.

There was no reason to lower to D0: three spans read as specific, externally confirmed facts.

**Classification (rule 10).**
- **A: N2, confirmed.** Prior plaintext: the substance yes, Gersdorff's wording no.
  - The substance is in Colyer to Heinsius, 12 and 18 Nov 1712 (Heinsius XIV nos. 336 and 367, pp.213-214 and 236), with related news
    in no. 453 (12 Dec 1712, pp.294-295), and in Sutton's printed despatches (Crispin as Stanislas's envoy).
  - Gersdorff's own relation was not found in the Heinsius edition (his printed letters of 2-26 Jan 1713 do not carry it), Lamberty
    VII-VIII, Droysen IV.2, the Sutton despatches, or the phrase searches.
  - Sbornik RIO and the press were only partly searched. N1 stays possible only if a Saxon-side edition prints Gersdorff's relations,
    and none was located.
- Key: published (Krauske 1893 manuscript table, credited). Prior decipherment: none located. Confidence: medium-high.
- **Safe sentence (corrected):** "Applying Dr. Krauske's 1893 manuscript key table to the unglossed cipher spans of an extract of
  Gersdorff's Hague relation of 3 January 1713 (SHStA Dresden, Loc. 694/09 f.8-8v) gives French fragments: the Porte recognising
  Stanislas as king, his envoy received, and the Polish envoy Goltz's papers kept at the Dutch ambassador Colyer's. The first two items
  are already printed in Colyer's letters to Heinsius of 12 and 18 November 1712 (Briefwisseling van Anthonie Heinsius XIV, nos. 336,
  367), which say only that the papers were hidden 'elsewhere'."
- **Unsafe sentence:** "A previously unread report on the Porte and Stanislas has been deciphered", or "all of its news is already in
  print".
- No SECOND-OPINIONS-QUEUE row: the item is N2 D1, below the N3 gate. No row exists for 694/09.

**Postmortem.**
- The first audit's search found the right other-correspondent source. Its safe sentence then generalised "agree in substance" into
  "already printed" for a detail the print does not carry. That is a small over-claim of *prior* print, and it would understate this
  reading if repeated.
- Families now covered: Heinsius XIV for Gersdorff's own letters, Lamberty, Droysen IV.2 and Sutton. Still open: an issue-level read of
  the Jan-Feb 1713 Mercure historique and Europäische Fama, and a volume index read of Sbornik RIO (both low yield).

**Requests:** resources.huygens.knaw.nl 7, be-api.us.archive.org 18, archive.org 4, www.googleapis.com 15 (three HTTP 503s, one retry
each), net calls by prior_work.py (ia-global, gbooks). No 403, 429 or challenge.

## AUDIT (V-MANT08)

MANT-FIX applied 8 Oct 2026 (NOTES.md "MANT-FIX (8 Oct 2026)"): the 0391 r4 tok5 39, 0390 r9 tok3 9 and r5 tok1 160 (M) fixes and the 217 line 8 / line 14 (M) additions are in f0390_08/ciphertext.tsv; reading now 95 tokens C 58 M 37; classes and depth unchanged.

Verifier V-MANT08 (account 2, LANE FAMILY, session_01LGtcNsB7fhJKGzmPRCaMLw), 8 Oct 2026, 20:39-20:5x UTC by `date -u`; a separate
session from the solver MANT-08 and from every earlier verifier of this target. Brief: .claude/briefs/runs/2026-10-08-ytbiz-family-1909-jobs.md
"### V-MANT08". Claim under audit: NOTES.md section MANT-08 (f0390_08/): 89 code tokens on SHStA Dresden 10026 Loc. 694/08 URL frames
0390, 0391, 0395, 0485 read with Krauske's 1893 table (C 54, M 35), pooled shuffled-key gate 0/1000, judge fr18 FAIL at N=83, read in
context "la treve, Oxford, detacheroit [Danemark], duc Ferdinand [of Courland], la Courl[ande], Breton". Depth rule pre-registered in
f0390_08/PREREG-V-MANT08.md (pushed 875543f1) before any depth ruling. Nothing decoded beyond the re-derivation; key.tsv, the
ciphertexts and the readings are untouched.

**Items** (one per letter; frame numbers are URL numbers): A 0390, Manteuffel, Berlin, letter begun 10 Oct 1712 (second leaf);
B 0391, P.S. of 13 Oct 1712 ("Berl. ce 13 Oct. 1712"); C 0395, a letter of mid-Oct 1712 (between 0391 and the clear Copenhagen
enclosure of 9 Oct on 0396); D 0485, the letter of (or just before) 12 Nov 1712.

**1. Re-derivation (rule 7).** `python3 tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712/f0390_08 --check`: "reading up
to date", tokens 89 C 54 M 35, exit 0; the main folder `--check` exit 0. gate.out re-read (seeded script; not re-run): pooled 83 letters
real -1.483 vs 1000 shuffled keys p99 -1.649, 0/1000 -> PASS, power control 0085 r9+r10 1/1000; per frame 0391 0/1000, 0485 16/1000
(FAIL), 0390 307/1000 and 0395 0/1000 not gated. The gate says Krauske's table is the right key family for these leaves; it is not a
reading. The 0391 r5 "known-answer" check is void as the solver says (bon gre malgre is a caret insertion, not a gloss).

**2. Transcription spot check (native frames, 4 requests to www.archiv.sachsen.de, 2 s apart, 200; region crops by
`tools/iiif_lines.py --image <frame> --region <solver's region> --lines-per-crop 3` plus 2-3x zooms; read by me, no subagent).**
Tokens compared: 0390 r7 (6), r9 (7); 0391 r1 (6), r4 (11), r5 (10); 0395 r1-r3 (18); 0485 r1-r6 (21): 79 tokens. Agreements: all
but the three below. Disagreements, for the solver to apply (not applied here):
- **0391 r4 tok5 is 39, not 34**: the glyph is the folder's own y-shaped 9 ("3y", the same form the solver accepts as 9 in 0391 r5
  "33.y.59" and in 0395). 39 = i (C), so the run reads b|[a] u l l i n b r|re|ro o|ou|ous u g = **Bullinbroug** as written: no
  changed token. The solver's "one token I" falls away; pass A's 39 was right.
- **0390 r9 tok3 is the y-glyph 9, not 4**: 1.26.9.55.35.21.120 = f r i b|[a] e n d. "Fr[ie]s[e]nd[orff]" now needs one changed
  token (55 -> 57 s), not two; still a hypothesis (I), not a reading.
- **0391 r5 tok1**: the second glyph has the tall bowl this hand uses for 6 (cf. "16" in r1), so 160 by shape, 100 by sense (d ->
  "detacheroit"; 160 = Manteuffel makes no sense after "on"). The solver's alt stands; tok1 is M, not C, on the image.
- **Omissions**: 0391 carries **217 three times**, not once: "et voicy ce que 217 s'est expliqué par ses ministres au sujet des affaires
  du nord" (line 8), "33.4.1.16.60.120 a dit en gros que 217 etoit trop loin de s'en meler" (line 10, = r2) and "Il a dit que 2[1|2]7
  vouloit absolument faire la paix dans le nord" (line 14, a corrected group, 217 or 227). runs.tsv has only r2. So the token count is
  at least 90-91, not 89.
- 0395 r3 tok1 reads 17 on the image (the same "J"-form 7 as in 107 on the line above), so "pinde" stands as written; Minde[n] needs
  the changed token (I), as the solver says. 0485 r3 51.15.33.28 and r5 202 (missed by both passes) are on the page as the solver gives.

**3. Prior-work checks 1-5.** `tools/prior_work.py sachsstaatsarchiv-manteuffel-1712 --item-spec 'shelfmark=SHStA Dresden 10026 Loc.
694/08;folio=frame <f>;date=<d>;sender=Manteuffel;recipient=Flemming' --step-type audit` for f = 0390/0391/0395/0485: exit 4 each; LEADs
= the FAM-MANTV claim (694/09 only, done), the MANT-08 claim (the solver under audit, done 20:22), this session's claim, and for 0485 the
generic frame-inventory gap line NOTES.md:1873 -- all recorded CLEAR (prior-work.tsv). UNCHECKED-NET aaymeloglu (no clone) and
4-editions (no prior_editions.tsv row) answered by hand:
1. Own work: grep of NOTES/AUDIT/mant0609/ROOM: only inventory lines before MANT-08. CLEAR.
2. Leaf and neighbours: no interlinear decipherment over any run on the four frames as re-read (the 0390 "touchant" and 0391 "bon gre
   malgre" interlinears are clear-text insertions, agreed). CLEAR.
3. Holder/portal/solver caches: offline as the solver; aaymeloglu UNCHECKED.
4. Editions -- Briefwisseling van Anthonie Heinsius Deel 14 (1 Sept 1712 - 30 Apr 1713, RGP GS 226; Deel 13 ends 31 Aug 1712), Huygens
   retroboeken `search_in_text`, source_id=14, plus OCR pages (16 requests, 2.2 s apart): 'Bolingbroke' 72 hits (London letters of
   L'Hermitage/Vrijbergen, Sept-Oct 1712); 'Koerland' 3 (index only: "Ferdinand (Kettler), hertog van Koerland, 79"; "Koerland,
   hertogdom, 79"); 'Curland', 'Courlande', 'Courland', 'Courlandt', 'Coerlandt', 'Koerlandt' 0; 'Ferdinand' 11 (index); 'Danemarc' 9;
   'Lintelo' 61 hits over three result pages: his printed Berlin letters run p.57 (Sept) then p.217 (12 Nov 1712) -- **no Lintelo letter
   of October 1712 is printed**, so the Dutch envoy at Berlin cannot carry 0390/0391/0395's news in this edition. Pages read in full: 42,
   43, 44, 50, 79.
   - **p.79, no. 142, Van Haersolte (Dutch envoy in Poland) to Heinsius, 1 Oct 1712 (H.A. 1697)**: "De heer Lölhöffel, resident van de
     coning van Pruyssen, is gisteren hier aengekomen met brieven van Sijne Majesteijt aen de croonschatsmeester om te faciliteren de
     cessie van het hartogdom Courlant aen gemelde coning, dog vertrouwe dat die saeck nog veel oppositie sal ontmoeten, dewijl de Polen
     sustineren dat na aflijvighijt van de tegenwoordige hertog sonder mannelijck oor dit hartogdom aen de republicq vervalt." Diff
     against C (0395): C says Berlin "is treating with [107] duke Ferdinand so that he cedes his rights to this court" and has offered
     him "the government of [p i n d e; Minden only by a changed token] and other great advantages". **Agree in substance** on the news
     the cipher spans carry (Prussia negotiating the cession of Courland's rights to the King, autumn 1712; Ferdinand is the duke whose
     death without male heir Van Haersolte's Poles invoke). Not in Van Haersolte: the approach to Ferdinand himself and the governorship
     offer. Date gap about two to three weeks (outside check 5's +-3 days), so this is printed background in substance, not a duplicate
     of the letter.
   - p.44, no. 83, L'Hermitage, London, 16 Sept 1712: ships recalled, "il n'est pas à croire qu'on persiste dans le dessein d'envoyer une
     escadre contre le roy de Danemarc" -- background to B's Bolingbroke declaration (detaching Denmark from its allies), not the same
     statement. No printed letter found with Oxford's "too far to meddle / defer to Hanover's sentiments" or Bolingbroke's declaration
     on detaching Denmark.
   - Droysen, *Geschichte der preußischen Politik* IV.1 (IA `droysen-geschichte-der-preussischen-politik-v-4-no-1`, djvu text, 3 IA
     requests, fetched once and grepped): positive control passes (Manteuffel quoted nn. 431, 485, 505, 510, 518-520); **no quotation
     from an Oct-Nov 1712 Manteuffel report**; no autumn-1712 Courland cession passage found by grep ('Curland' 7 hits, all earlier
     projects; 'Ferdinand' 0 -- the Fraktur OCR is poor, so a negative here is weak). n. 511 has Stanislas wishing Courland as
     compensation (Arnold's report, 6 Sept 1712) -- background only.
   - Google Books API (key, country=US): first call answered 503 backendFailed; host stopped per the good-citizen rule. **The press of the
     day (Mercure historique, Europäische Fama, Oct-Nov 1712) is UNCHECKED by me**; the solver's three Google Books queries (0-11 noise)
     stand. Acta Borussica BO I by date: not re-run (earlier audits searched it for Manteuffel's reports).
5. After decode: the solver's `--reading --network` run (ia-global/gbooks noise) stands; the other-correspondent route is item 4 above.

**4. Depth (rule 4a, the 8 Oct depth bar, PREREG-V-MANT08.md).** Cipher clause: the longest all-C stretch on any item is under 12 letters
against an AD of about 127-138 letters for this key (FAM-MANTV's computation; every r|re|ro and o|ou|ous choice is a liberty): **fails on
all four**. Code clause, tested on the real clear-text context read from the image (depth_stats windows splice across clear-text islands
on this shape of leaf, FAM-MANTV's flag), needing >= 2 non-verbatim sentences, a coarse class check and consistency with a letter-spelled
run of the same item:
| item | H/C/S % (tool counts) | recurring code | clause | ruling |
|---|---|---|---|---|
| A 0390 | 80.0 (C 16 of 20; but 45/46 are letter-valued codes standing for persons, so 60% read in sense) | 257 roi de Prusse x2 ("46 etant encore fort bien avec 257, il ne seroit pas de la prudence de l'attaquer"; "parle touchant la treve non seulement a 257, qui se feroit un fort grand plaisir de pouvoir l'effectuer") | 2 sentences, class OK, but no letter-spelled run on the item names a Prussian minister or the king: condition 3 fails | **D1** |
| B 0391 | 46.7 (C 14 of 30) | 217 la reine d'Angleterre x2 seen clearly (lines 8, 10; line 14 doubtful) | "217 s'est explique par ses ministres au sujet des affaires du nord" and "[Oxford] a dit en gros que 217 etoit trop loin de s'en meler": two non-verbatim sentences, person class, and both ministers named are spelled letter by letter on the same leaf under the same table (Oxford, Bullinbroug) -- **met** | **D2** |
| C 0395 | 66.7 | none | -- | **D1** ("duc Ferdinand" reads) |
| D 0485 | 57.1 | none (187, 202 singletons) | -- | **D1** (Breton, la Courl[ande]) |
D2 sentence for B (mine, from the reading and the clear text on the image): "In his postscript of 13 October 1712 Manteuffel reports,
from the contents of a packet for Fabrice that Heusch confided to him, that Oxford had said the Queen of England was too far off to meddle in pacifying the North and
would defer to Hanover's views on its execution, while Bolingbroke declared far more violently that she wanted peace in the North
absolutely and that, to get it, the King of Denmark would be detached from his allies whether he liked it or not." (Heusch and Fabrice
are named in clear at the head of the P.S.; their offices are not identified here.) D3 is out on every item (< 80%
read in sense, no non-statistical external check that the key reads these runs beyond the clear-text fit). depth_pct for status.json:
A 80.0 (60.0 in sense), B 46.7, C 66.7, D 57.1.

**5. Classification (rule 10).** Key on every item: **published** (Dr. Krauske's 1893 manuscript table, Loc. 694/10, someone else's
non-period key, credited). Prior decipherment: none located for any item.
- **A 0390: N3** -- no prior plaintext located (Heinsius XIV has no Berlin letter of October 1712; Droysen IV.1 quotes no Oct 1712
  report). Read is thin ("la treve" and codes for the King of Prussia, Manteuffel, two persons). Confidence medium; press unchecked.
  Safe: "Krauske's 1893 table reads 'la treve' and the code for the King of Prussia in Manteuffel's letter of 10 Oct 1712 (Loc. 694/08);
  no prior plaintext located in the Heinsius correspondence or Droysen." Unsafe: "Manteuffel's report on the truce deciphered."
- **B 0391: N3** -- the Oxford/Bolingbroke statements on the northern peace and Denmark were not located in Heinsius XIV (72
  Bolingbroke hits scanned, London letters read at p.44) or Droysen IV.1; background (British pressure on Denmark, Sept 1712) is printed.
  Confidence medium (the English and Hanoverian editions of 1712 northern policy -- Bolingbroke's Letters and Correspondence, Klopp's
  *Fall des Hauses Stuart* XIV, Macpherson's *Original Papers* -- were not searched; a second audit should). Safe: "Applying Krauske's
  1893 table to the cipher names in Manteuffel's postscript of 13 Oct 1712 (Loc. 694/08) gives Oxford, Bolingbroke and the queen of
  England in a report of their differing declarations on the northern peace; no prior plaintext located in the searched editions
  (Heinsius XIV, Droysen IV.1)." Unsafe: "A previously unread report on Bolingbroke has been deciphered."
- **C 0395: N2** -- the news its cipher spans carry (Berlin negotiating the cession of Courland's rights, autumn 1712) is printed in Van
  Haersolte to Heinsius, 1 Oct 1712 (Briefwisseling XIV no. 142, p.79); no prior mapping of this ciphertext to it found; the approach to
  Duke Ferdinand and the governorship offer are not in that letter (the class would rise to N3 only if a later auditor judges those
  details the substance). Safe: "Krauske's table reads 'duc Ferdinand' in a mid-October 1712 letter of Manteuffel's (Loc. 694/08) on
  Prussia's attempt to obtain Courland, news printed in Van Haersolte's letter to Heinsius of 1 Oct 1712." Unsafe: "Unknown Prussian
  designs on Courland revealed."
- **D 0485: N3** -- Breton and "la Courl[ande]" spans; no prior plaintext located (Heinsius XIV Lintelo 12 Nov 1712, p.217, read by the
  solver: Meurs, not this). Confidence medium-low (four runs unsettled). Safe: "Krauske's table reads the British envoy Breton's name
  and 'la Courl[ande]' in Manteuffel's letter of about 12 Nov 1712; no prior plaintext located in the searched editions." Unsafe:
  "Manteuffel's November report deciphered."
- Queued: SECOND-OPINIONS-QUEUE row SO-MANT-0839 (A, B, D; C excluded as N2); WORK-QUEUE row AUD2-MANT0391 for account 3 (B only, the
  only N3+ D2+ item). status.json not edited here (the lane orchestrator copies class, key `published`, depth and depth_pct).

**6. Postmortem and corrections.** Failure caught: the solver's transcription missed two occurrences of 217 on 0391 and read two
y-glyph 9s as 34 and 4 (the folder's own convention), which made "Bullinbroug" look like it needed a repair; the solver's check 4 read
Lintelo's hits only to the first page and did not try the duchy's Dutch spellings, which is where the Courland news sat (Van Haersolte,
Poland, not Berlin). Over-claim found: none outward (the solver wrote "no novelty class" and "not located in what was searched"); the
NOTES.md line "Bullinbrou[g] ... if tok5 34 (p) is 39 (i) (pass A read 39; one token I)" is now corrected in AUDIT only, the
transcription fix is the next reader's (NOTES Remaining gaps). Requests this audit: www.archiv.sachsen.de 4, resources.huygens.knaw.nl
16, archive.org 3, www.googleapis.com 1 (503); no 403/429/challenge.

## AUDIT 2 (AUD2-MANT08B)

Verifier AUD2-MANT08B (account 3, LANE VERIFY-3, session_0149CRvE4mU8kMqzvRD6UAXC), 8 Oct 2026, 21:43-22:0x UTC by `date -u`.
Brief: .claude/briefs/runs/2026-10-08-acct3-verify3-jobs.md "AUD2-MANT08B". Account 3 never read nor first-audited these items
(reader MANT-08 and first auditor V-MANT08 are account 2). Items: **A 0390** (letter of 10 Oct 1712), **C 0395** (mid-Oct 1712),
**D 0485** (about 12 Nov 1712), as defined in "AUDIT (V-MANT08)" above. Frame 0391 (B) is AUD2-MANT0391's, not audited here.
Nothing decoded; key.tsv, ciphertext.tsv and the readings untouched. Duplicate diff: the three entries' pointers (URL files
0390/0395/0485), dates and addressee differ from every other filed item of this target (status.json results for 694/08 f.410,
f.468, 0501, 694/09 0015-16 etc.); no duplicate.

**1. Re-derivation (rule 7).** `python3 tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712/f0390_08 --check`: tokens 89,
C 54, M 35, "reading up to date", exit 0; main folder `--check` exit 0. The four transcription fixes V-MANT08 item 2 lists are still
not applied to f0390_08/ciphertext.tsv at origin/main (21:5x UTC); for my items only 0390 r9 tok3 (4 -> 9) is affected, and it changes
no class. **Per-unit gate (CLAUDE.md rule 3, per-unit paragraph), from f0390_08/gate.out:** the pooled gate (83 letters, 0/1000)
passes, but the units do not clear it each on their own: **0390 307/1000** (18 letters, not gated, i.e. its own letters do not
separate Krauske's table from shuffled keys at all), **0485 16/1000 = FAIL** at the registered 10/1000 line, 0395 0/1000 (17 letters,
not gated). So A and D rest on the pooled gate, which is carried by 0391 and 0395, plus the sense of the runs in their clear context.
The first audit did not say this; it lowers confidence on A and D (below), not their depth class, because D1 rests on words read in
context, not on the per-unit statistic.

**2. Transcription.** Not re-checked on the image (V-MANT08 compared 79 tokens on the native frames, including every 0485 run and
0395 r1-r3; no request to www.archiv.sachsen.de this session).

**3. Prior-work checks 3-5** (`tools/prior_work.py sachsstaatsarchiv-manteuffel-1712 --item-spec 'shelfmark=SHStA Dresden 10026 Loc.
694/08;folio=frame <f>;date=<d>;sender=Manteuffel;recipient=Flemming' --step-type second-audit --fetch`, then `--reading <decoded
sentences> --network`; f/d = 0390/1712-10-10, 0395/1712-10-15, 0485/1712-11-12):
- First run, exit 4 each: LEADs = target-level ROOM claims of FAM-MANTV (694/09 only), MANT-08 (solver), V-MANT08 (first audit) and
  AUD2-MANT0391 (0391 only) -- recorded CLEAR in prior-work.tsv. UNCHECKED tomokiyo/solver-by-unit (no folio key); UNCHECKED-NET
  aaymeloglu and 4-editions, answered by hand:
- Check 3, solver repositories: github.com/aaymeloglu/unsolved-ciphers shallow clone (scratch) grepped for Manteuffel / Krauske /
  694/08 / Flemming / Courland: one row only, catalogue/decode-catalog.csv DECODE 4999 = "Key of Jakob Heinrich von Flemming and Count
  Manteuffel, 1717, HStAD 10026 Loc. 03233/02" -- a different (1717) key and unit, no reading. CLEAR. sources/cyphersolver: the prior
  runs' CLEAR stands.
- Check 4, editions by date (fetched once, grepped; positive control = each volume returns its own dated letters for 1712):
  - **Bolingbroke, Letters and Correspondence (ed. Parke, 1798)**, IA `letterscorrespon02boliuoft` (vol. 2, to about Sept 1712) and
    `letterscorrespo03boli` (vol. 3, Sept 1712-1713; dated letters of 17 Oct, 11 Nov, 29 Nov 1712 present). Breton: vol. 2 letters to
    him of May 1712 (his appointment to Berlin); vol. 3 only "To Mr. Breton, Whitehall, March 6th, 1712-13" (his leaving Berlin) --
    nothing of Nov 1712, nothing on Courland ('Courl'/'Curl' 0 relevant hits), nothing on a northern truce spoken of to the King of
    Prussia. Not located.
  - **Klopp, Der Fall des Hauses Stuart XIV** (IA `derfalldehauses07klopgoog`, Google Fraktur OCR, poor): Breton found once (p. 330,
    "dem britischen Gesandten Breton in Berlin", St John on Ober-Geldern, June 1712: not these frames); 'Kurland'/'Curland',
    'Manteuffel', 'Flemming' 0 under fuzzy grep. Weak negative (OCR).
  - **Macpherson, Original Papers II** (IA `originalpapersco02macp`): 'Courland' once (1650, Colepeper), 'Breton', 'Manteuffel',
    'Flemming' 0; no Oct-Nov 1712 letter on these matters. Not located.
  - **Briefwisseling Heinsius XIV** (Huygens retroboeken `search_in_text`, source_id=14): 'Courlant' 1 hit = p.79 (page index 88) --
    **I read it and confirm V-MANT08's quotation** of Van Haersolte, 1 Oct 1712 (no. 142): Lölhöffel, Prussian resident, arrived "met
    brieven van Sijne Majesteijt aen de croonschatsmeester om te faciliteren de cessie van het hartogdom Courlant aen gemelde coning".
    'Lölhöffel' 1 (same page); 'Courland' 0; 'Breton' 2 = index only, p.761 "Breton, William, Engels envoyé te Berlijn, (XIII)" --
    he appears in Deel XIII only, so Deel XIV prints nothing of his for Sept 1712-Apr 1713.
  - Courland histories: *Geschichte des Herzogthums Kurland und Semgallen* (1789, IA `10691426bsb`, after Ziegenhorn) on 1712-13:
    Ferdinand's quarrel with the Ritterschaft, the March 1712 conference, his deferred investiture (1712-13) -- no Prussian approach to
    him for a cession nor an offered governorship; the Prussian plan it prints is the 1718-19 Brandenburg-Schwedt one. *Obzor
    vneshnikh snoshenii Rossii* III (1897, IA `libgen_00713967`), "Kurlyandskoe gertsogstvo 1712": Ferdinand's complaints to the Tsar
    and Golovkin (May-July 1712) -- not this. Schmauss, *Einleitung zu der Staats-Wissenschafft* II (1747, IA `10725536bsb`): the
    Courland passages are 1659 and 1718-19. Not located.
  - Droysen IV.1 and Acta Borussica: V-MANT08's and earlier audits' greps stand (not re-run). Sbornik RIO: IA full-text query
    (Russian) returned only the Obzor and unrelated items; the RIO volumes themselves were not identified or read: **UNCHECKED**.
  - **The press of the day (Mercure historique et politique, Europäische Fama, Oct-Nov 1712): UNREACHABLE this session** -- Google
    Books API answered HTTP 429 (daily quota spent) on the first two calls, host stopped; IA advancedsearch finds no 1712 Mercure
    historique volume by title and the Europäische Fama items carry only the series date (1702), not searched. Unchecked by both audits.
- Check 5 (G3), `--reading --network`: 0390 phrases -> ia-global LEAD 'au roi de Prusse il' = unrelated items (a Mozart CD etc.),
  recorded CLEAR as noise; 0395 'traiter avec le duc Ferdinand' ia-global no hits, CLEAR; 0485 'a Breton le passage de' ia-global 1
  item = a book on Alain Resnais, recorded CLEAR as noise; gbooks UNCHECKED-NET on all three (429). IA full text by hand: '"Hertzog
  Ferdinand" Curland 1712', '"duc Ferdinand" Courlande Prusse 1712', 'Breton Courlande Berlin 1712 Manteuffel' (0), '"Mr. Breton"
  Berlin Courland 1712' (0): background only (above). Recipient-side and staff papers (Flemming's own papers, Saxon cabinet orders of
  Oct-Nov 1712) are unprinted as far as these searches reach; the sender's same-week letters to other recipients: none printed found.

**4. Depth (rule 4a, depth bar 8 Oct 2026; keep or lower only).** A **D1 kept**, C **D1 kept**, D **D1 kept**. Cipher clause fails on
all three (longest C stretch < 12 letters vs AD about 127-138 letters). Code clause: C and D have no recurring code. On A, code 257
(le roi de Prusse) reads sensibly in two sentences of the same letter; V-MANT08 refused the clause on a third condition of its own
pre-registration (a letter-spelled run on the item naming the king or a minister) that the 8 Oct depth bar does not contain. Under
the bar's wording the clause may be met; but this job may not raise depth and I did not write a D2 sentence, so A stays D1. Noted for
the lane (not a change). depth_pct unchanged (A 80.0, 60 in sense; C 66.7; D 57.1).

**5. Classification (rule 10).** Key: **published** (Dr. Krauske's 1893 manuscript table, Loc. 694/10, credited) on all three. No prior
decipherment located for any item.
- **A 0390: N3 held.** No prior plaintext located in Bolingbroke (Parke) II-III, Klopp XIV (weak OCR), Macpherson II, Heinsius XIV,
  Droysen IV.1 (first audit), Schmauss 1747. Confidence **low-medium** (lowered from medium): the frame's own letters do not clear the
  shuffled-key control (307/1000), the readable content is 'la treve' plus nomenclator codes, and the press is unchecked. Safe sentence
  (V-MANT08's, extended): "Krauske's 1893 table reads 'la treve' and the code for the King of Prussia in Manteuffel's letter of 10 Oct
  1712 (Loc. 694/08); no prior plaintext located in the Heinsius correspondence, Droysen, Bolingbroke's Letters and Correspondence,
  Klopp or Macpherson." Unsafe: "Manteuffel's report on the truce deciphered."
- **C 0395: N2 held; N1 tested and rejected.** N1 would need this letter's plaintext (or a decipherment of it) in print; none was
  found -- what is printed is the *news* in another man's letter (Van Haersolte to Heinsius, 1 Oct 1712, Briefwisseling XIV no. 142,
  p.79, read and confirmed above). N2 basis checked: Van Haersolte prints Prussia's approach to the Polish crown treasurer for the
  cession of Courland and does not name Ferdinand as a party; the item's cipher spans carry the duke's name (the reigning duke whose
  heirless death Van Haersolte's Poles invoke) and the place of the offered governorship ('pinde', unsettled). The direct approach to
  Ferdinand and the governorship offer were not located in Heinsius XIV, the 1789 Courland history, the 1897 Obzor, Schmauss or Droysen;
  a later auditor could argue N3 on those details, but this audit keeps or lowers and holds N2 on V-MANT08's basis and the FAM-MANTV
  precedent (news of the cipher spans printed in another correspondent's letter). Confidence medium. Safe sentence (V-MANT08's) stands.
- **D 0485: N3 held.** Breton is absent from Heinsius XIV (index: Deel XIII only) and from Bolingbroke III except a letter of 6 Mar
  1712-13; nothing on Courland in Nov 1712 in Bolingbroke, Klopp, Macpherson. Confidence **low** (lowered from medium-low): the frame's
  own gate FAILs (16/1000 vs 10/1000), four runs are unsettled, 'Breton' and 'la Courl[ande]' are identifications from sense
  (each with an r|re|ro or o|ou choice), and the press is unchecked. Safe sentence (V-MANT08's, extended): "Krauske's table reads the
  British envoy Breton's name and 'la Courl[ande]' in Manteuffel's letter of about 12 Nov 1712 (Loc. 694/08); no prior plaintext
  located in the searched editions (Heinsius XIV, Bolingbroke's Letters and Correspondence, Klopp, Macpherson); the frame's own
  shuffled-key gate fails, so the reading rests on the pooled gate." Unsafe: "Manteuffel's November report deciphered."
- SECOND-OPINIONS-QUEUE SO-MANT-0839 (A, B, D): no class or count changed for A or D; row and prompt left as filed (its question 1
  already asks for Bolingbroke, Klopp and Macpherson independently).

**6. Postmortem.** Two things the first audit missed: (a) the per-unit gate -- A's own frame ties its shuffled-key control and D's
fails it, so both readings stand only on the pooled gate (CLAUDE.md rule 3, per-unit paragraph); status.json depth_check for A and D now
says so; (b) the brief's named families (Bolingbroke/Parke, Klopp XIV, Macpherson) were unsearched; searched now, nothing found. No
over-claiming sentence found in NOTES.md or status.json lines (all use "fragments read" and "no prior plaintext located"). Still owed:
the press of Oct-Nov 1712 (Google Books, once its quota resets) and Sbornik RIO; the four V-MANT08 transcription fixes. Requests this
session: archive.org 14 (metadata/djvu/advancedsearch), be-api.us.archive.org 9, resources.huygens.knaw.nl 8, github.com 1 (clone),
www.googleapis.com 2 (429, stopped) plus prior_work.py's own --network calls; no 403 or challenge.

## AUDIT 2 (AUD2-MANT0391)

MANT-FIX applied 8 Oct 2026 (NOTES.md "MANT-FIX (8 Oct 2026)"): the four missing name codes (217 line 19, 266 line 20, 227 line 23, 257 line 27) are in f0390_08/ciphertext.tsv with the V-MANT08 fixes; `--check` exit 0, pooled gate PASS 0/1000 unchanged; classes and depth unchanged.

Verifier AUD2-MANT0391 (account 3, LANE VERIFY-3, session_017eR38q5E5bjn5bSwJrFGFg), 8 Oct 2026, 21:42-22:1x UTC by `date -u`.
Brief: .claude/briefs/runs/2026-10-08-acct3-verify3-jobs.md "AUD2-MANT0391". Account 3 never read nor first-audited this item (reader
MANT-08 and first auditor V-MANT08 are account 2). Item: **B 0391**, SHStA Dresden 10026 Loc. 694/08 URL file 0391 = f.313, P.S.
"Berl. ce 13 Oct. 1712", Manteuffel to Flemming. Nothing decoded; key.tsv, ciphertext.tsv and the readings untouched. Duplicate diff:
pointer, date and addressee differ from every other filed item of this target; no duplicate. Frames 0390/0395/0485 are AUD2-MANT08B's.

**1. Re-derivation and gate.** `decode_key.py f0390_08 --check` exit 0 (89 tokens C 54 M 35) as AUD2-MANT08B ran it at origin/main;
V-MANT08's fixes are still not applied. Per-unit gate (gate.out): **frame_0391 clears on its own letters**, 28 letters, real -1.298 vs
1000 shuffled keys p99 -1.487, 0/1000 -- unlike 0390 (307/1000) and 0485 (16/1000), so B does not lean on the pooled gate.

**2. Image check (native frame 0391, 1 request to www.archiv.sachsen.de, HTTP 200 image/jpeg 4339x3865; my own crops and 3x zooms of the
right page, no subagent).** V-MANT08's corrections:
- **r4 tok5 = 39, confirmed**: the glyph is the folder's y-form 9 with a long descender, unlike the closed 4s of "44" just before it.
  "Bullinbroug" reads as written.
- **r5 tok1 = 160 by shape, confirmed** (tall-bowled 6 in second place, "1b0"); 100 (d, "detacheroit") by sense: **M**, as V-MANT08 says.
- **Line 14 "Il a dit que 2?7 vouloit absolument faire la paix dans le nord"**: the middle digit is overwritten; 217 or 227 cannot be
  settled at native resolution. Agreed: doubtful.
- **217 omissions: V-MANT08 under-counted.** Beyond line 8 ("217 s'est expliqué par ses ministres au sujet des affaires du nord") and
  line 14, the leaf carries **four more name codes absent from ciphertext.tsv and runs.tsv**, all clearly written with a full stop:
  lines 18-19 "Heusch m'assure que l'El. son maitre a taché de detourner **217.** des sentiments du dernier"; line 20 "en luy declarant a son
  tour, que **266.** contribueroit de tout son coeur a faciliter la paix en question, lorsqu'elle devoit etre generale"; line 23 "mais
  qu'il ne se meleroit jamais de persuader **227.** d'en faire une particuliere"; line 27 (item 2 of the P.S.) "Le meme ajouta ... qu'il
  savoit bien que **257.** se meloit aussi de vouloir moyenner une paix". So 0391 carries 217 x4 (one more doubtful), 266 x2, 227 x2,
  257 x1: at least 35-36 code tokens, not 30. Key values (key.tsv): 217 la reine d'Angleterre C, 257 le roi de Prusse C, 266
  Hannover|Electeur de Hanovre M, 227 le roi de Danemark|Danemark M. For the next reader to add (with the earlier fixes), then re-run
  `--check` and shuffle_gate_0390.py; not applied here.
- Identification (new, from print): **Heusch is the Hanoverian resident at Berlin** -- "der hannoversche Resident Heusch in Berlin"
  (Publikationen aus den Preussischen Staatsarchiven 87, IA `publikationenaus87prusuoft`, be-api snippet), "his minister Heusch at
  Berlin" (J. F. Chance, *George I and the Northern War*, 1909, IA `georgeinorthernw0000jame`, snippet); "l'El. son maitre" on the leaf
  agrees. Fabrice is not identified here. This answers part of SO-MANT-0839 question 2.

**3. Prior-work checks 3-5.** `tools/prior_work.py sachsstaatsarchiv-manteuffel-1712 --item-spec 'shelfmark=SHStA Dresden 10026 Loc.
694/08;folio=frame 0391;date=1712-10-13;sender=Manteuffel;recipient=Flemming' --step-type second-audit --fetch`: exit 4; LEADs = the
FAM-MANTV/MANT-08/V-MANT08 claims (recorded CLEAR by V-MANT08) and my own claim line (this session: CLEAR); UNCHECKED tomokiyo and
solver-by-unit (no folio key); UNCHECKED-NET aaymeloglu, 4-editions. Then `--reading <decoded sentences> --clone <aaymeloglu clone>`
(offline): G3 ia-global and gbooks UNCHECKED-NET, answered by hand below. By hand:
- Check 3: github.com/aaymeloglu/unsolved-ciphers shallow clone grepped (Manteuffel / 694/08): one row, DECODE 4999, the 1717
  Flemming-Manteuffel key (Loc. 03233/02) -- another key and unit. CLEAR.
- Check 4, editions by date (djvu text fetched once from IA and grepped; positive control = each volume's own dated 1712 letters found):
  - **Bolingbroke, Letters and Correspondence (Parke 1798)** II (`letterscorrespon02boliuoft`) and III (`letterscorrespo03boli`; dated
    letters Whitehall 19, 26 Sept, Windsor 30 Sept, Whitehall 14 Oct, 19-28 Nov 1712 present): 'Denmark'/'Danish' 3 + 2 hits in all --
    II p.115 (the King of Denmark's offer, Jan 1712), II Hanover memorial (the Queen's steps with Denmark over Bremen), III p.70 (to
    Pulteney, 9 Sept 1712, on the King of Denmark's mistress); nothing on detaching Denmark from its allies, nothing to or about Hanover
    on a northern peace in Sept-Nov 1712. **Not located.**
  - **Klopp, Der Fall des Hauses Stuart XIV** (`derfalldehauses07klopgoog`, Fraktur OCR, poor): **pp. 421-422 print the related
    background**: Thomas Harley in Hanover (Aug-Sept 1712) was told to ask the Elector to join the Queen in restoring peace in the North;
    the Elector answered that he would count it an honour to support the Queen's intentions and join his efforts to hers for peace,
    "vorausgesetzt dass dieser Friede allgemein sei, und dass alle bei dem nordischen Kriege betheiligten Parteien in gleicher Weise seine
    guten Dienste annähmen" (from Grote's instruction, Robethon papers), and Harley left at the end of September with a written
    declaration that the Elector could not separate himself from Emperor, Empire and allies. This is the same Hanoverian position the
    P.S.'s clear text reports via Heusch (266 to help the peace "lorsqu'elle devoit etre generale", never to press 227 into a separate
    one), but on another occasion and not from Heusch's report. Oxford's "trop loin de s'en meler" and Bolingbroke's declaration on
    detaching Denmark: no match under fuzzy grep ('nemar' 10 hits, none 1712 London declarations). **Not located; weak (OCR).**
  - **Macpherson, Original Papers II** (`originalpapersco02macp`; first fetch HTTP 500, one retry 200): Hanover papers of 1712 jump
    from May to Dec; 'Denmark'/'Danes'/'Bremen' in 1712 pages: none on this. **Not located.**
  - **Sbornik RIO 61** (`sbornik33unkngoog`, vol. 61, 1888): Whitworth's Berlin letters to Bolingbroke nos. 64-67 (16/27 Sept, 20/31 Oct,
    25 Oct/5 Nov, 11/22 Nov 1712; read in full for Sept-Oct): the Tsar's movements, the Rügen project, Flemming's letter on Saxon
    confusion, "Mr Breton ... will give you an account of the affairs of this court"; **nothing on the Queen's or Hanover's northern
    declarations. Not located.**
  - **Chance 1909** (lending item; be-api snippets only): Bolingbroke "harped always in his despatches upon the theme that no action
    [in the north]..." (background: British non-intervention while the French peace was pending); 'detach' 3 hits, all on Prussia/the
    Tsar 1714-15. Not located (snippets only, pages not read).
  - **Hinrichs, Friedrich Wilhelm I.** (1941, IA `bwb_C0-BHF-356`, snippets): cites Heusch 12, 15, 20 Oct 1712 and Manteuffel to
    Flemming 4 and 23 Oct 1712 (via Acta Borussica BO I) on court matters (Kameke); no 13 Oct 1712 citation, no Oxford/Fabrice hit.
    Hinrichs, *Preussen als historisches Problem* (`preussenalshisto0000carl`): Heusch/Manteuffel 1713-14 only. Not located.
  - **Acta Borussica BO I**: AUDIT2-MANT's heading list (Google Books search-inside, 3 Oct 2026) has Manteuffel reports of 19 Sept, 4,
    7 and 23 Oct 1712 at pp. 256-258 and no 13 Oct one. My own search-inside queries (Bolingbroke 0, Oxford 0, Heusch 2 at front-matter
    pages, Danemarck 0) are **void**: the positive control 'Manteuffel' also returned 0 this session, so the endpoint is not answering.
    Droysen IV.1 and Heinsius XIV: V-MANT08's and AUD2-MANT08B's reads stand (Heinsius XIV has no Berlin letter of October 1712).
  - **The press of the day (Mercure historique, Europäische Fama, Lamberty) and Google Books generally: UNREACHABLE.** The Books API
    answered HTTP 429 to all 7 of my calls (I sent the batch of 7 at 2 s intervals before reading the first status -- six calls past the
    good-citizen limit, my error; host left alone after that); IA advancedsearch has no 1712 Mercure historique or Lamberty volume by
    title, and the Fama items carry only the 1702 series date. Unchecked by all three audits.
- Check 5 (G3) by hand, IA be-api global full text: '"trop loin de s'en meler"' 0; '"faire la paix dans le nord"' 2 (unrelated:
  anthropology 2005, Le Rhin dans l'histoire); '"bon gre malgre" Danemarc alliez' 132 (loose AND; top hits Charles V, Bender, Mercure
  françois -- unrelated); '"Heusch" Manteuffel' (Hinrichs, above); '"moyenner une paix" Prusse 1712' 44 (loose; Rákóczi, Polish
  partitions -- unrelated); '"Heusch" "Fabrice"', '"resident Heusch"', '"Heusch" Bolingbroke': only the identification above.
  Recipient-side (Flemming's papers) and the sender's same-week letters to other recipients: none printed found; the Hanoverian side
  (Heusch's own report of the same news to Hanover) is not printed in Klopp XIV or Macpherson II as far as grep reaches.

**4. Depth (rule 4a, 8 Oct depth bar; keep or lower).** **D2 kept.** Cipher clause fails (longest C stretch < 12 letters vs AD about
127-138). Code clause met more strongly than the first audit found: 217 reads in at least three clear-context, non-verbatim sentences
(lines 8, 10, 19), 266 in two (lines 12, 20), 227 in two (lines 16, 23), with Oxford and Bullinbroug letter-spelled on the same leaf.
The P.S. now makes sense end to end, and the Hanoverian half agrees in substance with the position Klopp XIV prints (a consistency
check, not proof the key reads these runs). D3 is out: H/C/S 46.7% by tool count (14 of 30); with the omitted name codes added it would
rise, but the in-sense share of cipher tokens stays under 80% and there is no independent check of the letter-valued runs. depth_pct
46.7 kept until the next reader's re-run. My D2 sentence (true on the image; line 14's doubtful code left out): "In his postscript of
13 October 1712 Manteuffel passes on what the Hanoverian resident Heusch had told him: Oxford had said the Queen of England was too far
off to meddle in pacifying the North and would defer to Hanover on its execution, Bolingbroke's declaration had been far more violent
(Denmark to be detached from its allies by the spring), and the Elector had tried to turn the Queen from Bolingbroke's view, saying
Hanover would gladly help a general peace but would never press Denmark into a separate one; Heusch added that the King of Prussia was
also trying to mediate a peace."

**5. Classification (rule 10).** Key: **published** (Dr. Krauske's 1893 manuscript table, Loc. 694/10, credited). Prior decipherment:
none located. **B 0391: N3 held**, confidence medium. Oxford's and Bolingbroke's declarations as reported here were not located in
Bolingbroke's Letters and Correspondence II-III, Klopp XIV, Macpherson II, Sbornik RIO 61 (Whitworth at Berlin), Heinsius XIV, Droysen
IV.1, Hinrichs 1941 (snippets) or IA full text; Hanover's matching position is printed in substance (Klopp XIV pp. 421-422, on another
occasion), which keeps the Hanoverian half from counting as unlocated. Not N4: Google Books and the press of the day were unreachable,
and Klopp/Chance were read by grep or snippet only. Safe: "Applying Krauske's 1893 table to the cipher names in Manteuffel's postscript
of 13 Oct 1712 (Loc. 694/08) gives Oxford, Bolingbroke and the queen of England in a report, passed on by the Hanoverian resident Heusch,
of their differing declarations on the northern peace; no prior plaintext located in the searched editions (Bolingbroke's Letters and
Correspondence, Klopp XIV, Macpherson II, Sbornik RIO 61, Heinsius XIV, Droysen IV.1); Hanover's own stance (a general peace only) is
printed in Klopp XIV pp. 421-422." Unsafe: "A previously unread report on Bolingbroke has been deciphered"; "the Queen's northern policy
of October 1712 revealed".

**6. Postmortem and corrections.** Failure caught: both MANT-08 and the first audit missed name codes on 0391 (the first audit found
two of the omissions, not the four in the P.S.'s second half); the first audit left Heusch unidentified, and that one identification
changes how the P.S. reads (a Hanoverian report, so the Hanoverian half has a printed parallel). Over-claim found: none outward;
status.json results[220] `line` named only Heinsius XIV and Droysen IV.1 as searched -- extended, audit_status set to "two audits",
depth_sentence replaced with the sentence above (the old one put line 14's doubtful code as "she"). SO-MANT-0839: class unchanged, row
not edited. Requests this audit: www.archiv.sachsen.de 1; archive.org (metadata, advancedsearch, download) 15; be-api.us.archive.org 27;
www.googleapis.com 7 (all 429); books.google.com 6 (200, answers void); github.com 1 clone. One 500 (archive.org, retried once).

## AUDIT (V-MANTR8)

Verifier V-MANTR8 (account 2, LANE FAMILY), 8 Oct 2026, 23:03-23:2x UTC by `date -u`; a separate session from the solver MANT-R8
(session_01Ch5SyJKu1jEKbwHfjBFxyT) and from every earlier verifier. Brief: .claude/briefs/runs/2026-10-08-ytbiz-family-2209-jobs.md
"### V-MANTR8". Claim under audit: NOTES.md section MANT-R8 (f0375_08/): seven unglossed frames (694/08 0375, 0214, 0436, 0241, 0435,
0065; 694/09 0070), 99 tokens C 67 M 30 U 2, PREREG-MANTR8 pooled shuffled-key gate PASS 7/1000 (limit 10), read in context "ma guerison"
(0214), Kraut (0436), Arnold / Eosand (0375). Nothing decoded beyond the re-derivation; key.tsv, ciphertexts and readings untouched.

**1. Re-derivation (rule 7).** `python3 tools/decode_key.py ciphers/sachsstaatsarchiv-manteuffel-1712/f0375_08 --check`: "tokens 99: C 67,
M 30, U 2 / reading up to date", exit 0. **Eye check against the crops: not done.** The solver's crops and frames lived in its own
scratch (NOTES MANT-R8: "images in scratch only, folder over 30 MB"); nothing for these seven frames is on disk, and this brief allowed
disk only. The transcription is therefore unchecked by any second eye beyond the solver's two Sonnet passes. Re-fetch route: the frame
URLs in images/loc694-08-09/frames.tsv with the region arguments pasted in NOTES MANT-R8.

**2. Gate robustness (rule 3; `f0375_08/vmantr8_seeds.py` -> `vmantr8_seeds.out`, same scorer and shuffle design as the registered
script).** Pooled string (89 letters), 1000 shuffles each, ten fresh seeds: 5, 8, 13, 10, 10, 10, 7, 11, 12, 6 per 1000 -- **4 of 10
seeds exceed the registered limit of 10**; 10,000 shuffles (seed 99): 98/10,000 = 9.8 per 1000, i.e. p ~ 0.01, on the line. Leave one
frame out (seed 11): without 0375 20/1000, **without 0214 39/1000**, without 0436 13, 0241 16, 0435 16, 0065 21, 0070 10; without 0214
and 0065 together 70/1000. So the registered PASS (7/1000) is a seed-lucky draw at p ~ 0.01, and it is carried by 0214 ("lamaguerison",
12 letters, 4/1000 on its own) with 0065 behind it: **the pooled gate does not license the other five frames as a group.** It is not a
negative either; most of the string is abbreviated names, which the 4-gram model cannot reward. The control can differ from the target
on this statistic (the shuffled key changes the letters scored), so the test is a real test, just a weak one.

**3. Known-plaintext check found in print (supersedes the gate for 0436).** Acta Borussica, *Behördenorganisation* I (Berlin 1894, ed.
G. Schmoller and **O. Krauske**), Google Books full view `ESf8fHFG9ngC`, search-inside JSON (34 requests, 1.8 s apart, all 200): Nr. 72,
headed p. 256 "Manteuffel an den Feldmarschall Grafen Flemming. Berlin 19. September, 4., 7. und 23. October 1712. Urschriften. Zerbst
... bezw. Dresden. Hauptstaatsarchiv. Vol. CXLV. Loc. 694", prints on **p. 258**: "[Krautt est] toujours malade ou, pour mieux dire,
mélancolique, et il y a apparence que ses affaires ne sont pas tout-à-fait nettes. **Blaspil dit hautement qu'il a volé le Roi, et que
Kameke qui le soutient, s'attirera un jour de mauvaises affaires** en prenant son parti. **Les raisons qui portent Kameke à cela, sont 1.
qu'il croit Krautt habile homme** et nécessaire au Roi, **2. que Krautt lui a prêté de l'argent dans le temps que Kameke était encore in
statu exa[mi]nationis, et 3., à ce que je devine, que Krautt fait peut-être** rouler quelque somme d'argent au profit de Kameke." This is
frame 0436 paragraph 4 sentence for sentence (runs.tsv contexts r1-r8). Diff, code by code:
| run | cipher | MANT-R8 read | print | agree |
|---|---|---|---|---|
| r1 | 11.60.66.6.28 | Kraut | Krautt | yes (k r a u t; print doubles t) |
| r2 | 55.12 | "b\|a l, unsettled" | Blaspil | yes as an abbreviation (b l) |
| r3, r4, r7 | 11 | "K", sense: Kraut | **Kameke** | letter yes (k); **identification wrong** |
| r5, r6, r8 | 11.60 | "Kr" = Kraut | Krautt | yes |
So on 0436 the key values 11 k, 60 r, 66 a, 6 u, 28 t, 55 b, 12 l are confirmed against Krauske's own 1894 print (C-grade agreement, 7
codes, 14 tokens), and the solver's sense identification of lone 11 is corrected: **11 = K[ameke], not K[raut]** (three occurrences in
print; r13 "voyage avec 11" is beyond the printed extract, M). The print is the editor's (Krauske's) decipherment of this very leaf:
the paragraph's plaintext and its decipherment were in print in 1894. The print has none of r9-r13 (150, 160, 230, 11).
Other printed pages read through the same endpoint: p. 257 (4 Oct 1712, "Le pauvre Krautt est fort malade de chagrin"); p. 212 (12 Sept
1712, Blaspil and Krautt reconciled). Queries with no hit in vol. I: Eosander, Eosandre, Suède/Suede, czar, ressemble, guérison, achever,
tombasse, créance, regarde, promener, Fürstenberg, Langvillette, mélancolique (OCR hyphenates "mélan- colique"), Arnold Stanislas.
"Arnold" hits only Arnold Westenberg (Lingen); "Stettin" 16 hits not read (0241's Stettin is a hypothesis only).

**4. Prior-work checks 1-5.** `tools/prior_work.py sachsstaatsarchiv-manteuffel-1712 --item-spec 'shelfmark=SHStA Dresden 10026 Loc. 694/08;
folio=frame <f>;sender=Manteuffel;recipient=Flemming;date=<d>' --step-type audit --fetch` for 0375 (1712-09-15), 0214 (1712-07-15), 0436
(1712-10-23): exit 4 each; LEADs = five target-level claims on other units (MANT-08, V-MANT08, AUD2-MANT0391, AUD2-MANT08B, MANT-0609X),
recorded CLEAR (prior-work.tsv); generic UNCHECKED rows answered here:
1. Own work: these frames appear only in inventory lines before MANT-R8. CLEAR.
2. Leaf: not re-read on the image (item 1). Solver: no gloss at sheet scale. UNCHECKED by me.
3. Holder, portal, solver caches: offline caches name no folio of this unit; aaymeloglu/unsolved-ciphers not cloned: UNCHECKED-NET.
4. Editions: **Acta Borussica BO I** (item 3: 0436 printed; 0375, 0214, 0241, 0435, 0065 not found by the queries listed). **Droysen,
   *Geschichte der preußischen Politik* IV.1** (IA `droysen-geschichte-der-preussischen-politik-v-4-no-1`, djvu text, 3 requests: one
   404 on a guessed filename, metadata, djvu): p. 267 and Anmerkungen 511-512: "Arnolds Schlußbericht über seine Sendung ist d. d. Berlin,
   6. September 1712" (Arnold, Bürgermeister from Neisse, sent to Stanislas, Instruction 8 July 1712) and "Instruction für den Brigadier
   Eosander d. d. 16. August 1712" (his mission to Charles XII at Bender; text after Anm. 513: "Man hoffte auf die Erfolge Eosanders in Bender"; later
   "sein erster Bericht war am 17. November eingetroffen"). This fits 0375 exactly as **"Arnold à St[anislas], et Eosand[er] au roi de Suède"**:
   51.28 = s t is the abbreviation St., not the solver's "a s|sa t" (I, from sense; every token keyed). No quotation of a Manteuffel report
   of Sept 1712, and no "guérison" or Kraut/Blaspil passage of 1712 (Fraktur OCR, a weak negative). **Heinsius Briefwisseling** (Huygens
   retroboeken `search_in_text`, all volumes, 6 requests, 2.2 s apart, my own terms): Eosander -- Deel XIV p. 364 ("L'on attend à tout moment
   Mons. Eosander de Bender") and p. 451 (Eosander at Vienna), background to 0375 later in the winter; Blaspil 2 and Kraut 3 hits, none in
   Deel XIII-XIV text; Kameke index only in XIII-XIV; Arnold, Stanislaus: no 1712 Arnold mission hit on the first page. Nothing prints
   0214's or 0375's cipher spans.
5. After decode: the cipher spans of 0375, 0214 and 0436 were phrase-checked as above; 0241, 0435, 0065, 0070 have nothing read to check.

**5. Depth (rule 4a under .claude/briefs/runs/2026-10-08-acct3-depth-bar.md).** Cipher clause: the longest all-keyed letter stretch on any
frame is 10-12 letters ("ma guerison"), against an AD of about 127-138 letters for this key (FAM-MANTV): fails everywhere. Code clause:
no multi-letter code value recurs in two independent sensible contexts as read by the solver; on 0436 the recurring value 11 was read in
sense wrongly, and its right reading (Kameke) is supplied by the print, which may confirm a D2 sentence but never supply it. Rulings:
0436 **D1**, 0375 **D1**, 0214 **D1**, 0435 **D1** (code 153 reads in "Je n'ai pas écrit à 153 que le frippon"), 0241 **D0**, 0065 **D0**,
0070 **D0** (abbreviated names; nothing reads). depth_pct (tool counts, C of tokens): 0375 77.8, 0214 64.3, 0436 71.4, 0241 78.6,
0435 10.0, 0065 83.3, 0070 75.0 -- percentages of letter-valued tokens keyed, not of sense read.

**6. Classification (rule 10).** Key on every item: **published** (Dr. Krauske's 1893 manuscript table, Loc. 694/10, credited).
- **0436 (Loc. 694/08 ff.343v-344, Manteuffel to Flemming, Oct 1712, paragraph 4): N0.** The plaintext and its decipherment are printed
  by Krauske himself in Acta Borussica BO I (1894) p. 258, as an extract of the reports of 7 or 23 Oct 1712 from "Dresden ... Vol. CXLV.
  Loc. 694" (the leaf sits beside the P.S. of 23 Oct on f.343, so 23 Oct is likely, I). text: known. Safe: "Frame 0436's cipher names
  (Krautt, Blaspil, Kameke) were deciphered and printed by O. Krauske in Acta Borussica, Behördenorganisation I (1894) p. 258; applying his
  1893 table to the leaf reproduces the letters of those names." Unsafe: "Kraut's illness and the charge of theft read from cipher";
  any wording that the reading is ours or unprinted.
- **0375 (ff.299v-300, Sept 1712): N2.** The news the cipher spans carry -- Arnold sent to Stanislas, Eosander to the King of Sweden -- is
  printed in Droysen IV.1 (text about p. 267-269, Anm. 511-512); no prior mapping of this ciphertext found. Safe: "Krauske's table reads the names
  Arnold and Eosand[er] beside 'St.' and the code for the King of Sweden in a September 1712 letter of Manteuffel's (Loc. 694/08), matching
  the two Prussian missions of summer 1712 printed in Droysen IV.1." Unsafe: "Manteuffel's report on the Bender mission deciphered."
- **0214 (f.165, Jul 1712): N3, confidence low.** "on n'attend que ma guérison pour achever l'ouvrage" (10 keyed tokens, one M); not found in
  Acta Borussica BO I (guérison, achever, tombasse: 0), Heinsius, or Droysen. The search covers only these three editions; Manteuffel's
  own illness in summer 1712 was not searched in Saxon scholarship. Safe: "Krauske's 1893 table reads 'ma guérison' in a cipher run of
  Manteuffel's letter of July 1712 (Loc. 694/08 frame 0214), beside his clear-text mention of having fallen ill; no prior plaintext located
  in Acta Borussica BO I, Droysen IV.1 or the Heinsius correspondence." Unsafe: "a previously unread passage on Manteuffel's illness".
- **0241, 0435, 0065, 694/09 0070: no class.** Nothing reads beyond single codes and unsettled names; there is no plaintext to classify.
- Second opinions: SO-MANT-0214 queued for 0214 (the only N3); none for 0436 (N0) or 0375 (N2). status.json: three result rows added.

**7. Postmortem and corrections.** (a) The solver's sense identification "11.60 'Kr' and lone 11 'K' ... abbreviations of the same name"
is wrong: lone 11 is Kameke (print, three places). (b) 55.12 is Blaspil, not "unsettled". (c) 0375's "a s|sa t" is "à St[anislas]" (I).
(d) "the pooled gate PASSes" overstates a p ~ 0.01 result that 4 of 10 fresh seeds fail and that collapses without 0214; only 0214 and,
weakly, 0065 stand on the gate. (e) The solver's check 4 ran Heinsius only; Acta Borussica BO I, the edition Krauske made from these
very reports and already named in this AUDIT.md (VERIFY-MANT, AUDIT2-MANT), was not searched for the seven frames, and it prints 0436.
Lesson for the next reader of this pool: **search Acta Borussica BO I (Google Books ESf8fHFG9ngC search-inside) by a distinctive clear word
of each frame before reading it**; its Nr. 64, 72, 82-83, 91-93 extracts cover June 1712-April 1713. Corrections are written in NOTES.md
"V-MANTR8"; the solver's own section is left as written. Requests this audit: books.google.com 34, resources.huygens.knaw.nl 6,
archive.org 3 (one 404); no 403/429/challenge.

9 Oct 2026 (MANT-EYE, LANE FAMILY-A2d account 2): eye check on crops done (NOTES "MANT-EYE"). 0214: every token matches ciphertext.tsv (blind Sonnet pass + eye), 110.297 stays U. 0375 r3 token 3 read 51 (low; was 57): Eosand run 35.16.51.66.14.100, letter s C -> s|sa M, first-alternative string unchanged; --check exit 0; pooled gate rerun with the same seeds 7/1000 -> 5/1000, PASS unchanged; frame 0375 223 -> 219/1000. N-classes and depth above not re-assessed by this worker.

## AUDIT 2 (AUD2-MANTR8)

Verifier AUD2-MANTR8 (account 3, LANE-VERIFY-4, session_018nvXsMuGuSPqhPgZGoWDnr), 8 Oct 2026, 23:39-23:5x UTC by `date -u`. Second
adversarial audit of frames 0214 and 0375 only. Account 3 never read or first-audited either frame (reader MANT-R8 and first auditor
V-MANTR8 are account 2). Brief: .claude/briefs/runs/2026-10-08-acct3-verify4-jobs.md "## AUD2-MANTR8". Nothing decoded; key.tsv,
decode files and readings untouched. V-MANTR8's Acta Borussica BO I, Droysen IV.1 and Heinsius searches were not repeated.

**1. Eye check (V-MANTR8 could not run one).** The two frames were fetched once each from the holder (archiv.sachsen.de frames.tsv URLs,
2 requests, 200, image/jpeg) into scratch only (not committed). The runs were cut with MANT-R8's pasted regions (f0214a 2140,1600,1240,420;
f0375a 880,1420,1260,300; f0375b 880,2290,1260,150) and read by eye:
- 0214 r3: the page reads "L'on me mande qu'on n'attend que 31.66.7.6.35.60.y.51.16.21. pour achever l'ouvra[ge]": every group agrees with
  ciphertext.tsv, the seventh group being the y-shaped 9 that MANT-R8 settled on. The neighbour inventory's "60.4.51" (NOTES, 694/08
  neighbours) misreads that glyph. Clear context above: "Certaine personne que V.E. devinera s'il lui plaît, et 160 avoient entrepris,
  avant que je tombasse malade, de mettre Mons: 110.297 d'icy sur le bon pied, et la chose étoit en très bon train." (110.297: the middle
  digit looks like 9 at this scale, so U stays.)
- 0375 r1-r4: "... qu'elle nous avoit donné des projets, qu'elle avoit envoyé 66.60.21.33.12.120. a 51.28., et 35.16.5?.66.14.100. au 187
  l'un et l'autre avec des instructions par écrit qui marquoient clairement les vues de cette cour contre 177." **51.28 is confirmed on
  the image**, written as one group with a stop after it and then a comma. The third group of the Eosand run is 51 or 57 (both s in
  key.tsv, so the letter is the same either way). 187 looks like 187 at this crop and stays low. r6 "a l'egard de 35" agrees.
**St[anislas] against the key table:** key.tsv gives 51 s|sa (M, note "sa") and 28 t (C), so 51.28 reads "st" or "sat"; "St." as an
abbreviation is consistent with the table. Expanding it to Stanislas is an identification (I), not something the key gives. Stettin is
a second expansion the key cannot exclude: Stanislas was with the Swedish forces in Pomerania in 1712, and the same digraph 51.28 sits
inside 0241's "...35.51.28..." (MANT-R8's hypothesis "Ste[ttin]"). The 0375 safe sentence should therefore keep "St." unexpanded, as
V-MANTR8's sentence already does.

**2. Prior-work checks 3-5.** `tools/prior_work.py sachsstaatsarchiv-manteuffel-1712 --item-spec 'shelfmark=SHStA Dresden 10026 Loc. 694/08;
folio=frame <f>;sender=Manteuffel;recipient=Flemming;date=<d>' --step-type second-audit --fetch` for 0214 (1712-07-15) and 0375 (1712-09-15):
exit 4 each. The only LEAD is this audit's own ROOM claim (48214b); the other rows are V-MANTR8's CLEARs. Generic rows: 3-tomokiyo
UNCHECKED (no folio key), 3-solver UNCHECKED-NET (aaymeloglu not cloned), 4-editions UNCHECKED-NET (no prior_editions.tsv row);
answered by hand below.
- G3 phrase search, Internet Archive full text (be-api fts, all items, 1.7 s apart): "attend que ma guérison", "que ma guérison pour
  achever", "ma guérison pour achever" 0 each. The 0214 clear-context phrase "avant que je tombasse malade" got 5 hits, all other texts
  (Destouches, Leprince de Beaumont): not this letter. 0375: "Arnold à Stanislas", "Eosander au roi de Suède" and the clear-context phrase
  "marquoient clairement les vues de cette cour" 0 each; "envoyé Arnold" 8 hits, none relevant. Positive-control note: "toujours malade
  ou, pour mieux dire" (Acta Borussica BO I p. 258, printed) also scores 0 on IA, so BO I is not in IA full text and IA's 0 tells us nothing
  about BO I (which V-MANTR8 covered through Google Books).
- **Hinrichs, *Friedrich Wilhelm I.*** (IA bwb_C0-BHF-356, lending-only; fts inside the item, 13 queries; snippets only, no page read).
  This is the scholarship most dependent on Manteuffel's reports for 1712-13. It cites them by date, mostly as "a. a. O. S." pages of
  Acta Borussica (31 May, 7 and 18 June, 29 June / 23 Oct, 12 Dec 1712; Jan-Feb 1713). It cites the Eosander mission from Prussian
  records ("Bericht Eosanders: 27. September 1712. Reskript an denselben, 13. September 1712", GStA Rep. XI 247) and says Eosander reached
  Bender on 19 September. No hit for Arnold, Neiße, Bürgermeister, "Manteuffel September 1712", Genesung (1712), "Manteuffel krank" (1712);
  "Manteuffel Juli 1712" matched nothing usable. Weak negative (snippets).
- **Waddington, *Histoire de Prusse* II (1922)** (IA histoiredeprusse02wadd djvu, full text grep): p. 212 "Le colonel Eosander fut expédié à
  Bender au mois d'août, en vue de solliciter l'approbation de Charles XII", and p. 212 n. 1 (Jablonski, 20 Dec 1712). Arnold is not
  named; there is no Manteuffel quotation for Jul-Sept 1712 (his only 1712 quotation is the "pot-pourri de vices" portrait). A second
  print of the 0375 news, beside Droysen.
- Manteuffel's own illness, summer 1712: IA fts "Manteuffels Krankheit" 0; "Manteuffel erkrankte" 8 hits, none in 1712 (Droysen IV.3
  Breslau, later; Neues Archiv f. sächs. Gesch. 5/21 Grodno-Warsaw, a later mission; 19th-20th-century namesakes); "Manteuffel malade
  1712 Flemming" turned up no relevant snippet (Vehse, Waddington, Maurice de Saxe works). OpenAlex (keyed, 5 searches): Rous 2016,
  "Der Weinkeller als Schlachtfeld" (Société des antisobres: Manteuffel/Flemming/Grumbkow), the only relevant hit; its PDF answered
  brill.com 403, **unreachable**. Stuber 2024 is about Urbich, not relevant (OAPEN 403/429 in any case). Haake, Ziekursch, Flemming
  biographies and Sbornik RIO: **not searched by title** this session; only the IA-wide fts above would have caught their texts.
- Press of Jul and Sept 1712 (Europäische Fama, Mercure historique): **not searched** (no full-text route tried in the box).
- Google Books: **unreachable**. 10 keyed calls with country=US returned 429 at 23:41 (the shared key's quota was apparently spent by
  parallel sessions), plus one retry after about 9 minutes, also 429; nothing further sent. So no Google Books coverage beyond
  V-MANTR8's earlier BO I search-inside.
- N1 test for 0375 (could Manteuffel's report itself be quoted?): neither the cipher-span phrases nor the clear-context phrase hit in IA.
  Hinrichs and Waddington, the two narrative works that use Manteuffel's 1712 reports, document the Eosander mission from Prussian
  sources, not from this letter. Not established.

**3. Classification (rule 10; key published, Krauske 1893 table, credited).**
- **0375 (Loc. 694/08 ff.299v-300, Sept 1712): N2 held.** The news (Arnold sent to St[anislas] or St[ettin], Eosander to the King of
  Sweden with written instructions against the czar) is in print: Droysen IV.1 Anm. 511-512 (V-MANTR8), and for Eosander also Waddington
  II p. 212 and Hinrichs. No prior mapping of this ciphertext and no quotation of this report found, so no N1. Confidence: medium.
  Gaps: Google Books 429; the press not searched. Safe sentence: V-MANTR8's, unchanged. Unsafe: "Arnold's mission to Stanislas
  read from cipher" (the expansion is I).
- **0214 (f.165, Jul 1712): N3 held, confidence low.** "ma guérison" is confirmed on the image (10 tokens, C 7 M 3; the M rows 60, 51 and 16 are each
  used in their first or second listed value). No prior plaintext was found in IA full text (cipher and clear phrases), Hinrichs (snippets),
  Waddington (full text), OpenAlex, or V-MANTR8's three editions. It holds at low confidence, not higher, because Google Books was
  unreachable, Rous 2016 was unreachable, and the Saxon biographies and the 1712 press were not searched. Safe sentence: V-MANTR8's,
  unchanged. Unsafe: "a previously unread passage on Manteuffel's illness", or any first/new wording.
- **Count correction (rule 4):** V-MANTR8's "10 keyed tokens, one M" for 0214 r3 (item 6 and status.json `grade`) is three M: 60 r|re|ro,
  51 s|sa, 16 o|ou|ous are M rows in key.tsv (reading_tokens.tsv: C 7, M 3). The reading needs each M row's first or second listed
  value, so the class is not affected; status.json corrected. SO-MANT-0214's prompt states no token count, so no edit.
- **Depth:** both D1 kept (keep-or-lower). The cipher clause fails (10-16 letters vs AD about 127-138), and no code value reads in two
  sensible contexts (51.28 recurs in 0241 only inside an unread run).
- SO-MANT-0214 (queued 8 Oct) still matches: class and counts unchanged, no edit. 0375 is N2, so no SO row.

**4. Registers.** VERIFY-BACKLOG flagged "REGISTERS DISAGREE". **PROGRESS.tsv is the wrong one.** Its own header says one row per
leaf/letter, but it carries a single row for this folder ("Manteuffel f.410", audit 2 = AUDIT2-MANT on f.410), and
tools/verify_backlog.py matches by folder, so that row looked as if it covered 0214 and 0375. status.json was right: "one audit" for
both until this section. Fix: two PROGRESS.tsv rows added (frames 0214 and 0375, stages 1 and 2 done), and status.json audit_status
"two audits" for both result rows with this section added to audit_refs.

**5. Postmortem.** No over-claim found in V-MANTR8's sentences. Two notes for the next reader: (a) the neighbour-inventory reading
"60.4.51" for 0214 (NOTES, MANT-0609X) is the y-shaped 9; ciphertext.tsv is right. (b) "St[anislas]" in V-MANTR8 item 4 and
NOTES V-MANTR8 is an identification that Stettin rivals; it should be written "St." with the expansion graded I. Requests this audit:
www.archiv.sachsen.de 2; be-api.us.archive.org fts 29; archive.org 7 (metadata 5, djvu 2, one 404 on a guessed name); api.openalex.org 8;
googleapis.com 11 (all 429); library.oapen.org 1 + 3 browser (403/403/429); brill.com 1 (403). Stopped at each block, no loops beyond
one retry.

9 Oct 2026 (MANT-EYE, LANE FAMILY-A2d account 2): eye check on crops done (NOTES "MANT-EYE"). 0214: every token matches ciphertext.tsv (blind Sonnet pass + eye), 110.297 stays U. 0375 r3 token 3 read 51 (low; was 57): Eosand run 35.16.51.66.14.100, letter s C -> s|sa M, first-alternative string unchanged; --check exit 0; pooled gate rerun with the same seeds 7/1000 -> 5/1000, PASS unchanged; frame 0375 223 -> 219/1000. N-classes and depth above not re-assessed by this worker.

## AUDIT (V-MANT0136)

Verifier V-MANT0136 (account 2, LANE FAMILY-A2f), 9 Oct 2026, 05:17-05:4x UTC by `date -u`; a separate session from the solvers MANT-0136
(identity look 01:08 and reading 04:17) and MANT-R07 (session_01E2qn7rVxaef1e54UV2oTGb) and from every earlier verifier. Brief:
.claude/briefs/runs/2026-10-09-ytbiz-family-0409-jobs.md "### V-MANT0136". Claim under audit (NOTES "MANT-0136 (9 Oct 2026, 04:17...)"
and "MANT-R07"): Loc. 694/09 file 0136 (p.102, P.S. in a clerk hand, "le chiffre que nous appellons celuy du procès"), 75 code tokens in
11 runs read with Krauske's table; gates (a) and (b) PASS; grades C 21 S 33 M 20 U 1 (A1); reads "faire obtenir a 170 la Livonie", "le czar
n'avoit plus la Po[r]te a craindr[e] ... [c]omme bien d'autr[es]". Nothing decoded here; key.tsv, ciphertexts and readings untouched.

**1. Item.** SHStA Dresden 10026 Loc. 694/09, URL file 0136 (film 0137), Manteuffel to Flemming, Berlin; date not on the crops read --
April 1713 by the neighbours (0135 a copy of a letter of 1 Apr 1713, 0137 Hamburg Apr 1713; I). Clear context carries most of the
sense: "que 257 pourroit contribuer a faire obtenir a 170 [la Livonie] pour luy & pour ses descendens"; "avec 150 contre tous ceux qui
pourroint vouloir faire les dictateurs dans le Nord". Cipher spans that read: r04 "la Livonie" (unglossed, S), r06 "n'avoit pl[us]"
(unglossed, S) running into r07-r08 "la Po[r]te a craindr[e] [le c]omme bien d'autr[es]" (period interlinear gloss under it, C/M).
Prior-work tool (`--step-type audit --fetch`): exit 4, the one LEAD being this audit's own claim (recorded CLEAR); 4-editions recorded
KNOWN-PART (below); 3-solver aaymeloglu/unsolved-ciphers not cloned: UNCHECKED-NET.

**2. Re-derivation (rule 7), every --check from the repository root:** `tools/decode_key.py .../f0136_09 --check` "tokens 75: C 56, M 18,
U 1 / reading up to date" exit 0; `f0136_09/gloss_gate.py --gloss gloss_{A,B,A1A,A1B}.tsv --check` (run from f0136_09/, as the script
expects) four times "up to date"; `judge_gate.py --check` "up to date"; `grade_0136.py --check` and `--a1 --check` "up to date". All exit 0.
(gloss_gate.py resolves --gloss relative to f0136_09/; judge_gate.py and grade_0136.py must run from the root -- a usage note, not a defect.)

**3. Design audit (rule 3).**
- *PREREG order.* PREREG-MANT-0136-A1 is verifiable: 978bf33fc (05:01:52 UTC, PREREG-A1 + crops_a1 + prior-work rows, no gate output)
  precedes bbbe276ca (05:04:43, passes, gate_A1A/B.out, grades_A1). **PREREG-MANT-0136 is NOT verifiable from git**: the commits the
  solver names (d339fbe20 "before scoring", 6215d7a60 final) are not objects in origin/main; every f0136_09 file, PREREG, passes, gate
  outputs and grades alike, first appears in c53d82cb9 (04:56:00, titled "ROOM: check-in ...", a `room.py --push` rebase fold). The
  order rests on the solver's ROOM done line (04:35) and NOTES only -- CLAUDE.md rule 6's known flag (the fold erases per-commit order).
  Not evidence of a breach; the gate (a)/(b) numbers re-derive exactly, and the A1 gate, whose order is provable, reproduces (a).
- *Gate (a), known answer.* The gloss is a period decipherment of this leaf; key.tsv (Krauske 1893) was not edited from it, so agreement
  is a real test of the table against an independent period reading. The control (key values permuted over codes) can differ on S.
  PASS in all four blind passes (A 9/13, B 8/13 vs p99 4; A1A 22/32, A1B 21/32 vs p99 8). Sound. Known caveats carried: the DP shifts one
  slot where a code has no gloss (r07 20/170); grade_0136.py grades every token in a span as glossed (r07 6 51 79 34 -> M, conservative).
- *Gate (b), unglossed tokens.* The permuted-letter-value control changes the letters scored, so it CAN differ from the target (not a
  coverage-type non-test). Power control 0085 r9+r10 at N=40 letters, below the target's 62: power shown at a smaller N than the target,
  so adequate (rule 3 last paragraph). Real -1.401 vs p95 -1.759, 0/1000: PASS. The judge's own real_p05 (-1.028) is not met -- the gate is
  the permuted control, as registered.
- *Gate (b) after A1 (not re-run by MANT-R07; audit sensitivity, `f0136_09/vmant0136_sens.py` -> `vmant0136_sens.out`, same scorer, key,
  seed 136, 1000 draws, not a registered gate):* unglossed set after the A1 spans, 41 letters: -1.416 vs p95 -1.696, 1/1000 -> PASS (holds).
  Runs that read (r04, r06), 19 letters: non-test (< 20). **Runs that do not read (r01, r02, r09), 20 letters: -1.984 vs p95 -1.601,
  441/1000 -> FAIL** -- indistinguishable from a permuted key.
- *What the S grade means.* S is the PREREG's mechanical grade for every unglossed letter token once (a) and (b) pass; it is not a
  per-token certification. Of the 33 S tokens under grades_A1.tsv, **16 (48%) sit in stretches that read** (r04 97-10 "la livonie", 8;
  r06 21-44 "n'avoit pl", 8); **17 do not** (r01 6, r02 2, r09 8 -- the three runs whose own permuted control fails at 441/1000 -- and 170
  in r04, whose value 'le' gives no sense where a person is wanted). Read the S count as "16 S supported, 17 S by aggregation only".

**4. Novelty search log (rule 10; prior-work checks 3-5, G3).**
- Own work: only MANT-0609Y, the identity look, MANT-0136 and MANT-R07 touch 0136. CLEAR.
- Leaf: the r07-r08 run carries a **period interlinear decipherment** (both blind gloss passes in both jobs): the plaintext of those 33
  tokens was written on the leaf in 1713. KNOWN (N0) for those spans.
- **Acta Borussica, Behördenorganisation I** (1894, ed. Schmoller and Krauske; Google Books full view ESf8fHFG9ngC, search-inside JSON,
  20 requests 2.5 s apart): positive control Manteuffel 20 hits (pp. 177-396, incl. reports of 26 Feb, 4 and 11 Mar 1713), Chiffre 4,
  Nachschrift 4; target terms Livonie, Liefland, descendans, descendens, dictateurs, dictateur, Czaar, czar, Moscovie, Russie, Pologne,
  gardes 0; craindre 1 (p. 320, another passage), Porte 5 (none the Ottoman Porte), procès 1 (p. 304, a lawsuit). 0136 is not printed
  there: the volume quotes Manteuffel on court and administration, not on the North. (An earlier batch of the same queries returned 0 for
  the control too -- a transient; the rerun with the control at both ends is the one logged.)
- **Droysen, Geschichte der preußischen Politik IV.1** (IA djvu): ends with Friedrich I's death (Feb 1713); Manteuffel quoted to 19 Feb
  1713 (Anm. 519-520). Not 0136.
- **Droysen IV.2** (IA `droysen-geschichte-der-preussischen-politik-v-4-no-2`, djvu, 2 requests): quotes Manteuffel 9 Apr 1713 (p. 25 n. 2,
  the departments), 18 Apr (p. 37 n. 1, Hanover and the troops), 16 and 20 May; none is 0136. **p. 43 and nn. 1-2 print the substance of
  0136's r04-r07 context**: the czar in Berlin 8-12 March 1713 pressing Friedrich Wilhelm I into the northern alliance, a Russian project
  answered by Dohna to Golovkin on 1 April 1713, the czar holding Livonia ("Er hatte Liefland inne") and not returning it to Poland, Charles
  XII in conflict with the Porte, and Flemming to Manteuffel 10 March offering Prussia part of Pomerania. Two rare entities (czar,
  Livonia) with Prussia and Poland within days of the letter: SUBSTANCE under check 5. Diff: Droysen does not print 0136's sentence
  (Prussia helping the czar to Livonia "pour luy & pour ses descendens"; the czar "n'avoit plus la Porte a craindre"); the news context is
  printed, the wording is not.
- Press of the day (Mercure historique et politique, Europäische Fama, Apr 1713): **unchecked** -- IA advancedsearch found no 1713
  Mercure item by title; Google Books API answered 429 twice (host stopped). IA full-text (be-api) phrase search: "dictateurs dans le
  Nord" 0, "pour ses descendens" 0, "celuy du proces" 15 (all a 16th-century divorce suit, unrelated; serves as a control that the
  endpoint answers).
- Not searched: Saxon scholarship on the 1713 Prussian-Russian talks (Haake, NASG beyond VERIFY-MANT's grep), Sbornik RIO (Golovkin's
  side), JSTOR (no row queued: below N3, nothing goes outward), aaymeloglu/unsolved-ciphers.

**5. Classification.** Key: **published** (Dr. O. Krauske's 1893 manuscript table, Loc. 694/10, credited), corroborated on this leaf by
the period gloss (period). Item (0136, its cipher spans): **N2**, with the glossed run r07-r08 **N0** (decipherment on the leaf, 1713).
text: partly known (the glossed run). The unglossed fragments that read ("la Livonie", "n'avoit pl[us]") carry news printed in Droysen
IV.2 p. 43; no prior mapping of this ciphertext located. Confidence medium (press of the day unchecked).
**Depth (rule 4a, depth bar 2026-10-08):** cipher clause -- longest contiguous H/C/S stretch r04 (9 tokens, 11 letters) or r08 9-27 (8
tokens) against AD ~127-138 letters (FAM-MANTV): fails. Code clause -- 257, 150, 177 occur once each here; 170 ('le') occurs twice and reads
in neither context: fails. **D1** ("fragments read"). depth_pct 72.0 (C 21 + S 33 of 75 tokens; percentage keyed, not sense read --
16 of the 33 S read in sense).
Safe sentence: "Krauske's 1893 table applied to a P.S. of Manteuffel's (Loc. 694/09 file 0136, about April 1713) reads 'la Livonie' and
'le czar n'avoit plus la Porte a craindre' in cipher; part of that run already carries a period interlinear decipherment, and the news
(the czar holding Livonia, Russia courting Prussia in March-April 1713) is printed in Droysen IV.2 p. 43."
Unsafe: "a previously unread passage on Prussian support for the czar's claim to Livonia"; "51 tokens deciphered (S)"; any wording that
the cipher named "celuy du procès" was identified by us as a separate system.
No SECOND-OPINIONS-QUEUE row and no AUD2 WORK-QUEUE row: N2 / D1 is below the brief's N3+ and D2+ trigger.

**6. Postmortem and corrections.** (a) MANT-0136's check 4 left Acta Borussica BO I and Droysen IV.2 unsearched (Google Books 429; IV.1 ends
before April 1713) although V-MANTR8's lesson names BO I as the first search for this pool; done here. (b) The S count 51 (MANT-0136) / 33
(A1) overstates what reads: 17 of the 33 are carried by the aggregate gate only, and their own runs fail the same control. (c) The
PREREG-MANT-0136 order cannot be shown from git; the A1 order can. (d) MANT-0136's "the gloss reads 'comme bien d'autres'" -- the blind
gloss letters are 'o n m e h i e n d a u t r e s' (A1A/A1B); 'comme bien' is the solver's sense, 31=n and 55=h are rule-4 slots (MANT-R07).
Requests this audit: books.google.com 39 (search-inside, 2-2.5 s apart; no error), www.googleapis.com 2 (429, stopped), archive.org 7
(advancedsearch 3, metadata 2, djvu 2), be-api.us.archive.org 3. No 403 or challenge.

## AUDIT (V-MANT0454)

Verifier V-MANT0454 (account 2, LANE FAMILY-A2g), 9 Oct 2026, 07:23-07:4x UTC by `date -u`; a separate session from the solver MANT-0454
(05:18-05:28 UTC) and from every earlier verifier; I had not read 0454 before this job. Brief: .claude/briefs/runs/2026-10-09-ytbiz-family-0709-jobs.md
"### V-MANT0454". Claim under audit (NOTES "MANT-0454"): "694/08 0454 read under Krauske's table: 62 tokens S46 M16, gate (b) PASS at N=52 (real
-1.659 vs p95 -1.693); stretches 'rebelle', 'Rozrasewsky' x2, 'renonce a', '[a]rnold', 'abdiquer'". Nothing decoded here; key.tsv, ciphertext and
reading untouched.

**Depth bar copied before ruling** (.claude/briefs/runs/2026-10-08-acct3-depth-bar.md): CLAUDE.md 4a governs. Cipher clause = a contiguous H/C/S
stretch longer than AD (~1.5 x unicity, every liberty counted; an unfitted external key does not shrink H(K)). External check = a D3/D4 element,
never a substitute for the clause at D2. Code clause = a code value that reads sensibly in >= 2 independent contexts; an H/C grade on the value does
not satisfy it on its own; a verbatim repeated phrase counts once. D2 = one clause plus the verifier's own true, specific sentence about the content,
written from the reading (an edition may confirm it, never supply it). Otherwise D1.

**0. Step 0 (the solver's owed lookup).** "sachsen take" 07:23, 2 GETs (URL files 0452, 0453; HTTP 200 image/jpeg, 4346x3860 and 4339x3865),
"sachsen release" 07:25. Reduced copies and manifest (full-size sha256) in f0454_08/neighbours/ (folder already over 30 MB, full size not committed).
The film card on URL file 0452 reads "Aufnahme Einheit 0453" and on 0453 "0454" -- the folder's known one-frame URL/card offset; numbers here are URL
numbers. Read by eye at reduced size: **neither frame carries a date line, place, address or signature**; both are mid-letter (0452 right page stamp
f.359, 0453 right page f.360; 0454 is ff.360v-361). The letter therefore begins on or before f.358 (URL 0451 or earlier; 0449 is f.356). Its date is
**not on the leaves seen (unchecked)**; by position in the volume it lies between URL 0396 ("Copie d'une lettre de Copenh. du 9 Oct." enclosure after
the P.S. of 13 Oct 1712) and 0487 (enclosure "a la lettre de Mant. du 12 Nov 1712"), i.e. **mid-October to early November 1712 (I)**. Content of
0452-0453 in clear: the Elbing affair ("l'affaire d'Elb[ing]"), the next Diet, Kettler grand marshal of Hesse-Cassel and the Duke of Courland's
marriage to a prince of Hesse (0453 right, paras 2-3). **Code groups on 0453** (right page para 3, eye at reduced size, not zoomed, not decoded):
"Il m'a dit de [struck] meme, que 198 a ecrit depuis peu a 257, qu'il est toujours dispose a 60.35.21.33.14.15.10.26 ... convenir avec 170 des
conditions ...", then 257 and 170 again in the next lines. These are unread cipher on the same letter (next step below); one Sonnet call was not
needed because no date or code had to be settled for this audit.

**1. Item.** SHStA Dresden 10026 Geheimes Kabinett Loc. 694/08, URL file 0454 (card 0455), ff.360v-361, Manteuffel to Flemming, Berlin (place by the
series; I), mid-Oct to early Nov 1712 (I, above). Ciphertext f0454_08/ciphertext.tsv, 62 tokens in 18 groups, no gloss. Prior-work tool
(`--step-type audit --fetch`) exit 4: five LEADs, all other jobs' claims (V-MANT0136, MANT-INV08B, MANT-NAMES136, GB-PHRASE) or this audit's own --
recorded CLEAR; 3-solver aaymeloglu/unsolved-ciphers and 4-editions UNCHECKED-NET (not cloned; editions by hand below).

**2. Re-derivation (rule 7), from the repository root:** `tools/decode_key.py .../f0454_08 --check` "tokens 62: C 42, M 20 / reading up to date";
`f0454_08/judge_gate.py --check` "judge_gate.out up to date"; `f0454_08/grade_0454.py --check` "grades.tsv: up to date". All exit 0.
Key values checked against key.tsv for every letter code in the six runs (60 r|re|ro M, 35 e, 55 b|[a] M, 10 e, 44 l, 103 le|la M, 26 r, 33 o, 82 z,
66 a, 73 s|z M, 69 w, 51 s|sa M, 11 k, 92 y, 14 n, 16 o|ou|ous M, 21 n, 30 c M, 50 a, 27 r, 12 l, 120 d, 25 a, 100 d, 9 i, 24 q, 6 u; names 198
Stanislas, 150 le Roi de Pologne, 187 Roi de Suede, 257 Le roi de Prusse, all C in key.tsv): the six letter strings follow.

**3. Transcription spot check (three runs, my own eye on the committed crops, 2x):** L01 "...gociation avec 198. qu'il" / "comme un
60.35.55.10.44.103." -- agrees (the 55 is two separated 5s, as the passes say); L06 "66.27.21.33.12.120., sur quoi" -- agrees (66 with a gap between the
digits; 68 not excluded, as the solver's low flag says); L08 "presse de 25.55.100.9.24.6.10.60." -- agrees (fourth group the looped-descender 9).
3/3 agree. I also read the clear text of crops L02-L09 myself and confirm the solver's context words for every code group from r03 to r16 (L02 "qui est
icy de la part de 198, mais qu'en attendant il seroit bon de savoir ce que 150 voudroit accorder a 198, en cas qu'il 60.35.14.16.21.30.35.50. et que 187
y consentit. Il m'a pria en meme temps d'en ecrire a V.E. et de luy demander ses sentiments. Il a aussi voulu savoir, qui je voudrois que 257 envoyat a
198 en cas que 150 s'expliqua ... le plus seur de continuer d'y employer le Sr. 66.27.21.33.12.120., sur quoi il me dit que c'etoit aussi son sentiment,
mais que 198 avoit temoigne etre malcontent de luy parcequ'il l'avoit peut etre un peu trop presse de 25.55... Ce que je sai d'assure de tout cela c'est
que 60.33.82... a pris, il y a 3 jours, une audience, et a dit au Roi de Prusse tout ce que 198 doit avoir ecrit"). "au Roi de Prusse" is in clear there,
which fits 257 = le roi de Prusse two lines earlier.

**4. Design audit (rule 3).** PREREG-MANT-0454 is in ae6a8b18f, before the fetch (solver's statement; not re-verified commit by commit -- the
folder's room.py fold caveat, V-MANT0136 item 3, applies). Gate (a) n/a (no gloss; I saw none on the crops either). Gate (b): the permuted-letter-value
control changes the letters scored, so it can differ from the target (not a coverage non-test); power measured at the target's own L=52 (11/11, a small
power sample of 11 windows, as the solver says). Real -1.659 vs p95 -1.693, 29/1000: PASS above p95, not above p99 -- a thin margin. The S grade is the
PREREG's mechanical grade; unlike 0136, here **every** S-graded run reads in sense (rebelle, Rozrasewsky x2, renoncea, arnold, abdiquer) and the two
witnesses of the 11-code run agree 11/11 by letter -- the strongest internal evidence on this leaf is that repeat, not the 4-gram margin.
"renoncea": the clear context is "en cas qu'il ___ et que [le Roi de Suede] y consentit" (imperfect subjunctive wanted), so the letters 'renoncea' sit
as "renonçât" without the t (or a doubtful final token); the sense is right, the form is M.

**5. Novelty search log (rule 10; checks 4-5).**
- Own work: only MANT-INV08 (inventory) and MANT-0454 touch 0454. CLEAR.
- Leaf: no gloss, clear copy or decipherment heading on 0454 (both solver passes and my crop reading); 0452-0453 carry none either.
- **Droysen, Geschichte der preussischen Politik IV.1** (IA `droysen-geschichte-der-preussischen-politik-v-4-no-1`, djvu text, 2 requests): p. 267 and
  Anm. 511-512 print that in July 1712 Berlin sent a confidant to King Stanislaus with the Swedes ("nach Schweden"), that Stanislaus at once declared himself ready to
  abdicate and then added conditions; the agent is Arnold ("Instruction fur den Burgermeister Arnold ... 8. Juli 1712. Arnolds Schlussbericht uber seine
  Sendung ist d. d. Berlin, 6. September 1712", Stanislaus wishing Courland as compensation); Eosander then sent to Charles XII at Bender; later in the same chapter (Nov
  1712) Stanislaus leaving the Swedish headquarters for Bender to obtain Charles XII's consent to his abdication. **SUBSTANCE**: Arnold's mission to
  press Stanislas to abdicate and the abdication negotiation are printed. Not printed there: Rozrazewski, his audience, Stanislas's displeasure with Arnold,
  the 'rebelle' remark, or what Augustus might grant Stanislas. 'Rozra-' 0 hits in IV.1 and IV.2 (OCR-quality caveat: Fraktur; 'Manteuffel' appears
  in IV.1 OCR as 'Mantenfel').
- **Droysen IV.2** (same route): starts 1713; 'Rozra-' 0, 'Arnold' 0. Not this letter.
- **Acta Borussica, Behordenorganisation I** (Google Books ESf8fHFG9ngC, search-within, tools/gbooks_search_within.py): positive control 'Manteuffel'
  20 hits (incl. pp. 256-258, reports of 4 and 7 Oct 1712); 'Rozrazewski' 0, 'Stanislaus' 0, 'abdiquer' 0, 'Arnold' 3 (Arnold Westenberg, unrelated).
  0454 is not printed there.
- **Sten Bonnesen, Studier over August II:s utrikespolitik 1712-1715, del I (Lund 1918)** (Google Books GS3SAAAAMAAJ, snippet view only; found by the
  Books API query '"Rozrazewski" Berlin 1712', 1 hit): pp. 68-70 "Rozrazewski ... till Stockholm", "Rozrazewski sandes till Berlin for att vid behov
  kunna ...", pp. 62-71 Stanislas's abdication ('abdikation'), p. 77 a French quotation dated October ("qu'il souhaitait fort de prendre mesures a ...");
  the front matter cites "Manteuffel in Berlin. 1711 Sept.-Nov." among its Dresden sources. **SUBSTANCE, and a real risk of prior print**: a 1918
  monograph on exactly this negotiation, written from the Dresden Manteuffel reports, treats Rozrazewski's mission to Berlin. Whether it quotes or
  paraphrases 0454 (or prints its cipher passages in clear from a period decipherment) cannot be told from snippets: **unchecked beyond snippets**.
  'Arnold' 0 and 'missnojd' unreachable (one search-within answered blocked; host stopped).
- Check 5 / G3 (`tools/print_check.py ... --phrases f0454_08/vmant0454_phrases.txt --only gbooks,ia-global --max-requests 25 --delay 2 --out
  f0454_08/vmant0454_print-check.tsv`; the solver's 6 phrases where its Google Books was 429, plus 3 clear-context phrases): IA global full text 0 hits
  for all 9; Google Books: 2 no hits, 1 HTTP 503 ('Rozrazewski qui est ici de la part de Stanislas'), 6 loose-AND noise (276-339 volumes, top hits
  unrelated: Charles-Quint, Vies des Saints, Codes et lois). IA be-api '"Rozrazewski" Stanislaus 1712' 336 (16th-century Rozrazewskis, unrelated),
  '"Rozrazewski" Stanislas Berlin' 0.
- Not searched: Mercure historique et politique / Europaische Fama Oct-Nov 1712 (no time-boxed route found this session; GB-PHRASE covers only Apr-May
  1713 for 0136); Lamberty's Memoires VII; Polish scholarship on the Rozrazewski mission (Feldman, Polska w dobie wielkiej wojny polnocnej); JSTOR (no
  row: below N3); aaymeloglu/unsolved-ciphers.

**6. Classification.** Key: **published** -- Dr. O. Krauske's 1893 manuscript table (Loc. 694/10), someone else's modern key, credited. Not `period`:
the brief invites the argument that the table was rebuilt from period glosses (it agrees 17/17 with the f.468 glosses), but `period` means a key we
rebuilt from a document of the time; here we used Krauske's finished table as given, so the key is his, as every earlier audit of this folder ruled.
Item (0454, its cipher spans): **N2**, confidence medium-low. No prior plaintext or decipherment of this leaf located; but its news -- Arnold's mission
to bring Stanislas to abdicate (Droysen IV.1 p. 267, Anm. 511) and Rozrazewski sent by Stanislas to Berlin (Bonnesen 1918 pp. 68-70) -- is printed,
which in this folder's practice (0375 Arnold/Eosander, 0395 duc Ferdinand) is N2, not N3. Bonnesen, written from these very reports and not readable
here beyond snippets, could lower it to N1. text: unknown (news known).
**Depth (rule 4a, the bar above).** Cipher clause: longest contiguous H/C/S stretch 11 letters (r03/r15 'rozrasewsky'), against an AD of about
127-138 letters for this key (FAM-MANTV): **fails**. Code clause, tested as V-MANT08 did on 0391 (>= 2 non-verbatim clear-context sentences, a coarse
class check, consistency with a letter-spelled run of the same item): **198 Stanislas** reads in at least five independent sentences read from the
image ("...negociation avec 198 qu'il regarderoit toujours comme un rebelle"; "qui est icy de la part de 198"; "ce que 150 voudroit accorder a 198, en
cas qu'il [renonc-]"; "qui je voudrois que 257 envoyat a 198"; "198 avoit temoigne etre malcontent de luy parcequ'il l'avoit ... trop presse de
[abdiquer]"; "tout ce que 198 doit avoir ecrit"); class person, a ruler who can renounce and send envoys; and the same item's letter-spelled runs
'abdiquer', 'renonc-' and 'rebelle' fit Stanislas's position in 1712 -- **met**. (150 le Roi de Pologne also reads in two sentences.) The C grade of 198
is not what meets it. **D2.** D3 out: S 46 of 62 = 74.2% by the PREREG grade (C 42 of 62 = 67.7% by key.tsv row), under 80%, and no non-statistical
check that the letter runs are right beyond the clear-text fit.
**My D2 sentence (written from the reading and the clear text on the crops, Droysen used only to confirm):** "In this letter of autumn 1712 Manteuffel
reports that Stanislas's envoy Rozrazewski, then at Berlin, had had an audience of the King of Prussia three days earlier and passed on all that
Stanislas had written, that the question was what the King of Poland would grant Stanislas if he renounced with the King of Sweden's consent, and that
Stanislas was said to be displeased with the Prussian agent Arnold for having pressed him somewhat too hard to abdicate."
depth_pct 74.2 (S 46 of 62; all six S runs read in sense).
Safe sentence: "Krauske's 1893 table applied to Manteuffel's letter of autumn 1712 (Loc. 694/08 ff.360v-361) reads 'rebelle', 'abdiquer', the name
Rozrazewski and the agent Arnold in cipher; the abdication negotiation and Arnold's mission are printed in Droysen IV.1 p. 267, and Rozrazewski's
mission to Berlin is treated in Bonnesen (1918), not read here beyond snippets."
Unsafe: "a previously unread report of Rozrazewski's audience"; "Stanislas's displeasure with Arnold, not known before"; "46 tokens deciphered (S)";
any date for the letter stated as read.
No SECOND-OPINIONS-QUEUE row and no AUD2 WORK-QUEUE row: N2 is below the brief's N3+ and D2+ trigger (D2 alone does not meet it).

**7. Postmortem and corrections.** (a) MANT-0454's check 4 was not run by date; Droysen IV.1 p. 267 / Anm. 511 (the Arnold mission) was already cited in
this folder (V-MANTR8 on 0375) and is the first place to look for any Stanislas/Arnold cipher -- done here. (b) The reading's "J., qu'il avoit dit" --
"J." is uncertain on the crop (a struck or abbreviated mark); not a cipher token, no grade change. (c) 'Rozrasewsky' stays I as an identification, now
corroborated (Bonnesen: Rozrazewski sent by Stanislas to Berlin); spelling as decoded, the modern form is Rozrazewski/Rozrażewski. (d) The solver's
letter-date cell "unseen" is now "not on 0452-0454; mid-Oct to early Nov 1712 by position (I)". No over-claim found in the solver's files.
Requests this audit: www.archiv.sachsen.de 2 (200); archive.org 4 (metadata 2, djvu 2); be-api.us.archive.org 11; www.googleapis.com 15 (two 503);
books.google.com 22 (search-within; one blocked answer, host stopped). Vision: none delegated (my own eye on committed crops and reduced frames).
Next: (1) read Bonnesen 1918 pp. 62-77 (JSTOR/LOCAL-QUEUE or a library scan) -- the decisive prior-print check for 0454; (2) transcribe 0453's cipher
groups (two blind passes on line crops, ~$3) -- 60.35.21.33.14.15.10.26 after "toujours dispose a" is a second context for the 'renonc-' run;
(3) fetch URL 0450-0451 for the letter's date line (2 GETs).

## AUDIT (V-MANT0109)

Verifier V-MANT0109 (account 2, LANE FAMILY-A2g), 9 Oct 2026, 08:05-08:2x UTC by `date -u`; a separate session from the solver MANT-0109
(07:43-07:57 UTC) and from every earlier verifier; I had not read 0109 before this job. Brief: .claude/briefs/runs/2026-10-09-ytbiz-family-0709-jobs.md
"### V-MANT0109". Claim under audit (NOTES "MANT-0109"): "694/08 0109 (f.80) both pages read under Krauske's table: 80 tokens, S37 M43 (38 M =
name-abbreviation groups 55.44 x12, 7.60 x7); gate (b) PASS at 43 letters (real -1.392 vs p95 -1.687, p99 -1.539, 0/1000; power 18/18); reads Kraut,
Kr., commissioners Feldm. le comte Dona / Printz / Kameke / Ilgen, le grand maitre". Nothing decoded here; key.tsv, ciphertext and reading untouched.

**Depth bar copied before ruling** (.claude/briefs/runs/2026-10-08-acct3-depth-bar.md): CLAUDE.md 4a governs. Cipher clause = a contiguous H/C/S
stretch longer than AD (~1.5 x unicity, every liberty counted; an unfitted external key does not shrink H(K)). External check = a D3/D4 element,
never a substitute for the clause at D2. Code clause = a code value that reads sensibly in >= 2 independent contexts; an H/C grade on the value does
not satisfy it on its own; a verbatim repeated phrase counts once. D2 = one clause plus the verifier's own true, specific sentence about the content,
written from the reading (an edition may confirm it, never supply it). Otherwise D1.

**0. Step 0 (the solver's owed lookup).** "sachsen take" 08:06, 1 GET (URL file 0108, HTTP 200 image/jpeg, 4339x3865, sha256 prefix 373dc9a3c2f57967;
film card reads "Aufnahme Einheit 0109", the folder's known one-frame URL/card offset), "sachsen release" 08:06; 0110 not fetched (0108 carries the head).
Crops committed in f0109_08/v0108/ (`python3 tools/iiif_lines.py --image 0108.jpg --out .../f0109_08/v0108 --region 2130,940,1700,2780 --prefix f0108R
--lines-per-crop 2 --overlap 60 --distance 55 --prominence 20 --debug`, 15 crops + overlay + manifest.json; full image not committed, folder over 30 MB).
One blind Sonnet call on the crop paths only (f0109_08/v0108/blind_0108.txt) and my own eye on L01-L02: the right page of URL 0108 is **f.79, the
letter's first page: "No. 40" (subagent "Ao: 40."), "L. S.", "Berlin ce 4 Juin 1712"**, opening "Je me suis donne plus d'une fois l'honneur d'entretenir
V.E. des differents de 55.44. 1000 7.60." (1000 = 'et' in key.tsv); its last line ends "qu'il avoit deja preparé conjoin-", which joins 0109's opening
"-ment avec 11.60.66.6.28". Code runs on f.79 (not decoded): 55.44 x4, 7.60 x4 (incl. "7.60 aiant obtenu l'entree au conseil de guerre"), 46.50.10.64.11.35.44
("par la protection de ___"). No gloss. The left page of 0108 is the end of the preceding letter (Charlottenburg, Ahlefeldt). So 0109 = ff.79v-80 of
**Manteuffel to Flemming, Berlin, 4 June 1712 (No. 40)**, read from the image.

**1. Item.** SHStA Dresden 10026 Geheimes Kabinett Loc. 694/08, URL files 0108-0109, ff.79-80, Manteuffel to Flemming, Berlin 4 June 1712. Ciphertext
f0109_08/ciphertext.tsv, 80 tokens in 24 groups, no gloss. Prior-work tool (`--step-type audit --fetch`, item spec with date 1712-06-04) exit 4: eleven
LEAD live claims, none covering 694/08 0109 except MANT-0109 itself, recorded CLEAR; tomokiyo CLEAR, solver-cache CLEAR; aaymeloglu and 4-editions
UNCHECKED-NET (editions by hand below -- and the hand check is where it is found).

**2. Re-derivation (rule 7), from the repository root:** `tools/decode_key.py .../f0109_08 --check` "tokens 80: C 52, M 28 / reading up to date";
`f0109_08/judge_gate.py --check` "judge_gate.out/token_blocks.tsv up to date"; `f0109_08/grade_0109.py --check` "grades.tsv: up to date". All exit 0.
Key rows checked: 55 b|[a] M, 44 l C, 7 g C, 60 r|re|ro M, 1000 et C, 284 comte C, 260 Kameke M, 259 Ilgen M (key.tsv).

**3. Transcription check.** Against the print (item 5): Acta Borussica's editor prints the one group he left unresolved as "10. 3. 1. 35. 44. 120. 13"
-- the same seven codes as MANT-0109's r18 tokens 1-7, **including tok4 = 35** (the solver's low token, alt 55): confirmed. All 24 groups fall at the
24 name/phrase slots of the printed text in order (12 Blaspil, 7 Grumbkow, 3 Krautt, the commissioners run, le Grand-Maitre): 24/24.

**4. Design audit (rule 3).** PREREG c0294af33 before any pass or score (solver's statement and ROOM; not re-verified commit by commit -- the room.py
fold caveat applies). Gate (b) can differ from the target (permuted letter values change the letters scored), power measured at L=43 (18/18). PASS stands
as a statistic; it is moot for novelty because the plaintext is printed.

**5. Novelty search log (rule 10; checks 4-5), by the letter's date.**
- **Acta Borussica, Behoerdenorganisation I (Schmoller/Krauske, 1894)** -- Google Books search-within ESf8fHFG9ngC (`tools/gbooks_search_within.py`;
  positive control 'Manteuffel' 20 hits) and IA full text `diebehrdenorgan01posngoog` (found by be-api phrase search '"Blaspil etait un ignorant"', 2 items:
  that one and `bub_gb_cmQBAAAAYAAJ`): **Nr. 64 (pp. 204-207), "Conflict Blaspils mit Grumbkow und Krautt"**, a royal order of 20 May / 1 June 1712 for a
  commission, followed by "der folgende Bericht des Saechsischen Gesandten Freiherrn von Manteuffel an den Generalfeldmarschall Grafen von Flemming, Berlin
  4. Juni 1712" (source note: "Urschrift. Dresden Hauptstaatsarchiv. Vol. CXLV. Loc. 694"), printed in French **in clear with every cipher name resolved**:
  "Grumbkow ayant obtenu l'entree au conseil de guerre ... par la protection de Jaeckel ... que Blaspil etait un ignorant, un paresseux et un ivrogne ...
  Grumbkow eut la malice de porter le projet de l'etat susdit qu'il avait deja prepare conjointement avec Krautt, a Blaspil pour qu'il voulut le revoir.
  Celui-ci lui repond qu'on ne saurait faire d'etat avant que Mr. Krautt ait rendu ses comptes ... Blaspil de son cote se retire tout camus chez lui ...
  Le Roi la dessus nomme sur le champ Wartensleben le feldmarechal, le comte Dhona, Printzen et Kameke (Ilgen ayant adroitement decline d'en etre) ...
  le Grand-Maitre sortant de son naturel, entreprit de plaider ... la cause de Blaspil ... que Grumbkow eut ose s'attaquer impunement ... a son commandant."
  Editor's footnote (p.206): "In der chiffrirten, nicht aufgeloesten Urschrift steht 10. 3. 1. 35. 44. 120. 13. Nach unserem Versuch zur Dechiffrirung ist
  dies zu uebersetzen: E. W. feldm." (Excellence Wartensleben feldmarechal, or Comte W. f. if 10 is a slip for 15). Footnote p.207: le Grand-Maitre = Paul
  Anton von Kameke, Grand-Maitre de la garderobe. Excerpt committed: f0109_08/vmant0109_AB_BOI_pp204-207.txt (OCR verbatim, public domain). The same
  volume quotes further Manteuffel reports on the affair (18 June 1712, pp. 208-213; 4 and 7 Oct 1712, pp. 256-258; 1713, pp. 285-287, 307-321, 356-359).
- Droysen IV.1 (IA djvu, 2 requests): 'Blaspeil' 1 (Cleve, unrelated), 'Kraut' 2 incl. p. 256 "Die geheimen Verhandlungen, Sommer 1712": "Die beiden
  Kamekes, der Generalcommissar Kraut waren oben auf" -- not this letter.
- Check 5 / G3: `tools/print_check.py ... --phrases .../f0109_08/phrases.txt --only gbooks --max-requests 8` (f0109_08/vmant0109_print-check.tsv): the
  solver's six loose phrases give 2 no hits, 2 HTTP 503, 2 generic-idiom noise (258-341 volumes) -- they miss Acta Borussica because they search the
  solver's paraphrase, not the names; the name search above is what finds it. books.google.com search-within answered 'blocked' on the second batch
  ('grand maître', 'Juin 1712'); host stopped.
- Sibling period gloss: 694/09 0085 (March 1713) carries the interlinear gloss "Grumbkow" over 7.60 (f0085_09/pairs.tsv G1) -- a period witness for
  7.60 independent of the print. Krauske's table itself has 8.60 Grumbkow (compounds.tsv), not 7.60.

**6. Classification.** Key: **published** (Krauske's 1893 table, credited; the same Krauske co-edited the 1894 volume). Text: **known**.
Item (694/08 0109, ff.79v-80, all 80 tokens): **N0** -- plaintext and decipherment of this very item already known: Acta Borussica BO I (1894) Nr. 64
pp. 204-207 prints this letter in clear from the Dresden original with the cipher resolved, and its editor's footnote shows he deciphered the original's
cipher (and left one group, 10.3.1.35.44.120.13, as "E. W. feldm."). Confidence high (24/24 slot agreement; distinctive clear phrases identical).
Grades against the print (rule 4, verifier's grade; grades.tsv stays the solver's PREREG grade): 80 tokens **C 80** (H 0, S 0, M 0) -- every group's
printed value matches the decode letters at its slot (55.44 'bl' = Blaspil x12, 7.60 'gr' = Grumbkow x7, 11.60.66.6.28 = Krautt, 11.26/11.27 'Kr.' =
Krautt, r18 = E. W. feldm. / le comte / Dhona / Printzen / et / Kameke / Ilgen, r21 = le Grand-Maitre). The two abbreviation groups are therefore C
(known plaintext), not M; 7.60 also has the 0085 period gloss.
**Depth (rule 4a, the bar above).** Cipher clause: longest contiguous run 21 letters (r18) against an AD of about 127-138 letters (FAM-MANTV): fails.
Code clause: 7.60 (Grumbkow) reads sensibly in seven non-verbatim sentences on 0109 ("sans que 7.60 en prit la peine", "Mr 7.60 (qui attendoit dans
l'antichambre)", "sur quoi 7.60 deploya d'abord sa marchandise", "le zele de 7.60", "l'etat de 7.60 ... fort defectueux", "celuy de 7.60", "que 7.60 eut
ose"), class person, a subordinate who encroaches on his superior's department; 55.44 likewise in twelve -- **met**. D3: 100% of tokens C plus a
non-statistical external check (the printed decipherment, group by group, and the 0085 gloss for 7.60) -- **met**. D4 not met: no fresh rule-7
re-derivation by a session that has seen only the spec and key. **D3**, depth_pct 100.
**My D3 sentence (written from the reading and the clear text on the crops; the print confirms it):** "In his letter of 4 June 1712 Manteuffel tells
Flemming how Grumbkow, newly admitted to the Prussian war council, laid before the King a war budget drawn up with Krautt showing the King some 400,000
thalers in debt, to the discredit of his superior Blaspil, how Blaspil answered with an account showing over 100,000 thalers in hand, and how the King
named commissioners -- Wartensleben, Dohna, Printzen and Kameke, Ilgen having declined -- the first two of whom upheld Blaspil."
Safe sentence: "Manteuffel's letter of 4 June 1712 to Flemming (SHStA Dresden Loc. 694/08 ff.79-80), cipher passages re-read with Krauske's 1893 table;
the letter is printed in clear in Acta Borussica, Behoerdenorganisation I (1894), Nr. 64, pp. 204-207, and our reading agrees with that print at all 24
cipher groups."
Unsafe: any wording that the letter or its names were unread, unidentified or newly read; "55.44 and 7.60 not identified" (they are printed as Blaspil
and Grumbkow); "'ew' unexplained" (printed as "E. W. feldm.", Wartensleben).
No SECOND-OPINIONS-QUEUE row and no AUD2 WORK-QUEUE row: N0 is below the brief's N3+ trigger.

**7. Postmortem and corrections.** (a) The miss: Acta Borussica BO I was named in the check-solved line, cited in this folder's own status note for f.410,
and V-MANT0454 logged 'Manteuffel' 20 hits there including p. 204 -- but no step ran the letter's names (here Blaspil/Grumbkow/Krautt) or date against
the volume before a reading campaign; MANT-0109 honestly left check 4 by date "unchecked". (b) Corrections made: HYPOTHESES.md "MANT-0109" gains a
V-MANT0109 note (names, 'ew', le Grand-Maitre resolved in print); NOTES.md pointer section; status.json row. (c) **Flag for the lane:** before any
further reading job on a Manteuffel leaf about Prussian administration (Kraut, Blaspil, Grumbkow, Kameke, the Generalkriegskasse, the 1713 reforms),
grep the IA djvu of `diebehrdenorgan01posngoog` for the leaf's names and date; the volume prints extracts of these reports. Diplomatic leaves (0391
Oxford/Heusch, 0454 Rozrazewski) have no hit there ('Heusch' 0, 'Oxford' 0, 'Rozra' 0, 'Stanislas' 0 in the djvu). (d) key.tsv: 55.44 Blaspil and 7.60
Grumbkow could enter compounds.tsv as C (print + 0085 gloss); not done here (verifier does not edit the key) -- a one-line job for the lane.
Requests this audit: www.archiv.sachsen.de 1 (200); archive.org 5 (metadata 1, djvu 2, advancedsearch 2); be-api.us.archive.org 2 (the same phrase query twice);
books.google.com 2 batches of search-within (second batch partly 'blocked', host stopped); www.googleapis.com 6 (two 503). Vision: 1 Sonnet call (0108
crops) + my own eye on two crops and the reduced frame.

## AUDIT (V-MANT0176)

Verifier V-MANT0176 (account 2, LANE FAMILY-A2h), 9 Oct 2026, 12:00-12:1x UTC by `date -u`. I am a separate session from the solver MANT-0176
(11:23-11:40 UTC) and from every earlier verifier, and I had not read 0176 before this job. Brief: .claude/briefs/runs/2026-10-09-ytbiz-family-1010-jobs.md
"### V-MANT0176". Claim under audit (NOTES "MANT-0176"): "694/08 0176 (Berl. 2 Juil 1712), 31 code tokens, gate (b) PASS real -1.288 vs p95 -1.670;
S26 M4 U1; reads Maier x2, deux colonels (Sp)ald et Horn jusqu'a Bernau". Nothing was decoded here. key.tsv, the ciphertext and the reading are untouched.

**Depth bar, copied before ruling** (.claude/briefs/runs/2026-10-08-acct3-depth-bar.md): CLAUDE.md 4a governs. Cipher clause = a contiguous H/C/S
stretch longer than AD (~1.5 x unicity, every liberty counted; an unfitted external key does not shrink H(K)). External check = a D3/D4 element,
never a substitute for the clause at D2. Code clause = a code value that reads sensibly in >= 2 independent contexts; an H/C grade on the value does
not satisfy it on its own; a verbatim repeated phrase counts once. D2 = one clause plus the verifier's own true, specific sentence about the content,
written from the reading (an edition may confirm it, never supply it). Otherwise D1.

**1. Item.** SHStA Dresden 10026 Geheimes Kabinett Loc. 694/08, URL file 0176, right page (stamp/letter no. 135), "a Berl. le 2 Juil. 1712",
Manteuffel to Flemming (sender and recipient by the folder's series, not by a signature on this page). The letter runs past the foot of the page (0177
not seen). Ciphertext f0176_08/ciphertext.tsv: 31 tokens in 5 runs, no gloss. Solver's search log: prior_work.py exit 4 (all LEAD rows recorded),
MANT-ABBO's grep of Acta Borussica BO I (mant0608/abbo_check.tsv row 0176 'n'), Droysen IV.1/IV.2 djvu grep, and print_check on 6 paraphrase phrases.
prior_work.py `--step-type audit --fetch` (this audit): one LEAD (MANT-CUC2's live claim). I recorded it CLEAR because CUC2 was done at 11:35 and its
work was 0410/0284. tomokiyo and solver-cache are UNCHECKED (no folio key), aaymeloglu and 4-editions are UNCHECKED-NET, and I did the editions by hand below.

**2. Re-derivation (rule 7), from the repository root:** `tools/decode_key.py .../f0176_08 --check` gave "tokens 31: C 24, M 6, U 1 / reading up to
date"; `f0176_08/judge_gate.py --check` gave "up to date"; `f0176_08/grade_0176.py --check` gave "grades.tsv: up to date". All three exit 0. Key rows the
reading leans on: 13 m, 66 a, 9 i, 10 e, 2 e, 26 r, 36 f, 17 p, 50 a, 44 l, 120 d, 1000 et, 8 h, 33 o, 21 n, 27 r, 14 n, 25 a, 6 u, all C
(Krauske 1893). 51 s|sa, 60 r|re|ro and 55 b|[a] are M, and 62 is the null. **'bernau' rests on 55 = b, an M row**, and 'spald' on 51 = s, an M row.

**3. Transcription check.**
- *One blind look at r04 positions 3-7* (the solver's native-zoom settlement, the line the crop band cut). I stacked crops f0176R_L10 and L11, which
  have contiguous boxes and so give the original pixels, enlarged the strip 2x and gave it to one blind Sonnet call. The call saw only the image and
  had no values. It read "a 55.2.27.14.25.6, [blot] ou je pourrois": 55 medium, 2 medium-high, 27 medium, 14 medium, 25 medium, 6 medium-low. **It
  agrees with the solver on positions 1-6.** On **position 7 it reads a comma, not a digit** ("a short hooked tick level with the base of the
  digits"). I see the same thing. So r04 pos 7 '7' (= g, already M low) is most likely punctuation, and the run reads 'bernau', not 'bernaug'. The
  call could not read r03's head under the strike and called the whole stretch struck. The solver also left that stretch (51.17.50 [struck] 44) at low.
- *Three tokens spot-checked by me on the committed crops (2x):*
  (i) r02 pos 3 (L09) and (ii) r05 pos 3 (L12): both are the y-shaped glyph, 9 or 4. The crops cannot settle it, the same open question as
  MANT-EYE63R's y-glyph. Under 4 (= x) the name would read 'maxer'. 'maier' is therefore conditional on 9, and the solver's 'medium' is fair.
  (iii) r01 pos 3 (L09): I read "171.35.26" (a 2 followed by a 6). This agrees with the worker's native look and MANT-INV08B's eye ('26'), not with
  the two passes' '62'. Under the key that gives 'le e r', which still does not read. The token stays U/unsettled, and the 'r01 unread' finding stands.
- r05 is followed by "(." or "C." on L12. I read it as clear punctuation, as the solver did.

**4. Design audit (rule 3).** PREREG-MANT-0176.md was pushed in its own commit (6d0a0ff8b, 11:29 UTC), before the fetch, according to the solver's
NOTES. I did not re-verify it commit by commit (the room.py fold caveat applies). Gate (b) permutes letter values over letter codes, which changes the
letters scored, so the control can differ from the target on the statistic. Power was measured at L = 32 (37/38). The PASS stands as a statistic. It
says the 32 decoded letters look more like French/names than permuted-key decodes do. It does not say what the names refer to.

**5. Novelty search log (rule 10), by date (+-2 days) and names.** Each edition was checked with a positive control first.
- **Acta Borussica, Behoerdenorganisation I (1894)**: IA `diebehrdenorgan01posngoog` _djvu.txt, fetched once. Positive control: 'Blaspil' gives 39 hits,
  and be-api's phrase '"Blaspil etait un ignorant"' returns this item. Stems tried: Manteuff 0 / 'teuff' 30 (Fraktur OCR), Meyerf/Mayerf/Meierf 0,
  Custrin/ftrin 6 (none 1712 diplomatic), Golowkin/lowk 0, Menschikoff 0, Spald 0, Horn 0, Bibliothe 1 (Lipenius, unrelated), Bernau 2 (a town list
  and an index entry on brewing). **The letter of 2 July 1712 is not found.** This agrees with MANT-ABBO's row 'n'.
- **Droysen, Geschichte der preussischen Politik IV.1**: on disk, sources/ia-fulltext/print-check/p1geschichtederpre04droyuoft_djvu.txt.gz. Positive
  control: note 505 cites "des saechsischen Gesandten Manteufel Bericht, Berlin, 21. Juni" (found). Pp. 265-267, "Menschikoff und Wellingk in Berlin,
  Juni 1712", show Menschikoff's audience demanding guns. They cite nothing of 2 July, and Maier/Meyerfeldt, Custrin, the library, Bernau and the
  colonels are absent. IV.2 starts in 1713 (solver's grep, not repeated).
- **Europaeische Fama / Mercure historique et politique, July 1712**: IA advancedsearch found Fama volumes, but their metadata is undated ('1702' on
  all of them), so the 1712 part was not identified. Mercure historique 1712 found nothing by title. Both are **unchecked** at the volume level. They
  are covered only by the IA-global phrase searches below.
- **Google Books API** (key, country=US, 12 calls). Positive control: 'Meyerfeldt Stettin 1713' gives 109 hits, among them Dumont's Corps universel
  diplomatique, "der Herr General Gouverneur von Meyerfeldt" at Stettin, and Droysen IV.2 p. 56, "mit Menschikoff und Meyerfeldt". Found nothing:
  '"Meyerfeld" Bernau 1712', 'Meyerfeldt Manteuffel 1712 Berlin', 'Mayer Bibliothek Menschikoff 1712 Custrin', and 'Spalding Horn Meyerfeldt 1712
  Obristen'. Noise only: '"Mayerfeld" Bernau'. 'Manteuffel Flemming "2 juillet 1712"' returned one hit, a 2026 book citing Acta Borussica's 4 June
  letter and Berner, *Aus dem Briefwechsel Koenig Friedrichs I.* (p. 265, 1712). Berner is a lead, **not searched**. Five queries got HTTP 503, and I
  stopped the host after the retry.
- **IA full text (be-api, global) and OpenAlex**: `tools/print_check.py --phrases f0176_08/vmant0176_phrases.txt --only ia-global,openalex`, output
  f0176_08/vmant0176_print-check.tsv. The phrases were 5 name phrases (Meyerfeldt Bernau; bibliotheque de Mayer Custrin; Mayer Bibliothek Custrin;
  deux colonels Spalding Horn; Menzikof bibliotheque Mayer). No hits in IA-global or OpenAlex. The OpenAlex keyword search 'Manteuffel Flemming 1712'
  gave 11 unrelated works. Further be-api phrases on the *clear-text* library: '"Mayers Bibliothec"' gave 17 hits, among them "des Hamburgischen Herrn
  D. Mayers Bibliothec, welche A. 1716 zu Berlin verauctioniret" (IA 10123080bsb). This is the library of the theologian Johann Friedrich Mayer
  (d. 1712), and it confirms the clear-text context only. It does not print this letter.
- Not searched: Bonnesen (1918), Berner (1901), Haake, and the Saxon-side Flemming papers in print. aaymeloglu is not cloned. JSTOR has no row
  queued (N3 is not blocked by a JSTOR row).

**6. Identification note (verifier's, grade M, not a key edit).** The solver writes "'Maier' x2 (also in the leaf's clear text)", which ties the
cipher name to the library's owner. I think they are two people. The clear text's "bibliotheque de Maier" is the library of the late Dr J. F.
Mayer, which was auctioned at Berlin in 1716. The cipher 'maierf' (r02), the one who "enverroit deux colonels ... jusqu'a Bernau", and 'maier' (r05),
whose "certificat" is asked for, read best as **Meyerfeldt**, the Swedish general and governor-general at Stettin in 1712-13 (Google Books control
above). On that reading r02's trailing 36 'f' is the start of the name, and is not a stray letter as the solver flagged it. Two Swedish colonels sent
toward Berlin fit the clear text's secret contact ("par quelque homme de confiance"). This is an M-grade hypothesis from context. No print located
confirms the contact. It is logged in HYPOTHESES.md.

**7. Classification.** Key: **published** (Krauske's 1893 table, credited). The brief says `period`. I keep `published` to match every earlier
Manteuffel row in status.json and V-MANT0109's ruling, and I flag the mismatch to the lane. Text: **unknown**.
Item (694/08 0176, 31 tokens): **N3**: no prior plaintext or decipherment located after the logged search. It is not N4, because Berner (1901),
Bonnesen (1918), the Fama/Mercure volumes for July 1712 and the Flemming-side editions were not read, so the principal editions are not covered.
Evidence quality: medium (OCR Fraktur greps with positive controls; Google Books partly 503). Confidence in "not in Acta Borussica BO I / Droysen
IV.1" is high. Confidence that it is in no print is low-moderate.
**Depth (rule 4a, the bar above).** Cipher clause: the longest contiguous run is 11 letters (r03 'spaldethorn', and it contains M tokens 51/17/44).
The other runs are 5-7 letters. The AD for this key is about 127-138 letters (FAM-MANTV), so the clause **fails**. Code clause: the leaf has no
nomenclator code value. Every token is a letter-cipher sign. The name spelled twice (13.66.9.10.26.36 and 13.66.9.2.26) is two letter-cipher
stretches, not one code value, and its third sign is the open y-glyph (9 or 4). Clause **not met**. No external check exists (no gloss, no print).
**D1** ("fragments read"). depth_pct 83.9 (S 26 of 31 by the PREREG grade). That share is reported only, because no clause is met.
Safe sentence: "Manteuffel's letter of 2 July 1712 to Flemming (SHStA Dresden Loc. 694/08, frame 0176): fragments read in its five short cipher runs
with Krauske's 1893 table (statistical gate passed at 32 letters). They give a name read 'Maier(f)' twice, two colonels '(Sp)ald' and 'Horn', and
'Bernau'. No prior decipherment was located in Acta Borussica BO I, Droysen IV.1, Google Books, Internet Archive full text or OpenAlex (searched 9 Oct
2026)."
Unsafe: "deciphered", "partially deciphered", any first/new/unpublished wording; "Maier is the owner of the library" (unproven, probably wrong);
"Meyerfeldt" stated as read (it is a verifier's M hypothesis); 'bernaug' (the final '7' is most likely a comma).
**No SECOND-OPINIONS-QUEUE row and no AUD2 WORK-QUEUE row**, because N3 with D1 is below the brief's N3+ D2+ trigger.

**8. Postmortem and corrections.** (a) No over-claim of novelty was found. The solver kept to rule 10. (b) Two sentence-level corrections. First,
"reads 'Maier' x2 (also in the leaf's clear text)" conflates a cipher name with the clear-text library owner (section 6). Second, r04 is 'bernau'
with a probable comma, not 'bernau' plus a seventh code. The solver had it at M low, so the grades do not change. (c) The transcription stays as
committed. A verifier does not edit it. Owed by the lane (one job, about $0.5): r04 pos 7 to punctuation and r01 pos 3 to 26 (agreeing with three
eyes), then re-run the --check scripts and the gate. The gate result would be expected to hold at 31 letters, but that is not computed here.
    Fix applied 0a781d4e4 (MANT-0177, 9 Oct 2026): r04 pos 7 removed as a comma, r01 pos 3 = 26; --check exit 0; gate (b) PASS holds (-1.277 vs p95 -1.665, 0/1000; S27 M3 U0, 30 tokens).
(d) Next print checks before any further reading of this letter: Berner (1901) and Bonnesen (1918) by date and the names Meyerfeldt/Bernau, and 0177
for the letter's end. The 0177 reading may identify 'le vieux'.
Requests this audit: archive.org 4 (djvu 1, advancedsearch 3); be-api.us.archive.org 7 by hand + 5 print_check; api.openalex.org 6 (print_check);
www.googleapis.com 12 (5 x 503, host stopped); www.archiv.sachsen.de 0. Vision: 1 Sonnet call (stacked L10/L11 strip) + my own eye on L09, L12 and the stack.

## V-MANTC (9 Oct 2026)

Verifier V-MANTC (Opus, account 2, LANE FAMILY-A2j; a session that solved none of these leaves), 15:21-15:3x UTC 9 Oct 2026 by date -u. Disk
only: no fetch, every look on committed crops (upscaled 2-5x with PIL in scratch). Scope: the three rule-4 code conflicts named in the
handoff (19, 63, 54) and the 0176 r01 eye check. No novelty class is assigned or changed here.

Directions and dates of the witness leaves (from NOTES.md, mant0608/abbo_check.tsv, mant0609/rank_glossed.tsv): 694/08 0398 Flemming to
Manteuffel, Greifswald 15 Oct 1712 (clear-under-code draft); 0410 Flemming to Manteuffel, Greifswald 20 Oct 1712 (same kind); 0474 (stamp 379,
~Nov 1712) and 0494 (stamp 395, ~Nov-Dec 1712) Manteuffel to Flemming, period interlinear gloss; 694/09 0007/0008 Manteuffel's report, Berlin
7 Jan 1713, gloss; 0056 694/09, 1713, gloss. Krauske 1893 (Loc. 694/10 ff.1-5): the table's own direction is not recorded on disk.

### Code 19 (key.tsv: null, M, Krauske brace 18-19 "wahrscheinlich non-valeurs")
| leaf | line/token | read | slot | dir / date | source file |
|---|---|---|---|---|---|
| 0398 | s02, ...17.33.[44].16.**19**.16.9.51 | 19 (both passes) | 'n' of 'Polonois' | F->M, 15 Oct 1712 | mant0608/cuc/cuc3_agreed.tsv, cuc_candidates.tsv |
| 0410 | s02, 12.2.**19**: | 19 | after 'l'E' of 'l'Electeur' (abbreviation point, colon after the group) | F->M, 20 Oct 1712 | mant0608/cuc/agreed.tsv |
| 0410 | s02, 8.?.**19**: | 19 | end of 'Han.' ('n', colon after the group) | F->M, 20 Oct 1712 | same |
| 0494 | T039 (L05) '19?' | 19? | G05 'declarera', DP miss 'dec' | M->F, ~Nov-Dec 1712 | f0494_08/ciphertext.tsv, gate.out |
| 0494 | T091 (L09) A 14 / B 19, med | 19 | G08 'quelque', DP null | M->F | same |

Eye (c0398_s02_L01, c0410_s02_L01): the second digit of each '19' on 0398/0410 is the open-topped, q-like y-shape that the same strips' '44'
and '24' carry, not the closed-loop 9 of '169' on the same 0398 strip. MANT-0494 records that its reconciliation settled y-shapes as 9 by
convention ("19" among them), and MANT-EYE63R leaves the 4/9 y-glyph open on this hand. Read as **14 (= n, C)**, 0398 gives p.o.l.o.n.o.i.s
fully keyed and 0410's second instance h.?.n under 'Han.'; 0410's first instance (after 'l.e', clear 'l'Electeur') fits neither n nor a letter
and reads best as a non-valeur at an abbreviation point. 0494 T091 is itself an A 14 / B 19 split, and its slot (inside 'quelque') wants
neither n nor a letter. **Verdict: not established as a key conflict.** The two 19 = n witnesses are most likely the y-shaped 4 transcribed
as 9 (14 = n); this is an eye judgement at strip resolution, low-medium, not settled. key.tsv 19 unchanged (null, M). Owed: a native re-read
of 0398 s02 pos 17 and 0410 s02 pos 3/8 (one sachsen GET each, or the y-glyph census MANT-EYE63R named) before 19 is cited either way; the
transcription files are left as read (rule 2).

### Code 63 (key.tsv: null, M, Krauske brace 61-63 "non valeurs?")
| leaf | token | read | slot | dir / date | source |
|---|---|---|---|---|---|
| 0474 | T032 (c0474R_L01) | A '76?' / B '7.63?', settled 63, low | 'a' of 'galere', between 7 (g) and 103 (le) | M->F, ~Nov 1712 | f0474_08/ciphertext.tsv, candidates.tsv, gate.out |
| 694/09 0008 | G05 '33.63.46.30' | 63 | 'ff' of 'offici' | M->F, Jan 1713 | HYPOTHESES.md MANT-0008 table |

Eye (c0474R_L01 at 5x): '7.6?' -- the second digit is crossed by the descender of the gloss 'g' above it and is not a legible 3 (this hand's
3, in '103' two places to the right, has two clear bowls). 66 (= a, C) fits the gloss slot exactly. **Verdict: 0474 is not a witness for 63**
(illegible second digit, most likely 66); the conflict rests on 0008's single instance (63 at 'ff'), which still stands as logged (rule 4, one
instance, not settled). key.tsv 63 unchanged (null, M). Correction to f0474_08/candidates.tsv's 63 row: recorded in HYPOTHESES.md, file left as is.

### Code 54 (key.tsv before this audit: u, **C**, Krauske f.3)
| leaf | token | slot (gloss) | value the slot needs | reader note | dir / date |
|---|---|---|---|---|---|
| 0474 | T052, T103, T107 | 'embarques', 'docteur luther' (gate (b) runs on the gloss text) | u x3 | all high | M->F, ~Nov 1712 |
| 0494 | T063 (L07) | G07 decode 'plus' (23.42.54.51) | u | high | M->F, ~Nov-Dec 1712 |
| 0494 | T151 (L15) | G11 'touchant', 2nd group | u | high | M->F |
| 694/09 0008 | G04 'veut', G10 'troupes' | gloss | u x2 | -- | M->F, Jan 1713 |
| 0494 | T149 (L15) | G11 'touchant', 1st group: [54].33.54.72.25.14.52 = t.o.u.ch.a.n.t | **t** | high; V-MANTC eye: same '54' shape as T151 two groups on | M->F |
| 0494 | T035 (L05) | G04 'Détaché': 120.[54].66 | **t** (or 'ét') | high | M->F |
| 694/09 0007 | G01 'cette': 30.10.[54].28.35 | **t** | low, alt 59 | M->F, Jan 1713 |
| 694/09 0008 | G01 'la Battaille': 110.55.66.[54].28 | **t** | -- | M->F, Jan 1713 |
| 694/09 0056 | G06 'futur': 36.6.[54].67.27 | **t** | A '54?', B '54' | M->F, 1713 |

Not a witness: 0494 **T134** (L15 line start), read 54 high by both passes and decoded by the key as '[54].e.n.t.e.m.e.n.t' after G10's
'...c.o.n': eye (c0494L_L15 at 2x) reads **59** (closed-loop 9, as MANT-INV08C's inventory '59.40.21...'), giving 'contentement' with 59 = t.
A transcription fix is owed in f0494_08/ciphertext.tsv T134 (54 -> 59), not made here (verifier; rule 2). Also: f0494_08/candidates.tsv and
the MANT-0474 section cite the 'Détaché' 54 as T036; in f0494_08/ciphertext.tsv and gloss.tsv it is **T035** (T036 is 66).

**Verdict: a real data conflict (rule 4).** 54 reads u in 7 slots on 3 leaves and t in 5 slots on 4 leaves, every one of them in Manteuffel's
letters to Flemming of Nov 1712 - Jan 1713 -- the same direction and date range, and on 0494 the same word ('touchant' has 54 = t and 54 = u two
groups apart, eye-checked). No direction or date separates the two values, so neither can be preferred by witness; 59 (= t) read as 54 is
possible on 0007 (low) and is what happened on 0494 T134, but T149 and 0008/0056 do not look like misreads at strip scale. Not settled by count.
**key.tsv change (the only one): row `54  u  C  Krauske 1893, Loc. 694/10 f.3  passes agree` -> grade M** (value, source and note unchanged;
grade lowered only), because a 54 token in any letter of this correspondence now has conflicting period support (u: Krauske and glosses on
0008/0474/0494; t: glosses on 0007/0008/0056/0494). Readings regenerated with `tools/decode_key.py` (rule 7): main reading.txt C 202 -> 199,
M 98 -> 101 (3 tokens of 54 on 0511/f410); f0052_09 C 29 -> 28, M 11 -> 12. No other committed reading carries 54. `--check` exits 0 on all 14
configs after regeneration.
Tool flag: before regeneration, with key.tsv already changed, `tools/decode_key.py <dir> --check` exited 0 on the main folder although a fresh
regeneration's header and token grades differed (C 202 vs 199) -- `--check` did not see a grade-only drift. Flagged in ROOM.md; not fixed here.

### 0176 r01: '171' vs '17.1'
Crop f0176R_L09 (the r01 line: 'Le vieux 171.35.26 est revenu voir'), 4x: '1', '7', then a short stroke from the 7's foot ending in a mid-height
tick before the next '1', then '-35'. The tick is the height of the run's separators ('13·66·9·10·26·36' on the next line) but sits joined to
the 7's stroke. **Not settled by eye; leans 17.1 (p.f), low.** ciphertext.tsv r01 pos 1 stays '171' at medium, both readings open; key.tsv 171
(le, note "Vicechancelier" written beside it on Krauske f.4) vs 17.1 is a question a native re-read (one sachsen GET) can settle; this crop cannot.

### Summary
key.tsv: 54 C -> M (grade only). 19: not established (probable 14 misreads), unchanged. 63: 0474 withdrawn as a witness (illegible), 0008 single
instance stands, unchanged. 0176 r01: open, lean 17.1. Transcription fixes owed (not made): f0494_08 T134 54 -> 59; native re-reads of 0398 s02
pos 17, 0410 s02 pos 3/8, 0176 r01 pos 1. Requests: none (disk only).

## V-MANTH (9 Oct 2026)

Verifier V-MANTH (account 2, Opus, LANE FAMILY-A2k; did not solve these leaves). Brief: .claude/briefs/runs/2026-10-09-ytbiz-family-1815-jobs.md
"V-MANTH". Disk only, 0 requests, 0 subagents. Held codes 321, 191, 254, 199, 42: every witness on disk pooled, committed crops eyed (f0312_08
A12/A17/A18, f0136_08 R02/R10/R13, f0314_08 R11, gloss strip and code strip each). Census by script over every `*/ciphertext.tsv`, the main
ciphertext.tsv and every `*.tsv` naming the codes (f0089_08, f0383_08, f0474_08, f0494_08 and the CUC leaves 0282/0284/0323/0348/0398/0410/0499
carry none of 321, 254, 199; 191 and 42 as below). All witnesses are Manteuffel to Flemming, Berlin, 1712 (one direction only).

| code | key.tsv | witnesses (leaf, run/pos, gloss or context, date, gate of that leaf, source file) | verdict |
|---|---|---|---|
| 321 | absent | (1) 694/08 0312 A12 T019, single code under 'Stockolm' (G1) / 'Stockhol' (G2), 16 Sept 1712 Extrait; leaf gate rows (a) and (n) PASS both gloss passes; digits low (crop ends at the gutter, '32' clear, third digit at the edge, a fourth not excluded by eye) -- f0312_08/ciphertext.tsv, candidates.tsv. (2) **conflicting**: 694/08 0530 (f.425v L_L01, 24 Nov 1712 letter) run 321.237.402.104.272.142.560.74 under 'frontiere de la v en bu r', A/B agree on the digits; with 237 = de, 402 = la (both M, R9-MANTPOOL) 321 sits in the 'frontiere' slot -- f425v_0530/reconciled.tsv; gloss M; whether 0528-0530 follow Krauske's table is itself open (HYPOTHESES.md 73/82, NOTES 'different table'). (3) not a witness: 0501 R_L05 '825/823/321' is an alternative read only. | **held, not keyed.** One witness, low digits, and a cross-leaf data conflict (rule 4): Stockholm (place block 310 Dresden, 312 Berlin, 313 Hambourg, Sept 1712) vs 'frontiere' (Nov 1712, table identity open). Not settled by either; M at any slot. No key.tsv row added (a row would merge a conflicted code). |
| 191 | Stenbock, M (Krauske f.4, passes split Stenbock?/Steenbock?) | (1) Krauske 1893 table. (2) 694/08 f.468 (frame 0580, Dec 1712) three single codes, gloss 'Stenbock' (A2-SAX2/GAPS154); leaf control 17/17 vs shuffled-key p99 1, cleared. (3) 694/08 0312 A17 T036, A18 T037, both passes 'Steinbock', 16 Sept 1712; leaf gate PASS; the name rule missed only on spelling. Eye: both groups written '1y1' (the folder's y-glyph in the middle). | **second and third witnesses agree, spelling only; grade left M** (this job may only lower). The y-glyph caveat: under y = 4 these would be 141 (unkeyed); the gloss agreeing with 191 is a point for y = 9 on 0312's hand. Independence caveat: Krauske may have built his table from these same period glosses, so gloss-vs-Krauske agreement is not two independent decipherments. A raise to C is the lane's call under a pre-registered spelling-tolerant name rule, not made here. |
| 254 | absent; **259 = Ilgen, M** (Krauske f.5, passes split Ilgen?/Flynn?) | (1) 694/08 0136 R10 T060 and R13 T064 (18 June 1712), both blind passes read **259** (R13 B '25'), MANT-0136B settled 254 by eye on V-MANTC's "the y glyph = 4"; notes over both the worker's eye reads 'Ilgen' (gloss pass 'maget Flyn', 'Haer?'; not scored). Eye (this job): the last glyph is the open y with long descender, the same form as the middle glyph of 0312's '1y1' = 191. (2) 694/08 0290 r12 '25y' ('que 25y fausse la parole qu'il luy a faite'), no note, leaf gate (a) FAILed both blind passes: not a witness. (3) 694/08 0314 R03/R08/R13/R18 passes '254', settled 257 (7-shaped last glyph) under 'R. de Prusse' = key 257: not a 254 witness. | **254 is not a separate candidate code.** The only '254' slots are the y-glyph settlement on 0136; read as the passes read them (y = 9, the convention on 0015, 0214, 0390, 0391, 0485 and here on 0312), they are 259, which key.tsv already holds as Ilgen. So 0136 R10/R13 are a second witness for **259 Ilgen** (eye-read note, unscored): 259 stays M. Under y = 4 they would be an unkeyed 254 under the same name, which would be a second Ilgen code (as 98 and 357 are on the Nov leaves) -- open until the y-glyph census. No key.tsv row; f0136_08/ciphertext.tsv's settled 254 is a transcription question owed to that census, not edited here. |
| 199 | absent | (1) 694/08 0136 R02 T037, tail of 110.43.66.60.48.26.25.68.2.199 under 'la marquaue?' (= la Margrave by print), 18 June 1712; both passes 199; eye '1yy' (both y-glyphs: 199 or 144); no gloss letter left (null slot). (2) 694/08 0502 F2-13 '1y1y' (199 or 1919) inside 714.431.73.612.237.715.199.612.89 'un merite de deux cotez' (Nov 1712; run-level M, no per-code split); the clear-text copy f.409v has **99** (s|ss|sa, M) at that place (RUN4-MANT3). | **held, no value.** Two uncertain-digit slots, one null and one inside an unsplit run whose copy reads 99; no witness assigns a meaning. M wherever it occurs. |
| 42 | l, C (Krauske f.3) | (1) Krauske. (2) **conflict**: 694/08 0314 R11 T031, 110.15.33.6.60.16.42.14.10 under 'la Couronne' (both gloss passes), 16 Sept 1712; 42 at the first n (under l: 'la courolne'); both code passes 42; R07's same word uses 14.21 for nn. (3) **support, decode context** (no gloss over the 42 itself): 694/08 0494 L07 T062 '23.42.54.51' = p-l-u-s before 'contre les Suedois' (gloss G07 placed from 23); f.410 (0511) L06 '...42.54.51.10.16.14.28.26' = '...lus contr' (same phrase); 0494 L17 T197 and f.410 M4 '...39.29.42.54' = '...mais lu[i]' after 'ne fera rien pour'. (4) not informative: 0474 R_L08 T105 (garbled run), 694/09 0015 r5, 0016 r3, 0136 r01 (low, alt 43), 0008 L11 (alt for 12). | **key 42 = l stands at C; the 0314 R11 slot is M** (as MANT-XTR graded it). One glossed slot against Krauske plus three unglossed contexts reading l: a single-slot data conflict (an enciphering slip or a second value for n), logged in HYPOTHESES.md, not settled by majority. |

Rule 3 (per-unit merge): every witness above that supports a key value sits on a leaf that cleared its own control (f.468, 0312, 0136 (a));
the two that did not (0290 r12, 0530 gloss M) are not used as support. key.tsv: **unchanged** (no held row added, no grade lowered: 321 and 199
have no value to hold, 254 collapses into 259, 191 and 259 are already M, 42's conflict is one slot). `tools/decode_key.py
ciphers/sachsstaatsarchiv-manteuffel-1712 --check` re-run after this section (nothing regenerated). The single thing that would move 191, 199,
254/259 together is the y-glyph (4|9) census per hand named by MANT-EYE63R and MANT-XTR (~$2, disk crops); recommended before any further name
code is held or keyed in this folder. No novelty class assigned or changed; no reading claimed.

## AUDIT (V-MANT16S)

Verifier V-MANT16S (Opus, account 2, LANE FAMILY-A2k), 9 Oct 2026, 18:44-18:5x UTC by `date -u`; a separate session from the solvers MANT-XTR
(0312/0314, LANE FAMILY-A2j) and MANT-0309 (session_01BJv3LLv5CgyEAymkFzuH5U); I had read none of these leaves before this job. Brief:
.claude/briefs/runs/2026-10-09-ytbiz-family-1815-jobs.md "### V-MANT16S". Claim under audit (NOTES "MANT-XTR" and "MANT-0309"): Loc. 694/08
frames 0309 (covering dispatch, stamp 240, Berlin 16 Sept 1712, 48 code tokens: C 35, M 13) and 0312 + 0314 (the "Extrait" pair it encloses,
91 code tokens: C 63, M 28) carry a period interlinear gloss; Krauske's table agrees with it past a key-shuffle p99 on every deciding row; "none
printed in Acta Borussica BO I". Both jobs are key tests, not readings: every scored span is the gloss's own text. Nothing decoded here;
key.tsv, ciphertexts and gate files untouched.

**1. Items.** SHStA Dresden 10026 Geheimes Kabinett Loc. 694/08, Manteuffel to Flemming, Berlin. 0309: covering letter (clear text per the
solver's eye: "Je joins ici les extraits de la resolution de [198 Stan:] et de la relation de [arnhold]"; four letters "de la main de [198]",
one to [Jablonski] "qui est du secret", one to [9 Ilgen]; [Razrozewski] named). 0314: the extract of Stanislas's resolution (cipher spans:
Stanislas, roi de Prusse, Pologne, roi de Suede, 'la Couronne', 'la Republique', Roy). 0312: the extract of Arnold's relation (Stanislas,
roi de Prusse/Suede, Czar, Stockholm, 'le Senat', 'le Comte Horn', Steinbock, 'Arnh:'). The cipher on all three leaves is names and short noun
phrases inside clear French; the sense is carried by the clear text.

**2. Re-derivation (rule 7).** `cd f0309_08 && python3 gloss_gate.py --check` "gate.out up to date" exit 0; `cd f0314_08 && python3
gloss_gate.py --check` (pooled 0312+0314) "gate.out up to date" exit 0. No reading.txt or decode.json exists for these leaves (no reading is
claimed); `tools/decode_key.py f0309_08|f0312_08|f0314_08 --check` stops on the leaf ciphertext.tsv layout (ValueError on the header 'pos') --
a format mismatch (these are pass/settle tables, not decode inputs), not a stale file. The gate outputs are the reproducible artefact.

**3. Design audit (rule 3).**
- *PREREG order.* PREREG-MANT0309.md: 5efeff79e (18:32:38 UTC, PREREG alone) precedes 3cc96f7b1 (18:35:38, passes, glosses, gate.out):
  verifiable. **PREREG-MANTXTR.md: not verifiable from git** -- the solver's 9a9ed332f is not an object on origin/main; PREREG, gloss passes and
  gate.out all first appear together in a768bc651 (18:23:07, "ROOM: check-in ...", a room.py rebase fold, CLAUDE.md rule 6's known flag). The
  order rests on the solver's NOTES only; the numbers re-derive exactly. Not evidence of a breach.
- *Gate.* The gloss is a period decipherment written on the leaf; key.tsv was not edited from it, so agreement tests Krauske's table against
  an independent period reading. The control (key values permuted over codes) changes the letters each code yields, so it CAN differ from the
  target on the statistic (not an orthogonal non-test). Deciding rows PASS on both blind gloss passes (0309 (a) 35/40 and 36/40 vs p99 12;
  pack (a) 38/49 and 39/49 vs p99 12-13, (n) 25/34 and 24/34 vs p99 4-6). Sound. Independence caveat carried from AUDIT (V-MANTH): Krauske
  may have compiled the table from such glosses, so agreement is a consistency check, not two independent decipherments.
- *0309 row (n)* (5/8 keyed, 3 slots of code 9 scored 0 by construction, value 'i' vs gloss 'Ilgen') is correctly reported "neither".
- *Spot check (rule 2), committed crops, my eye:* 0309 R08 c-strip reads 60.25.73.26.33.73.35.3.2y.11.71 (= ciphertext.tsv, the 2y being the
  folder's y-glyph read 29) under the gloss "Razrozewski" (I read "Razrolewski"; z/l is the gloss hand's z); 0312 A14 reads 103.284.47.16.60.21
  under "le Conte Horn" (= ciphertext.tsv). 17 tokens, 0 disagreements.

**4. Novelty search log (rule 10; families (a)-(g)).**
- (leaf) Every cipher run on the three leaves carries the period interlinear decipherment except 0309 R05b (11 80, the tail of the glossed
  'Jablonski' run), 0314 R14 (292, the Pologne code glossed elsewhere on the leaf) and 0312's title run 66.60.21.16.12.120 (its first three
  codes glossed 'Arnh:' twice on the same leaf). The plaintext of the cipher spans was written on the leaves in 1712: **KNOWN (N0)**.
- (a) **Acta Borussica, Behördenorganisation I** (1894): IA djvu (diebehrdenorgan01posngoog, 1 GET) grep Arnold 0, Stanislaus 0, Rozrazewski 0,
  Stenbock 0, Jablonski 1 (the Feb 1713 funeral sermon); Google Books search-inside ESf8fHFG9ngC: Manteuffel 20 (positive control; p.256 Nr. 72
  heading "Manteuffel an ... Flemming. Berlin 19. September, 4., 7. und 23. October 1712"), Arnold 3 (all Arnold Westenberg, Lingen),
  Stanislaus 0, Rozrazewski 0, Jablonski 1 (p.312 note, another matter). **0309/0312/0314 are not printed in BO I** (confirms the solvers).
  BO II (Akten from mid-1714) is out of date range; not searched.
- (b) **Droysen, Geschichte der preußischen Politik IV.1** (IA droysen-geschichte-der-preussischen-politik-v-4-no-1, djvu, 1 GET): p.267 and
  Anm. 511-512 print the substance -- a confidential envoy sent from Berlin to King Stanislas in Sweden in July 1712, Stanislas ready to
  abdicate, then after talking with the Swedish statesmen adding conditions; "Arnolds Schlußbericht über seine Sendung ist d. d. Berlin,
  6. September 1712"; Stanislas wanting Courland and the Silesian duchies as compensation. Manteuffel's 16 Sept letter and the extracts are not
  quoted.
- (b) **Bonnesen, Studier över August II:s utrikespolitik 1712-1715 I** (Lund 1918; Google Books GS3SAAAAMAAJ search-inside, 18 requests):
  pp.65-73 narrate the Arnold mission in detail (Benjamin Arnold, burgomaster of Lissa; Jablonski's role; Stanislas's own-hand letter to
  Arvid Horn on his negotiations with Arnold; Rozrazewski sent to Stockholm to consult the council (rådet = 'le Senat'); Horn's answer that
  Stenbock would bring the Senate's view; Arnold back in Berlin 4 Sept; "Jablonski till Ilgen, Berlin 14 sept. 1712"). The notes for these
  pages cite G.S.A. Rep. XI (Berlin); Bonnesen cites Manteuffel to Flemming from H.S.A. Loc. 3303 (13 Apr 1712) and Loc. 694 vol. 146 (23 Apr
  1713), but no snippet ties a 16 Sept 1712 Manteuffel letter or Loc. 694 vol. 145 to these pages. **SUBSTANCE printed; the leaves themselves
  unchecked beyond snippets** (page read owed: LOCAL-QUEUE L69, already open).
- (b) Berner 1901: not re-tried (djvu 500 on 9 Oct, MANT-UNG). Klopp, Sbornik RIO, the Prussian Staatsschriften: not searched.
- (e) Google Books API (country=US, key; 7 queries): "extraits de la resolution" 57 (all 20th-century, unrelated); "de la main du Roy
  Stanislas" 352 (loose, Poniatowski/Lorraine, unrelated); "qui est du secret" Jablonski 233 (loose, unrelated); Manteuffel Flemming "16
  septembre 1712" 0; Manteuffel Flemming 1712 Arnold Stanislas 0; "Rozrazewski" Manteuffel 2 (church lexica); a 7-term subject query 0.
  IA full text (be-api): "extraits de la resolution" Stanislas 10 (all 20th-century press); then HTTP 502 twice -- host stopped, the other 3
  phrase queries **unchecked**.
- (f) Solver repositories: dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers not cloned this session (prior-work UNCHECKED-NET as in the
  solvers' runs); no Manteuffel row is recorded for either in this folder's prior-work.tsv.
- (g) OpenAlex (key): "Arnold Stanislaus Leszczynski 1712 Prussia" 2 (Russian Baltic expansion 2022; Saxon-Polish union 2004 -- titles only,
  not read); "Manteuffel Flemming cipher 1712" 1 (Geheime Netzwerke im Militär 2016, unrelated). JSTOR: three rows appended to JSTOR-QUEUE.tsv,
  family (i) sender/subject AND cipher keyword, family (ii) the printed wording "Arnolds Schlußbericht" and the plaintext phrase "extraits de la
  resolution de Stanislas", no cipher keyword. Not blocking (below N3).

**5. Classification.**
| item | class | key | text | depth | safe sentence |
|---|---|---|---|---|---|
| 0309 (48 code tokens) | **N0** | `period` (the leaf's own interlinear gloss), Krauske's `published` table agreeing (gate PASS) | known (the gloss; substance printed in Droysen IV.1 p.267/Anm. 511 and Bonnesen 1918 pp.65-73) | **D1** (depth_pct 72.9, C 35 of 48) | "Manteuffel's covering letter of 16 Sept 1712 (Loc. 694/08 frame 0309) already carries a period decipherment between the lines; Krauske's 1893 table agrees with it far better than a shuffled key." |
| 0312 + 0314 (91 code tokens) | **N0** | as 0309 | known (as 0309) | **D1** (depth_pct 69.2, C 63 of 91) | "The two extracts Manteuffel enclosed on 16 Sept 1712 (Stanislas's resolution and Arnold's relation, frames 0314 and 0312) carry their own period interlinear decipherment, and Krauske's table reproduces it; the Arnold mission they concern is narrated in Droysen IV.1 and Bonnesen 1918." |
Depth reason: the cipher spans are names and short noun phrases ('la Couronne', 10 letters, the longest letter run), far below the
authentication distance (~127-138 letters, FAM-MANTV); 198 = Stanislas reads in many contexts, but only as the period gloss supplies it --
reading a period decipherment is not a code value read by us, so the code clause is not used to lift the depth. N0 is not counted either way.
Unsafe: "Manteuffel's report on the Arnold-Stanislas negotiation deciphered"; "unprinted extracts of Stanislas's resolution"; "Krauske's key
verified on the 16 Sept pack" (it agrees with the gloss; the table may derive from such glosses); any count of C tokens presented as our
reading. No SECOND-OPINIONS-QUEUE row: N0/D1 is below the N3+ D2+ trigger.

**6. Postmortem and corrections.** No over-claiming sentence found in MANT-XTR or MANT-0309 (both say "a key test, not a reading", "search
results, not novelty verdicts"); status.json carries no result for these frames. Corrections: (a) MANT-XTR's PREREG commit 9a9ed332f is not on
origin/main (folded into a768bc651) -- its pre-score order is the solver's statement only; (b) both solvers' BO I-only premise check missed the
two places the matter is printed (Droysen IV.1 p.267/Anm. 511, which V-MANTR8 had already found for 0375, and Bonnesen 1918 pp.65-73);
recorded here. (c) The leaf ciphertext.tsv files are not decode_key.py inputs; a future reading on these leaves needs a decode.json.
Requests this audit: archive.org 5 (metadata 3, djvu 2; the ROOM release line's '3' undercounts), be-api.us.archive.org 3 (200, 502, 502:
stopped), books.google.com 24 (search-inside, 2.2 s apart, all 200), www.googleapis.com 7 (200), api.openalex.org 2 (200). Vision: none (2 committed
crop pairs eyed). No 403, 429 or challenge.

## AUDIT (V-MANT0490)

Verifier V-MANT0490 (account 2, LANE FAMILY-A2k), 9 Oct 2026, 18:45-19:0x UTC by `date -u`. This is a separate session from the solver
MANT-0490 (session_01JSQGXzU4jxaXKy8aZsseiy) and from MANT-0490L. Brief: .claude/briefs/runs/2026-10-09-ytbiz-family-1815-jobs.md
"### V-MANT0490". Claim under audit (NOTES "## MANT-0490", commit eb4031655): the 0490 right page (p.392) is a key test, not a reading. Its
148 code tokens are read by two blind passes and reconciled; the gloss gate PASSes at S 61/92 keyed against a permuted p99 of 22; grades are
C 61 and M 87; key.tsv is unchanged. Scope: right page only, as committed at eb4031655. MANT-0490L's left-page and gutter work landed at
c035f5bff (18:55 UTC) while this audit ran. It adds only `_L` files and does not touch any right-page file: `gloss_gate.py --check` is still
"up to date" on origin/main. The left page is not audited here.

**1. Item.** SHStA Dresden 10026 Loc. 694/08, film frame 0490, right page, page no. 392. Manteuffel to Flemming, Berlin. Dated mid-November
1712 by its neighbours (0489 = 15 Nov, 0496 = 20 Nov; I). The clear text carries the sense around the codes, for example R10 "160 a fait le
meme sermon a 120 [gloss Dohna], qui le recut, dit-on" (my eye on crop c0490R10_L01). Every code run but two is glossed between the lines in
the period hand. The unglossed runs are R15 `10 35 2 14 288` and the R17 tail `29 35`, both M. The R01 line is a full-size line of
decipherment above R01+R02 ("la paix sans tiers, l'epee a la gloire et au profit du Roy de Prusse", per the blind gloss pass).

**2. Re-derivation (rule 7).** `python3 f0490_08/gloss_gate.py --check` gives "gate.out up to date" (exit 0) at eb4031655 and again at
origin/main after c035f5bff. The deciding row is S 61/92, control mean 14.08, p99 22, max 25, 0/1000: PASS. The reported row, which includes
the R01 line, is 96/130 against p99 32: PASS. The script's docstring still says "seed 8" and "--print ... BO I p.212". Both are leftovers
from the copied f0089_08 script. The code uses seed 490 and has no print_spans.tsv. This is cosmetic and does not change the gate.

**3. Design audit (rule 3).**
- *PREREG order: verifiable.* d7dec5c20 (18:30:21 UTC) holds only PREREG-MANT0490.md and gloss_gate.py, and it is on origin/main. Passes,
  ciphertext, spans and gate.out first appear in eb4031655 (18:34:13).
- *Control.* The control permutes key values over codes. That changes the value-to-code assignment that S measures, so the control can
  differ from the target. It is not a coverage-type non-test.
- *Reconciler bias (the main risk).* The reconciler had seen key.tsv and the glosses before settling digits (disclosed in the PREREG).
  Audit sensitivity `f0490_08/vmant0490_sens.py` -> `vmant0490_sens.out` (`--check` up to date) re-scores the deciding row using each blind
  pass's raw digits. Same statistic, key, seed 490 and 1000 draws; this is not a registered gate:
  pass A 53/90 (p99 22) PASS; pass B 58/89 (p99 22) PASS; digits where A = B only 53/84 (p99 21) PASS. **The gate does not depend on the
  reconciliation.** However, **8 of the 61 C tokens rest on digits the reconciler settled against at least one blind pass.** Most of these
  are y-shaped glyphs settled as 9 (i) by the MANT-0008 hand convention. At R11 both passes read 4; at R05 pos 2 the reconciler chose 74
  (sch) between A 77? and B 74?. These 8 C grades are therefore conditional on the y-glyph convention (MANT-YCEN's census, running in
  parallel). They should be read as C-if-9, not as independent C.
- *Spans.* Spans are placed by position, by the same key-aware worker. The per-span table in gate.out shows the misses where a span would
  have been tuned to the key (names abbreviated by the gloss: 160, 257, 150). No sign of tuning, but this cannot be excluded from the files.
- *Grades.* C counts only matched tokens in the PASSing row. The R01+R02 run (35/38) stays M because it matched only in the reported row,
  as the PREREG requires. Conservative and correct.

**4. Novelty search log (rule 10).**
- (a) **Acta Borussica, Behoerdenorganisation I** (1894). IA `diebehrdenorgan01posngoog` _djvu.txt, fetched independently (1 GET). Running
  heads give Nr. 75-81 for 1-21 Nov 1712 (administrative acts). The only Manteuffel report for November is **Nr. 82, Berlin 23 Nov 1712
  (p.285)**: ". . . Dhona a trop de complaisance pour le Prince Royal ... Ilgen ...". 0490's right page also names Dohna (120, glossed), so
  I checked the line: R10 reads "160 a fait le meme sermon a 120, qui le recut, dit-on", which is a different sentence, and no Prince Royal
  code (865, 283) occurs on the page. Nr. 82 is not this page. A footnote on Grumbkow cites an Austrian envoy, 29 Nov 1712; not this letter.
- (b)/(c) **Droysen, Geschichte der preussischen Politik IV.1** (IA `droysen-geschichte-der-preussischen-politik-v-4-no-1` djvu, 2
  requests). Manteuffel is quoted only at Anm. 32 (1706), 401 (Flemming to him, 1709), 431, 510 (a memoire to him, 1712) and 518-520 (27
  Jan to 19 Feb 1713); there is no mid-November 1712 report. **pp.268-269 ("Preussen in Mecklenburg, November 1712") print the news
  context**: Steenbock's November moves into Mecklenburg (Damgarten, Rostock, Wismar), Prussian sauvegarde companies at Guestrow and Rostock,
  and Flemming's armistice with Steenbock. Mecklenburg (288 x2, glossed 'mecklenbourg'), the King of Prussia (257) and a St- name glossed
  'tr?nbeck' (76) are on the page: **SUBSTANCE printed, wording not**. Berner 1901 was not tried (djvu 500 on 9 Oct, per MANT-0490). Not
  searched: Bonnesen 1918 for November 1712, Klopp, Sbornik RIO.
- (d) Holding archive: the frame is in the folder's own fetch manifest (mant0608/fetch_g.tsv); no edition or decipherment is noted in the
  folder for 0490 beyond MANT-CEN4's inventory row (solver's check 1, re-grepped here: same result).
- (e) IA full text (be-api): "au profit du Roy de Prusse" 0; "la paix sans tiers" 0; "Manteuffel" "Grumbkow" "Steenbock" 179 (general
  histories: Waddington, Histoire de Prusse II; Haake's August der Starke; not this letter by title, snippets not read). "fait le meme
  sermon" got HTTP 502, retried once (502), and the host was stopped: **unchecked**. Google Books API (country=US, key; 3 queries): "la paix
  sans tiers" Prusse 352 (loose: 1790-1891 French works on Prussia, unrelated by title); Manteuffel Flemming Grumbkow Steenbock 1712
  Mecklenbourg 0; "le meme sermon" Dohna 121 (loose: ecclesiastical, Macaulay; unrelated).
- (f) Solver repositories: not cloned (UNCHECKED-NET, as in the solver's prior-work run).
- (g) Scholarship: not run by API this session. JSTOR: two rows were appended to JSTOR-QUEUE.tsv. Family (i) is sender/subject AND a
  cipher keyword; family (ii) is the plaintext phrase "la paix sans tiers" with no cipher keyword. Not blocking (N0).

**5. Classification.**
| item | class | key | text | depth | safe sentence |
|---|---|---|---|---|---|
| 0490 right page (148 code tokens) | **N0** | `period` (the leaf's own interlinear decipherment), with Krauske's `published` 1893 table agreeing (gate PASS) | known (the period gloss; news context printed in Droysen IV.1 pp.268-269) | **D1** (depth_pct 41.2, C 61 of 148) | "On the right page of Manteuffel's mid-November 1712 report (SHStA Dresden Loc. 694/08, frame 0490, p.392), Krauske's 1893 table agrees with the leaf's own period interlinear decipherment at 61 of 92 glossed code tokens (permuted-key p99 22); the plaintext is the period gloss, and the news context (Steenbock in Mecklenburg, Prussian sauvegardes, November 1712) is printed in Droysen IV.1 pp.268-269." |

Depth reason: every C token is a gloss match, so the reading is the period decipherment, not ours. The longest matched stretch (G17, 11
codes) is far below the authentication distance (~127-138 letters, FAM-MANTV). The code clause is not used, for the same reason as
V-MANT16S: the gloss supplies the values. D1, "fragments read". The 8 conditional C tokens (section 3) do not change the depth.
Unsafe: "the 0490 report deciphered"; "an unprinted report on Steenbock in Mecklenburg"; "Krauske's key verified independently" (the table
may itself derive from such glosses); any C count presented as our reading; "unglossed runs read" (R15 and the R17 tail are M).
No SECOND-OPINIONS-QUEUE row: N0/D1 is below the N3+ D2+ trigger.

**6. Postmortem and corrections.** I found no over-claim in MANT-0490's NOTES section. It says "a key test, not a reading", "search
results, not novelty verdicts", and makes no novelty claim. Three corrections for the record, without editing the solver's files: (a) 8 of
the C 61 depend on reconciler-settled digits (mostly the y-glyph 4|9 convention) and are conditional on MANT-YCEN. The gate itself is robust
(53-58 on blind digits alone). (b) The gloss_gate.py docstring is stale (seed, --print). (c) The solver's BO I check was right that no
15-20 Nov report is printed; this audit adds that Nr. 82 (23 Nov), which also names Dohna, is a different passage, checked against crop
R10. Requests this audit: archive.org 3 (BO I djvu, Droysen IV.1 metadata + djvu), be-api.us.archive.org 9 (two 502s on one query, host
stopped), www.googleapis.com 3. No 403, 429 or challenge.
