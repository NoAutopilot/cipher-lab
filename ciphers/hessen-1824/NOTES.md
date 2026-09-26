partial
Bourdeau CATALOGUE.md #340 (fresh shallow clone, HEAD fc0c9e865d0fae67ca92d19750d2b09ab11972e0, read 26 Sept 2026) read in full: "Hessian polyalphabetic message of 1824: unknown -> unknown (Electorate of Hesse) ... HCPortal: 'Message encrypted with a polyalphabetic cipher', not solved. One page, image online. No reading found"; confirmed live against HCPortal's own API (`api.hcportal.eu/api/cryptograms/513`, HTTP 200 with header `Accept: application/json`, 26 Sept 2026 04:57 UTC), which carries `solution.name: "Not solved"`, `cipher_key_id: null`, `note: null`; Aymeloglu's repo (fresh shallow clone, HEAD 2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f) grepped for "hessen", "hessisch", "marburg", "hstam", "polyalphab", 0 hits, not in that catalogue at all; Tomokiyo/Cryptiana pages on disk (sources/cryptiana/web/) grepped for "hessen", "1824", "kurhessen", "electorate of hesse" -- no hits naming this item or shelfmark; one OpenAlex query ("Hessian polyalphabetic cipher 1824 Marburg", 0 results, header auth, 26 Sept 2026) and one Semantic Scholar query ("Hessian polyalphabetic cipher 1824 solved", 0 results, header auth, 26 Sept 2026).

# Hessian polyalphabetic message, 20 Feb 1824

Status: open. No reading, key or documented attempt found anywhere checked (see line 2).

## Target

- Shelfmark: Hessisches Staatsarchiv Marburg, HStAM 9 a Nr. 259, f. 249 (fond "9 a - Organisation und Geschäftsgang", folder "Nr.259").
- HCPortal record 513, name `hstam_9_a_nr_259_0249`, category "Polyalphabetic" / sub-category "Substitution", language German, date 20 Feb 1824, sender/recipient both "Unknown", `solution: "Not solved"` (id 1), created by Eugen Antal, no `cipher_key_id`, no `note`.
- 1 image online: f. 249 (`hstam_9_a_nr_259__0249`), fetched to `images/` (manifest.json).
- Bourdeau's own note (CATALOGUE.md #340, read 26 Sept 2026): "A rare polyalphabetic ciphertext from a German state chancery; a clean ciphertext-only exercise if the period is short" -- flags it as untried, not attempted by his own project either.

## Search log (intake, 26 Sept 2026)

1. Bourdeau's `dbourdeau/cyphersolver`, fresh shallow clone, HEAD `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`: `CATALOGUE.md` #340 read in full (quoted in line 2); `find -iname "*513*"` and `grep -ril "9 a.*259\|nr.*259\|1824" .` over the whole clone (excluding .git) found no dedicated solve folder, decode script or key file for this HCPortal id. Clone deleted after reading.
2. Aymeloglu's `aaymeloglu/unsolved-ciphers`, fresh shallow clone, HEAD `2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f`: `grep -rin "hessen\|hessisch\|marburg\|hstam\|polyalphab"` over the whole clone (markdown files): 0 hits relevant to this target. Not in this catalogue. Clone deleted after reading.
3. Tomokiyo/Cryptiana pages on disk (`sources/cryptiana/web/`, no live fetch): grepped for "hessen", "1824", "kurhessen", "electorate of hesse", "polyalphabetic" case-insensitively. No hits naming HStAM 9 a Nr. 259 or an 1824 Hessian chancery cipher.
4. HCPortal record status, live: `api.hcportal.eu/api/cryptograms/513` (browser UA + `Accept: application/json`, else the host returns a non-standard HTTP 466 "Access Forbidden" page, same finding as hessen-daenemark-1672 this session): HTTP 200, `solution.name: "Not solved"`, `cipher_key_id: null`, `note: null`, one image only, no attachment. 26 Sept 2026 04:57 UTC.
5. OpenAlex (`OPENALEX_KEY`, header auth): `search=Hessian polyalphabetic cipher 1824 Marburg`, 0 results, HTTP 200, 26 Sept 2026.
6. Semantic Scholar (`S2_KEY`, header auth): `query=Hessian polyalphabetic cipher 1824 solved`, 0 results, HTTP 200, 26 Sept 2026.

No reading, key or documented attempt found for HStAM 9 a Nr. 259 f. 249 in any of the six sources checked.

## Image and transcription

1 image fetched 26 Sept 2026 to `images/` (manifest.json). Host: api.hcportal.eu, 2 requests (1 record JSON + 1 image), >=1.6s apart; same Accept-header finding as hessen-daenemark-1672 (without `Accept: application/json` the host answers a non-standard HTTP 466 page, not a 429/403/challenge).

