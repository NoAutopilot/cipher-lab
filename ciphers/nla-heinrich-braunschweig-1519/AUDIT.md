# AUDIT -- nla-heinrich-braunschweig-1519 (NLA BU L 1 Nr. 548 and Nr. 562)

Verifier R9-NLAV, 6 Oct 2026, 05:56-06:04 UTC by `date -u`, account 2, LANE LANE-RUN9-account-2. A separate session from the
solver (R9-NLATX) and the check-solved worker (R9-NLACS). No fresh decode was made; the solver's files were read and recounted.

Claim under audit (R9-NLATX, commit c99076a0e): "the in-line cipher words of NLA BU L 1 Nr. 548 (letter to Countess Anna, 1519)
and Nr. 562 (K. Schepper, Trier 8 Aug 1522) read with the 1858/1860 archivist key sheets: 548 18/18 words agree with the sheet's
list (H 84, M 17 numbers), 562 11/12 (H 83, M 6; lant vs land)."

## 1. Verdict

| Item | Cipher tokens | H / M | Class | Key source | Depth | Status call |
|---|---|---|---|---|---|---|
| Nr. 548, f.269r, Heinrich d. J. to Countess Anna [of Holstein-Schaumburg], 1519 (18 cipher words) | 101 numbers | 84 / 17 | **N0** | archival key (Grein, 28 Feb 1860), credited; not of the time, not printed | **D2** (83.2% H) | see s.4 |
| Nr. 562, f.56, K. Schepper, Trier, 8 Aug 1522 (12 cipher words) | 89 numbers | 83 / 6 | **N0** | archival key (Grein, 2 Oct 1858), credited; not of the time, not printed | **D2** (93.3% H) | see s.4 |
| Both | 190 | 167 / 23 (87.9% H) | N0 | as above | D2 | `solved` (rule-5 vocabulary; the decipherment is Grein's, see s.4) |

N0 because rule 10's N0 is "plaintext and decipherment of this very item already known": each file carries, two leaves before
the letter, a 19th-century archivist's key table and the list of deciphered words, signed "Dr. Grein" (aufn_0002 of each file,
f.268 and f.55). Not N1: no printing of the sheets, the word lists or the cipher words was located (s.3). Precedents for a
decipherment held in the same file and not in print being N0: clair1067-brienne-poland-1646, clair1108-duvergier,
antt-fcc-costacabral-1865 (all N0).

Safe sentence: "NLA Bückeburg L 1 Nr. 548 (1519) and Nr. 562 (1522) each carry an archivist's key sheet and word list of 1858/1860
(signed Dr. Grein) in the same file; applying those keys to our transcription of the numeral groups reproduces 29 of his 30
listed words (one spelling difference, lant/land), and 166 of 167 numbers read without key knowledge agree letter for letter
with his list. The decipherment is the archive's, not ours; no printing of it was located (search log in AUDIT.md)."

Unsafe sentences: "we deciphered Heinrich's letters"; "previously unread"; "first reading"; "the letters are read" (the clear
Low German text around the cipher words has not been transcribed); "Heinrich's two letters" (Nr. 562 is Schepper's, per its own
wrapper and signature); any sentence calling the Grein key `period` or "of the time".

## 2. Circularity check (brief item a)

The reconciliation was key-aware (the reconciler had seen the sheets), so only numbers on which the blind pass and the
reconciliation agree are H; every number the reconciliation changed is M (`ciphertext_*.tsv` conf column, R9-NLATX's rule).
The blind pass's own TSV was not committed, so the H/M split could not be re-derived from raw pass output; it is taken from the
committed conf column and is consistent with R9-NLATX's own statement of the raw blind result (7/18 and 7/12 words exact before
reconciliation; the zero-M words below are exactly those words). Recount by this verifier (script in s.6, against
`grein_words.tsv`, letter by letter, u/v folded):

| Letter | H numbers whose key letter = Grein's letter | M numbers that agree | Words with 0 M tokens that agree | All words that agree |
|---|---|---|---|---|
| 548 | 84 / 84 | 17 / 17 | 7 / 7 | 18 / 18 |
| 562 | 82 / 83 (the t of lant) | 6 / 6 | 6 / 7 (lant) | 11 / 12 |
| Both | **166 / 167 (99.4%)** | 23 / 23 | **13 / 14** | 29 / 30 |

