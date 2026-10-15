# LANE DEFAULT-account-4-20261015-0437 jobs (account 4, lane orchestrator session_014F2NNFZiwF72cavhiYaLht) -- 15 Oct 2026 04:4x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 04:37-14:37 UTC 15 Oct. Gate 0a: no SESSION-SWEEP-account-4 row.
Backlog = the previous account-4 lane's next list (STATUS.md "LANE DEFAULT-account-4-20261015-0235 handoff") plus `next_steps.py --hot-only`
runnable rows, each checked against the folder's own NOTES.md Verdict (stale rows dropped: wallis-emus203 Thurloe grep done 6 Oct R8-SPLOOK;
naf14913 605 verified 6 Oct R9-ROUSV2). na-suriname SUR-2061: www.nationaalarchief.nl answered 503 at 04:43 UTC, held.
Excluded: LANE DEFAULT-A2-0209-15 holdings (sforza-*, sp105, eckert, fr4712, clair1161, baluze167, thurloe, erba), VIV-KEYSTONE (fr16104/fr16106),
BNF-FOCUS (fr3982, fr3985-3990), Birago family/ceppo, Armstrong, Debosnys, cipher-lab-private.
Intake gate 04:4x UTC (tools/intake_gate_check.py, exit 0): lodewijk-van-nassau-1573-74, fr16142-noailles-constantinople-1571,
hessen-daenemark-1672 (antt-linhares-chave reports `blocked` line 3 = terminal, the re-derivation is a rule-7 check, not deep work).

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-14-acct1-default-1840-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A4-0437-15 (account 4)"; export `CIPHERLAB_ACCOUNT=account-4` before any tools/room.py call;
- first actions: `git fetch origin && git checkout -B main origin/main`, `date -u`, read the last 40 ROOM.md lines, post a claim line with
  your box end time; if a live claim (< 6 h, no done) already covers your job, post a flag + done line and stop;
- every claim/halfway/done ROOM line ends "usage: not readable here";
- **images never go into git**: crops, regions and page fetches stay in your session scratchpad; commit only TSV/MD/scripts;
- www.googleapis.com answered 503 repeatedly 15 Oct 02:2x-03:41 UTC: no job here uses it;
- openapi.bnf.fr / gallica.bnf.fr and resources.huygens.knaw.nl are shared: ROOM take/release lines, >= 3 s apart, one at a time;
- run `tools/prior_work.py` for your item before the first priced step, and pre-register (PREREG-<job>.md pushed) before any score;
- pricing (last lane's overruns): an Opus vision call ~1.0, a Sonnet vision call ~0.6, a reconcile ~0.6-1.0; stop before a unit that would
  cross 80% of cap or box;
- every other rule there holds unchanged (halfway line, gaps_check on `partial`, decode_key --check where a reading changes, no novelty
  words, no AskUserQuestion, `date -u` before any time, "cost not visible to this session");
- solver jobs: report what was found and where it was not found; do not classify novelty.

## Wave 1 (04:5x UTC 15 Oct)

### LVN-4611 (Opus, cap 8, box 90 min, resources.huygens.knaw.nl <= 4 or disk): lodewijk-van-nassau-1573-74 LVN16-3R per-token read on 4611 + one eye check
Same protocol, same control, same gate as LVN-P2 (`lvn10p2/PREREG-LVN-P2.md` and its placement note; NOTES.md LVN-3R / LVN-P2 sections). Write a
PREREG addendum for 4611 and push it before any read. (a) Eye check of 4610 p2_L28/11 (LVN-P2's control miss: H 81 read 61; one crop, one Opus
look beside the H exemplars of 81 and 61; report whether the image contradicts the H grade -- do not edit the key; if it does, write it as a gap).
(b) 4611 per-token read: placement, ~4-5 Sonnet calls incl. control x 0.6 + 1 reconcile. Apply only tokens 4611's own control licenses (rule 3
per-unit merge). decode_key --check after; report C/H before and after.

### LIN-R7 (Opus, cap 2, box 45 min, no network): antt-linhares-chave rule-7 fresh re-derivation
You are the fresh session rule 7 asks for: you have not seen the reading. Read ONLY `specs/antt-linhares-chave.json`, `ciphers/antt-linhares-chave/
key.tsv`, `decode.json` and the ciphertext; do not open reading.txt / reading_tokens.tsv or NOTES.md readings before your re-derivation is written to
your scratchpad. Re-derive with the target's decode script (`python3 tools/decode_key.py ciphers/antt-linhares-chave`), then diff against the
committed reading and run `--check`. Report the diff count against the M-graded token count (a difference above the M tokens sends the reading back,
rule 7). Run `tools/judge_plaintext.py` with the spec as rule 7 says; paste output. Append a short "## LIN-R7 rule-7 re-derivation" section; tick the
gap if passed; gaps_check.

### HEL-R7 (Opus, cap 2, box 45 min, no network): hellen-frederick-1752 rule-7 fresh re-derivation of reading_R1953_img.txt
NOTES.md line ~1799 "VERIFIER WANTED". Same discipline as LIN-R7: read the spec (`specs/hellen-frederick-1752.json`), the key and the ciphertext
for R1953 first; locate the decode script that produced reading_R1953_img.txt (grep NOTES.md for its command only), re-derive into your
scratchpad before opening the committed reading, then diff, report the count against the M-graded tokens, judge output pasted. Append "## HEL-R7"
section; update the NEAR.md row's next step only if it names this re-derivation.

### NOAI-CH (Opus, cap 2, box 45 min, archive.org <= 6): fr16142-noailles-constantinople-1571 Charriere III p.168 note and p.207 n.1 against c231
NOTES.md Verdict line ~1791 and the NOAI-C262 section. Fetch Charriere III's IA djvu text (identifier from NOTES.md/sources.tsv; once, to scratchpad
or disk if already present), read p.168 note and p.207 n.1, and test whether either prints the clear text that c231's cipher carries (alignment on the
c231 clear/decoded tokens on disk, pre-registered gate + shuffled control before any score). Report hit or miss; a hit becomes a C-crib only through
the folder's existing alignment path.

### COL26-KEY (Opus, cap 4, box 75 min, no network): colbert26-lathuillerie-1644 next key revision with canvas 50 folded in
Verdict line ~2437: "cheapest next: the next key revision with canvas 50 folded in as a unit that cleared". Canvas 50 cleared its own control
(VER-COL50 word-grain check: C 21 kept). Fold only the 21 C-grade c50 pairs into the pooled key as a unit (rule 3 per-unit merge paragraph: check
each unit's own control result before merging; c51 FAILed, do not merge it). PREREG first: what the revision must do on the held-out canvases to
count (a leave-one-unit-out gain vs a shuffled-pair control). Write the revision as a new key file beside the old (never overwrite); report the
held-out numbers before/after; decode_key --check on any reading regenerated.
