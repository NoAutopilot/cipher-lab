# Köhler cryptograms -- hypotheses and prior attempts

Working file for constraints on the system behind the five February 1944 Köhler cryptograms (see NOTES.md for
the target, sources and check-solved verdict). Append-only by convention; each section is dated and signed by
the job that wrote it.

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
| B running key (book key) | `tools/running_key.py` two-stream beam decode, order-8 KN letter models with latent word boundaries, beam 1000 | German plaintext under a held-out Dutch novel key, vig: 72.7 / 60.4 / 68.3% plaintext letters recovered (seeds 1-3); under a held-out German novel key, vig: 73.7 / 79.1 / 77.1% either-stream (strict 48.6 / 36.6 / 35.3%, the two streams are exchangeable under vig); beau and varbeau, Dutch key, seed 1: 76.0% | pooled joint log-likelihood per letter -3.57 to -3.62 on every run so far, inside the one-time-key noise band (-3.57 to -3.64); controls read -3.12 to -3.17 | control-backed negative for a running key on a modern German or Dutch novel-like text, conditional on the Kahn/Schmeh transcription and on letter models of 1880s-1920s fiction |
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
| de plain, nl key, vig / beau / varbeau | see the appended block below | | | -3.571 | -3.155 to -3.161 |

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
