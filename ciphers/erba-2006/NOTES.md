# erba-2006

open

Minimal check-solved (LANE B3 bERB, 25 Sept 2026, no `ciphers/<slug>` folder existed before this pass, so the
breadth.md intake step's minimal check-solved route was used, not `tools/intake_gate_check.py`'s edition/page
citation form -- there is no edition to cite; the source is a blog post read in full, quoted below): read
Schmeh's Cipherbrain post 24 in full (`sources/schmeh/posts/24-erba.txt`, already on disk, fetched by bSPEC2
25 Sept 2026), including its 10-comment thread. Schmeh's own text: "I don't know if police has deciphered this
message. If so, they have never published the solution. Can a reader solve it?" -- distinguishing this 2013
bible-hidden message from the OTHER, already-solved 2006 MASC-with-nulls cryptogram police broke at trial
("Police had no trouble breaking it," out of scope for this target). Shallow-cloned both solver repositories
(`git clone --depth 1`, grepped, deleted): dbourdeau/cyphersolver's `TARGETS.md` line 242 lists it as a target,
"Erba murder, 2006 | low | Blocker is sourcing: only a press photograph, no authoritative transcription" -- no
folder for it under the repo's per-target directories, i.e. no attempt or reading on file there; word-boundary
grep for `erba`/`olindo` found nothing else project-specific (broad substring hits were noise from unrelated
Latin/French corpus text, discarded). aaymeloglu/unsolved-ciphers: no hits for `erba` or `olindo` anywhere in
the repo. OpenAlex (`works?search=Erba murder cipher Olindo Romano`, keyed): 0 results. Semantic Scholar
(`paper/search?query=Erba murder cipher Olindo Romano`, keyed, one 429 then one retry after a pause per the
good-citizen rule): 0 results. Verdict: **open**, unsolved as far as any of these five sources shows; nothing
found contradicts Schmeh's own "never published" note. Per rule 10, this is a search result, not a novelty
class -- no verifier has run.

Status vocabulary (rule 5): `open`.

Intake gate output (`python3 tools/intake_gate_check.py erba-2006`):
```
erba-2006: open (line 3) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Cheap test 1 (25 Sept 2026, LANE B3 bERB)

See `specs/erba-2006.json` `cheap_test_done` for the numbers. Summary: fetched both images named in the spec
from scienceblogs.de, cut the cryptogram crop, ran one blind re-transcription from the image, and diffed it
against the community (reader 'Marc') transcription quoted in the spec. See NOTES.md section below for the
agreement figure and disagreement detail once the fetch and pass are done.
