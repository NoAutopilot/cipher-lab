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

Wave 1 sessions (08:19 UTC): MAT-F91E session_01CwXmm2kfQrxeWKwtSRByST, OBRED-TRY session_017rc54gF8WMfS6E2fCbdQKu,
OBRED-552 session_019yesqUFWDdRLknRarNyG6X, HAR-F11 session_01HeBjVVz39Xj2r1vEJLhFn7.

## Wave 1b (08:3x UTC 15 Oct)
Intake gate 08:3x UTC: kaliningrad-2015 pass (open).

### KAL-HOMRU (Opus, cap 3, box 60 min, disk/CPU only, no network): kaliningrad-2015 homophonic family on ru20_lat
NOTES.md line ~779 (KAL-RUCORP, account 1, done 05:46): "the homophonic (written order) family re-run with `--corpus` the ru20_lat s1s files
(its own matched control at N 1066 on ru20), ~$2 CPU, since the era change can only matter if the solver's own model uses it". Use
`tools/family_run.py <spec> --family homophonic --corpus <ru20_lat s1s>` (control first; CONTROL BELOW GATE -> exit 3 = the result; check
the control's blind baseline is not near ceiling, rule 3). PREREG first (gate as the folder's earlier homophonic run, seeds/restarts stated
and sized to the box: time one control seed before choosing the count). Judge any target decode with judge_plaintext.py against ru20 and score
the shuffled-target decode through the same judge (rule 3, ARM-C1 clause). Both numbers to HYPOTHESES.md. Status stays `open` unless rule 5
says otherwise; no reading claimed. Update the Next step / Verdict line.

## Wave 2 (08:4x UTC 15 Oct)

### OBRED-549 (Opus, cap 3, box 60 min, service.archief.nl / nationaalarchief.nl <= 10): oldenbarnevelt-brederode-1605 inv. 6019 scans before 552 for the key enclosure
OBRED-552 (15 Oct, f2332fdc8): scan 552 ends a Heidelberg 8 Oct 1619 letter whose last paragraph says the cipher was reformed and sent "with an
instructie ende sleutel". Its named next: scans 549-551 for the key enclosure (~1.5). Fetch the METS once, then 549-551 at 5000 px (and, only
if 549 is still inside the 8 Oct letter, walk back one scan at a time to its start, <= 4 more). Look by eye for a key sheet / instruction
(numeral tables, alphabet, name list) anywhere in that run. If a key leaf is found: record scan, layout and a transcription of its table into
key_6019.tsv (two blind Sonnet passes on crops + reconcile, grade H for values read from the key), and compare its values against
ciphertext_556.tsv's 45 C glosses (agreement count vs a shuffled-value control, PREREG first) -- that is a known-answer test of the key, not
a reading of no. 92/187 (no key.tsv edit; applying it to 92/187 is a later job). If no key leaf: say what 549-551 are, and stop. Take/release
lines for the NA host. Update Remaining gaps / Escalation (known-keys rung), gaps_check.

## Wave 3 (08:5x UTC 15 Oct)

### OBRED-BAND (Opus, cap 4, box 75 min, disk only): oldenbarnevelt-brederode-1605 band-interval decode with held-out leaf check
Escalation key-rebuild line (OBRED-TRY, 15 Oct): "band-interval decode with a held-out leaf check and shuffled-band control, then no. 92/187
graded M, ~$3". OBRED-TRY's statistic B (gloss letter rises with code value, rho 0.959; 555 0.930, 556 0.989) says the code list is ordered
alphabetically by value. PREREG first: fit the value->letter band boundaries on one leaf (555) and score the held-out leaf (556) glossed
codes against it, vs a shuffled-band control (>= 200 draws) and a power check (subsample to no. 92/187's own token counts, rule 3 ARM3-ADJ
clause). Only if the held-out check passes: decode no. 92/187 single-letter-band codes as interval readings (each token a letter range, grade
M), through a script that regenerates it (rule 7 shape, `--check`); never key.tsv; name codes (band 588-751) left as codes. Report held-out
accuracy vs control, and what fraction of 92/187 tokens fall in bands narrow enough to name one letter. gaps_check.

