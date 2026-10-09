# XMATCH-TRIAGE, 9 Oct 2026 (account 2, for the account-4 orchestrator)

Brief: `.claude/briefs/runs/2026-10-09-account4-orch-jobs.md`, section XMATCH-TRIAGE. Every `key_crossmatch nightly`
"xmatch hit (new lead)" ROOM line of 4, 5, 7 and 8 Oct 2026, one line each. Classes: (a) same office/key family
already known; (b) a real new lead; (c) noise. Most were already checked by a worker on the day, and their
verdicts are only collected here; the two 8 Oct leads had a one-line orchestrator note and nothing in either
folder, and are checked below.

**Result: 0 (b) leads.** Nothing written to any NOTES.md "## While waiting", and no NEXT-STEPS row.

| Nightly | Key -> ciphertext (stat) | Class | One line, with where it was settled |
|---|---|---|---|
| 4 Oct 02:53 | fr3993-villeroy-1595 key_f159_letters -> august-van-saksen-1561-64 ct58_sample / ct74 / ct57 (8.66 / 7.22 / 6.48) | (c) | Noise from how the null was built: f159 covers only 8 sign types and decodes to o/i/l/t; 0/445 covered ct74 tokens agree with AVS key_74 (N4-XM, d3f3f467; AVS NOTES.md). |
| 4 Oct 02:54 (also 3 Oct 06:26) | fr3416-nevers-fils-1589 key_no25 -> fr3993-gonzague-nevers-1595 ciphertext_tokens (6.0) | (a) | Known relative: 40/40 shared letter codes agree, no.70 = no.25 plus 7 letters on its nulls (N4-XM; gonzague NOTES.md). Added to SIBLING_FOLDERS today. |
| 4 Oct 02:54 | hellen-frederick-1752 key_r4370 -> rah-morillo-1817 rederiv (5.17, n=21) | (c) | Too short: n=21 is below min_tokens 100, so the stat has no calibrated meaning (N4-XM; rah-morillo NOTES.md). |
| 5 Oct 02:53 | fr3993-villeroy-1595 key_f200_no57_syll -> sanguszkow-mniszech-dunin-1714 (4.12) | (c) | Frequency coincidence: z4gram is no better on true order than on order-shuffled order (43% of shuffles >= real), and no word stretch by eye (N9-XM e83752c4; sanguszkow NOTES + HYPOTHESES). |
| 5 Oct 02:53 | clair1161 two/key_shuf4_s1 -> decode-1168-modena-costabili-1492 (3.95) | (c) | A shuffled control key that cannot be real by construction; it cleared the gate through multiple testing. Control keys are now excluded by name (N9-XM; N9-XMFIX d7e51949). |
| 5 Oct 02:53 | clair1161 pool/key_shuf3_s1 -> decode-1168 (3.85) | (c) | Same as the row above. |
| 5 Oct 02:54 | hellen-frederick-1752 key_r4370 -> sanguszkow (3.63) | (c) | Does not survive its in-class null (3.629 vs p99 3.766; N9-XM). |
| 7 Oct 03:00 | rah-juan-manuel-1521 key_tomokiyo_alpha -> trew-posthius-1614-18 (5.68) | (c) | Loader bug: the key loaded as an identity alphabet and read Trew's clear crib lines. The judge FAILs la17 and de17 (XMATCH-0307 e45b385d; the loader was fixed by FRESH-0914; ADJUDICATED). |
| 7 Oct 03:00 (posted twice) | _keys/gonzaga-nevers-asmn-ag423-c396 -> jan-van-nassau j5s glossed 5557/5552 (4.22) | (c) | At shuffle level against the leaf gloss: exact 0 (shuffle 0), letter 0.819 vs shuffle mean 0.711 (XMATCH-0307; ADJUDICATED). The duplicate post came from that key being listed twice in the sweep. |
| 8 Oct 02:51 | ceppo-nevers-fr3251-1570s harvest/key_f11 -> ceppo-nevers-fr4702-f36 (5.05) | (a) | Same office: KEY-OFFICES row 61 (Ceppo -> Nevers). f.36r is the unread sibling KH4-A found on 7 Oct. Its decode with key_ceppo_nevers already FAILs the it16dip judge, and the folder is held at the intake gate (CEPPO-4702, 8 Oct). Added to SIBLING_FOLDERS today. |
| 8 Oct 02:52 | sforza-italien1584-1447 amidani/key_f367 -> dupuy468-anhalt ciphertext (3.65) | (c) | Checked today. 18 sign labels are shared (q, V, P, D, R, cc ...), but they name different drawn signs in the two folders: **0 of 512** tokens covered by both keys agree with Anhalt's gloss-backed key.tsv (q: a vs e, V: s vs i, P: o vs s ...). The target is found-solved. Added to ADJUDICATED today. |

## Tool change (tools/key_crossmatch.py, today)

- `SIBLING_FOLDERS`: added {ceppo-nevers-fr3251-1570s, ceppo-nevers-fr4702-f36} and {fr3416-nevers-fils-1589,
  fr3993-gonzague-nevers-1595}. Their hits are now labelled `sibling`, not `new lead`.
- `ADJUDICATED`: added the amidani key_f367 -> dupuy468-anhalt pair. The nightly run labels it and does not post it again.
- All four `tools/tests/test_key_crossmatch*.py` pass.

## N9-XM's 5 Oct flag (Usage 8 proposal on key_crossmatch.py): **yes**, both parts. Both were already applied on 5 Oct.

1. Exclude shuffled/control keys. **Yes.** A key built to be null cannot be a candidate. N9-XMFIX (d7e51949 + 19fa6b5f)
   added `KEY_NAME_EXCLUDE` (shuf|control|null in the basename), which drops 35 clair1161 key_shuf* files.
2. Add per-pair nulls before posting (an in-class shuffled-key p99 and an order-shuffled z4gram p99). **Yes.** About
   815 pairs scored at a roughly 1% per-pair false-positive rate means about 8 hits a night from noise alone. N9-XMFIX
   added `pair_lead_null`. With it, the 5 Oct nightly's 4 leads dropped to 0, and the 7 Oct XCAL run's 24 over-gate rows
   left 0 new leads.

What remains, shown by today's 8 Oct row: amidani -> anhalt passed **both** nulls (in-class p99 3.311, order p99 3.182)
and is still noise. Neither null can see that two folders use the same transcription label for different drawn signs.

Suggestion, not applied (Usage 7: a single incident): when the target folder already has its own verified key, report the
share of tokens where both keys give the same value, and drop the row as a lead when that share is near 0. On this pair
the check gives 0/512. It needs a second instance before it becomes a gate (Usage 8a).
