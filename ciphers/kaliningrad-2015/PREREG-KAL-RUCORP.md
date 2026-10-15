# PREREG-KAL-RUCORP (15 Oct 2026, 05:4x UTC by date -u, before any score on the new corpus)

Brief `.claude/briefs/runs/2026-10-15-acct1-default-0447-jobs.md` "KAL-RUCORP" (LANE DEFAULT-A1-0447-15, account 1).

Corpus: `tools/data/ru20` (6 public-domain Soviet-era Russian prose sources, texts written 1914-1942, printings 1928-1957,
Internet Archive OCR; MANIFEST.tsv), scheme s1s in `tools/data/ru20_lat/s1s/` (one file per source). Built before this file; no
score of any kind has been computed on it.

1. Fold check: `python3 tools/judge_plaintext.py --holdout tools/data/ru20_lat/s1s/*.txt.gz --N 1066` (a-z fold, default
   windows). Report blended FN, per-fold rates and spread, held-out p05/p01/min. Reliability rule (CLAUDE.md rule 3, es17c/en
   paragraphs): a per-fold spread above 3x, or any fold FN above 30%, makes a FAIL/PASS against this corpus "of unknown
   reliability"; it is reported, not hidden. gaidar_rakety_1942 (about 31k letters) is a short fold: its windows overlap.
2. Re-judge (no new solve): the two existing KAL-2ST decodes, target and shuffle-1 (`families/columnar_homophonic-1-...-convB2st.txt`
   and `...-shuffle1-...-convB2st.txt`; KAL-BIG decoded nothing, CONTROL BELOW GATE) with
   `tools/judge_plaintext.py families/kal_rucorp/spec_ru20.json --file <decode>` (spec = r15_kal13/spec_s1s.json with only the
   corpora changed). Reading: a target PASS counts only with the shuffle decode FAILing (ARM-C1: a shuffle PASS voids the judge as a
   gate for this family at N 1066). A target FAIL that also sits below the held-out p01 of step 1 is a FAIL that survives the
   corpus change; a FAIL above the held-out p01 is "judge cannot decide". Both numbers are written beside the ru19_lat s1s ones
   (-1.70 / -1.65, real_p05 -0.904).
