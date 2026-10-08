# PREREG-D1A-PIS -- key86 T40 witness from the aligned letters (8 Oct 2026, LANE DEFAULT-account-1-20261008-0540)

Written and pushed before any T40 score is computed. Instrument: the alignment on disk (tools/stream_align.band_dp, the
kp87a/kp87b cgrades settings: identical letter +2, any other pair -1, gap 1.0/1.0, free start, band max(200,|M-N|+200)),
not a crop compare (the blind crop compares are retired for T40, D07-PIST40/D07-PISSD).

Material (the committed readings' own transcriptions and the paired Colbert 16 pt II copies, norm() of kp86/kp86.py):
f.244r tx86/ciphertext_f244r.tsv vs kp86/colbert_p49_50.txt; f.244v+f.245r tx86c vs kp86b/colbert_p51_52.txt; f.247r tx86g vs
kp86g/colbert_f247r.txt; f.275r tx86e vs kp86d/colbert_p121_123.txt; f.275v tx86f (L01-L16, the PASSed block; L17-L20 excluded,
kp86d test retired there) vs kp86f/colbert_f275v.txt; f.301v tx87 vs kp87a/colbert_p338_339.txt; f.302v tx87b vs
kp87b/colbert_p341_342.txt. Tokens as the cgrades scripts read them (trailing '?' stripped, '/' dropped). 68 T40 tokens.

Masking: every token of the tested set is decoded as ONE neutral slot (symbol 26, scores -1 against every letter), so the
alignment cannot favour the key's 'a' or any other value at those slots. All other tokens decode with key86.tsv as committed.
Witness per masked token = the clear letter aligned to its slot, or GAP if the slot is not on a diagonal step.

Statistic: top-value share = (count of the most frequent aligned letter) / (number of masked tokens, GAP included).

Gate G (T40 gets a value): top-value share >= 0.70 AND that letter's count >= 5.
Null N0 (must be able to differ on the statistic; brief): 200 draws (numpy seed 20261008), each masking, page by page, the
same number of random non-T40 tokens that carry exactly one key letter as the page has T40 tokens; statistic as above.
The instrument is a non-test (no value assigned, whatever T40 shows) if the null's 95th percentile top-value share >= 0.70.
Power control P (rule 3: subsampled to the target's own count): for each of T17 (s) and T46 (u), 50 draws (same seed
stream) masking a random 68-token subset of that cell's tokens across the seven pages (all of them if fewer than 68,
reported); P passes for a cell if in >= 80% of draws the top letter equals the key letter at share >= 0.70. If either cell
fails P, the instrument lacks power at this N: a T40 FAIL is logged "non-test", not a negative.

Outcomes: (i) N0 and P pass, G passes with letter v: v is the T40 witness at grade S. If v != 'a', key86.tsv T40 is changed
to v (source column names this test; the table's printed 'a' noted), all seven readings are regenerated with
tools/decode_key.py and --check, and the rule-4 grade files are flagged in ROOM for a re-grade (not hand-edited).
If v == 'a', the table cell is confirmed, key86.tsv unchanged. (ii) N0 and P pass, G fails: T40 has no single value at
this N (logged, key unchanged). (iii) N0 or P fails: non-test, key unchanged.
Descriptive only (not gated): the per-page split of T40's aligned letters, and the GAP count.
Script: d1apis/t40_align.py (writes d1apis/result.json, d1apis/t40_witness.tsv; --check exits non-zero if stale).

## Addendum B (written 8 Oct 2026 05:5x UTC, after variant A's result, before any variant-B number)
Variant A (all tested tokens masked at once) failed its own power control P (0/50 for T17 and T46): non-test, recorded.
Variant B changes one thing: tokens are masked ONE AT A TIME (every other token, other T40s included, decodes with key86.tsv),
so each token's witness is a deterministic function of the token; the witness is computed once for every token of the seven
pages that carries exactly one key letter, and for every T40 token. Statistic, gate G, null N0 (200 draws, per-page counts
matched to T40, seed 20261008, drawn from the precomputed non-T40 witnesses), power control P (T17 and T46, 50 draws of 68)
and outcomes (i)-(iii) exactly as above. This is the last variant of the alignment instrument this job runs; if B also fails
P, the alignment instrument is logged untested-at-this-N for T40 and not re-tuned here.
Script: d1apis/t40_align_b.py (writes d1apis/result_b.json, d1apis/t40_witness_b.tsv; --check).
