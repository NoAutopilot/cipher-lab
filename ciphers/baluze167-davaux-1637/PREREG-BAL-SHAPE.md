# PREREG-BAL-SHAPE (BAL-CROP worker, LANE DEFAULT-A1-0640, owner account), written 13 Oct 2026 07:0x UTC by date -u,
# pushed in its own commit BEFORE any gloss read, tile cut for scoring, or tile read

Target: Baluze 170 f.228r-v (Chavigny to d'Avaux, Amiens 25 Aug 1640, bare cipher). Question: do the f.228 letter-sign shape
classes carry the values the reading gives them (b167228/to_pipe.py: f.229 majority + SIG-B228/B228B exemplar maps, all grade M),
when checked against PERIOD-glossed signs of the same hand? Brief: .claude/briefs/runs/2026-10-13-acct1-default-0640-jobs.md
"BAL-CROP" step 2 = .claude/briefs/runs/2026-10-11-ytbiz-default-0509-jobs.md "BAL-SHAPE".

Material (fetched 13 Oct 2026, openapi.bnf.fr, images/b170gloss/, manifest there): glossed Chavigny 1640 leaves of the f.228 hand,
eye-checked against the f.228 crops before cutting: f.258r (c270, dense block, gloss above most runs) and f.233r (c244, two short
runs, glossed) MATCH (same italic secretary hand, acute-marked numerals, same q / h / u+ / y-bar / mm forms). f.239r (c251) is a
looser hand with mostly unmarked numerals: NOT used for the positive control or exemplars (reported only).
Negative material: Baluze 169 f.208r (c420 of btv1b9001488b), Saint-Chamond's cipher -- a different key and a different hand
(NOTES.md l.14: "f.208 is Saint-Chamond's cipher, outside the pool"), with letter-like signs (y, g, w, 3-forms) that overlap the
d'Avaux inventory in look (a vocabulary-overlap negative: the reader can be fooled by look-alikes, so its number can differ).

## Step A: gloss labels (V-BRANDT rule)
1. Two independent blind Sonnet reads of the f.258r and f.233r line crops (images/b170gloss/lines_*), each transcribing per cipher
   line the cipher tokens in order and the interlinear words above them. No key, no values, no f.228 material shown.
2. A letter sign on f.258r/f.233r gets a gloss label L only when, in BOTH reads, the gloss word above its span is the same and the
   worker's alignment of that word against the flanking numerals (decoded with key.tsv H rows, Tomokiyo's published table) leaves
   exactly one letter for the sign. Labels per read are kept (passA/passB); signs whose label differs between reads are dropped.
3. From the labelled signs: one exemplar per letter (the first labelled occurrence) forms the exemplar sheet (E-<letter>);
   the remaining labelled occurrences are the positive-control tiles P. Target: >= 8 P tiles; if fewer than 8 survive, stop:
   "non-test, too few glossed signs", nothing scored.

## Step B: one blind tile read
4. Unknown sheet(s), shuffled with a fixed seed into blind ids: T = the 29 already-located f.228 letter-sign tiles with a current
   value (b167228/sig_tiles.py TARGET + DECOY minus 'wave' (no value), b167228/sig2_tiles.py SHAPES; same tile() geometry, same
   coordinates, no re-placement); P (step 3); N = 8 letter-like signs of 169 f.208r. Exemplar sheet: E-* from step 3 only (no f.229
   tile, no Tomokiyo block, so no exemplar carries a value from this project's own readings).
5. One blind Sonnet subagent read: per tile, the best-matching exemplar label or NONE, plus high/low confidence.
6. Gates (both must pass; P accuracy computed separately with pass-A and pass-B gloss labels, both must pass):
   G1 positive: P accuracy (reader label == gloss label) >= 0.75.
   G2 negative: N non-NONE rate <= 0.50 AND <= (P non-NONE rate - 0.25).
   If either fails on read 1, ONE second blind read (fresh subagent, reshuffled ids, seed+1); the gates are then evaluated on read 2
   alone; if still failing: logged non-test/negative, no grade or value changes.
7. Target statistic (only if gates pass): per f.228 shape class, the share of its tiles read as the exemplar whose letter equals the
   current value. Class CONFIRMED if >= 2/3 of its tiles (the one tile for a 1-tile class) agree and no tile is read as a different
   letter with high confidence. Overall T agreement is reported beside a permutation null (1000 shuffles of the T labels, seed
   20261013, p95) -- reported, not gating.
8. Adoption: tokens of a CONFIRMED class on f.228 move M -> S (cryptanalytic with a control) through an exceptions file read by
   decode_key.py, never by hand; a class read as a different letter by the majority is logged as a conflict in HYPOTHESES.md (stays M,
   image check next); every other class unchanged. Then `python3 tools/decode_key.py ciphers/baluze167-davaux-1637 --check`.
   Values never change in this job (shape classes keep their letter; only grades move), so the fr17 judge is not re-run.
Caps: USD 6 job cap, box to 08:42 UTC (80% 08:20). Units: 2 gloss reads + 1 tile read (+1 if under gate) + reconciliation.
