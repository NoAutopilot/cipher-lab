partial

# Robert Bowes to Walsingham, 7 April and 31 July 1583, and short Caligula B VIII ciphertexts 1580-83 — BL Cotton Caligula C VII, B VIII

- Source: QUEUE.md rank 17 (score 32), scored 20 September 2026; catalogued from Tomokiyo's Cryptiana
  `elizabeth.htm` page and Bourdeau's `TARGETS.md`.

## Check-solved sweep (23 September 2026)

1. **Web search.** "Robert Bowes Walsingham 1583 cipher Caligula Cotton solved decrypted" — results are general
   biographical and manuscript-catalogue pages (BL Archives Catalogue entries for other Caligula volumes,
   Wikipedia on Robert Bowes, a Cryptologia abstract on deciphering Mary Stuart's letters 1578-84) and confirm
   the manuscripts and their catalogue descriptions but report no decipherment of the 7 April or 31 July 1583
   letters, or of the Caligula B VIII fragments. found=false.

2. **Print.** The 20 September 2026 search-print pass recorded in QUEUE.md already established: CSP Scotland
   vol. 6 (Boyd 1910, covering 1581-83) is not on Internet Archive under its own title (`advancedsearch.php`
   found only vols 1, 2, 4, 8, 9, 13); british-history.ac.uk serves this volume's pages as paywalled "premium
   content" (confirmed for pp.356-434 and pp.521-570) and its site search returned HTTP 403; HathiTrust's
   Bibliographic API confirms a public-domain full-view copy exists (htid `nnc2.ark:/13960/t1gh9nc18`) but
   babel.hathitrust.org is Cloudflare-blocked to curl and to the browser tool. Not re-run this sweep (same
   blockers apply; HathiTrust access remains the identified next step, not completed this sweep). Google Books:
   not available in this account's environment (no key set here). Status: **unreachable, not settled** — same
   as 20 September 2026.

3. **Community lists.** `sources/cryptiana/web/elizabeth.htm` (grepped locally, never edited) is explicit and
   directly on point: "(f.196) Robert Bowes to (?)Walsingham, Edinburgh, 7 April 1583. A few words in cipher,
   **not deciphered**." and "(f.299) Robert Bowes to (?)Walsingham, Edinburgh, St Johnstons, 31 July 1583. A few
   words in cipher, **not deciphered**," with Tomokiyo's own transcription linked (`CottonMSBowes.txt`) and the
   note "If one can read the cleartext around the ciphertext, solution may not be difficult" — i.e. Tomokiyo
   flags it as an open, tractable target, not a solved one. The same page documents the sibling key lead already
   in QUEUE.md: Caligula B VIII f.290-293 ("Bowes's report of his conferences... to supplant Lenox," catalogued
   84) has an interlinear decipherment and a reconstructed key image (`elizabeth_bowes.png`); f.251-252 and
   f.306 are further short, undeciphered Bowes-related fragments in the same volume, also not solved. Cipherbrain
   /scienceblogs.de: no matching post found via WebSearch snippets; full-page fetch blocked by this
   environment's egress policy (see ciphers/charles-rupert-1645/NOTES.md item 3). found=false, confirmed
   explicitly "not deciphered" by the primary community source (Cryptiana); unreachable on Cipherbrain directly.

4. **DECODE.** No DECODE record IDs are attached to this QUEUE row (unlike ranks 11 and 13); the item is
   catalogued from Tomokiyo's own transcription rather than a DECODE upload. Not checked.

5. **Bourdeau (`github.com/dbourdeau/cyphersolver`, shallow clone 23 Sept 2026, MIT code / CC BY 4.0 text).**
   No target folder for this item (`grep -rli "bowes\|caligula"` across the repository returns only unrelated
   incidental mentions — e.g. "napoleon/unsolved.txt", the Randolph 1570 and Norfolk 1570 folders' source
   citations, Hamilton 1569 — none of which is a Bowes 1583 attempt). `TARGETS.md` lists it (per QUEUE.md's own
   rationale, "ranked it low", "101 groups of name") but with no working folder. found=false (not attempted).

6. **Aymeloglu (`github.com/aaymeloglu/unsolved-ciphers`, shallow clone 23 Sept 2026; no licence, cite only, no
   code copied).** No target folder and no catalogue-file mention (`grep -rli "bowes\|caligula"` returns zero
   matches anywhere in the repository). found=false (not attempted).

## Verdict

**Open.** Every source checked either found nothing (web search, Bourdeau, Aymeloglu, DECODE n/a) or explicitly
confirms the two named letters are "not deciphered" (Tomokiyo's Cryptiana page, the primary community source for
this exact item). The one print route that could settle it — CSP Scotland vol. 6 (Boyd 1910) via HathiTrust
`nnc2.ark:/13960/t1gh9nc18` — remains blocked by Cloudflare to every fetch route tried in prior sweeps and was
not re-attempted this sweep (no new access route available in this account's environment). The Caligula B VIII
f.290-293 interlinear decipherment (Tomokiyo, `elizabeth_bowes.png`) stands as the identified sibling-key lead
and is unchanged by this sweep.

Stage 2, verified unsolved.

## Search-print and image check (23 September 2026)

Network was opened for this account's environment at 23:00 UTC today (per ROOM.md 23:05 note); this pass used
route 1 of the access playbook (`curl -A "Mozilla/5.0"`) against archive.org and the BL's catalogue/IIIF hosts.
Per the owner's standing rate-limit rule: requests were single, sequential, at least 1.5s apart, never
parallel against the same host, and stopped (not retried in a loop) on the two 403s hit. Counts this session:
archive.org 8 requests (2 advancedsearch, 1 metadata, 5 download/djvu-text, all HTTP 200 after following one
redirect); searcharchives.bl.uk 4 requests (2 search pages, 2 catalogue records, all 200); bl.digirati.io 2
requests (one IIIF manifest per shelfmark, both 403); babel.hathitrust.org 1 request (403, not retried,
per the rule); cryptiana.web.fc2.com 2 requests (Tomokiyo's own linked transcription + key image, both 200).

### 1. Search-print

**CSP Scotland vol. 6 (Boyd 1910, 1581-83) is still not on archive.org.** Two targeted `advancedsearch.php`
queries (`title:(calendar state papers scotland)`; `creator:(Boyd) AND title:(calendar) AND mediatype:texts`)
return only `calendarstatepa00boydgoog` (vol. IV, 1905) and `calendarstatepa01boydgoog` (confirmed by its full
djvu text as vol. V, 1574-1581, Boyd 1907) — no identifier for vol. 6. Unchanged from the 20 September 2026
finding (also blocked on BHO and HathiTrust; babel.hathitrust.org repeated its Cloudflare 403 this pass too,
one attempt only, not retried).

**Found instead: *The Correspondence of Robert Bowes* (Surtees Society vol. 14, ed. Stevenson, 1842)**, on
archive.org as `correspondenceof00bowerich` (full djvu text fetched, 1.8 MB). Tomokiyo's own page already notes
this volume "does not include" the f.196/f.299 cipher letters (sources/cryptiana/web/elizabeth.htm line 428),
and this pass confirms why: it prints Bowes's own **Letter-Book copies**, a separate register kept alongside
the originals that Walsingham filed (now Cotton MS Caligula), not the originals themselves. A whole-volume
keyword sweep found "cipher" x2, "cypher" x12; none is flagged "deciphered", and no key or plaintext substitution
for a cipher passage is printed anywhere in the volume. Full detail (entry numbers, page citations, flagged
sentences) is in `print-check.tsv`. Three entries are directly relevant:

- **CLXXXVII, "To Sir Francis Walsingham, vijth April, 1583"** (Letter-Book p.172, printed pp.404-406): the
  same sender, recipient, place (Edinburgh) and date as the BL catalogue's f.196 entry (below). Contains
  unresolved **numeric name-codes** left as bare arabic numerals by Stevenson — 870, 91, 149, 19, 29, 85, 54,
  32 — e.g. "the doings and progress of Sir Henry Cobham with 870 and Smallet" and "he cannot abandon 149, 19,
  29, and 85." Not a decipherment (no name is ever substituted for a number); Tomokiyo's page independently
  flags these same codes as an "unidentified" lead separate from the Cotton MS symbol-cipher.
- **CCXXXIX, "To Sir Francis Walsingham, ultimo Julii, 1583"** (p.253, printed pp.525-529): the public/official
  companion letter of 31 July 1583; no cipher content.
- **CCXL, "The Private Letter of the same date"** (p.257, printed pp.529-534): numeric codes 223, 189, 32,
  0100, 54 — e.g. "upon suit made to 189 for the relief of Drumquhassell, 189 said that he must be examined
  what had passed betwixt 32 and him for the delivery of 0100 to 32." Tomokiyo's page separately notes "223" on
  Surtees p.530 as an unidentified code.

**Verdict on print: not found-solved, not an edition of the target letters.** [Verifier, 24 Sept 2026,
AUDIT.md section 4: superseded. CSP Scotland vi pp.370-371 (no. 389, fol.196) shares the vocabulary of CLXXXVII
and prints every cipher name in clear, so CLXXXVII is the same letter and its plaintext is in print.] The
Letter-Book entries are a related but textually distinct source (Bowes's own register, not the delivered/filed original), printed in a
public-domain 1842 edition, containing their own un-glossed numeric name-codes rather than the drawn cipher
symbols Tomokiyo transcribed from the Cotton MS. Whether entry CLXXXVII is word-for-word the same letter as
Cotton C VII f.196 (both dated 7 April 1583, same correspondents) is not established this pass — worth a
side-by-side check by whoever next has the manuscript images or Boyd's own calendar text.

### 2. Images (BL IIIF, route 1)

Fetched the British Library's own Archives and Manuscripts Catalogue records (`searcharchives.bl.uk`) for both
shelfmarks — not previously checked by this target's NOTES. Both **confirm and extend Tomokiyo's citations
verbatim**:

- **Cotton MS Caligula C VII** (`searcharchives.bl.uk/catalog/040-001102384`, covers 1582-1584, Languages
  includes "Cipher"): "**ff. 196r-197v**: Letter of Robert Bowes to (?) Sir Francis Walsingham, Edinburgh, 7
  Apr 1583. Original. Partly in cipher." and "**ff. 299r-v, 303r**: Letter of Robert Bowes to (?) Sir Francis
  Walsingham, Edinburgh, St Johnstons, 31 Jul 1583. Original. No address; Bowes addresses recipient as Your
  Honour. Some use of cipher." Two *other* Bowes-to-Walsingham items dated the same 31 July 1583 in the same
  volume (f.297r-v, a 17th-century copy; f.300r-302r, an original) are catalogued with no cipher note, so
  f.299/303 is specifically the cipher-bearing item among three same-day letters.
- **Cotton MS Caligula B VIII** (`searcharchives.bl.uk/catalog/040-001102375`): confirms Tomokiyo's three
  sibling fragments — **f.251r-252v** ("Copy of a letter from [Bowes?] to [Cecil?], reporting the state of
  affairs in Scotland [1583?]"), **f.290v-292v** ("Bowes's report of his conferences and negociations to
  supplant Lennox, partly in cypher [1580?]" — the interlinear/reconstructed-key lead, `elizabeth_bowes.png`),
  and **f.306r** ("A note, with some cipher, on Scottish affairs," undated).

**Neither volume is digitised.** Both catalogue pages give a Digitised Content link marked "(digital images
currently unavailable)"; the corresponding IIIF manifest at `bl.digirati.io` returns HTTP 403 (an S3
`AccessDenied` body, not a Cloudflare challenge page) for both arks. This is a different, harder failure mode
than the Cloudflare-gated hosts logged elsewhere in CLAUDE.md: the BL itself states the images do not exist
online yet, not merely that they are hard to reach. No image was captured; `images/manifest.json` records
what was tried. Not retried per the rate-limit rule (one manifest fetch per shelfmark, then stop on 403).

Also fetched (and added to `sources/cryptiana/web/`, since they are resources Tomokiyo's already-snapshotted
`elizabeth.htm` links to and were not yet mirrored): his own ciphertext transcription `CottonMSBowes.txt`
("the lines below are separate ciphertext fragments (not a contiguous ciphertext)", 11 short lines of 2-digit
symbol codes covering f.196 and f.299 combined) and `elizabeth_bowes.png` (his reconstructed key for the
f.290-293 fragment).

### Verdict

**Still open; status line unchanged.** No decipherment, key or plaintext for any of the five fragments (f.196,
f.299, f.251-252, f.290-293, f.306) is in print anywhere checked this pass. Per rule 10: reporting only what
was found and where it was not found, not novelty. Next steps, in order: (a) the manuscript images do not
exist yet at the BL, so transcription must wait on a physical/reading-room route (access playbook route 4,
not attempted this pass — no per-item price is quoted on the catalogue page to put in a REQUEST.md yet;
worth an email enquiry via route 4 if this target is prioritised further); (b) if CSP Scotland vol. 6 (Boyd's
own calendar text, which would settle whether f.196/f.299 print as deciphered or as symbols) becomes reachable
via HathiTrust or another route, re-run the search-print pass against it specifically; (c) cryptanalysis of
Tomokiyo's own 11-fragment symbol transcription (`sources/cryptiana/web/CottonMSBowes.txt`) remains the only
route that does not depend on new images, per his own note that the cipher "seems to be a simple one" and that
reading the surrounding cleartext (which does exist, via the BL catalogue folio numbers above, on a future
image-capture pass) "may be" enough to solve it.

## Solver session (24 September 2026)

> Verifier, 24 September 2026 (AUDIT.md): **N1**. The plaintext is in print since 1842 (letter-book), and
> for f.196 very probably in the 1910 calendar of the folio itself. Describe this as an independent
> re-decipherment giving a sign table for Tomokiyo's numbering, never as a first or new decipherment.

Solver worker (Opus), cap $15, no subagents. **Works from Tomokiyo's transcription only** (`ciphertext.txt`,
copied unchanged from `sources/cryptiana/web/CottonMSBowes.txt`, his "CottonMSBowes.txt", credit S. Tomokiyo,
Cryptiana). The manuscript images are not online (BL, 23 September 2026). Every result below is conditional on
his sign numbering and his reading of each sign (rule 2). His companion image `CottonMSBowes.png`, named in the
file's first line, could not be fetched: cryptiana.web.fc2.com is not on this container's egress allowlist
today, and the prior session's copy was not mirrored.

### Method

- **Ciphertext.** 11 fragments, 101 tokens, 25 distinct signs (02, 03, 06-28; 04, 05 and 01 unused).
  Fragment lengths 14, 7, 10, 26, 1, 10, 7, 9, 9, 3, 5. Doubled signs: 11 11 (F1), 13 13 (F2, F7), 09 09 and
  07 07 (F6), 02 02 (F10). Repeats: F2 and F7 match except for one sign (10 against 14). F3, F4 and F8 share
  "13 10 11 18 (19|26) 06 11 (10)".
- **Parallel text.** Bowes's own Letter-Book copies are printed in Surtees Soc. vol. 14 (1842; archive.org
  `correspondenceof00bowerich`, fetched once, `corpus/`, manifest). They cover the same dates and correspondents:
  CLXXXVII (7 April 1583, pp.404-406) and CCXXXIX-CCXL (31 July 1583, pp.525-534). In the Letter-Book the
  enciphered words stand in clear. Only the numeric name-codes (870, 91, 32, 54, 223 ...) remain as numbers.
- **Crib alignment (the method that read it).** The names in CLXXXVII come in this order: "Sir Henry Cobham
  with 870 and Smallet", "Glencarne", "Manningvile, Huntley, Glencarne, and Montrosse", "870", "Mauvisier",
  "return of Smaller [Smallet]". F2 has the pattern of "Smallet" (ABCDDEF). F4's tail has the pattern of
  "lencarne" (ABCDEFCB). One key from those two words reads F1, F3, F4, F6 and F7 in the same order as the
  Letter-Book. It also reads F8 and F9 against CCXL ("Glencarne and 223", "Ruthen"). key.tsv gives the evidence
  for every sign.
- **Ciphertext-only solver.** `tools/subst_hillclimb.py` (written this session, own code) is a simulated-anneal
  substitution solver. It allows many-to-one keys (at most 2 signs per letter), uses an interpolated letter
  4-gram model with a 24-letter alphabet (i=j, u=v), runs 100 restarts × 20000 iterations, and ends with a
  greedy polish. The model is trained on the Holmes and Moby Dick texts in tools/data plus Surtees vol.14
  lines 0-15000. `control/control.py` builds the controls and runs the target.
- **Crib significance.** `crib.py parallel` uses the capitalised non-initial words of the three parallel
  letters (68 words). It picks non-overlapping placements consistent with one key (each sign one letter, at
  most 2 signs per letter; randomised longest-first greedy, 300 restarts) to maximise the number of tokens
  covered. It then repeats the search with (i) the word lists of 40 random blocks of three other letters from
  the same volume and (ii) the parallel list on 20 shufflings of the target tokens. Same lengths and sign
  counts throughout.

### Control (rule 3)

Same shape as the target (fragment lengths 14,7,10,26,1,10,7,9,9,3,5; 101 tokens). Same solver settings as
T1. Three seeds per design. Plaintext comes from Surtees vol.14 lines 15000-22500, disjoint from the model's
training text and from the target letters. Full table: `control/results.tsv`.

| design | what | tokens correct (3 seeds) | found vs true-key score |
|---|---|---|---|
| a | one-to-one, running English | 96.0, 99.0, 89.1 % | found >= true (search reaches the answer) |
| b | a + two signs each for e and a | 0.0, 99.0, 97.0 % | seed 11 is a search miss (-0.978 < true -0.851) |
| c | a with F5 and F10 as code signs (excluded from the count) | 95.9, 99.0, 86.6 % | found >= true |
| d | **the target's own design: every fragment a proper name or name string** | 18.8, 15.8, 32.7 % | **found > true in all three** (a model limit, not a search limit) |

So ciphertext-only anneal reads running English of this length and shape (a-c: 8 of 9 runs at 87-99 %), but
not proper names (d). The 4-gram model prefers wrong English-like strings to the true names. On the target the
ciphertext-only solver is **not able to decide at this length**, and its failure (T1) says nothing about the
target. The crib method has its own control: target 43 covered tokens, other letters' word lists 28.8 +- 2.9
(max 34 of 40), shuffled target 27.0 +- 3.1 (max 31 of 20) (`crib_runs.tsv`).

### Runs

`runs.tsv` logs every run with its score against the shuffled baseline.

| run | method | score / token | baseline | agreement with key.tsv |
|---|---|---|---|---|
| T1 | ciphertext-only, control settings | -0.954 | shuffled B1-B3 -1.053..-1.027 | 51/93 (partial convergence: "smalleg", "ttlentaine") |
| T2 | key.tsv scored by the same model | -1.395 | same | 93/93: the names score below shuffled, as in control d |
| T3 | anneal with the 17 S-grade signs fixed | -1.198 | same | 85/93; the model fills the M signs badly ("cacham", "glencorn"); F11 "tohim" (03=t, 25=o) noted, not adopted |
| T4 | Tomokiyo's f.290-293 key as start | - | - | not applicable: drawn glyphs, not his 02-28 numbers |
| T5 | crib.py parallel (Letter-Book word lists) | 43/101 covered | 28.8 +- 2.9 / 27.0 +- 3.1 | the basis of key.tsv, extended by hand to 93 read tokens |

### Reading

Conditional on Tomokiyo's transcription, graded per token in `reading.tsv` (regenerated by `check.py`, which
exits 1 if stale):

