# Transcription standard (owner's ask, 3 Oct 2026: "a 10x effort on the tool we use for every cipher")

Every account, lane and worker that turns a page image into signs follows this file. It sets the target, the
measurement and the pipeline. `.claude/briefs/transcription.md` is the job template that applies it; CLAUDE.md Usage 6
points here. Changes go through a parent (SYSTEM.md row, UPDATES.md line), like any shared rule.

## Why

Transcription, not keys, is now the bottleneck. On 3 Oct 2026 every unread Birago 1572 letter (f.117, f.144, f.168)
already has its key; each stalls because two readers split 15-33% of signs, and at that error a power control
cannot license a key on a short letter. Same for Birago 1571 f.36/f.47 (0.33), Florence c.127 (0.17), Debosnys (0.28).
The look-alike pass showed that agreement can rise while accuracy does not (LESSONS.md "Look-alike pass").

## What excellent means (targets)

| # | Property | Target | Today (3 Oct 2026) |
|---|---|---|---|
| 1 | True per-sign error, measured against a known answer | <= 5% on symbol ciphers, <= 1% on digits | measured once or twice (no.87: 0.178 / 0.071); usually only two-reader agreement |
| 2 | Every transcription reports its error with the method named | always: `err_true` (benchmark-calibrated) or `err_2reader`, never "agreement" alone | mixed |
| 3 | Signs are image tiles in one atlas per key family, not strings typed per letter | every symbol cipher | tools/glyph_atlas.py exists (Carpi, Salviati) but Birago/Ceppo/Florence used line reads |
| 4 | Each sign carries top-k candidates with confidences | k=3 | one forced label |
| 5 | Ambiguity is settled with the key and the language in the loop, and reported as such (grade S, never H) | key-constrained decode over the candidate lattice | transcription fixed first, decoded second |
| 6 | A person's decision on one tile propagates to every tile of that cluster in every letter of the key family | always | sorter labels apply to one letter |
| 7 | The sorter asks the person only the tiles whose answer moves the reading most, about 10-20 per session | ranked by expected change in key rank / judge score | all tiles shown in piles |
| 8 | Cost per 100 signs known and falling | reported per job | not tracked |

## The pipeline (target state; each step names its tool)

1. **Images once** (CLAUDE.md Usage 4): `tools/gallica_folio.py`, `tools/iiif_lines.py --debug` (check the overlay).
2. **Segment every sign into a tile** across ALL letters of the key family at once: `tools/glyph_atlas.py segment`.
3. **Cluster** tiles by shape, deliberately over-split: `glyph_atlas.py cluster`. One atlas per key family, kept in
   the family's lead folder and reused by every sibling letter (Birago 1572: ciphers/nevers-birago-fr3251-1572).
4. **Name clusters, not tiles**: known answers first (clerk sheets, glossed lines, printed key shapes), then a model
   reader on cluster exemplar sheets (one call per sheet, not per line), then the person in the sorter.
5. **Classify** every tile to top-k clusters with distances: `glyph_atlas.py classify` (extended to emit top-k).
6. **Key-constrained decode** (to build, TX-DECODE): given top-k per sign, the key and a language model, choose the
   most probable reading; every changed sign is graded S and listed; controls as rule 3 (shuffled key, power at
   err_true).
7. **Active sorter** (to build, TX-SORTER): `tools/sign_sorter.py` gains a ranking of tiles by expected change in the
   decode, and `sign_sorter_apply.py` writes cluster-level decisions that every letter of the family picks up.
8. **Measure**: `tools/tx_bench.py` (to build, TX-BENCH) scores any pipeline output against BENCHMARK-TX.tsv and
   prints err_true per sign class; a job's NOTES.md pastes that line.

LLM line reading (two blind passes + `tools/reconcile_passes.py` + `tools/lookalike_pass.py`) stays the fallback for
pages the segmenter cannot cut (joined hands, digits run together) and for numeral ciphers, and it must still report
err_true where a benchmark item of the same hand exists.

## Benchmark (BENCHMARK-TX.tsv, built by TX-BENCH)

Known-answer items, each with image, the sign sequence a person or period source fixes, and the source of truth:
Birago no.87 (clerk sheet, canvas 182); Birago 1571 f.36v L1 (period gloss); Ceppo f.21v and f.87 (published key
decode, the S-graded spans); colbert26 f.23/f.24 (interlinear keys); Mercy (H-graded spans); later Florence c.111/c.127.
Splits: tune on some, report on held-out ones (BENCHMARK.tsv's own rule). A pipeline change is adopted only when it
lowers held-out err_true.

## Rules for every account (effective 3 Oct 2026)

- A transcription job reports `err_true` (with the benchmark item used) or says "err_true not measurable: no benchmark
  item of this hand/key", plus `err_2reader`. Power controls use err_true when it exists, else err_2reader -- never a
  look-alike residual.
- A symbol cipher with siblings in the same key family is segmented into the family atlas before any line read; a
  brief that skips it says why.
- Person time goes through the sorter only, never blocking (CLAUDE.md Usage 6).
- New capability goes into the shared tools above (Usage 8), never a private script in a target folder.

## Build plan (3 Oct 2026, account-3 orchestrator; jobs in WORK-QUEUE.tsv)

| Job | What | Done when |
|---|---|---|
| TX-BENCH | BENCHMARK-TX.tsv + tools/tx_bench.py + test; score the current line-read pipeline | err_true per item, held-out, in this file |
| TX-ATLAS-B72 | One atlas for every Birago 1572 letter (nos.71-90, f.117) with glyph_atlas; clusters named from the no.87 clerk sheet; top-k classify | err_true on no.87 held-out vs line reads |
| TX-DECODE | tools/key_decode_lattice.py: key-constrained decode over top-k, controls built in | f.117/f.144/f.168 re-tested; known-answer check on no.87 |
| TX-SORTER | sorter ranks tiles by value, decisions propagate per cluster across the family | one Birago session of <=20 tiles moves a letter's test |

Results land here (the "Today" column) as they come.
