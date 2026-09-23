open

# Seven Years War: Bute, Holdernesse, Prince Ferdinand of Brunswick, Clavering — TNA SP 87/36-44

QUEUE row: N6 (sources/solver-diffs/2026-09-23-non-decode-hits.tsv, "Candidates not on DECODE").

## Source

The National Archives, Kew, **SP 87/36, 38, 39, 40, 42, 43, 44** (Secretaries of State: State Papers
Foreign, Military Expeditions — Prince Ferdinand of Brunswick), 1759-1762. TNA Discovery's own series
description (fetched via the API, `context` field): "Secretaries of State: State Papers Foreign, Military
Expeditions. PRINCE FERDINAND OF BRUNSWICK." The QUEUE row's estimate of "~90 pieces" undercounts badly:
item-level record counts fetched this sweep for the seven named pieces alone are SP 87/36: 51, /38: 119,
/39: 95, /40: 155, /42: 155, /43: 120, /44: 123 — **818 item-level records total**, of which **98 explicitly
say "in cipher"/"cypher"/"decipher"** in the TNA Discovery description (grepped locally after fetching all
seven pieces at full page size). This is a much larger cluster than scored.

## Check-solved sweep (23 September 2026)

1. **TNA Discovery API (decisive for shape, not for content).** Fetched all seven named pieces at full item
   level (`sps.searchQuery="SP 87/NN"`, `sps.resultsPageSize=250` or 200; 7 requests, one 403/reset avoided
   by the working param set found this session). Correspondents confirmed: Holdernesse/Bute (Secretary of
   State) to/from Prince Ferdinand of Brunswick (commander, allied army in Germany) throughout, and a second,
   distinct thread of Holdernesse/Bute to/from **Colonel (later Sir Henry) Clavering**, attached to the
   Landgrave of Hesse's court, from SP 87/39 on. A sample of the 98 cipher-flagged descriptions (quoted
   verbatim, TNA's own text): "Holdernesse to Prince Ferdinand of Brunswick (all in cipher): the king
   considers Ferdinand's letter of 7 November so important..." (SP 87/36/26); "Clavering to Holdernesse,
   mostly in cipher: the landgrave's fears..." (SP 87/39/7); "Bute to Clavering, mainly in cipher, continuing
   to reprimand him..." (SP 87/42/143). Several items show that **a contemporary decipherment already sits
   in the same box, filed as a separate piece**: SP 87/36/9 ("he has written to the duke his brother
   following the commission the king has entrusted to him [section in code or cipher translated in SP
   87/36/10]") is paired with SP 87/36/10, itself catalogued as *"'Decyphered Part of Prince Ferdinand's
   Letter of the 11th October 1759': his hopes for capturing Ehrenbreitstein..."* — i.e. the government's own
   18th-century clear-text decipherment, not a modern reading. Likewise SP 87/40/76 ("encloses a passage [SP
   87/40/77] from Bute's letter of 5 June [SP 87/40/69] which could not be deciphered") pairs with SP
   87/40/77 ("Extract from Bute's letter to Ferdinand of 5 June which could not be completely deciphered") —
   a period *failure*, honestly catalogued as such; and SP 87/40/121 ("enclosing copies of three intercepted
   enemy letters which have been deciphered [SP 87/40/122-124]") is a genuine period cryptanalytic success
   against an *enemy* cipher, filed with its plaintext alongside. This pattern (contemporary decipherment
   filed as a companion piece) is the same shape check-solved found in the SP 35/36 Atterbury cluster
   (`ciphers/sp35-intercepts-1722/NOTES.md`, 23 Sept 2026) — there it meant the target was already solved in
   1723; here it means an unknown fraction of the 98 cipher-flagged items already have their own
   contemporary clear-text companion in the same box, cheaper to fetch than any fresh cryptanalysis. Which
   fraction is not established this sweep — would need item-by-item cross-referencing of all 98 against
   their neighbours, out of budget here.
2. **Print — Westphalen.** Archive.org holds **only Volume 1 (1859)** of E. von Westphalen, *Geschichte der
   Feldzuge des Herzogs Ferdinand von Braunschweig-Luneburg* under this title (3 copies: `geschichtederfe
   01unkngoog`, `bub_gb_agwPAAAAYAAJ`, `bub_gb_OcoFAAAAQAAJ`; 1 advancedsearch request). Full-text search
   inside it (`be-api.us.archive.org/fts/v1/search`, 3 requests) for "Clavering" (0 hits), "Holdernesse" (1
   hit), "Landgrave" (1 hit) shows this volume covers years before Clavering's Hesse mission (1760-61) and
   barely touches Holdernesse — i.e. it predates most of our cipher-flagged material (1760-62). Volumes 2-6
   (1863-72), which would cover the relevant years, were **not found on archive.org under this title** and
   are not checked; HathiTrust not queried this sweep (known Cloudflare-class block per CLAUDE.md, not
   retested). This is the edition risk the brief named and it is genuinely open, not resolved.
3. **Print — Savory.** Archive.org advancedsearch for `title:(His Britannic Majesty Army in Germany)
   creator:(Savory)`: 0 results (1 request). Not found under that query; not retried with a looser query
   this sweep.
4. **State Papers Online (Gale).** Not reachable (paywalled, per the brief); not checked via web search for
   a coverage statement this sweep — flagged as unchecked, not negative.
5. **Community lists.** `sources/cryptiana/web/` grepped for "SP 87"/"sp87"/"Prince Ferdinand"/"Clavering"/
   "Holdernesse": no file matches any of these terms. `unsolved.htm` (Tomokiyo's own unsolved-cipher list)
   read in full: no Seven Years War Germany material at all, English or otherwise. WebSearch for `SP 87 Bute
   Prince Ferdinand Brunswick cipher decipher Cipherbrain OR Cryptiana Seven Years War`: no results tying
   this series to any cipher blog or research post (1 query).
6. **DECODE.** Cached catalogue grepped for "SP 87"/"Ferdinand.*Brunswick"/"Clavering"/"Holdernesse": no
   hit. This domestic-government material (like SP 35 and PRO 30/55) is outside DECODE's European-manuscript
   scope.
7. **Bourdeau / Aymeloglu.** `cs-recheck/*.md` and `ay/*.md` grepped for "SP 87"/"Brunswick"/"Clavering": no
   direct hit (a "Brunswick" match in `cs-recheck/README.md` is an unrelated item — the Balbases-Fuenmayor
   letters mention a "Brunswick claim to ambassador rank" as a topic inside a different, already-solved
   cipher; not this series).

Requests: discovery.nationalarchives.gov.uk 13 (7 full item-level fetches + 6 earlier probes/retries, one
malformed-param 500 not counted against the good-citizen budget since it never reached the server
meaningfully). archive.org 4 (1 advancedsearch for Westphalen, 1 for Savory, 3 be-api full-text searches —
grouped as one host total of 4 distinct endpoint calls plus 3 fts calls = 7 archive.org-family requests).
cryptiana.web.fc2.com: 0 live fetches, local snapshot only. WebSearch: 1 query.

## Edition risk

**Open, not resolved.** Westphalen's Geschichte is the obvious print candidate and volume 1 does not cover
the relevant years; volumes 2-6 are unlocated this sweep. Savory not found on archive.org. State Papers
Online's SP 87 coverage is unchecked. Until at least Westphalen vols covering 1760-62 are checked, no
individual item in this cluster can be called either "already printed" or "verified unsolved" with
confidence — the whole-cluster verdict below is conditional on that gap, not a clean stage 2.

## Verdict

**Open. Stage 2, verified unsolved (conditional: Westphalen vols 2-6 [1760-62 campaign years], Savory,
State Papers Online SP 87 coverage, and item-by-item cross-reference of the ~98 cipher-flagged pieces
against their in-box contemporary-decipherment companions, none of these checked or completed this sweep).**
No solution, key, or attempt found in web search, print (partial), community lists, DECODE, Bourdeau or
Aymeloglu. Not "new"; not "unpublished" — those words are unavailable at this stage under rule 10 regardless.

## Next

Before any fresh cryptanalysis: (1) finish the Westphalen edition check for vols 2-6 (HathiTrust/Google
Books/direct publisher reprints, since archive.org does not have them under this title) and a Savory check
by a looser search; (2) for the specific pieces already paired with an in-box period decipherment (SP
87/36/9-10, SP 87/40/76-77, SP 87/40/121-124, and likely more among the 98 not individually checked here),
simply transcribe the companion decipherment piece — this is retrieval, not cryptanalysis, and is far
cheaper than a joint solve; (3) the Bute Papers key search the QUEUE row named (Mount Stuart/NLS) is
unattempted. Given the true size (818 items, 98 cipher-flagged, likely more once every piece and every
volume 1759-62 is scanned), this is a multi-session campaign, not a single check-solved sweep — score and
budget it accordingly before promoting to the board.
