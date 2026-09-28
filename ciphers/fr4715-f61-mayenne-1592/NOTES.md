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
alignment for target and controls. Gate: **pooled match >= 0.85** over the 55 letters of the five spans (4+10+12+7+11+11; S4 counted as its two lines), AND above the
maximum of **20 controls** in which the key's value sets are shuffled across its 16 symbols (seed 1; same coverage by
construction, so coverage is not the statistic). Ambiguity rate (share of decoded sign tokens with more than one value) is
reported beside it, non-gating. Diagnostic for outcomes (b)/(c), also fixed now: for every reader label, the letters
Tomokiyo reads under it are tabulated; a label that consistently takes one letter pair that differs from the key's cell
points at the key transcription (b); a label that takes scattered letters points at the reader (c).

**U1, sheets (1 Gallica request).** `sh images/regen_f61r_sheets.sh` runs
`python3 tools/iiif_lines.py --image images/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg --out images --prefix f61s --max-width 900 --follow-slope 300 --slope-local --debug`
on the native region 500,1880,3320,1420 of canvas f137. That region was fetched once with the brief's own
`--ark btv1b52509819x --canvas 137` form. A second request for a region 60 px taller got a connection reset. It was
not retried, and the script reads the cached region instead. The tool finds 11 lines, pitch 125 px, slopes -0.008 to
+0.010, and the overlay puts every band on its line. The last line's descenders sit at the bottom edge but are
readable. Then the script applies 3x LANCZOS and builds one stacked sheet per span line, holding only the segments
that carry cipher: `images/f61sheet_L01.jpg` (s4-5), `L03` (s1-3), `L05` (s2-4), `L07` (s3-5), `L08` (s1-2), `L11`
(s1-2). Each sheet is 2700 px wide. The reader was also given `images/key_inventory_sheet.png`: the 16 drawings of
`mayenne.png`, 4x, labelled S01-S16 with no values (the label-to-cell map is `scripts/inventory_values.json`). The
page is plain French prose with short cipher runs inside it. The five spans sit on L01, L03, L05, L07+L08 and L11.
Unmarked runs on L02, L04 and L10 were not read. images/ is 2.6 MB. The 55 raw crops are regenerable and not
committed.

**U2, one reading call (call A, Opus, about 109k subagent tokens, 80 s).** Output: `scripts/read_call_A.tsv`, 82
signs. 36 were labelled `?` ("matches no inventory symbol") and most other labels were at confidence l or m. The
reader said the manuscript sheets were "very legible" and the reference drawings "tiny and blurry". No second call
was made, although `?` is above a tenth. The `?`s are not undecided signs: each f.61 shape class got one label every
time it appeared (every loop-on-stem was S03, every 43-shape `?`). A second blind pass against the same 25-px
drawings would repeat the same class-level mapping, and the diagnostic below places the fault there.

**U3, score (`python3 scripts/f61cal.py`, result in `scripts/f61cal_result.txt`, `--check` for staleness).**

| span | line | matched / letters |
|---|---|---|
| S1 avec | L01 | 1/4 |
| S2 est capable | L03 | 2/10 |
| S3 trop avancees | L05 | 1/12 |
| S4a jalousi- | L07 | 1/7 |
| S4b -e au beau-pere | L08 | 2/11 |
| S5 mel'ente noit | L11 | 1/11 |
| **pooled** | | **8/55 = 0.145** (gate 0.85) |
| 20 shuffled-key controls, seed 1 | | mean 0.114, **max 0.309** |
| coverage (non-gating) | | 46/82 signs carry a key symbol |
| ambiguity (non-gating) | | 32/46 = 0.696 of the covered signs have more than one value (0.390 of all signs) |

Sensitivity check: Tomokiyo's image has two dashes after "p" in S2 (`estca-p--able`), where the pre-registered
reference, copied from INTAKE's text, has one. With two dashes the pool reads 7/55 = 0.127 against the same control
max of 0.309. The gate was decided on the pre-registered file.

**Diagnostic (pre-registered shape; `scripts/class_diag.tsv`, non-gating).** The DP's own diagnostic is weak, because
the alignment is driven by a key that mostly misses. So the worker placed Tomokiyo's letters over the reader's own
shape classes by the x-position of his markup in `BnFfr4715f61.png`. This was one look by eye, not a blind pass. On
that placement Tomokiyo's letters are consistent within each f.61 class:
- loop on stem: e/r, 14 times
- 43-shape: a/n, 10
- double-dagger: c/p, 6
- infinity on a bar: u/v, 5
- double loop: b/o, 5
- bracket: l, 3
- hook over two stems: i/j, 3
- beta: m, 1
- V with bar: s/t, 7
- the 6-shape, a-shape, ll, plus, plain 4 and loop-with-bar: dashes (nulls) only.

For 48 of the 55 letters the class falls in a single cell of the Mayenne table's own pairing. The exception is 7
letters: one class (V) takes both s and t, which the table puts in two columns, f/s and g/t. Against that, the
reader's class-to-drawing labels are right for only two classes: the double-dagger (S04) and the beta (S13).
- loop on stem: labelled S03, the b/o knot. Tomokiyo's cell is e/r, S06/S07.
- 43-shape: labelled `?`. The cell is S01/S02.
- infinity: labelled S11, i/x. The cell is h/u, S10.
- double loop: labelled `?`. The cell is S03.
- bracket: labelled S08, f/s. The cell is S12, l/y. In the table the two drawings are near-identical.
- V: labelled S14, que.

**Outcome (c).** The gate is missed because the reader disagrees with the symbol identities Tomokiyo's markup
implies. The failure is in matching f.61's hand to `mayenne.png`'s drawings, which were taken from other letters in
other hands and are about 25 px each. It is not in reading the manuscript: every class was read consistently and the
reader called the leaf very legible. Neither of the brief's two remedies fits this failure:
- A second blind pass against the same drawings (about one more Opus call, same size as call A) would test reader
  noise, which is not what failed.
- A native BnF capture would change the manuscript side, which was already legible.
The key's value pairing (a/n, c/p, e/r, b/o, l/y, h/u, i/x, m/z) is consistent with 48/55 of Tomokiyo's letters.
The one departure, V taking s and t, is logged as a data conflict, not settled.

Route logged: **untested-by-this-tool** (blind drawing-matching against the table image), not a negative on the key.

