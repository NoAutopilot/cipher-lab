# AUDIT -- szembek-bk1560 (PAN Biblioteka Kórnicka BK 1560-1, ff.65-67, "List zaszyfrowany")

Verifier: V8-SZEM (LANE V8 job 2), 26 Sept 2026, 06:18-06:40 UTC (clock read). Not the solver (LANE B7: bSZEM,
bSZL65/66/67, bSZM, bSZR, bLAJ); does not protect its conclusions. No decoding, alignment or key change was done.

**Claim under audit** (bSZM 05:32, B7 05:49, bSZR 05:55): all three leaves read at grade C from the manuscript's own
period interlinear gloss (letter-per-code key, `tools/interlinear_align.py --floor 100`; pooled consistency 0.878 vs
shuffle p95 0.204); 434 tokens C 384 / M 50; rule-7 re-derivation exit 0, 0 diffs; la18 judge FAIL narrow; "Pergenbeio"
0 hits in print.

## 1. Verdict

| Part | Tokens | Class | Key | Text in print | Confidence |
|---|---|---|---|---|---|
| A. Code tokens aligned letter-for-letter to the gloss written over their own line (`align.tsv` status agrees 337, conflict 41, single 3) | 381 | **N0** | `period` | no printing located (section 4) | high |
| B. Code tokens on the tail or head of a word that wraps across a line end, where the gloss word is written once, over the other half (`align.tsv` null-or-unaligned 43, plus 10 `doubtful` tokens such as `21=`/`46=` at line ends): letter supplied by our pooled key, word supplied by the gloss on the adjacent line (e.g. 65:8-9 "rec|tam", 66:11-12 "re|duxit", 67:12-13 "su|mat", 67:17-18 "Hono|rarii") | 53 | **N0** | `period` (rebuilt by us from the gloss, applied by us across the line break) | no printing located | high on the word, medium on the individual letter |

**Whole item: N0, key `period`, text not in print (no `text: known`).** N0 = "plaintext and decipherment of this very
item already known": a contemporary hand has written the plaintext word over every cipher word on all three leaves.
Every code run in the reading lies inside a word the gloss spells out; no code word was found that the gloss leaves
entirely unread (the six lines with no gloss of their own, 66:5, 66:12, 66:20, 67:7, 67:13, 67:18, carry only the wrapped
halves of words glossed on the neighbouring line). Our contribution is a transcription of cipher and gloss, the 22-sign
letter key rebuilt from the gloss (a letter substitution, not a nomenclator, with clear letters and words mixed in),
and a reproducible reading -- the same shape as the precedents antt-fcc-costacabral-1865, clair1067-brienne-poland-1646
and rah-canada-1869 (N0 from the leaf, `period`, `solved`), and unlike clair349-este-guise-1556 (N0 with the text also in
print).

