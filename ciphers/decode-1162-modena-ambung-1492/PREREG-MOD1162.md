# PREREG-MOD1162 (account-2 worker, LANE-A2PUSH3), committed 3 Oct 2026 before any decode or score

Brief: `.claude/briefs/runs/2026-10-03-acct2-mod1162.md`. Test: decode-1168's sign key (`ciphers/decode-1168-modena-costabili-1492/key.tsv`,
A2-COS2, 12 C + 15 M letter signs, Costabili 20 Mar 1492) applied to R1162's cipher groups (Costabili 27 Feb 1492, same envoy).

What changed before registration (facts, no score): one DECODE login 14:21 UTC fetched the full-size images (2592x3888) and the attached
transcription document 3593 (DECODE transcriber "RP", 11 Nov 2020). That document shows R1162 is a mixed leaf, Italian in clear with
cipher groups, and a **period interlinear gloss over most groups** (e.g. "la Regina", "pocha estima", "famiglia dl arcivescovo",
"ne comprino"). So this leaf carries its own known plaintext, independent of 1168. The gloss is the gate's reference; DECODE's own
sign labels (Unicode names) are a different convention from 1168's and are NOT used for the score (rule 3, transcription convention).

## Units
Letter-level cipher groups on p.1 that sit under a period gloss, as cut in the 9 line crops (`tools/iiif_lines.py --image`, command in
NOTES.md). Single-sign dotted codes (". t .", ". f .", ". 8 .", ". 3 0 .") are nomenclator codes: excluded from statistic G,
reported separately against their gloss. Signs read in 1168's label set (key.tsv first column) by two blind Sonnet passes with no
values shown, plus one reconciliation by this worker -> `ciphertext.tsv` (conf column). Gloss letters read from the crops by the
same passes, cross-checked against DECODE's PLAINTEXT lines.

## Statistic G (gating)
Decode each group with 1168's key.tsv (`tools/decode_key.py`). Per group, letters-only, lower case, u=v, j=i, gloss abbreviations
expanded only where the gloss itself writes them in full elsewhere (none assumed). G = sum over groups of LCS(decoded, gloss) /
sum over groups of decoded signs that have a key value. (LCS = longest common subsequence; unknown signs count in neither.)

## Control (>= 500 draws; 1000 used)
Same key, values shuffled within frequency bands: band 1 = the 12 grade-C signs, band 2 = the 15 grade-M signs (C needs >= 2
agreeing occurrences in both 1168 passes, so the grades are 1168's frequency bands). 1000 seeded draws (seed 0..999), same
ciphertext, same G. The control CAN differ from the target on G: G depends on which value each sign carries.
Second named control (1168's key on a different-envoy Modena cipher): **none on disk** (grep of ciphers/ for Modena/Este/Sforza
folders on 3 Oct 2026: only 1162 and 1168), so not run.

## Gate
PASS if G_real > the 99th percentile of the 1000 control draws AND G_real >= 0.50. Otherwise FAIL (a FAIL with the control
beaten but G < 0.50 is logged as "key partly transfers", not a negative for the same-key hypothesis).

## Reported, not gating
- J: `tools/judge_plaintext.py specs/decode-1162-modena-ambung-1492.json` (language it16dip, the closest era/register corpus on disk)
  on the decoded letters, with the same score on 500 control draws. Expected under ~100 letters: judge underpowered; descriptive only.
- Coverage: share of read signs that are in key.tsv. A value shuffle cannot change coverage (CLAUDE.md rule 3, bCAS), so it is
  descriptive, not a test.
- Nomenclator codes: each dotted code vs its gloss, listed.

## Grades (rule 4)
C: token whose 1168 key grade is C AND whose value agrees with 1162's own gloss at the LCS-aligned position.
S: key-transferred token, gate PASSED, not C. M: everything else when the gate fails, or the value disagrees with the gloss.
I: none planned. H: none (no key sheet).