Matched control (rule 3; can vary on the statistic, since it changes which letter each number maps to): the same H numbers keyed
with a random permutation of each sheet's own letter set, 2,000 permutations per letter: agreement with Grein's list mean 0.056 /
p95 0.238 / max 0.452 (548) and 0.062 / 0.241 / 0.554 (562), against 1.000 and 0.988 for the sheet key. So:
- The headline "18/18 and 11/12 words" **is** partly driven by M tokens: 11 of 548's 18 words and 5 of 562's 12 contain at least
  one M number, and all 23 M numbers were settled toward the list. On H tokens alone the agreement is 166/167 letters and 13/14
  whole words. The headline is to be quoted with that split, never alone.
- What the agreement tests: that our transcription of the numbers matches what Grein read (an independent reading of the same
  manuscript, 1858/1860). It does not test Grein's key against an outside witness: our "decode" and his list share his key.
  The external evidence that his key is right is that it turns every group into a Low German word (fulmechtig, vorlatinge,
  landtschop, regimentes) and is a 20-letter monoalphabetic table with no free parameter fitted by us.
- The M tokens are not independent evidence of anything; they are graded M and stay M.

## 3. Search log (brief item e; extends R9-NLACS's 8 queries)

Solver-side log: R9-NLACS (6 Oct 2026, 8 queries, NOTES.md "Web and blog check (R9-NLACS)"), GF-A2-7 (2 Oct, blogs), GAPS125
(Havemann vol. 2, 1855, full grep), GAPS129 (Stanelle 1982 index; Wallstein 2025 contents), csDA2 (1837-38 Lüneburg work).
This verifier, 6 Oct 2026, 05:58-06:01 UTC:

| Family | Query | Result |
|---|---|---|
| Google Books API, key, `country=US` | positive control `"Hildesheimer Stiftsfehde"` | 523 items (control works: Stanelle 1982, Wallstein 2025, 1887 reformation histories) |
| same | `"Gräfin Anna" Schaumburg Heinrich Braunschweig 1519` | 1 item, a coin catalogue; no hit |
| same | `Schepper Trier 1522 Heinrich Braunschweig Regiment` | 0 |
| same | `"Grein" Bückeburg Archiv Geheimschrift` | 0 |
| same | `"Grein" "Archiv zu Bückeburg"` | 1, Kurhessisches Staatshandbuch 1864 (archive staff list); no hit on the letters |
| same | `vorlatinge regimentes landtschop` (decoded words, phrase search on the decode) | 0 |
| same | `"Heinrich der Jüngere" Chiffren Schaumburg` | 33, all newspaper/trade noise; no hit |
| same | `Anna von Schaumburg Heinrich Wolfenbüttel Gevatterin 1519` | 0 |
| IA full text (be-api) | positive control `"Hildesheimer Stiftsfehde"` | hits incl. `zhv1919` (Zeitschrift des Historischen Vereins für Niedersachsen 1919, Varnhagen on Brandis/Oldecop) -- **so the index does cover at least one ZHVN volume, correcting R9-NLACS's note that it does not** |
| same | `"vorlatinge"` | 6+ hits, all Schleswig-Holstein / Paderborn charters (the word is ordinary Low German); none these letters |
| same | `"Grein" AND "Bückeburg" AND "Geheimschrift"` | Grein's Anglo-Saxon Bibliothek volumes and unrelated items; no hit |
| same | `"Geheimschrift" AND "Bückeburg"`; `"Gräfin Anna" AND "Schauenburg" AND "Heinrich" AND "1519"`; `"Schepper" AND "Bückeburg"`; `"Chiffren" AND "Schaumburg" AND "Heinrich" AND "Braunschweig"`; `"Schepper" AND "Trier" AND "1522" AND "Regiments"`; `"lant" AND "landtschop" AND "regimente"` | no hit about either letter (the endpoint's AND handling is loose: many hits match only common words; weak negative) |
| OpenAlex (key, header) | control `Hildesheimer Stiftsfehde` | 27 works (control works) |
| same | `Grein Bückeburg Archiv`; `Heinrich Braunschweig Anna Schaumburg 1519`; `Schaumburg Geheimschrift Heinrich Braunschweig` | 1 / 12 / 0, none about the letters |
| Semantic Scholar (key) | two queries | HTTP 429 twice (one retry after a 20 s pause); host stopped. **Unreachable** this pass |
| JSTOR | not queued (budget); a phrase row (`"vorlatinge des regimentes"`, `"Gräfin Anna" Schauenburg 1519`) is the named next step for an N1/N2 check, never blocking N0 | not searched |
| Schaumburg-Lippische Mitteilungen, Schaumburger Heimatblätter, Braunschweigisches Jahrbuch, Grein's archival reports, Koldewey 1883, Heinrich d. J. biographies (beyond Havemann/Stanelle) | not reached (print-only or not full-text indexed) | unreachable this pass; a printing there is not excluded |

Nothing in this log can lower the class below N0, and nothing found raises a question of print (N1). The unsearched families
matter only for F-grading if a print is found later.

## 4. Status call (brief item c)

Not `found-solved`. In this repository found-solved (README "Found-solved is not garbage", F0-F2) is defined by a print or a
specialist edition/database that already links the item; none was located. The decipherment of these very items is in the same
archival file (N0), and the repository's precedent for that case (clair1067, clair1108, antt-fcc-costacabral-1865 AUDIT.md "`solved`,
not found-solved") is status `solved` with class N0: the reading exists and is reproducible (`tools/decode_key.py --check`,
`compare_grein.py --check`), and N0 already records that the decipherment was on file. The status word records the item's
state; the decipherment is Grein's (1858/1860), and no sentence may say this project deciphered it.

