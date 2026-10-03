# AUDIT: na-suriname-map-1781 (NA 4.VEL Suriname fortification maps in cipher, Wollant 1781-82)

Verifier: VERIFY-SURINAME-2061 (account-4), 2 Oct 2026, 22:21-22:5x UTC. This session is separate from the
solver sessions on this target (VX-CS04, VX-RD03/B/C/D, GAPS to GAPS12). Rule 10, verifier brief template, steps 1-5.
It did no decoding and touched no other target.

## Verdict (per item)

| item | claim under audit | class | key source | prior plaintext | prior decipherment / key in print |
|---|---|---|---|---|---|
| 1 | the 17-sign key (key.tsv, grade C) and the 2039 legend decode (482 tokens: M 167, U 315, no word read whole) | **N1** for the key and the system. The 2039 legend has no reading to classify. | **ours**: alignment of 2007A against its own on-sheet gloss and the period plain twin 2007B. A **period** key sheet exists (NA 1.05.03 inv. 86, below) and was not used. | 2039: none located (AMH 2025 says "niet getranscribeerd"). The one source that could hold it, de Leeuw 1997, was not read. | **yes**: de Leeuw 1997 describes the system and reproduces "de sleutel tot het geheimschrift" from NA 1.05.03 inv. 86 |
| 2 | 2061 battery list No.1-6 and legend a-g: S 17, M 163, U 88 after GAPS12; cribs 'batterijen' (10 S) and 'wooning' (7 S) | **N0** | **ours** for the crib values (key_2061_crib.tsv; GAPS9/GAPS10 placements against the sheet's own gloss word and AMH's summary) | **yes**: Atlas of Mutual Heritage page 2218 prints the whole No.1-6 + a-g legend in English, after den Heijer 2012 | **yes**: the AMH sentence presents the content as a reading of "the legend in cipher on Wollant's map"; the key is in de Leeuw 1997 |
| 3 | 2039 legend and 2061 block under the PERIOD keys (inv. 86 scan 0002 Oud, scan 0003 Nieuw + 9 code groups): 2039 H 287 M 183 U 12; 2061 H 166 M 92 U 10 (VERIFY-SURINAME-PERIOD, 2 Oct 2026, below); revised by GAPS15 (2 Oct 2026, solver): 2039 H 290 M 180 U 12, 2061 H 176 M 82 U 10; 2061 revised again by GAPS16 (2 Oct 2026, solver): H 177 M 81 U 10 (see the GAPS15 revision note below) | **2039 legend: N1 (provisional)**, held there until LOCAL-QUEUE L36 is answered. **2061 block: N0** (unchanged). **Period key sheets: N1** | **period** for both readings (NA 1.05.03 inv. 86, read by GAPS13/GAPS14) | 2039: no Dutch or English text of the legend located; de Leeuw 1997 (unread) discusses fort Nieuw Amsterdam's garrison and barracks. 2061: AMH 2218 (English) | key sheets: **yes**, de Leeuw 1997 reproduces the "Nieuw Secrett Alphabeth" with its code groups (snippet). Decipherment of 2039: not located, not excluded |

Safe sentences:
- Item 1: "From 2007A's own interlinear gloss and its plain twin 2007B, we rebuilt 17 signs of Wollant's 1781 map cipher by
  alignment. The system and its period key sheet (NA Sociëteit van Suriname, 1.05.03 inv. 86) were already published by
  K. de Leeuw, Tijdschrift voor Zeegeschiedenis 16 (1997) 160-177. Our partial key is an independent re-derivation."
- Item 2: "Our partial letter-level reading of the 2061 (Redout Leyden) battery list and legend has 17 signs at grade S,
  through the cribs 'batterijen' and 'wooning'. It agrees with the legend content that the Atlas of Mutual Heritage already
  prints in English, after den Heijer 2012."

Unsafe sentences (never use): "first decipherment of Wollant's cipher maps"; "the 2061 legend, never transcribed, is now
read"; "no decipherment of these sheets has been published"; "the key is recovered" (the key was published in 1997 and the
period key sheet is in the archive).

Evidence quality and confidence. Item 2 N0 is high confidence: the AMH text is on disk, quoted and read in full. Item 1 N1
is medium-high: de Leeuw's article was located only by Google Books snippets, several of them independent, and its text was
not read. The snippets that carry the claim, quoted from the API's `textSnippet`:
- Title and author (the snippet and the 1998 OSO bibliography): "Leeuw, Karl de 'Enkele kaarten en plattegronden van de
  verdedigingswerken langs de Surinamerivier met geheimschrift (1782)'. Tijdschrift voor Zeegeschiedenis 16 (2), 1997,
  p. 160-175." UvA-DARE gives pp. 160-177.
- On the system: "Wollant maakte daarbij gebruik van een geheimschrift dat speciaal ontworpen was voor de codering van
  militaire berichten. Het was, met een of meer vaste substituten voor elke letter van het alfabet en negen codegroepen voor
  de meest voorkomende namen en begrippen, vrij ..."
