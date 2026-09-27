partial

INTAKE-4715-F61, 27 Sept 2026: solver-ready intake (Layout, no cryptanalysis, no new reading, no class). Built
from KEY-ADJACENT.tsv row 21 (rank 7) and two local mirrors, `sources/cryptiana/web/bnf4715.htm` (item
id=no38) and `sources/cryptiana/web/mayenne.htm`, both read in full this job (cp932-decoded per the file's own
declared charset, not re-fetched). Neighbour folder to `ciphers/fr4715-montholon-1589` (same shelfmark, BnF
fr.4715, ark btv1b52509819x; a **different, unrelated cipher family** -- Mayenne's polyphonic substitution vs.
the Vieuville-Nevers digit cipher -- so it is a separate folder, not a pool row). `ciphers/fr4715-montholon-1589`
and its POOL.md are the SOLVE parent's (parent 7n); this folder is not, and is read-only for that account's own
Vieuville-Nevers work and vice versa.

# BnF fr.4715 no.38 (f.61), "Duke of Mayenne's polyphonic cipher?"

Sender, recipient and date are **not given** by either Tomokiyo page for this specific item (unlike the
Vieuville-Nevers letters in the same volume, which nevers.htm dates and attributes item by item). The cipher
itself is attested in use 1592-93 by Charles de Lorraine, Duke of Mayenne (head of the Catholic League) and
his circle (commander de Diou, ambassador in Rome for the League, and others), per `mayenne.htm`'s own list of
letters in this cipher (BnF fr.3982 ff.97/101/124; BnF fr.3983 ff.106/108v/211) -- f.61 of fr.4715 is the only
item in *this* volume Tomokiyo assigns to this cipher family, distinct from the Vieuville-Nevers-cipher group
that fills most of the rest of the volume.

## Tomokiyo, verbatim

`bnf4715.htm`, table of contents line for this item:

> "no.38 (f.61)...Duke of Mayenne's polyphonic cipher? (**Solution Incomplete**)"

`bnf4715.htm#no38`, the item's own section, in full:

> "There are only 21 kinds of symbols and it is unlikely that homophones are used. Still, despite some
> seemingly viable repetitive patterns, an assumption of simple monoalphabetic substitution led nowhere."
>
> "Some symbols look like ones in the polyphonic cipher of the Duke of Mayenne (see [polyphonic.htm]). In
> particular, the succession of three instances of the clover-like symbol on the 8th line is a hallmark of
> this cipher. When unknown symbols are discarded as nulls, some words can be found. A phrase like 'jalousie
> au beau-pere' is hardly expected to occur by coincidence."

`mayenne.htm`'s own mention of this item (in its "Despatches in Cipher" list, after listing the fr.3982/3983
letters):

> "**BnF fr.4715** -- Undeciphered ciphertext on f.61 appears to be in this cipher. See [bnf4715.htm#no38]."

`mayenne.htm` does **not** print a reading of f.61 itself; it only cross-links to `bnf4715.htm#no38` (above)
for that. What `mayenne.htm` prints instead is the reconstructed cipher table itself (`mayenne.png`, the key
of record below) and, separately, a specimen of the cipher's use taken from a sibling letter (f.108 of BnF
fr.3983, `mayenne2.png` -- ciphertext only, no interlinear plaintext shown alongside in that specimen image).

## What Tomokiyo already reads (an existing partial decode, not a full reading -- see gate verdict below)

Tomokiyo's own published image of this leaf, `BnFfr4715f61.png` (fetched this job, see
`sources/cryptiana/web/manifest_2026-09-27-4715f61.tsv`; identical manuscript content to the Gallica fetch
below, confirmed by direct comparison), is not a plain scan: it carries his own interlinear markup over five
short spans of the cipher, spelling out (with dashes marking the underlying cipher-symbol boundaries):

- "avec" (over the first line, right side)
- "estca-p-able" (est capable)
- "trop--avance-es" (trop avancees)
- "jal-ous-i-e-au-beau---pere" (jalousie au beau-pere -- the phrase his own prose quotes above)
- "mel'ente-noit" (reading uncertain; possibly "m'entend" or similar, near the end of the letter)

The image is captioned, in his own hand, **"Solved with Polyphonic Cipher?"** -- his own question mark,
matching the TOC's "(Solution Incomplete)". This is a handful of isolated words and one distinctive phrase
recovered from a page of continuous cipher text (the rest of the leaf -- most of eleven lines -- carries no
markup at all), explicitly self-flagged as uncertain/incomplete by its own author. It is **not** a reading of
the letter, and grades no higher than M (rule 4: a cryptanalytic result, not from a key source or known
plaintext, and explicitly marked tentative by the person who produced it) if it is ever cited.

## Gate verdict (Job 0, this job)

