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
