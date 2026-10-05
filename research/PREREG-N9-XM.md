# PREREG N9-XM -- per-pair nulls for four key_crossmatch nightly leads (5 Oct 2026, written before any statistic is computed)

Worker N9-XM (account 2, for LANE-NEAR9). Brief: .claude/briefs/runs/2026-10-05-ytbiz-near9-wave1.md, job N9-XM. Disk only.

Leads (ROOM.md 5 Oct 2026 02:53-02:54, tools/key_crossmatch.py nightly; gate 3.292, null p99 3.498):
- (a) ciphers/fr3993-villeroy-1595/keys/key_f200_no57_syll.tsv on ciphers/sanguszkow-mniszech-dunin-1714/ciphertext.tsv, stat 4.12
- (b) ciphers/hellen-frederick-1752/key_r4370/key_decode.tsv on the same ciphertext, stat 3.63
- (c) ciphers/clair1161-avis-flandre-1688/two/key_shuf4_s1.tsv on ciphers/decode-1168-modena-costabili-1492/ciphertext.tsv, stat 3.95
- (d) ciphers/clair1161-avis-flandre-1688/pool/key_shuf3_s1.tsv on the same ciphertext, stat 3.85

Statistic S (the tool's own, imported, not copied): `pair_stats(key, signs, model, n_shuffle=20, seed=0)['own']['stat']`
= max(z 4-gram, z value-frequency) against 20 class-shuffled-value keys; key, signs, language and model loaded exactly as
`run()` loads them (load_key_meta, language_for, load_ct_meta, build_repo_corpora, get_model with the target folder excluded).
Step 0: S for each cross key is recomputed and compared with the nightly value (drift reported, not tuned away).

Nulls, each >= 200 draws (seeds 1..200), S computed identically on each draw:
- N1 shuffled key (GATE): the cross key's values permuted among its own codes (tool's `shuffled_key`, all codes).
- N1c shuffled key, class-preserving (GATE): values permuted within value class (tool's `shuffled_key_by_class`).
- N2 random key: same code set, each code given a value drawn uniformly with replacement from the key's set of
  distinct values (same size, same value alphabet). Reported.
- N3 order-shuffled target: the cross key on the target's token list in random order. Reported. Caveat registered
  in advance: z value-frequency is order-invariant by construction (CLAUDE.md rule 3, control that cannot vary), so
  N3 can only move the z 4-gram component; N3 is reported per component and is not a gate on S.

Survival rule (fixed now): a lead survives only if S_cross > p99(N1) AND S_cross > p99(N1c) on that very ciphertext.
Otherwise it is logged "does not survive the per-pair shuffled-key null".

Miscalibration test (the brief's expectation, tested not assumed): the global gate 3.292 is called miscalibrated for a
ciphertext if, on it, more than 5% of N1c draws (pooled over the keys tested there) reach S >= 3.292 (the gate's own
design target is ~1% false-positive). Reported for both ciphertexts. If so, the proposed fix (a per-target null:
the pair's S against p99 of >= 200 class-shuffled keys on the same ciphertext) goes to ROOM as a flag; the tool is not
edited in this job.

For a survivor only: print the first 60 decoded tokens; say by eye whether any word stretch is in a language. No reading
claimed, no grades written.

Script: research/n9xm/xmatch_pair_null.py; outputs research/n9xm/results.tsv and nulls.json.
