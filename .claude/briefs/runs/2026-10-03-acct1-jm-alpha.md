# LANE-JM job 2a: JM-ALPHA -- rah-juan-manuel-1521 letter-alphabet recovery (account 1), 3 Oct 2026

Lane brief `.claude/briefs/runs/2026-10-03-acct3-lane-jm.md` job 2; common rules = the "Common to every job" section of
`.claude/briefs/runs/2026-10-03-acct1-jm-wave1.md` (claim/done lines, per-unit stop, crops pasted, DECODE images never committed,
gaps_check, file_shrink_guard, no novelty words, no AskUserQuestion). Read first: ciphers/rah-juan-manuel-1521/NOTES.md whole
(FT-A test 0, CS-3, and JM-K's "Premise check 2" section), specs/rah-juan-manuel-1521.json, TRANSCRIPTION.md.
Opus (you); Sonnet subagents, at most 3 at once. **Cap USD 12, box 100 min.** `pip install numpy pillow` if tools need them.

State: Tomokiyo's nomenclator (sources/cryptiana/keys/AlonsoSanchez_2.tsv, word codes) reads; the letter alphabet (the '#' signs in
ciphertext_f194.tsv / f34.tsv, about half the signs) is unread and not on disk. R9528 has the clerk's decipherment f.197 of cipher page
f.194 (gloss_f197.tsv lines 1-15 transcribed once); R9529 has cipher f.199 and decipherment f.201 (not transcribed).

Steps (units and per-unit estimates; stop before a unit that would cross 80% of cap or box):
1. One DECODE browser login (`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js`), fetch R9528 and R9529 full-size images
   to your scratchpad (sha1 into images/manifest.json, never commit images). ~USD 0.5.
2. Crops (pasted command + overlay check): `tools/iiif_lines.py --image <file> --out <scratch>/crops --debug` for f.194, f.199, f.201.
3. Signs as tiles (TRANSCRIPTION.md steps 2-5): `tools/glyph_atlas.py segment` + `cluster` (over-split) over f.194 + f.199 (+ f.34 of
   R9501 if already fetched cheaply; FT-A's images are gone, refetch R9501 only if it costs no extra login). One family atlas in
   ciphers/rah-juan-manuel-1521/atlas/ (tiles of DECODE images stay out of git: commit the atlas TSV/JSON labels, not image tiles,
   unless the tool can write them to scratch; say what you did).
   If the atlas route fails on this hand within ~25 min, fall back to two blind Sonnet passes per cipher page with a shared sign
   inventory + your reconciliation (3 calls per page at ~USD 1.5) and report err_2reader.
4. f.201 gloss: one Sonnet read of the f.201 crops (~USD 1.5); f.197 lines beyond 15 if needed (~USD 1.5).
5. Alphabet recovery on R9528 ONLY: align f.194 (nomenclator codes decoded with Tomokiyo's table, symbol tiles/labels left open) to
   the f.197 gloss: the decoded code words anchor the alignment, the spans between anchors give sign -> letter(s) assignments.
   Use `tools/interlinear_align.py` (or `tools/decode_witness.py` with a letter layer) -- add an option rather than writing a private
   aligner (Usage 8). Output `alphabet.tsv` (sign/cluster id, letter, count, grade C, source f.194/f.197 line refs).
6. **Pre-register before touching R9529's scores**: write `witness/gate_alpha.txt` (with `date -u`, commit + push it BEFORE step 7)
   stating: statistic = letter-level agreement (or word LCS precision) of the decode of f.199 vs the f.201 gloss, computed ONLY over
   alphabet-spelled stretches (so the nomenclator layer cannot carry it); null = the same with 200 shuffled alphabets (sign->letter
   values permuted, nomenclator fixed: a shuffle that CAN move this statistic); gate = real > max of the 200 AND >= an absolute floor
   you set from step 5's in-sample number (state it). Name N.
7. Held-out on R9529: decode f.199 with alphabet + nomenclator, score vs f.201, write both numbers, rank, N, err_2reader/err_true.
   Grades per token (rule 4): C for in-sample values from the gloss, S only where the held-out gate passes; M otherwise.
8. NOTES.md section "## Test 1 (JM-ALPHA)", spec `cheap_test_done` entry for test 1, scripts/test1.py that regenerates every number
   (exits non-zero if stale), Remaining gaps/Escalation/Verdict, gaps_check pasted. Do NOT do job 2b (R9501 passes + key test):
   name it as the next step with a cost.
