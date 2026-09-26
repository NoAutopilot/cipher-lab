partial
Bourdeau CATALOGUE.md #338 (fresh shallow clone, HEAD fc0c9e865d0fae67ca92d19750d2b09ab11972e0, read 26 Sept 2026) read in full: "HCPortal marks all ten records 'Not solved'; no reading found"; confirmed live against HCPortal's own API (`api.hcportal.eu/api/cryptograms/496`, HTTP 200, `solution.name: "Not solved"`, 26 Sept 2026 03:41 UTC) and against Bourdeau's own harvest cache (`catalogue_harvest/hcportal/index.json`, all ten ids 496-509 `"solution": "Not solved"`, harvested by Bourdeau 23 Sept 2026); Aymeloglu's repo (fresh clone, HEAD 2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f) grepped for "malsburg", 0 hits, not in that catalogue at all; Tomokiyo/Cryptiana pages on disk (sources/cryptiana/web/) grepped for "malsburg", "hesse-kassel", "westfalen" -- the only hits are an unrelated target (Carl von Rabenhaupt 1646, to the regent of Hesse-Kassel, solved 2020, german.htm/habsburg.htm/unsolved.htm) and Antal/Zajac/Mírka's general HistoCrypt work on the same Marburg archive's ciphers, neither naming HStAM 4 h Nr. 1411; one OpenAlex query ("Malsburg 1636 Chiffre", 0 results) and one Semantic Scholar query ("Malsburg Hesse-Kassel cipher 1637", 0 results, 26 Sept 2026); one web search ("Otto von der Malsburg Chiffre 1636 1637 HStAM entschlüsselt cipher solved") returned an unrelated 1637 Kassel cipher (Heusner von Wandersleben to Oxenstierna, deciphered by Waldispühl and Kopal 2024, different sender/recipient) and no hit on this target; a second web search on the shelfmark itself ("4 h" "1411" Malsburg Marburg Chiffre Westfalen") returned nothing relevant.

# Otto von der Malsburg to the Hesse-Kassel government, 1636-37

Status: partial (LANE B7, 26 Sept 2026 05:55: homophonic control below gate at N=352, a non-test -- NEAR.md row; rule 5). See line 2 above for what was checked (26 Sept 2026).

## Target

- Sender: Otto von der Malsburg, General Commissary of Hesse-Kassel, on the Westphalian theatre of the
  Thirty Years' War.
- Recipient: the councillors of Landgrave Wilhelm V at Kassel (Hesse-Kassel government).
- Shelfmark: Hessisches Staatsarchiv Marburg, HStAM 4 h Nr. 1411 ("Korrespondenz in Chiffren mit dem
  Generalkommissar Otto v.d. Malsburg betr. Kriegführung in Münster und Westfalen"), ff. 3-33.
- Ten HCPortal records, ids 496, 497, 502, 503, 504, 505, 506, 507, 508, 509, all fond 7
  ("4 h - Kriegssachen"), folder "Folder 1411", language German, sender/recipient both "Unknown" in
  HCPortal's own structured fields (the archive description names Malsburg as the correspondent, not
  HCPortal's structured sender/recipient fields).
- Dates (from HCPortal metadata, o.s./period style, some clearly mis-year-tagged by HCPortal -- record
  506 is tagged 1636-02-23 but its description says "Message from the year 1637", so treat HCPortal's
  `date` field as unreliable and the archive's own Dec 1636 - 1637 range, and the letter text itself, as
  primary): 496 = f.3-4, 15 Jan 1637; 497 = f.12-13, 17 Jan 1637; 502 = f.14, 16 Jan 1637; 503 = f.15-17,
  30 Jan 1637; 504 = f.18, 14 Feb 1637; 505 = f.23-24, 7 Feb 1637; 506 = f.25, dated 1636 field but
  "year 1637" in description; 507 = f.28-29, 28 Mar 1637; 508 = f.30-31, 28 Mar 1637; 509 = f.32-33,
  "around 1637", three messages on one leaf-pair.

## Search log (intake, 26 Sept 2026)

1. Bourdeau's `dbourdeau/cyphersolver`, fresh shallow clone, HEAD `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`:
   `CATALOGUE.md` #338 read in full (quoted in the status line above); `oldest/scan_2026-09-23/hard_targets.md`
   #4 (a fuller writeup, same 23 Sept 2026 scan) read in full -- notes "the repo has only `marburg1635`
   (HStAM 4 d Nr. 1218, a different system)" and flags an unchecked lead: "Check whether any of the Marburg
   keys in 4 d Nr. 1219-1224 (HCPortal 519-523) fits before a blind attack" (Antal & Mírka, HistoCrypt 2022,
   "Wrong Design of Cipher Keys...Marburg", studied keys of this archive but this fond's key was not found
   among them); `catalogue_harvest/hcportal/index.json` (their 23 Sept 2026 harvest of all 1,493 HCPortal
   records) gives all ten ids 496-509 as `"solution": "Not solved"` (quoted above); `find -iname "*malsburg*"`
   over the whole clone found no dedicated solve folder. No decode/key files for this target anywhere in
   the repo. Clone deleted after reading.
2. Aymeloglu's `aaymeloglu/unsolved-ciphers`, fresh shallow clone, HEAD `2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f`:
   `grep -rin malsburg` over the whole clone: 0 hits. Not in this catalogue. Clone deleted after reading.
3. Tomokiyo/Cryptiana pages on disk (`sources/cryptiana/web/`, no live fetch): grepped for "malsburg",
   "hesse-kassel", "westfalen" case-insensitively across all files. Hits are all the unrelated Carl von
   Rabenhaupt 1646 letter to the regent of Hesse-Kassel (solved 2020 by finding the key in the archives,
   german.htm/habsburg.htm/unsolved.htm/unsolved-2026-09-24.htm) and a different 1637 Kassel-origin cipher
   (Heusner von Wandersleben to Oxenstierna, habsburg.htm's neighbouring entries reference the same general
   HistoCrypt authorship, not this fond). Nothing naming HStAM 4 h Nr. 1411 or Otto von der Malsburg.
4. HCPortal record status, live: `curl` reachability `hcportal.eu` HTTP 200, `api.hcportal.eu` (bare root)
   HTTP 404 (expected -- no root route); the documented record endpoint (from Bourdeau's
   `catalogue_harvest/hcportal/README.md`) `https://api.hcportal.eu/api/cryptograms/496` with a browser
   User-Agent and header `Origin: https://crypto.hcportal.eu` answered HTTP 200 with
   `"solution": {"id": 1, "name": "Not solved"}` -- confirms Bourdeau's harvest is current for this record,
   26 Sept 2026 03:41 UTC.
5. OpenAlex (`OPENALEX_KEY`, header auth): `search=Malsburg 1636 Chiffre`, 0 results, HTTP 200, 26 Sept 2026.
6. Semantic Scholar (`S2_KEY`, header auth): `query=Malsburg Hesse-Kassel cipher 1637`, HTTP 429 once, retried
   after a 3 s pause, HTTP 200, 0 results, 26 Sept 2026 (one retry, per the good-citizen rule).
