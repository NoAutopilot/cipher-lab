# Köhler cryptograms -- hypotheses and prior attempts

Working file for constraints on the system behind the five February 1944 Köhler cryptograms (see NOTES.md for
the target, sources and check-solved verdict). Everything below the first `##` is append-only, dated and signed by
the job that wrote it. This top block is rewritten once per cycle by the lane's consolidator and by nobody else.

**Summary, cycle 2** (GOLD-CONS2, Fable, session_01SPixjGTp23T4YyxPvHwkWs, 25 Sept 2026 21:12 UTC; replaces the
cycle-1 block of 19:30 UTC, whose target facts and structural argument are unchanged and restated here)

**Target facts every family must respect.** 924 letters in five messages of 237 / 178 / 140 / 140 / 229 (Kahn heads
the third "137"; it prints 140). All 26 letters present; counts run z 55 down to c 14, sorted profile 55 47 47 47 46
46 44 40 39 37 36 36 35 33 33 32 31 31 31 30 29 28 28 26 23 14. Two message lengths are odd. Transcription: Schmeh
2021 reproducing Kahn 1981 pp.65-66 (no image); six single-letter differences from Bourdeau's (`ciphertext-variants.tsv`,
ASKS 53), immaterial to every statistic below, material to any decode. No depth between messages (Bourdeau). IC 0.0399.

**The structural fact (GOLD-2C step 1, unchanged).** The letter statistics sit inside the keyed-tableau running-key
band on 6/6 statistics (percentile 0.41-0.52) and outside the uniform one-time-key 99 pct band on 5/6. The key stream
is not uniform; transposition is excluded by the flat IC; a 25-letter digraphic square by j and the odd lengths. What is
left is "non-uniform key + letter arithmetic + at least one unknown alphabet permutation". Cycle 2 closed four more
corners of that family; none moved.

**What cycle 2 added.** Every family B and B' negative was, at cycle 1, conditional on 1880-1920 novel-prose key models
(nl20). K1 built `tools/data/nl_dev` (Statenvertaling, 67 files, 3.4M letters; dbnl and gutendex unreachable, no Catholic
prayer book found) and reran both tableaux under it; K2 ran the beau and German-key corners of B' under nl20 and built
the English-keyword option without running it. Controls and targets side by side, same decoder settings per row:

| family, corner | key model | CONTROL (pct plaintext letters, seeds 1-3; gate) | TARGET pooled joint ll/letter | noise band (same pipeline) | read |
|---|---|---|---|---|---|
| B standard tableau, vig (GOLD-2A) | nl20 novels | 72.7 / 60.4 / 68.3, mean 67.1 (gate 60 met) | -3.589 (de/nl vig); -3.57 to -3.62 over 7 configs | -3.57 to -3.64 (3 uniform texts, order 8 beam 1000) | inside |
| B standard tableau, vig and beau (GOLD-K1) | nl_dev Bible | 83.0 / 89.5 / 80.3, mean 84.3 (gate 60 met) | vig -3.588; beau -3.640 | GOLD-2A's band reused (limit, see below) | inside; beau at the band's floor |
| B' keyword-mixed, vig, 4 placements (GOLD-2C) | nl20 | 79.1 / 74.0 / 64.7, mean 72.6 (gate 50 met) | -3.534 (`waarvan:plain`) | -3.507 / -3.544 (2 uniform texts, order 6 beam 300) | inside |
| B' keyword-mixed, **beau** (GOLD-K2 v1) | nl20 | 85.5 / 82.5 / 66.2, mean 78.1 (gate 50 met) | **-3.478** (`aufgabe:plain:beau`); msg-1 best-of-30 -3.443 vs noise -3.477 / -3.492 | the vig band above, reused | 0.029 above the higher of two draws; judge FAIL |
| B' keyword-mixed, vig, **German key** (GOLD-K2 v2) | de20 | strict 7.7 (label ambiguity: streams exchangeable); either-stream 89.6 / 90.7 / 88.6, mean 89.6 (gate met) | -3.573 | same | below the band's floor |
| B' keyword-mixed, vig (GOLD-K1) | nl_dev Bible | 87.8 / 81.0 / 85.6, mean 84.8 (gate 50 met) | -3.583 (`evelyn:plain`) | same, reused | 0.04-0.08 below the band's floor |
| B' English keyword list (GOLD-K2 v3) | -- | not run; `wordcorpus=` option built and tested | -- | -- | owed |

