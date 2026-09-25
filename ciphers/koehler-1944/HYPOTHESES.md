# Köhler cryptograms -- hypotheses and prior attempts

Working file for constraints on the system behind the five February 1944 Köhler cryptograms (see NOTES.md for
the target, sources and check-solved verdict). Everything below the first `##` is append-only, dated and signed by
the job that wrote it. This top block is rewritten once per cycle by the lane's consolidator and by nobody else.

**Summary, cycle 1** (GOLD-CONS1, Fable, session_017PRh6MAX17rgp5ayuycZ6c, 25 Sept 2026 19:30 UTC)

**Target facts every family must respect.** 924 letters in five messages of 237 / 178 / 140 / 140 / 229 (Kahn heads
the third "137"; it prints 140). All 26 letters present (j 32, q 39, x 33); counts run z 55 down to c 14, sorted
profile 55 47 47 47 46 46 44 40 39 37 36 36 35 33 33 32 31 31 31 30 29 28 28 26 23 14. Two message lengths are odd.
The transcription is Schmeh 2021 reproducing Kahn 1981 pp.65-66 (no image); it differs from Bourdeau's at six
single letters (`ciphertext-variants.tsv`, ASKS row 53) -- immaterial to every statistical test below, material
to any decode. No depth between messages (Bourdeau). IC 0.0399 pooled.

**The single most informative fact so far (GOLD-2C step 1).** The letter statistics sit at the median of what a
language key through a permuted tableau gives (inside the keyed band on 6/6 statistics, percentile 0.41-0.52 on
four of them) and outside the uniform one-time-key 99 pct band on 5/6 (IC pct 1.000, chi-square 1.000, entropy
0.000, min count 0.001, L1 0.999). So the key stream is **not uniform**: it carries a unigram skew of about the size
a natural-language key gives, and the ciphertext alphabet is a permutation of the sum. Two structural facts cut
further: transposition of anything with a language profile is excluded by the flat IC, and a 25-letter digraphic
square (Playfair, Doppelkasten) is excluded because j is present and two lengths are odd. What is left is the
family "non-uniform key + letter arithmetic + at least one unknown alphabet permutation", in which the standard
tableau (Bourdeau 4, GOLD-2A) and the keyword-mixed tableau (GOLD-2C) are the two corners already closed.

