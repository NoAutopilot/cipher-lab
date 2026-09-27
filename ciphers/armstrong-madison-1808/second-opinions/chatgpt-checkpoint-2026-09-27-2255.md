# Armstrong–Madison continuation: correct a Livingston reading and preserve bounded alignments

UTC 20260927T225504Z. Objective: a defensible, reproducible decipherment of Armstrong to Madison, 20 February 1808. This batch follows #55's concrete next action and improves the historical comparison evidence. It supplies no Armstrong plaintext.

Parent: [#55](https://github.com/NoAutopilot/cipher-lab/pull/55), immutable head `b8248af1dff3f78831a2cd0c2eab30f111f039f4`, file `ciphers/armstrong-madison-1808/checkpoints/20260927T224411Z.md`. Follow #55 through #54–44 for the complete recovery chain, source failures, saved solver results and user constraints. A fresh all-state check found #55 newest and unleased; no other worker's batch was taken.

## Completed: correct the earlier 715 candidate

**Retract #43's “715 = his” as an unsupported reading. Prefer “715 = for,” still M-provisional.** The direct evidence is the interlinear handwriting, not a guessed Armstrong sentence.

- September 17 witness, frame 1064, lower coded paragraph: after the second clear “much” annotation and the following word, the pencil above 715 reads as **for**. Native crop: `[2790,1170,3490,1290]`.
- September 18 witness, frame 1076: the annotated sequence `715 1583[mark] 648[mark] 967 913` reads **for full powers that he**, following the ordinary handwriting “he had written.” The first pencil word was previously misread as “his.” Native detail `[2745,480,3180,605]` and context `[1750,405,3180,665]` preserve the actual evidence. A 3× enlargement was also viewed; it adds no source resolution.
- March witness, frame 0205: the wider context `[2330,1530,3240,1775]` was acquired to avoid the top-edge clipping of #43's MAR-bottom crop. The pencil is faint; it does not provide secure support for the old “his” assignment. It is a supplementary comparison, not a third independently certified reading.

The September 18 phrase in #43 must therefore be read with **for**, not **his**. The visible marks still govern the actual forms “full” and “powers”; their semantics are not resolved by this correction. #53's restriction of 1583/full to the observed marked forms remains in force. Do not silently turn this into unmarked 1583 = full, a universal suffix rule, or a recovered complete WE027 key.

All observations remain one modern reader, answer-aware, M-provisional. Repeated historical occurrences are a consistency check, not independent modern replication. The previous 715/his value is retained in the capsule as explicitly superseded so recovery cannot accidentally resurrect it.

## Completed: one repeated word and one two-group alignment

LOC [mjm014121](https://www.loc.gov/item/mjm014121/) identifies the letter as **Robert R. Livingston to James Madison, 17 September 1803, partly in cipher and copy**. The recipient is Madison; do not confuse it with the separate September 11 Livingston-to-Monroe witness in #51–53. The resource has nine image entries, frames 1062–1070.

| Evidence | Provisional reading | Limit |
|---|---|---|
| 318, frame 1064, `[1920,1080,2500,1220]` | much | The pencil is above the number, between the preceding word and 849/to. |
| 318 again, frame 1064, `[2790,1170,3490,1290]` | much | Second occurrence in the same letter; not a blind control. |
| 1426 1133, frame 1064, `[2500,960,3576,1150]` | habit, as a run | No individual value or internal letter split is assigned to either group. |

The last alignment is bounded by the previously recorded 968/the and 1221/of. The selected numeric run is:

`1011 911 408 1105 1456 968 1426 1133 1221 978`

It supports the provisional span “I have not been in the habit of …,” while **1105/been remains faint**. The final 978 is not assigned plaintext. The next line's 1459 is likewise unassigned; do not promote a plausible “trusting” reading of the cross-line phrase into individual 978 or 1459 values without further evidence.

### What the copy does and does not verify

Acquired frames 1068 and 1069 from the current LOC item metadata. Frame 1068 is the preceding continuation. Frame 1069 contains the corresponding coded paragraph. The copy has the same ten selected groups in the same order, with a line break **between 1221 and 978**; frame 1064 places those two groups on the same line. The pencil decipherment is absent in the copy.

Thus the copy corroborates the **numbers, order, and changed line layout**, not the plaintext or its internal segmentation. There is no separate plain-language witness here. The complete crop is preserved at `[120,920,1550,1190]` on frame 1069. No claim of exact equality of all other groups/marks in the paragraph is made.

These observations expand the comparison fixture by one repeated single-group candidate (318/much) and one compound alignment (1426 1133/habit). They do not establish that each group always represents a whole word, that the pair is split ha/bit, or that either group cannot be a null or modified element in another context.

## Target check, deliberately limited

Extracted #48's embedded `lines.txt` programmatically from its recovery capsule, without executing the old experiments. SHA-256 of the exact recovered text: `c4ba5db4b1d7bc509b6ab531f6ba90dc9be4d06a3e62b43159c431742e0bc9b2`. Split each line after its vertical-bar label and counted decimal tokens only: **366 groups**, preserving #48's preferred 1843 and 200 readings.

None of 318, 715, 1426, 1133, 978 or 1459 occurs literally in that sequence. This is a literal overlap check, not a proof against transformed keys or homophones and not a decipherment attempt. The 715 correction changes no Armstrong assignment because none had been justified in the first place. The capsule embeds the exact lines and recomputes the count and all six empty position lists.

## Source and recovery record

Six source assets have exact URL, byte count, dimensions (images), and SHA-256 entries in DATA below. The existing three repository images were reacquired at immutable repository commit `67d717f734e490a238a913207bc4c79270eabcf2`; their hashes agree with #43. The new 1068/1069 images came from URLs explicitly supplied by the LOC item response. Frame 1064's public LOC URL is also in that response.

The capsule restores eight native crops, one 3× display of the 715 detail, the observations, selected-group correspondence, and the target overlap result. Save outside a repository as recover_livingston.py, obtain the six assets with the names in DATA, and run:

`python recover_livingston.py /scratch/input-directory /scratch/new-output-directory`

Python and Pillow are required. The script was executed successfully: all six input hashes/dimensions matched; the two selected ten-group sequences matched; eight native crops were written; the target count was 366 and every checked literal-hit list was empty. This is data-integrity verification and faithful recovery, not automatic handwriting recognition.

Access limits: the Rotunda table of contents was readable in the search tool but its item links failed to resolve; direct retrieval returned 403. No full published letter text was obtained. Founders retained its previously known robots restriction. A new request for the March item's LOC metadata timed out after 45 seconds with no bytes; no March date/recipient metadata was inferred from that failed request. Broad phrase searches returned irrelevant results and add no evidence. No access restriction was bypassed, no account was used, and no outreach was made.

```python
import hashlib, json, sys
from pathlib import Path
from PIL import Image
DATA = json.loads(r'''{"grade":"M-provisional, one modern reader; answer-aware historical control, not Armstrong plaintext","assets":[{"name":"sep17-loc.json","url":"https://www.loc.gov/item/mjm014121/?fo=json","bytes":29317,"sha256":"af4aecbcc3dd6344599f4450e2d361bee07a4c5ffc92d75b70ab7357e2044ac0"},{"name":"sep17-1064.jpg","url":"https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1064.jpg","bytes":603653,"sha256":"f0f58052aee3a561b036f8bb7339a699c074368fd99f24e5630c02f4c9d25c4f","dimensions":[3576,2377]},{"name":"sep17-1068.jpg","url":"https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1068.jpg","bytes":429670,"sha256":"a3d45129925850599651f3156fcd8cbe45bd345256f1e10b64d13a68f01e5ac2","dimensions":[3185,2059]},{"name":"sep17-1069.jpg","url":"https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1069.jpg","bytes":330770,"sha256":"8e58997a7b83cfe14a26c0321795f9cc1c7be568261ec235117df40d17523228","dimensions":[3206,2058]},{"name":"sep18-1076.jpg","url":"https://raw.githubusercontent.com/NoAutopilot/cipher-lab/67d717f734e490a238a913207bc4c79270eabcf2/ciphers/armstrong-madison-1808/pool/liv/img/mjm014123_1076.jpg","bytes":504973,"sha256":"895013cae34c254d8924e07aa3f81e4f49415da53673e98c7891db21c44a9539","dimensions":[3190,2059]},{"name":"mar-0205.jpg","url":"https://raw.githubusercontent.com/NoAutopilot/cipher-lab/67d717f734e490a238a913207bc4c79270eabcf2/ciphers/armstrong-madison-1808/pool/liv/img/mjm014224_0205.jpg","bytes":489458,"sha256":"aa24aa0f3ab5866402f0efcadd20520f1446bf182d92cfac1b04e58a62014594","dimensions":[3283,2107]}],"crops":[["habit","sep17-1064.jpg",[2500,960,3576,1150]],["much_a","sep17-1064.jpg",[1920,1080,2500,1220]],["much_b_and_for","sep17-1064.jpg",[2790,1170,3490,1290]],["a_context","sep17-1064.jpg",[1870,910,3576,1430]],["b_alignment","sep17-1069.jpg",[120,920,1550,1190]],["sep18_for_context","sep18-1076.jpg",[1750,405,3180,665]],["sep18_for_detail","sep18-1076.jpg",[2745,480,3180,605]],["mar_for_context","mar-0205.jpg",[2330,1530,3240,1775]]],"readings":{"new_single_group":{"318":"much"},"superseded_candidate":{"715":"his"},"replacement_candidate":{"715":"for"},"compound":[{"groups":[1426,1133],"word":"habit","internal_split":null}],"unassigned":[978,1459],"a_selected_line_groups":[[1011,911,408,1105,1456,968,1426,1133,1221,978]],"b_selected_line_groups":[[1011,911,408,1105,1456,968,1426,1133,1221],[978]],"faint_prior_entry":{"1105":"been"},"prior_marked_only":{"1583":"full"},"notes":"The copy corroborates digits and order, not the pencil decipherment or internal word split; modifying marks remain in the source crops."},"target_lines_sha256":"c4ba5db4b1d7bc509b6ab531f6ba90dc9be4d06a3e62b43159c431742e0bc9b2","target_lines":"p1.01|The 453 240 760 1480 @p1a 35 681 1752 1843 1314\np1.02|1840 240 @p1b 384 18 681 1340 1628 1267 1180\np1.03|76 1340 98 @p1c 388 1320 1254 64 1780\np1.04|341 1476 56 48 56 ?p1mark 200 38 @p1d 1141 1848 1541 1638\np1.05|88 1340 27 121 356 454 17 1640 1276 14 1760 1267\np1.06-07|61 45 @p1e 48 1360 18 1141\np1.08|143 436 489 17 946 496 18 36 1900 17 1 28 14\np1.09-10|@p1f\np1.11|44 176 564 387 840 671 41 431 18 640 1780\np1.12|1761 13 65 381 246 384 14 1 38 1120 1350 14\np1.13|671 48 370 751 18 1540 1320 12 1 1170 1842\np1.14|@p1g 41 1250 17 @p1h 1210\np2.01-03a|54 1631 12 78 350 1470 764 18 1801 @p2a\np2.03b|78 1364 1751 101 421 @p2b\np2.04|17 86 316 582 1017 18 @p2c 1248 1430\np2.05|1176 1164 1801 1747 672 564 481 1267 18 1\np2.06-07a|@p2d 45 147 1158 @p2e\np2.07b|48 1240 547 864 1762 11 1264 1567 ?p2edge7\np2.08|45 38 18 1741 180 150 1161 1240 1430\np2.09|1776 1830 3 1451 28 1540 1537 17 1894\np2.10|@p2f 13 230 481 @p2g\np2.11|1110 1267 84 19 41 364 17 @p2h 1480 1762 12\np2.12|1 1471 1480 22 561 17 1708 11 380 460 17 ?p2edge12\np2.13|17 1640 19 47 76 230 1540 @p2i\np2.14|1161 14 74 1461 1870 12 57 1899 3 47 1786\np2.15|2 471 29 390 1164 87 576 176 18 1480\np3.01-02a|760 @p3a 47 570 230 1254 1 @p3b\np3.02b|58 620 1307 451 576 17 680 38 36 1658\np3.03|460 365 @p3c 17 561 470 1360\np3.04-05|170 83 570 74 85 14 740 @p3d 67 780 1364\np3.06|@p3e 1170 1841 1 1161 674 701 3 61 1580 18\np3.07|170 1767 1870 5 @p3f\np3.08-09|160 240 876 1351 1107 1764 @p3g 1472 21 76 11 180 38 1641 15 1354 17\np3.10|170 658 49 967 1861 16 576 1564 12 1310\np3.11|1461 740 11 187 641 176 437 83 1451 1170 1807\np3.12-13|110 416 38 16 1208 141 @p3h\np3.14|1130 164 180 1767 162 38 161 15 580 1716 10\np3.15|27 614 641 110 1345 170 687 860 310 1900\np4.01|79 14 1160 1376 1740 18 38 764 364 1240\np4.02|1160 1401 176 671 604 4 560 38 1207 160\np4.03|380 87 768 14 870 462 47 648 140 1207 981\np4.04|?p4mark 5 760 47 38 580 170\n"}''')
src, dst = map(lambda s: Path(s).resolve(), sys.argv[1:3])
for p in (src,dst):
    assert not any((q/".git").exists() for q in (p,*p.parents)), "Use scratch outside repositories"
assert not dst.exists(), "Use a new empty output directory"
for a in DATA["assets"]:
    b=(src/a["name"]).read_bytes()
    assert len(b)==a["bytes"] and hashlib.sha256(b).hexdigest()==a["sha256"], a["name"]
    if "dimensions" in a:
        assert list(Image.open(src/a["name"]).size)==a["dimensions"]
r=DATA["readings"]
a=[v for line in r["a_selected_line_groups"] for v in line]
b=[v for line in r["b_selected_line_groups"] for v in line]
assert a==b and a[6:8]==r["compound"][0]["groups"]
lines=DATA["target_lines"]
assert hashlib.sha256(lines.encode()).hexdigest()==DATA["target_lines_sha256"]
nums=[int(w) for line in lines.splitlines() for w in line.split("|",1)[1].split() if w.isdecimal()]
assert len(nums)==366
hits={str(n):[i+1 for i,v in enumerate(nums) if v==n] for n in (318,715,1426,1133,978,1459)}
assert not any(hits.values())
dst.mkdir(parents=True)
for name,source,box in DATA["crops"]:
    im=Image.open(src/source).crop(box)
    im.save(dst/(name+".png"))
    if name=="sep18_for_detail":
        im.resize((1305,375)).save(dst/(name+"_3x.png"))
result={"evidence_grade":DATA["grade"],"readings":r,"matching_selected_groups":a,
        "target_numeric_count":len(nums),"literal_target_hits":hits,
        "caution":"This replays observations and checks arithmetic/data integrity; it does not independently read the handwriting or validate a key."}
(dst/"evidence.json").write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"verified_inputs":len(DATA["assets"]),"crops":len(DATA["crops"]),"target_count":len(nums),"literal_hits":hits}))

```

## State and next action

Completed: #55's September 17 span check; metadata identification; two manuscript copies aligned; 715/his retracted in favor of provisional for; 318/much and the unsplit habit run recorded; recovery and literal-overlap checks passed.

Running: none. Active lease: none retained. Blocked: complete Brant/Livingston key and the archival items described in #55 remain unacquired. No new user action is required for the next public-source check.

**One concrete next action:** inspect the still-unreviewed preceding frame **1063** from this same dated LOC item:
https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1063.jpg
(the metadata lists 3190×2059, 463263 bytes). Look specifically for an independently annotated occurrence of **1426, 1133, 978 or 1459** that can constrain the habit or following cross-line word without guessing a split. Record a bounded absence if none appears; do not rerun the same faint crop or repeat failed Rotunda/Founders retrieval. Keep modifying marks and source word boundaries in the evidence.

The strategic objective remains the Armstrong letter. Do not confuse improved historical controls with target progress, count answer-aware reconstructions as blind accuracy, or force a readable target from these sparse mappings. Preserve #48's target alternatives and #44's saved winning results without rerunning the failed searches. Continue useful source-grounded work; keep routine corrections and inconclusive results in checkpoints without notifying the user that it is “unsolved.”

## Append-only delivery

Fresh branch `second-opinion/armstrong-checkpoint-20260927T225504Z` was created from then-current remote main `d608ea25c4710b4244dfd06fc5d11b51f5f74b56`. The intended change is exactly one new file, `ciphers/armstrong-madison-1808/checkpoints/20260927T225504Z.md`. No existing repository file was edited. No main write/push or merge, no queue/coordination-file mutation, and no outreach occurred. Delivery checks require the commit's sole parent to equal that main SHA, exactly one ADDED file, zero deletions, and exact remote-content equality. The landing worker may copy and close unmerged. Further checkpoints must use another fresh branch from current remote main and exactly one new file; never edit this checkpoint or ROOM.md, STATUS.md, status.json or any TSV queue.
