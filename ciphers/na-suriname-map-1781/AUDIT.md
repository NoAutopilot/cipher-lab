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
| 4 | 2077 title cartouche, heading and "Explicatie der Signatuuren" legend a-z (+ alpha-eta), reading_2077_legend_nieuw.txt: 658 cipher tokens H 500 M 106 U 52, plus 98 plain words. [VERIFY2-SURINAME-2077, 3 Oct 2026: revised by GAPS23/GAPS24 to H 500 C 7 M 101 U 50; class re-checked and unchanged, see the section at the end of item 4.] [VERIFY3-SURINAME-2077, 3 Oct 2026: revised by GAPS25 to H 499 C 7 M 102 U 50 (GAPS29 changed nothing); class re-checked and unchanged, N1 (provisional), ceiling N2.] [VERIFY4-SURINAME-2077, 3 Oct 2026: revised by GAPS37 to H 540 C 7 M 61 U 50 (same-hand g|l call, held-out by a chosen-vs-swapped word check: 30/41 read only as chosen, 0 contradicted); class re-checked and unchanged, N1 (provisional), ceiling N2; see the last section of item 4.] GAPS22: the rate-matched nl18 gate PASSes 7/7 folds and 0/400 target shuffles pass; the non-gating half-M-right sensitivity check FAILs 4/7 | **N1 (provisional)**, held there until LOCAL-QUEUE L36/L41 are answered. **Ceiling N2** even if they come back empty (see below) | **period** (NA 1.05.03 inv. 86 scan 0003, Nieuw Secreet Alphabet + code groups; image exceptions from GAPS21) | **Content, yes, in a period plain sister plan.** NA 4.VEL 2078, Wollant's own July 1782 plan of the same fort "not in cipher" (Pl. E / E.E.), carries a plain "Nota" A-C, a-z that lists the same buildings. It is printed in facsimile on the same page as 2077 (den Heijer 2012, p. 329). The 2077 legend's own text was not located in print: AMH 2123 says "partly encrypted, not transcribed". | **Key: yes.** den Heijer 2012 p. 471 prints the Nieuw Secrett Alphabeth in facsimile (inv. 86 fols 1v-2), and so does de Leeuw 1997. **Decipherment of 2077: none located.** den Heijer's caption on p. 329 does not transcribe it. de Leeuw 1997 lists 2077 (no. 740 e) and is unread (L36). *Suriname en zijn historie* (1972) reproduces 2077 (plate 120/121) and is unread (L41) |

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

Reading revised by GAPS23/GAPS24 (3 Oct 2026, solver, rule 10 propagation, not a verifier pass): 2077 was H 500 M 106 U 52 when this item was classed and is now H 500 C 7 M 101 U 50, M+U 0.229 (2078 Nota known-plaintext check, passes/nota2078_gaps23 and passes/nota2078_gaps24). Re-class pending.

### Re-class on the revised reading (VERIFY2-SURINAME-2077, account-4, verifier, 3 Oct 2026, 05:20-05:4x UTC)

A session separate from every solver on this target (GAPS19-GAPS24, NL18-CORPUS), from REDERIVE-SURINAME-2077 and from
VERIFY-SURINAME-2077. Rule 10 propagation of GAPS23 (51d9794e) and GAPS24 (2d92f06b). No decoding; no other target touched.

[GAPS25, 3 Oct 2026: reading revised by GAPS25 (blind d/n/q sign call, prereg 12845ab7: x -> a 13 tokens, [v-tall] -> c 9 tokens, 22 values changed; 2077 H 499 C 7 M 102 U 50; GAPS23 gate re-run unchanged 0.696 -> 0.768); re-class pending.] [VERIFY3-SURINAME-2077: re-classed, see the next section.]

**Verdict: item 4 stays N1 (provisional), key source period, ceiling N2.** The revision makes the reading better supported. It
adds no print of this legend and removes none of the reasons for the hold.

| | before (VERIFY-SURINAME-2077) | now |
|---|---|---|
| 2077 cipher tokens (658) | H 500 M 106 U 52, M+U 0.240 | **H 500 C 7 M 101 U 50, M+U 0.229** (C 7 = 7 tokens settled against 4.VEL 2078; one of the 8 exceptions, L11:17, is capped at M by its transcription conf) |
| gates on file | GAPS22 rate-matched nl18 gate PASS 7/7, shuffled 0/400; half-M-right sensitivity FAIL 4/7 | unchanged (GAPS22 not re-run at 0.229), **plus** GAPS23 known-plaintext check against the plain 2078 Nota: pooled H-letter agreement 0.696 (78/112) vs label-shuffle N1 p99 0.446 and value-shuffled-key N2 p99 0.277, 0/2000 each, PASS; GAPS24 secondary pairs: 1 of 4 supported (e~h 9/9), k~s and l~t tie N1 p99 (no power at 9-16 H letters, not a negative), a~B fails |
| `decode_key.py --check` | exit 0 (04:32 UTC) | **exit 0** (05:2x UTC, this session): "ciphertext_2077_legend.tsv: tokens 658: C 7, H 500, M 101, U 50", "reading up to date" |