**On the brief's 14/52/15 per cent "glossed" figures.** Those are the share of code tokens carrying a `gloss_above`
entry in the three `groups.tsv` files, where each transcriber attached a gloss word only to the first code of the run it
sits over (bSZL65's own caveat). They measure a transcription convention, not how much of the cipher the gloss covers.
Measured from `align.tsv` instead: 381 of 434 code tokens (88%) align to a gloss letter on their own line; the other 53
(12%) are cross-line word halves (part B). No part of the reading is "filled by the pooled key where the gloss is blank"
in the sense of a word the period decipherer did not read.

## 2. Grade check (rule 4)

- Part A at **C** is right: the gloss is known plaintext for the very token it sits over.
- Part B at **C** is acceptable and is kept: the word is known plaintext from the gloss; only the letter-to-code split
  across the line break comes from the pooled key, which is itself built only from the gloss (no cryptanalysis). It is
  **not H**: no key sheet or cipher book exists, only a decipherment, and rule 4's H is "read from a key source".
  `decode.json`'s own note ("C = code's meaning from the gloss at that occurrence or a consistent gloss elsewhere")
  matches this. The 50 M tokens (46 per-occurrence conflicts plus B7's downgrade of thin codes 19, 24, 48) are the right
  place for doubt and stay M.
- Counts on disk are current: `decode_key.py --check` C 384 / M 50 (bSZR). The Merge section's "C 388, M 46" and the
  spec's `cheap_test_done` grades are stale (written before B7's 05:50 downgrade); corrected in NOTES.md by pointer.
- Caveat for anyone quoting the reading: `reading.txt` renders code letters and clear words as transcribed, and several
  stretches are not yet clean Latin (65:3 "c e q u / i UIJ RISSIMAM DNAONEM", 65:10-11 "p r o c E: e i t u s",
  66:18-20 "?IT u i 4?: ... EVEHS?", 67:20-21). These are transcription or gloss-legibility questions on the clear text and
  line ends, not key questions; the gloss itself is the authority there, and the readable text is the gloss's.

## 3. What the letter is (inferred from the reading, grade I -- not established)

- Form: a **postscript** ("P. S." at 65:1) in Latin, cipher words mixed with clear text; writer speaks as "nos"/"ego" and
  refers to "Celsissimus Princeps" (his master, in the third person) sending greetings to the addressee's
  "[Illu]strissimam Dominationem" (65:3, as transcribed).
- Subject: complaint against an "impostor et detractor ille ... Burgundus", named in the gloss "antidius Danod", with his
  accomplice, "perfido ac proditore", who afflicted "the fatherland" and misled "the late prince of pious memory" and
  "Serbanum" (66:9-11); vain promises from "that court" to the late prince; appeal to divine vengeance ("Deus
  justissimus ... vindictam sumat"); the fate of one "Pergenbeius" (67:14, 67:19), killed through a false friend's fraud,
  his head sent "in rem honorarii"; his associate named in the gloss "Sityk"/"Sityor".
- "Serbanum" with "defunctum principem" points to a Wallachian or Moldavian court (Șerban Cantacuzino, Prince of
  Wallachia 1678-1688, is the obvious candidate) and so to the Brâncoveanu-era correspondence with Poland, after 1688; the
  bound volume is "Akta do panowania Augusta II" (1697-1733), part of Jan Szembek's archive. Sender, recipient, place and
  date are **not** identified; this paragraph is an inference for the next searcher, not a finding.

## 4. Search log (task 2), 26 Sept 2026

| Family | Searched / unreachable | What | Result |
|---|---|---|---|
| (a) canonical series / sender's edition | partly | Romanian document editions: Giurescu, *Documente și regeste privitoare la Constantin Brâncoveanu* (IA `giurescu-constantin-c.-documente-si-regeste-privitoare-la-constantin-brancoveanu_202510`), be-api full-text for Serbanum, Burgundus, detractor, impostor, Szembek | Serbanum 1 (a different document: "antecessorem tuum Voiuodam Serbanum ... Imperialis noster Tesaurus"), the others 0. **Hurmuzaki (*Documente privitoare la istoria românilor*) and Veress (*Documente privitoare la istoria Ardealului, Moldovei și Țării Românești*) were not searched volume by volume** -- the next check if the letter's text matters (section 6) |
| (b) Szembek / Polish chancery editions, Kórnik catalogue | partly | Google Books: "Szembek" + "List zaszyfrowany"; "Katalog rękopisów Biblioteki Kórnickiej" + 1560; "Akta do panowania Augusta II"; Brancovanus Szembek cyfra | 0, 0, 7 (Jagiellonian and microfilm catalogues, a different "Akta" series), 0. The printed Kórnik manuscript catalogue itself was not opened (not on IA/Google full view from here) |
| (c) period Latin corpus on disk | searched | `tools/data/la18` (Załuski, *Epistolarum historico-familiarium* t.1-3, 1709-11), grep for serban, pergenb, "impostor et detractor", "grato animo tam", "debita veneratur", "vindictam sumat", danod, sityk, brancovan | all 0 (burgund 6, garrulitate 2 -- isolated words, not this letter) |
| (d) holding archive | not re-fetched | WBC record 343124 (catalogue metadata as read by bSZEM today); OAI-PMH not retried (JS challenge once, per brief) | record describes the item only as "List zaszyfrowany", 18th c., Latin; no transcription or decipherment attached |
| (e) IA, Google Books full text | searched | `tools/print_check.py` (25 phrases: bSZM's 10 plus 14 clear-text phrases written en clair on the leaf, which any edition would carry verbatim, plus 1 control), ia-global + gbooks + openalex + crossref; extra be-api calls for "Serbanum reduxit", "impostor et detractor", "garrulitate in mundo", "caput in rem" honorarii, Pergenbei* | all 14 clear-text phrases 0 on ia-global and 0 on Google Books except "perfido ac proditore" (biblical commentaries, unrelated); Pergenbeio 0 everywhere; extra calls 0 |
| positive control | searched | "Ablegatum nostrum extraordinarium", a phrase of Załuski t.1 (IA `bub_gb_RMM33dayMRYC`) | found by the global runs (21 IA items, Google Books 300) but **not in the Załuski volume itself under that spelling** (0 with `identifier=`); found there only under its OCR spelling "nofirum" (3 items incl. `bub_gb_RMM33dayMRYC`). So IA full text misses 18th-century prints set with long s unless the phrase is spelled as the OCR reads it: a 0 on an early-modern print is weak; a 0 on a 19th/20th-century edition (Hurmuzaki, Giurescu) is a real negative |
| (f) solver repos, blogs | searched | Bourdeau `CATALOGUE.md` (raw file, today): #348 "length and system not yet checked. No reading found"; Aymeloglu repo: bSZEM's same-day grep of a fresh clone (szembek, kornick, 343124: 0), not repeated; Tomokiyo on disk (`sources/cryptiana/`) | Tomokiyo mentions Jan Szembek only as the recipient of von der Goltz's reports (`web/german.htm`), a different correspondence; no entry for this item |
| (g) scholarship | searched | OpenAlex (Bearer key): "Szembek cipher" 4, "Szembek szyfr" 2 (interwar Jan Szembek, unrelated), "Brancoveanu Szembek correspondence" 0, "Biblioteka Kórnicka szyfr" 0; Semantic Scholar (key): "Szembek cipher letter" generic crypto only, one Brâncoveanu query returned no result object; CrossRef "Szembek szyfr" 24 (name records, "Szyfr Stanisława Lubienieckiego", unrelated); CrossRef 429 after 13 calls in print_check, not retried | nothing on this item |
| JSTOR | queued | 2 rows appended to `JSTOR-QUEUE.tsv` (Szembek + cipher + Kórnik; Brâncoveanu/Serban + impostor/detractor + Burgundus) | pending; cannot move an N0 |
| Polona | unreachable | `polona.pl/api/entities/?query=` 404 (one call; the API route has changed) | not searched |

Requests per host: be-api.us.archive.org 25 (print_check) + 17; www.googleapis.com 25 + 7; api.openalex.org 25 + 4;
api.crossref.org 13 (429) + 1; api.semanticscholar.org 2; raw.githubusercontent.com 1; polona.pl 1; wbc.poznan.pl 0.

## 5. Classification detail (rule 10)

- Prior plaintext: **yes, on the leaf** (contemporary interlinear gloss over every cipher word, ff.65-67); in print: not
  located (section 4).
- Prior decipherment: **yes, the gloss itself.**
- Evidence quality: strong -- the gloss letters agree with a single letter key at 0.878 pooled vs shuffle p95 0.204
  (bSZM), and bSZR's 10/10 image spot-check matched the gloss.
- Key source: `period` (rebuilt by us from a decipherment of the time on the leaf). Nothing in the reading is `ours` in
  the sense of a cryptanalytic key.
- **Safe sentence:** "BK 1560-1 ff.65-67 carries a contemporary interlinear decipherment over its cipher; we transcribed
  cipher and gloss and rebuilt from the gloss the 22-sign letter key, which regenerates the gloss's reading (434 code
  tokens, C 384 / M 50; key: period). No printing of the letter was located in the sources logged in AUDIT.md; class N0."
- **Unsafe sentences:** "we deciphered / cracked the Szembek cipher"; "first decipherment", "previously unread",
  "unpublished letter", "newly recovered"; "no prior decipherment exists" (the leaf itself carries one); any sentence
  naming sender, recipient or date as established.

## 6. Postmortem and corrections

Failure: none in the reading. Two over-claims in wording: NOTES.md's bSZEM paragraph says "No prior decipherment ...
found anywhere searched" and "consistent with nobody having opened the image before" while the leaf itself carries a
period decipherment (the sentence was written before the gloss was recognised as complete, and the second clause is a
guess about other people); and the header's "decoded at grade C" read as if the reading were ours rather than the
gloss's. Both corrected in NOTES.md (header and a pointer under bSZEM's paragraph; the solver's sections are otherwise
left as written). Status: `solved` is supported (section 1; by the costa-cabral/clair1067/rah-canada precedent a leaf
carrying its own plaintext with nothing in print is `solved`, not `found-solved`, which in this repository means a print
or someone else's decipherment the lane did not know of). The brief offered found-solved for this case; the precedent is
followed and the divergence is flagged to LANE V8.

Next step (one line, not run): if the letter's text is wanted for outreach, a Sonnet search of the Hurmuzaki and Veress
volumes on IA for the clear-text phrases in `phrases.txt`, and a look-up of BK 1560 in the printed *Katalog rękopisów
Biblioteki Kórnickiej*; neither can move the class from N0, only set `text: known`.
