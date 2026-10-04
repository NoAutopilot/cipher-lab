# TX-FABLE result (4 Oct 2026, 16:0x UTC, account-3 worker) -- FAIL: Fable is not better; on these items it is worse

Pre-registered in `benchmark-tx/PREREG-txfable.md` (commit 351c12c0, pushed before any Fable call). One blind Fable pass
(`claude-fable-5-1`) per BENCHMARK-TX item. Same crops, same sheet and the pass-A brief text pasted unchanged, in the same
call groups as pass A: 8 calls, 1,535 signs read. Raw output is in `raw/` and normalised to
`benchmark-tx/outputs/<item>/passF_fable.tsv` by `norm.py`. Each item's raw files were committed before that item was
scored. The worker opened no truth file.

## Per item (err_true, `tools/tx_bench.py --bench BENCHMARK-TX.tsv --item <item>`)

| item | split | Sonnet A | Sonnet B | reconciled / committed | **Fable** | Fable vs better single (paired fixed/broken, p) |
|---|---|---|---|---|---|---|
| birago1572-no87 | eval | **0.069** (55/803) | 0.100 (80) | passC 0.053 (43) | 0.093 (75) | vs A: 23 / 42, p 0.025 |
| dint-f128-print (label map) | dev | 0.247 (21/85) | **0.188** (16) | -- (truth built from it) | 0.271 (23) | vs B: 2 / 5, p 0.45 |
| dint-f128-print (no map) | dev | 0.353 | 0.306 | -- | 0.377 | (informative) |
| ceppo-f21v-S | dev | **0.048** (9/189) | 0.053 (10) | passC 0.005 (by construction ~0) | 0.058 (11) | vs A: 9 / 10, p 1.0 |
| ceppo-f87-S | dev | **0.043** (6/139) | 0.130 (18) | passC 0.050 | 0.295 (41) | vs A: 4 / 36, p < 1e-6 |
| ceppo-f36v-gloss | dev | **0.312** (5/16) | 0.375 (6) | recon 0.438 (7) | 0.500 (8) | vs A: 2 / 2, p 1.0 |

## Gate
- (a) Pooled paired test against the better Sonnet single pass of each item: fixed **40**, broken **95**. The two-sided
  sign test gives p = 2.5e-6, in the *wrong* direction. Not met.
- (b) Fable lower than the better single pass: no.87 no; dev 0 of 4. Not met.
- Against the reconciled two-pass read (informative): no.87 fixed 21 / broken 51 (p 0.0005); f21v 1 / 10; f87 3 / 32; f36v recon
  4 / 2 (p 0.69, 16 signs).
**Verdict: not meaningfully better. The gate fails on both arms. No model-rule change is proposed.**

## Where Fable lost (top confusions, truth value <- read)
- no.87: `m<-X_NEW x8`. Fable filed a recurring "t with curved foot" as off-sheet nine times in L11-23 instead of
  matching it to the m-cell. It also deleted 19 signs (pass A deleted 9). Calls 2 and 3 both reported that the s1/s2/s3 overlap
  "was 5-6 signs, more than the stated 100 px" and collapsed runs by sequence matching, which is the likely source of the
  extra deletions. On the f178r lines, call 1 also flagged that the run falls out of the crop bottom in s3. That is the same
  crop for every reader, but Fable gave up to ? / L on those tails.
  What it fixed: pass A's `s<-T50 x7` and `d<-T98 x7` are absent from Fable's top list.
- f87: `e<-S56 x4, o<-S88 x4, r/g<-S69` and others, 33 substitutions spread over the look-alike families that NOTES already
  calls the hardest hand.
  **Caveat:** the f21v/f87 truth is the committed decode's S tokens, and that sequence was adjudicated from passes A and B
  (f87: 29 splits sided with A). So these two items lean toward the Sonnet passes by construction, and a third reader is
  penalised wherever it disagrees with that adjudication. no.87 (clerk clear sheet) and dint (1882 print) are independent
  truths, and Fable loses or ties on both.
- dint: `n<-4 x4, i<-x x3`, plus 9 insertions (more signs per line than B).

## What this does and does not say
One pass and one seed per item, prompts written for Sonnet and pasted unchanged. Fable used tools on its own (79-95 calls
on the larger calls, making zoomed sub-crops of the given crops). It was neither told to do that nor stopped from it. The
test asked "same prompt, swap the model", and on that question the answer is no. It does not test a Fable-specific
prompt, or Fable as the reconciler or adjudicator (TRANSCRIPTION.md's split-settling role). Those are different
instruments, and a separate brief would have to name them.

## Cost
Fable token use over the 8 calls, from the subagent transcripts (approximate; streamed usage under-counts output):
cache-write about 1.15 M, cache-read about 12.2 M, output about 0.1 M. The dollar figure is the orchestrator's to read
(`get_session`; COMMON item 1). At Opus-class list rates that would be roughly USD 15, or **about USD 1.0 per 100 signs**
(1,535 signs), against **about USD 0.74 per 100 signs** for the Sonnet job-level rate (TX-SHEET, an upper bound). At Fable's
real rate the gap is likely wider. Wall time per call was 2.5-15 min (the dint call was 15 min for 8 crops).