**What this session checked (step 2 of the brief, stage 9):**
- Pre-registration order holds in git: 5c306ccd (GAPS23 prereg + score.py, 04:49 UTC) precedes 51d9794e (transcription and scores,
  04:55); 7c2e235b (GAPS24 prereg, 05:05:09) precedes 2d92f06b (scores, 05:05:58). The GAPS23 gating pairs were chosen by the earlier
  verifier, not by the solver; GAPS24's pairs were chosen from the solver's own word segmentation, which GAPS24 says, and which is why a
  pair counts only when it beats both of its own controls.
- Reproduced both scores on a scratch copy (committed files untouched). The real numbers are identical: GAPS23 per-pair and pooled
  78/112 = 0.696; GAPS24 4/10, 9/9, 10/16, 7/9. The control quantiles move slightly (N1 p99 0.438 vs committed 0.446; u~d own p99 0.476
  vs 0.524) because the script now reads a token file in which its own regrades are already applied. Verdicts unchanged.
- Re-derivation (rule 7): REDERIVE-SURINAME-2077 agreed on the pre-revision reading. The revision changes 8 tokens, every one of them
  M or U before, through 8 committed rows of exceptions_nieuw_image.tsv that cite their pre-registered source. That is within the
  rule-7 tolerance (differences only on M-graded tokens), and `--check` regenerates it. No fresh re-derivation is needed for this
  revision.
- **Stage 9 is still not ready.** Three things hold it: (1) the half-M-right sensitivity FAIL (GAPS22, 4/7) has not been re-run, and
  M+U only went from 0.240 to 0.229; (2) the per-instance g|l call that GAPS24 names as next (about 40 g|l tokens still M) is not done;
  (3) new from GAPS23's confusion table: the commonest mismatches against 2078 are H-graded letters, systematically d->c, n->m, q->a
  ("dassernes" for casserne). So some **H** grades are wrong in a patterned way, and the H count overstates the letters that are right.
  The grade mask cannot see this: an H grade says "read from the key sheet", not "right". Before stage 9 a solver should settle whether
  those are key-reading or sign-merge errors on the d, n and q signs (one blind sign call against inv. 86 scan 0003, about $1.5) and
  re-grade; then a verifier confirms the class on the settled reading.

**What the 2078 Nota means for the class (step 1 of the brief).** It is a period plain text of parallel content, by the same author,
eight to twelve months later, with different letters, order and wording. It is not a print of the 2077 legend, and nothing in the
record maps 2077's ciphertext to it before GAPS23 did. So it does not make the 2077 plaintext "already published" in the N1 sense.
N1 stays only as the provisional hold for the two unread sources that treat or reproduce this sheet (de Leeuw 1997, LOCAL-QUEUE L36;
*Suriname en zijn historie* 1972, L41; both still `queued` at 05:2x UTC). What GAPS23 does change is the ceiling's footing: 7 letters
of our reading are now graded C *from* that parallel, so part of the reading rests on known period text. That confirms the ceiling of
N2 ("plaintext known elsewhere, no prior mapping of this ciphertext to it"), loosely as before: if L36 and L41 come back empty, the class
is N2, not N3. The mapping of 2077 to 2078 is ours (GAPS23), not prior.

**Searches newly relevant to the revision (step 3),** for the newly C-graded words and the phrases they complete (artillerie,
laboratorium, bakkery, neeger), 3 Oct 2026:

| family | searched | result |
|---|---|---|
| (e) Google Books (key, country=US, 1.8 s apart) | "artillerie cassernen"; "Neeger gevangenhuysen"; "Neeger gevangenhuisen" Suriname; "laboratorium voor de artillerie" Suriname 1781; "monteerings kamer" Zeelandia artillerie; bakkery "fort Zeelandia" 1781 Wollant; "laboratorium voor de artillerie" Zeelandia | 503 twice on the last query (one retry, then stopped). Hits: a Copenhagen street register (1831); Temminck Groll 1973 (already logged, describes "artillerie-laboratorium" in prose); *Suriname en zijn historie* (1972), snippet "Artillerie Casernen, en boven het monteerings Magazijn; door de Engelschen tot het voorgemelde einde ingerigt" -- a description after the British occupation (1799-1816), not a transcription of 2077's legend; it does show the book describes these buildings in prose, which L41 should note |
| (e) IA full text (be-api) | "laboratorium voor de artillerie"; "artillerie cassernen"; "Neeger gevangenhuysen"; Zeelandia AND laboratorium AND bakkery | 6 / 1 / 0 / 0. The hits are 19th-century Delpher newspapers and a Danish weekly, none about Suriname's fort Zeelandia in 1781 |
| (g) CORE (key) | title search for de Leeuw 1997 ("verdedigingswerken langs de Surinamerivier"), to see if CORE holds the open-access full text that the Leiden repository blocks | 4 records of the article, all without full text or abstract (providers NARCIS and a Leiden collection). L36 stays the route |
| (a)-(d), (f), JSTOR | not re-run: the revision adds no new identifier, sender, recipient or date. JSTOR rows 175-176 (3 Oct 2026) already cover the 2078 words | -- |

