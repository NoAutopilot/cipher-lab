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

## Campaign step H182 (28 Sept 2026, 23:20 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- ZHOOK: the period letter i against Tomokiyo's letters (script-only)

Test key `family/key_period_v4n176z.tsv` = H179's `key_period_v4n176.tsv` + ZHOOK i/x from f.176r's period decipherment (H177b stage 2b:
the ZHOOK both passes agree on reads i 23, x 3 of 46; the C43/ZHOOK-split sign i 35 of 48). A test key, not v4, not a merge.
`test_period_key.py --key key_period_v4n176z.tsv --collapse-ebr --min 2 --frac 0.1 --sbs --perms 200`
(`family/test_period_key_result_v4n176z_frac0.1_sbs_p200_min2.txt`): **f.61 five spans 50/55** (v4n176 48; permuted p95 0.436), f.108r
overlay 62/84 (v4n176 57). `family/h182_zhook.py` (`--check`, `h182_zhook_result.txt`) lists Tomokiyo's letter at every ZHOOK position
under that alignment: **i or j at 10/10**. On f.61: L07/3 j, L07/11 i, L11/11 i. On f.108r: T1 L02/4, 8, 26, 35 i and L02/23 j; T2 L03/40 i,
L03/32 j. i and j are one letter in the period's spelling (the scorer keeps them apart, so the two j positions do not add to 50/55).

Reading for the verifier: the rare class ZHOOK, unread under v4, has a period letter from Desportes's decipherment (i, cell partner x in
the table) that equals Tomokiyo's published letter at every ZHOOK position in both of his read texts. Independence: the period letter is
not his; his i's come from his own table's i/x cell (published). The glyph link across hands failed its blind tile gate (H178b: Desportes's
form smaller and more cursive). The letter agreement (10/10, every position, two hands on his side) is the other kind of evidence the link
needed. H157's sequence-gain lean to i/x on f.108v points the same way. No class change, nothing merged: the verifier grades whether f.61's 3
ZHOOK tokens may be read i at S/C.
Addendum (same step, script run inline, nothing committed beyond this note): at the other rare or disputed classes' positions under
the same alignment, Tomokiyo writes a dash (no letter) at every CROSS (f.61 L01/1, L07/10), CA (L03/9, L05/7, L05/8, L08/10) and LL
(L05/16) position. His reading treats them as nulls or unread, so no period letter can be checked there. At 4PI he reads n (f.61 L11/9)
and p, d, d, d, d (f.108r): v4's a/d/n/q fits, and f.176r's p/c for the readers' "4PI" does not. That class does not carry over, as
4STEM p/c did not (H179).

## Campaign step H177b stage 2c (28 Sept 2026, 23:24-23:26 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- key rows f.176r L01-L40

Pre-registered (`family/passes/PROMPTS_f176_f175.md` stage 2c, 787bf38b). The builder now appends fol. 177v's lines after fol. 177r's (L01-L33
output unchanged, `--check` OK before the calls). Three Opus vision calls, inline replies written verbatim: passes A/B of f.176r L34-L40
(`passes/f176r_signs{A,B}_L34-L40.tsv`, 418/417 rows) and a read of fol. 177v strips 1-4 (`passes/f177v_clearA_S01-S04.tsv`, V01-V14,
mostly M/L). The two passes split systematically in L34-L40: A codes ZHOOK and LL where B codes VBAR_B and ZHOOK. Those columns leave
the consensus (0.74 over the stretch).
`build_f176_key.py L01-L40`: **2,638 signs, N 2,110; fol. 177r-v 0.531 vs the wrong text 0.345 (margin +0.186)**, steady across four
stages (+0.221, +0.182, +0.188, +0.186). With the new rows: C43 (agreed) n 26, a 20 of 61 -> a/n, as v4. HASH4 d 35, i 17, q 8 (70): the i
share rose with L34-L40's LL/HASH4 confusions. VBAR_A t 81, s 14, g 8 (138). EBR l 83, a 14 (124). ZHOOK i 23 of 48. VBAR_A/VBAR_B
disputes read s 16 of 33 (VBAR_B's s). Nothing merged. Remaining: L41-L47 and f.176v (47 rows), then fol. 179 (item 84's last leaf).

## Campaign step H177b stage 2d (28 Sept 2026, 23:31-23:31 UTC by the clock, runner 6 session_016YPPumG1PbhMJ3pBLuqaeW) -- key rows over the whole of f.176r

Pre-registered (dc5f0e53). Three Opus vision calls, inline replies written verbatim: passes A/B of f.176r L41-L47
(`passes/f176r_signs{A,B}_L41-L47.tsv`, 379/381 rows; L47 ends in an omega-like closing mark and a slash, coded OTHER) and a read of
fol. 177v strips 5-8 (`passes/f177v_clearA_S05-S08.tsv`, V15-V27). The decipherment itself leaves a few cipher signs undeciphered
(V23, V26: probably code symbols the decipherer did not expand). `build_f176_key.py L01-L47` (`key_period_f176.tsv`, result, `--check`):
**f.176r complete: 3,095 signs, consensus 0.70, N 2,476 letters of fol. 177r-v; 0.517 vs the wrong text 0.325 (margin +0.193)**.
Whole-leaf letters: VBAR_A t 100, s 16, g 10 (163); EBR l 95, a 16 (141); HASH4 d 40, i 18, q 9 (77); C43 n 26, a 20 (61); ZHOOK i 28 of 61
(and the C43/ZHOOK split sign i 35 of 48); VBAR_B s 57; INF u; PHI e/r. The margin held at +0.18 to +0.22 over five stages.

**Handover (runner 6 stops at about 660k context; the 700k line is the brief's).** H177b stays open for the next runner: f.176v (canvas 328,
47 rows, not yet cut), fol. 179 (canvas 333, item 84's last leaf, most likely the rest of the cipher), and the decipherment's remainder:
fol. 177v strips 9-12 (`sheets/f177v_strips/boxes.tsv`) and fol. 178r (canvas 331). All crops were in this session's scratch. Regenerate
them from the natives by the recipes in `family/sheets/f176r_full/README.md`, `f177r_full/README.md` and `f177v_strips/README.md`
(natives: Gallica btv1b9060633d canvases 327-331, 333, one request each). Reader prompts: inline replies only (22:45 firing rule). The
runner writes the files from the agent's hand-back message. Scripts: `family/build_f176_key.py` (clear files `f177r_clearA_*`,
`f177v_clearA_*` in line order; extend to fol. 178r and f.176v the same way). For the verifier: `scripts/H66_PAGE.md` section H168-H180
plus H181-H182.

## Campaign step H177c stage 1 (29 Sept 2026, 00:15-00:25 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- f.176v vs fol. 177v: GATE FAIL

Pre-registered in `family/passes/PROMPTS_f176_f175.md` section H177c (c7478950), builder `family/build_f176v_key.py` pushed before the
calls; `key_period_f176.tsv`, `build_f176_key.py` and v4 untouched (VERIFY-F61-V5 is auditing them). Natives canvases 328, 330, 331 fetched
once each (requests.log). f.176v cut into 45 cipher rows (`family/sheets/f176v_full/README.md`; crops not committed). Two Opus vision calls:
blind sign passes A/B of f.176v L01-L08 (`family/passes/f176v_signs{A,B}_L01-L08.tsv`, 515 rows each, written verbatim from the inline
replies). Pass A codes C43 where pass B codes 4TRI throughout (55 columns), as on f.176r.
Dry run of control (b) before the calls, on f.176r's own L01-L08: fol. 177r 0.569 vs fol. 177v 0.384 (the control separates passages).

**Result: 517 signs, consensus 0.80, N 413. fol. 177v from V01 0.339 vs (a) f.184r 0.373, (b) fol. 177r from L01 0.344; margin -0.034; GATE
FAIL** (`family/build_f176v_key_result.txt`, `--check` OK). No class shows the period signal f.176r showed (VBAR_B s 10/44 against 57/72 on
f.176r; EBR l 4/23 against l 43/55). So f.176v's text is not shown to start at fol. 177v V01, and nothing is keyed. Per the pre-registration,
no other start line was tried under this row. `key_period_f176v.tsv` holds the unendorsed DP pairs of this failed run only and is not a key.
Possible readings, untested: f.176r's text runs further into fol. 177v than the 0.8 rule puts it (stages 2c-2d used only N 2,476 letters,
so fol. 177v was never tested against f.176r); f.176v is deciphered on fol. 178r or elsewhere; or it is not deciphered at all. Next: H177d,
a pre-registered location scan with f.176r as positive control.

## Campaign steps H177d and H177e (29 Sept 2026, 00:26-00:29 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- f.176v starts at fol. 177v V06 (script-only)

**H177d, location scan** (`family/h177d_scan.py`, result `family/h177d_scan_result.txt`, `--check`). Disclosure: the script was meant to be
pre-registered for after new reads of fol. 178r and fol. 177v strips 9-12. Its first run, meant to check the positive control, also scored
f.176v on the clear already on disk (fol. 177r L01 to fol. 177v V27, 4,707 letters). So the gate below was not blind. PROMPTS section H177d
says so. Windows of N letters every 100 letters, F61-CAL DP under v4's sets; null = 200 letter-shuffled random windows.
- Positive control f.176r L01-L08: peak at letter 0 (0.569), best non-overlapping 0.419, null p99 0.414: PASS, at the right place.
- f.176v L01-L08: peak at letter 3000 (0.545), best non-overlapping 0.354, null p99 0.370: PASS. Every window from 0 to 2700 reads
  0.29-0.35 (noise). Descriptive fine scan at step 20: peak at 2960 (0.571), the head of fol. 177v V06 (letter 2,957, "ung chasteau par la
  necessite ...").

**H177e** (pre-registered before the run): `build_f176v_key.py L01-L08 --start V06`, H177c's fixed controls and gate. **0.567 vs (a) f.184r
0.373, (b) fol. 177r 0.344; margin +0.194, PASS** (`family/build_f176v_key_result.txt`, `family/key_period_f176v.tsv`, `--check`). The start
comes from the scan, so this confirms the location with fixed controls. It is not an independent test.

| class | v4 set | f.176v L01-L08 (fol. 177v V06-) | f.176r whole leaf (H177b 2d) |
|---|---|---|---|
| VBAR_B | s | **s 35** of 43 | s 57 |
| VBAR_A | s/t | **t 18**, g 2, s 2 of 25 | t 100, s 16, g 10 |
| EBR | a/l/s | **l 15**, a 2 of 23 | l 95, a 16 |
| INF | u | u 19 of 27 | u |
| 4TRI (agreed) | a/c/n/p/t | **c 8, p 8**, a 4 of 23 | a/n/p/c mixed |
| A C43 / B 4TRI (split) | | n 23, a 12 of 51 | C43 n 26, a 20 |
| HASH4 | d/i/q | **i 25, d 10** of 43 | d 40, i 18, q 9 |
| PHI | e/r | e 57, r 24, o 17 of 117 | e/r |

VBAR_B s, VBAR_A t (partner g), EBR l and INF u repeat on a second stretch of Desportes's hand. HASH4 leans i here, where f.176r leant d.
That fits H160/H162: the passes may lump bare hash (i) and 4-over-hash (d/q). Nothing is merged. key_period_f176v.tsv is a separate file.

**For the verifier (VERIFY-F61-V5), a fact about key_period_f176.tsv, not an edit to it.** f.176v's text starts at fol. 177v V06, so f.176r's text
runs through fol. 177r (2,589 letters) and fol. 177v V01-V05 (about 2,957 letters in all). f.176r's 3,095 signs are close to one letter per
sign, not the 0.8 the builder assumed. build_f176_key.py L01-L47 trimmed the clear to N = 2,476, which stops about 480 letters short of the
end of f.176r's text. The DP therefore compressed f.176r's last rows onto fol. 177r's last lines. The +0.193 margin held regardless, but the
class counts from f.176r's last rows (about L38-L47) may be misplaced. Re-running with N = the clear through V05 is the verifier's call, or
the next runner's after the audit. Next: H177f, f.176v L09-L45.

## Campaign step H177f stage 1 (29 Sept 2026, 00:26-00:34 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- f.176v L01-L24 against fol. 177v from V06

Pre-registered (PROMPTS section H177f stage 1). Four Opus vision calls, inline replies written verbatim: passes A/B of f.176v L09-L16 and L17-L24
(`family/passes/f176v_signs{A,B}_L09-L16.tsv`, `..._L17-L24.tsv`). In L17-L24, pass B codes 4PI where A codes 4TRI/4STEM, and SBS where A codes
a "trefoil" PHI; those columns leave the consensus (row consensus 0.65-0.74, L20 0.39). `build_f176v_key.py L01-L24 --start V06` (result and
`key_period_f176v.tsv` regenerated, `--check` OK; L01-L16 alone gave +0.226):

**1,540 signs, consensus 0.76, N 1,232 letters of fol. 177v V06-V27. Match 0.513 vs (a) f.184r 0.295, (b) fol. 177r 0.308; margin +0.205, PASS.**

| class | v4 set | true (fol. 177v) | (a) f.184r | (b) fol. 177r |
|---|---|---|---|---|
| VBAR_B | s | **s 82** of 113 | s 21 of 115 | s 33 of 118 |
| INF | u | **u 74** of 95 | u 26 | u 27 |
| VBAR_A | s/t | **t 58**, g 5, s 5 of 80 | t 20, s 15 | t 18, s 14 |
| EBR | a/l/s | **l 54**, a 6 of 77 | s 15, a 10 | a 17, l 13 |
| HASH4 | d/i/q | i 28, d 26, q 4 of 70 | i 15 | d 15, i 11 |
| 4TRI (agreed) | a/c/n/p/t | **c 20, p 13**, a 9 of 51 | n 13, a 12, t 11 | mixed |
| ZHOOK (agreed, not in v4) | - | **i 29** of 49 | e 11, c 6, i 4 | i 7, e 6 |
| BETA | m/s | m 6 of 7 | flat | flat |
| split A 4TRI / B C43 | | n 46, a 33 of 113 | | |
| split A PHI / B SBS | | o 6 of 14 | | |

What this adds, descriptively: on a second stretch of Desportes's hand, the rare class ZHOOK reads **i** on signs both passes agree on. f.176r's i
came from split columns (H178) and 23/46 agreed. It is flat under both wrong texts. VBAR_A t (partner g), EBR l, VBAR_B s and INF u repeat.
Agreed 4TRI reads c/p while the 4TRI/C43 split reads a/n: the passes seem to separate a c/p four-sign from an a/n one, as on f.176r (4STEM p/c,
C43 a/n). HASH4 is split between i and d here. Nothing is merged; key_period_f176v.tsv stays a separate file. f.61 is not read here.
Remaining for H177f: L25-L45. The clear on disk (V06-V27, 1,750 letters) covers about L25-L31; beyond that, fol. 177v strips 9-12 (crops
regenerated in scratch from boxes.tsv) and fol. 178r need one read each.

## Campaign step H177f stage 2 (29 Sept 2026, 00:35-00:40 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- f.176v L01-L32 against fol. 177v V06-V40

Pre-registered (PROMPTS section H177f stage 2). Three Opus vision calls, inline replies written verbatim: passes A/B of f.176v L25-L32
(`family/passes/f176v_signs{A,B}_L25-L32.tsv`) and a read of fol. 177v strips 9-12 (`family/passes/f177v_clearA_S09-S12.tsv`, V28-V40, all
l-grade). In L25-L32 the passes split systematically: A codes ISH where B codes VBAR_B, 4STEM where B codes 4PI, and HASH4 where B codes
ZHOOK. Row consensus falls to 0.55-0.78.
`build_f176v_key.py L01-L32 --start V06` (`--check` OK): **2,069 signs, consensus 0.73, N 1,655 of 2,674 letters (V06-V40). Match 0.507 vs
(a) f.184r 0.294, (b) fol. 177r 0.292; margin +0.213, PASS** (stage 1 +0.205, L01-L16 +0.226).

Classes (true vs the two wrong texts): VBAR_B s 103/139 (0.74 vs 0.23/0.23); INF u 100/130; EBR l 72/112; VBAR_A t 77, s 7, g 6 of 105;
HASH4 d 33, i 28, q 4 of 79; agreed 4TRI c 25, p 19, a 14 of 68; **agreed ZHOOK i 41 of 65** (wrong texts e 11 / e 8, i 4 / i 7); BETA m 10 of 11.
Split columns: A 4TRI / B C43 n 46, a 33 of 113; A 4PI / B 4TRI a 19, n 11 of 38; **A PHI / B SBS o 17 of 28** (the side-by-side glyph reads o,
as DBL did on f.176r and as H26/H65 found on f.61, f.108r and the glossed leaves); A HASH4 / B ZHOOK i 5, d 3 of 9.
Descriptive, for the verifier; nothing merged; key_period_f176v.tsv stays separate. Remaining for H177f: L33-L45, whose clear runs onto fol. 178r
(canvas 331, fetched; cut as strips like fol. 177v, one read).

## Campaign step H177f stage 3 (29 Sept 2026, 00:41-00:47 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- all of f.176v against fol. 177v V06 - fol. 178r

Pre-registered (PROMPTS section H177f stage 3). Five Opus vision calls, inline replies written verbatim: passes A/B of f.176v L33-L39 and L40-L45
(`family/passes/f176v_signs{A,B}_L33-L39.tsv`, `..._L40-L45.tsv`) and a read of fol. 178r (`family/passes/f178r_clearA_S01-S07.tsv`, R01-R19,
mostly l; strips in `family/sheets/f178r_strips/`). New systematic splits: A ISH / B VBAR_B, A 4PI / B 4STEM. Both passes code many signs in
L33-L39 as CROSS ("alt ZHOOK").
`build_f176v_key.py L01-L45 --start V06` (`--check` OK): **all of f.176v, 2,923 signs, consensus 0.73, N 2,338 of 3,976 letters (fol. 177v V06 -
fol. 178r R19). Match 0.478 vs (a) f.184r 0.298, (b) fol. 177r 0.291; margin +0.180, PASS.** Stages: +0.194 (L01-L08), +0.226 (L01-L16), +0.205
(L01-L24), +0.213 (L01-L32), +0.180 (L01-L45). The same N rule as f.176r (0.8 letters per sign) trims the clear at N 2,338, and the anchor below
puts the true rate near 1. So the last rows are compressed as on f.176r. The margin holds regardless.

**An anchor independent of the H177d scan.** Both blind passes read the plain words "In foro conscientie" standing in f.176v row L36. The blind
read of fol. 177v has "[In] [foro]" at the end of V34 and "conscienciae" opening V35. Before those words there are 2,263 consensus columns in
L01-L35 plus 39 signs in L36: about 2,300 cipher signs. On the clear side there are about 2,270 letters from the head of V06 to "conscienciae".
That is about one letter per sign, the rate f.176r implies from V05. A start at V01 would need about 2,640 letters for 2,300 signs. So the V06
start rests on a plain-text anchor as well as the scan. It also bears out the H177e flag that f.176r's text runs to fol. 177v V05.

Whole-leaf classes (true vs (a)/(b)): VBAR_B s 103/139 (0.74 vs 0.22/0.28); VBAR_A t 103, s 12, g 6 of 150; EBR l 95/150; INF u 130/187;
HASH4 d 38, i 30 of 88; agreed 4TRI c 34, p 30, a 22, n 16 of 117; **agreed ZHOOK i 52 of 85** (wrong texts e 18 / e 10); agreed SBS o 14 of 23;
BETA m 14 of 19; CROSS (not in v4) s 18 of 34, a lean on a class Tomokiyo's reading leaves as a dash. Split columns: A 4TRI / B C43 n 46, a 33;
A 4PI / B 4TRI a 28, n 19; A 4PI / B 4STEM a 18, n 11; A ISH / B VBAR_B s 14 of 32; A HASH4 / B ZHOOK i 16 of 28; A PHI / B SBS o 17 of 28.

What this is, descriptively: a second leaf of Desportes's hand, keyed by its period decipherment with fixed controls, gives the same single
letters as f.176r for VBAR_A (t, partner g), the form-B bracket EBR (l), VBAR_B (s), INF (u), and the side-by-side glyph (o). It also gives the
rare class ZHOOK the letter i, now on 52 agreed signs. The four-shaped signs look like two letter pairs: a c/p group and an a/n group, which the
passes code inconsistently (4TRI, 4PI, 4STEM, C43). Everything is in `family/key_period_f176v.tsv` (separate file). Nothing is merged into v4 or
key_period_f176.tsv; whether f.61's hand shares these classes is the verifier's (H178b's tile link across hands FAILED for ZHOOK). f.61 is not
read here. H177f done.

## Campaign step H183 (29 Sept 2026, 00:49-00:50 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- f.176r against its whole decipherment (script-only)

`family/h183_f176r_n1.py` (result `family/h183_f176r_n1_result.txt`, `--check` OK; build_f176_key.py and key_period_f176.tsv not edited). Same
design as build_f176_key.py, with the clear = fol. 177r L01 - fol. 177v V05 (2,957 letters, where H177d-H177f put f.176r's end) and N = min(letters,
signs) = 2,957 instead of 2,476. **Match 0.466 vs f.184r 0.304, margin +0.162.** Every class keeps its top letter and its proportions. VBAR_A t 103
(was 100), s 22 (16), g 11 (10); EBR l 100 (95); HASH4 d 43 (40), i 20 (18); ZHOOK i 28 (28), now of 78 (61); SBS o 33; DBL o 27; 4STEM p 13, c 9; C43
and VBAR_B unchanged. So the N cap the H177e flag and VERIFY-F61-V5 both noted cost coverage (about 480 letters unused), not the letter choices.
The four values the verifier endorsed are unchanged under the full clear. For the verifier and F61-FAMILY-9; nothing merged.

## Campaign step H184 (29 Sept 2026, 00:51-00:59 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- fol. 179 vs fol. 178r: two-part GATE FAIL (part 1 PASS)

Pre-registered (PROMPTS section H184; builder `family/build_f179_key.py` pushed with a dry run before the calls). Native canvas 333 fetched once
(requests.log); fol. 179 cut into 21 cipher rows (`family/sheets/f179_full/README.md`, crops not committed). Two Opus vision calls: blind sign passes
A/B of fol. 179 L01-L08 (`family/passes/f179_signs{A,B}_L01-L08.tsv`, 522/507 rows, written verbatim). The passes split heavily: A codes 4TRI and
HASH4 where B codes C43 and ZHOOK. Consensus 309 of 589 (0.52).
Result (`family/build_f179_key_result.txt`, `--check` OK):
- **(1) location scan over fol. 177r L01 - fol. 178r R19 (6,933 letters): peak at letter 5,800 (0.463), best non-overlapping 0.253, null p99 0.246;
  fol. 178r R01 is at 5,631. PASS.** Every window from letter 0 to 5,700 reads 0.18-0.27.
- **(2) build from fol. 178r R01 exactly: 0.221 vs (a) f.184r 0.231, (b) fol. 177r 0.217, (c) fol. 177v V06- 0.224; margin -0.010. FAIL.**
- **GATE (1) AND (2): FAIL.** Nothing keyed (key_period_f179.tsv holds the unendorsed pairs of this failed run only).
Why (2) fails where (1) passes, descriptively: the alignment runs over the full length and does not absorb an offset. A step-20 fine scan (descriptive,
after the gate) rises from 0.257 at letter 5,740 to 0.393 at 5,760 and peaks at 5,820 (0.467): the head of R03 is at 5,770 ("de leur [honneur] nous
n'aurions qu'a gaigner le temps"). So fol. 178r R01-R02 probably close f.176v's text and fol. 179 begins near R03. As in H177c/H177d, the start was
not moved inside this row; H185 pre-registers a build from R03, which will confirm the location, not test it independently.

## Campaign step H185 (29 Sept 2026, 00:59-01:02 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- fol. 179 built from fol. 178r R03: GATE FAIL (script-only)

Pre-registered (PROMPTS section H185). `build_f179_key.py L01-L08 --start R03` (result `family/build_f179_key_result_R03.txt`, `--check` OK):
**0.299 vs (a) f.184r 0.231, (b) fol. 177r 0.217, (c) fol. 177v V06- 0.224; margin +0.068, below the +0.10 gate: FAIL.** The letters lean the
Desportes way (VBAR_B s 15/38, SBS o 16/33, INF u 14/32, EBR l 8/24), but thinly. The limit is the transcription: the two blind passes agree on only
309 of 589 fol. 179 signs (0.52; f.176r/v ran 0.70-0.80). Pass A codes 4TRI and HASH4 where B codes C43 and ZHOOK, and CH/LL/OTHER split too.
Following rule 3's same-knob paragraph, the start is not moved again. The location stays at H184's descriptive level (scan peak inside fol. 178r at
about R03). The next attempt needs a better sign transcription: a third blind pass that adjudicates only the split columns (H186), not another start.
key_period_f179.tsv holds this failed run's unendorsed pairs only.

## Campaign step H186 (29 Sept 2026, 01:05-01:08 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- fol. 179 split-sign adjudication: CONTROL FAIL, stopped

Pre-registered (PROMPTS section H186; `family/h186_adj.py` and the tile key `family/h186_tiles.tsv` pushed before the call). Pairing passes A and B
by position (line, segment, x within 30 px) gives 489 of 522 signs paired, 279 agreeing and 210 split. That is a better picture of the passes than
difflib's 0.52, which lost its place in runs of systematic substitutions. 230 tiles (210 splits + 20 agreed anchors with decoy codes) on 7 sheets. One
Opus vision call (inline reply written verbatim, `family/passes/h186_adjudication.tsv`, 230 rows, 16 N).
**CONTROL: 11 of 20 anchors pick the agreed code (gate >= 17): CONTROL FAIL.** Per the pre-registration: no merge, no build, no fol. 179 key rows.
Probable cause: the tiles were cut 90 px wide around the readers' approximate x_px. The centred sign is often ambiguous with its neighbours (the
sheets show T001, T010 and others with two signs near the tick), and the 4TRI/C43 and HASH4/ZHOOK pairs differ in small strokes at this
scale (1.5x of a 1.0-scale crop).
**fol. 179 status after three attempts (H184, H185, H186), per rule 3's same-approach paragraph:** the location is descriptive only (scan peak
inside fol. 178r near R03, H184 part 1). The key build is untested at this transcription quality, not refuted. A fourth pass of the same kind is
not briefed. What would move it is new material or a different instrument: the natives at 2x with per-sign boxes from a segmenter (not reader
x_px), or a blind shape sort of the 4TRI/C43 and HASH4/ZHOOK families on fol. 179 with anchors from f.176r (H180's design).

## Campaign step H187 (29 Sept 2026, 01:08-01:09 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- f.176v's letters at f.61's own positions (script-only, descriptive)

`family/h187_f61_f176v.py` (result `family/h187_f61_f176v_result.txt`, `--check` OK), the H181 set-up: F61-CAL's DP aligns Tomokiyo's five spans under
key_period_v4n176.tsv, and at each aligned f.61 sign whose class has >= 10 agreed columns in key_period_f176v.tsv, f.176v's letters (share >= 0.15)
are compared with his letter. **38 of 44 agree**: PHI e/r 13/13, 4TRI a/c/p 6/6, VBAR_A t 4/4, EBR l 3/3, VBAR_B s 3/3, INF u 3/5, SBS o 3/5, ZHOOK i
2/3, BETA m 1/2. **Null (letter sets permuted across these nine classes, 1000, seed 187): mean 4.3, p95 16, max 32.**
Caveats, as for H181: the alignment itself uses letter sets overlapping these (v4n176), so agreement is partly built in, most for PHI (e/r in both);
the permutation null does not remove that; his letters come from his own table; f.61's classes are f.61's readers', and the ZHOOK tile link across
hands FAILED (H178b). What it adds beside H181/H182: the second Desportes leaf's letters for VBAR_A, EBR, VBAR_B and the side-by-side glyph agree with
his at f.61's positions too. The disagreements are INF 2 (u vs his letter), SBS 2 and ZHOOK 1, for the verifier to look at. No class change, nothing
merged.

## Campaign step H189 (29 Sept 2026, 01:13-01:14 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- fol. 179 marked-strip adjudication: CONTROL FAIL; fol. 179 closed for this campaign

Pre-registered (PROMPTS section H189; `family/h189_mark.py`, key `family/h189_items.tsv` pushed before the call). 230 items (the 210 fol. 179 splits + 20
anchors from signs both f.176v passes coded alike), each a 300-px context strip with a red triangle under the target. One Opus vision call (inline reply
written verbatim, `family/passes/h189_adjudication.tsv`, 2 N).
**CONTROL: 15 of 20 anchors pick the agreed code (gate >= 17): CONTROL FAIL** (H186: 11/20). Per the pre-registration: no merge, no build.
**fol. 179 is closed for this campaign at "untested at this transcription"** (H184 location PASS but build FAIL; H185 FAIL +0.068; H186 and H189
adjudication controls FAIL). Not refuted: H184's scan puts its text inside fol. 178r near R03. Reopening it needs new material or a person: per-sign
boxes from a segmenter on the native at 2x, or a person's reading of the 4TRI/C43 and HASH4/ZHOOK pairs on a few rows. No fifth model-read approach
is briefed. What the controls show generally: the readers' 4-family and hash-family codes do not hold even on signs two passes agree on, so class
counts that depend on 4TRI vs C43 or HASH4 vs ZHOOK (in any leaf) carry that uncertainty.

## Campaign step H190 (29 Sept 2026, 01:15-01:17 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- the 4-family: two letter pairs, unstable codes (script-only)

`family/h190_4fam.py` (result `family/h190_4fam_result.txt`, `--check` OK). DP pairs split into agreed-4TRI columns and 4TRI|C43 split columns, and
counted as {c,p} vs {a,n}:
- **f.176v, true text: agreed 4TRI c/p 64, a/n 38; split 4TRI|C43 c/p 2, a/n 79; Fisher p 1.2e-19.** Wrong text f.184r: 24/42 vs 2/8, p 0.48.
- **f.176r, true text: agreed 4TRI c/p 48, a/n 206; split c/p 2, a/n 11; p 1.** Wrong text: p 1.
Reading: the 4-family holds at least two signs, a c/p sign and an a/n sign, and the period decipherment separates them on f.176v. The readers'
codes do not map onto them consistently across sessions: on f.176v one pass calls the a/n sign C43 and the other 4TRI, while on f.176r both
passes mostly called the a/n sign 4TRI (the agreed C43 class there reads a/n, n 26 a 20). A class count that pools "4TRI" across leaves or reader
sessions therefore mixes the two signs. That fits the verifier's decision not to endorse 4STEM p/c (VERIFY-F61-V5) and the fol. 179 adjudication
failures (H186, H189). What would settle the 4-family is a blind attribute test (H180's design) on the shape difference between the c/p and a/n
signs, with anchors taken from f.176v's two groups, not another code pass. Descriptive; nothing merged.

## Campaign step H192 (29 Sept 2026, 01:17-01:19 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- two-leaf replication table (script-only)

`family/h192_repl.py` (result `family/h192_repl_result.txt`, `--check` OK). Per class, agreed columns: top letter and share on f.176r (whole clear,
h183 run) and f.176v (H177f run), each beside the wrong text's share of that letter. The pre-stated rule: same top letter, share >= 0.5 on both leaves,
wrong-text share < 0.3 on both, n >= 10 on both.
**Replicate (4): VBAR_A t (0.57 / 0.69; wrong 0.22 / 0.18), EBR l (0.62 / 0.63; 0.13 / 0.20), VBAR_B s (0.79 / 0.74; 0.20 / 0.22), SBS o (0.59 / 0.61;
0.22 / 0.13).** Near misses: ZHOOK i on both leaves (0.36 / 0.61; wrong 0.06 / 0.06), short on f.176r's share because of its split columns (H178);
INF u (0.69 / 0.70), where the wrong text's u share is 0.30/0.31 because u is v4's single letter for INF and the aligner forces it; HASH4 d on both
(0.51 / 0.43; wrong 0.10 / 0.13); BETA m (0.40 / 0.74); CROSS s (0.36 / 0.53; wrong 0.09 / 0.05). No replication for 4TRI (n 0.34 on f.176r vs c 0.29
on f.176v: the reader-code swap H190 found), C43/4PI/4STEM (codes absent or rare on one leaf).
This agrees with VERIFY-F61-V5's endorsement (VBAR_A g/t, EBR_B l/y, SBS b/o, ZHOOK i/x) on a second leaf the verifier did not see, and adds VBAR_B s
(v4's s already). For the verifier and F61-FAMILY-9; nothing merged.

## Campaign step H191 (29 Sept 2026, 01:19-01:20 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- the 4-family on f.61 (script-only, descriptive)

`family/h191_4fam_f61.py` (result `family/h191_4fam_f61_result.txt`, `--check` OK), the H181/H187 alignment. At f.61's own 4-family positions inside
Tomokiyo's spans, his letters by the f.61 readers' code: **4TRI c 3, p 3 (c/p 6 of 6); C43 a 7, n 2 (a/n 9 of 9)**; 4STEM one dash, 4PI n 1, HASH4 none.
The C43 result is built in (v4n176's C43 set is a/n). **Correction (H196, 01:3x): the 4TRI set this alignment used is c/p/t, not a/c/n/p/t**
(the a/c/n/p/t in the f.176r/v build tables is h170_gate's merged 4TRI+4HOOK set, a different load), so the 4TRI result only rules out t (6 of 6 c/p,
weak), and the exact-test figure above overstates it. So on f.61, as on f.176v (H190), the readers' 4TRI and C43 look like the c/p sign and the a/n
sign; on f.176r the readers' codes did not separate them. Descriptive, for the verifier: whether f.61's 4TRI can be narrowed from c/p/t to c/p is theirs. His letters come from his own table. Nothing merged.

## Campaign step H193 (29 Sept 2026, 01:20-01:23 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- the 4-family's c/p sign has a bowl at the stem foot: PASS on a second leaf

Pre-registered (PROMPTS section H193; `family/h193_attr.py`, key `family/h193_items.tsv`, attribute and its direction `family/h193_yes_group.txt` = CP,
pushed before the call). The runner looked only at the 20 labelled f.176v anchors: the c/p sign is a 4 whose stem runs below the line and ends in a closed
b-like bowl; the a/n sign is a 4 with a small r-like tail on the line. One Opus vision call, blind to group and leaf (inline reply written verbatim,
`family/passes/h193_attribute.tsv`, 2 n). Result `family/h193_attr_result.txt` (`--check` OK):
- **CONTROL: 19 of 20 f.176v anchors answer in their group's direction (gate >= 17): PASS.**
- **f.176r, 40 signs both passes coded 4TRI, letters from fol. 177r (h183 alignment): "bowl" 5 -> c/p 5, a/n 0; "no bowl" 27 -> c/p 4, a/n 23 (8 others:
  t, e, i ... or n); Fisher p 0.00063.**
So the shape difference is real and carries the period letters on a leaf the attribute was not built from. On f.176r the readers put both signs under
4TRI; the bowl separates them. This explains H190's code swap. Descriptive: the c/p (bowl) sign and the a/n (r-tail) sign are the table's two
4-signs in Desportes's hand. Whether f.61's 4-family signs split the same way is H194 (f.61's hand; H178b's cross-hand tile link FAILED for ZHOOK,
so f.61 needs its own anchors from Tomokiyo's c/p and a/n positions, H191). Nothing merged.

## Campaign step H194 (29 Sept 2026, 01:24-01:26 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- the bowl attribute on f.61: the readers' 4TRI is the bowl sign, and Tomokiyo reads it c/p (descriptive)

Pre-registered (PROMPTS section H194; scorer `family/h194_bowl_f61.py` pushed before the call; disclosed: the runner looked at images/f61sheet_L05.jpg
for legibility first, the question is H193's unchanged). One Opus vision call, inline reply written verbatim (`family/passes/h194_reply.tsv`).
Result `family/h194_bowl_f61_result.txt` (`--check` OK):
- **Repeat control: 18 of 20 f.176v anchors in their group's direction (gate >= 17): PASS** (H193 19/20).
- **f.61 span sheets: bowl yes -> Tomokiyo c/p 5 of 5; bowl no -> a/n 9 of 9; Fisher p 0.0005.** L03, L05, L08, L11 matched by count; L01 left out
  (4 listed vs 3 codes). The bowl answer coincides with the f.61 readers' codes throughout: every 4TRI is "yes", every C43 "no"; 4STEM and 4PI (L11)
  "no", 4PI read n.
What it says, descriptively: the shape difference validated against the period decipherment on two Desportes leaves (H193: a 4 whose stem ends in a
closed bowl reads c/p; the r-tailed or 3-tailed 4 reads a/n) holds on f.61's hand too. f.61's readers already separate the two signs (4TRI vs C43), and
at 14 of 14 of Tomokiyo's positions the bowl sign carries his c or p. On f.61, v4's and v5's 4TRI cell is c/p/t (corrected in H196; H191 had a/c/n/p/t). For the verifier: whether f.61's 4TRI
may be narrowed to c/p on this evidence (a period-validated shape rule plus his letters; C43 a/n is already v4's). His letters come from his own
table. H178b's cross-hand tile link failed for ZHOOK, a different sign, so each class's transfer stands on its own test. No class change, nothing merged.

## Campaign step H195 (29 Sept 2026, 01:27-01:29 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- hash-family 4-head attribute: CONTROL FAIL

Pre-registered (PROMPTS section H195; `family/h195_hash_attr.py`, key `family/h195_items.tsv`, `h195_yes_group.txt` = DQ, pushed before the call). One
Opus vision call (inline reply verbatim, `family/passes/h195_attribute.tsv`). **CONTROL: 14 of 20 f.176v anchors in their group's direction (gate >= 17):
CONTROL FAIL**; the f.176r targets were not scored (`family/h195_hash_attr_result.txt`, `--check` OK). The d/q anchors read "4-head" 9 of 10; the
i anchors split (no 5, yes 3, n 2), so the i anchors (agreed HASH4 columns the DP pairs with i) are not reliably bare hashes. Either the DP's i pairings on HASH4
columns are partly misplaced, or the i/d distinction is not a 4-head on this hand. Unlike the 4-family (H193), the hash family is not separated by
this instrument; HASH4 stays d/i/q (as VERIFY-F61-V5 held). Not re-briefed with the same question.

## Campaign step H196 (29 Sept 2026, 01:30-01:31 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- a test key v5 + 4TRI c/p (script-only)

Key v5 landed (F61-FAMILY-9, `family/key_period_v5.tsv`, `build_key_v5.py`), so the row's base changed from v4 to v5 (logged in CAMPAIGN.md).
`family/h196_4tri_cp.py` (result `family/h196_4tri_cp_result.txt`, `--check` OK), build_key_v5's own scorer: **v5's 4TRI cell is c/p/t; narrowed to c/p:
f.61 five spans 53/55 under both (2000 permuted keys p95 0.455, none reach it); f.108r overlay 74/84 under both (p95 0.43 / 0.42).** No known letter is
lost, but none is gained either: the narrowing is only the removal of t, and f.61 has 6 4TRI tokens (all c/p/t under v4). It changes those 6 from
three-way to two-way in f.61's meter. Correction carried back: H191, H194 and the verifier page said v4's 4TRI cell was a/c/n/p/t; for f.61's load it is
c/p/t (the a/c/n/p/t in the f.176 build tables is the builders' merged 4TRI+4HOOK set). The H193/H194 finding stands: the bowl sign is the c/p sign.
What it now adds for f.61 is dropping t from 6 tokens, not a wider narrowing. Nothing merged.

## Campaign step H197 (29 Sept 2026, 01:32 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- CROSS = s on f.108v: untestable, dropped (script-only)

`scripts/f61cross_108v.py` (result `scripts/f61cross_108v_result.txt`, `--check` fresh), H157's design with CROSS = s against e/a/i/t/n/null. f.108v has
**one** CROSS sign, below the pre-stated floor of 5: not tested. This matches H150 (CROSS under 10 occurrences in all f.61-hand text on disk). CROSS s
stays a Desportes-hand lean (H192: 0.36 / 0.53, wrong 0.09 / 0.05) with no test available in f.61's hand.

## Campaign step H188 (29 Sept 2026, 01:32-01:34 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- v5 plus the open Desportes leans (script-only)

`family/h188_v5_plus.py` (result `family/h188_v5_plus_result.txt`, `--check` OK), build_key_v5's scorer, 2000 permuted keys each. v5 cells: 4TRI c/p/t,
HASH4 d/i/q, BETA m/s. **Test keys 4TRI c/p, HASH4 d/q, BETA m, and all three together: f.61 five spans 53/55 and f.108r overlay 74/84 under every
one (v5 the same; no permuted key reaches any).** No contradiction with Tomokiyo's letters and no gain: his known positions do not discriminate these
cells (4TRI t, HASH4 i and BETA s occur at none of them). The narrowings therefore rest on the Desportes-leaf evidence alone (H190-H194 for 4TRI; H192
for HASH4 d and BETA m, both short of the replication rule). Earlier f.108r-specific findings still weigh against HASH4 d/q there (H114 d/q hurts,
H118/H119 i/x best on f.108r's sequence gain). For the verifier; nothing merged.

## Campaign step H198 (29 Sept 2026, 01:34-01:35 UTC by the clock, runner 7 session_012nGionjAX21NRbpi4TP69b) -- 4TRI c/p on f.108v by sequence gain: OPEN (script-only)

`scripts/f61tri_108v.py` (result `scripts/f61tri_108v_result.txt`, `--check` fresh), H157's design. f.108v has 6 4TRI signs; the 14-cell map already
has 4TRI = c/p. **c/p beats c/p/t in 4/30 resamples, a/n in 7/30, null (4TRI dropped) in 2/30: OPEN on all three** by the pre-registered rule
(CONFIRMED >= 29, PREFERRED <= 1). The design counts a tie as a loss, and with 6 signs ties are likely, so this is no evidence against c/p. It is
no support from f.108v's unread text either. The 4TRI c/p lean rests on H193/H194 (shape rule validated by the period decipherment; Tomokiyo's letters
14/14 on f.61) and cannot be tested further by sequence gain at this N.

## Runner 7 handover (29 Sept 2026, 01:36 UTC by the clock, session_012nGionjAX21NRbpi4TP69b; stopping near the context line)

Done this session (H177c-H198, spent today 32.9/600): f.176v keyed against fol. 177v V06 - fol. 178r (separate `family/key_period_f176v.tsv`, margin +0.180,
In foro anchor); f.176r's clear runs to V05 (H183: no class letter moves); fol. 179 closed at untested (H184-H186, H189); the 4-family is two signs, a
bowl-footed c/p sign and an r/3-tailed a/n sign (H190, H193 PASS on f.176r, H194 PASS on f.61 against Tomokiyo 14/14); two-leaf replication VBAR_A t, EBR
l, VBAR_B s, SBS o (H192); hash-family attribute CONTROL FAIL (H195); v5 test keys lose and gain nothing on the known spans (H188, H196); CROSS untestable
in f.61's hand (H197); 4TRI on f.108v OPEN (H198). Verifier page: `scripts/H66_PAGE.md` sections H177c-H177f and H183-H194.
Open for runner 8: **H199** (bowl question on f.108v's 4-family, H194's design: `family/h194_bowl_f61.py` is the model; f.108v line crops
`family/sheets/f108v3x_L*_s*.jpg` exist, and the readers' f.108v class sequence is `G.J.lines("f108v")` in scripts/f61beam_seqgain.py; repeat control on
`<scratch>/h193/sheet_01..03`, which a new session must regenerate: `python3 family/h193_attr.py tiles SCRATCH` needs the f.176v and f.176r crops, see
`family/sheets/f176v_full/README.md` and `f176r_full/README.md`, natives canvases 327 and 328). **H200** needs a person (fol. 179 desk pack; the orchestrator
writes the ASKS row). Extraction helper for inline replies: the runner parsed each subagent's hand-back from its task transcript (any string holding the
TSV header) and wrote it verbatim; files in family/passes/ carry "# written verbatim from the inline reply (runner 7 extract.py)".

## Campaign step H199 (29 Sept 2026, 02:12-02:18 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- the bowl sign on f.108v is the readers' 4STEM, not 4TRI (descriptive)

Pre-registered (PROMPTS_f176_f175.md section H199; `family/h199_bowl_108v.py` and key `family/h199_items.tsv`, commit 8890818f, before the call).
Targets: all 74 columns of the H59 f.108v draft with a 4-family code in the reconciled draft, pass A or pass B (reconciled C43 41, 4STEM 25, 4TRI 6,
OTHER 1, ZHOOK 1), cut from the native `family/images/3983_f108v.jpg` at pass A's x (the 3x crops stop 34 native px below the row centre and clip
the bowl), marker above the strip because the leaf's interlinear gloss sits under it. The H193 control strips were regenerated from the Gallica
natives (canvases 327, 328; 2 requests, same hashes as logged) and `h193_items.tsv` reproduced byte-identical. Disclosure: the runner looked at target
sheets 01 and 04 for legibility (a few markers sit about half a sign off). One Opus vision call, blind (reply verbatim, `family/passes/h199_reply.tsv`).
Result `family/h199_bowl_108v_result.txt` (`--check` OK), positions `family/h199_bowl_positions.tsv`:
- **Repeat control: 19 of 20 f.176v anchors in their group's direction (gate >= 17): PASS** (H193 19/20, H194 18/20).
- **By reconciled code: 4STEM bowl yes 19, no 2, n 4; 4TRI yes 0, no 6; C43 yes 0, no 41.** Pass A and pass B separately give the same picture
  (4STEM 19/4/6 and 18/3/4; 4TRI 0/4 and 0/6; C43 0/41 and 0/40).
- Pre-stated read-out: reconciled 4TRI yes share 0.00, C43 no share 1.00, so **"the readers' split does not follow the bowl on f.108v"** in the
  registered sense. It follows it under another code: on this leaf the passes wrote the bowl sign as 4STEM.
What it says, descriptively: f.108v, in f.61's hand, carries both 4-signs (bowl 19, no bowl 49, n 6 of 74). The H59 passes coded the bowl sign
4STEM and the no-bowl sign mostly C43, with 4TRI for six more no-bowl signs. This is the third time the 4-family codes have swapped between reading
sessions (H190 f.176r/f.176v; H194's f.61 readers wrote the bowl sign 4TRI). A 4-family code's meaning therefore depends on the pass session that
wrote it. The f.108v judge and skeleton cells (f61joint_h51_map: 4STEM a/n, 4TRI c/p, C43 a/n) key about 19 bowl signs a/n, where the rule validated on
H193/H194 (bowl = c/p against the period decipherment and against Tomokiyo) says c/p, and key the six no-bowl 4TRI as c/p. Key v5's pooled 4STEM
support mixes c/p and a/n on f.101r (a/n 25, c/p 16), which fits the same swap. H198's OPEN for 4TRI on f.108v is explained: those six signs are not the
bowl sign. Next: H201 (script-only sequence gain with the 4-family relabelled by bowl), H202 (the bowl at f.108r's period-glossed positions),
H203 (which v5 4-family cells mix the two signs). No class change, nothing merged.

## Campaign step H201 (29 Sept 2026, 02:19-02:21 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- f.108v relabelled by the bowl: sequence gain CONFIRMED, rank 1 of 201 (script-only)

`scripts/f61bowl_108v_seq.py` (committed 447367af before the run; result `scripts/f61bowl_108v_seq_result.txt`, `--check` fresh). The H59 f.108v
draft with every 4-family column relabelled by H199's blind bowl answer (yes -> c/p, no -> a/n; 68 columns answered, 19 yes), other cells the 14-cell
map unchanged, against the readers' own cells (4STEM a/n, 4TRI c/p, C43 a/n):
- **(1) 30 bootstrap resamples of f.108v's lines (seed 201): the bowl relabel wins 30/30 -> CONFIRMED** (registered gate >= 29).
- **(2) Whole leaf: gain 0.276 (bowl) vs 0.152 (readers' cells); among 200 random relabels giving 19 c/p to random answered 4-family columns (seed
  2011) the bowl relabel ranks 1 of 201 (best random 0.223, median 0.178).** The registered read-out "bowl relabel carries sequence information on
  f.108v" is met.
The null matters here. Any relabel with 19 c/p already scores above the readers' cells (median 0.178 vs 0.152), because the readers' cells key 19 bowl signs a/n
and 6 no-bowl signs c/p. The bowl's own placement beats every random placement, so the shape answer carries the positions and not only the count.
Together with H193/H194, which rest on period letters, this is a third, independent line: the bowl sign is c/p in f.61's hand on a leaf with no key
source used here. For the verifier: f.108v's 4-family should be read by bowl, not by the H59 pass codes; any f.108v or pooled 4STEM figure built
on those codes (the f.108v skeleton, H85 judge, v5's 4STEM support) mixes the two signs. No key change, nothing merged; grade stays with the verifier.

## Campaign step H202 (29 Sept 2026, 02:21-02:24 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- the bowl at f.108r's period-gloss letters: direction agrees, registered rule NOT met

Pre-registered (PROMPTS section H202; `family/h202_bowl_108r.py`, key `family/h202_items.tsv`, commit d935e29f, before the call). The 20 f.108r pass-A
4-family positions that the overlay letters (the leaf's period interlinear, reprinted by Tomokiyo; grade C for the test) align to under key v5 form A.
Strips from images/f108sheetB_L02/L03.jpg bands (descenders kept). Disclosure: the runner looked at f108sheetB_L02.jpg for band geometry and at the
target sheet for legibility; the strips came out as single-sign views (a scaling choice in the script, smaller context than H193's strips), and
S03/S09 sit at a strip edge or off a 4-sign. One Opus vision call, blind (`family/passes/h202_reply.tsv`). Result `family/h202_bowl_108r_result.txt`
(`--check` OK):
- **Repeat control 18/20 PASS.**
- **bowl yes: c/p 3, a/n 0; bowl no: c/p 2, a/n 11; Fisher p 0.018.** The 4 d positions (4PI) all answered no.
- Pre-stated read-out: **"bowl = c/p not shown at f.108r's period letters"**. The rule needed every answered c/p position to be yes, and two were no:
  S03 (4PI, letter p, marker at the strip's right edge) and S14 (4TRI, letter c).
What it says: the direction agrees with H193/H194/H201 (no a/n position carries a bowl; every bowl carries c/p), but at N 16 with two c/p misses the
registered rule fails, and this step does not add a fourth line of support. One of the two misses is a 4PI sign, whose shape is not the 4-family bowl
question's; the other (S14) is an unexplained miss. The alignment was made under v5, whose cells follow the readers' codes here (4TRI c/p, C43/4STEM
a/n), so the pairs could not disagree with the codes by construction; the blind bowl answer is what was tested. Not re-run with a different crop
(rule 3's "same knob" caution); a wider-context re-cut is possible but would be a second attempt at the same 16 positions.

## Campaign step H203 (29 Sept 2026, 02:24-02:25 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- which 4-family support pools the two signs (script-only, descriptive)

`family/h203_4fam_mix.py` (result `family/h203_4fam_mix_result.txt`, `--check` OK). Per 4-family code and leaf, {c,p} vs {a,n} counts in the period
evidence (key_period_v5.tsv non-CELL rows plus key_period_f176.tsv); MIXED = both >= 5 and the minority >= 0.25.
- **MIXED: 4STEM on f.101r (c/p 16, a/n 25), 4TRI on f.101r (51 / 19), 4STEM on f.176r (22 / 10).**
- Not flagged but known to pool both signs by H193's blind attribute test: 4TRI on f.176r (46 / 194; minority 0.19, under the threshold).
- Clean by these counts: C43 on every leaf (a/n 24-68, c/p 0-2); 4TRI on f.188r/f.184r (21 / 2); 4STEM on f.188r/f.184r (0 / 27).
- Each leaf's c/p majority sits under 4TRI (f.101r 51, f.176r 46, f.188r 21), but on f.108v the H59 passes wrote the bowl as 4STEM (H199).
For the verifier: v5's 4STEM cell (a/n, with "4STEM p/c" listed as not merged over a conflict with f.108r) and 4TRI cell rest partly on pooled counts.
Read f.61-hand leaves' 4-family by the bowl (H194 f.61, H199/H201 f.108v), not by the pass code. No key change, nothing merged.

## Campaign step H205 (29 Sept 2026, 02:27-02:35 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- model judge, bowl labels vs pass codes on f.108v: "no preference shown" by the registered rule; the rank part was a non-test by construction

Pre-registered (scripts/PROMPTS.md section H205; `scripts/f61judge108v_bowl.py`, sets and keys committed 70db041f before the calls). Two Opus text
calls, H94 no-leak prompt, replies verbatim in `scripts/f61judge_known_h51_swaps207_verdict.tsv` and `scripts/f61judge_f108v_bowl_s207_verdict.tsv`.
- **Control (known f.61 span lines, one-swap null, seed 207): target rank 1 of 21 (7.0; next 6.0): PASS** (`f61judge_known_h51_swaps207_result.txt`).
- **Target (`f61judge_f108v_bowl_s207_result.txt`, `--check` fresh): bowl labelling 7.0, rank 4 of 21 (ties against); the pass-code set 2.5 (rank 13).**
  Registered read-out: **"no preference shown"** (the rule needed rank 1 and above the pass-code set).
- **The runner's own design error:** after the relabel, f.108v carries no 4TRI, 4PI or C43 token (4BOWL 19, 4NOB 49, 4STEM 4). So the one-swap
  neighbours 4PI<->C43 and 4PI<->4TRI are the target text exactly (both scored 7.0, tying it), and 4STEM<->4TRI and 4PI<->4STEM differ from it at 4
  tokens (7.5, 6.5). The rank-1 part could not fail differently from the target for those sets (CLAUDE.md rule 3, "a control that cannot vary on
  the same axis"): the brief's error, not the judge's. The swap pool should have been drawn only from classes present in the relabelled text.
What the numbers do show, descriptively and outside the registered rule: the judge scored the bowl decode 4.5 points above the pass-code decode of
the same tokens, in line with H201's sequence gain. It is one call, so no claim rests on it. The judge's resolved text for the bowl set (in the verdict
file) is its own resolution under grade-M transcription and a two-way cipher: a verifier's input, not a reading. Not re-run in this session. A
corrected re-run (swap pool restricted to present classes, two seeds) is H208.

## Campaign step H207 (29 Sept 2026, 02:28-02:40 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- the bowl on fr.3982 f.101r against its period letters: direction agrees, registered rule NOT met

Pre-registered (PROMPTS section H207; `family/h207_bowl_101r.py`, key `family/h207_items.tsv`, commit c458d848, before the call). 39 f.101r signs under
the MIXED codes (H203), drawn with their period-gloss letter (passes/f101r_align_v4.tsv, grade C): 4TRI c/p 10 + a/n 10, 4STEM c/p 9 + a/n 10.
Strips cut from a fresh Gallica native of f210 (bytes differ from the 28 Sept fetch; pixel correlation 0.9996 with a committed crop). Disclosure in
PROMPTS (three geometry versions looked at; U13/U15 carry two cipher rows). One Opus vision call, blind (`family/passes/h207_reply.tsv`). Result
`family/h207_bowl_101r_result.txt` (`--check` OK):
- **Repeat control 19/20 PASS.**
- **Pooled: bowl yes -> c/p 11, a/n 5; bowl no -> c/p 5, a/n 15; n 3 (all c/p); Fisher p 0.017.** 4TRI alone 7/3 vs 2/7 (p 0.07); 4STEM alone 4/2 vs 3/8 (p 0.16).
- Registered read-out: bowl-yes c/p share 0.69 (< 0.75), bowl-no a/n share 0.75, p 0.017 (> 0.01): **"the bowl does not split f.101r's mixed support
  by the registered rule."**
What it says: the direction is the same as on f.176r (H193), f.61 (H194) and f.108v (H199/H201), but on this leaf the bowl separates the letters
less cleanly (10 of 36 answered signs against the rule's direction). The possible causes cannot be told apart here: the hand (fr.3982, not f.61's or
Desportes's), the strip geometry (rows drift; the reader saw ordinary words in every strip), or letters misplaced by the gloss alignment (the
align_v4 rows carry 'conflict' status at many positions). For the verifier: the bowl rule is supported on three leaves (two against period letters,
one by sequence gain) and only leaning on f.101r. v5's f.101r 4TRI/4STEM counts stay pooled; nothing merged.

## Campaign step H208 (29 Sept 2026, 02:42-02:49 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- H205 corrected: the model judge prefers f.108v's bowl labelling in both seeds

Pre-registered (scripts/PROMPTS.md section H208; `scripts/f61judge108v_bowl.py --present`, sets and keys committed 5d1798a7 before the calls). The
19 one-swap neighbours were drawn only from class pairs present in the relabelled text, so every neighbour differs from the target. Calibration: this
session's H205 control (known f.61 lines vs one-swap null, rank 1 of 21). Two Opus text calls, inline replies verbatim
(`scripts/f61judge_f108v_bowlp_s208_verdict.tsv`, `_s209_verdict.tsv`), results `f61judge_f108v_bowlp_s20{8,9}_result.txt` (`--check` fresh):
- **seed 208: bowl labelling 7.5, rank 1 of 21 (next 6.0); pass-code set 3.5 (rank 9-11).**
- **seed 209: bowl labelling 9.0, rank 1 of 21 (next 6.0); pass-code set 4.0 (rank 7-10).**
- Registered read-out: **"the judge prefers the bowl labelling" in both seeds**, so it holds overall.
Taken with H199 (the bowl sign is the passes' 4STEM on f.108v), H201 (sequence gain, 30/30, rank 1 of 201 random relabels) and H193/H194 (bowl = c/p
against period letters on f.176r and Tomokiyo's on f.61): reading f.108v's 4-family by the blind bowl answer, not by the pass code, is preferred
by two instruments that do not depend on each other. H202 (f.108r) and H207 (f.101r) lean the same way but did not meet their rules. The judge's
resolved text for the bowl sets is in the verdict files. It is a model's resolution of a two-way cipher over a grade-M transcription, a verifier's
input and not a reading claim. No class change; nothing merged into a key (a verifier decides whether the bowl split enters v6 as a shape rule for
the 4-family).

## Campaign steps H209 and H210 (29 Sept 2026, 02:51-02:53 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- HASH4 on the bowl-relabelled f.108v leans d/q; the relabelled map's rank (script-only)

`scripts/f61hash4_108v_bowl.py` (committed before the run; result `scripts/f61hash4_108v_bowl_result.txt`, `--check` fresh). f.108v relabelled by H199's
bowl answers, map = the 14 cells + 4BOWL c/p + 4NOB a/n; 14 HASH4 signs.
- **H209: HASH4 i/x vs d/q: i/x wins 0/30 -> d/q PREFERRED; i/x vs null: 13/30 -> OPEN.** So on f.108v, f.61's hand, the sequence prefers d/q over i/x
  for HASH4. That runs opposite to f.108r L04-L06 (H118/H119: i/x best there on sequence gain, and H127's f.108r rows), and fits H195's partial finding
  that the d/q anchors carry a 4-head (9/10) while the i anchors split: the hash family may also be two signs whose pass codes merge. d/q against null was
  not in the registered design (a follow-up, H211).
- **H210: relabelled map gain 0.276, rank 1 of 201 (best permuted 0.068, median 0.005); with HASH4 i/x 0.270, rank 1 (best 0.075).** Under the pass
  codes H127 gave 0.152 / 0.165 (best permuted 0.077 / 0.089). The relabel almost doubles the sequence gain; the permuted-map null does not move.
For the verifier: HASH4 stays d/i/q in v5; the f.108v evidence now points to d/q in f.61's hand, against f.108r's i/x, so the two leaves disagree unless
the hash family is split by shape. Nothing merged.

## Campaign step H211 (29 Sept 2026, 02:54-02:56 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- HASH4 on two f.61-hand leaves: opposite leans, all OPEN (script-only)

`scripts/f61hash4_two_leaves.py` (committed before the run; result `scripts/f61hash4_two_leaves_result.txt`, `--check` fresh), H209's design, seed 211.
- (a) f.108v (bowl relabel, 14 HASH4): **d/q vs null 28/30 -> OPEN** (one short of CONFIRMED).
- (b) f.108r L04-L06 (H112 draft, 10 HASH4): **i/x vs d/q 24/30, i/x vs null 24/30, d/q vs null 2/30 -> all OPEN.**
Descriptive: in f.61's hand the two leaves lean opposite ways for HASH4, d/q on f.108v and i/x on f.108r (where d/q scores below null 28 times in 30).
With H195 (the i anchors on f.176v are not reliably bare hashes) this is consistent with two hash signs under one pass code, like the 4-family, but
nothing here shows it. A shape sort is H212. HASH4 stays d/i/q; nothing merged.

## Campaign step H212 (29 Sept 2026, 02:53-02:56 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- two hash forms, mixed on f.108v; the leaf link misses the registered rule

Pre-registered (PROMPTS section H212; `family/h212_hash_sort.py`, key `family/h212_items.tsv`, commit a7ee044a). One Opus vision call, blind to leaf
(reply verbatim `family/passes/h212_sort.tsv`; the runner saw the sheet before the call, disclosed). Result `family/h212_hash_sort_result.txt` (`--check` OK):
- The reader's two groups: **A = a figure-4 stroke rising above the hash, usually one vertical running below the line; B = two small loops sitting on
  the hash, short verticals only.** 24 of 24 sorted (tile 9 uncertain A/B).
- **By leaf: A: f.108v 9, f.108r 1; B: f.108v 5, f.108r 9; Fisher p 0.013.** Registered read-out: f.108v's share in group A is 9/14 = 0.64 < 0.7, so
  **"no leaf-linked hash form shown"**. Both leaves carry both forms, in different proportions.
What it suggests: the HASH4 pass code holds two forms, as the 4-family's codes did. f.108r's HASH4 is mostly the looped form B and leans i/x (H211);
f.108v's is mostly the 4-headed form A and leans d/q (H209/H211). H162's note (a 4 on the hash = d/q, a bare hash = i) and H195's anchors (d/q anchors
4-headed 9/10) point the same way. Untested: A = d/q, B = i/x. That is H213 (script-only, sequence gain on f.108v with HASH4 split by these groups).
HASH4 stays d/i/q; nothing merged.

## Campaign step H213 (29 Sept 2026, 02:57-02:58 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- HASH4 split by blind form on f.108v: A (4-head) d/q, B (looped) i/x beats all-i/x and the reverse (script-only)

`scripts/f61hash4_form_seq.py` (committed before the run; result `scripts/f61hash4_form_seq_result.txt`, `--check` fresh). f.108v (bowl relabel) with its
14 HASH4 split by H212's blind groups (A 9, B 5), H198's rule, 30 resamples, seed 213:
- **split (A d/q, B i/x) vs all i/x: 30/30 -> CONFIRMED; vs the reverse split (A i/x, B d/q): 30/30 -> CONFIRMED; vs all d/q: 24/30 -> OPEN.**
Descriptive: on f.108v the 4-headed hash reads d/q and not i/x, and the reverse assignment loses in every resample. Whether the looped hash is i/x
rather than d/q rests on 5 signs here and is OPEN. With H211 (f.108r, mostly looped, leans i/x) and H195 (the Desportes d/q anchors are 4-headed 9/10),
this supports a second shape split, HASH4 = 4-head d/q vs looped i/x, the same kind of split as the 4-family's bowl. The evidence is sequence-only, no
period letters yet in f.61's hand; H214 tests it against the f.176 period letters. f.61 itself has one HASH4 (L01). HASH4 stays d/i/q; nothing merged.

## Campaign step H214 (29 Sept 2026, 02:58-03:00 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- the looped hash against f.176's period letters: CONTROL FAIL (the form is absent from Desportes's leaves)

Pre-registered (PROMPTS section H214; `family/h214_loops.py`, commit 91d00793). H195's unchanged 60 strips, regenerated, key byte-identical; direction
fixed before the call (looped = i). One Opus vision call, blind (`family/passes/h214_attribute.tsv`). Result `family/h214_loops_result.txt` (`--check` OK):
**anchors 10 of 20 in the pre-stated direction (gate >= 17): CONTROL FAIL.** The reader answered "no" or "n" on all 60 strips: none of the i anchors
(no 6, n 4) nor any other f.176 HASH4 sign carries H212's two small loops on the hash.
What it says: the looped hash of f.108r/f.108v does not occur in Desportes's hand on f.176, so this instrument cannot test it against f.176's period
letters. The f.176 i-signs are some other form, which H195 also could not separate. The HASH4 form split (H212/H213) therefore stays sequence-only
in f.61's hand. The period-letter test it needs is on a leaf in that hand with a gloss at HASH4 positions: f.108r's overlay rows carry none (checked
this session), and f.61's one HASH4 (L01) is outside Tomokiyo's letters. Not re-briefed with the same question (rule 3). Nothing merged.

## Campaign step H215 (29 Sept 2026, 03:01-03:09 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- the model judge prefers f.108v's HASH4 form split in both seeds

Pre-registered (scripts/PROMPTS.md section H215; `scripts/f61judge108v_hash.py`, sets and keys committed 19c9e973). Two Opus text calls, H205's
prompt; calibration = this session's H205 control. Replies verbatim `scripts/f61judge_f108v_hash_s21{5,6}_verdict.tsv`; results `_result.txt` (`--check` fresh).
- **seed 215: form split (A 4-head d/q, B looped i/x) 8.0, rank 1 of 21; all-d/q 7.5, all-i/x 6.5, reverse 6.0, HASH4 dropped 7.0.**
- **seed 216: form split 7.0, rank 1 of 21; all-d/q 6.0, all-i/x 5.0, reverse 3.5, dropped 5.5.**
- Registered read-out: **"prefers the form split" in both seeds.**
The margins over all-d/q are small (0.5 and 1.0 points, 5 tokens apart), as H213's sequence test found (OPEN 24/30). The reverse split scores lowest
of the named sets both times, as in H213 (30/30). Together: on f.108v the 4-headed hash reads d/q (two instruments), and the looped hash reads i/x
by a small margin in both (sequence 24/30 OPEN; judge +0.5/+1.0). No period-letter test is possible yet (H214: the looped form is absent from f.176).
For the verifier, sequence and judge evidence only; nothing merged.

## Campaign step H218 (29 Sept 2026, 03:13 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- which pass code each session wrote for each shape (script-only, for the verifier)

`family/h218_code_sessions.py` (result `family/h218_code_sessions_result.txt`, `--check` OK), from the blind shape answers on disk:
- **Bowl (c/p) 4-sign written as:** 4TRI on f.176v (9/10 yes) and f.176r (7 yes of 40, the rest the no-bowl sign also coded 4TRI), 4TRI on f.61 (5/5)
  and f.108r L02-L03 (3/4); **4STEM on f.108v (19 yes, 2 no)**, where 4TRI (0/6) and C43 (0/41) are the no-bowl sign; on f.101r 4TRI (10 yes / 9 no)
  and 4STEM (6 / 11) both mix.
- **No-bowl (a/n) 4-sign written as:** C43 almost everywhere (f.61 8/8 no, f.108v 41/41, f.108r 8/8), 4TRI|C43 splits on f.176v (10/10 no), 4TRI on f.176r
  (31 no) and on f.108v (6/6).
- **Hash forms:** f.108v HASH4 A (4-head) 9 / B (looped) 5; f.108r L06 A 1 / B 9.
For the verifier and any v6 build: a 4-family or HASH4 count pooled by pass code across reading sessions mixes shapes (H203's MIXED flags are the visible
cases). Re-splitting by shape needs the blind shape answers above, not the codes. Nothing merged.

## Runner 8 handover (29 Sept 2026, 03:14 UTC by the clock, session_011Taenrv3JSdk7VjpiBjids)

Done this session (H198 status, H199-H215, H218; spent today 45.0/600). **The 4-family bowl rule in f.61's hand:** on f.108v the bowl sign is the passes'
4STEM (H199). Relabelling by bowl beats the pass codes by sequence gain (H201: 30/30, rank 1 of 201 random relabels) and by the model judge (H208:
rank 1/21 in both seeds; H205 was a design-flawed first try). On f.108r (H202) and f.101r (H207) it leans the same way but misses the registered rules.
**HASH4:** a blind sort finds two forms, 4-head and looped (H212). On f.108v the split 4-head d/q, looped i/x beats all-i/x and the reverse 30/30
(H213), and the judge prefers it in both seeds (H215; small margin over all-d/q). The looped form is absent on f.176 (H214 control fail), so there is
no period-letter test yet. For the orchestrator: a "key source" ROOM line was posted at 02:49 for the bowl rule. Open for runner 9: **H216** (one vision
call, bowl and hash forms on f.108r L04-L06; crops images/f108g, images/f108h; seg/x in scripts/f61recon108r_draft.tsv; the H193 control strips
regenerate with the natives of btv1b9060633d f327/f328 and `family/cut_bands.py` as in NOTES H199), then **H217** (script, H201's design on f.108r).
Scripts to copy: `family/h199_bowl_108v.py` (tiles from a native with a marker above), `family/h212_hash_sort.py` (sort design),
`scripts/f61bowl_108v_seq.py` (relabel + seq gain + random-relabel null).

## Campaign step H216 (29 Sept 2026, 03:10-03:14 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- the bowl on f.108r L04-L06: two bowl signs, both coded 4STEM

Pre-registered (PROMPTS section H216; `family/h216_bowl_108r.py`, key `family/h216_items.tsv`, commit c9f1bb69). 15 4-family signs of the H108 draft cut
from the local source images; one Opus vision call (`family/passes/h216_reply.tsv`). Result `family/h216_bowl_108r_result.txt` (`--check` OK),
positions `family/h216_bowl_positions.tsv`: **repeat control 19/20 PASS; bowl yes only at L06 positions 3 and 32 (both 4STEM); 4STEM 2 yes / 4 no,
4TRI 0/1, C43 0/4, 4PI 0/4.** So on these rows the bowl (c/p) sign is rare, and where it occurs the H108 passes coded it 4STEM, as on f.108v (H199).
The one 4TRI is the no-bowl sign. Descriptive; nothing merged. H217 relabels these rows by shape.

## Campaign step H217 (29 Sept 2026, 03:16-03:18 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- f.108r L04-L06 relabelled by shape: OPEN (script-only)

`scripts/f61shapes_108r_seq.py` (committed 0f158193 before the run; result `scripts/f61shapes_108r_seq_result.txt`, `--check` fresh). Shape labels from
H216 (bowl) and H212 (hash form): 4BOWL 2, 4NOB 9, HASHA 1, HASHB 9 (4PI left as coded). **(1) shapes vs pass codes (HASH4 i/x): 18/30 -> OPEN. (2) whole
rows: gain 0.194 vs 0.183; the real shape placement ranks 13 of 201 random placements (best 0.204).** Descriptive: on these rows the pass codes already
mostly follow shape (the lone 4TRI becomes a/n, two 4STEM become c/p, one HASH4 becomes d/q), so the relabel changes few tokens and sequence gain
cannot separate them at this N. It is no evidence against H201/H213; f.108r adds nothing either way. Nothing merged.

## Runner 8 close (29 Sept 2026, 03:19 UTC by the clock, session_011Taenrv3JSdk7VjpiBjids)

Stopping near the context line. Since the 03:14 handover, H216 (f.108r L04-L06 bowl: 2 bowl signs, both 4STEM) and H217 (OPEN) are done. Rows written for
runner 9: **H219** (script-only: a TEST key, v5 + the two shape splits, on f.61's spans and f.108r's overlay, H196's design), **H220** (one vision call:
does the looped hash occur on fr.3982 f.101r, whose HASH4 positions carry period letters? the only route found to a period-letter test of the hash
split), **H221** (bowl and hash forms on fr.3983 f.106r, the other fr.3983 leaf on disk, to see whether its pass codes follow shape). Spent today 46.1/600.

## Campaign step H219 (29 Sept 2026, 03:47-03:50 UTC by the clock, runner 8 session_011Taenrv3JSdk7VjpiBjids) -- a shape-rule TEST key keeps every known letter but one (script-only)

`family/h219_shape_testkey.py` (committed before the run; result `family/h219_shape_testkey_result.txt`, `--check` OK), H196's design. On the span lines
the reader codes coincide with shape (H194, H202), so the shape rule there is 4TRI c/p, C43 a/n, 4STEM a/n (v5: c/p/t, a/n, a/c/e/n). **f.61 five
spans 53/55 under v5 and under the test key; f.108r overlay 74/84 under both (2000 permuted keys: none reach either); the one known exception is H202's
S14, a no-bowl 4TRI at letter c, which the shape rule reads a/n (-1). Pre-stated gate (no loss on f.61, at most one on f.108r): PASS.** The shape rule is
handed to a verifier as a v6 candidate: 4-family read by the blind bowl answer (bowl c/p, no bowl a/n), which narrows v5's 4TRI (drops t) and 4STEM
(drops c/e, moving f.108v's bowl 4STEM to c/p by shape). HASH4's form split (H212-H215) is not in this test: no HASH4 lies on a span line. No merge.

## Campaign step H220 (29 Sept 2026, 03:53-03:57 UTC by ROOM.md's machine stamps, runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- H212's hash forms against f.101r's period letters: the 4-head form is d/q there; the looped form is absent and the i/x sign is a third shape

Pre-registered (PROMPTS section H220; `family/h220_hash_101r.py`, key `family/h220_items.tsv`, commit d144a441, before the call). The row asked for 10 i +
10 d/q HASH4 positions; the pool has HASH4 i only 3 usable (all `conflict:d`), because f.101r's readers coded this leaf's i/x sign H24 (align_period.py's
code for pass A HASH4 + pass B 4STEM; period i 170). Targets: HASH4 d/q 12, HASH4 i 3, H24 i 12 (grade C gloss letters from passes/f101r_align_v4.tsv),
strips as H207 from a fresh Gallica native of btv1b9060543f f210 (1 request, family/requests.log); anchors: 10 of H212's own f.108 tiles (A 5, B 5; tile
9 excluded), shuffled in. One Opus vision call, fixed categories A (4-head) / B (two loops) / N, inline reply (`family/passes/h220_reply.tsv`); the runner
looked at sheet 1 once for marker geometry before the call (disclosed in PROMPTS). Result `family/h220_hash_101r_result.txt` (`--check` OK):
- **Anchor control 9/10 PASS** (H212 group A 5/5, group B 4/5).
- **HASH4 d/q: A 11, N 1, B 0. H24 i: N 11, A 1, B 0. HASH4 i (conflict rows): A 1, B 1, N 1.** Pooled B vs A by letter: p 0.21 -> registered read-out
  **"no form-letter link shown by the registered rule"** (B i-share 1.00 on n = 1, A d/q-share 0.85).
What it says, descriptively: on f.101r the period-read d/q sign is the 4-headed hash (form A), the direction H213/H215 took on f.108v. The half that
matters for the split -- looped form B = i/x -- is not testable here: f.101r's i/x sign is H24, which the reader puts in neither form, and form B occurs
once. With H214 (absent from Desportes's f.176), no glossed leaf yet carries form B, so HASH4 B = i/x stays sequence-only (H213) and judge-only (H215).
Not merged; v5 unchanged. Added: H222 (is form B the same sign as H24 in another hand? a matched-scale blind sort, since H220's strips and anchors differ
in scale) and H223 (script-only table of which code each glossed hand used for its i-sign and d/q-sign).

## Campaign step H222 (29 Sept 2026, 03:59-04:01 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- the looped hash is not f.101r's H24: three hash shapes at matched scale

Pre-registered (PROMPTS section H222; `family/h222_loop_h24.py`, key `family/h222_items.tsv`, commit 8b7a95e0, before the call; the runner looked at sheet 1
twice to fix marker geometry and disclosed its own impression there). 22 tiles at matched scale: f.108 H212 group A 5 + B 5, f.101r H24 i 6 + HASH4 d/q 6
(positions not used in H220), leaf hidden. One Opus vision call, free sort (`family/passes/h222_sort.tsv`). Result `family/h222_loop_h24_result.txt`
(`--check` OK). The reader's groups: **A "4#"** (a 4 on the hash), **B "2#"** (a 2-hook into the hash), **C a compact hash with small closed loops, no numeral**.
- **H24 i: B 5, A 1. f.101r HASH4 d/q: A 6. f.108 H212-A: A 4, C 1 (W14, a tile the reader called faint). f.108 H212-B: C 5.**
- Registered statistic (B in H24's group + A outside it) 5 of 10, exact p 1.000 over 252 -> **"no link shown"**: f.108's looped form is not f.101r's H24.
Reported, not gated: f.108's 4-headed form sorts with f.101r's period-read d/q sign (10 of 11), which agrees with H220 (f.101r HASH4 d/q answered 4-head
11/11) and with H213/H215's d/q reading of form A on f.108v. The looped form B has now been found on no glossed leaf read so far (f.176 H214, f.101r
H220/H222), so HASH4 B = i/x stays sequence-only. But **f.188r's gloss alignment puts HASH4 under i 10, x 3, d 12, q 3** (passes/f188r_align_v4.tsv),
the one glossed leaf on disk whose HASH4 carries both letter sets: H224 (rank 1) runs H220's design there. Nothing merged; v5 unchanged.

## Campaign step H224 (29 Sept 2026, 04:02-04:04 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.188r's HASH4 i/x rows are the "2#" sign: the 4-head reads d/q, the 2-hook reads i/x

Pre-registered (PROMPTS section H224; `family/h224_hash_188r.py`, key `family/h224_items.tsv`, commit 76d462e1, before the call). f.188r (fr.3984, Desportes's
hand; native btv1b9060633d f351, sha1 = MANIFEST) is aligned to its separate decipherment f.184r; passes/f188r_align_v4.tsv puts HASH4 under d 12 (all
'agrees'), q 3, i 10, x 3 (all 'conflict:d'). Targets: every usable i/x row (11) and 12 d/q, at H222's matched scale; anchors: 10 H212 tiles. Categories
A 4-head / B looped / C plain hash / D 2-hook into the hash / N. **Disclosure:** D and its read-out were added after the runner's geometry look at sheet 1,
where several targets looked like a 2 hooked into a hash; the runner did not see which targets carried i/x. One Opus vision call, inline
(`family/passes/h224_reply.tsv`). Result `family/h224_hash_188r_result.txt` (`--check` OK):
- **Anchor control 9/10 PASS** (A 4/5 with one N, B 5/5).
- **Targets: D (2#) i/x 8, d/q 0; A (4-head) i/x 2, d/q 12; C i/x 1; B 0; N 0.**
- Read-outs: B vs A "no link" (no looped sign on f.188r, as H214 found on f.176); C vs A "no link" (n 1); **D vs A: i/x-share 1.00 (8), A d/q-share 0.86,
  Fisher p 0.00014 -> "f.188r's letters follow the hash forms (2-hook i/x, 4-head d/q)"**.
What it says: f.188r's passes coded the "2#" sign as HASH4 at these positions (elsewhere on the same leaf they coded it H24: f188r H24 carries i 34), and
the gloss letters there are i/x -- the value f.101r's period decipherment gives H24 (i 170). So v5's HASH4 row "i 10, x 3 (f.188r/f.184r)" is, by shape,
support for H24 i/x, and HASH4 proper (the 4-head) reads d/q on every glossed leaf tested (f.101r 11/11 H220, f.188r 12/14 here, f.274r d 5 q 5).
The "conflict" status of those rows was a coding merge, not a misalignment. Nothing merged: a key-source line for the verifier was posted. The looped
form B (f.108) remains without a glossed occurrence; its i/x lean stays sequence-only (H213) and judge-only (H215). Added H225 (test key with the
re-split, script-only) and H226 (the stray-letter HASH4 rows by shape).

## Campaign step H225 (29 Sept 2026, 04:04-04:05 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- HASH4/H24 counts re-split by H224's shapes (script-only, descriptive)

`family/h225_hash4_resplit.py` (committed before the run; result `family/h225_hash4_resplit_result.txt`, `--check` OK). The row's H219-style gate (f.61 spans,
f.108r overlay) was **not run: a non-test by construction** -- no HASH4 or H24 lies on a span or overlay position, so a key change confined to those two
codes cannot score differently (CLAUDE.md rule 3). Descriptive part: H224's eight 2-hook rows (i 7, x 1) moved from HASH4 to H24 on f.188r.
- v5 HASH4 d/q: f.101r 67/108, f.188r 15/39, f.274r 10/10; **pooled 92/157 = 0.586 -> 0.617 after** (f.188r 15/31).
- v5 H24 i/x/j/y: pooled 233/296 = 0.787 -> 0.793 after.
HASH4 proper still carries many stray letters (p 7, s 6, n 5, b 4, f 4, o 4 ...), most on f.101r and on f.188r's conflict rows; H226 asks whether those
positions are other shapes. Nothing merged.

## Campaign step H226 (29 Sept 2026, 04:06-04:08 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- stray-letter HASH4 rows are mostly the 4-head; the looped form appears on f.101r

Pre-registered (PROMPTS section H226; `family/h226_hash4_strays.py`, key `family/h226_items.tsv`, commit b6c198f7, before the call; the runner did not look at
the sheets). 24 HASH4 rows whose period letter is not d/q/i/x (f.188r all 10, f.101r 14 of 22), anchors 10 H212 tiles, H224's five categories, one Opus
vision call (`family/passes/h226_reply.tsv`). Result `family/h226_hash4_strays_result.txt` (`--check` OK):
- **Anchor control 9/10 PASS.**
- **Strays: A (4-head) 17, B (looped) 3, D (2#) 3, C 1.** f.188r: A 9, D 1 (e). f.101r: A 8, B 3 (p, p, y), D 2 (b, s), C 1 (s).
- Read-out: non-A share 0.29 vs the d/q reference 3/26, Fisher p 0.16 -> **"mixed"** (neither pre-stated extreme).
What it says: most stray HASH4 letters sit on the ordinary 4-headed sign, so they are misplaced letters (f.188r's are all 'conflict' rows) or a wider
cell than d/q -- the shape test cannot tell which. A few are other shapes (2# at b/e/s, one plain hash). **The looped form B does occur on f.101r** (3 here,
1 in H220), so a period-letter table for B is possible after all: H227 shape-reads every remaining f.101r HASH4 position. Nothing merged.

## Campaign step H227 (29 Sept 2026, 04:09-04:10 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- every f.101r HASH4 position by shape: the looped form is rare and never at d/q

Pre-registered (PROMPTS section H227; `family/h227_loop_101r_all.py`, key `family/h227_items.tsv`, commit 8e3ba451, before the call; the runner did not look at
the sheets). The 32 f.101r HASH4 positions (pass-A-mapped, with a letter) not read in H220/H226, anchors 10 H212 tiles, H224's five categories, one Opus
vision call (`family/passes/h227_reply.tsv`). Result `family/h227_loop_101r_all_result.txt` (`--check` OK):
- **Anchor control 9/10 PASS.** This step: A 27, B 1 (e), N 4.
- **All three steps, f.101r HASH4 (61 read): 4-head A 47 -- d/q 34, c/p 3, a/n 2, i/x 1, other 7; looped B 5 -- i 1, p 2, y 1, e 1, d/q 0;** C 1, D 2, N 6.
- Pre-stated read-out: B n 5 < 6 -> **"too few or mixed"**. Reported, not pre-registered: B at d/q 0 of 5 vs A 34 of 47, Fisher p about 0.003 (h190.fisher).
What it says: on the leaf with a period decipherment the looped hash is rare and does not take d/q, which fits H213/H215's sequence and judge results
on f.108v (the looped form is not d/q), but its own letters are scattered, so there is still no period value for it. With f.176 (H214), f.188r (H224) and
f.101r (this step) done, no glossed leaf on disk holds enough looped signs to give it one. For the verifier: HASH4 proper (the 4-head) = d/q stands on
three leaves' period letters; the looped form stays unread. Nothing merged.

## Campaign step H221 (29 Sept 2026, 04:12-04:13 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- fr.3983 f.106r: H24 is the 2# form, HASH4 is mostly the looped form; the bowl call failed its control

Pre-registered (PROMPTS section H221; `family/h221_shapes_106r.py`, key `family/h221_items.tsv`, commit ac670071, before the calls; the runner looked at one
bowl sheet for geometry). f.106r (Mayenne's secretary; held leaf: its gloss passes agreed under 60%, so no period letter is used). Native btv1b9059406b
f191 fetched fresh (sha1 differs from the 28 Sept fetch, as H207 saw for f210). Two Opus vision calls, inline (`family/passes/h221h_reply.tsv`,
`family/passes/h221b_reply.tsv`). Result `family/h221_shapes_106r_result.txt` (`--check` OK), per-position answers `family/h221_positions.tsv`:
- **Hash call: anchors 8/10 PASS. H24: D (2#) 13 of 13. HASH4: B (looped) 13, A (4-head) 4.** Registered read-out "does not follow" (HASH4 A-share 0.24 <
  0.8): on this leaf the HASH4 code is mostly the looped form, not the 4-head. So f.106r's secretary writes the looped hash often -- the first leaf found
  where it is common (f.108v 5/14, f.108r 9/10 by H212; f.101r 5/61, f.188r 0, f.176 0).
- **Bowl call: anchors 6/10 -> CONTROL FAIL** (4 of the 5 f.108v anchors H199 read as bowl were answered no at this 3x, x +-60 window); targets not
  scored. H229 redoes it at H199's own strip geometry.
For the verifier: H24 = 2# holds on f.106r too (every H24 the passes wrote); HASH4 there is a different sign mix from f.101r/f.188r's, so pooling HASH4
counts across these leaves mixes the looped and 4-headed forms (as H218 found for the 4-family). H228 (script-only) reads the letters the held gloss places
at the looped positions, as a conditional look. Nothing merged.

## Campaign step H228 (29 Sept 2026, 04:13-04:14 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.106r's held gloss at the looped positions: a non-test (script-only)

`family/h228_loop_106r_gloss.py` (committed before the run; result `family/h228_loop_106r_gloss_result.txt`, `--check` OK), conditional on f.106r's HELD
alignment (gloss passes under 60%). Letters placed: **H24 (2#, 12 lettered): u 5, n, a, h, m, t -- no i**; HASH4 looped B (11 lettered): a 2, t 2, i 2, q, u,
o, l, s; 4-head A: i, n. Pre-stated read-out: "no lean shown". But the H24 row is an internal positive control that fails: on f.101r the period
decipherment reads H24 i 170 times, and here the alignment gives it no i at all, so the held alignment does not place letters reliably at these
positions. **Logged as a non-test, not a negative**: the looped form's letters on f.106r need a better gloss read (the leaf's gloss is sparse and
interlined with heavy bleed-through, KEY.md). Nothing merged.

## Campaign step H229 (29 Sept 2026, 04:15-04:16 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.106r bowl at H199's geometry: CONTROL FAIL again, and a question for H199

Pre-registered (PROMPTS section H229; `family/h229_bowl_106r.py`, key `family/h229_items.tsv`, commit 3d59631d; the runner did not look at the sheets). The same 33
f.106r 4-family targets and 10 f.108v anchors as H221, every strip cut exactly as h199_bowl_108v.py cuts (250 native px, box top+20 to bottom+30, x1.44, one
triangle above). One Opus vision call (`family/passes/h229_reply.tsv`). Result `family/h229_bowl_106r_result.txt` (`--check` OK):
**anchors 5/10 -> CONTROL FAIL; H199's five bowl-yes anchors all answered no, its five no-anchors all no.** Targets not scored.
With H221 (4 of 5 yes-anchors answered no at another geometry), 9 of 10 f.108v signs H199 read as "bowl" are read "no bowl" by two fresh blind calls.
The difference from H199's own call: H199 put H193's 60 f.176v strips (Desportes's hand, where the bowl is large) in the same call. So H199's yes answers
may depend on that context, and **H199 -- which H201 (sequence gain), H208 (judge) and H219 (test key) build on -- has not been reproduced.** This is not
a refutation of the bowl rule (f.176r/v, f.61 and f.101r answers came from their own calls), but the f.108v leg needs a reproduction before a verifier
relies on it. H230 (rank 1) reruns H199's exact prompt, sheets and control in one fresh call. Nothing merged.

## Campaign step H230 (29 Sept 2026, 04:17-04:21 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- H199 reproduces under its own prompt; the bowl answers depend on the call's context

Pre-registered (PROMPTS section H230; `family/h230_h199_repro.py`, commit 33dca818, before the call; the runner did not look at the sheets). H193's 60 control
strips regenerated from fresh natives (f327 sha1 a2b0d98e..., f328 4a13be67...; 2 requests) and H199's 74 f.108v strips, both item keys byte-identical;
H199's verbatim prompt in one fresh Opus call (`family/passes/h230_reply.tsv`). Result `family/h230_h199_repro_result.txt` (`--check` OK):
- **Control 18/20 PASS; Q items agree with H199's own 55/60.**
- **R items agree with H199 63/68 = 0.93; H199's 19 bowl-yes answers, 15 yes again (0.79).** By code: 4STEM yes 15 / no 10 (H199 19 / 2, n 4), 4TRI no 6,
  C43 no 40 / yes 1. Pre-stated read-out: **"H199 reproduces".**
What it says: H199's f.108v reading holds when the reader sees H193's f.176v strips (large, clear bowls in Desportes's hand) in the same call; without
them (H221, H229) the same f.108v signs were read "no bowl" 9 times of 10. So the bowl question on f.61's hand is context-dependent: a small bowl is
called only against clear exemplars. This corrects the 04:16 flag -- H199 is reproduced, with that caveat for the verifier (every bowl call should
carry H193's strips). H231 runs f.106r's bowl in H199's design. Nothing merged.

## Campaign step H231 (29 Sept 2026, 04:22-04:23 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.106r's bowl in H199's design: the 4TRI code mixes the two signs

Pre-registered (PROMPTS section H231; `family/h231_bowl_106r_h199.py`, key `family/h231_items.tsv`, before the call; the runner did not look at the sheets). H199's
verbatim prompt, part 1 = H193's regenerated strips, part 2 = f.106r's 33 4-family strips at H199 geometry; one Opus call (`family/passes/h231_reply.tsv`).
Result `family/h231_bowl_106r_h199_result.txt` (`--check` OK):
- **Control 18/20 PASS.**
- **C43: no 12 of 12. 4TRI: yes 5, no 7. 4STEM: yes 2, no 6, n 1.** Read-out: 4TRI yes-share 0.42 -> **"does not follow"** (C43 no-share 1.00).
So on f.106r the no-bowl sign is always coded C43 when C43 is written, but the 4TRI code carries both signs, as on f.176r and f.101r (H218's table), and
4STEM mostly the no-bowl sign. Any f.106r 4-family count pooled into a key would need re-splitting by these shape answers (positions in the reply/key
files). Descriptive; nothing merged.

## Campaign step H223 (29 Sept 2026, 04:24-04:25 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- the hash family by shape, code and letter (script-only, for the verifier)

`family/h223_hash_table.py` (result `family/h223_hash_table_result.txt`, `--check` OK), from the blind form answers on disk (H212, H220, H221, H224, H226, H227):
- f.101r HASH4: A 47 (d/q 34, i/x 1, other 12), B 5 (i/x 2, other 3), D 2, C 1, N 6. f.101r H24: N 11, A 1 (H220 offered no 2# category; at matched scale
  H222 sorted H24 with the 2# group 5 of 6).
- f.188r HASH4: A 23 (d/q 12, i/x 3, other 8), D 9 (i/x 8), C 1.
- f.106r (held, no letters): HASH4 B 13, A 4; H24 D 13. f.108v HASH4: A 9, B 5. f.108r HASH4: B 9, A 1.
For a v6 build: the 4-headed hash reads d/q on both period-glossed leaves; the 2# sign reads i/x (f.101r's H24, f.188r's mis-coded HASH4); the looped hash
is common only on f.61's hand (f.108r/v) and the secretary's f.106r, and has no period value. Pooled HASH4 counts mix all three. Nothing merged.

## Campaign step H235 (29 Sept 2026, 04:27-04:29 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.61's ZHOOK sorts with the period "2#" i/x sign

Pre-registered (PROMPTS section H235; `family/h235_zhook_2hash.py`, key `family/h235_items.tsv`, before the call). Disclosure: the idea came from the runner's
look at f.61's line sheets L01/L11 while placing H233's tokens; the runner did not look at the H235 sheet. 19 tiles, grey, autocontrast, all at height 180
(H178b's normalisation): f.61 ZHOOK 3 and C43 3 (H178b's positions), f.101r H24 i 5, f.101r 4-head HASH4 d/q 4 (H227 answers), f.188r 2-hook i/x 4
(H224 answers). One Opus free sort (`family/passes/h235_sort.tsv`). Result `family/h235_zhook_2hash_result.txt` (`--check` OK). Groups: **A** a 4- or
Z-shaped hooked head on two parallel slanted down-strokes; **B** a plain 4 with a 3/z tail (C43); **C** a 4 on a stem crossed by two bars (the 4-head hash).
- **ZHOOK: A 3. H24: A 4, C 1. f.188r 2-hook: A 4. C43: B 3. 4-head HASH4: C 4.**
- Pre-stated read-out: group A holds 8/9 of the 2# tiles, all 3 ZHOOK and 0 of the 7 others -> **"f.61's ZHOOK is the 2# sign"**.
- Caveat: group A is 11 of 19 tiles, so the chance of all three ZHOOK falling in it by itself is 0.17 (hypergeometric); the evidence is the clean
  three-way split (every class in its own group, none mixed but one H24), not that number.
What it says: H178b's "no link" compared ZHOOK with Desportes's small cursive i-sign; against the 2# sign of the two other period decipherments (f.101r,
f.188r) at a common height, the reader puts f.61's ZHOOK with it. v5's ZHOOK i/x (graded S on f.61 for want of a glyph link) now has a candidate glyph
link to a period i/x sign. For the verifier (VERIFY-F61-V6); not merged, grade unchanged.

## Campaign step H233 (29 Sept 2026, 04:30-04:31 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- the code 4PI names two different signs: f.101r's is the 4-head hash, f.61's is a 4 over a Pi

Pre-registered (PROMPTS section H233; `family/h233_4pi_shape.py`, key `family/h233_items.tsv`, before the call; f.61 positions placed by the runner's eye and those
three crops checked, the sheet not seen). 18 tiles at H235's normalised height: f.101r's 7 pass-A-mapped lettered 4PI, f.61's L01 11 (HASH4), L01 12 and L11 9
(4PI), anchors H235's 4-head (4) and 2-hook (4) tiles. One Opus call, fixed categories (`family/passes/h233_reply.tsv`). Result `family/h233_4pi_shape_result.txt`
(`--check` OK):
- **Anchors 8/8 PASS.**
- **f.101r 4PI: A (4-head hash) 6 -- letters d/q 4, other 2; E 1 (d).** Read-out: A share 0.86 -> **"4PI is the 4-head hash"** on f.101r.
- **f.61: L01 11 HASH4 -> A; L01 12 4PI -> E; L11 9 4PI -> E** (a figure-4 over two upright stems joined by a bar, no hash).
What it says: on f.101r the readers' 4PI is the same 4-headed hash as HASH4 (and reads d/q like it); on f.61 the readers' 4PI is a different sign, a 4 over a
Pi. So v5's 4PI letters (d/a/q/n, from f.101r and f.108r) do not transfer to f.61's two 4PI tokens by glyph; those two need their own evidence (f.108r's 4PI:
H202 read p 1 / d 4 under Tomokiyo's overlay -- which sign it is there is not yet checked). f.61's L01 HASH4 is the 4-head form, which reads d/q on both
period leaves (H224/H227), not i. For the verifier and H234. Nothing merged.

## Campaign step H234 (29 Sept 2026, 04:31-04:32 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.61's meter with the shape readings (script-only, descriptive, not endorsed)

`family/h234_meter_shapes.py` (committed before the run; result `family/h234_meter_shapes_result.txt`, `--check` OK), verify_v5/meter_v5.py's bands on the same decode:
- **v5: firm 12 / two-way 50 / wider 12 / unread-or-null 25** (wider: 4TRI c/p/t 6, 4PI 2, OTHER 2, 4STEM 1, HASH4 1).
- **v5 + the shape readings (none endorsed): 12 / 58 / 2 / 27** -- 4TRI c/p/t -> c/p x6 (bowl, H194/H219), 4STEM -> a/n x1 (no bowl), HASH4 -> d/q x1 (4-head,
  H233 with H224/H227's period letters), 4PI -> unread x2 (a 4 over a Pi, a sign with no period value yet, H233). Only OTHER x2 stays wider.
For the verifier: the shape work narrows every wider f.61 token but OTHER's two, and correctly moves 4PI to unread rather than carry f.101r's letters onto a
different sign. Nothing merged; the key stays v5.

## Campaign step H232 (29 Sept 2026, 04:32-04:33 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- where f.61's unread classes occur (script-only)

`family/h232_unread_census.py` (committed before the run; result `family/h232_unread_census_result.txt`, `--check` OK). f.61's unread: CA 10, C6 8, LOOPBAR 4,
CROSS 2, LL 1. Elsewhere (reconciled drafts; letters where aligned): f.101r CA 6, C6 2 (e 2), LOOPBAR 1 (e), CROSS 1 (p); f.188r CA 6, C6 1 (e), LOOPBAR 1 (u),
LL 1 (e); f.106r C6 1 (held: m); f.124r CA 1, C6 4, LOOPBAR 3, CROSS 3 (held gloss); f.97r CA 8, C6 3, LOOPBAR 3, CROSS 7, LL 1 (no alignment); f.108v LOOPBAR 2,
CROSS 2; f.274 none. CA's letters are scattered (p 2, q, s, t, c, z), consistent with H63's finding that CA is cipher signs inside word runs. C6 reads e at all
three lettered positions -- small n, but the one lead. Added H236 (f.108r's 4PI shape: the same hand's overlay reads it d 4 / p 1), H237 (C6 glyph link), H238
(f.61's two OTHER tokens). Nothing merged.

## Campaign step H236 (29 Sept 2026, 04:34-04:35 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.108r's 4PI by shape: CONTROL FAIL

Pre-registered (PROMPTS section H236; `family/h236_4pi_108r.py`, key `family/h236_items.tsv`, before the call; sheet not seen). One Opus call
(`family/passes/h236_reply.tsv`), result `family/h236_4pi_108r_result.txt` (`--check` OK): **anchors 5/8 -> CONTROL FAIL** (two of the four f.188r 2-hook anchors
answered N, one of the four 4-head anchors E). The five f.108r 4PI targets are **not scored**; their raw answers stay in the reply file and are not a result.
f.61's two 4PI were answered E again, a repeat of H233 (not gated). H239: one redo with 12 anchors (gate 10/12); if it fails too, f.108r's 4PI shape is logged
untestable in this format and not retried (CLAUDE.md rule 3's repeated-attempt clause).

## Campaign step H239 (29 Sept 2026, 04:36-04:37 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.108r's 4PI is the 4-head hash; f.61's "4 over a Pi" stays unmatched

H236 with 12 anchors (PROMPTS section H239; `family/h239_4pi_108r_2.py`, key `family/h239_items.tsv`, before the call; sheet not seen). One Opus call
(`family/passes/h239_reply.tsv`), result `family/h239_4pi_108r_result.txt` (`--check` OK):
- **Anchors 12/12 PASS** (4-head 6/6 A, 2-hook 6/6 D).
- **f.108r 4PI: A (4-head hash) 5 of 5** -- at overlay letters d, p, d, d, d. Read-out: **"f.108r's 4PI is the 4-head hash"**.
- f.61's two 4PI: E (a 4 over a Pi), the third time (H233, H236, here).
What it says: in f.61's own hand (f.108r) the readers' 4PI is the 4-headed hash and the period gloss reads it d 4 of 5 (grade C, Tomokiyo's reprint) -- so the
4-head hash = d/q holds on f.101r (34/47), f.188r (12/14) and f.108r (4/5 d). f.61's L01 HASH4 is that sign (H233). f.61's two "4PI" are a different sign,
a 4 over a Pi, with no lettered occurrence on any leaf read so far; they stay unread (H234's count). For the verifier; nothing merged.

## Campaign step H237 (29 Sept 2026, 04:38-04:39 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.61's C6 and the glossed C6: no link shown

Pre-registered (PROMPTS section H237; `family/h237_c6_glyph.py`, key `family/h237_items.tsv`, before the call; f.61 positions placed by eye and the crops checked;
sheet not seen). Only two glossed C6 (f.101r, both e) map to pass A; f.188r's does not. One Opus free sort (`family/passes/h237_sort.tsv`; the reply repeated one
line, dropped). Result `family/h237_c6_glyph_result.txt` (`--check` OK): **f.61 C6: A ('6'/b-shaped) 3/3; glossed C6: D (delta-shaped) 1, unclear 1; PHI: A 1,
B 2; C43: B 1, C 2** -> **"no link shown"**. The controls split as well, so this sort was noisy; with two lettered glossed C6 the question is near its floor.
C6 stays unread on f.61 (as VERIFY-F61-V4 left it). Nothing merged.

## Campaign step H238 (29 Sept 2026, 04:40-04:41 UTC by ROOM.md's machine stamps (corrected: the runner had typed estimated times here), runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.61's two OTHER tokens (script-only, descriptive)

From scripts/read_call_U.tsv and passes U1/U2 (the unmarked-line reads of f.61 L02/L04): **L02 2 OTHER** = "two short vertical stems joined by a heavy top bar
and a heavy bottom bar, like Roman numeral II" / "a Pi with a double bar, no 4 above it, so not 4PI" -- the base of f.61's 4-over-Pi (H233) without the 4.
**L04 2 OTHER** = "an S/8-like loop joined to a b/d form, written after 'Come'; may be a handwriting abbreviation (e.g. S.M.)" (pass U2, low confidence).
No atlas class with period letters matches either; they stay 'wider'/unread. No call.

## Runner 9 handover (29 Sept 2026, 04:41 UTC by ROOM.md's machine stamp (corrected from an estimated 07:12), session_012NTadgrCBftz3oRtgw5jFu)

Done this session: H220-H239 (plus H223, H225, H228, H232, H234, H238 script-only); spent today 62.45/600. Stopping near the context line by the runner's own
estimate (~480k): get_session reported used_tokens 0 at the time. RETRACTED at 04:45 UTC: get_session then read 432,550 (< 600k), so runner 9 continued.
**Hash family (for VERIFY-F61-V6):** three signs share the pass code HASH4 -- the 4-headed hash reads d/q on f.101r (34/47, H227), f.188r (12/14, H224) and
f.108r in f.61's hand (its "4PI", d 4/5, H239); the "2#" sign reads i/x (f.101r's H24, f.188r's mis-coded HASH4 8/8, H224) and f.61's ZHOOK sorts with it (H235,
pre-stated PASS, caveat p 0.17); the looped hash is common only on f.108r/v and f.106r and has no period value (rare on f.101r, 5/61, never d/q, H227).
**4PI:** f.101r's and f.108r's 4PI are the 4-head hash; f.61's two 4PI are a different sign, a 4 over a Pi (H233/H236/H239), with no lettered occurrence.
**Bowl:** H199 reproduces under its own prompt (H230); bowl calls need H193's f.176v strips in the same call (H221/H229 failed without them). f.106r's 4TRI mixes
bowl and no-bowl (H231). **f.61 meter** with the shape readings (not endorsed): 12 / 58 / 2 / 27 (H234). Key-source lines posted 04:04 (H224), 04:29 (H235),
04:32 (H234). Open for runner 10: **H240** (script test key, 4-head 4PI on f.108r's overlay), **H241** (script: which leaf could give the looped hash or the
4-over-Pi a period value), **H242** (judge on f.61's 4-over-Pi tokens). Scratch natives (f210, f351, f191, f327/f328) are not committed; fetch_gallica.py
regenerates them (sha1s in family/requests.log).

## Campaign step H240 (29 Sept 2026, 04:46-04:48 UTC by the clock, runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- 4PI split by shape keeps every known letter; Tomokiyo reads f.61's 4-over-Pi n (script-only)

`family/h240_4head_testkey.py` (committed 1bea2d34 before the run; result `family/h240_4head_testkey_result.txt`, `--check` OK), H219's design. f.61's L11 9 4PI
(a 4 over a Pi, H233) lies in Tomokiyo's span S5 and **he reads it n** (family/h191_4fam_f61_result.txt, published). Test keys: f.61 4PI a/n (the no-bowl 4's
cell), f.108r 4PI d/q (the 4-head, H239).
- **f.61 five spans: v5 53/55; 4PI a/n 53/55; 4PI unread 52/55** (2000 permuted keys: none reach 53).
- **f.108r overlay: v5 74/84; 4PI d/q 74/84.**
- Pre-stated gate (no f.61 loss, <= 1 on f.108r): **PASS**.
**Correction to H234:** H234 set f.61's two 4PI to unread for want of a period value; Tomokiyo's published span already reads one of them n, and the a/n cell
keeps it. The shape-reading meter is therefore **12 / 60 / 2 / 25** (4PI a/n x2 two-way), not 12 / 58 / 2 / 27. For the verifier: the code 4PI is two signs --
the 4-headed hash (f.101r, f.108r: d/q) and f.61's 4-over-Pi (a no-bowl 4, read n by Tomokiyo). Nothing merged.

## Campaign step H241 (29 Sept 2026, 04:49 UTC by the clock, runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- where a period value for the looped hash could come from (notes only)

From family/MANIFEST.tsv, H221-H227 and the H96 notes: the looped hash is common only in f.61's hand (f.108r 9/10, f.108v 5/14) and the secretary's (f.106r 13/17).
Of those leaves, f.108v's interlines are clear words (not a decipherment), f.108r's overlay (Tomokiyo's reprint) covers rows L02-L03 where no HASH4 falls,
f.211r has one ~15-sign glossed run (desk pack H96, waiting on ASKS 93), and **f.106r carries an interlinear period gloss that the model gloss readers could
not read reliably (held; H228 showed its alignment misplaces letters)**. So the one route found is a person's read of f.106r's gloss above its looped hashes.
H243 builds that desk pack (script-only); filing the ASKS row is left to the orchestrator. No call.

## Campaign steps H242 (dropped) and H243 (29 Sept 2026, 04:50 UTC by the clock, runner 9 session_012NTadgrCBftz3oRtgw5jFu)

**H242 dropped:** the judge on f.61's 4-over-Pi is superseded by H240 -- Tomokiyo's published span S5 already reads it n, and the a/n cell keeps it.
**H243 (script-only):** desk pack `family/images/person_pack_106r/` (`family/h243_pack_106r.py`, native btv1b9059406b f191): six row sheets of f.106r at 1.5x from 60 px
above each cut row, 17 HASH4 signs arrowed and numbered N01-N17 (looped 13, 4-head 4 by H221; `key.tsv`, not for the reader), README with the question and an
answer template (`family/passes/f106r_hash_person.tsv`). Filing an ASKS row for a person's read is the orchestrator's decision. No reading.

## Campaign steps H244 and H246 (29 Sept 2026, 04:51 UTC by the clock, runner 9 session_012NTadgrCBftz3oRtgw5jFu)

**H244 (script/notes):** `family/v6_shape_candidates.tsv` -- one row per shape-based cell proposed since v5 (4-family bowl rule; HASH4's 4-head d/q, mis-coded 2#
i/x, looped hash without a value; H24 = 2#; ZHOOK = 2#; 4PI's two signs; the f.61 meter by shape 12/60/2/25), each with evidence for and against, controls, the
test-key result and the result files, for VERIFY-F61-V6. Nothing merged. **H246 dropped:** f.108v's reconciled draft has no 4PI, so there is nothing to read.

## Campaign step H245 (29 Sept 2026, 04:52 UTC by the clock, runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- every shape cell at once: PASS (script-only)

`family/h245_shape_key_all.py` (committed c01b9985 before the run; result `family/h245_shape_key_all_result.txt`, `--check` OK). Test key = v5 with 4TRI c/p, C43 a/n,
4STEM a/n, and 4PI a/n on f.61 (4-over-Pi) / d/q on f.108r (4-head). **f.61 five spans 53/55 (v5 53/55); f.108r overlay 74/84 (v5 74/84)**; with H202's S14 the
f.108r loss is 1. Pre-stated gate: **PASS**. The permuted-key p95 drops (f.61 0.455 -> 0.436, f.108r 0.429 -> 0.405): narrower cells, same known-letter score.
This is the combined candidate in family/v6_shape_candidates.tsv, handed to VERIFY-F61-V6; nothing merged, v5 stays current.

## Campaign step H249 (29 Sept 2026, 04:54 UTC by the clock, runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- a pre-registered shape-key prediction of f.108r L04-L06 (script-only)

`scripts/f61shape_f108r_predict.py` -> `scripts/f61shape_f108r_prediction.txt` (`--check` OK), committed before any person's read of these rows' period gloss
(ASKS 88). H120's beam and map with cells set by blind shape: 4-family by H216's bowl answers, HASH4 by H212's forms (4-head d/q; looped i/x, flagged: no period
value). **Pairs changed from H120: L04 1 4TRI (no bowl) c/p -> a/n; L06 3 and L06 32 4STEM (bowl) a/n -> c/p; L06 40 HASH4 (4-head) i/x -> d/q. Beam letters
differ at 8 of 85 positions** (L04 1 c->n, L04 2 z->m, L04 3 i->x, L06 3 n->p, L06 4 e->r, L06 32 n->p, L06 34 m->z, L06 40 i->d). When ASKS 88 is answered, those
eight positions decide between the code-level map (H120) and the shape rule, on letters neither was fitted to. No reading; nothing merged.

## Campaign step H247 (29 Sept 2026, 04:55 UTC by the clock, runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.61's unread classes against Tomokiyo's table drawings (notes only)

Atlas descriptions (scripts/f61_atlas.tsv) against the drawing descriptions of keys/key_mayenne_1592.tsv (Tomokiyo's reconstructed table, published), with
F61-CAL's caveat that his drawings mislabel 8 of 10 of this hand's shape classes: **CROSS** ("a plain plus or cross, possibly with a stroke rising to the upper
right") matches his row-1 drawing almost word for word, in the a/n column (a); **C6** ("the digit 6") partly matches his word-code drawing for *pour* ("a hook or
loop like a numeral 6 into one long diagonal stroke") -- f.61's C6 is a plain 6 without the diagonal (H237's crops); **CA, LOOPBAR, LL** and the 4-over-Pi match
no drawing. Leads for the verifier or a later test (CROSS a/n; C6 = *pour*?), not values. No call.

## Campaign step H250 (29 Sept 2026, 05:47 UTC by the clock, runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- audit status in the v6 candidate table

`family/v6_shape_candidates.tsv` gains an `audit_status` column from AUDIT.md VERIFY-F61-V6/V7: the hash family by shape (4-head d/q; the 2# sign i/x, taking
f.188r's mis-coded rows; the looped hash a separate unread row) is **endorsed by V7**; the bowl rule is endorsed in part by V6. **Still pending audit:** ZHOOK =
the 2# sign (H235; V7 calls it a grade question for ZHOOK's row) and 4PI's two signs (H233/H239/H240; with 4PI a/n on f.61 the V7 meter 12/58/4/25 would read
12/60/2/25). Notes only.

## Campaign step H254 (29 Sept 2026, 05:51 UTC by the clock, runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.108r's ZHOOK is the 2# sign, at overlay letter i

Pre-registered (PROMPTS section H254; `family/h254_zhook_108r.py`, key `family/h254_items.tsv`, before the call; sheet not seen). Targets: the 7 pass-A ZHOOK on f.108r
L02/L03 (f.61's hand), each at an overlay letter i (Tomokiyo's reprint of the leaf's period gloss, aligned by f61crib.align under v5 -- caveat: v5 carries ZHOOK
i/x, so the pairing can follow the code); anchors 12 (4-head 6, 2# 6). One Opus call (`family/passes/h254_reply.tsv`); result `family/h254_zhook_108r_result.txt`
(`--check` OK): **anchors 11/12 PASS; f.108r ZHOOK: D (2#) 6, N 1 -> "f.108r's ZHOOK is the 2# sign"**.
With H235 (f.61's ZHOOK sorts with the 2#) and VERIFY-F61-V7 (2# = i/x on f.101r/f.188r), the glyph link now runs through f.61's own hand: the sign the readers
code ZHOOK in this hand is the 2# sign, and its same-hand period gloss reads it i. For the ZHOOK grade question V7 left open; nothing merged.

## Campaign step H255 (29 Sept 2026, 05:49-05:52 UTC by the clock, runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- f.108r L04-L06's 4PI are the 4-head hash too

Pre-registered (PROMPTS section H255; `family/h255_4pi_108r_l46.py`, key `family/h255_items.tsv`, before the call; sheet not seen). f.108r L04-L06's four 4PI (H108
draft, crops images/f108g|f108h) and f.61's two 4PI, anchors 12. One Opus call (`family/passes/h255_reply.tsv`); result `family/h255_4pi_108r_l46_result.txt`
(`--check` OK): **anchors 12/12; f.108r 4PI: A (4-head hash) 4 of 4; f.61 4PI: E 2** (the fourth read giving E). With H239, every 4PI on f.108r (9) is the 4-head
hash; the 4-over-Pi has been seen only on f.61 (two signs, one read n by Tomokiyo). Descriptive; nothing merged.

## Campaign step H253 (29 Sept 2026, 06:48-06:48 UTC by the clock, runner 9 session_012NTadgrCBftz3oRtgw5jFu) -- positions for f.61's signs (infrastructure)

Pre-registered (PROMPTS section H253; ruler sheets by `scripts/f61positions_sheets.py`, not seen by the runner). Two blind Opus calls listed every sign and clear word
per segment with its x (`scripts/h253_reply1.tsv`, `scripts/h253_reply2.tsv`, verbatim). `scripts/f61positions_score.py` (`--check` OK) joins them to read_call_A's
order where the sign counts agree: **L01 12/12, L03 15/15, L05 18/18 (one 'dot' dropped), L11 12/12 -> 57 signs with segment and x in `scripts/f61_positions.tsv`;
L07 10 vs 11 and L08 13 vs 14 are not joined.** Descriptive use (the dropped H251/H252 questions): **C6 3 joined, 0 next to a clear word; CA 5 joined, 1 next to a
clear word; PHI 0/9, C43 0/7.** So f.61's C6 sits inside cipher runs like the letter signs -- no placement support for H247's word-code lead. Note: the reader calls
the CA mark "a", and on L03 one "a" follows the clear word "Combien" (H63's finding that CA sits at text edges). For later tile work, the positions replace
eye placement on these four lines. No reading.

## Runner 9 status (29 Sept 2026, 06:49 UTC by the clock, session_012NTadgrCBftz3oRtgw5jFu)

Since the 04:41 handover (retracted at 04:45): H240-H255 and H253 done or dropped (see their sections); spent today 67.10/600. get_session read 536,853 tokens at the
06:45 firing; the next firing's reading decides whether runner 9 continues (under 600k) or stops for runner 10. Open: **H256** (is f.61's CA the clear letter a?
10 of f.61's 25 unread signs), **H257** (script: extend f61_positions.tsv to L07/L08), **H258** (LOOPBAR glyph link). Pending audit: ZHOOK = 2# (H235 + H254, same
hand at overlay i) and 4PI's two signs (H233/H239/H240/H255); candidate table family/v6_shape_candidates.tsv. Waiting on people: ASKS 88 (f.108r gloss; H249's
prediction is committed), ASKS 93 (f.211r), and a possible ASKS row for the f.106r looped-hash pack (H243).

## Campaign step H256 (29 Sept 2026, 09:58 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- f.61's CA has the letterform of the clear a

Pre-registered (PROMPTS section H256; `family/h256_ca_text.py`, key `family/h256_items.tsv`, committed f70b9432 before the call; rules and read-outs in the
docstring). Disclosure: the runner viewed images/f61sheetB_L01.jpg to place the text letters (its segment 4 shows L01's CA token in passing) and two
placement sheets of the nine TEXT tiles only; the CA/PHI/C43 crops and the test sheet were not seen. 20 tiles at H235's normalised height: f.61 CA 5
(H253's positions, L01/L03/L05), clear-text a 6 (H63's control a's: auons, parle, amplement, Cependant, ella, affere), clear-text non-a letters 3 (o, o, e,
a hand check), cipher PHI 3 and C43 3. One Opus free sort by letterform, ignoring ink, size, hand and joins (`family/passes/h256_sort.tsv`). Result
`family/h256_ca_text_result.txt` (`--check` OK):
- Groups: **A** "a cursive minuscule a: closed rounded bowl, short upright on its right, small exit tail"; **B** "43"; **C** "looped sign on a stem";
  **D** "small round o-type bowl with no upright".
- **Text a: A 6/6 (gate 1 pass). Text non-a: D 1, unclear 2 (gate 2 pass: 0 of 3 in A). CA: A 5/5. PHI/C43: C 3, B 3 (0 in A).** Hypergeometric
  P(5 of 5 CA in a group of 11 of 20) 0.030.
- Pre-stated read-out: **"CA is the clear letter a by letterform"**.
What it says, and what it does not: by the strokes alone, f.61's CA is the same letterform as the scribe's clear a, and nothing cipher-shaped sorts with
it. This complements H63, which judged the same marks by hand cues (weight, baseline, spacing) and put 5 of 6 in the cipher hand: together, CA is an
"a" written in the sign runs -- either a clear letter left among the signs or a null drawn as an a (Tomokiyo's nulls, H44). The sort cannot tell those
two apart (interpretation fixed before the call), so no key cell changes and no reading follows; the skeleton keeps CA as nulls. Caveat: the hand check
is thin -- two of the three non-a letters came back 'unclear', so only one non-a letter was actually placed outside A. The other five CA (L07, L08, L10)
have no positions yet (H257) and were not sorted. For the verifier; nothing merged. Vision calls: 1 of 4.

## Campaign step H257 (29 Sept 2026, 10:01 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- f.61 positions extended to L07 and L08 (script-only)

`scripts/f61positions_join2.py` (method in its docstring: keyword shape families, difflib alignment of the family sequences, and a word item read as the bare
letter 'a' joins an unmatched read_call_A position only where that position's class is CA; result `scripts/f61positions_join2_result.txt`, `--check` OK).
The keyword table was corrected once after a first run ('crossbar' had matched CROSS; '4 with 3/yogh-shaped tail' had fallen to the 4-family instead of
C43) -- a parsing fix, logged in the script. **L07: 10 of 11 matched by family in order, the 11th (pos 1, CA) is the item the blind reader listed as the
clear word 'a' at s2 880. L08: 13 of 14 matched, the 14th (pos 10, CA) is again a word 'a' (s2 1420), between the C6 and the 4TRI, inside the run.** Both
lines fully joined: `scripts/f61_positions_L07L08.tsv` (src column: sign / word_a) and `scripts/f61_positions_all.tsv` (H253's 57 + these 25 = 82 signs on
all six read_call_A lines). Descriptive: CA 7 positioned, 2 next to a clear word; C6 6, 1; PHI 14, C43 9, ZHOOK 3, 0 each; LOOPBAR 3, 1. What it says: a
reader given no atlas and no key takes f.61's CA for the word 'a' both at a run edge (L07 1) and inside a run (L08 10) -- the same letterform finding as
H256 from a different task. No reading; nothing merged. No call.

## Campaign step H259 (29 Sept 2026, 10:04 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- CA takes no letter in Tomokiyo's spans (script-only)

`family/h259_ca_span.py` (read-outs in the docstring, fixed before running; result `family/h259_ca_span_result.txt`, `--check` OK): the known-span
alignment (scripts/f61crib.align, the F61-CAL DP) of each of Tomokiyo's five spans under key v6's f.61 reading, printed position by position with his
markup character. **Four CA fall inside the spans and every one pairs with his dash: L03 9 (est ca[-]p able), L05 7 and 8 (trop [--] avancees), L08 10
(beau [-][-] pere, the first dash being C6).** The words around them are complete without an a -- every a of capable, avancees, beau is supplied by a C43
(a/n) -- so CA is not a clear letter left among the signs; three of the four sit at a word boundary and one inside a word. Controls: C43 pairs with a letter
of its cell 9/9, PHI 13/13. Pre-stated read-out: **"CA takes no letter"**. With H256 (the letterform of the clear a) and H63 (the cipher hand): f.61's CA
is a null drawn as the letter a, which is what Tomokiyo's markup already treats it as (H44); no cell changes, the skeleton keeps CA as nulls, and the
10 CA stay in the unread-or-null band. Two descriptive notes for the verifier: (1) C6 pairs with his dash at all six in-span positions (L01 2, L03 11,
L05 12 skipped, L07 6, L08 3, L08 9) although the pooled key carries C6 = e from three glossed tokens on other leaves (H232) -- a leaf-level conflict of
the rule-4 kind, already held at unread by V7's meter, logged here so the count is on record; (2) the DP places a valueless sign against a dash or skips
it at equal score, so the CA positions above are fixed only where both neighbours carry letters (all four do). No call.

## Campaign step H260 (29 Sept 2026, 10:08 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the other five CA: the same letterform as the clear a

Pre-registered (PROMPTS section H260; `family/h260_ca_text.py`, key `family/h260_items.tsv`, committed a8b4f9fa before the call; H256's rules, gates and
read-outs). Disclosure: the runner viewed images/f61sheetB_L02.jpg (a line with no CA) to place its letters and two ruler sheets of the nine TEXT tiles;
the CA crops (L07 1, L08 10 at H257's positions; L10's three at H63's positions, each re-centred on its ink centroid by script), the PHI/C43 crops and
the test sheet were not seen. One Opus free sort (`family/passes/h260_sort.tsv`); result `family/h260_ca_text_result.txt` (`--check` OK):
- Groups: **A** "crossed 4 ... with a 3-like hook" (C43), **B** "figure-8 or double loop on a long descender" (PHI), **C** "the ordinary cursive
  minuscule a: a closed round bowl with a short right-hand stem and no descender", **D** "the ordinary cursive minuscule o".
- **Text a: C 6/6 (gate 1). Text non-a: D 2, unclear 1 (gate 2: 0 of 3 in C -- this time two of the three were placed, in their own o group).
  CA: C 5/5. PHI/C43: B 3, A 3 (0 in C).** Hypergeometric P 0.030. Pre-stated read-out: **"CA is the clear letter a by letterform"**.
Taken with H256: **all ten CA of f.61, on six lines, sort with the scribe's clear a in two independent blind calls (10/10; cipher controls 0/12; non-a
letters 0/6)**, while H63 puts them in the cipher hand by weight, baseline and spacing and H259 finds no letter for them in Tomokiyo's markup. The
consistent account is a null drawn as the letter a, which is what the skeleton and Tomokiyo's markup already hold (H44). No cell changes, no reading;
the CA class is now described rather than unread: for the verifier's meter wording (unread-or-null -> null, on this evidence), not for any key edit.
Vision calls this session: 2 of the brief's 4 per step (one per step).

## Campaign step H261 (29 Sept 2026, 10:10 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- C6 = e gains nothing on f.61; the classes Tomokiyo never letters (script-only)

`family/h261_c6_markup.py` (result `family/h261_c6_markup_result.txt`, `--check` OK). The five known spans under key v6's f.61 reading score the same with the
pooled C6 = e cell and with C6 removed (50/55 either way in this run, which scores the raw markup; build_key_v6's scorer folds j->i and v->u and reports
53/55 -- the three letters of difference are v, v, j, the same both ways here, so the comparison is like for like). **Every in-span C6 (L01 2, L03 11,
L07 6, L08 3, L08 9) pairs with his dash.** Census of f.61 classes that pair only with his dash in the spans: **C6 5, CA 4, CROSS 2, 4STEM 1, CH 1, LL 1,
LOOPSTEM1 1**; every other class pairs with letters of its cell. What it says: the pooled C6 = e (grade C on f.101r/f.188r, three tokens) has no support
on f.61 -- Tomokiyo reads it as nothing at all five places, and H237 found no glyph link between f.61's plain 6 and the glossed delta-shaped C6 -- so a
rule-4 conflict row is filed in HYPOTHESES.md with both witnesses; the verifier already holds f.61's C6 at unread-or-null and the count stays 8. The
4STEM dash (L11 8) is on record too: the F61READ 4STEM a/n rests on f.176r's no-bowl positions (V6), not on a letter of his at L11. No call.

## Campaign step H262 (29 Sept 2026, 10:12 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the null band as one table for VERIFY-F61-V9 (script-only)

`family/f61_null_band.py` -> `family/f61_null_band.tsv` (result `family/f61_null_band_result.txt`, `--check` OK): one row per f.61 token in the meter's
unread-or-null band (25: CA 10, C6 8, LOOPBAR 4, CROSS 2, LL 1) and the four wider tokens (4PI 2, OTHER 2), with the v6 letters, the span and Tomokiyo's
character where the token lies inside one of his spans (15 of the 29 do), the class's evidence in one cell (the runner's summary of H63/H256/H259/H260 for
CA; H237/H259/H261 and the HYPOTHESES.md conflict row for C6; H232/H258 for LOOPBAR; H247/H261 for CROSS; H259 for LL; V8 for 4PI; H238 for OTHER) and the
result files in another. A hand-off, not a merge: the band's count stays 25 and no token moves; what the verifier could change is the wording -- CA from
"unread-or-null" to "null" on the evidence listed -- if it agrees. No call.

## Campaign step H264 (29 Sept 2026, 10:15 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- positions for the L10 fragment (infrastructure)

Pre-registered (PROMPTS section H264; ruler sheet by `scripts/f61positions_sheets.py --lines L10 --prefix f61sheetB --tag h264`, not seen by the runner; join
rule in `scripts/f61positions_L10_score.py`, committed f843aff6 before the call). One blind Opus call (`scripts/h264_reply.tsv`, verbatim). **The reader lists
13 signs after the last clear word ('si'), fragment_L10.tsv has 13: joined in order, and every shape description matches the fragment's class one for one
(bracket = EBR, a = CA x3, phi = PHI x2, nabla = VBAR_A, qo = SBS x2, V with bars = VBAR_B, oo on a line = INF, 6 = C6 x2).** Its clear words: prendre quelqu'
vne / Je ne seroys pas [p]aresseux si -- the two earlier passes' 'pas paresseux si'. Scale caveat, found after the call: the reader gave x in the half-size
sheet's display pixels rather than the ruler's labels (its three a-shaped signs at 720 / 490 / 920 against H63's sheet-B read of the same marks at 1440 / 985
/ 1820, ratio 2.00 / 2.01 / 1.98), so `scripts/f61_positions_L10.tsv` stores x as twice the reply's value (sheet px, comparable with f61_positions_all.tsv) and
keeps the reply's value in x_reply; the join itself uses only the count and order. Result `scripts/f61positions_L10_result.txt` (`--check` OK). Positions now
cover 95 of f.61's 99 signs (all seven lines with cipher runs; the four remaining tokens are L02/L04's OTHER and read_call_U items). Descriptive: the
reader calls all three L10 CA "a-shaped sign" inside the run, as H63 did. No reading; nothing merged. Vision calls this session: 3 (one per vision step).

## Campaign step H265 (29 Sept 2026, 10:18 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the scribe does not space words inside the cipher (script-only)

`family/h265_span_gaps.py` (rules in the docstring, fixed before running; result `family/h265_span_gaps_result.txt`, `--check` OK). Gaps between consecutive
signs of one segment, from the positions of H253/H257/H264; word boundaries from Tomokiyo's own phrases through the H259 alignment. **Clean boundary gaps
(no null between the two lettered signs): n = 2 -- est|capable 260, au|beau 320, mean 290; within-word gaps n = 34: mean 303, range 210-410; permutation
p95 350.** Pre-stated read-out: **no spacing shown** (n = 2, weak by construction, but the two boundary gaps sit in the middle of the within-word range, not
at its edge). The null-spanned boundaries (trop [CA CA] avancees: 270, 260, 310; beau [C6 CA] pere: 340, 200, 320) are ordinary gaps too. What it says:
the signs run at an even pitch (about 300 sheet px, 100 native) whatever the words, so sign spacing carries no word-boundary information on this leaf --
a word-boundary detector from gaps is ruled out for f.61, and H266 (null-class flanking gaps) cannot detect boundary placement: dropped as a non-test by
this calibration. H267 (positional reads of L02/L04/L06/L09) is dropped too: L06 and L09 carry no cipher signs in any pass, and L02/L04 carry only the
two OTHER tokens each that read_call_U and H238 already describe -- two vision calls for x on four tokens no open test needs. No call.

## Campaign step H268 (29 Sept 2026, 10:21 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- span S5 reads as French only as "me l'entendoit" (script-only)

`family/h268_entendoit.py` (read-out fixed in the docstring before running; result `family/h268_entendoit_result.txt`, `--check` OK). Tomokiyo's S5 on L11 is
"melente-noit" (his dash at L11 8, 4STEM; his n at L11 9, the 4-over-Pi). As French, "me l'ente?noit" needs a word "ente?noit": in the period corpus
tools/data/fr16 (Catherine de Medicis t.1-2, Marguerite de Valois; 933k words) **entendoit 6, entendoient 1 -- and no enten- form at all (entenoit / entenoyt / entenoient / entenois 0).** [Corrected
10:33 UTC by H278: the section first also cited "l entendoit 5"; that count was the substring of "il entendoit" (qu'il / s'il entendoit), so the
object-pronoun phrase "l'entendoit" is NOT attested in fr16; the word-level result above is unchanged.] Pre-stated read-out: **"entendoit is the word"**. What follows, as a lead and not a value: "me l'entendoit"
puts n at L11 8 (inside the F61READ 4STEM a/n cell, grade S, so consistent) and **d at L11 9**, where his letter is n. H85's blind judge resolution of the
known lines already read this span "melentendoit" (NOTES H85, control PASS), and H139 found this dash to be the only one of his that falls on a keyed sign.
So the published letter n at L11 9 (the one source of the a/n cell for f.61's 4-over-Pi, V8: grade M) is contradicted by the French: either his n is a slip
for d, or the phrase is not "entendoit". A rule-4 style conflict row is filed in HYPOTHESES.md with both witnesses (his markup; the lexicon through the
corpus). For the verifier (VERIFY-F61-V9): a candidate correction to a published reading, grade I on L11 9 = d and on L01 12 (the other 4-over-Pi) nothing;
rule 10 wording, no merge, no class change. H269 scores the test key both ways. No call.

## Campaign step H269 (29 Sept 2026, 10:23 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the 4-over-Pi = d test key against both witnesses (script-only)

`family/h269_4overpi_d_testkey.py` (H240's design under key v6's f.61 reading; result `family/h269_4overpi_d_testkey_result.txt`, `--check` OK; 2000 permuted
keys per cell, none reach any target score). **(a) Published markup: v6 53/55; 4-over-Pi = d 52/55 (the S5 n lost); 4-over-Pi = a/n 53/55. (b) S5 as
'melentendoit' (H268's witness): v6 54/56 (the 4STEM n gained; the pooled 4PI a/d/n/q already holds d); 4-over-Pi = d 54/56; 4-over-Pi = a/n 53/56.**
What it says: the two witnesses pull the one token opposite ways by exactly one letter each, as expected; the pooled v6 cell (a/d/n/q) satisfies both
because it is wide. Which witness the f.61 reading follows is the verifier's call (H268's conflict row); the runner's own view, for the record: the
lexicon is a stronger witness than one printed letter of a self-labelled incomplete solution, so L11 9 = d (grade I) and, since both f.61 4-over-Pi
tokens are one sign (V8), L01 12 has the same candidate at a weaker grade. No merge. H270 (a model judge on L11's variants) is dropped: it would only
re-derive that entendoit is a word, which H268 settles from the corpus, and H85's blind judge already read the span that way. No call.

## Campaign step H271 (29 Sept 2026, 10:24 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the L10 lattice admits everything, and so does every control (script-only)

`family/h271_l10_lattice.py` (rules in the docstring, fixed before running; result `family/h271_l10_lattice_result.txt`, `--check` OK). Word list: 16,183 forms
with count >= 3 in fr16. **The real lattice ([l/y][e/r][g/t][e/r][b/o][f/s][h/u][b/o]) admits 364 segmentations into 1-4 list words (l e gros ho, l et ro
sub, ...); the control, 200 cell-order permutations of the same cells, admits at least one in 200/200.** Pre-stated read-out: **descriptive only** -- the
instrument cannot discriminate: a count-3 word list from OCR'd letters holds two-letter fragments (ho, uo, eb, ...) that segment any string. No lead, no
reading; the fragment's letters stay M. H272 (the same search on L01's tail) is dropped as a non-test by this control; a stricter list (longer words,
higher counts) would be a post-hoc retune of the same instrument and is not tried (CLAUDE.md rule 3's repeated-attempt clause). No call.

## Campaign step H273 (29 Sept 2026, 10:26 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- 'ni mesme [LOOPBAR] jalousie': unsettled (script-only)

`family/h273_l07_head.py` (rules fixed before running; result `family/h273_l07_head_result.txt`, `--check` OK). fr16 holds **no 'ni mesme' / 'ny mesme(s)'
at all**, so the pre-stated determiner test has no cases; the word before 'jalousie' (14 cases) is a determiner or possessive 8 times (la 4, leur 1, de 1,
quelque 1, cesle 1) and 'et' 3 times, 'en' 1, 'el' 2 (OCR). Pre-stated read-out: **unsettled**. What it leaves: LOOPBAR at L07 2 may be a null or a
short word; the corpus cannot say. No call. **No runnable row after this step; three written:** H274 (a one-page hand-off for VERIFY-F61-V9 of this
session's findings, script/notes), H275 (a proposal file of the key-note changes the build worker would make after V8 and this session's rows: ZHOOK
glyph link, the 4PI split with L11 9's two witnesses, C6 unread on f.61), H276 (needs: person -- the f.106r looped-hash desk pack of H243, whose ASKS
row the orchestrator holds).

## Campaign step H274 (29 Sept 2026, 10:27 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the page for VERIFY-F61-V9 (notes only)

`family/V9_PAGE.md`: one table of the claims this session put up for audit (CA a null drawn as an a; C6 = e unsupported on f.61; S5 = "me l'entendoit"
with L11 9 = d against the published n; positions on 95 of 99 signs; no word spacing; the null-band table), each with its evidence, controls and files;
the non-tests logged; the meter variants the verifier chooses between (V8's 12/58/2/27 and its a/n variant; the grade-I lead moves no count unless the
verifier admits a one-letter grade-I candidate to the firm band); and what is not claimed. Compiled from NOTES.md and HYPOTHESES.md, adds nothing. No call.

## Campaign step H275 (29 Sept 2026, 10:29 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- key-note proposal for the build worker (notes only)

`family/PROPOSAL_v7_notes.md`: seven numbered row/note changes for a v7 build, each tagged endorsed (V8: the ZHOOK glyph-link note, the 4PI split with
f.188r's r-tail rows moved out, a separate 4OVERPI class for f.61 with L11 9 a/n grade M and L01 12 unread) or pending (V9: the lexicon witness L11 9 = d,
C6 unread on f.61 as an F61READ row, the CA null wording, the 4STEM note), with the reproduction numbers a build must keep. Nothing applied; key v6
unchanged. No call.

## Campaign step H277 (29 Sept 2026, 10:31 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the witness spans file (script-only)

`scripts/tomokiyo_spans_witness.tsv`: the five published spans with S5 as the lexicon witness "melentendoit" (H268), header naming both witnesses and the
HYPOTHESES.md row; `scripts/tomokiyo_spans.tsv` (the published transcript) is untouched. `f61crib.load_spans(path=None)` takes an optional path (default
unchanged), and `family/h269_4overpi_d_testkey.py` now reads witness (b) from the file, asserting it equals the published spans except S5; its result is
byte-identical (`--check` OK), as are h268, h259, h261, h265, h240 and build_key_v6 (`--check` OK each). A build worker or verifier scores either witness
by passing the path. No call.

## Campaign step H278 (29 Sept 2026, 10:33 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the entendoit contexts, and a correction to H268

`family/h278_entendoit_contexts.py` -> `family/h278_entendoit_contexts_result.txt` (`--check` OK): the seven fr16 contexts verbatim (six entendoit, one
entendoient; all in Catherine de Medicis t.1-2): "qu'il entendoit et veoyoit que", "s'il entendoit de tels predicants", "s'il entendoit que je permisse",
"qu'il entendoit preceder l'ambassadeur", "il entendoit augmenter", "ils entendoient qu'ils fortifioient". **Correction to H268:** its phrase count
"l entendoit 5" was the substring of "il entendoit" -- the pronoun-object phrase l'entendoit (as in "me l'entendoit") is not attested in this small corpus
(3 files); the word-level finding (entendoit 7 forms, enten- 0) stands and is the whole of the H268 argument. Carried into the H268 NOTES section,
HYPOTHESES.md's H268 row, CAMPAIGN.md's H268 result cell and family/V9_PAGE.md (rule 10's propagation requirement). The sense in these contexts is
"understood / intended", which fits "me l'entendoit" (understood it of me / from me) only loosely; the verifier weighs that. No call.

## Campaign step H280 (29 Sept 2026, 10:35 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the pronoun construction in the corpora on disk (script-only)

`family/h280_pronoun_phrase.py` (result `family/h280_pronoun_phrase_result.txt`, `--check` OK): a standalone pronoun before an entend- imperfect
("<l|m|le|me|se> entendoit/-oient/-ait/-aient") occurs **once in fr16** (983k words: `lettresdecatheri01cathuoft ... s asseure- ment que le roy le trouverait eucores plus, s il l entendoit. au moyen de quoy je leur es- criptz pr ...`) and **never in fr18, fr19 or fr19v** (595k, 593k, 26k
words); enten- forms 0 everywhere. Existence only, the other corpora being era-mismatched: the construction is attested once in the period letters, so
"me l'entendoit" is possible French but not common in these texts; the word-level H268 result is unaffected. For the verifier's weighing. No call.

## Campaign steps H281 and H282 (29 Sept 2026, 10:36 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the dash-need table; L04's OTHER after "comme" (script-only)

**H281** `family/h281_dash_need.py` -> `family/f61_dash_need.tsv` (result `family/h281_dash_need_result.txt`, `--check` OK): Tomokiyo's 16 dashes in the
five spans -- 12 sit on null-band classes (CA 4, C6 5, CROSS 2, LL 1), 3 on keyed classes (L05 1 LOOPSTEM1 q/s and L05 2 CH e/m, the two signs before
"trop", and L11 8 4STEM a/n), 1 unpaired. French needs a letter at exactly one of them, L11 8 (H268); at every other dash his own phrase is complete
without it. For the verifier: the pooled LOOPSTEM1 q/s and CH e/m (from other leaves) have no letter of his on f.61 either, one token each -- the same
shape as C6 (H261) at n = 1, noted, not filed as conflict rows at that n. **H282** `family/h282_l04_abbrev.py` (result `family/h282_l04_abbrev_result.txt`,
`--check` OK): in fr16 "comme/come" is followed 2,108 times by a pronoun or article and never by a majesty formula (0), although the abbreviation
tokens s a 74, v a 68, v m 65, s m 35 occur elsewhere -- so pass U2's guess that L04's OTHER after "Come" is "S.M." has no corpus support; the token
stays OTHER (wider). No call.

## Campaign steps H283, H284, H285 (29 Sept 2026, 10:39 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the two signs before "trop" are not letters there (script-only)

**H283** `family/h283_l05_head.py` (result `family/h283_l05_head_result.txt`, `--check` OK). Disclosure: no pass on disk lists L04's clear words, so the
runner read images/f61sheetB_L04.jpg once (grade M): "generosite pour bea[u]coup desirer [LOOPBAR] . Il a ... on cognoit Come [OTHER] le ... croys
aussi que les", the line ending "croys aussi que les"; L05 then opens at its left edge with LOOPSTEM1, CH, and "trop avancees" (S3). So the text runs
**"que les [LOOPSTEM1] [CH] trop avancees"**. In fr16, "les W1 W2 trop" occurs twice (choses allaient, pretentions etaient), "les W1 trop" never, and
no two-letter filler from the pooled cells (se, sm, qe, qm) ever stands there. What it says, as a lead for the verifier: at this place the two signs
cannot be the letters their pooled cells give (q/s, e/m; both from other leaves, both dashes in Tomokiyo's markup, H281); French wants a noun and a verb
("choses sont", "affaires estoient"), so they are word codes not in Tomokiyo's table (its three word codes are que, qui, pour) or the runner's read of
"les" is wrong -- H288 puts that read to a blind pass before anything rests on it. No value proposed; nothing merged. [WITHDRAWN 10:47 UTC, runner 10: the premise that L05 opens with the two signs was wrong -- the span sheet f61sheet_L05 keeps native segments 2-4 only (images/regen_f61r_sheets.sh), so H253's 'edge' was the sheet's edge; sheet B's segment 1 shows the line starting 'choses sont a' in clear before the run (H63's reader had said 'after sont'). The text is 'que les choses sont a [LOOPSTEM1] [CH] trop avancees', which is complete French with the signs as nulls; see the correction section below.]
**H284** (notes): family/V9_PAGE.md brought up to H283 (witness spans file, H268 correction, dash-need table, pronoun check, L04 OTHER negative, L05 head).
**H285 dropped:** f.108v's reconciled draft holds one CA (L02 6) and no C6 -- nothing to compare at n = 1.

## Campaign step H286 (29 Sept 2026, 10:41 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- a blind pass reads L04's last word as "les"

Pre-registered (PROMPTS section H286; `scripts/f61positions_L04_score.py`, committed ce3805af before the call, one comment-line fix after it; the runner's
own H283 read disclosed there). One blind Opus call (`scripts/h286_reply.tsv`, verbatim): "generosite pour beaucoup desirer [sign] . Mais on avoit Come
[sign] Je croys aussi que les" -- **the line's last item is the word "les"**, so the pre-stated read-out is **"H283's lead stands"**: f.61 reads "... Je
croys aussi que les [LOOPSTEM1] [CH] trop avancees ...", and the two keyed signs Tomokiyo leaves as dashes cannot be the letters of their pooled cells at
that place (H283). The two sign items (a Venus-like loop-on-stem = LOOPBAR; a W-like double loop = the OTHER) are not joined by the script: read_call_U.tsv lists one L04
sign, the OTHER being pass U2's alone (`scripts/f61positions_L04_result.txt` says so; f61_positions_L04.tsv is empty). Also from this pass: the OTHER after "Come" precedes "Je". Result
`scripts/f61positions_L04_result.txt` (`--check` OK). For the verifier: a word-code lead on two f.61 tokens (LOOPSTEM1 L05 1, CH L05 2), rule 10 wording,
no value, nothing merged. Vision calls this session: 4 (one per vision step). [WITHDRAWN 10:47 UTC, runner 10: the premise that L05 opens with the two signs was wrong -- the span sheet f61sheet_L05 keeps native segments 2-4 only (images/regen_f61r_sheets.sh), so H253's 'edge' was the sheet's edge; sheet B's segment 1 shows the line starting 'choses sont a' in clear before the run (H63's reader had said 'after sont'). The text is 'que les choses sont a [LOOPSTEM1] [CH] trop avancees', which is complete French with the signs as nulls; see the correction section below.]

## Campaign step H287 (29 Sept 2026, 10:41 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the two signs against the table's word codes (notes only)

Tomokiyo's table (keys/key_mayenne_1592.tsv, grade AB transcription of his drawing) has three word codes: **que** "two strokes converging down into a
small closed loop near the bottom (a cursive y whose descender curls into a loop)", **qui** "a vertical stem crossed by two horizontal bars (a double
dagger)", **pour** "a 6-like hook into one long diagonal". The atlas's LOOPSTEM1 ("a single loop on a long stem") and CH ("a mark shaped like a cursive h")
match none of the three, under F61-CAL's caveat that his drawings mislabel this hand -- and none of que/qui/pour can fill "les __ __ trop" anyway, so
the corpus and the shapes agree: if the two signs are word codes, they are codes his table does not hold. Provenance of the pooled cells they carry:
LOOPSTEM1 q 7 / s 3 from f.101r only; CH e 3 (f.101r) and m 3 (f.188r) with u/n strays -- the e/m cell is itself two leaves' different letters merged,
a cross-leaf conflict of the rule-4 kind, which H281's dash on f.61 makes three-way. For the verifier and the build worker (a note in
family/PROPOSAL_v7_notes.md is not added by the runner; the verifier decides). No call.

## Campaign step H288 (29 Sept 2026, 10:43 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- LOOPSTEM1 and CH in the family glosses (script-only)

`family/h288_wordcode_family.py` -> `family/h288_wordcode_family_result.txt` (`--check` OK): per alignment file, the plain-chunk length distribution
(0 / 1 / 2+) for LOOPSTEM1 and CH beside the all-class baseline. read-out: LOOPSTEM1/CH take single letters or nothing everywhere in the family The baseline is the point: whether the aligner ever gives any class a
multi-letter chunk decides whether "do these two take a word" can be asked of these files at all. Whatever the answer, on the glossed leaves the two
classes were aligned as letters (q/s on f.101r; e on f.101r and m on f.188r for CH), and on f.61 they stand where letters cannot (H283/H286): a
leaf-level difference of the C6 kind (H261), for the verifier. Also corrected in this commit: H286's NOTES/CAMPAIGN wording said L04's two sign items
were joined to read_call_U; they are not (read_call_U lists one L04 sign, the OTHER is pass U2's alone). No call.

## Campaign steps H289, H290, H291 (29 Sept 2026, 10:45 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the CH cell row; fillers of "les __ __ trop"; the family tokens in context (script/notes)

**H289:** HYPOTHESES.md row "campaign H289": the pooled CH e/m is two leaves' different gloss letters merged (f.101r e 3, f.188r m 3, strays each side),
with Tomokiyo's dash on f.61 as a third witness; recorded, not resolved. **H290** `family/h290_wordcode_candidates.py` (result `..._result.txt`, `--check`
OK): "les W1 W2 trop" is rare in both corpora -- fr16 2 (choses allaient, pretentions etaient), fr18 3 (cherchoit avec, pafiages etoient, batteries
etoient), and the three-word fillers are noise; so the construction is noun + imperfect verb ("choses estoient / sont" is the shape), but no single
candidate pair is frequent enough to name as the value of the two codes; descriptive. **H291** `family/h291_family_context.py` (result `..._result.txt`,
`--check` OK): on f.101r and f.188r, 25 of the 30 aligned LOOPSTEM1/CH tokens carry a letter of their own with lettered gloss neighbours on both sides
(e.g. f.101r L45 "- e [q] u e", f.188r L21 "l e [m] e n") -- on those leaves they are letters inside words. With H288 (never a word in the family) and
H283/H286 (a word slot on f.61), the two f.61 tokens are a leaf-level difference: either f.61's signs are a different glyph from the family's letter
signs (H293 tests that by blind sort, n = 1 each, flagged) or the same glyph is used differently on f.61. No value; for the verifier. No call. [WITHDRAWN 10:47 UTC, runner 10: the premise that L05 opens with the two signs was wrong -- the span sheet f61sheet_L05 keeps native segments 2-4 only (images/regen_f61r_sheets.sh), so H253's 'edge' was the sheet's edge; sheet B's segment 1 shows the line starting 'choses sont a' in clear before the run (H63's reader had said 'after sont'). The text is 'que les choses sont a [LOOPSTEM1] [CH] trop avancees', which is complete French with the signs as nulls; see the correction section below.]

## Correction (29 Sept 2026, 10:47 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- the word-code lead of H283-H291 is withdrawn

The runner's error: H283 read L04's tail ("croys aussi que les", confirmed blind by H286) and took L05's run to open the next line because H253's
positions mark L05 1 as prev=edge. That edge is the SHEET's: `images/regen_f61r_sheets.sh` keeps only native segments 2-4 of L05 on the span sheet, and
sheet B's first segment (images/f61sheetB_L05.jpg, viewed once by the runner for this check, grade M) shows the line beginning **"choses sont a"** in
clear before the run -- H63's reader had already recorded a CA "at the edge: after 'sont' and before the run" (L05 s1 1680). So the text is
**"Je croys aussi que les choses sont a [LOOPSTEM1] [CH] trop avancees"**: the noun and the verb are in clear, "les choses sont trop avancees" is complete
French, and the two keyed signs need carry nothing -- the null reading, which is what Tomokiyo's three dashes before "trop" say (the third dash is the
edge "a" that pass A did not code, H63; H294 answered). Withdrawn: "French wants a noun and a verb there" (H283, H286, the ROOM lines of 10:4x-10:5x,
family/V9_PAGE.md's word-code section, HYPOTHESES.md H289's third witness, H290's candidate list as a lead). Still standing: H281's dash table, H288/H291's
finding that the two classes are letters inside words on the family leaves (so on f.61 they would be nulls or unread, a leaf-level difference of the
C6 kind, not word codes), H289's CH e/m conflict (witnesses 1-2). H293 (glyph sort) dropped with its motivation. Lesson for the retrospective: a
positional read's "edge" on a span sheet is the sheet edge, and any inference about what precedes a run must read sheet B's first segment (or the
regen script's keep map) first.

## Campaign steps H295 and H296 (29 Sept 2026, 10:49 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- "sont trop" needs no filler; a sheet-edge guard (script-only)

**H295** `family/h295_sont_trop.py` (result `family/h295_sont_trop_result.txt`, `--check` OK): in fr16, "sont trop" bare 1, "sont W trop" 2 (en, pas), no
two-word filler; "est trop" bare 5, "est pas trop" 2, "est que trop" 1. Small counts, but nothing in the grammar wants a word between "sont" and
"trop": the null reading of the edge a + LOOPSTEM1 + CH on L05 (Tomokiyo's three dashes) is unforced either way, and no adverb is suggested. Descriptive.
**H296** `scripts/f61_sheet_edges.py` -> `scripts/f61_sheet_edges.tsv` (`--check` OK): from the regen script's keep map, every span-sheet segment with its
native segment and whether it is the line's first or last; and every "edge" row of the positions files classed as a LINE edge or a SHEET edge only --
L05 1 (LOOPSTEM1) and L03 15, L08 14 are sheet edges, not the line's; L11 1, L08 1 are line starts; L01 12, L07 11 line ends (the per-line native
segment count is assumed 5 because the f61s_L*_s*.jpg cuts are not on disk, flagged in the file). A guard for later runners against the H283 error.
No call.

## Campaign step H297 (29 Sept 2026, 10:51 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- a blind pass reads L05's start "choses sont a" before the run

Pre-registered (PROMPTS section H297; `scripts/f61positions_L05B_score.py`, committed f37cd677 before the call; the runner's own sheet-B look disclosed).
One blind Opus call (`scripts/h297_reply.tsv`, verbatim): **"choses sont a" precede the first sign** -- read-outs (a) the line begins with clear text
before the run, (b) the runner's read stands (last word "sont"); the Correction's premise now has a blind witness beside H63's "after sont". The reader
lists 17 signs against read_call_A's 18, so the join rule does not fire: **it reads the CH sign as the clear letter "h"** ("L05 1 2140 word h", between
the LOOPSTEM1 loop and the T-shaped VBAR_A), exactly as readers take CA for the clear "a" (H253/H257/H264) -- a second null-band class whose letterform
is a clear letter, to be tested as H256 was (H298). The rest of its list matches pass A sign for sign (phi, qo, 4-over-bar, a, a, 43, -oo-, 43, b/6, 43,
4, phi, ll, phi, barred x) and it closes the line "Et que si nous mesmes ey", the clear tail. Result `scripts/f61positions_L05B_result.txt` (`--check`
OK). No value, nothing merged. Vision calls this session: 5 (one per vision step).

## Campaign steps H299 and H300 (29 Sept 2026, 10:52 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- L05 joined from the true line start; nulls shaped as letters (script/notes)

**H299** `scripts/f61positions_L05B_join.py` (rule in the docstring; result `scripts/f61positions_L05B_join_result.txt`, `--check` OK): signs after taking the bare 'h' as CH: 18 vs read_call_A 18; edge a before the run: yes; joined from the true line start; classes in order: LOOPSTEM1 CH VBAR_A PHI SBS 4TRI CA CA C43 INF C43 C6 C43 4TRI PHI LL PHI VBAR_B. The file
`scripts/f61_positions_L05B.tsv` now holds L05 from the true start (pos 0 = H63's uncoded edge a, then pass A's 18 signs) at sheet-B coordinates (the
reader's scale). **H300** `family/f61_nulls_as_letters.tsv`: of the null-band and dash classes, CA (a), CH (h), C6 (6), LL (ll) and, partly, LOOPSTEM1
(q-like) are shaped like clear letters or digits in the atlas and in the blind readers' own words; CROSS, LOOPBAR, the 4-over-Pi and OTHER are not.
For the verifier's null-band wording and for H298's design (the CH letterform test). No call.

## Campaign step H298 (29 Sept 2026, 10:57 UTC by the clock, runner 10 session_0148wt8Aokh6aZEdJsXzYiZX) -- f.61's CH has the clear h's letterform (n = 1)

Pre-registered (PROMPTS section H298; `family/h298_ch_text.py`, key `family/h298_items.tsv`, committed 75877ea1 before the call; gates adapted to n:
all text h's in one group, no non-h letter in it). Disclosure: the runner placed the six TEXT tiles on two ruler sheets of those tiles only; the CH,
PHI and C43 crops and the test sheet were not seen (sheet B L05 had been viewed whole for the Correction). 11 tiles: CH 1 (sheet B L05 x 2140,
centroid-recentred), clear h 3 (choses x2, mehi), clear non-h 3 (l of les, C of Come, l of le), PHI 2, C43 2. One Opus free sort
(`family/passes/h298_sort.tsv`); result `family/h298_ca_text_result.txt` (`--check` OK): groups **A** "a cursive h, tall looped ascender, arched shoulder
ending in a descending tail", **B** "43", **C** "phi-8", **D** "a single tall looped ascender (an l-shape)". **Text h: A 3/3 (gate 1). Non-h: D 1, unclear 2
(gate 2: 0 in A). CH: A 1/1. PHI/C43: 0 in A.** Pre-stated read-out: **"CH has the clear h's letterform"**, at n = 1 on the CH side (flagged). With H281
(Tomokiyo's dash), H288/H291 (a letter inside words on the family leaves), H289 (the pooled e/m is two leaves' letters) and H297 (a blind reader lists
it as the word "h"): on f.61 the CH sign is an h-shaped mark that reads as nothing, the CA pattern at n = 1 -- a second null drawn as a clear letter,
for the verifier's null-band wording; no cell changes. Vision calls this session: 6 (one per vision step).

## Campaign step H301 (29 Sept 2026, 11:20 UTC by the clock, runner 11 session_01RNzUvRTqBTAw7BukhKyKBU) -- H298 carried into the null tables, the V9 page and the v7 proposal (notes/script only)

Runner 11 (this session) replaces runner 10 (stopped 10:58 on its own context count). Inherited: key v7 (F61-FAMILY-11, 10:17), VERIFY-F61-V9 (AUDIT.md,
10:33: CA endorsed in part, C6 conflict endorsed with the word test, null band endorsed, meter 12 / 59 / 2 / 26 [null 17 + unread 9]), F61-FAMILY-12's
merge of V9's notes (11:15: KEY.md "CA on f.61 (V9)", the null-band class note, HYPOTHESES.md's C6 row) -- its done line was in ROOM before this step
touched `family/f61_null_band.py`. Four files, no call, no value, no cell change:
- `family/f61_nulls_as_letters.tsv`: the CH row's letterform_test cell now carries H298's result (1/1 with the 3 clear h's, PHI/C43 0/4, PASS as
  pre-stated at n = 1, flagged) and the header says the test ran.
- `family/f61_null_band.py` -> `.tsv` (`--check` OK): one `note` row for CH (L05 2, keyed e/m, span S3, Tomokiyo's character "-" from the same
  alignment as the band rows) with the evidence and files; the 25 unread-or-null + 4 wider rows V9 recounted are unchanged (result line: 25, 4, 15 in a
  span, note rows 1). CH is not in the band because the meter counts it two-way (keyed); the note is for the next verifier.
- `family/V9_PAGE.md`: a status line (V9 ruled, v7 built, FAMILY-12 merged) above runner 10's header, and a section "Added after the withdrawal
  (H295-H300)" with H297/H298/H299/H300 and the meter variant a verifier would produce by moving CH to null (12 / 58 / 2 / 27 [null 18 + unread 9];
  not applied, CH stays keyed).
- `family/PROPOSAL_v7_notes.md`: row 8, a pending F61READ row `CH - 0 fr.4715 f.61r` beside the C6 one (item 4), with its evidence and the meter effect
  if applied; and a status paragraph recording which of items 1-7 landed in v7 or in FAMILY-12's notes (1-3 v7; 5 as a KEY.md section and class note;
  4 into HYPOTHESES.md's row, no key row; 3b, 7, 8 pending).
Nothing here is a reading; "null drawn as h" is at n = 1 and stands for the verifier only. Vision calls this session: 0.


## Campaign step H302 (29 Sept 2026, 12:37 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- LL against clear ll/Il: CONTROL FAIL; LL sorts with L02's disputed opening mark

Pre-registered (PROMPTS section H302; `family/h302_ll_text.py`, key `family/h302_items.tsv`, committed ea8c6846 before the call). Disclosure in PROMPTS:
the runner viewed sheets B L02, L04, L07 whole (L02 shows the DISPUTED mark) and a placement sheet of the six TEXT tiles; the LL, PHI and C43 crops and the
test sheet were not seen. 12 tiles: LL 1 (sheet B L05 seg 3 x 1330, centroid-recentred), clear ll-type 3 (ella L07; Il of 'Il seroit' L02; Il of 'Il a'
L04), clear single l 3 (les, les, le), PHI 2, C43 2, and one DISPUTED tile in no gate (L02's opening mark: read_call_U pass 1 LL, pass 2 'Il'). One Opus
free sort (`family/passes/h302_sort.tsv`, verbatim); result `family/h302_ll_text_result.txt` (`--check` OK):
- Groups: **A** phi-8 (PHI 2); **B** 4-with-3 (C43 2); **C** "L-shaped, tall looped ascender into a flat foot" (single l 3/3); **D** "two tall f/long-s-like
  stems side by side, the left crossed or footed by a short leftward stroke" (**LL and the DISPUTED L02 mark**); **E** "a long diagonal from lower left
  ending in a heavy blob meeting upright stems (M/H-like)" (the two clear 'Il'); the ella tile 'unclear'.
- **Gate 1: CONTROL FAIL** (text ll-type 2 of 3 in one group; the ella tile unclear) -- nothing scored, no read-out on LL, as pre-stated.
- Why, from the reader's own criteria: the design pooled two letterforms. The scribe's capital I of 'Il' opens with a long diagonal lead-in stroke and a
  blob (group E), which a doubled l does not have; 'ella' is joined at both sides and its ll did not stand out at the tile centre. f.61 holds only one
  clear doubled l (ella; 'aidilla' on the L07 span sheet is the same word), so a ll-only text control of n >= 3 cannot be cut from this leaf.
- Descriptive only (in no gate, stated before the call as descriptive): the LL tile and L02's opening mark were put in one group, apart from the clear
  'Il's, the single l's and the cipher controls. By letterform the L02 mark agrees with pass 1 (LL), not pass 2 ('Il') -- a lead at n = 1 + 1 for a
  verifier, not a recount: the null band keeps its V9-endorsed counts.
No reading, no cell change. Vision calls this session: 1.

## Campaign step H304 (29 Sept 2026, 12:39 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- L02's opening mark and LL against clear I and l: CONTROL FAIL again; same descriptive pairing

Pre-registered (PROMPTS section H304; `family/h304_ll_pair.py`, key `family/h304_items.tsv`, committed acc38774 before the call; a fresh reader, not
H302's). 12 tiles: LL 1, L02 opening mark 1 (both centroid-recentred), clear capital I 3 centred on the I (Il seroit L02, Il a L04, Impor L02), single l
3, PHI 2, C43 2. Result `family/h304_ll_pair_result.txt` (`--check` OK; reply verbatim in `family/passes/h304_sort.tsv`):
- Groups: **A** 4-with-3 (C43 2); **B** phi-8 (PHI 2); **C** "a single stroke with a hooked or barred head curving into a long diagonal descender (cursive
  7, T or J)" (clear I 2: Impor, Il seroit); **D** "a tall stem with a blob or loop at the top bending into a flat foot (cursive L)" (single l 3/3);
  **E** "two long-s stems side by side, joined by a crossbar (a cursive ff)" (**LL and the L02 mark, nothing else**); the I of 'Il a' (L04) unclear.
- **Gate: CONTROL FAIL** (clear I 2 of 3 in one group; the L04 I, the blob-headed one H302's reader also set with the other 'Il', came back unclear) --
  nothing scored, as pre-stated.
- Descriptive, in no gate: **two independent readers (H302, H304) each put the L02 opening mark and f.61's LL in a group of their own**, described both
  times as two tall long-s-like stems side by side (H302 "the left crossed or footed", H304 "joined by a crossbar"), apart from every clear I, every single
  l and the cipher controls. That agrees with read_call_U pass 1 (LL) against pass 2 ('Il') -- a lead at n = 2 for the verifier's null-band recount, not a
  runner's recount; the band keeps V9's counts.
Rule 3 (26 Sept 2026 lesson): two passes of the same letterform sort, the second changing only the control set, both miss their own gate on one tile; a
third pass on the same leaf's letters is not run -- the next evidence needs different material (H305: clear ll/I from the family leaves in the same hand)
or a verifier's judgement on the two descriptive agreements. Vision calls this session: 2.

## Campaign step H305 (29 Sept 2026, 12:41 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- no ll-only control in f.61's hand on disk (script/grep only)

`family/h305_ll_census.tsv`: clear doubled-l and capital-I letters by hand. In the f.61 hand (Mayenne's secretary: f.61, f.108r, f.108v) the files hold
**one** clear doubled l (ella, f.61 L07) and three clear capital I's (the H304 tiles); f.108v's 82 PLAIN items in the cipher rows (ce tam, fauldra, qu,
et, tant, aul Rigny ...) hold no ll and no capital I. Every other source with ll words (f.184r's separate decipherment, about 20; the f.101r/f.188r/
f.108 glosses) is de Diou's hand, the wrong hand for a letterform control of f.61's scribe; f.175r/f.177r's clear passes are not hand-compared on file
and carry no x. So an ll-only control of n >= 3 in this hand cannot be cut from material on disk: H302/H304's letterform question on LL stays open,
held on new material (a clear letter in the secretary's hand), not on another sort of the same tiles. By the way: a second LL token in this hand is on
file, f.108v L06 29 (scripts/pass108gB_classes.tsv, pass B only, confidence l). No call, no value, no count change.

## Campaign step H306 (29 Sept 2026, 12:42 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- H302/H304/H305 carried into the null tables and the V9 page (notes/script only)

`family/f61_null_band.py` -> `.tsv` (`--check` OK): one fixed `note` row `L02 0 LL?` for L02's opening mark (read_call_U pass 1 LL / pass 2 'Il';
not in the decode file, which follows pass 2), with H302/H304's descriptive pairing and both control fails; band counts unchanged (25 unread-or-null + 4
wider, 15 in a span), note rows 2. `family/f61_nulls_as_letters.tsv`: the LL row's letterform_test cell now records the two runs and H305.
`family/V9_PAGE.md`: a section "Added by runner 12 (H302-H306)". No call, no value, no count change.

## Campaign step H307 (29 Sept 2026, 12:44 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- f.175r/f.177r are not in f.61's hand on the record (notes only)

From the folder's own record: f.175r and f.177r are clear pages beside Desportes's cipher letter of 22 July 1593 to the pope (f.176r; H169, H175 --
f.177r is the separate-sheet decipherment of f.176r, gate PASS; f.175r the decipherment of another 22 July letter, H170). H169 already describes fol.
177-178 as "clear pages in another hand (not identified)", and the letters are Desportes's, in Paris, not the Duke of Mayenne's chancery. So neither
leaf is recorded as the hand of f.61's scribe (Mayenne's secretary: f.61, f.108r, f.108v), and a hand comparison by vision would start from a leaf with
no link to that scribe: the vision half of the row is not run. The LL letterform question (H302/H304) waits on a clear page by that secretary; H308
names where to look. No call, no value.

## Campaign step H308 (29 Sept 2026, 12:45 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- a clear page from Mayenne's chancery on disk: fr.3983 f.211r (no request)

No Gallica request was needed: `family/images/3983_f211r_ref1600.jpg` (Mayenne to de Diou, camp of Han, 1 April 1593; MANIFEST canvas 362) is a full
page of clear French with one short glossed cipher run on line 2 (H95/H96, ASKS row 93). The runner read it at 1600 px (grade M, words only) for
doubled l's and capital I's: **laquelle (line 1), ville (lines 4 and 9), elle and meilleure (line 10), Tellement (line 22), Monsieur daumalle (line 21),
seullement (line 26); 'Ils' (line 14), 'Il se' (line 24)** -- about eight clear doubled l's and two or more capital I's, against f.61's one 'ella'.
Caveat on the hand, not settled here: H95 calls the leaf "Mayenne's secretary's hand" from its sender and date; no side-by-side comparison with f.61's
scribe is on file, and at this scale the script looks smaller and faster than f.61's. So f.211r is the candidate source for an ll-only control (H309),
and the hand match is part of what that step must show (its hand-check tiles), not an assumption. No call, no value.

## Campaign step H309 (29 Sept 2026, 12:51 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- LL against doubled l's from f.211r: NON-TEST; the free sort retired for LL

Pre-registered (PROMPTS section H309; `family/h309_ll_211r.py`, key `family/h309_items.tsv`, committed 1133814f before the call). f.211r native fetched
once (family/requests.log, 12:46:17Z, 200, sha1 80c6c389 = MANIFEST; scratch only; 1 Gallica request this session). 16 tiles: LL 1, L02 opening mark 1
(descriptive), doubled l 5 (f.211r ville, elle, daumalle, Tellement; f.61 ella), single l 5 (f.211r la, le; f.61 les, les, le), PHI 2, C43 2. One fresh
Opus free sort (`family/passes/h309_sort.tsv`); result `family/h309_ll_text_result.txt` (`--check` OK):
- Groups: **A** "a single tall ascender stroke ... the cursive letter l, or one l of a doubled ll" (12 tiles: every doubled l, every single l, LL and the
  L02 mark); **B** 43 (C43 2); **C** phi-8 (PHI 2).
- **Gate 2: NON-TEST** (single l 5/5 in the doubled l's group): the reader sorted by "a tall ascender", not by the doubling -- nothing scored, as
  pre-stated. The doubled l's did not split by leaf (5/5 together), so the cross-leaf worry in PROMPTS did not arise.
- Descriptive only: LL and the L02 mark fall with the l family, apart from the cipher controls.
**Rule 3(c):** three attempts at the same instrument (a blind free letterform sort) on the same hypothesis, each changing only the control set (H302
ll/Il, H304 I and l, H309 doubled vs single l from a second leaf), none passing its own gate. Logged in HYPOTHESES.md as **untested-by-this-tool**, not
refuted; no fourth free sort. A different instrument would be a forced choice per tile ("one ascender or two") with a known-answer control -- H310.
The null band's LL row and the L02 note row are unchanged. Vision calls this session: 3.

## Campaign step H310 (29 Sept 2026, 12:53 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- forced choice: known answers 14/14; LL has two ascender strokes (n = 1)

Pre-registered (PROMPTS section H310; `family/h310_ll_forced.py`, committed 395ad937 before the call): H309's sheet and key (16 tiles), a fresh blind
Opus reader, per tile ONE / TWO / NEITHER / unclear. Reply verbatim `family/passes/h310_forced.tsv`; result `family/h310_ll_forced_result.txt` (`--check` OK):
- **Known answers: doubled l TWO 5/5 (f.211r 4, f.61 ella 1), single l ONE 5/5, PHI/C43 NEITHER 4/4 -- gate passes.**
- **LL = TWO** (read-out as pre-stated: "LL has two ascender strokes, like the clear ll"); **L02 opening mark = TWO**. n = 1 + 1, flagged.
What it says, and what it does not: where the free sort could not (H302/H304/H309, retired), a forced choice separates doubled from single l on known
answers, and puts f.61's LL with the doubled l's -- consistent with the atlas's "a mark shaped like ll" and with the CA/CH pattern (a null drawn as a
clear letter), now tested by one instrument with a passing known-answer gate. It cannot tell a doubled l from a clear 'Il' (no 'Il' tile was in this
set; a capital I plus l also has two tall strokes), so the L02 mark's TWO does not decide pass 1 (LL) against pass 2 ('Il'). No cell changes; LL stays
unread-or-null in the band (1 token); for the verifier's null-band wording only. Vision calls this session: 4.

## Campaign step H311 (29 Sept 2026, 12:55 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- Il vs ll forced choice: gate passes 11/11, both targets unclear

Pre-registered (PROMPTS section H311; `family/h311_il_forced.py`, key `family/h311_items.tsv`, committed f1b3593c before the call); a fresh blind Opus
reader; reply verbatim `family/passes/h311_forced.tsv`; result `family/h311_il_forced_result.txt` (`--check` OK):
- **Known answers 7/7** (f.61's two clear 'Il' LEADIN 2/2; doubled l UPRIGHT 5/5, four from f.211r and f.61's ella) and **PHI/C43 NEITHER 4/4 -- gate passes.**
- **L02 opening mark: unclear. LL: unclear.** As pre-stated, no read-out.
So the instrument separates a capital I's lead-in from an l's upright on clear letters, but the reader would not commit on either sign: pass 1 (LL)
against pass 2 ('Il') for L02's opening mark stays undecided by the runner's instruments, and is left to the verifier's own eye on the two tiles
(H302's sheet, family/h311_items.tsv positions). Not re-run with another wording (rule 3's one-knob lesson). No cell or count change. Vision calls
this session: 5.

## Campaign step H303 (29 Sept 2026, 12:56 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- the digit-shaped C6 null, one paragraph (notes only)

Written into `family/V9_PAGE.md` (the verifier's page), the paragraph "C6, the digit-shaped null (H303)": the markup evidence (Tomokiyo's dash at all
five in-span C6, H261; French complete without it, H281), the pooled C6 = e gaining nothing on f.61 and no glyph link to the glossed C6 (H237) -- and
why no letterform test is possible here (no digits in f.61's clear text; f.211r, the same-hand clear page, shows no numerals at 1600 px). A real test
would take clear numerals by Mayenne's secretary as known answers in H310's forced-choice format. C43 is left out (keyed a/n, reads letters in the
spans). No call, no value, no count change.

## Campaign step H312 (29 Sept 2026, 12:58 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- f.108v's "second LL" is not supported; H305's note corrected (script-only)

H305 noted a second LL token in f.61's hand at f.108v L06 29 (`scripts/pass108gB_classes.tsv`). Script-first, before any call: that code comes from the
H34 "g" cut, **a 720-px region whose L06 is cut through its lower half** (NOTES H34: "L06 is cut through its lower half by the region's bottom edge"),
every L06 sign at confidence l, "top only". **Pass A codes the same place OTHER, "two stems, top only"** (`scripts/pass108gA_classes.tsv` L06 31, s4 x
302, against pass B's s4 x 360). **The H59 native-resolution reconciled draft of f.108v** (`family/passes/f108v3z_draft_reconciled.tsv`, 304 signs,
both passes and the reconciler reading from `scripts/f61_atlas.tsv`, whose class list includes LL) **codes no LL anywhere on the leaf.** So there is no
supported second LL token in this hand: one low-confidence code by one pass on a half-cut low-resolution band. The vision half of the row (H310's forced
choice on that tile) is not run: a tile with the lower half of the sign missing would test nothing. Correction carried into
`family/h305_ll_census.tsv`'s last line. LL on f.61 stays n = 1. No call, no value.

## Campaign step H313 (29 Sept 2026, 13:00 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- eye pack for L02's opening mark (script-only)

`images/person_pack_L02/` (`L02_mark_pack.jpg`, 109 KB, and `README.md`), cut by `family/h313_eye_pack.py` at H311's crop geometry: the two targets
(f.61's LL and L02's opening mark), f.61's clear 'Il' x2 and 'ella', and two doubled l's from fr.3983 f.211r, labelled. The README states the one
question (pass 1 LL vs pass 2 'Il') and the five instruments' results (H302/H304/H309/H310/H311), none of which decides it. The runner viewed the
finished pack to check the crops; no judgement of the runner's is recorded as a result. For the verifier lane (ROOM post). No call.

## Campaign step H314 (29 Sept 2026, 13:01 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- no clear 6 in the secretary's hand on record; thumbnail sweep not run (script/notes)

Script-first over NOTES.md and family/MANIFEST.tsv for dates and figures on the family's leaves: the dated lines on record are "4 de mars 1593"
(f.106r heading), "Du camp de Soissons, ce IIIIe mars 1593" (Roman), "De Soissons ce dernier jour de fevrier 1593" (f.108v, in words), "7 de Nove[mbre]
1592" (f.124r, de Diou's side), "5 d'avril 1592" and "13 may 1593" (other senders), "22 de Juillet 1593" (Desportes); f.211r, the same-hand clear page,
writes its numbers as words ("six Jours", "huit Jours", "trois ou quatre Jours", H308's reading at 1600 px). Years 1592/1593 hold no 6, and no dated line
from Mayenne's chancery on record has a 6 in its day. So the prior that a thumbnail sweep (the row's second half) finds a clear digit 6 in this hand is
low; it is not run (0 Gallica requests), and the C6 argument stays on the markup and the missing glyph link (H303's paragraph). A later route, if one
is wanted: a leaf from this chancery with a sum or a count in figures, which none of the folder's leaf descriptions mentions. No call, no value.

## Campaign step H315 (29 Sept 2026, 13:04 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- fr.3983 f.211r's cipher run: two blind sign passes agree 16/18 (gate PASS)

Pre-registered (PROMPTS section H315; `family/h315_211r_signs.py`, committed 3ebc851f before the calls). ASKS 93's desk-pack strip cut into two
1700-px segments (`family/sheets/f211r_run_s1/s2.jpg`, overlap 220 px, each sign listed once by a fixed x rule); two independent blind Opus passes with
the atlas codes (verbatim `family/passes/f211r_s{1,2}_signs{A,B}.tsv`), joined to sheet x and reconciled by `tools/reconcile_passes.py` (nw;
`family/passes/f211r_rec/`). Result `family/h315_211r_signs_result.txt` (`--check` OK):
- Both passes list **18 signs**; **16 of 18 columns identical (0.89), gate 0.80: PASS.** The two disagreements are EBR_A/EBR_B (col 13) and
  VBAR_A/EBR_B (col 17).
- Sequence: VBAR_A SBS HASH4 SBS EBR_B DBL 4STEM SBS OTHER OTHER DBL DBL [EBR_A|EBR_B] EBR_B DBL DBL [VBAR_A|EBR_B] VBAR_A. Most agreed columns are
  at the passes' own m/l grade (agreed-H 1, agreed-uncertain 15).
- Every class but the two OTHER is a class of f.61's hand (the atlas), consistent with H95's "same secretary". DBL (two loops on a stem, one above the
  other) takes 6 of 18 signs.
This is the sign half of the held-out check; the gloss half is H316 (or ASKS 93), and H317 scores the two against key v7. No reading. Vision calls
this session: 7 (two here).

## Campaign step H316 (29 Sept 2026, 13:07 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- f.211r's gloss, two blind reads: gate FAIL (as expected); four word slots agreed

Pre-registered (PROMPTS section H316; `family/h316_211r_gloss.py`, committed 2aeb39be before the calls). Two independent blind Opus reads of the small
words above f.211r's cipher run only (verbatim `family/passes/f211r_s{1,2}_gloss{A,B}.tsv`); result `family/h316_211r_gloss_result.txt` (`--check` OK):
- A: forble[?] (sheet x 475-975) | comm[?] (1320-1700) | elle (2105-2350) | v[?]l (2590-2800).
- B: forbe[?]z (470-975) | comm[?] (1320-1700) | elle (2105-2340) | v[?]l (2595-2800).
- Exact agreements 3 (comm[?], elle, v[?]l), of which only **elle** is a complete word in fr16 -> **gate FAIL** (fewer than 3), as pre-stated; the gloss
  stays unread and ASKS 93 stays open for a person's reading.
Descriptive only: both readers put four gloss words at the same four x spans (to within 10 px), agree on 'elle' (h/m) and on the letters they could
read in the other three ('forb-', 'comm-', 'v-l'). That is the frame a person's reading fills; it is not a reading. H317 (the held-out cell check)
now waits on ASKS 93 (needs: person). Vision calls this session: 9.

## Campaign steps H320 and H318 (29 Sept 2026, 13:09 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- f.211r's run under key v7: 16/18 signs keyed; partial held-out check, no signal at this N (script-only)

`family/h318_211r_partial.py` (design and read-outs in its docstring, written before running; result `family/h318_211r_partial_result.txt`, `--check` OK).
- **H320 (coverage):** of the run's 18 signs (H315), 16 fall in classes key v7 gives a cell (VBAR_A g/t x3, SBS b/o x3, HASH4 d/q, EBR i/l or a/l/s x3,
  DBL e/r/u x5, 4STEM a/c/e/n); the two OTHER have none. (Stated assumption: atlas EBR_A read with v7's form A, EBR_B with form B.) So a person's gloss
  reading (ASKS 93) would test DBL, SBS, VBAR_A and EBR most -- none of them fitted on this leaf.
- **H318 (partial check):** the gloss letters both H316 readers agreed (f o r b / c o m m / e l l e / u l; grade M) matched one-to-one, order-free, to
  the signs under each slot's x span: forb- 1/4 over 3 signs, comm- 1/4 over 3, elle 2/4 over 2, v-l 0/2 over 2 -- **real 4 of 14**, against 1000 keys
  with v7's cells permuted across the classes: mean 2.71, **p95 5**, max 6, >= real 226/1000 -> **"no signal at this N"**, as pre-stated.
What it says: at 14 letters of M-grade gloss, placed by x alone, the check cannot tell key v7 from a shuffled key; the slots also hold fewer signs
(2-3) than letters (4), so the gloss-to-sign x placement on this run is looser than one letter per sign -- a reason the proper check (H317) needs a
person's full reading with sign spans (ASKS 93's template asks for them). Not a negative on the key; no reading.

## Campaign step H319 (29 Sept 2026, 13:09 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- the ASKS 93 desk pack gets H315/H316's frame (notes only)

`images/person_pack_211r/README.md` gains a section: the 18 signs at their ruler ticks with the two passes' atlas codes, and the four gloss slots both
model readers placed (forb-, comm-, elle, v?l with tick spans), stated as a frame to confirm or correct, not a reading; ASKS 93 is unchanged (open).

## Campaign step H321 (29 Sept 2026, 13:10 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- EBR forms: H320's mapping confirmed (script-only)

`family/build_key_v5.py` (load_key_v5, carried into v6/v7): the key rows carry the atlas classes EBR_A and EBR_B; `ebr='B'` takes EBR_B's cell (f.176r
brackets form B, H180 11/11: l, y -> i/l) for f.61's unsplit EBR, and `ebr='A'` takes EBR_A plus the unsplit EBR rows of the form-A brackets (f.108r).
The atlas defines EBR_A as the hairline-diagonal bracket (H22 group A) and EBR_B as the plain squared C/gamma (group B). So "form A" = atlas EBR_A and
"form B" = atlas EBR_B, as H320/H318 assumed; no rerun. Noted for H323: v5's endorsement table pools the f.176r reader code DBL into SBS ("reader code
DBL on f.176r is v4's SBS glyph") and lists DBL among the classes whose rows must equal v4's -- so which glyph v7's DBL e/r/u cell describes is H323's
question. No call.

## Campaign step H323 (29 Sept 2026, 13:11 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- DBL census: v7's e/r/u cell is f.101r's alone; in the secretary's hand readers code SBS (script-only)

- **Key v7's DBL rows** (`family/key_period_v7.tsv`): all from **fr.3982 f.101r** (the Bishop of Lisieux's letter from Rome, another hand): e 10, r 6,
  u 6, then t 2, i/n/p/q/s 1 each. No other leaf contributes to DBL.
- **f.176r (Desportes):** the readers' code DBL there was ruled to be v4's SBS glyph and pooled into SBS b/o (VERIFY-F61-V5; v7 rows 'f.176r code DBL').
- **Mayenne's secretary's hand:** f.61 (scripts/f61_positions_all.tsv) DBL 0, SBS 5; f.108v native H59 draft DBL 0, SBS 13 (the low-resolution H34 'g'
  alignment has DBL 29, the same kind of code drift f.176r showed); **f.211r's run (H315) DBL 5, SBS 3**.
What it means for the held-out check: of f.211r's 16 keyed signs, the five DBL would be scored with a cell fitted on another hand's leaf, while on two
leaves (f.176r, and by the native draft f.108v) the readers' DBL/SBS split tracks the reading resolution, not a second glyph. So before H317 scores
DBL as e/r/u, the question "is f.211r's DBL the f.101r glyph or the SBS glyph drawn taller" needs its own blind answer (a forced choice with f.101r DBL
and f.61/f.108v SBS tiles as known answers, H310's format) -- written as H324. H318's partial check used e/r/u for them; its "no signal" stands either
way (SBS b/o would score no letter of forb/comm/elle/ul there except 'o' and 'b' in forb/comm). No call.

## Campaign step H324 (29 Sept 2026, 13:16 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- f.211r's DBL: stacked vs side-by-side forced choice, CONTROL FAIL on the f.101r tiles

Pre-registered (PROMPTS section H324; `family/h324_dbl_forced.py`, key `family/h324_items.tsv`, committed 959a7e1c before the call; design narrowed
before the call from 4 to 2 f.101r tiles because automatic centring failed on that dense page, gate re-set to >= 5/6 known; PHI moved from NEITHER to a
report-only reference after the runner saw that f.211r's DBL are loops on a long stem). f.101r native fetched once (1 Gallica request). A fresh blind
Opus reader; reply verbatim `family/passes/h324_forced.tsv`; result `family/h324_dbl_forced_result.txt` (`--check` OK):
- Known: f.101r DBL (STACKED expected) **unclear 2/2**; f.61 SBS SIDEBYSIDE 4/4; NEITHER (C43, VBAR_A) 4/4 -> **known 4/6, gate CONTROL FAIL**, nothing
  read out, as pre-stated. The two f.101r tiles failed as tiles (dense page, neighbouring rows in frame), not as a shape answer.
- Descriptive only (in no gate): **f.211r DBL STACKED 5/5; f.211r SBS SIDEBYSIDE 3/3; f.61 PHI references STACKED 2/2.** So by this reader f.211r's
  DBL are not the side-by-side SBS glyph (H323's worry that they are SBS drawn taller finds no support), and they read like f.61's PHI (loops on a
  stem) as much as like f.101r's DBL.
For H317's scoring: PHI's cell (e/r) sits inside DBL's (e/r/u), so whether f.211r's DBL is scored as DBL or as PHI changes only the u; stated here so
the verifier can choose. Not re-run on the same f.101r tiles (rule 3). Vision calls this session: 10.

## Campaign step H322 (29 Sept 2026, 13:19 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- f.211r's two disagreement columns: forced choice CONTROL FAIL 3/4

Pre-registered (PROMPTS section H322; `family/h322_211r_recon.py`, key `family/h322_items.tsv`, committed with the claim before the call). One fresh
blind Opus forced choice EBRA / EBRB / VBARA on 6 tiles from the run's 2x strip; reply verbatim `family/passes/h322_forced.tsv`; result
`family/h322_211r_recon_result.txt` (`--check` OK):
- Known answers (columns both H315 passes agreed): col 5 EBRB, col 14 EBRB, col 18 VBARA right; **col 1 answered EBRA where both passes read VBAR_A**
  (pass A had noted "alt EBR_B") -> **3/4, gate CONTROL FAIL**; cols 13 and 17 stay flagged L in `family/passes/f211r_rec/ciphertext_h322.tsv`.
- Descriptive only: col 13 -> EBRB, col 17 -> VBARA.
What it shows: on this run the triangle-with-bar (VBAR_A) and the brackets (EBR_A/B) are confusable to model readers at this scale -- col 1 splits
them as col 17 did; for H317, VBAR_A (g/t) against EBR (i/l, a/l/s) is a real ambiguity at up to three columns (1, 13, 17), which a person's sign
rows (ASKS 93) would settle. Not re-run (rule 3). Vision calls this session: 11.

## Campaign step H325 (29 Sept 2026, 13:21 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- f.124r's held gloss under key v7: above the shuffled-cell p95 (148 vs 140), with a frequency confound named (script-only)

`family/h325_124r_agreed.py` (design and read-out in its docstring, written before running; result `family/h325_124r_agreed_result.txt`, `--check` OK).
fr.3982 f.124r's gloss (two blind passes, HELD since F61-FAMILY-4 at 42% word agreement; its rows never loaded into any key): **165 words read
identically by both passes** (651 letters), placed by x over **266 reconciled signs** (x from pass A where it equals the draft). Letters matched
one-to-one, order-free, into key v7's cells: **real 148**; 1000 keys with v7's cells permuted across the 15 keyed classes present: mean 109.9, **p95
140**, max 159, >= real **19/1000** -> pre-stated read-out **"consistent with key v7 on a held leaf"**. Hits by class (matched/signs under agreed
words): PHI 43/58, 4TRI 25/46, VBAR_A 24/51, C43 15/18, EBR_B 12/15, H24 12/20, HASH4 3/6, DBL 2/2, EBR_A 1/1 (SBS 0 -- f.124r's readers code a
LOOPS class instead, which v7 does not key).
**What limits it (for the verifier):** (1) the control permutes cells across classes but does not hold letter frequency: PHI (e/r) is by far the
commonest sign, so any key that gives common letters to common signs gains here whether or not its cells are right -- a frequency-matched control
(H328) is needed before this is more than a lead; (2) 651 letters over 266 signs: the gloss spans are wider than the signs matched, so most letters
cannot be matched by construction and the one-to-one cap is the sign count; (3) gloss letters are two-model-pass agreed (M), on a gloss hand the
passes disagree on 58% of words. Not a merge, not a reading; f.124r stays HELD. No call.

## Campaign step H328 (29 Sept 2026, 13:22 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- H325's f.124r result survives two frequency-matched controls (script-only)

`family/h328_124r_freq.py` (written before running; it executes H325's data-building code unchanged; result `family/h328_124r_freq_result.txt`,
`--check` OK). Same 165 agreed gloss words, 266 signs, one-to-one count; **real 148**.
- **(a) binned permutation** (cells permuted only within bins of 3 classes adjacent in f.124r token rank: PHI,4TRI,VBAR_A | H24,EBR_B,HASH4 |
  C43,BETA,ZBAR | 4STEM,RSIGN,DBL | EBR_A,VBAR_B,ISH): mean 124.9, **p95 143**, max 149, >= real **7/1000**.
- **(b) frequency key** (each keyed class given the k most frequent French letters of fr16, k = its v7 cell size): **132**.
- Pre-stated read-out: **"H325 lead stands"** (real > (a) p95 and > (b)).
What this is: on fr.3982 f.124r, a leaf whose gloss was never loaded into any key, the letters two independent model passes agree on fall inside key
v7's cells more often than under frequency-matched wrong keys -- a held-out check of the cells fitted on other leaves, at p about 0.007 against the
binned control. What it is not: a reading, a merge, or a check of f.61 itself; the gloss letters are grade M (two model passes on a gloss hand they
disagree on 58% of words); the margin over the binned p95 is 5 letters of 148; per-class hits (H325) are thin outside PHI/4TRI/VBAR_A/C43. For the
verifier: the first held-leaf evidence for v7's cells as a set. No call.

## Campaign step H329 (29 Sept 2026, 13:24 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- f.106r (the secretary's hand): too few agreed gloss words to test (script-only)

`family/h329_106r_agreed.py` (H325's data code with f124r -> f106r, H328's controls; written before running; result
`family/h329_106r_agreed_result.txt`, `--check` OK). fr.3983 f.106r's gloss passes (HELD at 0.339 word agreement; six cipher rows cut): **17 words
read identically, 49 letters, only 12 signs under them** (5 keyed classes). Real 5; shuffled cells p95 8; binned p95 7 (418/1000 >= real);
frequency key 4 -> pre-stated read-out **"no signal beyond frequency"**. At 12 signs the null spans nearly the whole range, so this is untestable at
this N, not a negative on v7 in the secretary's hand; a test there needs more of f.106r's gloss read (its other rows were never cut) or a person's
gloss reading. H325/H328's f.124r lead is the only held-leaf result so far. No call.

## Campaign step H327 (29 Sept 2026, 13:24 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- the instrument lesson, written down (notes only)

A paragraph "INSTRUMENTS" at the head of CAMPAIGN.md's "Attempts already made" and on `family/V9_PAGE.md`: the free letterform sort retired for LL
after three gate failures; the forced choice with known answers passed twice and failed only on poor or confusable known-answer tiles; held-leaf key
checks need a frequency-matched control (H325 -> H328). No call.

## Campaign steps H330 and H331 (29 Sept 2026, 13:27 UTC by the clock, runner 12 session_012eShPsWwW3quuzzUNV7nW5) -- the f.124r lead is fragile; PHI and C43 carry it, VBAR_A runs below chance there (script-only)

`family/h330_124r_boot.py` (written before running; H325's data code unchanged, H328's bins and frequency key; result
`family/h330_124r_boot_result.txt`, `--check` OK).
- **H330 (bootstrap, 200 resamples of the 165 agreed words):** real > binned p95 in **172/200 (86%)**, real > frequency-only key in **181/200 (90%)** --
  the pre-stated bar was 80% and 95%, so the read-out is **"fragile, rests on a few words"**. H328's pass stands as computed, but it does not survive
  resampling against the frequency key at the pre-stated level.
- **H331 (per class, v7 hits vs the binned permutation's per-class mean / p95):** PHI 43 of 58 signs vs mean 28.3, p95 43 (at p95; blanking PHI
  costs 43); C43 15/18 vs 6.9, p95 15 (at p95); EBR_B 12/15 vs 9.7, p95 13; H24 12/20 vs 11.0; 4TRI 25/46 vs 24.3; **VBAR_A 24/51 vs mean 29.9, p95
  35 -- below its binned mean**; the small classes sit at their means. No class is strictly above its p95.
What it means: on f.124r the v7 cells that look right are PHI (e/r) and C43 (a/n); VBAR_A's g/t scores worse there than other frequent classes'
cells would, which is either a direction-of-correspondence difference (f.124r is de Diou to Mayenne; v7's VBAR_A g/t is endorsed from f.176r and
f.108r) or the gloss passes' misreads -- rule 4 says a conflict like this is recorded by witness, not settled by the frequent value (added to
HYPOTHESES.md as a note, below). The held-leaf evidence is therefore thin: a lead for the verifier, not a confirmation of v7 as a set. No call.

## Campaign step H332 (29 Sept 2026, 15:03-15:16 UTC by the clock, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- f.106r rows 7-12: the model gloss readers fail this hand a second time; pooled rows 1-12 still untestable

f.106r native refetched once (btv1b9059406b f191, sha1 unchanged, requests.log). Rows 7-18 (the rest of the cipher block; row 18 is cipher only at
the left, then clear text) cut with `family/cut_bands.py` into `family/sheets/f106r_b/` (same geometry as sheets/f106r: 520 px segments, 60 overlap,
up 78 / down 42, x3; hand-set centres from an eye-marked strip, `--local 18 --slope -0.028`; boxes in `family/sheets/f106r_b_bands.json`, one sample
crop committed, the rest regenerable and git-ignored). Prompts `family/passes/prompts_h332/` (the F61-FAMILY-3 f.106r prompts re-targeted to L07-L12,
text otherwise unchanged, `family/gen_prompts_h332.py`) and the count script `family/h332_106r_more.py` committed before the calls returned. Four blind
Opus calls (two sign, two gloss; `family/passes/f106r_{signs,gloss}{A,B}_c2.tsv`). Result `family/h332_106r_more_result.txt` (`--check` OK):
- **Sign passes rows 7-12: 182/239 = 0.762** (rows 1-6 were 0.850); A 220 / B 234 signs. Both sign readers report the cut's fault at the right end:
  on L08-L10 the row leaves the band in s6-s7 (A skipped those signs, B read them from the next band's s7 at conf l) -- `--slope -0.028` under-follows
  the right end there. Named, not repaired in this step.
- **Gloss passes rows 7-12: 13 identical words of A 55 / B 48 = 0.252** (rows 1-6: 0.339); nearly every word graded l by both readers. HELD.
- **Pooled rows 1-12, H329's count and controls unchanged:** 29 agreed words, 88 letters, **27 signs under them** (9 keyed classes); real 11;
  shuffled cells p95 13 (300/1000 >= real); binned p95 12 (201/1000); frequency key 14 -> **"no signal beyond frequency"**, and under the pre-stated
  40-sign floor -> **untestable at this N, not a negative** on key v7 in the secretary's hand.
What it means: this is the second attempt at f.106r's gloss with the same instrument (blind Opus gloss passes), and agreement fell (0.339 -> 0.252);
with f.108r (H34, shared-wrong agreement) and f.124r (0.42) it is the fourth unit of the secretary's gloss the model readers fail. By rule 3's
"approach is the limit" clause this is logged **untested-by-this-tool** (HYPOTHESES.md), and rows 13-18 are not sent to the same passes. The one
instrument left for this gloss is a person's read (ASKS 99's f.106r desk pack, ASKS 88 for f.108r). Cost estimate 5.5 USD (four Opus image calls,
42 images each). No reading, no merge, no class change.

## Campaign step H334 (29 Sept 2026, 15:17 UTC by the commit stamp (corrected: first typed 15:20 without reading the clock), runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- f.106r right-end crops re-cut (script-only)

`family/h334_recut.py` (`--check` OK). A ruled strip of x 3600-4650 shows the rows at the right edge only about 35 px above their left-edge centres
(L08 1400, L09 1506, L10 1612 native): the rows rise through the middle of the leaf and flatten at the right, so H332's straight `--slope -0.028`
window sat 40-50 px above the row in L08 s7, L09 s6-s7 and L10 s7 -- exactly the four crops both sign readers flagged. `--track 18` was tried and is
worse (L10-L12 drift one row down). The four crops are re-cut at eye-set centres (boxes under `recut_h334` in `family/sheets/f106r_b_bands.json`);
each now holds its own cipher row with its gloss above (checked by eye). H332's pass rows for those four crops are therefore unreliable (A skipped them;
B read them from the neighbouring band at conf l); the count in H332 does not change its read-out (its words under those crops are few), and any
later use of rows 7-12 uses the re-cut crops. No call.

## Campaign step H333 (29 Sept 2026, 15:19 UTC by the commit stamp (corrected: first typed 15:26), runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- ASKS 99's f.106r desk pack extended to rows 7-12 (script-only)

`family/h333_pack2_106r.py` (`--check` OK): six more sheets in `family/images/person_pack_106r/` (f106r_L07-L12.jpg, H243's drawing), 25 more arrows
N18-N42 under every HASH4 both H332 sign passes wrote at the same reconciled position (10 'agree', 15 'agree-flagged'), x from pass A where its sign
matches, else pass B; the four H334 crops use their re-cut boxes. README section added; key.tsv rows N18-N42 'unshaped' (the looped/4-head shape was
not read on rows 7-12). Spot-checked by eye (N26, N38-N42 sit on hash-like signs in the sheet's own row). ASKS 99's text says 17 arrows on six
sheets; widening it to 42 on twelve (about 30 minutes) is the orchestrator's call -- flagged in ROOM, ASKS.md not edited here. No reading, no call.

## Campaign steps H335 and H336 (29 Sept 2026, 15:20-15:22 UTC by the commit stamps (corrected: first typed 15:30-15:33), runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- a gloss-free v7 check on f.106r: a non-test as gated; the frequency-key arm fails its own positive control (script-only)

`family/h335_106r_v7_beam.py` (written and committed before running; result `family/h335_106r_v7_beam_result.txt`, `--check` OK): f.106r rows 1-12
pooled draft (479 rows), runs of >= 4 v7-keyed signs (35 runs, 427 signs) resolved by the fr16 4-gram beam of scripts/f61beam_margin.py, score = log10
per letter. **Real (v7) -0.9491; binned-permuted keys (200, seed 3350) mean -1.1361, p95 -0.9477, 12/200 >= real; frequency-only key -0.7352** ->
pre-stated read-out "no signal beyond frequency".
`family/h336_beam_posctl.py` (written before running; result `family/h336_beam_posctl_result.txt`, `--check` OK) runs H335's code unchanged on two
leaves v7 was built from (in-sample, where the design must pass): **f.101r real -0.9416 vs binned p95 -0.9822 (0/200) but frequency key -0.7611 --
FAILS its own gate in-sample; f.188r real -0.8393 vs binned p95 -0.9459 (0/200), frequency key -0.8786 -- passes.** So the gate's frequency-key arm
cannot be met on a leaf whose key is right (a beam writes fr16's commonest 4-grams when every class holds e/s/a/...): **H335 is a non-test as gated, not
a negative** (the "control cannot fail differently" shape of rule 3). The binned arm does separate in-sample (0/200 on both leaves); on f.106r it sits
at its p95 (12/200, a borderline lead only). Its power at f.106r's 427 signs is unknown until the in-sample leaves are subsampled to that N (ARM3-ADJ's
rule) -- H337. The frequency-key arm is retired for beam scores (kept for the H325/H329 one-to-one counts, where it is a fair control). No call.

## Campaign step H337 (29 Sept 2026, 15:23-15:26 UTC by the commit stamps (corrected: first typed 15:36), runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- H335's binned arm is powered at f.106r's N; f.106r sits below the in-sample rate (script-only)

`family/h337_beam_power.py` (written and committed before running; result `family/h337_beam_power_result.txt`, `--check` OK): H335's code on 50 random
35-run subsets (f.106r's run count, 250-413 signs) of each in-sample leaf, 100 binned keys per subset. **f.101r: v7 > binned p95 in 43/50 (0.86);
f.188r: 50/50 (1.00)** -> pre-stated read-out "binned arm powered at f.106r's N -- H335's 12/200 is a weak lead".
What it means, without strengthening it: on leaves whose gloss built v7, a subset the size of f.106r's clears the binned p95 86-100% of the time;
f.106r itself falls just short (-0.9491 vs p95 -0.9477, 12/200 at or above). In-sample is optimistic (the cells were read from those very leaves), and
f.106r's sign draft is the least agreed of the three (0.85 / 0.76 by rows vs f.101r's and f.188r's), so the f.106r figure is a weak lead in the
secretary's hand that sits below the in-sample rate -- neither a confirmation of v7 there nor a negative. For the verifier with H325/H328/H330's f.124r
lead: two held-leaf checks, both at their gate's edge. No call.

## Campaign steps H338-H341 (29 Sept 2026, 15:26-15:37 UTC by the commit stamps and date -u (corrected: first typed 15:39-15:47), runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- the gloss-free beam check on the held leaves, then its shuffled-order control VOIDS the binned arm on four of seven leaves (script-only)

**H338-H340** (`family/h338_beam_held.py`, written before running; `family/h338_beam_held_result.txt`, `--check` OK): H335's code on the three family
leaves not in key_period_v7.tsv's leaf column, binned arm only. f.124r real -0.998 vs binned p95 -1.021 (0/200); f.97r -0.899 vs -0.906 (8/200);
f.108v (f.61's hand) rec108v -0.939 vs -1.016 (0/200), recf108vg -0.919 vs -0.942 (0/200; in-sample power at its 8 runs 0.40/0.82). All four read
'consistent' on the binned arm as stated.
**H341** (`family/h341_beam_shuffled.py`, written and pushed before running; `family/h341_beam_shuffled_result.txt`): rule 3's ARM-C1 order control --
each leaf's draft signs shuffled within the leaf (5 seeds), H335's code unchanged. v7 still beats its binned p95 on SHUFFLED order in **f.106r 2/5,
f.124r 4/5, f.108v rec108v 2/5, in-sample f.101r 3/5**; f.97r 1/5, recf108vg 0/5, f.188r 0/5. Pre-stated: >= 2/5 voids the arm on that leaf ->
**the binned beam arm is VOIDED as a gate at these N on f.106r, f.124r, f.108v (rec108v) and even in-sample f.101r**: there it measures v7's match of
letter frequency to sign frequency, not sequence. So H335/H337's "weak lead" on f.106r and H338's f.124r and H340's rec108v passes are **not evidence**
for v7; f.97r's pass and the recf108vg pass survive the rule on their own leaves only, and since the same leaf f.108v gives one voided and one clean
draft, and the arm voids in-sample on f.101r, those two are fragile leaf-level results, not a family gate. Descriptive (not pre-stated): the
real-order v7 score exceeds the mean shuffled-order v7 score on every leaf (f.106r -0.949 vs about -0.99; f.108v rec108v -0.939 vs about -1.08;
f.188r -0.839 vs about -0.97), but shuffling also re-cuts the runs, so this is not yet a clean statistic -- H342 would pre-state it.
Lesson (the ARM-C1 shape again): a within-frequency-bin key permutation is not an order control; a beam gate needs the shuffled-target arm from the
first run. No call.

## Campaign step H343 (29 Sept 2026, 15:38 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- the beam-check lesson, written down (notes only)

CAMPAIGN.md's INSTRUMENTS paragraph gains the beam-check lesson (a within-bin key permutation is not an order control; the frequency-only key is not a
fair beam control); `family/V9_PAGE.md` gains one line for the verifier: the H335/H338/H340 beam passes are not evidence for v7, f.97r fragile only, the
f.124r gloss-count lead unaffected, and the model gloss readers retired for the secretary's hand. No call.

## Campaign steps H342 and H344 (29 Sept 2026, 15:39-15:51 UTC by date -u and the commit stamps, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- an order statistic that passes its in-sample control and its shuffled-target control: held-leaf order signal for key v7 on f.124r and f.97r (script-only)

**H342** (`family/h342_beam_seqgain.py`, written and pushed before running; `family/h342_beam_seqgain_result.txt`): per leaf, v7's beam score in real
order minus its mean over 10 WITHIN-RUN shuffles (run cuts and each run's sign multiset fixed, so letter frequency cannot score), against the same gain
under 100 binned-permuted keys. **Positive control PASS: in-sample f.101r gain 0.080 vs binned p95 0.052 (0/100 >= v7), f.188r 0.179 vs 0.080 (0/100).**
Held leaves: **f.124r 0.032 vs 0.020 (0/100); f.97r 0.057 vs 0.037 (0/100); f.108v rec108v 0.134 vs 0.098 (1/100), recf108vg 0.096 vs 0.076 (2/100);
f.106r rows 1-12 0.051 vs 0.056 (13/100) -- no order signal.**
**H344** (`family/h344_seqgain_shuftarget.py`, written and pushed before running; `family/h344_seqgain_shuftarget_result.txt`): ARM-C1 -- H342's code on
whole-leaf-shuffled drafts, 3 seeds; any 'order signal' voids the leaf. **0/3 on f.101r, f.188r, f.124r, f.97r, recf108vg; 1/3 on rec108v (voided).**
What it means: on two large leaves v7 was not built from -- fr.3982 f.124r (de Diou's letter, 2105 keyed signs) and f.97r (1809) -- v7's cells make
the sign order read more like fr16 French than the same order under frequency-matched permuted keys, and the statistic passes both its in-sample control
and its shuffled-target control. This is **held-leaf evidence for v7's cells as a set** (cryptanalytic, script-only; not a reading, no token graded,
no cell changed). f.108v (f.61's own hand) is fragile: one draft passes both, the other is voided. f.106r (the secretary's hand) shows no order signal
at its N (power not yet measured for this statistic -- H346). The earlier beam-vs-binned passes (H338/H340) remain void (H341); this is a different
statistic. For the verifier (V9_PAGE.md line added). No call.

## Campaign step H346 (29 Sept 2026, 15:53-15:57 UTC by the commit stamp and date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- H342's order statistic is underpowered at f.106r's N (script-only)

`family/h346_seqgain_power.py` (written and pushed before running; `family/h346_seqgain_power_result.txt`): 30 random 35-run subsets of each in-sample
leaf, 50 binned keys each. **f.101r 19/30 = 0.63; f.188r 30/30 = 1.00** -> pre-stated read-out "underpowered at f.106r's N": f.106r's H342 miss
(13/100) is **untestable at this N, not a negative** on v7 in the secretary's hand. A test there needs more of the leaf's sign rows (rows 13-18, sign
passes only -- the gloss passes are retired for this hand, H332) or the person's gloss read (ASKS 99). No call.

## Campaign step H347 (29 Sept 2026, 15:58-15:59 UTC by the commit stamp and date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- v6 vs v7 on the held leaves: only 4PI differs; split, too few signs (script-only)

`family/h347_seqgain_v6v7.py` (written and pushed before running; `family/h347_seqgain_v6v7_result.txt`). Correction to the CAMPAIGN row: loaded pooled,
key v6 and v7 differ only in **4PI (v6 a/d/n/q -> v7 d/q)**; the change list the row named (VBAR_A g/t, EBR_B l/y, SBS b/o, HASH4 d/q, H24 i/x) is
v6's own change set, already in both keys. Under H342's gain (three shuffle seeds): f.124r v7 0.032/0.033/0.036 vs v6 0.033/0.033/0.037 (4PI 2 signs:
v7 change 'hurts' by under 0.001); f.97r v7 0.057/0.051/0.051 vs v6 0.051/0.046/0.047 (4PI 10 signs: 'helps'). At 2 and 10 signs this is split and
uninformative; nothing to carry to the key. No call.

## Campaign step H345 (29 Sept 2026, 15:52-16:00 UTC by the commit stamp and date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- per-class breakdown of H342's order signal: descriptive, confounded by cell size (script-only)

`family/h345_seqgain_perclass.py` (design change logged in its docstring before running: every other keyed class's v7 cell as the alternatives,
since bins of 3 give only two; result `family/h345_seqgain_perclass_result.txt`). v7's own cell ranked among the alternatives by H342's gain, per class:
- Across both held leaves: **HASH4 d/q rank 2 and 2; C43 a/n 3 and 1; VBAR_A g/t 5 and 3; PHI e/r 5 and 2; ZBAR f/s 4 and 2; H24 i/x 14 and 1;
  4TRI c/p/t 15 and 8; EBR_B (l/y, loaded folded as i/l) 13 and 22 of 22 -- the worst cell on f.97r; EBR_A a/l/s 12 and 18; RSIGN c/m/n/p/s/t 17 and 20.**
- Two flaws, so this is **descriptive only**: (1) a class with no signs in the runs (ZHOOK, 0) ranks 1 by ties -- its "supported" is an artefact;
  (2) the best alternatives are mostly one-letter cells (C6 e, ELOOP r, VBAR_B s), so the gain statistic appears to favour narrow cells: a broad v7
  cell (4STEM, RSIGN, 4TRI) ranks low partly for its size. A size-matched comparison is H349.
- For the verifier, as a pointer only: EBR_B scores worst-or-near on both held leaves, the same class whose form split the campaign has already flagged (H321, H322); its cell
  i/l is v7's l/y under the loader's i/y fold (key row: 'y = folded i/y of the clear'), not a different cell (corrected 16:19 UTC the same day); VBAR_A g/t ranks well on both held leaves by this statistic, unlike H331's gloss count on
  f.124r (below its binned mean there) -- a disagreement between two instruments, recorded, not resolved (rule 4). No call, no cell changed.

## Campaign step H348 (29 Sept 2026, 16:01-16:05 UTC by the commit stamps and date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- f.106r rows 13-18 sign passes; the order statistic on rows 1-18 shows no signal (power at 51 runs not yet measured)

Prompts `family/passes/prompts_h348/` (H332's sign prompts re-targeted to L13-L18, `family/gen_prompts_h348.py`) and `family/h348_106r_rows18.py`
committed before the two blind Opus sign calls returned (`family/passes/f106r_signs{A,B}_c3.tsv`; no gloss passes, retired for this hand). Crops' right
ends checked by eye first (no re-cut needed). Result `family/h348_106r_rows18_result.txt`: **sign agreement rows 13-18 190/232 = 0.819** (L18 turns to
clear French from s4; both readers listed it PLAIN). Rows 1-18 pooled (`passes/recf106rall18`): **51 runs, 622 signs; gain(v7) 0.0279 vs binned gains
mean 0.0160, p95 0.0490 (31/100 >= v7) -> "no order signal at >= 50 runs"** as pre-stated. The pre-statement did not carry a power figure at 51 runs
(H346: 0.63 / 1.00 at 35), and f.106r's gain (0.028) is of the size held f.124r's was (0.032, which cleared only at 227 runs); so this is logged as
no signal at this N, **not a negative, until H350 measures power at 51 runs**. The f.106r sign draft now covers the whole cipher block (rows 1-18). Two
vision calls, cost estimate 2.5 USD.

## Campaign step H350 (29 Sept 2026, 16:06-16:12 UTC by the commit stamps and date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- the order statistic is powered (just) at 51 runs in-sample: f.106r's miss reads as a negative at this N, with two caveats (script-only)

`family/h350_seqgain_power51.py` (written and pushed before running; `family/h350_seqgain_power51_result.txt`): 30 random 51-run subsets of each
in-sample leaf, 50 binned keys each. **f.101r 24/30 = 0.80; f.188r 30/30 = 1.00** -> pre-stated read-out "powered at f.106r's N -- f.106r's no-signal
result (H348, rows 1-18, 31/100) is a negative for v7 in the secretary's hand at this N". Rule 3's error-bracket check: the in-sample drafts' sign
agreement (f.101r 0.802, f.188r 0.776) brackets f.106r's pooled 576/711 = 0.810, so the control is not cleaner than the target.
Two caveats, carried, not argued away: (1) f.101r's power sits exactly at the 0.8 bar; (2) in-sample power is an upper bound for a held leaf (v7's cells
were read from those leaves), so the fairer reference is a held leaf that does show the signal, subsampled to 51 runs -- H351. Until H351, the reading
is "no order signal for v7 in the secretary's hand on f.106r, a negative at this N by the pre-stated in-sample power". This is a leaf-level result on
key v7, not a class change: the campaign stays open (rule 5). No call.

## Campaign step H351 (29 Sept 2026, 16:13-16:18 UTC by the commit stamp and date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- held-leaf power at 51 runs is low: f.106r's miss is untestable at this N, not a negative (H350's reading corrected) (script-only)

`family/h351_seqgain_heldpower.py` (written and pushed before running; `family/h351_seqgain_heldpower_result.txt`): 30 random 51-run subsets of the
held leaves where v7 does show the order signal, 50 binned keys each. **f.124r 3/30 = 0.10; f.97r 16/30 = 0.53** -> pre-stated read-out "held leaves
underpowered at 51 runs -- f.106r's miss is untestable at this N, not a negative". This supersedes H350's in-sample reading, as H350's second caveat
anticipated: in-sample power (0.80 / 1.00) overstates what a held leaf shows. **f.106r (the secretary's hand): no order signal and untestable at
51 runs**; the whole cipher block is now drafted, so no more of this leaf can raise N -- the order check in this hand needs a longer leaf in the
secretary's hand (f.211r's run is 18 signs) or the person's gloss read (ASKS 99). HYPOTHESES.md's H348/H350 row is corrected in place. No call.

## Campaign step H353 (29 Sept 2026, 16:21-16:22 UTC by the commit stamp and date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- f.108v (f.61's own hand): the order signal holds on the signs both drafts read alike, with a splice caveat (script-only)

`family/h353_108v_agreed.py` (written and pushed before running; `family/h353_108v_agreed_result.txt`, `--check` OK): f.108v's two sign drafts (rec108v,
recf108vg) aligned by tools/reconcile_passes.py; **180 of 318 columns (0.566) read alike**, kept in order as `passes/recf108vagree/`. **H342: 8 runs,
179 signs, gain(v7) 0.079 vs binned p95 0.071 (5/100) -> order signal; H344 shuffled targets 0/3** -> pre-stated read-out "f.108v's order signal is
carried by the signs both drafts read".
Caveats, carried: (1) dropping the 43% of columns where the drafts differ splices non-adjacent signs into one run, so some 4-grams span a gap -- this
should blur a real sequence signal rather than make one, but the design did not correct for it; (2) 8 runs, and the statistic's power at 8 runs was not
measured (H340's beam power at 8 runs was 0.40/0.82 in-sample, a different statistic). So f.108v moves from 'fragile' to 'a thin order signal in
f.61's own hand, on agreed signs'. Evidence about v7's cells as a set; not a reading. No call.

## Campaign step H354 (29 Sept 2026, 16:23-16:26 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- the order statistic becomes a mode of a shared tool (rule 8)

Rule 8 ("an option added to the tool, not a private copy"): `tools/partial_key_test.py` already scores a partial key by order structure against
shuffled controls, for one-letter codes; it gains a `--cells` polyphonic order mode (letter-SET cells, 4-gram beam, within-run shuffle gain, binned
keys, `--shuffle-target` for the ARM-C1 control; the H341 lesson in its docstring), rather than a new tools/order_gain.py as the row first said.
Offline test `tools/tests/test_partial_key_test_cells.py` (a pair-cell key on 480 letters of fr16 French: true key gain 0.474 > binned p95 0.118;
the same draft shuffled 0.019 <= p95 0.067; run breaks at unkeyed signs and line ends); the tool's own test still passes. Equivalence: with v7's cells
written as `family/key_v7_cells_h354.tsv`, `python3 tools/partial_key_test.py --cells family/key_v7_cells_h354.tsv --draft
family/passes/recf124r/ciphertext_draft.tsv` prints gain 0.0320, binned mean -0.0015, p95 0.0198, 0/100 -- H342's f.124r line exactly. h342-h351
are left as they are (their results are cited; their --check stays OK). SYSTEM.md line updated (system_map_check exit 0). No call.

## Campaign step H349 (29 Sept 2026, 16:23-16:29 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ; first run stopped at 16:23 for a loop bug fixed before any output) -- size-matched per-class order gain on the held leaves (script-only)

`family/h349_seqgain_sizematch.py` (written and pushed before running; the draw-loop cap fixed and pushed before the rerun, no output seen; result
`family/h349_seqgain_sizematch_result.txt`). Per class with >= 30 signs in runs, v7's cell against its size-matched alternatives (other v7 cells of the
same size plus fr16-frequency-weighted random sets), share beaten, f.124r / f.97r; pre-stated 'supported' iff >= 0.95 on both:
- **HASH4 d/q 1.00 / 1.00 -> supported.**
- Mixed (one leaf): **C43 a/n 0.92 / 1.00; H24 i/x 0.51 / 1.00; ZBAR f/s 0.92 / 0.97.**
- Not supported: PHI e/r 0.82 / 0.92; VBAR_A g/t 0.90 / 0.95 (f.97r: 37 of 39 = 0.949, printed rounded, just under the bar; the script's 'miss'
  stands); BETA m/s 0.79 / 0.82; 4STEM a/c/e/n 0.80 / 0.57; 4TRI c/p/t 0.06 / 0.94; **EBR_B l/y (loaded folded i/l) 0.46 / 0.08 -- the lowest**;
  one leaf only: VBAR_B s 0.91, EBR_A a/l/s 0.41.
What it means: by an order statistic with size-matched alternatives, the held leaves back v7's d/q cell for HASH4 (the 4-head) outright, and C43 a/n,
H24 i/x and ZBAR f/s on one leaf each. EBR_B's l/y is a period cell (fr.3984 f.176r's gloss, 95 counts, grade C); a weak cryptanalytic score does not
outrank a period witness (rule 4) -- recorded as a pointer for the verifier: EBR_B's form split or its cell may not carry from f.176r's hand to
f.124r/f.97r (H321/H322 already flag this class's forms). A per-class test at 95% of about 39 alternatives is strict and each class's share of the
signal is small, so 'not supported' here is not 'wrong'. No cell changed. No call.

## Campaign steps H356 and H357 (29 Sept 2026, 16:33-16:34 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- EBR forms and 4TRI's mixed code under the order gain: two pointers, uncontrolled (script-only)

`family/h356_357_cells_order.py` (written and pushed before running; result `family/h356_357_cells_order_result.txt`), H347's design, gain under three
shuffle seeds, v7 first:
- **H357, f.124r: 4TRI widened to c/p/t + a/n: 0.072/0.080/0.072 vs v7 0.032/0.033/0.036 -- raises the gain, more than double**; on f.97r unclear
  (0.054/0.049/0.052 vs 0.057/0.051/0.051). Consistent with H218/H231's finding that the 4TRI code carries the no-bowl sign too (C43's a/n), and with
  H349's 4TRI 0.06 on f.124r vs 0.94 on f.97r: the readers' 4TRI on f.124r would mix two signs.
- **H356, f.97r: EBR forms swapped (EBR_B <- a/l/s, EBR_A <- l/y) raises the gain (0.072/0.067/0.069 vs 0.057/0.051/0.051); pooled union raises it
  too**; on f.124r swap unclear, union lowers it. A pointer that on f.97r the readers' EBR_A/EBR_B labels may run opposite to f.176r's form B (H321/H322).
Uncontrolled: widening a cell or moving a cell gives the beam other letters to choose, and whether a/n or a/l/s *specifically* does this, rather than
any added letters, is not tested here -- H358 is that control. Pointers for the verifier only; no cell changed. No call.

## Campaign step H358 (29 Sept 2026, 16:35-16:37 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- the control for H356/H357: the 4TRI pointer on f.124r stands, the EBR one does not (script-only)

`family/h358_variant_ctl.py` (written and pushed before running; `family/h358_variant_ctl_result.txt`), mean order gain over three shuffle seeds:
- **(a) f.124r, 4TRI c/p/t + a/n: 0.0748; 30 random 2-letter widenings mean 0.0494, max 0.0602; beats 1.00 -> pointer stands.** On de Diou's f.124r the
  readers' 4TRI code behaves as if it also carries a sign that stands for a/n -- the no-bowl sign whose period cell is C43's a/n (H218/H231 found the
  4TRI code mixes the bowl and no-bowl signs on f.176r, f.101r and f.106r). A shape split of f.124r's 4TRI tokens would test it directly (H359).
- **(b) f.97r, EBR_B <- a/l/s: 0.0667; 30 random 3-letter cells mean 0.0593, max 0.0683; beats 0.87 -> 'added letters, not these letters'.** H356's EBR
  pointer is withdrawn: on f.97r any other 3-letter cell for EBR_B scores about as well, so it says only that l/y fits f.97r's EBR_B poorly (H349).
Pointer (a) is for the verifier and for the transcription side, not a cell change: v7's 4TRI and C43 cells are unchanged. No call.

## Campaign step H355 (29 Sept 2026, 16:33-16:39 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- H349's per-class test is underpowered in-sample: its misses carry no information, only its passes stand (script-only)

`family/h355_sizematch_posctl.py` (H349's code on the in-sample leaves, written and pushed before running; `family/h355_sizematch_posctl_result.txt`).
**f.188r: every one of 11 classes >= 0.95 (PHI, 4TRI, VBAR_A, C43, H24, HASH4, INF, VBAR_B 1.00; 4STEM, EBR_B, ZBAR 0.97). f.101r: 4 of 10 (VBAR_A
0.97, H24, HASH4, INF 1.00); PHI 0.95 (just under), C43 0.95, ZBAR 0.90, 4STEM 0.87, 4TRI 0.84, EBR_B 0.77, RSIGN 0.67.** Supported on both: 4 of 11
-> pre-stated read-out **"per-class test underpowered: H349's misses carry no information, only its passes stand"**.
Carried into H349's reading: HASH4 d/q (both held leaves) and C43 a/n, H24 i/x, ZBAR f/s (one each) stand as order support; **EBR_B's low held-leaf
scores (0.46/0.08) are not evidence against its l/y cell** -- in-sample f.101r scores it 0.77 too. f.101r, the largest leaf, is also where the
per-class test is weakest (gain 0.080 vs f.188r's 0.179): the per-class statistic tracks how cleanly a leaf's draft and hand fit v7 as a whole. No call.

## Campaign step H359 (29 Sept 2026, 16:39-16:45 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- f.124r's 4TRI code is mostly the no-bowl sign: shape supports H358's order pointer (1 vision call)

`family/h359_bowl_124r.py`, key `family/h359_items.tsv`, prompt section H359 in `family/passes/PROMPTS_f176_f175.md` (H199's text verbatim), committed
before the call. Natives refetched once each (f.176r f327, f.176v f328 -- sha1 as H230's; f.124r f256, sha1 8b7e91c7 as the 28 Sept fetch; 3 requests,
requests.log); H193's 60 strips regenerated, h193_items.tsv byte-identical. Two changes made before the call and disclosed: the target filter widened
to 'agree' + 'agree-flagged' (only 54 4TRI were unflagged), and the marker moved above the strip after the runner looked at the top of target sheets
01-02 for placement (f.124r's gloss sits below its cipher rows). One blind Opus call, reply `family/passes/h359_reply.tsv`; result
`family/h359_bowl_124r_result.txt` (`--check` OK):
- **Control 18/20 f.176v anchors PASS (gate 17).**
- **f.124r 4TRI (50): no bowl 31, bowl 15, unclear 4 -> no-share 0.67; C43 (20): no bowl 20 -> 1.00.** Pre-stated read-out: **"shape supports H358's
  pointer"**.
What it means: in de Diou's f.124r, two thirds of the tokens both readers coded 4TRI lack the stem-foot bowl that marks the c/p sign on f.176v -- they
look like the no-bowl sign whose period cell is a/n (C43). This matches H358 (widening 4TRI by a/n beats every random widening under the order gain) and
H218/H231's finding that the 4TRI code mixes the two signs. It is a transcription finding: the readers' 4TRI on this leaf is two signs. For the
verifier and the transcription side; v7's cells are unchanged; f.124r's HELD gloss is untouched. Caveat: the bowl gate is on Desportes's hand
(f.176v); de Diou's bowl may be drawn differently -- the C43 tokens' 20/20 no-bowl is the leaf's own check that 'no' is not simply the default. 1 call.

## Campaign step H360 (29 Sept 2026, 16:46-16:51 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- f.124r's agreed 4TRI tokens bowl-read in full: three quarters are the no-bowl sign, and splitting them doubles v7's order gain (4 vision calls)

`family/h360_124r_4tri_split.py`, key `family/h360_items.tsv`, prompt note H360 in `family/passes/PROMPTS_f176_f175.md` (H359's prompt verbatim),
committed before the calls; the runner did not look at the H360 sheets. The other 220 agreed 4TRI tokens of f.124r in four blind Opus calls of 55,
H193's 60 strips in each; replies `family/passes/h360_reply_c1..c4.tsv`; result `family/h360_124r_4tri_split_result.txt`:
- **Gates: c1 18/20, c2 19/20, c3 18/20, c4 19/20 -- all PASS** (H193's anchors are the same 60 strips in every call; their answers agree across calls
  except Q06/Q12/Q34/Q37, one or two calls each).
- **All 270 agreed 4TRI (H359 + H360): no bowl 202, bowl 59, n 9.** The split draft (`passes/recf124r_split/`) relabels the 202 as C43.
- **Order gain (H342, v7 unchanged): as transcribed 0.032/0.033/0.036 -> split 0.071/0.073/0.068, higher under all three seeds; H344 shuffled targets
  on the split draft 0/3 -> pre-stated read-out "the split raises the order gain".**
What it means: on de Diou's f.124r the readers' 4TRI code is mostly (about 75%) the no-bowl sign, which v7 reads a/n (C43), and reading those tokens
so makes the leaf's sign order fit French about twice as well under v7 -- a shape answer (with its own known-answer gate) and an order statistic (with
its own controls) agree. A **transcription correction for the f.124r draft**, not a cell change and not a reading; it also means every earlier f.124r
count on the unsplit draft (H325/H328/H330's gloss lead, H331's per-class, H338-H349) saw two signs under one code. For the verifier. Four calls,
cost estimate 4.0 USD.

## Campaign step H361 (29 Sept 2026, 16:52-16:54 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- the gloss count agrees with the 4TRI split on f.124r (script-only)

`family/h361_124r_split_gloss.py` (written and pushed before running; `family/h361_124r_split_gloss_result.txt`, `--check` OK): H325/H328's held-gloss
count (two-pass agreed gloss letters matched one-to-one into v7's cells) on H360's split draft, code unchanged except the draft path and the pass-A
match rule (compared with the original draft's sign, so relabelled tokens keep their x). **Split draft: real 156 (original 148); binned permutation
mean 131.7, p95 148, 1/1000 >= real; frequency key 130** -> pre-stated read-out **"the split is supported by the gloss"**.
What it means: two instruments that share neither method nor data path -- the order gain over the sign draft (H360) and the one-to-one count against
the leaf's own period gloss letters (H361) -- both improve when f.124r's no-bowl 4TRI tokens are read as C43 (a/n). The gloss is HELD (grade M, two
model passes at 0.42 word agreement), so this is agreement between leads, not a reading; H330's fragility caveat on the gloss lead still applies to
the gloss count as such. For the verifier, together with H359/H360. No call.

## Campaign steps H362 and H364 (29 Sept 2026, 16:55-16:58 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- on f.101r too the readers' 4TRI is mostly the no-bowl sign, and there the period gloss confirms it pairs with a/n (1 vision call + script)

**H362** (`family/h362_bowl_101r.py`, key `family/h362_items.tsv`, prompt note in `family/passes/PROMPTS_f176_f175.md`, committed before the call; the
runner did not look at the sheets; native f.101r refetched once, canvas 210): H359's design and prompt on fr.3982 f.101r, 50 agreed 4TRI + 20 C43,
one blind Opus call (`family/passes/h362_reply.tsv`; result `family/h362_bowl_101r_result.txt`, `--check` OK). **Control 17/20 PASS (at the bar).
4TRI: no bowl 36, bowl 11, n 3 (no-share 0.77); C43: no 19, yes 1 (0.95).** Pre-stated read-out: "f.101r's 4TRI mixes the no-bowl sign: write the
full split row". f.97r not run (its draft is built from several cuts; its 4TRI scored 0.94 in H349) -- logged in the script.
**H364** (`family/h364_101r_bowl_letter.py`, written and pushed before running; `family/h364_101r_bowl_letter_result.txt`, `--check` OK): H362's
answers joined to f.101r's period alignment (`passes/f101r_align.tsv`, the gloss letter the alignment pairs with each code; the draft and alignment
code sequences matched per line by difflib). **4TRI no-bowl: a/n 23, c/p/t 6, other 5; 4TRI bowl: c/p/t 6, a/n 4, other 1; C43 no-bowl: a/n 15, c/p/t 1;
bowl-letter agreement 44/56 = 0.79** -> pre-stated read-out **"the bowl tracks the letter on f.101r"**.
What it means: on the very leaf whose period gloss built v7's 4TRI cell, the tokens the readers code 4TRI but that lack the stem-foot bowl are paired by
the period decipherment with a or n (23 of 29 with a c/p/t or a/n letter): they are the a/n sign, not the c/p sign. So the readers' 4TRI code conflates
two signs across hands (f.101r, f.124r; H218/H231 found the same on f.176r and f.106r), the bowl separates them (H193's attribute, now checked against
period letters on a second hand), and the a/n rows in v7's own 4TRI tally (a 9, n 10 on f.101r) are those no-bowl tokens. For the verifier: this bears
on v7's 4TRI cell as built (it pools two signs' letters, then keeps c/p/t by the top-two rule) and on every 4TRI count in the family. No cell changed
here: re-splitting the pooled key by shape is a key-build step with its own gates (H365, H366). Cost: 1 call, estimate 1.0 USD.

## Campaign step H365 (29 Sept 2026, 16:59-17:04 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- f.101r in full: the no-bowl "4TRI" is the a/n sign by f.101r's own period gloss (118 of 130), and the split raises the order gain in-sample too (4 vision calls)

`family/h365_101r_4tri_split.py` (H360's code with the leaf swapped, plus H364's cross-tab at full N), key `family/h365_items.tsv`, prompt note H365,
committed before the calls; the runner did not look at the sheets. Four blind Opus calls (191 tokens), replies `family/passes/h365_reply_c1..c4.tsv`,
result `family/h365_101r_4tri_split_result.txt`:
- **Gates 19, 18, 17, 18 of 20 -- all PASS.** With H362: **241 answered 4TRI: no bowl 155, bowl 67, n 19.**
- **Period letter (f.101r's own alignment) by bowl answer: no bowl -> a/n 118, c/p/t 12, other 20, none 5; bowl -> c/p/t 33, a/n 19, other 15;
  bowl-letter agreement 151/182 = 0.83** (H364's bar 0.75 -> the bowl tracks the letter).
- **Order gain (v7, in-sample): as transcribed 0.080/0.079/0.087 -> split 0.097/0.099/0.108; shuffled targets 0/3 -> "the split raises the order gain".**
What it means: on the leaf whose period gloss built v7's 4TRI cell, the readers' 4TRI code is about two thirds the no-bowl sign, and the period
decipherment reads that sign a or n in 118 of the 130 cases with an a/n or c/p/t letter -- the no-bowl "4TRI" behaves as the a/n sign (C43's cell), by the
period key itself (grade C per pair), not only by our statistics. The bowl sign leans c/p/t (33 v 19): cleaner, not clean. So v7's 4TRI cell was built
from a tally that mixes two signs. **For the verifier, and for the key: H366 writes the split tally as a proposal (rule 4, witnesses named); nothing is
loaded into a key here.** Four calls, cost estimate 4.0 USD.

## Campaign steps H366 and H363 (29 Sept 2026, 17:05-17:06 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- the 4TRI resplit written as a proposal for a verifier; the instrument lesson (script/notes)

**H366** (`family/h366_4tri_proposal.py`, `--check` OK) writes `family/PROPOSAL_v8_4tri.md`: f.101r's period letters for the readers' 4TRI by bowl
answer -- **bowl (67): p 17, c 15, n 11, a 8, ...; no bowl (150): a 62, n 56, p 5, c 4, ...** -- with the witnesses for and against, proposing (not
applying) that the no-bowl "4TRI" be read as the a/n sign and 4TRI's c/p/t kept for the bowl sign. Rule 4: the verifier decides; f.61's own 4TRI tokens
have not been bowl-read (H367).
**H363** (notes): CAMPAIGN.md's INSTRUMENTS paragraph gains the sequence that found this: an order-gain pointer (H358) -> its random-variant control ->
a shape forced choice with known answers in every call (H359/H360/H362/H365) -> the split's order gain with a shuffled-target control -> the leaf's own
period letters by shape answer (H364/H365) -> an independent held-gloss count (H361). Each link had its own control; the period letters are the only
link that is not our statistic. No call.

## Campaign step H369 (29 Sept 2026, 17:06 UTC by date -u, runner 13 session_01MSoJWwZxNPSjQd4hszNdvQ) -- the ask to the verifier (notes only)

A paragraph at the foot of `family/V9_PAGE.md` asks the verifier lane to rule on `family/PROPOSAL_v8_4tri.md` before any key v8, with the witnesses and
the open objections; the matching ROOM line is posted. No call, no class, no cell.

## Campaign step H367 (29 Sept 2026, 17:16-17:22 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.61's own 4TRI is the bowl sign: 5 of 6 at fixed positions, H194 reproduces 14/15 (1 vision call)

`family/h367_bowl_f61.py`, key `family/h367_items.tsv`, prompt note H367 in `family/passes/PROMPTS_f176_f175.md` (H359's prompt verbatim), committed
before the call. Natives f327/f328 fetched once each (sha1 a2b0d98e / 4a13be67 as H230/H359; 2 Gallica requests, requests.log); H193's 60 strips
regenerated, h193_items.tsv byte-identical. Targets: all 18 4-family signs of `scripts/f61_positions_all.tsv` (6 4TRI, 9 C43, 1 4STEM, 2 4PI; L10
has none), cut from the native f.61 region image (verify_v9's source and x mapping). H194 had asked the same question of 15 of them in a different
design (count-matched span sheets; L01 left out), so the call doubles as its reproduction at fixed positions. **Disclosed change before the call:** the
runner looked at the sheet for marker placement; markers sat on the intended signs, but H359's -60/+55 window clipped every stem below the line, so
the window moved to -45/+92 (the runner has seen the target shapes; the reader has not). One blind Opus call, reply `family/passes/h367_reply.tsv`;
result `family/h367_bowl_f61_result.txt` (`--check` OK):
- **Control 19/20 f.176v anchors PASS (gate 17).**
- **f.61 4TRI: bowl 5, no bowl 1 (yes-share 0.83); C43 no bowl 9/9; 4STEM no 1/1; 4PI no 2/2.** Pre-stated read-out: **"f.61 4TRI is the bowl sign"**.
- 4TRI answered no (its cell would move under PROPOSAL_v8_4tri.md): **L05/14** only. H194 answered yes there, and it sits inside Tomokiyo's span S3
  where his published letter is c (H194 result) -- the one disagreement between the two reads is against the published letter, so it is more likely a
  reading slip of this call than a no-bowl sign; the verifier decides.
- C43/4STEM/4PI answered yes: none. **H194 agreement 14/15 -> "H194 reproduces"**; L01's three signs (C43 no, 4TRI yes, 4PI no) are read for the first
  time in this campaign and follow the same pattern.
What it means: in f.61's own hand (the target leaf), the readers' 4TRI code is the bowl sign and C43 the no-bowl sign almost without exception -- unlike
de Diou's f.124r (75% no-bowl, H360) and f.101r (64%, H365), and unlike f.108v, where the same hand's bowl sign was coded 4STEM (H199). So the
PROPOSAL_v8_4tri.md split, if the verifier adopts it, would move at most one f.61 position (L05/14) and probably none; f.61's 4TRI tokens sit in the
bowl (c/p) half of the proposed split. Evidence for VERIFY-F61-V11; no key, cell or grade changed. 1 call, cost estimate 1.5 USD.

## Campaign step H368 (29 Sept 2026, 17:23-17:27 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.106r (the secretary's hand): both readers' codes 4TRI and 4STEM mix the bowl and no-bowl signs; C43 is always no-bowl (2 vision calls)

**Re-scoped before running (logged in the row):** f.108v is not re-read -- H199 bowl-read its 4-family in full (74 strips) and H230 reproduced it
(the bowl sign there is the readers' 4STEM, 4TRI 0/6). Both calls went to fr.3983 f.106r rows 1-18 (H231 had read 33 strips of rows 1-6 only).
`family/h368_bowl_106r.py`, key `family/h368_items.tsv`, prompt note H368 in `family/passes/PROMPTS_f176_f175.md` (H359's prompt verbatim), committed
before the calls; the runner did not look at the H368 sheets. Targets from pass A (the reconciled draft carries no x): all 19 4TRI and 59 4STEM, plus
20 of 63 C43 (seed 368), cut at H231's geometry (validated on this leaf) from the native (Gallica btv1b9059406b f191, sha1 5aa1a799 as the 15:04 fetch;
1 request, requests.log); H193's 60 strips in each call. Replies `family/passes/h368_reply_c1.tsv`, `_c2.tsv`; result
`family/h368_bowl_106r_result.txt` (`--check` OK):
- **Gates c1 19/20, c2 18/20 -- PASS.**
- **4TRI: bowl 9, no bowl 8, n 2 (no-share 0.47, over H362's 0.4 bar); 4STEM: bowl 24, no bowl 31, n 4 (yes-share 0.44); C43: no bowl 20/20.**
  Split by the draft's agreement: agreed 4STEM bowl 13 / no 9; agreed 4TRI 2 / 2 (only 6 agreed 4TRI on the leaf).
- Pre-stated read-out: **"the codes mix"**. H231 agreement on shared rows 1-6 positions **22/24**.
What it means: in the secretary's hand on f.106r the readers did not keep the bowl sign under one code -- both 4TRI and 4STEM carry both shapes in
about equal parts, while C43 is only ever the no-bowl sign. Taken with H367 (f.61: 4TRI = bowl 5/6), H199/H230 (f.108v: 4STEM = bowl), H360 (f.124r:
4TRI 75% no-bowl) and H365 (f.101r: 4TRI 64% no-bowl), the readers' code for the bowl sign changes by leaf and session; a key cell built from pooled
4TRI or 4STEM counts mixes two signs unless it is re-split by shape (H218's point, now on six leaves). For VERIFY-F61-V11: the split PROPOSAL_v8_4tri.md
proposes is a shape split, and the shape answers per leaf are on disk for f.61, f.101r, f.106r, f.108v, f.124r, f.176r/v. No key, cell or grade
changed. 2 calls, cost estimate 2.0 USD.

## Campaign step H370 (29 Sept 2026, 17:27-17:30 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.97r's 4TRI also mixes the no-bowl sign: 29 of 49 answered (1 vision call)

`family/h370_bowl_97r.py`, key `family/h370_items.tsv`, prompt note H370 in `family/passes/PROMPTS_f176_f175.md` (H359's prompt verbatim), committed
before the call; the runner did not look at the sheets. fr.3982 f.97r (de Diou, HELD leaf with an order signal for v7) recut rows L17-L43 only (the
first cut was superseded); pools of agreed tokens with pass A matching: 4TRI 127, C43 39; sample 50 + 20 (seed 370), H359's geometry (the bands have
f.124r's up 70). Native canvas 202 refetched once (sha1 87d4236c as MANIFEST.tsv; 1 request). One blind Opus call, reply `family/passes/h370_reply.tsv`;
result `family/h370_bowl_97r_result.txt` (`--check` OK):
- **Control 19/20 PASS.**
- **4TRI: no bowl 29, bowl 20, n 1 (no-share 0.59); C43: no bowl 19, n 1 (1.00).** Pre-stated read-out: **"f.97r's 4TRI mixes the no-bowl sign: run
  H371 (full split + order gain)"**.
What it means: the readers' 4TRI on de Diou's f.97r is, like f.124r (H360, 0.75) and f.101r (H365, 0.64), more often the no-bowl sign than the bowl
sign; the leaf's 233-to-44 4TRI/C43 imbalance is the same code conflation. A transcription finding for the f.97r draft; nothing applied. 1 call, 1.5 USD.

## Campaign step H371 (29 Sept 2026, 17:31-17:36 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.97r: splitting 4TRI by bowl LOWERS v7's order gain (read-out "lowers"), with a caveat on one chunk (2 vision calls)

`family/h371_97r_4tri_split.py` (H360's scoring code with the leaf and H370's answers swapped in), key `family/h371_items.tsv`, prompt note H371,
committed before the calls; the runner did not look at the sheets. The other 77 agreed 4TRI of f.97r L17-L43 in two blind Opus calls (39 + 38),
H193's strips in each; replies `family/passes/h371_reply_c1.tsv`, `_c2.tsv`; result `family/h371_97r_4tri_split_result.txt`:
- **Gates c1 18/20, c2 18/20 -- PASS.** c1: no 23, yes 13, n 3; **c2: no 37, n 1, yes 0.**
- **All 127 agreed 4TRI of L17-L43 (H370 + H371): no bowl 89, bowl 33, n 5.** Split draft `passes/recf97r_split/` relabels the 89 as C43 (L01-L16 not
  bowl-read, left as transcribed).
- **Order gain (v7 unchanged): as transcribed 0.0566/0.0514/0.0509 -> split 0.0508/0.0455/0.0435, lower under all three seeds; H344 shuffled targets on
  the split 0/3.** Pre-stated read-out: **"lowers"**.
What it means, and the caveat: on de Diou's f.124r the same split doubled the order gain (H360); on f.97r it costs about 0.006 per seed. Taken at face
value, the no-bowl tokens under 4TRI on f.97r fit v7's c/p/t cell better than its a/n cell -- the opposite of f.124r and of f.101r's period gloss. But
chunk c2 answered 'no' to every item it could read (37/37), while c1 (0.64), H370 (0.59), H360 (0.77) and H365 (0.70) never did; a reader that passes
its part-1 anchors yet answers part 2 by default would look exactly like this, and the gate cannot see it (the anchors are all in part 1). So H371's
read-out stands as pre-stated but rests on one chunk whose answers are uncorroborated; H373 re-reads c2 in a fresh call before anything is made of it.
Also: only 127 of f.97r's 348 4TRI were split (L01-L16 and non-agreed tokens untouched), so this is a partial split. For VERIFY-F61-V10/V11; nothing
applied. 2 calls, cost estimate 2.0 USD.

## Campaign step H372 (29 Sept 2026, 17:36 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- one bowl-by-code table for the verifier (script-only)

`family/h372_bowl_code_table.py` -> `family/h372_bowl_code_table_result.txt` (`--check` OK): per leaf and readers' code, the bowl answers of every
gated H359-design call (only calls at >= 17/20 counted; a re-read token counts once, the later call's answer), with H194, H199/H218 and f.101r's
period-letter cross-tab carried verbatim. No-bowl share of the readers' 4TRI: **f.124r 0.77 (261), f.101r 0.70 (222), f.97r 0.73 (122), f.106r 0.47
(17), f.61 0.17 (6)**; f.106r 4STEM 0.56 (55); C43 no-bowl 0.95-1.00 on every leaf. f.106r's H231/H368 re-reads disagree on 2 of 24 tokens. The f.97r
rows include H371's c2 chunk, which H373 re-reads; the table regenerates from the replies on disk. Descriptive, for VERIFY-F61-V11; nothing applied.

## Campaign step H373 (29 Sept 2026, 17:39-17:42 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- H371's all-no chunk does not reproduce; replaced, and f.97r's split still lowers v7's order gain (1 vision call)

`family/h373_97r_c2_reread.py` (written and pushed before the call; `family/h373_97r_c2_reread_result.txt`, `--check` OK): the same c2 sheets, one fresh
blind Opus call, H359's prompt and H193's strips; reply `family/passes/h373_reply.tsv`. **Re-read gate 17/20 PASS (at the bar). Original c2: no 37, n 1,
yes 0; re-read: no 26, yes 12; agreement 25/37 = 0.68 < 0.85 -> pre-stated "c2 replaced".** Done as pre-stated: the original reply kept as
`passes/h371_reply_c2_orig.tsv`, the re-read copied to `passes/h371_reply_c2.tsv`, H371 rescored with its code unchanged (one fix: its `--check`
flag is now read before `gains()` resets `sys.argv`; the inherited h360_124r_4tri_split.py has the same reset, so its own `--check` rewrites rather
than checks -- noted for the verifier, not edited).
**H371 rescored:** 127 agreed 4TRI of f.97r L17-L43: no bowl 78, bowl 45, n 4 (0.63). **Order gain v7: as transcribed 0.0566/0.0514/0.0509 -> split
0.0541/0.0486/0.0471, lower under all three seeds; shuffled targets 0/3 -> "lowers" stands** (by about 0.003 instead of 0.006). H372's table
regenerated (f.97r 4TRI no-share 0.63).
What it means: (1) a part-1-only gate cannot catch a reader that answers part 2 by default; a chunk whose answers are all one value is re-read before
use (instrument lesson, H376). (2) On de Diou's f.97r the no-bowl 4TRI tokens do not fit v7's a/n cell better than its c/p/t cell under the order
statistic, unlike f.124r (H360, gain doubled) -- the shape split is supported by the period gloss on f.101r and by order on f.124r, but not by order on
f.97r. Whether that is the split or the statistic's resolution at this size of change is H374's question. For VERIFY-F61-V10/V11; nothing applied.
1 call, 1.5 USD.

## Campaign steps H374/H375 (29 Sept 2026, 17:44-17:48 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- the bowl split against random relabellings of equal count: beats all 20 on f.124r, 16 of 20 on f.97r (script-only)

`family/h374_split_randctl.py` (written and pushed before running; results `family/h374_split_randctl_f97r_result.txt`, `_f124r_result.txt`, `--check`
run): H358's random-variant control applied to the split itself. From the same bowl-read 4TRI pool, 20 random relabellings (seeds 374 / 375) of the
same number of tokens the shape split relabels, each scored with H360/H371's order gain for v7 (mean of seeds 342-344).
- **f.124r (H375): as transcribed 0.0335, shape split 0.0706; random relabellings of 202 mean 0.0493, max 0.0569 -> shape beats 20/20, pre-stated
  "carries order information".** Random relabelling alone raises the gain here (4TRI -> C43 helps in bulk), but choosing the tokens by the bowl
  answer raises it clearly more: the shape answers pick out the tokens that fit a/n.
- **f.97r (H374): as transcribed 0.0530, shape split 0.0499; random relabellings of 78 mean 0.0447, min 0.0376, max 0.0534 -> shape beats 16/20,
  "unclear".** On f.97r any relabelling costs order gain, and the shape split costs less than most random ones; the bowl answers point the right
  way but not past the 95% bar at this N (78 of 127).
What it means: H360's f.124r result is not a by-product of moving tokens out of 4TRI -- the shape answers carry order information beyond the count.
On f.97r the question stays open: the split neither helps v7 nor is it no better than random. (The as-transcribed and split figures here differ
slightly from H371's because this script averages the three seeds.) For VERIFY-F61-V10/V11; nothing applied. Script-only.

## Campaign step H378 (29 Sept 2026, 17:50-17:52 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.101r: the bowl split beats all 20 random relabellings too (script-only)

`family/h374_split_randctl.py f101r` (the f101r branch added and pushed with the row before its result was read; H362 + H365 answers, seed 378;
result `family/h374_split_randctl_f101r_result.txt`): **as transcribed 0.0823, shape split 0.1016; 20 random relabellings of 155 from the same 241-token
bowl-read pool mean 0.0938, max 0.0997 -> shape beats 20/20, pre-stated "carries order information".** With H375 (f.124r, 20/20) and H374 (f.97r, 16/20),
the bowl answers pick the tokens that fit v7's a/n cell better than chance on two de Diou leaves, one in-sample (f.101r, where the period gloss agrees,
H365) and one held (f.124r); f.97r points the same way below the bar. For VERIFY-F61-V11; nothing applied. Script-only.

## Campaign step H379 (29 Sept 2026, 17:50-17:52 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.108v (f.61's hand): relabelling the 4-family by bowl shape raises v7's order gain and beats every permuted-answer draft (script-only)

`family/h379_108v_shape_relabel.py` (written and pushed before running; result `family/h379_108v_shape_relabel_result.txt`). Corrected before running
(logged in the row): H199's columns index H59's draft `passes/f108v3z_draft_reconciled.tsv` (74/74), not rec108v (27/74). Shape draft: H199's 68
answered targets relabelled bowl -> 4TRI (v7 c/p/t), no bowl -> C43 (a/n), whatever the readers' code. Control: 20 drafts with the same 19 yes / 49 no
answers permuted across the same targets (seed 379).
- **Order gain v7 (mean of seeds 342-344): as transcribed 0.1568; shape-relabelled 0.2213; permuted-answer drafts mean 0.1331, max 0.1699 -> shape beats
  20/20, pre-stated "carries order information".**
What it means: in f.61's own hand (Mayenne's secretary on fr.3983 f.108v), reading the bowl sign as v7's c/p/t cell and the no-bowl sign as its a/n
cell -- regardless of which code the readers wrote (on f.108v they coded the bowl sign 4STEM, H199) -- makes the leaf's sign order fit French under v7
clearly better than the transcription or any placement of the same answers. This is the shape rule PROPOSAL_v8_4tri.md states, supported now by order
on a leaf in the target's hand, alongside f.124r and f.101r (H375/H378, 20/20). Caveat carried from the row: f.108v's order signal is thin (H353,
8 runs); the permuted control is the one this design can fail against, and it did not. For VERIFY-F61-V11; nothing applied. Script-only.

## Campaign step H377 (29 Sept 2026, 17:52-17:54 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- 64 more f.97r 4TRI, with known strips in part 2: the enlarged split clears the random-relabel bar, just (1 vision call)

`family/h377_97r_4tri_more.py`, key `family/h377_items.tsv`, prompt note H377, committed before the call; the runner did not look at the sheets. The
64 remaining pass-A 4TRI of f.97r L17-L43, plus **H376's fix: 6 known f.61 strips in part-2 format** (positions where H194 and H367 agree; 3 bowl, 3
no-bowl). One blind Opus call; reply `family/passes/h377_reply.tsv`; result `family/h377_97r_4tri_more_result.txt`:
- **Gate 1 (H193 anchors) 17/20 (at the bar); gate 2 (known part-2 strips) 6/6 -- PASS.** The part-2 gate works as intended on its first use.
- **The 64: bowl 17, no bowl 35, n 12 (no-share 0.67).**
- **Enlarged split** (H370 + H371 after H373 + H377; relabelled only where the draft has 4TRI at that position): pool 148, relabelled 86. **Order gain v7
  (mean of 3 seeds): as transcribed 0.0530, shape split 0.0515; 20 random relabellings of 86 mean 0.0414, max 0.0515 -> shape beats 20/20, pre-stated
  "carries order information"** -- by a margin at the fourth decimal over the random maximum, so this is at the bar, not clear of it.
What it means: with more tokens the f.97r shape split separates from random relabelling as it does on f.124r, f.101r and f.108v, though narrowly; on
f.97r any move of tokens out of 4TRI still costs a little gain against the transcription (0.0530 -> 0.0515), so the no-bowl tokens there fit a/n only
about as well as c/p/t. Only 21 of the 64 new tokens sit on a draft 4TRI position (the rest are reconciler disagreements), which caps what more reads
can add on this leaf. For VERIFY-F61-V11; nothing applied. 1 call, cost estimate 2.0 USD.

## Campaign steps H381/H382 (29 Sept 2026, 17:54-17:56 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- bowl answer vs known letter on four leaves, and the V9 page (script-only, notes)

**H381** (`family/h381_shape_letter_pool.py`, `family/h381_shape_letter_pool_result.txt`, `--check` OK; results already on disk, no new reading):
agreement = (bowl & c/p) + (no bowl & a/n) over tokens whose letter is c/p(/t) or a/n.
| leaf, letters | bowl&c/p | bowl&a/n | no&c/p | no&a/n | n | agreement |
|---|---|---|---|---|---|---|
| f.101r period gloss (H365; c/p/t) | 33 | 19 | 12 | 118 | 182 | 0.83 |
| f.108r period overlay (H202; c/p), f.61's hand | 3 | 0 | 2 | 11 | 16 | 0.88 |
| f.176r period decipherment (H193; c/p) | 5 | 0 | 4 | 23 | 32 | 0.88 |
| f.61 Tomokiyo's published spans (H367; c/p) | 4 | 0 | 1 | 9 | 14 | 0.93 |
| pooled | 45 | 19 | 19 | 161 | 244 | 0.84 |
Per-leaf spread 0.83-0.93 over four leaves; f.101r carries 75% of the pooled tokens, so the pooled figure is mostly f.101r's (rule 3). The error runs
both ways (bowl read with a/n 19; no bowl read with c/p 19), about one token in six. Letters are period decipherments on three leaves and Tomokiyo's
published spans on f.61 (published, not ours).
**H382:** `family/V9_PAGE.md` runner-14 section extended with H374-H381.
What it means for VERIFY-F61-V11: the shape rule PROPOSAL_v8_4tri.md states (bowl -> c/p, no bowl -> a/n) matches the known letter about five times
in six on every leaf with letters, in three hands (de Diou, Desportes, Mayenne's secretary), and separately beats random relabellings under the order
statistic on f.124r, f.101r, f.108v (20/20 each) and f.97r (at the bar). Nothing applied; the ruling is the verifier's.

## Campaign step H380 (29 Sept 2026, 17:56-17:58 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.106r (the secretary's hand): relabelling by bowl shape more than doubles v7's order gain and beats every permuted-answer draft (script-only)

`family/h380_106r_shape_relabel.py` (written and pushed before running; `family/h380_106r_shape_relabel_result.txt`, `--check` OK): H379's design on
f.106r rows 1-18 with the H231/H368 answers (H368 wins on re-reads), used only where the pooled draft `passes/recf106rall18` carries pass A's code at
the same (line, position): 75 tokens (bowl 28, no bowl 47). **Order gain v7 (mean of seeds 342-344): as transcribed 0.0261, shape-relabelled 0.0604;
20 permuted-answer drafts mean 0.0371, max 0.0513 -> shape beats 20/20, pre-stated "carries order information".**
What it means: on the held leaf where v7 showed no order signal as transcribed (H342/H346/H348, underpowered at 51 runs, H351), reading the bowl sign
as c/p/t and the no-bowl sign as a/n -- whichever of 4TRI/4STEM the readers wrote, since in this hand both codes carry both shapes (H368) -- more than
doubles the gain and beats every placement of the same answers. Permuted drafts also gain on average (0.026 -> 0.037: moving tokens between the two
cells helps in bulk), so the comparison that counts is shape vs permuted, which it clears. This does not reverse H351's power finding for the
as-transcribed test; it says the shape-corrected draft fits v7 by a margin the as-transcribed draft did not. With H379 (f.108v), the shape rule now has
order support in both of the target's own hands (Mayenne's secretary on f.106r and f.108v). For VERIFY-F61-V10/V11; nothing applied. Script-only.

## Campaign step H383 (29 Sept 2026, 17:59-18:01 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- the shuffled-target arm for H379/H380: clean on both shape drafts (script-only)

`family/h383_shape_shuftarget.py` (written and pushed before running; `family/h383_shape_shuftarget_result.txt`, `--check` OK): H344's code unchanged
on the two shape-relabelled drafts, now on disk for the verifier (`passes/rec108v_shape/`, `passes/recf106r_shape/`, 75 tokens relabelled, built as
H379/H380 built them). **rec108v_shape: order signal on 0/3 shuffled targets (gain/p95 0.021/0.053, -0.002/0.045, 0.020/0.044); recf106r_shape: 0/3
(0.019/0.025, 0.040/0.042, -0.027/0.035)** -> pre-stated: **H379's and H380's read-outs stand.** One f.106r shuffle sits close under its p95
(0.040 vs 0.042), so f.106r's margin against this arm is thin. For VERIFY-F61-V10/V11; nothing applied. Script-only.

## Campaign step H384 (29 Sept 2026, 18:01-18:02 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.61's exposure to the 4TRI split: one position, against Tomokiyo's letter (script-only)

`family/h384_shape_at_f61.py` -> `family/h384_shape_at_f61_result.txt` (`--check` OK): the 18 f.61 4-family tokens with code, v7's cell, H367's bowl
answer, the cell under the shape rule, and Tomokiyo's letter where H194's span alignment gives one.
- **Within PROPOSAL_v8_4tri.md's scope (4TRI only): 1 of 6 would change -- L05/14, c/p/t -> a/n, where Tomokiyo prints c** (and H194 read bowl). So the
  proposal, applied to f.61 on H367's answers, would move the one position where our shape read and the published letter disagree; the other five
  4TRI keep c/p/t, and four of them carry Tomokiyo's c or p.
- **Beyond the proposal's scope** (shown as exposure only; the proposal does not cover these codes): L01/12 4PI d/q, L11/8 4STEM a/c/e/n, L11/9 4PI
  d/q would read a/n under a no-bowl rule stretched to them. **L11/9 is a 4PI where Tomokiyo prints n and v7's cell is d/q** -- a disagreement between
  v7 and the published letter on the target, independent of the bowl question, for the verifier.
What it means for VERIFY-F61-V11: on the target leaf the 4TRI split is nearly neutral (one token, and there the published letter argues for the
transcription as it stands); the proposal's weight lies on the sister leaves and on key building, not on f.61's own tokens. Nothing applied.

## Campaign step H385 (29 Sept 2026, 18:02-18:05 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.106r's remaining C43 are all the no-bowl sign; the completed shape draft keeps H380's result (1 vision call)

`family/h385_106r_c43_bowl.py`, key `family/h385_items.tsv`, prompt note H385, committed before the call; the runner did not look at the sheets. Pass A
codes no 4PI on f.106r (noted in the row before running), so the targets were its 36 C43 not yet read by H231/H368, plus H377's 6 known f.61 strips.
One blind Opus call; reply `family/passes/h385_reply.tsv`; result `family/h385_106r_c43_bowl_result.txt`:
- **Gate 1 19/20, gate 2 6/6 -- PASS.** The reader answered 'yes' to exactly the three known bowl strips and 'no' to everything else: the one-value
  answer on the targets is not a default, because the same reader told the known bowl strips apart in the same part 2 (H376's fix doing its job).
- **C43: no bowl 34, n 2, bowl 0 (1.00).**
- **Completed draft (H231 + H368 + H385): 99 usable tokens (bowl 28, no 71); order gain v7 as transcribed 0.0261, shape 0.0604 (unchanged -- C43 read
  no-bowl stays C43); 20 permuted drafts mean 0.0358, max 0.0511 -> shape beats 20/20, "carries order information".**
What it means: in the secretary's hand the C43 code is always the no-bowl sign (54 of 54 answered, H368 + H385), so the two-sign problem on f.106r
sits entirely inside 4TRI and 4STEM (H368). For VERIFY-F61-V11; nothing applied. 1 call, cost estimate 1.5 USD.

### Correction to H384 (29 Sept 2026, 18:06 UTC by date -u, runner 14)

H384's first version compared the shape rule with key v7's POOLED cells only. Key v7 also carries an f.61 reading key (`load_key_v7(f61=True)`, with
F61TOK for the 4-over-Pi): 4TRI c/p, 4STEM a/n, L11/9 4PIPI a/n (grade M from Tomokiyo's S5), L01/12 unread. Rerun with that column added
(`family/h384_shape_at_f61_result.txt`, `--check` OK): **within the proposal's scope only L05/14 changes (c/p -> a/n, Tomokiyo c), as before; beyond it
only L01/12 (held unread) would take a/n.** The two other "beyond scope" flags (L11/8 4STEM, L11/9 4PI) are already a/n in the f.61 reading key, and
the sentence above that L11/9 is "a disagreement between v7 and the published letter" is **withdrawn**: v7's f.61 reading key already reads it n's
cell a/n from Tomokiyo's S5 (build_key_v7.py point 3). The ROOM line of 18:03 carried the same error and is corrected there.

## Campaign step H386 (29 Sept 2026, 18:06-18:07 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- 4STEM by shape: on f.101r it splits like 4TRI, at small n (script-only)

`family/h386_4stem_by_shape.py` -> `family/h386_4stem_by_shape_result.txt` (`--check` OK). v7's 4STEM cell is a/c/e/n pooled, a/n in the f.61 reading key.
On f.101r (H207, the only 4STEM answers with letters): **4STEM bowl&c/p 4, bowl&a/n 2, no&c/p 3, no&a/n 8 -> agreement 0.71 (n 17)**, beside 4TRI
in the same call 0.74 (n 19) -- the same direction at the same strength, both too small alone. f.108v's 4STEM is mostly the bowl sign (19/2, H199);
f.106r's is mixed (24/31, H368); neither has letters. Pointer for V11: if the verifier adopts the 4TRI split by shape, 4STEM looks like the same two
signs under another code (the pooled a/c/e/n cell reads as a c/p half plus an a/n half), so a shape rule written for the sign rather than for the code
would cover both. H387 (f.101r's full 4STEM bowl read against the period gloss) is the test. Nothing applied. Script-only.

## Campaign step H387 (29 Sept 2026, 18:07-18:10 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.101r's 4STEM: the bowl tracks the period letter where the letter is c/p or a/n, but relabelling by shape adds nothing to the order gain at 25 tokens (1 vision call)

`family/h387_101r_4stem_bowl.py`, key `family/h387_items.tsv`, prompt note H387, committed before the call; the runner did not look at the sheets.
Targets: f.101r's 25 draft 4STEM with agreement and pass A matching (fewer than the 46 agreed, since pass A's position must carry 4STEM too), plus
H377's 6 known strips. Native canvas 210 refetched once (sha1 313f92b3; 1 request). One blind Opus call; reply `family/passes/h387_reply.tsv`;
result `family/h387_101r_4stem_bowl_result.txt`:
- **Gate 1 18/20, gate 2 6/6 -- PASS.** 4STEM: bowl 9, no bowl 16.
- **Period letter by bowl: bowl -> c/p/t 6, other 3; no bowl -> a/n 4, c/p/t 1, other 9, none 2. Agreement over tokens with a c/p/t or a/n letter
  10/11 = 0.91 -> pre-stated "tracks"** -- but only 11 of 25 tokens carry such a letter; 12 carry another letter (4STEM's pooled v7 cell a/c/e/n
  includes e), so the rule covers under half of f.101r's 4STEM.
- **Order gain (4STEM relabelled bowl -> 4TRI, no -> C43, 25 tokens): as transcribed 0.0823, shape 0.0827; 20 permuted drafts mean 0.0835, max 0.0853
  -> shape beats 6/20, pre-stated "no better than random".** At 25 tokens on a leaf of about 2,400 signs the change is small; the order statistic's
  power for so few relabelled tokens was not measured, so this is a pre-stated miss of unknown power, not a refutation.
What it means for V11: the 4STEM code on f.101r behaves partly like 4TRI (where its period letter is c/p or a/n, the bowl predicts it, 10/11) and
partly not (half its tokens carry other letters, and the shape relabel does not move the order gain). A shape clause for 4STEM is not supported by
this leaf beyond the letter cross-tab; PROPOSAL_v8_4tri.md's 4TRI-only scope looks right. Nothing applied. 1 call, cost estimate 1.5 USD.

## VERIFY-F61-V10's six items, recorded by runner 14 (29 Sept 2026, 18:13 UTC by date -u, session_01N7YQoVMZj1SfiFvc4XG9DH)

AUDIT.md "What runner 13 (or its successor) should record", carried into HYPOTHESES.md (rows H338-H341, H342/H344, H353, H349) and here:
1. H341's void covers the binned beam arm on every leaf, f.97r and recf108vg included -- not evidence either way.
2. H342/H344: endorsed on f.97r and f.124r by V10's independent instrument; f.124r's margin on the unsplit draft is thin there (3/100), clear on the split.
3. H353: f.108v is "a lean, instrument-dependent at 8 runs", not "a thin order signal". This also bounds H379: H379's shape-vs-permuted comparison
   is a within-leaf comparison on the runner's instrument, and the leaf's own order signal for v7 is only a lean.
4. H349/H355: quote HASH4 d/q and C43 a/n only; H24's f.97r pass and ZBAR's leaf do not replicate.
5. Named limit: the H146 pool behind VBAR_A included f.97r and f.124r (contamination); V10's control (e) shows the signal survives VBAR_A = s/t.
6. H358: f.188r specificity -- the a/n widening LOWERS the gain on a clean-4TRI leaf.
VERIFY-F61-V11 (17:30) ruled on PROPOSAL_v8_4tri.md before runner 14's H368-H387 landed: 4TRI_NB (a token read no-bowl in a gated blind read) = a/n
(grade C on f.101r, M where shape only); the bowl class not narrowed (stays v7 4TRI); L05/14 stays c/p M. Runner 14's later rows (H370-H387, all in
HYPOTHESES.md) are further evidence for the VO3 lane, not a change to that ruling.

## Campaign step H391 (29 Sept 2026, 18:13-18:14 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- the bowl reader's repeatability from re-reads on disk (script-only)

`family/h391_bowl_reader_agreement.py` -> `family/h391_bowl_reader_agreement_result.txt` (`--check` OK). Cohen's kappa on yes/no, items answered both times:
- **H194 vs H367 (f.61, 15): agreement 0.93, kappa 0.84. H231 vs H368 (f.106r, 24): 0.92, kappa 0.81.** Target tokens re-read in a second call agree well.
- **H371 c2 original vs H373 (f.97r, 37): 0.68, kappa 0.00** -- the all-'no' chunk carries no information about the re-read (H373 replaced it).
- **H193's 60 anchor strips across 21 H359-design calls (210 pairs): mean agreement 0.98, mean kappa 0.94 (min 0.80); every call agrees with the
  per-strip majority at 0.95-1.00 -- including H371 c2's original call (1.00).**
What it means: (1) the reader is repeatable on the same strips (0.8-0.94) when it is reading; V11's inter-reader kappa of 0.35-0.49 was measured on a
different set (V11's own readers and tokens, AUDIT.md VERIFY-F61-V11), so the two are not in conflict but are not the same measurement -- for the VO3
lane. (2) Gate 1 is passed near-perfectly by every call, the defective one included: it tests the reader's eye on part 1 and says nothing about part 2.
The H376 fix (known strips inside part 2, gate 2) is the gate that can fail; it passed 6/6 in H377, H385 and H387. Instrument lesson, added to
CAMPAIGN.md INSTRUMENTS. Nothing applied. Script-only.

## Campaign step H390 (29 Sept 2026, 18:14-18:17 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- the gated bowl reader repeats its f.124r answers at kappa 0.88 (1 vision call)

`family/h390_bowl_kappa_gated.py`, key `family/h390_items.tsv`, prompt note H390, committed before the call; the runner did not look at the sheets. 50
f.124r 4TRI already answered by H359/H360 (stratified: 25 originally yes, 25 no; seed 390), re-cut at H359's geometry from native f256 (sha1 8b7e91c7,
1 request), plus H377's 6 known strips; one fresh blind Opus call; reply `family/passes/h390_reply.tsv`; result `family/h390_bowl_kappa_gated_result.txt`
(`--check` OK). **Gate 1 19/20, gate 2 6/6. Answered both times 48: original yes -> yes 22 / no 2; original no -> yes 1 / no 23. Agreement 0.94,
kappa 0.88 -> pre-stated "the gated reader is repeatable at this design".** With H391 (re-reads on f.61 0.84, f.106r 0.81), the bowl answers the
runner's split rests on repeat at 0.8-0.9 kappa in this design; VERIFY-F61-V11's inter-reader 0.35-0.49 (its own readers and design) is a different
measurement, for the VO3 lane to weigh. Nothing applied. 1 call, cost estimate 1.5 USD.

## Campaign step H392 (29 Sept 2026, 18:17-18:22 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.188r (Desportes): the readers' 4TRI is mostly the bowl sign, 0.73 -- "unclear" by the pre-stated bands (1 vision call)

`family/h392_bowl_188r.py`, key `family/h392_items.tsv`, prompt note H392, committed before the call; the runner did not look at the sheets. Changed
before running (logged in the row): f.188r's draft has no agreed C43, so all 66 agreed 4TRI were read and the no-bowl check rests on gate 2 alone.
Native f351 refetched once (sha1 1c584b0f as MANIFEST.tsv; 1 request). One blind Opus call; reply `family/passes/h392_reply.tsv`; result
`family/h392_bowl_188r_result.txt` (`--check` OK). **Gate 1 17/20 (at the bar), gate 2 6/6. f.188r 4TRI: bowl 48, no bowl 18 -> yes-share 0.73,
pre-stated "unclear"** (bands: >= 0.8 bowl sign, no-share >= 0.4 mixes).
What it means for VERIFY-F61-V10 item 6: f.188r's 4TRI is mostly the bowl sign (0.73), where de Diou's leaves are mostly the no-bowl sign (bowl share
0.23-0.37 on f.124r, f.101r, f.97r) -- so widening every 4TRI to a/n lowers the gain on f.188r because most of its 4TRI are c/p, as the shape rule
would predict; but a quarter read no-bowl, so f.188r is not clean either, and the pre-stated read-out does not decide it. A follow-up, if wanted:
split f.188r's 18 no-bowl tokens and test the order gain against random relabellings of 18 (H374's design, script-only). Nothing applied. 1 call,
cost estimate 1.5 USD.

## Campaign step H393 (29 Sept 2026, 18:17-18:23 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- --check sweep of runner 14's scripts (script-only)

`family/h393_check_sweep.sh` -> `family/h393_check_sweep_result.txt`: 20 checks (h367-h391, h374 on three leaves). **19 OK; h391 STALE** because its
glob of reply files took in H390's and H392's replies written after it ran; the script is now pinned to the 21 calls (h359-h387) it reported and
rechecks OK (the figures in "Campaign step H391" are unchanged). Disclosure: H395's script was started a minute before its commit (pushed with this
section, before its result was read).

## Campaign step H395 (29 Sept 2026, 18:22-18:24 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.188r: its minority no-bowl 4TRI behave as the a/n sign too (script-only)

`family/h395_188r_split_randctl.py` (started a minute before its commit, disclosed in H393; `family/h395_188r_split_randctl_result.txt`, `--check`
OK; split draft `passes/recf188r_split/`): H392's 18 no-bowl 4TRI of f.188r relabelled C43. **Order gain v7 (mean of seeds 342-344): as transcribed
0.1887, shape split 0.1975; 20 random relabellings of 18 from the same 66: mean 0.1792, max 0.1938 -> shape beats 20/20, pre-stated "carries order
information".**
What it means, with VERIFY-F61-V10 item 6: widening EVERY f.188r 4TRI to a/n lowers the gain (V10), because 48 of its 66 are the bowl (c/p) sign
(H392); relabelling only the 18 the gated reader called no-bowl RAISES it, and beats random choices of 18. So V10's specificity result and the shape
rule agree: the rule is token-level, not code-level, on Desportes's hand as on de Diou's and the secretary's. For LANE VO3; nothing applied. Script-only.

## Campaign step H397 (29 Sept 2026, 18:24-18:27 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- a second instrument: VERIFY-F61-V10's order statistic confirms every shape split, 20/20 on all six leaves (script-only)

`family/h397_shape_v10instrument.py` (written and pushed before running; `family/h397_shape_v10instrument_result.txt`, `--check` OK) imports V10's
own statistic (`verify_v10/order_v10.py`: its letter model, exact Viterbi, its within-run shuffles, seed 10010) -- no scoring code shared with the
runner's -- and scores v7 on each leaf's as-transcribed draft, its shape draft and 20 fresh controls in the runner's design (seed 397+i). One fix
after the first run, disclosed: the f.106r arm had added H385's answers without the draft-match rule (109 tokens instead of 99); with the rule it
gives 99 as H385, and the read-out is unchanged.
| leaf (design) | V10 gain as transcribed | shape | 20 controls mean / max | beats |
|---|---|---|---|---|
| f.124r (relabel 202 of 261) | 0.0300 | 0.0484 | 0.0380 / 0.0410 | 20/20 |
| f.101r (relabel 155 of 222, in-sample) | 0.0449 | 0.0551 | 0.0480 / 0.0514 | 20/20 |
| f.97r (relabel 86 of 138) | 0.0295 | 0.0343 | 0.0286 / 0.0316 | 20/20 |
| f.188r (relabel 18 of 66, in-sample) | 0.0957 | 0.1026 | 0.0915 / 0.0985 | 20/20 |
| f.108v (permuted answers, 68; f.61's hand) | 0.1038 | 0.1358 | 0.0832 / 0.1021 | 20/20 |
| f.106r (permuted answers, 99; f.61's hand) | 0.0368 | 0.0548 | 0.0367 / 0.0506 | 20/20 |
Pre-stated read-out on every leaf: **"carries order information (second instrument)"**. Under V10's statistic the f.97r split also RAISES the gain
over the transcription (0.0295 -> 0.0343), where the runner's instrument showed a small loss (H371/H377) -- the f.97r direction was
instrument-dependent, the shape-vs-random comparison is not. For LANE VO3; nothing applied. Script-only.

## Campaign step H396 (29 Sept 2026, 18:28-18:30 UTC by date -u, runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH) -- f.61 L05/14 tie-break: the bowl sign, 3-0 (1 vision call)

`family/h396_l05_14_tiebreak.py`, key `family/h396_items.tsv`, prompt note H396, committed before the call. L05/14 cut at three windows (H367's, H359's,
wider) among the other 17 f.61 4-family tiles; one fresh blind Opus call; reply `family/passes/h396_reply.tsv`; result
`family/h396_l05_14_tiebreak_result.txt` (`--check` OK). **Gate 1 18/20, gate 2 (the 6 known f.61 strips) 6/6. L05/14: W1 yes, W2 yes, W3 yes ->
pre-stated tie-break "bowl (3-0)"**, with H194 and Tomokiyo's c; H367's 'no' there (at W1's own window) does not reproduce. The other 9 non-known
f.61 tiles agree with H367 9/9.
What it means: f.61's 4TRI is the bowl sign 6 of 6 (H367 + H396), and PROPOSAL_v8_4tri.md / V11's 4TRI_NB class would move **no** f.61 position; the
V11 note "L05/14 stays c/p M (H194 bowl vs H367 no-bowl conflict)" now has a third read on the bowl side. H384's result (one in-scope change, L05/14)
is superseded by this read for the record; its script is left as it was run. For LANE VO3; no grade or key changed. 1 call, cost estimate 1.5 USD.

## Campaign steps H389 and H400 (29 Sept 2026, 18:4x-18:44 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- key v8 exists (F61-FAMILY-13); the v8 meter and spans are already on file (script-only, no new run)

H389 (build key v8) was done by F61-FAMILY-13 (18:25, commit 921e9ebb; `family/build_key_v8.py`, `family/key_period_v8.tsv`, family/KEY.md
"key v8"), on the orchestrator's go; the runner does not rebuild it. Re-checked here: `family/build_key_v8.py --check` OK and
`verify_v11/meter_v11.py --check` OK at 18:44. H400 asked for the f.61 meter and the five-span reproduction under v8 with f.61's 4TRI read as the bowl
sign 6/6 (H367 + H396): that is exactly FAMILY-13's "key v8 as merged (six f.61 4TRI c/p)" line in `family/build_key_v8_result.txt` -- **meter firm
12 / two-way 59 / wider 2 / unread-or-null 26 of 99; spans 53/55 (2000 permuted keys p95 0.418, 0/2000 at or above); f.108r overlay 74/84 (p95 0.405,
0/2000)**. So key v8 moves no f.61 band, as H396 predicted. One record point for the verifier lane, no grade changed: L05/14 now has four gated reads,
bowl 3 of them at three windows (H194, H396 x3 in one call) against H367's one no-bowl; V11's "stays c/p M until a third read" has its third read on
the bowl side. The grade move (M -> S) is the verifier's.

## Campaign step H398 (29 Sept 2026, 18:46-18:53 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- V11's own f.101r bowl tiles under the runner's prompt and gates: the new read sides with the runner, and tracks the period letter best (1 vision call)

`family/h398_bowl_design.py`, key `family/h398_items.tsv`, prompt note H398 in `family/passes/PROMPTS_f176_f175.md`, committed before the call (49c5e5f7's
parent). VERIFY-F61-V11's 80 f.101r target tokens (c1, c2, c4, c5, first occurrences) re-cut in V11's OWN tile format (v11_bowl.tile; the one change:
the marker drawn red instead of blue, so H359's wording is true), plus H377's 6 known f.61 strips in the same format at H367's window; H193's 60
strips as part 1. Natives fetched once each (3 Gallica requests, requests.log): f327 sha1 115f9923 (a2b0d98e on record -- a server re-encode;
h193_items.tsv regenerated byte-identical), f328 4a13be67, f210 313f92b3. One blind Opus call (H359's prompt verbatim), reply
`family/passes/h398_reply.tsv`; result `family/h398_bowl_design_result.txt` (`--check` OK). The runner did not look at the sheets.
- **Gate 1 18/20, gate 2 6/6.** Targets: no 47, yes 23, n 10.
- **new vs runner kappa 0.68 (agreement 0.85, n 66); new vs V11 kappa 0.56 (0.77, 66); runner vs V11 on the same tokens 0.44 (0.71, 70).**
  Pre-stated read-out: **"the disagreement is V11's design (prompt/anchors)"** -- the new read used V11's tiles, so the part that differs is V11's
  prompt and anchor set, not its tiles. The V11 kappa (0.56) sits just under the 0.6 bar: the new read sits between the two labellers, nearer the runner.
- Known answer (period letter, V11's own crosstab functions, same tokens, bowl -> c/p/t vs no -> a/n): **new 0.905 (n 63; P(a/n|yes) 0.10), runner
  0.809 (68; 0.31), V11 0.687 (67; 0.47)**, all perm p < 0.001; new and runner "tracks", V11 "unclear". So V11's tiles carry the letter split at least
  as well as the runner's own tiles when read under the runner's prompt and gates. The V11 labels' weaker tracking comes from how they were asked
  (prompt, 10 Desportes anchors, no known part-2 strips), not from what the tiles show.
What it means for LANE VO3: V11's "bowl = c/p/t is not a narrowed cell (the bowl class still holds a/n: V11 up to 9/11)" rests on V11's labels. On
these same 80 tokens a gated read gives P(a/n | bowl) 0.10 (2 of 21). That does not change key v8 (V11 kept the bowl 4TRI at c/p/t), but it is
evidence for a narrower bowl cell (c/p/t without a/n), for a verifier to weigh. No key, cell or grade changed. 1 call, cost estimate 1.5 USD.

## Campaign step H399 (29 Sept 2026, 18:56-18:59 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- f.97r L01-L16 bowl-read: 49 of 54 no-bowl; the completed f.97r split still beats 20/20 on V10's instrument (1 vision call)

`family/h399_97r_firstcut.py`, key `family/h399_items.tsv`, prompt note H399, committed before the call (132e5c6c's parent). The 65 agreed draft 4TRI of
f.97r L01-L16 (first cut: the draft renumbers positions, so each draft token was mapped to pass A's row by a per-line sequence alignment, 149/149 draft
4TRI mapped) cut at H359's geometry from native f202 (sha1 87d4236c, 1 request), plus H377's 6 known f.61 strips; H193's strips as part 1. Disclosed:
the runner looked at sheet 01 for marker placement -- markers on or beside the 4-sign, some about 25 native px off; x moved to the mean of pass A and B
where both read the sign (few tiles changed). One blind Opus call, reply `family/passes/h399_reply.tsv`; result `family/h399_97r_firstcut_result.txt`
(`--check` OK).
- **Gate 1 18/20, gate 2 6/6** (the 3 known yes strips answered yes, so this is not H371 c2's one-value defect, though the chunk is no-heavy).
- **L01-L16: bowl 5, no bowl 49, n 11 (no-share 0.91)** -- de Diou's f.97r 4TRI is mostly the no-bowl (a/n) sign here too (L17-L43: 0.64-0.73).
- **Second instrument (V10's order statistic via h397's f.97r arm, the same control seed as H397, 397+2), completed draft L01-L43: pool 192, relabelled 135; gain
  as transcribed 0.0295 -> shape 0.0368; 20 random relabellings of 135 mean 0.0299, max 0.0326 -> beats 20/20, "carries order information (second
  instrument)"** (H397 on L17-L43 alone: 0.0343 vs max 0.0316, 20/20). The margin over the controls' max widens (0.0027 -> 0.0042) with the 54 added.
What it means: f.97r's split, now bowl-read over the whole leaf, holds on the independent instrument with a wider margin; family-level support for key
v8's 4TRI_NB class on a third de Diou leaf (V11 audited only f.101r and f.124r; runner reads of f.97r are not in v8). No f.61 position is touched
(H396). For LANE VO3; no key change. 1 call, cost estimate 2.5 USD.
(Script fix after the run, disclosed: `--check` was lost because h397.leaves() rewrites sys.argv; CHECK is now read at import; result file unchanged, `--check` OK.)

## Campaign step H401 (29 Sept 2026, 19:08-19:04 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- e vs r under PHI in f.61's own hand: no attribute visible (the runner's look; H402 dropped)

Why this was worth a step: of f.61's 59 two-way tokens, only the e/r (PHI 17) and a/n (C43 9, 4STEM 1, 4PI 1) cells are pairs the published table
draws as TWO symbols (keys/key_mayenne_1592.tsv); every other pair (b/o, c/p, d/q, g/t, h/u, i/x, l/y, m/z) is one shared symbol by design, so no
shape test can narrow it -- only a reading can. The free sort that failed on e/r (H71) is a retired instrument; this used H193's design.
`family/h401_er_attr.py` (committed before the look, e7327bb0's parent): the 20 f.108r PHI tokens paired with a period overlay letter (h202's alignment:
e 13, r 7; f.61's hand), cut as H202, shown as two group sheets. The runner looked at those two sheets only and wrote `family/h401_attribute.txt`:
**none visible** -- both groups are the same trefoil / stacked double loop on a slanted stem, with the same variants in each (three-loop heads r1-r3 as
e1-e5; two stacked loops with a small left stroke at the junction r4-r7 as e7-e12). Per the pre-stated rule **H402 is dropped** (no call spent).
What it means: a second, different look (after H71's free sort) finds no e/r sub-form in f.61's hand; the table's two drawings are Tomokiyo's
composite of other hands. **PHI e/r stays two-way on f.61 by design**: its 17 tokens (11 of Tomokiyo's 13 lettered ones are e) can narrow only by a
reading with a control, not by shape. The same argument limits the a/n cell (H403 dropped with H402: the design did not open on this hand, and H73/H24b
already failed on the 43 glyph). So the meter's two-way band on f.61 is at its shape floor apart from the 4-family splits already made. Cost ~0.1.

## Campaign step H404 (29 Sept 2026, 19:07-19:12 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- key hunt: all 119 BnF hits read; one Mayenne-chancery lead (fr.3980 f.10), not f.61's design

Campaign rule (a), new material without a person. BnF Archives et manuscrits (plain POST `resultatRechercheSimple.html`, cookie jar, descriptive UA,
>= 2 s apart): the POST response for H143's query "Mayenne chiffre déchiffrement" now carries **all 119 hits on one page** (H143 read 50; the
`nbResultParPage=100` GET returns "Aucun résultat", as the host table warns), and four spelling variants were added: "duc du Maine chiffre
déchiffrement" (1: fr.3641 no.71, known), "Mayenne déchiffré" (2), "du Mayne chiffre" (11), "Maienne chiffre" (1: fr.2751, known). Parsed
(scratch): of the 119, 21 name Mayenne/Maine/Diou/Lorraine; every one is already on file (the fr.3982-3984 family leaves; fr.3641 nos.21/59/68/71,
figure ciphers; fr.2751 f.116, a clear copy, H144; fr.4699 ff.37/41, not digitised; fr.4715's 1585-86 Mayenne-to-Nevers letters, an earlier
cipher, NOTES "the finding aids") **except one: Français 3980, fol. 10 (item 6, ark:/12148/cc504266/cd0e10351), "Lettre, avec chiffre et
déchiffrement, de CHARLES DE LORRAINE [duc DE MAYENNE]... à monsieur l'evesque de Plaisance [Filippo Sega, the legate]... De Soissons, le XIme
jour de janvier 1591"** (item 7 begins at fol. 15). It is digitised (Gallica SRU: btv1b90605458, 682 canvases, no folio labels): by eye on 500-px
thumbnails, canvas 17 = the Provins capitulation (item 5, fol. 9), **canvas 19 = fol. 10r, cipher runs after two clear lines; canvas 21 = a
clear page ("que l'on evitast l'effort du Roy de Navarre ...", the decipherment or the letter's clear part); canvas 23 = fol. 13, a full cipher
page**. One 2000-px look at canvas 23: the signs are **Arabic figures (5, 4, 6, 3, 0, 1, 9) mixed with symbols (phi, delta, a lemniscate,
hash, triangles, v)** -- a larger inventory than the polyphonic family's ~21 kinds on f.61 and with figures (0, 1, 3, 5, 9) that none of the
family's classes contain. Tomokiyo (sources/cryptiana/web/league.htm, "BnF fr.3980") treats "another cipher used in letters between the Duke of
Mayenne and Sega in the same month" as a separate cipher, reconstructed in his Cryptologia article (doi 10.1080/01611194.2017.1370038), and his
mayenne.htm family list does not include fr.3980. **So: a lead, most likely not f.61's key family (the specialist's own classification plus the
runner's look; no controlled design check was run).** Settling it would take a design check with known answers (f.61-family tiles vs fr.3980
tiles, H310's forced-choice format); not worth a call while the specialist's classification stands. Nothing else in the 119 is new.
Other Mayenne-side items found for the record (not leads for this key): fr.3980 nos.21-22 (Mayenne to Sega, 19 Jan, no cipher in the aid),
fr.3977 no.47 (news of Mayenne, 1589, to Maumarché), fr.3632 no.64 (Picardie, Nevers papers). Requests: archivesetmanuscrits 12 (home, 5 POST,
5 GET, 1 item page), Gallica 7 (SRU 1, manifest 1, thumbnails 4, one 2000-px canvas 1); `family/requests.log`. Images in scratch only (sha1 in
the log). No key, no reading. Cost ~0.6.

## Campaign steps H405 and H406 (29 Sept 2026, 19:18-19:13 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- the meter's floor table; the VO3 packet (script and notes only)

`family/h405_meter_floor.py` -> `family/F61_FLOOR.md` (`--check` OK). **Of f.61's 59 two-way tokens under key v8, 27 are in letter pairs the published table draws as one shared symbol (b/o, c/p, g/t, l/y, i/x, d/q) -- polyphony by design, which no shape test can narrow; 4 carry a fitted set that is not a table column (BETA m/s 2, LOOPSTEM1 q/s 1, CH e/m 1: a single-cell test could correct these, but only to a table column, still two-way unless it lands in e/r or a/n); and 28 are in the two pairs the table draws as two symbols (e/r: PHI 17; a/n: C43 9, 4STEM 1, 4PI 1), where no shape instrument has separated the letters (in f.61's hand H23, H24b, H401; elsewhere H71, H73). 44 of the 59 lie inside Tomokiyo's spans, 15 outside.** So the meter's
two-way band is at its floor for shape work; it moves only by (a) a reading of a position with a control (H125: none exists at the length of
f.61's out-of-span material alone), (b) new lettered material in f.61's hand (ASKS 88/89/93; fr.4699 by reproduction), or (c) a verifier grading
Tomokiyo's in-span letters (published). H406: runner-15 section added to `family/V9_PAGE.md` for LANE VO3. Cost ~0.07.

## Campaign steps H407, H408, H409 (29 Sept 2026, 19:29-19:21 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- the two span letters key v8 missed were transcription slips on f.61; corrected, the key reproduces 55/55 (1 vision call)

Script-first (NOTES H405 context): key v8's f.61 reading key reproduces 53 of Tomokiyo's 55 span letters; the two misses were **L07/4** (reader
code BETA, cell m/s; Tomokiyo's 'a' of "jal") and **S2's final 'e'** ("capable": no sign after L03/15 in pass A). The runner then looked at both
places on the f.61 native region image (disclosed): L07/4 is drawn like the "43" glyph, not like L11/1's beta; after L03/15's bracket a
loops-on-a-stem sign stands before the clear words "a les entendre". Design committed before the call (`family/h407_span_miss.py`, key
`family/h407_items.tsv`, prompt note H407; 452d02b6's parent), two changes before the call recorded in its docstring (control B3 moved off the
letter-shaped CA; one known PHI tile replaced for marker placement). One blind Opus call, reply `family/passes/h407_reply.tsv`, result
`family/h407_span_miss_result.txt` (`--check` OK):
- **Part A (forced choice vs reference X = L11/1 beta, Y = L03/8 43): known items 9/9 (6 C43 -> Y, 3 PHI -> neither); L07/4 at three windows Y, Y, Y
  -> pre-stated "L07/4 is the 43 sign (C43, a/n): the BETA code there is a reader slip".**
- **Part B (count cipher signs from a marked sign to the first clear word): controls L05 from pos 13 = 6 and L08 from pos 11 = 4, both exact; L03
  from pos 10 = 7 (pass A 6), last "a looped sign like phi, loops on both sides of a long descending stem, just before 'a les entend...'" -> pre-stated
  "pass A missed a sign at L03/16 (PHI-like)".**
H408 (script-only): the two corrections written to `scripts/f61_positions_corrections.tsv` (pass files untouched) and applied by
`family/h408_span_miss_apply.py` (`--check` OK), result `family/h408_span_miss_apply_result.txt`:
- **Five spans under key v8's f.61 reading key: uncorrected 53/55 (2000 permuted keys p95 0.418 -- FAMILY-13's figure reproduced); corrected 55/55 =
  1.000 (permuted mean 0.280, p95 0.436, 0/2000 at or above).**
- **Meter: uncorrected 12 / 59 / 2 / 26 of 99; corrected 12 / 60 / 2 / 26 of 100** (L07/4 stays two-way, BETA m/s -> C43 a/n; L03/16 adds one
  two-way PHI).
Caveats for the verifier: the 55/55 is in-sample for part of the f.61 reading key (4PIPI's a/n at L11/9 comes from Tomokiyo's S5 alone; the F61READ
rows from f.176r), and the two positions were chosen because the key missed them -- the corrections rest on the blind shape reads and their controls,
not on the key. Both corrections sit inside published spans (Tomokiyo's letters), so they improve the transcription and the key check, not a
reading claim. No key, class or grade changed; the pass files and key v8 are untouched. H409: HYPOTHESES.md rows and family/V9_PAGE.md line
written. 1 call, cost estimate 1.5 USD.

## Campaign step H410 (29 Sept 2026, 19:41-19:26 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- f.61 L10's transcription holds: 13 of 13 signs confirmed by blind forced choice (1 vision call)

`family/h410_l10_class_qa.py`, key `family/h410_items.tsv`, prompt note H410, committed before the call (2f324f03's parent); the runner looked at the
sheets for marker placement only. L10's 13 signs (outside every Tomokiyo span; scripts/f61_positions_L10.tsv) and 16 known in-span items (2 per class)
against 8 reference signs cut from f.61's in-span positions (EBR, PHI, VBAR_A, SBS, VBAR_B, INF, C6, CA), one blind Opus call, reply
`family/passes/h410_reply.tsv`, result `family/h410_l10_class_qa_result.txt` (`--check` OK): **gate 16/16; L10 13/13 confirmed** (EBR CA PHI
VBAR_A PHI SBS VBAR_B INF CA C6 SBS CA C6), including the VBAR_A / VBAR_B distinction (plain triangle vs triangle with a second stroke) at L10/4
and L10/7. What it means: the reader codes any reading of L10 would rest on are confirmed by a second instrument with a known-answer gate; the
H407 slips were local, not a sign that pass U2's L10 is unsound. No key, grade or reading. 1 call, cost estimate 1.5 USD.

## Campaign step H411 (29 Sept 2026, 19:47-19:29 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- the rest of f.61's out-of-span signs: 13 of 14 confirmed, one flag (L05/1 reads as the LOOPBAR null, as Tomokiyo's dash implies) (1 vision call)

`family/h411_class_qa.py` (H410's design; key `family/h411_items.tsv`; prompt note H411), committed before the call (27b6f156's parent); placement look
only. Twelve references from f.61's in-span positions (H410's 8 + CROSS, 4PI, C43, LOOPBAR); targets L01/1-2, L01/7-12, L03/1-3, L05/1-2, L11/8 (no
position data exists for L02 or L04); classes with no second token on f.61 (ELOOP, HASH4, 4STEM, LOOPSTEM1, CH) pre-stated to confirm as 'none'.
One blind Opus call, reply `family/passes/h411_reply.tsv`, result `family/h411_class_qa_result.txt` (`--check` OK): **gate 18/18; 13 of 14
confirmed; one flag: L05/1 (reader code LOOPSTEM1, fitted cell q/s) answered R12 = LOOPBAR**, the ♀-with-bar sign Tomokiyo publishes as a null.
Tomokiyo's S3 marks L05/1 with a dash ("---trop"), so the flag and the published markup agree: L05/1 would be a null, not a q/s letter. By the
pre-stated rule a flag is not applied on one read: H413 re-reads it. What it means if it holds: one cross-column two-way token (H405's floor
table) becomes a null -- the one meter move shape work can still make on f.61. No key, grade or reading. 1 call, cost estimate 1.5 USD.

## Campaign step H413 (29 Sept 2026, 19:52-19:31 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- L05/1's LOOPBAR flag does not reproduce (1 vision call)

`family/h413_l05_1_reread.py` (key `family/h413_items.tsv`, prompt note H413), committed before the call (470c6035's parent). One fresh blind Opus
forced choice, H411's references and prompt; reply `family/passes/h413_reply.tsv`; result `family/h413_l05_1_reread_result.txt` (`--check` OK):
**gate 18/18 known and the positive L03/2 -> R12 (LOOPBAR); L05/1 at W1 / W2 / W3: none / n / R12 -> pre-stated "the flag does not reproduce"**.
LOOPSTEM1 stays as coded; nothing written to scripts/f61_positions_corrections.tsv. With H411 the record for L05/1 is LOOPBAR 2 reads (H411, H413
W3), none 1, unclear 1 -- a sign the readers cannot place firmly, beside Tomokiyo's dash. The out-of-span QA (H410, H411, H413) thus confirms 26 of
27 out-of-span sign codes on f.61 and leaves L05/1 unsettled. 1 call, cost estimate 1.5 USD.

## Campaign steps H414 and H415 (29 Sept 2026, 19:56-19:34 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- the meter's two 'wider' OTHER signs: L04/2 is punctuation, L02/2 a sign matching no reference (1 vision call)

`family/h414_other_two.py` (key `family/h414_items.tsv`, prompt note H414), committed before the call (8d1d6b8e's parent). No position file covers L02
or L04, so the runner set the two positions by eye on the native region image (disclosed; markers checked): L02/2, the barred double stroke after
the PHI before "particulierement"; L04/2, a dot after the LOOPBAR before "Mais". One blind Opus forced choice against 15 f.61 in-span references
(H411's 12 + HASH4, ZHOOK, 4TRI) with an added option P (punctuation / not a cipher sign); reply `family/passes/h414_reply.tsv`; result
`family/h414_other_two_result.txt` (`--check` OK): **gate 17/18; L04/2 P at 3 of 3 windows -> punctuation, not a cipher sign; L02/2 'none' at 3 of 3
windows -> a cipher sign matching none of the 15 references** (not VBAR_B, HASH4, 4PI or ZHOOK: its class stays open; the cell stays wider).
H415 (script-only): the L04/2 deletion added to `scripts/f61_positions_corrections.tsv`; `family/h408_span_miss_apply.py` extended for 'delete'
rows (`--check` OK): **meter with every correction 12 / 60 / 1 / 26 of 99** (uncorrected 12 / 59 / 2 / 26 of 99; spans 55/55 unchanged). The
transcription corrections so far (H407, H414): L07/4 BETA -> C43; L03/16 PHI inserted; L04/2 removed as punctuation. No key, grade or reading.
Cost estimate 1.6 USD.

## Campaign step H416 (29 Sept 2026, 20:04-19:36 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- the ten f.108r overlay misses under key v8 sorted (script-only)

`family/h416_108r_misses.py` -> `family/h416_108r_misses_result.txt` (`--check` OK). Key v8 (pooled, EBR form A) reads 74 of 84 overlay letters on
f.108r (f.61's hand); the ten misses fall in three kinds:
- **word sign (3):** T2 letters 8-10 'qui' meet one OTHER sign (sign 8) -- the table's own 'qui' word code (keys/key_mayenne_1592.tsv), not an error;
- **cells that do not close to a table column (2):** 'f' at an EBR (form A cell a/l/s: s without its column partner f) and 'z' at a BETA (cell m/s:
  m without its partner z) -- the published design pairs f/s and m/z under one symbol each, so a fitted cell holding one letter of a pair and not the
  other contradicts it (the same cross-column sets as F61_FLOOR.md);
- **transcription questions (5):** 'p' at a 4PI (T1 sign 20; the 4-family bowl question), 'e' at an INF (T1 sign 36), and three unclassed OTHER signs
  (T2 signs 3, 27, 37 for l, l, m).
No key change. Rows H417 (the column-closure question as a scored key variant) and H418 (the f.108r transcription questions) follow. Cost ~0.05.

## Campaign step H417 (29 Sept 2026, 20:07-19:37 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- the table's column structure as a key constraint: neither variant beats the fitted cells on both known answers (script-only)

`family/h417_column_closure.py` (written before running) -> `family/h417_column_closure_result.txt` (`--check` OK). Three keys scored on f.61's five
spans (with the corrections file) and the f.108r overlay, each against 2000 permuted keys of its own:
| key | f.61 spans | margin over own p95 | f.108r overlay | margin |
|---|---|---|---|---|
| v8 (fitted cells) | 55/55 | +0.564 | 74/84 | +0.476 |
| closed (every letter brings its column partner) | 55/55 | +0.527 | 76/84 | +0.429 |
| column (cross-column classes cut to their top-mass column) | 55/55 | **+0.618** | 68/84 | +0.464 |
Column variant changes: 4STEM a/c/e/n -> a/n; 4TRI c/p/t -> c/p; BETA m/s -> m/z; CH e/m -> m/z; DBL e/r/u -> e/r; EBR (form A) a/l/s -> i/l
(y folded to i); LOOPSTEM1 q/s -> d/q; RSIGN -> m/z. Pre-stated read-out: **neither variant fits as well as v8 on both leaves**. The closed key
gains two f.108r letters (the 'f' and 'z' of H416) but, being wider, loses margin; the column key sharpens f.61 (+0.618) but loses six f.108r
letters, i.e. the fitted cells' extra letters (4TRI t, DBL u, EBR form A's a and s) do real work on f.108r. What it means: the published column
pairing is not by itself a better key than the period-fitted cells; BETA m/s -> m/z alone is the one change H416's evidence (the 'z' of
"commoditez") supports without a loss -- a single-cell question for the verifier, not applied. No key change. Cost ~0.1.

## Campaign step H419 (29 Sept 2026, 20:09-19:38 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- BETA m/s -> m/z: supported on both known answers (script-only)

`family/h419_beta_mz.py` (written before running; `family/h419_beta_mz_result.txt`, `--check` OK): key v8 with the single cell BETA m/s -> m/z
(the table's m/z column): **f.61 spans (corrected) 55/55, margin +0.564 (= v8); f.108r overlay 75/84, margin +0.488 (v8 74/84, +0.476)** ->
pre-stated "BETA m/z is supported". For the verifier, rule 4: the period tables attest BETA s too (f.101r 3, f.188r 2 against z 3 on f.101r and
f.274r), so the choice between m/s and m/z (or m/s/z) is a weighing of witnesses, not settled by this count; on f.61 the one BETA (L11/1, Tomokiyo
m) reads m under either. A proposal; no key change. Cost ~0.05.

## Campaign step H418 (29 Sept 2026, 20:12-19:41 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- f.108r class check: CONTROL FAIL (16/19), nothing scored (1 vision call)

`family/h418_108r_qa.py` (key `family/h418_items.tsv`, prompt note H418), committed before the call (5f6a13fa's parent). Ten references from f.108r's
overlay-confirmed tokens, 19 known items, H416's six transcription questions at three widths; one blind Opus call, reply
`family/passes/h418_reply.tsv`, result `family/h418_108r_qa_result.txt` (`--check` OK): **gate 16/19 (bar 17) -> CONTROL FAIL, nothing scored.**
The three known misses: a ZHOOK tile cut at its band's right edge (answered n) and both 4STEM known items answered as the C43 reference -- the
readers' 4STEM/C43 boundary on f.108 does not follow shape (H199's finding on f.108v), so 4STEM was not a fair reference class. Ungated observation
only, not a result: the targets answered consistently across their three windows (T1/20 4PI -> 4TRI x3, where the overlay has p; T2/37 OTHER -> BETA
x3, where it has m; T2/3 and T2/27 OTHER none x3; T2/8 'qui' none x2 / n; T1/36 INF n x3). H420 re-runs with the control fixed before any use.
Cost estimate 1.5 USD.

## Campaign step H420 (29 Sept 2026, 20:16-19:44 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- f.108r class check with the control fixed: gate 17/17; T1/20 is a 4TRI (overlay p), the 'qui' sign is drawn like 4TRI as the table draws it (1 vision call)

`family/h420_108r_qa2.py` (H418 with the pre-stated fixes: no 4STEM class, no band-edge tiles, seed 420; known items H418's non-edge ones -- the row
said re-drawn, disclosed), key `family/h420_items.tsv`, prompt note H420, committed before the call (2b054724's parent). One blind Opus call, reply
`family/passes/h420_reply.tsv`, result `family/h420_108r_qa_result.txt` (`--check` OK): **gate 17/17.**
- **T1 sign 20 (pass-A 4PI, overlay p): 4TRI at 3 of 3 widths** -- a reader slip in the 4-family, the letter then fits (4TRI c/p).
- **T1 sign 36 (INF, overlay e): INF confirmed 3/3** -- the miss there is not the sign's class (an alignment or overlay question).
- **T2 signs 3, 27, 37 (OTHER; overlay l, l, m): none 3/3 each** -- signs outside the nine references (H418's ungated BETA for sign 37 does not
  reproduce).
- **T2 sign 8 (OTHER, overlay 'qui'): 4TRI 3/3** -- the published table draws the 'qui' word sign as "similar in construction to the c/p column's
  letter symbol" (keys/key_mayenne_1592.tsv), so the reader's answer agrees with the table's description.
The one correction goes to `scripts/f108r_positions_corrections.tsv` (pass files untouched). `family/h420_rescore.py` (`--check` OK): **f.108r
overlay under key v8 74/84 -> 75/84 with the correction -> 76/84 with the correction and H419's BETA m/z** (own permuted p95 0.405, 0/2000 each).
No key or grade change. Cost estimate 1.5 USD.

## Campaign step H421 (29 Sept 2026, 20:21-19:47 UTC by date -u, runner 15 session_01BDhspZ38TdrrXYSvLPTpjc) -- f.61 L02/2 is not f.108r's l-sign or m-sign; f.108r's two 'l' OTHER signs are one sign (1 vision call)

`family/h421_l02_crossleaf.py` (key `family/h421_items.tsv`, prompt note H421), committed before the call (6210c624's parent); INF dropped from the
references before the call after the placement look (f.108r draws it crossed, f.61 open), disclosed in the docstring. One blind Opus call, reply
`family/passes/h421_reply.tsv`, result `family/h421_l02_crossleaf_result.txt` (`--check` OK): **gate 8/8 cross-leaf known items (f.61 tiles in
greyscale against f.108r references) and the internal check (f.108r T2/27 -> R1, the T2/3 'l'-sign) passed; f.61 L02/2 'none' at 3 of 3 windows ->
unassigned.** Two points for the verifier: the forced-choice design transfers across the two leaves of f.61's hand (8/8); and f.108r's overlay
'l' at T2/3 and T2/27 falls on one sign outside the reader codes (a distinct l-form in this hand, H420/H421). f.61's L02/2 remains a sign with no
class (the meter's one 'wider' token). Cost estimate 1.5 USD.

## Campaign step H423 (29 Sept 2026, 20:23-20:26 UTC by date -u, runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W) -- a per-cell context chooser: known-answer control FAILs its pre-registered power gate; f.61 not touched (script-only)

The lead row after H401/H405 (the two-way band is at the table's shape floor): choose the letter in each two-way cell from the
surrounding French. Instrument (`family/h423_ctx_chooser.py`), deliberately not H33/H57 (no model judge, no letter sets wider than
key v8's cells, no ? wildcards): each line cut into segments (break at a clear word, a word code or a sign with no cell; nulls
dropped as Tomokiyo drops them; on f.61 the meter of record's rows with the corrections file applied, C6/CA dropped, L01/12 and
L02/2 breaks); every cell starts at the pair's more frequent fr16 letter; iterated conditional modes (<= 50 sweeps) then give each
multi-letter cell the letter maximising the fr16 5-gram log-probability (tools/french16_ngram.py -- the shared period model, letters
of Catherine de Medicis and Marguerite de Valois, 1550s-1600s: era- and register-matched to a 1592 League letter) with every other
cell held. Known letters never enter the chooser. Gates G1-G3 in HYPOTHESES.md H423, pushed 81ec946e before the scoring run.

| known-answer set | N | chooser | unigram start | McNemar (chooser-only / unigram-only, one-sided p) | order-shuffle null mean / p95 |
|---|---|---|---|---|---|
| f.61 spans, Tomokiyo's letters hidden | 47 | 39 = 0.830 | 36 = 0.766 | 7 / 4, p 0.27 | 0.624 / 0.723 |
| f.108r overlay (f.61's hand) | 50 | 43 = 0.860 | 35 = 0.700 | 10 / 2, p 0.019 | 0.658 / 0.720 |
| f.101r period decipherment (DP-aligned) | 1129 | 817 = 0.724 | 776 = 0.687 | 128 / 87, p 0.003 | 0.659 / 0.676 |
| f.188r period decipherment (DP-aligned) | 442 | 322 = 0.729 | 295 = 0.667 | 70 / 43, p 0.007 | 0.634 / 0.667 |
| f.61's hand (f61 + f108r) | 97 | 82 = 0.845 | 71 = 0.732 | 17 / 6, p 0.017 | 0.642 / 0.701 |
| pooled | 1668 | 1221 = 0.732 | 1142 = 0.685 | 215 / 136, p 1.5e-05 | 0.651 / 0.667 |

Coin flip is 0.5 on every row (binomial p from 2.8e-06 on f.61's 47 to 3e-83 pooled). Per pair, pooled (N, chooser, unigram): e/r
698 488 512 (the chooser is BELOW the unigram rule on e/r pooled), i/x 225 215 219, g/t 214 185 191, i/l 147 76 0, a/n 138 93 71,
d/q 104 83 73, f/s 61 50 54, m/s 48 11 5, q/s 10 3 3; on f.61's hand e/r 34 32 25, a/n 19 13 12, g/t 11 9 9, i/x 10 10 10, b/o 7 6 5,
c/p 6 5 3, d/q 4 4 4, l/y 3 3 3, m/s 3 0 0. Per-cell rows for f.61 and f.108r are in `family/h423_ctx_chooser_control_result.txt`.

**Gate: G1 pooled PASS, G2 f.61's hand PASS, G3 power FAIL (0.763 at N 60 from the pooled control, gate 0.80) -> FAIL as
pre-registered: untested-by-this-tool at f.61's N.** H424 (choosing f.61's 60 two-way letters) is dropped by the pre-stated rule;
no f.61 letter was chosen and none is recorded. Descriptive only, computed after the gate result and not a gate: the same power
figure drawn from f.61's own hand alone (97 cells) is 0.961 -- the pooled figure is pulled down by the two other-hand leaves, whose
known letters are DP-aligned and noisy (f.101r's alignment is half conflicts) and whose e/r cells run against the chooser. Whether
a gate on f.61's own hand may license the target in a fresh pre-registration, or new lettered material in the hand is needed first,
is the verifier's / orchestrator's decision (H425), not a re-gate by this runner (rule 3's one-knob paragraph). Two caveats a
verifier should weigh: key v8's f.61 cells were fitted partly to these same spans (the chooser picks within cells that contain
the known letter by construction; that helps the unigram rule and the chooser alike), and the null rule on the other leaves uses
the aligned-to-nothing flag, a mild advantage those controls have over f.61. The brief's "letter pairs permuted across cells" null
cannot be scored against a known letter (the letter leaves the cell), so the within-segment order shuffle, which can differ on this
statistic, stands in for it. f.124r was not used: its gloss is HELD (readers agree on 43-49% of words) and the committed
alignment's numeric codes do not map back onto the committed draft (45/45 lines differ).
Reproduce: `python3 family/h423_ctx_chooser.py --build|--control [--check]` (both check OK). Script-only, about 1 minute of CPU.
Not a reading; no key, cell, grade or class change.

## Campaign steps H426, H427, H425 (29 Sept 2026, 20:27-20:31 UTC by date -u, runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W) -- f.108r T1/36 is not an offset; the chooser's gain is inconsistent by pair across hands; VO3 packet (script-only / notes)

- **H426** (`family/h426_t1_36_offset.py`, check OK): f.108r T1 has 39 signs and 39 overlay letters; f61crib.align pairs them one-to-one with no
  gap, misses T1/6 (EBR under f) and T1/36 (INF under e). Window T1/30-39: unshifted 9/10 signs carry their overlay letter; shifted -2, -1, +1,
  +2: 3, 0, 1, 1 of 10. So T1/36 is a genuine INF-e conflict in "plusieurs" (INF twice for "eu"), not an alignment offset; the overlay truth
  stands. Runner 15's suggestion (2) is closed.
- **H427** (`family/h427_ctx_perpair.py`, `family/h427_ctx_perpair_result.tsv`, check OK): per pair and leaf with Wilson intervals. The
  chooser is below the unigram rule on e/r, i/x and g/t on both other-hand leaves (f.101r e/r 0.684 vs 0.734, N 474; f.188r 0.695 vs 0.732,
  N 190) and on f.188r f/s; above it on i/l (0.50-0.56 vs 0), a/n, d/q, m/s. On f.61's hand it is above on e/r (f.108r 0.90 vs 0.65; f.61 spans
  1.00 vs 0.86), and below on f.61's a/n (7/11 vs 8/11) and g/t (3/4 vs 4/4). A blended gain over opposite per-pair signs: any later use of a
  context chooser needs a per-pair gate, not the pooled figure (rule 3's AX-NAMES paragraph).
- **V12 sensitivity:** VERIFY-F61-V12 (AUDIT.md) endorses L05/1 = LOOPBAR (null); `h423_ctx_chooser.py --control --v12` drops it: f.61's
  two-way cells 59, the f.61 known-answer row unchanged (39/47 vs unigram 36/47), gate unchanged. The corrections file itself is the
  orchestrator's to update (V12's "What should merge"); not edited here.
- **H425:** runner-16 section in `family/V9_PAGE.md` for LANE VO3 and the orchestrator, naming the one decision that is not the runner's
  (whether f.61's-hand power 0.961 may gate a fresh pre-registration of H424, given the per-pair inconsistency and the in-sample caveat).

## Campaign step H428 (29 Sept 2026, 20:32-20:34 UTC by date -u, runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W) -- V12's two held reads reproduce: L11/8 is the CROSS sign, the L02 opening mark is LL (1 vision call)

VERIFY-F61-V12 held L11/8 (reader code 4STEM; its one read CROSS) and the unlisted mark opening L02 (its C4: LL) for one more read each.
`family/h428_v12_holds.py` (script, items key `family/h428_items.tsv` and prompt `scripts/PROMPTS.md` H428 pushed 387c7771 before the call):
references R1 4STEM from f.108r T1/2 (f.61's hand, overlay a -- the in-hand 4STEM V12 asked for), R2 CROSS L07/10, R3 4PI L11/9, R4 C43 L03/8,
R5 LL L05/16, R6 PHI L01/5, R7 VBAR_A L03/6, options N / O (plain handwriting); all tiles greyscale; the L02 mark's centre is V12's own eye
placement (disclosed). Placement look by the runner: the references sheet only. One blind Opus call, reply verbatim in
`family/passes/h428_reply.tsv`. **Gate 9/9 known (>= 8), both f.108r 4STEM known items -> R1: PASS.**
- **L11/8: R2 CROSS at W1, W2, W3 -> CROSS**, V12's read reproduced by a second instrument with the in-hand 4STEM on the panel. Tomokiyo's S5
  markup ('melente-noit') has a dash at this position, consistent with a null. The reader's caveat: the match to R2's small cross is
  "moderate confidence" (it describes the sign as an open-topped cross, stem curving left). If merged, one two-way token (4STEM a/n) becomes null.
- **L02 opening mark: R5 LL at W1, W2, W3 -> LL**, V12's C4 reproduced. Out of every span. If merged, one null sign is added (cipher count 100).
With V12's endorsed state (12 / 59 / 1 / 27 of 99) and both of these merged the meter would read **12 / 58 / 1 / 29 of 100** -- computed by hand
from the bands, for the verifier; nothing is applied here (the corrections file is the orchestrator's, after a verifier's ruling). H428b (L01/11
HASH4 vs 4PI) still needs an in-hand HASH4 tile source. Cost: one Opus call (~102k subagent tokens), est. 1.5.

## Campaign step H429 (29 Sept 2026, 20:36 UTC by date -u, runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W) -- f.108r's "fitted extras" are form-A brackets (script-only)

`family/h429_108r_fitted_extras.py` -> `h429_108r_fitted_extras_result.tsv` (check OK): the f.108r overlay letters key v8 catches and H417's column
key does not are seven, every one a bracket under 's' (T1/1, 5, 14, 34, 39; T2/7, 31; both passes EBR, pass A conf h) -- none is a 4TRI t or DBL u
(runner 15's suggestion listed those; they do not occur here). H22 (28 Sept) already split the bracket blind on both leaves, EBR_A (hairline
diagonal) = f/s 6/6, EBR_B (squared C) = l/y 4/4, and all of f.61's in-span brackets are form B ('l'). The f.108r sequence used by
H417/H420/H423 carries the unsplit code EBR and loads form A's pooled cell a/l/s, which H417's column rule cut to i/l; under H22's split the seven
's' are the table's f/s column. So these are not evidence for letters outside the columns, and no new shape test is warranted. No key change.

## Campaign step H428b (29 Sept 2026, 20:36-20:38 UTC by date -u, runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W) -- f.61 L01/11 is not the 4PI; the in-hand hash reference turned out to be the looped form (1 vision call)

V12's third hold: L01/11 (reader code HASH4; V12's one read 4PI, against a panel with no hash reference). `family/h428b_l01_11_hash4.py` (script,
key, prompt pushed 9a11d732 before the call): R1 HASH4 from f.108r L05/19 (read HASH4 by both independent passes C and D), R2 4PI L11/9, R3 4STEM
f.108r T1/2, R4 C43, R5 PHI, R6 VBAR_A, R7 CROSS; check item L01/12 (the 4-over-Pi beside it). Placement look: references sheet only. Reply
verbatim `family/passes/h428b_reply.tsv`. **Gate 8/8 known (>= 7), both f.108r HASH4 known items (L05/9, L07/5) -> R1, check L01/12 -> R2: PASS.**
**L01/11: N at W1, W2, W3** ("large hatched blob of several uprights, 4/W-like top; not matched"). Pre-stated read-out: neither 'HASH4' nor
'4PI'. What it settles: V12's 4PI read does not reproduce (the reader put the true 4-over-Pi beside it on R2 and L01/11 elsewhere at every
window). What it does not: the in-hand reference is the crossed-loop hash ("dense crossed loop cluster", both f.108r passes), which key v6
already separates from the 4-headed HASH4 (the HASHLOOP row, UNREAD); the reader's description of L01/11 (a 4-topped hatched sign) fits the
4-over-hash, for which no f.61-hand reference with position data is on disk. So the reader code HASH4 d/q stays as coded; no change proposed;
the meter is unaffected. For a verifier: V12's hold on L01/11 can be closed as "not 4PI" on two reads (V12 1, this 3/3 N); its class needs a
4-over-hash reference in f.61's hand (f.108v's 4-over-hash, H144/H212 tiles) if anyone wants it settled.

## Campaign steps H432 and H430 (29 Sept 2026, 20:39-20:41 UTC by date -u, runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W) -- the proposals' meter by script; a waiting held-out scorer for the context chooser (script-only)

- **H432** (`family/h432_meter_proposals.py`, VERIFY-F61-V12's own meter/spans functions imported; check OK; V12's meter_v12 --check also OK):
  (c) V12 endorsed 12 / 59 / 1 / 27 of 99; (c) + H428 L11/8 CROSS 12 / 58 / 1 / 28 of 99; (d) + L02 opening LL 12 / 59 / 1 / 28 of 100;
  (e) both H428 proposals 12 / 58 / 1 / 29 of 100 -- the figure H428's NOTES gave by hand, now reproduced by script. Spans 55/55 in every state
  (L11/8 sits on Tomokiyo's dash). Corrections file untouched.
- **H430** (`family/h430_ctx_heldout.py`, pushed before any gloss exists): the only licence left for H424 after H423's power FAIL. When the
  person's f.108r L04-L06 gloss lands (ASKS 88, `scripts/gloss108_person.tsv`, H137's format and placement, key v8 cells), it runs H423's
  chooser UNCHANGED on those lines and gates, fixed now: chooser > unigram (exact McNemar one-sided p < 0.05 on the new cells alone), > the
  order-shuffle p95 (100 reps, seed 430), and no pair with >= 5 new cells where the chooser is below the unigram rule (H427). PASS -> H424 goes
  to a verifier's decision; FAIL -> the chooser is retired for f.61. Today it prints "waiting". `--selftest` (a synthetic gloss built from the
  chooser's own letters, 17 words, 53 two-way cells) scores the chooser 53/53: PASS (plumbing only; says nothing about accuracy). f.211r
  (ASKS 93) and f.106r (ASKS 99) adapters are not written; their pack formats are not fixed.

## Campaign step H431 (29 Sept 2026, 20:42-20:44 UTC by date -u, runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W) -- f.61 L01/11 reads as the 4-over-hash when that form is on the panel (1 vision call)

H428b's panel had only the looped hash; L01/11 matched none. `family/h431_l01_11_4overhash.py` (script, key, prompt pushed 1938ddfd before the
call): R1 the 4-over-hash in f.61's hand, f.108v L03/6 (one of the f.108v HASH4 H162's gated read called 'four present'; tile trimmed of sheet
padding before the call, disclosed), R2 the looped hash f.108r L05/19, R3 4PI L11/9, R4 4STEM f.108r T1/2, R5 C43, R6 PHI, R7 CROSS; check item
L01/12. Reply verbatim `family/passes/h431_reply.tsv`. **Gate 8/8 known (>= 7), both f.108v 4-over-hash known items (L03/33, L05/34) -> R1,
check L01/12 -> R3 (4PI): PASS. L01/11: R1 at W1, W2, W3 -> the 4-over-hash**, i.e. the reader code HASH4 (d/q) stands. The reader's own
caveat: the mark is "heavily overwritten ... possibly a correction", R1 or R3, low confidence -- so this is grade-M transcription support, not
firm. With H428b (not the looped hash, not 4PI) and V12's single 4PI read, the reads on L01/11 are 4PI 1 (V12), none 3 (H428b, no 4-over-hash on
the panel), 4-over-hash 3 (H431): for a verifier, V12's hold resolves to "HASH4 as coded, M". Meter unchanged.

## Campaign steps H433 and H434 (29 Sept 2026, 20:42-20:50 UTC by date -u, runner 16 session_01Vtwc6CEJD2BSnYdzzY4f8W) -- the held-out scorer covers ASKS 89 and 93, filters to pass-agreed cells, and knows its own power (script-only)

- **H433** (`family/h430_ctx_heldout.py` extended, no gloss exists yet): adapters in the desk packs' fixed formats for ASKS 89 (f.108v,
  `scripts/gloss108v_person.tsv`, pass A numbering) and ASKS 93 (f.211r, `scripts/gloss211r_person.tsv`, ruler ticks from the pack's own
  table); ASKS 99 asks for hash shapes, not letters (no adapter). The gate is applied to the pool of whichever sources have landed. Transcription
  filter, pre-registered: on f.108r and f.108v a cell is scored only where both sign passes read the same class (f.108r 74 of 85 signs, f.108v
  179 of 311), because f.61's own transcription is QA'd and f.108v's passes differ on about half their columns; unfiltered cells still give
  context. Self-tests (synthetic glosses from the chooser's own letters, plumbing only): f108r 45/45, f108v 60 + f211r 7: PASS.
- **H434** (`family/h434_heldout_power.py`, check OK): power of H430's criterion (1) (McNemar p < 0.05, chooser > unigram), resampling f.61's
  own-hand cells from H423 (97; seed 434), at the most cells each gloss could give (every agreed two-way cell glossed -- an upper bound):
  **f.108r alone N 57: 0.46; f.108v alone N 91: 0.66 (0.34 at half coverage); f.211r N 7: 0.00; all three N 155: 0.88.** Criteria (2)/(3) are
  not simulated, so these are upper bounds. Wired into H430's read-out before any data: a FAIL at power < 0.80 reads "untestable at this N --
  keep waiting", and only a pooled FAIL at power >= 0.80 retires the chooser. In plain words: the chooser can be licensed or retired for f.61
  only when all three person reads (ASKS 88, 89, 93) are in; any one alone can pass it but cannot fail it.

## Campaign step NEXT-F61 (2 Oct 2026, 03:13-03:35 UTC by date -u, worker session_019h7LDxX3JCrDUk2KxMg2EQ) -- print search for f.61r's clear fragments: no printed text located (script-only, no vision call)

The finish-or-blocker pass's cheapest next step, run as written. Inputs: `phrases.txt` (12 phrases: 11 clear-prose fragments on disk
from H16 `scripts/read_call_U.tsv`, H264, H286 and H297, each a single blind pass, grade M and conditional on that reading, rule 2;
plus Tomokiyo's own published span phrase "jalousie au beau pere"), `sources.tsv` (the six volumes of the 1758 Memoires de la Ligue,
IA memoiresdelaligu01goul-06goul; OpenAlex and CrossRef keywords). Output: `print-check.tsv`, `print-check-hosts.tsv`.

- **IA full text (ia-global, be-api, every phrase):** no hit for the distinctive fragments. One item matched "sur les lieux vous
  verres": lettresinstructi07richuoft, Richelieu's Lettres et instructions vol. 7 (1853 ed., Richelieu 1585-1642) -- a coincidence of
  phrasing, not this letter. The short generic fragments ("que les choses sont", "particulierement sur les", "pas paresseux si") return
  thousands of unrelated items and test nothing.
- **Memoires de la Ligue (1758), all six volumes:** no hit, exact or by proximity. Vols 1-5 searched in full djvu text (downloaded
  once, cached in sources/ia-fulltext/print-check/; vols 1-3 on the one retry after a connection reset); vol 6's djvu answered HTTP
  500, so it was searched by be-api only (no page locator). The OCR is real for the period: vol 5 names Mayenne 220 times and carries
  1592 17 times, 1593 104 times.
- **Gomberville, Memoires de M. le duc de Nevers (1665):** on Gallica (ark:/12148/bpt6k8717151d and bpt6k6435941k), not on IA. Covered
  only by Gallica-wide SRU exact-phrase search (`text adj`): 0 hits for "seroys pas paresseux", "sur les lieux vous verres", "s il s y
  presentoit les occasions" and "jalousie au beau pere". Control for the instrument: `text adj "paris vaut bien une messe"` returned
  2100 records, so the phrase search works; whether 1665 OCR is good enough to carry these words was not tested, so this is a weak
  negative for that edition. (Gallica's `text all` is a word bag, not a phrase search: its tens of thousands of hits mean nothing.)
- **Henry and Loriquet, Correspondance du duc de Mayenne (Reims 1860-64):** not located as full text from the cloud. IA advancedsearch
  0 items (two queries), Gallica SRU finds only E. Henry's 1860 *Notice sur la "Correspondance du duc de Mayenne", manuscrit de la
  bibliotheque de Reims* (ark:/12148/bpt6k56265188), Google Books API 0 matching volumes (after two 503s). Its date range against 1592
  is therefore **unchecked**. HathiTrust is Cloudflare-blocked from the cloud, so this went to the owner's desk runner as LOCAL-QUEUE
  row L30 (date range first, then the phrase searches).
- **Google Books API (every phrase, country=US):** quoted queries come back as hundreds of loosely matching volumes (348 for "sur les
  lieux vous verres"); no listed volume is a League edition or a Mayenne letter. This is word-matching, not exact phrase.
- **OpenAlex / CrossRef (keywords):** scholarship on the League in general (e.g. "Les marechaux de la Ligue", 2010); nothing on this
  letter. Semantic Scholar answered 429 on its first call and was not asked again.

Result: no clear copy or printed text of f.61 was found by this method on 2 Oct 2026 (a search result, not a novelty verdict, rule 10).
Nothing here changes a sign, so no decode re-run (rule 7). Two limits stand: the phrases are single-pass fragments, not a checked
transcription, and the Henry-Loriquet edition is unsearched (L30). Requests: archive.org about 19 (advancedsearch 9 including 4 resets,
djvu 10), be-api.us.archive.org 73, www.googleapis.com 18, gallica.bnf.fr 16 (2 resets), api.openalex.org 13, api.crossref.org 2,
api.semanticscholar.org 1 (429). Aside for the orchestrator, not acted on (Usage 7): Gallica SRU returned btv1b525085665, "Collection
Memoires de la Ligue. Recueil de chiffres avec leurs clefs, de l'annee 1580 a l'annee 1595"; it is already cited by fr3625-lauriere-1593
and tools/keys/key60.tsv, but no line in this folder says whether it was checked for f.61's table.

## Campaign step A2-F61 (2 Oct 2026, 21:50-21:58 UTC by date -u, worker A2-F61 session_01DbvDk2S6Gkr81RkdBU6tyH, account 2) -- the L02-opening LL foil read: V13's foil condition is met; endorse inserting LL (null) for the verifier (1 vision call)

Intake gate pasted before work: `fr4715-f61-mayenne-1592: partial (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).

The Verdict's cheapest worker step, run as written: the settling read VERIFY-F61-V13 named for the mark opening L02 ("a clear 'll' inside a word
in this hand, read as O -- together with the target still at LL"). Pre-registered and pushed before the call (`family/a2f61/PREREG.md`, commit
eb9091fe; answer key sha256 62bdcfbd..., held outside the repository until the reply was in, now `family/a2f61/key.json`, sha matched by
`score.py`). Instrument: V13's own `cut.py` tile function and V13's position rows unchanged (target = V13's eye placement), V13's 12-reference
panel re-shuffled (seed 20261002); one new row, the foil `F_LL_DELLA`, the clear in-word 'll' of "...della" on f.61 L07 (x 1398, y 835),
placed by this worker on a gridded crop (disclosed look; the foil's W1 tile was checked for centring). One blind Opus call, 19 items, sheets
only. Reply verbatim `family/a2f61/reply.tsv`; `family/a2f61/score.py --check` regenerates `score_result.txt`.

- **Gates:** G1 anchors 9/9 (>= 8; plain 'les' -> O, and CROSS, 4PI, C43, PHI, ZHOOK, 4TRI, 4STEM and the 4-over-hash all right): PASS. G2
  in-span LL L05/16 W3 -> LL: PASS. G3 repeats (target W1 LL/LL, foil W1 O/O): PASS. Rule 3: the foil was free to read O, LL or N at every window,
  so the control could have failed.
- **Foil (in-word 'll', "della") W1/W2/W3: O O O** (reader: "ordinary word 'ella'", high). **Target (L02 opening) W1/W2/W3: LL LL LL** (repeat LL;
  reader: "double looped tall strokes 'll' at centre", medium). Decision rule: foil O at >= 2/3 and target LL at >= 2/3 -> **endorse `L02 0
  insert LL`** (a null).
- Observational, as in V13: the plain 'Il' of "Il seroit" (L02) again read N, "large cursive H-shape", not O. Caveat for the verifier: the
  reader named the foil from its word ("ella"), and the target has no word around it (it opens the line and is followed by PHI), so part of
  the O/LL split may be word context rather than stroke shape; the in-span LL control (L05/16, also between cipher signs) reads LL, and four
  instruments now read the L02 mark as LL at 12 windows of 12 (V12 C4, H428, V13, this read).
- If merged (a verifier's ruling and the orchestrator's merge; this worker edits no corrections or key file): the meter becomes **12 / 59 / 1 /
  28 of 100** (V12's own state (d), `verify_v12/meter_v12.py`); spans unchanged 55/55 (the mark is out of every span). It adds a null, not a
  letter; no reading changes, so no decode re-run (rule 7). Grades: no token graded (rule 4: no letter is claimed). Novelty not classified.

### VERIFY-F61-LL ruling on A2-F61 (2 Oct 2026, 22:09-22:10 UTC by date -u, verifier VERIFY-F61-LL, account 2, separate from the solver)

**Ruling: ENDORSE `L02 0 insert LL` (a null, grade S: an instrument reading with a passing control and a met foil condition; no letter, no H/C).
Merge allowed; not merged by this verifier.**

Checked: (1) order -- PREREG.md and the deterministic `build.py` (seed 20261002) are in eb9091fe at 21:53:15, reply.tsv and key.json in 53c2d53c at
21:54:42; the sha was not itself in the prereg commit, but re-running `build.py` here regenerates a key identical to the committed key.json (sha
62bdcfbd...), so the answer key was fixed before the reply. (2) `score.py --check`: OK; gates G1 9/9, G2 PASS, G3 PASS; target LL LL LL, foil O O O,
reproduced. (3) Sheets regenerated and read by eye.
Leak question (rule 3): the foil's W1/W2/W3 tiles show the whole word "ella" with its flanking e and a, and the reader's notes name the word, so
O was the likely answer from context alone. That weakens the foil as a test of stroke shape, but it is not a non-test: the foil was free to read
LL or N on every window, and V13's own condition asked for exactly this ("a clear 'll' inside a word ... read as O"). What tips it is shape,
which I checked on the tiles directly: the in-word 'll' of "della" is two plain straight stems with no heads, while the L02 mark (#424/#723/#588)
has the hooked, looped heads of the LL reference exemplar L05/16 (#881) -- this hand's ordinary 'll' is not drawn like the LL sign. The target's
context (line start, after the stamp's edge, followed by PHI) carries no word for the reader to complete either.
Chance: the three windows are overlapping crops of one mark, not independent trials, so "3/3 vs 3/3" is closer to one read each than to a
p-value; the weight comes from four instruments concordant at 12 windows of 12 (V12 C4, H428, V13, A2-F61), the anchors at 9/9 and the repeats.
Residual caveat, carried: A_PLAIN_IL (the capital 'Il') still reads N, so the reader's O class is shown only for lower-case in-word script.
Verdict: endorsed; next: F61-FAMILY merges `L02 0 insert LL` into `scripts/f61_positions_corrections.tsv` and re-runs the meter (expected 12 / 59 /
1 / 28 of 100, spans 55/55), ~$1. Novelty not touched (no reading changes).

## Campaign step A2-F61M (2 Oct 2026, 22:27-22:35 UTC by date -u, worker A2-F61M, account 2) -- the endorsed L02-opening LL merged; meter 12 / 59 / 1 / 28 of 100, spans 55/55 (script-only, no vision call)

Merged VERIFY-F61-LL's endorsed row (ROOM 2 Oct 2026 22:10; null, grade S) as `L02 0 insert LL` in `scripts/f61_positions_corrections.tsv`
(header note updated: held, not merged, is now only L11/8 CROSS and L01/11). `family/h408_span_miss_apply.py` gained `"LL": "-"` in its
correction-letter map (the only code change; L02 is not in the span-reader sequence, so the insert touches the meter only, as V12 (d) did).
Re-run: `family/h408_span_miss_apply.py` -> **meter with every correction: firm 12 / two-way 59 / wider 1 / unread-or-null 28 of 100**
(was 27 of 99); **spans with every correction 55/55 = 1.000, 2000 permuted keys mean 0.280 p95 0.436, >= key 0/2000** (unchanged).
`family/h405_meter_floor.py` regenerated `family/F61_FLOOR.md` (meter line only: 28 of 100; the two-way floor table is unchanged).
Both match VERIFY-F61-V12's state (d) in `verify_v12/meter_v12_result.txt`, which is what the endorsement predicted. The 28: 19 nulls
(CA 10, LOOPBAR 5, CROSS 2, LL 2) and 9 unread (C6 8, 4PI L01/12 1). Grades: no letter is read or changed; the one added token is a null
at grade S (no H, no C); the spans' 55 letters remain Tomokiyo's published reading under key v8.
Rule 7: the target has no decode.json or ciphertext.tsv, so `tools/decode_key.py --check` does not apply (it exits on the missing
ciphertext.tsv); the target's regenerators were run instead, all `--check` OK after the merge: h405, h408, h413, h417, h419, h420, h423,
h426, h429, h432, verify_v12/meter_v12.py, verify_v13/meter_v13.py (the two verifier scripts pin their own correction lists and are
unchanged by design). No spec exists for this target (specs/ has no f61 file), so no judge is run. Requests: none. Cost: the orchestrator reads get_session.

## Remaining gaps (finish-or-blocker pass, 2 Oct 2026)
Read so far: no passage outside Tomokiyo's five spans is read. Of the leaf's 100 cipher signs, 12 are firm, 59 two-way, 1 wider and 28 unread-or-null (19 nulls: CA 10, LOOPBAR 5, CROSS 2, LL 2; 9 unread: C6 8, 4PI L01/12 1). Source: VERIFY-F61-V13 (AUDIT.md; verify_v13/meter_v13_result.txt), merged by F61-FAMILY-14, plus the L02-opening LL null endorsed by VERIFY-F61-LL and merged by A2-F61M (2 Oct 2026; family/h408_span_miss_apply_result.txt). 45 of the 59 two-way signs sit inside the spans and 14 outside. family/F61_FLOOR.md says 44/15 because its span column comes from scripts/f61_skeleton.txt, which predates the L03/16 insert; that sign carries Tomokiyo's final 'e' of "capable" (H407 part B, H408). Key v8 reproduces his 55 span letters 55/55 (permuted p95 0.436, 0/2000), so those letters are published, not ours.
- print search on f.61r's full clear text with the reconciled reading's phrases - blocker: not-attempted; tools/print_check.py was re-run on 2 Oct 2026 (VERIFY-F61R) but phrases.txt still holds the older single-pass fragments ("s'il s'y presentoit", "On ne desiroit"), not the reconciled and normalised forms (scripts/f61r_clear_reading.tsv, verified: H 87 / M 17 / I 8; normalised forms in scripts/f61r_clear_corrections.tsv); next: replace phrases.txt with runs from the verified reading, e.g. "Il seroit trop long vous en dire les propos", "s'il s'en presentoit les occasions", "on n'ose enuoyer", "Je ne seroys pas paresseux si", "tant soit peu", and re-run tools/print_check.py, ~$0.5
- 12 two-way signs outside the spans: L01/9, L01/10, L02/1, L03/13, L05/2, L05/13, L10/1, L10/3, L10/4, L10/5, L10/6 and L10/11 (family/F61_FLOOR.md, less L03/16, which is inside S2; L01/11 and L11/8 are listed separately below) - blocker: waiting-on LOCAL-QUEUE L30 (the Henry-Loriquet edition, HathiTrust from the owner's desk); shape work is at its floor (H405), the context judge is retired (H33, H57, H25 L10 3/3 FAIL), the lattice was a non-test (H271), the n-gram chooser failed its power gate (H423), and H125 found that a controlled reading of the out-of-span material alone is impossible at its length. The print search ran on 2 Oct 2026 (NEXT-F61): no printed text of the letter was found in IA full text, the six volumes of the 1758 Memoires de la Ligue, Gallica's exact-phrase search (which covers Gomberville's Nevers, 1665), Google Books, OpenAlex or CrossRef. The Henry-Loriquet date range is unchecked, so L30 asks for it first; next: when L30 answers, re-run tools/print_check.py with any hit volume as a listed source, ~$0.5; and re-run the search on the full clear text once it is transcribed (gap above)
- 45 two-way signs inside the spans: an independent choice of letter by our own instrument (today they carry only Tomokiyo's published letters, grade M) - blocker: waiting-on ASKS 88, 89 and 93 (a person's reads of the f.108r, f.108v and f.211r period glosses); H423's chooser needs a held-out licence. The scorer family/h430_ctx_heldout.py is ready, and H434 puts its power at 0.88 only once all three reads have landed. None of scripts/gloss108_person.tsv, gloss108v_person.tsv or gloss211r_person.tsv exists, and all three ASKS rows are 'backlog' (checked 2 Oct 2026); next: run family/h430_ctx_heldout.py when the files land, ~$0
- BnF fr.4699 ff.37-38 and 41-42 (P. de Fortia to Mayenne's secretaries, Lyon, 7 Feb 1593, catalogued "avec chiffre et dechiffrement", ark:/12148/cc57749t items 18-19; not on Gallica): a possible fourth period witness for the key - blocker: needs-physical-access; family/REQUEST_fr4699.md was drafted 28 Sept 2026 (F61-FAMILY-7) but never sent, and it has no ASKS, LOCAL-QUEUE or SEND-QUEUE row (grepped 2 Oct 2026). The classifier listed this only under siblings; next: the orchestrator files an ASKS row from REQUEST_fr4699.md, asking for a single image of fol. 37r first, ~$0
- L01/11 (pass-A HASH4, d/q) - blocker: illegible; every instrument finds an overwritten or cancelled sign: "heavily overwritten ... possibly a correction" (H431) and "struck-through hash cluster, cancelled sign" (VERIFY-F61-V13). The reads split 4PI 1, 4-over-hash 3, N 6, so the sign is held M as coded.
- L01/12 (4-over-Pi, a split 4PI class) - blocker: open-codes; it is the class's only token outside the spans, and the other token (L11/9) takes a/n from Tomokiyo's S5 alone (H268). VERIFY-F61-V8 found no source for a value here, so it is held unread (AUDIT.md V8/V9 meter verdicts).
- L11/8 (pass-A 4STEM a/n, or CROSS = null) on Tomokiyo's S5 dash - blocker: open-codes; a rule-4 conflict between two instruments that each pass their own gates: CROSS 4 (V12 1, H428 3) against N 4 (VERIFY-F61-V13). It is held M in its pass-A class, and his reading needs no letter there.
- C6, 8 tokens (5 on Tomokiyo's dashes: L01/2, L03/11, L07/6, L08/3, L08/9; 3 outside) - blocker: open-codes; his words exclude the pooled C6 = e at 4 of 5 in-span positions (H261; VERIFY-F61-V9 v9_c6_words.py), and that value comes from another hand and the other direction of the correspondence. f.61's plain 6 is a different glyph (H237), and no glossed leaf in f.61's hand writes C6 (H285). The sign stays unread-or-null.
- L02/2 OTHER (the meter's one 'wider' sign) - blocker: open-codes; it is a single occurrence with no class on any panel ('none' at 3 of 3 windows, H421), followed by clear "particulierement sur les" (read_call_U.tsv), which does not narrow it.

## Escalation (2 Oct 2026)
- [x] siblings: opened, read and aligned into key v8: fr.3982 f.97r, f.101r and f.124r; fr.3983 f.106r, f.108r, f.108v and f.211r; fr.3984 f.176r/177r, f.184r/188r and f.274r. Dropped: fr.3984 f.7 is not f.61's design (H168); fr.2751 f.116 is a clear copy of another letter with no cipher (F61-FAMILY-8); fr.3641 holds figure ciphers and fr.3980 f.10 is a different (Sega) cipher (H404). All 119 BnF aid hits for Mayenne were read (H404). f.61v is blank (H18). The rest of fr.4715 is the Vieuville-Nevers family, and the DECODE crawl has no hit. Not opened: fr.4699 ff.37-38/41-42 is not digitised, and its request was never filed (gap above). fr.3984 f.186r/189r (H48) would add no lettered material in f.61's hand.
- [x] clear-pages: the sister leaves' interlinear and separate-sheet decipherments were the key source throughout (H19, H21, H28, H30, H34, H44, H177b), and fr.4715 holds no decipherment of f.61 (H7). f.61r's own clear prose was transcribed by two gated blind passes plus a reconciliation (A2-F61R, 2 Oct 2026: known-answer 12/13 both passes, word agreement 0.845 vs shuffled max 0.286; 112 words H 87 / M 15 / I 10, scripts/f61r_clear_reading.tsv); it states no writer, recipient or date. Its print search is the open gap above.
- [x] known-keys: tried Tomokiyo's mayenne.htm table (keys/key_mayenne_1592.tsv, F61-CAL); KEY-OFFICES rows 19, 20 and 65 with KEY-DESIGN rows 55-64 (the family's period keys; the 1593 homophonic variant, fr.3984 f.7, is not f.61's design, H168); and Tomokiyo's Mayenne-Sega cipher (different, H404). Bourdeau's repository has no entry (SCOUT-OWN-8, CHECK-SOLVED-WEB). Key v8 reads the spans 55/55. design_prior.py was not run, because the design is already known.
- [x] print: the BnF finding aids (H7/H8/H32, H143, H165, H404); a web and blog sweep (CHECK-SOLVED-WEB, 28 Sept 2026, 'jalousie au beau-pere' 0 hits); tools/print_check.py on 12 clear phrases on disk (NEXT-F61, 2 Oct 2026): no printed text found in IA full text, the Memoires de la Ligue (1758, six volumes), Gallica exact-phrase search (covers Gomberville's Nevers, 1665; control phrase found), Google Books, OpenAlex or CrossRef. Still out: the Henry-Loriquet edition (Reims 1860-64), not located online, date range unchecked, LOCAL-QUEUE L30; JSTOR-QUEUE rows 131-136 unanswered. Re-run print_check on the full clear text once it is transcribed.
- [x] key-rebuild: cell fits H1-H27, transfer and joint fits (H19, H20, H51) and keys v4-v8 from the period alignments give the spans 55/55, and the shape floor is reached (H405). Retired under rule 3(c): the free letterform sort on LL (H302/H304/H309), the model gloss readers for the secretary's interlinear hand (H332, four units) and the model context judge on this leaf (H33, H57, H25). Dead ends: the a/n blind sort is untestable (H24/H24b), the lattice is a non-test (H271) and the beam/seqgain gate was voided (H338-H341). The n-gram chooser failed its power gate once (H423, 0.763 against 0.80); its held-out licence waits on ASKS 88/89/93 (H430/H434).
- [x] image-check: H407 (L07/4 is C43; a missed PHI at L03/16; spans 55/55), H410 (L10 13/13 confirmed), H411/H413/V12 (L05/1 LOOPBAR), H414 (L04/2 is punctuation, deleted), H421 (L02/2 'none'), and H428, H428b, H431 and VERIFY-F61-V12/V13 on L11/8, L01/11 and the L02 opening. Corrections were merged by F61-FAMILY-14. The L02-opening LL foil read ran (A2-F61, 2 Oct 2026): foil O 3/3, target LL 3/3, VERIFY-F61-LL endorsed it (grade S) and A2-F61M merged it (2 Oct 2026): meter 12/59/1/28 of 100, spans 55/55.
- [x] retry: F61-FAMILY-14 (H435) re-ran key v8 over all 99 signs with the merged corrections: meter 12/59/1/27, spans 55/55, f.108r 74/84; A2-F61M re-ran it with the L02 LL merged: meter 12/59/1/28 of 100, spans 55/55. No word outside the spans is forced.
Verdict: keep going: 5 internal gaps (f.61r clear text transcribed 2 Oct 2026), 1 waiting on LOCAL-QUEUE L30; cheapest next: the orchestrator files an ASKS row from family/REQUEST_fr4699.md, ~$0; cheapest worker step: tools/print_check.py on the H-graded phrases of scripts/f61r_clear_reading.tsv, ~$0.5

## Premise check (GF-A2-2, 2 Oct 2026)

Worker GF-A2-2 (account 2, LANE-A2PUSH), 2 Oct 2026 21:16-21:20 UTC (clock read). The open-web and blog check is the CHECK-SOLVED-WEB section above (28 Sept 2026, 8 queries, Cryptiana post read with 0 comments). It was not repeated.

- (a) **Decipherments the folder already mentions.** Found, already known, none beyond partial: Tomokiyo's five interlinear spans on `BnFfr4715f61.png`, captioned "Solved with Polyphonic Cipher?" and listed "(Solution Incomplete)" in `bnf4715.htm`; the BnF dépouillement (ark:/12148/cc577658) gives "Fol. 61 • 38 Lettre avec chiffre." with no "déchiffrement" (H7), unlike the neighbouring nos 36, 37, 39 and 43. The fr.4699 ff.37-38/41-42 "avec chiffre et dechiffrement" letters (Fortia to Mayenne's secretaries) are other letters, a possible key witness, and are not on Gallica (Remaining gaps). The sibling decipherments (fr.3982/3983/3984) are other letters, already used as key sources.
- (b) **Other solvers' working files.** Not found: shallow clones today. Bourdeau's `research/gallica_sweep/NOTES.md` row for fr.4715 reads "most items with decipherments; ff. 82, 84 solved by Lasry; f. 61 open". The sweep fetched f.61 (`f4715_full/`) but holds no reading or key run on it, and there is no `targets/` folder for this item. Its `notice_4715.txt` is the same dépouillement text as H7. Aymeloglu's repository (cited, not copied) has no fr.4715 or Mayenne row (its one "4715" hit is DECODE record id 4715, a Marburg key, unrelated).
- (c) **Physical neighbours, native resolution.** Not found: Gallica IIIF native fetches today (ark btv1b52509819x; canvases by manifest label via `tools/gallica_folio.py`, not by formula): canvas 136 (f.60v), 4079 px wide, blank apart from show-through of the mounted f.60 letter and the stamp; canvas 138 (f.61v, the cipher's own verso), blank, with no slip or note laid in or pasted; canvas 139 (f.62r, no.39), Montholon, Tours 17 Dec 1589 (dépouillement: "avec chiffre, en partie déchiffrée"), a mounted letter of clear text with digit-cipher runs. It is a different cipher family (the Vieuville-Nevers digits, `ciphers/fr4715-montholon-1589`) and holds no clear copy of f.61. f.61r itself (canvas 137) carries no gloss beyond the cipher and its clear prose (intake, 27 Sept). The volume's other "déchiffrement" items are of other letters (dépouillement).
- (d) **Recipient-side editions.** Not found, conditional: neither the dépouillement nor Tomokiyo names a recipient for no.38. The volume is the Nevers papers, so the likely recipient side is the duc de Nevers, whose printed papers (Gomberville's *Mémoires de M. le duc de Nevers*, 1665, covered by the Gallica exact-phrase search in NEXT-F61) and the *Mémoires de la Ligue* (1758) were searched for f.61's clear phrases by `tools/print_check.py` (NEXT-F61, 2 Oct 2026) with no hit. Henry-Loriquet's edition remains unread (LOCAL-QUEUE L30). An identified recipient other than Nevers would need a new search.

Requests this pass: gallica.bnf.fr 3 (native canvases 136, 138, 139, 2 s apart); github.com 2 (shallow clones).

## Campaign step A2-F61R (2 Oct 2026, from 22:47 UTC by date -u, worker A2-F61R, account 2) -- f.61r clear-text transcription: two blind passes + one reconciliation

Intake gate pasted before any deep work: `fr4715-f61-mayenne-1592: partial (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).

**Pre-registered (written before any pass was called).** Inputs: the existing line sheets `images/f61sheetB_L01-L11.jpg`
(cut by `tools/iiif_lines.py --overlap 0`, campaign step H2, 4 segments per line) plus a known-answer line cut fresh by
`tools/iiif_lines.py --image images/src_ark_12148_btv1b9059406b_f195_1250_450_3600_720.jpg --out images/f61rclear
--prefix ka108 --centres 300,387,500 --overlap 0 --debug` (only `images/f61rclear/ka108_L02_s1/s2.jpg` is used: f.108r's
clear line). Both passes see the 11 f.61r sheets and the f.108r line mixed in as "line K", not told which is a control.
Known answer (f.108r clear line, from the leaf matched against Tomokiyo's mayenne2.png, H19): "Et pour cela je vous
laisse a juger quel contentement je debvois avoir" (12 words). Normalisation for every comparison: lowercase, accents
stripped, u=v, i=j=y, punctuation dropped, cipher signs and [?] removed. Gates: (KA) each pass reads at least 10 of the 12
known words (word-level NW alignment); (WA) pooled word agreement between the two passes on the f.61r clear words is at
least 0.80 AND exceeds the maximum of a line-shuffled control (pass A line i vs pass B line j, i != j, all 110 pairs),
which can differ from the target on this statistic by construction. A pass failing KA is dropped; if either gate fails,
no reading is reported beyond the pass files. Reconciliation: one Opus call over only the disagreeing words with the
same crops; grade H for words both passes agree on, M for words settled by the reconciler, I for illegible.
Writer/recipient/date are named only if the clear text states them; otherwise "not stated in the clear text".

**Result (A2-F61R, 22:51 UTC).** Three Opus vision calls (pass A, pass B with the lines in reverse order, one
reconciliation over 20 disputed words only), each given line sheets only, never a full page; 0 network requests.
Files: `scripts/f61r_clear_passA.tsv`, `scripts/f61r_clear_passB.tsv` (verbatim), `scripts/f61r_clear_score.py` ->
`scripts/f61r_clear_score.txt`, `scripts/f61r_clear_recon.tsv` (verbatim), `scripts/f61r_clear_reading.py` (`--check`)
-> `scripts/f61r_clear_reading.tsv`.

- **KA (known answer) PASS, both passes:** 12/13 words each. Correction to the pre-registration: the reference
  has 13 words, not 12; the threshold of 10 was not changed. Both blind passes read the miss as "Je doibs auoir"
  where the reference has "je debvois avoir". The reference wording came from H19's match against mayenne2.png, so
  this miss counts against the reference wording as much as against the passes.
- **WA PASS:** pooled word agreement on f.61r was 93/110 = 0.845 against a gate of 0.80. The line-shuffled control
  (110 mismatched line pairs) had mean 0.052 and max 0.286. Lowest lines: L11 0.50 (2 words), L01 and L03 0.667,
  L07 0.70.
- **Reading, f.61r clear hand.** Grades: H = both passes identical; /M = settled by the reconciliation at medium
  or high confidence; /I = low confidence. [#] = cipher run.
  - 01 `N?us/I auons parlé familieremē/M et amplemē/M de toutes choses [#]`
  - 02 `[#] particulieremē/M sur les plus Importances Il seroit trop long vous en dire les`
  - 03 `propos Et Combiey/M a/I [#] a/I les/M entendud/M Et pleay/I de`
  - 04 `generosité pour beaucoup desiree/M [#] Mais on auoit Come Je le croys aussy/M que les`
  - 05 `choses sont a/I [#] . Et que si nous mesmes ey/M`
  - 06 `en conoyssant le fruit ey/M fesions la premiere pointe On ne desfieroit/I point du reste .`
  - 07 `Cependant/M on n'ose enuoyer depard/M della pour ni mesr'/I a/I [#]`
  - 08 `[#] maintenant qu'oy en a affere Vous/M estes`
  - 09 `sur les lieux vous verres s'il s'ey/M presentoit les occasions Et s'il s'ey/M pouuoit`
  - 10 `prendre quelqu'vne Je ne seroys pas paresseux si [#]`
  - 11 `[#] tant sou/I peu/I .`

  112 words: H 87, M 15, I 10. "ey" is this hand's form of "en" in some places (the reconciler and pass A agree it
  ends in a descender). The "-mē" endings carry a looped suspension for -ment.
- **Four lone "a" signs** sit next to cipher runs (L03 twice, L05, L07). Neither the reconciler nor pass B could
  decide from the ink whether each is a clear word or a cipher sign; they stay I and are not counted in the
  cipher meter.
- **Writer, recipient, place, date:** not stated in the clear text. The letter's first surviving words are a report
  of a conversation ("[N]ous auons parlé familieremēt et amplemēt de toutes choses"). The recipient is "sur les
  lieux". The writer offers to act ("Je ne seroys pas paresseux si [#]").
- **No change** to the cipher meter, key v8 or the span readings; this is clear-hand text only, and no decode script
  re-run is needed (rule 7: the reading's own regenerator is `scripts/f61r_clear_reading.py --check`, OK).
- No judge was run. A clear-hand transcription has no spec judge, and the leaf's context judge is retired.
- **Not found / not done:** the full-clear-text print search (gap, next step).


### Verifier VERIFY-F61R (2 Oct 2026, 23:04-23:15 UTC by date -u, account 2, LANE-A2PUSH): second eye on the A2-F61R clear text

Separate session from A2-F61R. Read in full: the eleven line sheets `images/f61sheetB_L01-L11.jpg` (my own eye, word by word against
`scripts/f61r_clear_reading.tsv`; no full page, 0 subagent calls), the pass, reconciliation and score files, both scripts.

- **Scripts.** `scripts/f61r_clear_reading.py --check` OK before and after my edit. `scripts/f61r_clear_score.py` has no `--check`; re-run on the
  committed passes into a scratch file, it is byte-identical to `scripts/f61r_clear_score.txt` (KA 12/13 both passes, WA 93/110 = 0.845, control
  mean 0.052 max 0.286).
- **Control design (rule 3).** The line-shuffled control can fail differently from the target: word agreement depends on which two lines are
  paired, so it is not a non-test. It is weak, though. It shows that the passes track the same lines; it does not show that they are right. Both
  passes are the same model and can share an error: both read the f.108r known line as "Je doibs auoir". Accuracy rests on the KA gate
  (12/13 per pass), not on WA. So "H" here means two passes by one model agree on the ink. It is not an independent reader's grade.
- **Per line.**
  - L01: endorse. "N?us/I" stays I: the initial is under the stamp, though "auons" makes "Nous" the only fit.
  - L02: endorse.
  - L03: endorse the letterforms. Normalised: "Combiey" = Combien, "pleay" = plein ("Et plein de generosité" runs into L04).
  - L04: endorse, plus one correction. A clear stop sits after the cipher run, before capital "Mais". It is restored as punctuation, not a word.
  - L05: endorse. "ey" = en.
  - L06: endorse. "ey" = en; "desfieroit" stays I.
  - L07: endorse, including "mesr'" at I. Seg1's "on" ends in the same descender loop that the reading writes as y elsewhere, and both passes read it "on".
  - L08: endorse. "qu'oy" = qu'on (the same tailed n).
  - L09: endorse. "s'ey" = s'en, twice.
  - L10: endorse.
  - L11: **correct** "sou/I" to **"soit"/M**: "so", one minim, then a t whose crossbar runs on as a hairline, the same t-bar as "tant" just
    before it, with no separate u bowl. This gives the idiom "tant soit peu". Also **upgrade** "peu/I" to **M**: a p with a crossed
    descender, then "eu", then a stop.
- **The y-for-n letterform, not a correction.** The descender-loop final the reading writes as y in "Combiey", "pleay", "ey", "qu'oy" and
  "s'ey" is this hand's tailed final n. The reading keeps the diplomatic letterform, which is right for a transcription. A phrase search must
  use the normalised forms, though, and so must anyone quoting the text. These are listed in `scripts/f61r_clear_corrections.tsv`. No grade
  changes for these.
- **Totals after verification:** 112 words, H 87 / M 17 / I 8 (was H 87 / M 15 / I 10). Corrections log: `scripts/f61r_clear_corrections.tsv`.
- **Print check.** phrases.txt already listed H-word runs, so `tools/print_check.py` was run: 12 phrases, 124 rows, 19 with hits. Requests:
  archive.org 1, be-api 24, googleapis 12, openalex 13, semanticscholar 3 (HTTP 429 after the first two phrases; stopped, not retried), crossref 2.
  The one exact IA full-text hit, "sur les lieux vous verres" in `lettresinstructi07richuoft` (Richelieu's *Lettres, instructions
  diplomatiques*, vol. 7), is a common formula in a 17th-century edition and is not taken as this letter. The Google Books and OpenAlex counts
  are loose-match volumes. A search result, not a novelty verdict (rule 10). The phrase list predates the reconciled reading. Refreshing it is
  the named next step in Remaining gaps.

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: the Remaining gap 'print search on f.61r's full clear text' -- refresh phrases.txt with the reconciled, normalised phrases of scripts/f61r_clear_reading.tsv (the y-for-n forms normalised per scripts/f61r_clear_corrections.tsv) and re-run tools/print_check.py, ~$0.5. LOCAL-QUEUE L30 and ASKS 88/89/93 stay the outside blockers for the sign gaps.
