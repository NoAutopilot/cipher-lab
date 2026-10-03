# AVS-SPOT pre-registration (3 Oct 2026, worker AVS-SPOT, account 2, LANE-A2PUSH3)

Committed before any native crop of f.139 (WVO 126 p4) is looked at.

Source: https://resources.huygens.knaw.nl/media/wvo/images/00000-00999/00126.pdf page 4 (f.139), fetched once to the
scratchpad, rendered at native resolution; line crops by `tools/iiif_lines.py --image`; one vision read of the spot crops.

| spot | line | pos | current sign (conf) | value now | candidates | word context |
|---|---|---|---|---|---|---|
| S1 | 1 | 32 | L (M) | m (M, exceptions_126) | filled Λ (Lf, m) / open Λ (L, l) | `9 L Z D 1 3 L` = 'gehaimbtem'-like end "...chem"? read as m from context |
| S2 | 5 | 6 | Pf (M) | f | Pf (stemmed f-sign, f) / other sign | `1 3 Pf 9 Z Qg` = 'heftig' |
| S3 | 5 | 7 | 9 (M) | t | 9 (t) / other digit (e.g. 0 = a, 3 = e) | 'heftig' |
| S4 | 8 | 6 | Pf (M) | f | Pf (f) / other sign | `Pf Or 5 D 1 9` = 'frucht' |
| S5 | 6 | 6 | Sb (conf blank, SO-SAXONY-126 'adesn') | s | Sb (s) / Or (r) | `0 Td 3 Sb N` = 'adesn' vs expected 'adern' |

Decision rule: a spot moves (conf M -> blank, value graded C from key_98 for S1-S4; sign recoded for S5) only if the
native crop shows one candidate unambiguously AND the key value of that candidate fits the word context. If the crop
shows the other candidate unambiguously, the sign is recoded to it and graded by key_98 only if the word context then
also fits; otherwise it is recoded and left M. Anything not unambiguous stays as it is (M, or for S5 Sb with a note).
S5 specifically: Sb is kept unless the crop shows the Or shape; a clear Sb is recorded as a writer's slip (s for r),
reading 'adesn' kept as transcribed, not emended.