Requests by host: www.googleapis.com 8; be-api.us.archive.org 4; api.core.ac.uk 3.

Safe sentence (2077, replaces the one above): "Under the period key in NA 1.05.03 inv. 86 (printed in facsimile by de Leeuw 1997 and den Heijer 2012,
p. 471), we read the 2077 (fort Zeelandia) legend at 500 of 658 cipher signs from the key sheet and 7 more from Wollant's own plain
1782 plan of the same fort (NA 4.VEL 2078), with 101 uncertain and 50 unkeyed. Where the two plans name the same building, our reading
agrees with the 2078 Nota well beyond chance (pre-registered check). No printed transcription of the 2077 legend was found in the
sources searched; de Leeuw 1997 and *Suriname en zijn historie* (1972), which both treat or reproduce the sheet, have not been read."
Unsafe (unchanged, plus one): "first decipherment of the Zeelandia map"; "previously unknown contents of fort Zeelandia"; "we recovered
Wollant's key"; "read in full"; **"confirmed against known plaintext"** or "verified by 2078" for the whole legend (the check covers 5
gating entries and 1 supported secondary pair, and the matches are H-letter agreement with a differently worded text, about 70%).

Postmortem: no over-claim found in the revision. GAPS23/GAPS24 left the class to a verifier and wrote the "re-class pending" line, as
rule 10 asks. One gap: GAPS23 reported the d->c / n->m / q->a pattern as "descriptive, non-gating" and its Verdict and GAPS24's go
straight to the g|l call. That pattern is direct evidence about H-graded tokens, so it belongs in the reading's next step ahead of the
g|l call. Added to the stage-9 list above, not to NOTES.md's gaps (a solver's job).

No SECOND-OPINIONS-QUEUE.tsv row: the class is N1 (provisional), below N3. No CONTRIBUTIONS or outreach.

### Re-class on the GAPS25 reading (VERIFY3-SURINAME-2077, account-4, verifier, 3 Oct 2026, 06:18-06:3x UTC)

A session separate from every solver on this target (GAPS19-GAPS29, NL18-CORPUS), from REDERIVE-SURINAME-2077 and from
VERIFY-SURINAME-2077 and VERIFY2-SURINAME-2077. Rule 10 propagation of GAPS25 (12845ab7, a10d58e3, ebe2ab1d) and GAPS29
(e8726900, ce9f68a4). No decoding, no vision call; no other target touched.

**Verdict: item 4 stays N1 (provisional), key source period, ceiling N2. Stage 9 ("Novelty verified") cannot be set yet.**

| | VERIFY2 (05:2x UTC) | now |
|---|---|---|
| 2077 cipher tokens (658) | H 500 C 7 M 101 U 50 | **H 499 C 7 M 102 U 50**, M+U 0.231 (22 values changed by GAPS25: q->a 13, d->c 9; one d->c instance at L19:29 went H->M) |
| `decode_key.py --check` | exit 0 | **exit 0** (06:2x UTC, this session): "ciphertext_2077_legend.tsv: tokens 658: C 7, H 499, M 102, U 50", "reading up to date" |
| GAPS23 registered gate (5 pairs vs 2078 Nota) | 0.696 (78/112), N1 p99 0.438 | **0.768 (86/112)**, N1 p99 0.455, N2 p99 0.277, 0/2000 each, PASS. Re-run here on a scratch copy with the committed passes/nota2078_gaps23/score.py: result.tsv byte-identical to passes/nota2078_gaps25/result.tsv and passes/nota2078_gaps29/result.tsv |
| GAPS29 g|l call | -- | non-test by its own prereg (partner gate 5/22), no value change; sheet-tile g|l method [retired] under rule 3 (GAPS21 + GAPS29) |

**Pre-registration order (git).** 12845ab7 (GAPS25 prereg, brief, blind refs, queries; 05:44:06 UTC) precedes a10d58e3 (apply
script and the gate baseline re-run, 05:47:12) and ebe2ab1d (decisions, exceptions, reading; 05:53:14). e8726900 (GAPS29 prereg,
06:01:21) precedes ce9f68a4 (06:04:56). The GAPS25 class rule (settled >= 0.6, >= 3 settled, >= 2/3 on one value) is written in
the prereg before the call, and the deviation from sign-level boxes is stated there too. Order holds.

**One caveat on the 0.768 (not a failure, a limit on what it shows).** GAPS25 chose which sign classes to re-examine (d, n, q) from
GAPS23's confusion table, which is computed on the same five gating pairs; 8 of the 22 changed tokens sit inside those pairs. The
call itself was blind to 2078 (sheet tiles under shuffled labels, masked targets), so the agreement it bought is real, but the gain
from 0.696 to 0.768 is not a held-out test of the fix: the gate is no longer independent for the d/n/q classes. The out-of-gate check
is the 14 changes outside the five pairs (this session, diff a10d58e3..ebe2ab1d): they turn "sedretarye" into "secretarye",
"paqrdesta[g|l]en" into "paardesta[g|l]en", "waqter" into "waater" (twice), "nq[g|l]asyn"/"na[g|l]qsyn" into "na[g|l]asyn"
(magazyn) three times, "arsenqe[g|l]" into "arsenae[g|l]", "[g|l]eweernaq[k|i]ers" into "...naa[k|i]ers" (geweermakers),
"brandspvyten ... nasdines" into "nascines" (machines). Every one is a period Dutch word or nearer to one, none of them scored by
any gate. That is the stronger evidence for GAPS25, and it is what the safe sentence below leans on. Future gates on this legend
should use pairs (or the GAPS24 secondary pairs) that did not select the fix.

