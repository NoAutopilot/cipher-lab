open

Intake (25 Sept 2026, LANE B3 worker bSSR, minimal check-solved per breadth.md's intake step):
Cipherbrain post "The Top 50 unsolved encrypted messages: 25. The SS radio message" (7 Aug 2017)
and its full 28-comment thread read in full from `sources/schmeh/posts/25-ss-radio.txt` (already
on disk); the post's own text states "The cleartext is unknown" and no commenter claims a
solution -- comments 9-27 instead argue the item is a probable forgery (wrong Fraktur-s usage,
misspelled "Lublin" on the rank stamp, mismatched unit/location, non-standard rank abbreviations,
eagle facing the wrong way; a near-identical forged item later sold on eBay, comment 28). Both
solver repositories grepped (shallow clone, `grep -ril lippert`, deleted after): dbourdeau's
`top50/NOTES.md` and `TARGETS.md` (row 25) both read "probably a forgery ... Treat as
questionable before spending anything on it", no claimed solution of any standing; no match
anywhere in aaymeloglu/unsolved-ciphers. One OpenAlex query
(`search=SS radio message Lippert cipher decrypted`) returned 0 results. One Semantic Scholar
query 429'd twice (one retry after a pause, per the good-citizen rule); not reachable this pass.

Verdict: open, unsolved by any source checked, probable forgery per Bourdeau and the post's own
comment thread (consistent with UNSOLVED-SURVEY.md row 22 and specs/ss-radio-lippert-1944.json).
No Latin-letter transcription of the ciphertext exists anywhere on disk or in either repo; cheap
test 1 (image fetch + blind transcription) is the first thing that can be run.

## Status
open

## Gate check
`python3 tools/intake_gate_check.py ss-radio-lippert-1944` -- pasted below before proceeding.

```
ss-radio-lippert-1944: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Cheap test 1 (25 Sept 2026, LANE B3 worker bSSR)

Image over transcription (rule 2): fetched the original photograph, `images/SS-Code.jpg`, from
scienceblogs.de (the only Latin-letter source is this photo -- no transcription exists in the
post text, its comment thread, or either solver repository, per the intake pass above). Single
blind pass, no subagent, read directly off 3x/5x upscaled crops of the image (`images/crop_lines.png`,
`images/crop_right.png`, `images/crop_seps2.png`, `images/crop_p4sx.png`; manifest in
`images/manifest.json`). Every letter and digit shape was checked against a close crop before
being committed to the transcription; no shape was ambiguous enough to need an M grade.

Ciphertext as transcribed (`ciphertext.txt`), one line per form line, separator kept exactly as
written:

```
MASS=QRLZ
H9/OSLY
ALAP=DETL
27163:KSSY
J1=EFLS
KOMM P4SX
```

Separator positions (character index after which the separator falls, in the concatenated
left+sep+right form): line 1 `=` after position 4 (MASS|=|QRLZ); line 2 `/` after position 2
(H9|/|OSLY); line 3 `=` after position 4 (ALAP|=|DETL); line 4 `:` after position 5
(27163|:|KSSY); line 5 `=` after position 2 (J1|=|EFLS); line 6 no separator character, only the
form's grid-cell gap (KOMM␣␣␣P4SX) -- five of six lines carry a separator, matching Schmeh's own
description in the post text. The `=` is written as a stylized cursive double-wavy stroke, not a
straight typewritten equals sign; transcribed as `=` for the ASCII file, noted here for anyone
re-checking the image.

Grade: all 45 symbols (37 letters + 8 digits) graded S (cryptanalytic transcription from the
primary image; no key or known plaintext involved) -- no H or C tokens (rule 4), consistent with
"cryptanalytic result" only.

N/K/IC (`specs/cheap-tests/ss-radio-lippert-1944/ic_test.py`, letters only, digits treated as a
separate sub-alphabet and excluded from this letter-IC test since a German-prose control is
letters-only):

- N (letters, digits excluded) = 37; N_all (letters+digits) = 45; digits = 8 (9,2,7,1,6,3,1,4),
  7 distinct digit values, from H9/27163/J1/P4SX.
- K (distinct letters) = 18: A D E F H J K L M O P Q R S T X Y Z.
- target IC (N=37) = 0.0631
- German control (tools/data/de20, 1880-1940 prose, era-matched to 1944; 5 seeds x 200 draws of
  37-letter windows) = mean 0.0725, 95% range [0.0465, 0.1066]
- uniform-random control (K=18, N=37; 5 seeds x 200 draws) = mean 0.0554, 95% range
  [0.0420, 0.0751] (flat expectation 1/K = 0.0556)
- **Target IC falls inside both 95% ranges** -- inconclusive at this N, not a control-backed
  negative either way. Expected: 37 letters split across six short code-like groups is far too
  little text for IC to discriminate German prose from a flat cipher alphabet; this is not
  evidence for or against structure, only a first look.

No language judge run (spec's judge block's `letters_min` is 20-80, a placeholder pending this
transcription -- narrower bounds and a real judge pass belong to test 2/3, not this test).

Per the brief, test 2 (comparing the form's field layout against the WW2 Wehrmacht
Spruchformular) was **not** run.

Requests: scienceblogs.de 2 (one reachability check, one image fetch; both HTTP 200 -- note for
the next holder: these two were not spaced >=2s apart, an oversight, flagged here rather than
silently passed over; no further requests to this host were made, so no retry/backoff was
triggered and no complaint or block was seen).