Every control cleared its gate, every target sits at noise, every judge line reads FAIL. Yes: every B and B' negative
is now also conditional on a devotional key model, and the devotional model made the *controls* easier (84 vs 67-73
pct) without moving the target at all. The register lever is spent for the standard and keyword-mixed tableaux.

**(i) The beau corner, weighed.** K2's -3.478 sits 0.029 nats above the higher of the two noise draws (-3.507) and 0.066
above the lower. Two draws 0.037 apart have no tail: the expected maximum of ten such draws lies a few hundredths above
the maximum of two, which is exactly where -3.478 is. Against that, the scale of a real signal in this pipeline is 0.35-0.5
nats (the controls' true tableau over its near-misses, and the controls' pooled -3.01 to -3.18 over noise -3.51 to -3.54);
the beau excess is under a tenth of it, the msg-1 best-of-30 gap is 0.03, and the judge failed. Not a flag by the 0.1-nat
rule and not a signal at the control's scale. A 10-text band for the beau pipeline (the vig band was reused; beau changes
the candidate tableaux, so it is not strictly the same pipeline) should run **beside** B'', not before it: it cannot change
the B'' design, only the sentence the record carries. It is folded into K3 below (Sonnet, about $3 of a $6 box) rather
than given its own box. NEAR.md should carry: beau/Dutch-key target -3.478 vs a two-text band top of -3.507 (excess
0.029 against a control signal of 0.35-0.5 nats), 10-text beau band owed to K3.

**(ii) The nl_dev bands, weighed.** K1 scored its nl_dev targets against bands whose LM_k was trained on nl20/de20. The
band is the decoder's pooled score on uniform text, and a lower-entropy key model (the Bible: controls 84 vs 67 pct) lets
the decoder find higher-scoring key strings on any input, so an nl_dev-trained band would sit *higher* (less negative)
than the reused one, not lower. That makes K1's "inside" reads conservative in the safe direction: the targets (-3.588,
-3.583, -3.640) would be deeper inside a band that had moved up. At the 0.05-nat scale it does not matter for these
verdicts; it would matter only for a target within 0.05 of a band top, and none is. Recorded as a limit; no re-run.

**Family E (digit system re-lettered), weighed once more.** K1 and K2 test letter arithmetic and say nothing about E.
E's own prediction (count tiers from a 100-cell table onto 26 letters) is testable by the GOLD-2C step-1 simulation, but
the band depends on the unknown table and additive, so it would be wide and would sit where the keyed band sits: low
information per dollar. Kept recorded, not briefed. B''-c below covers E's re-lettering step (a permutation on the cipher
side) for the letter-arithmetic case; digit arithmetic mod 10 is a different group and stays open.

**The corner nobody has run.** `running_key.mixed_tabula` mixes the plaintext side (plain), the key side (key), both
(both) or all three consistently (full). A mixed alphabet on the **cipher side alone**, c = M[(p + k) mod 26] with
standard plain and key letters (the rows of the square filled with a shifted mixed sequence, the commonest practical
way a Vigenere square was mixed), and the two mixed pairs {plain, cipher} and {key, cipher}, are not among the four
modes and were not among Bourdeau's six (his test 4 assumes the identity on the cipher side). Its statistics match the
target: the sorted profile under cipher-side mixing is the STANDARD band's, where the target sits at percentile 0.16
(GOLD-2C step 1). It is the keyword-restricted instance of B'' with S1 = S2 = id, and it costs one Sonnet box.

| family | status after cycle 2 | CONTROL | TARGET | what is left |
|---|---|---|---|---|
| A recovery | **blocked on the owner** (ASKS 55, 53) | n/a | no decrypt, key or system located (GOLD-1A) | nothing a cloud worker can add |
| Bourdeau's six | **excluded**, cited | his controls | see cycle 1 | nothing |
| B standard tableau | **parked** at two key registers | 67.1 (nl20) / 84.3 (nl_dev) mean | -3.57 to -3.64, all inside | nothing cheap; a reading needs a key text, not a model |
| B' keyword-mixed, modes plain/key/both/full, vig/beau, nl/de/dev keys | **parked** on five corners with both numbers | 72.6 / 78.1 / 89.6 / 84.8 | -3.534 / -3.478 / -3.573 / -3.583 | English keyword list (owed, $4); 10-text beau band (K3) |
| B'-c keyword-mixed, cipher-side placements (cipher; plain+cipher; key+cipher) | **open, not run**; cycle-3 job K3 | owed: same construction as GOLD-2C, gate 0.5 | -- | the highest-EV corner left in B' |
| B'' general permuted tableau, first B''-c (S3 free, S1 = S2 = id) | **open, design owed**; cycle-3 job (Fable) | owed: German plaintext at the five lengths under a Dutch key through a random permutation, gate 0.5 | -- | the general S1, S2, S3 case after B''-c's control reads |
| C book / word-sum code | **parked**, merged into B'' | -- | -- | -- |
| D uniform one-time key | **excluded** at 99 pct on 5/6 | 1000 OTPs | -- | -- |
| D' hand-made non-uniform key | **open, unfalsifiable from the ciphertext**; park | -- | inside the keyed band | only family A |
| E digit system re-lettered | **recorded, not briefed** (above) | -- | -- | -- |
| F Abwehr hand systems in print | **mostly excluded** by the two structural facts | -- | -- | what survives is B'/B''/E |

