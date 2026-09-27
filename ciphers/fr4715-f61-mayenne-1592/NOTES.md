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

