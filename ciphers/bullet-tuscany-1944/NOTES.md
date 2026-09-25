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