7. Web search: "Otto von der Malsburg Chiffre 1636 1637 HStAM entschlüsselt cipher solved" -- returned an
   unrelated 1637 Kassel-to-Oxenstierna letter (Heusner von Wandersleben, deciphered by Waldispühl and Kopal
   2024) and Bourdeau's own catalogue page, no hit on this target. A second query on the shelfmark itself,
   "4 h" "1411" Malsburg Marburg Chiffre Westfalen, returned nothing relevant (only unrelated Marburg-town and
   Malsburg-Marzell results).

No reading, key or documented attempt found for HStAM 4 h Nr. 1411 in any of the seven sources checked.

`python3 tools/intake_gate_check.py malsburg-hessen-1636`:
```
malsburg-hessen-1636: open (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT: 0
```
Gate passed 26 Sept 2026 03:43 UTC. Proceeding to image fetch and sampled blind transcription.

## Pass B + first test (bMAL2, 26 Sept 2026)

Intake gate re-run by the orchestrator at brief time (04:50 UTC): `open`, exit 0. Job bMAL2 continues from bMAL's
pass A (f.3 `postscript` 8 lines/136 tokens, f.12 `postscript2` 6 lines/~110 tokens; bMAL was interrupted at
8.67/6 USD before writing its own NOTES.md section, so this is the first narrative account of what pass A covers).