| family | status | CONTROL | TARGET | what it rests on / what is left |
|---|---|---|---|---|
| A recovery (TNA KV 2/KV 3/HW 19/HW 20/HW 40, FBI Vault, NARA RG 65, Kahn's source, Farago 1971) | **blocked on the owner** (ASKS 55: NARA 105-9673 and Farago; ASKS 53: Kahn pp.65-66 for the six groups) | n/a | no decrypt, key or system located (GOLD-1A, ARCHIVE.md) | nothing a cloud worker can add until the owner writes to NARA or reads Farago; one message-count coincidence ("137 messages by March 1944" vs the "137" header) noted, uncorroborated |
| Bourdeau's six: MASC / transposition / ABC-Verfahren; periodic Vig-Beau-varBeau 1-26 de/en/nl; ciphertext autokey 1-40; standard-tableau running key (unigram-identity likelihood); Gronsfeld; any Enigma wiring | **excluded** by Bourdeau 15 Sept 2026, each with a matched or shuffled control, on his transcription (6 letters from ours) | his: true running key >= +7.5 nats in 95 pct of trials; Enigma-like chi-sq median 26 | IC 0.0398; periodic keys at shuffle level; running key below uniform (-4.0 nats); chi-sq 57.9 (p 0.0003) | cited, not rerun (rule 8, MIT/CC BY 4.0); nothing here needs a second run on our transcription |
| B standard-tableau running key, two-stream beam decode (`tools/running_key.py`) | **parked** (GOLD-2A) | 60.4-79.1 pct plaintext letters recovered, 3 seeds, Dutch or German novel key (gate 60 met) | joint ll -3.57 to -3.62 per letter on 7 configs, inside the one-time-key noise band -3.57 to -3.64; controls -3.12 to -3.17; period scan 31-120 max 0.0664 at P=85 (p 0.10); crib-drag top -1.82 inside noise -1.60 to -1.99 | conditional on 1880-1920 literary-prose models for both streams: a devotional or military key text is outside them (K1 below) |
| B' keyed tableau, keyword-mixed alphabets (`tools/families/keyed_running_key.py`) | **parked with both numbers; continue only on the untried variants** (GOLD-2C) | 79.1 / 74.0 / 64.7 pct, mean 72.6, gate 50 met; true tableau stage-1 rank 1-27 of 45,749 | winner -3.534 per letter inside the full-pipeline noise band -3.507 to -3.544; best-of-30 -3.470 vs noise -3.477/-3.492; judge FAIL | run so far: vig arithmetic, Dutch key, one keyword from de20+nl20 words, four placements. Untried: beau/varbeau, a German key read from both streams, English/French keywords, transposed-keyword alphabets, two different keywords, and the general permutation (B'' below) |
| B'' general permuted tableau (S1, S2 annealed on the pooled unigram likelihood, S3 free; the stage-2 decoder as discriminator) | **open, not run**; cycle-3 candidate | design owed (Fable, about $12): NEAR.md row item (2) | -- | only family that covers the rest of Bourdeau's case (a); no cheap scorer at 924 letters beyond the stage-1 multinomial, so identifiability is the risk; a 1000-permutation noise band is the control |
| C book or word-sum code (Thouless-type; Bean 2019 key-text ranking) | **downgraded, parked** | -- | -- | a word-sum with letter arithmetic on a standard tableau *is* family B, excluded twice; Bean's ranking by decrypt letter frequencies is Bourdeau's test 4. What survives is a codebook with letter superencipherment, which has no ciphertext-only attack at 924 letters without the book. Reopen only as B'' with named candidate key texts |
| D uniform one-time key | **excluded at 99 pct on 5/6 statistics** (GOLD-2C step 1) | 1000 simulated OTPs at the five lengths | see the fact above | -- |
| D' hand-made non-uniform key (a table of letters or digits written by hand, or any key with a language-like skew) | **open, unfalsifiable from the ciphertext alone**; park by definition | -- | inside the keyed band 6/6 | only family A can resolve it; the lane does not spend on it |
| E digit system re-lettered (straddling checkerboard, additive from a book or table, digit pairs to letters through a 2-digit table) | **hypothesis, not tested; weakly disfavoured** | -- | a 100-cell table onto 26 letters gives two count tiers (4 cells vs 3 cells, about 37 vs 28 at N=924) after a flattening additive; the target's profile is a smooth gradient with a 4x spread (55 to 14) | a short repeating additive would keep a language skew and fit; no cheap test better than B'' names it. Not briefed this cycle |
| F Abwehr hand systems of 1943-44 as described in print (to check, not cited from memory as fact: Kahn, *Hitler's Spies* 1978; Kahn, *The Codebreakers* ch. on WWII agent ciphers; the ISOS histories): double columnar transposition keyed by a book line; substitution table then transposition; Doppelkasten; Rasterschlüssel 44; book-page additive systems | **mostly excluded by the two structural facts** (transposition keeps IC; digraphic squares need 25 letters and even lengths) | -- | -- | what survives of F is a substitution table with a non-uniform additive, i.e. B'/B''/E. One line for the owner's Farago read (ASKS 55): note how the Hamburg channel's prayer-book cipher turned a page into a key -- letters, digits, or a transposition key |

**Decisions, cycle 1.** A: park (owner). Bourdeau's six: excluded, cited. B: park. B': continue on the four cheap
variants, one Sonnet box (K2). B'': design in cycle 3 if K1 and K2 come back flat. C: park (merged into B''). D:
excluded. D': park. E, F: recorded, not briefed. New this cycle: the key-register lever (K1) -- every B and B'
negative is conditional on 1880-1920 novel models for the key stream, while the one documented Koehler key is a
Dutch prayer book; a devotional Dutch key corpus (Statenvertaling and a Catholic prayer text if reachable) is the
cheapest change that both strengthens the logged negatives and gives B/B' another run.

**Next two Köhler jobs by expected value** (P(the first result moves the target) x value / cost; P is a judgement):

| rank | job | P(moves) | cost | EV per dollar | brief |
|---|---|---|---|---|---|
| 1 | K2: B' variants on the existing corpora -- `arith=beau`, German key (`kcorpus=tools/data/de20`, both streams read), English keyword list; control first per variant, gate 0.5 | about 0.05 per variant, 0.15 for the three | $6 Sonnet | 0.025 V | `2026-09-25-lane-gold-c2-koehler-bprime-variants.md` |
| 2 | K1: devotional Dutch key corpus (`tools/data/nl_dev`, at most 40 fetches, one host at a time), then B (standard) and B' (keyword-mixed) reruns with `kcorpus=nl_dev`, controls first | about 0.10 | $8 Sonnet | 0.0125 V, plus it tightens every prior B/B' negative | `2026-09-25-lane-gold-c2-koehler-devotional-key.md` |
| 3 (cycle 3) | B'' general permuted tableau, Fable design then Sonnet runs | about 0.10 | $12 + $10 | 0.0045 V | not briefed |

K1 and K2 are independent (different workers, CPU-bound, at most three decoder processes each for memory) and
may run at once. Both stop at a control that fails its gate: the tool or corpus is fixed first, never the target.
Rule 10: nothing in this file is a reading; status stays `open`; the lane never writes solved, new, first or
unpublished.

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

