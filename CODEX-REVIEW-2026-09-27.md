**Cipher-lab: increasing the rate of credible, previously undocumented decipherments**

Prepared by ChatGPT/Codex · 27 September 2026

**My assessment:** the project has a credible foundation and promising early results. Its strongest opportunity is to make each successful key, transcription, and archival acquisition unlock a family of documents. The immediate constraints are unreliable scheduling data, uneven manuscript transcription, validation instruments that do not generalize reliably, and excessive coordination. Adding more concurrent work before addressing those constraints will probably multiply them.

This is a review of [NoAutopilot/cipher-lab at commit e909aa8](https://github.com/NoAutopilot/cipher-lab/tree/e909aa87559cbe9c1d6522f828e2bfb408534860), committed 27 September at 07:27 UTC. I inspected the workflow and role instructions, result board and rendering code, calibration records, recent retrospectives, next-step queue and its generator, solver infrastructure, and audit documents for the principal result families. I reproduced one committed decipherment locally. This is a sampled scientific and operational review, not independent certification of every manuscript reading or a new novelty audit of every result. Recommendations and proposed targets below are judgments, not measured forecasts. Repository references are pinned to that snapshot because other sessions are working concurrently.

**1. Keep the ambition; define the output precisely.**

The current [headline](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/status.json) says **20 letters, represented by 15 board entries, at N3 or better after two audits**. That is different from 20 complete N4 translations. N4, under your rules, means that no prior plaintext or decipherment was located after covering the principal editions, catalogues, and project pages. It explicitly leaves unpublished work open. This is a reasonable search standard; it is not a measure of completeness or correctness.

Your results encompass genuinely different outputs:

| Example | What the repository actually supports | Implication |
|---|---|---|
| Gramont f.30 | A substantial partial reading using a published key plus cryptanalytic extensions | Valuable recovery; completion remains a separate task |
| WVO 5797 | Two names/titles recovered in blanks within an otherwise printed letter; another proposed value withdrawn | Count the newly recovered passages, with their scope |
| Blathwayt BLA 184 | Three syllable groups read out of seven code groups; important names unresolved | A partial recovery, not a completed letter |
| Mercy, BnF Espagnol 144 f.22 | Reproducible cryptanalytic reading, N3, with uncertainty and an inconclusive language judge | A strong candidate for independent reading validation and targeted archival follow-up |
| Van Beuningen 1657 | Letter text N1; key/decipherment N3 | A cipher-mapping contribution, separate from newly recovered plaintext |
| WVO 53 and 126 | N4 with an explicitly named, unseen Japikse witness that may contain prior decipherment | The specific archival check now has much higher value than another broad web sweep |

Sources: [Gramont audit](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/ciphers/fr2980-gramont/AUDIT.md), [Nassau audit](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/ciphers/lodewijk-van-nassau-1573-74/AUDIT.md), [Blathwayt audit](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/ciphers/huntington-blathwayt-madrid-1728/AUDIT.md), [Mercy audit](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/ciphers/espagnol142-mercy-1648/AUDIT.md), [Van Beuningen audit](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/ciphers/vanbeuningen-dewitt-1657/AUDIT.md), [Saxony audit](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/ciphers/august-van-saksen-1561-64/AUDIT.md).

Keep separate counts for documents with newly recovered passages, completed readings, new keys/mappings to already known text, and catalogue contributions. For the first two, show novelty class, secure-token coverage, unresolved meaningful spans, and reviewer status. Count each physical document once; revisions increase its coverage. One document split across recto and verso is not two discoveries.

Do not make “changes our understanding of a famous historical event” an eligibility condition. A previously unavailable letter can be a useful historical source even when it confirms familiar events. Conversely, a fluent modern translation must not conceal gaps in the underlying decipherment. Preserve three layers: diplomatic transcription, keyed original-language reading, and modern translation with aligned uncertainties.

**2. Repair two concrete sources of misleading management information.**

I parsed [NEXT-STEPS.tsv](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/NEXT-STEPS.tsv), excluding its comment/footer. It contains 182 entries, 169 labelled runnable. **67 of those runnable entries have an empty next-step field**, and 65 have no last-touched date. These sets can overlap. In [next_steps.py](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/tools/next_steps.py), unmatched blocker text defaults to runnable and unmatched cost text defaults to the small band. An empty instruction therefore becomes apparently cheap, executable work. Rows are emitted in folder-name order, rather than estimated discovery yield.

Replace that fallback with “needs triage.” A runnable task needs a specific action, available inputs, expected output, acceptance criterion, owner, and stop condition. Keep the complete instruction; the generator currently truncates it before classifying the blocker. Rank executable tasks by expected marginal contribution, not alphabetically or simply by whether a past note contains “next step.”

I also reproduced the counting logic in [build_dashboard.py](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/tools/build_dashboard.py): 15 counted rows, comprising 11 parsed N4 rows and four parsed N3 rows. These are rows, not individual documents. The code extracts the first N-class mentioned in prose and treats N4 itself as sufficient evidence of two audits. It also admits the Van Beuningen key result although the letter text is already published. This does not prove audits are missing—the files contain substantial auditing—but the display cannot enforce the claim it makes.

Introduce explicit per-item fields: document ID, witness ID, claim scope, plaintext novelty, mapping novelty, completeness, input hashes, audit references, audit status, and superseded verdict. Generate the dashboard and counts from those fields. In particular, an audit should approve a particular reading version, not an indefinitely changing folder. Replace the dashboard's N4 shorthand “everywhere looked” with “principal sources searched,” which matches the actual standard.

**3. Turn the existing orchestration reforms into measured savings.**

Your [September 26 optimization review](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/OPTIMIZATION-2026-09-26.md) reports 241 ledger rows and about 1,457 units of dollar-equivalent usage at its measurement time, with no new letters added during the stated period. It allocates approximately 28% to meta/process work and 10% to lane orchestration. These are the repository's measurements, not my independent re-accounting. Under [BUDGETS.md](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/BUDGETS.md), the figures proxy rate-limit consumption rather than necessarily representing cash charges.

The proposed SUPPLY/SOLVE specialization, one daily retrospective, owner-desk limit, next-step queue, and key-matcher repair are sensible. Several are already implemented or underway. The remaining question is whether they reduce time per verified result. A system can faithfully document every failure while still spending too little effort on the highest-value next experiment.

For a two-week trial, budget approximately 50% of effort to focused recovery, transcription, and solving; 20% to acquiring specific high-value inputs; 20% to reading validation and novelty research; and 10% to coordination and maintenance. These are starting allocations, not scientifically established optima. Reserve roughly ten percentage points of total capacity within the solving allocation for one difficult research campaign. Reallocate weekly using actual gains.

Use one canonical task record and generate views. Preserve long research logs, but supply workers with a compact current-state packet: inputs, surviving hypotheses, failed tests with their power limitations, dependencies, and the exact experiment. A new process rule should replace or consolidate an existing rule where possible. The snapshot's CLAUDE.md alone is roughly 112 KB; adding another paragraph for every coordination mishap creates a reading tax on future work.

Report compute/rate-limit usage per validated recovered passage, per newly productive key family, and per completed document, alongside raw counts. Also report review backlog age, rework caused by bad transcriptions, and classification reversals. Do not reward job completion as if it were a decipherment.

**4. Make a cipher family the main unit of investment.**

The repository already says “pools first” and has key crossmatching, office metadata, and a leaf-pooling gate. The improvement is to make those facilities control the allocation of work. A small improvement to a shared key may recover text in several letters; opening another unrelated short puzzle usually cannot.

Select three active families with an explicit inventory of available ciphertext, sibling decipherments, period keys, and unresolved publication status. My provisional candidates from this review are:

| Family/campaign | Why it deserves attention | Next decisive work | Continue when |
|---|---|---|---|
| Nassau correspondence | Several recoveries already demonstrate shared-key value | Build an evidence-backed map of key versions and disputed codes; freeze a key and predict an unused sibling | New mappings predict further text without per-letter exceptions |
| Gramont / the applicable French diplomatic key | Published key already supports sizeable partial readings | Rank ambiguous repeated glyphs by total downstream effect; finish selected passages and test related documents | Image corrections or key extensions create independently readable new spans |
| One input-limited research family, with Salviati as a candidate | A substantial pool and explicit failed-control evidence already exist | Settle the plaintext/cipher boundary and glyph inventory before another solver campaign | Corrected transcription improves matched-control performance or unlocks predictive decoding |

These are provisional campaign choices, not a claim that they outrank every uninspected folder. A brief comparison against the top executable backlog tasks should confirm them. Keep archive follow-ups on Mercy, Linhares, and the Japikse witnesses moving in parallel through the acquisition capacity.

Same correspondent or similar symbol frequencies are useful clues, not proof of the same key. Nassau's contested code 172 is a concrete warning: the audits record conflicting period values and withdraw the proposed reading. Represent key version, date range, sender, recipient, language, and direct attestations. Compare common-key and separate-key hypotheses before pooling. A similarity score must not erase evidence for key changes.

Prioritize acquisition by its expected downstream benefit: the probability a page settles a key or transcription ambiguity, multiplied by the number and extent of documents it could unlock, relative to acquisition and processing cost. Bundle requests for complete key sheets, deciphered siblings, and adjacent leaves. A targeted paleographer or archivist intervention may outperform many repeated model passes; establish that on a small priced sample before expanding.

**5. Treat transcription uncertainty as part of the problem.**

The [latest Salviati notes](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/ciphers/fr2933-salviati-1525/NOTES.md) describe a particularly important failure: some boxes that earlier passes agreed were blank contained sign-like ink. Agreement between two readers was not sufficient. The corrected inventory reaches 2,932 tokens and 251 types; the [subsequent controls](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/ciphers/fr2933-salviati-1525/HYPOTHESES.md) fail the stated gate at both tested noise settings. This diagnoses an input/instrument problem. It does not refute the underlying cipher hypothesis.

Retain alternative glyph readings with image coordinates and visual confidence. Distinguish blank, illegible, plaintext, cipher sign, and mark; they are not interchangeable unknowns. Search over a small set of plausible transcription alternatives instead of permanently collapsing every disputed mark by majority vote. Keep visual evidence separate from language plausibility so a persuasive plaintext cannot silently rewrite the image.

Choose the next human or model inspection by influence: frequent uncertain glyphs affecting several documents first, rare marks with little effect later. Validate agreement against a small expert-labelled or otherwise securely known sample. Report error rates by hand and sign type, including omitted signs and incorrect segmentation. Maintain a gold image-to-token benchmark separate from the solver benchmark.

**6. Give the solver a stronger verifier, with the limits made explicit.**

I ran the committed decode pipeline for Mercy using its exact ciphertext, key, exceptions, configuration, and expected reading files. It reproduced the reading and token file, reporting **522 cipher tokens: S 496, M 26**. This is a real strength. It demonstrates deterministic regeneration; it does not independently establish the glyph readings, key, historical interpretation, or novelty.

The [plaintext judge](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/tools/judge_plaintext.py) explicitly calls itself a gate rather than a proof. Preserve that distinction. Re-encryption consistency also proves only consistency with a specified cipher model. It cannot alone establish that an underconstrained key or freely chosen exceptions are historically correct.

I recommend three validation layers:

1. **Mechanical consistency:** regenerate the exact reading from frozen inputs, test allowed encryption relations, account for every sign/null, and enumerate every position-specific exception. Test changed mappings against all previously validated sibling readings.
2. **Predictive evidence:** recover a key on one part of the family, freeze it, and decode held-out lines or a separate letter. Evaluate against withheld known plaintext where available; otherwise obtain an independent transcription/linguistic assessment and seek an external crib or witness. Repeated optimization on the held-out material turns it into training data.
3. **Independent historical assessment:** review the image, diplomatic reading, proposed word divisions, dates and entities, and the edition search. An external specialist's acknowledgement is not automatically endorsement of every token or universal novelty.

For very short fragments, reserve judgment when several keys or readings fit. Direct period-key evidence can justify a short recovery even when statistical language tests lack power. Record the remaining alternatives rather than forcing a single confident answer.

**7. Calibrate against new families and against the whole search procedure.**

The key-crossmatch repair is already present. [KEY-CROSSMATCH.md](https://github.com/NoAutopilot/cipher-lab/blob/e909aa87559cbe9c1d6522f828e2bfb408534860/KEY-CROSSMATCH.md) reports an operating threshold admitting 13/13 verified calibration pairs in its supported stratum, with 3/260 shuffled-value null draws passing. It also states that 50/65 token-order-shuffled decodes pass and that the rerun produced no new lead. The document correctly warns that its statistic tests key-frequency compatibility, not readable order.

Do not treat 13/13 as an out-of-sample success rate: the threshold was selected to admit those pairs, and multiple pairs share a family. Build a frozen benchmark split by correspondence/key family, keeping entire families out of calibration. Include actual wrong-period and wrong-key pairs as well as matched synthetic ciphers. Use length, symbol inventory, nulls, nomenclator share, transcription noise, and historical language/register as benchmark dimensions.

Run the entire candidate-selection pipeline on negatives—including retries, crib proposals, and picking the best score—when estimating false positives. A null scored once is not equivalent to a target optimized over many keys and variants. Twenty null draws per pair give limited tail resolution; pooled draws do not make every pair equally calibrated. Measure precision of adjudicated new leads and recovery on held-out known cases at the actual search budget.

Retain the existing “control failed means non-test” rule. Add a limited diagnostic allowance when the control fails, aimed at determining whether transcription, language model, segmentation, or cipher design is responsible. A weak instrument should not permanently veto a promising archive family. For unusually promising targets, a larger finite campaign can be justified by newly acquired information, measurable partial recovery, or an improving control curve; do not force every advance to fit a tiny per-job cap.

**8. Use stronger models for constrained cryptanalysis.**

The repository already implements model-assisted crib rounds. The next development experiment should compare concrete solver improvements on the frozen benchmark, with the same compute budget. Candidates include neural rescoring of a beam of mechanically valid decryptions, dictionary-code decoding lattices, and explicit joint search over glyph alternatives and keys.

There is relevant published evidence. [Kambhatla et al. (2018)](https://aclanthology.org/D18-1102/) use a neural language model to score complete candidate plaintext during beam search. [Chu, Valenti and Knight (2020)](https://aclanthology.org/2020.emnlp-main.471/) combine a decoding lattice with a neural language model for historical dictionary codes. [Megyesi et al. (2023)](https://www.ecp.ep.liu.se/index.php/histocrypt/article/view/701) find benefits from historical and century-specific language models in their English/German experiments. These results motivate tests; they do not establish that a particular model will solve Salviati or Armstrong.

The model's output should be a testable key constraint, segmentation hypothesis, candidate codebook, or reproducible search procedure. Fluent narrative reconstruction by itself earns no cryptanalytic credit. Measure verified token recovery and unseen-letter prediction, not how convincing a translation sounds.

**9. Apply the useful Navier–Stokes lessons.**

[OpenAI's September 8 account](https://openai.com/index/navier-stokes-solution/) describes parallel exploration of different formulations, an intermediate Euler result that caused resources to be concentrated on Navier–Stokes, exchange of useful intermediate results, and a separate Lean formalization/verification phase. [Clay's September 11 statement](https://www.claymath.org/news/navier-stokes-announcement/) acknowledges the apparent settlement while retaining its evaluation process.

For cipher-lab, the corresponding experiment is to give distinct groups genuinely different hypotheses on one promising family: period-key recovery; known-plaintext alignment; direct constrained search; and transcription/segmentation alternatives. Start them with the same frozen evidence packet. Exchange compact, reproducible findings at milestones. Move effort toward the branch that predicts new evidence. Keep one independently assessed outcome standard.

The analogy has a limit: an old manuscript usually has no complete formal specification, and a language score is not a proof checker. Your closest equivalent combines provenance, mechanical consistency, unseen-text prediction, and external historical evidence. A large agent count is not a substitute for those components, and the Navier–Stokes resource scale is not a demonstrated prescription for this repository.

**10. Make novelty research targeted and cumulative.**

Keep the strong practice of searching editions, translations, duplicates, and correspondence-specific sources. Preserve blocked/unread as distinct from a completed negative search. Reuse already verified family-level bibliographic work across siblings, while still checking each item's identity and distinctive decoded passages. Reopen a search when a reading, date, attribution, or source changes; do not repeat an unchanged full sweep simply because another worker has started.

The Saxony/Japikse example shows how valuable specialist feedback can be: it identifies a particular unpublished witness to inspect. That should trigger a concrete acquisition task with a receipt and result, rather than another broad search cycle. An N5 entry should record exactly what the archive or specialist confirmed and the limits of their knowledge; nobody can establish a universal absence of undocumented prior work.

One policy change worth considering is a small, explicitly provisional decoding allowance for promising items whose full edition check is blocked. A plaintext can make later novelty searches much more precise. Such work would remain outside any published novelty tally until the existing verification requirements are met. This is a proposed revision to the current intake policy, not an exception I exercised during this review.

**11. A concrete two-week trial.**

| Timing | Deliverable | Acceptance criterion |
|---|---|---|
| First 48 hours | Repair the runnable queue; add structured per-document claim and audit fields; establish baseline usage | No empty task labelled runnable; every counted claim has a scope, reading version, and audit references |
| Days 2–4 | Select three families; map key versions, siblings, available images, and unresolved source checks | Each has one executable experiment and a finite budget; acquire the few inputs with highest expected downstream effect |
| Days 3–7 | Freeze an initial benchmark of about 20 cases drawn from existing material, with family-separated development and evaluation sets | Test positives, realistic negatives, and noisy manuscripts; use confidence intervals and avoid overinterpreting a small pilot |
| Days 4–10 | Run focused production campaigns and one difficult research campaign | New key constraints or transcription corrections must improve recovery or predict withheld material; record uninformative failures honestly |
| Days 8–14 | Independently review the best candidate readings and issue complete evidence packets | Each packet links image, tokenized text, key, exceptions, original-language reading, translation, tests, and novelty evidence |
| Day 14 | Compare against baseline and reallocate | More validated text/documents per unit effort, bounded review delay, and no increase in unsupported claims |

Do not promise a fixed number of discoveries before measuring these conversion rates. The trial should establish which family, acquisition route, and solver improvement actually produce additional validated plaintext. A useful discovery target can then be forecast from observed yield.

**Recommended order:** first repair task and result records; then concentrate production on three families; then improve the transcription and predictive-validation bottlenecks those families expose. Preserve the existing adversarial novelty work, but make it operate on stable, clearly scoped results. This gives the project's ambition a measurable path from promising fragments to a growing body of defensible historical text.