| F | signs | decoded by key.tsv | as read | parallel Letter-Book text (Surtees 1842) |
|---|---|---|---|---|
| 1 | 14 | sirhennicobham | Sir Henri Cobham | CLXXXVII "Sir Henry Cobham with 870 and Smallet" |
| 2 | 7 | smallet | Smallet | same sentence |
| 3 | 10 | gclencarne | Glencarne | "credit by and with Glencarne" |
| 4 | 26 | magnyuilhrntleyoglencarne? | Magnyuil, Huntley, ? Glencarne ? | "Manningvile, Huntley, Glencarne, and Montrosse" |
| 5 | 1 | ? | (code sign) | "with especial commendations from 870" follows (not verified) |
| 6 | 10 | mauuissier | Mauvissier | "offer himself to Mauvisier" |
| 7 | 7 | smallet | Smallet | "return of Smaller" (Stevenson's misprint or the OCR's) |
| 8 | 9 | ?glencarn | ? Glencarn | CCXL "This day Glencarne and 223" |
| 9 | 9 | hisruthen | his Ruthen | CCXL "the act done at Ruthen on his person"; "his fault at Ruthen" |
| 10 | 3 | ??? | unread | pattern AAB; CCXL has the code number 223 (not verified) |
| 11 | 5 | ??him | ? ? him | unread first two signs |

