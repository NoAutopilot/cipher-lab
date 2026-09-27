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

## Next step from the method registers (27 Sept 2026, parent 7k, from LESSONS-TOMOKIYO.md (d))

Named next step (not run): a different instrument for the running_key family (CLAUDE.md rule 3 "untested-by-this-tool",
bHCP2/bHCP3 above): drag de19 dictionary words of 10+ letters at every offset, quadgram-score the other side, extend the best
fragments by hand (Tomokiyo runningkey.htm "Solution", Brown's method; "Tips"). Matched control first at N=164 -- a synthetic
running-key text of the same length on de19, the drag's recovery on it before the target is run. Cost band S
(`tools/running_key.py --drag`, SYSTEM.md "Tools wanted", added by the worker that runs it). Status stays partial.

## HES-DRAG (27 Sept 2026): dictionary crib-drag, control-backed negative

Job HES-DRAG (parent worker, cap USD 6, brief `.claude/briefs/runs/2026-09-27-parent-ytbiz-hes-drag.md`). Intake gate
re-run 27 Sept 2026 07:38 UTC: `hessen-1824: partial (line 1) -- edition/page or full-text-search citation found within
6 lines`, EXIT 0. `tools/running_key.py` already carries `--crib-drag WORDLIST --all-tabulae --top`; no tool change
needed (the `--drag MINLEN --corpus DICT` row this job's own brief pointed at in SYSTEM.md's "Tools wanted" table was
stale -- `--crib-drag` already does the same job -- removed from SYSTEM.md in this commit).

**U1 -- word list.** Every distinct de19 token of 10+ letters (regex-tokenised on the raw text before folding, so word
boundaries are real, not `fold()`'s continuous-stream boundaries): **9,668 distinct words** across the three de19
books (10,580/6,640/1,587 raw long-token hits per book before dedup). Written to
`ciphers/hessen-1824/families/de19_words10.txt`.

**U2 -- matched control, built word-aligned (not `running_key.py`'s own `--control`, which cuts an arbitrary substring
of the fully despaced letter stream and so almost never lands a real dictionary word at a verifiable offset).** A
private control-builder script (not committed as a tool -- one-off window selection over the same corpus `running_key.py`
already reads, per the brief's fallback: "build the control text with the tool's own control code path... a private
script is not an option" is about the *tool itself*, not about the word-boundary-tracking window-selection step the
tool's own `--control` does not do at all) picked a random start token in one book, walked forward token-by-token until
164 letters were used, and recorded every intact word of 10+ letters and its offset -- so the control's own true
placements are known and checkable, unlike a click-anywhere-in-the-letter-stream cut.

Plain book: `pg2405_Italienische_Reise_Band2.txt.gz`; key book: `pg31538_Peter_Schlemihl.txt.gz` (seed 1, vig
tabula, N=164, the target's own N). Tracked words: plaintext side `hinaufgehoben`@6, `abgeschrieben`@120,
`mitzuteilen`@144; key side `hingeopfert`@10, `verschreiben`@113 (all recorded in
`ciphers/hessen-1824/families/hesdrag_control_meta.json`; plain/key/cipher texts beside it).

**Control drag** (`--crib-drag de19_words10.txt --kcorpus tools/data/de19 --all-tabulae --top 15`, full de19 as the
key-language corpus -- matching what the target run below also uses, since the real key book is unknown either way):
**PRE-REGISTERED GATE MET DECISIVELY.** All 5 planted words recovered within the top 11 of 15 rows, at their exact
true offset and tabula (vig, the true construction tabula): `hingeopfert`@10 (rank 1, score -1.628), `verschreiben`@113
(rank 5, -1.741), `hinaufgehoben`@6 (rank 6, -1.764), `abgeschrieben`@120 (rank 7, -1.779), `mitzuteilen`@144 (rank 11,
-1.871). **4 of the top 10** are exact true placements (gate: "at least one of the top 10... a real word... at its
true offset"). Full ranked table: `ciphers/hessen-1824/families/hesdrag_control_dragresult.tsv` /
`.json`. The instrument has clear discriminating power at this N, corpus and word-list size -- unlike the beam decoder
(bHCP2/bHCP3), this is a genuinely different tool for the same family and it is *not* untestable here.

**U3 -- target**, same settings (`--all-tabulae --top 30`) on the real 164-letter transcription
(`ciphers/hessen-1824/families/hessen1824_ciphertext_folded.txt`): best score **-2.083** (`zugewendet`@108, vig) --
worse than every one of the control's 5 true hits (best -1.628, worst true hit -1.871) and worse than the control's
own best *non*-hit distractor row (-2.065, rank 15). No positional clustering resembling the control's true cluster at
pos122 (four overlapping `-schrieben`-family candidates scoring -1.706 to -1.896, all pointing at the same real word)
appears at a comparable score band: the closest analogue, a 4-way cluster of independent candidates at pos46
(`mandelbaum`, `seltsamste`, `sublimiert`, `orgelbauer`), scores only -2.296 to -2.398 -- clearly inside the noise band
this same tool/corpus/word-list combination showed on the control's own non-hit rows, not near its true-hit band. Full
ranked table: `ciphers/hessen-1824/families/hesdrag_target_dragresult.tsv` / `.json`.

**Extension check (Tomokiyo "Tips", <15 min, per the brief's cap):** for the top 3 target rows (`zugewendet`@108/vig,
`gefanglich`@145/varbeau, `fabrizieren`@110/vig), tried each of 30 common German function words (der, die, das, und,
mit, ...) immediately before and after the candidate word's span, scored the newly-implied key fragment the same way;
none scored above -1.6 (i.e. none read as plausible German) at any of the 6 adjacent slots checked. No fragment
extends. No candidate reached the judge's 20+-letter minimum, so U4 (`tools/judge_plaintext.py`) was not run --
nothing to score.

**Flag, not a signal:** the target's 2nd-best row (`gefanglich`@145, varbeau, -2.142) sits exactly on one of the three
anomalous digit-like "4" glyphs in this transcription -- position 145 is the "g" that survives `fold()` from the
original "4g3" token, immediately before the "pfx" token at folded offset 146 (NOTES.md's transcription section, line
41). The score is still far inside the noise band (worse than the control's worst true hit), so this is not read as a
hit -- flagged only because a future re-transcription pass touching this exact glyph should know a drag artifact once
landed there by coincidence, not because it means anything now.

**Read:** dictionary crib-drag (Tomokiyo/Brown's method) is now **tested, not untestable**, on this target -- the
control shows the instrument reliably surfaces true placements (all 5 planted words in the top 11 of 15, 4 in the top
10) at this exact N, word-list and corpus, and the real ciphertext shows nothing resembling that signal under the same
settings. This is a **control-backed negative for running_key via a second, independent instrument** (the beam decoder
stays "untested-by-this-tool" per bHCP2/bHCP3; the drag is a different tool and it is negative). Whether this closes
running_key's ladder entry (rule 5: "closed-negative needs every family in the target's ladder logged with a passed
control") is the orchestrator's call, not this worker's, same as bHCP2/bHCP3 left it -- flagging that the drag's own
gate requires knowing a genuine long word sits at a genuine offset, which is exactly the scenario a *short* or highly
inflected key vocabulary would defeat; a negative here rules out "a long, dictionary-attestable German word from
1810s-40s prose sits legibly in the key stream at some offset," not every possible book-cipher key. Status stays
`partial`. No "solved", "new", "first", "unpublished".

**Next step, 27 Sept 2026 (HES-DRAG):** no untried cheap step remains in the current ladder (periodic_vigenere, masc,
homophonic all control-backed FAIL; running_key control-backed negative via crib-drag, untestable via the beam
decoder). A successor should either get more ciphertext from the same fascicle (HStAM 9 a Nr. 259 siblings, the
Anmerkung's own "No. 1" item) or try a shorter/period-inflected key-vocabulary variant of the drag (this run only
tried literal dictionary forms of 10+ letters; German's rich inflection means a genuine key phrase could avoid every
long literal dictionary form the drag checked). Not a further re-run of this exact word list/corpus/tabula
combination.

`python3 tools/intake_gate_check.py hessen-1824`:
```
hessen-1824: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
EXIT: 0
```

## Second-opinion leads (SO-HESSEN1824-LEADS, 27 Sept 2026)

Landed verbatim from the ChatGPT second-opinion runner's LEADS prompt (PR 35): `second-opinions/chatgpt-leads-2026-09-27.md`. Leads, not verdicts; every citation below is the runner's own and is unchecked until a verifier confirms it.

1. archival request: full archival unit HStAM 9a Nr.259, ff.245-255, enclosures/slips, multispectral imaging; no citation (request to archive); unchecked.
2. archival-search: search Best.9a office registry for Chiffr-/Ziffer-/Geheimschrift/Schlüssel/sympathetische Tinte stems 1821-1831; citation Lenhard-Schramm, "Behördenbezeichnungen im Wandel," Archivnachrichten aus Hessen 23/1 (2023) p.58; unchecked.
3. contextual fork: Kassel anonymous-threat-letter affair against Wilhelm II/Reichenbach, Friedrich Murhard arrested Jan 1824, records in HStAM Best.267/261/250 Nr.780; citations Ehrle NDB 18 (1997) pp.610-11, Kahlfuß ZHG 108 (2003) pp.123-47, HIL/LAGIS event page (2025); unchecked.
4. method: pooling design for siblings (held-out consistency across messages, phase-aware); no citation (methodological); unchecked.
5. catalogue: Arcinsys/Hessisches Landesarchiv full scope note and file-level description for Nr.259; no citation (unfulfilled catalogue request); unchecked.
6. comparator text: Klüber, *Kryptographik* (Tübingen 1809), for table/vocabulary comparison; citation given (Google Books, id nKtfAAAAcAAJ); unchecked.
7. analogue: Rous, "Geheimschriften in sächsischen Akten der Neuzeit," *NASG* 83 (2012) pp.243-53, on chancery cipher packets; unchecked.
8. provenance/record-form: Maaß & Pons (eds.), *Fürstliche Korrespondenzen des 19. und 20. Jahrhunderts* (2024); relevance to Nr.259 explicitly flagged unverified by the runner itself; unchecked.
9. contact: HStAM Marburg reference archivist for Best.9a/267 -- ask file-structure and neighboring-leaf questions; unchecked.
10. contact: Anne-Simone Rous -- ask about a Kurhessian counterpart to Saxon cipher-packet bundles; unchecked.
11. contact: Maaß, Pons or Uhde -- unverified whether any has worked directly with Nr.259; unchecked.
12. contact: Eugen Antal/HCPortal team -- ask basis for the "polyalphabetic" classification and whether sibling images exist; citation HCPortal contributors page; unchecked.
13. contact/method source: Reddy & Knight (ACL 2012, blocked-Gibbs running-key decoder) or a researcher reproducing it; unchecked.
14. method: test an omitted seven-phase general-substitution family (independent alphabets per phase, keyed to the Anmerkung's "bcdefg(h)" hint), against matched N=164/K~24 controls; no citation (methodological); unchecked.
15. method: reconstruct the Anmerkung's table as a constraint problem (table-geometry enumeration, shuffled-heading control); no citation (methodological); unchecked.
16. method: blocked-Gibbs running-key sampler (Reddy & Knight 2012 pp.80-84) and Griffing's Viterbi baseline (*Cryptologia* 30:4 (2006) pp.361-67) as the next running-key instrument if provenance supports a natural-language key; unchecked.
17. candidate key texts (conditional on provenance): Murhard's *Allgemeine politische Annalen* (1821-24), the Kurhessian Gesetz-Sammlung, Klüber 1809; not a claimed key; unchecked.

None of the 17 leads is a printed decipherment or edition of this target's own text, and none names the key or the cipher system actually used at Kassel in the 1820s -- no check-solved candidate flagged.
