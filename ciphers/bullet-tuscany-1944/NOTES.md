# bullet-tuscany-1944

partial

Search record (rule 1, reused from specs/bullet-tuscany-1944.json and UNSOLVED-SURVEY.md row 20, both
LANE B2 25 Sept 2026): Cipherbrain post 44 (Schmeh, 4 March 2017, "The Top 50 unsolved encrypted
messages: 44. A WW2 encryption hidden in a bullet") read in full from sources/schmeh/posts/44-bullet.txt,
including its 9-comment thread, on 25 Sept 2026 -- no accepted solution posted there; Schmeh explicitly
rejects the forum "solution" reported by SPLOID (January 2015) for lacking a method. Both solver
repositories (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers) checked by LANE B2, no hit. This
session (bBUL3, 25 Sept 2026, 21:38 UTC) added one full-text search each on OpenAlex
(`search=bullet cryptogram Tuscany 1944`, key from the environment, 0 results) and Semantic Scholar
(`query=bullet cryptogram Tuscany 1944`, key from the environment, 0 results) -- no scholarship indexed
under this description. Two cheap tests already run with matched controls (specs/bullet-tuscany-1944.json
`cheap_test_done` 1-2; NEAR.md row): the forum "solution" is mechanically excluded, Caesar and 93
header-derived keys are excluded, periodic keys of period 2-8 are not testable at N=44 (control below
gate). Status stays `partial` per rule 5's amendment (a control-backed gap is never `closed-negative`).

## Indicator-system lookup (this job, bBUL3)

Task: identify what system a header of the form `QM / ... / 605YZ/FF` belongs to, from print WW2
signals literature, before spending more on a solver at N=44. Sources tried: archive.org full-text
(be-api fts and advancedsearch) and Google Books (key + country=US), one request at a time, >=1.5 s
apart. Cipherbrain's own comment thread (already on disk, read above) is quoted first because two of
its readers independently proposed period-plausible readings of the header text itself (not a cipher
system, but a candidate plain reading of the metadata lines) -- recorded here as prior art on the
header, distinct from the print-literature search this job's brief actually asks for.

Cipherbrain thread readings of the header (comment #4, Bernhard Gruber, 6 March 2017; comment #5, Max
Baertl, 6 March 2017; sources/schmeh/posts/44-bullet.txt lines 311-327): "605YZ" read as "605th" (the
605th Ordnance Ammunition Company, part of the 87th Ordnance Battalion Headquarters and Headquarters
Detachment, stationed in Tuscany in 1944); "FF" guessed as a misreading of "HH" for "Headquarters and
Headquarters Detachment"; "QM" guessed as "Quartermaster". These are readers' guesses at what the
header *says*, not a citation to a signals manual describing an indicator system of this form -- kept
separate from the table below, which is this job's own lookup against printed WW2 signals sources.

### Checklist (applied to every header below, control and target alike)

1. Alphabet: letters-only, digits-only, or mixed.
2. Group shape: fixed group length(s), a slash separator present or absent, a trailing digraph.
3. Position: does the group run together as one string, or is it split into a prefix line and a
   separate suffix line around the body?
4. What the source says the group *is* (an enciphered indicator vs a plaintext heading field).

### Candidate systems checked against print sources

| System | Printed header/indicator form (source, locator) | Does QM / 605YZ/FF fit? | Test it would license | N=44 feasibility |
|---|---|---|---|---|
| M-209 (Converter M-209 / Hagelin), TM manual | "the system indicator, WW in this example, message indicator, DKSLG/J in this example, and key-list indicator" -- system indicator = 2 letters; message indicator = a group of 6 letters "selected at random by the operator" (par. governing message-indicator selection); key-list indicator = a digraph giving the pin/lug setting, substituted by the system indicator when omitted. archive.org `converterm209m2000unse` ("Converter M-209, M-209-A, M-209-B"), par. 23 and the paragraph naming "WW"/"DKSLG/J" (full-text search, quoted above; the item's `page_num` field is not a real page locator per this repo's Access playbook note on IA full-text search, so cited by paragraph/quoted text, not a page number) | **Partial.** Shape matches closely: a short (2-letter) code + a 5-character group + `/` + a short trailing code is exactly the printed example's `WW ... DKSLG/J` shape, and QM (2 letters) sits where the manual's system indicator sits. But the manual is explicit the message/key-list/system indicator groups are letters-only ("group of six letters", "a digraph"); 605YZ mixes 3 digits into the group, which the manual's own worked example never does. Position also differs: the manual's indicator groups run together as one unit near the ciphertext, not split into a top line (QM) and a separate bottom line (605YZ/FF) as Schmeh transcribes it. | If treated as indicator material despite the digit violation, the natural test is to use the footer's letters (Y, Z, F, F) as key/setting material -- **already run**: cheap test 2 (`cheap_test_done.2`, run_test2c.py) tried the footer letters (`YZFF`) as a key under Vigenere/Beaufort/variant-Beaufort and Caesar, 0/93 candidates passed the judge, matching the random-text noise ceiling. No further M-209-indicator-shaped test is licensed by this lookup. | Not feasible as a genuine M-209 attack: a real M-209 key/lug/pin recovery from known- or guessed-plaintext needs on the order of a few hundred letters (six overlapping wheel periods, longest 29); 44 letters is far short. Only the already-run key-string test (test 2) was ever feasible at this N, and it is done. |
| US Army standard message form, FM 24-5 (1942) | "insert precedence in the space at the upper right of the message form ... the use of a serial number ... inserted on the first line ... after the word 'No.' ... After the word 'Date' [insert it, e.g.] 15 Jan 41 ... After the word 'To' ... insert the official designation of the addressee." Separately: "a two-figure date group [precedes] the four-digit time group ... For example, 080600 is the 8th day of the month and the time is 6:00" (a pure 6-digit date-time group). archive.org `FM24-5BasicFieldManualSignalCommunication` (1942), "Message Form" section and the date-time-group paragraph (full-text search, quoted above; same `page_num` caveat as the M-209 row) | **No.** The heading fields FM 24-5 actually prescribes (precedence word, serial number after "No.", a spelled date like "15 Jan 41", an addressee's official designation, a pure-digit date-time group like "080600") never take the shape of a 2-letter code standing alone on its own line, nor an alphanumeric group with an embedded `/`. If QM is an addressee designation abbreviation (Quartermaster -- also the Cipherbrain thread's own guess, comment #5, Max Baertl, 6 March 2017), that is a plaintext heading word, not part of a cipher/indicator system, and outside this lookup's scope. | None -- this is a plaintext-heading form, not a cipher system, so no cryptanalytic test follows from it. | n/a |
| SLIDEX (RT code), Kruh, "The SLIDEX RT Code", *Cryptologia* 8:2 (April 1984), p.162 | The Slidex card mixes letters and digits ("letters ... and numbers on the card"; sample fragment from the OCR: "OS 32 CORR OW TONIGHT TRANSMITTERS TRANSPORT"). archive.org `1984-04-cryptologia`, p.162 (page number read directly from the article's own printed running head in the OCR text, not from the unreliable `page_num` field) | **No new information beyond the spec's existing rejection.** The spec already excludes Slidex for the 44-letter *body* because Slidex groups mix letters and digits and the body is letters-only. This lookup's full-text search of Kruh's article found no description of a Slidex message *header* or indicator convention distinct from the card groups themselves (no hits for "indicator" or "call sign" in this article by full-text search) -- so Slidex offers no separate indicator-system match for QM / 605YZ/FF to be tested against; the header's own letter+digit mix (605YZ/FF) is at least compatible with Slidex's card alphabet in the abstract, but with no printed indicator convention on file to compare it to, this is not a fit claim, just an absence of a counter-example. | None licensed -- no printed indicator form to test the header against. | n/a |
| M-94 / M-138 strip ciphers | Not found: no printed message-indicator or header convention for these devices turned up in this lookup's IA search (only modern replica/hobbyist and Friedman-correspondence items indexed under "M-94"). Per the spec's own note, these are named only as possible backup devices, not committed to. | Not tested -- no printed indicator form on file to compare. | None. | n/a |

### Control check (rule 3, for a lookup)

Applying the checklist above to two headers of *known* system, printed in the same literature, before
applying it to QM / 605YZ/FF:

- **Control A -- M-209's own worked example, "WW ... DKSLG/J".** Alphabet: letters-only (confirmed by
  the manual's own wording, "group of six letters", "a digraph"). Group shape: short code + 5-character
  group + `/` + short code -- matches the checklist's M-209 criteria by construction, since this *is*
  the manual's own example. Classified: M-209 external indicator. Correct (it is one, by definition).
- **Control B -- FM 24-5's date-time group, "080600".** Alphabet: digits-only. Group shape: one
  6-digit block, no slash, no letters. Classified: plaintext message-heading date-time group, not an
  M-209 indicator (fails the letters-only test) and not a match for QM / 605YZ/FF's shape (no slash,
  no letters, single block not split top/bottom). Correct (that is exactly what FM 24-5 introduces it
  as).
- Both controls classify correctly under the same checklist used on the target below: **2/2**.
- **Target -- QM / 605YZ/FF.** Alphabet: mixed (QM letters-only; 605YZ/FF has 3 digits and 2 letters).
  Group shape: 2-letter code (matches M-209's system-indicator length) + 5-character group + `/` +
  2-letter code (matches M-209's message-indicator + key-list-indicator shape in length and slash
  position) -- but violates M-209's letters-only rule, and fails FM 24-5's date-time-group shape
  entirely (mixed alphabet, has a slash, split top/bottom rather than one block). Classified: **partial
  fit to M-209's indicator shape only, on structure, not alphabet; no fit to the FM 24-5 heading forms
  checked; no counter-example found in the one Slidex source read.**

### Conclusion

Best-fitting system: **M-209 (Converter M-209)**, on structural grounds only (2-letter code + 5-character
group + `/` + 2-letter code matches the manual's own `WW ... DKSLG/J` shape) -- but the fit is explicitly
partial because the manual states its indicator groups are letters-only and 605YZ contains three digits,
and because the manual's indicator groups run together as one unit rather than splitting into a header
line and a separate footer line the way Schmeh transcribes QM and 605YZ/FF. The natural key-material test
this partial fit would license (the footer's letters, YZFF, as key material) is already run and excluded
with a passing control (`cheap_test_done.2`, run_test2c.py, 0/93 candidates passed the judge). No system
checked in this lookup licenses a new, not-yet-run test at N=44; FM 24-5's plaintext heading forms and the
one Slidex source read give no indicator-system match at all. No solver run is recommended from this job.

### Request log

archive.org (advancedsearch.php + be-api.us.archive.org/fts): 15 requests, one at a time, >=1.5 s apart,
no 429/403 seen. Google Books (www.googleapis.com/books/v1, with GOOGLE_BOOKS_KEY and country=US): 2
requests, one 429 seen on an earlier unkeyed reachability probe (not counted here, no retry needed once
keyed). OpenAlex and Semantic Scholar: 1 request each (reported above, under Search record). No
gallica.bnf.fr, dbnl.org or de-crypt.org use. Well under the 60-request cap named in the brief.

SO lead prompt, 26 Sept 2026, QUEUE-FILL.

## Second-opinion leads (SO-BULLET-LEADS, 27 Sept 2026)

Landed from the ChatGPT second-opinion runner's answer to the LEADS prompt
(`second-opinions/chatgpt-leads-2026-09-27.md`, PR 33). Leads for the verifier, not a reading or an
attribution; every citation below is a claim to verify, never a fact ("unchecked").

- Provenance/find route (web forum thread): Ze-Pequeno's Reddit post names an Italian metal-detecting
  association and links its own discussion thread (`metaldetector.forumfree.it/?t=70205379`, did not load
  in this check) as the route to the discoverers, findspot notes, custody and a possible museum
  accession record -- unchecked.
- Findspot conflict (caveat, not a new source): Ze-Pequeno says "approximately near Florence" while Díaz
  2015 and Schmeh 2017 say southern Tuscany; the repository's own "Villa Rossi" label is not established
  as the same place by any post read -- unchecked.
- Companion material (web forum/holder route): no second coded slip is reported anywhere read; Díaz's
  "insignia recovered at the same site" is a different find, not a companion cipher -- the Italian
  association thread and the object's holder are the only named route to any undisclosed photographs or
  find log -- unchecked.
- Transcription length dispute (web comment): a Reddit commenter (atoponce) reads the last group as
  `RSUAI` (45 characters) against Schmeh's printed `RSUA` (44); the extra character is one reader's
  interpretation, not a verified correction -- unchecked.
- Provenance contacts (web forum posts): Karletto (Friendly Metal Detecting Forum, Jan 2015) and
  Ze-Pequeno may be the same person or collaborators; identity and current contactability are
  unchecked.
- Retraction of the circulated "grenade" decoding (web forum posts #37/#40): Karletto states dockmur's
  proposed decoding was a joke, dockmur confirms it -- stronger evidence against that claim than the
  newspaper retelling alone; the forum posts themselves are unchecked (not re-read by this landing).
- Format hypothesis (web comment): `QM` as an addressee ("quarter master") and `605YZ/FF` as
  sender/rank/location material, a contemporary reader's layout guess, not evidence for either
  expansion or for a named national system -- unchecked.

No printed decipherment, edition, or companion ciphertext of this target was named in the PR; nothing
here is a check-solved candidate.

## Web and blog check (CS-A2-G, 3 Oct 2026)

No printed edition or calendar exists for this item (a 2015 find, not a document series); the sources read by
this worker on 3 Oct 2026 were the web and blog threads below, and Cipherbrain post 44 with its 9 comments
(sources/schmeh/posts/44-bullet.txt, re-read by this worker). Searches (WebSearch, standard mode, 1 each):
1. `WW2 bullet cipher Tuscany 1944 "CBFUK YYEVO ZILOO"` -- hits: Cipherbrain post 44; Cipherbrain "Unsolved
   ciphertexts from World War II (1)"; gizmodo.com/tag/secrets; boingboing.net 2015/08/13; warhistoryonline.com.
   Every hit repeats only the forum "THEY THROW GRENADES..." reading, which Cipherbrain post 44 comment #3
   (Bernhard Gruber, 6 Mar 2017) says its author called a joke on 1 Feb 2015 (metaldetectingforum.com
   showthread.php?t=207067 p.2, cited there, not opened by this worker). Not a decipherment (already excluded
   mechanically, spec `cheap_test_done`).
2. `encrypted message found inside WW2 bullet casing Italy metal detectorist solved decoded` -- same set, plus
   unrelated Italian naval-cipher pages; no new decipherment.
3. `"bullet" cryptogram 1944 "605YZ" OR "QM" cipher solves Claude OR GPT` -- no model-solve announcement for this
   item (a "ChatGPT Astra Enigma" page, letemsvetemapplem.eu 28 Sept 2026, concerns an Enigma message, not this).
4. `Cipherbrain Schmeh bullet cryptogram WW2 Tuscany solution` -- Schmeh: "To my knowledge, this encrypted
   message is still unsolved" ("Unsolved ciphertexts from World War II (1)", read by this worker via WebFetch).
Blog site searches: Cipherbrain (scienceblogs.de/klausis-krypto-kolumne): post 44 comment thread read in full
(readers' guesses at the header only, comments #1, #3-#5, no key); WWII list (1) read. Cipher Mysteries
(`ciphermysteries.com WW2 bullet cipher note 1944 Italy`): no post on this item; the one ciphermysteries.com
hit (?p=11759) opened and is the 1918 Palermo postcard, unrelated. Cryptiana (cryptiana.blogspot.com /
Tomokiyo, one query): no hit. DECODE: this item is not in sources/decode/records-non-decrypted-2026-09-24.tsv
(grep "bullet|tuscany", 0 rows matching this find) and not in aaymeloglu's decode-catalog.csv (0); live
decode_list.py crawl not re-run. Solver repositories, shallow clones 3 Oct 2026: dbourdeau/cyphersolver
(810a777) mentions it only in research/top50/NOTES.md line 99 ("bullet 1944 ... 44 letters. All far too short",
low priority) and the pasted list text; no working files, key or reading. aaymeloglu/unsolved-ciphers
(d2800bb): grep for bullet/605YZ/CBFUK/tuscany finds nothing about this item (hits are other targets).
Request count: WebSearch 7 (4 verdict, 3 blog or list) plus WebFetch 2: scienceblogs.de 1,
ciphermysteries.com 1; github.com 2 clones; archive/Google Books/OpenAlex not used (item is not in print).
No 403/429 seen. Result: no decipherment, key or plaintext found in any source read; not found != unsolved
proof (rule 10: no novelty claim).

## Premise check (CS-A2-G, 3 Oct 2026)

- (a) folder's own mentions: the forum "solution" (SPLOID, Jan 2015) -- found, already excluded and
  retracted as a joke by its poster (comment #3 above); the Cipherbrain readers' header guesses (605th
  Ordnance Ammunition Co., QM = Quartermaster) -- found, readings of metadata, no key, no decipherment of the
  body. Nothing else in NOTES.md, the spec or second-opinions/ names a decipherment, gloss or clear copy.
- (b) other solvers' working files: not found. Bourdeau lists it as low priority/too short, with no files;
  Aymeloglu has none (3 Oct diff files agree).
- (c) physical neighbours: unreachable/not applicable -- a single slip in a cartridge case; the only image is
  the press photo (Cipherbrain files/2015/02/Bullet-Cipher.png, gizmodo/kinja image), not opened at native
  resolution by this worker. No companion slip reported anywhere read (second-opinions lead 3).
- (d) recipient side: not applicable; no addressee or edition series exists (QM is a reader's guess).
Verdict: nothing found that makes the item calibration or found-solved; status stays `partial` (NEAR.md row).

## Remaining gaps (GAPSFIX, 4 Oct 2026)
Read so far: 0 of 44 body letters read (0 H, 0 C); header QM and footer 605YZ/FF unread except as readers' guesses (Premise check above). Excluded with passing controls: the forum "solution", Caesar and 93 header/footer-derived keys (spec `cheap_test_done` 1-2).
- 44-letter body under periodic keys (period 2-8) and machine systems (M-209 by structure, Conclusion above) - blocker: too-short; family_run.py periodic_vigenere control 5.3-6.1% against gate 0.6 at N=44 (NEAR.md row, cheap_test_done 2), and 44 letters are too few to test M-209 pins/lugs (cheap_test_done 1)
- native-resolution image and the RSUA/RSUAI length dispute (second-opinion lead 4) plus the findspot/companion route (forumfree thread, lead 1, did not load) - blocker: not-attempted; the press photo was never opened at native resolution (Premise check (c)); next: fetch the Cipherbrain Bullet-Cipher.png once and eye-check the last group and every letter against Schmeh's transcription, plus one fetch of metaldetector.forumfree.it/?t=70205379, ~$1

## Escalation (GAPSFIX, 4 Oct 2026)
- [n/a] siblings: no companion slip reported in any source read (second-opinion lead 3)
- [n/a] clear-pages: single slip, no clear text or addressee series exists
- [x] known-keys: header/footer-derived keys and Caesar excluded with passing control (cheap_test_done 2)
- [n/a] print: a 2015 find, no printed edition or calendar exists (Web and blog check)
- [n/a] key-rebuild: no decipherment, key list or period material to rebuild from
- [ ] image-check: native-resolution read of the press photo (RSUA vs RSUAI), and the forumfree thread for further photographs
- [x] retry: indicator-system lookup (bBUL3) after the two cheap tests; no system licensed a new test at N=44
Verdict: keep going: 1 internal gaps; cheapest next: native-resolution image check of the photo + forumfree thread fetch, ~$1
