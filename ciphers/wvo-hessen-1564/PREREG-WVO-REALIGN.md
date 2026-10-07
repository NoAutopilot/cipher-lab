# PREREG WVO-REALIGN -- f.23 gloss re-aligned on the owner's settled signs (written and pushed before any scored run)

Worker WVO-REALIGN, account 1 for account 3, 7 Oct 2026 (01:4x UTC by date -u). Brief:
.claude/briefs/runs/2026-10-07-acct3-wvo-realign.md. Files in `realign/`.

Input: `sorter/settled_labels.tsv` (owner's settled signs), `r9align/tile_order.tsv` (tiles in x order),
`r9align/gloss_reconciled.tsv` (R10-WVOTX gloss, unchanged). Pairs: each cipher row is its tiles in x order labelled
'@'+settled sign; the clear E.L. tile stays clear; each aside/bad-cut tile (10) gets its own unique label so it carries
no shared evidence (kept in the stream, as PREREG-R9 kept every tile).

Alignment: `tools/interlinear_align.py align` with the PREREG-R9-WVOALIGN parameters unchanged
(`--code-prefix @ --seg-bonus 0 --keep-fs --null-cost -1.0`, 6 iterations). Key: settled/make_key.py's rule unchanged
(C: top letter >= 2 times on >= 2 rows and >= 0.6 of aligned occurrences; else M; aside/bad-cut no key row).

Primary statistic (the verifier's measure, AUDIT 2): AGREE = tiles at grade C whose key value equals the gloss letter the
alignment puts over that tile. Before (WVO-APPLY, R10 alignment on k-piles): 159/257. Also reported: CONSISTENT (PREREG-R9
statistic), C/M counts, C-conflict and C-unaligned tiles.

Control (the brief's): settled labels permuted within each row (same row multiset, order destroyed), 300 draws, seed 1564,
full pipeline (align, key, AGREE) per draw. It can vary on AGREE: permuting labels within a row breaks the letter-over-sign
correspondence, so a sign's aligned letters scatter and fewer signs reach C. Gate: real AGREE > control p95 -> gain shown
against chance; real <= p95 -> "gain not shown". Secondary: the PREREG-R9 derangement control (`--shuffle 1000 --seed 1564`)
on CONSISTENT, reported. The before/after change (159 -> real) is reported as a difference, not gated (no control varies the
before figure). Settled key is rebuilt in `realign/`, `settled/` left as WVO-APPLY wrote it.

C09 l-vs-f: one look at the gloss crop over C09's end (r10tx/crops) for the letter the key predicts as l where the gloss
reads f; report the letter shape seen, no German reading beyond the gloss letters.
