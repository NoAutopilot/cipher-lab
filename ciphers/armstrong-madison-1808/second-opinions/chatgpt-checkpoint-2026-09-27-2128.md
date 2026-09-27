# Armstrong checkpoint: independent manuscript copy constrains the Livingston readings

Recorded UTC: 2026-09-27T21:28:51Z.
Objective: decipher Armstrong to Madison, 20 February 1808, while preserving reproducible evidence and uncertainty.
Parent: [PR #50](https://github.com/NoAutopilot/cipher-lab/pull/50), immutable head `0537d3352c911300008d9f13bbf5f05b771b723a`, file `ciphers/armstrong-madison-1808/checkpoints/20260927T211726Z.md`. Follow its links through #49 and parallel #48 to bootstrap #44. Expected landing remains copy-and-close without merging.

## Completed: separate Livingston-to-Monroe witness

Located the LOC original catalogue record [mjm014115](https://www.loc.gov/item/mjm014115/), **Robert Livingston to James Monroe, 11 September 1803, partly in cipher and copy**. The public JSON record `https://www.loc.gov/item/mjm014115/?fo=json` supplies ten images in resource [mjm.07_1031_1040](https://www.loc.gov/resource/mjm.07_1031_1040/). This item was not among the existing five raw Livingston witnesses in `pool/liv/manifest.tsv`.

The first version starts at frame 1031d; a separate manuscript copy beginning at 1036d explicitly says **Duplicate**. These are two physical manuscript copies of one communication, not two independent messages or two independent modern readers. Images 1032/1037 and 1033/1038 were also retrieved for comparison. The duplicate retains most cipher groups; it is not a complete decipherment.

The first coded span in 1031d and 1036d is provisionally:
`596 968 1070 1022 1221 968 1421 1645 1661 179[diamond]`.
In 1031d, the faint interlinear words at 968 / 1221 / 968 agree with #43's already-saved THE / OF / THE readings. This is a three-token, two-value out-of-document consistency check against an earlier frozen partial table, not a recognition score over the whole letter. Other words in the span were not assigned from context.

This supports a connection to #43's official Livingston witness family. It does not validate the compact frame-127 key from #50 for this correspondence. The compact key's THE=15 and OF=243 are different; the acquired primary sources must remain separate.

## A useful copy substitution, with a modifier warning

After the shared prose anchor **“that we have”**, image 1031d writes `640 1295`; image 1036d writes **“no right”** in ordinary prose. Both continue with `1356 1462 1290 1488 424 388 1678`. This gives a source-based alignment of the two-number run with the two-word phrase. Conditional individual readings 640=no and 1295=right are **M, provisional**; preserve the run as the authoritative alignment instead of treating the individual split as certified.

A comparison with #43's May source, `mjm014253_0303.jpg`, raises a concrete caution. The May annotation “Talleyrand” sits over `1295[diamond] 934 1667`. A diamond-like mark is visible below the May 1295; no comparable mark is visible below the September occurrence. Do not collapse these observations into one unqualified integer dictionary. Do not infer the diamond's meaning (capitalization, another register, reversal, inflection, etc.) without more evidence. Nor should the May run be silently “corrected” to fit the September pair.

This is the reason to retain literal marks and manuscript-copy differences. It is not a newly certified key entry, a contradiction proving a different code, or an Armstrong plaintext proposal.

## Completed: lower part of the separate undated key

Retrieved [Monroe reel 9, frame 955](https://www.loc.gov/resource/mss33217.009_0001_1022/?sp=955). It overlaps frame 954 and continues the numbered columns down through 1700. **Frame 954 alone shows the upper portion, not the entire table**; the two images together cover the numbered form. Many slots are blank, and no full table transcription has been made.

A native crop from frame 954 reads **812=the** (M). The earlier discriminants 911=ven and 967=trade remain visible. This is therefore provisionally a THE=812 table, not THE=968, THE=972, or the compact THE=15 key. Do not infer its historical identity merely from the THE number.

The 1963 Monroe index, PDF p26 / printed p10, lists “JEFFERSON THOMAS–CIPHER KEY”, undated, Series 1, two pages, “PRINTED FORM”; a separate entry is Series 2, three pages, “PREPARED FOR JM2”. PDF p20 / printed p4 cross-references diplomatic cipher keys to Jefferson and Livingston. These are useful identification leads, not proof that a particular WE designation belongs to frame 954. Frame 953 is a preceding docket for notes taken from Skipwith for Monroe and supplies no key attribution.

## Verification and recovery

All reading is M, one reader. Seven native crops and a machine-readable evidence record preserve the copy alignment, prior-table matches, mark distinction, and separate-table reading. No target numbers or glyphs were assigned. No solver, scoring model, or completed experiment was rerun.

Exact inputs:

| Asset | SHA-256 |
|---|---|
| 1031d JPEG (first version) | `e666f0cc6767112bc56ce38003651a2704f79db6f325d4a614bc1e39fc325e19` |
| 1036d JPEG (Duplicate) | `e39365c2df1d293d7a1bcecbf172fe9d49a42c14da3942f1cc322cce2cce0620` |
| 1032 JPEG | `122251a4e327ba3fa333980dc7ca846481f97d324dba08daf4b76602bde2e21b` |
| 1037 JPEG | `d1d65cb1375c7938a7e8dcd2048acbc78b1f64e844bfb55a05e2cd9590a27ae1` |
| 1033 JPEG | `d78237927c4f6da5993ae648cba311500184ddb92135ad6c3a3bc674e20dc7b7` |
| 1038 JPEG | `b6609cc389ce52a49675c77230e63384c36732f123b0cdd85f4cd4c3431a1dc7` |
| Existing May control image | `cb390aec0ff02b7a0787a4065719842bbd6bd49835a9ec1da9cd2d2424b28a2c` |
| Monroe reel 9 frame 955, full JPEG 5143×3010 | `99ef4205e9c33533ec9c7a2a3f0000a7e5a191dc7a190f143921e936c26e531e` |
| LOC item JSON for mjm014115, 30,972 bytes | `9eaa8878e5a61f9753ed3027f84154446eaf3049fa9b61fe34f2bca8d2c09409` |
| Successful LOC search JSON, 60,659 bytes | `24328b29ad88e0333f3f77e84eb5a9447b847d6b22223a6dfe924f9c5155febb` |

Frame 954 and index hashes are unchanged from #50. Native URLs for 1032, 1033, 1037, 1038 are `https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/NNNN.jpg`; these exact filenames were read from the item metadata.

Recovery code SHA-256: `23b24db4b71630ddebfb53092e552b6915a9719e47958fa893698cb37b3599ee`.
Output `evidence.json` SHA-256: `832a93a73ee2571297809538fd9b4bf006188434ad38aa68c837f345dd184257`.
The recovery program was run successfully: 7 crops, 3 prior-known token matches, one copy/prose alignment, zero Armstrong assignments. It only checks hashes and reconstructs saved source evidence; it neither solves nor downloads. Requirements: Python 3 and Pillow. Download the five ASSETS to scratch using their exact URLs, then run `python recover_witness.py INPUT_DIRECTORY NEW_OUTPUT_DIRECTORY`. Output in a detected Git worktree or a nonempty directory is refused.

## Failures and non-results to preserve

- First LOC collection-search request timed out after 6,586/60,678 bytes. Its partial JSON is invalid. A single retry succeeded; use the successful item ID and metadata instead of repeating the search.
- First frame-955 metadata request ended with curl HTTP/2 INTERNAL_ERROR. A single HTTP/1.1 retry succeeded. This was a transport retry, not bypass of a challenge or access control.
- Exact-title public web searches had poor recall, despite the item existing in LOC's catalogue. Search misses are not absence evidence.
- The previous #50 worked example remains answer-aware, with zero independent controls. The September witness did not supply a control for that compact key.
- The full WE027 and Brant Box 37 reconstruction remain unacquired. The THE=812 images do not close that gap.
- The target's preferred readings and unresolved marks in #48 remain unchanged. Source marks were not imported into Armstrong.

## Continuation state

Completed batches: compact key acquisition/fixture (#50); new witness-copy alignment and table lower image (this checkpoint).
Running jobs: none at checkpoint completion.
Active leases: **none**. The owner releases #50's `armstrong-compact-key-witness` lease. #49's glyph lease was already released in #50.
Blocked prerequisites: independent interpretation of the Livingston modifier marks; independent validation of any literal compact-key use; complete comparison key and certified target transcription.

**One concrete next action:** check additional occurrences of marked versus unmarked **1295** in the existing Livingston source images and the remaining pages of mjm014115. First distinguish a manuscript-number error or different entry from an actual modifier rule. Preserve each occurrence's crop, neighboring groups and mark. The already-retrieved 1033 and 1038 images have not been transcribed; the resource metadata provides the other four pages. Do not substitute an English-looking target guess for this source test. If those pages offer no comparable marked occurrence, record that once and select another primary-key or transcription lead rather than repeating the same lookup.

Secondary available work: identify the THE=812 table against an independently published primary-code witness before using it as a computational control; transcribe only values needed for such a control. The large table is now locatable without another reel hunt.

## Immutable boundary and communication

Base: current remote main `4b75d3246f9484fc8689df3eee8626c0747dad6c`. One ADDED checkpoint file on a fresh branch, zero deletions, PR to main. No existing repository file, ROOM.md, STATUS.md, status.json or queue was edited. No merge or push to main; no outreach. The separate Cipher Lab queue automation was not changed.

The user asked whether work was stuck and was told that source acquisition and checking were active. Routine negative results should continue to go into checkpoints quietly. Do not claim a solution, novel reading, detached process or new chat without corresponding evidence.

## Recovery capsule

```python
#!/usr/bin/env python3
"""Source-only recovery: Python 3 + Pillow, no network or repository writes.
Usage: python recover_witness.py INPUT_DIRECTORY NEW_OUTPUT_DIRECTORY
Download the exact ASSETS URLs to the corresponding filenames first.
"""
import hashlib,json,pathlib,sys
from PIL import Image
ASSETS={
 'sep11-1031.jpg': ['e666f0cc6767112bc56ce38003651a2704f79db6f325d4a614bc1e39fc325e19','https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1031d.jpg'],
 'sep11-1036.jpg': ['e39365c2df1d293d7a1bcecbf172fe9d49a42c14da3942f1cc322cce2cce0620','https://tile.loc.gov/storage-services/master/mss/mjm/07/1000/1036d.jpg'],
 'may-control.jpg': ['cb390aec0ff02b7a0787a4065719842bbd6bd49835a9ec1da9cd2d2424b28a2c','https://raw.githubusercontent.com/NoAutopilot/cipher-lab/67d717f734e490a238a913207bc4c79270eabcf2/ciphers/armstrong-madison-1808/pool/liv/img/mjm014253_0303.jpg'],
 'key0954-full.jpg': ['4475fb0b5bf9d233c5cc983c8747618504e31db75f3835c55c17d20d62631636','https://tile.loc.gov/image-services/iiif/service:mss:mss33217:009:0900:0954/full/pct:100/0/default.jpg'],
 'key0955-full.jpg': ['99ef4205e9c33533ec9c7a2a3f0000a7e5a191dc7a190f143921e936c26e531e','https://tile.loc.gov/image-services/iiif/service:mss:mss33217:009:0900:0955/full/pct:100/0/default.jpg']
}
CROPS={
 'sep11_A_top':['sep11-1031.jpg',[470,380,1640,740]],
 'sep11_B_top':['sep11-1036.jpg',[580,420,1720,830]],
 'sep11_A_bottom':['sep11-1031.jpg',[80,790,1610,1100]],
 'sep11_1295':['sep11-1031.jpg',[540,570,835,675]],
 'may_marked_name':['may-control.jpg',[1720,380,3300,660]],
 'featured_THE812':['key0954-full.jpg',[2360,70,2690,880]],
 'featured_900_column':['key0954-full.jpg',[2630,0,2945,4166]]
}
EVIDENCE={
 'grade':'M, one reader. Source comparisons, not an Armstrong reading.',
 'item':'https://www.loc.gov/item/mjm014115/',
 'message_date':'1803-09-11',
 'title':'Robert Livingston to James Monroe, September 11, 1803. Part in cipher and copy.',
 'copy_relation':'1036 explicitly says Duplicate; these are separate manuscript copies of one message, not independent communications.',
 'first_span':{'numbers':[596,968,1070,1022,1221,968,1421,1645,1661,179],
   'marks':{'10':'diamond-like mark below 179'},
   'prior_frozen_readings':{'968':'the','1221':'of'},
   'prior_matches':[{'position_1based':2,'group':968,'reading':'the'},
                   {'position_1based':5,'group':1221,'reading':'of'},
                   {'position_1based':6,'group':968,'reading':'the'}],
   'scope':'Matches to visible faint annotation only; other groups deliberately left unassigned.'},
 'copy_plaintext_substitution':{'A_numbers':[640,1295],'B_plaintext':'no right',
   'left_anchor':'that we have','right_anchor_numbers':[1356,1462,1290,1488,424,388,1678],
   'conditional_individual_readings':{'640':'no','1295':'right'},
   'caution':'Keep the two-number alignment authoritative; individual values remain provisional.'},
 'marked_1295_conflict':{'may_numbers':[1295,934,1667],
   'may_marks':{'1':'diamond-like mark below 1295'},
   'may_annotation':'Talleyrand',
   'sep11_1295_mark':'no comparable diamond visible below this occurrence',
   'interpretation':'Do not collapse the marked and unmarked 1295 observations into one dictionary entry. No meaning is assigned to the diamond.'},
 'separate_table':{'frames':[954,955],'provisional_entries':{'812':'the','911':'ven','967':'trade'},
   'coverage':'954 shows the upper portion; 955 overlaps and extends down to numbered 1700. Numerous slots are blank; full transcription has not been performed.',
   'historical_identity':'not authenticated; catalog has an undated Jefferson cipher on a printed form in Series 1, a comparison lead only.'},
 'target_assignments':0,
 'limits':['No independent second reader','No full WE027 reconstruction','No interpretation of modifier marks','No demonstrated transfer into Armstrong']
}
def main():
 src,out=map(lambda x:pathlib.Path(x).resolve(),sys.argv[1:])
 if any((p/'.git').exists() for p in [out,*out.parents]):raise SystemExit('Refusing Git worktree output')
 if out.exists() and any(out.iterdir()):raise SystemExit('Output must be new or empty')
 for name,(sha,url) in ASSETS.items():
  if hashlib.sha256((src/name).read_bytes()).hexdigest()!=sha:raise SystemExit('Hash mismatch: '+name)
 out.mkdir(parents=True,exist_ok=True)
 for name,(asset,box) in CROPS.items():Image.open(src/asset).crop(box).save(out/(name+'.png'))
 data={'assets':ASSETS,'crops':CROPS,'evidence':EVIDENCE}
 (out/'evidence.json').write_text(json.dumps(data,indent=2)+'\n')
 print(json.dumps({'crops':len(CROPS),'prior_known_token_matches':3,'copy_substitution':'640 1295 -> no right','target_assignments':0}))
if __name__=='__main__':main()
```
