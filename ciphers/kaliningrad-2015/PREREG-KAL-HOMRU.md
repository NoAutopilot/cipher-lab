# PREREG-KAL-HOMRU (15 Oct 2026, 08:3x UTC by date -u, before any score)

Brief `.claude/briefs/runs/2026-10-15-ytbiz-default-0810-jobs.md` "KAL-HOMRU" (LANE DEFAULT-A2-0810-15, account 2).
Named next step of KAL-RUCORP (NOTES.md): the homophonic family re-run with the solver's own language model on the era-matched
ru20_lat s1s corpus (earlier Russian homophonic units annealed against ru19_lat, an 1876 Bible register).

Unit: `tools/family_run.py ciphers/kaliningrad-2015/families/kal_rucorp/spec_ru20.json --family homophonic
--cipher ciphers/kaliningrad-2015/ciphertext_signs_B.tsv --corpus tools/data/ru20_lat/s1s --param profile=target
--gate 0.9 --restarts 20` (convention B, N 1066, K 28, written order -- the N KAL-RUCORP named). Control first, built by the tool
from the same corpus at N 1066 / K 28 with the target's sign-count profile.

- Gate 0.9 on mean control recovery, never lowered (the folder's homophonic gate since GOLD-KAL1).
- Seeds and restarts: restarts 20 (GOLD-KAL4/A2-KAL method). Timing: one control seed is timed first with `--control-only
  --seeds 1` written to a scratch HYPOTHESES file (its number is reported but not used for the gate). If that seed takes
  <= 6 min, the main unit runs `--seeds 5`; if 6-10 min, `--seeds 3`; over 10 min, stop and log "untestable in this box".
  A 6th seed only for GOLD-KAL4's pattern (all seeds >= 0.9 but one collapsed under 0.5 and the mean below gate); no 7th
  (rule 3 third-attempt clause).
- Headroom (rule 3): if the control mean is >= 0.95 the family is near ceiling on the control, which is the intended state for
  a negative here (the question is whether the target reads, not whether a technique adds a gain); recorded, not a stop.
- CONTROL BELOW GATE (exit 3) is the result: target untested, not excluded.
- If the gate is met: target decode judged by the tool against the spec's ru20 corpora; then the shuffled-target decode
  (`--shuffle-target 1 --target-only-if-gated`, same seeds/restarts) through the same judge (ARM-C1). A target PASS counts only
  with the shuffle decode FAILing; a shuffle PASS voids the judge as a gate for this family at N 1066. A target FAIL below the
  ru20 held-out min (-1.156, KAL-RUCORP fold check) is a control-backed negative of the corpus change on the solver's model
  (corpus of unknown in-model reliability: fold spread 2.5-99.5%); a FAIL above -1.156 is "judge cannot decide".
- Both numbers to HYPOTHESES.md (the tool's row plus a short section). Status stays `open`; no reading claimed.