Scope of the call: the target is the two shelfmarks. Nr. 548's filmed images are f.267-270 consecutive (wrapper, key sheet,
letter recto, verso), so Grein's second word list ("an den Drosten") belongs to a letter outside f.267-270 -- elsewhere in
I Ca 30 Bd. 1 or not filmed under this signature; it is a pointer, not a gap in this target. The clear Low German text of both
letters is untranscribed; that limits depth (s.5), not the cipher reading.

## 5. Depth (brief item d, rule 4a)

Cipher tokens = the 190 numbers of the 30 cipher words (clear text is not cipher). H 167, M 23, C/S/I 0: **87.9% H**
(548 83.2%, 562 93.3%). Unread: none; residue is M only.

**D2, not D3.** For D2: each letter's cipher stream (101 and 89 letters) is read with a key with no parameter fitted by us, well
above any authentication distance, and the readings fit together: 562's words are regimente / regimentes (x3), vorlatinge,
vorlassinge, sonen, sone, landtschop, lant, landen, luden -- a coherent subject, matching the archivist's wrapper. Not D3: the
cipher words are scattered single words inside clear text that has not been transcribed, so no word has yet been read in its
sentence; the only external check (Grein's list) shares the key and checks our transcription, not the key; and 548 alone is
83.2% H with 17 M. D3 is open once the clear text is transcribed and each cipher word is read in context.

Verifier's sentence (depth_sentence): "In the 1522 Trier letter the enciphered words concern the 'regimente' (government), its
'vorlatinge'/'vorlassinge' (relinquishing), 'sonen' (sons) and the 'landtschop' (estates of the land), the matter the archive's
wrapper summarises as the duke's intentions about resuming the government."

`tools/depth_check.py` output pasted in NOTES.md (R9-NLAV section).

## 6. Postmortem and corrections

- Failure: none in the reading. The over-claim risk was the headline "18/18, 11/12" quoted without its H/M split; with H only it
  is 166/167 letters and 13/14 words (s.2). Corrected in NOTES.md's R9-NLAV section and in the status.json row.
- Key source: the brief and R9-NLACS call Grein's sheet a "period key". It is not of the time (1519/1522); it is a 19th-century
  archivist's decipherment -- someone else's key, credited, unprinted. H grades stand (rule 4: "read from a key source"); the
  status.json `key` field reads `archival` with that explanation, not `period`.
- R9-NLACS's line "the IA full-text index does not cover the Zeitschrift des Historischen Vereins für Niedersachsen" is wrong
  for at least the 1919 volume (`zhv1919`); corrected here, not in R9-NLACS's section (left as written, dated).
- Nr. 562 is Schepper's letter (wrapper, signature), not Heinrich's; the folder title "Two enciphered letters of Heinrich der
  Jüngere" over-states it. Noted in NOTES.md.
- Grein's 1860 date vs his 1856-59 Bückeburg tenure (R9-NLACS) stays M, unresolved.
- No SECOND-OPINIONS-QUEUE row: class N0 (rule: rows only at N3+).

Recount script (scratch, not committed; reproducible from the committed TSVs): per group, zip the decoded letters
(`reading_tokens_<n>.tsv` value, grade) with `grein_words.tsv`'s word, u/v folded; control = 2,000 random permutations of the
sheet's letter set over the same numbers, H tokens only.

Requests: www.googleapis.com 8 (all 200), be-api.us.archive.org 9 (all 200), api.openalex.org 4 (200),
api.semanticscholar.org 2 (429, 429; stopped).
