# Köhler cryptograms -- hypotheses and prior attempts

Working file for constraints on the system behind the five February 1944 Köhler cryptograms (see NOTES.md for
the target, sources and check-solved verdict). Everything below the first `##` is append-only, dated and signed by
the job that wrote it. This top block is rewritten once per cycle by the lane's consolidator and by nobody else.

**Summary, cycle 4** (GOLD-CONS4, Fable, session_01CSQuomCj5Simbsx6r6VVcK, 26 Sept 2026 00:47 UTC; replaces the
cycle-3 block of 25 Sept 23:06 UTC, whose target facts and the three established points are unchanged and restated here)

**Target facts every family must respect.** 924 letters in five messages of 237 / 178 / 140 / 140 / 229 (Kahn heads
the third "137"; it prints 140). All 26 letters present; counts run z 55 down to c 14, sorted profile 55 47 47 47 46
46 44 40 39 37 36 36 35 33 33 32 31 31 31 30 29 28 28 26 23 14. Two message lengths are odd. Transcription: Schmeh
2021 reproducing Kahn 1981 pp.65-66 (no image); six single-letter differences from Bourdeau's (`ciphertext-variants.tsv`,
ASKS 53: the Cryptologia scan is print-disabled on the Internet Archive and cannot be borrowed by this account,
IA-BORROW 25 Sept 22:44 UTC, so the six groups stay with the owner), immaterial to every statistic below, material to
any decode. No depth between messages (Bourdeau). IC 0.0399.

**What the ladder has established (four cycles, every number with its control).**
1. The key stream is non-uniform (GOLD-2C step 1): the letter statistics sit inside the keyed-tableau running-key band
   on 6/6 statistics (percentile 0.41-0.52) and outside the uniform one-time-key 99 pct band on 5/6. Transposition is
   excluded by the flat IC, a 25-letter digraphic square by j and the odd lengths, a fixed period 2-120 by two coset
   scans with controls.
2. No letter-arithmetic tableau reachable by a keyword or by a cipher-side mixing reads above noise at 924 letters:
   the standard tableau at two key registers (nl20 novels, nl_dev Bible) and the keyword-mixed tableau in all seven of
   its placements at vig (plain, key, both, full, cipher, plaincipher, keycipher) and five of seven at beau, with three
   keyword lists (de20+nl20, German-only, English), all have controls at 67-90 pct plaintext letters recovered and
   targets inside the same pipeline's noise band, judge FAIL every time (GOLD-2C, K1, K2, K3, K4).
3. A free permutation is unidentifiable at this length (GOLD-B2D): with S1 = S2 = identity and S3 free, the best search
   that fits a box (sum-stream n-gram proxy, 30k evaluations x 3 chains, beam rescoring) reads a random S3 at 9.5 pct
   (7.4 / 12.9 / 8.1; chance 3.8) and places 1 / 8 / 3 of 26 letters; the proxy's maximum is the true permutation only
   from about 5,000 letters (English: 3/26 at 2,000, 26/26 at 6,000-8,000), and the decoder objective's hill spans about
   3 swaps around the truth and is flat beyond 8. The general case (S1, S2, S3 free) has 26!^2/26 more states and two
   symmetries on top; it has no chance with these objectives at 924 letters.

**Final family table, cycle 4.** Controls and targets side by side, same decoder settings per row; "band" is the noise
band of the same pipeline (two-text -3.507 / -3.544 at order 6 beam 300 unless stated; the ten-text beau band of K3 is
min -3.5481, median -3.5305, max -3.4944).

