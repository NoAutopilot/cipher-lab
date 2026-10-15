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

## Wave 2 (05:1x UTC 15 Oct)
Wave 1 results (all ledgered + archived, 16.29): LVN-4611 7.54 D, LIN-R7 1.63 Q, HEL-R7 1.71 Q (duplicate of VERIFY-HELLEN 9 Oct: my error),
NOAI-CH 2.56 D, COL26-KEY 2.85 D. Lesson applied below: before briefing a "next step", grep the folder for a section that already did it.
LANE DEFAULT-A2-0209-15 closed 04:4x; its folders are free, but nothing it touched in the last hour is taken here. nationaalarchief.nl 503 at 05:09.

### LVN-PIN (Opus, cap 5, box 75 min, resources.huygens.knaw.nl <= 2 or disk): lodewijk-van-nassau-1573-74 freeze the settle LM corpus, then 4611 p3
NOTES.md ~4697-4705 (LVN-4611 "Drift found"). (a) ~1: settle.py's LM corpus reads ciphers/fr2980-gramont/reading*.txt live, so another target's
edit makes this target's committed readings STALE (rule 7 hazard). Freeze it: a committed corpus snapshot (text only, inside the lodewijk folder or
tools/data with a manifest naming the source files and their git blob ids), settle.py reads only the snapshot. Then regenerate 4612 and 4616 (4616
via lvn16/apply.py per its note) and report every decision that flips vs the committed files (expected: few or none, like 4611's p2_L15/20 82 S->M);
all `--check` exit 0 afterwards. Do not change any decision rule. (b) ~2.5: 4611 p3 per the existing PREREG 48c69fc7a (key_p3.tsv already built and
pre-registered): placement, blind Sonnet calls incl. control, apply only what p3's own control licenses; decode_key --check. Stop before (b) if
(a) used > 50% of cap. Do not touch 4610 p2_L28/11 (a verifier rules on it in a later wave).

### COL26-1181 (Opus, cap 2, box 40 min, no network): colbert26-lathuillerie-1644 per-code test of 11=re and 81=me
COL26-KEY (NOTES.md, its section; PREREG 5b99f48cc; key_f23_c50rev.tsv) found the held-out gain carried by 11=re and 81=me. Test each code at every
occurrence with `tools/decode_key.py <t> --try 11=re` / `--try 81=me` (and `--avalanche` for the runner-up values), PREREG first with a per-code
shuffled control; a code that passes may move to S only if its own control passed (CLAUDE.md "Mary Stuart method tools": an accepted value is M
unless --try's own control passed for that value class). Write the result into key_f23_c50rev.tsv grades only; never overwrite key_f23.

### BAL-C275G (Opus, cap 4, box 60 min, openapi.bnf.fr <= 12 at >= 3 s, take/release lines): baluze167-davaux-1637 c275 7/5/E gloss search
Verdict ~2922 and gap ~2912. First grep NOTES.md and ROOM.md for any section after BAL-C275U4 that already searched c266-273/c277-285 line by line, or
already settled the f.22r last numerals (LANE DEFAULT-A1-0206-15 did "baluze167 f.22r three numerals M->S" on 15 Oct): if either is done, say so and
take only what is left. Job: search c266-273 and c277-285 line by line for a glossed occurrence of 7, 5 or E (the c275 hand's open signs), at a
resolution where the gloss is legible (canvases to scratchpad, never git); per-line crops, one Sonnet vision call per canvas at most (~0.6 each,
10-17 canvases: stop at 80% of cap). Any glossed hit is tested at every c275 occurrence (--try) before it enters anything; PREREG first.

### MANT-BERNER (Sonnet, cap 1.5, box 30 min, archive.org <= 6 at >= 2 s): sachsstaatsarchiv-manteuffel-1712 Berner 1901 djvu grep
NOTES.md ~3843, 3899, 4044: Berner 1901 was not re-tried after archive.org answered 500 on 9 Oct. Find the identifier in NOTES.md/sources.tsv, fetch
the _djvu.txt once (one retry after a pause max; a second failure stops the job), grep for the terms the earlier BO I passes used (Manteuffel,
Stanislas, Arnold, Jablonski, the report dates of Sept-Nov 1712); log hits and misses as search results (rule 10 wording), update the gap.