### OBRED-KEYHUNT (Opus, cap 4, box 75 min, resources.huygens.knaw.nl <= 30, service.archief.nl/nationaalarchief.nl <= 25): oldenbarnevelt-brederode-1605 the 1619 "instructie ende sleutel"
Remaining gaps line ~1917 (OBRED-549): "the States General resolutions of 17-28 Oct 1619 (Resolutien der Staten-Generaal, Huygens retroboeken,
nieuwe reeks 1619) for a note on the key's receipt or where it was laid, then a stride-1 screen of inv. 6019 scans 520-548 and 558-600 at
sheet size for a key leaf". Order: Resolutien first (host table row "Huygens retroboeken"; full-text search for Brederode / sleutel / cijffer
/ chiffre in the 1619 volume, read the hits for 17-28 Oct). Then the 6019 screen at the smallest size that shows a numeral table (e.g. 1000
px), stride 1, from 548 backward and 558 forward, stopping before 80% of cap or box; any candidate leaf at 5000 px. PREREG not needed for a
screen; if a key leaf is found, record scan, layout and a sample of rows only (transcription and the known-answer test against
ciphertext_556.tsv's glosses are a later job). Take/release lines for both hosts. Update known-keys line, gaps_check.

### KAL-SHEET2 (Opus, cap 1.5, box 45 min, web search + <= 10 requests to the source hosts): kaliningrad-2015 higher-resolution image of sheet 2
NOTES.md KAL-HOMRU "Next step": "a higher-resolution image of sheet 2 (the Russian source thread or strana39.ru) for the ghost lines below line
6, one fetch, ~$1". Find in NOTES.md / sources where cryptogram2.png came from; look for the original post and any larger copy (the source
thread, strana39.ru, a web archive capture via the CDX API). If a larger image exists, fetch it once to ciphers/kaliningrad-2015/images/ only
if under the folder's 30 MB limit (record manifest, sha1, URL, date), and one Opus look at the area below line 6: are the ghost lines
bleed-through of sheet 1, a second text, or cipher? Grade any read M. If none exists, log the hosts tried. No solving. Update Next step.

## Wave 4 (09:1x UTC 15 Oct)

### OBRED-MEM (Opus, cap 3, box 60 min, service.archief.nl / nationaalarchief.nl <= 25): oldenbarnevelt-brederode-1605 Maurits's deciphered memorie
OBRED-KEYHUNT (27f658b7d): res. 1779 (11 Oct 1619) records a Brederode memorie deciphered by Maurits; next "inv. 6019 stride-1 from 532 backward to
the 2 Oct 1619 letter (res. 1779c, S.G. 6019 orig.) for the memorie and any decipherment filed with it". Screen at 1000 px, candidates at 5000 px.
If a cipher memorie and/or its decipherment (interlinear, marginal, or a separate clear copy) is found: record scans and layout, and whether its
numeral groups are in the no. 92/187 / 1619 system (by eye: value range, name band 588-751); transcription and alignment are a later job,
priced in your Remaining gaps line. That is a period decipherment: say so plainly (rule 4: grade C for what it fixes, once aligned). Take/release
lines. Update Remaining gaps / Escalation (known-keys), gaps_check.

### MAT-KA (Opus, cap 3, box 60 min, disk only): matignon-mayenne-1586 held-out known-answer test of the label candidates
Verdict ~1408 (MAT-F91E): "a known-answer instrument for the U=e/T=r/D2=a/BOX2=u/+=m candidates pooled over blocks A-F, holding out one block's
gloss per label with the same shuffle control (~$2)". Rule 3 third-attempt clause: the --try window score is retired for these (power control
failed); this is a different instrument (block-held-out gloss agreement). PREREG first: per label, fit on five blocks, predict the held-out
block's gloss letter at that label's positions, pooled leave-one-block-out accuracy vs >= 200 label-shuffled draws (p95) and a power check (a
known H code with the same occurrence count must pass). Labels below power are "too-short", not rejected. A passing label is reported as a
candidate for key.tsv at grade S with its numbers; no key.tsv edit in this job. HYPOTHESES.md rows, Verdict, gaps_check.