| family, corner | job | CONTROL (pct plaintext letters, seeds 1-3; gate) | TARGET | read |
|---|---|---|---|---|
| A recovery (TNA KV 2 / HW 19, FBI Vault, NARA index, Kahn's source) | GOLD-1A | n/a | no decrypt, key or system located; FBI HQ file RG 65 105-9673 box 156 located, unopened (ASKS 55); Farago 1971 unread; Cryptologia scan not borrowable (ASKS 53) | **blocked on the owner** |
| Bourdeau's six: masc/transposition (IC), periodic vig/beau 1-26 (quadgram vs shuffle), ciphertext autokey 1-40, standard running key (unigram likelihood), Gronsfeld, any Enigma wiring (chi-square) | Bourdeau 15 Sept 2026, cited | his controls (true running-key text >= +7.5 nats in 95 pct of trials; simulated Enigma chi-sq median 26) | below uniform on family 4 (-4.0 nats); chi-sq 57.9 (p 0.0003) on family 6 | **excluded**, cited |
| B standard tableau, vig, nl20 key | GOLD-2A | 72.7 / 60.4 / 68.3, mean 67.1 (gate 60 met) | -3.589; -3.57 to -3.62 over 7 configs vs band -3.57 to -3.64 (3 uniform texts, order 8 beam 1000) | inside |
| B standard tableau, vig and beau, nl_dev Bible key | GOLD-K1 | 83.0 / 89.5 / 80.3, mean 84.3 (gate 60 met) | vig -3.588; beau -3.640 (GOLD-2A's band reused) | inside; beau at the floor |
| B' keyword-mixed, vig, modes plain/key/both/full, nl20 key | GOLD-2C | 79.1 / 74.0 / 64.7, mean 72.6 (gate 50 met) | -3.534 (`waarvan:plain`) | inside |
| B' keyword-mixed, beau, four modes, nl20 key | GOLD-K2 v1 | 85.5 / 82.5 / 66.2, mean 78.1 (gate 50 met) | **-3.478** (`aufgabe:plain:beau`); msg-1 best-of-30 -3.443 vs noise -3.477 / -3.492 | 0.029 above the two-text top; **0.016 above the ten-text beau band's max** (-3.494); judge FAIL; under the 0.1-nat flag line; still the record's largest excess |
| B' keyword-mixed, vig, four modes, de20 (German) key | GOLD-K2 v2 | strict 7.7 (streams exchangeable under vig, label ambiguity); either-stream 89.6 / 90.7 / 88.6, mean 89.6 (gate met) | -3.573 | below the floor |
| B' keyword-mixed, vig, four modes, nl_dev Bible key | GOLD-K1 | 87.8 / 81.0 / 85.6, mean 84.8 (gate 50 met) | -3.583 (`evelyn:plain`) | 0.04-0.08 below the floor |
| B'-c cipher-side mixing (mode `cipher`), vig, nl20 key | GOLD-K3 a | 81.3 / 78.5 / 70.9, mean 76.9 (gate 50 met) | -3.498 (`zutun:cipher:vig`); msg-1 best-of-30 -3.458 | inside the ten-text band (0.004 below its max, 0.033 above its median); 0.009 above the two-text top; judge FAIL |
| B'-c cipher-side mixing (mode `cipher`), beau, nl20 key | GOLD-K3 b | 77.1 / 76.4 / 72.2, mean 75.2 (gate 50 met) | -3.518 (`zickzack:cipher:beau`) | inside both bands (0.024 below the ten-text max); judge FAIL |
| B'-c modes `plaincipher`, `keycipher`, vig, nl20 key | GOLD-K4 unit 1 | 79.1 / 74.0 / 70.5, mean 74.5 (gate 50 met) | **-3.4935** (`ruht:plaincipher:vig`); msg-1 best-of-30 -3.491 | 0.0009 above the ten-text max and 0.0135 above the two-text top: the band's edge, not an excess (the ten-text max is itself one draw); judge FAIL (-0.963 vs real_p05 -0.823) |
| B' English keyword list (`wordcorpus=tools/data/en`), four modes, vig, nl20 key | GOLD-K4 unit 2 | 81.2 / 79.8 / 68.5, mean 76.5 (gate 50 met) | -3.515 (`opportunity:plain:vig`); msg-1 best-of-30 -3.473 | inside both bands (0.021 below the ten-text max); judge FAIL (-0.94) |
| B'-c modes `plaincipher`, `keycipher`, beau | owed (K4 box, 80 pct rule) | -- | -- | **not run**; the one empty cell of the `mixed_tabula` grid; command logged in the GOLD-K4 section |
| B''-c free cipher-side permutation (S3 free, S1 = S2 = id), vig, nl20 key | GOLD-B2D | **7.4 / 12.9 / 8.1, mean 9.5 (gate 50 NOT met)**; S3 letters correct 1 / 8 / 3 of 26 | not run (CONTROL BELOW GATE, exit 3); bands not run | **unidentifiable at 924 letters**; parked |
| B'' general (S1, S2, S3 free) | GOLD-B2D design paragraph | no chance with these objectives at this N (26!^2/26 more states, two symmetries) | not run | parked, no code |
| C book / word-sum code | cycle 1 | merged into B'' (its letter-arithmetic form) | -- | parked with B'' |
| D uniform one-time key | GOLD-2C step 1 | 1000 OTP trials, 99 pct bands | outside on 5/6 (IC pct 1.000, chi2 1.000, entropy 0.000, min count 0.001, L1 0.999) | **excluded** at 99 pct |
| D' hand-made non-uniform key | -- | -- | inside the keyed band, as any non-uniform key is | **unfalsifiable from the ciphertext**; only family A |
| E digit system re-lettered | cycle 3 | -- | -- | **untestable at this N** (B2D's 9.5 pct against a 50 pct gate is the number) |
| F Abwehr hand systems in print | cycle 1 | -- | -- | mostly excluded by facts 1-3; what survives is B'/B''/E, now all run or unidentifiable |

**Is the B' record complete?** At vig arithmetic, yes: seven of seven `mixed_tabula` placements and three keyword
lists, every one a control-backed negative with controls 72.6-89.6 pct and judge FAIL. At beau arithmetic, five of
seven placements (plain, key, both, full: K2 v1; cipher: K3 b); `plaincipher`/`keycipher` at beau is the one cell of
the grid never run. The largest excess over the ten-text band is unchanged: K2's beau -3.478, 0.016 nats above the
max (-3.4944); K4's -3.4935 sits 0.0009 above the same max, which is the edge of a ten-draw band, not a second excess
(a band's maximum moves by more than that when an eleventh draw is added). GOLD-K4's done line carried no `flag:`
and no judge PASS, so no re-derivation is owed and no cycle-5 Koehler brief is written.

**Decision, cycle 4: Köhler PAUSED for lane spend until family A material (ASKS 55: NARA RG 65 105-9673 and Farago
1971; ASKS 53: Kahn's six groups) or more ciphertext arrives.** Every cheap corner in the ladder is now run with a
passed control or shown unidentifiable with one; what remains (D' hand key, general B'', E) needs the FBI file, the
Farago chapter or the printed groups, all on the owner's desk. The one condition that reopens it: a document from
family A that names the system, the key text or a plaintext (then the re-derivation is a $3 Sonnet job through
`tools/family_run.py` with the named key), or a sixth message that lifts N past about 5,000 letters (then B''-c becomes
identifiable, GOLD-B2D's own curve). The pause starts now, not after the last beau unit: that unit's P(moves) is about
0.015 (the two placements read at noise under vig and the five other placements read at noise under beau; K3's beau
and vig on the same placement differed by 0.02 nats), which at about $3 for a one-unit box (about 25 minutes) is
0.05 per $10 -- above the 0.03 bar on cost alone, but a third of the reserve's cheapest Russian unit in absolute terms
(kaliningrad-2015 HYPOTHESES.md, cycle-4 block). It is not worth a box of its own; if a Sonnet worker is ever on
Köhler for another reason (family A material arriving), it runs first, from the command logged in the GOLD-K4 section,
so the grid reads seven of seven at both arithmetics. Rule 5: the target stays **partial** with its NEAR.md row (it beat
no control, but every negative has a passed control behind it and one number, K2's -3.478, sits 0.016 nats above a
ten-text band with no tail); never closed-negative.

**NEAR.md koehler-row numbers for the orchestrator (cycle 4).** GOLD-K4 unit 1 (plaincipher/keycipher, vig, Dutch
key): control 79.1 / 74.0 / 70.5 pct (mean 74.5, gate 0.5 met) vs target -3.4935 (0.0009 above the ten-text max
-3.4944, 0.0135 above the two-text top -3.507), judge FAIL; unit 2 (English keyword list, vig, Dutch key): control
81.2 / 79.8 / 68.5 (mean 76.5, gate met) vs target -3.515 inside both bands, judge FAIL. B' record: seven of seven
placements and three keyword lists at vig, five of seven at beau, all control-backed negatives; largest excess still
K2's beau -3.478 (0.016 above the ten-text max, under the 0.1-nat flag line). Next step: paused, owner asks (ASKS 55a
NARA file, 55b Farago, 53 Kahn's groups); reopened by family A material or more ciphertext; the beau
plaincipher/keycipher unit is an owed filler (about $3, 25 minutes), not a step.

**The beau excess, final read (unchanged from cycle 3).** K2's -3.478 is the one number in the record above every
noise draw seen (two-text top -3.507, ten-text max -3.494). The excess shrank from 0.029 to 0.016 when the band grew
from two draws to ten, which is what a tail does; a real signal in this pipeline is 0.35-0.5 nats (controls over their
near-misses and over noise), the msg-1 best-of-30 gap is 0.03, and the judge failed. K4's -3.4935 at the band's edge
is the same lesson from the other side: a ten-draw band's max is a soft ceiling. Bookkeeping, not a lead; a 30-text
band would cost about $6 and can only move the sentence, not the verdict. Not briefed.

**Cycle-5 Köhler jobs by expected value: none briefed.**

| rank | job | P(moves) | cost | P per $10 | brief |
|---|---|---|---|---|---|
| -- | beau `plaincipher`,`keycipher` (the grid's empty cell) | 0.015 | about $3 Sonnet, 25 min | 0.05 | not briefed; owed filler, command in the GOLD-K4 section |
| -- | 30-text beau band | 0 (bookkeeping) | $6 | 0 | not briefed |
| -- | B''-c with a decoder-objective anneal (hours per seed) or a Monte Carlo over (p, k, S3) | under 0.02 at this N | $20+ Fable + hours of CPU | under 0.01 | not briefed; reopen only with more ciphertext |
| -- | family A re-derivation once a document names the system | conditional on ASKS 55 / 53 | $3 Sonnet | n/a | written when the material arrives |

Rule 10: nothing in this file is a reading; status stays `open` in NOTES.md (`partial` on the board per rule 5's
near-solve amendment); the lane never writes solved, new, first or unpublished.

## Prior attempts (Bourdeau 15 Sept 2026)

Source: `github.com/dbourdeau/cyphersolver`, `abwehr/` folder (`NOTES.md`, `profile.json`, `msgs.py`, `periodic.py`,
`lm.py`), shallow-cloned and read by this job (GOLD-1A) 25 Sept 2026, MIT-licensed code / CC BY 4.0 text, credited
per rule 8, not copied. TARGETS.md row 47: "Köhler, Abwehr 1944 | skipped | ATTEMPTED 2026-09-15, skipped as
intractable." One Claude-Opus-5 session, a real control-backed campaign, not a solve.

Families tried, all with matched controls, against the pooled 924-letter ciphertext (Bourdeau's own transcription,
which differs from ours at 6 group positions -- see `ciphertext-variants.tsv`; families below were run on
Bourdeau's text, not ours):

| # | family | test | result |
|---|---|---|---|
| 1 | monoalphabetic substitution, transposition, ABC-Verfahren | index of coincidence | target IC 0.0398 vs German prose IC 0.076 vs random IC 0.0385 -- excluded (too flat for any of these) |
| 2 | periodic Vigenere / Beaufort / variant Beaufort, periods 1-26, in de/en/nl | quadgram hill-climb per period vs shuffled-ciphertext control at the same setting | best keys score at shuffle level, hundreds of points below real text -- excluded. Weak period-IoC peaks (237 at period 17, 140 at period 9; p=0.04 after correction) yield nothing when solved |
| 3 | ciphertext autokey, offsets 1-40 | undone directly, IoC of result | 0.039 at best -- excluded |
| 4 | running key from natural-language book text, standard tableau | likelihood of ciphertext letter counts under every plaintext x key combination (de/en/nl x de/en/nl x 3 variants) vs true running-key and shuffled controls | all models score below uniform (-4.0 nats); true 924-letter running-key ciphertexts score >= +7.5 in 95% of trials (median +18) -- excluded |
| 5 | Gronsfeld (digit shifts 0-9, e.g. from book page numbers) | same likelihood test, all offsets | <= +3.3 nats -- excluded |
| 6 | any Enigma wiring (not only G-31/G-312/G-260/G-111 tried in 2017) | letter-count chi-squared vs uniform, vs simulated Enigma-like German output (median chi-sq 26) | target chi-sq 57.9, p=0.0003 -- excluded. Driven by low `c` (14 vs 35.5 expected) and high `z` (55) |

Depth between messages: best cross-message coincidence rates 0.073-0.091 over 61 offsets -- what short overlaps
give by chance; no sign of key reuse.

Two systems left un-excluded by Bourdeau's tests (their own words): (a) a mixed-tableau (keyed) running-key
Vigenere/book-key system on a non-standard alphabet table, which could match the documented Dutch-prayer-book
procedure of the FBI-run Hamburg channel if these five messages turn out to belong to it after all; (b) a
hand-made one-time pad or random key table. Both are judged to have no practical ciphertext-only attack without
the book or the FBI's own plaintexts for the channel.

Bourdeau's own `abwehr/NOTES.md` "What would reopen it" section names exactly this job's targets: the FBI case
file on Koehler (NARA RG 65, possibly released under the Nazi War Crimes Disclosure Act) and Kahn's source file
in The National Archives -- both searched below.

A lane running `cheap_tests_in_order` item 5 (book cipher) should start from `periodic.py`/`lm.py` (MIT licence
permits copying, cite per rule 8) rather than re-deriving them, and should resolve the six-group transcription
discrepancy against a real page image first (rule 2) -- see `ciphertext-variants.tsv` for why Bourdeau's own
`abwehr/koehler_cryptologia.png` does not settle it.

-- GOLD-1A (Sonnet, session_012i9FKxBKg4uHiogV2PopJ5), 25 Sept 2026

## Family A, recovery (archive lookup)

See `ARCHIVE.md` for the full table and search log. Short version: no archive item located in this pass holds or
describes a decrypt of the five Paris messages. The strongest new lead is a real, uncatalogued-online FBI HQ file
for Walter Kohler (RG 65, class 105, file 9673, box 156, NARA location 230 86/16/05) -- existence and location
established from NARA's own released name-index PDFs, not yet opened by anyone in this repository. It is not
known to describe a "system" or key; class 105 is "Foreign Counterintelligence", consistent with an FBI file
about running Koehler as a double agent (the Hamburg book-cipher channel), not necessarily with the Paris
messages Koehler sent behind the FBI's back. No decrypt found anywhere; status stays open, not found-solved.
Constraint for families B-D: nothing found here narrows the system beyond what Bourdeau's campaign (above)
already excluded. The next-best documentary lead for the *system* (not a decrypt) is Ladislas Farago's 1971
"The Game of the Foxes", which per a secondary account drew on Koehler's own file in captured German records and
interviews with three Abwehr officers who remembered him -- also not opened in this pass (see ARCHIVE.md).

-- GOLD-1A (Sonnet, session_012i9FKxBKg4uHiogV2PopJ5), 25 Sept 2026

## Family B summary (GOLD-2A, 25 Sept 2026)

| Family | Test | Control (same N, design, language) | Target | Read |
|---|---|---|---|---|
| B running key (book key) | `tools/running_key.py` two-stream beam decode, order-8 KN letter models with latent word boundaries, beam 1000 | German plaintext under a held-out Dutch novel key, vig: 72.7 / 60.4 / 68.3% plaintext letters recovered (seeds 1-3); under a held-out German novel key, vig: 73.7 / 79.1 / 77.1% either-stream (strict 48.6 / 36.6 / 35.3%, the two streams are exchangeable under vig); beau and varbeau, Dutch key, seed 1: 76.0% | pooled joint log-likelihood per letter -3.57 to -3.62 on every configuration run (7; varbeau de/nl on 3 of 5 messages), inside the one-time-key noise band (-3.57 to -3.64); controls read -3.12 to -3.17 | control-backed negative for a running key on a modern German or Dutch novel-like text, conditional on the Kahn/Schmeh transcription and on letter models of 1880s-1920s fiction |
| long period | per-message coset IC, periods 31-120 | period-40/85/120 Vigenère on German, same lengths: IC 0.069-0.087 at the true period (or a multiple), seeds 1-3 | max 0.0664 at P=85; P(max over 31-120 >= 0.0664) = 0.10 on 2000 uniform texts of the same lengths | not distinguishable from a one-time key |
| B crib-drag | 67 German military/Abwehr words, all tabulae, key scored under de20 and nl20 letter models | top hit on uniform random text of the same lengths: -1.60 to -1.99 per letter (3 seeds x 2 key languages) | top hit -1.82 (de key, "werden" -> "citire"), -1.82 (nl key, "amerika" -> "jeaando") | inside the noise band |

### Family B, running key, detail (GOLD-2A, 25 Sept 2026, 16:48-18:15 UTC)

**Method.** `tools/running_key.py` (this job; offline test `tools/tests/test_running_key.py`). For each message
independently (the key offset in a book is unknown per message) find the plaintext p maximising
LM_p(p) + LM_k(k(p, c)), k fixed by the tabula (vig c = p + k, beau c = k - p, varbeau c = p - k, mod 26).
Letter n-gram models with interpolated Kneser-Ney (continuation counts on lower orders, D = 0.9), order 8, with a
latent word-boundary symbol in both streams (the decoder may insert a boundary before any letter in either stream;
boundaries are then dropped from the letters compared). Beam 1000 over the joint (plaintext context, key context)
state with recombination, 10 best expansions per hypothesis. No polish pass (on the English development set the
hill-climb never changed a beam optimum). The decoder is deterministic: target runs at seeds 1-3 are identical, so
each target configuration was run once; the seeds apply to the controls and noise.

**Tuning record (development, before the gate).** Held-out German cross-entropy (nats/letter): add-k-style
absolute discounting order 5 1.84; KN order 6 1.70, order 7 1.68. Control recovery (de plaintext / nl key, seed 2,
two messages 140 + 229): letters-only order 6 beam 1000 52.3%; order 7 56.1%; + word boundaries order 6 59.3%,
order 7 61.0%, order 8 64.2%; order 7 beam 3000 62.1% (beam is not the limit). On every control message checked
the decoded pair out-scored the true pair (e.g. -3.27 vs -3.70 per letter): errors are model errors, not search
errors, so a larger corpus would help more than a larger beam.

**Corpora.** `tools/data/de20` (7 Gutenberg novels 1883-1919, Fontane, Hesse, Döblin, Wassermann, about 2.5M
letters) and `tools/data/nl20` (7 Gutenberg novels, Multatuli-era to 1920s incl. Couperus, Van Eeden, Kloos,
Streuvels' Flemish Rozeke, about 2M letters), fetched by GOLD-C. No prayer book, no military German, no 1940s text:
the models are literary prose. The real key text (if a book) is unknown; the real plaintext is telegraphic German.

**Control design (rule 3).** Five messages of the target's lengths 237/178/140/140/229. Plaintext cut from one
de20 book, key from a different book (de20 or nl20), each at a random start in the middle 90% of the book (skips
front matter), seeded. Both books are held out of both language models. Same decoder settings as the target.
Per-message cells below read strict plaintext recovery / either-stream recovery.

| run | seed | plaintext book | key book | plain | either | per message | ll_p / ll_k |
|---|---|---|---|---|---|---|---|
| vig, nl key | 1 | Schach von Wuthenow | Rozeke van Dalen 2 | **72.7%** | 75.4% | 237:44/49 178:79/81 140:79/83 140:76/79 229:91/91 | -1.586 / -1.569 |
| vig, nl key | 2 | Effi Briest | Dichtertje etc. | **60.4%** | 65.3% | 237:73/76 178:69/71 140:58/64 140:49/59 229:50/54 | -1.565 / -1.596 |
| vig, nl key | 3 | Schach von Wuthenow | Rozeke van Dalen 2 | **68.3%** | 72.4% | 237:82/84 178:80/83 140:59/65 140:72/76 229:48/55 | -1.546 / -1.616 |
| vig, de key | 1 | Schach von Wuthenow | Frau Jenny Treibel | 48.6% | **73.7%** | 237:36/65 178:74/90 140:31/62 140:74/84 229:37/70 | -1.518 / -1.655 |
| vig, de key | 2 | Effi Briest | Der Mann von vierzig Jahren | 36.6% | **79.1%** | 237:57/87 178:28/66 140:19/79 140:12/81 229:48/79 | -1.607 / -1.508 |
| vig, de key | 3 | Schach von Wuthenow | Frau Jenny Treibel | 35.3% | **77.1%** | 237:68/84 178:26/83 140:9/81 140:10/49 229:39/80 | -1.534 / -1.586 |
| beau, nl key | 1 | Schach von Wuthenow | Rozeke van Dalen 2 | 76.0% | 76.0% | 237:57 178:83 140:66 140:81 229:93 | -1.593 / -1.565 |
| varbeau, nl key | 1 | same | same | 76.0% | 76.0% | identical to beau (c -> -c symmetry) | -1.593 / -1.565 |
| vig, nl plain, nl key | 1 | Een liefde | Eline Vere | 45.8% | 77.6% | 237:33/74 178:54/82 140:21/81 140:75/79 229:50/76 | -1.567 / -1.596 |

**GATE: passed** for vig with a Dutch key (strict recovery >= 60% on seeds 1-3) and for vig with a German key on
the either-stream measure (>= 73% on seeds 1-3). Strict recovery with a German key is 35-49%: under vig with the
same language in both streams the decoder has no way to tell plaintext from key and swaps them in stretches, so on
the target a de/de reading would have to be read from both streams. Beau/varbeau: one seed each (76%), not three.
The 140-letter messages are the hardest (9-83%).

**Noise band.** Uniform random (one-time key) ciphertext of the same five lengths, decoded with the same settings:
pooled joint log-likelihood per letter (ll_p + ll_k) de/de -3.636, de/nl -3.571, nl/nl -3.600 (seed 1 each;
per-message joint -3.55 to -3.66). Control decodes of real running-key cipher: -3.12 to -3.17 pooled
(per message about -3.0 to -3.3). The gap is about 0.45 nats per letter.

**TARGET** (`specs/koehler-1944.json`, the Kahn/Schmeh transcription, 924 letters).

| config | ll_p | ll_k | joint | noise band (same models) | control joint |
|---|---|---|---|---|---|
| de plain, de key, vig | -1.752 | -1.857 | -3.609 | -3.636 | -3.12 to -3.17 |
| de plain, de key, beau (= varbeau with streams swapped) | -1.723 | -1.845 | -3.568 | -3.636 | (not run for beau de/de) |
| nl plain, nl key, vig | -1.704 | -1.912 | -3.616 | -3.600 | -3.163 |
| de plain, nl key, vig | -1.841 | -1.748 | -3.589 | -3.571 | -3.155 to -3.162 |
| de plain, nl key, beau | -1.707 | -1.900 | -3.607 | -3.571 | -3.158 |
| de plain, nl key, varbeau (msgs 1-3 only: the process was killed for memory after msg 3) | msg joint -3.601 / -3.576 / -3.653 | | | per-message noise -3.55 to -3.66 | -3.158 |

Every target configuration run sits in the noise band and about 0.4-0.5 nats per letter below every control. No
stretch in any target decode stands above noise; none was sent to ROOM as a flag, and no reading is claimed.

Partial decodes (15+ letter stretches, both streams; shown to document what noise looks like, not as readings).
Target de/de vig msg 4: P `wollte_weil_es_gut_mit_beiden_hielten` / K `lagen_ihr_an_hem_faulbeinig_inhalflau`; msg 5:
P `mochte_so_gross_wie_hauser` / K `die_unruhig_uber_diese_worte_eisen`. Noise de/de seed 1 (uniform random
cipher) msg 5: P `um_den_wagen_strandes_der_guitarre_flog_den_kopfe_vorweg_und_blieben`. The decoder produces
word-salad stretches of this quality on any input; only the log-likelihood against the noise band separates them.

Relation to Bourdeau's test 4 (above): his exclusion was a letter-count likelihood test on his transcription (6
groups differ from ours, `ciphertext-variants.tsv`); this is an independent two-stream decode on the Kahn/Schmeh
transcription as in `specs/koehler-1944.json`, with its own controls. The two agree (no standard-tableau running key
on natural-language text detected). Neither covers Bourdeau's open case (a), a mixed (keyed) tableau.

**Dead ends and limits.** (1) The models are 1880s-1920s literary fiction; a 1940s military plaintext, a prayer-book
key or a technical manual key are outside them, and the control does not cover those registers. (2) Stream swap under
vig with same-language models. (3) Memory: order-8 models with word boundaries take 3-4 GB per process; four at once
were killed by the container (OOM) twice; run at most three. (4) Crib-drag: 67 German words, all tabulae, key scored
under de20 and nl20; the best hits (-1.82/letter) sit inside the uniform-random band (-1.60 to -1.99). (5) Period
scan 31-120: target max 0.0664 at P = 85 (z = +3.9 at that single period; after taking the maximum over 90 periods,
p = 0.10 on 2000 uniform texts), against 0.069-0.087 at the true period for a matched German Vigenère control at
P = 40, 85, 120. Not distinguishable from a one-time key.

Next test named by this negative: family C (book or word-sum code, key-text identification) or family A (archive
recovery), per UNSOLVED-SURVEY.md's Gold-lane ladder; within B, a larger or period-matched corpus (1930s-40s German
military/administrative prose, a Dutch prayer book) is the only lever the model-error diagnosis leaves.

Files: `running-key/control_*.txt`, `noise_*.txt`, `target_*.txt`, `period_scan_31_120.tsv`, `cribdrag_*.tsv`,
`cribs.txt`. Reproduce a row with, e.g.,
`python3 tools/running_key.py --control --pcorpus tools/data/de20 --kcorpus tools/data/nl20 --spaces --order 8 --beam 1000 --seed 1 --tabula vig`
and `python3 tools/running_key.py specs/koehler-1944.json --pcorpus tools/data/de20 --kcorpus tools/data/nl20 --spaces --order 8 --beam 1000 --tabula vig`.

-- GOLD-2A (Opus, running-key tool), 25 Sept 2026

## Family B', keyed-tableau running key (GOLD-2C, 25 Sept 2026, 18:26-19:03 UTC)

Bourdeau's open case (a): a running (book) key through a mixed, keyed tableau, c = S3(S1(p) + S2(k)) with unknown
alphabet permutations. Two steps, a statistic and then a family run through `tools/family_run.py` (parent rule
18:18). Worker: Fable, session_01MD88FhWpv6brRnw9QfVG5n.

### Step 1, permutation-invariant distribution test (`scripts/keyed_dist_test.py`, `.out`, `.json`)

Under any keyed tableau the ciphertext letter distribution is a permutation of a circular convolution of the
(permuted) plaintext and key unigram distributions, so the SORTED count profile, IC, entropy and chi-square vs
uniform are invariant to S3 and depend on S1, S2 only through which letters happen to combine. Simulated 1000 times
at the five target lengths (seed 1): de20 plaintext windows, de20 or nl20 key windows from a different book, three
uniformly random permutations (KEYED); uniform random letters (ONE-TIME KEY); identity permutations (STANDARD,
Bourdeau's family 4, for reference only). Percentile = share of simulated texts at or below the target.

| statistic | TARGET | KEYED 99% band (percentile) | ONE-TIME-KEY 99% band (percentile) | STANDARD 99% band (percentile) |
|---|---|---|---|---|
| IC | 0.0399 | 0.0386-0.0419 (0.52) inside | 0.0379-0.0395 (1.000) OUTSIDE | 0.0392-0.0425 (0.16) inside |
| entropy, bits | 4.653 | 4.617-4.679 (0.41) inside | 4.662-4.693 (0.000) OUTSIDE | 4.611-4.669 (0.80) inside |
| chi-square vs uniform, 25 df | 58.65 | 27.7-108.3 (0.52) inside | 10.5-48.6 (1.000) OUTSIDE | 41.5-122.0 (0.16) inside |
| max count | 55 | 47-74 (0.46) inside | 42-58 (0.98) inside | 49-73 (0.28) inside |
| min count | 14 | 10-26 (0.06) inside | 17-29 (0.001) OUTSIDE | 10-25 (0.12) inside |
| L1 to one-time-key mean sorted profile | 71.1 | 23.5-140.2 (0.52) inside | 12.1-61.3 (0.999) OUTSIDE | 41.0-156.4 (0.16) inside |

Target sorted counts 55 47 47 47 46 46 44 40 39 37 36 36 35 33 33 32 31 31 31 30 29 28 28 26 23 14; keyed mean 57 51
48 46 44 42 41 40 39 38 37 36 35 34 33 33 32 31 30 29 28 27 26 24 23 20; one-time-key mean 48 45 43 ... 27 24.
Beside it, Bourdeau's standard-tableau number (15 Sept 2026, a letter-IDENTITY unigram likelihood, not
permutation-invariant): target below uniform where true running-key text scores >= +7.5 nats in 95% of trials.
Read: the target's letter counts sit at the median of what a keyed running key gives and outside the one-time-key
band on five of six statistics (the sorted profile cannot separate keyed from standard; only a letter-identity
test can, and Bourdeau's did). GATE: family B' is NOT excluded at step 1 (the brief's stop condition did not fire).
The same statistic is also what any non-uniform hand-made key gives, so "not one-time key" here means "not a
UNIFORM one-time key".

### Step 2, keyword-mixed tableau search (`tools/families/keyed_running_key.py`, via `family_run.py --gate 0.5`)

**Method.** Restricted to tableaux built from one keyword-mixed alphabet M (what an agent could carry), four
placements (`running_key.mixed_tabula`): plain (S1 = index in M), key (S2 = index in M), both (S1 = S2), full (S1 =
S2, cipher read out of M: the classic mixed Vigenère square), arithmetic vig (beau/varbeau available, not run). Stage
1 ranks every candidate (11,437 distinct alphabets from words of 4-12 letters in de20 + nl20, x 4 modes + the
identity = 45,749) by the multinomial log-likelihood of the pooled 924 letter counts under the distribution the
tableau predicts (conv(de20 unigram, nl20 unigram) permuted by the tableau), in nats above uniform: 26x26 per
candidate, seven seconds for all. Stage 2 decodes the top 30 with `running_key.py`'s two-stream beam (order 6,
Kneser-Ney, latent word boundaries, beam 300, LM_p de20, LM_k nl20) on message 1 (237 letters), keeps the tableau
with the best joint log-likelihood per letter, and decodes all five messages under it. Score = pooled joint
log-likelihood per letter (GOLD-2A's noise band for this decoder family: -3.57 to -3.64; controls -3.12 to -3.17
at order 8, beam 1000).

**Control (rule 3).** Per seed: German plaintext windows at 237/178/140/140/229 from one de20 book, key windows from
one nl20 book (Dutch book key), keyword drawn from the same word list, mode drawn from the four, both books held
out of the models. Stage-1 calibration on six seeds before the run (true keyword's rank among 45,749): 6, 3, 4, 27,
1, 2 -- hence top 30. Stage 2 on seed 1: the true tableau `grube:plain` scored -2.894 per letter on message 1
against -3.39 to -3.53 for the 29 near-miss alphabets (`bucher`, `duchesse`, `burger`, ...), a 0.5-nat gap.

| seed | keyword, mode (control) | stage-1 rank of the true keyword (of 45,749) | stage 2, msg 1 joint ll/letter: true tableau vs best near-miss | plaintext letters recovered (pooled, strict) | pooled joint ll/letter |
|---|---|---|---|---|---|
| 1 | grube, plain | 6 | -2.894 vs -3.252 (druber) | **79.1%** | -3.01 |
| 2 | ausschlag, plain | 3 | -3.003 vs -3.396 (schlug) | **74.0%** | -3.10 |
| 3 | omsloeg, key | 4 | (lines lost, see note in the log) | **64.7%** | -3.18 |

**CONTROL pooled mean 72.6% (64.7-79.1%) on 3 seeds; GATE 50% met** (family_run.py row below, 18:50 UTC). In every
seed the stage-2 winner was the true tableau, and the plaintext (not the key stream) was recovered because the Dutch
key model and the German plaintext model differ (GOLD-2A's stream-swap caveat for a German key applies here too).

**Stage-1 noise band** (`running-key/keyed_stage1_noise.out`): best stage-1 score over all 45,749 candidates on 20
uniform random texts of the target's lengths: min -5.5, median 0.1, max 6.9 nats. TARGET best stage-1 score 11.8
(`zustimmung:key`; then `schlurfte:full` 10.4, `truus:full` 9.2, `hauswirtin:key` 8.8, `wofur:both` 8.4); the
standard tableau on the target -13.9 (rank far down, as Bourdeau found). Controls' true keywords scored 12-49 nats
on the six calibration seeds. So on stage 1 alone the target sits above the one-time-key band and at the bottom of
the keyed-control range -- consistent with either a keyed tableau whose keyword is in or near the list or with any
other non-uniform key; stage 2 decides.

**TARGET** (the Kahn/Schmeh transcription, `specs/koehler-1944.json`, 924 letters; `families/keyed_running_key-1.txt`,
re-run to `running-key/keyed_target_rerun.log` because the family_run log's tail was lost to a `git rebase --autostash`
while the process was writing -- lesson: never autostash with a live log in the tree; the decoder is deterministic and
the re-run reproduces the row's score exactly).

| | stage-1 best (nats over uniform) | stage 2, msg 1 joint ll/letter: best of 30 (range) | pooled joint ll/letter, winner | winner |
|---|---|---|---|---|
| TARGET | 11.8 (`zustimmung:key`) | **-3.470** (-3.586 to -3.470) | **-3.534** | `waarvan:plain` (stage-1 rank about 30, 5.8 nats) |
| NOISE, full pipeline on uniform random text, seed 1 | -1.4 | -3.492 (-3.589 to -3.492) | -3.544 | `papenhagen:plain` |
| NOISE, seed 2 | 8.3 | -3.477 (-3.586 to -3.477) | -3.507 | `jongetje:plain` |
| CONTROL seeds 1-3 (true tableau) | 12-18 | -2.894 / -3.003 / (lost) | -3.01 / -3.10 / -3.18 | true keyword, 79.1 / 74.0 / 64.7% read |

Read: on the target no candidate tableau stands out in stage 2 (best-of-30 -3.470 against the noise pipeline's
-3.477 to -3.492; the controls' true tableau stands 0.35-0.5 nats above its near-misses), and the winner's pooled
score -3.534 sits inside the full-pipeline one-time-key band (-3.507 to -3.544) and 0.35-0.5 nats below every
control (-3.01 to -3.18). The stage-1 winner `zustimmung:key` (11.8 nats, above the stage-1 noise band) did not
survive stage 2 (msg 1 -3.51). Judge on the winner's decode: FAIL (score -0.901 vs real_p05 -0.823; its null_p99 of
-2.071 is far below because the decoder emits German-like letter strings on any input, so the judge's null is not
the right noise for a decoder output -- the pipeline noise band above is). Decoded streams are word salad of the
kind GOLD-2A documented (msg 1 P `schenambrutetedannauchherwarnochaufumso...`, K `evisplaatsingalonessetrieknieten...`);
no stretch of 15+ letters in either stream reads above the noise band, so nothing was sent to ROOM as a flag and no
reading is claimed. **Control-backed negative** for a running key on de20/nl20-like text through a tableau built from
one keyword-mixed alphabet (four placements, vig arithmetic, keyword within de20 + nl20's 11,437 words), conditional
on the transcription and on the literary-prose models. Together with Bourdeau's family 4 and GOLD-2A's family B, the
standard and the keyword-mixed tableau are both excluded at this control strength; what remains of Bourdeau's case
(a) is a tableau outside the keyword-mixed set (see limits), and case (b), a hand-made non-uniform key, which step 1
cannot separate from a keyed running key. Next test named by this negative: family C (code / word-sum book cipher)
or family A (archive recovery), as GOLD-2A said; within B', `--param arith=beau`, a German key (`kcorpus=tools/data/de20`,
read from both streams) and an English word list are the cheap remaining variants, each about the same box as this run.

**Dead ends and limits.** (1) Keyword-mixed alphabets only: a transposition-block mixed alphabet, a phrase, a name
outside de20/nl20's vocabulary, or two different keywords on the two sides are outside the candidate set; a general
permutation search (26!^3) has no cheap scorer at 924 letters. (2) Porta and a keyed Beaufort were not run
(`--param arith=beau|varbeau` exists; a keyed Porta does not). (3) The same model-register limit as family B:
1880s-1920s literary prose for a 1944 telegraphic plaintext and an unknown key book. (4) Stage 1 assumes the key
stream has a natural-language unigram distribution (Dutch); a German key is covered by `kcorpus=tools/data/de20`
(not run within the box). (5) Decoder settings are lighter than GOLD-2A's (order 6, beam 300 vs order 8, beam 1000)
for the 30-candidate stage 2; the control number is what these settings read.

Files: `scripts/keyed_dist_test.py|.out|.json`, `running-key/keyed_family_run.log`, `running-key/keyed_stage1_noise.out`,
`families/keyed_running_key-1.txt` (if the target ran), the family_run.py table row below. Reproduce:
`python3 ciphers/koehler-1944/scripts/keyed_dist_test.py --trials 1000 --seed 1` and
`python3 tools/family_run.py specs/koehler-1944.json --family keyed_running_key --corpus tools/data/de20 --param kcorpus=tools/data/nl20 --param top=30 --param beam=300 --param order=6 --param spaces=1 --seeds 3 --gate 0.5`.

-- GOLD-2C (Fable, session_01MD88FhWpv6brRnw9QfVG5n), 25 Sept 2026

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 18:50 | keyed_running_key | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/nl20,top=30,beam=300,order=6,spaces=1 | 1 | 0.726 (0.647-0.791) | -3.534 | FAIL language: score=-0.901, null_p99=-2.071, real_p05=-0.823, real_median=-0.78, mode=both, N=924 | yes (gate 0.5) | GOLD-2C family B' keyed tableau, keyword-mixed alphabets, control before target |
| 25 Sept 2026 20:16 | keyed_running_key | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/nl20,arith=beau,top=30,beam=300,order=6,spaces=1 | 1 | 0.781 (0.662-0.855) | -3.478 | FAIL language: score=-0.937, null_p99=-2.071, real_p05=-0.823, real_median=-0.78, mode=both, N=924 | yes (gate 0.5) | GOLD-K2 B' beau, Dutch key, keyword-mixed, control before target |
| 25 Sept 2026 20:37 | keyed_running_key | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/nl_dev,top=30,beam=300,order=6,spaces=1 | 1 | 0.848 (0.810-0.878) | -3.583 | FAIL language: score=-0.982, null_p99=-2.071, real_p05=-0.823, real_median=-0.78, mode=both, N=924 | yes (gate 0.5) | GOLD-K1 B' keyword-mixed, devotional Dutch key (nl_dev), control before target -- target rerun standalone after a timeout |

## Family B' variants (GOLD-K2), 25 Sept 2026, worker GOLD-K2 (Sonnet, session_0196VjuQaoVfdo8pYY9Avvm9)

The three untried corners named at the end of the GOLD-2C section above: beau arithmetic (Dutch key), a German
key (both streams German, vig), and an English keyword list (`wordcorpus=` option added to
`tools/families/keyed_running_key.py` for this). Same method as GOLD-2C throughout: stage 1 ranks keyword-mixed
tableaux by the pooled unigram multinomial likelihood, stage 2 beam-decodes the top 30 (order 6, beam 300, LM_p
de20, LM_k per variant) on message 1, pooled joint log-likelihood per letter is the score. Noise band for this
exact pipeline (GOLD-2C, two uniform-random texts of the target's lengths): -3.507 to -3.544 per letter; a target
above -3.40 (0.1 nats above the band's top) without a judge PASS is a ROOM flag per the brief.

### Variant 1: beau arithmetic, Dutch key (`--param arith=beau --param kcorpus=tools/data/nl20`)

CONTROL (German plaintext, held-out nl20 key, keyword from the de20+nl20 list, seeds 1-3): 85.5 / 82.5 / 66.2 pct
plaintext letters recovered, mean 78.1 pct -- gate 50 pct met.

TARGET: stage-1 best 13.4 nats over uniform (`rijpende:plain`); stage-2 winner `aufgabe:plain:beau` (stage-1 rank
lower, 12.3 nats), msg-1 best-of-30 -3.443; pooled joint ll (all 5 messages) **-3.478** per letter, 0.03-0.07 nats
above the -3.507/-3.544 noise band (below the -3.40 flag line, so not flagged). Judge: FAIL (score -0.937 vs
real_p05 -0.823, null_p99 -2.071, mode=both). Message 1 decoded streams, first 40 letters (word salad, not a
reading): P `smaskemitderlangertewasjetztistichzusche`, K `rotterdopvinnigswantgevalenerdehoelangzo`.
Control-backed negative for the beau-arithmetic corner of the keyword-mixed tableau family (same keyword list as
GOLD-2C's vig run).

### Variant 2: vig arithmetic, German key, both streams German (`--param kcorpus=tools/data/de20 --param arith=vig`)

With plaintext and key corpus both `tools/data/de20`, the streams are exchangeable under vig (same caveat GOLD-2A
logged for the standard-tableau family): the control's STRICT recovery (decoded "P" stream vs the true plaintext
label) reads near chance, 6.4/8.5/7.7 pct (mean **7.7 pct**, well below gate 0.5), because the decoder's search is
free to land on either labelling. Computing the EITHER-STREAM recovery (decoded "P" stream vs whichever of the two
true streams it actually matches; `truth_key` added to `keyed_running_key.solve()`'s info dict for this) gives
89.6 / 90.7 / 88.6 pct (mean **89.6 pct**) -- the method reads the German-key control very well once the label
ambiguity is accounted for. Gated the target run on the either-stream number (0.5 met), not the tool's own
strict-only default, which would have wrongly reported CONTROL BELOW GATE (both rows are in the table below: the
first, strict-gated, correctly shows the tool's default behaviour; the second reruns the target after gating on
either-stream).

TARGET: stage-1 best 10.9 nats over uniform (`wachturme:both`); stage-2 winner `schlurfte:full:vig` (stage-1 rank
lower, 8.5 nats), msg-1 best-of-30 -3.487; pooled joint ll (all 5 messages) **-3.573** per letter, *below* the
-3.507/-3.544 noise band's bottom (worse than both noise draws -- no signal, not a flag). Judge: FAIL (score
-0.975 vs real_p05 -0.823, null_p99 -2.071, mode=both). Message 1 decoded streams, first 40 letters (word salad,
not a reading): P `rfuhrensichnurihrgraduberfreitstandnisst`, K `pulthelfenaufeinschauungtaitseknurrenart`.
Control-backed negative for the German-key corner of the keyword-mixed tableau family, read correctly (either
stream) rather than under the tool's default strict labelling.

### Variant 3: English keyword list -- not run

`--param wordcorpus=DIR[,DIR]` was added to `tools/families/keyed_running_key.py` (draws the stage-1 keyword list
from named corpora instead of corpus+kcorpus; tested in `tools/tests/test_keyed_running_key.py`) so this box could
try `wordcorpus=tools/data/en16_repo,tools/data/de20,tools/data/nl20`. Not run: variants 1 and 2 (control+target,
~25 minutes each) used most of this job's 75-minute box; the option is built, tested and pushed for the next
Koehler B' job to spend its box on the run itself, control first.

## Families B and B', devotional Dutch key (GOLD-K1), 25 Sept 2026, 19:57-20:46 UTC

Every Family B and B' negative logged so far (GOLD-2A, GOLD-2C, GOLD-K2) is conditional on `tools/data/nl20`'s
1880-1920 Dutch novel-prose key model, while the one documented Koehler key is a Dutch prayer book (CLAUDE.md).
This job builds a devotional-register Dutch corpus and reruns Family B (standard tableau, `tools/running_key.py`)
and Family B' (keyword-mixed tableau, `tools/family_run.py --family keyed_running_key`) under it. Worker: Sonnet,
session_01WDJiUb1ijocbB3N3LtsLWk.

**Corpus** (`tools/data/nl_dev/`, README.md/MANIFEST.tsv): the Statenvertaling (17th-century Dutch Bible
translation), fetched in one request from `api.getbible.net/v2/statenvertaling.json` (route (c) of the brief's
order; (a) dbnl.org unreachable, `SSL_ERROR_SYSCALL`; (d) gutendex.com for a Catholic Dutch prayer book
unreachable, timeout on both the try and the one permitted retry -- no such text found, as GOLD-C also found
none on Gutenberg for nl20). 67 files (one per book), 3,426,073 letters after folding, `distribution_license:
"Public Domain"` per the API's own metadata. Closest reachable register to a prayer book, not the item itself
(README.md "Limits").

**Family B, standard-tableau running key** (`tools/running_key.py --spaces --order 8 --beam 1000`, de20 plaintext
model, nl_dev key model).

CONTROL (German plaintext at the target's 5 lengths, held-out nl_dev book key, vig, seeds 1-3): 83.0 / 89.5 /
80.3 pct plaintext letters recovered, mean **84.3 pct** (range 80.3-89.5) -- gate 60 pct met, and higher than
nl20's control on the same test (72.7/60.4/68.3 pct, GOLD-2A): the Bible's more repetitive vocabulary makes it
an easier key model for the decoder, a property of the corpus, not evidence either way about which corpus the
real key was.

TARGET, two tabulae:

| tabula | ll_p | ll_k | pooled joint ll/letter | GOLD-2A noise band (order 8, beam 1000, same models) | control (GOLD-2A) |
|---|---|---|---|---|---|
| vig | -1.882 | -1.706 | **-3.588** | -3.57 to -3.64 | -3.12 to -3.17 |
| beau | -1.899 | -1.741 | **-3.640** | -3.57 to -3.64 | -3.12 to -3.17 |

Both configurations sit inside the established one-time-key noise band (not re-run for nl_dev specifically --
per this job's brief, reused from GOLD-2A; the noise band's own LM_k was trained on nl20/de20, so this is an
approximation, noted as a limit) and about 0.45-0.5 nats below every control. Neither is above the band's top
by 0.1 nats or more, so no ROOM flag. Message 1 decoded streams, first 40 letters (word salad, not a reading):
vig P `lhattenbipphonsche_goldung_ihre_truppe`, K `nuthai_den_zoon_van_kenaz_bid_achter_t`; beau P
`lzahlt_kommandavorwuluht_oh_das_zweite`, K `jathefatha_die_in_dienzelven_noch_gog_`.

**Control-backed negative** for a standard-tableau running key under a devotional (Bible) Dutch key model, same
strength as GOLD-2A's negative under the novel-prose model.

**Family B', keyword-mixed tableau** (`tools/family_run.py --family keyed_running_key`, order 6, beam 300, de20
plaintext model, nl_dev key model). CONTROL (German plaintext, held-out nl_dev book key, keyword from the
de20+nl_dev-derived word list*, seeds 1-3): 87.8 / 81.0 / 85.6 pct plaintext letters recovered, mean **84.8 pct**
(range 81.0-87.8) -- gate 50 pct met. TARGET winner `mixed:evelyn:plain:vig` (stage-1 rank about 11, 5.77 nats
over uniform; `zustimmung:key` again the stage-1 leader at 11.06 nats, as in every prior run of this family, but
did not win stage 2 here either): pooled joint ll **-3.583** per letter, inside GOLD-2C's full-pipeline noise
band (-3.507 to -3.544) -- actually 0.04-0.08 nats *below* its bottom, i.e. no signal at all, not a flag. Judge:
FAIL (score -0.982 vs real_p05 -0.823, null_p99 -2.071, mode=both). Message 1 decoded streams, first 40 letters
(word salad): P `offelnliebstkaumzuhabemirheuterneidige`, K `iskariotvijandwasmijeenenzoonkruikenka`.
(*The first family_run.py invocation for this job ran all 3 control seeds to completion -- logged in the table
row above, 20:37 UTC -- but was killed by an over-tight 1500s timeout partway through the target's stage 2;
`scripts/gold_k1_bprime_target_only.py` reruns the target only, reusing that same logged control rather than
recomputing it a second time. Not a shortcut around rule 3: the control was run and read before the target, only
the re-run of the *target after a timeout* skipped repeating the control.)

**Control-backed negative** for a keyword-mixed tableau under a devotional Dutch key model, same strength as
GOLD-2C's and GOLD-K2's negatives under the novel-prose model.

**Read across all three key registers now run (nl20 novel prose, nl20+beau, nl_dev devotional Bible):** every
Family B and B' configuration tried lands inside its noise band regardless of register. The key-register lever
named in the cycle-1 consolidation (GOLD-CONS1) does not move Koehler off the noise band for either tableau
family; the standard and keyword-mixed tableaux stay excluded whether the Dutch key model is 1880-1920 novels or
a 17th-century Bible translation. What is not yet ruled out: a Catholic Dutch prayer book specifically (not
located, see Limits above), a German-register devotional key, and the general (non-keyword) permutation B''.

**Limits.** (1) This is the Bible, not the documented prayer book (README.md's own limits, above). (2) The
noise band comparisons reuse GOLD-2A's and GOLD-2C's bands (trained on nl20/de20), not a band re-trained on
nl_dev; a corpus swap could in principle shift the noise band itself as well as the control, though the control
numbers here (80-90 pct recovery, similar or higher than nl20's) argue against the devotional corpus being a
*weaker* language model that would make the noise band easier to sit inside. (3) Family B' target run used a
standalone rerun script after a timeout, documented above, not `family_run.py`'s own committed row for the
target line (the table row above is from the direct run, correctly attributed to `family_run.py`'s own
CONTROL-then-TARGET path; the *decode itself* came from the rerun script). (4) No noise-band or control number
was recomputed for Family B at order 6/beam 300 (not needed; every order-8/beam-1000 control finished in
6-7 minutes, well under the brief's 15-minute drop-down trigger).

Files: `tools/data/nl_dev/{README.md,MANIFEST.tsv,*.txt.gz}`, `ciphers/koehler-1944/scripts/gold_k1_bprime_target_only.py`,
`ciphers/koehler-1944/families/keyed_running_key-1-nldev.txt`, the family_run.py table row (20:37 UTC) above.
Reproduce Family B: `python3 tools/running_key.py --control --pcorpus tools/data/de20 --kcorpus tools/data/nl_dev
--spaces --order 8 --beam 1000 --seed 1 --tabula vig` and `python3 tools/running_key.py specs/koehler-1944.json
--pcorpus tools/data/de20 --kcorpus tools/data/nl_dev --spaces --order 8 --beam 1000 --tabula vig` (or `--tabula
beau`). Reproduce Family B' control: `python3 tools/family_run.py specs/koehler-1944.json --family
keyed_running_key --corpus tools/data/de20 --param kcorpus=tools/data/nl_dev --param top=30 --param beam=300
--param order=6 --param spaces=1 --seeds 3 --gate 0.5 --control-only`.

-- GOLD-K1 (Sonnet, session_01WDJiUb1ijocbB3N3LtsLWk), 25 Sept 2026

## Family B'', permuted tableau (GOLD-B2D), 25 Sept 2026, 21:39-22:05 UTC

Worker GOLD-B2D (Fable, session_01GvGAepME5fvmUDuaJuc9cA), brief `.claude/briefs/runs/2026-09-25-lane-gold-c3-koehler-bprime2-design.md`.
Family B'' is c = S3(S1(p) + S2(k)) mod 26 with S1, S2, S3 free permutations; this job built the tool for the first sub-family
B''-c (S1 = S2 = identity, S3 free: a free permutation on the cipher side of a standard running-key square, equivalently
c' = S3^-1(c) is a standard-tableau running-key ciphertext) and ran its matched control. GOLD-K3's `mixed_tabula(..., "cipher")`
(pushed df3f7f9 while this job ran) is the keyword-restricted instance of the same tableau; `perm_tabula` reproduces it exactly
for every keyword under vig/beau/varbeau (checked on `koehler`), so the two modules agree where they overlap.

**Tool.** `tools/families/permuted_tableau.py` (registered in `family_run.py`; offline test `tools/tests/test_permuted_tableau.py`,
27 s): `perm_tabula(S1, S2, S3, arith)` in `mixed_tabula`'s dict shape, accepted by `running_key.key_of`, `encipher`, `beam_decode`
unchanged. Search, three stages: (1) the sort-match start (ciphertext letters by count matched to the sums s = p + k by the
predicted conv(de20 unigram, nl20 unigram)); (2) simulated annealing over S3 (swap 80 pct, 3-cycle 20 pct; T0 = median |delta| of
200 random swaps from the start, measured per run at 10.5-13.8, geometric to T0/200; 30,000 evaluations per chain, stop after
6,000 non-improving; 3 chains, chain 1 from the sort-match start, 2-3 random) under a CHEAP PROXY objective; (3) the top 3 distinct
chain winners rescored by the two-stream beam decoder on message 1's first 140 letters at ANNEAL settings (order 5, beam 80, word
boundaries on, LM_p de20, LM_k nl20), the best decoded on all five messages at the STANDARD settings (order 6, beam 300), pooled
joint log-likelihood per letter as the family score, comparable to GOLD-2C's band. The brief's objective (the decoder itself)
was measured first and does not fit: **1.59-1.80 s per evaluation** at anneal settings (order 5, beam 80, 140 letters), so 1,500-3,000
evaluations per chain x 3 chains x 3 seeds is 4-7 hours of decoder time, beyond a 90-minute box; the brief's "cheaper objective"
clause was used. The proxy (the brief's option 2, made primary): the n-gram log-likelihood of c' = S3^-1(c) under the empirical
n-gram distribution of the SUM stream s = p + k, built once by adding the training de20 and nl20 texts letter by letter mod 26 at
3 random offsets (6.7M sum n-grams, order 4, add-0.5 smoothing, 6 s to build, pure Python since this container has no numpy);
delta-scored over the 909 windows a move touches, **0.12-0.15 ms per evaluation**. Two more search modes were built and measured
when the proxy failed (below): `search=beam`, an open-tableau beam decoder that carries a partial S3 in every hypothesis (26
open positions of 676 (p, k) options each, the rest on the mapped sum line; contexts reset per message, the mapping persists), and
`refine=ROUNDS`, a decoder-guided greedy over swaps proposed by proxy delta plus random swaps.

**Control (rule 3), `family_run.py --gate 0.5`, seeds 1-3** (row in the table below, 21:56 UTC; log
`scripts/permuted_tableau_control_seeds1-3.log`): German plaintext windows at 237/178/140/140/229 from one de20 book, key windows
from one held-out nl20 book, S3 uniformly random from 26!, both books out of the models and out of the proxy table. About 95 s per seed.

| seed | S3 (control) | sort-match start, letters of S3 correct (exact / under best shift) | best chain, letters correct (exact / shift) | chain proxy scores | rescore winner msg1[:140] joint ll/letter | pooled plaintext recovery | pooled joint ll/letter |
|---|---|---|---|---|---|---|---|
| 1 | eclbjfrqgxszwvukdhioytnmap | 2 / 4 | 1 / 5 | -11742, -11736, -11747 | -3.426 | **7.4 pct** | -3.475 |
| 2 | dczjkyepgrhwuaxiolqmnfvsbt | 3 / 4 | 8 / 8 | -11666, -11654, -11650 | -3.340 | **12.9 pct** | -3.463 |
| 3 | fjqdlstonbaxickyemvuzpwghr | 2 / 3 | 3 / 3 | -11712, -11693, -11714 | -3.372 | **8.1 pct** | -3.47 |

**CONTROL mean 9.5 pct (7.4-12.9) on 3 seeds; GATE 0.5 NOT met; the target was not run** (exit 3). Chance is 3.8 pct; the anneal
reads a random cipher-side permutation only slightly above chance. Neither of the two bands nor the target was run, per the brief
(bands after the control clears). The pooled scores -3.46 to -3.475 sit at GOLD-2C's noise band (-3.507/-3.544) and 0.3-0.45 nats
below what the true S3 reads (controls -3.01 to -3.18 for a known tableau): the identifiability is there, the search does not reach it.

**Why the proxy fails at 924 letters (`scripts/permuted_tableau_landscape.py`, `.out`, seed 1).** At orders 2 and 3 the anneal's winner
OUTSCORES the true S3 under the proxy (order 2: true -5953.0, anneal -5934.1, random mean -6052; order 3: true -8866.7, anneal
-8825.9) and at order 4 it matches it (true -11760.4, anneal -11768.6) with 4/26 letters right: the marginal n-gram statistics of
924 letters of a sum stream do not contain S3, which is GOLD-2C step 1's finding (the profile sits at the keyed band's median) one
order up. The same proxy does identify S3 once the text is long enough: English (Holmes plain x Moby-Dick key, order 3) 3/26 at
2,000 letters, 26/26 at 6,000 (one chain) and 26/26 at 8,000 (the offline test, best of two chains). **The proxy needs roughly
5,000 or more letters; the target has 924.** Adding pairings or evaluations cannot change that (the table is not the limit, the
target is).

**Why the decoder objective cannot be searched from far away.** Landscape at anneal settings on control seed 1, msg1[:140]: true S3
-3.336; 1 random swap away -3.475 / -3.430; 2 swaps -3.479 / -3.448; 3 swaps -3.504 / -3.346; 5 swaps -3.436 / -3.518; 8 swaps
-3.501 / -3.523; 13 swaps -3.555 / -3.611; a random S3 -3.615. A steep hill within 1-3 swaps of the truth (0.1-0.14 nats per letter
per swap, 14-20 nats over 140 letters, unmistakable), flat beyond about 8 swaps. Full 325-swap neighbourhood of seed 2's best
start (8/26 correct, -3.340; `scripts/permuted_tableau_nbhd.py`, `_nbhd_seed2.out`, 3 processes, 1.6 s per evaluation): of the 17
swaps that add a correct letter, every one LOWERS the objective (best -3.363); of the 9 swaps that raise it (best `ci` -3.296), none
adds a correct letter and 6 remove one. So a greedy or an anneal on the decoder objective from 8/26 walks away from the truth; the
hill is only climbable from a start with about 20 or more letters right, and no cheap start gives that (sort-match 2-3/26).
`refine=25` (8 decoder-scored proposals per round) accordingly stopped in round 1 on seeds 1 and 2.

**Open-tableau beam (`search=beam`, seed 1).** Beam 500 / per_open 20: 0/26 exact (4 under a shift), joint -3.440 per letter on 924
letters, recovery 6.5 pct, 26 s. Beam 2000 / per_open 40: 0/26 (3 under a shift), -3.458, recovery 6.9 pct, 89 s. With the mapping
free the decoder fits both streams to any commitment made at the 26 first occurrences; the true partial mapping is pruned early.

**Dead ends, named:** (a) proxy anneal at orders 2/3/4, 30k evaluations x 3 chains: at or below chance plus a few letters; (b)
open-tableau beam at widths 500 and 2000; (c) decoder-guided greedy with 8 proposals per round; (d) the full 325-swap decoder
neighbourhood from the best start, which shows (c) cannot be fixed by more proposals.

**What a 26!-search would need, from these numbers.** Either a start within about 3 swaps of the truth (20+ of 26 letters; the
sort-match gives 2-3, the proxy 1-8), or an objective with the decoder's power at the proxy's price. The decoder's power comes from
joint inference over both streams; a Monte Carlo / EM over (p, k, S3) with the beam's posterior would be the honest next design, at
tens of seconds per iteration on 924 letters, and is not obviously convergent from a flat start. Nothing here reduces the cost
below hours per seed. **General case (S1, S2, S3 free), design paragraph, no code:** the general anneal has 26!^2/26 more states than
B''-c and two extra symmetries (the (S1 + t, S2 - t) shift family and the stream swap under vig); its objective can only be the
decoder (the proxy has no S3 information at 924 letters, and none about S1, S2 either, since the sum stream's n-gram distribution
under permuted p and k is what the proxy already fails to use). With B''-c's control at 9.5 pct and a decoder landscape flat beyond
8 swaps for ONE permutation, a three-permutation anneal at 924 letters has no chance with these objectives. **Recommendation: park
B'' (both sub-families) at this control; do not brief the general case.** Cheap corners that remain live are the keyword-restricted
cipher-side placements (GOLD-K3, `mixed_tabula` modes cipher/plaincipher/keycipher: a word list makes the 26! search a ranking) and
a longer text, which the target does not have.

**Reproduce.** Control (this row): `python3 tools/family_run.py specs/koehler-1944.json --family permuted_tableau --corpus tools/data/de20
--param kcorpus=tools/data/nl20 --param arith=vig --seeds 3 --gate 0.5 --label "..."` (exit 3, about 5 minutes). Landscape and
proxy-vs-length: `python3 ciphers/koehler-1944/scripts/permuted_tableau_landscape.py` (about 3 minutes). Neighbourhood:
`python3 ciphers/koehler-1944/scripts/permuted_tableau_nbhd.py 2 koxbdjepgytwqcharliumfvszn K 3` for K in 0 1 2 (3 minutes in parallel).
Open beam and refine: `python3 ciphers/koehler-1944/scripts/permuted_tableau_ctl1.py 1 search=beam open_beam=2000 per_open=40` and
`... 2 refine=25`. Owed if anyone reopens B''-c with a better search (only then): the shuffle band `--shuffle-target S` for S = 1-3
and three uniform-random texts of the five lengths through the same command, and the target itself; beau arithmetic (`--param
arith=beau`) likewise. Rule 10: nothing here is a reading; NOTES.md status stays `open`.

-- GOLD-B2D (Fable, session_01GvGAepME5fvmUDuaJuc9cA), 25 Sept 2026 22:05 UTC

## Family B'-c, cipher-side placements (GOLD-K3), 25 Sept 2026, worker GOLD-K3 (Sonnet, session_01K4n8VHbDXGiaAwDk12dgrP)

Not run by anyone before this job: a mixed alphabet on the CIPHER side alone (`running_key.mixed_tabula` mode
`cipher`: S3 = M, S1 = S2 = identity -- standard plain and key letters, the rows of the vig/beau square shifted and
read out through M; the commonest practical way a Vigenere square was mixed by hand) and the two mixed pairs
`plaincipher` (S1 = M, S3 = M) and `keycipher` (S2 = M, S3 = M), added to `tools/running_key.py` this job (test:
`tools/tests/test_keyed_running_key.py`, `mixed_tabula('grube','cipher')` checked against the standard vig table
mapped through M for all 676 cells; `keyed_running_key.stage1` already ranks tableaux generically through the
tabula's `enc` table, so no family-side change was needed). Same method as GOLD-2C/K2 throughout: stage 1 ranks
keyword-mixed tableaux by the pooled unigram multinomial likelihood (11,438 candidates: the de20+nl20 word list,
one mode per run, plus the identity), stage 2 beam-decodes the top 30 (order 6, beam 300, LM_p de20, LM_k nl20) on
message 1, pooled joint log-likelihood per letter over all 5 messages is the score.

**Ten-text beau noise band** (`ciphers/koehler-1944/scripts/keyed_noise_band.py`, run in the background as two
processes of 5 texts each while the family runs below were going; `running-key/keyed_beau_noise_band.tsv` and the
two raw logs): the full pipeline at GOLD-K2 variant 1's exact settings (arith=beau, kcorpus=nl20, top=30, beam=300,
order=6, spaces=1, modes default plain/key/both/full) on 6 uniform-random texts (seeds 1-6) and 4 shuffles of the
target's own 924 letters (seeds 1-4, pooled then redistributed into the five message lengths, so stage 1 ranks
identically to the real target -- the sharper of the two floors). Ten scores: -3.5071, -3.5282, -3.5481, -3.5474,
-3.5340, -3.5328, -3.4944, -3.5266, -3.4995, -3.5330. **min -3.5481, median -3.5305, max -3.4944.** The four
shuffle scores (-3.5266, -3.4995, -3.4944, -3.5330) sit no lower than the six uniform scores; shuffling the
target's own letters instead of drawing fresh random ones does not sharpen the floor here.

### Variant (a): vig arithmetic, cipher-side mode, Dutch key (`--param modes=cipher --param arith=vig`)

CONTROL (German plaintext, held-out nl20 key through a random cipher-side-mixed tableau, keyword from the de20+nl20
list, seeds 1-3): 81.3 / 78.5 / 70.9 pct plaintext letters recovered, mean **76.9 pct**, gate 50 pct met (row in the
table below, 22:04 UTC).

TARGET: stage-1 best 10.5 nats over uniform (`zuchtend:cipher`); stage-2 winner `zutun:cipher:vig` (stage-1 rank
near the bottom of the top 30, 1.41 nats), msg-1 best-of-30 **-3.458** (range -3.588 to -3.458); pooled joint
log-likelihood (all 5 messages) **-3.498** per letter -- above the two-text band's top (-3.507) by 0.009 nats and
inside the ten-text band (below its max of -3.4944 by 0.004 nats, above its median by 0.033). Judge: **FAIL**
(score -0.887 vs real_p05 -0.823, null_p99 -2.071, real_median -0.78, mode=both, N=924). Not flagged (below the
-3.40 line by a wide margin on both bands). Message 1 decoded streams, first 40 letters (word salad, not a
reading): P `efrapptsiedemdreijungenbeklombauenkwangd`, K `valenbaronestjeomdieietsgegaanofikgebrok`. Control-backed
negative for the vig cipher-side corner of the keyword-mixed tableau family. Decode backed up as
`families/keyed_running_key-1-vigcipher.txt` before variant (b), same seed, overwrote the shared path.

### Variant (b): beau arithmetic, cipher-side mode, Dutch key (`--param modes=cipher --param arith=beau`)

CONTROL (same design, beau arithmetic, seeds 1-3): 77.1 / 76.4 / 72.2 pct, mean **75.2 pct**, gate 50 pct met (row
in the table below, 22:27 UTC).

TARGET: stage-1 best 9.6 nats over uniform (`zuerst:cipher`); stage-2 winner `zickzack:cipher:beau` (stage-1 rank
8th of 30, 6.4 nats), msg-1 best-of-30 **-3.488** (range -3.602 to -3.488); pooled joint log-likelihood **-3.518**
per letter -- inside both the two-text band (-3.544 to -3.507) and the ten-text band (below its max of -3.4944 by
0.024 nats, above its median -3.5305 by 0.013). Judge: **FAIL** (score -0.972 vs real_p05 -0.823, null_p99 -2.071,
mode=both, N=924). Not flagged. Message 1 decoded streams, first 40 letters (word salad, not a reading): P
`eckigerfigurengonnteihmberthalbscheineng`, K `dhemarinevanjozefontloosnuikboerderiiifr`. Control-backed negative
for the beau cipher-side corner. Decode backed up as `families/keyed_running_key-1-beaucipher.txt`.

### Variant (c): plaincipher and keycipher modes, vig, Dutch key -- not run, owed

Variants (a) and (b) (control + target each) took about 24 minutes apiece with the box's process contention (this
job's own two background noise-band processes plus one family_run.py, three decoder processes throughout, as the
brief allows); by the time (b) finished only about 20 minutes remained in this job's 75-minute box, not enough to
run a third control-plus-target cycle of the same shape and still write this section up. Owed to the next Koehler
B' job at the same box size: `python3 tools/family_run.py specs/koehler-1944.json --family keyed_running_key
--corpus tools/data/de20 --param kcorpus=tools/data/nl20 --param modes=plaincipher,keycipher --param arith=vig
--param top=30 --param beam=300 --param order=6 --param spaces=1 --seeds 3 --gate 0.5`.

**Reading K2's beau/Dutch-key target and this job's own beau target against the ten-text band.** K2's variant 1
(full/plain/key/both modes, beau, Dutch key) pooled score was -3.478. Against the old two-text band it sat 0.029
(-3.507) to 0.066 (-3.544) nats above the top; against this job's ten-text band it is STILL above the max (-3.4944)
by 0.0164 nats -- smaller than before, since the wider band's own top is higher than the two-text band's top, but
K2's reading has not moved inside the band, it remains the one number in this family's whole record sitting above
every noise draw (still well under the -3.40 flag line, so not flagged, and still judge FAIL). This job's own beau
target (variant b, cipher mode, -3.518) is different: it sits INSIDE the ten-text band, 0.024 nats below its max
and 0.013 above its median. So widening the band from two draws to ten did not clear K2's target of sitting above
every noise draw seen so far, it only shrank the margin; a single value above ten draws is not itself evidence
(the band has no tail at n=10 either), so this is bookkeeping, not a lead, and K2's reading remains an
unclassified excess pending a larger band, not a candidate.

**Read across all three cipher-side placements.** Both controls clear gate at rates similar to the four
placements already run (72.6-89.6 pct in GOLD-2C/K1/K2 vs 76.9/75.2 pct here), so the method reads a real
cipher-side-mixed tableau about as well as the other four placements when one is present. Both targets sit inside
the noise band on both bands. Together with GOLD-2C, K1, K2 (four placements: plain, key, both, full) and
GOLD-B2D's B''-c (a general 26!-permutation search on the cipher side alone, control below gate at this N), this
extends the control-backed negative for family B' to six of the seven `mixed_tabula` placements at vig and beau
arithmetic, keyword restricted to the de20+nl20 list; `plaincipher`/`keycipher` (variant c) and varbeau arithmetic
remain untried corners of the same restricted search.

Files: `tools/running_key.py` (modes cipher/plaincipher/keycipher), `tools/tests/test_keyed_running_key.py`,
`ciphers/koehler-1944/scripts/keyed_noise_band.py`, `running-key/keyed_beau_noise_band.tsv` (+ `_A.log`, `_B.log`),
`families/keyed_running_key-1-vigcipher.txt`, `families/keyed_running_key-1-beaucipher.txt`, the two family_run.py
table rows below (22:04 and 22:27 UTC). Reproduce: `python3 tools/tests/test_keyed_running_key.py`; the two
family runs, `--param modes=cipher --param arith=vig` and `--param arith=beau`, both otherwise as in variant (a)
above; the noise band, `python3 ciphers/koehler-1944/scripts/keyed_noise_band.py u1 u2 u3 u4 u5 u6 s1 s2 s3 s4
--out running-key/keyed_beau_noise_band.tsv` (about 60 minutes single-threaded; split across processes as this job
did to run alongside the family runs). Rule 10: nothing here is a reading; NOTES.md status stays `open`.

-- GOLD-K3 (Sonnet, session_01K4n8VHbDXGiaAwDk12dgrP), 25 Sept 2026

## Family B', owed runs (GOLD-K4), 26 Sept 2026, worker GOLD-K4 (Sonnet, session_01PYtPexePhLjYkgc8VsZ7Zn)

The two runs GOLD-K3 left owed (variant c cipher-side placements, plaincipher/keycipher at vig) plus GOLD-K2's
owed English keyword list. Same method throughout (stage 1 unigram-count ranking over the de20+nl20 candidate
list unless noted otherwise, stage 2 beam-decodes the top 30, order 6, beam 300, LM_p de20, LM_k nl20). Bands
compared against: two-text full-pipeline noise -3.507 / -3.544 (GOLD-2C); ten-text beau-pipeline noise band min
-3.5481, median -3.5305, max -3.4944 (GOLD-K3).

### Unit 1: plaincipher and keycipher modes, vig arithmetic, Dutch key (`--param modes=plaincipher,keycipher --param arith=vig`)

CONTROL (German plaintext, held-out nl20 key, keyword from the de20+nl20 list, mode drawn from plaincipher/keycipher,
seeds 1-3): 79.1 / 74.0 / 70.5 pct plaintext letters recovered, mean **74.5 pct** -- gate 50 pct met.

TARGET: stage-1 best 11.2 nats over uniform (`furchten:keycipher`); stage-2 winner `ruht:plaincipher:vig` (stage-1
rank lower, 6.9 nats), msg-1 best-of-30 **-3.491**; pooled joint log-likelihood (all 5 messages) **-3.4935** per
letter -- 0.0135 nats above the two-text band's top (-3.507) and 0.0009 nats above the ten-text band's max
(-3.4944), the closest any `mixed_tabula` placement in this family has sat to that ceiling, still well under the
-3.40 / -3.394 flag line. Judge: **FAIL** (score -0.963 vs real_p05 -0.823, null_p99 -2.071, mode=both, N=924).
Message 1 decoded streams, first 40 letters (word salad, not a reading): P `kommlichvondienurinihrsetzteeffibeiderku`,
K `looppenhaarouderaanglimlhoofdeengoestenl`. Control-backed negative for the plaincipher/keycipher corner; this is
the seventh of seven `mixed_tabula` placements to run at vig arithmetic.

### Unit 2: English keyword list, default modes, vig arithmetic, Dutch key (`--param modes=plain,key,both,full --param wordcorpus=tools/data/en`)

CONTROL (German plaintext, held-out nl20 key, keyword drawn from `tools/data/en` -- three 1880-1925 Gutenberg
novels -- mode from plain/key/both/full, seeds 1-3): 81.2 / 79.8 / 68.5 pct letters recovered, mean **76.5 pct** --
gate 50 pct met.

TARGET: stage-1 best 11.3 nats over uniform (`illustration:key`); stage-2 winner `opportunity:plain:vig` (stage-1
rank near the bottom of the top 30, 5.3 nats), msg-1 best-of-30 **-3.473**; pooled joint log-likelihood **-3.515**
per letter -- inside both the two-text band (-3.507 to -3.544) and the ten-text band (min -3.5481, median -3.5305,
max -3.4944; -3.515 sits 0.0155 above the median, 0.021 below the max, not near either edge). Judge: **FAIL**
(score -0.94 vs real_p05 -0.823, null_p99 -2.071, mode=both, N=924). Message 1 decoded streams, first 40 letters
(word salad, not a reading): P `tfragenmittagundundsturzsimistinflaggefi`, K `vorsfalmplannenendithaarlevenhetveelgoed`.
Control-backed negative for an English keyword drawn from outside the de20+nl20 list restriction; this is the third
keyword list tried for this family (de20+nl20 restricted list, German-only via `kcorpus=de20`, English via
`wordcorpus=tools/data/en`).

### Unit 3: beau arithmetic, plaincipher/keycipher modes -- not run

Units 1 and 2 (control+target each) took about 22 and 25 minutes respectively; by the time unit 2 finished, this
job was at 47 of its 75-minute box (63 pct), and a third control-plus-target cycle of the same shape (about
20-25 minutes on this record) would have crossed the brief's 80 pct rule before finishing. Not started. Owed to
whoever next spends a Koehler B' box: `python3 tools/family_run.py specs/koehler-1944.json --family
keyed_running_key --corpus tools/data/de20 --param kcorpus=tools/data/nl20 --param modes=plaincipher,keycipher
--param arith=beau --param top=30 --param beam=300 --param order=6 --param spaces=1 --seeds 3 --gate 0.5`.

**Record status.** At vig arithmetic, all seven `mixed_tabula` placements (plain, key, both, full -- GOLD-2C/K1/K2;
cipher -- GOLD-K3; plaincipher, keycipher -- this job) have now run, all control-backed negatives, judge FAIL
throughout; the vig placement record is complete. At beau arithmetic, five of seven have run (plain/key/both/full
-- GOLD-K2 variant 1; cipher -- GOLD-K3 variant b); plaincipher/keycipher at beau (unit 3 above) is the one placement
left in the whole `mixed_tabula` grid. Three keyword lists have now been tried at vig (de20+nl20 restricted,
German-only, English), all control-backed negatives.

Files: `families/keyed_running_key-1-kcorpus=tools_data_nl20,modes=plaincipher,keycipher,arith=vig,top=30,beam=300,or.txt`,
`families/keyed_running_key-1-kcorpus=tools_data_nl20,modes=plain,key,both,full,arith=vig,top=30,beam=300,orde.txt`,
the two family_run.py table rows below (23:52 and 00:16 UTC). Reproduce: the two commands above (unit 1's
`--param arith=vig` variant already run; unit 3's `--param arith=beau` variant is what remains). Rule 10: nothing
here is a reading; NOTES.md status stays `open`.

-- GOLD-K4 (Sonnet, session_01PYtPexePhLjYkgc8VsZ7Zn), 26 Sept 2026

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 20:47 | keyed_running_key | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/de20,arith=vig,top=30,beam=300,order=6,spaces=1 | 1-3 | 0.078 (0.064-0.085) | not run (CONTROL BELOW GATE) | - | no (gate 0.5) | GOLD-K2 B' vig, German key |
| 25 Sept 2026 20:54 | keyed_running_key | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/de20,arith=vig,top=30,beam=300,order=6,spaces=1 | 1 | strict 0.077 (0.064-0.085); either-stream 0.896 (0.886-0.907) | -3.573 | FAIL language: score=-0.975, null_p99=-2.071, real_p05=-0.823, real_median=-0.78, mode=both, N=924 | yes (gate 0.5 on either-stream) | GOLD-K2 B' vig, German key, gated on either-stream recovery (streams exchangeable) |
| 25 Sept 2026 21:56 | permuted_tableau | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/nl20,arith=vig | 1-3 | 0.095 (0.074-0.129) | not run (CONTROL BELOW GATE) | - | no (gate 0.5) | GOLD-B2D B''-c cipher-side permutation anneal (sum-stream proxy), control before target |
| 25 Sept 2026 22:04 | keyed_running_key | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/nl20,modes=cipher,arith=vig,top=30,beam=300,order=6,spaces=1 | 1 | 0.769 (0.709-0.813) | -3.498 | FAIL language: score=-0.887, null_p99=-2.071, real_p05=-0.823, real_median=-0.78, mode=both, N=924 | yes (gate 0.5) | GOLD-K3 B'-c cipher-side mixed alphabet, vig, Dutch key, control before target |
| 25 Sept 2026 22:27 | keyed_running_key | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/nl20,modes=cipher,arith=beau,top=30,beam=300,order=6,spaces=1 | 1 | 0.752 (0.722-0.771) | -3.518 | FAIL language: score=-0.972, null_p99=-2.071, real_p05=-0.823, real_median=-0.78, mode=both, N=924 | yes (gate 0.5) | GOLD-K3 B'-c cipher-side, beau, Dutch key |
| 25 Sept 2026 23:52 | keyed_running_key | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/nl20,modes=plaincipher,keycipher,arith=vig,top=30,beam=300,order=6,spaces=1 | 1 | 0.745 (0.705-0.791) | -3.494 | FAIL language: score=-0.963, null_p99=-2.071, real_p05=-0.823, real_median=-0.78, mode=both, N=924 | yes (gate 0.5) | GOLD-K4 B'-c plain+cipher and key+cipher, vig, Dutch key, control before target |
| 26 Sept 2026 00:16 | keyed_running_key | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/nl20,modes=plain,key,both,full,arith=vig,top=30,beam=300,order=6,spaces=1,wordcorpus=tools/data/en | 1 | 0.765 (0.685-0.812) | -3.515 | FAIL language: score=-0.94, null_p99=-2.071, real_p05=-0.823, real_median=-0.78, mode=both, N=924 | yes (gate 0.5) | GOLD-K4 B' English keyword list, vig, Dutch key, control before target |
