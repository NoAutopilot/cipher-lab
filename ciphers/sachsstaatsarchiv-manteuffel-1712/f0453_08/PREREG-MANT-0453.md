# PREREG-MANT-0453 (MANT-0453, 9 Oct 2026, LANE FAMILY-A2g account 2; committed and pushed in its own commit BEFORE any transcription pass is read or any score computed)

Unit: HStA Dresden 10026 Loc. 694/08, URL file 0453 (film card 0454), ff.359v-360 (right page stamp 360), both pages; every numeric code
group on the frame. Full-size image re-fetched this job (sha256 prefix aa6766c203dbbdd7 = V-MANT0454's fetch, f0454_08/neighbours/manifest.json);
not committed (folder over 30 MB), crops committed. Key: key.tsv at origin/main as of this commit, unchanged by this job. Design = PREREG-MANT-0454
(f0454_08/), scripts copied into f0453_08/ (f0454_08/ not edited).

Letter context, recorded before any pass (worker's eye on reduced copies and one header crop of URL 0451; neighbours fetched this job, 0450/0451):
URL 0451 right page f.358 is the letter's head, "Berl. d. 29 oct. 1712." with a number "88" (an earlier number struck above it) and para "1.";
its last line "...que la cour de Prusse ne" runs on to 0452 left (f.358v) "pensoit plus a l'affaire". So 0451-0454 are presumed one letter,
No. 88, Berlin 29 Oct 1712 (continuity 0453 -> 0454 to be checked on the crops and reported). URL 0450 f.357 is a draft reply to Manteuffel
dated "le 30. Octobre 1712" acknowledging "vôtre lettre du no. 88".

Crops: `python3 tools/iiif_lines.py --image 0453.jpg --out ciphers/sachsstaatsarchiv-manteuffel-1712/f0453_08/crops --region <x,y,w,h>
--prefix f0453<L|R> --lines-per-crop 2 --overlap 60 --debug`, one region per code-bearing area chosen by eye from the 1600 px view before any
pass (left page foot, right page para 3); commands pasted in NOTES.

Transcription: two blind Sonnet code passes (A crop order, B reversed), crop paths only, readers told to report every number with its
neighbouring clear words, dot-separated runs as one group, and whether interlinear/sub-linear letters sit over or under any code. Worker
reconciliation from the image (one unit) -> f0453_08/ciphertext.tsv (decode_key.py format; conf low where the passes disagree and the image
does not settle it, or the settle is doubtful). Ordinary numerals (dates, counts, paragraph numbers) are not codes.

Gate (a): only if a pass or the worker's look finds interlinear letters on a code run (as PREREG-MANT-0454); else n/a.

Gate (b1) (f0453_08/judge_gate.py, design of f0454_08/judge_gate.py, unchanged statistic): this unit's unglossed letter tokens, page order;
key.tsv letter values (first '|' alternative, 1-3 letters a-z; word/name codes dropped); fr18 4-gram score; 1000 letter-value permutations,
seed 453; gate real > p95. Power control at this unit's letter count L, run first, same positive-control windows and rule as PREREG-MANT-0454
(0085 r9+r10, 0136 unglossed; 200 permutations seed 7 per window; pass if real > 190th of 200). TEST only if power >= 0.80; else
"too-short" (non-test, neither PASS nor negative). If L < 4: too-short unscored.
Gate (b2), POOLED, named here before scoring: letter No. 88 = this unit's unglossed tokens followed by f0454_08/ciphertext.tsv's (page order,
0453 then 0454); same statistic, 1000 permutations seed 4530, power control at the pooled L. Because 0454 alone already PASSed (52 letters),
a pooled PASS is mostly 0454's; it is reported as the letter's gate, not as 0453's own.
Grades (rule 4): name/word codes (key value 4+ letters) M, identification I; low-conf M at best; not in key U. A 0453 letter token is S if
(b1) is a TEST and PASSes, OR if (b2) is a TEST and PASSes AND 0453's own score in (b1) is above its own p95 (whatever (b1)'s power); else M.
Also reported (no verdict): each run's own score; any 0453 run whose decoded letters repeat a 0454 run's word with different codes (two-context
check, rule 4a) listed with both code strings.
No key.tsv change; candidate values to HYPOTHESES.md as rule-4 slots. Decode: tools/decode_key.py f0453_08 (--check). Check 5: tools/print_check.py
on decoded + clear phrases after decode. Rule 7: every script here has --check.