- On the key: "... sleutel tot het geheimschrift wordt weergegeven. Collectie en foto Algemeen Rijksarchief 's Gravenhage,
  Sociëteit van Suriname, inv.nr. 86."
- The sheets it treats: "... (= 4.VEL 2039) no. 740 c: van de redout Leyden (= 4.VEL 2061) ... no. 740 d: van de redout
  Purmerend (= 4.VEL 2046) ... (= 4.VEL 2007 A)".
- "... Wollant in het voorjaar van 1782 tekende in opdracht van Gouverneur Texier ... geheimschrift was alleen een
  voorzorgsmaatregel tegen eventuele onderschepping door de vijand."

Not established, because the article was not read: whether de Leeuw prints a transcription or decipherment of any legend.
The 2039 legend is the open question. Until the article is read, a 2039 reading cannot go above N1-pending.

## Step 1: extract (from the repo)

- Items: NA 4.VEL 2007A/2007B, 2039 (fortress Nieuw Amsterdam), 2046 (Purmerent), 2061 (Redout Leyden) and 2077
  (Zelandia). All are by J.F.F. Wollant, made for Governor Texier in 1781. They went to the directors of the Sociëteit van
  Suriname.
- Plaintext as read. Item 1 is the 17-sign key (key.tsv) and the fragmentary 2039 legend decode (reading_2039_legend.txt).
  Item 2 is the 2061 block (reading_2061_battery.txt) with the cribs "batterijen" on legend e, "wooning" on legend a and
  "yser" on No.4 (grade M/I).
- What the solvers searched: NA finding aid 4.VEL 2030A5-2090C; AMH pages 2025, 2218, 2123 and 2228-2232; 6 + 11 web
  searches and the three blogs; DECODE cached dumps; both solver repos (on-disk snapshots); Google Books (5 queries across
  GAPS5); Internet Archive (be-api, 1 query); Leupe 1867. Not opened: den Heijer 2012 and Koeman. None of these passes
  found de Leeuw 1997.

