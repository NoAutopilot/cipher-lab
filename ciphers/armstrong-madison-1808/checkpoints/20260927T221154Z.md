# Armstrong–Madison continuation: manuscript control of the printed doubling rule

UTC 20260927T221154Z. Objective: a defensible, reproducible reading of Armstrong to Madison, 20 February 1808. This batch validates a historical control, not the target.

Parent: [#53](https://github.com/NoAutopilot/cipher-lab/pull/53), immutable head `c90d4f635fc7014cd392ffc0577973cecdafb3f0`, file `ciphers/armstrong-madison-1808/checkpoints/20260927T215949Z.md`. Follow its parent chain through #52–44. Latest all-state PR check found #53 newest, #52 closed unmerged as expected. #53 retained no active lease; this batch was unleased.

## Completed: a dated handwritten control matches the printed table

LOC [mcc.036](https://www.loc.gov/item/mcc.036/) identifies this as James Madison to Thomas Jefferson, **23 May 1789**, partially ciphered with Jefferson's interlinear decipherment. The catalogue links it to the cipher Jefferson sent Madison on 11 May 1785. This catalogue statement concerns Madison, and must not be confused with the separate Jefferson-to-Monroe letter and Code No. 9 lead in #53.

Page 2 is available at [resource](https://www.loc.gov/resource/mcc.036/?sp=2). Its lower passage provides an actual manuscript instance of the rule transcribed from the printed THE=812 key:

| Manuscript token | Printed numerical entry | Operation |
|---|---|---|
| 1109, at end of line | sti | unchanged |
| 1598, at beginning of next line, caret beneath final 8 | l | double final letter: ll |
| 416 | more | unchanged |

The resulting phrase is **still more**, matching Jefferson's interlinear reading. The preceding manuscript group 1687 is annotated with; the numerical face also reads 1687 with. The displayed phrase spans a line break: 1598 belongs to **still**, not **more**. A preliminary reduced-image impression of 1588 was corrected by native inspection to **1598** before entering the fixture. It is not a source variant.

Native printed lookups: frame 954 gives 1109 sti and 416 more; frame 955 gives 1598 l. Frame 956's printed caret rule doubles the last letter when beneath the last digit. All exact source hashes and crops are in the recovery capsule. Other visible matches including 812/the helped locate the control, but the minimal fixture deliberately contains only the three natively checked entries above.

**Evidence grade: M-provisional, one modern reader, answer-aware.** The printed table and handwritten historical letter are distinct source objects; their agreement supports table identification and the final-letter doubling rule in this specific control. It is not an independently replicated transcription, a blind test, a numerical accuracy estimate, or validation of penultimate/antepenultimate/deletion/affix rules. Word segmentation comes from the historical interlinear, not a solver.

## Implication and limits

The control demonstrates why retaining the mark and line boundary matters: ignoring it produces “stil more.” A caret on a one-letter entry can add a repeated letter completing a word begun by the preceding code group. A space or line break between numbers is not automatically a plaintext word boundary.

This does **not** establish that Livingston's THE=968 system or Armstrong's target uses this key or operator. Keep #53's marked-only 1583/full restriction and the unverified ful-plus-doubling hypothesis separate. Do not substitute this control for the failed nomenclator/shape control gates in earlier checkpoints. No target group or graphic has been assigned new plaintext; no solver search was rerun.

## Recovery capsule

Save the following script outside the repository, obtain the named assets using the exact URLs in DATA, then run:
`python recover_madison.py /path/to/inputs /new/empty/scratch/output`.
Dependencies: Python and Pillow. It verifies all six input hashes, reconstructs six native crops, and reproduces “still more” from the manually selected key entries and observed caret. It writes only outside a Git repository. It does not download, classify glyphs, infer word boundaries, or search keys. The script was run successfully in scratch; the equality check passed.

```python
import pathlib, sys, json, hashlib
from PIL import Image
DATA = json.loads("{\"grade\":\"M-provisional; one modern reader; answer-aware primary-source lookup control, not blind accuracy\",\"inputs\":[[\"mcc036.json\",\"https://www.loc.gov/item/mcc.036/?fo=json\",\"becf3274e47f0db828c18fa4bf0be98808b1125a4eeb419665467da0bf311a36\"],[\"mcc036-1.jpg\",\"https://tile.loc.gov/image-services/iiif/service:mss:mssmcc:036:0001/full/pct:100/0/default.jpg\",\"f641724b6fb45e451a44a944a01811f6dd408fc361ce368f6515b017e72bb480\"],[\"mcc036-2.jpg\",\"https://tile.loc.gov/image-services/iiif/service:mss:mssmcc:036:0002/full/pct:100/0/default.jpg\",\"a22c12bbcc7f0072686b913abf6371d9be7480e2ac49beaead61f2545f6da2c5\"],[\"key0954-full.jpg\",\"https://tile.loc.gov/image-services/iiif/service:mss:mss33217:009:0900:0954/full/pct:100/0/default.jpg\",\"4475fb0b5bf9d233c5cc983c8747618504e31db75f3835c55c17d20d62631636\"],[\"key0955-full.jpg\",\"https://tile.loc.gov/image-services/iiif/service:mss:mss33217:009:0900:0955/full/pct:100/0/default.jpg\",\"99ef4205e9c33533ec9c7a2a3f0000a7e5a191dc7a190f143921e936c26e531e\"],[\"key0956-full.jpg\",\"https://tile.loc.gov/image-services/iiif/service:mss:mss33217:009:0900:0956/full/pct:100/0/default.jpg\",\"c9d0a84dc629b5b5945eceeb7a7d0bd187a91e90b27969fdb16fd672bcc77a5f\"]],\"crops\":[[\"mcc036-2.jpg\",[3430,3030,4490,3390],\"line-end.png\"],[\"mcc036-2.jpg\",[160,3370,940,3770],\"line-start.png\"],[\"key0954-full.jpg\",[3270,420,3580,760],\"key1109.png\"],[\"key0954-full.jpg\",[1250,0,1540,1900],\"key416.png\"],[\"key0955-full.jpg\",[4410,2370,4720,2770],\"key1598.png\"],[\"key0956-full.jpg\",[4510,1920,5020,3570],\"rules.png\"]],\"key\":{\"416\":\"more\",\"1109\":\"sti\",\"1598\":\"l\"},\"tokens\":[{\"n\":1109,\"mark\":null},{\"n\":1598,\"mark\":{\"shape\":\"caret\",\"below_digit_from_right\":1}},{\"n\":416,\"mark\":null}],\"expected\":\"still more\"}")
src, out = map(pathlib.Path, sys.argv[1:3])
out = out.resolve()
if any((p / ".git").exists() for p in (out, *out.parents)):
    raise SystemExit("Output must be outside a repository")
out.mkdir(parents=True, exist_ok=False)
for name, url, sha in DATA["inputs"]:
    b = (src / name).read_bytes()
    assert hashlib.sha256(b).hexdigest() == sha, name
for name, box, dest in DATA["crops"]:
    Image.open(src / name).crop(box).save(out / dest)
def double_from_right(s, position):
    assert 1 <= position <= len(s)
    i = len(s) - position
    return s[:i] + s[i] + s[i:]
pieces=[]
for token in DATA["tokens"]:
    s=DATA["key"][str(token["n"])]
    if token["mark"]:
        s=double_from_right(s, token["mark"]["below_digit_from_right"])
    pieces.append(s)
# Word boundary from the historical annotation, not inferred by this script.
result = "".join(pieces[:2]) + " " + pieces[2]
assert result == DATA["expected"], result
DATA["recovered"]=result
DATA["without_mark"]="sti"+"l"+" more"
(out / "control.json").write_text(json.dumps(DATA,indent=2)+"\n")
print(result)

```

## Source acquisition and failures

New catalogue JSON: 46,207 bytes. Page 1: 2,591,576 bytes, 4669 × 5688; page 2: 2,853,559 bytes, 4640 × 5705. Their exact SHA-256 values are in DATA; old key image hashes are inherited unchanged from #50–53. Page 1 contains the opening and date; page 2 contains the control.

The first page-2 image transfer ended with curl error 18 (partial transfer). One retry completed successfully; only the complete file, opened and hashed, is used. A metadata read before its transfer finished failed; the completed JSON was subsequently read successfully. These are recovered transient transfer issues, not missing evidence. No blocked Founders endpoint was retried. Pages 3–4 and the item's PDF have not been acquired.

Additional leads returned during source discovery, **not inspected or validated as target controls**:
- LOC [Jefferson memorandum on Barbary States, 1785–87, in shorthand](https://www.loc.gov/resource/mtj1.004_1009_1009/).
- [Bradford to Madison, 1 March 1773](https://founders.archives.gov/documents/Madison/01-01-02-0017): indexed editorial text discusses Weston and personal strokes. No manuscript acquired; no permission to revive the retired shape grader.
- LOC [Jefferson to Madison, 11 May 1785](https://www.loc.gov/item/mjm012540/) and [Madison to Jefferson, 3 October 1785](https://www.loc.gov/item/mjm012583/): possible provenance chain for the control key, not proof about the Armstrong key.

## Current state and exact next action

Completed: locate and hash the catalogue plus first two pages; inspect native marked span; verify three printed entries; reproduce the final-letter doubling control; preserve line-wrap semantics.
Running: none. No retained batch lease or claimed background process.
Blocked: no user action required; target-key identification remains uncertain, as do the other printed operations.
**Next action:** acquire mcc.036 page 3 from its catalogue-provided image URL and inspect for an annotated deletion or non-final-position doubling mark. Preserve a literal digit-relative observation and printed base entry before applying the operation. If absent, record a bounded audit rather than rerunning target searches. This is a narrow follow-on control, not an invitation to transcribe the entire letter blindly.

Fresh branch origin: current remote main `156afd3d954759bb84e301d88be863cf8fcf0875`. This report is the sole new file; no existing repository file was changed. Verify commit parent, one ADDED file/zero deletions, and remote byte equality before reporting completion. Landing workflow: copy and close without merging. Continue respecting all immutable user boundaries and quiet routine-result preference.