## Wave 5 (09:3x UTC 15 Oct)

### MAT-KEY (Opus, cap 3, box 60 min, disk; openapi.bnf.fr <= 4 only for the image check): matignon-mayenne-1586 apply the four S candidates
MAT-KA (a948d56a8): U=e, T=r, D2=a, BOX2=u passed the block-held-out gloss test with power (grade S); next "key.tsv edit + decode_key --check +
per-leaf judge (~1.5), image check Bourdeau labels vs f.91 labels (~1)". Order: image check FIRST -- confirm by eye on the f.91/92 crops and the
target leaves that the labels U, T, D2, BOX2 name the same sign shape in both transcriptions (the f.91 passes and the target's ciphertext); a
label that does not match is not applied. Then add the matching values to key.tsv at grade S through the folder's own decode path
(decode_key.py / decode.json), regenerate the readings with --check, and run judge_plaintext.py per leaf before and after (paste both outputs in
NOTES.md, rule 7). Report tokens changed per leaf and the grade counts before/after. A reading that changes after AUDIT.md is propagated per rule
10 (AUDIT.md section + any SECOND-OPINIONS-QUEUE row) -- name it in a ROOM flag for a verifier rather than re-auditing yourself. gaps_check.

### OBRED-SEG (Opus, cap 4, box 75 min, disk only): oldenbarnevelt-brederode-1605 constrained segmentation of the no. 92/187 intervals
OBRED-BAND (5417397a0): held-out band check PASS; reading_92_187.tsv gives each token a letter interval (72 of 180 one-letter); next "constrained
segmentation of the intervals with its own control (~3)". PREREG first: a Dutch (nl16/nl17, check era match per rule 3) lexicon/n-gram search
over the interval lattice, scored against (a) the same search on shuffled-band intervals (>= 200) and (b) a synthetic control: a known Dutch
1600s text enciphered with the fitted bands at no. 92's length, which must segment above gate. Report words recovered with their spans, the
control numbers, grade M throughout (S only where the control licenses it). No key.tsv; a script that regenerates the output with --check.
gaps_check.

### OBRED-OCT2 (Opus, cap 2.5, box 45 min, service.archief.nl/nationaalarchief.nl <= 8 plus catalogue lookups <= 10): oldenbarnevelt-brederode-1605 the 2 Oct 1619 letter and the memorie's home
OBRED-MEM (5fdcc740a): next "read the 2 Oct letter (528-530) for a mention of the memorie (~1.5), then Maurits papers (KHA) / S.G. secrete
liassen (~1)". Read 528-530 (one Opus read, crops in scratchpad) for any mention of a memorie, cipher, sleutel; then catalogue lookups only
(NA 1.01.02 secrete liassen 1619 inventory; Koninklijk Huisarchief A14 Maurits finding aid if online) for where a deciphered Brederode memorie
would be filed. Record what was read and where nothing was found. No fetching of whole series. gaps_check.

## Wave 6 (09:5x UTC 15 Oct, last refill)

### MAT-EYE (Opus, cap 2, box 40 min, disk; openapi.bnf.fr <= 4): matignon-mayenne-1586 eye f.110 T/BOX and f.143 x/D
MAT-KEY (ca9992ef7): next "eye f.110 T/BOX and f.143 x/D (~2)"; f.110 T (38 of 53) were not eyed before T=r was applied at S. Check by eye on
native crops that the f.110 tokens labelled T and BOX2 are the same shapes as the f.91/f.124v exemplars, and the f.143 x/D labels likewise. Any
mismatch: list the tokens, and regrade them (to M or U) only through the folder's decode path with --check. Report counts matched / not. gaps_check.