The page carries two parts: (1) a 6-line ciphertext block headed "Snell an [name, illegible]" in a neat Latin-letter cursive hand (much easier to read than German Kurrent); (2) below it, headed "Anmerkung", a note in German Kurrent describing a related item and a partial substitution key -- see next section.

**Ciphertext (own blind transcription, grade M, word/group boundaries uncertain):**
```
uf moqmr. onxiplql. tkmt. huslu. cqh. kxu kmiwomt
zsskkw fkguvzswzm. Jmixl ntldkt.
4cv. mfz. wcxp. lusnhr. zlogz erylfe.
iuw. hunky vmhr il4. gwxk. nm krvy?
ohvwi ipm ixkl pufxrm kqqrix vscqu ot
4g3. pfx. tguoqpkkh. ktrogg?
```
164 letters (N=164), 24 distinct signs; three occurrences of an anomalous digit-like "4" glyph (line 3 "4cv", line 4 "il4", line 6 "4g3") excluded from the letter count -- possibly a real numeral filler/null, possibly a Kurrent flourish that reads like "4"; not resolved this pass. Dots mark what look like group boundaries but spacing within a "group" is a scribe's natural word-spacing, not necessarily a cipher boundary, so groups are not claimed as sign-groups; the statistical test below uses the continuous letter stream (`--tokens letters`), which sidesteps this ambiguity entirely.

