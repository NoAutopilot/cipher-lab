# Livingston annotation witnesses: provisional partial key and word fragments

Recorded 2026-09-27T19:35:29+00:00. **Armstrong–Madison, 20 February 1808 remains undeciphered.**

This continues PR #42's historical-source work. It adds 19 explicitly provisional base readings from four existing Livingston manuscript images, with exact image hashes, crop coordinates, and three inspectable numeric spans. This is a small reconstruction aid for the Livingston comparison material, **not a recovered full WE027 table or an Armstrong key**. No repository image, transcription, coordination file, or queue was changed.

## What is supported

The interlinear writing supports repeated common-word readings such as `968` = “the”, `849` = “to”, `1221` = “of”, and `1456` = “in”. The short May passage is especially useful: `1467` appears both as the standalone “is” and as the last component of “Marbois”. Thus a word entry can also serve as part of a name in this witness. The repeated `648`/`1583` combination changes order between “powerfull/powerful” and “full powers”. These concrete examples support keeping word-fragment boundaries and inflection marks in a Livingston reconstruction.

All readings here are **M-provisional, one reader**. Repetition within or across witnesses is a consistency check, not a second independent transcription. The witnesses were already seen during exploratory work; none is a blinded holdout. In particular, the `1105` = “been” annotation is faint and remains a lower-confidence candidate. No number was assigned from a guessed Armstrong sentence, from a statistical solver's output, or from an unlocated published quotation.

The readings are base forms, not a complete decoding rule. Diamond-like marks, superscript/quote-like marks, and other small additions are visible near some groups. Their semantics are not established. The source crops, rather than the normalized integers alone, are the authoritative evidence. Do not silently discard those marks in future tests.

## Candidate readings

| Group | Base reading | Witness regions | Qualification |
|---:|---|---|---|
| 324 | my | MAY-upper, SEP17-middle | Repeated annotation in two witnesses. |
| 408 | not | SEP17-middle | In the annotated sequence I have not ... in the ... . |
| 531 | me | MAR-bottom, SEP17-middle | Clearer beside the following to in the March witness; second occurrence is fainter. |
| 648 | power | MAY-upper, SEP18-upper | Stem reading; the September occurrence carries a small mark below it and reads powers in context. |
| 715 | his | MAR-bottom, SEP18-upper | Repeated annotation. |
| 731 | friend | MAY-upper | One located annotation. |
| 849 | to | MAR-bottom, SEP17-middle, SEP17-left | Repeated annotation. |
| 911 | have | SEP17-middle | In I have not ...; distinct from 913, read he. |
| 913 | he | MAR-bottom, SEP18-upper | Repeated annotation. |
| 967 | that | SEP17-top, SEP18-upper | Repeated annotation; not derived from Armstrong. |
| 968 | the | SEP17-top, SEP17-middle, MAR-bottom, SEP18-left | Repeated annotation. |
| 1011 | I | MAR-bottom, SEP17-middle | Repeated annotation. |
| 1081 | they | SEP17-top | Two occurrences within the same passage. |
| 1105 | been | SEP17-middle | Single, faint annotation; retain as a lower-confidence candidate. |
| 1221 | of | MAR-top, SEP17-middle | Repeated annotation. |
| 1456 | in | MAR-bottom, SEP17-middle | Repeated annotation. |
| 1467 | is | MAY-upper | Appears alone and as the final component in Marbois. |
| 1583 | full | MAY-upper, SEP18-upper | May occurrence has a small diamond-like mark below it; retain the mark. |
| 1667 | and | SEP17-top, SEP17-middle | Repeated ampersand/and annotations; also consistent with the final part of Talleyrand in MAY-upper. |

`1295 934 1667` remains a **run** annotated “Talleyrand”; the repeated independent use of `1667` for “and” is consistent with its final letters. This does not license assigning internal values to `1295` and `934`. Likewise, `1523 518 1126 1467` is retained as the annotated Marbois run without forcing the first three components. The ambiguous all-group `1[0/6]75` is deliberately absent from the candidate key.

## Concrete checks

| Witness span | Literal groups | Rendering using only this candidate set |
|---|---|---|
| September 17, middle of right page | `1011 911 408 1105 1456 968 1426 1133 1221 978` | `i have not been in the [1426] [1133] of [978]` |
| September 18, first coded right-page passage | `715 1583 648 967 913` | `his full power that he` — source annotation reads powers, and the marks remain unresolved |
| May frame, upper right | `324 731 1523 518 1126 1467` | `my friend [1523] [518] [1126] is` — final is belongs inside the annotated name Marbois |