F1-F7 fall in the order of CLXXXVII, so f.196 (7 April) is very probably the original of that Letter-Book
entry. The last NOTES section left that question open. F8-F9 fit CCXL, the private letter of 31 July 1583,
which suggests Cotton f.299/303 is the original of CCXL. This rests on the fragments' order and names only; an
image would settle it. The cipher is a simple substitution (one sign per letter, with second signs for a, e and
g, each of them a single token at grade M) used for proper names inside clear sentences. The numbers in the Letter-Book (870, 223 ...) are a separate
code layer. F5 (28), F4's last sign (27), and perhaps F10, are probably that layer's signs.

### Grading (rule 4)

S 82, M 8, I 3, unread 8, H 0, C 0 (101 tokens). **Cryptanalytic result** (no H or C). S means the sign's value
is fixed by a crib-matched name and confirmed in at least one other fragment, with the crib control above.
M covers single-occurrence values: 14=e, 20=o in F4, 21=b, 23=g, 24=y, 26=a. I marks three tokens where the key
letter is not the parallel word's letter: F1 pos.7 (sign 11 = n where "Henry" wants r), F3 pos.2 (sign 18 = c,
extra), F4 pos.10 (sign 06 = r where "Huntley" wants u). Each is either a scribal slip or a transcription
confusion; the image would decide. The Letter-Book is a parallel copy, not a key, and nothing has matched a
fragment to its line in the original, so no token is graded C.