**What still blocks stage 9.**
1. **Novelty, not reading:** LOCAL-QUEUE L36 (de Leeuw 1997) and L41 (*Suriname en zijn historie* 1972; Temminck Groll 1973) are
   both still `queued` on origin/main at 06:2x UTC. Either may print a transcription of the 2077 legend. Until they are answered the
   class is N1 (provisional); if both come back empty it is N2 (the 2078 Nota gives the content in plain period Dutch), never N3.
   Stage 9 needs a class that the next verifier can confirm on a settled reading with those two answered.
2. **Reading, still patterned:** n->m 3 (GAPS23/25 confusion: "nonteerings", "laboratorivn", "[k|i]aner"), all on the [u-dots]
   code, which the GAPS25 call kept on N ij 17/17 at its own threshold; GAPS29's partner gate then put [u-dots] at N ij only 0.55
   (runner-up M y 0.35). These are H-graded letters that the only known-plaintext check says are wrong in 3 of 3 aligned places. A
   verifier cannot settle a sign, but it can say that until they are settled (or downgraded to M), the H count overstates letters
   read right by about the size of that class (17 tokens).
3. **g|l, 46 tokens M:** the sheet-tile method is retired (rule 3, two attempts). The next instrument GAPS29 names, a same-hand
   leave-one-out call with the 4 C-known 2077 g tokens as references (~$4), is a genuinely different instrument and is open.
4. The half-M-right sensitivity FAIL (GAPS22, 4/7) has still not been re-run at M+U 0.231; M+U moved 0.240 -> 0.231 in two
   revisions, so it is unlikely to flip, but it is not re-tested.
Items 2-4 are solver jobs; item 1 is the owner's desk runner. Stage 9 is set only after (1) is answered and a verifier confirms the
class on the reading as it then stands.

**Search log (this session, 3 Oct 2026), phrase searches on the words GAPS25 made readable:**

| family | searched | result |
|---|---|---|
| (e) Google Books (key, country=US, 1.8 s apart) | "paardestallen" Zeelandia Suriname; "geweermakers" "fort Zeelandia"; "secretarye" Zeelandia Wollant; "magasyn" "brandspuiten" Suriname; "arsenael" Zeelandia 1781 Suriname; "water noodige" Zeelandia | 0 / 7 / 503 (not retried) / 0 / 0 / 77. "geweermakers" hits: a 1760 VOC Naamboekje and *Beschrijving van Suriname, historisch-geographisch ...* (1854, several copies; author not checked): 19th-century prose on the fort's workshops, not a transcription of 2077. "water noodige" hits are the Taiwan Zeelandia dagregisters (different fort) |
| (e) IA full text (be-api) | "paardestallen" AND Zeelandia AND Suriname; "geweermakers" AND Zeelandia AND Suriname; Wollant AND secretarye | 0 / 0 / 0 |
| (a)-(d), (f), (g), JSTOR | not re-run: GAPS25/29 add no identifier, sender, recipient, date or new source. JSTOR rows 175-176 stand | -- |

Requests by host: www.googleapis.com 6; be-api.us.archive.org 3.

Safe sentence (2077, replaces VERIFY2's): "Under the period key in NA 1.05.03 inv. 86 (printed in facsimile by de Leeuw 1997 and den
Heijer 2012, p. 471), we read the 2077 (fort Zeelandia) legend at 499 of 658 cipher signs from the key sheet and 7 more from Wollant's
own plain 1782 plan of the same fort (NA 4.VEL 2078), with 102 uncertain and 50 unkeyed. Where the two plans name the same building,
our reading agrees with the 2078 Nota well beyond chance (pre-registered check). No printed transcription of the 2077 legend was found
in the sources searched; de Leeuw 1997 and *Suriname en zijn historie* (1972), which both treat or reproduce the sheet, have not been
read."
Unsafe (unchanged): "first decipherment of the Zeelandia map"; "previously unknown contents of fort Zeelandia"; "we recovered
Wollant's key"; "read in full"; "confirmed against known plaintext" or "verified by 2078" for the whole legend; and, new, any use of
the 0.768 as an independent measure of the GAPS25 fix (see the caveat above).

Postmortem: no over-claim in GAPS25 or GAPS29 (NOTES.md additions checked for first/new/ready/verified wording; none). GAPS25 wrote
"re-class pending" as rule 10 asks. One methodological point recorded above, not an over-claim: the gate that motivated the fix was
re-run as the fix's evidence. No SECOND-OPINIONS-QUEUE.tsv row exists for this target (grep, 06:2x UTC) and none is added: the class
is N1 (provisional), below N3. No CONTRIBUTIONS or outreach.

