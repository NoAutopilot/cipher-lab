open
Klaus Schmeh, Cipherbrain, "Update: Five encrypted radio transmissions from a New York Nazi spy" (13 Jul 2021, saved sources/schmeh/posts/47b-koehler-update-2021.txt, re-read by this worker 25 Sept 2026) and its predecessor "Still unsolved: ..." (4 Jul 2021, fetched live by this worker 25 Sept 2026) both state the solution is unknown; both read in full by this worker, not just quoted from a prior pass.

## Target

Five short letter-cipher messages (237, 178, "137"/140, 140, 229 letters, 924 letters total) quoted in a German
teleprinter letter addressed "An Abwehrleitstelle Frankreich, Paris Funkstelle -- Sofort vorlegen! -- Betr.:
Koehler", February 1944. David Kahn published the letter and its five cryptograms in Cryptologia 5(2), April
1981, from a copy he found in the British archives (Kahn's own footnote, not yet independently traced by this
worker -- that is job GOLD-1A's archive lookup, not this one's). Schmeh's Cipherbrain blog (scienceblogs.de)
reproduced Kahn's text in three posts (2013, 2017, 2021) and it is Schmeh's Top 50 unsolved list, no. 47.

Sender: Walter Koehler, Dutch engineer recruited by the Abwehr in the late 1930s, sent to New York, ordered back
to Germany in 1941 over suspected embezzlement, returned to the US in 1942 and confessed his espionage mission
to US officials at the Madrid consulate, after which the FBI ran him as a double agent from a New York hotel.
The FBI-controlled radio channel to Hamburg used a book cipher on a Dutch-language prayer book (Hoover 1946,
"The spy who double-crossed Hitler", American Magazine, quoted by Schmeh). The five messages Kahn found went to
Paris, not Hamburg, and (per Schmeh, from David Alan Johnson's Warfare History Network article) are read as
Koehler's own, true reports sent behind the FBI's back -- so probably not in the prayer-book cipher, though
Bourdeau's repository (below) notes the routing also allows Hamburg forwarding the FBI channel's own traffic on
to Paris unread, which would put it back in that system.

## Established vs inferred

- H (from the source, Schmeh's 2021 reproduction of Kahn 1981): all 924 ciphertext letters as transcribed here.
- I (inferred, not verified against an image): the letter groups themselves, since Schmeh's page is a
  transcription of Kahn's 1981 journal page, not a photograph of it (rule 2) -- and a second transcription
  (Bourdeau's cyphersolver repo, below) disagrees with ours on six individual letters. Neither transcription has
  been checked against an image of the Cryptologia 5(2) page or the original TNA-held letter by this worker.
- No plaintext exists anywhere in the sources checked (all say the solution remains unknown).

## Known transcription discrepancy -- NOT repaired (rule 2, "never silently repair")

Diffed our ciphertext.txt (from sources/schmeh/posts/47b-koehler-update-2021.txt, the spec's source) against
`abwehr/msgs.py` in dbourdeau/cyphersolver (git clone, grepped 25 Sept 2026, MIT-licensed code / CC BY 4.0 text,
credited here per rule 8). Bourdeau's file states one explicit correction ("Norbert's corrections, Schmeh 2017
comment #7; Schmeh's 2021 repost": msg "137" group 9 `ayddg` -> `ayddq`) but in fact differs from our copy at
six group positions total, all single-letter, all classic transcription/OCR confusions:

| msg (Kahn header) | group # (1-indexed) | ours (Schmeh 2021, this worker's source) | Bourdeau's msgs.py |
|---|---|---|---|
| 237 | 15 | nogex | mogex |
| 178 | 9  | gwymn | gwwmn |
| 178 | 36 (last) | avl | evl |
| 137 | 9  | ayddg | ayddq (Bourdeau's one explicitly-flagged correction) |
| 229 | 28 | hkisf | hklsf |
| 229 | 40 | albon | alhon |

Message "140" (the fourth) matches exactly between the two copies. Bourdeau's profile.json says the whole file
was "checked against the Cryptologia printing" but explicitly counts only 1 correction, so the other five
differences are unexplained by that note -- possibly present already in whatever earlier Schmeh post or reader
correction Bourdeau started from, not confirmed by this worker against Kahn's page or an image. Per rule 2 this
worker has NOT changed ciphertext.txt to match either version; both readings are recorded here for whoever next
gets an image of Cryptologia 5(2) p.69 (identified below) or the TNA original. `flag`ged in ROOM.md.

## Check-solved search log (this worker, 25 Sept 2026, date -u confirmed 16:47-16:58 UTC)

1. **Kahn's own 1981 article, Cryptologia 5(2) (April 1981).** Located on Internet Archive as
   `sim_cryptologia_1981-04_5_2` (be-api.us.archive.org full-text search, `q=Koehler+cryptogram+Abwehr`, one
   request, 200): the article is "GERMAN SPY CRYPTOGRAMS" by David Kahn, page 69 (be-api's `page_num` field is
   not a real page locator per CLAUDE.md's Access playbook note -- logged, not cited as a page number).
   printdisabled/sim_microfilm collection, lending-only, this worker did not borrow it (out of scope for
   intake). Scoped full-text search inside that one identifier for "Koehler solution solved" (`identifier=
   sim_cryptologia_1981-04_5_2`) returned zero hits -- no mention of a solution in the article itself, a search
   result not a proof of absence since only OCR text was searched. 3 be-api requests total, >=1.5s apart, no
   429/403.
2. **The Cryptologia index since 1981** (OpenAlex, header `Authorization: Bearer $OPENALEX_KEY`; Semantic
   Scholar, header `x-api-key: $S2_KEY`; CrossRef, no key): OpenAlex `works?search=Koehler cipher Abwehr` (1
   irrelevant hit, a 2022 German-language "Registratur der Quellen"), `works?search=Cryptologia Koehler spy
   cryptogram` (0 hits), `works?filter=primary_location.source.id:S4210191193&search=Koehler` (0 hits, wrong or
   empty source-id filter, not retried further). Semantic Scholar 429'd on the first Koehler-specific query
   despite the key (matches CLAUDE.md's Access-playbook note that S2 sometimes still 429s with the key); one
   retry after a 3s pause on a near-identical query succeeded (200) but again 0 Koehler hits among 22 results for
   "Koehler cryptogram unsolved" (Kipling, Sator Rebus, Dorabella, Zodiac Killer papers, nothing on Koehler).
   CrossRef `works?query=Koehler+cipher+Abwehr+spy` returned 10 items, all noise (an unrelated "Hugo William
   Koehler" naval-attache letters collection; German psychoanalysis papers using "Abwehr" as the ordinary German
   word for psychological defence). 6 requests total (2 OpenAlex, 2 Semantic Scholar, 1 CrossRef, plus 1 retry),
   >=1.1-1.6s apart.
3. **Schmeh's 2021 posts and comment thread** (scienceblogs.de, one live re-fetch of the earlier "Still unsolved"
   post plus its German comment thread, as the brief allows; the saved copy of the later "Update" post was used
   without refetching). Read in full: both posts explicitly say the cipher (not just Koehler's identity) is
   still unsolved -- "Update" (13 Jul 2021): "The solution remains unknown to this day"; "Still unsolved" (4 Jul
   2021, fetched live, article:published_time meta confirms 2021-07-04): after readers confirmed Koehler's
   identity, Schmeh's own reply in the German comment thread (comment #12, 6 Jul 2021, read in the live fetch of
   the German-language page, which is where this post's comments live) says "As it seems, Koehler used an
   unknown method for these five radio messages. I'm afraid it will be difficult to break these" -- i.e. the
   identity mystery (comment #3) was solved, the cipher was not. All 13 comments on that thread (4 Jul - 17 Oct
   2021) read: readers proposed Phillips cipher, ADFGX+substitution, Enigma-family, and one commenter's remark
   (#11, garbled German, not a real plaintext candidate) -- none is a solution, none since disputed or confirmed
   as a reading by Schmeh. 2 scienceblogs.de requests (English post via WebSearch-found URL, German post for
   comments), 1 GET each, no login, no 429/403.
4. **Bauer, Unsolved! (2017/2019).** Google Books API (`&country=US&key=$GOOGLE_BOOKS_KEY`): located the volume
   (id `l8iXDwAAQBAJ`, Craig P. Bauer, "Unsolved!", PARTIAL viewability) via `q=Bauer+Unsolved+History+Mystery+
   Greatest+Ciphers`, but could not search inside it for "Koehler" specifically -- the Books API's `q=` search
   does not support an in-volume full-text scope, and `q="Koehler"+inauthor:Bauer` returned 300 unrelated hits
   (author-name collisions on "Bauer", not this book) rather than a real in-book search. This edition was NOT
   independently opened/searched by this worker; recorded as unread, not as a negative (rule 2/intake gate). IA
   full-text search for `"Koehler cryptogram" solved` (whole-corpus, not Bauer-scoped) returned 0 hits; a
   broader `Koehler spy cryptogram` search's first 50 hits (of 5237 total, mostly noise on the common words
   "spy"/"cryptogram") surfaced only the Kahn 1981 article itself and Kahn's own "Seizing the Enigma" (unrelated
   book, matches on "spy"/"cryptogram" as words) -- no Bauer volume, no solution claim. 5 Google Books requests,
   1 IA fts request, all 200, >=1.5s apart.
5. **Cipher Mysteries** (ciphermysteries.com, WordPress search). `?s=Koehler`: "Nothing Found". `?s=K%C3%B6hler`:
   one hit, "The elusive Reynolds: from HC to C...?" (2012), an unrelated post (Reynolds cipher) that merely
   contains the string "Köhler" somewhere in its text/sidebar, not a Koehler-cryptogram post. 2 requests, 200,
   >=1.5s apart.
6. **DECODE (de-crypt.org).** Not re-fetched live -- grepped the existing login-free listing snapshots in
   sources/decode/ (records-non-decrypted-2026-09-24.tsv, 1187 rows; records-decrypted-2026-09-24.tsv, 1361
   rows; both fetched 24 Sept 2026, one day old, cipher-record-type listing) for "koehler", "köhler", "abwehr":
   zero hits. Consistent with the DECODE catalogue's contents being pre-20th-century archival ciphers (dates
   checked: no entry later than the 18th-19th century in a spot sample); a 1944 espionage item would be outside
   its normal scope. No live DECODE requests made by this worker (none needed; spec's "not on DECODE" from 24
   Sept 2026 stands).
7. **Solver repositories.** `git clone --depth 1` of both (as the brief allows, "clone only to grep"), 25 Sept
   2026:
   - **dbourdeau/cyphersolver** (MIT code / CC BY 4.0 text -- credited per rule 8): has a dedicated `abwehr/`
     folder with `NOTES.md`, `profile.json`, `msgs.py`, `periodic.py`, `lm.py`. TARGETS.md row 47: "Köhler,
     Abwehr 1944 | skipped | **ATTEMPTED 2026-09-15, skipped as intractable.**" This is a real, matched-control
     cryptanalytic campaign (their own words, one Claude-Opus-5 session, 15 Sept 2026) that ruled out, against
     shuffled/simulated controls: monoalphabetic substitution, transposition and ABC-Verfahren (IC 0.0398 vs
     German 0.076 / random 0.0385); periodic Vigenere/Beaufort/variant-Beaufort periods 1-26 in de/en/nl
     (quadgram hill-climb vs shuffled-ciphertext controls); ciphertext autokey offsets 1-40; standard-tableau
     running key and Gronsfeld (likelihood vs true running-key/shuffled controls); any Enigma wiring (letter
     counts chi-sq 57.9 vs uniform, p=0.0003, vs simulated Enigma-like German output). Their own outcome field:
     `"method": "not solved"`, `"class": "not read"`, `"fraction_read": 0`. Two systems left un-excluded by their
     tests: a mixed-tableau (keyed) running-key Vigenere, or a hand one-time pad/random key table -- both judged
     to have no practical ciphertext-only attack without the book or the FBI's plaintexts. This closely matches
     and extends our own spec's cheap_test_done (pooled/periodic IC, Kasiski, 24 Sept 2026 LANE B): both find a
     flat, near-uniform letter distribution and rule out short fixed-period Vigenere-family systems; Bourdeau's
     pass additionally rules out Enigma, autokey, Gronsfeld and standard running-key with controls, which our
     spec's cheap_tests_in_order had not yet run. This is a documented negative with controls, not a solve --
     status stays open, not closed-negative (that word is for our own control-backed negative, not one we are
     citing).
   - **aaymeloglu/unsolved-ciphers**: grepped for "koehler"/"köhler" (case-insensitive, whole tree excluding
     .git): zero hits.
8. **A search engine (WebSearch), incl. the model-solve family.** Queries run: "Koehler cipher solved Abwehr
   1944 Paris Funkstelle" (all hits are Schmeh's own blog posts, still-unsolved every time, plus unrelated
   cryptology sites -- CryptoCellar, Funkspiel/Wikipedia, Cryptomuseum -- none mentioning a Koehler solution);
   "Köhler 1944 Kryptogramm gelöst Kahn" (same posts, confirms unsolved, plus one irrelevant "Langie-Kryptogramm:
   Rätsel gelöst" -- a different, already-solved cipher, not this one); "\"Koehler cipher\" solves Claude GPT AI
   2026" (zero hits naming Koehler; the model-solve family is real for other targets -- Vals AI/Claude Fable 5.1
   on Urquhart's Cyphral Distich, 31 Aug 2026, and the HAWK post-quantum cipher break -- but none for Koehler);
   "Walter Koehler Abwehr spy Warfare History Network Johnson decrypt" (surfaces the Johnson article itself and
   Schmeh's posts quoting it; no decrypt claim). "FBI Vault Walter Koehler spy file NARA decrypt": surfaces
   archives.gov's RG 65 FBI-records name index PDF (name entry "Koehler, Walter -- see Kohler, Walter", i.e. a
   catalogue cross-reference, not a released file) and vault.fbi.gov's general reading-room search page; no
   decrypt content found by search (a real archive lookup, e.g. actually querying vault.fbi.gov/search or the
   RG65 finding aid for a Kohler/Koehler file, is job GOLD-1A's, out of scope here).
9. **Johnson's Warfare History Network article and any FBI/NARA page on decrypts.** The article itself
   (warfarehistorynetwork.com/walter-koehler-j-edgar-hoover/) is Cloudflare-challenged from this environment:
   plain curl returned HTTP 403, and one retry via the browser tool (tools/browser_fetch.js, the allowed single
   retry) timed out against a Cloudflare challenge host (brunhild.challenges.cloudflare.com, connection
   rejected by the egress proxy) -- logged as unreachable, not retried further (good-citizen rule). Its content
   is available second-hand through Schmeh's two posts, which quote it at length (Koehler's recruitment, 1941
   recall over embezzlement, 1942 return, Madrid confession, FBI double-agent status, prayer-book cipher on the
   FBI channel) and through WebSearch snippets of the article and a related piece ("Military Secrets: The Nazi
   Spies Who Never Were"); none of these mention a decrypt of the five February 1944 messages themselves --
   Johnson's article is a biographical/historical piece, not a cryptanalytic one. No FBI or NARA page with a
   decrypt of these specific messages was located; the RG 65 name-index cross-reference above is a lead for
   GOLD-1A's archive lookup, not a decrypt.

## Verdict

**open.** Not solved in: Kahn's own 1981 article (as far as its OCR text can show); the Cryptologia citation
index since 1981 (OpenAlex/S2/CrossRef); Schmeh's three Cipherbrain posts (2013/2017/2021) and their full comment
threads; Bauer's Unsolved! (unread, not searched -- logged as unread, not as a negative); Cipher Mysteries;
DECODE's catalogue (a scope mismatch, not a real check); both solver repositories (Bourdeau has a real,
control-backed negative campaign, 15 Sept 2026, calling it "skipped as intractable", not solved; Aymeloglu has
nothing); a general web search including the model-solve-announcement family; and no FBI/NARA page located shows
a decrypt. Status matches specs/koehler-1944.json's `status_24_Sept_2026` field and CLAUDE.md rule 10: nothing
here is claimed as new, unread or unpublished, only "not found in the sources listed above, searched by the
method above, on 25 Sept 2026."

## Intake gate

$ python3 tools/intake_gate_check.py koehler-1944
koehler-1944: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit code: 0

## Next steps (one-line suggestions only, per Usage rule 7 -- not run here)

- GOLD-1A (already the spec's own next-ranked route): TNA Discovery API for Kahn's British-archives source file
  and HW 19 ISOS/ISK Abwehr decrypts; FBI Vault / NARA RG 65 "Kohler, Walter" (name-index cross-reference found
  above, not yet opened).
- Whoever runs cheap_tests_in_order item 5 (book cipher) should use Bourdeau's `abwehr/` scripts (periodic.py,
  lm.py) as a starting point rather than re-deriving them (MIT licence permits copying, cite per rule 8), and
  should resolve the six-group transcription discrepancy above against an image first (rule 2) since a wrong
  letter in a 924-letter ciphertext-only problem is exactly the kind of error a book-cipher letter-arithmetic
  search cannot tolerate silently.
- GOLD-K1 (25 Sept 2026): the devotional-register key-corpus lever is now spent for Family B and B' (both stay
  control-backed negatives under `tools/data/nl_dev`, the Statenvertaling, same as under nl20's novels) --
  next is B'' (general permuted tableau, cycle-3 candidate per GOLD-CONS1) or a Catholic Dutch prayer book
  specifically, if one turns up through a route other than dbnl.org/gutendex.com (both unreachable this pass).
- GOLD-2C (25 Sept 2026): family B' (keyed-tableau running key) is a control-backed negative for keyword-mixed
  alphabets (control 72.6% read, target at the one-time-key noise band; HYPOTHESES.md "Family B'"); step 1 puts the
  target's letter counts inside the keyed-running-key band and outside the uniform one-time-key band, so a
  hand-made non-uniform key is not excluded. Cheap remaining B' variants, each one box: `--param arith=beau`, a
  German key (`kcorpus=tools/data/de20`), an English word list; otherwise family C or A next, as GOLD-2A said.
- GOLD-K3 (25 Sept 2026): the cipher-side placements of the keyword-mixed tableau (`mixed_tabula` modes cipher/
  plaincipher/keycipher, added this job) are a control-backed negative for vig and beau arithmetic (controls
  76.9%/75.2%, targets -3.498/-3.518, both inside a new ten-text beau-pipeline noise band -3.5481/-3.5305/-3.4944);
  `--param modes=plaincipher,keycipher --param arith=vig` is owed (built and tested, not run, ~20-25 min box).
  Six of seven `mixed_tabula` placements are now spent at vig/beau (plain, key, both, full, cipher; GOLD-B2D's
  general cipher-side permutation search separately failed its own control at this N); varbeau arithmetic and the
  two remaining mixed pairs are what is left of the keyword-restricted keyed-tableau search before family C or A.
- GOLD-B2D (25 Sept 2026): family B'' (general permuted tableau) is built as `tools/families/permuted_tableau.py` and its
  first sub-family B''-c (free cipher-side permutation) reads its matched control at 9.5 pct (7.4/12.9/8.1, gate 0.5 not
  met, target not run): at 924 letters neither a sum-stream n-gram proxy nor an open-tableau beam identifies S3, and the
  decoder objective is climbable only within about 3 swaps of the truth (HYPOTHESES.md "Family B'', permuted tableau").
  Park B'' unless a search with the decoder's power at the proxy's price appears; GOLD-K3's keyword-restricted cipher-side
  placements are the live corner of the cipher-side family.
