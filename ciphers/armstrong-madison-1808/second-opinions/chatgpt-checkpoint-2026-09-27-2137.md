# Armstrong–Madison continuation: a manuscript plaintext/cipher alignment

UTC checkpoint: 20260927T213748Z. Objective: recover and verify the 20 February 1808 Armstrong–Madison cipher without manufacturing plaintext or losing completed work.

Parent: [checkpoint #51](https://github.com/NoAutopilot/cipher-lab/pull/51), immutable head `2abf1de5613b2248dbda2f75e8a70e851a971229`, file `ciphers/armstrong-madison-1808/checkpoints/20260927T212851Z.md`. Follow its parent chain through #50, #49/#48 and the pinned #44 continuity handoff. This is an append-only continuation, not a replacement for their recovery capsules.

## Completed in this batch

The September 11, 1803 Livingston-to-Monroe letter and its manuscript duplicate contain an additional directly aligned plaintext/cipher passage. This gives a source-grounded fixture for testing a prospective Livingston key or modifier rule. It is **not an Armstrong decipherment**, a full Livingston key, or a blinded control.

**All new readings are M-provisional and by one modern reader.** Two physical manuscript copies are different witnesses of the same letter, not two independent messages or independent modern transcriptions. The surrounding plaintext was visible when identifying the cipher span. No solver search, target key assignment, or target transcription change was made.

In image `1033.jpg`, after “is obvious from their having refused it when”, copy A writes:

> you did make it after all those difficulties were removed

Copy B, image `1038.jpg`, puts the following groups at the corresponding position, before the shared continuation “that any good could have resulted”:

```text
476 168 510 1031 1601 1675[diamond below] 976 164 1021 91
351 905[double quote-like mark above/right]
```

The `351` also appears separately at the foot of the left page as a catchword, then again at the start of the right page. The normalized run counts it once. There are 12 normalized numeral groups. Preserve the catchword event in source data so it cannot silently inflate a frequency count.

Keep this as a **whole-run alignment**. The image does not license allocating one code group to each ordinary word. For example, a model that inserts a word boundary after every group would miss the word-fragment behavior already established in #43. The diamond and quote-like marks have not been assigned meanings. Do not infer an ED or S rule merely from the end of this sentence.

Two provisional anchors can be checked against actual interlinear annotations elsewhere in this same letter:

| Group | Candidate | Source and qualification |
|---|---|---|
| 476 | you | `1034.jpg`, crop A_you; visibly annotated above the group, compatible with the aligned run's opening |
| 510 | make | `1031d.jpg`, crop A_make; annotation is faint, compatible with the aligned run's third group |

These are observational additions, not canonical key entries. The recovery code renders only these two anchors:
`you [168] make [1031] [1601] [1675] [976] [164] [1021] [91] [351] [905]`.
It deliberately does not silently assign the intervening groups from the prose answer.

## Copy differences and marked-number audit

The existing “no right” comparison from #51 remains intact. The larger native crops show copy A `640 1295` where copy B writes ordinary “no right”, followed in both by `1356 1462 1290 1488 424 388 1678`. The source pair still does not establish the internal word boundary independently. May's `1295[diamond] 934 1667` annotated Talleyrand remains a separate marked run. No meaning for the diamond was recovered.

A separate numeral discrepancy is now preserved explicitly: following `849 510` and before `1421`, copy A reads **1070**, while copy B reads **1072**. The two shapes are visible in native crops. Keep both observations; do not “repair” one from a desired plaintext. This demonstrates a concrete reason to compare copies before interpreting an apparent codebook contradiction.

Images 1033/1038 were newly inspected in this batch; 1034/1039 were newly downloaded and inspected. No additional 1295 occurrence was located in this visual review, but this is not an exhaustive machine transcription or a verified absence claim. The two remaining images in the catalogue set, 1035 and 1040, were not retrieved in this batch.

## Source identities and recovery

Catalogue: [LOC mjm014115](https://www.loc.gov/item/mjm014115/), “Robert Livingston to James Monroe, September 11, 1803. Part in cipher and copy.” Resource: [mjm.07_1031_1040](https://www.loc.gov/resource/mjm.07_1031_1040/). The item JSON and earlier images are hashed in #51.

Newly retrieved bytes:
- `1034.jpg`: 349009 bytes; 3226 × 2082; SHA-256 `bd38442123a507188bbe362f6680f92661b10cb9aeffbd985f191188bff1977b`.
- `1039.jpg`: 377397 bytes; 3266 × 2111; SHA-256 `810915992b7b427c9ff1ed8bafb6486aec14221b105fa703782ca45db62e5bb4`.

The runnable capsule below includes exact hashes and download URLs for every image it reads, native crop coordinates, the literal marked-token sequence, the catchword event, the two provisional anchors, and the copy variant. Download the six listed public image URLs to a scratch input folder using the exact local names in `assets`; then save and run the script **outside the repository**:

```sh
python recover_alignment.py /tmp/armstrong-monroe /tmp/armstrong-alignment-recovered
```

The script makes no network requests, checks every input hash before output, refuses nonempty output and any output within a Git repository, writes native crops and evidence JSON, and does not rerun any search. Verified run:
- script SHA-256: `601a0a742e4c5404e71fd13736785eabac3ad418caaa3363b10c40d3015a42b5`;
- recovered `evidence.json` SHA-256: `97b4d66a902385daac236caa01b351fa7526049d067605227e56417ce0b545d5`;
- 12 normalized groups, one counted 351, both modifier shapes retained.

These checks verify artifact integrity and the declared transcription structure. They do not certify handwriting or decode the target.

## Sources that did not advance the investigation

Fresh searches for Livingston/Monroe with 1295, 968, diamond/cypher, and the exact September 11 date produced no newly usable primary key or instruction for the marks. One returned the already known Monroe Museum numerical code, which was not reclassified as the Livingston key or downloaded again. Other results were irrelevant. No negative claim about the existence of a key follows from those searches. Both new LOC image downloads succeeded with HTTP/1.1. No outreach, login, archive request, or access-control workaround was attempted.

## Current status and exact next action

**Completed:** the new source-pair alignment, catchword handling, two provisional annotation anchors, explicit 1070/1072 copy variant, native crops, hash-checked recovery. The earlier compact THE=15 key acquisition remains in #50 and is distinct from this THE=968 witness family and the separate provisional THE=812 table. Their rules must not be mixed.

**Running:** no background jobs and no active lease retained by this batch. #51 already released the #50 witness lease. A future continuation should inspect newer checkpoint PRs in all states before choosing its batch.

**Still unresolved:** a complete authenticated Livingston/WE027 key, the semantics of the small marks, the 1295 marked/unmarked discrepancy, independently verified target graphics, and a defensible Armstrong plaintext. Existing negative search runs and weak-control findings in #44–#48 still stand; do not repeat them.

**One concrete next action:** inspect the existing September 17 and September 18 Livingston images from #43 for a second annotated occurrence of the marked Talleyrand run or unmarked 1295. Preserve the adjacent groups and mark positions. The aim is to decide whether the May/September discrepancy is a copied numeral, an alternate marked entry, or a change of key before extending a universal integer dictionary. Do not infer a modifier solely from the new “removed” ending. If no relevant occurrence is found, preserve that bounded audit once and pivot to a newly located primary rule/key rather than repeat parameter searches.

## Repository boundaries and landing record

All-state PR inspection immediately before creating this checkpoint found #51 newest; no conflicting active lease was found in the parent record. Fresh branch base is current remote main `4b75d3246f9484fc8689df3eee8626c0747dad6c`; branch `second-opinion/armstrong-checkpoint-20260927T213748Z`. The intended change is exactly this one new file, with no edits or deletions. Do not merge: the landing worker copies the checkpoint and closes its PR. Verify the commit parent, one added file/zero deletions, and byte-for-byte remote content after publication. Nothing here changes main, any existing file, ROOM.md, STATUS.md, status.json, or a TSV queue.

## Runnable recovery capsule

```python
import hashlib, json, sys
from pathlib import Path
from PIL import Image

DATA = json.loads(r'''{
  "status": "M-provisional, one modern reader. Same-letter manuscript duplicate alignment, not a blind decipherment or an Armstrong key.",
  "parent": {
    "url": "https://github.com/NoAutopilot/cipher-lab/pull/51",
    "commit": "2abf1de5613b2248dbda2f75e8a70e851a971229"
  },
  "catalogue": "https://www.loc.gov/item/mjm014115/",
  "resource": "https://www.loc.gov/resource/mjm.07_1031_1040/",
  "assets": {
    "1033.jpg": {
      "url": "https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1033.jpg",
      "sha256": "d78237927c4f6da5993ae648cba311500184ddb92135ad6c3a3bc674e20dc7b7"
    },
    "1034.jpg": {
      "url": "https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1034.jpg",
      "sha256": "bd38442123a507188bbe362f6680f92661b10cb9aeffbd985f191188bff1977b"
    },
    "1038.jpg": {
      "url": "https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1038.jpg",
      "sha256": "b6609cc389ce52a49675c77230e63384c36732f123b0cdd85f4cd4c3431a1dc7"
    },
    "1039.jpg": {
      "url": "https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1039.jpg",
      "sha256": "810915992b7b427c9ff1ed8bafb6486aec14221b105fa703782ca45db62e5bb4"
    },
    "sep11-1031.jpg": {
      "url": "https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1031d.jpg",
      "sha256": "e666f0cc6767112bc56ce38003651a2704f79db6f325d4a614bc1e39fc325e19"
    },
    "sep11-1036.jpg": {
      "url": "https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1036d.jpg",
      "sha256": "e39365c2df1d293d7a1bcecbf172fe9d49a42c14da3942f1cc322cce2cce0620"
    }
  },
  "crops": {
    "A_plain": [
      "1033.jpg",
      [
        170,
        1030,
        1550,
        1280
      ]
    ],
    "B_cipher_left": [
      "1038.jpg",
      [
        150,
        1620,
        1610,
        2040
      ]
    ],
    "B_cipher_right": [
      "1038.jpg",
      [
        1770,
        65,
        2480,
        225
      ]
    ],
    "A_make": [
      "sep11-1031.jpg",
      [
        995,
        545,
        1650,
        715
      ]
    ],
    "A_you": [
      "1034.jpg",
      [
        400,
        450,
        1050,
        590
      ]
    ],
    "A_variant_context": [
      "sep11-1031.jpg",
      [
        60,
        480,
        1610,
        920
      ]
    ],
    "B_variant_context": [
      "sep11-1036.jpg",
      [
        50,
        555,
        1700,
        1020
      ]
    ],
    "A_lower_annotations": [
      "1034.jpg",
      [
        120,
        70,
        1500,
        780
      ]
    ]
  },
  "alignment": {
    "left_flank": "is obvious from their having refused it when",
    "plaintext": "you did make it after all those difficulties were removed",
    "right_flank": "that any good could have resulted",
    "source_A": "1033.jpg",
    "source_B": "1038.jpg",
    "left_body": [
      {
        "n": 476
      },
      {
        "n": 168
      },
      {
        "n": 510
      },
      {
        "n": 1031
      },
      {
        "n": 1601
      },
      {
        "n": 1675,
        "mark": "diamond below"
      },
      {
        "n": 976
      },
      {
        "n": 164
      },
      {
        "n": 1021
      },
      {
        "n": 91
      }
    ],
    "left_catchword": {
      "n": 351,
      "role": "catchword; repeated in right body, not counted twice"
    },
    "right_body": [
      {
        "n": 351
      },
      {
        "n": 905,
        "mark": "double quote-like mark above/right"
      }
    ],
    "normalized_groups": [
      476,
      168,
      510,
      1031,
      1601,
      1675,
      976,
      164,
      1021,
      91,
      351,
      905
    ],
    "segmentation": "Keep as whole run; internal word boundaries and mark semantics are not certified."
  },
  "provisional_anchors": [
    {
      "n": 476,
      "reading": "you",
      "source": "1034.jpg",
      "crop": "A_you",
      "note": "Interlinear annotation; compatible with duplicate-aligned prefix."
    },
    {
      "n": 510,
      "reading": "make",
      "source": "sep11-1031.jpg",
      "crop": "A_make",
      "note": "Faint interlinear annotation; compatible with duplicate-aligned prefix."
    }
  ],
  "copy_variant": {
    "preceding": 510,
    "following": 1421,
    "source_A": {
      "file": "sep11-1031.jpg",
      "n": 1070
    },
    "source_B": {
      "file": "sep11-1036.jpg",
      "n": 1072
    },
    "rule": "Preserve both readings; do not silently choose a key assignment or assume the numeral difference is cryptographic."
  },
  "not_inferred": [
    "meaning of diamond",
    "meaning of double quote-like mark",
    "numeric-to-word segmentation of the whole run",
    "1295 base meaning",
    "Armstrong plaintext"
  ]
}''')

def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python recover_alignment.py ASSET_DIR EMPTY_SCRATCH_OUTPUT")
    src, out = [Path(x).resolve() for x in sys.argv[1:]]
    if src == out or any((p / ".git").exists() for p in [out, *out.parents]):
        raise SystemExit("Output must be separate scratch, outside every Git repository.")
    if out.exists() and any(out.iterdir()):
        raise SystemExit("Refusing nonempty output.")
    for name, row in DATA["assets"].items():
        assert hashlib.sha256((src/name).read_bytes()).hexdigest() == row["sha256"], name
    a = DATA["alignment"]
    groups = [x["n"] for x in a["left_body"] + a["right_body"]]
    assert groups == a["normalized_groups"] and len(groups) == 12
    assert a["left_catchword"]["n"] == a["right_body"][0]["n"] == 351
    assert groups.count(351) == 1
    assert a["left_body"][5]["mark"] == "diamond below"
    assert a["right_body"][1]["mark"] == "double quote-like mark above/right"
    assert DATA["copy_variant"]["source_A"]["n"] == 1070
    assert DATA["copy_variant"]["source_B"]["n"] == 1072
    out.mkdir(parents=True, exist_ok=True)
    for name, (filename, box) in DATA["crops"].items():
        Image.open(src/filename).crop(box).save(out/(name + ".png"))
    payload = json.dumps(DATA, indent=2, ensure_ascii=False) + "\n"
    (out/"evidence.json").write_text(payload, encoding="utf-8")
    anchors = {x["n"]: x["reading"] for x in DATA["provisional_anchors"]}
    print("12 numeral groups; 351 catchword counted once; two modifier shapes preserved.")
    print("Partial rendering:", " ".join(anchors.get(n, "["+str(n)+"]") for n in groups))
    print("evidence_sha256", hashlib.sha256(payload.encode()).hexdigest())
    print("Checks cover recovery integrity, not paleography, independent validation, or target transfer.")

if __name__ == "__main__":
    main()
```