[GAPS37, 3 Oct 2026 -- rule 10 propagation by the solver, not a verifier pass: reading revised by a same-hand g|l sorting call
(passes/signcmp_gaps37, prereg 34dbb366, 1 blind Opus call, leave-all-out gate on the four C-known g tokens PASS: L06:4 in
form F1, L10:61/L12:26/L12:48 in form F2). 41 of 42 other g tokens moved: g H 25, l H 16 (1 unsettled, L15 approx). 2077 is
now **H 540 C 7 M 61 U 50** (was H 499 C 7 M 102 U 50); decode_key --check exit 0. Words now reading whole include "selve",
"paardestal", "logis", "garnisons", "berging van drooge goederen", "arsenael", "kleingeweer", "geweer", "winkel". GAPS23's
registered gate re-run unchanged: pooled 0.752 (88/117; was 0.768, 86/112), N1 p99 0.453, N2 p99 0.274, 0/2000, PASS; no g/l
mismatch against 2078 in confusion.tsv. Re-class of item 4 is pending a separate verifier.]

### Re-class on the GAPS37 reading (VERIFY4-SURINAME-2077, account-4, verifier, 3 Oct 2026, 06:54-07:0x UTC)

A session separate from every solver on this target (GAPS19-GAPS37, NL18-CORPUS), from REDERIVE-SURINAME-2077 and from
VERIFY-, VERIFY2- and VERIFY3-SURINAME-2077. Rule 10 propagation of GAPS37 (34dbb366 prereg, 456aa471, 369a5752). No decoding,
no vision call; no other target touched.

**Verdict: item 4 stays N1 (provisional), key source period, ceiling N2. Stage 9 ("Novelty verified") cannot be set yet.** The
reading is better than at VERIFY3 and the g|l change is held-out (below); the class is held by the unread editions, not by the reading.

| | VERIFY3 (06:2x UTC) | now |
|---|---|---|
| 2077 cipher tokens (658) | H 499 C 7 M 102 U 50 | **H 540 C 7 M 61 U 50**, M+U 0.169 (41 g tokens M -> H: g 25, l 16; L15:2 left g|l M) |
| `decode_key.py --check` | exit 0 | **exit 0** (06:5x UTC, this session): "ciphertext_2077_legend.tsv: tokens 658: C 7, H 540, M 61, U 50", "reading up to date" |
| GAPS23 registered gate (5 pairs vs 2078 Nota) | 0.768 (86/112), N1 p99 0.455 | **0.752 (88/117)**, N1 p99 0.453, N2 p99 0.274, 0/2000 each, PASS. Re-run here on a scratch copy: passes/nota2078_gaps37/score.py and nota2078.tsv are byte-identical to the gaps25 and gaps23 copies; result.tsv, confusion.tsv and regrade.tsv came out byte-identical to the committed ones |

**Pre-registration order (git).** 34dbb366 (prereg.md, brief.md, build_call.py, queries_key.tsv, query_sequences.txt; 06:38:41 UTC)
precedes 456aa471 (apply.py and the gate copies, 06:41:16, "call still running") and 369a5752 (result.tsv, decisions.tsv, exceptions,
reading; 06:43:58). The gate (four C-known tokens, sure + conf >= 0.6, three l in one form, the g in another), the apply rule and the
class-collapse note are all in the prereg before the call. Order holds.

**Is the g|l change held-out? Yes, and VERIFY3's d/n/q caveat does not carry over.** (1) The class was not chosen from the
GAPS23 gate: g|l had been an open M class since GAPS21 (sheet tiles, retired after GAPS29), named by GAPS29 as the next instrument;
GAPS23's confusion table had no g/l mismatch to motivate it. (2) The call was value-blind: brief.md gives shape nicknames and masked
#k positions only, says nothing about what the signs mean or which four are known, and confines the reader to 26 crops and
query_sequences.txt (2078 not shown). (3) The gate's gain is small and is not what carries the change: 5 newly H g/l letters enter
the five pairs, 2 match and 3 align to 2078 gaps (88/117 from 86/112), so the pooled figure fell slightly; it neither proves nor
disproves the g|l split.

Two limits, recorded rather than failed. (a) The prereg's anchor gate is weak on its own: with the 27/19 F1/F2 split the call
returned, a value-blind random assignment puts #12 in one form and #22/#27/#28 in the other with probability about 0.125
(hypergeometric, this session), and there is a single g exemplar, so the orientation F1 = g rests on one token. (b) That is why this
session ran an out-of-gate check the solver did not: for each of the 41 settled tokens, the line context under the chosen value and
under the swapped value (script on the committed tokens, by eye; the decisions were made blind to values, so word sense is a held-out
test of both the split and its orientation). **30 of 41 make a period Dutch word only under the chosen value and break under the swap**
("'tselve" x2, "nog", "sigt", "'t gouvernement", "magazyn(en)" x6, "paardestalen", "materiaal", "sluys", "defecte gebouwen",
"monteerings", "logis" (l then g in one word, forms F2 then F1), "garnisons", "oly", "berging" x4, "drooge goederen" x2, "arsenael",
"kleingeweer" x2, "geweer(makers)", "winkel"); **9 are neutral** (no word decides: L02:4, L02:25, L03:7, L05:19, L06:29, L06:36,
L09:3, L15:13, L15:15); **2 read a non-word either way**, L08:51 and L10:30, "waater noo[l]e" (l chosen; "nooge" is no better; the
expected "noodige" needs a sign that is neither, so these two H letters may be wrong or the word abbreviated -- a solver question);
**0 are contradicted**. Under the swapped orientation none of the 30 would read. The g|l change is the best-supported change to this
legend so far.

