# POOLS survey, wave 2 (10 Oct 2026, 02:2x-02:4x UTC), for LANE FAMILY-A2n (account 2)

Disk-only survey of KEY-OFFICES.tsv rows in this lane's families against SIBLINGS-2026-10-08.tsv, NEXT-STEPS.tsv and each folder's NOTES. Table: `research/POOLS-FAMILY-2026-10-10.tsv` (sorted runnable, claimed, blocked, done-already; within a class by key in hand, images, signs, cost). Signs estimates are token counts of the folder's own ciphertext file where one exists, otherwise `?`. The "ROOM claim < 6 h" column is read against 20:25 UTC 9 Oct.
Top 5 runnable (unclaimed), each a cheap step:
1. wvo-hessen-1564, WVO 1109 f.23 (key.tsv in hand, 19 images, 209 signs, glossed 10/10 row pairs): separate verifier on gloss reading and key + two blind passes on the ten German gloss rows, ~$3.
2. thurloe-printed P25-P28 (~409 tokens, four keys in hand): fetch page images with tools/iiif_lines.py to replace OCR-line pairs, then --check with shuffled-key control, ~$2.
3. wvo-11008-certain-1572 (39/54 at H): fix the R2 span in w5194_gate.py (AUDIT 3), regenerate the gate, ~$0.5.
4. thurloe-printed P3 postscript and P10 p.620 L10 (~40 tokens): key_butler / key_blake_extended --check with shuffled control; too short for D2, ~$0.5.
5. decode-4450-bnf-fr20506-1525 f.2/f.4 (20 images, no key in KEY-OFFICES): initial-letter test with shuffled-pairing control, ~$3 (oldenbarnevelt-brederode inv. 6016 contact sheets, ~$1.5, is next but shares NA with OLD-O2).
design_prior.py (all `--no-write`, top line): wvo-hessen-1564/ciphertext.tsv 209 tokens, mixed (partial table) d=1.59 not above null, letter-for-letter d=2.10 not above null; august-van-saksen ciphertext_53.tsv 364 tokens, letter-for-letter d=0.05 plausible; wvo-11008 ciphertext.tsv 54 tokens, mixed (partial table) d=0.27 plausible; na-suriname ciphertext.tsv 56 tokens, multi-sign not above null; thurloe P25 412 tokens, letter-for-letter excluded, multi-sign not above null. decode-1411 ciphertext_f136.tsv: tool traceback (input shape), not run further.
HTRC probe, rah-salazar-soria-sanchez-1524-28, 02:22 UTC: `htrc_ef_headwords.py osu.32435013919725 ...` returned PrimaryUnavailableException; no rerun, no retry (ROOM line posted).
Not covered: oxenstierna and trew-posthius name no unread sibling in the three registers; Scandinavian and DECODE-held rows beyond decode-4450/1411/2678 were not enumerated one by one.
