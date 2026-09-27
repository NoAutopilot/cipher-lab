# Armstrong–Madison continuation: printed positional rules and marked-form correction

Checkpoint UTC: 20260927T215949Z. Objective: produce a defensible, reproducible reading of Armstrong's 20 February 1808 letter while preserving source distinctions and every completed investigation.

Parent: [#52](https://github.com/NoAutopilot/cipher-lab/pull/52), immutable head `274be7e777b1abda6816ddd115d6ca9143331427`, file `ciphers/armstrong-madison-1808/checkpoints/20260927T213748Z.md`. Its parent chain preserves #51's Livingston duplicate, #50's compact THE=15 key, #49/#48's target transcription/Annet work, and #44's saved experiment results. Continue that chain; do not restart the searches.

## Completed: locate the printed instructions on the alphabetical face

The provisional THE=812 table in Monroe Papers reel 9 is not limited to numerical frames 954–955. **Frames 956–957 contain its alphabetical face, including printed instructions in the right margin.** Frame 958 is a different document, an R. M. Johnson note about land in Ohio, so it does not supply an extra cipher-key rule page or an attribution for the table.

Primary views:
- [frame 956](https://www.loc.gov/resource/mss33217.009_0001_1022/?sp=956)
- [frame 957](https://www.loc.gov/resource/mss33217.009_0001_1022/?sp=957)
- [boundary frame 958](https://www.loc.gov/resource/mss33217.009_0001_1022/?sp=958)

The native crop `[4510,1920,5020,3570]` from frame 956 supports these instructions, all **M-provisional, one reader**:

1. A printed caret-like sign beneath the last numeral digit doubles the last letter represented by that code number. Beneath the penultimate digit, it doubles the penultimate letter; beneath the antepenultimate, the corresponding third-from-last letter.
2. A small curved deletion sign beneath a digit withdraws the corresponding represented letter, using the same positional convention. Its exact glyph identity should be read from the crop, not normalized into a guessed Unicode symbol.
3. U/V and I/J are stated to be interchangeable in this key.

The two affix instructions above these rules are partially obscured. Their prose concerns noun genitive/plural, a verb's third-person singular, and past participle/imperfect forms, but the associated glyphs are not securely transcribed here. **No affix decoder or mark classifier has been implemented.** Do not fill the blurred signs from expectation.

These rules belong to **this printed THE=812 table**. They are not authenticated rules for Livingston's THE=968 witnesses, the compact THE=15 key, or Armstrong's target. Recovering a rule is not a license to apply it to a superficially similar handwritten sign. Frames 954/955 and 956/957 are overlapping views of table faces, not four independent key witnesses.

## Completed: bound the 1295 audit and correct the scope of 1583

The two existing #43 witness images, September 17 `mjm014121_p_1064.jpg` and September 18 `mjm014123_1076.jpg`, were checked as whole frames and in native quadrants. No further `1295` or annotated Talleyrand run was located. This is a bounded one-reader visual audit, **not a certified exhaustive transcription or proof of absence**. Do not repeat the same audit without a changed image/transcription or a specific new location.

The printed instructions prompted a useful audit of an existing provisional key claim. In both located “full” contexts the group **1583 is marked**:

| Witness | Source crop | Observation |
|---|---|---|
| May, within annotated powerfull | `may-control.jpg [2840,470,3300,690]` | closed angular/diamond-like shape beneath final digit 3 of 1583 |
| September 18, within annotated his full powers that he | `sep18.jpg [2750,405,3180,580]` | small loop/closed shape beneath final digit 3 of 1583 |

Therefore these two occurrences support a **marked-token reading of full**. They do not independently establish **unmarked 1583 = full**. Narrow the use of #43's provisional base entry accordingly in future derived data; this checkpoint does not edit #43 or any canonical file. A base `ful` plus a final-letter doubling operation is a plausible hypothesis, but remains unverified because neither the unmarked base nor the handwritten operator's identity has been established. The two hand-drawn shapes also must not be silently merged.

This distinction matters to any later solver: storing only integer 1583 and plaintext full discards evidence that could change the base entry. Preserve integer, mark shape, digit-relative mark position, source region, and reading confidence separately.

The #51 marked/unmarked 1295 problem remains unresolved. The newly located printed rule must not be used to “explain” it without a source-backed base and matching operator. No new Armstrong word assignment was made.

## Small correction to the parent's fixture

#52's descriptive `alignment.right_flank` says “that any good could have resulted”. The native `1038.jpg [1770,65,2480,225]` crop reads **“that any good would have resulted”**. Carry this correction forward; the twelve numerical groups, their aligned plaintext “you did make it after all those difficulties were removed”, modifier observations, and catchword handling are unchanged. This is a flank transcription correction, not a new decipherment.

## Provenance, checks, and source limitations

New primary assets:
- `key0956-full.jpg`: 3149889 bytes; 5097 × 4186; SHA-256 `c9d0a84dc629b5b5945eceeb7a7d0bd187a91e90b27969fdb16fd672bcc77a5f`.
- `key0957-full.jpg`: 2609631 bytes; 5076 × 3297; SHA-256 `fdfb76962886e13daf768eb2d4cc5917372949e8eabbd0dd1f47387031e7183c`.
- `key0958-full.jpg`: 902351 bytes; 3076 × 2514; SHA-256 `b036e417c5dc308b56c9670b33e3928a07f1c047479ee9d2099613bf72171cb2`.

LOC metadata query files:
- frame 956 JSON: SHA-256 `00b751afa620581997ad683095b626fcde2a88d7dbad34b50933548543ed3620`;
- frame 957 JSON: SHA-256 `a637b517957a6f73d7b5c499294f87c71a7b4f20d7c19b6fc6996b17ceada7f1`;
- frame 958 JSON: SHA-256 `b094c35ad0b4018cee8e93a7370cd9a2332e4b6c821a95f3ea89d5635aae03cb`.
Each query was the corresponding LOC resource URL with `?fo=json&sp=956`, 957, or 958. Image URLs came from the returned `page` entries; 958 was followed from 957's pagination. All three image downloads succeeded. No retry of protected sources or access-control workaround was used.

The old numerical face was consulted at frame 954: 17 reads magistrate and 18 navigation; THE=812 was already checked in #51. These are provisional fingerprints for identifying the table, not a proposed target decode. The complete table was not transcribed. Existing negative direct-table-transfer and weak-solver findings in HYPOTHESES.md, read at `4b75d3246f9484fc8689df3eee8626c0747dad6c`, have not been rerun or overturned.

A domain-filtered search returned the primary letter [Jefferson to Monroe, 11 May 1785](https://founders.archives.gov/documents/Jefferson/01-08-02-0096). Jefferson says he intends to complete a cipher to accompany the letter; the edition identifies the enclosure as Code No. 9. **This is an attribution lead, not proof that frames 954–957 are that enclosure.** The search service provided indexed text while reporting that direct Founders page retrieval is restricted by robots.txt. Exact follow-up searches yielded no usable new rule/control; do not keep retrying that endpoint. Earlier broad searches with an inline site qualifier produced irrelevant results; an explicit domains filter was the effective way to retrieve this indexed letter.

## Runnable recovery and verification

The capsule below includes the exact seven image hashes and URLs, the rule observations and scope restriction, the two marked 1583 observations, the negative audit boundaries, the parent-flank correction, and source lead. It reconstructs four evidence crops and eight audit quadrants after verifying every input. It writes only to a new, empty scratch output outside Git repositories. It does not fetch over the network, run a solver, classify handwriting, or claim historical accuracy.

Save the code below outside the repository as `recover_rules.py`. Download the seven assets in DATA under their specified local names, then run:

```sh
python recover_rules.py /tmp/armstrong-monroe /tmp/armstrong-rules-recovered
```

Executed successfully:
- script SHA-256 `294b028d1669f0730586a4c5034afca953ccbaaa285ffeaa45b38dba97bffba7`;
- output `evidence.json` SHA-256 `94116551477758538649d587c0eb54975905184a692e0251daa7f1c6ea9d83c7`;
- seven verified input hashes, four evidence crops, eight audit quadrants.

## State and next action

**Completed:** #52's named September-witness audit; acquisition of alphabetical frames 956–957 and boundary 958; printed positional-rule reading; marked-only scope correction for 1583; parent-flank correction; reproducible recovery.

**Running:** no background jobs; no active lease retained. The latest all-state PR scan found #52 newest, with no conflicting active lease. Closed-without-merge #49–#51 are expected landing outcomes, not failures.

**Still uncertain:** authorship/date of THE=812, identity of its affix/deletion glyphs, transferability of any rules, unmarked Livingston bases, the 1295 discrepancy, and the target key. No defensible Armstrong reading is asserted. The work is not blocked from further source investigation.

**One concrete next action:** locate the original enclosure or a separately identified copy of Code No. 9 associated with Jefferson's 11 May 1785 letter to Monroe, and compare the three fingerprints `17=magistrate`, `18=navigation`, `812=the`. Use primary LOC material and preserve exact provenance. If the table identity is established, that supplies a specific key family from which to select a dated manuscript control for the printed positional rules. Do not yet transfer the rules to Livingston or launch another blind target parameter search.

## Repository landing

Fresh branch `second-opinion/armstrong-checkpoint-20260927T215949Z` was created from then-current remote main `d36f0b70a9f3a5d257d1cce721b46ae0e8270c82`. The intended change is exactly one added file, this checkpoint. No existing repository file is edited, no protected coordination/queue file is touched, no main write/push or merge is performed. The landing worker copies this file and closes the PR without merging. Verify parent commit, exactly one ADDED file with zero deletions, and exact remote contents after publication.

## Recovery capsule

```python
import hashlib, json, sys
from pathlib import Path
from PIL import Image

DATA = json.loads(r'''{
  "grade": "M-provisional; one reader; no target decipherment or validated rule transfer.",
  "parent": {
    "pr": 52,
    "commit": "274be7e777b1abda6816ddd115d6ca9143331427"
  },
  "assets": {
    "key0956-full.jpg": {
      "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:009:0900:0956/full/pct:100/0/default.jpg",
      "sha256": "c9d0a84dc629b5b5945eceeb7a7d0bd187a91e90b27969fdb16fd672bcc77a5f"
    },
    "key0957-full.jpg": {
      "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:009:0900:0957/full/pct:100/0/default.jpg",
      "sha256": "fdfb76962886e13daf768eb2d4cc5917372949e8eabbd0dd1f47387031e7183c"
    },
    "key0958-full.jpg": {
      "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:009:0900:0958/full/pct:100/0/default.jpg",
      "sha256": "b036e417c5dc308b56c9670b33e3928a07f1c047479ee9d2099613bf72171cb2"
    },
    "sep17.jpg": {
      "url": "https://raw.githubusercontent.com/NoAutopilot/cipher-lab/67d717f734e490a238a913207bc4c79270eabcf2/ciphers/armstrong-madison-1808/pool/liv/img/mjm014121_p_1064.jpg",
      "sha256": "f0f58052aee3a561b036f8bb7339a699c074368fd99f24e5630c02f4c9d25c4f"
    },
    "sep18.jpg": {
      "url": "https://raw.githubusercontent.com/NoAutopilot/cipher-lab/67d717f734e490a238a913207bc4c79270eabcf2/ciphers/armstrong-madison-1808/pool/liv/img/mjm014123_1076.jpg",
      "sha256": "895013cae34c254d8924e07aa3f81e4f49415da53673e98c7891db21c44a9539"
    },
    "may-control.jpg": {
      "url": "https://raw.githubusercontent.com/NoAutopilot/cipher-lab/67d717f734e490a238a913207bc4c79270eabcf2/ciphers/armstrong-madison-1808/pool/liv/img/mjm014253_0303.jpg",
      "sha256": "cb390aec0ff02b7a0787a4065719842bbd6bd49835a9ec1da9cd2d2424b28a2c"
    },
    "1038.jpg": {
      "url": "https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1038.jpg",
      "sha256": "b6609cc389ce52a49675c77230e63384c36732f123b0cdd85f4cd4c3431a1dc7"
    }
  },
  "crops": {
    "printed_rules": [
      "key0956-full.jpg",
      [
        4510,
        1920,
        5020,
        3570
      ]
    ],
    "may_1583": [
      "may-control.jpg",
      [
        2840,
        470,
        3300,
        690
      ]
    ],
    "sep18_1583": [
      "sep18.jpg",
      [
        2750,
        405,
        3180,
        580
      ]
    ],
    "parent_right_flank": [
      "1038.jpg",
      [
        1770,
        65,
        2480,
        225
      ]
    ]
  },
  "source_rules": [
    {
      "id": "double",
      "sign_description": "printed caret-like sign",
      "placement": "under a numeral digit",
      "semantics": "Double the represented plaintext letter at the same ordinal position counted from the right."
    },
    {
      "id": "delete",
      "sign_description": "small curved deletion sign; use source crop, not an asserted Unicode identity",
      "placement": "under a numeral digit",
      "semantics": "Withdraw the corresponding plaintext letter, using the same positional convention."
    },
    {
      "id": "equivalences",
      "semantics": "u/v and i/j are convertible in this printed key."
    }
  ],
  "rule_scope": "The printed THE=812 key only. No assertion that Livingston's or Armstrong's marks use these rules.",
  "marked_readings": [
    {
      "n": 1583,
      "source": "may-control.jpg",
      "mark": "closed angular/diamond-like shape below final digit 3",
      "reading": "full",
      "qualification": "within annotated powerfull; retain source word-fragment context"
    },
    {
      "n": 1583,
      "source": "sep18.jpg",
      "mark": "small loop/closed shape below final digit 3",
      "reading": "full",
      "qualification": "within annotated his full powers that he"
    }
  ],
  "base_form_status": "Unmarked 1583=full not established by these two marked occurrences; ful plus a doubling operator is a hypothesis only.",
  "audit_1295": {
    "files": [
      "sep17.jpg",
      "sep18.jpg"
    ],
    "result": "No additional 1295 or annotated Talleyrand run located in whole-frame and quadrant review. Not a certified exhaustive transcription."
  },
  "parent_alignment_correction": {
    "field": "alignment.right_flank",
    "old": "that any good could have resulted",
    "new": "that any good would have resulted",
    "note": "The source crop reads would. The twelve coded groups and their plaintext span are unchanged."
  },
  "frame_boundary": {
    "numerical_views": [
      954,
      955
    ],
    "alphabetical_views": [
      956,
      957
    ],
    "next_frame": 958,
    "next_subject": "R. M. Johnson note concerning land in Ohio, not a further cipher-key page",
    "attribution": "Table authorship/date remain unconfirmed by this boundary."
  },
  "source_lead": {
    "url": "https://founders.archives.gov/documents/Jefferson/01-08-02-0096",
    "date": "1785-05-11",
    "observation": "Jefferson writes to Monroe of completing a cypher to accompany the letter. Editorial enclosure is identified as Code No. 9.",
    "limitation": "No identity established between that enclosure and THE=812; search-index text retrieved while direct page reports robots restriction."
  }
}''')

def main():
    if len(sys.argv) != 3:
        raise SystemExit("Usage: python recover_rules.py ASSET_DIR EMPTY_SCRATCH_OUTPUT")
    src, out = [Path(x).resolve() for x in sys.argv[1:]]
    if src == out or any((p/".git").exists() for p in [out, *out.parents]):
        raise SystemExit("Output must be separate scratch outside Git repositories.")
    if out.exists() and any(out.iterdir()):
        raise SystemExit("Refusing nonempty output.")
    for name, record in DATA["assets"].items():
        assert hashlib.sha256((src/name).read_bytes()).hexdigest() == record["sha256"], name
    out.mkdir(parents=True, exist_ok=True)
    for name, (filename, box) in DATA["crops"].items():
        Image.open(src/filename).crop(box).save(out/(name+".png"))
    for filename in DATA["audit_1295"]["files"]:
        im = Image.open(src/filename)
        w, h = im.size
        boxes = [(0,0,w//2,h//2), (0,h//2,w//2,h),
                 (w//2,0,w,h//2), (w//2,h//2,w,h)]
        for i, box in enumerate(boxes):
            im.crop(box).save(out/(Path(filename).stem+"-audit-"+str(i)+".png"))
    payload = json.dumps(DATA, ensure_ascii=False, indent=2) + "\n"
    (out/"evidence.json").write_text(payload, encoding="utf-8")
    print("Verified",len(DATA["assets"]),"input hashes; restored four evidence crops and eight audit quadrants.")
    print("evidence_sha256",hashlib.sha256(payload.encode()).hexdigest())
    print("No codebook search, decipherment, mark classifier, or historical accuracy test is run.")

if __name__ == "__main__":
    main()
```