**Decisions, cycle 2.** A: park (owner). B: park at both registers. B': park the five run corners; continue only on the
cipher-side placements (K3) and carry the English list as owed. B'': design now (K1 and K2 came back flat, the cycle-1
condition), as B''-c first. C, D, D', E, F: as before. No LOCAL-QUEUE row for a Catholic Dutch prayer book: the
register lever moved the controls and not the target across two registers, the documented prayer-book key belongs to
the FBI-run Hamburg channel and not to these Paris messages, and the owner's time is better spent on ASKS 55 and 53.

**Cycle-3 Köhler jobs by expected value** (P(the first result moves the target) x value / cost; P is a judgement):

| rank | job | P(moves) | cost | EV per dollar | brief |
|---|---|---|---|---|---|
| 1 | K3: B' cipher-side placements (three new modes in `mixed_tabula`, control first per mode, vig then beau for the cipher-only mode), plus the 10-text beau noise band in the background | 0.10 for the three | $6 Sonnet, 75 min | 0.017 V | `2026-09-25-lane-gold-c3-koehler-bprime-cipher-side.md` |
| 2 | B''-c design: `tools/families/permuted_tableau.py`, anneal over S3 with the two-stream decoder as objective, matched control through a random permutation, uniform-text and shuffle-target bands | 0.10 | $12 Fable, 90 min (+ about $8 Sonnet runs later) | 0.005 V | `2026-09-25-lane-gold-c3-koehler-bprime2-design.md` |
| 3 (owed) | B' English keyword list, `wordcorpus=tools/data/en16_repo,...`, control first | 0.04 | $4 Sonnet | 0.01 V | not briefed this cycle (box limit); the K2 brief's step 3 is the brief |

K3 and the B''-c design are independent and may run at once (K3 is CPU-bound, three decoder processes at most at order
6). Rule 10: nothing in this file is a reading; status stays `open`; the lane never writes solved, new, first or
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

<!-- family_run.py table: one row per run, appended by the tool, never edited by hand -->

| date (UTC) | family | parameters | seeds | CONTROL mean (range) | TARGET best score | judge | gate met | label |
|---|---|---|---|---|---|---|---|---|
| 25 Sept 2026 20:47 | keyed_running_key | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/de20,arith=vig,top=30,beam=300,order=6,spaces=1 | 1-3 | 0.078 (0.064-0.085) | not run (CONTROL BELOW GATE) | - | no (gate 0.5) | GOLD-K2 B' vig, German key |
| 25 Sept 2026 20:54 | keyed_running_key | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/de20,arith=vig,top=30,beam=300,order=6,spaces=1 | 1 | strict 0.077 (0.064-0.085); either-stream 0.896 (0.886-0.907) | -3.573 | FAIL language: score=-0.975, null_p99=-2.071, real_p05=-0.823, real_median=-0.78, mode=both, N=924 | yes (gate 0.5 on either-stream) | GOLD-K2 B' vig, German key, gated on either-stream recovery (streams exchangeable) |
| 25 Sept 2026 21:56 | permuted_tableau | N=924 K=26 restarts=8 corpus=pg15736_Der_Mann_von_vierzig_Jahren.txt.gz+pg36905_Schach_von_Wuthenow.txt.gz+pg41051_Peter_Camenzind.txt.gz+pg41907_Demian.txt.gz+pg43987_Die_drei_Spruenge_des_Wang_lun.txt.gz+pg46184_Frau_Jenny_Treibel.txt.gz+pg5323_Effi_Briest.txt.gz kcorpus=tools/data/nl20,arith=vig | 1-3 | 0.095 (0.074-0.129) | not run (CONTROL BELOW GATE) | - | no (gate 0.5) | GOLD-B2D B''-c cipher-side permutation anneal (sum-stream proxy), control before target |
