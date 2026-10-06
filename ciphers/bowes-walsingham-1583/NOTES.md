partial
Surtees Society vol.14 (Correspondence of Robert Bowes, 1842; IA correspondenceof00bowerich full text, corpus/) pp.404-406 (CLXXXVII, 7 Apr 1583) and pp.530-534 (CCXL, 31 Jul 1583) read by this worker (GF-A2-2, 2 Oct 2026): Bowes's own Letter-Book clear copies of both letters, the folder's crib (AUDIT.md: plaintext in print, N-class there); no decipherment of the Cotton cipher signs is printed with them.

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

**Verdict on print: not found-solved, not an edition of the target letters.** [Verifier, 23 Sept 2026,
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

## Solver session (23 September 2026)

> Verifier, 23 September 2026 (AUDIT.md): **N1**. The plaintext is in print since 1842 (letter-book), and
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

Searched 23 September 2026, a search result only, not a novelty verdict:
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
  CSP Scotland vi (Boyd 1910) is still unreachable (see 23 September 2026). [Verifier, 23 Sept 2026: its HTRC
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


## Specialist reply, 24 Sept 2026 (Cryptiana)

The sign table was offered to S. Tomokiyo by email on 23 Sept 2026 (CONTRIBUTIONS.md row of that date; ASKS row 20).
He replied on 24 Sept 2026, accepted the identification, and updated https://cryptiana.web.fc2.com/code/unsolved.htm
the same day (section "Ciphers related to Sir Francis Walsingham", read 24 Sept 2026 14:29 UTC, one request): the
entry now credits the repository owner, links this folder, and records that the two letters are printed in the
Surtees Society Correspondence of Robert Bowes (1842) and CSP Scotland vi (1910). His own check of the manuscript
adds three corrections and one identification that our reading, made from the transcription alone, did not have:

- fragment 4: the print's "Manningvile" is the manuscript's MAGNYVIL (so the one-letter disagreement logged in the
  token table is the print's normalisation, not a key error);
- fragment 4: the token read as "and" is a handwriting abbreviation, not a cipher sign (our "?" token);
- "Montrosse" in the print stands for the numerical code 189 in the manuscript (grade C for 189 = Montrose);
- the other numerical codes (870, 149, 19, 29, 85 and the rest listed above from the Letter-Book) remain unread on
  his side too.

Status stays `partial`: the letter-substitution fragments are read and now confirmed by the specialist who
transcribed them; the numerical name-codes are the open remainder. Next step when a solver runs again: collate the
numerical codes across both letters with the Letter-Book and calendar contexts (870 appears with Cobham twice, 189 is
Montrose) and attempt identifications with CSP Scotland vi as the check; grade every identification C or M. No
image of the manuscript is in the folder; Tomokiyo's check is from his own reading of the leaves.

## Numerical name-codes (24 Sept 2026, LANE R4 E)

Worker LANE R4 E (Opus, cap $5), 24 Sept 2026 from 15:28 UTC. Disk and printed text only. No image was fetched.
Scripts: `codes_scan.py` lists every bare number in the body of the Surtees 1842 OCR (1,490 hits, `codes_scan.tsv`).
It skips years, page headers and money or measure words. `codes.py` collates the codes of CLXXXVII (7 Apr 1583) and
CCXL (31 Jul 1583) and writes `codes.tsv`. That file has one row per occurrence, with 200 characters of print
context, CSP vi token counts, the other occurrences in the Letter-Book, the identification, the grade and a
one-line reason. `codes.py --check` exits 1 if `codes.tsv` is stale. CCXXXIX has no codes.

**CSP Scotland vi (1910) is not on archive.org.** Four requests on 24 Sept 2026: three advancedsearch queries and
one metadata call. They found vols IV (`calendarstatepa00boydgoog`), V? (`calendarstatepa01boydgoog`, 1907), VIII,
IX (`calendarofstatep08grea`, metadata vol. 9) and XIII, but not vol. VI. The calendar check therefore rests on the
HTRC token counts already on disk (`audit_csp6_tokens.tsv`, pp.369-371 and 564-567). The calendar's running text
was not read. The token bags show that **the calendar keeps the codes as numbers**:
- p.371 (the 7 Apr entry) has 870 ×7, 91 ×3, 32, 54 and 000. The Surtees print has 91 ×3 as well.
- p.566-567 (31 Jul) has 223, 111, 54 and 85.
- The calendar prints Montrose in clear on p.371 and has no 189 token. This matches Tomokiyo's check.

So the 1910 calendar identifies none of the other codes, and no C grade can come from it.

**Result.** 12 codes, 33 occurrences in the two letters.
- **Codes:** C 1 (189), M 9 (870, 91, 32, 54, 000, 149, 19, 29, 223), unread 2 (85, 0100).
- **Occurrences:** C 3, M 28, unread 2.

The code is one-to-one across every use found (1577-1583). The one exception is 29, read as a misprint or OCR slip
for 23.

| code | identification | grade | basis (full line in codes.tsv) |
|---|---|---|---|
| 189 | John Graham, 3rd Earl of Montrose | C | Tomokiyo: MS f.196 has 189 where the print has "Montrosse". CCXL uses the same code |
| 870 | Esmé Stewart, Duke of Lennox | M | In France with Cobham and Smallet in 1583; "return this summer into 70" with French forces; last used Apr 1583, before his death on 26 May 1583 |
| 91 | James VI | M | "223 shall be on his knees before 91 and council" |
| 32 | Queen Elizabeth / England | M | "the minister of 32"; "32 hath shaken him off ... the course of France" |
| 54 | France | M | "others in 54"; "54, and chiefly the duke of Guyse" |
| 000 | England | M | "come into 000"; "an ambassador into 000 to intreat her Majesty" |
| 149 | Henri III (alt. Catherine de Médicis) | M | "an ambassador ... from 149 into this realm"; Mary via Mauvissière persuades 149 |
| 19 | Duke of Guise (alt. Anjou), weak | M | "149 and 19 ... until advertised by Manningville" |
| 29 | = 23, Mary Queen of Scots (list reads "149, 19, 23, and 85" in CLXXXIX) | M | 23: "dealt with Mauvisier", "intelligence with 23 will satisfy G. Douglas" |
| 223 | William Ruthven, Earl of Gowrie | M | "on his knees before 91 ... to acknowledge his fault done at Ruthen". CCXL also prints "Gowrye" in clear nearby |
| 85 | unread (Spain, the Pope, the Queen Mother, Archbishop Beaton?) | - | only in the two lists |
| 0100 | unread (the King? Dumbarton Castle?) | - | once: "delivery of 0100 to 32" |

key.tsv and reading.tsv are unchanged. 189 is a number in the manuscript, not one of Tomokiyo's drawn signs 02-28.
check.py still exits 0. What would settle the M grades:
- the Bowes/Cary nomenclator ("the cypher left me by Sir George Cary, the double whereof I send inclosed",
  CLXXXVII), or any decipher of these letters that gives the names;
- the running text of CSP vi pp.370-371 and 566-567.

Suggestion (not done): the Letter-Book uses about 40 further codes outside these two letters (0150 ×24, 111, 333,
0700, 41, 31, 70, 90, 440, 800 ...; `codes_scan.tsv`). Collating them would test and tighten the M grades above.

## Boyd's cipher asterisks and the F8-F11 alignment (NEXT-BOW, 2 Oct 2026)

Parent worker NEXT-BOW (account 2, Fable, brief `.claude/briefs/runs/2026-10-02-acct3-next-bow.md`, cap USD 4.8, box
45 min from 01:10 UTC), running the Verdict line's cheapest next step and nothing else. No image was fetched (none
exists online); everything below is conditional on Tomokiyo's transcription (rule 2). Files: `csp6_584_snippets.tsv`
(every snippet returned, 146 rows), `align_ccxl.py` (the alignment test), `check.py`/`key.tsv`/`reading.tsv` (regraded).

**Source.** CSP Scotland vi (Boyd 1910) through the Google Books search-within endpoint (`tools/gbooks_search_within.py`'s
`jscmd=SearchWithinVolume2`, at most three ~300-character hits per query, printed page number given), copies
`a3ZZTPid3VQC` (55 queries) and `414MAQAAIAAJ` (4 confirming queries); queries were phrases of the Letter-Book private
letter CCXL (Surtees vol.14 pp.530-534, `corpus/`) likely to fall on pp.566-568. 61 requests to books.google.com in
all (2 reachability tests included), one at a time, 1.6 s apart, no challenge page. The verbatim pages are still
unread (HathiTrust blocked from the cloud); the snippets cover every sentence of no.584 that CCXL's phrases could reach.

**Boyd's device.** Where the Cotton original has a cipher word he did not read, Boyd prints a blank with an asterisk
(`--*`, page-foot footnote "* In cipher."); where it has a code number in plain he prints the numeral in quotes
(`"223"`, `"000"`). So the asterisks fix the *position* of each cipher word in the original, and Bowes's own
Letter-Book copy (CCXL) supplies the word at that position. Snippets, OCR as returned (page, copy a3ZZTPid3VQC;
414MAQAAIAAJ agrees where queried, its OCR garbling the asterisk run as `at - * shall * *`):

- p.566, entry head: `July 31. 584. ROBERT BOWES TO [ WALSINGHAM ] . Cott . Calig . This day - * and " 223 " have given
  him understanding that the King and sundry of the Council especially chosen , and without` ... (margin `C. VII., fol.
  299.`; footnotes `* In cipher. * In cipher. etc. * The date is taken`, the second of which may belong to no.583's
  tail on the same page -- not read). CCXL: "This day Glencarne and 223 have given me understanding". So the first
  cipher word of f.299 is the name (F8, `15 glencarn`) and 223 stands there as a plain numeral.
- p.567: `he charges Gowrie to consent to it , or otherwise all that has been done by * late submission at * shall
  nothing avail him . In this * has sent for his advice , wherein he has let him see that he cannot with honour either
  subscribe or con- sent to`. CCXL: "by his late submission at Ruthen shall nothing avail him. In this 223 hath sent
  for mine advice". Two cipher words on one line with clear words between = F9 (`his` + `ruthen`, 3 + 6 signs);
  the third asterisk is a cipher group where CCXL has 223 = F10 (`02 02 03`). Earlier on the same page `the act done
  at Ruthven on his person was to be disproved` has no asterisk: that first Ruthen is in clear.
- p.567-568, abridged by Boyd: `Is informed that the King's affection to the Queen of England is greatly abated . The
  King is noted by sundry honest persons about` -- the Letter-Book's "kept in like sort as his mother is. Moreover
  upon suit made to 189 for the relief of Drumquhassell, 189 said that he must be examined what had passed betwixt 32
  and him for the delivery of 0100 to 32" is not in the calendar (queries `suit made`, `must be examined`, `what had
  passed`, `Drumquhassil`, `kept in like sort`: no hit on pp.566-568). No asterisk check exists for that sentence.
- p.568: `shall be 50,000 * sent to " 000 " in case he will agree thereto` (CCXL: "5000 men sent shortly into
  England" -- the Letter-Book resolved 000 as England; the 50,000 footnote is unread); `it is " done " him to think`
  (sic); postscript `himself could nothing prevail with the King ... condemnation of the act at Ruthven last year , yet
  on making up these [ this letter ]`, `mitigate the form and words in the first draft of the proclamation`, `the more
  liberal . Names the " intelligencer "` (Boyd withholds James Melvyn's name).
- Not retrievable this way: how many "In cipher" footnotes pp.567-568 carry (`In cipher` and `cipher` return their
  first three hits, pp.39/374/392), and whether the p.567 asterisks are printed with the dash.

**Alignment test (`align_ccxl.py`).** F8-F11 placed in transcription order on CCXL's 1,832 words with one shared key
(key.tsv's 19 letter values fixed; a value shared by at most two signs; F9 as two cipher words with clear words between,
per the asterisks; F8's unread leading sign 15 left free, its 8 read signs matching the first 8 letters of an 8- or
9-letter word; F11 allowed as code number + clear `and` + `him`). Control: the other 23 orders of the four fragments
(order-dependent, so it can differ; floor 1/24 = 0.042, as the gap line said).

| hypothesis | F8 | F9 | F10 | F11 | monotone placements, order F8 F9 F10 F11 | orders admitting one (of 24) |
|---|---|---|---|---|---|---|
| 02 = 2, 03 = 3 (F10 = 223) | `[15] glencarne` (2 places) | `his .. ruthen` (2) | `223` (4) | `32 and him` (1, p.532) | **1**: F8@15, F9@164-168, F10@175, F11@949-951 | 6 (0.25) |
| letters only, no digits (T3's `to him`) | same | same | none | `by/do/to him` (4) | 0 | 0 |

So sign 03 cannot be both the `t` of T3's `tohim` and a sign of F10: under letter values F10 has no place in CCXL at all,
and only the digit reading aligns. The order control is weak (6 of 24 orders also admit some placement, because 223
occurs four times in CCXL and `his .. ruthen` twice): the evidence is the asterisk positions, not the order. F11's
`32 and him` placement is unchecked (Boyd omits the sentence) and would make 25 a second sign for 2 while 02 is already 2,
so 25 stays unread. Alternatives for F10 weighed: a three-letter name of pattern AAB does not exist, and Boyd's asterisk
(not a quoted numeral) shows the original has a cipher group there, unlike the plain 223 at the entry head -- cipher
digit-signs 2 2 3 is the reading, at grade M (one fragment, no image).

**Regrading (rule 4, `check.py --write`, exit 0 on `--check`).** Three changes: (1) F4 pos.26, Tomokiyo's sign 27, is a
handwritten `and` abbreviation (his manuscript check, 24 Sept 2026) -- kept in ciphertext.txt as transcribed, listed in
check.py's EXCLUDED, printed with value `and` and counted apart; the cipher-token total is 100. (2) F9's nine tokens go
from S to **C**: the calendar of the original marks two cipher words at `by * late submission at *` and the Letter-Book
copy gives `his` and `Ruthen` there, which the key reads independently. (3) F10 = `223` at M (02 = 2, 03 = 3), F11 pos.1
(03) = 3 at M; 25 unread. MAGNYVIL and Montrosse = code 189 (C) are now in check.py's F4 note. Grades: **S 73, M 12,
I 3, H 0, C 9, unread 3 (signs 15, 25, 28), total 100**, plus 1 excluded; read 97 of 100 (97.0%). Still cryptanalytic
with a known-plaintext component (C 9), no H.

**For the codes worker (gap 3), not pursued here:** Boyd prints 223 as a plain numeral at the entry head (p.566) and
`"000"` where CCXL has "England" (p.568) -- an editorial resolution of 000 like the `["32"]` gloss on p.371; `50,000*`
against the Letter-Book's "5000 men" is a discrepancy with a footnote not yet read.

**Not found / rule 10.** Boyd did not read the cipher words (he printed asterisks), so the calendar adds positions, not
a decipherment; the words come from Bowes's own Letter-Book copy printed in 1842. Nothing here is a novelty claim; the
class is the verifier's (AUDIT.md, N1), and AUDIT.md section 10's sentence "Which words they mark cannot be read from the
snippet" is now superseded for pp.566-567 -- the parent or a verifier carries this into AUDIT.md (rule 10 propagation),
not this worker. Suggestions, one line each: the parent's LOCAL-QUEUE.tsv row for the verbatim pages should ask what the
second p.566 footnote marks, how the p.567 asterisks are printed, and what the p.568 `50,000*` footnote says; the gap-3
collation should start from the three Boyd readings above.

Requests this session: books.google.com 61 (one at a time, 1.6 s apart, browser User-Agent per the tool, no login, no
challenge). No other host. No subagents.

## GAPS59-bowes-walsingham-1583 (3 Oct 2026, account-4)

Worker GAPS59 (account 4), 3 Oct 2026 from 08:08 UTC (clock read). The Verdict's gap-3 step only: the codes_scan.tsv
collation, starting from Boyd's three readings. Disk only (Surtees OCR in corpus/, csp6_584_snippets.tsv, AUDIT.md
section 10); no network request, no image, no subagent, 0 vision calls.

**Filter (`codes_collate.py`, `--check` exits 0).** The 1,490 numbers of codes_scan.tsv are re-derived with the same
regex (count asserted equal) and filtered with stated rules: front matter/introduction 668, single digits 196, page
headers 109 (OCR variants of BOWES CORRESPONDENCE), dates 90, folio numbers 76, sums 41 (`,000`), counts and sums with
a noun 34, references 20 (Harl. MS. 6999, Art. N; Letter-Book p. N), back matter 13 (library stamp), years 7, year
splits 2, initial 1, and 11 read by eye (MANUAL in the script: page numbers, dates, the 24 gentlemen). Kept: **221
occurrences of 54 numbers**, each dated by its letter heading (`~` = heading carries no year, previous letter's year).
Dropped hits and the rule that dropped each are in `codes_collation_filter.tsv`; kept ones in `codes_collation.tsv`.
The kept set is a lower bound: OCR-damaged codes the scan regex cannot see were found by grep and not added: `S70`
(= 870, CLXXXIX), `1)1`/`J)l` (= 91, five times), `fO` (CXVIII, 'recover fO with the presence of 31'), `GOG`
(CLXIII), `4sJ` and `SO` (CCLXV).

**Boyd's three readings, collated against the Letter-Book (rule 4: C only from Boyd's printed calendar text, the F9
precedent: Boyd's position in the original + the Letter-Book word at the same position).**

| Boyd (CSP Scotland vi) | Letter-Book (Surtees) at the same place | result |
|---|---|---|
| p.568 `shall be 50,000* sent to "000" in case he will agree thereto` | CCXL p.532 `5000 men sent shortly into England in case he will agree thereunto` | **000 = England, C** (the original has the numeral 000 where Bowes's own copy has England) |
| p.371 `Finds the Queen of England ["32"] as well resolved to entertain the matter` | CLXXXVII p.404 `finding therewith, as well her Majesty's resolution to entertain the matter` | **32 = Queen Elizabeth, C** (same reasoning; Boyd's bracket is his gloss, the Letter-Book's 'her Majesty' is the clear word) |
| p.566 `This day --* and "223" have given him understanding`; p.568 `"223" and himself could nothing prevail` | CCXL `Tins day Glencarne and 223 have given me understanding`; `the labour of 223 and himself` | no identification: both renderings keep the numeral. 223 stays M (Gowrie) |
| p.568 `50,000*` | `5000 men` | open: a tenfold difference and an 'In cipher' asterisk; the footnote is unread (gap 4's question) |

So 000 and 32 are no longer the one code for "England / the Queen" the 24 Sept table allowed: 32 is the Queen, 000 the
country, one-to-one. codes.py now reads **C 8, M 23, unread 2 occurrences (by code C 3 = 189, 32, 000; M 7; unread 2)**,
up from C 3, M 28; `codes.py --check` exits 0, `check.py --check` exits 0 (key.tsv, reading.tsv unchanged).

**91 = the King of Scots is stated in the Letter-Book itself** (CXXI, 8 Nov 1582, p.237): "By the error of my man that
copied out the last cypher you sent me ... in figure for the King of Scots had wrongfully placed and set the figures of
31 for 91, therefore in my former letters to you of the ijd hereof ... set down for the King aforesaid the figures of
31, where it should have been 91". CXVIII is dated 2 Nov 1582, so its four 31s are 91. This is known plaintext of the
key, but the brief allows C only from Boyd, so codes.py keeps 91 at **M, marked C-candidate**; the parent decides. The
same sentence says the cipher of 1582-83 was sent by Walsingham ("the last cypher you sent me"), a lead for the
known-keys rung.

**One-to-one test, 1580-1583.** Every code of the two target letters keeps one plausible referent across all its
dated uses (codes_collation.tsv, contexts read): 91 (32 uses, 1582-83), 870 (26, 1582-Apr 1583, none after Lennox's
death on 26 May 1583), 32 (16), 223 (15, 1583 only; 'on his knees before 91 ... at Ruthen', '485 sought that 223 might
be warded', '0150 is a special friend to 223'), 149 (9), 000 (4), 54 (2), 19 (3). Conflicts and doubles, logged, none
settled by majority:
- 31 for 91 (CXVIII): explained by Bowes himself (copyist's error), above.
- 29 for 23 (CLXXXVII) and 140 for 149 (CCXXXVI): single occurrences beside the regular form in the same list or
  phrase; print or OCR slips, M as before.
- 70 and 90 (both CLXXXIX): 70 is a place Lennox returns into, departed from, has friends and livings in (Scotland on
  context, also CXVIII 'recover fO'); 90 once, 'his behaviour and course in 90 in the time past', which fits Scotland
  too. Two codes for one country, or 90 is another place; unresolved, not in the target letters.
- 19 = Guise is weakened, not contradicted: CXXIII prints 'Guise' twice in clear beside '19 is come into Piccardy',
  and CCXL prints 'the duke of Guyse' in clear beside 54. Clear-name co-occurrence was counted for every M referent
  (the King appears in clear in 11 of the 13 letters that use 91), so the letters mix clear and code and this count
  cannot test an identification; recorded as context only.
- 1580 letters (XXVIII-LXXVII: 98, 45, 48, 24, 27, 36, 72) use two-digit codes that never recur after 1580, and the
  1582-83 letters never use them: a different cipher (the 1580 one), so they say nothing about the 1583 code.

**85 and 0100.** Not found anywhere else in the Letter-Book: 85 only in the two lists ('149, 19, 29, and 85',
CLXXXVII; '149, 19, 23, and 85', CLXXXIX), 0100 only in CCXL; grep for OCR variants (`S5`, `8.5`, `0l00`, `OlOO`,
`O100`) found none. Both stay unread.

**Other 1582-83 codes collated (no identification made here; contexts in codes_collation.tsv).** 0150 (24, 1582-
1583: Bowes's principal informant at court, refuses a French present, 'many battles betwixt 0150 and me'), 111 and 333
(6 and 4, 1583, lords who 'shall down'), 485 (4, an adversary of 223), 321 (3), 900 (3), 00 (5), 0700 (2), and 22 single
uses (001, 002, 010, 10, 41, 44, 81, 220, 249, 440, 770, 787, 800, 910, 2560 ...). None is in the target letters.

Not found / rule 10: no decipherment or key of the 1582-83 code was found in the Surtees print beyond Bowes's own 91
sentence; the two C grades come from Boyd 1910 and Surtees 1842, both in print (AUDIT.md, N1). No novelty claim.

## Verifier note: the code layer in print (VERIFY-BOWES, 3 Oct 2026)

Verifier correction (AUDIT.md section 13), not a solver step. The numeric name-codes are not open in print:
Alan Haynes, *Invisible Power* (1992; reissued as *The Elizabethan Secret Services*, 2000, 2009) prints "In April 1583
Robert Bowes was using it for communications with Walsingham: France is 54; Scotland, 70; James VI, 91; the Earl of
Lennox, 870; Elizabeth, 32 and Mary, 23"; Stevenson's own Contents to this folder's crib volume (Surtees 14, 1842,
p.xxix, no.189) summarises "870 shall return this summer into 70" as "Lennox's return into Scotland"; and Boyd (1910)
glosses 32 as the Queen of England. So 870, 91, 32, 54 and 23 (29) are published identifications (key source
`published`, class N0 for these codes); 000 = England (N2), 189 = Montrose (N1) and the M inferences 149, 19, 223 are
ours. codes.tsv's identification column and the 24 Sept text above ("remain unread", "open remainder") predate this
and carry no credit; cite Haynes 1992 and Stevenson 1842 with any code identification. Haynes's footnote source is
unread (lending-only, snippet search only): it may name a period key, which is the known-keys rung below.

## Known-keys rung: Walsingham-Wotton 1585 and one TNA search (R11A-BOWES, 6 Oct 2026)

Worker R11A-BOWES (LANE-RUN11-account-1), 6 Oct 2026 13:48-13:53 UTC by `date -u`. Not a reading; nothing adopted, so no PREREG was needed (brief: only an adopted code value needs one).
- **Source.** S. Tomokiyo's reconstruction of the Walsingham-Wotton cipher of 1585 (Cryptiana `elizabeth.htm`, Caligula C VIII f.276 and Add MS 32657; credit S. Tomokiyo): `walsingham_wotton.jpg` and `elizabeth_walsingham_wotton2.png`, fetched once from cryptiana.web.fc2.com (https; the http URL only redirects) into `images/wotton1585/`. The second image gives a homophonic sign alphabet (a-z, nulls) and six name codes: the Queen 3, the King 10, Earl of Leicester 14, Arran 19, England 36, Scotland 37.
- **Test.** Direct value comparison against this folder's code layer (`wotton1585_compare.tsv`). Shared referents: 0 of 4 agree (Queen 3 vs 32, King 10 vs 91, England 36 vs 000, Scotland 37 vs 70). Wotton numbers that also occur in Bowes's Letter-Book 1580-83 (codes_collation.tsv): 3 of 6 (10, 19, 36), and every one's Bowes context contradicts the Wotton value (10 is named beside "the King" as someone else, 1582; 19 "is come into Piccardy with the French army", 1582, not Arran; "travelled with 36", 1580, a person, not England). Control for the method: Bowes's own dated letters 1582 and 1583 agree with each other on 91, 32, 870 and 223 (codes_collation.tsv, one referent per code across dates), so a value comparison does show agreement when two letters share a key. 85 and 0100 are not among the Wotton codes. Result: the 1585 Wotton nomenclator is a different code list from Bowes's 1582-83 one; it supplies no value for 85, 0100 or the M codes. The sign alphabet could not be compared: Bowes's signs exist here only as Tomokiyo's index numbers 02-28 and his glyph sheet CottonMSBowes.png is 404.
- **TNA Discovery API**, `records?sps.searchQuery=Bowes cipher`: with `sps.dateFrom/dateTo` 1580-1585, 0 records; without dates, 3 records (Manchester Cathedral 1756, Bedfordshire postcards, Lambeth Talbot Papers 1544-58), none a Bowes or Cary cipher of 1582-83. Not searched: a browse of SP 106 (State Papers, Ciphers), the series where a Cary/Bowes key would sit if it survives.
- Requests: cryptiana.web.fc2.com 4 (2 redirects, 2 images); discovery.nationalarchives.gov.uk 2.

## SP 106 browse on TNA Discovery (R11A-BOWES2, 6 Oct 2026)

Worker R11A-BOWES2 (LANE-RUN11-account-1), 6 Oct 2026 14:26-14:30 UTC by `date -u`. Lookup only; no key change. Table: `sp106_browse.tsv`.
- **Series search.** Discovery API `search/records`, `sps.recordSeries=SP 106`: 'cipher' 68 records (the whole series, SP 106/1-67, piece level); 'Scotland', 'Bowes', 'Cary', 'Carey', 'Walsingham' 0 each.
- **Elizabethan pieces.** SP 106/1 (C3677731, "Ciphers used at the time of Elizabeth I, names A to L. Indexed."), SP 106/2 (C3677732, names M to W, indexed in SP 106/1), SP 106/3 (C3677733, Elizabeth I and before, names unknown). `records/v1/details`: `digitised: false` for all three; `records/v1/children`: 0 child records for all three. So Discovery describes SP 106 only at piece level: no item list exists there to browse, and whether a Bowes, Cary or Hunsdon key sits in SP 106/1 (A-L) or 106/3 cannot be read from the catalogue. Not found: any Discovery record naming Bowes, Cary or Scotland in SP 106.
- **Item level from disk instead.** DECODE's key list (`sources/decode/keys-all-2026-09-28-merged.tsv`, no new request) holds 34 SP 106/1-3 leaves. Dated within 1580-84: none. Dated ones: 1509-34, 1554, 1559 x2, 1562, 1566, 1569, 1577 x2, 1587, 1588 (R337, Croft's key, already compared for harley-287-1587), 1590, 1594, 1596; 20 carry only the reign span 1558-1603. The list carries no sender/receiver field, so those 20 undated leaves cannot be ruled in or out from disk.
- Requests: discovery.nationalarchives.gov.uk 12 (6 search, 3 details, 3 children), all 200, 1.7 s apart.
- Next (one line, not run): read the DECODE record metadata (receiver/sender, docket) of the 20 undated SP 106/1-3 leaves with `tools/decode_list.py` / RecordsView, login-free metadata first, to find any Bowes, Cary, Hunsdon or Scottish-embassy key of 1580-84, ~$1.

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Updated in place 2 Oct 2026 (NEXT-BOW) for what the Boyd-asterisk step settled; see the step section above. Settled and removed from the list: the F4 pos.26 sign-27 gap (excluded as a handwritten 'and', check.py EXCLUDED, key.tsv row 27; MAGNYVIL and 189 = Montrose carried into check.py's F4 note).
Read so far: 97 of 100 cipher-sign tokens of Tomokiyo's transcription (97.0%: S 73, M 12, I 3, C 9, H 0; unread 3 = signs 15, 25, 28), reading.tsv grades line (check.py --write, 2 Oct 2026); Tomokiyo's 24 Sept correction (F4 pos.26, sign 27, a handwritten 'and' abbreviation) is now folded in as an excluded token, so the total is 100, not 101. F9 is C from Boyd's calendar asterisks + the Letter-Book word at the same position; F10 = 223 and F11's first sign are M (NOTES "Boyd's cipher asterisks", 2 Oct 2026). Numeric code layer: 31 of 33 occurrences identified (C 8, M 23; by code C 3 = 189, 32, 000, M 7, unread 2 = 85, 0100), codes.tsv (GAPS59, 3 Oct 2026; was C 3, M 28). Unmeasured: whether Tomokiyo's file holds every cipher word on ff.196/299/303 (no image), and the B VIII f.251-252 and f.306 cipher words (no transcription).
- F11 sign 25 (1 token, f.299, 31 Jul 1583) - blocker: open-codes; settled 2 Oct 2026 for the rest of F10/F11: F10 (02 02 03) sits where Boyd p.567 prints a cipher asterisk and the Letter-Book has 223, so 02 = 2, 03 = 3 (M) and F11 = '3 ? him'; T3's 'tohim' (03 = t) is excluded (align_ccxl.py: under letter values F10 has no placement in CCXL and no fragment order aligns; under digits exactly one monotone placement in transcription order, control 6 of 24 orders, floor 0.042). The only CCXL phrase of F11's shape is 'betwixt 32 and him' (p.532), which Boyd's calendar omits (no asterisk check) and which would make 25 a second sign for 2 beside 02; next: nothing cheap -- an image of f.299 (gap 6's reproduction request) or the verbatim p.567-568 text if Boyd prints that sentence after all, $0 extra on gap 4's row
- Numeric code layer: 85 (2 occurrences) and 0100 (1) unread; 870, 91, 54, 149, 19, 29(=23), 223 at M (23 occurrences); 189, 32, 000 at C - blocker: open-codes; the codes_scan.tsv collation ran 3 Oct 2026 (GAPS59 step above; codes_collate.py, codes_collation.tsv: 221 kept occurrences of 54 numbers, 1580-83): Boyd's printed numerals aligned to the Letter-Book's clear words give 000 = England (p.568 vs CCXL) and 32 = the Queen (p.371 vs CLXXXVII) at C; 91 = the King is Bowes's own statement (CXXI, the 31-for-91 erratum), held at M as a C-candidate for the parent; every target-letter code keeps one referent across its dated uses (conflicts 31/91, 29/23, 140/149, 70/90 logged, none settled by majority); 85 and 0100 occur nowhere else in the Letter-Book, OCR variants included; Boyd's 223 is a numeral in both renderings, no identification; the known-keys rung ran 6 Oct 2026 (R11A-BOWES: Walsingham-Wotton 1585 codes agree on 0 of 4 shared referents, a different list; TNA Discovery 'Bowes cipher' 0 relevant records); the SP 106 browse ran 6 Oct 2026 (R11A-BOWES2: Discovery holds SP 106/1-3 at piece level only, undigitised, 0 child records; DECODE's on-disk key list has no SP 106/1-3 leaf dated 1580-84 and 20 undated); next: DECODE record metadata of the 20 undated SP 106/1-3 leaves for a Bowes/Cary/Scottish key, ~$1
- CSP Scotland vi (Boyd 1910) verbatim running text, pp.370-371 (no.389, fol.196) and pp.566-568 (no.584, fol.299) - blocker: waiting-on LOCAL-QUEUE L44 (owner's desk runner, HathiTrust); the search-within pass of 2 Oct 2026 (csp6_584_snippets.tsv, 61 requests) reached no.584's running text around every asterisk CCXL's phrases could locate: p.566 'This day --* and "223"', p.567 'by * late submission at *' and 'In this *', p.568 '50,000* sent to "000"', and found the 189/32/0100 sentence omitted by Boyd; still unread verbatim: what the second p.566 footnote marks (perhaps no.583's tail), how the p.567 asterisks are printed, the p.568 '50,000*' footnote, and pp.370-371 as a whole (HathiTrust nnc2.ark:/13960/t1gh9nc18 Cloudflare-blocked from the cloud); LOCAL-QUEUE.tsv row L44 (hathitrust-page) filed 3 Oct 2026 by GAPS60 with those four questions and the F11 '189/32/0100' sentence check
- F5 sign 28 and F8 pos.1 sign 15 (2 tokens, each a single occurrence) - blocker: open-codes; neither sign recurs in the 100 tokens; F5 is a whole one-sign fragment between F4 ("... Glencarne and" [189]) and F6 (Mauvissier), where the print and Boyd p.371 have "with especial commendations from "870"" -- but the manuscript writes codes as numerals (189, Tomokiyo), so 28 = 870 is not established (key.tsv note); 15 is now positioned (2 Oct 2026): F8 is the first cipher word of f.299, Boyd's 'This day --*' where CCXL has 'Glencarne', so 15 stands inside the one blank that covers the name -- a null, a word-start mark or a misread, not a separate word; next: the image (gap 6)
- Doubtful tokens in the read part: three I-grade tokens (F1 pos.7, F3 pos.2, F4 pos.10), the unexplained 'o' at F4 pos.16 (sign 20, between 'huntley' and 'glencarne', key.tsv note), and the M signs 14, 21, 23, 26 (single occurrence) and 20, 24 (two occurrences each; the classifier listed them as single), plus 02, 03 (digit-signs from one fragment, 2 Oct 2026) - blocker: needs-physical-access; Cotton Caligula C VII is undigitised (BL "digital images currently unavailable", IIIF 403, images/manifest.json; BL IIIF dead since 2023) and Tomokiyo's glyph sheet CottonMSBowes.png redirects to a 404 on cryptiana.web.fc2.com (classifier, 1 Oct 2026; the Wayback CDX check for it was tried this pass, 2 Oct 2026 00:28 UTC, connection reset twice, 2 requests, not retried further); Tomokiyo has already given his manuscript check and nothing more is asked of him (CONTRIBUTIONS.md); no REQUEST.md or ASKS row exists for a BL reproduction; next: parent files an ASKS row and REQUEST.md for BL reproductions of Caligula C VII ff.196r-197v, 299r-v, 303r (access route 4, the person's), ~$1
- Cotton Caligula B VIII f.251r-252v (Bowes? to Cecil?, [1583?]) and f.306r (undated, "Monsieur de la Noues", "Mr Randolph"), "a few words in cipher", not deciphered - blocker: needs-physical-access; no transcription exists anywhere (Tomokiyo's CottonMSBowes.txt covers only C VII f.196 and f.299), the volume is undigitised (images/manifest.json, IIIF 403), and Cryptiana elizabeth.htm (sources/cryptiana/web/, the B VIII block) marks both "not deciphered"; add these leaves to the same BL reproduction request, no extra cost

## Escalation (1 Oct 2026)
- [ ] siblings: opened so far -- the BL catalogue for neighbouring leaves (f.193, f.297, f.300: no cipher note); the B VIII fragments f.251-252, f.290-293, f.306 (catalogued); the Letter-Book copies CLXXXVII, CCXXXIX, CCXL (used as cribs); DECODE (no record; Aymeloglu's DECODE cache has no Caligula C VII). Opened 3 Oct 2026: the Letter-Book codes of 1580-83 in codes_scan.tsv (GAPS59: 221 occurrences, 54 numbers, codes_collation.tsv; the 1580 letters use a different two-digit code). Not opened: Harley 6999 (11 Jan 1581, Surtees p.164, "cannot be expressed by types") and the Cotton-sourced 1580 letter LXII ("names in cypher", Surtees prints only the numeric layer, AUDIT.md section 3(b)), both without images. B VIII f.290-293 reads from its period interlinear decipherment (Tomokiyo, elizabeth_bowes.png). The codes_scan.tsv collation ran 3 Oct 2026 (gap 3)
- [x] clear-pages: Bowes's Letter-Book clear copies of the same two letters (Surtees vol.14 CLXXXVII, CCXL; corpus/) read the cipher: T5 crib.py covered 43/101 tokens vs 28.8 +- 2.9 (other letters' word lists) and 27.0 +- 3.1 (shuffled tokens), crib_runs.tsv, and key.tsv was built from it. Boyd's calendar abstracts (AUDIT.md section 10) are a second clear rendering; 2 Oct 2026: their "* In cipher." asterisks on pp.566-567 fix the position of each cipher word of f.299 (F8 at the entry head, F9's two words, F10 at 'In this *'), used for the F9 C grade and the F10 digit reading (NOTES "Boyd's cipher asterisks"). For B VIII f.290-293 the period interlinear decipherment is the clear text
- [ ] known-keys: T4 tried Tomokiyo's f.290-293 key (elizabeth_bowes.png): not applicable, drawn glyphs vs his 02-28 index numbers, and the CottonMSBowes.png that maps them is 404 on Cryptiana (Wayback CDX attempt 2 Oct 2026 00:28 UTC: connection reset twice). KEY-OFFICES.tsv line 8 and KEY-DESIGN.tsv line 18 hold only this target's own key. Tried 6 Oct 2026 (R11A-BOWES, section above): Tomokiyo's Walsingham-Wotton 1585 reconstruction (images/wotton1585/) shares no name code with Bowes's list (0 of 4 shared referents; 10, 19, 36 contradicted by Bowes's own contexts); one TNA Discovery API search 'Bowes cipher' found no Cary/Bowes key. Tried 6 Oct 2026 (R11A-BOWES2): SP 106 on TNA Discovery is piece-level only (SP 106/1-3 undigitised, no items; 'Bowes', 'Cary', 'Scotland' 0 hits); DECODE's key list has no SP 106/1-3 leaf dated 1580-84. Still untried: the Cary nomenclator ("the cypher left me by Sir George Cary", CLXXXVII) among the 20 undated SP 106/1-3 DECODE leaves; next: their DECODE record metadata, ~$1
- [x] print: Surtees vol.14 full text (corpus/, print-check.tsv); CSP Scotland vi through HTRC token counts (audit_csp6_tokens.tsv) and Google Books search-within running-text snippets of nos 389 and 584 (AUDIT.md section 10: names in clear, codes as quoted numerals, 'Queen of England ["32"]'; 2 Oct 2026, csp6_584_snippets.tsv: no.584's text around every asterisk, '"000"' for England, the 189/32/0100 sentence omitted by Boyd); Thorpe's CSP Scotland i (SP 52, AUDIT.md section 3(a)); archive.org (no vol. VI); BHO (paywalled); JSTOR-QUEUE rows 8-11 (done 24 Sept, nothing); open-index pass (AUDIT.md, 24 Sept); Bourdeau and Aymeloglu greps; Cryptiana. Still unread: the verbatim calendar pages (gap 4)
- [x] key-rebuild: T1 ciphertext-only anneal is a non-test (its matched control design d, names only, reads 15.8-32.7%, a model limit); T3 anneal with the 17 S signs fixed agrees 85/93, 'tohim' noted not adopted and now excluded (2 Oct 2026); codes.py collated the two letters' numeric codes (C 1, M 9); the constrained F8-F11 alignment against CCXL ran 2 Oct 2026 (align_ccxl.py: one monotone placement in transcription order under 02 = 2, 03 = 3; none under letter values; control 6 of 24 orders, floor 0.042 -- the asterisk positions carry the evidence, not the order). Each instrument ran once, so nothing is retired
- [ ] image-check: no manuscript image (C VII and B VIII undigitised at the BL, images/manifest.json; glyph PNG 404). Tomokiyo's own reading of the leaves (24 Sept) gave MAGNYVIL, 'and' as an abbreviation, 189 = Montrose. The three I tokens, the F4 pos.16 'o', the M signs and the digit-signs 02, 03 have not been re-read. Planned: ASKS row and REQUEST.md for a BL reproduction (gap 6), which the person must order
- [x] retry: Tomokiyo's corrections folded into check.py, key.tsv and reading.tsv on 2 Oct 2026 (sign 27 excluded, total 100; check.py exit 0); F10 and F11 rerun through align_ccxl.py (above)
Verdict: keep going: 3 internal gaps (3 open-codes: the code layer 85/0100 and M codes, sign 25, signs 15 and 28), 1 waiting-on (LOCAL-QUEUE L44, the verbatim calendar pages), 2 needs-physical-access; gap 4's LOCAL-QUEUE.tsv row is filed (L44, 3 Oct 2026, GAPS60; waiting on the owner's desk runner); cheapest next: DECODE record metadata of the 20 undated SP 106/1-3 key leaves for the Cary/Bowes key, ~$1 (the SP 106 Discovery browse ran 6 Oct 2026: piece level only, no hit) (the Walsingham-Wotton 1585 rung ran 6 Oct 2026, no shared codes); the codes_scan.tsv collation ran 3 Oct 2026 (GAPS59: 000 and 32 to C)

## Web and blog check (GF-A2-2, 2 Oct 2026)

Worker GF-A2-2 (account 2, LANE-A2PUSH), 2 Oct 2026 21:16-21:21 UTC (clock read). WebSearch standard mode; WebFetch for opened hits. Known answer: Bowes's own clear Letter-Book copies (Surtees vol.14 CLXXXVII, CCXL) and Boyd's calendar (CSP Scotland vi nos 389, 584), already in AUDIT.md. A hit repeating those is not a decipherment of the cipher signs.

| # | Query / page | Hits |
|---|---|---|
| 1 | `Robert Bowes Walsingham 1583 cipher letter Edinburgh deciphered Glencairn` (sender + recipient + date) | Wikipedia (Robert Bowes, diplomat); BL searcharchives 040-001102385 (Caligula C VIII, 1584 letters); news items on the 2023 Mary Queen of Scots decipherment (Lasry, Biermann, Tomokiyo), other letters. No reading of f.196/f.299 cipher signs. |
| 2 | `"Caligula C VII" cipher Bowes 1583` (shelfmark + cipher) | BL searcharchives 040-001102384 (the volume record, opened, row 9); livesandletters.ac.uk Herle catalogue 013; unrelated numismatic pages. No reading. |
| 3 | `"Glencarne and 223" OR "Glencairn and 223" Bowes` (distinctive clear phrase, CCXL p.530) | 0 relevant hits (Glencairn museum, whisky glasses). |
| 4 | `Robert Bowes to Walsingham 7 April 31 July 1583 Cotton Caligula cipher unsolved Tomokiyo` (folder title) | BL records 040-001102383/4/5; popular-history pages on Walsingham's spies; flyingpenguin "Secret Inks". No reading. |
| 5 | `site:scienceblogs.de klausis-krypto-kolumne Bowes Walsingham Schottland 1583` (Cipherbrain) | No scienceblogs.de result; general Bowes/Mary pages only. |
| 6 | `site:cryptiana.blogspot.com Bowes Walsingham Scotland cipher` (Cryptiana blog) | No cryptiana.blogspot.com post returned. Tomokiyo's own page `elizabeth.htm` (on disk) marks both letters "not deciphered" (check-solved above), and his 24 Sept 2026 reply (section "Specialist reply") is already folded in. |
| 7 | `site:ciphermysteries.com Robert Bowes cipher Scotland 1583` (Cipher Mysteries) | One ciphermysteries.com result (?p=7357, the 1539 "Devil's Handwriting" post, unrelated); BHO CSP Scotland v pp.231-242 and vi pp.434-481 (May 1583) pages; TNA Discovery creator page. Nothing on these letters. |
| 8 | (Bourdeau `targets/napoleon/unsolved.txt` l.57, a mirror of Tomokiyo's page, found by grep in the clone) | "There are some undeciphered ciphertext in letters to Walsingham. One is from Robert Bowes (1583)". Confirms status, no reading. |
| 9 | WebFetch searcharchives.bl.uk/catalog/040-001102384.json (Caligula C VII item list) | ff.196r-197v "Partly in cipher"; ff.299r-v, 303r "Some use of cipher". Neighbours: f.193 (Bowes, 6 Apr 1583, original), f.297r-v (Bowes to Walsingham 31 Jul 1583, 17th-century copy), ff.300r-302r (Bowes, 31 Jul 1583, original). The volume's "deciphered" items are ff.69v-70r (Bowes, 17 Oct 1582), **ff.201r-203r ("Letter of Robert Bowes deciphered, Edinburgh, 12 apr 1583")**, f.325 and ff.338/341: deciphered copies of other letters, already listed in AUDIT.md section (d). |

Comment threads: no hit is a blog post about these letters, so there was no relevant comment thread to read. **Result: no decipherment of the f.196 or f.299 cipher signs found on the open web or in the three blogs**, beyond the clear-text copies and calendar already in AUDIT.md.

## Premise check (GF-A2-2, 2 Oct 2026)

- (a) **Decipherments the folder already mentions.** Found, already known and already classed: the folder's whole reading rests on Bowes's own clear Letter-Book copies (Surtees vol.14 CLXXXVII pp.404-406, CCXL pp.530-534, checked again today, see line 2) and Boyd's calendar (CSP Scotland vi nos 389, 584, names in clear, AUDIT.md sections 4 and 10). The plaintext of both letters is in print, and the open item is the sign-to-letter table and the residual codes (AUDIT.md row C). Tomokiyo's f.290-293 interlinear key (Caligula B VIII) was opened and does not apply (Escalation, known-keys). No other decipherment is mentioned.
- (b) **Other solvers' working files.** Not found: shallow clones today. Bourdeau has no target folder; his only Bowes mention is the Tomokiyo mirror line in row 8 above (the `TARGETS.md` line cited on 23 Sept no longer matches a grep for "Bowes"). His decode catalogue harvest has Caligula C II rows, not C VII. Aymeloglu's repository (cited, not copied) has no Bowes or Caligula C VII entry.
- (c) **Physical neighbours.** Found, already known; no new decipherment of these two letters. BL item list fetched today (row 9): f.297r-v is a 17th-century copy of Bowes's 31 Jul 1583 letter, calendared by Boyd as no.583 with f.300 (AUDIT.md p.564 note), so it is presumably the public letter (Surtees CCXXXIX) and not the cipher-bearing private letter, an inference from the calendar, not from the leaf. ff.201r-203r is a decipherment of the 12 Apr 1583 letter, five days after f.196's 7 Apr and a different letter (Surtees CLXXXVIII/CLXXXIX are the xijth April letters, p.407ff.). It is a possible same-period key sibling, not a reading of f.196. ff.69v-70r (17 Oct 1582) is the same kind of sibling. The facing pages and any laid-in slips cannot be viewed: Caligula C VII is undigitised (images/manifest.json; iiif.bl.uk dead since 2023). Next step for the siblings: whether ff.201-203 or ff.69v-70r carry cipher beside the deciphered copy (a key witness for signs 15, 25 and 28) can only be settled from the leaves (BL reproduction request).
- (d) **Recipient-side editions.** Found, already known: the recipient is Walsingham, whose side is CSP Scotland vi (Boyd 1910), already used (AUDIT.md section 10; NEXT-BOW snippets). The Scottish side holds no recipient for an English ambassador's report. Nothing new.

Requests this pass: searcharchives.bl.uk 1 (via WebFetch); github.com 2 (shallow clones, shared with the other two targets).

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: the known-keys rung this folder's Verdict names as cheapest -- Tomokiyo's Walsingham-Wotton 1585 reconstruction (elizabeth.htm images) tried against the code layer (85, 0100 and the M codes) plus one TNA Discovery API search, ~$2. LOCAL-QUEUE L44 and the BL reproduction (gap 6) stay the outside blockers.

## IA-DESK-ALT (account-3 worker, 5 Oct 2026): CSP Scotland vi via Internet Archive, re-checked

These are search results only (rule 10).

Two advancedsearch queries on 5 Oct 2026 returned the same set as on 24 Sept: CSP Scotland vols I, II, IV, VIII, IX, XIII (`calendarstatepa00baingoog`, `CalendarStatePapersMaryQueenOfScotsVol2`, `calendarstatepa00boydgoog`, `calendarofstatep0008vari`, `calendarofstatep08grea`, the XIII.1 item) and Thorpe's 1858 calendar. The second Boyd Google scan, `calendarstatepa02boydgoog` (1903), was not opened; its metadata gives no volume and is dated 1903 (vol. III was published in 1903), not 1910, so it is not vi.

**Vol. vi (Boyd 1910) is still not on IA.** Google Books has already been used for search-within snippets only, not full view (csp6_584_snippets.tsv). The verbatim pp.370-371 and 566-568 **still need HathiTrust** (LOCAL-QUEUE L44, `nnc2.ark:/13960/t1gh9nc18`). Gap 4 is unchanged.

## CSP Scotland vi pp.370-371 page read (5 Oct 2026 03:47 UTC, owner's browser on HathiTrust nnc2.ark:/13960/t1gh9nc18, seq 414-415; LOCAL-QUEUE L44 part 1)

Screenshots in the private repository (bowes-walsingham-1583/csp-vi/). No. 389, Bowes to [Walsingham], 7 Apr 1583, Cott.
Calig. C. VII fol.196, "4 pp. Holograph. No address or indorsement." The calendar prints the code numbers in quotation marks,
as the Letter-Book does: "870" x7, "91" x3, "000", "54", and once the editor's own bracket: **"Finds the Queen of England
[\"32\"] as well resolved to entertain the matter"** -- Stevenson, who had the manuscript, identifies 32 with the Queen of
England. That is a print identification for 32 (was M on context, above); grade it C (editor's gloss) at the next key pass, not
changed in codes.tsv by this note. Other editorial brackets gloss pronouns only ("[Bowes and Davison]" on p.370, no. 387;
"[Walsingham]" after "with him" on p.371, which glosses "him", not "91"). The entry closes: "the errors in the cipher left with
him by Sir George Cary" -- no decipherment printed. Not yet read: pp.566-568 (31 Jul 1583, LOCAL-QUEUE L44 part 2).

## CSP Scotland vi pp.566-568 page read (5 Oct 2026 03:54 UTC, owner's browser, seq 610-612; LOCAL-QUEUE L44 part 2 -- L44 now done)

No. 584, Robert Bowes to [Walsingham], 31 Jul 1583, Cott. Calig. C. VII fol.200, St Johnstone, "3½ pp. No flyleaf or address".
The calendar does **not** decipher the sign cipher: every enciphered name is printed as a blank dash with the footnote
"* In cipher" ("This day ——* and \"223\" have given him understanding"; "all that has been done by ——* late submission at
——* shall nothing avail him"; "50,000 ——* sent to \"000\""; postscript "Albeit that ——* at his departure"). The numeric codes
stay as numbers: "223" (x3, with Ruthven and "the King's remission for his fault at Ruthven" nearby, consistent with 223 =
Gowrie), "54" and "85" ("an especial favour and good liking of \"54,\" and chiefly of \"85,\""), "000". So Stevenson printed
only what was in clear or numeric; the sign-cipher stretches are blanks. Result for this target: no printed decipherment of
the Cotton cipher signs in either CSP entry (389, 584); the CSP gives the clear context around each blank (useful as cribs:
the blanks' positions are now known in the calendar's paraphrase). 85 is still unread. Screenshots private (csp-vi/).

## Lead: an 18th-century key to Walsingham's cipher in the Hamilton papers (5 Oct 2026 04:03 UTC)

HMC Supplementary Report on the Hamilton MSS (1932), introduction p.n11 (owner's search-inside of archive.org
supplementaryrep0000grea): James MacKenzie, inventorying the Hamilton Palace Charter House (note of 1762), reports "searching
out the keys to Ralph Sadler's cipher and making a key to Sir Francis Walsingham's" while reading "the twelve volumes of State
Papers on the affairs of England and Scotland in the reigns of King James V and his daughter Queen Mary". Whether that key
covers the Bowes/Cary system of 1583 is unknown; it would be a reconstruction (MacKenzie's own), not a period key. Next: NRS
catalogue search of GD406 for MacKenzie / Walsingham / key / cipher (~$1, a worker); not yet done.

## RUN6-BOWESNRS (5 Oct 2026)
Status unchanged (lead only; nothing read). Searched 5 Oct 2026 04:45-04:47 UTC by `date -u`; requests: catalogue.nrscotland.gov.uk 2 (GET `/` and `/nrsonlinecatalogue/`, browser-neutral descriptive UA), web.archive.org 3.
- NRS: both URLs HTTP 403 with the Cloudflare "Just a moment..." interstitial. Not retried (good-citizen rule). No GD406 search was run.
- Wayback CDX (`web.archive.org/cdx/search/cdx?url=catalogue.nrscotland.gov.uk`) and a `web/2024if_/` fetch: connection reset by the agent proxy (ws_closed_mid_exchange) on 3 of 3 tries, one after a 20 s pause. Even if reachable, an archived copy would not hold a dynamic GD406 search result.
- Route: LOCAL-QUEUE.tsv row L56 (catalogue-lookup, owner's-browser runner) with the six terms and the HMC lead. No ASKS row (the runner queue is the route).
- Not found / not tested: no GD406 record for MacKenzie, Walsingham, key, cipher, cypher or Sadler was seen, because no catalogue page was readable. This is a non-test, not a negative.
- Next: L56 answer; if a record names a key, then check-solved Premise step for the Hamilton key before any use on the 1583 Bowes cipher.