**The "Anmerkung" (grade M, my own reading of German Kurrent, real uncertainty):** a note, on the same leaf, describing how its writer worked out a key for a related "No. 1" item (mentions invisible/sympathetic ink written between the lines of that item) -- paraphrasing: "I copied the concept of the cipher in writing, but was still not able to reach a solution by means of the unknown key, until by a chance circumstance I discovered that b c d e f g (h) in the top row of the key are the 'resolution letters', which must be placed continuously over the ciphers, whereupon the key sets up the following letter on the left margin, thus for example, namely:" -- followed by a small table giving, for each of 7 column positions, a pair of interchangeable cipher letters and the plaintext letter they resolve to (my best reading: u/c->s, f/o->c, m/e->h, o/f->i, g/g->k, ?/b->n, v->t; a keyword-like word appears beside the header "bcdefgh" that I could not read with confidence). Whether this note describes the very ciphertext above (which would make HCPortal's "not solved" wrong) or a different, related item in the same fascicle ("No. 1") is not established -- the note's own wording ("zweyerlei Zettel", "two kinds of slips") suggests a plurality of related cryptograms in this file, of which our record 513/f.249 may be only one. I did not commit a key.tsv or attempt to apply this table as a formal reading: transcribing 19th-century German Kurrent correctly under a $2 cap carries real misreading risk, and a wrong guess committed as a key is worse than none (rule 2). See crops referenced above (not committed individually; full page is `images/hstam_9_a_nr_259__0249.jpg`).

## Cheap test 1: IC / periodic IC (Friedman/Kasiski, period 2-20) vs a de20 control, family_run.py periodic_vigenere

Matched control run FIRST per rule 3 (`tools/family_run.py specs/hessen-1824.json --family periodic_vigenere --control-only --seeds 3 --param period_max=20 --gate 0.6 --tokens letters`): German de20 plaintext window of the same N=164 under a random periodic Vigenere key (period found by the same 2-20 coset-IC scan), 3 seeds: **recovery 1.000 (1.000-1.000)** -- gate (0.6) met easily, so this design has full power at this N and the control can discriminate a real signal from noise.

Target run (same command without `--control-only`): coset-IC scan over periods 2-20 finds its own best at **period 16** (coset IC 0.0664; next-best 20 at 0.0565, 17 at 0.0516, 14 at 0.0504, 18 at 0.0491 -- no sharp peak, IC well below real German's ~0.07-0.075). Best decode score -3.629 nats/letter; `tools/judge_plaintext.py`'s de20 language judge: **FAIL** (score -2.0 vs null_p99 -1.935, real_p05 -0.86, real_median -0.778, N=164) -- inside the null band, not close to the real-language gate.

Two extra period-specific runs, motivated directly by the Anmerkung's "bcdefg(h)" hint (period 6 or 7): **period=7** best score -4.022, judge FAIL (score -1.893, still inside null_p99 -1.935 but the worst of the three runs' judge scores is actually this one's raw score being closer to threshold -- read the sign correctly: -1.893 > -1.935 so nominally just above null_p99, but well below real_p05 -0.86, still FAIL); **period=6** best score -4.104, judge FAIL (score -2.046). Neither period-6 nor period-7 solve beats the auto-scanned period-16 attempt; the Anmerkung's implied period is not confirmed by this test, whether because it describes a different item ("No. 1") or because of transcription error in my own reading of either the ciphertext or the note.

All four rows (control-only N=37 tokens=space mistake -- see below --, control-only N=164, target period_max=20, target period=7, target period=6) are in `ciphers/hessen-1824/HYPOTHESES.md`. Note for whoever reruns this: the spec's `alphabet` field text did not trigger family_run.py's `auto` tokens-mode letter-detection (it defaulted to `tokens=space`, treating each whitespace-separated word as one sign, N=37) -- pass `--tokens letters` explicitly, as done here; the erroneous N=37 control-only row is left in HYPOTHESES.md (append-only per its own header) but superseded by the N=164 rows below it.

**Read:** a real periodic-Vigenere/Beaufort signal at N=164 would be caught by this design and gate (control recovery 1.000) -- the target does not show one, at the auto-found period (16) or at the two periods the page's own Anmerkung suggests (6, 7). Given the era-mismatch flag on the de20 judge corpus (see spec `constraints.era_note`), this is a **control-backed negative for the periodic_vigenere family at periods 2-20 on this transcription**, not a proof the item is unsolvable -- the next step is a careful, dedicated re-transcription (my own reading carries real uncertainty, both of the ciphertext letters and of the Anmerkung's key table) before ruling out this family altogether, and/or reading whether the Anmerkung's "No. 1" refers to this very record or a sibling in the same HStAM 9a Nr.259 folder.

specs/hessen-1824.json `cheap_test_done`: see HYPOTHESES.md rows above (family_run.py writes there, not into the spec file's own field, for this family).

`python3 tools/intake_gate_check.py hessen-1824`:
```
hessen-1824: open (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT: 0
```
Gate passed 26 Sept 2026 04:58 UTC. Proceeding to image fetch and the brief's first cheap test.

## Remaining families (bHCP2, 26 Sept 2026)

Job bHCP2 (LANE B8). Intake gate re-run 26 Sept 2026 06:55 UTC: `hessen-1824: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, EXIT 0. IC finding from bHCP (coset IC scan, periods 2-20): best period 16 at 0.0664, next-best 20/17/14/18 at 0.0565/0.0516/0.0504/0.0491 -- no sharp peak, all values well below real German monoalphabetic (~0.07-0.075) and only moderately above random (~0.0385). Read as: the text does not show the clean peaked-coset signature of a genuine short-period polyalphabetic cipher (not flat-polyalphabetic), so the brief's third step (homophonic) was run.

1. **masc** (`--family masc --seeds 3 --tokens letters`): control N=164 K=24, 3 seeds, mean recovery **0.823 (0.634-0.994)** -- gate (0.6) met. Target best score -411.145; judge **FAIL** (score=-1.354, null_p99=-1.935, real_p05=-0.86, real_median=-0.778, N=164).
2. **running_key** (`--family running_key --corpus tools/data/de20 --seeds 1 --control-only` first, per the brief's overrun check; ran in 64s so the full call would not have overrun the box, but the control itself came in below gate): control N=164 K=26, 1 seed, recovery **0.372** -- **gate (0.6) NOT met**, CONTROL BELOW GATE, target not run (non-test, not a negative, per rule 3 / the brief).
3. **homophonic** (`--family homophonic --param profile=target --seeds 3 --tokens letters`, run because the IC above is not flat-polyalphabetic): control N=164 K=23-24, 3 seeds, mean recovery **0.878 (0.793-0.933)** -- gate met. Target best score -411.145 (same decode as masc -- the homophonic solver with profile=target and K=24 reduces to the same one-sign-per-letter search here); judge **FAIL** (score=-1.354, null_p99=-1.935, real_p05=-0.86, real_median=-0.778, N=164).

All rows in `ciphers/hessen-1824/HYPOTHESES.md`. Together with bHCP's periodic_vigenere runs (control 1.000, target FAIL at periods 16/7/6), every family in the spec's ladder (periodic_vigenere, masc, homophonic) now has a logged run with a passed control and a target FAIL; running_key's control fell below its own gate at this N (a non-test, not counted as a negative). Whether this closes the ladder is the orchestrator's call, not this worker's (rule 5, brief line 5) -- flagging that the ciphertext transcription itself carries real M-grade uncertainty (NOTES.md's own transcription section) and the de20 judge corpus is era-mismatched (spec `constraints.era_note`), so a FAIL here is conditional on both.

## running_key de19 (bHCP3, 26 Sept 2026)

Job bHCP3 (LANE B9). Intake gate re-run 26 Sept 2026 08:20 UTC: `hessen-1824: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, EXIT 0.

**U1: built `tools/data/de19`** -- three Project Gutenberg prose works first printed 1814-1817 (Goethe, *Italienische Reise* Band 1+2, 1816/1817; Chamisso, *Peter Schlemihls wundersame Geschichte*, 1814), 1,040,997 letters after `fold()`. This replaces de20 (1880-1940, 56-116 years later than the target) and de16 (Early New High German, too early) for this target's judge/control corpus, per CLAUDE.md rule 3's pt18/es17c era-matching precedent. Host `www.gutenberg.org` only, >=1.5s apart, own User-Agent, 12 requests total (9 `ebooks/search` queries locating candidates + 3 downloads) -- the search budget, not source scarcity, is why the corpus has three files rather than the brief's suggested 5-8: clean single-work hits were not found within budget for Kleist (only a mixed "Ausgewählte Schriften", genre unverified), Heine's *Reisebilder* (only an English "Prose Writings" translation), Clausewitz (no hit, only a secondary English commentary) or Hoffmann (no clean single-author hit). See `tools/data/de19/README.md` for the full search log and the follow-up this leaves (adding Kleist's actual novellas and Hoffmann once their clean ebook IDs are confirmed).

**U2: leave-one-file-out false-negative check** (`tools/data/de19/holdout_check.py`, N=164, 200 samples/fold): held-out false-negative rates 54.5% (Goethe Band 1), 29.0% (Goethe Band 2), 34.5% (Chamisso) -- **blended 39.3% (236/600)**, **per-fold spread 0.255** (29.0-54.5%). Three folds only, under the ~5-file reliability floor CLAUDE.md rule 3 names (the es17c/EN-FOLDS lesson): **this corpus's judge FAIL/PASS verdicts are of unknown reliability**, flagged here and in the corpus's own README rather than smoothed over, same as EN-FOLDS did for `en`. (No judge PASS/FAIL is actually reported from this job -- the target was never run, see below -- so this caveat matters only for a future de19 judge call, not for today's result.)

**U3: running_key control-only, de19, wider beam than bHCP2's.** bHCP2 (job bHCP2, 26 Sept, this file's "Remaining families" section above) ran `--corpus tools/data/de20 --seeds 1 --control-only` with no `--param beam`, i.e. the family wrapper's own default, **beam=3000** (`tools/families/running_key.py`'s default; confirmed by reading the wrapper, not inferred) -- control recovery 0.372, gate 0.6 not met.

This job ran the same control at N=164 on de19 with beam widened first to **beam=6000** (`--seeds 3`): CONTROL mean **0.331 (0.213-0.457)**, gate 0.6 **NOT met** (5m21s wall time). Per the brief's own escalation ("the widest beam the box allows"), ran again at **beam=15000** (2.5x wider, `--seeds 3`, same seeds): CONTROL mean **0.331 (0.213-0.457)** -- **byte-identical per-seed recovery to beam=6000** (13m13s wall time, vs 5m21s at beam=6000: cost scaled with beam width but the *result* did not move at all). This is a clean signal, not a coincidence of rounding: the beam search has already converged at 6000 for this N=164/K=26 design, so widening it further buys nothing. **running_key's control is not beam-limited at this N; it is solver-power-limited.** Both control-only rows are in `ciphers/hessen-1824/HYPOTHESES.md` (08:28 and 08:42 UTC).

**Verdict, per the brief's own stop condition:** the control stayed below gate at the widest beam that showed any further computation was worth doing (6000 -> 15000 gave identical output) -- **running_key is untestable at N=164 with this solver**, on de19 as it already was on de20 (0.372 at beam=3000, 0.331 at beam=6000/15000; the de19-vs-de20 corpus swap did not change the qualitative outcome either). The target was never run (rule 3: no control, no target). This is consistent with, not contradicting, bHCP2's reading: at N=164 the ciphertext is simply too short for this project's running_key two-stream beam decoder to recover a known-plaintext control reliably, whatever corpus or beam width backs it -- a genuine running-key/book-cipher signal in the real ciphertext (if the "Anmerkung"'s hinted periodic-table interpretation is wrong and it is in fact a book cipher) would not be caught by this tool at this length either, so this stays a **non-test**, not a negative, exactly as CLAUDE.md rule 3 requires.

**Degenerate-optimum check (brief item 5):** moot here -- the target was never decoded (control-only throughout), so there is no target key offset or decoded span to check against a de19 source file. Recorded for whoever runs the target if a beam/design change ever clears the gate: check the best key text span against `tools/data/de19/*.txt.gz` word-for-word before trusting a "German" reading, since the corpus and the judge share the same source pool.

**Status:** `hessen-1824` stays `partial` (rule 5's near-solve amendment; not `closed-negative`). Every family in the spec's ladder (periodic_vigenere, masc, running_key, homophonic) now has a logged control-first run; running_key's is a non-test at two independent beams and two independent era-matched-vs-mismatched corpora, not a negative. Whether the ladder is exhausted, and any NEAR.md update, is the orchestrator's call.

SO lead prompt, 26 Sept 2026, QUEUE-FILL.
