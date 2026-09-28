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