### Where it was not found

Searched 24 September 2026, a search result only, not a novelty verdict:
- **Bourdeau** (github.com/dbourdeau/cyphersolver, shallow clone at 2e9ec01, 23 Sept 2026). grep
  `bowes|smallet|glencarne|mauvissier|magnyvil|caligula c vii` finds only `TARGETS.md` line 105 ("Bowes 1583
  is 101 groups of name") and unrelated Mauvissière hits in French targets (sp53, gallica_sweep, matignon1586).
  No folder or reading for this item.
- **Aymeloglu** (github.com/aaymeloglu/unsolved-ciphers, shallow clone at 6f9c462, 21 Sept 2026, cite only).
  The same grep finds no Bowes item. The DECODE catalogue cache has Caligula C II and C V records but none for
  Caligula C VII.
- **WebSearch** (one query): `Bowes Walsingham 1583 cipher "Smallet" Glencarne Mauvissier Caligula C VII
  deciphered`. The results are general: Wikipedia on Robert Bowes, Lasry-Biermann-Tomokiyo 2023 on Mary
  Stuart's letters to Mauvissière, and news on those letters. None prints or mentions a decipherment of these
  fragments.
- **Surtees vol.14** prints the Letter-Book plaintext of the words (the parallel text above), not the
  ciphertext or a key. Whether an edition places the cipher signs next to the plaintext was not checked:
  CSP Scotland vi (Boyd 1910) is still unreachable (see 23 September 2026). [Verifier, 24 Sept 2026: its HTRC
  Extracted Features token counts show the fol.196 entry (no. 389, pp.370-371) with Cobham, Smallet,
  Glencairn, Maineville, Huntly, Montrose and Mauvissière in clear. The class is N1, independent
  re-decipherment; see AUDIT.md.]

### What a next solver needs

1. Images of Cotton Caligula C VII ff.196r-197v and ff.299r-v, 303r. They would check the three I tokens and
   the unread signs (02, 03, 15, 25, 27, 28), and confirm which clear words surround each fragment. The BL has
   not digitised the volume, so this is a route 4 (the person) item: a copy order for those folios. No
   REQUEST.md written; the brief did not name one.
2. Tomokiyo's `CottonMSBowes.png` (glyph shapes), to compare with his f.290-293 key (`elizabeth_bowes.png`).
   That key uses drawn glyphs, not these sign numbers, so it could not seed the solver. Some of its glyphs may
   be the same system.
3. CSP Scotland vi (Boyd 1910) at the f.196/f.299 calendar entries, to see how the calendar prints the cipher
   words (the verifier's job, not this session's).