The brackets represent unresolved entries, **not missing manuscript text**. Spaces in these renderings separate code groups, not certified plaintext words. The last row demonstrates why inserting a word boundary after every code group would be wrong for this witness.

Applying the same integers to the unchanged 366-group Armstrong transcription gives only **two literal hits**, each occurring once: `967` at numeric position 285 and `648` at position 357 (positions are 1-based and exclude graphic markers). These are not proposed Armstrong readings. Such sparse overlap provides no usable transfer. It is not a formal exclusion of transformed keys, unknown homophones, different registers, or another private nomenclator.

## Reproducible witness locations

Paths are relative to `ciphers/armstrong-madison-1808`. Coordinates are `[left, top, right, bottom]` in the original image pixels; a crop is `PIL.Image.open(path).crop(box)`. The images already exist in the repository. The May frame's direction label in the earlier manifest remains unresolved here; use its image ID as the provenance anchor.

| Region | Source image | Crop box |
|---|---|---|
| MAY-upper | `pool/liv/img/mjm014253_0303.jpg` | `[1720, 380, 3300, 660]` |
| SEP17-top | `pool/liv/img/mjm014121_p_1064.jpg` | `[1830, 165, 3576, 650]` |
| SEP17-middle | `pool/liv/img/mjm014121_p_1064.jpg` | `[1870, 910, 3576, 1430]` |
| SEP17-left | `pool/liv/img/mjm014121_p_1064.jpg` | `[125, 620, 1790, 1370]` |
| MAR-top | `pool/liv/img/mjm014224_0205.jpg` | `[0, 345, 1660, 660]` |
| MAR-bottom | `pool/liv/img/mjm014224_0205.jpg` | `[1610, 1660, 3283, 2107]` |
| SEP18-upper | `pool/liv/img/mjm014123_1076.jpg` | `[1750, 405, 3180, 665]` |
| SEP18-left | `pool/liv/img/mjm014123_1076.jpg` | `[0, 30, 1690, 530]` |

