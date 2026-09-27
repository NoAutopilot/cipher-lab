# Armstrong primary-source checkpoint: compact 1803 key located

Recorded UTC: 2026-09-27T21:17:26Z.
Objective: recover a defensible reading of Armstrong to Madison, 20 February 1808, by testing historically grounded mechanisms against primary evidence.

Parent: [PR #49](https://github.com/NoAutopilot/cipher-lab/pull/49), immutable head `c12e2c43736c16646216fa4c505e1308027b76eb`, checkpoint `20260927T205529Z.md`. Parallel parent incorporated: [PR #48](https://github.com/NoAutopilot/cipher-lab/pull/48), immutable head `b67f898578778f2b23f3de43acc5e38c420fbaf5`, checkpoint `20260927T205032Z.md`. Follow #49 through #47, #46, #45 and [bootstrap #44](https://github.com/NoAutopilot/cipher-lab/pull/44). Closed without merging is the expected landing workflow.

## Completed source acquisition

The end-of-1803 Monroe catalogue lead is now tied to readable manuscript images. In James Monroe Papers, Series 1, **reel 3, frames 127–128**, frame 127 contains a compact cipher key and worked example; frame 128 is its adjacent reverse/docket, including “Cyphers” and “1803 - La Treaty” (reading provisional). These sit immediately before the January 1804 letters: frame 131 is a Pinkney 1804 docket, frame 132 begins Madison's 5 January 1804 letter. The 1963 index, PDF page 27 / printed page 11, lists LIVINGSTON ROBERT R–CIPHER CODE, 1803, Series 1, two pages, KEY. The 1904 chronological catalogue places “Cipher of Robert R. Livingston” at the same chronological boundary. This alignment supports identification with the catalogued item, but does not independently authenticate authorship or date.

Primary image views:
- [Reel 3, frame 127](https://www.loc.gov/resource/mss33217.003_0001_1159/?sp=127).
- [Reel 3, frame 128](https://www.loc.gov/resource/mss33217.003_0001_1159/?sp=128).
- [1963 index](https://tile.loc.gov/storage-services/service/gdc/gdclccn/62/06/00/06/62060006/62060006.pdf).
- [1904 catalogue, printed p29](https://upload.wikimedia.org/wikipedia/commons/a/a2/Papers_of_James_Monroe_-_listed_in_chronological_order_from_the_original_manuscripts_in_the_Library_of_Congress_%28IA_papersofjamesmon00librrich%29.pdf).

The compact key has three letter alphabets with distinct marks, a short-word column, a political/person/place vocabulary column, trailing-zero permission, and explicit null numbers. It is **not the anticipated 1,700-entry WE027 table**: do not relabel it WE027 or transfer #43's entries into it. This resolves the location of one archival lead without resolving the separate Brant/WE027 gap.

## Provisional source fixture

All transcription here is **M, one reader**. The recovery capsule preserves 25 letter entries (J is not separately listed), 45 readable short-word entries, the explicit nulls, and exact source crops. It deliberately omits the smudged ON code, the over-inked FOR entry, the proper-name vocabulary and third-alphabet repetition signs.

Important readable values include:
- 15 = the, 17 = this, 71 = will, 75 = want, 48 = do.
- 24 = and, 26 = an, 234 = I, 243 = of, 282 = to, 284 = that.
- Alphabet 1: digits 1–9 correspond to a–i.
- Alphabet 2: k=2, l=4, m=1, n=6, o=7, p=5, q=8, r=9, s=3.
- Alphabet 3: t=2, u=4, v=6, w=8, x=7, y=5, z=9.
- The marked alphabet digits are not interchangeable with unmarked whole-word codes.

The source says zeroes can be appended on the right without changing the meaning. It separately lists 100, 200, …, 900 and 1000, 2000, …, 9000 as having no signification. A correct implementation must preserve the distinction between alphabet marks, whole-word entries and explicit nulls; stripping zeroes from a bare integer stream is insufficient.

The printed worked example reads **“The plan will not do.”** The capsule's answer-aware normalized sequence reproduces `theplanwillnotdo`, including 71=will, 200=null and 48=do. **This is a consistency demonstration, not an independent positive control.** The example is ink-heavy; the plaintext was used to identify ambiguous individual digits/marks. No blinded recognition accuracy is claimed. Independent positive controls: 0. Armstrong assignments: 0.

This evidence supplies a concrete historical mixed system (marked letters + word codes + nulls). It does not license another blind search over arbitrary mixed models.

## Separate undated manuscript table acquired

The LOC collection's featured undated key is [reel 9, frame 954](https://www.loc.gov/resource/mss33217.009_0001_1022/?sp=954). The full image was retrieved at 5141×4166. It is a large numbered table, distinct from frame 127 and from #43's provisional Livingston witness readings. For example, its 911 reads “ven” and 967 reads “trade”, whereas #43 gives 911=have and 967=that. These are M readings from the image, not a completed transcription or a historical identification. Do not call this the Monroe WE028 or Livingston WE027 table without a separately verified correspondence.

## Exact inputs and reproducibility

| Asset | SHA-256 |
|---|---|
| Reel 3 frame 127, full JPEG, 2891×4270 | `eafdc2d40fa44cb55bf023fec74092312c131f6e0f9348c8e97ce3e3b490489f` |
| Reel 3 frame 128, full JPEG, 4240×2735 | `d1a4df4ebee4aa6c4087b5c49597f7ce3854801dd83d29fcd1bd4c98ffb250c5` |
| Reel 9 frame 954, full JPEG | `4475fb0b5bf9d233c5cc983c8747618504e31db75f3835c55c17d20d62631636` |
| 1963 index PDF | `d8c172a37adeebd9239232339cd2f7fe968b3213eae3f364bbece20cd060db16` |
| Reel 3 metadata JSON, 1,468,675 bytes | `89bf521f0c1bc8f2eb7d63a5013abbd7545c5eeb18552e18426fe28a2f431a32` |
| Featured frame metadata JSON, 44,230 bytes | `a644ba5bdcd0ec4d60e26a9bc47d50da8d9ad73afe7bd528be092cec5df8dcc2` |

Metadata URLs: `https://www.loc.gov/item/mss33217003/?fo=json` and `https://www.loc.gov/resource/mss33217.009_0001_1022/?sp=954&fo=json`. Reel 3 metadata contains 1159 image entries in `resources[0].files`; array position is frame minus one. Full image URLs in the capsule came from these metadata, not guessed directory traversal.

Recovery code SHA-256: `e99e2b3bede6158d5b2c534ddce9fa81b61ce0e9d46ce168fa4a8a3a53c76d1d`.
Produced fixture JSON SHA-256: `2222ef94dcc3fd4bf07b69f8c89c49a7a2c208bcf8bf75b58ecd7a6955675a43`.
The capsule was run successfully against the four source assets; it produced 45 word entries, 25 letter entries, the normalized example, and five inspectable crops. Download the four assets using the exact URLs in ASSETS, naming them as the keys there, then run `python recover_primary.py INPUT_DIRECTORY NEW_OUTPUT_DIRECTORY` with Pillow installed. It refuses nonempty output or output in a detected Git worktree. No solver search or repository mutation is performed.

## Incorporated parallel work and released batch

PR #48's event ledger and uncertainty corrections stand: 366 numbers, 25 graphic contexts, preferred first 1843 rather than 1841 and preferred 200 rather than 203 while retaining alternatives. The apparent repeated 1841 equality at positions 8/253 disappears under the preferred reading. Frames 31 and 32 photograph the same leaf, so they are not independent witnesses. Its unresolved graphic marks remain unresolved. Do not overwrite its transcription with the earlier editorial baseline.

The #49 lease `armstrong-glyph-source-comparison` is **released** by its owner. Native long glyph passages and both Annet editions were visually compared; no secure literal reading was established. This was not a validated negative test of Annet. No new target aliases were accepted, and no completed solver was rerun. Primary-key acquisition became the higher-value next investigation.

## Source failures and navigation record

The ordinary LOC web reader returned 403, but a later direct shell request to the public JSON catalogue returned 200 and exposed valid image URLs. This is a newly successful public access surface, not authentication or challenge bypass. Use the documented JSON and image endpoints; do not repeat failed general reader requests.

- Guessed manifest `https://tile.loc.gov/metadata-services/iiif/manifest/ms009142.mss33217.003.json` returned 404. The metadata itself supplies a correct manifest URL; do not reuse the guess.
- Python urllib request for frame 240 returned 403; a curl request to the public asset succeeded. Prefer the successful surface.
- Thumbnail frame 126 timed out after 8192/62789 bytes; its partial file is invalid. Full frame 126 was subsequently fetched and showed a docket for Louisiana-related chronological notes, not the key. It is not an input to this fixture.
- Search-engine-1 queries were noisy and one reported founders.archives.gov robots blocking. They supplied no evidence. Do not infer absence from these failures.
- Thumbnail navigation sampled reel-3 frames 50,70,100,110,120,125,126(partial),127,128,130,131,132,135,140,150,160,170,180,185,190,200,205,210,215,220,225,230,235,240,260,280,300. Do not repeat this hunt: the key is 127–128.
- No outreach, login, or protected/paid access was attempted.

## Running, blocked, next action

Completed: key acquisition, catalogue alignment, partial fixture and reproducible source crops.
Running at this checkpoint: foreground retrieval of a potentially independent Livingston-to-Monroe witness, **11 September 1803**, described as partly in cipher with a copy in the Madison papers. No background solver exists.
Blocked/unacquired: complete WE027/Brant table, independent validation of the compact key's marked-letter rules, certified target transcription.

Active lease: `armstrong-compact-key-witness`, this foreground continuation, expires **2026-09-27T22:00:00Z**. It covers locating and comparing the 11 September 1803 witness to this compact key; other research is unleased.

**Next concrete action:** locate the LOC original of Livingston to Monroe, 11 September 1803 (the public catalogue title is reproduced at [PICRYL](https://picryl.com/media/robert-livingston-to-james-monroe-september-11-1803-part-in-cipher-and-copy-3)), read a coded span and its copy without assigning Armstrong values, and establish whether its table is the compact key, #43's official key family, or neither. PICRYL's source-link display is subscription-limited; use LOC's public catalogue/search, not hidden paid metadata. No result from this witness is claimed yet.

## Boundary and communication

Fresh branch base: current remote main `4b75d3246f9484fc8689df3eee8626c0747dad6c`. Exactly one new checkpoint file; no existing repository file edited. Never write/push main, merge, touch ROOM.md/STATUS.md/status.json/TSV queues, or change the separate queue automation. The user wants continued work and quiet checkpoints for routine inconclusive results. Notify for verified substantial progress or an actionable blocker, not another routine negative status.

## Recovery capsule

```python
#!/usr/bin/env python3
"""Recover an M-provisional source fixture; this is NOT an Armstrong solver.
Usage: python recover_primary.py INPUT_DIRECTORY NEW_OUTPUT_DIRECTORY
INPUT_DIRECTORY must contain the four hash-identified primary assets below.
No network, repository writes, or search runs are performed.
"""
import hashlib, json, pathlib, sys
from PIL import Image

ASSETS = {
 'f0127-full.jpg': {'sha256':'eafdc2d40fa44cb55bf023fec74092312c131f6e0f9348c8e97ce3e3b490489f','url':'https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0100:0127/full/pct:100/0/default.jpg'},
 'f0128-full.jpg': {'sha256':'d1a4df4ebee4aa6c4087b5c49597f7ce3854801dd83d29fcd1bd4c98ffb250c5','url':'https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0100:0128/full/pct:100/0/default.jpg'},
 'key0954-full.jpg': {'sha256':'4475fb0b5bf9d233c5cc983c8747618504e31db75f3835c55c17d20d62631636','url':'https://tile.loc.gov/image-services/iiif/service:mss:mss33217:009:0900:0954/full/pct:100/0/default.jpg'},
 'index1963.pdf': {'sha256':'d8c172a37adeebd9239232339cd2f7fe968b3213eae3f364bbece20cd060db16','url':'https://tile.loc.gov/storage-services/service/gdc/gdclccn/62/06/00/06/62060006/62060006.pdf'}
}
ALPHABETS = {
 'first_line': {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i'},
 'second_line': {2:'k',4:'l',1:'m',6:'n',7:'o',5:'p',8:'q',9:'r',3:'s'},
 'third_line': {2:'t',4:'u',6:'v',8:'w',7:'x',5:'y',9:'z'}
}
# One-reader transcription, normalized case; not all entries on the leaf.
# Smudged ON and FOR entries, proper-name list and repetition symbols excluded.
WORDS = {23:'a',24:'and',26:'an',28:'as',32:'all',34:'any',36:'but',38:'by',42:'because',43:'can',46:'could',48:'do',63:'give',64:'got',68:'have',82:'had',83:'how',84:'he',86:'in',232:'is',234:'i',236:'it',238:'know',243:'of',246:'out',248:'our',262:'so',263:'should',264:'soon',268:'some',282:'to',283:'take',284:'that',286:'they',15:'the',17:'this',19:'very',51:'us',57:'with',59:'was',71:'will',75:'want',79:'while',91:'when',97:'you'}
NULLS = [n*100 for n in range(1,10)] + [n*1000 for n in range(1,10)]
CROPS = {
 'alphabet_and_markers': [1610,60,2810,1810],
 'words_upper': [970,80,1510,2030],
 'words_lower': [970,1900,1510,4120],
 'worked_example': [1480,2780,2780,3380],
 'null_rule': [1500,2220,2780,2800]
}
# ANSWER-AWARE normalized construction, NOT a diplomatic transcription of
# the over-inked example and NOT a blinded accuracy test. The printed
# plaintext is used to identify ambiguous digits and alphabet marks.
EXAMPLE = [('word',150),('second_line',5),('second_line',4),('first_line',1),('second_line',6),('word',71),('null',200),('second_line',6),('second_line',7),('third_line',2),('word',48)]

def strip_trailing_zeroes(n):
    assert n > 0
    while n % 10 == 0: n //= 10
    return n

def example_units():
    out=[]
    for kind,n in EXAMPLE:
        if kind=='null':
            assert n in NULLS
            out.append('')
        elif kind=='word': out.append(WORDS[strip_trailing_zeroes(n)])
        else: out.append(ALPHABETS[kind][strip_trailing_zeroes(n)])
    return out

def main():
    src,out=map(lambda s:pathlib.Path(s).resolve(),sys.argv[1:])
    if any((p/'.git').exists() for p in [out,*out.parents]):
        raise SystemExit('Refusing output in a Git worktree')
    if out.exists() and any(out.iterdir()):
        raise SystemExit('Output must be new or empty')
    for name,meta in ASSETS.items():
        got=hashlib.sha256((src/name).read_bytes()).hexdigest()
        if got != meta['sha256']: raise SystemExit('Input hash mismatch: '+name)
    out.mkdir(parents=True,exist_ok=True)
    im=Image.open(src/'f0127-full.jpg')
    assert im.size==(2891,4270)
    for name,box in CROPS.items(): im.crop(box).save(out/(name+'.png'))
    fixture={'grade':'M, one reader; example answer-aware', 'assets':ASSETS,
      'alphabets':ALPHABETS,'partial_word_table':WORDS,'explicit_nulls':NULLS,
      'example_normalized_inferred_units':EXAMPLE,'example_decoded_units':example_units(),
      'example_reading_without_spaces':''.join(example_units()),
      'target_assignments':0,'independent_positive_controls':0,
      'unresolved':['Exact alphabet-mark transcription in the ink-heavy example',
        'ON code obscured; FOR entry over-inked',
        'Repetition symbols in third alphabet not implemented',
        'J treatment not stated by this fixture',
        'Catalog attribution to Livingston does not establish WE027 identity',
        'No demonstrated Armstrong relationship']}
    assert fixture['example_reading_without_spaces']=='theplanwillnotdo'
    (out/'fixture.json').write_text(json.dumps(fixture,indent=2)+'\n')
    print(json.dumps({'partial_words':len(WORDS),'letter_entries':sum(map(len,ALPHABETS.values())),
      'example':fixture['example_reading_without_spaces'],'independent_controls':0,'target_assignments':0}))

if __name__=='__main__': main()
```
