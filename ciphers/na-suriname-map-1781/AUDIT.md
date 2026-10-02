# AUDIT: na-suriname-map-1781 (NA 4.VEL Suriname fortification maps in cipher, Wollant 1781-82)

Verifier: VERIFY-SURINAME-2061 (account-4), 2 Oct 2026, 22:21-22:5x UTC. This session is separate from the
solver sessions on this target (VX-CS04, VX-RD03/B/C/D, GAPS to GAPS12). Rule 10, verifier brief template, steps 1-5.
It did no decoding and touched no other target.

## Verdict (per item)

| item | claim under audit | class | key source | prior plaintext | prior decipherment / key in print |
|---|---|---|---|---|---|
| 1 | the 17-sign key (key.tsv, grade C) and the 2039 legend decode (482 tokens: M 167, U 315, no word read whole) | **N1** for the key and the system. The 2039 legend has no reading to classify. | **ours**: alignment of 2007A against its own on-sheet gloss and the period plain twin 2007B. A **period** key sheet exists (NA 1.05.03 inv. 86, below) and was not used. | 2039: none located (AMH 2025 says "niet getranscribeerd"). The one source that could hold it, de Leeuw 1997, was not read. | **yes**: de Leeuw 1997 describes the system and reproduces "de sleutel tot het geheimschrift" from NA 1.05.03 inv. 86 |
| 2 | 2061 battery list No.1-6 and legend a-g: S 17, M 163, U 88 after GAPS12; cribs 'batterijen' (10 S) and 'wooning' (7 S) | **N0** | **ours** for the crib values (key_2061_crib.tsv; GAPS9/GAPS10 placements against the sheet's own gloss word and AMH's summary) | **yes**: Atlas of Mutual Heritage page 2218 prints the whole No.1-6 + a-g legend in English, after den Heijer 2012 | **yes**: the AMH sentence presents the content as a reading of "the legend in cipher on Wollant's map"; the key is in de Leeuw 1997 |

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
