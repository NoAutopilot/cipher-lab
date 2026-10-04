# LANE-POOLS2 wave 2 follow-ups (account 1), 4 Oct 2026 06:1x UTC

Common: CLAUDE.md, `tools/room.py --start`, last 30 ROOM.md lines, claim before work, `date -u` before any time, common tail of
`.claude/briefs/README.md`. Good-citizen rule and the CLAUDE.md host table. Never print credentials, never name the owner, never call
AskUserQuestion. Do not touch QUEUE.md, POOLS.tsv, status.json, NEAR.md. Report what was found and where it was not found; do not
classify novelty. Done line via tools/room.py, role "LANE-POOLS2 <JOB> (account-1 worker)", ending "cost: see the lane ledger".

## COS-M -- costabili-modena-1491: measure the pool, then (only if it passes) the first cheap test
Model Opus 5.5 (you). Cap USD 7, box 60 min. Read `ciphers/costabili-modena-1491/NOTES.md` (CS-4, 4 Oct) and the two sibling folders
`ciphers/decode-1162-modena-ambung-1492`, `ciphers/decode-1168-modena-costabili-1492` (key.tsv, MOD1162's band-shuffled control).
1. One DECODE browser login (`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js ...`, `--guess-fullsize` as A2-HDK did),
   one session, fetch R1163-R1167 and R1095-R1097 page images (images go to a scratch dir, NEVER committed; record a manifest with
   record id, file, size, sha1). If full-size is refused, use whatever size is served and say so.
2. For every page: cipher present (y/n), a period gloss/interlinear or Exemplum present (y/n), and an estimated sign count (count
   signs on 3 sampled lines x lines on the page; say the sample). Compare R1095-R1097 with Berzeviczy no. CLXXXVIII (13 Feb 1493).
   Write the per-record table into NOTES.md; replace "FAIL-PROVISIONAL" with "Pool bar: PASS|FAIL (<open signs> measured-estimate)".
3. Only if PASS: write `specs/costabili-modena-1491.json` (CLAUDE.md Pipeline 3a fields, `judge` block; it15/it-era corpus check:
   say whether tools/data has an era-matched Italian corpus) and run the first cheap test: transcribe ONE sampled page of R1165 (or
   the record with the most unglossed cipher) by crops -- `python3 tools/iiif_lines.py --image <file> --out <scratch>` pasted -- 2
   blind Sonnet passes + your reconciliation (3 units, ~USD 1.5 each), apply decode-1168 `key.tsv` with `tools/decode_key.py`
   (decode.json if needed), statistic = the MOD1162 statistic G against its band-shuffled-key null (>= 1000 shuffles, computed first;
   a shuffled-key null CAN differ on G -- rule 3 orthogonality check stated in one line), and the positive control G on R1162 from
   its folder in the same run. Pre-register (commit) before the decode. Write both numbers into `cheap_test_done`. Ciphertext
   transcription (text, not images) may be committed.
4. Gaps/Escalation refreshed, gaps_check passes, intake gate exit 0 pasted. Stop.

## VIV-M -- fr16106-vivonne-longlee-1579: finish check-solved and measure the Vivonne residual
Model Sonnet. Cap USD 5, box 50 min. **Started only when no other LANE-POOLS2 worker is on Gallica.** Read
`ciphers/fr16106-vivonne-longlee-1579/NOTES.md`. Never write to `ciphers/fr16104-vivonne-spain-1572`.
1. Run the check-solved template's "Web and blog check" section that CS-1 skipped (Cryptiana blog, Cipherbrain, Cipher Mysteries,
   DECODE listing for fr.16106-16110, Bourdeau + Aymeloglu grep for Vivonne/Longlée/Saint-Gouard/16107/16108).
2. Parse Mousset's printed table of letters into `mousset_letters.tsv` (date, printed page, source folio) from the IA djvu text on disk
   or one fetch.
3. Measure the Vivonne 1579-82 residual: for fr.16106 ff.207+, fr.16107, fr.16108, use Gachard II's dates and double-numbering to
   predict which cipher letters lack a decipherment leaf; verify by contact sheets at 600 px (<= 60 Gallica requests, each canvas
   once, >= 2 s apart). Table: letter, folio, cipher pages, decipherment leaf (y/n, folio), est. signs (3-line sample x lines).
4. Replace the Pool bar line with a measured PASS|FAIL; if PASS name the cheapest first test (the in-volume decipherments make a
   grade-C key by `tools/interlinear_align.py` the obvious one). Gaps/Escalation, gaps_check, intake gate pasted. Stop.
