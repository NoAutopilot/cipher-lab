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

### Candidate systems checked against print sources

| System | Printed header/indicator form (source, page) | Does QM / 605YZ/FF fit? | Test it would license | N=44 feasibility |
|---|---|---|---|---|
| (table filled below as sources are checked) | | | | |

### Control check (rule 3, for a lookup)

Two headers of a known system from the same literature, classified by this job's own checklist before
QM / 605YZ/FF, to show the checklist is not tuned to the answer it wants:
(filled below)

### Request log

Host request counts per the good-citizen rule (>= 1.5 s apart, one at a time), filled as run.
