# AUDIT -- colbert26-lathuillerie-1644 (f.23 reading, f.24 as it shares the folder's decode)

## AUDIT 1 (verifier DA1-COLV, account 1, LANE DEFAULT-account-1-20261007-1440, 7 Oct 2026, 16:10-16:4x UTC by date -u)

Separate session from every solver of this folder (KX-, A2-COL1-17, A4-RFCOL/COLALN, R7A/R8/R9/R10-COL26*, D22-COL26P, D07-COL26K,
DA1-COL, DA1-COL2, DA1-COL3). Brief: `.claude/briefs/runs/2026-10-07-account1-default-1440-jobs.md` job DA1-COLV.

Claim under audit (NOTES.md, Remaining gaps, after DA1-COL3): "Read so far: 27 of 168 f.24 tokens and 141 of 306 f.23 tokens at grade
C ... DA1-COL3 raised 30 = s and 85 = na to C, 123 -> 141."

### 1. Items

| Item | Leaf | Date, place | Sender -> recipient | Cipher | Period decipherment on the leaf |
|---|---|---|---|---|---|
| f.23 | Mel. Colbert 26, fol. 23 (Gallica btv1b10035069t, canvas 26) | "17e Mars 1646" | unclear; salutation "Mon Nepveu" (leaves.tsv) | two-digit nomenclator, 306 tokens in 42 glossed runs | yes: a second hand's interlinear gloss over every run (interlinear/f23_reconciled.tsv) |
| f.24 | fol. 24 (canvas 27) | 1646 | La Thuillerie -> Servien (leaves.tsv) | mixed letters/digits, 168 tokens, 11 runs | yes: interlinear gloss (interlinear/f24_reconciled.tsv) |

Distinctive content (from the period gloss, not from our key): f.23 -- "la charge de Surintendance des bastimens", "pour la charge de
M de Brienne", "Il vous cognoistroit et que vous le supplanteriez", "vous ferez un peu mieux cette charge que luy", "nomme M de la Court
pour lemploy d'Oznabrug", "a Mad de Sauoye", "auec M de Prefontaines"; f.24 -- "le Comte de Trautmandorff a fait faire les expeditions
de l'Erection en Duche et Principaute de l'Empire du Comte de Meurs a M le P d'Orange ... relever sa maison par un titre de cette sorte".

### 2. Rule 7 re-derivation

`python3 tools/decode_key.py ciphers/colbert26-lathuillerie-1644 --check` at start (key as DA1-COL3 left it, b1d35d3c1): "reading up to
date", exit 0; f.23 C 141, M 164, U 1; f.24 C 27, M 140, U 1. Not stale.

### 3. Today's key changes against their registrations

Git order: word_da1.py (eff0df6fd 14:53) before word_pairs_da1.tsv / word_da1_out.txt (9c9dce471 15:01); PREREG-DA1-COL2.md and
word_col2.py (79c0bd7a8 15:21) before word_pairs_col2.tsv (f993b1f26 15:23) and word_col2_out.txt (996b3a2d4 15:24); PREREG-DA1-COL3.md
and word_col3.py (daed123cf 15:44) before the pairs and output (b1d35d3c1 15:48). The only post-registration change to word_col3.py is
the label string of the output TSV's source column (checked by diff). Registered before scoring: yes, all three.

Control: Control W permutes gloss words over word spans within a canvas; the hit statistic depends on which word sits over which code run,
so the control can differ from the target (rule 3) -- accepted. Per-unit instrument check (Szembek rule): applied in all three runs;
c62 failed its own instrument in DA1-COL3 and was correctly left unscored. Bonferroni within each run: applied.

