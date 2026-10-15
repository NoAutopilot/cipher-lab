# LANE DEFAULT-account-2-20261015-0810 jobs (account 2, lane orchestrator session_01YL9az8HuRPaSxvHMRW6h8m) -- 15 Oct 2026 08:2x UTC

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 08:10-18:10 UTC 15 Oct. Gate 0a: SESSION-SWEEP-account-2 stale-claimed since 5 Oct, proceeding.
Backlog: VERIFY-BACKLOG (Birago/ceppo `counted` rows off limits; eckert and sachsstaatsarchiv audit2 rows held by other lanes) -> step b,
`next_steps.py --hot-only` runnable rows, checked against each folder's latest Verdict line, plus the named nexts of LANE DEFAULT-A2-0509-15.
Excluded: LANE DEFAULT-A1-0740-15 (pro3055, fr5761, fr4712, mccormick, fr4735-monluc), LANE DEFAULT-A4-0645-15 (baluze167, clair1161,
lodewijk, na-suriname), VIV-KEYSTONE (fr16104/fr16106), BNF-FOCUS (fr3982, fr3985-3990), Birago family/ceppo, Armstrong, Debosnys,
cipher-lab-private.
Intake gate 08:2x UTC (tools/intake_gate_check.py, all pass): matignon-mayenne-1586, oldenbarnevelt-brederode-1605, harley-287-1587.

## Common rules for every job
Exactly the "Common rules for every job" section of `.claude/briefs/runs/2026-10-14-acct1-default-1840-jobs.md` (read it in full, and the
files it points to), with these substitutions:
- address every ROOM line "for LANE DEFAULT-A2-0810-15 (account 2)"; export `CIPHERLAB_ACCOUNT=account-2` before any tools/room.py call;
- first actions: `git fetch origin && git checkout -B main origin/main`, `date -u`, read the last 40 ROOM.md lines, post a claim line with
  your box end time; if a live claim (< 6 h, no done) already covers your job, or the folder's NOTES.md shows the step already done, post a
  flag + done line and stop;
- every claim/halfway/done ROOM line ends "usage: not readable here";
- **images never go into git**: crops, regions and page fetches stay in your session scratchpad; commit only TSV/MD/scripts;
- www.googleapis.com has 503'd repeatedly since 12 Oct: no job here uses it;
- openapi.bnf.fr / gallica.bnf.fr, de-crypt.org, service.archief.nl / nationaalarchief.nl and resources.huygens.knaw.nl are shared: ROOM
  take/release lines, >= 3 s apart, one at a time; DECODE: one browser login per session (tools/decode_browser_login.js), never a retry loop;
- run `tools/prior_work.py` for your item before the first priced step, and pre-register (PREREG-<job>.md pushed) before any score;
- pricing: an Opus vision call ~1.0, a Sonnet vision call ~0.6, a reconcile ~0.6-1.0; stop before a unit that would cross 80% of cap or box;
- every other rule there holds unchanged (halfway line, gaps_check on `partial`, decode_key --check where a reading changes, no novelty
  words, no AskUserQuestion, `date -u` before any time, "cost not visible to this session");
- solver jobs: report what was found and where it was not found; do not classify novelty.

## Wave 1 (08:2x UTC 15 Oct)

### MAT-F91E (Opus, cap 4, box 75 min, gallica/openapi.bnf.fr <= 4 only to regenerate crops): matignon-mayenne-1586 f.92r block E
Verdict line ~1370: "f.92r block E with MAT-F91B's corrected regions by MAT-F91C's crop recipe (iiif_lines --deskew-region --band-extent
--mask-neighbours), 2 blind passes + reconcile + the PREREG-MAT-F91 alignment (~$2.5)". Exactly MAT-F91C's method (NOTES section MAT-F91C,
PREREG 8c14b4143, f91/regen_f91.sh, f91/blocks.tsv): PREREG addendum first (same gate: pass agreement >= 0.65 and alignment R vs 200
shuffled-gloss draws p95). Units: cipher lines 2 blind Sonnet passes (<= 12 crops per call, ~0.6 each) + 1 reconcile (~1); gloss 1 Opus
read (~1). Report tokens, key values confirmed / conflicting / candidate (M), control numbers. No key.tsv edit; conflicts to HYPOTHESES.md
with witnesses (rule 4). Update Verdict, gaps_check.

### OBRED-TRY (Opus, cap 4, box 75 min, service.archief.nl <= 4 only to re-see 555/556 at native size): oldenbarnevelt-brederode-1605 glossed values on no. 92/187
Remaining gaps / Escalation key-rebuild line (OBRED-556): "resolve the gloss conflicts (415, 337, 100) on the image and build a per-unit
glossed-pair table, then apply it to no. 92/187 by decode_key.py --try with a value-class control". OBRED-556's route and scripts for the
images (NOTES section OBRED-556; images were not committed, so refetch the scans you need into your scratchpad). PREREG first: the conflict
rule (rule 4: conflicting H/C support is logged with witnesses, never settled by majority), the per-unit gate (rule 3, per-leaf merge: the
1619 letter's own pairing must clear a shuffle control before its glosses touch no. 92/187), and the --try control (value-class / shuffled
glossed-value control, power stated). Accepted values stay M unless --try's own control passes for that value class; no key.tsv edit except
through the folder's decode path with --check. Report per code: glossed value, occurrences in 92/187, --try outcome. Update Verdict, gaps_check.
Take/release lines for service.archief.nl; coordinate with OBRED-552 (one at a time on that host).

### OBRED-552 (Opus, cap 4, box 75 min, service.archief.nl / nationaalarchief.nl <= 8): oldenbarnevelt-brederode-1605 inv. 6019 scans 552-554 + 555 L15
Remaining gaps line 2 (OBRED-556): "fetch 552-554 (3 NA requests), two blind passes of any further numeral lines plus a second pass of 555 L15,
glosses read and checked, ~$3". OBRED-556's route (METS then the scans), its ciphertext_556.tsv columns and its pass protocol. PREREG addendum
first if anything is scored. If 552-554 hold no part of this letter (by eye: hand, address, sense), say so and record what they are. Output
ciphertext_552.tsv (or an extension of ciphertext_556.tsv with scan column) and the gloss table rows, graded as OBRED-556 did. Do not run the
--try (that is OBRED-TRY's). Update Remaining gaps, gaps_check. Take/release lines; coordinate with OBRED-TRY.

### HAR-F11 (Opus, cap 2, box 45 min, de-crypt.org one browser login, <= 8 requests): harley-287-1587 R8477 f.11 at full size vs R328 and R330
Verdict line ~206: "view R8477 f.11 at full size against R328 and R330 (~$1)". Use disk first (sources/decode/ and the HAR-KEYS section's
sha1 list). One DECODE browser login (tools/decode_browser_login.js, `--guess-fullsize` as A2-HDK did); fetch R8477's f.11 image at full size if
not on disk. Write a sign transcription of the f.11 cipher groups (one Opus look, crops in scratchpad, M-graded) as ciphertext_f11.tsv, then
compare each group against R328's alphabet/code list and R330's name list; pre-register what counts as a fit (as PREREG-HAR-KEYS.md's Fit A/B
with its control) before comparing. No key.tsv edit; a fit becomes a planned --try step. Update the known-keys line and Verdict, gaps_check.