**Next step (suggested, not run).** F61-CRIB: take the f.61 shape classes from a blind pass that uses the manuscript's
own classes, not the table's drawings. Map classes to table cells from Tomokiyo's five spans, which grade M (his own
"?"). Pre-register a leave-one-span-out check against 20 shuffled mappings before applying the mapping to the
unmarked runs on L02, L04, L08's tail and L10. Those runs are short (about 20-25 signs), so the result would be a
cryptanalytic reading of a few words at most, graded S/M. The V s/t conflict and the six null classes stay open. The
sibling letters in fr.3982/3983 remain the other calibration source (INTAKE's note).

Requests this job: gallica.bnf.fr 2 (1 served, 1 connection reset, no retry). 1 subagent reading call. No
credentials, no AskUserQuestion, no novelty wording.

## Campaign step H1 (2026-09-27 21:50 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i), one step per `.claude/briefs/campaign.md`, script-only, no
subagent or vision call, no network. Hypothesis H1 (F61-CRIB) from CAMPAIGN.md: a class-to-letter map built from the
reader's own shape notes, leave-one-span-out against Tomokiyo's five spans, 20 shuffled class-maps.

**Method (`scripts/f61crib.py`; `--check` for staleness, rule 7).** Every sign in `scripts/read_call_A.tsv` is put in a
shape class by 20 string rules on its `marks` text alone (the S0x labels F61-CAL found wrong are never read): 19
classes over the 82 signs (PHI 15, C43 9, CA 9, VBAR 8, C6 6, 4TRI 6, INF 5, DBL 4, LOOPBAR/EBR/ZHOOK 3, CROSS/ELOOP/4PI
2, HASH4/LOOPSTEM1/CH/LL/4STEM 1). Rule choices made before scoring: all V-shapes are one class (the reader's one
"V/triangle" without "bar" is taken as an elision); the reader's lone "loop on long stem" (L05/1) is kept apart from
the "phi" class since the reader did not call it phi. The map is fitted with the shared
`tools/interlinear_align.py align --code-prefix @` (CLAUDE.md Usage item 8: the alignment tool, not a private DP):
each class is a code taking 0 or 1 letters of the markup with Tomokiyo's dashes deleted, hard-EM, 6 iterations. A
class's value set is its top-2 letters by count (the Mayenne table pairs two letters per symbol). The withheld span is
scored with F61-CAL's own DP (`align()` copied unchanged from `scripts/f61cal.py`), S4a+S4b as one span (L07+L08).
Controls: for each fold the fitted sets are permuted across classes 20 times (seed 1) and pooled the same way.

**Result (`scripts/f61crib_result.txt`).**

| held-out span | matched / letters | shuffled max (mean) |
|---|---|---|
| S1 avec (L01) | 2/4 | 3/4 (1.90) |
| S2 est capable (L03) | 5/10 | 5/10 (3.20) |
| S3 trop avancees (L05) | 6/12 | 6/12 (3.40) |
| S4 jalousie au beau-pere (L07+L08) | 7/18 | 8/18 (5.65) |
| S5 mel'ente noit (L11) | 4/11 | 4/11 (2.60) |
| **pooled held-out** | **24/55 = 0.436** | controls mean 0.305, **max 0.345** |
| sensitivity, uncapped value sets (non-gating) | 28/55 = 0.509 | |

H1's gate (pooled above every one of the 20 shuffled-map values): **met**, 0.436 vs 0.345. F61-CAL's own absolute level
(0.85) is not approached, and F61-CAL's 8/55 = 0.145 with the table-drawing labels is tripled by the same reader's
shape notes alone. No single fold beats its own shuffled max; only the pool does.

**What the result does and does not say.** The reader's shape classes carry the signal Tomokiyo's markup implies (the
pool beats the shuffle), but the fitted maps disagree between folds: PHI reads e/l, e/c, e/c across folds; 4TRI p/a, p/n,
a/n; C43 a/b, e/b; VBAR t/s, t/n, n/t, e/n, s/u. The map fitted on all five spans (`scripts/f61crib_map.tsv`) puts
Tomokiyo's letters onto the six classes he leaves as dashes (C6 a:4, CA u:2, LL/HASH4/4STEM e), because
`interlinear_align.py`'s DP, tuned for Thurloe's lines, charges -3.0 for a code that takes no letter and the dashes
were deleted before alignment. F61-CAL's eye-placed diagnostic (`scripts/class_diag.tsv`, not blind) had these same
classes clean (PHI e:12 r:2, C43 a:8 n:2, 4TRI c:3 p:3). So the limit here is the fitting instrument, not the classes:
H11 (CAMPAIGN.md) adds a null-aware option to the shared tool and keeps the dashes as explicit unread positions, and
asks for fold-stable sets before H4-H6 apply any map to the unmarked runs. Not a reading; no class change; grade of
the 55 reference letters stays H-for-this-test only (Tomokiyo's own "Solution Incomplete" markup, rule 4).

Files: `scripts/f61crib.py`, `scripts/f61crib_result.txt`, `scripts/f61crib_map.tsv`; HYPOTHESES.md row added. Requests:
none. No credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H11 (2026-09-27 22:50 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i), script-only, no subagent or vision call, no network. Hypothesis
H11 (F61-CRIB2): H1's class map refitted with a null-aware alignment, dashes kept.

**Tool change (CLAUDE.md Usage item 8: an option on the shared tool, not a private copy).** `tools/interlinear_align.py`
gained `--null-cost X` (the charge for a code that takes no plain letter; the Thurloe default -3.0 stays the default) and
`--wildcard C` (a plain-line character kept as an explicit "sign here, unread" position: a code may take it at score 0,
it never counts as evidence and never joins a longer chunk). `tools/tests/test_interlinear_align.py` has a new case: a
three-line markup with dashed nulls, where the new options recover the three letter codes at agreement 3/3 and leave
the null code without a meaning row, and the Thurloe default does not; the existing cases still pass.
`tools/system_map_check.py` ok.

**Method (`scripts/f61crib2.py`, importing `scripts/f61crib.py`'s classes, folds, DP and controls; `--check`).** Same 19
classes, same leave-one-span-out, same scoring DP, same 20 shuffled class-maps (seed 1). The fit passes the markup with
its dashes to the tool with `--code-prefix @ --wildcard - --null-cost -1` (pre-registered main run); sensitivity at
null-cost 0 and -3, non-gating. Gate, two parts: (a) pooled held-out above every shuffled value; (b) the top-2 sets of
PHI, C43, 4TRI, VBAR, DBL and INF identical in all five folds. One implementation fix before the result was written:
the stability check first compared value sets as count-ordered strings ("cp" vs "pc"); corrected to compare as sets.
Both versions fail (b).

**Result (`scripts/f61crib2_result.txt`).**

| held-out span | matched / letters | shuffled max (mean) | fitted set for PHI, C43, 4TRI, VBAR, DBL, INF |
|---|---|---|---|
| S1 avec (L01) | 3/4 | 2/4 (1.60) | er, an, pc, ts, ob, u |
| S2 est capable (L03) | 9/10 | 6/10 (2.85) | er, an, pc, ts, ob, u |
| S3 trop avancees (L05) | 8/12 | 6/12 (3.15) | eo, ab, pc, ts, bl, u |
| S4 jalousie au beau-pere (L07+L08) | 9/18 | 10/18 (5.35) | e, na, co, ts, lo, a |
| S5 mel'ente noit (L11) | 7/11 | 5/11 (2.60) | eo, ab, cp, st, bl, u |
| **pooled held-out** | **36/55 = 0.655** | controls mean 0.283, **max 0.400** | |
| sensitivity null-cost 0 / -3 | 33/55 / 36/55 | max 0.309 / 0.400 | |

Gate (a) **met** (0.655 above every one of the 20 pooled shuffles; H1 was 0.436 vs 0.345). Gate (b) **not met**: the
top letter is fold-stable (PHI e, C43 a, VBAR s/t, 4TRI c, INF u except the S4 fold) but the pair's second letter
(r, n, p, b) rests on one or two of the 55 letters and drops out of the top-2 when its span is withheld. **H11 FAIL on
its own gate.** Not a reading; no class change.

**What moved.** The all-span map (`scripts/f61crib2_map.tsv`, grade M, from Tomokiyo's own "Solution Incomplete" markup)
now reads PHI e/r (e:10 r:2), C43 a/n, VBAR t/s, 4TRI p/c, INF u (5/5), DBL o/b, EBR l, ZHOOK i/j, with CROSS, ELOOP,
LOOPSTEM1, CH, LL and 4STEM as nulls -- the same cells F61-CAL's eye-placed `scripts/class_diag.tsv` gave for 8 of its 10
letter classes, reached here by the tool blind. The two departures are C6 (a:2) and CA (a:1 m:1), which the eye placement
had as nulls; and the V s/t conflict stands (one class, two table columns). The 0.85 level is not reached (0.655): the
S4 fold is the weak one (9/18, below its shuffled max 10/18), which is the span with most polyphonic partner letters
(j, b, p, r) and the one line pair cut across a sheet edge (L08/14 partial).

**Next (H12, CAMPAIGN.md).** The free-letter fit asks 55 letters to supply both members of each pair; the Mayenne table
already pairs them. H12 fits each class to a table cell (top-1 cell by count) and scores the withheld span with the
cell's pair, controls permuting cells across classes, stability required on the cell only. Files: `scripts/f61crib2.py`,
`scripts/f61crib2_result.txt`, `scripts/f61crib2_map.tsv`, `scripts/f61crib.py` (import guard added, `--check` still
fresh), `tools/interlinear_align.py`, `tools/tests/test_interlinear_align.py`; HYPOTHESES.md row added. Requests: none.
No credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H12 (2026-09-27 22:53 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i), script-only, no subagent or vision call, no network. Hypothesis
H12 (F61-CRIB3): the class map fitted through the Mayenne table's own pairing.

**Method (`scripts/f61crib3.py`, importing `scripts/f61crib.py`; `--check`).** Same 19 classes, folds, scoring DP and
H11's null-aware alignment (`--wildcard - --null-cost -1`). A class takes ONE table cell of `keys/key_mayenne_1592.tsv`
(a/n, b/o, c/p, d/q, e/r, f/s, g/t, h/u, i/x, l/y, m/z), the cell whose two letters its aligned markup letters fall in
most often (ties broken alphabetically and reported); no aligned letter means null. The withheld span is scored with
the cell's pair, so the pair's partner letter comes from the key, not from 1-2 occurrences. Controls: 20 maps per fold
with the fitted cells permuted across classes (seed 1). Gate: (a) pooled above every control AND (b) the cell of PHI,
C43, 4TRI, VBAR, DBL, INF identical in all five folds. The V s/t conflict is reported per fold.

**Result (`scripts/f61crib3_result.txt`).**

| held-out span | matched / letters | control max (mean) | VBAR cell counts (f/s : g/t) |
|---|---|---|---|
| S1 avec (L01) | 3/4 | 2/4 (1.50) | 3 : 4 |
| S2 est capable (L03) | 8/10 | 5/10 (2.85) | 2 : 3 |
| S3 trop avancees (L05) | 10/12 | 8/12 (3.60) | 2 : 3 |
| S4 jalousie au beau-pere (L07+L08) | 10/18 | 9/18 (5.80) | 2 : 4 |
| S5 mel'ente noit (L11) | 6/11 | 6/11 (3.40) | 3 : 1 |
| **pooled held-out** | **37/55 = 0.673** | controls mean 0.312, **max 0.436** | |
| sensitivity, v->u and j->i folded (non-gating) | 40/55 = 0.727 | max 0.455 | |
| all-span map, in-sample (non-gating) | 46/55 | | misses s@VBAR 3, v@INF 2, j@ZHOOK 1, o@PHI 1, m@CA 1 |

Gate (a) **met**. Gate (b) **not met** on two of the six classes: VBAR reads g/t in four folds and f/s when S5 is held
out (the pre-identified conflict: one f.61 shape class under both s and t, 4:3 overall); INF reads h/u in four folds
and a/n when S4 is held out (4 of INF's 5 signs are in S4, so that fold trains on 1-2 letters and ties). PHI e/r, C43
a/n, 4TRI c/p and DBL b/o are the same cell in all five folds. **H12 FAIL on its own gate**, as pre-registered. Not a
reading; no class change. The v/j sensitivity was added after the gated run was read (the key has no v and no j, u=v
and i=j in the period hand, `scripts/class_diag.tsv` already noted u=v; CLAUDE.md rule 3's one-convention lesson): it
lifts the pool to 40/55 and the in-sample map to 49/55, and does not change either gate verdict.

**What this leaves.** The letter-class map is now stable at the cell level for every class with enough occurrences
(`scripts/f61crib3_map.tsv`: PHI e/r 12:1, C43 a/n 6:1, 4TRI c/p 5:0, INF h/u 5:0, DBL b/o 3:1, EBR l/y 2:1, ZHOOK
i/x 2:0; CROSS, ELOOP, LOOPSTEM1, CH, LL, 4STEM null; C6, CA, LOOPBAR, 4PI, HASH4 on 1-2 letters each, unsettled) and
the one open question is VBAR: one glyph with a data conflict, or two glyphs (the table's f/s bracket and g/t T-shape)
the reader merged. H13 (CAMPAIGN.md) tests that with one blind vision sort of the 8 VBAR crops against a permutation
control. Files: `scripts/f61crib3.py`, `scripts/f61crib3_result.txt`, `scripts/f61crib3_map.tsv`; HYPOTHESES.md row
added. Requests: none. No credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H13 (2026-09-27 22:57 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i). One Opus vision subagent call (the step's one allowed; about
100k subagent tokens, 57 s), no network. Hypothesis H13 (F61-VBAR): is the reader's one "V with bar" class two glyphs?

**Design, pre-registered (`scripts/f61vbar.py`, committed a94e9ff0 before the call's output was read).** The subagent was
given the six `images/f61sheet_L*.jpg` sheets and asked to list every cipher sign "whose main body is a V or a triangle
combined with a horizontal bar", with fixed shape attributes (bar position, bar length, closed/open, point, weight,
extra element), sorted into 2-3 groups by shape with a one-sentence criterion. No letters, no key, no table, no expected
count. Pairing rule 1: per sheet, the call's signs in order are paired with `read_call_A.tsv`'s VBAR positions in order
(L01/10, L03/5, L03/6, L05/3, L05/18, L07/9, L11/6, L11/12); a sheet whose count differs is dropped. Labels: the markup
letter at each position under H12's alignment (s at L03/5, L05/18, L07/9; t at L03/6, L05/3, L11/6, L11/12; L01/10 a
dash, never scored). Statistic: best group-to-letter match over the labelled positions. Null: all 35 arrangements of
3 s and 4 t over the 7 positions (exact) and 200 permutations (seed 1). Gate: above the permutation p95 with exact
p < 0.05. Power note, posted in ROOM before the output: at n=7 only a perfect split passes (p = 0.029); 6/7 has p = 0.14.

**Output (`scripts/read_call_V.tsv`, verbatim).** 18 signs in three groups. The call's own criterion: "A is a closed
down-pointing triangle whose only bar is its top side; B is the same triangle with a second bar across its point; C is
a smaller, partly open triangle under a bar, with a 4-shaped element and a stem above the bar." Group C (11 signs) is
the reader's separate "4 over triangle" class (4TRI, read_call_A.tsv), which the prompt's wording let the call include.

**Result (`scripts/f61vbar_result.txt`).**

| pairing rule | reconciled sheets | scored | split | exact p | permutation p95 | gate |
|---|---|---|---|---|---|---|
| 1, pre-registered (every listed sign paired in order) | 1 of 5 (L07 only) | 1 position | -- | -- | -- | **NON-TEST** |
| 2, amended after reading (rows whose own `extra` names the 4-shaped element dropped; one row the call itself flags as a possible repeat across a segment overlap dropped) | 5 of 5, all 8 VBAR positions | 7 (3 s, 4 t) | B = s 3/3, A = t 4/4, **7/7** | **0.029** | 6/7 (mean 4.70) | PASS under rule 2 |

Under the rule as pre-registered this is a non-test, because the prompt's shape wording was wider than the reader's
class. Under rule 2, which uses only the call's own shape text and its own flag (never the s/t labels), the two
remaining groups separate every s position from every t position: group B ("second bar at the point, extending left",
heavy) sits under s at L03/5, L05/18 and L07/9; group A ("top bar only") sits under t at L03/6, L05/3, L11/6 and L11/12
and under the unlabelled L01/10. So the "V s/t conflict" carried since F61-CAL is most simply a reader merge of two
glyphs, not a polyphonic cell that breaks the table's pairing -- but because rule 2 was written after the output was
read, this is reported as an amended-rule result and H14 pre-registers the confirmation (prompt fixed to the reader's
class, rule 1 as written) before the split is used anywhere. Not a reading; no class change; nothing here is said to
be solved or new.

Files: `scripts/f61vbar.py`, `scripts/read_call_V.tsv`, `scripts/f61vbar_result.txt`; HYPOTHESES.md row added.
Requests: none. Vision calls: 1 of 4. No credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H14 (2026-09-27 23:02 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i). One fresh Opus vision subagent call (about 102k subagent
tokens, 59 s), no network. Hypothesis H14 (F61-VBAR2): the pre-registered confirmation of H13's amended-rule split.

**Design, pre-registered.** `scripts/f61vbar.py --in read_call_V2.tsv` (committed d89a91ed before the call) with pairing
rule 1 as written; `scripts/f61crib4.py` (9c357a60, before the call) to re-run the H12 cell fit with VBAR split on a
rule-1 PASS only. Prompt fixed to the reader's class: closed down-pointing triangles whose top side is a bar, any sign
with a 4-shaped element or stem above the bar excluded; fixed attributes; groups by shape; no letters, no key, no
count. The prompt also said consecutive segments "may overlap slightly" -- the runner's own guess, wrong in degree (see
below).

**Output (`scripts/read_call_V2.tsv`, verbatim).** 9 signs, two groups: "group B has a second horizontal bar across the
bottom point of the triangle; group A is the plain triangle with only the top bar." Per sheet: L01 1, L03 2, L05 2,
L07 1, L08 0, L11 3 -- the reader's VBAR counts except L11, where the reader listed 2. The call judged its L11 segment-2
x70 triangle "a separate sign (not a repeat across the edge)".

**Result (`scripts/f61vbar2_result.txt`).**

| pairing rule | reconciled sheets | scored | split | exact p | gate |
|---|---|---|---|---|---|
| 1, pre-registered | 4 of 5 (L11 dropped, 3 vs 2) | 5 (3 s, 2 t) | B = s 3/3, A = t 2/2, 5/5 | 0.100 (10 arrangements) | **FAIL** |
| 3, geometric de-duplication (written after this output) | 5 of 5, all 8 positions | 7 (3 s, 4 t) | B = s 3/3, A = t 4/4, **7/7** | 0.029 | PASS under rule 3 |

**H14 FAIL as pre-registered.** At n=5 no outcome can pass (the only perfect arrangement has p = 0.10), so the
pre-registered test lost its power when L11 dropped. The cause is in the runner's pairing design, not in the signs:
`images/manifest.json`'s `iiif_lines` boxes show the sheet segments are 900 native px wide stepping 605 px, so
consecutive segments overlap by 295 native px (885 px on the 3x sheets), about a third of each segment. The call's L11
segment-1 x1856 and segment-2 x70 triangles sit at native x 619 and 628 -- one sign seen twice -- and the H13 call's L01
"same as L01 s1" pair likewise (2588 and 2600). Neither call was told the true overlap; H13's call flagged its repeat
itself, H14's did not. Rule 3 de-duplicates by the manifest geometry only (a listed sign within 40 native px of one
already listed on the same sheet is the same sign), never by the labels; under it both independent blind calls
reconcile every one of the 8 VBAR positions and put group B (second bar at the point) under s at L03/5, L05/18 and
L07/9 and group A (top bar only) under t at L03/6, L05/3, L11/6 and L11/12 -- the same assignment at every position
across the two calls. `scripts/f61crib4.py` was not run (its guard asks for a rule-1 PASS). Not a reading; no class
change; no word of solved or new.

**Consequences.** (1) H15 is the confirmation H14 was meant to be, with rule 3 on disk before the call and the prompt
stating the overlap; a third miss leaves the split "supported by two amended-rule results, unconfirmed by a
pre-registered one" and is not called a fourth time. (2) Any per-sheet sign count from these overlapping sheets can
double-count a sign in the overlap band; call A's per-line counts equal Tomokiyo's markup lengths on the three full
spans (L05 18, L08 14, L11 12), so it probably did not, but H2's second blind read is amended to sheets re-cut without
overlap. Files: `scripts/read_call_V2.tsv`, `scripts/f61vbar2_result.txt`, `scripts/f61vbar.py` (rule 3, `--in/--out`),
`scripts/f61crib4.py`; HYPOTHESES.md row added. Requests: none. Vision calls: 1 of 4. No credentials, no
AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H15 (2026-09-27 23:04 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i). One fresh Opus vision subagent call (about 102k subagent
tokens, 60 s), no network. Hypothesis H15 (F61-VBAR3): the confirmation, with both of H14's defects fixed on disk before
the call (pairing rule 3, geometric de-duplication from `images/manifest.json` boxes, in `scripts/f61vbar.py`; the guard
of `scripts/f61crib4.py` on a rule-3 PASS; commit 6a8e6e43) and the prompt stating the 885-px overlap.

**Output (`scripts/read_call_V3.tsv`, verbatim).** 8 signs, one per reader VBAR position on every sheet (the call noted
the L11 segment-1 sign reappearing at segment-2 x about 50 and did not list it again). Two groups: "group A is the
triangle closed only by its top bar, and group B has a second horizontal bar crossing the triangle's bottom point,
running mostly to the left."

**Result (`scripts/f61vbar3_result.txt`).** Scored 7 positions (3 s, 4 t): B = s at L03/5, L05/18, L07/9; A = t at
L03/6, L05/3, L11/6, L11/12; A also at the unlabelled L01/10. **7/7, exact p = 0.029** against the 35 label arrangements,
permutation p95 6/7 -- **PASS as pre-registered**, and identically under rules 1 and 2. Three independent blind calls
(H13, H14, H15) now assign the same group to every one of the 8 positions. The "V s/t conflict" carried since F61-CAL
is closed: the reader's one VBAR class was two glyphs, and the table's pairing holds for both (A = g/t, B = f/s).

**Second half (`scripts/f61crib4.py`, `f61crib4_result.txt`, `f61crib4_map.tsv`).** H12's cell fit with VBAR split into
VBAR_A (5 signs) and VBAR_B (3):

| held-out span | matched / letters | control max (mean) |
|---|---|---|
| S1 avec (L01) | 3/4 | 2/4 (1.30) |
| S2 est capable (L03) | 9/10 | 5/10 (3.00) |
| S3 trop avancees (L05) | 11/12 | 6/12 (3.15) |
| S4 jalousie au beau-pere (L07+L08) | 11/18 | 10/18 (6.50) |
| S5 mel'ente noit (L11) | 8/11 | 6/11 (3.15) |
| **pooled held-out** | **42/55 = 0.764** | controls mean 0.311, **max 0.400** |
| all-span map, in-sample (non-gating) | 49/55 | |

Gate (a) met; gate (b) met: PHI e/r, C43 a/n, 4TRI c/p, VBAR_A g/t, VBAR_B f/s, DBL b/o are the same cell in all five
folds (INF h/u in four, a/n when S4, which holds 4 of its 5 signs, is withheld -- reported, not gated). **H15b PASS.**
The remaining held-out misses are the v/j notation (the key has neither), one o under PHI, one m under CA, and the S4
fold, which is the span with the sheet-edge cut sign (L08/14). Not a reading: every one of the 55 letters is Tomokiyo's
own markup, used as the reference; the map (`scripts/f61crib4_map.tsv`, grade M) has not yet been applied to any sign
outside those spans. No class change; no word of solved or new.

**Next, as ranked.** H2 (second blind read of the span lines, on sheets re-cut without the overlap, agreement on at least
9 of 10 letter classes) before H4 applies the map to the unmarked runs under the 20-shuffled-map control. Files:
`scripts/read_call_V3.tsv`, `scripts/f61vbar3_result.txt`, `scripts/f61crib4.py`, `scripts/f61crib4_result.txt`,
`scripts/f61crib4_map.tsv`; HYPOTHESES.md rows added. Requests: none. Vision calls: 1 of 4. No credentials, no
AskUserQuestion, no novelty wording; the owner not named.

## Correction to steps H1-H15b (2026-09-27 23:09 UTC, found while preparing H2)

`scripts/f61crib.py`'s CLASS_RULES tested `a-shape` before `beta`, so the reader's two "beta-shape" signs (L07/4, L11/1,
both under Tomokiyo's m) were classed CA (the a-shape, a null) from H1 on; `scripts/class_diag.tsv` had them right
(beta = m). The self-test of H2's scorer (pass A against itself should agree 10/10) exposed it: BETA had no signs. Fixed
by ordering the beta rule first; every class-map script re-run and its result file rewritten (`--check` fresh):
H1 unchanged (24/55 vs max 0.345, PASS); H11 now 34/55 = 0.618 vs max 0.436 (was 36/55 vs 0.400), gate (a) PASS and
gate (b) FAIL as before; H12 unchanged (37/55 vs 0.436; the all-span map's in-sample misses now name a@BETA instead of
m@CA); H15b unchanged (42/55 vs 0.400, PASS). CAMPAIGN.md's H11 cell and HYPOTHESES.md's H11 row carry the corrected
numbers with the first ones beside them. `scripts/f61_atlas.tsv` gained a BETA code and `scripts/passA_classes.tsv`
was rebuilt before pass B was called.

## Campaign step H2 (2026-09-27 23:12 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i). One Opus vision subagent call (about 110k subagent tokens,
79 s), no network. Hypothesis H2: a second independent blind read reproduces call A's shape classes.

**Preparation, all pushed before the call.** (1) Sheets B, `images/f61sheetB_L*.jpg` (regen stanza appended to
`images/regen_f61r_sheets.sh`): the whole of each span line in 4 segments cut with `tools/iiif_lines.py --overlap 0`
and each non-final segment trimmed to the next one's x0 before the 3x scale, so no sign repeats (a sign on a boundary
is split, and the reader was told to count it once). (2) `scripts/f61_atlas.tsv`: the reader's own 19 shape classes
plus VBAR_A/VBAR_B (H15) and BETA, worded as shapes only, no letters, no cells -- the shared code book of
`.claude/briefs/transcription.md`. (3) `scripts/passA_classes.tsv`: call A in atlas codes. (4) `scripts/f61pass2.py`:
`tools/reconcile_passes.py` (long format, NW) aligns the passes; a letter class agrees if more than half of its pass-A
signs get the same class in pass B; gate 9 of 10 (VBAR_A/B counted as one class for this count). Self-test 10/10 on
identical passes -- which exposed the beta/a-shape rule-order bug corrected above.

**Result (`scripts/passB_classes.tsv` verbatim, `scripts/f61pass2_result.txt`).** Pass B lists 85 signs (call A 82):
identical counts on L01, L07, L08, L11; L03 17 vs 15 and L05 19 vs 18, the extras being 'a' shapes at the edges of the
cipher runs that pass B itself flags as probably handwriting ("Cambray a", "a le...", "sont a"). Aligned columns 85,
identical code 79 (0.929).

| class | pass-A signs | pass B same | verdict |
|---|---|---|---|
| PHI | 16 | 14 (1 gap, 1 DBL) | agree |
| C43 | 9 | 9 | agree |
| 4TRI | 6 | 6 | agree |
| VBAR (A 5, B 3) | 8 | 8, and A/B split 8/8 | agree |
| DBL | 4 | 4 | agree |
| INF | 5 | 5 | agree |
| ZHOOK | 3 | 3 | agree |
| EBR | 3 | 3 | agree |
| BETA | 2 | 1 (L07/4 read C43, alt 4STEM; cut at a sheet-B segment boundary) | DISAGREE |
| 4PI | 2 | 2 | agree |
| null classes (non-gating) | | CROSS 2/2, C6 6/6, ELOOP 2/2, CA 7/9, HASH4, LOOPBAR 3/3, CH, LL, 4STEM 1/1 each; LOOPSTEM1 -> LOOPBAR | |

**Gate: 9 of 10, PASS.** Call A's classes are not reader noise: a second blind reader with a different sheet cut and only
a shape code book reproduces them, including the VBAR split H13-H15 established. The one miss is the smaller of the
two BETA signs on a boundary-cut crop. Not a reading; no class change.

**Next, as ranked.** H4: apply the cell map (`scripts/f61crib4_map.tsv`) to the unmarked runs (L02, L04, L10) under the
20-shuffled-map control. Files: `images/f61sheetB_L*.jpg` (6), `images/regen_f61r_sheets.sh`, `scripts/f61_atlas.tsv`,
`scripts/passA_classes.tsv`, `scripts/passB_classes.tsv` (+ `.README`), `scripts/f61pass2.py`,
`scripts/f61pass2_result.txt`; HYPOTHESES.md row added. images/ is 4.7 MB. Requests: none. Vision calls: 1 of 4. No
credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H4 (2026-09-27 23:16 UTC) -- dropped, control below gate

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i), script-only; the step's vision call was NOT spent. Hypothesis
H4: apply the H15b cell map to the unmarked runs under a permuted-map control.

**Pre-registered pipeline (`scripts/f61apply.py`, committed 29a3e470 before any unmarked line was read).** Letter classes
= those of `scripts/f61crib4_map.tsv` with top-cell count >= 2 and no tie (11: PHI e/r, C43 a/n, C6 a/n, 4TRI c/p, INF
h/u, VBAR_A g/t, DBL b/o, LOOPBAR a/n, VBAR_B f/s, EBR l/y, ZHOOK i/x); everything else null. Each letter sign offers its
cell's two letters; a beam search (width 200) picks the string maximising `tools/judge_plaintext.py`'s fr16 4-gram model
(Lettres de Catherine de Medicis t.1). Statistic: best-path mean log10 4-gram per letter, pooled. Control: 20 maps with
the cells permuted across the letter classes (seed 1). Positive control, run first per the control-first rule: the five
known span lines (pass A classes), also compared with Tomokiyo's letters.

**Positive control result (`scripts/f61apply_result.txt`).**

| run | letters | target | permuted mean / max | gate | best path vs Tomokiyo |
|---|---|---|---|---|---|
| pre-registered map | 62 | -0.992 | -1.159 / -0.959 | **FAIL** | 32/51 = 0.627 |
| post hoc: dash-share null rule (C6 5/6 and LOOPBAR 2/3 of occurrences under Tomokiyo's dashes -> null) | 53 | -0.927 | -1.208 / -0.932 | PASS by 0.005 | 32/51 = 0.627 |
| judge reference at N=53-62 | | | real p05 -0.53 to -0.57, shuffled-letters p99 -1.47 to -1.60 | | |

The best paths themselves show the problem: L03 reads "aestcapanabl" (Tomokiyo: est capable), L08 "raaubeaunpere"
(e au beau-pere), L11 "ryentroit" (mel'ente noit) -- the map's cells are right, the spurious a/n from the C6 and LOOPBAR
classes and the 4-gram model's choice within each pair are not. Under the pre-registered rule the positive control is
**below its gate**, so by CLAUDE.md rule 3 (control first, Usage item 8) the target read was not run: a target FAIL would
have been a non-test and a target PASS uninterpretable. The post-hoc dash-share rule, which drops exactly the two classes
`scripts/class_diag.tsv` already had as nulls, brings the control to a 0.005 margin -- consistent with the map, but no
power at N=53, and the unmarked lines hold about 20-25 signs. **H4 dropped**: the statistic, not the map, is the limit.
Not a reading; no class change. Sheets B for L02, L04, L06, L09, L10 (`images/f61sheetB_*.jpg`, 6.5 MB folder) are on
disk for the next attempt.

**Next (H16).** A blind model-judge ranking with the same permuted-map control, positive control first: one Opus text
call ranks 21 candidate sets (the target map and 20 permutations, shuffled order) by how well each resolves into French;
the target must rank first of 21 on the known lines before the unmarked lines are read. Files: `scripts/f61apply.py`,
`scripts/f61apply_result.txt`, `images/f61sheetB_L02/L04/L06/L09/L10.jpg`; HYPOTHESES.md row added. Requests: none.
Vision calls: 0. No credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H16 (2026-09-27 23:24 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i). One Opus vision call (unmarked lines, about 103k subagent
tokens) and two Opus text calls (the judge, about 105k and 88k), no network. Hypothesis H16 (F61-JUDGE): a blind
model-judge ranking with the permuted-map control, positive control first.

**Design, pre-registered (`scripts/f61judge.py`, committed 42e049d9 before any judge call).** The H15b cell map with H4's
dash-share null rule (9 cells: PHI e/r, C43 a/n, 4TRI c/p, INF h/u, VBAR_A g/t, VBAR_B f/s, DBL b/o, EBR l/y, ZHOOK i/x;
all other classes null and dropped) and 20 permutations of those cells across those classes (seed 1) each render the
same sign sequences as pair-ambiguous strings ([e/r] [a/n] ...). The 21 sets go to one Opus text call in a shuffled
order (seed 7) with the key withheld (`f61judge_<tag>_key.json`, which the judge is told not to open); it resolves each
set into its most French-like reading and scores it 0-10. Statistic: the target's rank among 21, ties against it.
Gate: rank 1 (p = 1/21 = 0.048 if the judge cannot tell). Order: the five known span lines first (positive control),
the unmarked lines only on a pass.

**Positive control (`scripts/f61judge_known_sets.txt`, `_verdict.tsv`, `_result.txt`).** Target SET-13 scored 7; every
other set 2 or less (SET-01 2, SET-06 1.5, five at 1, the rest 0.5). **Rank 1 of 21, PASS.** The judge's blind
resolutions of the target: "auecet | estcapabl | tropauancers | ileusi | enuoenupere | elentroit" -- against Tomokiyo's
avec, est capable, trop avancees, jalousi(e), e au beau-pere, mel'ente noit, without ever seeing them.

**Unmarked lines (`scripts/read_call_U.tsv`, verbatim).** One Opus vision read of `images/f61sheetB_L02/L04/L06/L09/
L10.jpg` with the atlas: L10 carries one run of 13 signs ending the line after the clear words "pas paresseux si"
(EBR CA PHI VBAR_A PHI PHI VBAR_B INF CA C6 PHI CA C6: 8 letter-class signs); L02 a 3-sign fragment at the line start
(LL, PHI, OTHER: one letter sign); L04 a lone LOOPBAR (null); L06 and L09 no cipher. The 21 sets built from it
(`f61judge_unmarked_sets.txt`) went to a fresh judge with the clear words before the run as context.

**Result (`scripts/f61judge_unmarked_verdict.tsv`, `_result.txt`).** Target SET-13 scored 8; next best 3 (SET-01), then
2.5, the rest 2 or less. **Rank 1 of 21, PASS.** Resolution of L10: **l e t r e s u r** ("le tresur", the sign-by-sign
pairs being [l/y][e/r][g/t][e/r][e/r][f/s][h/u][e/r]); L02's one letter sign e/r resolved e.

**What this is and is not.** A controlled cryptanalytic fragment: eight letters of L10 under a map that ranks first of
21 on known text and, independently, on this run (p = 0.048 each, rule 3 satisfied with the positive control run
first). Grades (rule 4): the 8 letters S (the cell is cryptanalytic with a control), the choice within each pair M
(the judge's, not checked against anything); the 55 letters of the five spans remain Tomokiyo's (H for this test
only). It rests on ONE blind pass of L10 and is therefore not reading-ready (`.claude/briefs/campaign.md` step 6 asks
for two passes reconciled): H17 is that second pass. It is a fragment, not a reading of the letter; nothing here is
solved, new or first. The cell map is now: PHI e/r, C43 a/n, 4TRI c/p, INF h/u, VBAR_A g/t, VBAR_B f/s, DBL b/o, EBR
l/y, ZHOOK i/x (9 of the table's 11 cells; d/q and m/z unassigned -- BETA m/z rests on 1 letter), with CA, C6,
LOOPBAR, CROSS, ELOOP, LL, HASH4, 4STEM, 4PI, LOOPSTEM1, CH as nulls or unassigned.

Files: `scripts/f61judge.py`, `f61judge_known_*` (4), `f61judge_unmarked_*` (4), `scripts/read_call_U.tsv`;
HYPOTHESES.md row added; H5 dropped as superseded. Requests: none. Vision calls: 1 of 4; text calls: 2. No credentials,
no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H17 (2026-09-27 23:26 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i). One Opus vision call (about 95k subagent tokens), no
network. Hypothesis H17: a second independent blind read of L02/L04/L10 reconciles with H16's read.

**Result (`scripts/passU2_classes.tsv` verbatim, `scripts/f61pass3_result.txt`; gate pre-registered in
`scripts/f61pass2.py --gate-line L10`, commit 3b70d555).** `tools/reconcile_passes.py` (NW) aligns 18 columns over the
three lines, 16 identical. **L10: 0 of 13 columns differ** (EBR CA PHI VBAR_A PHI PHI VBAR_B INF CA C6 PHI CA C6 in both
passes), **PASS**. The two differences: L02's opening "ll", which pass 2 reads as the handwritten "Il" (pass 1 had coded
it LL with the same doubt), and a second L04 sign after "Come" that pass 2 codes OTHER at confidence l as a possible
abbreviation -- both nulls, both outside the fragment.

**Fragment (`scripts/fragment_L10.tsv`, regenerated by `scripts/f61fragment.py --check`, rule 7).** f.61r, line L10, the
run that ends the line after the clear words "pas paresseux si" (both passes): 13 signs, 8 letter classes and 5 nulls,
under the H15b cell map with the dash-share null rule, resolved by the blind judge (H16) as

    l e t r e s u r    ([l/y] [e/r] [g/t] [e/r] [e/r] [f/s] [h/u] [e/r]; nulls CA, CA, C6, CA, C6 between and after)

Grades (rule 4): 0 H, 0 C, 8 S for the cells (controlled: H15b 42/55 vs permuted max 0.400; judge rank 1 of 21 on the
known lines and 1 of 21 on this run, p = 0.048 each), the same 8 M for the letter chosen within each pair (the judge's
choice, unchecked), 5 nulls S. A cryptanalytic result. Not a reading of the letter: one run of eight letters. No
letters of this run are marked on Tomokiyo's annotated image (`sources/cryptiana/web/img/BnFfr4715f61.png`, the image
`bnf4715.htm#no38` embeds), which spells out only the five spans but also sets two dashes, and no letters, over the
last two signs of L10 (CA C6, positions 12-13; correction by VERIFY-F61-FRAG-1, 27 Sept 2026 -- the earlier wording
said the image "marks only the five spans"); nothing here is said to be new, first or unpublished (rule 10: the
verifier's call). [Audit 1, 27 Sept 2026, AUDIT.md: cells of positions 6, 7 and 11 downgraded S -> M (5 S, 3 M), letters
within pairs all M; the judge positive control did not reproduce at its gate on a fresh order and prompt (target tied
first, 3 vs 3); verdict held, no N-class.]

**Reading-ready line posted for LANE VO3** (campaign brief step 6): the fragment, the two passes, the map, the two judge
rankings and their controls are all in `scripts/` and this file. Files: `scripts/passU1_classes.tsv` (H16's read
without its comment lines), `scripts/passU2_classes.tsv` (+ `.README`), `scripts/f61pass2.py` (--a/--b/--out/--gate-line),
`scripts/f61pass3_result.txt`, `scripts/f61fragment.py`, `scripts/fragment_L10.tsv`; HYPOTHESES.md row added.
Requests: none. Vision calls: 1 of 4. No credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H3 (2026-09-27 23:29 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i), script-only plus 3 requests to cryptiana.web.fc2.com (1.6 s
apart, browser UA as recorded for this host). Hypothesis H3: a Cryptiana page or image on a fr.3982/3983 sibling with
its own interlinear markup.

**Search.** `sources/cryptiana/web/` (318 files) grepped for 3982/3983: ten pages; the sibling list is only in
`mayenne.htm`, and `league.htm`/`nevers.htm`/`paleography.htm` name other letters in those volumes (Pelissier, Pisany,
Gondy, Vinta, the Savoy ambassador), none of this cipher. `mayenne.htm` embeds four images; the mirror held only
`mayenne.png` (the table). Fetched the other three, now in `sources/cryptiana/web/img/` with rows in
`sources/cryptiana/web/manifest_2026-09-27-4715f61.tsv` (sha1 recorded).

**Found.** `mayenne2.png` (1069x256), captioned "Part of Duke of Mayenne's letter (1593)", is the page's "specimen of
the use of this cipher (taken from f.108 of BnF fr.3983)": two cipher lines with Tomokiyo's letter-by-letter reading
overlaid in magenta ("satisfaire ung seul au prejudice de plusieurs" / "au[t]res ... appr[e]nent ... de leurs ... la
commoditez", about 85 letters, one look by the runner, not a transcription), and two further lines where the manuscript
itself appears to carry period interlinear clear words above cipher groups. `mayenne3.png` is Tomokiyo's reconstruction
of the different homophonic cipher of fr.3984 ff.7-10 (May 1593), not this cipher. `mayenne4.png` not looked at.
fr.3983's Gallica manifest is already cached (`sources/gallica-manifests/btv1b9059406b.json`); `tools/gallica_folio.py`
gives the canvas for f.108 offline.

**What it changes.** A second letter of the same office and key with about 85 letters read by Tomokiyo would more than
double the known-answer set and, better, lets the f.61-fitted cell map be tested on a letter it was not fitted on
(a transfer test, before any refit). If the leaf's own interlinear clear words are a period decipherment, that is a
grade-C key source for the verifier and the recovery route, not a cryptanalytic one. The strip itself is about 25 px
per sign, F61-CAL's own failure mode, so nothing is read from it blind: H19 fetches the leaf. Requests this step:
cryptiana.web.fc2.com 3. No credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H19 (2026-09-27 23:50 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i). Three vision calls (one Sonnet anchoring look, two Opus
passes; about 177k, 95k and 95k subagent tokens) plus one Sonnet text-from-image call (Tomokiyo's overlay, 114k);
8 requests to gallica.bnf.fr (5 small canvases and one native region, plus the runner's two at 800 px), 1.6 s apart.
Hypothesis H19 (F61-3983): fetch fr.3983 f.108 and test the f.61 map on it before any refit.

**The leaf.** BnF fr.3983 f.108r is canvas 195 of ark btv1b9059406b (no folio labels in the manifest; anchored by the
ink "108" top right and the clear lines "Et pour cela je vous laisse a juger quel contentement je debvois avoir" matching
`mayenne2.png`; canvases 114, 116, 118 = ff. c.67-69, 196 = f.108v, 197 = f.109r, in `images/manifest.json`). The native
region 1250,450,3600,720 (the strip's four lines and three more) was fetched once
(`images/src_ark_12148_btv1b9059406b_f195_1250_450_3600_720.jpg`) and cut by `tools/iiif_lines.py --overlap 0` into 7
bands at pitch 96 (`images/f108_lines_debug.jpg`), then trimmed sheets B (`images/f108sheetB_L01-L07.jpg`, regen stanza
in `images/regen_f61r_sheets.sh`). **The page carries a period interlinear decipherment**: small clear words above the
cipher lines ("satisfaire ... ung seul au prejudice de plusieurs", "aultres qui ... de leurs incommodites", "la ... je ...
retour ...", "quinze ..."), which Tomokiyo's magenta overlay reprints. That is a grade-C key source (CLAUDE.md
transcription brief's first check), logged here for the verifier and H21; it is not our reading.

**Reference.** `scripts/tomokiyo_spans_3983.tsv`: Tomokiyo's overlay letters on the strip's two cipher lines, transcribed
from the printed overlay by one Sonnet call (T1 39 letters "satisfaireungseul auprejudicedeplusieurs", T2 45
"aultresquimeprenentagarentdeleurs jacommoditez"); grade H for this test only.

**Passes (`scripts/pass108A_classes.tsv`, `pass108B_classes.tsv`, verbatim).** Two independent blind Opus reads of
bands L02 and L03 with `scripts/f61_atlas.tsv`: both count 39 and 43 signs; `tools/reconcile_passes.py` (NW) 67/82 =
81.7% identical (15 columns differ, mostly PHI/DBL, C43/4STEM and 4PI/HASH4 alternations the passes themselves flag as
alternatives; L03 has two OTHER signs, an I-shape read the same by both, and a 7/F shape).

**Transfer test (`scripts/f61transfer.py`, pre-registered f18c2ac4 before the passes; `f61transfer_result.txt`).** The
f.61 map (9 cells, dash-share null rule), unrefitted, DP-aligned to the reference letters on the reconciled draft:

| | signs | reference letters | matched |
|---|---|---|---|
| T1 on L02 | 39 (0 OTHER) | 39 | 26 |
| T2 on L03 | 43 (4 OTHER) | 45 | 28 |
| **pooled** | | **84** | **54/84 = 0.643** |
| 20 permuted-cell maps | | | mean 0.219, **max 0.381** |

**Gate met, PASS.** A map fitted on 55 letters of one leaf reads a second letter of the same office, in another hand,
at 0.643 -- about 1.7x the best permutation and three times the mean -- with no refit. Rule 3 satisfied (the control is
the same statistic on the same signs under permuted maps); rule 4: nothing here is a reading of ours (the 84 letters
are Tomokiyo's, reprinting the period gloss), it is a test of the map. No class change; no word of solved or new.

**What it opens.** (H21) The period interlinear decipherment on f.108 can give the key at grade C -- every cell,
including d/q and m/z and any word codes, with counts -- by the Thurloe method (`tools/interlinear_align.py`), which is
the recovery route the successful solvers use; the f.61 fragment and any further f.61 reading would then be key
application, not cryptanalysis. (H20) A joint cell fit with each leaf as a held-out fold. Files: `images/` (region,
debug overlay, 7 sheets; folder 9.7 MB), `images/manifest.json` (f108_bands), `scripts/tomokiyo_spans_3983.tsv`,
`scripts/pass108A/B_classes.tsv` (+ READMEs), `scripts/f61transfer.py`, `f61transfer_result.txt`; HYPOTHESES.md row
added. No credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H20 (2026-09-27 23:53 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i), script-only, no calls, no network. Hypothesis H20 (F61-JOINT):
the cell fit across both leaves, each leaf as a held-out fold (`scripts/f61joint.py`, pre-registered in its docstring;
`f61joint_result.txt`, `f61joint_map.tsv`).

| fold | read | 20 permuted maps mean / max | gate |
|---|---|---|---|
| (a) fit f.61 (55), read f.108 (84) | 57/84 = 0.679 | 0.237 / 0.321 | PASS |
| (b) fit f.108 (84), read f.61 (55) | 37/55 = 0.673 | 0.178 / 0.327 | PASS |
| (c) five f.61 span folds, f.108 always in training, pooled | 44/55 = 0.800 (42/55 without f.108) | per fold max 0.50-0.83 | reported |
| nine cells identical in every fold | PHI e/r, C43 a/n, 4TRI c/p, INF h/u, VBAR_A g/t, ZHOOK i/x yes; EBR f/s on f.108 vs l/y on f.61; VBAR_B, DBL null in (b) (absent from f.108's two lines) | | **FAIL** |

**H20 FAIL as pre-registered** on the stability part; both transfer folds pass by wide margins. The one real conflict is
the bracket class: on f.108 the "E-like bracket open right" sits under f/s (8 of 13 counts), on f.61 under l (3). The
Mayenne table itself draws two bracket-like glyphs -- an E shape for f/s and a squared C or gamma for l/y -- and f.108's
I-shaped OTHER signs (read the same by both passes) come out l/y (2). The atlas most likely merges two glyphs, the shape
H13-H15 found for the V signs; H22 tests it the same way. Absences (no VBAR_B or DBL on f.108's two lines) are not
conflicts. The joint map (139 letters) adds cells the f.61 map lacked: 4PI = d/q (4 counts, the table's 11th cell),
BETA = m/z (4), 4STEM = a/n (3, beside C43 = a/n -- the table draws a and n as two distinct symbols, H23 checks whether
these classes are that split). Not a reading; no class change; grades unchanged (M for the cells, from Tomokiyo's markup
and the period gloss it reprints). Files: `scripts/f61joint.py`, `f61joint_result.txt`, `f61joint_map.tsv`;
HYPOTHESES.md row added. No credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H23 (2026-09-27 23:54 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i), script-only. Hypothesis H23 (F61-SUBSYM): do the reader's
classes already separate the table's two a/n symbols and two e/r symbols? (`scripts/f61subsym.py`, `f61subsym_result.txt`,
pre-registered gate: a class pair with 3+ counts each side and at most 1 crossing.)

| class | a | n | other | | class | e | r | other |
|---|---|---|---|---|---|---|---|---|
| C43 | 8 | 6 | b 1 | | PHI triple loop (f.61) | 5 | 2 | |
| 4STEM | 3 | 0 | | | PHI plain (f.61) | 6 | 0 | o 1 |
| C6 | 2 | 0 | | | PHI (f.108, unsplit) | 13 | 7 | o 2 |
| LOOPBAR | 2 | 0 | | | | | | |
| 4PI | 0 | 1 | d 4, p 1 | | | | | |

**FAIL as pre-registered.** C43 carries a and n alike over the two leaves; 4STEM's three a's are suggestive but n never
appears under it, and PHI's subtypes both lean e. The polyphony is genuine at the reader's class level: the table's
second symbol for a/n and e/r is not a class the atlas has. H24 (CAMPAIGN.md) proposes the H13-H15 instrument -- a blind
shape sort of the C43 signs against the a/n letters at their positions -- which is what separated VBAR. Not a reading;
no class change. Day's budget after this step 39.25/40 (the orchestrator's 23:43 reconciliation plus the runner's
estimates since): the next steps (H22 est 2, H21 est 4) wait for the new day's budget or a raise. No credentials, no
AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H22 (2026-09-28 00:53 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i). One Opus vision call (about 131k subagent tokens), prompt
written to `scripts/PROMPTS.md` before the call (audit 1's ask), no network. Hypothesis H22 (F61-BRACKET): H20's one real
conflict -- the bracket class reads f/s on f.108 and l/y on f.61 -- is two glyphs the atlas merges.

**Design, pre-registered (`scripts/f61bracket.py`, commit aa00572e).** Expected positions computed from disk: 18
bracket-class signs (EBR and OTHER I-shapes) on the eight sheets, 14 labelled by Tomokiyo's letters under the joint
alignment (8 f/s, 6 l/y). The call sorts every bracket-like cipher sign on both leaves into 2-3 shape groups with fixed
attributes, no letters shown. Pairing per sheet in order (sheets B do not overlap); a sheet whose count differs is
dropped. Statistic: best group-to-letter match; exact null over all label arrangements, plus 200 permutations.

**Output (`scripts/read_call_BR.tsv`, verbatim).** 18 signs, three groups: A "a fine hairline diagonal from the right
end of the top bar down to the foot of the vertical and a foot bar longer than the top bar that tapers into a tail"
(f.108 only, 9 signs); B "a plain squared C open to the right with no diagonal and the top bar longest" (all four f.61
signs, two on f.108, one uncertain on f.108 L07); C "closed like a capital I" (f.108 L03's two I-shapes, one uncertain on
L07). The call itself notes that A's hairline diagonal "nearly closes the sign into a triangle" -- the table's own f/s
drawing is an E-like bracket, its l/y a squared C or gamma (keys/key_mayenne_1592.tsv rows f and l).

**Result (`scripts/f61bracket_result.txt`).** Reconciled sheets: f.61 L03, L07, L11, L10 (1 each) and f.108 L02 (8);
f.108 L03 dropped (expected 6 because the expected list carried two non-bracket OTHER shapes; the call listed 4) and
L07 unscored (no reference). Scored 10 labelled positions: **A = f/s 6/6, B = l/y 4/4, 10/10, exact p = 0.005** (210
arrangements), permutation p95 8/10. **PASS.** The unlabelled f.61 L10/1 (the fragment's first sign) is group B, the
squared C, consistent with its l/y cell.

**Consequence.** The bracket class splits as the V class did: EBR_A (E with hairline diagonal) = f/s, EBR_B (squared C)
= l/y, on both leaves; the I-shape (C) stays its own class (l/y by 2 counts in the joint fit, unsettled). H27 re-runs the
joint fit with the split, which should close H20's stability gate. Not a reading; no class change. Files:
`scripts/f61bracket.py`, `read_call_BR.tsv`, `f61bracket_result.txt`, `scripts/PROMPTS.md` (H22 section); HYPOTHESES.md
row added. No credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H27 (2026-09-28 00:55 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i), script-only. Hypothesis H27 (F61-JOINT2): the joint fit with
the bracket class split by H22's blind groups (`scripts/f61joint2.py`, a relabel hook added to `scripts/f61joint.py`
whose default output is unchanged; `f61joint_h27_result.txt`, `f61joint_h27_map.tsv`).

| fold | H20 (one EBR class) | H27 (EBR_A / EBR_B, ISH) | permuted max (H27) |
|---|---|---|---|
| (a) fit f.61, read f.108 | 57/84 = 0.679 | 57/84 = 0.679 | 0.286 |
| (b) fit f.108, read f.61 | 37/55 = 0.673 | **41/55 = 0.745** | 0.400 |
| (c) f.61 span folds pooled, f.108 in training | 44/55 = 0.800 | **48/55 = 0.873** | per fold 0.42-0.73 |
| gated cells | EBR f/s vs l/y | EBR_A f/s 8/8, EBR_B l/y 5/5, ISH l/y 2/2; no cell differs between folds | |

**FAIL on the letter of the pre-registered gate** (VBAR_B, DBL and EBR_A read "null" in the one fold whose training leaf
has none of them, and the gate counts an absence as instability, as in H20) -- and **no real conflict remains**. Every
one of the ten gated cells is the same wherever it is fitted. The f.61 held-out pool crosses F61-CAL's original 0.85
level for the first time (48/55), with the map fitted on Tomokiyo's markup of both leaves (grade M reference). The
absence rule is noted as too strict for a two-leaf set and left as written rather than re-litigated. Not a reading; no
class change. The atlas (`scripts/f61_atlas.tsv`) now carries EBR_A, EBR_B and ISH; passes before this date used EBR.
No credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H21 (2026-09-28 01:20 UTC) -- FAIL, the runner's crop design

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i). Four calls, all prompts in `scripts/PROMPTS.md` before the
calls: two Sonnet gloss passes (about 253k and 183k subagent tokens, slow: 23 and 15 minutes) and two Opus sign passes
of bands L05-L07 (96k each). Hypothesis H21 (F61-GLOSS): the period interlinear decipherment on fr.3983 f.108r as a
grade-C key source, by the Thurloe method.

**What came back (`scripts/gloss108A.tsv`, `gloss108B.tsv`, `pass108C_classes.tsv`, `pass108D_classes.tsv`, verbatim).**
Gloss: both passes find nothing above band L02 -- because the gloss of cipher line 1 ("satisfaire ... ung seul au
prejudice de plusieurs") is band L01, cut as its own band above the cipher and never named in the prompt; on L03 the
two passes agree on 1 of 7 words, on L05 on 1, on L07 on 0, and the 7 "gloss" words of L06 in pass A are the clear
main-line clause ("Et ... d'autant que dictes"), which pass B correctly files as main line. Signs: L05 26 and L06 19 in
both passes, L07 35 in both with both readers stating the band is cropped below the line's middle; agreement 44/82 =
53.7% over the three (a systematic PHI/DBL split on L05 -- the audit's "qo" question again -- plus the unreadable L07).

**Alignment (`scripts/f61gloss.py`, pre-registered a8310c2f; `f61gloss_result.txt`).** With 11 reconciled words the
counts (`scripts/f61gloss_counts.tsv`) reach 2 on no class the map already has and agree with none of the nine cells;
**FAIL as pre-registered**, and the script was guarded afterwards so that a failed run writes its counts to `scripts/`,
never a file under `keys/` (the first run's `keys/key_f108_gloss.tsv` was deleted before commit). No key, no reading,
no class change.

**Cause and next step.** The failure is the runner's: `tools/iiif_lines.py`'s bands at pitch 96 separate each gloss row
from its cipher line, which the family worker met on f.274 and solved with `family/cut_bands.py` (a band per cipher row,
tall enough to hold its gloss, per-segment centres) -- H34 repeats H21 that way, ranked behind the family's f.101r
(H28, about 60 interlined lines) and f.108v rows. The L05/L06 sign passes stay on disk for that step. Requests: none.
No credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign steps H7, H8, H32 (2026-09-28 01:26 UTC) -- the BnF finding aids

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i), no subagent calls (the account is at its rate-limit warning;
BUDGETS.md scaling rule). Requests: archivesetmanuscrits.bnf.fr 5 (one notice, three POST searches
`resultatRechercheSimple.html` with `TEXTE_LIBRE_INPUT=Français NNNN`, one notice), oai.bnf.fr 1; 1.6 s apart, browser
UA as the playbook records for this host. Snapshots, unmodified, in `sources/bnf-aem/` with `MANIFEST.tsv` (sha1).

**fr.4715 (ark:/12148/cc577658).** The dépouillement lists no.38 as "Fol. 61 • 38 Lettre avec chiffre." and nothing more:
no sender, recipient or date (H7: the aid adds none). Fol. 66 is no.43, Mayenne to the duc de Nevers, "Au camp devant
Auxonne, 29 août 1586. Chiffre et déchiffrement", one of four Mayenne-to-Nevers letters of 1585-86 in the volume (nos
26, 43, 49, 53; ff. 49, 66, 72, 76), the earlier cipher, not this family. So the boxed ink "66" on the leaf
(`images/manifest.json`'s flag) is an older foliation, superseded: **the leaf is fol. 61, no.38** (H8 resolved), and an
outward citation reads "BnF, Français 4715, fol. 61 (no.38)".

**The family (ark:/12148/cc504266, Français 3974-3995, "Collection Mémoires de la Ligue", one finding aid for the 22
volumes).** Read within each volume's own section (folio numbers repeat across volumes):

| leaf | no. | the aid's entry (abridged) |
|---|---|---|
| fr.3982 f.97 | 41 | commandeur de Diou to "monseigneur le president Janyn, conseiller d'Estat", Rome, 27 Oct 1592; chiffre et double déchiffrement |
| fr.3982 f.101 | 42 | Anne de Perusse d'Escars de Givry, evesque de Lizieux, to "monseigneur", Rome, 27 Oct 1592; chiffre et double déchiffrement |
| fr.3982 f.124 | 55 | Diou to the duc de Mayenne, Rome, 12 Nov 1592; chiffre et double déchiffrement |
| fr.3983 f.106 | 48 | Mayenne to the commandeur de Diou, ambassador at Rome, "De Soissons, ce dernier jour de fevrier 1593", Copie; chiffre et déchiffrement |
| fr.3983 f.108 | 49 | Mayenne to Diou, "Du camp de Soissons, ce IIIIe mars 1593"; chiffre et déchiffrement |
| fr.3983 f.211 | 110 | Mayenne to Diou, "Du camp de Han, ce premier jour d'apvril 1593"; chiffre et déchiffrement |
| fr.3984 f.176 | 84 | Baudouyn Desportes to Pope Clement VIII, Paris, 22 Jul 1593; chiffre et déchiffrement |
| fr.3984 f.184 | 87 | "Deschiffrement de la lectre de Baudouyn Desportes à Mr [l'évêque] de Lizieux", Paris, 22 Jul 1593 |
| fr.3984 f.186 | 88 | Desportes to don Pietro Aldobrandini, Paris, 22 Jul 1593; avec chiffre |
| fr.3984 f.188 | 89 | "Original de la lettre déchiffrée sous le n° 87" (so: Desportes to the Bishop of Lisieux) |
| fr.3984 f.189 | 90 | Desportes to Hieronimo Frachetta, Paris, 22 Jul 1593; avec chiffre |
| fr.3984 f.274 | 115 | Anne de Givry, evesque de Lisieux, to Mr Desportes, Sr de Beuvillier, Rome, July 1593; chiffre et déchiffrement |

Two things this settles for the family rows (H28-H31, `family/KEY.md`): every leaf Tomokiyo lists is catalogued with its
decipherment ("double déchiffrement" for the three fr.3982 letters -- two decipherments, presumably the interlinear one
and a separate sheet), and the dates the family worker read on the leaves (f.106r headed "4 de mars 1593", f.108v ending
"De Soissons ce dernier jour de fevrier 1593") are the aid's dates for ff.106 and 108 **swapped**: either the two letters
were rebound or the aid's items 48/49 were numbered against the other leaf. Both are recorded here; in a citation the
aid is the authority for cote and folio and the leaf's own heading is quoted beside it, not silently reconciled (H32).
No reading, no class change, no novelty wording; the owner not named.

## Campaign step H9 (2026-09-28 01:27 UTC)

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i), script-only. Six rows appended to `JSTOR-QUEUE.tsv` for the
owner's local runner, in the verifier brief's two families: (i) "Mayenne" AND "Diou" AND chiffre; "duc de Mayenne" AND
"commandeur de Diou" AND 1593; "Diou" AND "Jeannin" AND 1592 AND chiffre; (ii) the bare quoted phrases "pas paresseux si"
(the clear words before the L10 run, both passes), "satisfaire ung seul au prejudice de plusieurs" (the period gloss of
fr.3983 f.108r line 1, as Tomokiyo's overlay prints it) and "jalousie au beau-pere" (Tomokiyo's own f.61 reading). A
queued row never blocks N3 or N4 on its own. No calls, no requests.

**Runner hold.** Every remaining open row (H29, H30, H31, H33, H34 family leaves; H25 judge re-run; H26, H24 shape sorts)
needs Opus or Sonnet subagent calls and H10 a person; the account is at its seven-day rate-limit warning (orchestrator,
01:16 UTC), under which BUDGETS.md's scaling rule allows no new workers. The runner holds until the orchestrator clears
the warning or the next firing finds it cleared; the campaign is neither budget-stopped nor closed.

## Campaign step H29 (2026-09-28 01:54 UTC) -- dropped, the runner's crop parameters

Campaign runner (Fable, session_01UgTmQhR7wFtVFrTVdtsq9i). Four Opus calls (two sign passes, two gloss passes, about
106-120k subagent tokens each), prompts in `scripts/PROMPTS.md` before the calls. Hypothesis H29: fr.3983 f.108v re-cut
at 3x for the family key.

**Non-test.** The cut (`family/cut_bands.py`, region 840,540,3160,760, the family's seven centres, --up 45 --down 25
--local 70 --scale 3.0 --seg 900 --overlap 60, as the row worded "70-px bands, --local 70") produced four byte-identical
segment files across bands (md5: L04_s4 = L03_s4, L05_s2 = L04_s2, L06_s4 = L05_s4, L07_s1 = L06_s1 -- the +-70 px
per-segment centre search jumped to the neighbouring row at pitch about 100) and 70-px bands that cut the gloss row off
at the top. All four readers reported the defect unprompted (`family/passes/f108v3x_signsA/B.tsv`, `_glossA/B.tsv`,
verbatim, with READMEs). For the record, `scripts/f61v3x.py` (pre-registered, one segment-format fix afterwards):
signs: lines 7  signs A 230  B 254  agree 187/257 = 72.8%  (nw) (PLAIN rows dropped: A 230 signs, B 254); gloss: words A 36, B 34, both 5 -> agreement 0.139; GATE H29: signs 0.728 (>= 0.80 NO), gloss 0.139 (>= 0.50 NO) -> FAIL -- numbers of a defective cut, not of the leaf. A corrected cut (--up 62 --down 34 --local 30,
3x, 288-px bands, 0 duplicate files) is installed as `family/sheets/f108v3y_*` with its `bands.json` and debug overlay;
H35 re-runs the four passes on it. Not a reading; no class change; `key_period.tsv` untouched.

**Runner handover.** This session's context is past the 700k line; the orchestrator replaces it before H35. State for the
next runner: every prompt used is in `scripts/PROMPTS.md`; the corrected f.108v crops are on disk; the campaign's open
rows are H35 (rank 4), H30, H31, H25, H26, H24, H33, H34, H10 (person); H28 is F61-FAMILY-2's.

## Campaign step H28 (2026-09-28 01:56 UTC) -- fr.3982 f.101r period interlinear key (F61-FAMILY-2)

Parent worker F61-FAMILY-2 (Fable, session_01Vs8P4sQjDByybDuR8xhQBB, brief .claude/briefs/runs/2026-09-28-parent-f61-family-2.md),
01:18-01:5x UTC. Key source `period` (rule 10 vocabulary): every pair below is the contemporary decipherer's own word,
aligned to the atlas-coded signs; grade C per pair, no cryptanalysis, no refit on f.61; f.61's known letters are used only as
the held-out test. Nothing here is called solved, new or first.

**Material.** fr.3982 f.101r (Bishop of Lisieux to "monseigneur", Rome, 27 Oct 1592; Gallica canvas 210 of btv1b9060543f),
native scan refetched once (1 Gallica request, family/requests.log 01:2x UTC; sha1 313f92b3..., identical to F61-FAMILY's
fetch). 46 cipher rows (not "about 60": the leaf carries 46 cipher rows, each with a clear line above it, plus the clear
opening line), region 940,1440,3440,4680 native px. The cutter's ink-profile detector and a stem-density detector both
locked onto the gloss rows on this leaf (gloss and cipher are equally heavy here), so the 46 row centres were set by hand
from four overlay strips and cut with `family/cut_bands.py --centres ... --up 80 --down 60 --seg 760 --overlap 60 --scale 2.0`
(140 native px tall so a row that droops up to 35 px at the right margin stays inside; segments 1520 px wide at 2x so the
vision reader gets them undownscaled; a `--track` option was added and rejected -- it drifts onto the next gloss row).
230 crops in family/sheets/f101r/ (24 MB, NOT committed: the family folder is at the 30 MB line; L01's five crops are
committed as the sample and sheets/f101r/f101r_bands.json holds every box; regenerate with the two commands in
family/MANIFEST.tsv's storage note).

**Passes (28 vision calls of the 32 allowed; every prompt on disk before its call, family/passes/PROMPTS_f101r.md and
passes/prompts_f101r/*.txt).** Six chunks of 8 bands (c6: 6 bands), 40-42 images per call. Per chunk two blind Opus sign
passes (atlas codes only) and two blind gloss passes.
- Chunk 1 ran on the atlas as first written: sign passes agreed 67.8% raw, with one systematic split -- pass A wrote OTHER
  with a shape note (60 "loop chain, no stem", 38 "z-like with bar", 11 "r-like") where pass B wrote PHI / ZHOOK / BETA. The
  atlas lacked three signs of this hand; rows LOOPS, ZBAR, RSIGN were added before any chunk-2 call and chunk 1's two passes
  were relabelled by the rule in f101r_pipeline.py (each pass by its own text, raw files kept): 80.2% after relabel.
- Gloss: the two Sonnet passes of chunk 1 (the brief's model) agreed on 31/122 words = 25.4% and misread the secretary hand
  systematically ("nona" for nous, "boua" for vous, "dedublea" for dernieres) -- the f.108v failure again. Gloss moved to
  Opus (passes C and D, same prompt text; the two Sonnet chunk-2 calls already in flight were stopped and their partial
  output discarded; the Sonnet chunk-1 files are kept as written and not used). Opus passes agree 72.4% by identical word
  (532/735), and both readers still write "Bona anona" where the leaf reads vous avons on L01 -- a b/v confusion the
  alignment inherits (recorded, not corrected by hand).
- Sign agreement over all 46 bands: 2472/3081 aligned columns = 80.2% (tools/reconcile_passes.py, nw). Per band 65-95%;
  one band, L23, at 47/72 = 65% is under the brief's 70% line (chunk 3 as a whole 74.7%, above it) -- L23 is kept in the
  alignment and named in H38 for a re-cut. L46's right end (s4-s5) droops out of its band with no next band to read it
  from: both readers graded those signs l.
- Independence caveat: the chunk-5 sign-A reader reported that another pass overwrote two of its scratch working files
  (shared scratchpad, same file names) and that it rebuilt them from its own reading before writing its TSV; chunk-6 gloss D
  was told to use a pass-named subfolder. Chunk 5's sign agreement (80.4%) is in line with the other chunks.

**Alignment (family/align_period.py f101r; tools/interlinear_align.py --code-prefix @ --null-cost -1 --clear-consumes,
one pair per band).** 3,077 sign tokens against the reconciled gloss (dashes and struck-through words dropped): 1,352 take
their class's top meaning, 1,522 a secondary meaning (the polyphony plus reader class merges), 197 null. 288 (class, letter)
rows over 27 classes -> family/key_period_f101.tsv. At n >= 2 and n >= 10% of the class's total on this leaf (the threshold
the tests use, see below), the leaf's key reads: PHI e/r/o (742 tokens), 4TRI a/n/c (438: this hand's readers merged the
"43" sign into 4TRI -- C43 itself a/n on only 76), VBAR_A t/s (368), LOOPS u (263; the h/u cell, f.274's INF, which also
reads u here on 35), H24 i (235), EBR_B l (146), HASH4 d/q (108), 4STEM a/n/c/e (77, the third 4-shape merge), C43 a/n (76),
EBR_A s/l (62), BETA m (52), ZBAR s (49), VBAR_B s (35), DBL e/r/u (29), 4PI d/n/q (15), RSIGN m/t (30), LOOPSTEM1 q (15),
C6 e (2 -- too few to use). Against family/key_period.tsv (f.274r, same secretary hand) every shared class gives the same
top letters (PHI e/r, C43 a/n, INF u, VBAR_A t/s, 4TRI c/p within its a/n/c/p set, EBR l, HASH4 d/q, H24 i, BETA m);
merge_period_keys.py records two top-letter conflicts, both reader merges rather than key conflicts: 4TRI (f.274 top c, f.101r
top n) and OTHER.

**Merge.** family/key_period_v2.tsv = key_period.tsv rows + key_period_f101.tsv rows, one row per (class, letter, leaf), nothing
summed across leaves, conflicts in the header (merge_period_keys.py). 325 rows, 24 classes.

**Tests, no refit (family/test_period_key.py --key key_period_v2.tsv --collapse-ebr; 20 permuted keys, seed 1; results in
test_period_key_result_v2*.txt).** At this token count the letter sets need a threshold: with every n >= 1 letter kept, a
permuted key already reads 0.836 of f.61's known letters (every class carries a tail of one-off alignment letters), so
n >= 1 and n >= 2 alone are NOT tests here (permuted max 0.836 and 0.818 against targets 0.855 and 0.800). The figure this
step reports is the n >= 2 AND n >= 10%-of-class rule (--min 2 --frac 0.1, per leaf):

| key | f.61 five known spans (55) | permuted mean / max | f.108r overlay (84) | mean / max | f.61 signs covered |
|---|---|---|---|---|---|
| key_period.tsv (f.274 only, n >= 2; F61-FAMILY) | 40/55 = 0.727 | 0.165 / 0.273 | 51/84 = 0.607 | 0.205 / 0.274 | 0.56 |
| key_period_v2.tsv, n >= 2, >= 10% of class | 43/55 = 0.782 | 0.344 / 0.618 | 65/84 = 0.774 | 0.317 / 0.488 | 0.80 |
| key_period_v2.tsv, n >= 2 (no fraction) | 44/55 = 0.800 | 0.642 / 0.818 | 69/84 = 0.821 | 0.551 / 0.690 | 0.80 |

Gate (brief step 5, 0.75 on the 55 known letters): PASS at 0.782, above the permuted max (0.618) but with a thinner margin
than f.274 alone had (0.382), because the wider letter sets help permuted keys too. Coverage of f.61's signs rises from
0.56 to 0.80: of the seven classes named in the brief, **C6, DBL, VBAR_B and 4PI are now covered** (C6 only by 2 tokens);
**CA, LOOPBAR and ZHOOK are not** (this hand does not use them, or its readers coded them otherwise), and CROSS and LL
(one and two signs on f.61) are not either.

**Step-5 decision.** The 0.75 condition holds but the every-class condition does not (CA, LOOPBAR, ZHOOK, CROSS, LL
uncovered), so no "reading ready" line is posted. For the record, family/decode_period.py --key key_period_v2.tsv --frac 0.1
writes the C/M skeleton f61_decode_period_v2_frac0.1.txt: 99 signs, C 15, C+ 8 (two leaves agree on the one letter),
M 56 (period pair, choice by context not made), unread 20 (was C 14 / M 42 / unread 43 under f.274 alone). Not a reading of
the letter.

**Left undone, as CAMPAIGN.md rows:** L23 re-cut and re-run (H38); L46 s4-s5 droop re-cut with a taller band (H39); a blind
shape sort of this leaf's 4-shaped signs (4TRI / C43 / 4STEM / HASH4 / H24 / 4PI) to undo the reader merges before the
family key is used further (H40); the gloss b/v reading; the missing classes come only from another hand (H29/H31 as
already ranked).

**Calls and cost.** 28 vision calls (Opus 24: 12 sign + 12 gloss; Sonnet 4: chunk-1 gloss A/B counted, chunk-2 gloss A/B
stopped mid-way and counted as spent), about 120-150k subagent tokens each; Gallica 1 request. Cost about USD 40 (this
worker's own estimate; the orchestrator's get_session figure is the record).

## Campaign step H30 (2026-09-28 02:2x UTC) -- fr.3984 f.188r/f.184r, the separate-sheet pair (F61-FAMILY-3)

**What was done.** The leaf is mixed clear-and-cipher (48 rows, cipher from row 10), not an 18-line block; rows 13-35 were
read: 23 bands, two blind Opus sign passes in three chunks (6 calls, 77.6% identical over 1,206 aligned columns), and the
whole clear copy f.184r (40 lines, two blind Opus passes, 95.5% by word, 2 calls). Alignment by the new separate-sheet mode
`family/align_separate.py` (rule recorded in family/KEY.md "f.188/f.184"): clear-word anchors, proportional spans, then
the shared `tools/interlinear_align.py` DP per band. Result `family/key_period_f188.tsv`, 186 rows / 23 classes from 1,006
signs (band L23 dropped, defective crop). Grade C per pair (period decipherment, no cryptanalysis, no refit).

**Control (rule 3).** Held-out against the f.274 key (the H30 gate): the nine shared classes give the same top letters read
blind on a third hand (PHI e/r, C43 a/n, 4TRI c/p, INF u, VBAR_A t, EBR l, HASH4 d/q, H24 i, BETA m). Family key v3 (the
three leaves merged, nothing summed): f.61 known spans 43/55 = 0.782 vs 20 permuted keys mean 0.372 max 0.618; f.108r
66/84 = 0.786 vs 0.344 / 0.512 (`family/test_period_key_result_v3_frac0.1_min2.txt`). Coverage of f.61's signs 0.80;
CA, LOOPBAR, ZHOOK, CROSS, LL still uncovered (Desportes' hand does not write them; 3 CA, 1 LOOPBAR, 0 ZHOOK read).

**Failure log.** First alignment run: the first band's junk clear words (cipher runs the reader wrote as letters, 'gueu')
anchored 276 words away and the open-ended spans took the rest of the page (letters per sign 12-40) -- fixed by
length-weighted anchors, an off-trend anchor filter and a 1.0 letters-per-token cap on the open-ended spans; with the cap at
1.4 the last five all-cipher bands read 1.35-1.45 letters per sign and the key degraded (C43 e/o/u), at 1.0 they read
0.98-1.03 and the key matches the other leaves. L23's crop was cut at the bottom edge (region height set 4 px short): the
brief's error, both readers flagged it, band excluded. Files: family/passes/f188r_*, recf188r/, f184r_*, f188r_spans.tsv
(per-band letters per sign, anchors, underline share), f188r_separate_stats.json.

**Calls and requests.** 8 Opus vision calls (about 125-130k subagent tokens each); Gallica 2 requests (native refetch of
canvases 351 and 343). Cost: the orchestrator's get_session figure is the record.

## Campaign step H31 (2026-09-28 02:2x UTC) -- fr.3983 f.106r at 3x: signs read, gloss HELD (F61-FAMILY-3)

First six cipher rows cut at 3x with family/cut_bands.py (hand-set centres; sheets/f106r, 42 crops), prompts on disk first.
Two blind Opus sign passes agree 204/240 = 85.0% (per band 0.76-0.92): the Mayenne-secretary hand reads at 3x, which
answers the H29/H35 question for the sign side. Two blind Opus gloss passes agree on 20 words of 58/60 = 33.9%, under the
brief's 60% gate: the leaf is HELD, nothing merged, the alignment run for the record only
(`family/key_period_f106_held.tsv`, 109 rows, 15 classes). The six rows carry none of CA, LOOPBAR, ZHOOK. 4 Opus vision
calls; Gallica 1 request (native refetch of canvas 191). Next cheap step (new CAMPAIGN row): a gloss-only recut around the
gloss rows at 4x, or a person's reading of the six glosses; the sign passes stand.

## Campaign step H33 (2026-09-28 02:4x UTC) -- context judge on the v3 skeleton: FAIL as pre-registered (F61-FAMILY-3)

The every-class condition failed (CA, LOOPBAR, ZHOOK, CROSS, LL uncovered by all three glossed hands), so H33 ran on the v3
skeleton in the H16 shape (`family/f61ctx.py`, prompt in family/passes/PROMPTS_f188_f184_f106.md written before the call,
key withheld, 20 permutations of the period letter sets across the covered classes, seeds as H16, unread signs shown as ?).
**Positive control** (six known span lines, Tomokiyo's letters withheld): the target set ranked 1st of 21 -- PASS on the
pre-registered rank gate, but by half a point (5.0 vs 4.5 for a permuted key) and the judge's resolved reading of the target
matched Tomokiyo's letters at only 14/34 (e.g. "arrestantpeines" for est ca-p-able): the wide v3 letter sets plus 20 ?
wildcards let the judge write plausible French under almost any key. **Target** (all nine lines, 99 signs): the target
ranked 2nd of 21 (4.5; a permuted key scored 7.0) -- FAIL. `family/f61_decode_period_v3_ctx.txt/.tsv` is written for the
record (C 10, C+ 4, M-ctx 65, I 20) and is NOT reading-ready: every M-ctx choice is unlicensed. Reading of the result: at
99 signs with 5 uncovered classes and 3-6-letter sets, a French-plausibility judge has no discriminating power (rule 3's
control-near-ceiling shape inverted: the control barely passes and its reading is wrong), so this method is logged
"untestable at this coverage", not a negative on the key -- the key itself reads the known spans at 0.782 vs 0.618 by the
DP test. Two Opus text calls (about 160k subagent tokens each). Next: cover the five classes (H43 shape sort; H42 more of
f.188r for LOOPBAR/CA if Desportes uses them further down; H41 f.106r gloss) before any further context pass.

## Campaign step H45 (2026-09-28 03:14-03:5x UTC) -- the "undeciphered" family leaves and the rare classes (F61-FAMILY-4, account 3)

Brief: `.claude/briefs/runs/2026-09-28-parent-f61-family-4.md` (its row id H41 was already F61-FAMILY-3's f.106r gloss recut, so the row is H45). Cap 45, box 150 min (to 05:42 UTC). Everything under `family/`; F61-FAMILY-3's files untouched.

**What the leaves are.** On the native Gallica images (2 requests this job, `family/requests.log`; Gallica now serves fr.3982 f.124r and f.97r with a different byte stream than at 00:42 -- sha1 8b7e91c7 vs 4d47de8c and 4ee0a5aa vs 87d4236c, same dimensions, a re-encode on their side) neither de Diou leaf is undeciphered: **fr.3982 f.124r** (headed "7 de Nove[mbre] 1592", de Diou to Mayenne) is interlined THROUGHOUT, 45 cipher rows each with the period decipherer's clear line above it, plus a clear opening sentence; **fr.3982 f.97r** (27 Oct 1592, to Jeannin) is interlined throughout as well, about 38 rows. The manifest's "partly interlined" / "none seen" came from the 1200-px thumbnail looks. fr.3984 f.186r and f.189r (Desportes) are not re-examined here (not fetched, not cut: no budget beside f.124r).

**f.124r signs (done).** Region 950,1250,3450,4750 native; 45 cipher-row centres from a long-vertical-stroke profile of the left quarter (both ink-weight detectors lock onto the gloss rows here, as on f.101r), checked by eye on three debug strips, one missed row inserted (y 4392); `cut_bands.py --up 70 --down 55 --track 18`, 2x, five segments of 1520 x 250 px (s5 1300), sheets/f124r (225 crops, 21 MB, not committed; `sheets/f124r_bands.json` and one sample are; regen line in MANIFEST.tsv). Prompts in `passes/PROMPTS_undec.md` (written before the first call; the f.101r atlas unchanged), per-call files `passes/prompts_f4/`, generated by `gen_prompts_f4.py`. Two blind Opus sign passes per chunk of 8 bands, 6 chunks, 12 calls: `undec_pipeline.py f124r` -> **2387/2839 aligned columns identical = 84.1%** (per band 0.70-0.94; L08 at 0.696 is the one band at the 70% line, not re-cut: its two passes differ on VBAR_A/EBR splits, not on a crop defect), draft `passes/recf124r/ciphertext_draft.tsv`, 2,839 signs. One crop defect found by both readers: `--track 18` drifted one row at s5 on L27-L30 (the rows rise faster than 18 px per segment there); those four s5 crops are held out of the leaf decode (`passes/f124r_drop.tsv`), not settled by a third look.

**f.124r gloss (HELD).** Two blind Opus gloss passes on the 2x bands for chunks 1-2 (4 calls) agreed on 49% and 43% of words; the disagreements are real misreads of a cramped secretary gloss, not spelling ("dissention la ra grand provision" vs "desmouuoir a ce quil gouuerne"). Chunk 3 re-run on a gloss-centred 3x recut (sheets/f124g, the H41 f.106r recipe, up 34 / down 30 native around the gloss row; template added to PROMPTS_undec.md before the call; 2 calls): 36% by word, 64% by letter, both readers mostly '?' -- no better (the image reader downsizes a 2280-px crop to 2000 anyway). Chunks 4-6 gloss not run (6 calls saved; the material would enter a held file). Under the family's 60% gate the leaf's gloss is HELD: `family/key_period_f124_held.tsv` (172 rows, agreed-word tokens only, flat -- top-letter share 0.205), nothing merged. Two things established on the way: (1) the shared aligner in `--code-prefix` mode cannot take OTHER as a word code, and on this hand OTHER IS the word-code sign ("que", "Monsieur", "m'" on L01): `align_period.py --numeral-other` (OTHER = 200, above the Thurloe floor) and `--wild-disagree` (a word the passes disagree on enters as `?` wildcards, evidence for nothing) were added, off by default, other leaves' outputs unchanged; (2) **band L01, whose gloss the passes agree on at 82%, reads cleanly under key_period_v3 with no refit** -- "auant" = C43 LOOPS C43 C43 VBAR_A, "la lettre" = EBR_B C43 EBR_B PHI VBAR_A VBAR_A PHI PHI, "escrite" = PHI VBAR_B 4STEM PHI H24 VBAR_A PHI, "luy aye este rendue" = EBR_B LOOPS EBR_B / C43 EBR_B PHI / PHI VBAR_B VBAR_A PHI / PHI PHI C43 4STEM LOOPS PHI (numeral-mode alignment of L01 alone: PHI e 10 r 3, C43 a 8 n 2, VBAR_A t 7 s 2, EBR_B l 3 y 2, LOOPS u 3 v 2, OTHER que 2 monsieur 1). So the family key applies to de Diou's hand and the leaf is a letter-by-letter interlinear decipherment with word codes; what is held is the gloss READING, and the fix is a recipe that reads this gloss hand (H46), not another sign pass.

**f.124r under v3 (`decode_leaf_period.py f124r --key key_period_v3.tsv --drop passes/f124r_drop.tsv`, `family/f124r_decode_period_v3.txt`):** 2,782 signs (after the drop), covered 0.939, firm (C/C+) 0.061 -- C 6, C+ 163, M 2,444, unread 169 (CA 1, ZHOOK 1, LOOPBAR 3, CROSS 3, OTHER 151 = word codes, the rest CH/ISH/LOOPSTEM1/ELOOP). A skeleton, not a reading.

**Rare classes (step 3): positive control FAIL, target not run.** `family/rare_classes.py` gathers every occurrence of CA/LOOPBAR/ZHOOK/CROSS/LL across six leaves (78; f.124r adds 8 -- de Diou's hand does not write them either) with four neighbours a side rendered under v3 (`family/rare_contexts.tsv`). Rule 3 first: three covered classes hidden (HASH4 d/q, BETA m, INF u), shown as X1..X3 among 20 re-dealt sets to one blind Opus text judge (prompt on disk before the call, key and names withheld): true set rank 13 of 21, INF's u missed, proposals 'd,l,v' / 'l,d,m' / 'd,l,m' -- the judge cannot tell a real class from a random deal at this coverage, because v3 leaves 0-1 firm neighbours per context. The target call was not spent; `family/rare_classes.tsv` records the control and no proposal; HYPOTHESES.md row: untestable by context inference at this coverage (H33's limit, met from the class side).

**Merge / tests / reading-ready (steps 4-5): no v4.** Nothing cleared a gate (f.124r gloss held, no rare-class rows), so no `key_period_v4.tsv` is written -- a v4 identical to v3 would only mislead; the newest key stays v3: f.61 known spans 43/55 = 0.782 vs permuted mean 0.372 / max 0.618, f.108r 66/84 = 0.786 vs 0.344 / 0.512, f.61 coverage 0.80, uncovered CA CROSS LL LOOPBAR ZHOOK (`test_period_key.py --key key_period_v3.tsv --collapse-ebr --min 2 --frac 0.1 --check`: fresh). NOT reading-ready (every-class condition fails, unchanged); F61-FAMILY-3's line stands, no second decode.

**Calls and cost.** 19 subagent calls (18 Opus vision: 12 sign, 6 gloss; 1 Opus text), 2 Gallica requests; own estimate about USD 33 (18 x 1.43 at F61-FAMILY-2's ledger rate + the text call + this session's own reading of debug strips); the orchestrator's get_session figure is the record.

**Left undone (rows H46-H48):** f.124r gloss with a recipe for this hand; f.97r the f.124r way (native on disk, regen line in MANIFEST.tsv; the stroke detector found 38 rows with 4-5 missed at gaps of about 200 px -- hand-check before cutting); f.186r/f.189r sign passes (Desportes, genuinely undeciphered).

## Campaign step H44 (2026-09-28 04:40 UTC) -- PUBLISHED-CHECK of the five uncovered classes

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV, replacing session_01UgTmQhR7wFtVFrTVdtsq9i), script-only, no
calls, no network. Hypothesis H44 (the orchestrator's 02:43 row): the five sign classes of f.61r with no period reading
(CA, LOOPBAR, ZHOOK, CROSS, LL; family/KEY.md) looked up in the one PUBLISHED source on disk -- Tomokiyo's reconstructed
table (`keys/key_mayenne_1592.tsv` from `mayenne.png`) and his own interlinear markup of f.61 (`scripts/tomokiyo_spans.tsv`)
-- written as `published` pairs to a separate file, never merged into `key_period_*`. Script `scripts/f61published.py`
(pre-registered gate in its docstring, `--check` fresh), result `scripts/f61published_result.txt`, pairs
`family/key_published_rare.tsv`.

**What the published source says, per class** (three facts each: the F61-CAL reader's drawing label in
`read_call_A.tsv`, Tomokiyo's markup letters over the class's positions per `class_diag.tsv` and the DP, the runner's
own reading of the two shape descriptions):

| class | f.61 signs (spans) | reader's drawing label | Tomokiyo's markup | table drawing of the same construction | published value |
|---|---|---|---|---|---|
| ZHOOK | 3 (L07/3, L07/11, L11/11) | S02 = n (x3) | **j, i, i** | none (the i/x drawing is a knot over a crossed bar, grade ? in the key file) | **i/x** (his letters; the cell partner x unattested) |
| CROSS | 2 (L01/1, L07/10) | S01 = a (x2) | dash, dash | **row a**: "cross/plus with a short diagonal rising to the upper right" = the atlas's CROSS | **conflict**: the drawing says a (or the a/n cell), his own markup leaves both signs unread |
| CA | 7 in the spans, 10 on the leaf | ? | dashes only | none is a cursive a | null |
| LOOPBAR | 3 (+1 on L04) | ? | dashes only by eye (H4's DP rule 2/3) | none (que and pour are other constructions) | null |
| LL | 1 (L05/16) | ? | dash | none | null |

So the published source reads ONE of the five classes, ZHOOK, and it does so from the leaf itself (his own partial
decode, "Solution Incomplete", grade M as a reading) rather than from a drawing: the reader's drawing match (S02 = n) is
one of F61-CAL's eight consistent mislabels, and the table has no 7/Z-hook glyph at all. Three of the five are nulls in
his reading, which is what H4's dash-share rule and `class_diag.tsv` already had.

**Test (rule 3, pre-registered).** `key_period_v3.tsv` under `test_period_key.py`'s own filter (`--collapse-ebr --min 2
--frac 0.1`, re-implemented and checked: K0 reproduces 43/55 and 66/84 with the same permuted mean and max) plus the
published pairs, 20 keys with the letter sets permuted across classes (seed 1):

| key | f.61 known 55 | permuted mean / max | f.108r overlay 84 | permuted mean / max | f.61 covered |
|---|---|---|---|---|---|
| K0 v3 | 43/55 = 0.782 | 0.372 / 0.618 | 66/84 = 0.786 | 0.344 / 0.512 | 0.80 |
| **K1 v3 + ZHOOK i/x** | 45/55 = 0.818 (2 of the 3 ZHOOK letters are the reference itself: circular; 43/53 without them) | 0.381 / 0.618 | **71/84 = 0.845** | 0.345 / **0.560** | 0.84 |
| K2 K1 + CROSS a/n | 45/55 | 0.332 / 0.473 | 71/84 | 0.335 / 0.452 | 0.87 |
| K3 K1 + CROSS a | 45/55 | 0.326 / 0.473 | 71/84 | 0.332 / 0.452 | 0.87 |

**Gate (f.108r only, the non-circular leaf): PASS** -- ZHOOK i/x raises f.108r from 66 to 71 of 84 and the result stays
above every permuted key (max 47/84). The seven ZHOOK signs of f.108r's two overlaid lines carry i, i, j, i, i, j, i in
Tomokiyo's overlay, which reprints the leaf's own period interlinear decipherment (H19) -- so the ZHOOK = i/x pair is
published (Tomokiyo, 10 of 10 positions over the two leaves) and, at one remove, period (the f.108r gloss, not yet read by
us: H21 failed on the runner's crop, H34 is the recut). CROSS adds nothing on either leaf (absent from f.108r's two lines;
under dashes on f.61) and stays a recorded conflict, unused. CA, LOOPBAR, LL: published nulls, no drawing, no test possible.

**What this changes.** (1) ZHOOK is not a gap in the key, it is a gap in the period *sources on disk*: the sign is written
by Mayenne's own secretary (f.61 3, f.108r 7, f.108v 20 in `family/rare_contexts.tsv`) and by no other hand of the family
(f.101r 3, f.124r 1, f.188r 0), whose i/x sign is the readers' H24 ("2 joined to a crossed 4", i 170 on f.101r) -- the
same cell, most likely the same glyph coded twice across atlases (the H43/H22-style blind sort would test it). The one
period source that writes ZHOOK and has a readable gloss is f.108r, so **H34 (the f.108r gloss with the family recipe)
moves from rank 8 to rank 3**: it is the step that turns ZHOOK = i from `published` into `period` grade C and adds the
d/q, m/z and word-code cells with counts. (2) The held f.108v alignment (`key_period_held.tsv`, passes at 65%) reads ZHOOK
a 7 / e 4 / u 4 -- against i at 10 of 10 published positions; H35 (the corrected f.108v re-run) now carries that as its
named check. (3) A decode of f.61r under v3 + ZHOOK i/x is `mixed` (period + published for that class) and is not run
here: the skeleton's C count would rise by three tokens and nothing else changes. (4) No class change; nothing here is a
reading, solved, new or first; the words are Tomokiyo's and the period decipherer's.

Files: `scripts/f61published.py`, `scripts/f61published_result.txt`, `family/key_published_rare.tsv` (a new file in
family/, as the row asked; no family file edited). HYPOTHESES.md row added. Requests: none. Vision calls: 0 of 4. No
credentials, no AskUserQuestion, no novelty wording; the owner not named.

## Campaign step H34 (2026-09-28 04:54 UTC) -- FAIL as pre-registered: the f.108r gloss with the family cut; the readers, not the cut, are the limit

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV). Four Opus vision calls (two gloss passes, two sign passes; about
108-112k subagent tokens each, 94-117 s), prompts in `scripts/PROMPTS.md` before the calls; 2 Gallica requests, both refused
(a 503 after two minutes, then an empty reply on the one permitted retry; `images/requests_h34.log`), so the cut is on the
720-px region already on disk. Hypothesis H34 (F61-GLOSS2): H21 again with `family/cut_bands.py` -- a band per cipher row
with the gloss riding above it.

**Cut (`images/f108g/`, regen stanza in `images/regen_f61r_sheets.sh`).** Six cipher rows (centres 198, 294, 411, 504, 618,
712 in region y; L03 is the clear main-line sentence with a few signs at its end, L04/L05 mix clear clauses and cipher, L06
is cut through its lower half by the region's bottom edge -- stated in both prompts), `--up 72 --down 34 --local 20 --seg 960
--overlap 80 --scale 3.0`: 24 crops of 2880 x 318 px, no duplicate files (the H29 defect), gloss inside every band except
L01's, whose gloss sits 66 px above its row and is clipped at the top edge (both gloss readers said so).

**Passes (verbatim: `scripts/gloss108gA.tsv`, `gloss108gB.tsv`, `pass108gA_classes.tsv`, `pass108gB_classes.tsv`).**
Signs: both passes 192 rows, identical per-band counts (L01 39, L02 43 -- the same counts as H19's two passes on the other
cut -- L03 16, L04 32, L05 25/26, L06 36/37), `tools/reconcile_passes.py` (nw) 156/197 = **79.2%** identical (family gate
0.80: missed by one column; L06 all at confidence l). Gloss: A 45 / B 44 gloss words, 31 in both passes = **0.697** by word
(family gate 0.50: met), and both readers agree on the same ZHOOK-rich bands.

**Scoring (`scripts/f61gloss.py --tag h34`, the x-placement rule pre-registered in the script and pushed 992f4506 before
any output was read; `f61gloss_h34_result.txt`, `f61gloss_h34_counts.tsv`).** Each reconciled gloss word matched by x
position to the signs under it in each sign pass (39 words, 84 signs each pass), aligned per word, a pair counted at the
minimum of the two passes' counts. Min-count key: PHI e:5 d:3 t:2; OTHER o:3 u:2; C43 e:2 c:1; INF u:3 n:1; ZHOOK t:1 s:1
i:1; nothing else above 1. **Nine cells: 0 of 9 agree** (PHI's top letter e is the one right answer; C43 e/c, INF u/n,
VBAR_A n/e are not the cells); new material: none. **GATE H21: FAIL.**

**Why -- the known-answer check that the agreement gate cannot make.** Bands L01 and L02 are the two lines Tomokiyo's
overlay reprints from this very gloss (`scripts/tomokiyo_spans_3983.tsv`), so their gloss is known. Against it the two
Opus readers score **11/32 = 0.344** exact words (A: L01 2/7 "satisfaire en que au faueur plaisir", L02 3/9 "amitie qui
sans preiudice a grands de seurete incommoditez"; B: 3/7, 3/9) -- the true words being "satisfaire ung seul au
preiudice de plusieurs" and "aultres qui me prenent a garent de leurs iacommoditez". The readers agree with each other on
wrong words ("amitie", "sans", "preiudice", "grands") as often as on right ones, so a two-pass word-agreement figure of
0.70 measures a shared failure mode, not correctness -- the rule-3 shape of two passes that are not independent on the
axis that matters. At 0.344 on the known bands, the unknown bands' words (L04-L06, about 25 gloss words: "misere", "Je me
retourne/ressouuiens", "quinze mois", "peu on voulu seiourne pleur") license nothing, and the leaf stays **HELD**: no key
row is offered, `f61gloss_h34_counts.tsv` is for the record only.

**What this establishes.** Three units of Mayenne's secretary's gloss have now been read by the same instrument -- f.106r
(H31, 33.9% agreement), f.108v (H29 non-test; H35 pending) and f.108r (this step, 0.697 agreement but 0.344 known-answer
accuracy) -- and de Diou's by F61-FAMILY-4 (42%): an Opus vision read of this cramped secretary gloss at 3x is the limit,
not the crop (CLAUDE.md rule 3's "unchanged approach" paragraph). The f.108r gloss is short (about 40 words on the six
rows, 16 of them already known from the reprint) and the leaf is on Gallica at native zoom: a person's reading of the
remaining 25 words is a ten-minute desk task that would turn ZHOOK and the d/q, m/z and word-code cells into period grade
C -- filed as ASKS row 88 and CAMPAIGN.md row H50 (`needs: person`); H35 is re-ranked down and re-scoped to its sign passes.
The sign side is fine: the four passes on L01/L02 now on disk (two cuts, four independent reads, identical counts) are
the material for a reconciled draft of those two lines whenever a key needs it. Not a reading; no class change; nothing
solved, new or first; no credentials, no AskUserQuestion; the owner not named.

Files: `images/f108g/` (bands.json, debug overlay and, since the close of this runner, all 24 crops committed as the H34 pass inputs, 3.3 MB; regenerable by the stanza), `images/requests_h34.log`,
`images/regen_f61r_sheets.sh` (stanza), `scripts/PROMPTS.md` (H34 sections), `scripts/gloss108gA/B.tsv`,
`scripts/pass108gA/B_classes.tsv`, `scripts/f61gloss.py` (--tag/--gloss/--signs/--bands options, the H21 default byte-identical),
`scripts/f61gloss_h34_result.txt`, `scripts/f61gloss_h34_counts.tsv`; HYPOTHESES.md row added. Vision calls: 4 of 4.

## Campaign step H49 (2026-09-28 04:57 UTC) -- null test of the uncovered classes: untestable at this n

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV), script-only, no calls, no network. Hypothesis H49 (F61-NULLTEST):
do CA, LOOPBAR, LL (and CROSS, ZHOOK) behave as nulls in the family's period alignments, as Tomokiyo's dashes say (H44)?
`scripts/f61nulltest.py` (verdict rule pre-registered in its docstring; `f61nulltest_result.txt`, `--check` fresh).

**Design.** Per class, on `family/key_period_v3.tsv`'s rows: top-2 letter share and normalised entropy of the lettered
tokens, dash share of all tokens. Controls subsampled to the class's OWN lettered count n (rule 3, the ARM3-ADJ lesson):
15 covered classes with 30+ lettered tokens, 2000 multinomial draws of n tokens each (the cell band), and a null model of
2000 draws from the pooled letters of those classes (what a sign that takes a random neighbour's letter looks like under
this aligner). Verdict 'null-like' only below every cell control's p05 and inside the null band; 'cell-like' only above the
null's p95 and inside every cell band; else untestable.

| class | v3 tokens (dash) | lettered n | letters | top-2 share | null model at n (p05 / median / p95), P(null >= obs) | cleanest cells' p05 at n (C43, EBR_B, INF, VBAR_B) | verdict |
|---|---|---|---|---|---|---|---|
| CA | 9 (2) | 7 | c 2, s 2, q, t, p | 0.57 | 0.29 / 0.43 / 0.71, **0.44** | 0.71 (reader-merged cells 4STEM 0.29, EBR_A 0.43) | **untestable at n=7** |
| LOOPBAR | 2 (0) | 2 | e, u | | | | untestable (n < 7) |
| LL | 1 | 1 | e | | | | untestable |
| CROSS | 1 | 1 | p | | | | untestable |
| ZHOOK | 3 | 3 | a, e, r | | | | untestable (its i/x reading rests on f.61/f.108r, H44) |

**Result: untestable at this n, as the rule says.** CA's seven letters are what the null model produces at its median
(P = 0.44) and fall below the 5th percentile of the four cleanest cells (C43, EBR_B, INF, VBAR_B at 0.71), but the
reader-merged classes (4STEM, EBR_A, 4PI, HASH4, ZBAR) reach that low a top-2 share at n = 7 themselves, so the
pre-registered 'below every cell control' condition is not met and no verdict is licensed either way. The three glossed
hands write CA 9 times in 3,000 aligned tokens: the test would need about 30 tokens, which only f.61r's own hand supplies
(10 CA signs on one leaf) -- i.e. the period alignments cannot settle the null question for this letter's hand; Tomokiyo's
dashes (H44) remain the only published statement on it, and H4's dash-share rule the only working one. No class change;
no reading; nothing new or first. Files: `scripts/f61nulltest.py`, `f61nulltest_result.txt`; HYPOTHESES.md row added.

## Campaign step H26 (2026-09-28 05:08 UTC) -- PASS: the loop family is three glyphs; the side-by-side pair is b/o, the audit's 'qo' signs are b/o

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV). One Opus vision call (about 134k subagent tokens, 157 s), prompt in
`scripts/PROMPTS.md` (H26) and scorer `scripts/f61qo.py` (the H22 design) pushed dc1b693a before the call; no network.
Hypothesis H26 (F61-QO): audit 1's question -- the atlas folds every loops-on-a-stem sign into PHI (e/r) except the stacked
o-T-o form (DBL, b/o); on L10 the verifier saw a two-loops-SIDE-BY-SIDE form at positions 6 and 11, coded PHI, that pass 1
itself had flagged 'could be DBL-like'. Is the loop family more than one glyph, and where does the side-by-side form go?

**Design, pre-registered.** Expected positions from disk: the PHI and DBL signs of the six span lines (`passA_classes.tsv`),
of L10 (`read_call_U.tsv`) and of f.108r bands L02/L03 (the reconciled draft) -- 45 signs on nine sheets B, 39 under a
Tomokiyo letter (e/r 33, b/o 6) by the joint cell map's DP. One blind sort into 2-4 shape groups, no letters shown; pairing
per sheet in reading order, a sheet with a count mismatch dropped; statistic = best group-to-cell match; null = 2000 label
permutations (C(38,6) = 2.76M arrangements, above the exact threshold), plus the 200-permutation p95. Gate: above p95, p < 0.05.

**Output (`scripts/read_call_QO.tsv`, verbatim).** 46 signs, three groups, its criterion: "G1 has a third loop sitting above
two side-by-side loops with the stem running up through the cluster (trefoil); G2 has only two loops side by side hanging
either side of the stem head, with nothing above; G3 has two loops stacked one above the other as a figure-8, with the stem
leaving from the bottom loop (seen only on f108)." f.61 L03 listed 3 against 2 expected (dropped by the rule); every other
sheet reconciled.

**Result (`scripts/f61qo_result.txt`).** Scored 38 labelled positions (e/r 32, b/o 6), three groups: **38/38**, permutation
P(>= obs) = 0.0000 over 2000 (seed 1), p95 32/38 -- **PASS**. Group by cell: G1 trefoil = e/r 26/26 (both leaves); **G2
side-by-side = b/o 6/6** -- the three f.61 signs the atlas had as DBL (L05/5 o, L08/5 b, L11/10 o) AND three signs the
readers had coded PHI (f.61 L07/7 under o; f.108 L03/35 and L03/38 under o); G3 stacked figure-8 = e/r 5/5 (f.108 only:
L02/15, L03/6, L03/15, L03/22, L03/42, every one under e). So the atlas's DBL wording ("two loops on a stem, one above the
other, o-T-o") named the wrong glyph: the b/o sign of this cipher is the two loops SIDE BY SIDE at the stem head; the stacked
pair is an e/r variant of the trefoil. **L10 positions 6 and 11 are both G2** -- b/o, not e/r.

**Consequences.** (1) The held L10 fragment (audit 1, AUDIT.md): its cells at positions 6 and 11 change from PHI e/r (audit
grade M) to side-by-side b/o (grade S with this control), so the letter sequence is [l/y][e/r][g/t][e/r][b/o][f/s][h/u][b/o]
and the judge's string 'le tresur' is withdrawn by the solver; a solver-side revision paragraph is appended to AUDIT.md (rule
10's propagation requirement), the class stays the verifier's. H51 re-derives `fragment_L10.tsv` and the joint fit with the
split (script-only). (2) The period key: family/KEY.md already notes "PHI e 507, r 189, o 145 -- o = DBL (b/o) merged into PHI
by the readers" on f.101r; this call shows which glyph carries the o (side by side), so a family pass that codes the
side-by-side form apart from the trefoil turns PHI's e/r/o triple into two cells on every leaf -- the largest single
ambiguity in every decode so far (family row H52). (3) `scripts/f61_atlas.tsv` gains a row SBS (two loops side by side at
the head of a stem, nothing above) with the H26 note; passes before this date used PHI/DBL. No class change; not a reading;
nothing here is solved, new or first (the letters are Tomokiyo's and the period decipherer's). Vision calls: 1 of 4.

## Campaign step H51 (2026-09-28 05:10 UTC) -- the H26 split applied on disk; the L10 fragment regenerated

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV), script-only, no calls. Hypothesis H51 (F61-QO2): apply H26's
groups through the joint fit and regenerate the fragment of record.

**Joint fit with the loop split (`scripts/f61qo2.py`, pre-registered in its docstring; `f61joint_h51_result.txt`,
`f61joint_h51_map.tsv`).** Relabel before the fit: every H26 group-G2 sign and every pass-A DBL on f.61 -> SBS; G1/G3 stay
PHI; then H27's bracket relabel. Same folds, permutations (seed 1) and gate as H20/H27, the gated cells now ten with SBS in
place of DBL.

| fold | H27 (bracket split only) | H51 (+ loop split) | permuted max (H51) |
|---|---|---|---|
| (a) fit f.61, read f.108 | 57/84 = 0.679 | **59/84 = 0.702** | 0.405 |
| (b) fit f.108, read f.61 | 41/55 = 0.745 | **46/55 = 0.836** | 0.400 |
| (c) f.61 span folds pooled, f.108 in training | 48/55 = 0.873 | **49/55 = 0.891** | per fold 0.50-0.75 |
| gated cells | ten, no conflict | PHI e/r 33 of 34 counts (the o's are gone), SBS b/o 7/7, no conflict; FAIL only on the absence rule (VBAR_B, EBR_A missing from one fold's training) | |

Both transfer folds rise; PHI is now a clean e/r cell (33/34 counts) and SBS a clean b/o one (7/7). The absence rule fails
as in H20/H27 and is not re-litigated. Grades unchanged (M: the reference letters are Tomokiyo's and the period
decipherer's, reprinted).

**Fragment (`scripts/f61fragment.py`, `fragment_L10.tsv` regenerated, `--check` fresh; the pre-H51 file is in git history
at 310c85e5).** Positions 6 and 11 are SBS b/o (cell grade S with H26's control), their letter within the pair unresolved
(the H16 judge chose within e/r; withdrawn). Pair sequence of the run after "pas paresseux si": **[l/y] [e/r] [g/t] [e/r]
[b/o] [f/s] [h/u] [b/o]**, five nulls between and after. No reading is claimed; the fragment stays held with the verifier
(AUDIT.md's solver-side paragraph, H26). For H25: the judge's candidate sets carry the old cell for L07/7 (a reader PHI that
H26 puts in the b/o group) and for L10 6/11 -- H25 rebuilds its sets with the split, stated before its calls.

Files: `scripts/f61qo2.py`, `f61joint_h51_result.txt`, `f61joint_h51_map.tsv`, `scripts/f61fragment.py`,
`scripts/fragment_L10.tsv`; HYPOTHESES.md row added. No class change; nothing solved, new or first.
## Campaign step H46 (2026-09-28 04:32-05:0x UTC) -- de Diou's gloss hand, a letter-aligned recipe, HELD after its own control (F61-FAMILY-5)

Parent worker F61-FAMILY-5 (Fable, session_015tVb7hadE1VHpChmm1nEYK, cap 45, box 150 min), owner account, working in
family/ only. Both natives regenerated once (2 Gallica requests, family/requests.log; f.124r sha1 8b7e91c7 as the 03:15
fetch, f.97r 87d4236c as the 00:xx fetch -- Gallica's byte stream alternates between two encodes, same dimensions).

**Recipe (brief step 1).** The gloss on f.124r is a letter-by-letter interlinear decipherment (H45: L01 reads cleanly under
v3), so it was read as letters aligned to signs, not as words: `family/cut_segments.py` cuts each coded band into segments of
8 signs at 3x (cipher centre - 82 / + 42 native px, chosen after three segments were looked at by this session), with a
numbered red tick under every sign's x (recovered per draft position from pass A, or B where A has a gap), and writes the
v3 skeleton per segment (`family/f124r_decode_period_v3.tsv`) with 40% (control) / 30% (target) of the covered positions
HIDDEN as `?` so a reader cannot tell a hidden covered position from an uncovered one. Two blind Opus passes per chunk,
prompts in `family/passes/PROMPTS_f124r_gloss.md` written before every call (exact texts `family/passes/prompts_f5/`),
reconciled by `tools/reconcile_passes.py` (nw) per (segment, position); scored by `family/score_letters.py` /
`family/place_letters.py` on the hidden positions (in the v3 set or not), the shown positions and A-vs-B agreement.

**Positive control (pre-registered gate 0.8 on the hidden positions; chunk c0 = 8 segments of L01-L02 whose classes
are all covered, 32 hidden positions, 2 calls per form):**

| form | hidden in set: A / B / A = B | shown in set: A / B | A vs B |
|---|---|---|---|
| letter per tick (62 rows per pass) | 12/32 = 0.375 / 10/32 = 0.312 / 9/23 = 0.391 | 15/28 = 0.536 / 0.536 | 34/51 positions |
| word + tick span, letters placed by DP (the one knob change; 27 / 26 rows) | 14/32 = 0.438 / 12/32 = 0.375 / 11/20 = 0.550 | 16/28 = 0.571 / 14/28 = 0.500 | words 10/25 = 0.400 |

FAIL both forms. The readers agree with each other on 40% of words, H45's 42% again, and even where the answer set is
shown they pass at 0.5-0.57: the gloss is written compactly, one word over a span of signs, not a letter per sign
(`family/sheets/f124s/f124s_L01_g8.jpg`: "tisfaict" over four struck signs, then a dash; own look), and the words
themselves are read differently by two readers at 3x with the signs ticked ("?rie"/"?ue", "estr"/"astr", "fin ss?r"/"tiu sse
d?"). Per the brief (one knob, then hold): no target gloss call on f.124r's 45 rows, none on f.97r; no key rows from de
Diou's gloss; `key_period_f124_held.tsv` stands; no `key_period_f124.tsv`, no `key_period_f97.tsv`, no v4 (brief steps 3-4
not reached, the every-class condition unchanged); v3 stands at 511 pairs / 24 classes, known spans 0.782 vs permuted max
0.618, f.108r 0.786 vs 0.512, f.61 coverage 0.80. The pass files are kept for the record and used by nothing
(`family/passes/f124s_letters*_c0.tsv`, `f124s_words*_c0.tsv`, `f124s_placed_c0.tsv`, `recf124s_c0/`). Calls: 4 (all
vision). Untestable [by blind model readers at 2x-3x] on this hand, not refuted: what would settle it is a known answer --
a person's reading of six f.124r rows (H46 option b) against which a reader's word list is scored before any further
call, or a period gloss in a clearer hand for the same signs; not a further pass at the same segments (CLAUDE.md rule 3).

## Campaign step H47 (2026-09-28 04:4x-05:2x UTC) -- fr.3982 f.97r: signs read on de Diou's second leaf, gloss not read (F61-FAMILY-5)

Same worker as H46. **Cut.** 42 cipher rows between native y 621 and 5031 (region 880,560,3450,4540). The first cut
(`cut_bands.py`, ink-weight centres plus three hand inserts, `--track 18`, sheets/f97r, bands.json committed) let the
rising-then-falling rows drift out of the s3-s5 windows on the lower two thirds of the leaf (both readers of chunks 3-5
reported windows one row off and duplicate crops; the brief's error, not the readers'), so the leaf was recut by
`family/chain_rows.py` (rows detected per segment column from the ink-weight profile and chained by continuity, 43 bands,
two of them extrapolated phantoms) into sheets/f97r3 (bands.json, debug overlay and one sample committed; regen line in
MANIFEST.tsv), and the two bands the chain lost (L22, L31) were cut with hand-set per-segment centres (sheets/f97r4,
committed). **Passes.** Two blind Opus sign passes per chunk of 8 bands with the f.101r atlas unchanged (the f.124r sign
template with the leaf description swapped, `passes/PROMPTS_f124r_gloss.md` "f.97r sign passes"; exact texts
`passes/prompts_f5/`): chunks 1-2 on the first cut (L01-L16), chunks 3-7 on the recut (L17-L43; the first cut's chunk
3-5 files kept as `*_cut1.tsv`, superseded). Reconciled by `undec_pipeline.py` (a later chunk's rows replace an earlier
chunk's for the same band): **2,485 signs, 1,820/2,485 aligned columns identical = 73.2%** (L17-L32 of the recut 72-93%;
L01-L16 57-83%, the 4TRI/4STEM/C43 split of f.101r again; L34, L35, L38, L41, L43 under 70% where the chain still shared
a row between two bands -- `passes/f97r_drop.tsv` holds L35/L38/L43 s3-s5 out). One caveat on blindness: the chunk-3
pass-A reader reported that a concurrent pass overwrote its draft files in the shared scratchpad and rebuilt its rows
privately; the two passes of a chunk run at the same time, so this is logged as a possible leak between passes, not
ruled out. `passes/recf97r/ciphertext_draft.tsv`; inventory PHI 634, 4TRI 348, LOOPS 308, VBAR_A 233, H24 196, EBR_B 167,
4STEM 106, ZBAR 67, BETA 65, HASH4 63, VBAR_B 52, EBR_A 48.

**Under v3, no refit** (`decode_leaf_period.py f97r --key key_period_v3.tsv --frac 0.1 --drop passes/f97r_drop.tsv`,
`family/f97r_decode_period_v3.txt`): 2,424 signs, covered 0.970, firm 0.091 (C 7, C+ 214, M 2,130, unread 73) -- the same
polyphonic skeleton as f.124r (0.939) and f.61. **Rare classes on f.97r: 20 of 2,424 signs** -- CA 8, CROSS 7, LOOPBAR 3,
ZHOOK 1, LL 1 (`family/rare_contexts.tsv`, rebuilt by `rare_classes.py contexts` with f.97r added): de Diou's second leaf
does not write f.61's five uncovered classes either. Across every leaf read (f.61r, f.108r, f.101r, f.188r, f.108v, f.124r,
f.97r) the census is now 98 occurrences: CA 31, ZHOOK 35, CROSS 15, LOOPBAR 14, LL 3 -- on f.61r 20 of 99 signs, on every
other leaf 0.3-2%. **Gloss:** not read (H47's own condition, "gloss passes only with whichever H46 recipe clears 60%":
neither form did), so no `key_period_f97.tsv`, no v4, not reading-ready. Calls this job: 24 vision (4 gloss-recipe control,
20 sign passes), 0 text; Gallica 2 requests. Family folder size: the tracked family/ tree was 41 MB before this job (over
the 30 MB line already); this job adds about 3 MB (control segments, bands and samples), the 20 MB of f97r/f97r3 crops are
not committed (regen lines in MANIFEST.tsv). What would settle f.97r's gloss: the same known-answer control as f.124r
(H53). What the census says for the blocker: the five classes are f.61r's own, rare on every sibling (0.3-2%), so a period
gloss over them will come from f.61r-like density only on f.108r/f.108v (ZHOOK 27 there, gloss held at 3x) or from a shape
identification against the covered classes (H43), not from more de Diou leaves.

## Campaign step H25 (2026-09-28 05:25 UTC) -- the judge re-run audit 1 asked for: known lines PASS 3/3, the L10 run FAIL 3/3 under the corrected cells

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV). Six Opus TEXT calls (no images; about 89-113k subagent tokens
each), prompts verbatim in `scripts/PROMPTS.md` (H25: the H16 known-lines prompt unchanged, the H16 unmarked prompt written
out in full) before the calls; `scripts/f61judge.py` gained `--order-seed/--perm-seed` (a fresh set order and fresh cell
permutations per call) and `--h26-split` (the loop family split by H26: SBS = b/o, DBL out of the cell list), with every
H16 output byte-identical without the options. Hypothesis H25 (F61-JUDGE2): does the H16 judge reproduce as a gate when
its prompt is fixed on disk and the target's label, the permutations and the order are all re-drawn?

**Known lines (positive control), seeds 101 / 102 / 103 (`f61judge_known_s10x_{sets,key,verdict,result}`).**

| seed | target label | target score | next best | rank of 21 (ties against) | target's blind resolution |
|---|---|---|---|---|---|
| 101 | SET-05 | 7.0 | 2 | **1** | aupret / estpapnol / tropaunapers / ilousi / eaubeaupere / elentroit |
| 102 | SET-10 | 7.5 | 1 | **1** | auecet / estcapabl / tropaunapres / ilousi / eaubeaupere / elentroit |
| 103 | SET-06 | 8.0 | 2 | **1** | auecet / estpacnol / tropauancers / ilousi / eaubeaupere / elentroit |

**PASS as pre-registered** (rank 1 in all three; under the null the chance is 1/21 per call, about 1e-4 jointly). The
judge, with its prompt recorded and the key withheld, ranks the true cell map first every time and reads "eaubeaupere" and
"elentroit" blind in all three; audit 1's non-reproduction was the verifier's differently worded prompt, as the audit itself
suspected. The judge is a usable gate for this cipher at this N -- on a positive control.

**L10 (the unmarked run), same three seeds, sets built with the H26 split (positions 6 and 11 = [b/o]).**

| seed | target label | target score | best score (label) | rank of 21 | target's blind resolution of L10 |
|---|---|---|---|---|---|
| 101 | SET-05 | 1.5 | 1.5 (three tied) | 3 | letrosuo |
| 102 | SET-10 | 1.5 | 4 (SET-06 'yprcautn'), 3, 2.5, 2 | 7 | letrosuo |
| 103 | SET-06 | 1.5 | 2 (two sets) | 4 | leteosuo |

**FAIL in all three.** With the two side-by-side signs as b/o, the run [l/y][e/r][g/t][e/r][b/o][f/s][h/u][b/o] does not
resolve to French the judge recognises (its best attempt, 'letrosuo', scores 1.5, and it does no better than random
permutations), while the same judge separates the true map on the known lines by 5 points. So H16's L10 'PASS' (rank 1,
'letresur') was an artefact of the merged loop class rendering positions 6 and 11 as e/r; under the corrected cells the
run is a controlled negative: the eight cells (grade S) do not spell a French word by this judge. Possible reasons, each a
hypothesis and none tested here: the five 'nulls' of the run (CA x3, C6 x2, H4's dash-share rule from the known lines)
may carry letters in this run; the run may hold a name or a word code; the pair choice may need the clear words after
the line break (L11 begins the next line). The fragment stays held with the verifier, its cells S, its letters M, no
string proposed (`fragment_L10.tsv` as regenerated in H51 already claims none). The verdicts are verbatim on disk.

**Cost.** Six Opus text calls; the row's est (3) priced them at about half the ledger rate -- about 7 USD spent (own
estimate; the orchestrator's get_session figure is the record). No class change; nothing solved, new or first; no
credentials, no AskUserQuestion; the owner not named.

## Campaign step H24 (2026-09-28 05:33 UTC) -- FAIL as pre-registered (a non-test): four of nine sheets did not reconcile

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV). One Opus vision call (about 129k subagent tokens, 132 s), prompt in
`scripts/PROMPTS.md` (H24) and scorer `scripts/f61an.py` pushed 68d3742c before the call; no network. Hypothesis H24
(F61-AN-SORT): the table's two a/n symbols -- does a blind sort of the 4-shaped signs (C43, 4STEM, C6, LOOPBAR) separate the
a positions from the n positions (32 expected signs, 18 labelled C43/4STEM: a 13, n 5)?

**Output (`scripts/read_call_AN.tsv`, verbatim).** 36 signs in four groups: A "a closed 6-figure with no 4-element" (10),
B "a 4 with a 3-like curl joined low on its right" (the 43; 20), C "a lone 4 on a long stem usually crossed by a second
bar" (3), D "a single small loop on a stem with a bar at its foot" (4). It excluded four f.108 "4 over two stems with two
crossbars" signs as the hash/pi family.

**Result (`scripts/f61an_result.txt`).** Reconciled sheets: f.61 L01, L03, L08, L11, L10 (counts match); NOT reconciled and
dropped by the rule: f.61 L05 (expected 4, listed 5: the reader's D at segment 1 is pass A's LOOPSTEM1, a class the expected
list did not carry), L07 (2 vs 3: a "43 cut on the segment 3/4 boundary" where pass A has no C43), f.108 L02 (4 vs 5) and
L03 (7 vs 8). Only 5 labelled positions survive (a 4, n 1), all in group B: **non-test** (exact P = 1.0 over 5
arrangements). **FAIL as pre-registered.** Four of the five n labels sit on the dropped f.108 sheets, so nothing is
licensed either way about a versus n.

**What the call does show, ungated.** Every "43" the reader saw on both leaves went into ONE group (B, 20 signs, including
f.61 L11/5 under n and the f.108 C43 signs under n on the dropped sheets): at this resolution the reader does not see two
43 glyphs. That is an observation, not a verdict; the H13-H15 precedent (a count-mismatched first call, then a
pre-registered re-run with the class scope fixed) is the route: H24b restricts the sort to the 43 glyph alone (18 expected
C43 signs, labels a 13 / n 5), excludes the 6-figures, loops and lone 4s explicitly, and asks for x positions so a
mismatch can be diagnosed -- a re-run with one pre-registered fix, not a third try of the same call. Not a reading; no class
change; nothing solved, new or first. Vision calls: 1 of 4.

## Campaign step H24b (2026-09-28 05:38 UTC) -- FAIL: the reader sorts the 43 glyph by hand, not by letter; a/n logged untestable by this instrument

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV). One Opus vision call (about 114k subagent tokens, 98 s), prompt
in `scripts/PROMPTS.md` (H24b) and the scorer's scope (`scripts/f61an.py --c43-only`) pushed 59fb2d77 before the call.
Hypothesis H24b (F61-AN-SORT2): H24 with its scope fixed -- the 43 glyph alone (17 expected signs, labels a 10 / n 5),
exclusions named with counts, x positions required.

**Output (`scripts/read_call_AN2.tsv`, verbatim).** 20 signs in three groups, and its own criterion says what they are:
A = the f.61 hand (a large two-bowled 3 joined high, on a 45-degree 4: all 9 f.61 signs), B = the f.108 hand (a steeper 4
with a small 3 hanging low: 8 signs), C = "the f108 form with the curl reduced to a faint single hook" (3 signs, flagged
uncertain) -- which are the draft's 4STEM signs at f.108 L02 pos 2 and 7 (pass 108A x 1283 and 2417 in segment 1, the
reader's x 1280 and 2420), i.e. the readers' existing C43/4STEM split, not a new one.

**Result (`scripts/f61an_c43_result.txt`).** f.61 sheets reconciled 5/5 (9 signs, 7 labelled: a 6, n 1, all group A); f.108
L02 (2 expected, 4 listed) and L03 (6 vs 7) dropped again. One group over the scored positions: 6/7, exact P = 1.0.
**FAIL.** With two calls of the same instrument -- the first sweeping in neighbouring classes, the second, with the
scope fixed, separating the hands and the readers' own class boundary instead of the letters -- the a/n question is logged
**untestable by a blind shape sort at this resolution** (CLAUDE.md rule 3's unchanged-approach paragraph): not refuted,
not re-briefed on the same sheets. H23's finding stands: the polyphony of the a/n cell is genuine at the reader's class
level, and the table's two a/n drawings do not correspond to a shape difference a model reader sees at 3x. What would
test it: a person's eye on the 17 signs against the table's two drawings, or native crops of each sign side by side in
one image (a different instrument), neither briefed here. Not a reading; no class change; nothing solved, new or first.
Vision calls: 1 of 4.

## Campaign step H57 (2026-09-28 05:47 UTC) -- FAIL: the context judge's positive control is below its gate on the corrected skeleton; the full leaf not run

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV). One Opus TEXT call (the positive control only; the full-leaf call
was not spent, per the control-first rule), prompt in `scripts/PROMPTS.md` (H57: the H33 prompt verbatim) and the sets
pushed 61fdb59a before the call. Hypothesis H57 (F61-CTX2, the parent's row): the H33 design on the CORRECTED skeleton --
`family/f61ctx.py --h26-split --published-zhook` (defaults unchanged, H33's outputs byte-identical): f.61's side-by-side
signs as their own SBS b/o cell, PHI e/r on this leaf, ZHOOK i/x from `family/key_published_rare.tsv` (published), every
other class its v3 period letter set (n >= 2, 10% rule), uncovered classes as ?.

**Positive control (`family/passes/f61ctx_known2_{sets,key,verdict}`, `f61ctx.py score known2`).** Target SET-13 scored 1.5;
best set 2.5, then 2, 2, and eight sets at 1.5: **rank 11 of 21, FAIL** (H33's control had ranked 1st by half a point). The
judge's resolution of the target ("deauecreesia | eerestaneceenos | setroneeauaenceers | ...") is not Tomokiyo's text at any
line. The full-leaf set (`f61ctx_full2_*`, built, on disk) was NOT judged.

**Why, and what it settles.** The same judge, the same known lines, the same session window: with the nine f.61-fitted cells
and the nulls dropped (H25) it ranks the true map first by 5 points three times out of three; with the period key's letter
sets -- 4STEM n/a/c/e, 4TRI n/a/c/p, EBR l/s/a, OTHER seven letters, 4PI four -- and ? wildcards for the uncovered classes,
it cannot tell the true map from a permutation. The width of the sets, inherited from the family readers' merged classes on
other hands, is what removes the judge's power, not the judge and not the corrected cells (H33's near-miss was the same
thing). So the context route on the period-key skeleton is closed at this coverage, as the row said a FAIL would do; the
context route that works is the f.61-fitted cell map (H25), which has already been run on every line of f.61 that has
cipher (the five spans: known; L10: FAIL 3/3; L02: one sign). H56 (the L10 nulls as wildcards) is dropped on the same
ground: a judge set with three ? positions in an eight-letter run is the H33/H57 shape and would fail its own control by
construction (rule 3's "a control that cannot vary" paragraph, from the judge's side). Not a reading; no class change;
nothing solved, new or first. Text calls: 1 of 2.

## Campaign step H35 (2026-09-28 05:53 UTC) -- FAIL: f.108v sign passes on the corrected cut agree 52%; the cut still misplaces L01 s1

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV). Two Opus vision calls (about 123k subagent tokens each, 189 s),
prompt in `scripts/PROMPTS.md` (H35), scorer `scripts/f61v3x.py --prefix f108v3y --signs-only` (the H29 output unchanged)
pushed 64233590 before the calls; no network. Hypothesis H35 (F61-108V3Y, re-scoped at H34 to the sign passes only): do two
blind sign passes on the corrected f.108v cut (`family/sheets/f108v3y_*`, 28 crops, no duplicates) agree at 0.80?

**Passes (verbatim, `family/passes/f108v3y_signsA.tsv`, `_signsB.tsv`).** A 297 rows (9 PLAIN, 17 low-confidence OTHER
including 10 vertical strokes it took for separators and 5 end-of-line dashes), B 303 (no PLAIN, 8 vertical strokes as
OTHER). `tools/reconcile_passes.py` (nw) over the seven bands: **163/312 = 52.2% identical columns** (H29's defective cut:
72.8%; the family's first cut: 65.2%). **GATE FAIL.** The reconciled draft is written to `family/passes/f108v3y_draft.tsv`
for the record only (inventory PHI 63, C43 44, VBAR_A 35, 4STEM 27, OTHER 26, ZHOOK 20, EBR_A 19, HASH4 16, INF 15, SBS 14,
EBR_B 14, BETA 11, ISH 7, CROSS 1; ZHOOK 2/1/4/2/3/5/3 per band): not a transcription, no key, nothing merged.

**Why.** (1) The cut, again: reader B reports that L01 segment 1 is cut about one row too high (its middle shows the gloss
"et tant ... faudra qu", and B read those 12 signs off the top edge of L02 s1 instead) and that L02 s1's cipher row sits
cut at the bottom edge; reader A coded L01 s1 as five PLAIN clear words -- the same segment. The per-segment `--local 30`
re-centring locked onto the gloss row on the first segment of the first two bands; the previous runner's corrected cut was
checked for duplicate files, not for this. (2) The readers split the loop and bracket families differently (PHI / DBL / SBS
now that the atlas has SBS; INF / DBL; VBAR_A / EBR_A) -- both say so -- and one lists vertical strokes and dashes as OTHER
where the other does not, so the NW alignment pays for extra columns throughout. This is the third unit of Mayenne's
secretary's hand read by two passes at 3x (f.106r 85% signs but gloss 34%; f.108r 79%; f.108v 52%): the sign agreement on
this leaf is the worst of the family, and a fourth pass of the same shape is not the next step (CLAUDE.md rule 3's unchanged-
approach paragraph). The H29/H35 cut error is logged as the runner's (this runner inherited and did not re-check it).

**Next (new rows).** H59: a targeted recut of L01/L02 segment 1 with hand-set centres and ONE reconciliation call restricted
to the draft's disagreement columns with crops (Usage 6's priced reconciliation step) -- the reconciler route, not a third
blind pass; gate <= 10% flagged columns, else f.108v is logged untestable at 3x by two-pass agreement. Not a reading; no class
change; nothing solved, new or first. Vision calls: 2 of 4.

## Campaign step H58 (2026-09-28 05:54 UTC) -- the f.61r skeleton under the corrected cells (for the verifier and the person rows)

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV), script-only, no calls. `scripts/f61skeleton.py` -> `scripts/f61_skeleton.txt`
(`--check` fresh). One file with every sign of the leaf (99: pass A's six span lines with the VBAR split, pass U2's L02/L04/L10;
L06/L09 carry no cipher), relabelled by H26 (SBS) and H22 (EBR_A/EBR_B/ISH), each token one of: `T:x` (Tomokiyo's own markup
letter on his five spans -- his tentative reading, grade M as a reading, the reference of every control: 54 placed by the DP),
`[x/y]` (the class's cell from the H51 joint map, grade M; SBS b/o from H26; ZHOOK i/x also published: 15 positions, no letter
chosen), `-` (a null: a class his markup dashes at every f.61 position, H44 -- CA, LOOPBAR, LL, CROSS, ELOOP, HASH4, LOOPSTEM1,
CH, C6: 28), `?` (OTHER on L02/L04: 2). The L10 run reads as in `fragment_L10.tsv`. Not a reading of the letter: outside the
five spans the leaf carries 15 two-way choices and nothing chooses them (H25 and H57 closed the judge routes; the cells
themselves are M). What it is for: the verifier's one-page view of the state, and the person-reading rows (ASKS 88, H50/H53) --
a person who reads the f.108r gloss gives the same cells period grade C and, with the SBS split, PHI e/r and SBS b/o on every
leaf. No class change; nothing solved, new or first.

[Correction 2026-09-28 05:55 UTC: the counts above were first written from a run before C6 joined the null set; the committed file reads 54 T / 15 pairs / 28 nulls / 2 unread, as `--check` confirms.]

## Campaign step H60 (2026-09-28 05:56 UTC) -- the desk pack for ASKS 88 (f.108r gloss rows L04-L06)

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV), script-only, no calls. `images/person_pack/`: one contact sheet per
row (`f108r_L01.jpg` as the worked example with its known gloss, `f108r_L04.jpg`, `f108r_L05.jpg`, `f108r_L06.jpg`; 1.9 MB
in all) -- the H34 3x crops stacked with a numbered sign strip beneath each segment (pass A's sign order; PLAIN words named)
-- and `README.md` with the paste-ready TSV template (`line, word, first_sign, last_sign, note`), so a person's ten-minute
reading comes back positionally aligned to the signs and `scripts/f61gloss.py --tag h50` scores it unchanged. ASKS row 88's
exact action now names the pack. Checked by eye on `f108r_L04.jpg`: the gloss ("La misere ... on Je me retourne ... dargent")
is legible, the numbers sit under their signs. Nothing here reads the cipher; no class change.

## Campaign step H59 (2026-09-28 06:09 UTC) -- f.108v by the reconciler route: PASS on its gate (3.2% still flagged), a grade-M transcription, not a key

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV). Three Opus vision calls (two small re-reads of the recut segment,
about 87k subagent tokens each; one reconciliation call, about 174k, 365 s), prompts in `scripts/PROMPTS.md` (H59, two
sections) and the task file pushed before each call; no network. Hypothesis H59 (F61-108V-RECON): the reconciler route
(Usage item 6's priced reconciliation step) instead of a third blind pass.

**Cut defect confirmed and fixed.** On `family/sheets/f108v3y_bands_debug.jpg` the segment-1 centre of band L01 sits on the
clear line above the row (y 63 in region coordinates; the cipher row is at 128, plain-ink 277 vs 53) and L02 s1 leaves its
row at the bottom edge (189 vs 217): the `--local 30` per-segment search jumped to the heavier clear line on the first
segment. Both recut with hand-set centres (`family/sheets/f108v3z_L01_s1.jpg`, `_L02_s1.jpg`, `f108v3z_bands.json`); the
other 26 segments were not questioned by either reader and stand. Two blind re-reads of the two crops (`passes/
f108v3z_s1_signsA/B.tsv`): 13 and 11 signs in both. Merged into the H35 passes (`f108v3z_signsA/B.tsv`, old s2 rows inside
the overlap dropped, positions renumbered): agreement **179/315 = 56.8%** (from 52.2%) -- the cut was a small part of the
gap; the readers' coding of PHI/DBL/SBS, INF/DBL and VBAR_A/EBR_A, and B's separator strokes, is the rest.

**Reconciliation (`passes/f108v3z_recon_task.tsv`: the NW draft, 136 columns to settle = 123 differ + 13 gap; the 117
agree-flagged columns are agreed and were not the reconciler's).** One Opus call with the 28 crops settled all 136
(`f108v3z_recon_verdict.tsv`, verbatim): h 29 / m 96 / l 11 by the file (the call's own count line says 24/91/10), none 11
(7 end-of-line dashes, 2 separator strokes, 2 alignment duplicates: it noticed NW column shifts in L03 7-13, L04 1-2 and
48-49, L06 22-25 and 45-46, L07 45-46 and placed each sign by x). `scripts/f61recon108v.py` (gate pre-registered in its
docstring, `--check` fresh): **still flagged 10/315 = 0.032, GATE PASS**; `passes/f108v3z_draft_reconciled.tsv`, 304
columns: PHI 64, C43 41, EBR_A 37, 4STEM 25, **ZHOOK 20**, VBAR_A 18, INF 17, HASH4 14, OTHER 13, SBS 13, EBR_B 12, BETA 11,
ISH 10, 4TRI 6, CA/CROSS/LOOPBAR 1 each.

**What it is.** A sign transcription of the seven rows of f.108v with every disagreement settled by one reconciler from the
crops: grade M on the 136 settled columns and on the 117 agreed-at-low-confidence ones, H only on the 62 columns both passes
gave confidently -- a transcription a person's gloss reading can be aligned to (the leaf carries a sparse period gloss, the
one that read ZHOOK a 7 / e 4 / u 4 in the held f108vg alignment, against i at 10/10 published positions), not a key and not
a reading; nothing is merged into `key_period_*`. Rule 3 caveat: a reconciler is one more Opus eye on the same 3x crops --
the same instrument that agrees with itself at 57% -- so the 10% gate measures how often it was unsure, not how often it
was right; no known-answer control exists for this leaf's signs (Tomokiyo reprints none of its lines). Not solved, new or
first. Vision calls: 3 of 4. Cost: about 3.5 USD (two small calls, one large) against est 3.

## Campaign step H61 (2026-09-28 06:10 UTC) -- the desk pack for f.108v's sparse gloss (ASKS row 89)

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV), script-only, no calls. `images/person_pack_108v/`: seven contact
sheets (`f108v_L01.jpg` .. `f108v_L07.jpg`: the f108v3y crops, the f108v3z recut for L01/L02 segment 1, with pass A's sign
numbers beneath each segment, PLAIN words named) and `README.md` with the TSV template; ASKS row 89 filed. The person's
reading is scored by the H34 x-placement scorer against pass A's positions (the same file the numbers come from). Nothing
here reads the cipher; no class change.

## Campaign step H62 (2026-09-28 06:11 UTC) -- the f.108v skeleton under the corrected cells

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV), script-only. `scripts/f61skeleton.py --leaf f108v` ->
`scripts/f108v_skeleton.txt` (`--check` fresh; the f.61 output unchanged). On the H59 reconciled draft (304 signs: sign grades
H 62, M 217, L 25) with the H51 cells, SBS b/o and ZHOOK i/x (published): 274 pair positions (no letter chosen), 17 nulls, 13
unread (OTHER, ISH), coverage 0.96. Every covered sign of this leaf is a two-way choice: the leaf has no Tomokiyo letters and
its gloss is unread by any model (ASKS 89 is the person route), so nothing here is a reading and no letter is proposed. What
the file shows the verifier and the desk: which rows a person's gloss reading would settle first (L01: 44 signs with 42
covered), and that the hand's inventory is f.61's (VBAR_A/EBR_A/4TRI/INF/SBS/ZHOOK). No class change; nothing solved, new or
first.

## Campaign step H63 (2026-09-28 06:19 UTC) -- the CA signs inside the runs are in the cipher hand; the edge ones may be text

Campaign runner (Fable, session_01J8hunWPcE7QYcpCx59CUHV). One Opus vision call (about 105k subagent tokens, 42 s), prompt in
`scripts/PROMPTS.md` (H63) and scorer `scripts/f61ca.py` (verdict rule pre-registered) pushed 35b171fb before the call.
Hypothesis H63 (F61-CA-HAND): are f.61's ten CA signs (Tomokiyo's nulls, H44) cipher signs at all, or letters of the clear
text at the run edges?

**Output (`scripts/read_call_CA.tsv`, verbatim).** 12 a-shaped marks in or at the cipher runs and 10 control a's from the
clear words (all 10 judged text, as required). Its verdicts split by position, not by sheet: every a INSIDE a run "same
size, pen weight and spacing as the signs, on their baseline, not joined" = cipher (8 of 12), every a at a run EDGE (after
"Cambrey", before "le...", after "sont", after "ni mesme") = text at low-to-moderate confidence (4 of 12).

**Result (`scripts/f61ca_result.txt`).** Reconciled sheets L01, L07, L08, L10 (6 CA positions): cipher 5, text 1 (L07/1,
pass A's own "a-shape; run-break", the run's first sign); L03 and L05 listed one extra a each (an edge a pass A did not
code) and were dropped by the rule. Control 10/10 text. **Verdict as pre-registered: CA = cipher signs; Tomokiyo's nulls
stand** -- with the qualification the call itself supplies: the CA signs pass A placed at run starts or ends (L03/1, L05/7,
L07/1) are the ones a reader takes for the text's own "a", and whether they are counted as a null sign or as the clear
word "a" changes no cell and no letter of any reading (a null and an unread text letter render the same). The skeleton
(H58) keeps them as nulls. No class change; nothing solved, new or first. Vision calls: 1 of 4.

## Campaign step H65 (28 Sept 2026, 14:19-14:28 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

Question: is H26's two-loops-side-by-side glyph (SBS, b/o on f.61r and f.108r by our fit only) the glyph under which the
period decipherers of the family leaves write o, i.e. does the period gloss itself separate it from the e/r trefoil PHI?

Design (pre-registered, pushed 9c78f3f8 before the call; `scripts/f61sbs.py`, prompt in `scripts/PROMPTS.md` "H65"):
every PHI token of `family/passes/{f101r,f274,f188r}_align.tsv` whose aligned period letter is a single o or e, placed
by pass A's x (difflib match of the reconciled draft to pass A, A's own sign also PHI). Matched: f.101r 66 o / 220 e,
f.188r 20 o / 64 e, f.274 none (its align lines do not equal its draft). Sample (seed 65): f.101r 10 o + 10 e, f.188r
10 o + 10 e, 40 tiles cut from the native Gallica images (f.101r and f.188r fetched once each, 2 requests to
gallica.bnf.fr, kept in the scratchpad, not committed), re-centred on the local ink row, the period gloss row above cut
away so no letter is shown, shuffled, four contact sheets `images/h65/sbs_sheet1-4.jpg`; answer key
`scripts/f61sbs_tiles.tsv` never named to the reader. One blind Opus vision call (1 of 4), told only to describe and
sort the loop-on-stem sign between the ticks, no letters.

Result: the reader made two groups -- A "two loops side by side at line height, stem hangs from their junction, through
neither" and B "a loop raised above the line (phi-like) or a small top loop over a pair (trefoil), stem through it";
tile 24 marked none (the ticks fall on a long-s and a 4-like sign: an x error in the pass, not scored).

| group | period e | period o |
|---|---|---|
| A (side by side) | 1 | 18 |
| B (trefoil / phi) | 18 | 2 |

Scored 39 (e 19, o 20): observed 36/39, permutation P < 0.0005 (0 of 2000, seed 1), p95 26/39 -> **GATE H65 PASS**
(`scripts/f61sbs_result.txt`, `--check` OK). Per leaf, the two hands separately: f.101r 17/19 (A: o 9, e 1; B: e 8,
o 1), f.188r 19/20 (A: o 9; B: e 10, o 1). Balanced classes (19/20), so the blended figure is not a majority-class
artefact (rule 3's AX-NAMES lesson).

What it licenses: the period decipherers of two further hands write o under the side-by-side glyph and e under the
trefoil, so the SBS cell's o value rests on a period gloss (grade C for o), not only on our f.61/f.108r fit (H26/H51).
The b half of the b/o cell is NOT tested here (f.101r 13 and f.188r 8 PHI tokens carry a period b: H67). The
readers' PHI code on the family leaves is therefore two glyphs; the family key's PHI e/r/o triple is a coding merge,
and H52's per-leaf re-sort plus key rebuild (the family worker's row) now has a positive sampled test behind it. No
reading claimed, no class change; nothing here is solved, new or first. Three misses (tiles 6, 28, 40) are left as
they fell (alignment or x-placement noise, or a real variant): not re-read.

Reader's criterion verbatim: "in group A the two loops sit side by side at writing-line height and the stem hangs from
the point where they meet, without passing through either loop; in group B at least one loop rises above the line (a
phi-like loop or a small top loop over a pair, making a trefoil) and the stem runs up through the loop or cluster."
Group per tile in `scripts/read_call_SBS.tsv`.

## Campaign step H67 (28 Sept 2026, 14:29-14:33 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

The b half of the SBS b/o cell (H65 tested o only). Design pre-registered and pushed 4c057470 before the call
(`scripts/f61sbs.py build-b` / `score-b`, gate in `score_b`'s docstring, prompt `scripts/PROMPTS.md` "H67" = H65's with
file names and count changed): every PHI token under a period b matched to pass A (f.101r 8, f.188r 6) plus per leaf
as many e and o tokens (seed 67; some o/e tiles may repeat H65's, drawn from the same pool), 42 tiles
(`images/h67/sbsb_sheet1-5.jpg`, key `scripts/f61sbs_b_tiles.tsv`), one blind Opus vision call (1 of 4 this step).

The reader made three groups: A two loops side by side, stem from the junction; B the same pair with a bare ascender
through it; C a head loop stacked over a pair (the trefoil). Tile 28 none (tick on ruled strokes).

| group | b | e | o |
|---|---|---|---|
| A (side by side) | 11 | 3 | 12 |
| B (bare ascender) | 1 | 4 | 2 |
| C (head loop / trefoil) | 2 | 6 | 0 |

SBS group = A (o share 12/14 = 0.86, the anchor recovered); b 11/14 = 0.79 vs e 3/13 = 0.23, Fisher one-sided
P = 0.0056 -> **GATE H67 PASS** (`scripts/f61sbs_b_result.txt`, `--check` OK). Per leaf, b in A: f.101r 6/8, f.188r 5/6.
With H65: the period decipherers write both b and o under the side-by-side glyph and e under the trefoil; the SBS cell
b/o is period-attested at grade C on both halves, matching the table's own b/o cell. The reader's own B/C boundary
("B may be a lighter or less careful form of C") is not scored. No reading, no class change; nothing solved, new or first.

H68 dropped: its "prior" (period o vs b counts under SBS) would be French letter frequency (o about six times b) and
adds nothing a verifier does not already bring to L10 positions 6/11.

## Campaign step H69 (28 Sept 2026, 14:33-14:37 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

Is the readers' 4TRI class (atlas: "a 4-shaped element with a crossbar above a small triangle or V") one glyph, given
that the period gloss puts letters of two table cells under it (a/n and c/p)? Design pre-registered and pushed
959055ff before the call: `scripts/f61sbs.py build-pair NATIVE 4TRI a,n c,p 69 h69` (the H65 recipe generalised; pass A
must agree on 4TRI), 10 a/n + 10 c/p tokens per leaf (f.101r matched 161 a/n / 58 c/p, f.188r 14 / 21), 40 tiles
`images/h69/pair_sheet1-4.jpg`, key `scripts/f61pair_h69_tiles.tsv`; a 4-shape prompt (`scripts/PROMPTS.md` "H69"); one
blind Opus vision call. Four tiles none (f.101r x misplacements: empty space, a rule, an 8-like and a w-like sign).

| reader's group | a/n (set A) | c/p (set B) |
|---|---|---|
| A closed triangle on the stem below the crossbar | 2 | 18 (c 10, p 8) |
| B tall open hook from the crossbar end (f.188r only) | 9 | 0 |
| C open r/7 stroke beside the 4 (f.101r only) | 4 | 1 |
| D closed loop at crossbar height (f.101r only) | 2 | 0 |

Scored 36 (A 17, B 19): observed 33/36, permutation P < 0.0005 (0/2000), p95 24/36 (the p95 is taken over the reader's
own four groups, so the extra groups are paid for) -> **GATE PASS** (`scripts/f61pair_h69_result.txt`, `--check` OK).
Per leaf: f.188r 19/20, f.101r 14/16. What it licenses: the 4-over-triangle glyph is the c/p cell in both hands, as the
table draws it; the a/n tokens the family readers also coded 4TRI are a different, hand-specific 4-with-hook form
(f.188r a hook from the crossbar end; f.101r an r/7 stroke or a loop beside the 4) -- a reader merge like SBS, not
polyphony across two cells. The key's "4TRI n/a/c/p" wide set (H57's control failure named it) is two glyphs. Not
applied to any f.61 cell here (whether f.61's own 4TRI signs carry the triangle is a separate test: H72). No reading,
no class change; nothing solved, new or first.

Reader's criterion verbatim: "the groups split by where the right-hand element attaches and whether it closes: A has a
small closed triangle on the stem below the crossbar; B has a tall, mostly open hook hanging from the crossbar's right
end; C has an open r/7 stroke beside the 4 at crossbar height with nothing on the lower stem; D has a closed round loop
at crossbar height."

## Campaign step H70 (28 Sept 2026, 14:37-14:42 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

F61-CAL's open data conflict (the 'V with bar' class takes s and t, which the table splits across its f/s and g/t
columns) against a period gloss. Design pre-registered and pushed d9b432c7 before the call: `scripts/f61sbs.py
build-pair NATIVE VBAR_A s t 70 h70 20 --rc 20,-20,30` -- the f.101r readers' VBAR_A tokens under a period s (55
matched) or t (88), 20 + 20 (f.188r gives none: its readers already code s as VBAR_B), 40 tiles `images/h70/`, key
`scripts/f61pair_h70_tiles.tsv`; the re-centring window was narrowed after a first cut (looked at by the runner,
discarded, never shown to a reader) caught gloss rows; H65-H69's builds are unchanged (default window; H65 rebuilt
byte-identical). Triangle prompt in `scripts/PROMPTS.md` "H70"; one blind Opus vision call. Tile 15 none.

| reader's group | s | t |
|---|---|---|
| B second lower stroke from the point, running right (Z-like) | 14 | 4 |
| A short top bar only | 4 | 11 |
| C top bar only, drawn long past the right side | 1 | 5 |

Scored 39: observed 30/39, permutation P = 0.0025, p95 27/39 -> **GATE PASS** (`scripts/f61pair_h70_result.txt`,
`--check` OK); margin thinner than H65/H67/H69 (3 over p95). One hand only (f.101r). What it licenses: in f.101r's
hand the period decipherer writes s mostly under the triangle with a second stroke at its point and t under the
triangle with a top bar only -- the same A/B split H15 found on f.61 from Tomokiyo's letters (B = s, A = t, 7/7) and the
atlas's own VBAR_A/VBAR_B wording, which f.188r's readers applied and f.101r's merged. F61-CAL's s/t conflict reads as a
glyph merge by the readers, consistent with the table's two columns, now with a period-gloss attestation in one further
hand (grade C for the split on f.101r; f.61's own split stays at its H15 grade). Eight of 39 misfit (4 s under A, 4 t
under B), which a reader who draws the lower stroke faintly, or a gloss alignment slip, would produce. No reading, no
class change; nothing solved, new or first.

Reader's criterion verbatim: "group B has a second, lower horizontal stroke leaving the triangle's point and running
right (a Z-like form); group C has only a top bar, drawn long past the right side of the triangle; group A has only a
short top bar with no long rightward extension (the A/C boundary is a matter of degree and less secure than the B
distinction)."

## Campaign step H72 (28 Sept 2026, 14:42-14:44 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

The row asked for a vision sort of f.61's 4-shaped signs beside family anchors. The tally on disk answers it first
(`scripts/f61h72.py`, `f61h72_result.txt`, `--check` OK; Tomokiyo's letters placed by the joint cell map's DP, the
f61qo machinery): on f.61's span lines, L10 and f.108r L02/L03 our readers' 4TRI stands under c/p 10 of 10 lettered
positions (c 5, p 5) and their C43 + 4STEM under a/n 18 of 19 (a 13, n 5, one b). So f.61's own coding already
separates the 4-over-triangle (c/p) from the 43 (a/n), which is the split H69 found in the period gloss of two
further hands; nothing to re-sort, no call spent. The family readers' 4TRI a/n tokens (H69 groups B-D) correspond to
f.61's C43/4STEM, not to its 4TRI. This is a consistency tally on Tomokiyo's letters (grade H for the test), not a
reading; no class change.

## Campaign step H71 (28 Sept 2026, 14:44-14:46 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

PHI tokens under a period e vs under r, pre-registered and pushed de9a5a09 before the call (`build-pair NATIVE PHI e r
71 h71`, f.101r 10+10 and f.188r 10+10, the H65 prompt with the file names changed, `scripts/PROMPTS.md` "H71"). One
blind Opus vision call. The reader made two groups -- B "a third, smaller closed loop above the side-by-side pair (a
trefoil, or an 8-shape on one side)", A "only the two side-by-side loops" -- with three tiles none.

| reader's group | e | r |
|---|---|---|
| A (pair only) | 10 | 9 |
| B (third loop above) | 8 | 10 |

Scored 37: observed 20/37, permutation P = 0.757, p95 25/37 -> **GATE FAIL**, as the row expected
(`scripts/f61pair_h71_result.txt`, `--check` OK). The reader's own split partly follows the hand (A: f.188r 14 of
19; B: f.101r 12 of 18), not the letter.

Correction to the row's premise (mine): I framed e/r as "one table cell, true polyphony", which is Tomokiyo's prose
("e" and "r" share a symbol); the table transcription (`keys/key_mayenne_1592.tsv` header) draws two distinct symbols
in both the a/n and the e/r columns and one shared symbol in the other nine. So H71 is a negative on e vs r in these
two hands under a free shape sort -- the period decipherers' e and r do not fall under two glyphs this reader
separates -- and only a partial control for the method: it shows the sort does not align with letters when the
reader's groups are driven by something else (hand, the third loop), but the truth for e/r is not known to be one
glyph. The clean one-symbol control is the table's d/q column (H75). H65-H70 stand on their own permutation nulls.
No reading, no class change.

## Campaign step H73 (28 Sept 2026, 14:47-14:49 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

a vs n under the readers' C43 (the "43" glyph) on the family leaves, where the table draws a and n as two symbols and
H24/H24b's sorts on f.61/f.108r split the hands instead. Pre-registered and pushed 57ff9194 before the call:
`build-pair NATIVE C43 a n 73 h73` (f.101r 10+10, f.188r 9+9), 38 tiles, a 43-shape prompt (`scripts/PROMPTS.md`
"H73"), the statistic stratified by leaf (`score-pair ... --strat`: best match within each leaf, summed; labels permuted
within leaf) so a hand split cannot score. One blind Opus vision call; no tile none.

| reader's group | a | n |
|---|---|---|
| A 4 + open r/z/7 zigzag | 10 | 11 |
| B 4 + single closed bowl | 4 | 7 |
| C 4 + 3-like double curve | 5 | 1 |

Stratified observed 23/38, permutation P = 0.64, p95 26/38 -> **GATE FAIL** (`scripts/f61pair_h73_result.txt`,
`--check` OK). The reader's groups cut across both hands (its own note: "the ink ... cuts across all three groups") and
across a/n. In the two glossed hands the period decipherers write a and n under one 43 glyph that a free shape sort
does not separate; with H24b this is the second instrument on the question, so a vs n is logged untestable by a blind
shape sort (rule 3's two-attempt paragraph), and the table's two drawn a/n symbols stay unmatched to any hand. H74
(e vs r with the stratified statistic) is dropped by its own condition (skip if H73 FAILs). No reading, no class change.

## Campaign step H75 (28 Sept 2026, 14:50-14:52 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

The method's clean negative control: the table's d/q column is ONE shared symbol, so the period d and q under the
readers' HASH4 should not split. Pre-registered and pushed ebbf0de0 before the call: `build-pair NATIVE HASH4 d q 75
h75 20` (f.101r 15+15, f.188r 2+2), 34 tiles, a hash-4 prompt (`scripts/PROMPTS.md` "H75"), H73's leaf-stratified
statistic. One blind Opus vision call; tiles 15 and 33 none (x misplacements).

| reader's group | d | q |
|---|---|---|
| A 4 over a true hash (two stems, two bars) | 17 | 12 |
| B 4 over a single stem crossed by two bars | 0 | 3 |

Stratified observed 20/32, permutation P = 0.087, p95 20/32 -> **GATE FAIL**, as expected
(`scripts/f61pair_h75_result.txt`, `--check` OK). The three "double cross" tiles are all q, a minority variant not
significant at this n and left unexplained. With this, the tile sort has one clean one-symbol negative (H75) and two
free-sort negatives (H71 e/r, H73 a/n) beside its four PASSes (H65 SBS o, H67 SBS b, H69 4TRI c/p, H70 VBAR s/t, the last
thin): it does not manufacture a letter split on a shared-symbol cell, which is what the PASSes needed. No reading, no
class change.

## Campaign step H76 (28 Sept 2026, 14:54-14:55 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

For the verifier page (H66): `scripts/f61attest.py` (a sibling of f61skeleton.py rather than an option on it, so the
H58 skeleton is untouched; both `--check` fresh) tags every lettered or paired position of `scripts/f61_skeleton.txt`
by what its CELL rests on -- {P} both letters attested by a blind tile sort against the family period gloss (SBS b/o
H65/H67, 4TRI c/p H69), {P1:x} one letter (VBAR_A t, VBAR_B s, H70, one hand), {pub} published (ZHOOK), {K} both letters
in the period key's top 3 for the class on a leaf with n >= 5, {K1} one letter, {F} our f.61 fit only. Output
`scripts/f61_skeleton_attest.txt`: of 69 positions, P 13, P1 10, pub 3, K 39, K1 2, F 2; L10's 8 pairs: P 2 ([b/o] x2),
P1 2 ([g/t] t, [f/s] s), K 4 ([l/y], [e/r] x2, [h/u]). The tag grades the cell, not a letter choice within it, and
not Tomokiyo's letters (still grade M as a reading); the two F positions are his a and n on C6 signs, a class his own
markup elsewhere leaves as a dash (H44's null list). No reading, no class change.

## Campaign step H77 (28 Sept 2026, 14:55-14:58 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

The family readers' LOOPS class (their atlas: "a chain of two or more small loops written side by side with NO stem")
takes u 158 / o 31 / h 17 on f.101r. Pre-registered and pushed 911b7d48 before the call: `build-pair NATIVE LOOPS o u 77
h77 20 --rc 20,-10,35` (f.101r only: 20 o, all matched, and 20 of 105 u; f.188r has no LOOPS under o), 40 tiles, a
loop-chain prompt (`scripts/PROMPTS.md` "H77"). One blind Opus vision call; 8 tiles none (x/row misplacements, as the
pre-registration expected).

| reader's group | o | u |
|---|---|---|
| A three loops, a stem from under the middle junction ("oqo") | 14 | 1 |
| B loops crossed or joined by a horizontal bar, no stem | 0 | 15 |
| C plain loops, no stem or bar | 1 | 0 |
| D a tail from the last loop | 1 | 0 |

Scored 32: observed 31/32, permutation P < 0.0005 (0/2000), p95 22/32 -> **GATE PASS**
(`scripts/f61pair_h77_result.txt`, `--check` OK). One hand (f.101r). What it licenses: the f.101r readers' LOOPS class
is two glyphs, both matching atlas classes the f.61 and f.188r readers already keep apart -- under period o the
stemmed form (two loops side by side on a stem, with a neighbouring loop in the chain: the SBS glyph of H26/H65,
b/o), under period u the barred stemless pair (the INF sign, "an infinity sign or figure-8 lying on a horizontal
bar", h/u, which f.188r's readers code INF with u 23). So the family key's LOOPS u/o/h triple is a coding merge of
SBS and INF, not a further polyphony; for the family worker's key rebuild (H52), LOOPS-under-o joins the SBS
evidence (period o now attested in a third coding of the same glyph) and LOOPS-under-u joins INF. That the "oqo"
reading counts three loops (one of them the next sign) is the reader's framing; the stem from the junction is the
SBS mark. No reading, no class change; nothing solved, new or first.

Reader's criterion verbatim: "group A is three loops with a stem from under a junction ("oqo"); group B is loops
crossed or joined by a horizontal bar with no stem ("θθ-"); group C is plain loops with no stem or bar; group D is a
chain whose tail comes from its last loop."

## Campaign step H78 (28 Sept 2026, 14:59-15:00 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs) -- dropped, no call

4STEM c vs a/n on the family leaves: only 4 period-c tokens under 4STEM match pass A on f.101r (a 8, n 5; f.188r a 5, n
2, no c), 8 tiles at most against the row's pre-registered minimum of 18 scored. Untestable at this n by this recipe;
no vision call spent. (Match counts from `scripts/f61sbs.tokens`, the same filter every H65-H77 build used.)

## Campaign step H79 (28 Sept 2026, 15:01-15:03 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

f.101r's EBR_A under l/y vs under f/s (two table columns; f.61's readers keep EBR_A f/s apart from EBR_B l/y by H22).
Pre-registered and pushed 5da60743 before the call: `build-pair NATIVE EBR_A l,y f,s 79 h79 15 --rc 20,-10,35`, 24
tiles (12 + 12, every matched f/s token), a form-neutral prompt (the runner had seen several ticks fall on a barred
triangle), `score-pair --strat --min 18`. One blind Opus vision call; no tile none.

| reader's group | l/y | f/s |
|---|---|---|
| A bars joined by a diagonal (triangle / Sigma-E bracket) | 3 | 9 (s 7, f 2) |
| B upright with top and bottom bars, no diagonal (L / squared C) | 5 | 2 |
| C F-like, top and middle bars, stem below | 3 | 0 |
| D fits none | 1 | 1 |

Observed 18/24, permutation P = 0.0565, p95 18/24 -> **GATE FAIL** (observed equals p95; `scripts/f61pair_h79_result.txt`,
`--check` OK). The direction is the expected one (f/s mostly under the diagonal/triangle form, which is also the
VBAR_B s glyph of H70 and the atlas's EBR_A "hairline diagonal"; l/y mostly under forms without a diagonal, EBR_B's
squared C), but it does not clear its own gate, and every matched f/s token is already in the sample, so more tiles
cannot be drawn from f.101r. Logged as a near miss, untestable at this n by this recipe -- not a split and not a
negative. No reading, no class change.

## Campaign step H80 (28 Sept 2026, 15:04-15:06 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

Second clean one-symbol control: the table's g/t column is ONE shared symbol, so the period g and t under the top-bar
triangle (VBAR_A, the t glyph of H70) should not split. Tiles pushed 397a72c4 and the prompt 994bc22e, both before the
call (the prompt commit followed a failed assertion in my own script, not a change of design): `build-pair NATIVE
VBAR_A g t 80 h80 10 --rc 20,-20,30`, f.101r 10+10 and f.188r 1+1, 22 tiles, H70's prompt, `--strat --min 18`. One blind
Opus vision call; tiles 17 and 21 none (ticks on clear-text letters).

| reader's group | g | t |
|---|---|---|
| A plain barred triangle | 7 | 9 |
| B upturned hook at the bar's end | 1 | 1 |
| C vertical stroke crossing the bar | 0 | 1 |
| D second bar under the point (low confidence) | 1 | 0 |

Stratified observed 12/20, permutation P = 0.836, p95 14/20 -> **GATE FAIL**, as expected
(`scripts/f61pair_h80_result.txt`, `--check` OK). The tile method now has two clean one-symbol negatives (H75 d/q, H80
g/t) beside its PASSes (H65, H67, H69, H70, H77). No reading, no class change.

## Campaign step H81 (28 Sept 2026, 15:07-15:09 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

`scripts/f61splits.py` writes `scripts/f61_glyph_splits.tsv`, one row per blind tile-sort test H65-H80 (numbers parsed
from the committed result files, `--check` fresh; P 0.0000 means 0 of 2000 permutations): the family reader class, the
letter sets, the leaves, scored / observed / p95 / P / gate, the glyph each set went to, the f.61 atlas class that glyph
corresponds to, the table cell, and the kind (split, within-cell, control). Summary: five PASSes (H65 PHI o -> SBS, H67
PHI b -> SBS, H69 4TRI a/n -> hook forms vs c/p triangle, H70 VBAR_A s -> VBAR_B-like vs t, thin, H77 LOOPS o -> SBS vs
u -> INF), two within-cell FAILs (H71 e/r, H73 a/n), two clean one-symbol controls FAIL as expected (H75 d/q, H80 g/t),
one near miss (H79 EBR_A). For the family worker's key rebuild (H52) and the verifier page (H66). Not a reading.

## Campaign steps H82 and H83 (28 Sept 2026, 15:09 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs) -- dropped, no call

Both rested on the idea that narrowing H57's wide period-key letter sets with the tile-attested splits would give the
context judge back its power. Re-reading H57's own section: narrowed to their table cells, those sets ARE the
f.61-fitted cell map, and that map has already been judged on every f.61 line that carries cipher (H25: known lines
PASS 3/3, L10 FAIL 3/3). A rerun would be H25 again under another name (rule 3's same-instrument paragraph), and the
projection (H82) had no other consumer -- the family worker already has `scripts/f61_glyph_splits.tsv` (H81). No cost.

## Campaign step H84 (28 Sept 2026, 15:10-15:11 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

`scripts/H66_PAGE.md`: the runner side of the verifier's H66 -- audit 1's three asks and where each stands (judge
re-run H25; the "qo" form by our fit H26 and by the period gloss H65/H67/H77 with the H75/H80 controls; the
second-letter pair-choice test not yet done), the files with their `--check` commands (all fresh at 15:11), the counts a
verifier can re-derive, and the questions only the verifier or a person can close. No new claim, no reading, no class.
C6 checked on the way (the skeleton's null): settled as a null by the dash-share rule (5/6 under Tomokiyo's dashes) and
rare in the family gloss (3 tokens, e) -- no lead.

## Campaign step H52 (28 Sept 2026, 15:06-15:3x UTC, parent worker F61-FAMILY-6, session_01TPNoYGTE6dLBPfyEgZTLAc) -- key v4

Row H52 widened by the orchestrator's brief (`.claude/briefs/runs/2026-09-28-parent-f61-family-6.md`) to the four splits of
H65/H67, H69, H70 and H77. Full record in `family/KEY.md` "## v4"; the numbers:

- Re-coding: five blind Opus shape sorts (design pushed 58d4c7f0 before the calls, `family/recode_split.py`), the runner's
  H65-H77 tiles as labelled anchors, held-out anchors as the check. Held-out 1.00 on f.101r loops (8), f.101r 4TRI/4HOOK
  (4), f.188r loops (6), f.188r 4TRI/4HOOK (4); **f.101r VBAR_A/VBAR_B STOPPED** (held-out VBAR_B 1/2), so VBAR_A keeps its
  v3 rows. f.274r (no x positions) loses its merged-class rows. Recoded tokens: `family/passes/f101r_align_v4.tsv`,
  `f188r_align_v4.tsv`.
- Key v4 (`family/key_period_v4.tsv`, period): PHI e/r, SBS b/e/o (the e is the sort's misfit rate x stratum weight, kept as
  pre-registered), 4TRI c/p/t, 4HOOK a/n, INF u, VBAR_A s/t, VBAR_B s.
- Tests, no refit, 200 permuted keys: f.61 five spans **48/55 = 0.873** (v3 0.782; permuted p95 0.436, max 0.527, 0/200 at or
  above), f.108r 65/84 = 0.774 (v3 0.786), coverage 0.80 (unchanged; CA, CROSS, LL, LOOPBAR, ZHOOK).
- f.61r meter (`family/f61_decode_period_v4_frac0.1_sbs.txt`): **firm 20 / M 59 / unread 20** (v3 14 / 65 / 20); two-letter M
  sets 36 (v3 19). The six new firm signs are the INF signs (u, two leaves). 42 signs moved; table in KEY.md.

Brief step 5 condition met (known-letter test at least 0.782 and above every permuted key; firm count up): posted "reading
ready" in ROOM.md for the orchestrator, in its two-way form. Not a reading of the letter; no class change; nothing here is
solved, new or first.

## Campaign step H85 (28 Sept 2026, 15:12-15:26 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

Audit 1's third ask, a pair-choice test beyond the 13-sign L10, on the longest text in f.61's hand: fr.3983 f.108v's
reconciled draft (`family/passes/f108v3z_draft_reconciled.tsv`, H59, a grade-M transcription: two blind passes, 136
disagreement columns settled by one reconciliation call, 10 still flagged) under the 14 cells of its skeleton (H62: the
H51 map, n >= 2 both leaves, no tie, minus the skeleton's nulls), nulls and uncovered classes dropped. Builder and gates:
`scripts/f61judge108v.py` (docstring); prompts (H25's verbatim, only the file name and for f.108v the line list
changed) in `scripts/PROMPTS.md` "H85", pushed 66704c30 before any call.

**Positive control first** (the 14-cell set differs from H25's nine): one Opus text call on the five known span lines
(`f61judge_known_h51_s101_*`, 58 pair positions per set): target rank 1 of 21, 7.5 vs next 1.0; its resolution reads
"...tropaunapres | ... | enubeaupere | melentendoit" blind -> **PASS**.

**Target, three Opus text calls** (`f61judge_f108v_s10{1,2,3}_*`, 274 pair positions per set, fresh permutations and
order per seed; sets pushed 3d84b841 before the calls):

| seed | target score | next best | rank |
|---|---|---|---|
| 101 | 6.5 | 0.5 | 1 of 21 |
| 102 | 2.0 | 1.5 | 1 of 21 |
| 103 | 3.5 | 2.0 | 1 of 21 |

**GATE H85 PASS** as pre-registered (rank 1 of 21 in all three, ties against; `--check` fresh on every result). The
margins on seeds 102 and 103 are thin (0.5 and 1.5 points), and the scores themselves are low (2.0 to 6.5 of 10): the
judge finds the true cell map the most French-like of 21, not a clean text.

Consistency of the three independent resolutions of the target (`scripts/f61judge108v_agree.py`,
`f61judge108v_agree.txt`, reported, not gated): all seven lines the same length in all three; letters agreeing in all
three 184/274 = 0.672, pairwise 0.781 -- against 0.25 and 0.50 if each within-pair choice were a coin flip. (The script
also prints the best permutation of each call, 0/272, but that is not a fair floor: each call's permutations are
different maps.) Seed 101's resolution, verbatim, grade M at every letter (M transcription, M cell, choice by the judge):
"tctsepspurcnousaeusnuissionsmentresurloss | ecsacusanueonsasleulementuuolsouen |
iensaesseiuranlanonseruationenomilles | eullentesterreleuresetneinainallementaelle |
araneisaonnaraetitmesseitmmaisanertenaz | rialointzaussisontilzsersnenessairesatrez |
atilnyanyusananeraneraonteniraellelarssi" -- runs such as "seulement", "conseruation", "terre", "sont ilz",
"necessaires", "il n'y a" recur across the calls. Not a reading: no letter has been chosen by anything but the
judge, the transcription is grade M, and whether f.108v is already read in print has not been searched (a verifier's
job). What it licenses: the f.61-fitted cell map gives French-like text under a blind judge on 274 pair positions of a
second letter in the same hand, with the permuted-map control beaten three times out of three -- the kind of
second-letter support audit 1 said the L10 fragment lacked. For LANE VO3 / the orchestrator: H86-H87 do not depend on
this; a verifier pass on f.108v (print search, the resolution's word list against the reconciled draft's flagged
columns) is the next step it suggests (H88).

## Campaign step H86 (28 Sept 2026, 15:27 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs) -- answered from the passes, no call

The two unread signs of f.61r (`scripts/f61_skeleton.txt` '?') are already described by the U2 pass
(`scripts/passU2_classes.tsv`): L02 pos 2 "two thick vertical stems between a heavy top bar and a heavy bottom bar (Roman
II or pi with a double bar); no 4 above it, so not 4PI" -- no atlas class and no cell; L04 pos 2 "an S/8-like loop joined
to a b/d form, written after 'Come'; it may be a handwriting abbreviation (e.g. S.M.) rather than cipher" -- probably
clear text. A blind atlas-match call would re-ask what the reader already answered in the atlas's own terms; neither
sign joins a cell, so both stay unread in the skeleton. No cost.
## Web and blog check (CHECK-SOLVED-WEB, 28 Sept 2026)

Parent worker CHECK-SOLVED-WEB, 28 Sept 2026 15:23-15:27 UTC (clock-read; the Spinelli lesson). Known answer here is Tomokiyo's own
five interlinear spans on `BnFfr4715f61.png` (see "What Tomokiyo already reads"); a hit repeating only those is not new.
**Verdict: no reading of f.61 beyond Tomokiyo's spans found.**

| # | Query / page | Hits |
|---|---|---|
| 1 | `Mayenne polyphonic cipher BnF fr.4715 f.61 solved` | Bourdeau index + forks, Bourdeau issue #11 (Gramont, unrelated), Tomokiyo's MysteryTwister PDF, ciphermysteries.com home. The Bourdeau snippet about "Henri III's murder ... Nevers-Piles alphabet ... fr.4715 f.2" is the **Orbais / fr.3413 no.62** item, not f.61 (WebFetch of the arya1515 fork confirms: no f.61 entry). |
| 2 | `"jalousie au beau-pere" OR "jalousie au beau pere" Mayenne chiffre` (Tomokiyo's own distinctive span) | 0 relevant hits. |
| 3 | `duc de Mayenne 1592 lettre chiffrée déchiffrement Ligue chiffre polyphonique` | BnF finding-aid records fr.3641, fr.4715, fr.3623, fr.3362, fr.3974-3995, fr.4699, fr.4718; bibmath Viète page. No reading of f.61. **Key-hunt lead (not a reading):** the search summaries describe fr.3641 as holding a letter "avec chiffre et déchiffrement" on Mayenne's taking of Noyon, and fr.4699 letters "chiffrées avec déchiffrement" of Feb 1593 to Mayenne from P. de Fortia -- neither shelfmark appears in this folder; both archivesetmanuscrits records answered WebFetch 403 (one attempt each, not retried). Whether either is in the polyphonic cipher is unchecked. |
| 4 | `"fr.4715" OR "français 4715" chiffre Mayenne déchiffré` | noise only. |
| 5 | `cryptiana.blogspot.com polyphonic Mayenne Catholic League cipher` + WebFetch cryptiana.blogspot.com/2018 | "Unsolved ciphers in the French archives (ca.1586-1593)", 30 Nov 2018: "no.38 seems to be in an interesting polyphonic cipher but I'm not sure yet"; **0 comments**; no reading. |
| 6 | WebFetch mysterytwister.org mtc3-tomokiyo-02-polyphonic-01-en.pdf (Nov 2019) | a synthetic English challenge; cites `mayenne.htm` as ref [2]; no f.61 text. |
| 7 | `site:scienceblogs.de klausis-krypto-kolumne polyphon Mayenne OR "Katholische Liga" OR Tomokiyo polyphone` (Cipherbrain) | Madison 1780, Catinat 1702, Danish West Indies telegram -- nothing on f.61. |
| 8 | `site:ciphermysteries.com Mayenne OR "Catholic League" polyphonic cipher` | nothing on f.61. The Bourdeau snippet on Lebel -> Charles Emmanuel of Savoy 1593 read "with Tomokiyo's key" is the Savoy unit already on file (INTAKE-SAVOY, line 78). |

No flag raised. Only Tomokiyo's own spans are public. Not a novelty statement (rule 10); AUDIT.md untouched.

## Campaign step H87 (28 Sept 2026, 15:27-15:28 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

Why f.274 gave no tiles in H65-H80: its align lines equal its reconciled draft in length on every line (L01-L06: 26,
25, 28, 31, 29, 28) but not in content, because the align was built after a relabel of some HASH4 signs as H24 (e.g.
L02 pos 4, L04 pos 2, L05 pos 3), while `scripts/f61sbs.tokens` required exact equality. New opt-in flag `--len-match`
(off by default; H65 rebuilt byte-identical, every earlier result `--check` unaffected) accepts an equal-length line,
still requiring pass A to agree on the class at each position. With it, f.274 gives PHI e 24 / r 11 / o 7, 4TRI c 7 / p
3, VBAR_A s 11 / t 7 -- a third glossed hand for the SBS o test and a second hand for H70's thin s/t split (H89).

## Campaign step H89 (28 Sept 2026, 15:29-15:33 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

Third-hand replication of H65 (SBS o) and second-hand replication of H70 (VBAR s/t, thin on f.101r alone), on f.274's
glossed cipher (recovered by H87's `--len-match`). Pre-registered and pushed 240c7085 before the call: `scripts/f61sbs.py
build-h89` (seed 89; the window x +-25, y -60..+60 on ink darker than 80, fixed in the builder after three trial cuts
the runner looked at and discarded -- f.274's cipher hand is larger and heavier than its gloss), family P = PHI under
o 7 (all) + under e 7, family V = VBAR_A under s 7 + under t 7, 28 tiles in one shuffled run; each family scored alone
with an exact null (`score-h89`). One blind Opus vision call; tile 1 none (a numeral-like form).

| family | reader's group | letters |
|---|---|---|
| P | A flat row of 2-3 loops, stem hanging from below | o 7 |
| P | B stacked / trefoil loops, stem through the centre | e 7 |
| V | C barred triangle, top bar only | t 6 |
| V | D top bar plus a long second stroke at the point | s 7 |

P: 14/14, exact P = 0.0006 over 3432, p95 10/14 -> **GATE H89P PASS**. V: 13/13, exact P = 0.0006 over 1716, p95
10/13 -> **GATE H89V PASS** (`scripts/f61pair_h89_result.txt`, `--check` OK). With H65/H67/H77 the side-by-side glyph
carries period o (and b) in three glossed hands (f.101r, f.188r, f.274); with H70 the triangle with a second stroke
carries period s and the top-bar triangle t in two (f.101r, f.274) -- the VBAR_A/VBAR_B split H15 found on f.61 from
Tomokiyo's letters, now attested by two period decipherers. `scripts/f61_glyph_splits.tsv` gains rows H89P/H89V and
`scripts/f61_skeleton_attest.txt`'s tag text now names both hands (counts unchanged). No reading, no class change.

## Campaign step H90 (28 Sept 2026, 15:35-15:36 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

How reliable are the judge's WITHIN-PAIR letter choices, on which H85's f.108v resolutions rest? `scripts/f61judgeletters.py`
(result `scripts/f61judgeletters_result.txt`, `--check` fresh) scores the H85 control call's resolution of the five f.61
span lines against Tomokiyo's letters, placed exactly as the skeleton places them:

- target set: his letter lies inside the cell at 47 positions; the judge chose it at **43/47 = 0.915** (one-sided
  binomial P vs 0.5 = 1.4e-09); 5 positions have his letter outside the cell.
- best permutation set (a floor): 16/20 = 0.80 at the 20 positions where the permuted cell happens to contain his letter.

Two caveats, both lowering what the 0.915 licenses: (1) the floor shows much of the accuracy is the judge's
French-frequency prior at the pair level (it picks the commoner letter), not sentence context; (2) the H16/H25 prompt,
reused verbatim by H85, gives "beau-pere" as a spelling example, and "beaupere" is one of Tomokiyo's own words on these
lines, so the known-lines figure is inflated for that span (the f.108v calls carry the same example word but no reason
to contain it). Applied to f.108v: a letter chosen by the judge is right well above chance where the cell is right, but
H85's resolutions stay grade M and not a reading. For the verifier page (H92). No reading, no class change.

## Campaign step H91 (28 Sept 2026, 15:36-15:37 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

`scripts/f108v_consensus.py` -> `scripts/f108v_consensus.txt` (`--check` fresh), for the verifier's H88: the
position-by-position majority of the three H85 target resolutions of f.108v, UPPER CASE where all three calls agree
(184 of 274) and lower case where two do (90), with the draft's sign grade under each letter (12 positions sit on signs
still flagged L after reconciliation). Grade M at every letter; not a reading; no word boundaries asserted. The
verifier's print search (is this letter's text already known?) and any class are H88's, not the runner's.

## Campaign step H92 (28 Sept 2026, 15:37 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

`scripts/H66_PAGE.md` brought up to date for LANE VO3: audit 1's third ask now points at H85 (f.108v judge gate 3/3
after its control) with the H90 calibration and its caveats, the H91 consensus file and the open print search H88;
the "qo" item gains H89 (third hand) and the two-hand V-with-bar split; the file table gains the H85/H90/H91 files. No
new claim.


## Campaign step H93 (28 Sept 2026, 15:38-15:39 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

A model-free check of H85 with a matched null (gate pre-registered in the CAMPAIGN.md row before scoring):
`scripts/f61judge_ngram.py` scores every set's resolution in each judge verdict with `tools/judge_plaintext.py`'s 4-gram
model on fr16 (LANG_CORPORA["fr"], 16th-century French letters). The null is the same judge's resolutions of the 20
wrong maps in the same call, so the Frenchness the judge's within-pair choices add sits on both sides.

| call | target | best permuted | median permuted | rank |
|---|---|---|---|---|
| known lines (control) | -1.091 | -1.433 | -1.971 | 1 of 21 |
| f.108v seed 101 | -1.227 | -1.610 | -2.017 | 1 of 21 |
| f.108v seed 102 | -1.558 | -1.731 | -2.078 | 1 of 21 |
| f.108v seed 103 | -1.255 | -1.560 | -2.007 | 1 of 21 |

**GATE H93 PASS** (`scripts/f61judge_ngram_result.txt`, `--check` fresh). Context at 274 letters: fr16 real-text p05
-0.870 (median -0.781), letter-shuffled p99 -1.798 -- the target resolutions sit between shuffled and real prose, well
below real text: consistent with a noisy text (grade-M transcription, dropped nulls, some wrong cells) rather than a
clean one, and not a language PASS in `judge_plaintext.py`'s sense. What it adds to H85: the true cell map's advantage
on f.108v is visible to a mechanical score, not only to the model judge that produced the letters. Not a reading; no
class change.

## Campaign step H94 (28 Sept 2026, 15:40-15:52 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

H85 rerun with the prompt's spelling examples ("estoit", "avecques", "beau-pere" -- the last one of Tomokiyo's words on
the known lines, H90) replaced by "icelluy", "soubz", "advis", otherwise verbatim; fresh permutations and order (seed
104); prompts and sets pushed 12f9eac9 before the calls (`scripts/PROMPTS.md` "H94"). Two Opus text calls.

- **Control, known lines** (`f61judge_known_h51_s104_*`): target rank 1 of 21, 6.0 vs next 2.0 -> PASS. The resolution
  no longer writes "beaupere" (it gives "enuoenuprere") but still reads "tropau..." and "melentendoit". Within-pair
  letters against Tomokiyo (`scripts/f61judgeletters.py --tag known_h51_s104`, `f61judgeletters_known_h51_s104_result.txt`):
  31/36 = 0.861 (binomial P 6.5e-06; one line skipped for a length mismatch), against 43/47 with the leaked example.
- **f.108v** (`f61judge_f108v_s104_*`): target rank 1 of 21, **6.5 vs next 1.0** -> PASS, the widest margin of the
  four f.108v calls; its resolution repeats the runs of H85 ("...missionsmentresurloss", "seulement", "conservation",
  "sont ilz", "necessaires").

**GATE H94 PASS** (both calls rank 1 of 21). H85 does not depend on the leaked example word; the judge's letter
choices lose a little accuracy without it (0.915 -> 0.861 on the known lines). Not a reading; grade M throughout; no
class change. For the verifier (H88) the f.108v evidence is now four judge calls at rank 1 of 21 (margins 6.0, 0.5,
1.5, 5.5) plus the 4-gram check H93.

## Campaign step H95 (28 Sept 2026, 15:53 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs) -- dropped, no call

fr.3983 f.211r (Mayenne to de Diou, camp of Han, 1 April 1593; the aid: "chiffre et déchiffrement"), looked at on the
1600-px reference (`family/images/3983_f211r_ref1600.jpg`): the leaf is clear text but for one short cipher run of about
15 signs on line 2, with small clear words written above it. It is not a third text for the judge (H85 needed hundreds
of pair positions). What it is: a small period known answer in Mayenne's secretary's hand, used in no fit -- a held-out
check of the f.61 cells once a person reads its gloss (the model gloss readers fail on this hand, H34/H35/H57). That is
H96 (a desk pack). No cost.

## Campaign step H96 (28 Sept 2026, 15:54-15:55 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

Desk pack for f.211r's one glossed cipher run: the native fetched once from Gallica (btv1b9059406b f362, 1 request, kept in
the scratchpad, not committed), the run cut at 2x with a numbered ruler (`images/person_pack_211r/f211r_run.jpg`, the
whole run and its four gloss words checked by eye) and `README.md` with the TSV template; ASKS row 93 filed. On arrival
(`scripts/gloss211r_person.tsv`) the run's signs are coded with the atlas and the gloss letters are compared with the
f.61 cells (H64's recipe) -- a held-out period check, independent of every fit. No reading.

## Campaign step H97 (28 Sept 2026, 15:55-15:56 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

`--len-match` census on the other family leaves (`scripts/f61sbs.tokens`, pass A agreeing on the class): f.106r gives PHI
e 2 / r 2 / b 1, VBAR_A t 2, 4TRI a 3 / n 1 (its gloss is HELD, 34% words, so few positions carry an aligned letter);
f.124r gives none for PHI, VBAR_A/B, 4TRI or LOOPS (its align, built in the numeral-OTHER mode for de Diou's hand, does
not line up with the draft by length either); f.97r has no align file. No fourth glossed hand for the tile tests; the
SBS and VBAR attestations stay at three and two hands. No cost beyond the census.

## Campaign step H98 (28 Sept 2026, 15:56-15:58 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

For the family key only (HASH4 is a null on f.61): the readers' HASH4 carries a period i 7 times on f.188r, where the
H24 glyph carries i 26 times. Pre-registered and pushed 768bdb8f before the call: `build-pair NATIVE HASH4 i d,q 98 h98 7`
(f.101r 3+3, f.188r 7+7, 20 tiles), a prompt that does not presume the 4, `score-pair --strat --min 16`. One blind Opus
vision call; tile 2 none.

| reader's group | i | d/q |
|---|---|---|
| A a 4 joined above a hash cluster | 1 | 9 (d 7, q 2) |
| B a bare hash / H-like cluster, no 4 | 8 | 1 |

Stratified observed 17/19, permutation P = 0.0015, p95 14/19 -> **GATE PASS** (`scripts/f61pair_h98_result.txt`,
`--check` OK; row H98 in `scripts/f61_glyph_splits.tsv`). The family readers' HASH4-under-i is the bare hash glyph
(the family atlas's H24, i/x in the table) coded HASH4: one more coding merge for the family worker's key rebuild (H52),
beside PHI/SBS, LOOPS/SBS+INF, 4TRI/hook forms and VBAR_A/VBAR_B. No f.61 cell changes. No reading, no class change.

## Campaign step H99 (28 Sept 2026, 15:59 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

`scripts/family_relabel_proposal.tsv`: the six tile-tested coding merges of the family readers in one table for the family
worker's key rebuild (H52) -- PHI o/b -> SBS (three hands), LOOPS o -> SBS and LOOPS u -> INF, 4TRI a/n -> the hook
forms (C43/4STEM on f.61), VBAR_A s -> VBAR_B (two hands), HASH4 i -> the bare hash (H24) -- with steps, leaves, tiles and
the blind sorts' own shape criteria, plus the tested non-merges (e/r, a/n, d/q, g/t) and the EBR_A near miss. A
proposal only; nothing in family/ touched.

## Campaign step H101 (28 Sept 2026, 15:59 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

`scripts/f108v_lines.py` -> `scripts/f108v_lines.txt` (`--check` fresh): per row of f.108v, the fr16 4-gram rank of the
judge's target resolution among the 21 resolutions of the same call, in the four calls (H85 seeds 101-103, H94 seed 104).
The target ranks 1 of 21 in 23 of 28 row-calls; rows L03, L04, L06 and L07 rank 1 in all four calls on their own (L06
with 3 flagged signs); L01 and L02 miss once (rank 4, seed 102); L05 is the weak row (ranks 1, 6, 4, 3; 2 flagged
signs). For the verifier (H88): the signal is spread across the leaf, not carried by one lucky row. Not a reading.

## Campaign step H100 (28 Sept 2026, 16:00-16:03 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

A harder null for the f.108v judge result: 20 maps each differing from the fitted 14-cell map by ONE swap of two classes
whose cells differ (`scripts/f61judge108v.py build f108v --seed 105 --swap`; prompt = H94's no-leak prompt, file name
changed; sets and prompt pushed 3f7e4097 before the call). One Opus text call, which wrote its verdict to
`scripts/f61judge_f108v_swaps105_verdict.tsv`.

Target rank **1 of 21**, 5.0 vs next 4.5 -> **GATE PASS**, thin (`f61judge_f108v_swaps105_result.txt`, `--check`
fresh). The runner-up (4.5) is the swap 4TRI c/p <-> 4PI d/q -- the two 4-shaped cells Tomokiyo himself names as easily
confused ("the similarity of the symbols for a/n, c/p, and d/q", `sources/cryptiana/web/mayenne.htm`); every other
one-swap map scores 2.5 or less (swaps touching PHI e/r, SBS b/o, C43 a/n, INF h/u, EBR, VBAR, ZHOOK, BETA among them).
So the judge resolves the f.108v cells at the single-swap level except for c/p against d/q, where the text barely
prefers the fitted assignment. Not a reading; grade M; no class change.

## Campaign steps H102 and H103 (28 Sept 2026, 16:04-16:06 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

**H102, the control H100 lacked.** The one-swap hard null on the known f.61 span lines (`build known_h51 --seed 105
--swap`, H94 no-leak control prompt; sets and prompt pushed e3a957f7 before the call; one Opus text call, verdict written
to disk by the judge): target rank **1 of 21**, 7.0 vs 5.5 (runner-up swaps BETA m/z <-> 4STEM a/n) -> **PASS**
(`f61judge_known_h51_swaps105_result.txt`, `--check` fresh). No swapped set renders identical to the target on either
the known lines or f.108v (checked), so no tie is hidden.

**H103, model-free check of H100/H102** (`scripts/f61judge_ngram.py --hard`, `f61judge_ngram_hard_result.txt`): by fr16
4-gram the known-lines target ranks 1 of 21 (-1.349 vs -1.366, thin), but on f.108v the target ranks **2 of 21**
(-1.260) behind SET-04 (-1.241) -- the same 4TRI c/p <-> 4PI d/q swap the judge placed second (4.5 vs 5.0); the next map
is well below on both instruments (-1.301; judge 2.5). **GATE H103 FAIL** as pre-registered.

Reading the two together: on f.108v the cell assignment is resolved at single-swap level for every pair of cells except
c/p against d/q, where the judge barely prefers the fitted map and the 4-gram score barely prefers the swap -- the two
4-shaped cells Tomokiyo calls confusable. The f.61/f.108r fit decided that assignment from Tomokiyo's markup and the
reprinted period gloss (H51); f.108v's text neither confirms nor contradicts it. For the verifier (H88): the c/p and
d/q positions of the f.108v consensus are the least supported letters. Not a reading; no class change.

## Campaign step H104 (28 Sept 2026, 16:06 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

`scripts/H66_PAGE.md` brought up to H93, H94, H100-H103 and H99 for LANE VO3 (the finding aid's "chiffre et
déchiffrement" for f.108, the model-free and no-leak checks, the per-row ranks, the one-swap hard null and the c/p-d/q
near tie; the file table extended). No new claim.

## Campaign step H105 (28 Sept 2026, 16:07 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

How many positions does each one-swap map actually change (`scripts/f61swappower.py`, `f61swappower_result.txt`,
`--check` fresh)? On f.108v the 4TRI <-> 4PI (c/p <-> d/q) swap changes **6 of 274** pair positions -- the fewest of all
twenty (f.108v's draft has 6 4TRI signs and no 4PI); every other swap changes 11 to 101. On the known lines the same
swap changes 8 of 58. So H100's runner-up and H103's near tie are a null that could hardly differ from the fitted map
(rule 3's "a control that cannot vary"): f.108v is a NON-TEST of the c/p-versus-d/q assignment, not evidence against
it. That assignment rests on H72 (our 4TRI under Tomokiyo's c/p 10 of 10) and H69 (the 4-over-triangle carries the
period c/p in two glossed hands). Every swap with real power (11 or more positions) scores well below the fitted map
under both the judge and the 4-gram score. The H103 FAIL stays logged as run; this is its reading. No reading, no class
change.

## Campaign step H107 (28 Sept 2026, 16:09-16:12 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

A pre-registered judge prediction of f.108r rows L04-L06 ahead of the person's gloss (ASKS 88): sets from the family cut's
pass A (`scripts/pass108gA_classes.tsv`, the person pack's numbering; 94 signs, of which 18 OTHER and 12 PLAIN leave 59
cell positions; pre-H26, so side-by-side signs sit in PHI as [e/r]); the H94 no-leak prompt; ONE Opus text call (amended
from three before the call, recorded in `scripts/PROMPTS.md` "H107"); sets and prompt pushed 275dae78 before it.

Target rank **4 of 21** (1.5; best 2.0; every set scored 2 or less) -> **gate FAIL**: on these rows the judge finds no
French under any map, which fits the handicapped input (a third of the signs uncovered, the loop split not applied, a
single uncorrected pass). The target's resolution ("pmimeruuiemereteuueqnete | ptduinemisilmarm | ctaelturepieceuruue",
`f61judge_f108r_L04_L06_s107_result.txt`) stays committed as the pre-registered prediction for H64 to score against the
person's gloss letter by letter; expect it to score poorly. A useful prediction on these rows needs the reconciled,
H26-relabelled signs first (a later runner's row). No reading, no class change.

## Campaign step H106 (28 Sept 2026, 16:13 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

f.108v row L05, the weak row of H101 (`scripts/f108v_L05.py`, `f108v_L05.txt`, `--check` fresh): the four target
resolutions (H85 x3, H94) disagree on 16 of its 39 positions, the same order as L01 (16/41), L03 (16/37), L06 (18/41)
and L07 (17/40), with L04 the steadiest (10/42); only one L05 disagreement sits on a flagged (L) sign. Over all rows the
disagreements fall mostly on PHI e/r and C43/4STEM a/n -- the within-cell choices that no period glyph separates (H71,
H73) -- then ZHOOK i/x and BETA m/z. So L05's weaker 4-gram rank comes from the judge's within-pair choices, not from the
transcription flags. For the verifier (H88): the e/r and a/n letters of the f.108v consensus are its softest,
together with c/p/d/q (H105). No reading, no class change.

## Campaign step H109 (28 Sept 2026, 16:14 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs), script-only

`scripts/H66_PAGE.md` brought up to H105-H107 (the c/p-d/q non-test, the e/r and a/n softness, the f.108r prediction FAIL
and its handicap). `scripts/f61_glyph_splits.tsv` needs no change (no new tile test). No new claim.

## F61-FAMILY-7: fr.3641 and fr.4699 leads (28 Sept 2026, 16:12-16:25 UTC)

Detail and evidence in `family/FR3641_FR4699.md`. **fr.3641 f.126r-v** (Gallica btv1b52508089f canvases 269-270; the
Noyon letter, Reims 4 May 1593, Italian) carries an interlined decipherment but is in a **two-digit figure cipher**
(e.g. "45 74 46 46 81 75 46 90 75 16 56", about thirty distinct groups in four rows), not the Mayenne polyphonic
signs: no use for f.61's key. **fr.4699 ff.37 and 41** (Fortia to Roissieu and to La Chapelle, Mayenne's secretaries,
Lyon 7 Feb 1593, "avec chiffre et déchiffrement") is **not digitised** (no Gallica link in the record; SRU 0 records
vs 1 for the fr.3641 control), so whether it is in f.61's cipher is undetermined; reproduction request drafted in
`family/REQUEST_fr4699.md` for the person's card. No glossed signs aligned, no per-leaf key, key v4 untouched.

## Campaign step H110 and a correction to H100/H103 (28 Sept 2026, 16:47-16:52 UTC, runner session_01NQpd6L9ZvLvjU1L7ttFmZs)

**H110.** A second one-swap hard-null draw (seed 106; sets and the H94 no-leak prompts pushed 19592f15 before the calls).
Control on the known lines: target rank 1 of 21, **8.0 vs 6.5 -> PASS** (`f61judge_known_h51_swaps106_*`). The f.108v call
is **VOID**: the judge's own report says it resolved one set by hand and generated the other twenty with a script
anchored on that set, then wrote the file without reading it back -- the sets were not judged independently, and the
prompt forbids reading any command output. Its file is kept, marked void on its first line; its rank (1 of 21) is not a
result.

**Correction to H100 and H103.** Checking the transcripts of every judge call that delivered its verdict by writing a
file (H100, H102, H107, H110 x2; the earlier calls returned their verdicts inline): the H100 f.108v judge also ran a
Python script over its sets file before writing its verdict, so **H100 is VOID** as a test and **H103**, which scored
H100's resolutions, falls with it. H102 (known lines, 7.0 vs 5.5), H107 and the H110 control used no script and stand.
H105's position counts depend only on the maps and stand: the c/p <-> d/q swap changes 6 of 274 positions on f.108v, so
that assignment is not testable on f.108v by any call. What is withdrawn: "f.108v resolves every cell pair at the
single-swap level" -- the one-swap null on f.108v is UNTESTED (H111 reruns it with an inline verdict). What stands on
f.108v: H85 (3/3, inline), H94 (inline), H93 (4-gram on those inline verdicts), H101, H106. The failure is the runner's
delivery instruction ("write your TSV to the file"), which invited a tool-using judge to script; later judge prompts
return the verdict inline only. No reading, no class change.

## Campaign step H108 (28 Sept 2026, 17:17-17:28 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe)

Fair input for the f.108r L04-L06 prediction (H107 failed its gate on an uncorrected pass A with L06 half cut). Row amended
before any call (CAMPAIGN.md H108, `scripts/PROMPTS.md` "H108", pushed 833a6435): four Opus vision calls, the judge rerun
moved to H112.

**Re-cut.** The H34 region (y 450-1170 of canvas 195) cuts L06 through its lower half, so both H34 passes graded every
L06 sign l ("top only"). One Gallica IIIF request (200, `images/requests_h34.log`) fetched the strip y 1050-1310
(`images/src_ark_12148_btv1b9059406b_f195_1250_1050_3600_260.jpg`); its 120-px overlap with the H34 region is
pixel-identical (mean abs diff 0.0; 38.1 at a 10-px shift), stitched to `images/stitch_f108r_f195_1250_450_3600_860.jpg`
and L06 re-cut whole with the H34 cutter parameters (`images/f108h/`, 4 crops; the L04/L05 boxes come out identical to
the H34 cut, so their passes stand).

**Calls 1-2: two blind passes of L06 on the whole row** (`scripts/pass108hC_L06.tsv`, `pass108hD_L06.tsv`; each read
the atlas and the four crops only, no script): 40 signs each, 34/40 columns identical (the half-cut H34 passes had
agreed on none of L06 at better than l).

**Call 3: reconciliation** (`scripts/f61recon108r.py task|apply`, `f61recon108r_task.tsv`, `_verdict.tsv`, `_draft.tsv`,
`_result.txt`; `apply --check` fresh). 85 aligned columns (L04 26, L05 19, L06 40, PLAIN dropped), 11 to settle: h 1,
m 9, l 1, none 0. Still flagged 1/85 = 0.012 -> **draft gate (the H59 gate, <= 10%) PASS**. Stated alongside: 12 L06
columns are agreed by both passes but both at l (agree-flagged, not settled by the pre-registered rule), so 13/85 = 15%
of the draft is grade L; L04 and L05 carry no L beyond the one flagged column. Inventory PHI 14, ZHOOK 10, HASH4 10,
VBAR_A 8, BETA 7, 4STEM 6, DBL 5, INF 4, 4PI 4, C43 4, OTHER 3, SBS 3, ISH 3, others 1 each.

**Call 4: loop-arrangement classification on tiles** (`scripts/f61loop108r.py build|score`, sheets `images/h108/`,
key `scripts/f61loop108r_tiles.tsv` never named, reply verbatim `scripts/read_call_H108.tsv`; the reader read the five
sheets only). 26 target tiles (every PHI/DBL/SBS/LOOPSTEM1/OTHER of the draft) and 18 controls from H26's own sort
(9 G2 side-by-side, 9 G1/G3; all tiles greyed and contrast-stretched so the f.61 colour sheets do not stand out).
Controls **13/18 on H26's side -> gate (>= 15/18) FAIL, so no relabel is applied**, as pre-registered. The misses are
one-sided: G2 9/9 right; G1/G3 4/9, and all five misses are f.61-hand trefoils called "two side by side" (the f.108 G1
controls 3/3 right). So at this tile scale the reader cannot be trusted to see a trefoil's small top loop in the f.61
hand; whether it can in the f.108 hand is untested at 5 controls (a per-leaf breakdown, not a pass). For the record only
(not applied): the reader put the three draft OTHER signs described by the passes as "two loops side by side" (L04/8,
L05/10, L05/19) and PHI L04/18 in "side by side", the three draft SBS on L06 two side by side and one "three small loops
in a row", and all five L06 DBL and 12 of 14 PHI in "trefoil".

**What this leaves for H112.** The corrected input is the reconciled draft (`f61recon108r_draft.tsv`) without a loop
relabel from this call: OTHER, DBL and LOOPSTEM1 are outside the 14-cell map and would drop, as HASH4 does. H112 must
pre-register, before its build, how the draft's DBL is rendered; H26's own result (the stacked figure-8 G3 = e/r, 5/5,
f.108 only) is the established rule for it, independent of this call's failed gate. No reading, no class change.

Files: as named above; `images/regen_f61r_sheets.sh` unchanged (the H108 stanza is the commands in this section).
Vision calls: 4 of 4. Requests: Gallica 1. No credentials, no AskUserQuestion; the owner not named.

## Campaign step H111 (28 Sept 2026, 17:30-17:36 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe)

The f.108v one-swap hard null of H100, rerun with a VALID judge call (H100 and H110's f.108v calls were void: their judges
scripted the verdict). Same sets file (`scripts/f61judge_f108v_swaps105_sets.txt`, unchanged), the H94 no-leak prompt plus
one sentence forbidding any tool but reading that file (`scripts/PROMPTS.md` "H111", pushed a2425db4 before the call). The
transcript shows two Read calls of the sets file (the second an offset read of its tail) and the hand-back, nothing else:
the call stands. Verdict verbatim `scripts/f61judge_f108v_swaps105i_verdict.tsv`, scored under the copied key
(`f61judge108v.py score f108v_swaps105i`, `f61judge_f108v_swaps105i_result.txt`).

Target **rank 1 of 21 (5.0) -> gate PASS**, thin. Runner-up SET-04 (4.0) is the 4TRI<->4PI (c/p<->d/q) swap, which changes
only 6 of 274 positions (H105: a swap with no power, so its near tie is a non-test of that assignment, not a negative);
next SET-16 (3.5), EBR_B<->VBAR_B (l/y<->f/s, 12 positions); every swap changing 17 or more positions scores 2.5 or less
(`scripts/f61swappower_result.txt` for the counts). With the H102 (7.0 vs 5.5) and H110 (8.0 vs 6.5) controls on the known
lines, the fitted map beats its one-swap neighbours on f.108v wherever a swap has power, by at least 1.5 points except the
l/y<->f/s pair (1.5) and the powerless c/p<->d/q pair (1.0). The judge's own note: scattered French fragments under the
target ("nous", "aurons", "seulement", "terre leur", "allez", "mais non", "aussi sont ilz ... necessaires", "tenir"), no
set continuous French. One call; no reading claimed, no class change.

## Campaign step H112 (28 Sept 2026, 17:40-17:47 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe)

The H107 f.108r L04-L06 prediction rerun on H108's corrected input (reconciled draft, L06 whole, DBL -> PHI by H26, no loop
relabel): `f61judge108v.py build f108r_L04_L06_h108 --seed 108|109` (71 pair positions, 14 cells; sets pushed 59429f74,
prompts `scripts/PROMPTS.md` "H112" pushed 10e2155f, both before the calls). Two Opus text calls, each VALID (transcript:
one Read of its sets file and the hand-back, nothing else); verdicts verbatim `f61judge_f108r_L04_L06_h108_s10{8,9}_verdict.tsv`.

Seed 108: target 1.5, **rank 2 of 21** (tied with one permutation; ties against) -> FAIL. Seed 109: target 1.5, **rank 8
of 21** (two sets at 2.0) -> FAIL. Every set in both calls scored 2.0 or less: with the input corrected, the judge still
finds no French on these rows under the 14-cell map or any permutation of it. So H107's FAIL was not only the handicapped
input. What the map leaves out is large on these rows: HASH4 (10 of 85 draft columns, a null on f.61 but d/q under the
4-over-hash on the family leaves, H98 PASS 17/19) is dropped, with OTHER 3 and LOOPSTEM1 1 -- 14 of 85 signs gone, and
three of them are the "two loops side by side" OTHER signs H108's relabel could not license. The target resolutions stay
committed as the pre-registered prediction for H64 (ASKS 88); expect them to score poorly. No reading, no class change.

## Campaign step H114 (28 Sept 2026, 17:50-17:53 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61hash4_108r.py` (gates in its docstring, pushed 87aae8b6 before the first run; `f61hash4_108r_result.txt`,
`--check` fresh): each line resolved by a 4-gram beam (fr16, width 400) over the x/y choices, the fitted map ranked against
200 cell permutations (seed 114). No model call.

- **Control, known f.61 span lines, 14 cells: fitted -0.906, rank 1 of 201** (best permuted -0.959, median -1.293) -> PASS:
  the instrument sees the known key at this length.
- **f.108r L04-L06 (H108 draft), 14 cells: fitted -1.092, rank 2 of 201** (best permuted -1.075, median -1.364).
- **Same with HASH4 = d/q: fitted -1.200, rank 12 of 201** (81 covered signs; best permuted -0.988).

So HASH4 = d/q does **not** help these rows: it drops the fitted map from rank 2 to rank 12, which fits HASH4 behaving
as on f.61 (a null or another value) rather than as the family leaves' 4-over-hash d/q -- or the passes' HASH4 here
lumping the bare hash (H24, period i by H98) with the 4-over-hash; not separated on this draft. The row's pre-registered
verdict is "does not move", but the step also shows something H112's judge did not: model-free, the 14-cell map sits at
rank 2 of 201 on f.108r L04-L06 (about the top 1%), close to the control's rank 1. One seed, one draft, beam-resolved
(the beam's letter choices are made the same way for every map, so the Frenchness it adds is on both sides): a signal to
replicate, not a reading. No class change.

## Campaign step H115 (28 Sept 2026, 17:55-17:57 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61ngram108r_repl.py` (gate in its docstring, pushed be5a8458 before the run; `f61ngram108r_repl_result.txt`):
H114's instrument on a fresh 1000-permutation null (seeds 115/116). The HASH4 split the row named was not run (amended
before the run: the passes code every hash HASH4 and their notes do not separate bare hash from 4-over-hash).

- Control, known f.61 span lines: fitted -0.906, **rank 2 of 1001** -> PASS.
- f.108r L04-L06 pooled: fitted -1.092, **rank 13 of 1001** (10th-best permuted -1.089, median -1.368) -> **gate (rank
  <= 10) FAIL, narrowly**: the fitted map sits in the top 1.3% of the null, not the pre-registered top 1%.
- Per line: L05 alone rank 13, L06 alone rank 27, L04 alone rank 146 of 1001 -- the pooled figure comes mostly from L05
  and L06; L04 carries little.

Read together with H114 (rank 2 of 201 on another seed): a consistent lean toward the fitted map on f.108r, in the top
1-2% on two nulls, just outside this step's gate, so no "signal on f.108r" is claimed. The judge (H107, H112) saw nothing
on the same rows; the two instruments disagree at this length and neither licenses a reading. The deciding material is
still the person's gloss of these rows (ASKS 88). No reading, no class change.

## Campaign step H113 (28 Sept 2026, 18:00-18:05 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe)

H108's loop classification again, with controls from the f.108/family hands only (`scripts/f61loop108r.py build-h113 |
score-h113`, sheets `images/h113/`, key `f61loop108r_h113_tiles.tsv`, reply verbatim `scripts/read_call_H113.tsv`,
result `f61loop108r_h113_result.txt`; prompt pushed fe57d7d5 before the call; the reader read the six sheets only).
26 targets, 26 controls: 20 H65 period-glossed tiles (10 o, 10 e, cut back out of the H65 sheets) and 6 H26 f.108 tiles.

Controls **18/26 on the expected side -> gate (>= 90%) FAIL, no relabel**. By source: H26 f.108 tiles 6/6; H65 period
tiles 12/20 (o 7/10, e 5/10) -- the reader called several of the pale period-hand tiles "single", "other" or ordinary
handwriting ("hogo", "Eogo"), i.e. the H65 tiles re-cut from their contact sheets are too faint after re-contrast for this
reader, not a shape failure it shows on the f.108r hand. This is the second failure of the same instrument (H108 13/18,
H113 18/26) on the same question, each for a different control-side reason; by CLAUDE.md rule 3's unchanged-approach
paragraph the loop relabel of f.108r L04-L06 is logged **untested by this tile classification**, not re-briefed a third
time. What would settle it is a different instrument or material: the person's gloss (ASKS 88) gives o/b vs e/r directly
under each sign. No reading, no class change.

## Campaign step H116 (28 Sept 2026, 18:09-18:11 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_known.py` (method and gate in its docstring, pushed e9fd8d73 before the run; `f61beam_known_result.txt`,
`--check` fresh). The H114/H115 4-gram beam's within-pair letter choices scored against Tomokiyo's known span letters on
f.61r (the known_h51 lines, 14-cell map; markup placed by F61-CAL's DP).

- 54 known letters aligned; 49 on covered signs whose pair contains the true letter.
- **Choice accuracy 38/49 = 0.776** (always the pair's first letter 29/49 = 0.592; chance 0.5, one-sided binomial P about
  5e-5 against 0.5).
- Letters matched: fitted map 38 vs 200 permuted maps median 2, p95 12, max 20.
- **GATE H116 (>= 0.75 and > p95): PASS.**

Caveats for the verifier: the 14 cells were fitted partly on these very spans (f61joint_h51_map), so (i) is circular and only
(ii) tests anything; (ii) is the beam's own choice between the two letters of a cell and uses no span letter. 49 positions:
the accuracy's 95% interval is roughly 0.64-0.87. This licenses the beam as a grading aid for two-way choices at about three
right in four on text of this kind -- it does not by itself read any unmarked passage. No reading, no class change.

## Campaign step H117 (28 Sept 2026, 18:12-18:14 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_margin.py` (design and gate in its docstring, pushed 3450e76d before the run; `f61beam_margin_result.txt`,
per-position `f61beam_margin_positions.tsv`). The H116 beam applied to f.61r in VERIFY-F61-V4's two-way form under key v4
(sets of 2-7 letters, lines cut at the unread <CLASS> signs), margin per position, leave-one-span-out calibration.

- 59 set positions (the audit's 59); 42 carry a Tomokiyo letter inside the set; **beam right on 23/42 = 0.548**.
- Calibration: three of five folds find no margin threshold at 90% on their training spans; the other two score 1/3
  held out. **GATE H117 (>= 0.85 on >= 8 held out): FAIL (1/3)**; nothing is applied outside the spans.

So H116's 0.776 does not carry over to key v4's two-way form: there the beam is near chance. Two differences, not separated
here: v4's sets are wider (up to seven letters, e.g. [e/q/i/p/r/s/t]) than the 14-cell pairs, and cutting each line at its
unread signs leaves segments of two to six letters, too short for a 4-gram model to choose within. The two-way choices on
f.61r stay unmade by any controlled instrument (AUDIT.md sec. 6 item 1 unchanged). No reading, no class change.

## Campaign step H118 (28 Sept 2026, 18:15-18:16 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61hash4_values.py` (pushed 064fc71c before the run; `f61hash4_values_result.txt`): H114's beam and 200-permutation
null (seed 114) on f.108r L04-L06 with HASH4 given INF's cell or the bare hash's period value.

| HASH4 as | fitted | rank of 201 | best permuted |
|---|---|---|---|
| dropped (H114) | -1.092 | 2 | -1.075 |
| d/q (H114) | -1.200 | 12 | -0.988 |
| h/u | -1.038 | 2 | -0.993 |
| i/x | -1.013 | **1** | -1.018 |

HASH4 = i/x (H98's bare-hash value, period i 8/9 on the family leaves) gives the best fitted score and rank 1; d/q is the only
value that hurts. Four values have now been tried on the same 201-map null, so rank 1 for the best of four is weaker than a
single pre-registered rank 1 (roughly a 4x look-elsewhere factor); the permutation null moves with the value, which partly
controls for a value simply being easier French. Suggestive, not established: H119 replicates i/x alone on a fresh
1000-permutation null. No reading, no class change.

## Campaign step H119 (28 Sept 2026, 18:17-18:18 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61ngram108r_repl.py --hash4-ix` (the H115 design, option pushed 2bbd3d9a before the run;
`f61ngram108r_repl_ix_result.txt`): HASH4 = i/x added to the 14-cell map, which then joins the permuted classes; the fresh
1000-permutation null of H115 (seeds 115/116).

- Control, known f.61 span lines (their one HASH4 sign now included): fitted -0.918, **rank 1 of 1001** -> PASS.
- **f.108r L04-L06 pooled: fitted -1.013, rank 1 of 1001** (best permuted -1.046, 10th -1.121) -> **gate (<= 10) PASS**.
- Per line: L06 alone rank 1, L05 rank 13, L04 rank 171 of 1001.

Weight for the verifier: the value i/x was chosen as the best of four on H114's seed of this same text (H118), so the fresh
null guards against seed luck, not against that choice; with four values tried, rank 1 of 1001 is roughly P <= 0.004 after
the look-elsewhere factor. Read with H116 (the beam's within-pair choices 0.776 right on the known spans), this is the first
model-free, controlled sign that f.108r L05-L06 decode toward French under f.61's cells plus HASH4 = i/x -- a family-key
fact about f.108r (HASH4 as the bare-hash i, as H98 found on the period-glossed leaves), not a reading of f.61 or of f.108r.
The judge calls (H107, H112) saw no French on the same rows; the disagreement stands. H120 commits the beam's resolution under
this map as a second pre-registered prediction for H64 before the ASKS 88 gloss lands. No class change.

## Campaign step H120 (28 Sept 2026, 18:19-18:20 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_f108r_predict.py` -> `scripts/f61beam_f108r_prediction.txt` (per draft position: class, pair, beam letter;
`--check` fresh), pushed before the ASKS 88 gloss lands, as a second pre-registered prediction of f.108r L04-L06 beside the
judge's (H107, H112). The beam's strings ('.' = a class outside the map: OTHER, LOOPSTEM1, ...):

    L04: czimere.uiemeretrehuedarge
    L05: ngquin.em.isilznem.
    L06: agneioiibilitbieniralitdedixiiintmiletai

Not a reading: a model-free resolution of two-way pairs under a cell map that H119 ranks first of 1001 on these rows, with a
within-pair accuracy of about 0.78 on known text (H116). For H64 only, and only after the person's gloss is in: the H34 model
gloss readers' unverified words for these rows (NOTES H34: "misere" over L04, "quinze mois" over L05; 0.344 exact on known
rows) are to be compared then, not now. No class change.

## Campaign step H121 (28 Sept 2026, 18:22-18:23 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_known.py --f108r` (option pushed c0cf6b94 before the run; `f61beam_known_108r_result.txt`; the result
file prints the shared gate's name "H116"): the H116 method on Tomokiyo's printed overlay of f.108r L02/L03 (84 letters;
lines as f61joint.py builds them, H51 relabel, 14-cell map).

- 82 known letters aligned; 76 on covered signs whose pair holds the true letter.
- **Beam within-pair choice accuracy 69/76 = 0.908** (always-first-letter 40/76 = 0.526; chance 0.5).
- Letters matched: fitted 69 vs 200 permuted maps median 3, p95 15, max 27 -> **gate PASS**.

With H116 (f.61 spans, 38/49 = 0.776), the beam's two-way choices are right 107/125 = 0.856 over both known texts in this
cipher. Same caveat as H116: the cells were fitted partly on these letters; the choice within a cell was not. This makes
the beam a controlled instrument for the within-pair choices wherever the cell map holds and the text is long enough to
give it context (it failed on key v4's short, wide-set segments, H117). No reading, no class change.

## Campaign step H122 (28 Sept 2026, 18:24-18:26 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61ngram108r_repl.py --f108v [--hash4-ix]` (option pushed ea7c36da before the run; results
`f61ngram108v_repl_result.txt`, `f61ngram108v_repl_ix_result.txt`): the H115/H119 instrument on f.108v, the H59 reconciled
draft (grade M transcription), 1000-permutation null (seeds 115/116), known-lines control first.

| map | control (known lines) | f.108v pooled | margin to best permuted | lines at rank <= 10 alone |
|---|---|---|---|---|
| 14 cells | rank 2 | **rank 1 of 1001** (-1.011; best permuted -1.102) | 0.091 | 6 of 7 (L02 46) |
| 14 cells + HASH4 = i/x | rank 1 | **rank 1 of 1001** (-1.003; best permuted -1.146) | 0.143 | 6 of 7 (L01 15) |

**GATE (rank <= 10 of 1001, control also): PASS under both maps.** The model-free beam places f.61's cell map first of 1001
on the longest text in f.61's hand, with the signal spread over the rows (L04, L06, L07 rank 1 alone under both maps), not
carried by one line. This is the model-free counterpart of the H85/H94 judge results and the valid H111 one-swap result on
f.108v, and it agrees with them. It says f.108v is enciphered in the same cells as f.61; it is not a reading of either leaf
(the beam's within-pair choices run at about 0.86 on known text, H116/H121, and the transcription is grade M). H123 now
commits the beam's f.108v resolution as a pre-registered prediction before the leaf's sparse period gloss is read. No class
change.

## Campaign step H123 (28 Sept 2026, 18:27 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_f108r_predict.py --f108v` -> `scripts/f61beam_f108v_prediction.txt` (per H59 draft position: class, pair,
beam letter), committed before f.108v's sparse period gloss is read, as a pre-registered prediction under the H122 map with
the wider margin (14 cells + HASH4 = i/x). For scale: the pooled per-letter score of this resolution (-1.003) sits below
fr16 real prose at the same length (p05 -0.870, median -0.781; letter-shuffled p99 -1.798, `f61judge_ngram_result.txt`),
i.e. between shuffled text and real prose -- expected with a grade-M transcription, dropped classes and about one wrong
choice in seven. Not a reading. No class change.

## Campaign step H124 (28 Sept 2026, 18:29-18:31 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only -- a correction to H122

`scripts/f61beam_shuffle.py` (pushed 09377899 before the run; `f61beam_shuffle_result.txt`): CLAUDE.md rule 3's ARM-C1 check
on the beam's rank-1 results -- each target's signs shuffled within their lines (five seeds), ranked by the same instrument
against the same 1000 permutations. A result stands only if the shuffled targets' mean rank is outside the top 5% (> 50).

| result | real order | shuffled-order ranks (mean) | verdict |
|---|---|---|---|
| H119 f.108r L04-L06, HASH4 = i/x | 1 | 56, 181, 8, 93, 66 (80.8) | stands (thin: one shuffle ranks 8) |
| H122 f.108v, 14 cells | 1 | 2, 3, 2, 1, 2 (2.0) | **VOID as a gate** |
| H122 f.108v, HASH4 = i/x | 1 | 1, 7, 5, 1, 4 (3.6) | **VOID as a gate** |

**Correction:** H122's "rank 1 of 1001 on f.108v" is not evidence of sequence: on 274 positions the fitted map ranks at the
top even when the signs are shuffled, i.e. the rank measures how well the map's letter frequencies suit French, which a
fitted map does by construction. My 18:26 ROOM line and the H122 section above overstate it; H122 is void as a gate (rule 3),
and H123's prediction stands only as a committed resolution, with no rank behind it. The same concern applies in part to the
H114/H115/H119 ranks on f.108r, where the shuffled ranks are lower (mean 80.8) but not null. The known-answer results (H116
0.776, H121 0.908) are unaffected: they score the beam's choices against known letters, not a rank. The right statistic for
the unknown texts is the gain of real order over shuffled order under the fitted map, compared with the same gain under
permuted maps (H127). No reading, no class change.

## Campaign step H127 (28 Sept 2026, 18:32-18:34 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_seqgain.py` (statistic and gates in its docstring, pushed 8b038c6a before the run; `f61beam_seqgain_result.txt`).
Gain = beam score of the real sign order minus the mean over 20 within-line shuffles, under a map; the fitted map's gain
ranked among 200 permuted maps (seed 127). Letter frequency alone gives no gain, so this is the statistic H124 called for.

| text | gain (fitted) | rank of 201 | best permuted | median permuted |
|---|---|---|---|---|
| CONTROL known f.61 span lines, 14 cells | 0.255 | **1** | 0.194 | -0.014 |
| f.108v, 14 cells | 0.152 | **1** | 0.077 | 0.000 |
| f.108v, HASH4 = i/x | 0.165 | **1** | 0.089 | 0.002 |
| f.108r L04-L06, 14 cells | 0.120 | 6 | 0.156 | -0.002 |
| f.108r L04-L06, HASH4 = i/x | 0.183 | **1** | 0.175 | 0.000 |

Control PASS; **all four targets PASS (rank <= 10 of 201)**. On f.108v the fitted map's sequence gain is about twice the
best of 200 permuted maps', under both maps: the H122 conclusion (f.108v is enciphered in f.61's cells) is restored on a
statistic that frequency cannot produce. On f.108r the margin is thin (0.183 vs 0.175 with HASH4 = i/x; rank 6 without).
Post-hoc sanity check, not pre-registered (run once after the result, reported as such): f.108v with its signs shuffled gives
the fitted map a gain of -0.008 (rank 120) and 0.027 (rank 40) on two shuffles -- the statistic behaves as a null on a
shuffled target. H128 makes that check formal. No reading, no class change.

## Campaign step H128 (28 Sept 2026, 18:35-18:40 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61seqgain_shuffle.py` (pushed before the run; `f61seqgain_shuffle_result.txt`): rule 3 (ARM-C1) for H127 -- every
H127 text with its signs shuffled within lines (seeds 1281-1285), run through the same sequence-gain rank as a real target.
Gate: shuffled versions rank > 10 of 201 in at least 4 of 5.

| text | shuffled-target ranks | H127 |
|---|---|---|
| known f.61 span lines, 14 cells | 97, 96, 116, 169, 14 | stands |
| f.108v, 14 cells | 66, 186, 135, 41, 97 | stands |
| f.108v, HASH4 = i/x | 27, 172, 179, 49, 107 | stands |
| f.108r L04-L06, 14 cells | 173, 149, 53, 23, 101 | stands |
| f.108r L04-L06, HASH4 = i/x | 195, 191, 128, 6, 72 | stands |

The sequence-gain statistic behaves as a null on shuffled text (one shuffle in 25 inside the top 10), so the H127 results
stand as gates: f.108v is enciphered in f.61's 14 cells (rank 1 of 201, gain about twice the best permuted), with f.108r's
L04-L06 thinly the same. This is evidence about the cell map on the family leaves, not a reading of any leaf; the within-pair
letters are the beam's (about 0.86 right on known text, H116/H121) on a grade-M transcription. No class change.

## Campaign step H125 (28 Sept 2026, 18:41 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe) -- dropped before any run

f.61r's cipher runs outside Tomokiyo's spans are 17 signs on disk (`scripts/passU1/U2_classes.tsv`: L02 2-3, L04 1-2, L10 13),
of which the 14-cell map covers 7-8 (L10: PHI VBAR_A PHI PHI VBAR_B INF PHI; CA, C6, EBR and OTHER outside it). No rank or
sequence-gain statistic can be run on 7 letters with a control at the same length (rule 3), and the one thing the beam could
emit -- seven letters of L10 -- is the fragment audit 1 already weighed (AUDIT.md "Fragment L10"). Dropped: no step can test
anything here; f.61's own unread text is inside the span lines, where Tomokiyo's letters already stand.

## Campaign step H126 (28 Sept 2026, 18:43-18:45 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_margin14.py` (gate in its docstring, pushed 6443cc88 before the run; `f61beam_margin14_result.txt`,
per-position `f61beam_margin14_positions.tsv`): H117's leave-one-out margin calibration under the 14-cell pairs, seven folds
over both known texts (f.61 spans S1-S5, f.108r overlay T1-T2). 125 known positions, beam right 107/125 = 0.856.

Held-out positions above their fold's margin threshold: S1 2/2, S2 6/6, S3 **4/11**, S4 8/8, S5 7/7, T1 30/31, T2 28/30 --
pooled **85/95 = 0.895 -> GATE (>= 0.90 on >= 20) FAIL, by one position**. The miss is one fold: S3 ("trop avancees",
beam 4/11 overall) gets a near-zero threshold from the other folds and its wrong choices pass it; without S3 the held-out
rate is 81/84. No threshold is licensed, so no per-position firm/soft flag is offered to the verifier; the threshold is not
tuned after the fact. What the step does show: the beam's errors cluster in a span (S3) rather than spreading evenly, so a
margin alone cannot flag them. No reading, no class change.

## Campaign step H131 (28 Sept 2026, 18:49 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only diagnostic

From `scripts/f61beam_margin14_positions.tsv` and `scripts/passA_classes.tsv` (L05, span S3 "---trop--avance-es"): the beam
reads the 11 known positions as g r b p . n . n . a p r . e s against Tomokiyo's t r o p . a . a . n c e . e s (dots:
positions outside the known set). Seven wrong:

- **three on C43 (a/n)**, positions 9, 11, 13 -- all three inverted (n n a for a a n), each at pass-A confidence h: the
  a/n choice, not the sign;
- two on signs pass A graded l: VBAR_A g/t at 3, 4TRI c/p at 14;
- one on the DBL -> SBS relabel (b/o at 5, beam b for o) and one e/r (15).

So S3's cluster is mostly the a/n cell -- the within-pair choice H106 already found softest on f.108v (e/r and a/n) -- plus
two low-confidence transcriptions; the nulls Tomokiyo dashes (CA CA at 7-8, C6 at 12, LL at 16) split the span into short
pieces, which leaves the 4-gram little context. For the verifier: the beam's a/n and e/r letters are its weakest, and a span
cut by nulls into runs of 2-4 letters is where it fails. No reading, no class change.

## Campaign step H129 (28 Sept 2026, 18:48-18:55 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61seqgain_family.py` (pushed b6fbe4a0 before the run; `f61seqgain_family_result.txt`): the H127 sequence-gain rank
(null on shuffled text, H128) of f.61's 14-cell map on the six family leaves' reconciled drafts; classes outside the map
dropped (the family passes' LOOPS, H24, ZBAR, OTHER ...).

| leaf | signs | covered | gain | rank of 201 | best permuted |
|---|---|---|---|---|---|
| CONTROL known f.61 lines | -- | -- | 0.255 | 1 | -- |
| fr.3982 f.97r | 2,485 | 1,724 (0.69) | 0.065 | **1** | 0.044 |
| f.101r | 3,081 | 2,172 (0.70) | 0.053 | **1** | 0.044 |
| f.188r | 1,206 | 784 (0.65) | 0.110 | **1** | 0.068 |
| f.124r | 2,839 | 2,018 (0.71) | 0.051 | 2 | 0.052 |
| f.106r | 240 | 175 (0.73) | 0.074 | 4 | 0.102 |
| f.274 | 167 | 129 (0.77) | 0.079 | 10 | 0.104 |

All six at rank <= 10 -> by the pre-registered rule each is "in f.61's cells"; f.97r, f.101r and f.188r clearly (rank 1),
f.124r, f.106r and f.274 at the edge (a permuted map comes within or above them). The 14 cells were fitted on f.61 and
f.108r only, so this is out-of-sample for the family leaves. It supports the family route the campaign already takes (the
period keys of these leaves feeding key v4) with a model-free, frequency-proof statistic, and it makes f.101r and f.188r --
long, period-glossed, rank 1 -- the known-answer material for H130. No reading, no class change.

## Campaign step H130 (28 Sept 2026, 18:57-18:59 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_period.py` (pushed 2efb4bed before the run; `f61beam_period_result.txt`): the beam's within-pair choice
under f.61's 14 cells against the period decipherer's letter aligned under each sign (`family/passes/<leaf>_align.tsv`).

| leaf | scored positions | beam right | always-first-letter |
|---|---|---|---|
| f.101r | 1,042 | 724 = 0.695 | 0.583 |
| f.188r | 491 | 373 = 0.760 | 0.554 |
| pooled | 1,533 | 1,097 = **0.716** | 0.573 |

**GATE H130 (>= 0.80 on >= 100): FAIL.** On the period-glossed leaves the beam beats the first-letter baseline by about 14
points over 1,533 positions but does not reach the 0.86 it showed on Tomokiyo's known texts (H116/H121). Two causes the step
does not separate: the period letters come from an automatic sign-to-gloss alignment (the align files mark 1,522 of 3,075
f.101r rows "conflict"), so some "errors" are alignment slips whose letter happens to sit in the pair; and these leaves are in
other hands with their own spelling and the family passes' coarser classes (PHI here still holds the side-by-side b/o
form). The beam's accuracy on f.61 itself therefore stays the H116 figure (0.776 on 49), with 0.72 as a lower bound from a
noisier known answer. No reading, no class change.

## Campaign step H132 (28 Sept 2026, 19:03-19:10 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61swap_family.py` (rule in its docstring, pushed f7903848 before the run; `f61swap_family_result.txt`): every
one-swap neighbour of f.61's cell map (plus KEY.md's period equivalences LOOPS = h/u, H24 = i/x, ZBAR = f/s) scored by
sequence gain on the pooled family drafts (f.97r, f.101r, f.188r, f.124r: 9,611 signs, 8,488 covered). Fitted gain 0.0874.

**128 of 129 swaps have a lower gain than the fitted map (rejected); 1 is higher.** The close ones (fitted minus swap):
EBR_A f/s <-> ISH l/y -0.0007 (the one preferred; 154 positions), SBS <-> ZHOOK +0.0004 (5 positions: no power),
INF <-> ZHOOK +0.0006 (116), **4STEM a/n <-> 4TRI c/p +0.0007 on 1,626 positions**, ISH <-> ZHOOK +0.0012 (28); every other swap
+0.0018 or more. The two near-ties on many positions have a known cause in KEY.md, not in the cells: this hand's readers put
the "43" (a/n) sign into 4TRI (f.124r: n 140, a 121, c 45, p 34), so 4TRI on these drafts is half a/n already and swapping it
with a/n costs little; and EBR_A on these drafts is mixed (s 18, l 13, a 8), so f/s <-> l/y is near even. Where the family
classes are clean, the pool confirms f.61's assignments one swap at a time -- including c/p vs d/q (4TRI <-> 4PI), which f.108v
could not test (H105). No noise scale was pre-registered, so differences under about 0.002 are reported, not judged. No
reading, no class change.

## Campaign step H133 (28 Sept 2026, 19:11-19:13 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_period.py --ext` (option pushed 129e0e0f before the run; `f61beam_period_ext_result.txt`): H130 with KEY.md's
period equivalences for this hand added to the map (LOOPS = h/u, H24 = i/x, ZBAR = f/s).

| leaf | scored | beam right | always-first-letter |
|---|---|---|---|
| f.101r | 1,420 | 1,047 = 0.737 (H130 0.695) | 0.561 |
| f.188r | 588 | 465 = 0.791 (H130 0.760) | 0.529 |
| pooled | 2,008 | 1,512 = **0.753** (H130 0.716) | 0.551 |

**GATE (>= 0.80 on >= 100): FAIL**, closer: coverage up by a third and accuracy up about 4 points on both leaves together,
as H130 predicted (context was a limit). Logged as the beam's accuracy against the period gloss at this alignment: 0.75,
about 20 points over the first-letter baseline on 2,008 positions. A third pass at this gate with another tweak would be
the rule-3 "same knob" pattern; the remaining gap is at least partly the automatic gloss alignment, which only a cleaner
alignment (or a person's gloss reading) can remove. No reading, no class change.

## Campaign step H134 (28 Sept 2026, 19:14-19:15 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_words.py` (pushed bcc87a73 before the run; `f61beam_words_result.txt`): the beam's final states rescored
with a fixed word-cover bonus (0.5 per covered letter). Word beam 107/125 = plain beam 107/125 (f.61 spans 38/49, f.108r
overlay 69/76 both ways) -> **GATE (>= 115/125): FAIL, no change at all**. Why, structurally: the beam recombines states on
their last three letters, so its final 400 candidates differ only near the end of each line and a rescoring of them cannot
reach an earlier choice. A word model would have to live inside the search (states carrying a word position), a different
instrument (H136), not a weight on this one. No reading, no class change.

## Campaign step H135 (28 Sept 2026, 19:17 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only writing

`scripts/H66_PAGE.md` gains a section "H108-H134" (the f.108r draft, the retired loop instrument, the beam's known-answer
figures, the H124 correction and the sequence-gain results, HASH4, the committed predictions) and a files row. No new claim.

## Campaign step H137 (28 Sept 2026, 19:18-19:22 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61score_gloss108.py`, written and pushed before ASKS 88 is answered: reads the person's `scripts/gloss108_person.tsv`
(the person pack's format), maps pass-A sign numbers to the H108 draft (L04/L05 by segment and x through the reconciliation
task; L06 by nearest x within 90 px, since pass A read the half-cut row), places each gloss word on its covered signs with
F61-CAL's DP, and scores the four committed predictions (H107, H112 s108/s109, H120 beam) letter by letter where the gloss
letter is in the sign's pair, beside first-letter and 0.5 baselines. Today it prints "waiting". `--selftest` builds a
synthetic gloss from H120's own letters (19 words): H120 scores 71/71 and the selftest PASSes; the other predictions'
numbers in that run mean nothing (the synthetic gloss is H120's). H64 now only needs the file. No reading, no class change.

## Campaign step H136 (28 Sept 2026, 19:23-19:27 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_lattice.py` (design and the one bonus weight fixed in its docstring, pushed 2c63d308 before the run;
`f61beam_lattice_result.txt`): a beam whose state carries a position in a trie of the fr16 word list (15,402 words), bonus
0.5 per letter of a completed word, width 2000. On the 125 known positions: **lattice 111/125 vs plain 107/125 -> GATE
(>= 115) FAIL**. By text: f.61 spans **44/49 = 0.898** (plain 38/49), f.108r overlay 67/76 (plain 69/76). The word model helps
exactly where H131 said the plain beam fails (f.61's spans, cut by nulls into short runs) and costs two letters on the longer
f.108r lines. Not re-tuned (one weight, fixed before the run). For the verifier: on f.61 itself the lattice's within-pair
choices are about 0.9 right on known letters, the best figure any instrument has shown on this leaf, but on 49 positions and
below this step's pooled gate. No reading, no class change.

## Campaign step H138 (28 Sept 2026, 19:29-19:33 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_period.py --lattice` (option pushed 30bc3063 before the run; `f61beam_period_lattice_result.txt`): H133's scoring
against the period gloss letters with the H136 word-lattice beam in place of the plain beam.

| leaf | scored | lattice | plain beam (H133) | first-letter |
|---|---|---|---|---|
| f.101r | 1,420 | 1,091 = 0.768 | 0.737 | 0.561 |
| f.188r | 588 | 480 = **0.816** | 0.791 | 0.529 |
| pooled | 2,008 | 1,571 = **0.782** | 0.753 | 0.551 |

**GATE (>= 0.80 on >= 100 pooled): FAIL** by 0.018; f.188r alone clears 0.80. The lattice gains 3 points on both leaves over
the plain beam, as on f.61's spans (H136). With the automatic gloss alignment's slips counted as errors, 0.78 is a lower
bound on the instrument's choice accuracy in this hand. Not re-run. No reading, no class change.

## Campaign step H139 (28 Sept 2026, 19:34 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61lattice_dashes.py` -> `scripts/f61lattice_dashes.tsv`: of Tomokiyo's dash positions inside his five spans, only
**one** falls on a sign the 14 cells cover (S5, L11 pos 8, 4STEM a/n: lattice n, plain beam n -- "melente-noit" ->
"melentenoit" with n, which is his own letters list's reading of that span). Every other dash sits on a null or an
unmapped class (CA, C6, LL, CROSS, ZHOOK-free positions), so the within-pair instruments have nothing to add inside the
spans; f.61r's open questions are the unmapped classes and the two-way choices of key v4, not the 14-cell pairs.
No reading, no class change.

## Campaign step H140 (28 Sept 2026, 19:35-19:37 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61beam_f108r_predict.py --lattice [--f108v]` -> `scripts/f61lattice_f108r_prediction.txt`,
`scripts/f61lattice_f108v_prediction.txt`: the H136 word-lattice beam's resolutions of f.108r L04-L06 and f.108v, committed
as further pre-registered predictions before ASKS 88/89 land. They differ from the plain beam's (H120/H123) on a few letters
per line (f.108r L05 "atquin.em.isilznem." vs "ngquin..."). `scripts/f61score_gloss108.py` now scores the lattice prediction
too ("H140 lattice"); its selftest still PASSes (the synthetic gloss is H120's, so H140 scores 69/71 there by construction
of the test, not as evidence). No reading, no class change.

## Campaign step H143 (28 Sept 2026, 19:40-19:47 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe) -- key hunt, a new lead

Campaign rule (a). BnF Archives et manuscrits, one plain POST search (`resultatRechercheSimple.html`, "Mayenne chiffre
déchiffrement"): 119 results, page 1 (50) read; pagination needs a real browser (host table), not pursued. Beside the known
fr.3641 f.126 (H/F61-FAMILY-7: a figure cipher) and Nevers-papers letters about Mayenne (other senders), one lead in the
family's own correspondence: **Français 2751, fol. 116, item 45: « Lettre du sieur DE DIOU à monsieur le duc de Maienne,
... escripte en chiffre ». Déchiffrement de cette lettre** (ark:/12148/cc49202m/cd0e560; a recueil of pieces 1549-1599).
It is digitised (Gallica SRU: 1 record, ark:/12148/btv1b52523734p); the manifest gives f.116r = canvas f241, f.116v = f242.
Every image request for that ark returned **HTTP 403** (four, then one retry after 60 s), so the cloud stopped per the
good-citizen rule; whether the letter is in f.61's polyphonic signs is undetermined. Request written:
`family/REQUEST_fr2751.md` (a desk look at f.241-f.244, or a later cloud retry, H144). Requests this step:
archivesetmanuscrits 4, Gallica 7 (SRU 1, manifest 1, images 5 -- all 403), logged in `family/requests.log`.
Not a key, not a reading; no class change.

## Campaign step H141 (28 Sept 2026, 19:49-19:51 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61lattice_v4.py` (pushed a6699ad5 before the run; `f61lattice_v4_result.txt`): the H136 word-lattice beam on key
v4's two-way form with unread signs dropped rather than cut. **Lattice 23/42, plain beam 22/42** (H117, with cuts: 23/42)
-> **GATE (>= 34/42): FAIL**. Neither H117 cause was the limit: dropping the unread signs and adding a word model leave the
choice near chance, while the same instruments under the 14-cell pairs choose 0.78-0.90 right on the same leaf (H116, H136).
So the obstacle is v4's sets themselves -- up to seven letters per sign ([e/q/i/p/r/s/t], [n/a/c/e], [o/b/e]), wider than
the two-letter design Tomokiyo's table and the 14-cell map describe; within such a set a language model has too much
freedom. For the verifier: the two-way choices AUDIT.md sec. 6 item 1 counts are choosable with a control only where the
sign's set is a pair; widening the pairs is where v4 and the 14-cell map disagree, not a grading question. No reading, no
class change.

## Campaign step H145 (28 Sept 2026, 19:52-19:54 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only table

`scripts/f61v4_vs_14.py` -> `scripts/f61v4_vs_14.tsv` (`--check` fresh): per f.61 class, key v4's set on f.61 (frac 0.1), the
14-cell pair, and v4's pooled period counts. Where they differ:

- **Wider in v4 (a third period letter admitted at frac 0.1):** SBS o/b/**e** (period o 98, b 49, e 31), 4TRI c/p/**t**, 4PI
  d/q + **a/n**, 4STEM n/a + **c/e**, EBR l/s/a, OTHER seven letters, HASH4 d/q/**i** -- the sets that defeat any within-set
  choice (H117/H141).
- **A different second letter:** **VBAR_A t/s in v4 vs g/t in the 14 cells** (period t 179, s 93, g 21; six f.61 signs) and
  **VBAR_B s in v4 vs f/s** (period s 57, f 2) -- here v4 and the fit disagree on the cell itself, not on its width.
- **C6 e (v4) vs a/n (14 cells)**: VERIFY-F61-V4 regraded C6 on f.61 to unread/null (its three gloss tokens against
  Tomokiyo's dashes); both are weak.

So the gap H141 found has two parts: sets widened by the frac-0.1 rule (a presentation choice of v4's decode), and two genuine
cell conflicts (VBAR_A, VBAR_B) that the family pool can test with the H127 statistic (H146). No new key, no reading.

## Campaign step H146 (28 Sept 2026, 19:55-20:02 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61vbar_cells.py` (rule in its docstring, pushed dee63f1c before the run; `f61vbar_cells_result.txt`): H145's two
cell conflicts scored by sequence gain; family pool with 30 bootstrap resamples, f.108v and the known f.61 lines as is.

| map | pool gain | f.108v | known f.61 lines |
|---|---|---|---|
| VBAR_A g/t, VBAR_B f/s (14 cells) | 0.0874 | 0.1521 | 0.2546 |
| VBAR_A g/t, VBAR_B s | **0.0894** | 0.1521 | **0.2600** |
| VBAR_A t/s (v4), VBAR_B f/s | 0.0827 | 0.1409 | 0.2369 |
| VBAR_A t/s (v4), VBAR_B s (v4) | 0.0843 | 0.1409 | 0.2248 |

- **VBAR_A: g/t preferred over v4's t/s** on the pool (29/30 and 30/30 resamples, both VBAR_B settings) and higher on f.108v
  and on the known f.61 lines. v4's s for VBAR_A (period s 93) most likely comes from VBAR_B signs the family readers coded
  VBAR_A (the two differ only by a second bar), which H145's table cannot see.
- **VBAR_B: s alone preferred over f/s** on the pool (f/s wins 0/30) and on the known lines; f.108v cannot tell (no
  difference). Caveat: a one-letter set removes a choice, so this says only that f is rarely right under VBAR_B, not what
  VBAR_B's second letter is.

For the verifier and the family worker: on this evidence the 14-cell g/t stands for VBAR_A against v4, and VBAR_B is s
nearly always. Model-free, frequency-proof, out-of-sample on the family pool; not a period attestation and not a reading.
No class change.

## Correction: runner 5's section times (read from the clock, 28 Sept 2026, 19:19 UTC)

CLAUDE.md rule 6 breach, found when `date -u` read 19:19 at the end of H142: from H113 on, the UTC times in runner 5's section
headings above and in its CAMPAIGN.md log lines were typed, not read, and drift up to about 70 minutes ahead of the clock.
The push times from `git log origin/main` (one clock) are the record: H108 17:28, H111 17:34, H112 17:39, H114 17:40,
H115 17:41, H113 17:44, H116 17:46, H117 17:48, H118 17:49, H119 17:50, H120 17:50, H121 17:52, H122 17:53, H123 17:53,
H124 17:56, H127 17:59, H128 18:04, H126 18:05, H131 18:07, H129 18:23, H130 18:25, H132 18:33, H133 18:34, H134 18:35,
H135 18:36, H137 18:37, H136 18:38, H138 18:39, H139 18:40, H140 18:41, H143 18:45, H141 18:46, H145 18:47, H146 18:54,
H142 about 19:20. No figure or result is affected; ROOM.md's own lines carry machine stamps.

## Campaign step H142 (28 Sept 2026, pushed about 19:20 UTC, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61swap_noise.py` (rule in its docstring, pushed 7958a270 before the run; `f61swap_noise_result.txt`): H132's 15
closest one-swaps on 30 bootstrap resamples of the family pool. **Only INF<->SBS and 4PI<->SBS are confirmed rejected
(29/30); the other 13 are OPEN** (fitted map wins 9-28 of 30), including 4STEM<->4TRI (16/30) and the one H132 "preferred",
EBR_A<->ISH (the fitted map wins 9/30). So H132's "128 of 129 rejected" holds for the swaps with clear margins, but the
closest 13 are within the pool's resampling noise; the family pool cannot yet decide them. The same bootstrap gave the H146
VBAR results 29-30/30, so those stand. No reading, no class change.

## Campaign step H147 (28 Sept 2026, 19:20-19:21 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61refined_known.py` (pushed e4425175 before the run; `f61refined_known_result.txt`): the known-answer scores under
the map refined by H119/H146 (HASH4 = i/x, VBAR_B = s alone). Refined: lattice 110/125 (f.61 spans 43/49, f.108r overlay
67/76), plain 106/125; unrefined: lattice 111/125 (44/49, 67/76), plain 107/125. **GATE (>= 113, no text worse): FAIL** --
the refinement costs one known letter on f.61's spans and gains nothing on f.108r. The family-pool preferences of H146 do not
carry to the known texts at this size; the refined cells stay a family-key candidate, not a change to f.61's map. No reading,
no class change.

## Campaign step H148 (28 Sept 2026, 19:21-19:31 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61v4_widen.py` (rule in its docstring, pushed 2042a6d6 before the run; `f61v4_widen_result.txt`; `f61hash4_108r.resolve`
generalised to sets of any size in the same commit, every earlier pair result `--check` fresh): each key-v4 widening added
alone to the pool map, sequence gain on 30 bootstrap resamples of the family pool.

- **REJECTED** (widened wins <= 1/30): SBS b/o/**e** (0/30), 4PI d/q/**a/n** (1/30), HASH4 d/q/**i** (0/30).
- **OPEN**: 4TRI c/p/**t** (6/30), 4STEM a/n/**c/e** (7/30) -- leaning against, not decided.

So the text does not want v4's third letters: three of the five widenings are rejected and none is supported. v4's wide sets
(H145) come from its frac-0.1 admission rule letting in period letters that are gloss-alignment noise or reader coding merges,
which is why the within-set choice on v4 failed (H117/H141). For the family worker: evidence to keep these classes at two
letters in a key v5. No reading, no class change.

## Campaign step H149 (28 Sept 2026, 19:32 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), writing

`family/PROPOSAL_H146.md`: candidate edits for a key v5 with their evidence (H119, H129, H132, H142, H146, H147, H148),
for the family worker to weigh; nothing applied to KEY.md or any key file. No new claim.

## Campaign step H150 (28 Sept 2026, 19:34 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), count only

Occurrences of f.61's unmapped classes over the texts in f.61's hand on disk (f.61 span lines, f.108v H59 draft, f.108r
L04-L06 H108 draft, f.108r L02/L03 of the joint fit): **CA 8, C6 6, LOOPBAR 4, CROSS 3, ELOOP 2, LL 1** (ZHOOK 40 is mapped,
i/x, published). None reaches the pre-registered 10 -> **every rare class untestable by sequence gain on this material**;
no value computed. AUDIT.md sec. 6 item 2 stands: these classes wait on more text in this hand or a period key sheet (the
fr.2751 f.116 lead, H143/H144, is de Diou's hand, not f.61's). No reading, no class change.

## Campaign step H151 (28 Sept 2026, 19:34-19:39 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61vbar_repl.py` (pushed 82c61573 before the run; `f61vbar_repl_result.txt`): H146's VBAR_A g/t vs key v4's t/s on a
fresh bootstrap and leaf by leaf. **Pooled: g/t wins 41/50** (gate >= 48); leaves: g/t higher on f.97r, f.101r, f.188r,
t/s higher on f.124r (3 of 4). **DOES NOT STAND** as pre-registered: H146's 29/30 does not replicate at the 95% level (41/50
= 82%). VBAR_A g/t is a lean, not a result; `family/PROPOSAL_H146.md` is corrected to say so. No reading, no class change.

## Campaign step H152 (28 Sept 2026, 19:40-19:42 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61seqgain_108v_boot.py` (pushed 9948e9f7 before the run; `f61seqgain_108v_boot_result.txt`): 30 bootstrap resamples
of f.108v's seven lines, the fitted 14-cell map's sequence gain ranked among 50 permuted maps in each. **Rank 1 in 29 of 30
(once rank 2) -> STANDS** (gate >= 27). H127's "f.108v is enciphered in f.61's cells" survives resampling of its lines. No
reading, no class change.

## Campaign step H153 (28 Sept 2026, 19:44 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), writing

`scripts/H66_PAGE.md` gains a section "H135-H152". No new claim.

## Campaign step H154 (28 Sept 2026, 19:45-19:49 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61seqgain_108v_boot.py --f108r [--hash4-ix]` (options pushed 38331d4b before the run; results
`f61seqgain_108r_boot_result.txt`, `f61seqgain_108r_boot_ix_result.txt`; the result files print the shared gate's name
"H152"; the f.108v default re-checked fresh): H152's bootstrap on f.108r L04-L06's three lines.

- HASH4 dropped: fitted map rank 1 of 51 in **5/30** resamples (median rank about 3) -> does not stand.
- HASH4 = i/x: rank 1 in **20/30** (median 1; two resamples at 17 and 28) -> does not stand (gate 27).

So "f.108r L04-L06 in f.61's cells" is a lean, strongest with HASH4 = i/x, not a result that survives resampling its three
lines -- unlike f.108v (29/30, H152). With three lines, a resample often drops the one that carries the signal (L06, H119).
The f.108r predictions stay committed; the person's gloss (ASKS 88) remains the test. No reading, no class change.

## Campaign step H155 (28 Sept 2026, 19:50-19:52 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61108v_rows.py` (pushed 5acfe7c9 before the run; `f61108v_rows_result.txt`): per f.108v row, the fitted map's
sequence gain rank among 200 permuted maps: L06 1, L04 2, L01 2, L03 7, then L07 38, L05 40, L02 55 (single rows, one seed;
each row 34-42 covered signs). The ASKS 89 desk pack (`images/person_pack_108v/README.md`) gains a reading order note
(L06, L04, L01, L03 first) with no letters in it. Rows L02, L05, L07 fit no better than chance alone -- a transcription or
null question for the verifier, the same rows H101 found weakest by the judge (L05). No reading, no class change.

## Campaign step H157 (28 Sept 2026, finished 19:52 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61zhook_108v.py` (pushed 7bb5fccf before the run; `f61zhook_108v_result.txt`): ZHOOK's value on f.108v (20
signs) by sequence gain, 30 bootstrap resamples of the leaf's lines. **i/x beats a/e, a/u, e/u and null in 30/30 resamples
each -> i/x CONFIRMED against all four.** The held f.108v alignment's a/e/u reading of this sign (the H44-era note) does not
fit the text; Tomokiyo's i/x (from his markup and his f.108r reprint) does, on a leaf he did not mark. Model-free support for
a published value, not a period attestation. No reading, no class change.

## Campaign step H156 (28 Sept 2026, finished 19:53 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), diagnostic

Per f.108v row of the H59 draft (`family/passes/f108v3z_draft_reconciled.tsv`): signs 41-47, grade H 7-11 / M 28-35 / L 1-6,
reconciled columns 13-19, uncovered 2-7, SBS 0-3. The three rows at chance under f.61's cells (H155: L02, L05, L07) are **not
distinguished by transcription grade, reconciled share or coverage**: L05 has the fewest L columns (2) and uncovered signs (2)
of all seven; only L02 carries more HASH4 (4, dropped by the map) than the rest. So the weak rows are not a re-read target on
this evidence; the likelier causes (proper names, figures or code words inside the enciphered stretch, or single-row noise at
about 40 signs) cannot be told apart without the gloss (ASKS 89). No reading, no class change.

## Campaign step H158 (28 Sept 2026, 19:5x-20:08 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61family_boot.py` (design scaled and fixed in its docstring, pushed fc5b65e2 before the run;
`f61family_boot_result.txt`): each family leaf's lines resampled 20 times, the fitted 14-cell map's sequence gain ranked
among 20 permuted maps each time. **f.97r ROBUST (19/20), f.188r ROBUST (20/20); f.101r EDGE (17/20), f.124r EDGE (17/20);
f.106r OUT (8/20), f.274 OUT (6/20).** H129's six "in f.61's cells" hold robustly for the two leaves of f.61's cipher family
with the most text per line pattern (f.97r, f.188r), nearly for f.101r and f.124r, and not for the two short leaves (240 and
167 signs), where the rank-1 of H129 was not robust -- a length limit, not evidence of another key. For the family worker.
No reading, no class change.

## Campaign step H160 (28 Sept 2026, finished 20:09 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61zhook_108v.py --hash4` (option pushed ae81249b before the run; `f61hash4_108v_result.txt`; the ZHOOK default
re-checked fresh): HASH4 on f.108v (14 signs) by sequence gain, 30 bootstrap resamples. **i/x vs d/q: i/x wins 6/30 (OPEN,
leaning d/q); i/x vs null: 20/30 (OPEN).** On f.108v the family value d/q leans ahead of the i/x that fitted f.108r best
(H118/H119, itself only a lean, H154) -- consistent with the passes' HASH4 lumping two forms (bare hash, period i; 4-over-hash,
period d/q, H98) in different proportions on the two leaves. Nothing decided; a sign-shape split of HASH4 on these leaves
(the H98 tile design) is what would separate them. No reading, no class change.

## Campaign step H161 (28 Sept 2026, finished 20:17 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61zhook_pool.py` (pushed 7901599c before the run; `f61zhook_pool_result.txt`): the H157 ZHOOK test on the family
pool. The pool carries **only 5 ZHOOK signs** in 9,611 (the family passes code this hand's z-shapes as ZBAR, f/s by KEY.md).
By the pre-registered wording a/u (i/x wins 0/30) and e/u (1/30) come out "preferred" and a/e, null open -- but on five signs
a bootstrap resamples the same handful of positions, and each swap moves at most five letters in 8,500: a test with almost
no power (rule 3's "control that cannot vary" shape at this n). **Logged as untestable on the pool at n = 5**, not as
evidence against i/x; H157's f.108v result (20 signs, 30/30 for i/x) stands for f.61's hand. No reading, no class change.

## Campaign step H159 (20:18 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), writing

`scripts/H66_PAGE.md` gains a section "H153-H161". No new claim.

## F61-FAMILY-8: BnF fr.2751 f.116 (de Diou to Mayenne, "escripte en chiffre"), 28 Sept 2026, 20:16-20:20 UTC by the clock (owner account, parent worker)

Brief: .claude/briefs/runs/2026-09-28-parent-f61-family-8.md (steps 2-4 of F61-FAMILY-7). Images: 7 page images at 1200 px (canvases f241-f247 = f.116r-f.119r), committed in family/fr2751/; 3 native fetches (f241-f243) kept in the scratchpad only (30 MB rule; regen `python3 family/fetch_gallica.py btv1b52523734p 24N full OUT`). 10 Gallica requests, all HTTP 200, 2 s apart, in family/requests.log. Two native crops of the residual marks: family/fr2751/f242_marks_row20.jpg, f243_marks_rows1-2.jpg. No vision subagent calls; own looks only.

**Result: a clean negative for the key hunt.** The item (f.116r-f.119r) is a later fair copy (17th-century italic book hand, a volume of copies) in **clear text only**. Its heading reads "Lettre du sieur de Diou a Monsieur le Duc de Maienne, lieutenant general de la couronne et Estat de France, escripte en chiffre, lequel signifie tout ce qui s'ensuit". So the finding aid's "Déchiffrement de cette lettre" is this copy itself. There is no cipher text on any of the seven pages: no polyphonic signs, no loops on stems, no 4-shapes, no barred triangles. The copy ends on f.119r: "Vostre treshumble et tresobeissant serviteur de Diou", "De Rome le 5 d'avril 1592", "Scellee d'un cachet", followed by a postscript naming letters from Cardinal Sfondrato.
- Same cipher as f.61? **Not testable from this item.** The original cipher letter is not here, and no sign of key v4's classes appears.
- Where is the decipherment? The whole item is the decipherment, as a copy. There is nothing to align it against.
- Signs aligned 0; agreement with v4 n/a (0/0); rare classes (CA, CROSS, LL, LOOPBAR, ZHOOK, C6) glossed: none; v4 two-way cells decided: 0. No key_period_fr2751_v1.tsv was built, because there is no cipher and gloss pair.

**What the copy does carry (recorded, not interpreted beyond grade I).** About 20 isolated marks are set between dashes inside the clear text, where the copyist evidently reproduced nomenclator name marks from the original. Examples: "Ambassade -- ‡ -- d'Espagne ≡" (f.117r row 2; again f.118r), "Cardinal Caietan -- & --" / "-- s --" (f.117r rows 1-2), "ce secours de mil -- :. -- six mille -- c -- &" (f.116v), "la Religion -- R/ --" (f.117r, f.118r), "le Pape -- G. --" and "du feu Pape -- G. Sixte" (f.118v), "-- A --", "-- π --" (twice, "Cardinal -- π --"), "-- ⊖ --", "-- o --", "-- 8 --". These are code marks for names and titles, not the letter-level polyphonic signs of f.61, and nothing in the copy glosses them independently.

**Date (grade I, inferred).** The copy dates the letter 5 April 1592. The content fits spring 1591 better:
- The pope is convalescent and his nephew is "le Cardinal" (Sfondrato).
- "le feu Pape Sixte" is dead.
- The "monitoires" and "le comte Sfondrato" with Italian and Swiss levies point to Gregory XIV's expedition.
- Someone "y entra le deuxiesme de Mars" at Marseille and then embarked "avec Monsieur le President Jeannin ... pour passer en Espagne".

Those details are consistent with Gregory XIV (Dec 1590-Oct 1591) and Savoy at Marseille in March 1591. This is unverified; the copy's own year stands as written.

**Named next step (one line, not run):** find the ciphered original of de Diou's Rome letter of 5 April [1591/1592] among the Mayenne papers (fr.3977-3984 or the fr.4715-type recueils). If it is in the polyphonic cipher, this copy is a full-length period clear text for it: a known-plaintext alignment of the fr.101r kind over roughly 150 copy lines, with the name marks as a bonus.

## Campaign step H162 (28 Sept 2026, 20:1x-20:21 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe)

One Opus vision call (the reader read the five sheets only; reply verbatim `scripts/read_call_H162.tsv`; tiles and prompt
pushed b0d19a43 before the call; `scripts/f61hash4_forms.py score`, `f61hash4_forms_result.txt`). Controls (H98's
period-labelled tiles) **17/20 -> gate PASS** (misses: one period-d tile called "no", one period-i called "yes", one "none").
Targets: **23 of 24 HASH4 signs have a 4 above or joined** (f.108v 14/14; f.108r 9/10) -- the 4-over-hash, d/q on the family
leaves; one f.108r sign (L06/7) is a bare hash. So the passes' HASH4 on these leaves is almost entirely one form, and H160's
lean to d/q on f.108v fits it. H119's i/x lean on f.108r is then not the bare-hash i: on f.108r L06 the reader describes most
of these as "4-like apex, looped feet" (the passes' "crossed double loop, alt INF"), a looped variant whose value is open.
H163 (split values) is moot: a split moves one sign. No reading, no class change.

## Campaign step H164 (28 Sept 2026, finished 20:23 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only

`scripts/f61lattice_seqgain.py` (sizes amended and pushed 40f460cb before the run; `f61lattice_seqgain_result.txt`): the
sequence gain with the word-lattice resolution (10 shuffles, 100 permuted maps). Control, known f.61 lines: gain 0.161,
**rank 3 of 101 -> PASS** (weaker than the plain beam's rank 1: the lattice's word bonus lifts shuffled text too).
**f.108r L04-L06 (HASH4 = d/q per H162): rank 8 of 101 -> FAIL** (gate 5). The lattice does not make the f.108r evidence
stronger; it stays a lean (H154). No reading, no class change.

## Campaign step H165 (28 Sept 2026, 20:24-20:27 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe) -- key hunt, a lead

BnF Archives et manuscrits searches ("Diou Rome chiffre", "Diou avril 1592", "Diou avril 1591", "Diou chiffre"; 6 requests) and
Gallica (1 manifest via `tools/gallica_folio.py`, 5 image requests, all 200), logged in `family/requests.log`.
- The Rome letter of 5 April: a second copy only, **Français 5045 fol. 275, item 125, "5 avril 1591. Copie."** -- the finding
  aid dates it 1591, as F61-FAMILY-8 inferred from content; no ciphered original found in fr.3982-3984's cipher items.
- **Lead: Français 3984, fol. 7, item 4 -- Mayenne to de Diou, Paris, 13 May 1593, "avec chiffre et déchiffrement"**
  (cc504266/cd0e19002). Not among the family leaves in KEY.md. Gallica canvas f15 (inferred fol. 7r) is a full page of cipher
  runs mixed with clear lines in the polyphonic family's signs (4-shapes, barred triangles, loops on stems, 4-over-hash, the
  "(a)" mark); canvas f17 is a page of clear text (possibly the decipherment), f21 the address to de Diou. Same correspondents,
  same months as f.108r/v (Mayenne to de Diou, Feb-Mar 1593). Images in `family/fr3984_f7/` with a README.
Whether the cipher runs are f.61's own cells, and whether f17 deciphers them, is not checked here (H168). No key, no reading.

## Campaign step H167 (28 Sept 2026, finished 20:27 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only, descriptive

`scripts/f61l06_loophash.py` (pushed 15e2ea9f before the run; `f61l06_loophash_result.txt`): f.108r L06 alone (40 signs,
10 "HASH4", mostly the looped 4-over-hash of H162), sequence-gain rank among 200 permuted maps by HASH4 value: **h/u rank 1**
(gain 0.313), i/x rank 3 (0.212), d/q rank 27 (0.084), dropped rank 60. The passes' own note on these signs, "crossed double
loop, alt INF", points the same way (INF = h/u). Four values on one line of 40 signs, no gate: descriptive only -- a question
for the person's gloss of L06 (ASKS 88) and for the family worker (whether the looped hash is a separate class from the
4-over-hash d/q). No reading, no class change.

## Campaign step H166 (20:28 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe), writing

`scripts/H66_PAGE.md` gains a section "H162-H167". No new claim.

## Campaign step H168a (28 Sept 2026, 20:47-20:48 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe)

fr.3984 canvases f15 and f17 at 2000 px (2 Gallica requests, 200; `family/fr3984_f7/c15_2000.jpg`, `c17_2000.jpg`), one Opus
vision call (read the two images only; reply verbatim `scripts/read_call_H168a.tsv`; prompt pushed 079ce253 before the call).
f15's one long clear stretch (the Suresnes conference delegates: "Messieurs l'Archevesque de Lyon, l'Evesque d'Avranches,
l'Abbé de St Vincent de Laon ... le Baron de Talmay ... de ma part les Srs de Villars, de Villeroy ... Jeannin") **does not
appear on f17**; f17 is continuous prose about religion, the crown and the people. **Gate (>= 3 clear lines of f15 found in
f17 in order): FAIL** -- f17 is not the page-for-page decipherment of f15. The finding aid still says "avec chiffre et
déchiffrement", so the decipherment may be on another canvas (f16, f18, or a separate sheet near the item); H168 is re-scoped
to locate it first. Readings provisional (small hand, reduced image). No key, no reading.

## Campaign step H168b (28 Sept 2026, 21:46-21:46 UTC by the clock, runner 5 session_01RbeePKZVn83gNfES8yFmhe)

Nine 600-px thumbnails of fr.3984 (canvases f13, f14, f16, f18, f20, f22-f25; Gallica, 9 requests, all 200;
`family/fr3984_f7/thumb600_c*.jpg`), one contact sheet looked at by the runner. By eye, provisional:
- **f14 = fol. 7r** (a "7" at the top right): a dense full page of cipher runs; **f15 = fol. 7v**, its continuation (cipher runs
  and the Suresnes clear lines).
- **f16-f18: clear pages** (f16 with a date line at its head, apparently "13 may 1593"; a "9" at the top right of f18): the likely
  decipherment of fol. 7r-v, starting at f16 -- which is why H168a found f15's clear stretch absent from f17 (the order runs
  f16 -> f18, and f17 need not face f15).
- f13 and f19/f21: address and docket leaves; f20: a clear page signed "Charles de Lorraine" (another item);
  f22-f23: clear letters; **f24-f25: further dense cipher pages** (a later item, not identified here).
For H168: compare f15's Suresnes delegates list against f16 and f18 (not f17) first. No key, no reading.

## Campaign step H168 (28 Sept 2026, 22:15-22:24 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- dropped: not f.61's design

Re-scoped from the orchestrator's 22:14 brief: confirm that fr.3984 fol. 7 (canvases f14-f15, Mayenne to de Diou, Paris, 13 May
1593) is written in f.61's polyphonic design and that f16-f18 is its aligned period decipherment, then passes and a key.
- **Fetch:** canvases f14, f16, f18 at 2000 px (3 Gallica requests, all 200, `family/requests.log`; `family/fr3984_f7/c14_2000.jpg`,
  `c16_2000.jpg`, `c18_2000.jpg`; f15/f17 already on disk from H168a).
- **Decipherment (by eye, runner):** f16 (fol. 8, headed "13 de May 1593") opens "Mons.r le Comandeur, la depesche que je ..." where
  fol. 7r opens "Monsieur le Commandeur" + cipher. It renders only the cipher runs, not fol. 7's clear lines (the army near
  St Quentin, the Reims meeting with Lorraine, Aumale and Elbeuf, the Suresnes delegates), and so it skips them. That is why H168a's
  clear-line gate found nothing on f17: the gate's premise was wrong, and H168a's FAIL says nothing about f16-f18.
- **Design check, pre-registered** (`family/fr3984_f7/h168/PROMPT_DESIGN.md`, pushed 6304123c before the calls): two blind Opus vision
  calls, same prompt: list the query's 12 commonest signs and mark each as found or not in a family reference (f.61 sheets L03/L05 +
  an fr.3982 f.101r strip); gate >= 8/12 YES.
  - Control, fr.3984 f.188r (a family leaf in key v4): **5/12 YES (7 UNSURE), below the gate**, so the test is a **non-test**
    (rule 3). The reader blamed the coarse strip. Its sentence (4): "the same sign system".
  - Target, fr.3984 f14: 3/12 YES. Sentence (4): "probably a different sign system ... each image's most characteristic signs (ф, ♀
    and '43' in REFERENCE; A, (a), ‡ and '::' in QUERY) do not appear in the other". Replies verbatim: `h168/reply_C_f188r.txt`,
    `reply_T_f14.txt`. Both descriptive only.
- **Settled from the folder's own record, not by the test:** Tomokiyo's mayenne.htm, section "Duke of Mayenne Forsook Polyphonic
  Substitution" (`sources/cryptiana/web/mayenne.htm`, on disk since H3, image `web/img/mayenne3.png`), says Mayenne "used a more
  conventional homophonic substitution cipher in May 1593 in writing from Paris to the same recipient (BnF fr.3984, ff.7-10)". It
  names BnF fr.3995 no.55 as that cipher's original table and says "the decipherment on a separate sheet (f.8) omits the few lines of
  the second portion in cipher (f.7)". nevers.htm no.55 says the same. The H3 manifest row for mayenne3.png already read "the
  DIFFERENT homophonic cipher of BnF fr.3984 ff.7-10 ... not this target's cipher".
- **Result: fol. 7 is not in f.61's polyphonic design. No passes, no `key_period_fr3984_v1.tsv`**. A key for a different cipher
  cannot decide any of key v4's 59 two-way cells or rare classes. 2 vision calls spent of 6.
- **Correction (rule 10, postmortem):** H165's "in the polyphonic family's signs" and `family/fr3984_f7/README.md`'s "the signs are
  the polyphonic family's" overstated. Both rest on shared generic forms (4-shapes, the "(a)" mark), and the published record says
  otherwise. README corrected in this step. The lesson for the loop: before chasing a new leaf, grep `sources/cryptiana/` for its
  folio. Here that grep answers in one line.
- **What it opened:** mayenne.htm lists fr.3984 **f.176** (Desportes to Clement VIII, 22 July 1593) as polyphonic, "Deciphered on a
  separate sheet". The finding aid (NOTES F61-FAMILY table: item 84, "chiffre et déchiffrement") agrees, and `family/KEY.md` still
  marks that sheet "not located". Row H169 takes it. f.186 and f.189 (undeciphered, same design) are pool for a keyless step.

## Campaign step H169 (28 Sept 2026, 22:23-22:25 UTC by commit times, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- the f.176r decipherment located (candidate)

H168's lesson applied first: `grep 176 sources/cryptiana/` finds only mayenne.htm's line "(f.176) Baudouin-Desportes to Pope
Clement VIII, Paris, 22 July 1593. Deciphered on a separate sheet." It gives no folio for the sheet. 600-px thumbnails of fr.3984
canvases 322-326 and 328-334 (12 Gallica requests, all 200, `family/requests.log`; `family/images/thumb_3984_c*.jpg`), one contact
sheet looked at by the runner (no subagent), then canvas 326 at 2000 px (1 request, `family/images/3984_f175r_2000.jpg`). 13 requests.
By eye, provisional:
- **c326 = fol. 175r: a clear French page headed "22 de Juillet 1593"**, the date of f.176r, placed just before it. It carries a
  one-word title (unread) and opens "depuis mes dernieres, on n'a proposé l'archiduc ... on nous a pressés de vouloir promptement
  declarer Roy et proprietaire de cette couronne l'Infante ... au Roy d'Espagne ...". This is the Estates' debate on the Infanta,
  the matter of a July 1593 letter to Rome. **It is the leading candidate for the separate-sheet decipherment of f.176r.**
- c327-c328 = f.176r-v: headed "22 de Juillet 1593 / Tres saint pere", then cipher throughout in the family's signs (loops and
  circles on stems, 4-shapes, square brackets). That design match is by eye and backed by Tomokiyo's listing, unlike H168's.
- c329-c331 = fol. 177-178: clear pages in another hand (not identified). c332: a small docket leaf. c333 = **fol. 179: a full page
  of cipher in what look like the family's signs, not in Tomokiyo's list** (by thumbnail only). c334: an address leaf. c322-c324:
  Italian clear pages (fol. 173-174). c325: a docket.
- **Not yet shown:** that fol. 175 renders f.176r's cipher rather than one of Desportes's three other letters of 22 July (f.186 to
  Aldobrandini, f.189 to Frachetta; f.184 is already f.188's). That alignment gate is H170's first step. No key, no reading.

## Campaign step H170 (28 Sept 2026, 22:26-22:36 UTC by commit times, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- alignment gate FAIL (not shown)

Pre-registered in `family/passes/PROMPTS_f176_f175.md` with the scorer `family/h170_gate.py` (pushed 46228d45 before any call).
Native f.176r (canvas 327) and fol. 175r (canvas 326), fetched once each (2 Gallica requests, 200; not committed, 4-5 MB each),
plus one 2000-px f.176r (1 request, superseded by the native and deleted). Crops: `family/sheets/f176r/` (4 cipher rows, native
px, about 117 px high), `family/sheets/f175r/` (8 clear lines). Three Opus vision calls:
- blind sign passes A/B of f.176r L01-L04 (`passes/f176r_signs{A,B}_h170.tsv`): 261 / 263 rows (PLAIN at the start of L01, not
  read). Every sign graded m or l. The passes disagree on major classes: A codes 27 ZHOOK where B codes 24 C43, and B has
  HASH4 10 / 4STEM 10 where A has 4PI 9. Not reconciled (the gate scores each pass separately).
- blind read of fol. 175r L01-L08 (`passes/f175r_clearA_h170.tsv`, 688 letters; lines graded l/m): "Depuis [mon] [dernier]
  decembre, on no^s a propose Larchiduc ... apres on no^s a presse de voulloir promptemen declarer Roy et proprietaire de ceste
  couronne, l'Infante et celluy [qu'elle] ... prenne francois quil plairoit au Roy despagne ...".

`h170_gate.py` (result `family/h170_gate_result.txt`, `--check`):

| pass | signs (v4 coverage) | N | fol. 175r | wrong: f.184r @0 / @120 | 200 permuted keys mean / p95 / max | gate |
|---|---|---|---|---|---|---|
| A | 260 (0.87) | 208 | 0.399 | 0.413 / 0.361 | 0.319 / 0.404 / 0.433 | FAIL |
| B | 261 (0.95) | 208 | 0.385 | 0.452 / 0.389 | 0.334 / 0.413 / 0.471 | FAIL |

**GATE FAIL on both passes: that fol. 175r renders f.176r's head is not shown.** The candidate does no better than another letter
of the same writer and day, or than permuted keys. This is not a negative on the pairing. The scorer's power at N = 208, on two
unreconciled m/l-grade passes, has no positive control (rule 3: a failure needs a matched control that reads). Two other readings
remain open: fol. 175r may render a different 22 July letter (f.186r or f.189r); or it may begin at a different point from
f.176r's first cipher row (the DP is local on the signs but must consume all N letters). No key rows, nothing merged. Row H173
(the scorer's positive control on the known pair f.188r/f.184r, script-only on disk) is added, and H170's continuation waits on it.

## Campaign step H173 (28 Sept 2026, 22:36-22:38 UTC by commit times, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- H170's statistic has power; its FAIL stands

`family/h173_power.py` (design pre-registered in its docstring, pushed 3687c5b5 before the run; result `family/h173_power_result.txt`,
`--check`). Script-only, no calls. The known pair is fr.3984 f.188r (its blind passes A/B from F61-FAMILY-3, sign grades mostly m,
like H170's) against its clear f.184r, under key v4 **without f.188r's own rows** (f.101r + f.274r only). Two all-cipher windows of
four rows (W1 L19-L22, W2 L08-L11). Everything else is H170's statistic, N and gate.

| window | pass | N | true clear | wrong: fol. 175r / other window | permuted p95 / max | gate |
|---|---|---|---|---|---|---|
| W1 | A | 210 | **0.648** | 0.329 / 0.386 | 0.400 / 0.490 | PASS |
| W1 | B | 191 | **0.581** | 0.335 / 0.366 | 0.393 / 0.461 | PASS |
| W2 | A | 186 | **0.575** | 0.392 / 0.355 | 0.403 / 0.462 | PASS |
| W2 | B | 187 | **0.594** | 0.374 / 0.374 | 0.396 / 0.535 | PASS |

On a true separate-sheet pair, H170's statistic separates the right clear from wrong clears of the same key and period by
0.19-0.28 at N of about 200, on passes of the same grade. **H170's FAIL therefore stands as a control-backed result: fol. 175r's
opening does not render f.176r's first four cipher rows** (f.176r scored 0.385-0.399, inside the wrong-text band). Still open: fol.
175r is the decipherment of another 22 July letter, or f.176r's decipherment is elsewhere (fol. 177-178 are clear pages in another
hand, H169). H174 is re-scoped to include fol. 177r.

## Campaign step H174 (28 Sept 2026, 22:38-22:39 UTC by commit times, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- the pairs by eye

The 1600-px references of f.186r and f.189r already on disk (F61-FAMILY), and fol. 177r (canvas 329) at 2000 px (1 Gallica request,
200; scratch, not committed). By the runner's eye, provisional:
- **fol. 177r opens "Tres saint pere / Les larmes aux yeux et l'ame plaine de desespoir, j'oseray dire a V. Sainteté ..."**, f.176r's
  salutation ("Tres saint pere", its only clear words), with underlined stretches as on f.184r (the decipherer's mark). It is **the
  lead candidate for f.176r's separate-sheet decipherment**; fol. 175r was the wrong sheet (H170/H173).
- f.186r (to Aldobrandini) opens in clear, "Illustrissime Monseigneur, Si je n'ay escript à Sa Sainteté ...": not fol. 175r's text.
- f.189r (to Frachetta), headed "[Ju]illet 1593", is cipher from its first row, so **fol. 175r ("Depuis mes dernieres ...") may be
  its decipherment**.
Rows H175 (fol. 177r vs f.176r with the passes on disk, one read call) and H176 (fol. 175r vs f.189r) follow.

## Campaign step H175 (28 Sept 2026, 22:39-22:41 UTC by commit times, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- fol. 177r deciphers f.176r: gate PASS

Pre-registered in `family/passes/PROMPTS_f176_f175.md` section H175 (a6d9a6c3), with one amendment logged before the call
(d34ca3f7: the clear salutation dropped from the candidate). Native canvas 329 fetched once (1 Gallica request, scratch), crops
`family/sheets/f177r/`. One Opus vision call: blind read of fol. 177r L01-L08 (`passes/f177r_clearA_h175.tsv`, 564 letters, lines
graded m/l): "Tressainct pere / Vn larme aux yeux et lame plaine de desespoir, Je [scay] dire a v^re sainctete [ql] me desplaist
infiniment. Elle ayt a me trouuer si veritable sur ce que tant de fois [ie] [luy] [ay] asseure que ce que le R. dhespaigne ... sa
fille Royne de france ... du Roy de Nauarre ...". `family/h175_gate.py` (result `h175_gate_result.txt`, `--check`) on the two
f.176r passes of H170, key v4, h170_gate.py's statistic and gate:

| pass | N | fol. 177r | wrong: f.184r @0 / @120 / fol. 175r | 200 permuted mean / p95 / max | gate |
|---|---|---|---|---|---|
| A | 208 | **0.577** | 0.413 / 0.361 / 0.399 | 0.337 / 0.409 / 0.447 | PASS |
| B | 208 | **0.606** | 0.452 / 0.389 / 0.385 | 0.359 / 0.442 / 0.500 | PASS |

**GATE PASS on both passes: fol. 177r renders f.176r's first four cipher rows.** The margin over the best wrong text is
0.16 / 0.15, and the scores sit in the range the true f.188r/f.184r pair gave under the same statistic (H173: 0.58-0.65). f.176r
(Baudouin-Desportes to Clement VIII, Paris, 22 July 1593, in the polyphonic design per Tomokiyo) and its separate-sheet period
decipherment fol. 177r(-178?) are therefore a **second separate-sheet known-plaintext pair for the family key**, after
f.188r/f.184r. Key source: `period`. What this is not: no key row is built yet, and nothing is merged into v4. The statistic is a
test of the pairing, not a reading. Next, H177: full passes of f.176r-v, a read of fol. 177r-178, and alignment into
`family/key_period_f176.tsv` by align_separate.py's rule. Then the report against v4's two-way f.61 cells and rare classes. The
merge is a verifier's.

**Time correction (runner 6, 22:43 UTC by `date -u`):** the H169-H175 headings and CAMPAIGN log lines of this runner first carried
times estimated by the runner (up to 40 minutes ahead of the clock, rule 6); they are now replaced by the commits' own times
(`git log`, one clock). No result changes.

## Campaign step H177a (28 Sept 2026, 22:43-22:53 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- key rows from f.176r/fol. 177r, stage 1 (rows L01-L12)

Pre-registered in `family/passes/PROMPTS_f176_f175.md` section H177a (eb601579). The builder `family/build_f176_key.py` was pushed
(491b48f8) before the stage-1 rows were read. Natives: canvases 328, 330 and 331 fetched once each (3 Gallica requests; 327 and 329 on
hand), scratch only. Band boxes are committed (`family/sheets/f176r_full/`: 47 cipher rows; `family/sheets/f177r_full/`: 34 clear
lines, centres set by eye on a ruler because line finding failed on the underlines). The crops are not committed (the folder is over
30 MB). Three Opus vision calls: blind sign passes A/B of f.176r L05-L12 (`passes/f176r_signs{A,B}_L05-L12.tsv`, 519 / 523 signs,
m/l; the readers could not separate EBR_A from EBR_B and coded every bracket EBR_B), and a blind read of fol. 177r L09-L20
(`passes/f177r_clearA_L09-L20.tsv`, mostly l-grade). With H170's L01-L04 passes and H175's L01-L08 read, stage 1 covers f.176r
L01-L12 against fol. 177r L01-L20.

Method (the builder's docstring). A∩B consensus signs only (82%; a disputed column never matches and never yields a row). Key v4's
letter sets decide only where signs and letters line up; the letter of each class comes from the period decipherment. Control: the
same pipeline on a wrong clear (fr.3984 f.184r, same writer and day, same N). Result: `family/build_f176_key_result.txt`; rows
`family/key_period_f176.tsv` (leaf `fr.3984 f.176r/f.177r`, `--check`).

**Whole stretch (788 signs, N 630 letters): fol. 177r 0.586 vs the wrong text 0.365, margin +0.221.**

| class (passes' code) | v4 set | fol. 177r (true) | f.184r (wrong) | in-set share true / wrong |
|---|---|---|---|---|
| PHI | e/r | e 81, r 33 (130) | e 59, r 20 ... (147) | 0.88 / 0.54 |
| 4TRI (4HOOK merged, no atlas code) | a/c/n/p/t | a 34, n 23, p 5, c 4, t 3 (78) | n 15, t 10, a 8 ... | 0.88 / 0.54 |
| VBAR_B | s | **s 41** (53) | s 12, e 9 ... | 0.77 / 0.23 |
| EBR | a/l/s | **l 38**, a 4 (47) | s 7, t 5, a 5 ... | 0.91 / 0.27 |
| INF | u | **u 32** (39) | u 9, e 7 ... | 0.82 / 0.26 |
| DBL | e/r/u | **o 21**, r 4, e 3, b 3 (37) | e 13, u 8, r 6 ... | 0.22 / 0.66 |
| VBAR_A | s/t | **t 23**, s 1 (35) | s 9, t 6 ... | 0.69 / 0.37 |
| 4STEM | a/c/e/n | **p 11, c 6**, n 3 (24) | e 7, n 5 ... | 0.50 / 0.64 |
| HASH4 | d/i/q | **d 15, q 4**, i 1 (22) | i 7, s 4, d 3 ... | 0.91 / 0.46 |
| BETA | m/s | m 3 (4) | s 2 (3) | small |
| C43, ZHOOK | a/n; none | **absent from the consensus**: pass A codes ZHOOK where pass B codes C43 on the same signs | | |
| CA, CROSS, LL, LOOPBAR | none | 0-1 consensus occurrences | | |

What this is. On f.176r, in Desportes's hand, the period decipherment gives single letters where v4 carries a merged pair. **VBAR_A =
t** (v4 s/t: the VBAR split had stopped at 1/2, KEY.md v4). **EBR = l.** **HASH4 = d/q** (as H162 found on f.108v/r). **4STEM = p/c**
(v4 a/c/e/n). **DBL = o**, the side-by-side glyph (v4's SBS relabel, H26/H51). PHI stays a genuine e/r cell. The same classes are flat
under the wrong text.

Against f.61r's 59 two-way tokens (`f61_decode_period_v4_frac0.1_sbs.tsv`), descriptive: VBAR_A t/s 6 tokens -> t on this leaf; EBR l/s/a
4 -> l; BETA m/s 2 -> m (4 signs only); HASH4 d/q/i 1 -> d/q; 4STEM n/a/c/e 1 -> c/p. That is about 12-14 of 59 leaning to one letter,
with PHI e/r (17) confirmed two-way. C43 a/n (9 tokens) and the rare class ZHOOK are exactly the signs the two passes split, so they are
undecided until H178. Not decided here: any f.61 reading. A class on f.61 is f.61's reader's class; that f.176r's VBAR_A is f.61's
VBAR_A is the atlas's claim, not tested here. Nothing is merged into v4 (a verifier's). Stage 1 is a third of f.176r (12 of 47 rows)
and none of f.176v.

## Campaign step H178 (28 Sept 2026, 22:54-22:54 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- the ZHOOK/C43 split on f.176r reads i (script-only)

Re-scoped script-first. `family/build_f176_key.py` now keeps, in its consensus, the code pair of each 1:1 disputed column (pass A code
| pass B code) and reports the letters the stage-1 DP puts opposite those columns under the true and the wrong clear. The key rows are
unchanged: disputed columns still yield none (`key_period_f176.tsv` byte-identical; `build_f176_key_result.txt` gains the section).
No calls.

| disputed pair (A, B sorted) | fol. 177r (true) | f.184r (wrong) |
|---|---|---|
| C43 / ZHOOK | **i 25**, g 2, x 1, e 1, o 1, b 1 (37) | e 8, u 8, o 4, a 3, c 2, n 2 (37) |
| BETA / LOOPSTEM1 | m 5, n 1, l 1, u 1 (8) | l 2, r 1 ... (9) |
| 4PI / 4STEM | e 3, c 2 ... (8) | flat (7) |
| PHI / SBS | e 3, r 3, i 2 (8) | flat (9) |
| 4STEM / HASH4 | d 3, i 1 (4) | flat (4) |

**The sign the two passes split between C43 and ZHOOK stands for i (25 of 37) in Desportes's cipher on f.176r**, per its period
decipherment. It is not C43's a/n: pass A's ZHOOK is the right reading of its value. This fits the i/x cell of Tomokiyo's table and
H157's f.108v result (ZHOOK = i/x in f.61's hand, by sequence gain). The wrong text is flat on the same columns. For f.61: ZHOOK is one of
f.61's five rare classes (3 tokens, unread under v4), with no period reading until now. What is **not** shown: that f.176r's sign is the
same glyph as f.61's ZHOOK signs (the atlas's shape description is shared, the hands differ). H178b tests that link by a blind tile
match before anything is proposed for f.61. Nothing merged. BETA/LOOPSTEM1 -> m (5 of 8) supports BETA = m.

## Campaign step H178b (28 Sept 2026, 22:55-22:58 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- tile link f.176r i-sign / f.61 ZHOOK: NO LINK by the gate

Tiles, key and prompt pre-registered in `scripts/H178B_PROMPT.md` (4dfffe1c), with the gate amended before the call: centre sign or
'unclear'. The tiles are `images/h178b/tiles.jpg`, built by `scripts/h178b_tiles.py`: f.61r's 3 ZHOOK and 6 C43 signs located by the
runner's eye on its line sheets, and 10 of f.176r's 52 C43/ZHOOK-disputed columns cut at pass A's x. One Opus vision call, inline reply
(`scripts/h178b_reply.tsv`):

| group (reader's description) | f.61 ZHOOK (3) | f.61 C43 (6) | f.176r (10) |
|---|---|---|---|
| G1 large hooked 7/z top over two long crossed slanting strokes | **3** | 0 | 0 |
| G2 "43" | 0 | **6** | 0 |
| G3 small z/3 body run into two short crossed strokes, "may be a smaller, cursive version of G1" | 0 | 0 | **7** |
| unclear | 0 | 0 | 3 (tiles holding two signs or off the row) |

**Gate (f.61 ZHOOK and >= 80% of the clear f.176r tiles in one group): FAIL, NO LINK.** The reader keeps Desportes's smaller cursive
form (G3) apart from f.61's large ZHOOK (G1). The size and the hand differ, and the gate cannot separate "another glyph" from "the same
glyph in another hand". The f.176r i-reading (H178) therefore stays a result about Desportes's sign only, and nothing is proposed for
f.61's ZHOOK. What the call does show: none of the 7 f.176r signs groups with f.61's C43 (0/7), which agrees with the letter evidence
(i, not a/n). A same-hand link would need a family leaf in f.61's own hand writing this sign with a period gloss. Among the glossed
leaves only f.108v (H157) is in that hand, and it has no gloss over its ZHOOK signs. No further row.

## Campaign step H177b stage 2a (28 Sept 2026, 22:59-23:03 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- key rows f.176r L01-L19

Pre-registered in `family/passes/PROMPTS_f176_f175.md` section H177b (2dc56b33). Three Opus vision calls, inline replies written verbatim
by the runner (from the agents' own hand-back messages, `extract.py` in scratch): passes A/B of f.176r L13-L19
(`passes/f176r_signs{A,B}_L13-L19.tsv`, 444 / 449 rows) and a read of fol. 177r L21-L34 (`passes/f177r_clearA_L21-L34.tsv`, mostly m).
`build_f176_key.py L01-L19` (result and `key_period_f176.tsv` regenerated, `--check`):

**Whole stretch: 1,262 signs, consensus 0.79, N 1,009 letters; fol. 177r 0.550 vs the wrong text 0.368 (margin +0.182).**

| class | v4 set | fol. 177r (true) | f.184r (wrong) | in-set share true / wrong |
|---|---|---|---|---|
| PHI | e/r | e 126, r 57 (221) | e 98, r 39 (243) | 0.83 / 0.56 |
| 4TRI (+4HOOK) | a/c/n/p/t | a 46, n 41, p 10, c 8, t 7 (135) | n 31, t 19, a 14 ... | 0.83 / 0.59 |
| VBAR_B | s | **s 57** (72) | s 13, e 9 ... | 0.79 / 0.19 |
| INF | u | **u 46** (64) | u 23, i 6 ... | 0.72 / 0.36 |
| VBAR_A | s/t | **t 45, g 4**, s 2 (64) | s 12, t 12 ... | 0.73 / 0.36 |
| EBR | a/l/s | **l 43**, a 5 (55) | s 11, a 8, t 7 ... | 0.89 / 0.36 |
| DBL | e/r/u | **o 26**, e 5, r 5, b 3 (45) | e 10, u 10, r 9 ... | 0.24 / 0.62 |
| HASH4 | d/i/q | **d 23, q 4** (31) | i 11, d 5 ... | 0.90 / 0.47 |
| 4STEM | a/c/e/n | **p 13, c 7** (31) | e 10, n 9 ... | 0.48 / 0.69 |
| BETA | m/s | m 4 (5); BETA/LOOPSTEM1 disputes m 8 of 13 | | |

Disputed columns: **C43/ZHOOK -> i 35 of 48** (wrong: e 9, u 8, flat); ZHOOK/CROSS (a new split in L13-L19, A ZHOOK = B CROSS) -> s 4,
e 3, i 2, d 2 of 16: mixed, a different glyph from the i-sign, undecided. Agreed ZHOOK 8: mixed. CA 1. The stage-1 picture holds at
1.6x the length, and VBAR_A's partner letter now shows as g (4), Tomokiyo's g/t cell. Descriptive against f.61 as before: VBAR_A t
(6 two-way tokens), EBR l (4), HASH4 d/q (1), 4STEM p/c (1), BETA m (2). Nothing merged. Remaining for H177b: f.176r L20-L47 against
fol. 177v-178r (bands not yet cut), then f.176v.

## Campaign step H179 (28 Sept 2026, 23:05 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- does f.176r's narrowing hold on f.61 and f.108r? (script-only)

`family/narrow_v4_f176.py` (pre-registered in its docstring, pushed before the run) builds a TEST key `family/key_period_v4n176.tsv` (not
v4, not a merge): v4's rows with VBAR_A narrowed to t/g, EBR (EBR, EBR_A, EBR_B) to l, 4STEM to p/c and HASH4 to d/q, as f.176r's period
decipherment reads them (H177b). `test_period_key.py --key key_period_v4n176.tsv --collapse-ebr --min 2 --frac 0.1 --sbs --perms 200`
(`family/test_period_key_result_v4n176_frac0.1_sbs_p200_min2.txt`):

| key | f.61 five known spans (55) | 200 permuted mean / p95 / max | f.108r overlay (84) |
|---|---|---|---|
| v4 | 48/55 | 0.319 / 0.436 / 0.527 | 65/84 |
| v4 narrowed on all four | **48/55** | 0.290 / 0.400 / 0.564 | **57/84** |

One class at a time (20 permutations each, counts only): VBAR_A t/g: f.61 48, **f.108r 67 (+2)**; HASH4 d/q: 48, 65 (0); 4STEM p/c: 48,
62 (-3); **EBR l: 48, 58 (-7)**.

Reading. On f.61's 55 known letters nothing is lost: these cells barely occur in Tomokiyo's spans, so f.61 cannot test them. On f.108r,
in the Mayenne secretary's hand, the transfer is class by class: **VBAR_A = t transfers and improves the overlay (+2), HASH4 = d/q is
neutral, 4STEM = p/c (-3) and above all EBR = l (-7) are contradicted.** The EBR loss has a known cause. f.176r's readers could not tell
EBR_A from EBR_B and coded every bracket EBR_B. v4's f.101r rows split them, with EBR_A reading s 18, l 13, a 8, so "l" is one form's
value, not the class's. Conclusion for a verifier: f.176r's rows are a period key for Desportes's hand. Only VBAR_A's t, and HASH4's d/q
(already H162), carry over to the Mayenne hands by this test. No class change, nothing merged.

## Campaign step H180 (28 Sept 2026, 23:06-23:08 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- f.176r's brackets are form B (f.61's form): PASS

Pre-registered in `scripts/H180_PROMPT.md` (bedd290e), with the design change logged before the call: fixed attributes, not a free
grouping, because H178b's free sort grouped by hand. Tiles `images/h180/tiles.jpg` (`scripts/h180_tiles.py`, key `scripts/h180_key.tsv`):
H22's blind bracket-sort anchors, form A 8 (hairline diagonal; f/s under Tomokiyo's letters, f.108) and form B 6 (plain squared C; l/y,
every f.61 bracket), plus 12 f.176r brackets that both H177b passes code as a bracket (L13-L19). One Opus vision call, inline reply
(`scripts/h180_reply.tsv`), asking per centre sign "diagonal from the top bar to the foot? yes/no/unclear".

- **Control: 14/14 anchors right** (A yes 8/8, B no 6/6; gate >= 12).
- **Target: 11 of 11 readable f.176r brackets "no" diagonal** (1 tile unclear, no bracket at its centre); gate >= 80% with >= 7 tiles:
  **PASS -> form B.**

Joined with the earlier steps: f.176r's form-B brackets read **l** in its period decipherment (H177b: l 43, a 5 of 55; the other
letters 1 each). Under Tomokiyo's letters, H22 put f.61's form-B brackets in the l/y cell (4/4). H179's -7 on f.108r is the other form:
f.108r's brackets are mostly form A (f/s, H22 A 6/6). So **for f.61's bracket form the period evidence now reads l** (partner y in the
table), where v4's merged EBR row gives l/s/a. That bears on f.61's 4 two-way EBR tokens (v4 l/s/a), 3 of which H22 saw as form B; all
of f.61's brackets are B. Scope: the form test used 11 tiles from rows L13-L19, while the letter count is over L01-L19 (every bracket there
coded EBR_B by both readers). Two hands (Desportes; f.61's), one form, one cell: a verifier's question whether that licenses grading
f.61's form-B brackets l at C. Not merged, no class change.

## Campaign steps H172 and H176 (28 Sept 2026, 23:09-23:11 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- answered from the finding aid and Tomokiyo

The BnF finding aid on disk (`sources/bnf-aem/cc504266_francais3974-3995.html`, fr.3984 section) gives items 83-90:
- **Fol. 175 = item 83, "Déchiffrement de la lettre portée sous le n° 74"**, where item 74 (fol. 153) is "Lettre, avec chiffre et
  déchiffrement, du baron DE TALMET, député de Bourgogne, au gouverneur de Bourgogne. « A Paris, ce XXe juillet 1593 »". Fol. 175r
  deciphers Talmet's letter. That is why it failed H170's gate against f.176r, and H176's premise (fol. 175r = f.189r's decipherment) is wrong.
- **Item 84 (Desportes to Clement VIII, "avec chiffre et déchiffrement") runs fol. 176-179** (item 85 starts at fol. 180). So **fol. 179
  (canvas 333, the cipher page H169 saw) belongs to the same letter**, most likely the rest of its cipher, in Desportes's hand. It is
  not a new correspondent or a new hand. That answers H172.
- Tomokiyo's league.htm lists "no.74 (fol.153) Baron de Talmet ... / no.83 (fol.175) Dechipherment of no.74" with its own image
  `league5.png`, fetched once (1 request, 200; `sources/cryptiana/web/img/league5.png`, manifest row). It is his **"Cipher Reconstructed
  from BnF fr.3984, f.153"**: a homophonic table of figures and symbols with nulls and double letters, not the polyphonic family.
  A published key for a different cipher: nothing for f.61. He then lists nos. 84-115 (the Desportes letters and the Lisieux reply) as
  using the mayenne.htm cipher, which is H168-H180's material.
H176 dropped (wrong premise, a different cipher). H172 done. Only H177b (the rest of f.176r, then fol. 179 and f.176v) remains open
among the fr.3984 rows.

## Campaign step H181 (28 Sept 2026, 23:12-23:12 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- f.176r's letters at f.61's own positions (script-only)

`family/h181_f61_positions.py` (`--check`, result `family/h181_f61_positions_result.txt`): the positions of f.61r's VBAR_A and bracket
(EBR) tokens inside Tomokiyo's five spans, under H179's alignment, compared with the letter f.176r's period decipherment gives those
classes (VBAR_A t, H177b; form-B bracket l, H180).

**Agree 7/7:** VBAR_A t = Tomokiyo t at L03/6, L05/3, L11/6, L11/12; bracket l = Tomokiyo l at L03/15, L07/5, L11/3.
f.61's 10 two-way tokens of these classes (v4: VBAR_A t/s x6, EBR l/s/a x4) all have a Desportes-hand period letter; the 3 outside his
spans are L01/10 (VBAR_A), L10/1 (EBR) and L10/4 (VBAR_A; inside the L10 fragment of H16/H17, where the pair was [g/t]).
Independence, for the verifier. The letters come from a period decipherment of another hand, so they are not Tomokiyo's. But f.61's
VBAR_A/VBAR_B boundary was first set by blind sorts scored on his letters (H13/H15, VERIFY-F61-V4 section 2), so the VBAR_A half of the
7/7 is not fully independent of him. The bracket half rests on H22's blind form sort (scored on his letters too, 10/10) and H180's
attribute test. A cross-hand period reading, two classes, 7 agreeing positions: evidence for a verifier to grade. Not a reading of
f.61, no class change, nothing merged.

## Campaign step H177b stage 2b (28 Sept 2026, 23:17-23:19 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- key rows f.176r L01-L33

Pre-registered in `family/passes/PROMPTS_f176_f175.md` (stage 2b, 2ae8bbcf). Four Opus vision calls, inline replies written verbatim
by the runner: passes A/B of f.176r L20-L26 and L27-L33 (`passes/f176r_signs{A,B}_L20-L26.tsv`, 434/434 rows;
`..._L27-L33.tsv`, 431/430). The readers note a struck-through run in L26 (pos 24-30), which the decipherment skips; the DP takes it as
gaps. No new clear read: fol. 177r L01-L34 covers these rows. fol. 177v is cut as strips for the next stage (`family/sheets/f177v_strips/`).
`build_f176_key.py L01-L33` (result and `key_period_f176.tsv` regenerated, `--check`):

**2,140 signs, consensus 0.80, N 1,712: fol. 177r 0.532 vs the wrong text 0.344 (margin +0.188).** Stage 2a's classes hold at 1.7x the
counts: VBAR_A t 69, s 7, g 6 (110); EBR l 68, a 12 (103); HASH4 d 33, q 5, i 5 (50); INF u 80 (114); VBAR_B s 57; PHI e 208, r 96. New in
L20-L33, where both passes now agree on signs they split before:

| class (agreed) | fol. 177r (true) | f.184r (wrong) | note |
|---|---|---|---|
| ZHOOK | **i 23**, s 3, x 3 (46) | s 8, i 8, u 6 (57) | agrees with the C43/ZHOOK-split sign (i 35/48): Desportes's i-sign |
| C43 | **n 8, a 7** (19) | n 9, a 6, e 5 (37) | the real "43" glyph reads a/n, as v4 |
| CROSS | s 16, i 7, l 4 (42) | i 10, e 8, m 5 (51) | Desportes's "x between bars" glyph; mixed, weak s |
| 4PI | p 7, c 3 (16) | a 6, n 4 (17) | against v4's a/d/n/q (in-set 0.12); possibly the 4TRI c/p glyph coded 4PI |
| disputed DBL/SBS | o 14, b 2 (26) | flat | the side-by-side b/o glyph again |

The row keeps its scope: a period key in Desportes's hand. Cross-hand use is H179/H180/H181's question (only VBAR_A t and the form-B
bracket l have been carried over and checked). The CROSS figure is not proposed for f.61's CROSS: that is a different glyph by the
atlas ("plus with a stroke rising to the upper right") and not tested. Nothing merged.
