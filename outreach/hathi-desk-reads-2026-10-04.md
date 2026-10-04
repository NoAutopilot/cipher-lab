# HathiTrust desk reads, 4 Oct 2026 (HATHI-UNLOCKS, account-3 worker)

For the owner's browser (babel.hathitrust.org is Cloudflare-blocked from the cloud). The owner asked on 4 Oct for more volumes
like AOSB I:4 (riksarkivet-r4282-1628). Every htid below was confirmed **Full view** by the HathiTrust Bibliographic API
(`catalog.hathitrust.org/api/volumes/brief/...`) on 4 Oct 2026, 20:0x-20:1x UTC. These are leads only. A hit is a search
result, not a reading, and it says nothing about novelty (rule 10).

**Method limit:** the HTRC Extracted Features API (`data.htrc.illinois.edu/ef-api`) returned HTTP 500 (`MongoError: No primary
node is available`) for all 19 volumes at 20:0x UTC, and again on the one retry at 20:08 UTC. So **no page was flagged by
numeral density or cipher-word tokens**, and there are no scan `seq` numbers. Each row gives a search-inside URL instead
(`.../cgi/pt/search?q1=WORD&id=HTID`) and, where the printed page is known, a page jump (`.../cgi/pt?id=HTID&num=PAGE`; if
`num=` misses, type the page into the viewer's page box). Re-running `tools/htrc_numeral_pages.py` on these htids once EF is
back would add the seq flags. Note on the tool: it writes the 500 error body into `--cache`, so a cache filled during an outage
has to be deleted before a rerun.

What to capture for each hit: a screenshot of the full page plus a zoomed one of the footnotes, the printed page number, and
the scan seq from the viewer's address bar. Paste them into the target's NOTES.md (or hand them to the account-3 orchestrator,
as for AOSB I:4).

## Top 5

| # | Target | Volume (htid) | Why | Search inside / pages |
|---|---|---|---|---|
| 1 | huntington-blathwayt-madrid-1728 | HMC *Report on the MSS of Lord Polwarth* **V** (`msu.31293105166841`) and **IV** (`mdp.39015031910725`) | This is the target's own correspondence (Marchmont papers). BLA 191 was sent from Cessnock, and a copy went to Newcastle on 8 Aug 1729. NOTES.md lists "[ ] print: HMC Polwarth V (1961) for a decipherment of BLA191(a)" as unread. BLA 186's writer is very probably the Abbé Pareti (Rose 1831 prints only "(Cypher.)"). | `Pareti`, `Paretti`, `cypher`, `decypher`, `Cessnock`, `Port St Mary` / `Santa Maria`, `1729`. Open V: https://babel.hathitrust.org/cgi/pt/search?q1=cypher&id=msu.31293105166841 ; IV: https://babel.hathitrust.org/cgi/pt/search?q1=Pareti&id=mdp.39015031910725 |
| 2 | august-van-saksen-1561-64 | Rachfahl, *Wilhelm von Oranien und der niederländische Aufstand* **II.1** (1907) (`hvd.hnt3bj`; second copy `njp.32101073665554`) | II.1 was only ever checked through HTRC token counts (not on IA, Google NO_PAGES). Item 57's Dresden minute "met een 'Zettel'" is the likeliest place for the plaintext in clear. A text read of the Oct-Dec 1561 and 1564 pages could show whether Rachfahl prints or paraphrases it. | `Zettel`, `chiffr`, `Ziffer`, `Chiffre`, `1561`, `1564`, `Kurfürst August`. https://babel.hathitrust.org/cgi/pt/search?q1=Zettel&id=hvd.hnt3bj (the "chiffrierter Zettel" token pages were 1562 per D2: check them anyway and give dates) |
| 3 | riksarkivet-r4282-1628 | AOSB ser. II Bd 1, *K. Gustaf II Adolfs bref och instruktioner* (`mdp.39015026707037`); AOSB ser. I Bd 3, *Bref 1625-1627* (`mdp.39015028586371`) | Same edition family as the AOSB I:4 read. Ser. II prints letters **to** Oxenstierna (per the HathiTrust MARC 505 contents), so it is the recipient side the I:4 read did not cover. Ser. I Bd 3 holds the earlier Camerarius letters, which could mention a cipher or key being sent. No Camerarius volume exists in ser. II (MARC 505 lists all 14). L46 searched Riksarkivet's online AOSB texts (no 1628 hit), and it is not clear that covers ser. II. | `chiffer`, `cifra`, `ziffer`, `characteres`/`characteribus`, `clavis`, `Camerarius`, `dubitatur`, `expensas`, `Stralsund`. https://babel.hathitrust.org/cgi/pt/search?q1=chiffer&id=mdp.39015026707037 ; https://babel.hathitrust.org/cgi/pt/search?q1=Camerarius&id=mdp.39015028586371 |
| 4 | ra-karlxi-fullmakt-1677 | *Sverges traktater med främmande magter*: **v. 8 pt. 1-2** full view (`nyp.33433090738414`); v. 6 pt. 1 search-only (`nyp.33433090738372`) | NOTES.md keeps the target from stage 2 until "the Sverges traktater volume-7 question" is resolved. Bib API, 4 Oct 2026: HathiTrust holds v. 1-4, 8, 10-14 in full view and v. 5-6 search-only, with **no v. 7 at all** on this record (OCLC 11777373). A full power of 1677 would sit in v. 7 or v. 8. | Open v. 8 pt. 1 title page and contents and note its date range. Search-inside (this also works on the search-only v. 6) for `1677`, `fullmakt`, `plenipotentia`, `Carolus`. https://babel.hathitrust.org/cgi/pt?id=nyp.33433090738414 ; https://babel.hathitrust.org/cgi/pt/search?q1=1677&id=nyp.33433090738372 |
| 5 | sp90-raby-1704 | Riezler, *Geschichte Baierns* **Bd 7** (1913) (`mdp.39015014685286`; second copy `uc1.b3277768`) | NOTES.md: pp. 602-603 ("Max Emanuels Forderungen" / "preußische Mediation", "Raby anweisen, alle Zugeständnisse an Baiern zu billigen") are reachable only as Google snippets. A page read gives the Bavarian promemoria's points as context words (a possible crib list for the Reichart-Berlepsch channel). This is not plaintext of the target. | Pages 602-603 plus footnotes: https://babel.hathitrust.org/cgi/pt?id=mdp.39015014685286&num=602 ; search `Raby`, `Berlepsch`, `Reichart` |

## Already queued HathiTrust desk rows (htid added where found)

| LOCAL-QUEUE | Target | htid | Note |
|---|---|---|---|
| L44 (queued) | bowes-walsingham-1583 | `nnc2.ark:/13960/t1gh9nc18` (CSP Scotland vi) | pp. 370-371, 566-568, asterisks and "In cipher" footnotes. Best value of the queued rows (the calendar prints deciphered text). |
| L30 (queued) | fr4715-f61-mayenne-1592 | not found (Open Library has no record for "Correspondance du duc de Mayenne", so there is no OCLC for the bib API) | desk catalogue search remains the route |
| L3 (queued) | fr2980-gramont | Le Grand, *Histoire du divorce* v. 3 is `njp.32101037456694` (already read from the MDZ scan) | L3 is a whole-HathiTrust phrase search, unchanged |
| L4 (queued) | eckert-1864 | (not resolved) | unchanged |
| L38 (queued) | berthier-napoleon-1812 | Bazeries 1896 *Les "chiffres" de Napoléon Ier* is full view at `hvd.hnxw98` | the target is now found-solved, so this is low priority: grand chiffre 34 tables pp. 19-36 if wanted for KEY-DESIGN |

## Checked and dropped (no desk read needed)

- lodewijk-van-nassau-1573-74, Blok 1887 (`nnc1.0036704156`, full view): superseded (contents read from page photographs, 24 Sept 2026).
- sachsstaatsarchiv-manteuffel-1712, Acta Borussica *Behördenorganisation* I (`njp.32101065980920`): done another way (AUDIT2-MANT, Google Books full view).
- fr16142-noailles-constantinople-1571 (Charrière III), jan-van-nassau / willem-van-hessen / wvo-hessen (Groen van Prinsterer), fr16106-vivonne-longlee-1579 (Mousset 1912), sp77-nicholas-1659 (Nicholas Papers IV): all full view on HathiTrust, but each has already been read in full from IA or DBNL text.
- hamilton-1650 (OCLC 1828960), armstrong-madison-1808, pro3055-clinton-1779 (OCLC 11013774), fr16104-vivonne (OCLC 988579745), debosnys-1883: no HathiTrust items.
- fr3416-nevers-fils-1589 (`mdp.39015059979289`), fr4687-paleologue-nevers (`mdp.39015062439453`), rah-salazar (`osu.32435013919725`): search-only, not full view.

## Requests

HathiTrust Bibliographic API 47 (>=1.6 s apart); HTRC EF API 20 (19 + 1 retry, all HTTP 500); Open Library search 11. No subagents.