**What still blocks stage 9.**
1. **Novelty, not reading:** LOCAL-QUEUE L36 (de Leeuw 1997) and L41 (*Suriname en zijn historie* 1972; Temminck Groll 1973) are
   both still `queued` on origin/main (fetched 06:5x UTC, empty result column). Until answered the class is N1 (provisional);
   if both come back empty it is N2 (2078's plain Nota gives the content in period Dutch), never N3.
2. **n->m, untested:** the 3 aligned [u-dots] tokens ("nonteerings", "laboratorivn", "[k|i]aner") still read n where 2078 has m;
   GAPS37's prereg rightly excluded them (2077 has no m exemplar, so a same-hand call cannot test it). The 17 [u-dots] tokens stay H;
   until a different instrument settles them or they are downgraded to M, H overstates letters read right by up to that class.
3. **L08:51 / L10:30 "noo[l]e":** two H l tokens that give no word (above); worth one look in the next reading pass.
4. **Half-M-right sensitivity** (GAPS22, FAIL 4/7) not re-run; M+U has moved 0.240 -> 0.169, a larger move than at VERIFY3, so a
   re-run is now worth its cost before anyone cites the judge.
Items 2-4 are solver jobs; item 1 is the owner's desk runner. Stage 9 only after (1) is answered and a verifier confirms the class on
the reading as it then stands.

**Search log (this session, 3 Oct 2026), phrase searches on the words GAPS37 made whole:**

| family | searched | result |
|---|---|---|
| (e) Google Books (key, country=US, 1.8 s apart) | "berging van drooge goederen"; "drooge goederen" Zeelandia Suriname; "kleingeweer" Zeelandia Suriname; "paardestal" Zeelandia Suriname; "garnisons" "logis" Zeelandia Suriname; "geweermakers" "winkel" Zeelandia | 1 / 19 / 9 / 0 / 0 / 5. "berging van drooge goederen": Raad van State 1896 (a warehouse specification, unrelated). Zeelandia hits: 1839-1900 colonial reports and the 1853-54 pilot description; "kleingeweer": van der Aa's Biographisch woordenboek (1852/63), a salute narrative; "geweermakers-winkel ... rondom of in het fort Zeelandia": *Beschrijving van Suriname* (1854, reprinted in a 1981 compilation) -- 19th-century prose naming the same workshop, corroborating content, not a transcription of 2077 |
| (e) IA full text (be-api; control "Zeelandia AND Suriname" = 60 hits, endpoint live) | "drooge goederen" AND Zeelandia AND Suriname; kleingeweer AND Zeelandia AND paardestal; "geweermakers winkel" AND Zeelandia; Wollant AND Zeelandia AND garnisons | 0 / 0 / 0 / 0 |
| (e) Delpher (jsru.kb.nl SRU; www.delpher.nl answers 200) | DTS_document: Zeelandia and Suriname (control 2005); + paardestal; + kleingeweer and arsenael; + "drooge goederen"; same four in BOEKEN | 2005 / 3 / 0 / 0; BOEKEN 0 for all four including the control, so BOEKEN is not a usable collection name here (logged, not a negative). The 3 paardestal hits are 1928-1960 periodicals, unrelated |
| (a)-(d), (f), (g), JSTOR | not re-run: GAPS37 adds no identifier, sender, recipient, date or source. JSTOR rows 175-176 stand | -- |

Requests by host: www.googleapis.com 6; be-api.us.archive.org 5; www.delpher.nl 1; jsru.kb.nl 10.

Safe sentence (2077, replaces VERIFY3's): "Under the period key in NA 1.05.03 inv. 86 (printed in facsimile by de Leeuw 1997 and den
Heijer 2012, p. 471), we read the 2077 (fort Zeelandia) legend at 540 of 658 cipher signs from the key sheet and 7 more from Wollant's
own plain 1782 plan of the same fort (NA 4.VEL 2078), with 61 uncertain and 50 unkeyed. Where the two plans name the same building,
our reading agrees with the 2078 Nota well beyond chance (pre-registered check). No printed transcription of the 2077 legend was found
in the sources searched; de Leeuw 1997 and *Suriname en zijn historie* (1972), which both treat or reproduce the sheet, have not been
read."
Unsafe (unchanged from VERIFY3, plus one): "first decipherment of the Zeelandia map"; "previously unknown contents of fort Zeelandia";
"we recovered Wollant's key"; "read in full"; "confirmed against known plaintext" or "verified by 2078" for the whole legend; any use
of the 0.768 as an independent measure of the GAPS25 fix; and, new, "the anchor gate proves the g/l values" (the 4-token gate passes
by chance about one time in eight; the word check above is the evidence).

Postmortem: no over-claim in GAPS37 (NOTES.md and AUDIT.md additions checked for first/new/unpublished/verified/confirmed/ready
wording; none). GAPS37 wrote "re-class pending a separate verifier" as rule 10 asks, reported the gate fall 0.768 -> 0.752 honestly,
and excluded n->m with a stated reason. One gap in method, not an over-claim: the solver cited newly whole words as support but did
not tabulate chosen-vs-swapped per token; done above. No SECOND-OPINIONS-QUEUE.tsv row exists for this target (grep, 06:5x UTC) and
none is added: the class is N1 (provisional), below N3. No CONTRIBUTIONS or outreach.

[GAPS45-na-suriname-map-1781, solver, account-4, 3 Oct 2026 -- item 4 propagation note, not a verifier pass.] No reading
change. (1) At the current M+U 0.169, the GAPS22 rate-matched gate still PASSes 7/7 with the shuffled-target check clear.
The half-M-right sensitivity still FAILs, 3/7 folds (judge/ratematch_gaps45/), so the caveat this item weighs stands.
(2) A same-hand n|m call (prereg c93d24e2, 1 blind call, gate PASS on 15 plain-letter refs) puts all 17 [u-dots] with the
sheet's plain dotted ÿ (the key's N sign), and none with plain m. The n->m mismatches against 2078 are therefore the
encipherer's own use of the N sign for m, not a misread sign. The reading keeps n. H 540 C 7 M 61 U 50, --check exit 0,
GAPS23 gate 0.752 unchanged. Re-class (if any) stays a separate verifier's.

