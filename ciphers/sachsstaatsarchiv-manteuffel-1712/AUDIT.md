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
