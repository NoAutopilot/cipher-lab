# untersberg-code cheap test 1: abbreviation hypothesis

25 Sept 2026, LANE B3 worker bUNT. Spec `specs/untersberg-code.json`, `cheap_tests_in_order[0]`.

**Question.** Schmeh's own text leans toward a scribal-abbreviation reading over a substitution
cipher ("some knowledge of ancient German or Latin might be more helpful than codebreaking
skills"); before running any substitution-cipher control (test 3), check whether the
period-after-short-token structure the transcription shows is a real, non-random feature at
all, or would arise from the target's own character frequencies by chance.

**Method.** `test1_abbreviation.py` counts occurrences of the pattern "1-3 letters immediately
followed by a period" (the shape a suspension abbreviation like "S." "d." "occo." takes) in the
target's six transcribed lines (228 characters, spaces included). The control (set by the LANE
B3 orchestrator's brief) is a synthetic string of the same length, drawn i.i.d. per character
from the target's own unigram character distribution (same alphabet: letters, digits, '.', ',',
whitespace, same relative frequencies), tokenised and counted the same way, 500 trials.

**Result** (`test1_output.json`):

| | count |
|---|---|
| target | 36 |
| control mean (500 trials) | 12.0 |
| control range | 5-20 |
| target percentile in control | 100.0 |

Target is above every one of 500 control trials. The short-token+period clustering is a real
structural feature of the transcription, not an artifact of how often a period or a short
letter-run happens to occur in a string of this length and alphabet.

**What this test does and does not show.** It rules out "the periods are meaningless noise
given the letter frequencies" -- they are not. It does *not* by itself distinguish a real
16th-century Latin/German abbreviation convention from some other structured design (e.g. a
homophonic or code+mark cipher that also groups short symbol runs with a separator); no corpus
of known abbreviation conventions was on hand to test against directly (out of this brief's
disk-only, no-fetch scope), so this is a necessary-but-not-sufficient check, not a positive
identification. Per the spec's own note, the substitution-cipher control (test 3) still applies
if/when the abbreviation reading is rejected on other grounds (a Latin/German philologist's
read of the actual short forms against known suspension tables, e.g. via test 2's image fetch --
not run this pass).

**Verdict for CLAUDE.md rule 5/near-solve amendment.** This is not a reading and not a
closed-negative: it is a control-backed *positive* signal (the pattern exceeds its control) that
supports treating the target as abbreviation-shaped rather than assuming substitution outright,
but it does not itself solve or close the target. No candidate plaintext, no judge run. Per the
brief, do not run test 2 or test 3 this pass.