## Step 2: independent search log (2 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a) canonical catalogue | NA item page 1.05.03 inv. 86 (1 request): "Registers van secrete resoluties, met losse bijlagen, o.a. betreffende de kritiek op de verdediging", 1707 Oct 15 - 1794 May 7, digitised, 167 scans. Folder's on-disk 4.VEL catalogue (vel_2030-2090_catalogue.tsv) re-read: no "ontcijferd"/"sleutel" | the key sheet de Leeuw cites lies somewhere in those 167 scans. Its scan number was not located (not this job's) |
| (b) sender/recipient editions | Google Books: Wollant + Texier/defensie/Suriname; "Redout(e) Leyden"; OSO 1996 (an article citing SvS inv. 370 and Wollant's 1781-82 cordon map) | de Leeuw 1997 (Mededelingen/Tijdschrift NVZ). OSO 1996 and 1998 snippets only, no cipher content |
| (c) documentary editions / atlases | AMH 2025 (fetched, snapshot sources/amh/2026-10-02/page2025_en.*): no 2039 legend plaintext. AMH 2218 (on disk): full English legend summary. den Heijer 2012: Google Books "Grote Atlas van de West-Indische Compagnie" Suriname -> 7 volumes, none the atlas; `intitle:` query -> 0 | den Heijer **unreachable from the cloud**, logged as a family not covered. LOCAL-QUEUE L36 |
| (d) holding archive | NA 1.05.03 inv. 86 description (above). NA 4.VEL descriptions: "In cyferschrift, met verklaring" (2061), "Gedeeltelijk in cijferschrift" (2039) | the NA catalogue does not mention a key or decipherment |
| (e) full text | Google Books, 24 queries with key and country=US. Phrase queries: "borrowed from the Cordon" (0 relevant), "officiers wooning" Suriname (0 relevant), "Plan en defensie staat" Leyden (Leupe only), "4.VEL 2061" and "4.VEL 2039" (both -> de Leeuw 1997 only), "negen codegroepen", "geheimschrift op zeekaarten". Internet Archive and HathiTrust: not re-run (GAPS5's be-api query is on file) | de Leeuw 1997 is the only hit on the sheets' own inventory numbers. Snippets quoted above |
| (f) solver repos, cipher blogs | covered 2 Oct 2026 by GAPS (on-disk snapshots, 3 blogs); not repeated | none |
| (g) scholarship | OpenAlex: "Wollant Suriname geheimschrift" -> 1 work; "de Leeuw geheimschrift kaarten" -> 2. Two records of de Leeuw 1997: W7165290719 (Leiden repository, green OA, hdl 1887/4305872) and W249820809 (UvA-DARE, closed, vol. 16 pp. 160-177). Semantic Scholar -> the same paper, no OA PDF. CORE "Wollant AND Suriname" -> 0. Web search on the exact title -> no other copy | the Leiden OA PDF answered "Access blocked by our protection system" to curl. One retry via the browser on the handle gave "upstream request failed", so this host was **not retried again** (good-citizen rule). The Wayback CDX connection was reset by the proxy. LOCAL-QUEUE L36 asks for a desk read |
| JSTOR | rows appended to JSTOR-QUEUE.tsv in both families (i) and (ii). They never block | queued |

Requests by host: atlasofmutualheritage.nl 2; www.googleapis.com 24 (1.6 s apart); api.openalex.org 3;
api.semanticscholar.org 1; api.core.ac.uk 1; scholarlypublications.universiteitleiden.nl 2 (1 curl blocked, 1 browser
failed); web.archive.org 2 (proxy reset); www.nationaalarchief.nl 1; web search 1.

## Step 3: classification reasoning

- **Item 2, N0.** The plaintext content of this very legend is printed (AMH 2218, after den Heijer 2012), and it is
  presented as the reading of the cipher legend on this map. The key that reads it is published too (de Leeuw 1997). What
  we add is an independent, partial (17 S tokens), letter-level re-reading that agrees with that content: legend e =
  batteries, legend a = officers' quarters, "iron" after the weights. No Dutch letter-level transcription of the 2061
  legend was located in print. den Heijer and de Leeuw were not read, so that question is open, but it does not change N0.
- **Item 1, N1** (key/system). A period key sheet and a published description with facsimile have existed since 1997. Our
  17-sign key re-derives part of it independently, from the 2007A gloss and 2007B. That fits N1: the plaintext (the key)
  is already published, and ours is an independent re-derivation. The 2039 legend decode is fragments (no word read whole),
  so there is no reading to classify. If one is made later, it starts at N1-pending until de Leeuw 1997 is read for a 2039
  transcription.

## Step 4: postmortem

Failure: eight solver passes and a premise check searched for a decipherment of these sheets by the sheets' names, the
mapmaker and the archive, and missed a crypto-historian's 1997 article. That article carries the sheets' 4.VEL inventory
numbers and reproduces the key. It turned up only when the inventory number itself ("4.VEL 2061") and the Dutch word
"geheimschrift" went into Google Books with "Wollant". GAPS5's queries used "cijferschrift" and English "cipher", which are
the catalogue's words, not de Leeuw's. Lesson: run a full-text query on the item's own shelfmark string ("4.VEL 2061") and
on every period synonym of "cipher" in the language (geheimschrift / cijferschrift / cyferschrift / ontcijferd / sleutel).
The premise check's (d) "recipient-side editions" would have found the key's location in the recipient's own archive
(1.05.03) had it searched secondary literature on that fonds.

Sentences corrected in NOTES.md (bracketed "[VERIFY-SURINAME-2061, 2 Oct 2026: ...]" notes, original text kept):
- line 7, "No full decipherment of 2007A, 2039, 2046, 2061 or 2077 located anywhere";
- the Closing line, "all five sheets are undeciphered (no transcription or decipherment published anywhere found)";
- VX-RD03 "Key source and method", the "period key ... and ours" dual label (it is `ours`; a `period` key sheet exists
  unused);
- the Premise check's Verdict "no decipherment, gloss, clear copy or print of 2039's legend found by (a)-(d)";
- the Escalation rows `known-keys` and `print`, and the Verdict line (a new cheapest step: locate the inv. 86 key sheet).

No SECOND-OPINIONS-QUEUE.tsv row: both items are below N3. No CONTRIBUTIONS or outreach.

## JSTOR

Appended to JSTOR-QUEUE.tsv on 2 Oct 2026 as queued: (i) Wollant AND Suriname AND (geheimschrift OR cijferschrift OR
cipher); (i) "Redout Leyden" OR "redoute Leiden" AND 1781; (ii) "met een of meer vaste substituten" (a phrase from de
Leeuw 1997, no cipher keyword); (ii) "officers' quarters" "garrison barracks" "gunpowder magazine" Suriname (AMH 2218
wording).

## Addendum (GAPS13-na-suriname-map-1781, solver, 2 Oct 2026 -- not a verifier pass)

The period key sheet this audit named is located: NA 1.05.03 inv. 86, scan NL-HaNA_1.05.03_86_0002, "Oud Secreet
Alphabet", 45 signs (key_period.tsv). Our 17-sign key agrees with it on 16 values, and the 17th (G) is an open sign
identity. The classes above are unchanged. A 2039 legend reading now exists under the period key (key source `period`,
reading_2039_legend_period.txt, H 277 / M 179 / U 26). It needs a separate verifier's class (N1-pending until de Leeuw
1997 is read, LOCAL-QUEUE L36). This addendum makes no novelty claim.

## Period readings (VERIFY-SURINAME-PERIOD, account-4, verifier, 2 Oct 2026, 23:16-23:26 UTC)

Separate session from GAPS13/GAPS14 (the solvers) and from VERIFY-SURINAME-2061. Claims under audit: the 2039 legend and the
2061 battery list read under the period keys of NA 1.05.03 inv. 86 (key_period.tsv, key_period_nieuw.tsv,
key_period_codes_nieuw.tsv): reading_2039_legend_nieuw.txt H 287 M 183 U 12, reading_2061_battery_nieuw.txt H 166 M 92 U 10;
pre-registered vocabulary control 13 against a shuffled max of 4. No decoding beyond the re-derivation. No other target touched.

### Rule 7 re-derivation

From decode.json, the ciphertext TSVs, key*.tsv, exceptions_2061_battery.tsv and plain_votes.tsv only, copied to a scratch
directory, `python3 tools/decode_key.py <scratch>` regenerated all seven jobs. `reading_2039_legend_nieuw.txt`,
`reading_2061_battery_nieuw.txt` and both `_nieuw_tokens.tsv` files are **byte-identical** to the committed ones (cmp).
Counts match: 2039 H 287 M 183 U 12, 2061 H 166 M 92 U 10. `tools/decode_key.py ciphers/na-suriname-map-1781 --check` exits 0.
The re-derivation differs by 0 tokens, so the readings stand as committed.

Pre-registration checked on GitHub, because this clone is shallow: commit f0840cdc (23:00:20 UTC) adds only vocab_prereg.txt and
control_prereg_vocab.py, and is earlier than the scoring commit 209f50b4 (23:06:48 UTC). The vocabulary is mechanical (crib_2038/2042
words). Both nulls (shuffled value, shuffled order) can change the hit count, so the control is a real test (rule 3). It shows the
period key reads Dutch words far above chance. It does not show the reading is correct letter by letter: many H-graded strings
are still not words (2039 heading, legend s). Here H means "value from the period key sheet". The sign identities still rest on our
two-pass transcription. The 183 + 92 M tokens are the [g|l], [k|i], [c|z] and shape-named code signs that GAPS14 lists as open.

### Search log (this session)

| family | searched | result |
|---|---|---|
| (a)/(d) catalogue, holding archive | relied on VERIFY-SURINAME-2061 (NA 1.05.03 inv. 86 and 4.VEL descriptions, same day); not repeated | no decipherment named |
| (b)/(c) editions, atlases | AMH 2025 (2039), from the prior pass: "niet getranscribeerd". den Heijer 2012: unreachable (prior pass) | none for 2039 |
| (e) Google Books, key + country=US, 27 calls | interior phrases from the 2039 decode, normalised: "cazernes voor de besetting", "laboratorie magazyn", "magazyn op de batteryen", "voor de bandieten" Suriname, "kruit magazyn" "corps de garde" Suriname 1781, "stuk geschut" Wollant Suriname, "secreet alphabet" Suriname, "Nieuw Secreet Alphabet", "fort Nieuw Amsterdam" legenda Wollant | 0 relevant hits. Only de Leeuw 1997 (Mededelingen NVZ, volume id -5XtAAAAMAAJ, snippet view) answered |
| (e) term probes inside de Leeuw 1997 (term + "Wollant", 40 results, filtered to that volume) | cazernes, magazyn, magazijn, batterij, batterey, bandieten, ontcijferd, ontcijfering, vertaald, Corps de garde, kruitmagazijn, legenda, lijst + geschut, "Nieuw Amsterdam" + kazernes: no snippet. kazernes, accommodatie, "1500 man", Verklaring, toelichtingen, opgelost, Purmerend: snippets (below) | absence in snippet search is weak (a 'Leyden' probe also missed, though the prior pass saw "redout Leyden" in this volume) |
| (e) Internet Archive full text (be-api fts) | "cazernes voor de besetting", "magazyn op de batteryen", Wollant Suriname geheimschrift | 0 hits each |
| (f), (g) | covered the same day by VERIFY-SURINAME-2061 and GAPS; not repeated | -- |
| JSTOR | 3 rows appended to JSTOR-QUEUE.tsv: family (i) and (ii) | queued, never blocking |

Snippets from de Leeuw 1997 that bear on this audit (Google Books `textSnippet`):
- "... [fort] Amsterdam Snapbaantr kogels fuyter Roopaarden 7 t P \"Nieuw Secrett Alphabeth\" waarin de sleutel tot het
  geheimschrift wordt weergegeven. Collectie en foto Algemeen Rijksarchief 's Gravenhage, Sociëteit van Suriname, ..." -- the
  figure is the **Nieuw** alphabet with its code groups (Snaphaanen, kogels, Affuyten, Roopaarden), i.e. the same leaf as
  key_period_nieuw.tsv. The key GAPS14 transcribed is printed in facsimile.
- "... Wollant 1500 man nodig om het fort lange tijd te kunnen verdedigen tegen belegeraars. Het fort had echter onvoldoende
  accommodatie om zoveel manschappen te kunnen huisvesten. In dit licht moet het plan voor de verhoging van de ..." -- de Leeuw
  discusses the content of the fort plans (garrison, barracks). That matches the 2039 legend's "cazernes voor de besetting"
  (legend b). Whether he took it from the cipher legend or from a plain report is not visible.
- "... toelichtingen en onderschriften werden echter gegeven in geheimschrift ..."; "... Wollant verraden en die alle
  toelichtingen bevatten in geheimschrift. De serie vormt een unicum ..."; "... opgelost doet vermoeden dat het materiaal van het
  Sociëteitsbestuur niet de aandacht heeft gekregen die het ..." (context cut off).

Requests by host: www.googleapis.com 27 (>=1.7 s apart, one 503, not retried); be-api.us.archive.org 3; api.github.com 1.

### Classification

- **Period key sheets (Oud scan 0002, Nieuw scan 0003 + 9 code groups): N1, key source `period`.** Our transcription of them is
  independent. The Nieuw leaf with its code groups is printed in facsimile in de Leeuw 1997.
- **2039 legend under the period key: N1 (provisional), key source `period`.** No prior plaintext was located (AMH 2025:
  not transcribed; phrase searches: none). But the one study of exactly these sheets, which prints the key and discusses the
  fort's barracks, has not been read. A paraphrase or transcription there would make it N1 or N0. So it is not classed N3 until
  L36 answers. If L36 finds no 2039 legend text or paraphrase in de Leeuw 1997, the next verifier may raise it to N3, with
  den Heijer 2012 still logged as unread. Confidence: medium.
- **2061 block under the period key: N0, unchanged, key source now `period`** (was `ours`, crib values). AMH 2218 prints the
  legend content in English and presents it as a reading of the cipher legend. The period reading agrees with it (guns,
  iron, powder magazine, officers' quarters, batteries). Confidence: high.

Safe sentence (2039): "Under the period key in NA 1.05.03 inv. 86 (published in facsimile by de Leeuw 1997), we read the
2039 (fort Nieuw Amsterdam) legend at 290 of 482 signs from the key sheet and 180 uncertain (counts revised by GAPS15, 2 Oct 2026). No printed text of this legend
was located in the sources searched; de Leeuw 1997, which discusses these sheets, has not been read."
Safe sentence (2061): "Under the period key, our letter-level reading of the 2061 battery list and legend agrees with the
content the Atlas of Mutual Heritage already prints in English."
Unsafe: "first reading of the 2039 legend", "previously unread", "we recovered Wollant's key" (the key is a period sheet,
printed 1997), any word for a 2039 novelty above N1 before L36 is answered.

No SECOND-OPINIONS-QUEUE.tsv row: every item is below N3.

### Postmortem

No over-claim found. NOTES.md's GAPS14 section says "Rule 10: key source `period` ... No novelty claim" and "N1-pending".
VERIFY-SURINAME-2061's Step 2 reports a fact that is now stale: the de Leeuw caption it quoted is the **Nieuw** leaf (scan 0003
with code groups), not only "a key sheet". Recorded here; NOTES.md line 1313 already names scan 0003. One lesson: the H grade
here is key-sourced, but the readings are not yet clean text. Any outward sentence quotes the counts, never "read in full".

## Revision carried in (GAPS15-na-suriname-map-1781, solver, account-4, 2 Oct 2026 -- rule 10 propagation, not a verifier pass)

One blind image call compared 17 tiles of 1781 reader signs with the Nieuw sheet's signs (passes/signcmp_gaps15/result.tsv).
Changed: [thorn] = c (was c|z; two tokens H by exception), [MM] / [ladder-III] / [hand-box] H (were M), 2039 b:2 = s, 2061 L01:4
= a H. Item 3 counts are now 2039 H 290 M 180 U 12 and 2061 H 176 M 82 U 10 (`tools/decode_key.py --check` exit 0); the
pre-registered vocabulary control is unchanged (13 hits; shuffled-value null max 4, shuffled-order max 3, 0/1000 each). The
classes above are not changed by this. New, not yet classified by any verifier: the 2039 title lines 1 and 3 and the lower-left
Remarque under the same key (ciphertext_2039_remarque.tsv, reading_2039_remarque_nieuw.txt; 295 tokens H 188 M 101 U 6, from a
two-pass draft both readers rated low-confidence). No SECOND-OPINIONS-QUEUE.tsv row exists for this target, so none to update.

## Revision carried in (GAPS16-na-suriname-map-1781, solver, account-4, 2 Oct 2026 -- rule 10 propagation, not a verifier pass)

A second blind sign call settled four 2061 tokens by exception (L04:10 and L06:22 readers' y = psi = s, L10:26/29 g = q = p;
passes/signcmp_gaps16/result.tsv): item 3's 2061 count is now H 177 M 81 U 10; the 2039 legend is unchanged (H 290 M 180 U 12).
`tools/decode_key.py --check` exit 0; the pre-registered vocabulary control is unchanged (13; null max 4 and 3, 0/1000 each).
The 2039 Remarque rows of ciphertext_2039_remarque.tsv were replaced by a native-resolution re-pass (2 blind passes 247/261,
1 blind reconciliation): the title/Remarque job now reads H 190 M 87 U 15 (was H 188 M 101 U 6), still unclassified by any
verifier. The classes above are not changed by this. No SECOND-OPINIONS-QUEUE.tsv row exists for this target.

## Item 4: the 4.VEL 2077 legend under the Nieuw period key (VERIFY-SURINAME-2077, account-4, verifier, 3 Oct 2026, 04:26-05:0x UTC)

This session is separate from the solvers (GAPS19-GAPS22, NL18-CORPUS) and from REDERIVE-SURINAME-2077. It follows the verifier
brief template, steps 1-5. It did no decoding and touched no other target.

### Verdict

| item | claim under audit | class | key source | prior plaintext | prior decipherment / key in print |
|---|---|---|---|---|---|
| 4 | 2077 title cartouche, heading and "Explicatie der Signatuuren" legend a-z (+ alpha-eta), reading_2077_legend_nieuw.txt: 658 cipher tokens H 500 M 106 U 52, plus 98 plain words. GAPS22: the rate-matched nl18 gate PASSes 7/7 folds and 0/400 target shuffles pass; the non-gating half-M-right sensitivity check FAILs 4/7 | **N1 (provisional)**, held there until LOCAL-QUEUE L36/L41 are answered. **Ceiling N2** even if they come back empty (see below) | **period** (NA 1.05.03 inv. 86 scan 0003, Nieuw Secreet Alphabet + code groups; image exceptions from GAPS21) | **Content, yes, in a period plain sister plan.** NA 4.VEL 2078, Wollant's own July 1782 plan of the same fort "not in cipher" (Pl. E / E.E.), carries a plain "Nota" A-C, a-z that lists the same buildings. It is printed in facsimile on the same page as 2077 (den Heijer 2012, p. 329). The 2077 legend's own text was not located in print: AMH 2123 says "partly encrypted, not transcribed". | **Key: yes.** den Heijer 2012 p. 471 prints the Nieuw Secrett Alphabeth in facsimile (inv. 86 fols 1v-2), and so does de Leeuw 1997. **Decipherment of 2077: none located.** den Heijer's caption on p. 329 does not transcribe it. de Leeuw 1997 lists 2077 (no. 740 e) and is unread (L36). *Suriname en zijn historie* (1972) reproduces 2077 (plate 120/121) and is unread (L41) |

Safe sentence (2077): "Under the period key in NA 1.05.03 inv. 86 (printed in facsimile by de Leeuw 1997 and den Heijer 2012, p. 471),
we read the 2077 (fort Zeelandia) legend at 500 of 658 cipher signs from the key sheet, with 106 uncertain and 52 unkeyed. Its content
matches the plain Nota of Wollant's 1782 plan of the same fort (NA 4.VEL 2078). No printed transcription of the 2077 legend was found
in the sources searched. de Leeuw 1997 and *Suriname en zijn historie* (1972), which both treat or reproduce the sheet, have not been
read."
Unsafe: "first decipherment of the Zeelandia map", "previously unknown contents of fort Zeelandia", "we recovered Wollant's key", "read
in full", or any sentence that implies the legend's content was unknown (4.VEL 2078 gives it in plain Dutch).

### Step 1: extract

- Item: NA 4.VEL 2077, "Plan van de fortress Zelandia", 1781, J.F.F. Wollant for Governor Texier. The catalogue (vel_2030-2090_catalogue.tsv)
  says "In cyferschrift en gedeeltelijke verklaring" and "Gefacsimileerd in Grote Atlas van de West-Indische Compagnie deel II p. 329".
  The legend is mixed: plain entries such as f Menagerie, Neegerhuijsen voor d' Edl. Directie Slaaven, g huÿs voor den Opsigter,
  n bootehuÿs, s Cöps de garde, w gevangenhuÿsen, z Cipiers=wooning and alpha Smeederÿ heel defect, with ciphered entries between them.
- Reading (word level M, as GAPS20 segmented it): c "secretarye", p "cassernes ...", q "artilleri[e] cassernen [m]onteer[i]ngs [k]a[m]er",
  r "logis voor d[e] adjudant de[r] garnisoens ...", t "bakkery", u "laboratorium voor de art[i]llerie", x "... magazyn ... berging van droog
  goederen", "magasyn ... voor kleine geweer", delta "magasyne tot berging van brandspuiten", L20 "dispositie der batteryen". The title
  lines read only in fragments.
- What the solvers searched (GAPS19 premise check): Google Books (~22 calls: "4.VEL 2077", "fortress Zelandia" cyferschrift, "Explicatie
  der Signatuuren", "Ambagts Slaaven", "Monteerings Kamer"), IA be-api 1, NA item page. They found de Leeuw 1997's list and *Suriname en
  zijn historie* (1972). Not found: den Heijer's digital edition, AMH 2123, and the plain sister plan 2078 as a content parallel.
  VX-CS04 eye-checked 2078 on 25 Sept 2026 and recorded it only as "entirely plain Dutch".

### Step 2: independent search log (3 Oct 2026, this session)

| family | searched | result |
|---|---|---|
| (a) canonical catalogue | on-disk 4.VEL catalogue rows 2070-2082 re-read | 2077 and 2078 are both facsimiled in den Heijer II. 2078 is "Plan van de teegenswoordigen staat der fortress Zeelandia met de daerby ontworpene noodige verandering", ca. 1784, "Met nota", made by Wollant |
| (b) sender/recipient editions | Google Books: "Suriname en zijn historie" + Zeelandia/Wollant/geheimschrift/cijferschrift/legenda; Temminck Groll, *De Architektuur van Suriname 1667-1930* (1973) + Wollant + secretarie/laboratorium/kazernes/geheimschrift | *Suriname en zijn historie* (1972, Pg9sAAAAMAAJ, NO_PAGES): picture list "120/121 Kaart van Wollant, 1781. Algemeen Rijksarchief ... nr. Leupe 2077". Its OCR of "Ambagts Slaaven ... Mon tecringe Kamer, 1. jagiotist sal einsday ..." is cipher noise from the plate, not a transcription. Temminck Groll 1973 (YQI3AQAAIAAJ, NO_PAGES) describes Zeelandia's buildings and Wollant's July 1782 memorie ("gebouw dient nu tot artillerie-laboratorium", "secretarie"). It is a content source of the 2078 kind, and nothing shows it deciphers 2077. Both unread beyond snippets |
| (c) documentary editions, atlases | **den Heijer 2012, now reachable**: the Nationaal Archief's digital edition (2.14.97 inv. 24.2, 475 page scans, IIIF). The route was found through Caert-Thresoor 41-2 (2022, archive.org ct-41-2). Read: p. 329 (2077 + 2078 + caption), p. 471 (key), p. 342 (2039) | p. 329: 2077 in facsimile, no transcription. The caption says "Most or in some cases even all of the annotation on these plans is in cipher ... The key to the decipherment is given in Chapter VII (sheet 471)". Below 2077 is 2078, Wollant's July 1782 plan "not in cipher", with a plain Nota. p. 471: the Nieuw Secrett Alphabeth in facsimile and its caption. p. 342: 2039 in facsimile, no legend text. Snapshots in sources/gawic/2026-10-03/. AMH 2123 (VEL2077) fetched: "partly encrypted, not transcribed" (sources/amh/2026-10-03/) |
| (d) holding archive | NA 4.VEL catalogue (on disk); NA 1.05.03 inv. 86 was covered by earlier passes | the catalogue names no decipherment |
| (e) full text | Google Books, about 33 calls, with the key and country=US, 1.8 s apart (three 503s, not retried in a loop): the phrases "Ambagts Slaaven", "Explicatie der Signatuuren", "Cipiers wooning", "Neegerhuijsen voor", "bootehuys voor" Directie, "Smeederij heel defect", "magazyn voor kleine geweer", "berging van brandspuiten", "Monteerings Kamer" Paramaribo, "Leupe 2077", "4.VEL 2077", "fortress Zelandia" Wollant, Wollant + Zeelandia + geheimschrift/plattegrond/1781. IA be-api: Wollant AND Zeelandia, "Ambagts Slaaven", "Cipiers wooning" AND Suriname, Zelandia AND cyferschrift, Wollant AND geheimschrift (0 each); "Wollant" "Zeelandia" (12) | no transcription of the 2077 legend. Hits: the Leupe 1867 inventory, Caert-Thresoor 41-2 (the den Heijer route), and the volumes in (b). Every phrase hit outside these is an unrelated period text (Amsterdam town hall, placaat books) |
| (f) solver repos, cipher blogs | covered 2 Oct 2026 (GAPS web and blog check, on-disk snapshots); not repeated | none |
| (g) scholarship | OpenAlex (key): "Wollant Zeelandia", "Wollant Suriname 1781" -> only de Leeuw 1997 (W7165290719); "fort Zeelandia 1781 plan" -> 15, none relevant. CORE (key): the same three queries, no relevant hit in the top 5. Semantic Scholar: 3 queries returned no data (logged as unanswered this pass) | de Leeuw 1997 is the only scholarly work on the cipher sheets |
| JSTOR | 2 rows appended to JSTOR-QUEUE.tsv, one each in families (i) and (ii) | queued; they never block |

Requests by host: www.googleapis.com ~33; be-api.us.archive.org 9; archive.org 2; atlasofmutualheritage.nl 1; www.nationaalarchief.nl 2;
service.archief.nl 6; api.openalex.org 3; api.core.ac.uk 3; api.semanticscholar.org 3; web search 3; historischecartografie.nl 2.

### Step 3: classification reasoning

- No printed transcription or decipherment of the 2077 legend was located. den Heijer, the one source that reproduces the sheet and also
  prints the key, leaves it untranscribed, and AMH 2123, which follows him, says so. That alone would support N3.
- Two unread sources treat the sheet: de Leeuw 1997, which lists 2077 as no. 740 e and is the study of these ciphers, and *Suriname
  en zijn historie* (1972), which reproduces 2077 as plate 120/121. Item 3 holds 2039 at N1 (provisional) for the same reason, so 2077
  is held there too.
- **Ceiling N2.** The *content* of the legend is already in period plain Dutch, by the same author, about the same buildings: the Nota
  of 4.VEL 2078 (July 1782), printed in facsimile on the same page, den Heijer p. 329. Examples: 2078 b "Artillerie Casserne en
  Monteerings Kamer" ~ 2077 q; 2078 d "Laboratorium van d'Artillerie" ~ 2077 u; 2078 k "Adjudant Wooning & Garnisoen Schryvery" ~ 2077 r;
  2078 n "Bakkery, defect" ~ 2077 t; 2078 c "Casserne, oud en defect" ~ 2077 p; 2078 "Wooning van d'Ambagts Slaaven de Monteerings
  Kaemer, w. Wooning van den Opsigter der Directie Slaaven" ~ 2077 g/h (plain). The 2078 Nota is a different text, with different
  letters, order and wording, so it is not this plaintext, and nobody has mapped 2077's ciphertext to it. That fits N2, "plaintext
  known elsewhere", only loosely. Even if L36 and L41 are empty, the class is N2 and not N3: a reader would rightly say the contents of
  the 1781 Zeelandia legend were knowable from 2078 since 1782, and in print since 2012.
- Confidence: medium. The ceiling is high confidence, because the 2078 Nota was read on the page image (sources/gawic/2026-10-03/p329_nota1782.jpg).

### Grade mix and stage 9 (the brief's question)

**The reading is not ready for a stage-9 move. Run the per-instance g|l check first, together with a cheaper and stronger step that
did not exist before this audit.**
- M is 106 of 658 (16.1%) and U is 52 (7.9%), so 24% of the cipher tokens are not read from the key. The PASS holds only when every M
  letter is assumed wrong. With half of the M letters right, the same score FAILs 4 of 7 folds. That is a reading whose letters carry
  more error than the grade mask counts, not a cleanly gated reading. The g|l class alone is 46 tokens, a third of the M+U.
- New instrument: the 2078 plain Nota is a period known-plaintext parallel for about ten 2077 entries. A pre-registered comparison of
  the cipher entries that have a 2078 counterpart would show how many letters the reading gets right where an answer exists. Examples
  are 2077 r against "Adjudant Wooning & Garnisoen Schryvery", and q and u (above). The [g|l] tokens inside "garnisoen", "magazyn" or
  "Monteerings" would be settled there by the known text, which is a grade C source. This is a solver job, not done here (no
  decoding). Under rule 3 it is a matched control on this very sheet. The judge gate cannot be that.
- A class assigned now on a reading that the g|l check and the 2078 comparison will change would have to be re-propagated (rule 10).
  The class above stands for the reading as committed (`tools/decode_key.py ... --check` exit 0, 3 Oct 2026 04:32 UTC). The board
  moves to "Novelty verified" only after the next verifier confirms the class on the settled reading.

### Step 4: postmortem

- Failure: the folder had the plain sister plan on disk since 25 Sept 2026 (images/2078_overview.jpg, VX-CS04: "entirely plain Dutch,
  signed Wellant"). Eight days later it was still filed only as "ruled out, plain". Nobody used it as the content parallel or crib for
  2077, though den Heijer prints the two sheets one above the other. "Ruled out" answered "is it a cipher?" and not "is it the same
  legend in clear?". Lesson for the premise check's (c) physical neighbours: a plain neighbour by the same author, of the same place and
  year, is a candidate plain twin, and its legend must be read before the cipher sheet is called unglossed.
- den Heijer 2012 was logged as "unreachable from the cloud" (GAPS5, VERIFY-SURINAME-2061, VERIFY-SURINAME-PERIOD). It is open on the
  Nationaal Archief site, 2.14.97 inv. 24.2, through service.archief.nl IIIF. The second half of L36 can now be answered from the
  cloud: p. 342 (2039) prints no legend text, and neither does p. 329 (2077). The 2061 page was not checked in this pass.
- Over-claims corrected in NOTES.md (bracketed notes, original text kept): the "Key beside the letter" sentence, "2039, 2046 and 2077
  have **no** key or gloss found on the sheet or elsewhere"; and the GAPS5 and GAPS19 sentences logging den Heijer as unreachable.
  The GAPS22 ROOM.md line "reading ready" is a solver's gate statement and not a novelty claim; it is left as is.

No SECOND-OPINIONS-QUEUE.tsv row: 2077 is below N3. No CONTRIBUTIONS or outreach.