For a stable online source view, use the existing image at [repository base 67d717f](https://github.com/NoAutopilot/cipher-lab/tree/67d717f734e490a238a913207bc4c79270eabcf2/ciphers/armstrong-madison-1808/pool/liv/img). The image hashes below identify the exact bytes inspected. Native crops are materially clearer than the whole-frame previews.

## Limits and continuation

The Brant reconstruction and complete Livingston key remain unacquired. These 19 observations should be checked by a second reader before becoming a canonical key. More reliable annotations can expand the partial table, while preserving uncertain groups and marks as alternatives. The original 1808 target's symbol transcription also remains provisional. This report supplies source evidence and a way to audit it; it does not certify a solution.

## Machine-readable evidence

```json
{
  "status": "Provisional one-reader observations, not a certified WE027 key and not an Armstrong decipherment.",
  "entries": [
    {
      "group": 324,
      "base_reading": "my",
      "regions": [
        "MAY-upper",
        "SEP17-middle"
      ],
      "note": "Repeated annotation in two witnesses.",
      "grade": "M-provisional"
    },
    {
      "group": 408,
      "base_reading": "not",
      "regions": [
        "SEP17-middle"
      ],
      "note": "In the annotated sequence I have not ... in the ... .",
      "grade": "M-provisional"
    },
    {
      "group": 531,
      "base_reading": "me",
      "regions": [
        "MAR-bottom",
        "SEP17-middle"
      ],
      "note": "Clearer beside the following to in the March witness; second occurrence is fainter.",
      "grade": "M-provisional"
    },
    {
      "group": 648,
      "base_reading": "power",
      "regions": [
        "MAY-upper",
        "SEP18-upper"
      ],
      "note": "Stem reading; the September occurrence carries a small mark below it and reads powers in context.",
      "grade": "M-provisional"
    },
    {
      "group": 715,
      "base_reading": "his",
      "regions": [
        "MAR-bottom",
        "SEP18-upper"
      ],
      "note": "Repeated annotation.",
      "grade": "M-provisional"
    },
    {
      "group": 731,
      "base_reading": "friend",
      "regions": [
        "MAY-upper"
      ],
      "note": "One located annotation.",
      "grade": "M-provisional"
    },
    {
      "group": 849,
      "base_reading": "to",
      "regions": [
        "MAR-bottom",
        "SEP17-middle",
        "SEP17-left"
      ],
      "note": "Repeated annotation.",
      "grade": "M-provisional"
    },
    {
      "group": 911,
      "base_reading": "have",
      "regions": [
        "SEP17-middle"
      ],
      "note": "In I have not ...; distinct from 913, read he.",
      "grade": "M-provisional"
    },
    {
      "group": 913,
      "base_reading": "he",
      "regions": [
        "MAR-bottom",
        "SEP18-upper"
      ],
      "note": "Repeated annotation.",
      "grade": "M-provisional"
    },
    {
      "group": 967,
      "base_reading": "that",
      "regions": [
        "SEP17-top",
        "SEP18-upper"
      ],
      "note": "Repeated annotation; not derived from Armstrong.",
      "grade": "M-provisional"
    },
    {
      "group": 968,
      "base_reading": "the",
      "regions": [
        "SEP17-top",
        "SEP17-middle",
        "MAR-bottom",
        "SEP18-left"
      ],
      "note": "Repeated annotation.",
      "grade": "M-provisional"
    },
    {
      "group": 1011,
      "base_reading": "I",
      "regions": [
        "MAR-bottom",
        "SEP17-middle"
      ],
      "note": "Repeated annotation.",
      "grade": "M-provisional"
    },
    {
      "group": 1081,
      "base_reading": "they",
      "regions": [
        "SEP17-top"
      ],
      "note": "Two occurrences within the same passage.",
      "grade": "M-provisional"
    },
    {
      "group": 1105,
      "base_reading": "been",
      "regions": [
        "SEP17-middle"
      ],
      "note": "Single, faint annotation; retain as a lower-confidence candidate.",
      "grade": "M-provisional"
    },
    {
      "group": 1221,
      "base_reading": "of",
      "regions": [
        "MAR-top",
        "SEP17-middle"
      ],
      "note": "Repeated annotation.",
      "grade": "M-provisional"
    },
    {
      "group": 1456,
      "base_reading": "in",
      "regions": [
        "MAR-bottom",
        "SEP17-middle"
      ],
      "note": "Repeated annotation.",
      "grade": "M-provisional"
    },
    {
      "group": 1467,
      "base_reading": "is",
      "regions": [
        "MAY-upper"
      ],
      "note": "Appears alone and as the final component in Marbois.",
      "grade": "M-provisional"
    },
    {
      "group": 1583,
      "base_reading": "full",
      "regions": [
        "MAY-upper",
        "SEP18-upper"
      ],
      "note": "May occurrence has a small diamond-like mark below it; retain the mark.",
      "grade": "M-provisional"
    },
    {
      "group": 1667,
      "base_reading": "and",
      "regions": [
        "SEP17-top",
        "SEP17-middle"
      ],
      "note": "Repeated ampersand/and annotations; also consistent with the final part of Talleyrand in MAY-upper.",
      "grade": "M-provisional"
    }
  ],
  "regions": {
    "MAY-upper": {
      "source_file": "pool/liv/img/mjm014253_0303.jpg",
      "box_xyxy": [
        1720,
        380,
        3300,
        660
      ]
    },
    "SEP17-top": {
      "source_file": "pool/liv/img/mjm014121_p_1064.jpg",
      "box_xyxy": [
        1830,
        165,
        3576,
        650
      ]
    },
    "SEP17-middle": {
      "source_file": "pool/liv/img/mjm014121_p_1064.jpg",
      "box_xyxy": [
        1870,
        910,
        3576,
        1430
      ]
    },
    "SEP17-left": {
      "source_file": "pool/liv/img/mjm014121_p_1064.jpg",
      "box_xyxy": [
        125,
        620,
        1790,
        1370
      ]
    },
    "MAR-top": {
      "source_file": "pool/liv/img/mjm014224_0205.jpg",
      "box_xyxy": [
        0,
        345,
        1660,
        660
      ]
    },
    "MAR-bottom": {
      "source_file": "pool/liv/img/mjm014224_0205.jpg",
      "box_xyxy": [
        1610,
        1660,
        3283,
        2107
      ]
    },
    "SEP18-upper": {
      "source_file": "pool/liv/img/mjm014123_1076.jpg",
      "box_xyxy": [
        1750,
        405,
        3180,
        665
      ]
    },
    "SEP18-left": {
      "source_file": "pool/liv/img/mjm014123_1076.jpg",
      "box_xyxy": [
        0,
        30,
        1690,
        530
      ]
    }
  },
  "source_sha256": {
    "mjm014121_p_1064.jpg": "f0f58052aee3a561b036f8bb7339a699c074368fd99f24e5630c02f4c9d25c4f",
    "mjm014123_1076.jpg": "895013cae34c254d8924e07aa3f81e4f49415da53673e98c7891db21c44a9539",
    "mjm014224_0205.jpg": "aa24aa0f3ab5866402f0efcadd20520f1446bf182d92cfac1b04e58a62014594",
    "mjm014253_0303.jpg": "cb390aec0ff02b7a0787a4065719842bbd6bd49835a9ec1da9cd2d2424b28a2c"
  },
  "target_sha256": "bc25f718fa59dda0ccd6e9ddad5049d370c47343550031fb3f3c7e8239db5f30",
  "spans": [
    {
      "id": "sep17-I-have",
      "region": "SEP17-middle",
      "groups": [
        1011,
        911,
        408,
        1105,
        1456,
        968,
        1426,
        1133,
        1221,
        978
      ],
      "note": "Read only the assigned groups; do not infer 1426, 1133, or 978 from the surrounding sentence.",
      "partial_render": "i have not been in the [1426] [1133] of [978]"
    },
    {
      "id": "sep18-full-powers",
      "region": "SEP18-upper",
      "groups": [
        715,
        1583,
        648,
        967,
        913
      ],
      "note": "The manuscript marks below 1583 and 648 remain part of the witness. Base readings alone do not supply the inflection rule.",
      "partial_render": "his full power that he"
    },
    {
      "id": "may-name-standalone",
      "region": "MAY-upper",
      "groups": [
        324,
        731,
        1523,
        518,
        1126,
        1467
      ],
      "note": "Annotation reads my friend Marbois, with Mar-/bois crossing a line break. Keep 1523 518 1126 unresolved rather than forcing an internal name segmentation.",
      "partial_render": "my friend [1523] [518] [1126] is"
    }
  ],
  "target_overlap": [
    {
      "group": 648,
      "base_reading": "power",
      "count": 1,
      "one_based_numeric_positions": [
        357
      ]
    },
    {
      "group": 967,
      "base_reading": "that",
      "count": 1,
      "one_based_numeric_positions": [
        285
      ]
    }
  ]
}
```

## Read-only verification

Save the following block outside the repository as `check.py`, then run `python check.py /path/to/cipher-lab /path/to/this/REPORT.md`. It checks image/input hashes, unique groups, the numeric overlap, and the three partial renderings. It does not validate paleography. It writes no files.

```python
import hashlib, json, re, sys
from pathlib import Path
repo, report = map(Path, sys.argv[1:3])
base = repo / "ciphers/armstrong-madison-1808"
data = json.loads(report.read_text().split("```json\n", 1)[1].split("\n```", 1)[0])
for name, expected in data["source_sha256"].items():
    assert hashlib.sha256((base/"pool/liv/img"/name).read_bytes()).hexdigest() == expected, name
target_path = base/"codex-2026-09-27/ciphertext_editorial_clean.txt"
assert hashlib.sha256(target_path.read_bytes()).hexdigest() == data["target_sha256"]
text = "\n".join(x for x in target_path.read_text().splitlines() if not x.startswith("#"))
target = list(map(int, re.findall(r"\b\d+\b", text)))
assert len(target) == 366
key = {e["group"]:e["base_reading"].lower() for e in data["entries"]}
assert len(key) == len(data["entries"]) == 19
assert sorted(set(target)&set(key)) == [648,967]
for row in data["target_overlap"]:
    assert row["count"] == target.count(row["group"])
    assert row["one_based_numeric_positions"] == [i+1 for i,n in enumerate(target) if n == row["group"]]
for span in data["spans"]:
    assert span["partial_render"] == " ".join(key.get(n, f"[{n}]") for n in span["groups"])
print("Hashes, 19 distinct candidates, three renderings and two literal overlaps verified.")
print("This check does not certify the handwritten readings or transfer the key to Armstrong.")
```