What the registrations did not cover, and this audit tested (PREREG-DA1-COLV.md, siblings/verify_colv.py, pushed 2bf34f181 before it was
run; output siblings/verify_colv_out.txt, DA1-COL2's reader in siblings/verify_colv_col2_out.txt):

(a) **In-sample value choice.** Every value tested today came from key_f23_anchor_r10.tsv, which R10-COL26B chose by span containment
on the 14 cleared units; DA1-COL scored on c3940/c47/c50 and DA1-COL3 on c54-56/c63, which are, code by code, mostly the same units the
value was chosen from (DA1-COL3 registered this as caveat 7 but its merge rule did not act on it). Splitting each code's occurrences into
the R10 value-choice units (IN) and the others (OUT), same statistic and control, gate on OUT P < 0.05/7:

```
code value  OUT N  OUT H  ctrl mean  P (DA1-COL reader)  P (DA1-COL2 reader)  verdict
16   se     19     5      0.74       0.0007              0.0004               keep C
20   i      7      3      0.90       0.0417              0.0430               -> M
67   leur   7      2      0.07       0.0012              0.0005               OUT passes; see (b)
81   me     8      3      0.22       0.0003              0.0002               OUT passes; see (b)
96   que    10     0      0.34       1.0000              0.3228               -> M (c50 0/6)
30   s      23     8      3.36       0.0129              0.0038               -> M (reader-dependent)
85   na     4      1      0.03       0.0301              0.0297               -> M
```

96 = que reads 0 of 10 outside the units its value was picked from; 85 = na's held-out PASS rested on "Naples" written twice with the same
three groups (85 25 76) on c56, which is one of the three units R10-COL26B took "na" from; outside them 85 reads 1 of 4.

(b) **Conflict with f.23's own gloss (rule 4).** DA1-COL held 31 = t as a two-witness conflict; the same shape was not applied to 85, 81,
67 or 96. On f.23 itself (interlinear/f23w_align.tsv): the gloss writes **luy** over code 85 standing alone (P16w052, "...que luy"; the
sign itself is disputed 85/86 in f23_reconciled P16), **il** over code 81 standing alone (P22w072, "Il y ira"), puts 67 in the chunk
"uasi" of "quasi" (P25w083, 48 67) and 96 inside "ordres" (P42w116). Applying a sibling value to f.23 tokens whose own gloss says
otherwise wrote "que na" where the leaf reads "que luy". These are data conflicts, graded M, not settled by count; the 1646 leaf and the
1648 siblings may simply use different editions of the nomenclator.

**Key changes made by this audit** (key_f23.tsv; each row's note names this audit): 20 i C->M; 30 s C->M; 67 leur C->M; 96 que C->M;
81 me C->M with the value restored to **il** (f.23's own single-segment gloss); 85 na C->M with the value restored to **luy** (same).
16 = se stays C (OUT 5/19, P 0.0007; it does not occur on f.23). 46 ce (M, DA1-COL2) and 31 (held, M) unchanged. The sibling values
(me, na, leur, que, s, i) are leads for the sibling-leaf key, not refuted.

Reading regenerated: `tools/decode_key.py ... --check`: reading up to date, exit 0. **f.23 C 141 -> 110 of 306** (M 164 -> 195);
f.24 unchanged (C 27 of 168). Judge (rule 7), spec specs/colbert26-lathuillerie-1644.json:

```
FAIL language: score=-1.401, null_p99=-1.888, real_p05=-0.873, real_median=-0.785, mode=both, N=690
ok   words: cover=0.735, min=0.4, real_text_median_cover=0.945
FAIL - colbert26-lathuillerie-1644 (a PASS is a gate for a verifier, not a reading; rule 10)
```

### 4. Grades and depth (rule 4, 4a)

| Item | H | C | S | M | I | U | % C | longest C stretch |
|---|---|---|---|---|---|---|---|---|
| f.23 | 0 | 110 | 0 | 195 | 0 | 1 | 35.9 | 10 letters, broken by M tokens (P25) |
| f.24 | 0 | 27 | 0 | 140 | 0 | 1 | 16.1 | -- |

No H (no key sheet) and no S: the C grades are known plaintext from the leaves' own period glosses, applied back to the same leaves, so
the reading is a key-to-known-text alignment, not a cryptanalytic result. No clause reads from the key alone above the authentication
distance; the content is known only because the gloss writes it. **Depth D1 for both leaves** ("fragments read"); the gloss, not our
key, carries the text. `tools/depth_check.py` run after the status.json row was added (section 7).

### 5. Novelty search (rule 10)

Already logged by the folder (KX-COLB26P1, GF-A2-3): Le Clerc, *Negociations secretes*, vols 1-4 (IA full text grepped); APW database;
Tomokiyo's pages; DECODE catalogue crawl; both solver repositories; web search; BnF finding aid cc955062 (no cipher mentioned). Added by
this audit (7 Oct 2026):

- **APW** (apw.digitale-sammlungen.de/search/query.html, descriptive UA, 8 requests, stopped after two 502s): "supplanteriez" 0;
  "Surintendance des bastimens" 0 (after one 504); "supplanter Brienne" 0; "tresbien icy" 2 unrelated 1647 documents (APW II B 5,2
  nos. 227, 295); "Trautmansdorff Meurs" 1: APW II B 4 no. 29, memorandum of Longueville, d'Avaux and Servien to Louis XIV, Munster 25 June
  1646, reports in its own cipher (|: :|) that Trautmansdorff promised to erect the county of Meurs -- **the same affair as f.24's gloss is
  in print in a different document; f.24 itself is not printed there.** "comte de Meurs" and a La Court/Osnabruck query returned 502, not
  retried (good-citizen rule).
- **Phrase search in print**: `tools/print_check.py` on 10 gloss clauses (phrases.txt) against Le Clerc vols 1-4 (sources.tsv), IA
  full text, HathiTrust EF, Google Books (key, country=US), OpenAlex, CrossRef -- result in section 5a.
- **Open-index scholarship** (OpenAlex with key; Semantic Scholar with key): "Coignet de La Thuillerie" 13 works, "La Thuillerie Servien
  1648" 5, "Servien Lionne 1646" 52 -- titles read, none about this volume or a decipherment; two studies of the French embassy's
  personal networks (A. Tischer 2015, doi 10.1524/9783486835441-005; A. Schirrmeister 2025, doi 10.1515/9783111389325-011) may cite
  Servien's private correspondence and were not read in full. Semantic Scholar "La Thuillerie cipher": no relevant hit in the top 5.
- **JSTOR**: four rows appended to JSTOR-QUEUE.tsv for the owner's runner, family (i) names+cipher keyword (2 rows) and family (ii)
  bare quoted gloss phrases (2 rows); queued, not blocking.
- Not searched: Danish/Swedish mediation editions (GF-A2-3 premise (d)); Lionne's or Servien's family papers in print beyond APW.

### 5a. print_check result

`tools/print_check.py` finished 16:3x UTC (print-check.tsv, print-check-hosts.tsv; requests: archive.org 2, be-api 20, googleapis 10,
OpenAlex 10, Semantic Scholar 7, CrossRef 10). 10 phrases x 4 listed sources + global hosts, 90 rows. Le Clerc vols 2-4 (cached djvu text):
no hit for any phrase; vol 1: djvu 500, be-api fts no hits for 7 phrases, 3 not searched (502). IA global full text: 4 phrases not
searched (502), the rest no hits. Google Books: the high counts (333-348 volumes) are loose word matches, not the phrase (top titles are
Francois de Sales, Bible, dictionaries); the one narrow result is "erection en duche et principaute de l'empire du comte de meurs" -> 6
volumes, all Groen van Prinsterer, *Archives ou correspondance inedite de la maison d'Orange-Nassau* (1859) -- the Orange side of the
Meurs affair is in print there; whether it prints this La Thuillerie letter was not checked (snippet only; next verifier step, an IA
full-text read of that series volume for "Meurs" 1646). Semantic Scholar: 4 phrases blocked by 429; the others matched nothing relevant.
OpenAlex/CrossRef: no relevant record. None of these alters N0: the decipherment of each item is on the leaf itself.

### 6. Classification

| Item | Class | Key | Text | Safe sentence |
|---|---|---|---|---|
| f.23 | **N0** | period (rebuilt by us from the leaf's own interlinear gloss) | known (manuscript gloss on the leaf; not located in print) | "The cipher on Mel. Colbert 26 f.23 carries a contemporary interlinear decipherment; we rebuilt part of its nomenclator from that gloss (110 of 306 tokens at grade C) -- fragments, not a decipherment." |
| f.24 | **N0** | period (same) | known (same) | "The f.24 cipher's own interlinear gloss gives a partial key (27 of 168 tokens at C); its subject, the erection of Meurs for the Prince of Orange, is in print in APW II B 4 no. 29." |

Evidence quality: the plaintext of both items is the period decipherment written on the leaf (N0: decipherment of this very item already
known), so no novelty claim of any kind is open. Confidence high for N0. Unsafe sentences: "deciphered", "first reading of the La
Thuillerie cipher", "unpublished letter decoded", "141 of 306 tokens read" (superseded by this audit: 110).

### 7. Postmortem

Failure: today's three solver runs promoted seven codes on positional tests whose scored canvases were mostly the same units the values
were picked from, and replaced f.23's own single-segment gloss values (luy, il) with sibling values without applying the rule-4 conflict
test they applied to 31. Corrected: key_f23.tsv (six rows), reading_f23.txt / reading_tokens_f23.tsv regenerated, NOTES.md Remaining
gaps count 141 -> 110 and a DA1-COLV section. No AUDIT.md or SECOND-OPINIONS-QUEUE.tsv row existed before, so nothing else to propagate;
N0 needs no second-opinion row. A brief or registration for a sibling-key merge should split IN/OUT value-choice units and check the
leaf's own gloss for conflict before C (proposed as a one-line NOTES suggestion, not applied to briefs here).