**Not found-solved. Not non-cipher. Partially read (an existing published crib), most of the leaf unread --
continues to intake.** The brief's own three-way gate (a full reading exists -> found-solved; the pool says
non-cipher -> retired; unread ciphertext -> continue) does not have a clean bucket for "partially read, self-
described as incomplete" -- treated here the same way `ciphers/fr4715-montholon-1589/POOL.md` treats its own
no.27/no.58 rows ("partial (existing folder's crib)"): an existing partial crib is valuable material for a
future worker, not a reason to retire the row, and not the same thing as a full reading already sitting in
print (contrast `ciphers/colbert108-nucheze-1662`, INTAKE-MC108, 27 Sept 2026, found-solved because
Tomokiyo's page prints a full plaintext reading of that target). Precedent for treating a partial gloss this
way without retiring the row: `QUEUE.md` "INTAKE-SAVOY unit A gate", 27 Sept 2026 (`savoy.htm`, KEY-ADJACENT.tsv
row 23) reached the same "partly read, not found-solved" verdict on a different item in this same intake
sweep.

- **(a) bnf4715.htm#no38**: quoted in full above. Prints a partial decode (one phrase, several isolated
  words), explicitly labelled incomplete. No BnF catalogue line is quoted on this page for this item (unlike
  `nevers.htm`'s per-item quotes, which `ciphers/fr4715-montholon-1589/POOL.md` sourced separately from the
  BnF's own dépouillement, ark:/12148/cc577658, via a cached copy in `dbourdeau/cyphersolver`'s repository
  history) -- **not checked this job**: fetching that notice was out of this job's allowed network (cryptiana.
  web.fc2.com only; GitHub was not in scope). A worker with GitHub access could re-check the same cached
  notice POOL.md used for item 38's own line before any deep-work brief.
- **(b) POOL.md's table** (`ciphers/fr4715-montholon-1589/POOL.md`, read in full this job): does not list
  no.38/f.61 at all -- correctly, since that table covers only the "Vieuville-Nevers Cipher" group (nos.
  3,6,10,12,21,27,28,35,37,39,41,42,44,47,48,50,52,54,55,57,58,60) and no.38 is a different cipher family
  (Mayenne's polyphonic substitution), outside that pool's scope.
- **(c) mayenne.htm**: does not print a reading of f.61 itself (see quote above); only the reconstructed
  cipher table and a ciphertext-only specimen from a sibling letter.

No vision subagent call was needed for the gate itself -- the page text alone (both htm files) settles it, the
same way INTAKE-MC108 settled its own gate from text plus one direct (non-subagent) look at an image.

## The leaf (BnF fr.4715 f.61r; f.61v blank)

Gallica ark `btv1b52509819x`, canvas f137 labelled '61r' (per `tools/gallica_folio.py`'s own manifest-label
lookup, not a formula -- this ark's offset is INCONSISTENT across its own run, see `images/manifest.json`).
One page of continuous hand-drawn cipher symbols, about eleven lines, no interlinear gloss on the manuscript
itself beyond Tomokiyo's own five short markups (reproduced above from his published image, not the raw
scan). A second, larger ink foliation ("66", in a ruled box) is visible on the same leaf alongside the small
number both the Gallica label and Tomokiyo's own citation use ("61") -- flagged in `images/manifest.json`, not
resolved; a future worker should check which numbering the volume's own finding aid uses before citing a folio
number outward.

## The key (key of record)

`keys/key_mayenne_1592.tsv`, transcribed from the reconstructed-cipher-table image `mayenne.png` (embedded in
`mayenne.htm`, fetched this job). See that file's own header for the transcription method (two independent
blind Sonnet subagent reads, disagreements settled by this worker) and the AB/M/? grade counts.