[GAPS56-na-suriname-map-1781, solver, account-4, 3 Oct 2026 -- item 4 propagation note, not a verifier pass.] Reading
revised in 2 tokens. The n->m on [u-dots] is logged as Wollant's own use of the key's N sign (GAPS45, GAPS55). Of the three
[u-dots] that GAPS23's gating alignment places on a 2078 m, L11:10 and L11:23 pass GAPS23's context clause (ii) and are
now C m (value from the 2078 Nota, entry b). L12:37 fails the clause and stays H n. The rule's clause (i) covers M/U tokens
only, and this extension to H tokens is stated in NOTES.md, "GAPS56". 2077 is H 538 C 9 M 61 U 50, --check exit 0.
GAPS23's gate re-run unchanged gives 0.765 (88/115) vs N1 p99 0.452 / N2 p99 0.278, PASS. The rise from 0.752 is by
construction: two H mismatches became C, which the gate does not count. Do not cite it as independent. VERIFY4's blocker 2
("n->m, untested") is now tested (GAPS45/55) and is partly graded. Blocker 1 (LOCAL-QUEUE L36, L41) is unchanged: both are
`queued` with empty results as of 08:1x UTC. Re-class (if any) stays a separate verifier's (VERIFY5, when L36/L41 land).

[FT4k-na-suriname-map-1781, solver, account-4, 3 Oct 2026 -- item 4 propagation note, not a verifier pass.] Reading
revised in 1 token: L11:21 (sign b, key k|i, M) -> C k, value from the 2078 Nota entry b ("Monteerings Kamer"), under
GAPS23's registered Regrade rule as stated (clause (i) yes; clause (ii) 6/6, and 6/6 with GAPS56's C m tokens counted;
`passes/nota2078_ft4k/decide_l1121.tsv`). It was the knock-on GAPS56 listed and left. 2077 is H 538 C 10 M 60 U 50,
--check exit 0. GAPS23's gate re-run unchanged gives 0.765 (88/115) vs N1 p99 0.452 / N2 p99 0.278, PASS, identical to
GAPS56 (the gate counts H only). Not new evidence. No second-opinion row is filed for this target. Blockers for stage 9 are
unchanged (LOCAL-QUEUE L36, L41 queued). Re-class (if any) stays with a separate verifier (VERIFY5, when L36/L41 land).

[GAPS64-na-suriname-map-1781, solver, account-4, 3 Oct 2026 -- item 4 propagation note, not a verifier pass.] Reading
revised in 1 token: L10:66 (unkeyed [sigma], transcription M, decoded U) -> value e from the 2078 Nota entry b
("Artillerie", final e), under GAPS23's registered Regrade rule as stated (clause (i) binds M only; clause (ii) 6/6;
`passes/nota2078_gaps64/decide_l1066.tsv`). Its exceptions row is C, but decode_key caps it at M by its transcription conf,
as with L11:17. 2077 is H 538 C 10 M 61 U 49, --check exit 0. GAPS23's gate re-run unchanged gives 0.765 (88/115) vs
N1 p99 0.461 / N2 p99 0.270, PASS, same pooled score as FT4k (the gate counts H only). Not new evidence. The same class
[sigma] now aligns to i (L11:17) and e (L10:66); both stay M. No other APPLY token is undecided. No second-opinion row is
filed for this target. Stage 9 blockers unchanged (LOCAL-QUEUE L36, L41). Re-class (if any) stays with VERIFY5.

