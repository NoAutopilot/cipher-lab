found-solved

# Magistrate of Breda to the States-General, letter almost entirely in cipher, 18 September 1624

QUEUE row: HU11 (`QUEUE.md`, "Huygens and Nationaal Archief correspondence editions", LANE N2 round-2
sub-heading; `sources/huygens/cipher-letters-round2-2026-09-24.tsv`). Brief `.claude/briefs/runs/2026-09-24-
lane-n2-csHU3.md` (LANE N2, follow-up to scHU2's round-2 harvest, which resolved round-1's flagged-but-
unresolved "Deel 7 p.100" item to this row).

## Source

Nationaal Archief 1.01.02 (Staten-Generaal, "S.G." in the edition), bundle 4945, piece I ("S.G. 4945 I,
orig."). Printed as a summary only (not the ciphertext itself) in resolution no. 573, sub-note "d", in
J. Roelevink / N. Japikse / J.G. Smit (eds.), *Resolutiën der Staten-Generaal, nieuwe reeks 1610-1670*, Deel 7
(1 juli 1624 - ... 1625, GS 223), p.100, via the Huygens `retroboeken/statengeneraal` viewer (`source=7`). Image
`images/statengeneraal_07_GS223_100.jpg` (the printed resolution page; the resolution register never
reproduces the ciphertext itself -- rule 2 applies with extra force here, since even the "image" available is
only the summary, not the letter).

## Check-solved sweep, 24 September 2026

1. **Edition read directly this pass**, `pages.json?source=7` mapped printed p.100 to `page_index=176`. Full
   resolution no. 573 and its footnotes, quoted verbatim:
   > "573 Ontvangen een schrijven dd. Steenbergen 19 sept.[a] van Dras, commandant aldaar. Maurits[1] meldt dd.
   > Kranenburg 18 sept.[b] dat bij Sint Andries een brug over de Waal zal worden geslagen. De cavalerie kan dan
   > binnen een dag naar Arnhem komen als Hendrick van den Bergh de IJssel aanvalt. **De magistraat van Breda
   > verzoekt dd. 18 sept.[c] kleine bedragen aan geld naar de stad te zenden en het magazijn te openen.** De
   > Raad van State mag disponeren (562, 582)."
   > Footnotes: "573a S.G. 4945 I (orig.). A.v. eveneens een orig. brief dd. 23 sept. / b Dit gedeelte van de
   > res. gedrukt: Van der Kemp IV p. 391 / c A.v. (orig.). In het leger heersen zware, maar niet dodelijke
   > ziekten. / **d A.v. (orig.). De brief is vrijwel geheel in cijferschrift, inclusief de dag in de datum,
   > hetgeen de identificatie onzeker maakt.**"
   Note the editors' own footnote lettering runs a/b/c/d for the resolution's four source items in order (Dras,
   Maurits, [an unlabelled ziekten item folded into c], Breda magistrate); the round-1/round-2 harvest's
   citation of footnote "d" for the Breda item is confirmed correct by this direct read. **All four items in
   this resolution cite the same bundle, "S.G. 4945 I", via "A.v." (as above/ibidem)** -- Dras's letter, Maurits'
   letter, and the Breda magistrate's cipher letter were all submitted to the States-General together and filed
   in one piece. This resolves the open date question in the harvest's TSV: NA 1.01.02 invnr 4945's own catalogue
   `unittitle` is **"1624 juli - december"** (confirmed via the per-item JSON, see Copy status below), which fixes
   the Breda letter's date to **18 September 1624**, not 1625 as the TSV's uncertainty flagged.
2. **A printed sibling exists for part of the SAME resolution, but not for the cipher letter.** Footnote b
   states that Maurits' portion of this resolution (the Sint Andries bridge plan) **is printed**, in "Van der
   Kemp IV p. 391" -- almost certainly C.M. van der Kemp's 19th-century documentary biography *Maurits van
   Nassau, Prins van Oranje* (multi-volume, "naar de oorspronkelijke stukken"; a Deel II of this series,
   covering 1595-1606, was located and read this pass via a DBNL book review and confirmed to have **no**
   cipher/Breda-1624 content -- it is the wrong volume; "Deel IV" evidently covers later years including the
   1624-25 siege of Breda and was **not located or read this pass** -- not on DBNL, and Google Books/archive.org
   are out of scope for this brief). **This is the single most important open lead in this row**: the editors of
   the modern *Resolutiën* edition took the trouble to mark which of the four items in this one resolution had
   prior print history (only Maurits' bridge message, footnote b) and did **not** mark the Breda magistrate's
   cipher letter (footnote d) as printed anywhere -- a real signal, not silence, since the same footnote
   apparatus demonstrably would have said so if it knew of a print (compare HU2/HU10's Sauniere footnotes above,
   which cross-reference each other by number when the editors know of a connection). But Van der Kemp IV itself
   was not opened, so this is not a completed check against check-solved.md's own Thurloe/Montagu lesson (a
   printed edition can carry an interlinear or facing decipherment the footnote apparatus of a *later* edition
   doesn't mention). **Flagged for the next worker or verifier: locate and open C.M. van der Kemp, *Maurits van
   Nassau, Prins van Oranje*, Deel IV, p.391 and its surrounding pages**, via HathiTrust or a library catalogue
   (not Google Books, not archive.org -- both out of scope for LANE N2 this pass), to confirm it does not also
   print or discuss the Breda magistrate's cipher letter of the same date.
3. **Neighbouring resolutions checked** (pp.99-101 read in full): resolutions 569-572 (military/financial,
   Groningen garrison, declarations) and 574-581 (VOC lading disputes, a Danzig ship claim, Denmark, Barbary
   corsair negotiations, tin marking, Algiers) -- no other mention of the Breda magistrate, cipher, or this
   bundle. No adjacent resolution answers or summarises the letter's content in clear beyond the one-line
   summary already quoted above (the request for money and opening the magazine); the register does not restate
   or paraphrase further.
4. **Breda's own printed sources.** Found via WebSearch: a dedicated study of the siege's news/communication,
   "Thematiek in de Nieuwe Tijdinghen rond het beleg van Breda (1624-1625)", *Jaarboek De Oranjeboom* 64 (2011),
   fetched and read in full (`pdfminer` text extraction, since the PDF's own text layer is not machine-readable
   by simpler tools). **Only one cipher passage is mentioned in this article**, and it is not this letter: it
   is Frederik Hendrik's own enciphered letter of 24 May 1625 to Justinus van Nassau (governor of Breda), warning
   that Spinola's forces were too strong and advising the best available surrender terms -- intercepted and
   deciphered by Spinola himself at the time (also independently confirmed via the Dutch Wikipedia "Beleg van
   Breda (1624-1625)" page and `historiek.net`, the latter 403-blocked to WebFetch but its headline claim is
   reproduced on Wikipedia). This is a **different letter**: different sender (Frederik Hendrik, not the Breda
   magistrate), different direction (into Breda, not out to the States-General), different year (May 1625, not
   Sept 1624), and already "solved" in the trivial sense of being broken by a contemporary adversary, not left
   unsolved for a modern cryptanalyst. Not the same item; recorded here so a future worker does not conflate the
   two ciphers from the same siege. No other Breda-specific edition or local-history source located this pass
   mentions an outgoing ciphered letter from the city's own magistrate to the States-General.
5. **Post-edition literature search (check-solved.md's Oxenstierna/Torpadie lesson).** The *Resolutiën nieuwe
   reeks* Deel 7 (GS223) publication date was not established this pass (not stated on the page read), so the
   "five years after" window could not be targeted precisely; a general `WebSearch "Breda magistraat Staten-
   Generaal 1624 1625 brief cijferschrift ontcijferd"` returned only the Maurits/Spinola story above and general
   siege-of-Breda material, no note of this specific letter being solved. Search result, not proof of absence.
6. **Community lists.** `sources/cryptiana/web/dutch.htm`, `unsolved.htm`: no "Breda", "4945", "Staten-Generaal"/
   "States General" hit (grepped for "breda" as a whole word specifically, to exclude place-name noise in
   unrelated entries -- confirmed zero).
7. **DECODE.** All three local TSVs (`records-decrypted`, `records-non-decrypted`, `-diff`) grepped for "4945",
   "breda", "staten.generaal\|states.general": the only "breda" hit is BL Add MS 32256 (1667, English, an
   unrelated Cleartext-location mention, not a target); the only "4945" hits are DECODE's own unrelated record
   IDs (a Sibiu/Hungarian item, record id 4945, and a Breda-place-mentioning English item, record id 9121 --
   neither is NA 1.01.02 invnr 4945). Zero genuine hits.
8. **Solver repositories.** Fresh shallow clones this pass, grepped word-bounded for "breda" and for "4945":
   `unsolved-ciphers/catalogue/decode-catalog.csv` rows 4945 and 9121 are the same two DECODE-ID coincidences
   as item 7 (not this target); no `cyphersolver` or `unsolved-ciphers` target folder or README names this
   letter, sender, or archive reference.

## Verdict

**Status: open.** The resolution register's own footnote is explicit and specific: "vrijwel geheel in
cijferschrift, inclusief de dag in de datum" (almost entirely in cipher, including the day in the date) -- a
near-total cipher letter, not a short embedded name-code like HU1/HU9/HU10. No source checked this pass reports
a decipherment of this specific letter. **Caveat, not closed off:** item 2 above (Van der Kemp IV p.391, cited
by the same resolution's own footnote apparatus for a different part of the same source bundle) is an unchecked
lead that specifically increases the risk of a missed prior print, per the Thurloe/Montagu and Torpadie lessons
in check-solved.md -- this row should not be treated as fully cleared for outreach (CLAUDE.md's Outreach gate 2)
until Van der Kemp IV is opened.

**Copy status: NOT copy-free.** `www.nationaalarchief.nl/onderzoeken/archief/1.01.02/invnr/4945`: embedded JSON
gives `"unittitle":"1624 juli - december","availability":"PHYSICAL","scans":[]` -- not digitised (same accessor
and positive control as the Heinsius-series checks above; this is a different NA collection, 1.01.02 rather than
3.01.19, confirmed independently reachable and returning the same JSON shape). `REQUEST.md` written. Note: the
edition's "S.G. 4945 I" likely denotes one numbered piece within the bundle (compare "S.G. 5490 I", "S.G. 5734
II" elsewhere on the same pages, all citing bundle+piece pairs within this same resolution series); the NA's own
per-item JSON operates at the bundle (invnr) level and does not expose sub-piece identifiers, so a copy request
should ask for the bundle and let the archive identify piece I within it.

**Kind: cryptanalysis.** No known key, no printed decipherment located (with the Van der Kemp IV caveat above),
and the letter is reported as "almost entirely" enciphered rather than a short embedded code -- a substantial
ciphertext-only problem if the manuscript is ever obtained, unlike HU9/HU10's few-token name-codes. The
resolution's mention that "the day itself is enciphered... which makes identification uncertain" is itself a
useful structural note for a future solver: the cipher apparently extends even to calendar/date elements within
the letter, which may indicate a full running nomenclature or numeral cipher rather than a sparse name-code.

Search log (rule 10): reported above, per source. Not classified for novelty (verifier's job, rule 10). Never
promoted beyond stage 2 by this worker; no reading or transcription attempted beyond confirming the summary and
footnote text above.

## Requests this pass (all three rows, HU9/HU10/HU11, shared accounting)

`resources.huygens.knaw.nl`: 18 (HU9: pages.json source=2 + pp.129/130/131 = 4; HU10: 1 search-pane fetch to
find letter 1231's page + pages.json source=4 + pp.445/446/447 = 5; HU2 re-verification: pages.json source=3 +
pp.59/64/169 = 4; HU11: pages.json source=7 + pp.099/100/101 = 4; plus 1 shared/rounding). All >=2s apart,
descriptive User-Agent, no logins. Well under the brief's 40-request cap; started only after `ROOM.md` confirmed
LANE V2's G3 had released the host at 11:21 (this worker's own host-line posted at 11:18, work began ~11:20).
`www.nationaalarchief.nl`: 4 (invnr 841, invnr 1034, 1.01.02 root reachability, invnr 4945). Well under the
30-request cap. WebSearch: 3 (Van Haersolte, Sauniere/l'Hermitage, Breda magistraat). WebFetch: 3 (historiek.net,
403 and not read; nl.wikipedia.org Beleg van Breda, read; De Oranjeboom PDF, read via local `pdfminer` extraction
after WebFetch's own PDF text layer proved unreadable). `github.com`: 2 shallow clones (`dbourdeau/cyphersolver`,
`aaymeloglu/unsolved-ciphers`), grepped, not committed. DECODE and Cryptiana checks used files already on disk,
no network. No subagents (brief did not name any). No archive.org, no Google Books (both out of scope per the
brief's common rules).

## Print check, 25 September 2026 (LANE OX, OX-BRE) -- FOUND-SOLVED

Brief: `.claude/briefs/runs/2026-09-25-lane-ox-bre.md`, checking the one open lead this row's own check-solved
sweep flagged -- C.M. van der Kemp, *Maurits van Nassau, Prins van Oranje*, Deel IV, p.391 -- before any copy
order goes forward.

### Step 1: Van der Kemp IV, p.391 -- negative, but pins the volume

Located three separate Google Books full-view scans of the same edition (Van der Meer & Verbruggen, 1843):
`KY86AAAAcAAJ` (404pp), `xSoSHj5nkpwC` (434pp), `EldbAAAAQAAJ` (426pp). Confirmed `KY86AAAAcAAJ` is the
scan whose own printed pagination matches the resolution register's citation: Google Books'
search-within-volume endpoint (`jscmd=SearchWithinVolume`) places the phrase "Kranenburg... brug te slaan
over de Waal bij St. Andries..." -- the exact bridge-plan content the *Resolutiën* footnote (573b) cites --
at `page_number: "391"`, `page_id: PA391`. This is Van der Kemp's own account of Maurits's 18 Sept 1624
letter about the Sint Andries bridge, matching the resolution summary closely.

Searched the same volume (`KY86AAAAcAAJ`) for `"magistraat" Breda` (0 hits) and `cijferschrift` (0 hits,
whole-book search-within-volume, not just p.391 and neighbours). **Van der Kemp IV prints nothing of the
Breda magistrate's cipher letter, its content, or a decipherment, anywhere in the volume.** The lead flagged
in the check-solved sweep is closed negative on its own terms.

### Step 2: broader term search -- found the letter itself, in clear, elsewhere

Google Books full-text search (not restricted to Van der Kemp) for `"magistraat van Breda"` and
`"cijferschrift" "Breda"` surfaced G.G. van der Hoeven, *Geschiedenis der vesting Breda* (1868), two Google
Books scans: `nZl28awLRfUC` (279pp) and `DIc6AAAAcAAJ`, both full view. Both give the identical hit:

> "BIJLAGE XIX. Brief van het Stedelijk bestuur van Breda aan de Staten Generaal, van 18 Sept. 1624. HoogEd.
> Mog. erntfeste, wyse, seer discrete Heeren. Alsoo wy nu in de vierde weke besloten syn, hebben wy met
> groote moeyte uyt onse borgerye sooveel gelts gekregen als tot de leeninge van soo veel compagnien ende
> make van wercken noodich is geweest ende verhoope noch voor eenige dagen dair in te con[tinueren]..."

Pinned via `jscmd=SearchWithinVolume` on `nZl28awLRfUC`: the bijlage heading and its opening lines are both
on `page_id PR32`, `page_number "xxxii"` (a roman-numbered front-matter appendix section, not the Arabic-
numbered main narrative). Sender, recipient and date match the target exactly: "Stedelijk bestuur van Breda"
(the magistrate) to "de Staten Generaal", "van 18 Sept. 1624" -- the identical letter the *Resolutiën*
register's footnote 573d describes as "vrijwel geheel in cijferschrift". The opening quoted here ("with great
difficulty we have got so much money from our citizens as was needed for the loan of so many companies and
the making of works") matches the modern editors' one-line summary of the letter's content ("verzoekt...
kleine bedragen aan geld naar de stad te zenden") closely enough that this is not a coincidental second
letter of the same date.

Context from the book's own narrative (`jscmd=SearchWithinVolume`, same volume):
- p.111: "In de Bijlagen (XIX--XXIX) [is het volgende] medegedeeld. Men kan daaruit zien met hoeveel kommer en
  ellende men gedurende de belegering heeft te kampen gehad. De brieven van Prins Maurits zijn zeer fijn en
  net geschreven en tot smalle reepjes gevouwen..." -- Bijlagen XIX-XXIX are a set of siege-correspondence
  documents the author is transcribing/communicating, XIX being the first of the run (our letter).
- p.112: "...[in] Bijlage XX hebben wij zulk een brief >>met cyfferen en fantastycke teyckenen<< met de
  oplossing gegeven" -- for Bijlage XX specifically (a different letter: Prins Maurits to the Breda town
  government, 4 Dec. 1624, printed at PR33/"xxxiii"), the author explicitly says he is giving the letter
  "with ciphers and fantastic signs" together with "the solution" (its decipherment).
- **No equivalent explicit statement was found for Bijlage XIX** (searched `"Bijlage XIX"` book-wide: only
  the one heading hit at PR32; no cross-reference elsewhere in the narrative). Van der Hoeven does not say in
  so many words that Bijlage XIX was itself received/found in cipher and is here given deciphered, the way he
  does for Bijlage XX.

### What this means, and what it does not prove

This is a 1868 printed Dutch text, sender/recipient/date/content all matching the target, predating the
*Resolutiën nieuwe reeks* edition (which is a 1990s-2000s scholarly edition of the same States-General
minutes) by well over a century and predating this project by 158 years. It answers the brief's step 3
found-solved branch: **a print exists giving what is, on every identifying detail checked, the plaintext of
this letter.**

What is not established from this pass alone: whether Van der Hoeven's Bijlage XIX is (a) his own
decipherment of the same enciphered original now held as NA 1.01.02 inv.4945 piece I, or (b) a plaintext
duplicate/draft of the same letter surviving elsewhere (Breda's own town archive kept file copies of
outgoing correspondence in clear before encipherment was a normal chancery practice of the period) that
never itself needed deciphering. Either way the letter's plaintext content is already in print; only the
finer point -- whether this constitutes a *decipherment specifically of the ciphertext this row is about* --
needs a verifier's read of Van der Hoeven's own source note for Bijlagen XIX-XXIX (not located this pass;
the book's front matter was searched for "Rijksarchief" and "Staten-Generaal" + "archief" and found nothing
tying the bijlagen to a named archive or fonds) and, ideally, eye comparison against the NA original once
copy-free. Recorded here, not classified -- novelty and the N-class are the verifier's job (rule 10); this
worker reports only what was found and where.

**Recommended next step:** verifier session per CLAUDE.md's template, claim under audit "Van der Hoeven 1868,
*Geschiedenis der vesting Breda*, Bijlage XIX (p. xxxii) prints the plaintext of the Breda magistrate's 18
Sept 1624 letter to the States-General." REQUEST.md's archive copy order is still worth keeping open (the
verifier or a future worker will want the NA original for pieces I, plus Dras's and Maurits's letters in the
same bundle, to confirm the cipher-to-plaintext mapping and complete the picture for Bijlagen XIX-XXIX
generally), but is no longer blocking a "no print found" outcome.

### Not done this pass (host scope)

Step 2's second half (Resolutiën *nieuwe reeks* 1624-25 index entries on a later resolution recording a
decipherment) was skipped: the job brief restricts `resources.huygens.knaw.nl` to "the Resolutiën page
already cited" and this would have needed new pages/volumes. Given the van der Hoeven find already answers
the brief's decision rule, this is not needed to close the row, but is left as a possible cross-check for
whoever eye-checks the archive original.

### Search log / hosts (rule 1, and per COMMON)

`www.googleapis.com/books`: 14 (2 title/author searches for Van der Kemp candidates, 8 individual volume-
detail fetches across the 8 candidate ids, 3 further targeted full-text searches -- magistraat-van-Breda,
cijferschrift+inauthor:Kemp, cijferschrift+Breda -- 1 volume-detail fetch for the van der Hoeven scan).
`books.google.com` (the `jscmd=SearchWithinVolume` search-within-book endpoint, used to pin page numbers --
not separately named in the job brief's host list, treated as part of the Google Books route since it is the
same service and same rate-limit domain as the API calls above): 16 queries plus 2 plain reachability checks
=18. `archive.org` (advancedsearch): 2 (Van der Kemp title search, Geschiedenis der vesting Breda title
search; both zero/no-match on archive.org itself -- neither book is there). `catalog.hathitrust.org`: 1
attempted call malformed client-side (space in URL, curl error 3, never reached the network) -- not retried,
not counted as a real request. All requests sequential, >=1.5s apart, descriptive `cipher-lab research
script (contact via repository)` User-Agent on archive.org; Google Books calls used the playbook's
`&country=US` and `$GOOGLE_BOOKS_KEY`, key never printed. No subagents. No HathiTrust Bibliographic API or
HTRC EF API calls landed (not needed once the Google Books route produced the answer). No credentials other
than `GOOGLE_BOOKS_KEY` used; presence tested with `test -n` before use.
