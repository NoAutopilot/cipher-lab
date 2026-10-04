# LANE-NEAR4 wave 4 (4 Oct 2026, written 05:1x UTC by LANE-NEAR4, account 2 / ytbiz, session_01LRQBWNfFKjoMQfG9LHoUuz)

Common rules: the "Common to every job below" section of `.claude/briefs/runs/2026-10-04-ytbiz-near4-wave1.md`.

## N4-RDPAG -- clairambault1225-paget-1714: rule-7 re-derivation of the N4-PAG65 + N4-PAG213 + N4-PAG126 state (Opus; cap USD 2.5; box 35 min)
Same method and restrictions as A3V-RD7 / A3V-RD117P (`.claude/briefs/runs/2026-10-04-acct3-a3v-wave1.md` section A3V-RD7; prior result
`ciphers/clairambault1225-paget-1714/RD7-2026-10-04-run2.md`): read only decode.json, key.tsv, exceptions.tsv, the committed ciphertext,
the tools' --help, and the headers of the scripts the last three commits name (`align/settle7.py`, `align/gibbs_pass.py`) -- not NOTES.md or
the committed reading before your own run. Regenerate gibbs_pass (as its header says) + settle7 + decode_key on a scratch copy; diff token by
token against the committed reading (committed: H 50 S 79 M 363 I 7 U 6 of 505); report tokens compared/identical/differing by grade and
whether the difference exceeds the M count. Also list, without ruling, every token whose grade went H -> M in commits e74d7ba7, 08cfc358,
4f027dd5 (a gloss-read value demoted by a Gibbs disagreement) for the verifier. Write `RD7-2026-10-04-near4.md`; do not fix solver files.

## N4-VIV3 -- fr16104-vivonne-spain-1572: ink piece 38 and the legibility of the 8 June decipherment (Opus; cap USD 1.5; box 25 min)
N4-VIV2 (ROOM 04:58, d9939135): the clerk decipherment is fr.16105 ff.104r-108v; Gachard XXXVIII (4 June, sans dechiffrement) is likely ink
piece 38, a second copy before f.99. (1) View canvases 95-101 at 1200 px (<= 7 Gallica requests, >= 2 s apart; at most 2 vision calls) for
ink 38 and whether it is cipher. (2) One native crop of f.104r's first lines (`tools/iiif_lines.py --region`) to say whether the decipherment
is legible enough to transcribe. Write the transcription+alignment brief's facts into NOTES (canvases, line counts, legibility, Tomokiyo key
file on disk), estimate per pass. No transcription. NOTES "N4-VIV3", gaps refresh.