Crop step (mandatory, `tools/iiif_lines.py`, numpy/pillow/scipy installed this session):
```
python3 tools/iiif_lines.py --image ciphers/malsburg-hessen-1636/images/hstam_4_h_1411_0003.jpg --out ciphers/malsburg-hessen-1636/crops/0003 --debug
  -> region 2946x2312, 30 lines, 30 bands x 2 segments
python3 tools/iiif_lines.py --image ciphers/malsburg-hessen-1636/images/hstam_4_h_1411_0012.jpg --out ciphers/malsburg-hessen-1636/crops/0012 --debug
  -> region 2834x4284, 64 lines, 64 bands x 2 segments
```
Debug overlays checked (both kept in crops/*/[]_lines_debug.jpg). f.3's postscript (pass A's 8 lines) is the
numeral block below the signature at the very bottom of the page, lines L24-L30 of the auto-detector plus one
line the detector missed below its last band (image y 2047-2110, saved manually as L31_s1.jpg, box added to
manifest.json with a note) -- the detector's region bottom (y=2047) fell short of the actual page bottom
(y=2312) by 265px, cutting off the 8th line. f.12's postscript2 (pass A's 6 lines) is NOT the first numeral
block encountered after "Datum den 17/7 Januarij Ao 1637" (that block runs 11 lines total, L39-L49); pass A's
6 lines are the LAST 6 of those 11 (L44-L49) -- confirmed by exact token match: pass A line 1 (47 O 60 93 54 61
7 97 95 10 16 63 18 61 83 129 76 G 42, 19 tokens) reads identically off crop L44. Lines L39-L43 (the first 5 of
the 11) are untranscribed by either pass -- flagged below as a follow-up, out of this job's scope. f.12 also
carries a THIRD cipher-looking passage below the two signatures, in a visually different hand/alphabet (mixed
case letters and digits, no dot-separated numeral groups, marked "cifrat cela" in the margin) -- also untouched,
also flagged below.

Pruned crops/0003 and crops/0012 to only the 14 line-crop files actually used (8+6) plus each debug overlay and
manifest.json, after the full 60+128 auto-detected crops pushed the folder to 31 MB (over the 30 MB rule);
manifest.json still records every auto-detected line's box for a future worker who wants the rest re-cut from
the images already on disk.

**Blind-pass integrity note:** before writing this section, the worker ran `head -20` on pass_a_0003.tsv and
pass_a_0012.tsv to check the column format, which incidentally displayed pass A's actual token values for f.3
line 1 (17 tokens) + line 2's first 2 tokens, and f.12 line 1 (19 tokens) in full -- more than the "FORMAT only"
allowance in the brief. To keep pass B itself genuinely blind despite this, the actual transcription was
delegated whole (both leaves, all 14 lines) to a fresh Sonnet subagent given only the 14 crop image paths above,
with no mention of pass A, its tokens, or expected line/token counts; the subagent's own context has no exposure
to the values the worker saw. The worker's own line-boundary identification (which physical image rows are the
postscript blocks) rests on the manuscript's visible layout, not on pass A token values, except for the one
cross-check quoted above (matching pass A's already-seen line-1 tokens against crop L44 to confirm the f.12
block-start hypothesis) -- that check confirms a boundary, not a token reading, and no pass_b value was copied
from it. Recorded here in full per rule 7/10's honesty convention rather than left for a QA pass to catch.

## Reconcile + first test (bMAL3, 26 Sept 2026)

Continues bMAL2 (interrupted at 2.2x cap before reconciling; pass A/B of f.3 and f.12 postscripts were
already committed). Intake gate re-run: `python3 tools/intake_gate_check.py malsburg-hessen-1636` -> `open`
(line 1), exit 0.

Reformatted pass_a/pass_b TSVs so each line id matches its crop file stem (`hstam_4_h_1411_0003_L24_s1` etc.,
`transcription/*_r.tsv`, not committed as core artifacts -- regenerable from the pass files and the crop
manifest), then:
```
python3 tools/reconcile_passes.py transcription/pass_a_0003_r.tsv transcription/pass_b_0003_r.tsv --crops crops/0003 --out-dir recon_0003
  -> lines 8  signs A 193  B 192  agree 174/194 = 89.7%
python3 tools/reconcile_passes.py transcription/pass_a_0012_r.tsv transcription/pass_b_0012_r.tsv --crops crops/0012 --out-dir recon_0012
  -> lines 6  signs A 159  B 159  agree 153/159 = 96.2%
```
Matches bMAL2's own reported figures exactly.

**Disagreements settled from the image, not guessed.** 26 rows in disagreements.tsv (20 f.3, 6 f.12), all 26
opened at the named crop (well under the 40-row cap), most re-zoomed 5-14x with PIL crops of the specific
column to compare digit shapes against unambiguous agreed tokens elsewhere in the same line (the local "4"
always has a closed triangular top + crossbar, the local "7" an open diagonal, "2" a curl-top, "9" a full
loop, "6" a hook-tailed loop, "0" a plain circle -- distinguishable once compared side by side at high zoom).
23 of 26 settled to H by this method (12 to pass A's reading, 11 to pass B's -- neither pass is
systematically better). One row (f.3 line 6, cols 11-12, `9`/`38` in pass A vs one token `930` in pass B):
the image shows no dot separating the digits (they are one connected stroke run under an ink blot on the
middle digit) -- reconciled as a SINGLE 3-digit token `930`, kept at grade M because the blot leaves the
exact digits uncertain even though the token count is now settled. Two rows (f.3 line 7 `hstam_4_h_1411_0003_L30_s1.jpg`,
cols 12-13) sit under a genuine water/ink stain; re-examined at 10x, neither pass's reading nor a third one
could be read with confidence -- left at grade M, marked UNSETTLED in ciphertext.txt's `why` column, per
CLAUDE.md item 2 (image over transcription; a negative/uncertain reading is conditional on what the image
actually shows, not filled in to make agreement look better).

`ciphertext.txt` written (line/position/sign/confidence/alt/why, one row per sign, both leaves): N=352 sign
tokens (351 numeral/mark signs + the one clear word "Und"), K=95 distinct sign values, 27 singletons, 3 rows
at M (the blotted 930 and the two stained-illegible tokens), the rest H.

**Nomenclator flag.** K=95 at N=352 (K/N=0.27, 27 singletons) is well above the brief's ">~60 distinct with
many singletons" heuristic -- treated as a nomenclator/code+mark design, not a plain substitution alphabet.

**Spec written**: `specs/malsburg-hessen-1636.json`, judge `language: "de"` (resolves to the de16 Early New
High German corpus, `tools/judge_plaintext.py`'s only German default) with an explicit era-flag: this is a
1637 letter, roughly a century later than de16's register and much earlier than the only alternative on file
(de20, 1880-1940 prose) -- neither corpus is era-matched; de16 used as the closer available option, any
FAIL/PASS below is a de16-register verdict, not a verdict on 1637 chancery German specifically (CLAUDE.md
rule 3's pt17/pt18/es17c corpus-era lesson).

**First cheap test.** `tools/freq.py` on the reconciled numeral stream: IC 0.0143 vs flat-over-94-symbols
0.0106 (about 35% above flat -- a mild, not strong, skew consistent with a real nomenclator's uneven code
reuse; not comparable to German letter-level prose IC ~0.076, which is computed over a ~26-symbol alphabet,
not 94). `tools/family_run.py --family masc --seeds 3` (control first, per rule 3): CONTROL mean 0.987
(0.980-1.000, gate 0.6 met) but masc's control is built over K=22 letters, not the target's real K=95 --
**not a matched design** for a 95-code nomenclator (this is exactly the brief's own ">~60-K" carve-out; run
anyway for the record since the brief listed it first). TARGET best score -780.425, judge FAIL: score
-1.472, below even the shuffled-null bar (null_p99 -1.618) against de16. `--family homophonic --param
profile=target --seeds 3` (the actually-matched design at K=95): CONTROL mean 0.392 (0.318-0.511) is BELOW
the 0.6 gate -- **CONTROL BELOW GATE, non-test**, target not run. Both rows in HYPOTHESES.md. The homophonic
control's own failure to read a synthetic 95-code nomenclator at N=352 says the anneal doesn't have enough
signal at this length/K to be a fair test either way, matched or not -- not a negative on the target, a
statement about what N=352 signs can support for this design (rule 3's own headline: a control below its
own gate licenses nothing).

**Next step (not this job):** pool the fond. Test 2 in the spec -- fetch and reconcile the other eight
HCPortal records on HStAM 4 h Nr. 1411 (502-509) to get above the sign-pool threshold before a from-scratch
attack, per CLAUDE.md's pools-first selection rule; a single ~350-sign postscript is short for K=95.

Hosts: none (crops on disk, no fetch this job).

## Pooled-N control and leaf extent (bMALC, 26 Sept 2026)

Intake gate re-run: `python3 tools/intake_gate_check.py malsburg-hessen-1636` -> `malsburg-hessen-1636: partial
(line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

**A. Projected-N control.** `tools/family_run.py` always overwrote `params["N"]` with the target's own
ciphertext length, so a control at a pool size larger than what's on disk could never be run -- added
`--control-n N` (valid only with `--control-only`; keeps the target's own K, scales any `profile=target`
sign-count profile proportionally to N; offline test in `tools/tests/test_family_run.py`). Ran the homophonic
family (the matched design for this K=95 nomenclator) control-only at N=1000, 2000, 3000, 3 seeds each,
serialized (no concurrent CPU work in this box, each battery took well under a minute):

```
python3 tools/family_run.py specs/malsburg-hessen-1636.json --family homophonic \
  --cipher ciphers/malsburg-hessen-1636/ciphertext.txt --param profile=target \
  --control-only --control-n N --seeds 3 --gate 0.6 --label "bMALC pooled-N control"
```

| N (projected) | K | control mean (range) | gate 0.6 |
|---|---|---|---|
| 352 (actual, bMAL3) | 95 | 0.392 (0.318-0.511) | NOT met |
| 1000 | 95 | 0.928 (0.867-0.964) | met |
| 2000 | 95 | 0.844 (0.710-0.957) | met |
| 3000 | 95 | 0.976 (0.970-0.984) | met |

Rows in HYPOTHESES.md. The gate the actual N=352 control could not meet is comfortably met by N=1000 and
stays met (with some seed-to-seed noise at 2000, which is not monotonic but every seed at every N clears
0.6) up to 3000 -- pooling the fond is worth paying for, on this test alone.

**B. Per-leaf cipher extent, before paying for 14 leaves.** `tools/iiif_lines.py --image <leaf> --out
crops/<leaf> --debug` run on all 16 remaining images (records 502-509's 14 leaves, plus ff.4 and 13, the
address-panel leaves of records 496/497 that pass A/B/bMAL3 did not need); one low-resolution look at each
leaf's debug overlay (no transcription) to count cipher lines vs clear lines and estimate signs at roughly
the density already measured on f.3/f.12 (~17-27 signs/line). Full table in `extent.tsv`. Findings, by
record:

- 496 (f.3 done, f.4 remaining): f.4 is the outer address/cover panel (2 wax seals, address in clear,
  everything else is ink bleed-through from f.3) -- 0 cipher.
- 497 (f.12 partly done, f.13 remaining): f.13 is likewise the outer address/cover panel -- 0 cipher. (Note:
  f.12 itself still has 5 untranscribed cipher lines, L39-43, and a third "cifrat cela" passage in a
  different hand/alphabet, per bMAL2 -- neither is on this job's leaf list and neither is counted below; a
  gap for the next transcription job to close.)
- 502 (f.14, one leaf): ~30 lines dense cipher (~600 signs est.) framed by clear salutation/close; a further
  passage in a second, looser hand at the very bottom is unclassified.
- 503 (f.15-17, three leaves): f.15 has one short cipher passage embedded mid-letter (~5 lines, ~120 signs)
  in an otherwise clear letter; f.16 opens with ~6 clear lines then is dense cipher for the rest (~38 lines,
  ~760 signs) -- the image is a two-page opening and its right-hand panel (a clear-text name/docket list) is
  a separate item, not counted; f.17 is the address/cover panel, 0 cipher.
- 504 (f.18, one leaf): a short self-contained letter, ~24 lines dense cipher (~480 signs) between a clear
  salutation and a clear, dated, signed close.
- 505 (f.23-24, two leaves): f.23 opens with ~8 clear lines then is dense cipher to the end of the leaf
  (~44 lines, ~880 signs); f.24 continues the cipher for ~9 more lines (~180 signs) then closes in clear
  with signature and a clear postscript in a second hand.
- 506 (f.25, one leaf): ~12 clear lines then continuous cipher to the signature (~26 lines, ~520 signs).
- 507 (f.28-29, two leaves, 28 Mar 1637): f.28 opens with ~3 clear lines then is dense cipher for the rest of
  the leaf (~52 lines, ~1040 signs); f.29 continues cipher for ~26 more lines (~520 signs) then closes in
  clear with a postscript about a 12,000-Reichsthaler Bremen matter.
- 508 (f.30-31, two leaves, also 28 Mar 1637): same shape as 507 -- f.30 ~55 cipher lines (~1100 signs), f.31
  ~19 more (~380 signs) then the same Bremen/ducats postscript almost verbatim. Same date and matching
  postscript wording as 507; read as a second copy or route of the same dispatch, not independent plaintext
  -- flagged for whoever pools these two records, since pooling near-duplicate plaintext under one K=95 key
  is still a valid signal source (it is real ciphertext of the same design) but is not two letters' worth of
  independent content.
- 509 (f.32-33, "around 1637", three items per the archive description): f.32's first item (French, "Haut et
  Puissant Seigneur...") is entirely clear, no cipher; its second item (German, headed "Extrait", dated
  26 Mart[ii] 1637) and the dispatch items continuing onto f.33 (5 April, 26 Mart[ii], 27 Marti 1637) carry
  cipher codes interspersed among mostly-clear prose, not solid cipher lines -- counted by token (~60 on
  f.32, ~40 on f.33), not by line, and much less certain than the solid-block estimates above.

**Sum of estimated additional signs (extent.tsv, rough, unconfirmed): ~6680**, against the already-committed
N=352. Even discounting the two least-certain leaves (509's ~100 interspersed-code signs) and the near-
duplicate risk on 507/508, the fond comfortably clears every N tested in part A (1000/2000/3000) many times
over -- this is not a marginal pooling case.

**Which leaves to transcribe first:** the four fullest, cleanest, single-hand cipher pages -- f.28 (507,
~1040 signs), f.30 (508, ~1100 signs), f.23 (505, ~880 signs), f.16 (503, ~760 signs) -- would alone put the
pool over 3000 signs (plus the existing 352) with their completing leaves (f.29, f.31, f.24) needed to close
each letter. f.14 (502, ~600) and f.25 (506, ~520) are good next adds. Leave f.4/f.13/f.17 (address panels,
0 signs) and f.32/f.33 (mostly clear, interspersed codes only, hardest to transcribe blind) for last, and
note the 507/508 near-duplicate when weighing whether both are worth the double transcription cost.

Hosts: none (all 16 images already on disk). Tool changes: `tools/family_run.py` (`--control-n`),
`tools/tests/test_family_run.py` (offline test for it). Folder shrunk back under 30 MB by deleting the 16
new debug-overlay directories after reading them (regenerable in one command each, same as recorded above
and in extent.tsv); `crops/0003` and `crops/0012` (pass A/B's own committed crops) untouched.

## 507/508 duplicate test (bMALDUP, 26 Sept 2026)

Intake gate re-run: `python3 tools/intake_gate_check.py malsburg-hessen-1636` -> `partial` (line 1), exit 0.

**Question.** extent.tsv flags 507 (f.28-29, 28 Mar 1637) and 508 (f.30-31, same date) as visually near-
identical (same header wording, same Bremen/ducats postscript). Is 508 a literal copy of 507's ciphertext,
the same plaintext re-enciphered with different homophone choices, or two different texts that only look
alike at a glance?

**Leaf layout (read off the debug overlays before cropping).** Both leaves open with a heading + salutation
+ one sentence of clear German carrying the "hujus"/"Im diploschab" dating phrase (f.28 L01-L04, f.30
L01-L04, wording near-identical between the two), then dense digit-group cipher begins at L05 on both
leaves. Crops cut for lines L05-L14 only (10 lines each), `tools/iiif_lines.py --image
ciphers/malsburg-hessen-1636/images/hstam_4_h_1411_0028.jpg --out ciphers/malsburg-hessen-1636/crops/0028
--debug` -> region 2126x2546, 57 lines; same for `_0030.jpg` -> region 2084x2548, 59 lines. Both debug
overlays checked by eye; pruned to the 10 used crops + overlay + manifest per leaf after cutting (manifest.json
keeps every auto-detected line's box for a future worker).

**Two blind passes per leaf** (4 Sonnet subagent calls, one per leaf per pass, each given only that leaf's
10 crop paths, no cross-leaf or cross-pass exposure), reformatted to the `line pos sign` convention and
reconciled with `tools/reconcile_passes.py`:

```
f.28: pass A 495 signs, pass B 477 signs, agree 328/497 = 66.0% (nw), 169 disagreement columns
f.30: pass A 451 signs, pass B 448 signs, agree 355/464 = 76.5% (nw), 109 disagreement columns
```

Agreement is well below bMAL3's f.3/f.12 figures (89.7%/96.2%) -- these crops are denser, lower-contrast
cursive with more compressed digit groups, and the two passes disagree on far more columns (278 total) than
this job's budget could settle one-by-one against the image (the brief anticipated "at most 15" crops for
disagreements, sized against bMAL3's ~10% rate, not this ~30-34% rate). **Disagreements were NOT individually
settled from the image in this job** -- `recon_0028/ciphertext_draft.tsv` and `recon_0030/ciphertext_draft.tsv`
carry the reconciler's majority/pass-A-preferred pick at grade M wherever the two passes differed (169/497 and
109/464 rows respectively); this section's alignment numbers below are built on those M-heavy drafts, not an
H-grade reading, and are graded S (cryptanalytic signal) throughout, not C or H. A follow-up that wants an
H-grade transcription of these 20 lines needs a third pass or per-disagreement image zoom, out of this job's
scope/budget.

**Alignment test** (`dup_align.py`, scratch script, output kept as `dup_align.tsv`/`equivalences.tsv`):
Needleman-Wunsch global alignment (match +1, mismatch -1, gap -1) of the f.28 draft sign sequence (497 signs)
against the f.30 draft sign sequence (464 signs); identity = aligned non-gap columns with equal sign.

```
TARGET   f.28 vs f.30                                    : 210/447 aligned columns identical = 0.4698
CONTROL-A f.28 vs recon_0003+recon_0012 (different, already-reconciled H-grade text, same cipher/design)
                                                           : 40/349 = 0.1146
CONTROL-B f.28 vs 200 shuffles of f.30's own groups (seed 20260926)
                                                           : mean 0.1137, p95 0.1378, p99 0.1466, range 0.0788-0.1524
```

Target identity (0.470) is well above both controls (a different genuine text at 0.1146; 200 label-shuffles
of f.30 itself at mean 0.1137, p95 0.1378) -- about 3.4x the shuffle p95, not a coincidence at this N. It is
**not** near 1.0, so this is not a byte-for-byte identical ciphertext copy. Per the brief's own verdict rule
(copy near 1 / re-enciphered well-above-control with structured differing pairs / different texts at control):
this reads as **same plaintext, re-enciphered** (or read through transcription noise of a copy -- see caveat
below), not two independent letters.

**Differing pairs (equivalences.tsv, 210 distinct aligned pairs, grade S candidates, not a key).** A
substantial share look like transcription artifacts common to cursive digit-group reading rather than real
cipher differences: 12 pairs are flagged `likely_transcription_noise=yes` by a simple digit/letter-confusion
rule (`1`<->`i`, `0`<->`O`, any `ILLEGIBLE`), e.g. `16<->i6` x5, `11<->ii` x3, `31<->3i` x3 -- the established
f.3/f.12 H-grade alphabet (`ciphertext.txt`) uses only 2-digit numbers plus a handful of capital-letter marks
(D, G, H, L, N, O, S, W, X, Y, #); it has **no** lowercase `i` or `z` sign anywhere, which is strong
circumstantial evidence that this job's blind passes are misreading a numeral shape as a letter on these
denser lines, on both leaves, in both passes -- not that f.28 and f.30 genuinely differ there. A `z`-tailed
mark appears very often in this job's transcriptions (`zz`, `1z`, `4z`, `z9`, `z5`, etc.) and is NOT flagged
noisy by the simple rule above (it doesn't map cleanly to a known digit), but given it is equally absent from
the established alphabet, its status is unresolved -- flagged here rather than silently trusted. The clean
(non-letter-confusion) recurring differing pairs are pure digit-for-digit swaps: `5i<->6i` x4 (itself
z/i-adjacent, treat with the same caution), `30<->36` x3, `70<->40` x2, `74<->44` x2, `87<->67` x2 -- too few
confidently-clean recurring pairs, and too much plausible noise in the rest, to promote any of them to a
grade-M or grade-H equivalence without image-level digit-shape zoom (bMAL3's method: compare against
unambiguous agreed tokens elsewhere in the same line at 5-14x). **Net read: the true identity share between
f.28 and f.30 is very likely higher than 0.470** (the noise floor from two independent low-resolution blind
passes plausibly explains much of the 53% mismatch), but this job's data cannot distinguish "same text,
re-enciphered with some different homophone choices" from "same text, transcribed noisily but actually closer
to a literal copy" -- both are consistent with what was measured. Either way, 507 and 508 are not independent
plaintext content, confirming extent.tsv's flag: whoever pools the fond (per bMALC's next-step note) should
NOT count f.28-29 and f.30-31 as two letters' worth of independent signal, only as (at most) one plaintext's
worth of ciphertext with a second, less-certain data point on that plaintext's key relationship.

**Verdict: `partial` / re-enciphered-or-noisy-copy** (grade S, well above a matched control but not at copy
identity 1.0 and not resolvable further within this job's transcription quality). Not `closed-negative` --
this is a positive relatedness signal, not a negative (rule 5 does not apply; this was never a solve attempt).

Files: `transcription/pass_{a,b}_00{28,30}.tsv` (+ `_r.tsv` reformatted), `recon_00{28,30}/` (disagreements,
ciphertext_draft, agreement), `crops/00{28,30}/` (10 line crops + debug overlay + manifest each, pruned),
`dup_align.tsv` (full aligned pair list), `equivalences.tsv` (210 differing pairs with noise flag).

Hosts: none (all images already on disk).

### Orchestrator check of bMALDUP's verdict (LANE B8, 26 Sept 2026 08:03 UTC)

The identity share (0.470 vs controls 0.115 / p95 0.138) shows ff.28 and 30 carry the same text. It does NOT by itself separate
"copy" from "re-enciphered". Checked from dup_align.tsv (script in the orchestrator's session, rerunnable from the file):
of 237 aligned substitutions, 123 differ in one digit (68/66, 57/37, 95/93) and several only in case (D/d, V/v, N/n);
of the 50 f.28 groups substituted more than once, only 2 always map to the same f.30 group. Homophone re-encipherment
would give consistent pairs; this pattern is transcription noise (pass agreement was only 66/77%). Working reading:
**a copy read through noise**, pending a settle on the crops. Consequence: `equivalences.tsv` is NOT a list of
equivalences and must not feed a key (grade nothing from it). Useful instead: the second copy is a free extra witness
when transcribing 507 -- transcribe ff.28-29 once, and use ff.30-31 only to settle disagreements.

## Glyph conventions (bMALG, 26 Sept 2026)

Intake gate re-run: `python3 tools/intake_gate_check.py malsburg-hessen-1636` -> `malsburg-hessen-1636: partial
(line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

**Question.** ff.3/12 (bMAL3, H-grade, N=352) have no lowercase `i` or `z` sign anywhere in the established
alphabet (95 values: 2-3 digit numbers, single digits `4`/`7`, and the marks D/G/H/L/N/O/S/W/X/Y/#/Und). ff.28/30
(bMALDUP)'s blind passes wrote `i` and `z` constantly (`ii`, `i6`, `zz`, `1z`...) and pass agreement fell to
66.0%/76.5% (nw). Census of all 8 pass TSVs (`transcription/pass_{a,b}_{0003,0012,0028,0030}_r.tsv`): 0003/0012
have zero letter-containing signs; 0028/0030 have ~150 distinct letter-containing readings, dominated by `i`/`z`
compounds (`ii` 62, `zz` 61, `i6` 36, `6i` 32, `3i` 27, `5i` 26, `z6` 25, `7i` 23, `7z` 23, ... down to singletons).

**`i` = digit `1` (H, shape-settled).** Both passes independently AGREE (ciphertext_draft H rows) on tokens like
`ii` (0028 L07 c17), `i6` (0028 L08 c12, c27), `6i` (0028 L08 c30, c39) -- not just disagreements. Zoomed 10-12x
on 0028 L08 cc.23-24 (`i0`, `i6`) against the line's own agreed digit `1` in `51`/`107` (cc.1-4, also H-agreed):
same short vertical stroke with a raised dot/flick in both places -- this hand's numeral `1` carries a dot that
makes it read as a lowercase dotted `i` to a blind transcriber, not a separate sign. Disagreements.tsv shows the
identical pattern at token level, both leaves: `10/i0`, `16/i6`, `31/3i`, `51/3i`, `13/i3`, `149/i49`,
`15/i5`, `193/i7i`, `148/i48` etc. -- one pass reads `1`, the other `i`, rest of the token matches, no
counter-example found in either leaf. **Mapped `i`->`1` wherever the letter appears alone or fused with a digit
(`ii`->`11`, `i6`->`16`, `6i`->`61`, ...), grade H.**

**`z` = most likely digit `2`, grade M (not shape-settled).** `z` behaves differently from the established marks:
D/G/H/L/N/O/S/W/X/Y/# never fuse with a digit anywhere in the H-grade ciphertext.txt (checked: all 20 occurrences
across f.3/f.12 stand alone), but `z` fuses with a digit in the large majority of its ~330 occurrences (`4z`,
`z6`, `zz`, `7z`, `z5`, `z9`...) -- not the same kind of sign. Disagreement pairs where the position and the other
digit match and only `z`-vs-a-digit differs: 9 clean pairs read `2` in one pass, `z` in the other (`z5/25` x2,
`z4/24`, `8z/82`, `z73/273`, `z00/200`, `z6/26`, `z9/29` x2) against 2 clean pairs against `3` (`z/3`, `4z/43`).
Zoomed 10x on 0030 L14 (the densest run of z/2 disagreements) and on 0028 L06/L08's `4z`/`7z`: the stroke is a
sharp angular diagonal, sometimes doubled (`zz`), distinct at this resolution from the established `2` shape
(open curl-top) or `3` shape (double hump) elsewhere in the same lines, but the visual check could not confirm
digit identity to H -- consistent with a period numeral `2` given a hooked/looped cursive tail in this denser
hand (a documented period form), but not ruled out as a distinct 12th mark. Kept at **grade M: canonical `2`,
majority hypothesis from the 9:2 disagreement-pattern count, not confirmed by shape alone.** A future job with a
third pass or per-token image zoom (bMALDUP's own recommendation) should settle it properly; do not promote to H
without that.

**Compounds.** `glyph_map.tsv` mechanically substitutes `i`->`1`, `z`->`2` character-wise for every distinct raw
pass reading of length <=3 that consists only of digits plus `i`/`z` (59 rows, 23 H / 36 M). Longer merges
(`zz7i`, `z778`, `9z239`, `733i`, `iz55`...) are NOT mapped -- these look like token-boundary/segmentation
disagreements between the two passes (bMALDUP already flagged `zz`+`7i` fusing into one pass's `zz7i` where the
other kept two tokens), a different question from glyph shape, and mapping them would fabricate 4-5 digit "codes"
outside the established 1-3 digit design. They stay open disagreements for a future per-token image settle.
Signs mixing `i`/`z` with any other unvalidated letter (`yi`, `ib`, `4ud`, `bLS`...) are likewise left unmapped.

**Degenerate-optimum check (brief's own warning).** Applying only the H-grade rows (`i`/`ii` and their digit
compounds, `glyph_map_H_only.tsv`, 24 rows) already recovers real signal without touching the uncertain `z`
rows -- ruling out that the gain is manufactured by folding everything into one bucket:

| leaf | baseline (bMALDUP) | H-only (`i`/`ii` compounds) | H+M (full map, incl. `z`/`zz`) |
|---|---|---|---|
| f.28 (0028) | 328/497 = 66.0% | 357/497 = 71.8% | 364/497 = 73.2% |
| f.30 (0030) | 355/464 = 76.5% | 359/464 = 77.4% | 368/464 = 79.3% |

H-only accounts for most of the gain on f.28 (+5.8 of +7.2 points) and about half on f.30 (+0.9 of +2.8 points);
`z` adds a further, smaller, still-real improvement on top, consistent with a real but less certain effect
rather than one mapping doing all the work. `recon_0028/` and `recon_0030/` (disagreements.tsv,
ciphertext_draft.tsv, agreement.tsv) are overwritten with the H+M run above, superseding bMALDUP's raw-noise
draft; `equivalences.tsv`/`dup_align.tsv` from bMALDUP are untouched (out of scope, already flagged unusable by
the orchestrator's check).

**Case: D/d, V/v, N/n -- not significant, transcription noise.** Direct same-position evidence: 0030 L06 c3, pass
A wrote `v`, pass B wrote `V` for the identical stroke (disagreements.tsv) -- the only clean case-only swap found,
and it matches how `V` behaves everywhere else in this job's data (8 other occurrences, all capital, all
standalone, all either agreed or off by a digit elsewhere in the line, never a segmentation change). `D`: 0028 has
4 consistent capital `D` readings (both passes, 4 positions) matching the established mark; 0030's 2 lowercase `d`
readings come from pass A alone with no `D`/`d` agreement from pass B at either position -- one-sided, read as
pass-A noise on a hard leaf, not a genuine `d` sign. `N`/`n`: `N` is a well-established, frequently-agreed
standalone mark (e.g. 0028 L08 c29, H); the 4 lowercase `n` occurrences sit in positions where the other pass
reads something structurally unrelated (`i03`, other multi-char noise), not a same-stroke case swap like `V`/`v`
-- **not** treated as a case variant of `N` and not merged into it (would be exactly the degenerate-optimum
folding the brief warns against); left as unresolved noise. **Convention: canonical case is always the capital
mark (D, N, V, ...); a lowercase reading of a known mark is transcriber noise, but a lowercase letter that does
not correspond to any known mark in context (like most of the `n` instances) is not automatically that mark.**

**Other marks noticed, out of scope for this job.** 0028/0030 also show standalone capital marks absent from the
f.3/f.12 alphabet -- `V` (8x), `T` (11x), `K`/`R`/`B`/`E`/`F`/`M`/`C`/`Q` (2-4x each), and a capital `Z` (distinct
from lowercase `z`, 4x, e.g. `Zoo`/`z00` disagreement at 0028 L14/0030 L14) -- plus a recurring compound
(`du`/`Xu3`/`Xu5`, 3-4x, likely one more mark or abbreviation, not resolved here). These are a mark-inventory
question for a future job, not this one; flagged here per rule 7 rather than investigated.

**Instruction for the next transcription/pass subagent (paste verbatim):** "This leaf's cursive `1` is written
with a raised dot and will look like a lowercase `i` -- read it as `1`. A sharp angular diagonal stroke, often
doubled, that doesn't match any digit or the established marks (D,G,H,L,N,O,S,W,X,Y,#) may be the digit `2` in a
hooked cursive form, or may be a separate sign -- transcribe it as `z` (not as `2`, not merged into the next
digit) and let reconciliation apply the convention; do not guess between the two. Marks are always capital and
always their own token, never fused to a digit (`D`, `N`, `V`, `G`, `H`, `L`, `O`, `S`, `W`, `X`, `Y`, `#`); if you
write one lowercase, it will be corrected by convention, not treated as a different sign."

**Tool.** `tools/reconcile_passes.py --sign-map FILE` (new): reads `pass_reading`/`canonical` columns from a TSV
(other columns ignored) and substitutes the exact raw token for its canonical value in every pass before
alignment, so a reading that only differs by this kind of glyph convention stops scoring as a disagreement.
Offline test added (`tools/tests/test_reconcile_passes.py`, three checks: no-map baseline, mapped full agreement,
draft carries canonical signs) -- `python3 tools/tests/test_reconcile_passes.py` exits 0.

Files: `glyph_map.tsv` (59 rows), `glyph_map_H_only.tsv` (24-row H-grade subset, for the before/after check
above), `recon_0028/`, `recon_0030/` (re-run with the full map), `tools/reconcile_passes.py`,
`tools/tests/test_reconcile_passes.py`.

Hosts: none (all work from images and pass TSVs already on disk).

## Record 507 f.28 (bMAL28, 26 Sept 2026) -- PARTIAL, stopped at cost cap

Intake gate re-run: `python3 tools/intake_gate_check.py malsburg-hessen-1636` -> `partial` (line 1), exit 0.

**Scope.** f.28 has 57 detected lines total (`tools/iiif_lines.py`, region 2126x2546, matches bMALC/bMALDUP's
prior count exactly); L01-L04 are the clear salutation, L05-L57 (53 lines) are cipher. L05-L14 (10 lines) already
had two reconciled blind passes from bMAL2/bMAL3/bMALDUP/bMALG. This job's remit was the remaining ~42-43 lines
in 5 blocks of <=10 lines each, two fresh blind Sonnet-subagent passes per block, reconciled with the bMALG sign-map,
settled against f.30 as witness, then `tools/leaf_pool_gate.py`.

**Done: blocks 1-3 (L15-L44, 30 lines), two blind passes each** (6 subagent calls: `pass_{a,b}_0028_b{1,2,3}.tsv`).
Re-cut f.28's full 57-line crop set and f.30's full 59-line set (`tools/iiif_lines.py`, byte-identical manifest
boxes to bMALC's prior sweep) so blocks 4-5's crops are on disk for a follow-up job even though this job did not
reach them.

**Not done: blocks 4-5 (L45-L57, 13 lines).** This job hit its cost cap before starting them. Per Usage 6/CLAUDE.md
cost discipline ("stop before starting a unit that would cross 80% of cap"): after block 2 (4 calls) the
orchestrator-read cost was already 70.4% of the $12 cap (one of the 4 calls ran far outside the ~$0.9/call estimate
this job's brief was priced on -- 216,829 subagent tokens and 178 tool-use turns vs ~100k tokens/12 tool-uses for
the other three -- a single-call overrun the wall-clock box cannot catch, the same shape as CLAUDE.md Usage 6's
GOLD-4D/AT55V/AX-COMP2 paragraphs, here on a call-count-priced job rather than a page-count-priced one). After
block 3's two calls the cost was 90.5%, past the 80% stop line -- this job stopped there rather than starting
blocks 4-5, and did not attempt per-image disagreement settling either (see below), which would have needed more
image-reading turns at a point where none of the remaining ~$1.15 was budgeted for it.

**Finding: embedded clear-text spans mid-cipher, not previously flagged.** bMALDUP/bMALC's extent estimate called
f.28 "dense cipher for the rest of the leaf" from a low-resolution overlay glance, with no line-by-line read. Both
blind passes on block 3 (L35-44), independently and before either saw the other's work, flagged short clauses of
ordinary German cursive prose embedded mid-line in the cipher stream, not cipher groups:
- **L36**: pass A "hiet dab allb so muss zufordern sein Vnd hernacher antwortling", pass B "bin dab allß so muß zu
  fordern was fleiß haben allein" -- both passes agree this is prose starting "...(h)ie(t)/bin da(b)(s) all(e/es)(s)
  so mu(s)(s)(s) zu fordern..." at the same line position (between cipher runs "...79.63." and "...54.61.z.S.W...").
  Neither reading is confident enough to grade above M; a dedicated zoom pass is needed to fix the wording.
- **L39**: pass A "wollest das fromm ding schreiben nach massgab wiederumb alsofort seyn", pass B "welfat das frinom
  fing forüben nach maening kagen wiedert alsint frim" -- same location (between "...16.z." and "71.83.z6..."),
  same rough shape ("...das from(m) ... nach ma(ss/ening) ... wieder(umb/t) al(so/sint) ..."), same low confidence.
- **L44**: pass A read a third short clause here ("ich diss mahl etwas gewesen", flagged as its own most-uncertain
  reading); pass B flagged the same position as prose but returned `[PLAIN:ILLEGIBLE]` rather than guessing words.
  Weakest of the three -- may be prose, may be a garbled mark run; needs the image, not adjudicated here.

This is a genuine finding worth flagging for whoever transcribes blocks 4-5 or settles these three spans: f.28 is
not solid nomenclator code throughout, it has short plaintext asides bracketed by cipher on at least two (possibly
three) lines, which changes the sign-pool accounting in bMALC's extent.tsv (those spans are prose, not additional
K=95 signs) and could itself be a crib if the wording is fixed by a careful image zoom. Not resolved by this job
(out of budget); the `[PLAIN:...]` tokens are carried into the reconciled draft below as their own aligned column
(`--keep-plain`), not dropped, so they are visible to whoever settles them next.

**Reconciliation (L05-L44, 40 of 53 cipher lines).** Concatenated the existing L05-L14 reformatted passes
(`pass_{a,b}_0028_r.tsv`) with the three new blocks into `pass_{a,b}_0028_full.tsv`, then:
```
python3 tools/reconcile_passes.py transcription/pass_a_0028_full.tsv transcription/pass_b_0028_full.tsv \
  --sign-map glyph_map.tsv --crops crops/0028 --out-dir recon_0028_full --keep-plain
  -> lines 40  signs A 1797  B 1742  agree 1404/1827 = 76.8% (nw); disagreement columns 423
```
Per-line agreement 55.6%-93.3% (`recon_0028_full/agreement.tsv`), consistent with bMALDUP's 66.0-76.5% on the same
leaf's denser lines and above bMAL3's cleaner f.3/f.12 postscripts (89.7/96.2%) only where the line itself is
cleaner (L17 87.2%, L23 93.3%) -- no single block is uniformly worse, agreement varies line by line with local
ink quality.

**Settling: NOT done.** 423 disagreement rows over 40 lines is far beyond the brief's own "at most 60" settling
budget, and this job had no cost margin left to open even 60 image pairs against the f.30 witness (each settle
needs the f.28 crop, the aligned f.30 crop found by neighbouring-agreed-group position, and often a zoom crop of
each -- the method bMAL3/bMALG used). `recon_0028_full/disagreements.tsv` (423 rows) and `ciphertext_draft.tsv`
(1827 signs, all disagreement positions at grade M per the reconciler's default) are committed as-is, unsettled,
for the next job. f.30's full L15-L59 crop set is on disk and pushed for that job to use directly.

**Gate (mechanical, on the unsettled draft):**
```
python3 tools/leaf_pool_gate.py --leaf recon_0028_full/ciphertext_draft.tsv --pool ciphertext.txt --json recon_0028_full/gate.json
-> N=1827 K=174 M=0.232 (<=0.15 NOT met) offform=0.024 (<=0.05 met) vocab overlap 0.806;
   cosine real 0.681 vs relabel mean 0.413 p95 0.514 (met, real > p95) -> HELD
```
HELD on the M-share gate alone (0.232 vs 0.15) -- entirely explained by the unsettled disagreements above, not a
same-system problem: the cosine gate (the one that would show a different key or noise) passes comfortably (0.681
real vs 0.514 p95, well clear). Off-form share also passes (0.024): most non-digit tokens are the recognised
marks; the `[PLAIN:...]` clauses and a handful of `ILLEGIBLE`s make up the offform total, listed in the tool's own
output. **This leaf is admissible on the same-system test; it is held only pending settling the M-graded rows**,
unlike bMALDUP's f.28-vs-f.30 alignment test (a different question -- copy-vs-reenciphered -- not a pool-admission
gate). K=174 across L05-44 (up from bMAL3's K=95 on L05/L12 alone) is itself expected: more lines see more of the
nomenclator's code space, not a design change.

**Next steps (not this job):** (1) transcribe blocks 4-5 (L45-L57, 13 lines, crops already on disk in `crops/0028`)
the same way; (2) settle `recon_0028_full/disagreements.tsv`'s 423 rows against the f.28 image and the f.30
witness (crops on disk in `crops/0030`), at least the highest-value ones first (recurring codes, not singletons);
(3) re-run the gate after settling -- the cosine/offform gates already pass, so settling M down should clear the
M-share gate on its own without a design question to resolve; (4) a dedicated zoom pass on L36/L39/L44's
`[PLAIN:...]` spans to fix the wording, which may be a crib.

Files: `crops/0028/` (all 57 L-crops, `hstam_4_h_1411_0028_lines_debug.jpg` overlay, manifest.json), `crops/0030/`
(all 59 L-crops for witness use, manifest.json), `transcription/pass_{a,b}_0028_b{1,2,3}.tsv` (raw subagent
output), `transcription/pass_{a,b}_0028_full.tsv` (concatenated L05-L44), `recon_0028_full/` (disagreements.tsv,
ciphertext_draft.tsv, agreement.tsv, gate.json).

Hosts: none (all work from images already on disk).

## Record 505 f.23 (bMAL23, 26 Sept 2026)

Intake gate re-run: `python3 tools/intake_gate_check.py malsburg-hessen-1636` -> `malsburg-hessen-1636: partial
(line 1)`, exit 0.

**Crop step.** `python3 tools/iiif_lines.py --image images/hstam_4_h_1411_0023.jpg --out crops/0023 --debug` ->
region 2226x2930, 52 lines, 52 bands x 1 segment. Debug overlay checked. The clear/cipher boundary is not where
bMALC's low-resolution estimate placed it: reading the crops directly (not just eyeballing the debug overlay),
L01 is the salutation/header line, L02-L13 are clear German prose (13 clear lines, not ~8), and L14 opens with
two or three clear words ("bestand gegeben,") before the cipher block starts mid-line and runs solid to L52
(39 cipher-bearing lines, L14-L52). `clear_0023.txt` transcribes L01-L13 in a single non-blind pass (this
worker read the crops directly) -- flagged LOW CONFIDENCE throughout: this is dense 17th-century chancery
cursive at the edge of what a non-specialist single pass can read, provided as crib context only, not cited as
an H/C-grade reading (rule 2).

**Two blind passes, four blocks.** L14-L52 (39 lines) split into four blocks of <=10 lines (L14-23, L24-33,
L34-43, L44-52); each block's crop paths (never a full leaf) given to two fresh Sonnet subagents per block,
neither seeing the other's output or any other repository file, both given bMALG's glyph-convention paragraph
verbatim. 8 subagent calls total (Usage 6 pricing: 4 blocks x 2 passes, not the brief's rough 5x2=10 estimate,
since the real clear/cipher boundary gave fewer cipher lines than bMALC's rough estimate). Per-block token
counts: block1 (L14-23) A=403/B=406, block2 (L24-33) A=394/B=392, block3 (L34-43) A=368/B=372, block4 (L44-52)
A=323/B=318. Pushed after each block.

**Reconcile.** `python3 tools/reconcile_passes.py transcription/pass_a_0023.tsv transcription/pass_b_0023.tsv
--sign-map glyph_map.tsv --crops crops/0023 --out-dir recon_0023` (the four blocks' pass files concatenated
first, line ids unique across blocks) -> lines 39, signs A 1490 B 1488, agree 1237/1503 = 82.3% (nw), 266
disagreement rows.

**Settling from the image.** 267 disagreement rows (266 data rows) is well over the 50-row settle cap, so
settling targeted the highest-value patterns rather than working row by row: five recurring value-pair
patterns were each confirmed by zooming (PIL crop + 2-6x upscale, `recon_0023/zoom/`) on 2-4 independent
occurrences before generalizing to every instance of that exact pair, plus four one-off L14 tokens settled
individually --

| pattern (A/B canonical) | n | zoomed at | settled to | grade | note |
|---|---|---|---|---|---|
| 26 / 16 | 11 | L14 x2, L17 x2, L18 | 16 | H | pass A mislabelled the established i6->16 dotted-cursive-1 shape (glyph_map.tsv, H, 36 occurrences on f.28) as the ambiguous z-hook; not a new convention, a mis-tagged instance of the existing one |
| 16 / 10 | 23 | L34 pos12, L36 | 16 | H | same i6->16 shape read correctly by pass A as literal "16"; pass B misread the dotted-i as a "0" |
| 61 / 01 | 7 | L36 | 61 | H | plain "6" + dotted-1, order reversed from the i6 pattern; pass B misread the leading 6 as 0 |
| Und / und | 4 | (case only, no zoom needed) | Und | H | bMALG's own case convention: canonical is the capital mark, already an H-grade clear word |
| 22 / 2 | 10 | L45 | -- left M | not settled -- kept M/open (see below) |
| L14 pos12 | 1 | L14_mid | 19 | H | dotted-1 + loop-9 |
| L14 pos19 | 1 | L14_gap | 11 | H | two matching dotted strokes, no crossbar for a 4 |
| L14 pos34 | 1 | L14_right | 80 | H | round figure-eight, not 30 |
| L14 pos36 | 1 | L14_right | 55 | H | two matching 5-shapes |

49 rows settled (at the cap), all recorded with a `why` column note in `recon_0023/ciphertext_draft.tsv`
(`settled:<reason>`) rather than silently overwritten. The `22/2` pattern (10 rows) was zoomed and the stroke
count genuinely confirmed as doubled (matching pass A's "zz"), but z remains grade M per bMALG (shape not
settled to a confirmed digit, only the token-count question was resolved) -- left as an open M rather than
counted against the 50-row cap, since choosing between two M-grade readings isn't the same operation as
confirming an H-grade digit. Two segmentation-only disagreements (L14 pos18 `56`/`z56`, pos37 `27`/`77`) were
looked at and left open per bMALG's own guidance ("these look like token-boundary/segmentation disagreements
... a different question from glyph shape ... stay open disagreements"). The remaining ~210 disagreement rows
were not individually zoomed (over the 50-row cap) and stay at grade M.

**Result.** N=1503 signs, K=164 distinct values. Grade counts after settling: H=1286 (85.6%), M=217 (14.4%).

**Gate.** `python3 tools/leaf_pool_gate.py --leaf recon_0023/ciphertext_draft.tsv --pool ciphertext.txt --seed
20260926 --json recon_0023/gate.json`:
```
leaf recon_0023/ciphertext_draft.tsv: N=1503 K=164 M=0.144 (<= 0.15) offform=0.039 (<= 0.05) vocab overlap 0.865;
cosine real 0.826 vs relabel mean 0.435 p95 0.515 -> ADMITTED
  offform examples: AH FF GG Gauß ILLEGIBLE Y1 agindest antwort auff dato daß es
```
All three gates met (M 0.144<=0.15; off-form 0.039<=0.05; cosine 0.826 well above the relabel p95 0.515) --
f.23 is admitted to the pool. Not yet merged into `ciphertext.txt` (out of this job's scope; the orchestrator
admits per CLAUDE.md rule 3's per-leaf merge gate).

**L34/L38/L41/L42 plain-script spans.** These four lines (all in blocks 3-4) carry short runs of plain cursive
German interleaved with the numeral code rather than being solid cipher (matches the pattern already seen on
507/508's postscripts) -- pass A's block3 call read one such span as "Befehlshaber Gauß" (L34, opening words);
zoomed directly (`recon_0023/zoom/L34_start.jpg`) and confirmed there genuinely is cursive prose there (not a
subagent fabrication), but the exact reading is not confirmed to H and is left as pass A's plain-text guess at
grade M in the draft, flagged here rather than promoted. A future job could zoom these four spans specifically.

Files: `crops/0023/` (52 line crops + manifest; debug overlay recompressed then dropped from git, regenerable
in one command from images/hstam_4_h_1411_0023.jpg), `clear_0023.txt`,
`transcription/pass_{a,b}_0023_block{1,2,3,4}.tsv` + concatenated `pass_{a,b}_0023.tsv`, `recon_0023/`
(disagreements.tsv, ciphertext_draft.tsv, agreement.tsv, gate.json, zoom/ -- 11 settling-zoom images kept at
reduced JPEG quality, matching the settled rows above, redundant/duplicate zooms pruned).

**Folder-size flag for the orchestrator.** This job's own net addition (crops/0023 + recon_0023 +
transcription increment) is about 2.2 MB; the folder crossed 30 MB (30.5 MB after this job's own crops were
recompressed to quality 45-55 and the regenerable debug overlay dropped from git) because `images/` (22.6 MB,
16 leaf images from bMALC's earlier fetch, none of them mine) plus `crops/0028`/`crops/0030` (4.6 MB, bMALG's)
were already close to the line before this job started. Not shrunk further here: doing that safely needs the
AX2-SHRINK regen-verified process (byte-identical re-derivation check before deleting anything), which is a
separate, larger job than this one's brief -- flagged for the lane orchestrator per rule 7/Usage 8a rather than
improvised.

Hosts: none (image already on disk from bMALC's fetch).