Design, per Tomokiyo's own prose (`mayenne.htm`): a **polyphonic** substitution -- the table pairs two
plaintext letters per column (a/n, b/o, c/p, ... per the table's own two stacked letter rows) and at least one
pair of high-frequency letters ("e" and "r") is stated to share the identical cipher symbol; separately, a/n,
c/p and d/q are described as having *visually similar but not necessarily identical* hand-drawn symbols,
"caus[ing] confusion" -- the table image itself is the only place this distinction can be settled column by
column, hence the careful shape-only transcription in `keys/key_mayenne_1592.tsv` (not a "these two letters
share a symbol" shortcut). Three word-code entries (que, qui, pour) are also on the table, each with a single
symbol. 21 kinds of symbols total per Tomokiyo's own count (`bnf4715.htm#no38`) is the expected total across
both letter rows plus the three word codes; `tools/key_design.py`'s own `sign_inventory`/`n_codes` count is
the mechanical cross-check once the key file is registered.

## Check-solved header (not a formal `.claude/briefs/check-solved.md` pass -- see "What remains")

- Tomokiyo's own two pages (`bnf4715.htm#no38`, `mayenne.htm`) both read and quoted in full above; neither
  prints a full reading, both flag the item as incomplete/partial.
- `ciphers/fr4715-montholon-1589/POOL.md` (CS-4715-POOL, 27 Sept 2026, a six-source check-solved-shaped sweep
  of the same volume) does not cover this item -- different cipher family, out of that sweep's scope.
- `KEY-ADJACENT.tsv` row 21's own `in_repo` cell already records a solver-repository grep (SCOUT-OWN-8, 27
  Sept 2026): "none in dbourdeau/cyphersolver or aaymeloglu/unsolved-ciphers" for this item -- not re-run this
  job (out of this job's allowed network scope; GitHub was not on the allowed-hosts list).
- `CATALOG.md` and `LESSONS-LASRY.md` grepped this job (offline, already on disk): no row for fr.4715 no.38 or
  f.61 in either. `LESSONS-LASRY.md` does name an unrelated target, `matignon-mayenne-1586` -- a **different**
  shelfmark and a different Mayenne-cipher letter entirely, sharing only the name "Mayenne"; not to be
  confused with this folder (the same caution the fr3251 folders give for Ceppo-Nevers vs. Nevers-Birago).
- `sources/decode/records-non-decrypted-2026-09-24.tsv` and `records-decrypted-2026-09-24.tsv` (the cached 24
  Sept 2026 DECODE crawl) grepped this job for "mayenne" and "4715": no hit.
- No full-text/phrase search run this job (out of scope for an intake job per the 3251/mc108 pattern; a
  phrase search on "jalousie au beau-pere" once a fuller reading exists is the kind of check rule 10 and
  `tools/print_check.py` are for, not this job).

What remains before any class (rule 10) or any deep-work brief:
- The BnF's own dépouillement entry for item 38 (not checked this job, see gate (a) above).
- A formal `.claude/briefs/check-solved.md` pass proper; `tools/intake_gate_check.py fr4715-f61-mayenne-1592`
  should be run before any deep-work brief (this job runs it once below).
- The competing "61"/"66" foliation (above) checked against the volume's finding aid.
- Once any reading exists: `tools/print_check.py` on the decoded phrases (rule 10), and a check of whether
  Tomokiyo's own "jalousie au beau-pere" phrase is independently findable in print (it would not be novel to
  us either way, but is worth logging per rule 10's search-result standard).

**Next step:** calibrate `keys/key_mayenne_1592.tsv` against the known cipher-symbol/plaintext-word pairings
Tomokiyo's own interlinear markup already gives on this same leaf (five spans, "What Tomokiyo already reads"
above -- a small but genuine known-answer set, the same "known answer first" discipline as
`.claude/briefs/README.md`'s common tail), before any blind transcription of the rest of the leaf; then two
blind passes on the remaining unmarked lines and a 20-shuffled-key control (rule 3); reading to a verifier.
The sibling letters `mayenne.htm` lists in BnF fr.3982/fr.3983 (ff.97, 101, 106, 108v, 124, 211) are a possible
further calibration source if any of them turn out to carry their own period or Tomokiyo decipherment --
not checked this job (out of scope: this job's allowed network was cryptiana.web.fc2.com only, and none of
those folios' own pages were named in this job's reading list).

**Requests:** cryptiana.web.fc2.com 2 this job (`BnFfr4715f61.png`, `mayenne.png`; both files already on disk
from a prior fetch for `bnf4715.htm`/`mayenne.htm` themselves, no re-fetch needed for those two htm files).
gallica.bnf.fr 2 (canvas f137 and f138 at 1000px, 2s apart; `tools/gallica_folio.py`'s own folio lookup used
the already-cached manifest, 0 further requests). No other hosts. No credentials. No AskUserQuestion. No
novelty/first/unpublished wording (rule 10) -- Tomokiyo's own partial decode is credited to him throughout,
not claimed as ours.

## F61-CAL (27 Sept 2026)

Per `.claude/briefs/runs/2026-09-27-parent-ytbiz-f61-cal.md` (parent worker F61-CAL, Opus). Box started 19:56 UTC
(clock read). Intake gate re-run: `fr4715-f61-mayenne-1592: partial (line 1) -- edition/page or full-text-search
citation found within 6 lines`, exit 0.

**Pre-registered gate (written before the reading call).** Statistic: token-level match between our decode of the five
marked spans and Tomokiyo's readings of them (`scripts/tomokiyo_spans.tsv`, his markup as the reference, grade H for this
test, not the manuscript). Decode = the reader's per-sign label (a key-inventory symbol S01-S16 or `?`) mapped through
`keys/key_mayenne_1592.tsv` to its value set (the a/n and e/r columns carry one value per symbol; the nine shared columns
two; que/qui/pour a word). A position matches if any value in the set is the letter Tomokiyo reads there (a word code
matches if it equals his letters at that point). Each span's markup (one character per sign, dashes as wildcards) is
aligned to the reader's full sign sequence for that line by one fixed local DP (match +1, mismatch 0, gap -1), the same
alignment for target and controls. Gate: **pooled match >= 0.85** over the 45 letters of the five spans, AND above the
maximum of **20 controls** in which the key's value sets are shuffled across its 16 symbols (seed 1; same coverage by
construction, so coverage is not the statistic). Ambiguity rate (share of decoded sign tokens with more than one value) is
reported beside it, non-gating. Diagnostic for outcomes (b)/(c), also fixed now: for every reader label, the letters
Tomokiyo reads under it are tabulated; a label that consistently takes one letter pair that differs from the key's cell
points at the key transcription (b); a label that takes scattered letters points at the reader (c).
