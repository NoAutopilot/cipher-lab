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
