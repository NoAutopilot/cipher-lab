# Prompt for an external opinion on the transcription tests (written 10 Oct 2026 00:0x UTC by the orchestrator (account-4), for the owner to paste into ChatGPT)

Paste everything below the line.

---

I run a small open project (one person plus AI agents) that reads unsolved historical ciphers from archive images. The public repository is https://github.com/NoAutopilot/cipher-lab. I want a critical outside opinion on how we are testing our **transcription** step (turning a page image of cipher signs into a per-sign text file), not on any cipher solution. Please read the files linked below if you can browse; the key numbers are also given here so you can answer without browsing.

**What we are trying to do.** Transcribe 16th-century cipher pages (hand-drawn signs, no standard alphabet) at <= 5% per-sign error on a hand the system has not seen before. Today's product reads an unseen hand at roughly 15-30% error depending on how it is counted (see below).

**How the pipeline works.** Each page is cut into line crops. Two independent model passes (an "atlas" sheet of exemplar signs is given to the reader) each transcribe the crops; disagreements go to a third adjudication pass; the reconciled file is scored against a truth file. Truth files come from pages where a contemporary decipherment or a published key lets us fix every sign's value independently of our own reading.

**How we measure.** A benchmark of truth-labelled pages (BENCHMARK-TX.tsv) split into dev and held-out eval pools. The scorer (tools/tx_bench.py) aligns the read to the truth and reports per-sign error. Two figures per run: "flagged-excluded" (positions the reader marked uncertain are dropped from the denominator) and "as measured" (everything counted). Every experiment is pre-registered before any read (benchmark-tx/PREREG-txeng2-*.md), with success criteria S1-S5: S1 held-out per-sign error lower under the new pipeline, paired fixed > broken at p < 0.01, one eval look per experiment; S2 a single look at a sealed confirm item never opened before the final score; S3 a live letter; S4 a doubt feed for a human sign-sorter; S5 cost per 100 signs. An adversarial reviewer session ("TX-RED") outside the engineering lane logs findings (research/TX-RED-2026-10-09.md).

**Results so far (9 Oct 2026).**
- Sealed confirm item (an unseen hand, vivonne1573-f103r): 0.150 flagged-excluded (75 of 500 positions) and 0.296 as measured (316 of 1068). Error classes: notation 0, segmentation 42, read 33 of the flagged-excluded errors.
- Second leaf of the same hand (f.102r, a dev item): 0.199 flagged-excluded (80 of 403), 0.431 as measured; of the 80 errors, 48 segmentation (42 inserted signs, 6 deleted), 26 read, 6 notation. An anchor check then found this leaf's truth file beats a shuffled key by only 0.003, so that number is provisional until the truth is re-anchored.
- A model swap alone did not help (a stronger reader model read worse on the same crops). Pair classifiers, count-then-read, same-sign retrieval strips and lattice-proposed cells each failed their own pre-registered gate or gave no measurable gain.
- The reviewer's open points: the dev pool would be dominated by one leaf whose errors are mostly insertions; the scorer folds line insertions into one rate; the "flagged-excluded" figure can hide error by flagging.

**What I want from you** (be blunt; I would rather hear the method is wrong than be reassured):
1. Is the measurement sound? In particular: the two-figure reporting (flagged-excluded vs as measured), the alignment-based scorer with insertions and deletions, the single sealed look, and the "paired fixed > broken" gate. What would a reviewer in document image analysis or historical handwriting recognition object to?
2. Is 5% per-sign error on an unseen hand a realistic target for this kind of material with any method, and what does the published literature on handwritten text recognition of unusual alphabets suggest is achievable with a few hundred truth-labelled signs per hand?
3. Segmentation (where one sign ends and the next begins) dominates our errors. What approaches have worked elsewhere for segmentation of invented-sign scripts, and which of them can be tested cheaply against a benchmark like ours?
4. What experiment would you pre-register next, with the exact pass condition, if you had one week and the benchmark above?
5. Name anything in the setup that looks like it could produce a false improvement (leakage from truth files, a reader seeing the key, test-set reuse, selection of items) and how you would check for it.

Please cite sources you rely on. If you cannot open the repository, say so and answer from the numbers above. Do not try to solve any cipher.

Files to read, in order:
- https://github.com/NoAutopilot/cipher-lab/blob/main/research/TX-PROGRAM.md (the charter)
- https://github.com/NoAutopilot/cipher-lab/blob/main/TRANSCRIPTION.md (the standard)
- https://github.com/NoAutopilot/cipher-lab/blob/main/benchmark-tx/PREREG-txeng2-S2.md (the sealed-look pre-registration)
- https://github.com/NoAutopilot/cipher-lab/blob/main/benchmark-tx/txeng2/s2score/tx_bench_S2.txt (the sealed-look score)
- https://github.com/NoAutopilot/cipher-lab/blob/main/benchmark-tx/txeng2/viv102base/RESULTS.md and .../viv102anchor/RESULTS.md (the second leaf and its anchor check)
- https://github.com/NoAutopilot/cipher-lab/blob/main/research/TX-RED-2026-10-09.md (the adversarial reviewer's findings)
- https://github.com/NoAutopilot/cipher-lab/blob/main/research/TX-REGISTER.tsv (every experiment tried and its outcome)
- https://github.com/NoAutopilot/cipher-lab/blob/main/tools/tx_bench.py (the scorer)

## Corrections (10 Oct 2026 00:3x UTC by date -u, orchestrator (account-4), from TX-RED pass 11 F51)

The prompt above was pasted by the owner before this check and answered as PR 71 (research/SO-TX-TRANSCRIPTION-2026-10-10.md). Five
of its sentences were wrong or loose, by TX-RED's reading against the register; the reviewer caught the first and fourth itself from
the repository, which is why its answer is unaffected on those points:
1. "positions the reader marked uncertain are dropped" -- wrong. The flags are truth-side (the build's align-conflict and clerk-split
   classes, then TXV-VIV's), never the reader's marks. The real caveat is F39: the flags are the folder's earlier reading's disagreements
   with the witness, so the 500 binding positions are selected on a correlated reader.
2. "a stronger reader model read worse on the same crops" -- X21b is a null at this N (Opus 17 / Sonnet 11 errors, p 0.345), not a
   worse read.
3. "Pair classifiers, count-then-read, same-sign retrieval strips ... each failed their own pre-registered gate" -- X3/X5/X7 were
   non-tests at E 12 (too few baseline errors to test), not failed gates.
4. "an 'atlas' sheet of exemplar signs is given to the reader" -- the S2 readers had a value-blind text-list sheet, not exemplar images.
5. "roughly 15-30% error depending on how it is counted" -- two operational scores with different masks (0.150 flagged-excluded,
   0.296 as measured), not a bracket on the true page error (PR 71 section 1 says the same).
A future paste of this prompt uses the corrected wording; a draft sent outside by the owner gets a `checked:` line from a session other
than its drafter first (outreach gate 7), which this one did not.