## JSTOR run (local runner, 4 Oct 2026)

A. J. A. Quintus Bosz, "De geschiedenis van het fort Nieuw-Amsterdam in het verdedigingsstelsel van Suriname", Nieuwe West-Indische Gids 43 (1963-64) 103-148, https://www.jstor.org/stable/41848992 (only hit for ("Redout Leyden" OR "redoute Leiden") AND 1781). Read in the page viewer: the matches are "Redoute Leiden" on pp.125, 127, 129, 140 (p.125 the 1782 defence situation; p.140 its later quarantine use). No mention of Wollant, the 1781 maps, a legend or secret writing. Context only. The other nine Suriname queries (Wollant/geheimschrift, the de Leeuw and AMH phrases, Zeelandia 1781-82, the legend words) returned 0.

## Revision carried in (R10-SURV, verifier of R10-SUR693, account 2, 6 Oct 2026, 07:59-08:0x UTC -- rule 10 propagation, no re-class)
Key change from Texier's glossed cipher letter (NA 1.05.03 inv. 373 scans 0692-0693, Paramaribo 29 Oct 1781; same sign system
as the map key, blind-pass re-test 0.740 vs control p99 0.148, passes/inv373_0693_r10/verify_blind.out): key_period_codes_nieuw.tsv
S, t, [x-dot] M -> C; rows [x-dots] = a (C) and n = z (C) added. Item 4 (2077) now **H 538 C 12 M 63 U 45** (was H 538 C 10 M 61
U 49); `decode_key.py --check` exit 0. Reading change: L01 "planens·t·at" -> "planens·taat" (staat); L05, L08, L14 "nag·syn" ->
"nagasyn" (magazijn, Wollant's N for M). No N-class asked or changed in this pass; the item 4 safe sentence is unaffected beyond the
grade counts. No SECOND-OPINIONS-QUEUE.tsv row exists for this target (checked 6 Oct 2026). Details: NOTES.md "R10-SURV".

## Carry-over (R15-SURV, verifier, account 2, 6 Oct 2026, 17:19-17:36 UTC -- candidate verdicts, no re-class, no key change)
Verifier on R14-SURDP2's descriptive value candidates (inv. 373 per-pair DP) and on R14-SUR2039's "smeederyen" placement on
4.VEL 2039 legend k. Full table in NOTES.md "R15-SURV". R14-SURDP2's dp2_run.py was regenerated from scratch: byte-identical dp2.out and all nine run tsv files (3 min 35 s CPU). The
candidates were pre-registered only as a descriptive output class, with no gate, so every value is post hoc. A grade above M needs
an image check plus agreement with the inv. 86 period sheet.
- 0702 K -> o: **S at most**. On the image the reader's K is the sheet's lowercase k (O row), a reader case split.
- 0758 s -> h: **S at most**. The image shows the sheet's [sh-lig] long-s ligature, which the reader split in two in L04.
- 0758 j -> n: **S at most**. The reader's "i j" is one dotted [ij] sign (sheet N).
- 0702 [thorn] -> c/f: **M**. One checked instance has no glyph of its own (a phantom token).
- 0730 ss-like -> h and f-like -> i: **M**. They fit the sheet's descriptions but were not image-checked.
- 2039 k: the image does not allow s-m-e-e-d-e-r-y-e-n. Pos 1-2 look like one dotted [ij] sign (n), which contradicts m+e. Pos 5 looks
  like [delta-small] (e), which supports it. Pos 7 is a clear separate r (t), which contradicts the drop. "smederyen" is reachable only
  through Wollant's N-for-M habit plus an extra t. Not a reading, not graded above M as a word.
No N-class asked or changed. No key, transcription or reading changed (decode --check not needed). No SECOND-OPINIONS-QUEUE.tsv row
exists for this target.

## Carry-over (R15-SURV2, verifier of R15-SUR758, account 2, 6 Oct 2026, 18:46-18:51 UTC -- key row added, no re-class)
R15-SUR758's re-score (passes/inv373_0758_tok_r15/retok_run.py) reproduces byte-identical; its PREREG (f53d915f1, 18:19:00) predates
the labels and the scored run (2c651efba, 5f7ed3421). Own eye on 3 of the 6 0758 SH tokens and the OTHER token: 4/4 agree with the
labels. [sh-lig] = h is **licensed at C** and entered in key_period_codes_nieuw.tsv: 0730 7/7 (R15-SURALIAS A4) and 0758 5/6, each
past its own deranged-gloss control before pooling (12/13), matching the inv. 86 Nieuw sheet's H row. Labels were not blind to the
earlier hit list (logged). No 4.VEL ciphertext carries [sh-lig], so no map reading or token count changed (decode --check exit 0); the
4.VEL [s-loop]/[s-hook] codes are not aliased to it pending an image comparison. `i j` = [ij] stays M (n=4). No N-class asked or
changed; no SECOND-OPINIONS-QUEUE.tsv row exists for this target.
