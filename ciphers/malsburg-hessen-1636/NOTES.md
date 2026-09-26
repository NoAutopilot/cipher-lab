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
