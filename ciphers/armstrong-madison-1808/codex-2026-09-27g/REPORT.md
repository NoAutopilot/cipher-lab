# Armstrong continuation checkpoint — 27 September 2026

Status: open. No verified target plaintext or key assignment.

## Where Chat GPT Push stopped

The user requested recovery and continuation of the Chat GPT Push conversation on
27 September 2026. The latest completed research checkpoint retrieved from that
conversation is commit `4d0e1dba767f14c1bc9902014000b5675716004e`, committed at
17:37:42 UTC; the corresponding assistant response was at 17:38:06 UTC.

The repository contains a later ROOM entry at 17:43 UTC from **Codex ARM-KEYIMAGE**,
claiming retrieval of the Livingston key image and naming `codex-2026-09-27f`.
That folder and a completion report were absent from the fetched repository.
Conversation retrieval returned no later assistant result. This establishes a
recoverable checkpoint, **not** that the other conversation exhausted context,
stopped executing, or lost its unsaved work. Its runtime state is not visible here.

This continuation uses its own folder, `codex-2026-09-27g`, to avoid overwriting
any result the predecessor might later save. No previous source, transcription,
candidate, or result file was altered.

## Recovered work that must carry forward

| Prior report | What it establishes | Limits to preserve |
|---|---|---|
| [Numeric screens](../codex-2026-09-27/REPORT.md) | Editorial cleanup removes three prose line-count numerals; working target has 366 numeric tokens and 216 distinct values. Digit, affine and grid renumbering screens and shuffled comparisons are recorded. | No coherent reading; manuscript uncertainties and incomplete codebook coverage remain. The 15 February introduction is a proposed crib with a repetition conflict, not recovered text. |
| [Glyph inventory](../codex-2026-09-27b/REPORT.md) | Working inventory: 257 glyph tokens, 36 types, 28 fragments; letter-substitution experiments and controls saved. | Provisional M-grade inventory. Clean English controls do not establish the target's language or design. |
| [Annet and digraph pass](../codex-2026-09-27c/REPORT.md) | Historical shorthand sources and controlled letter/digraph search recorded. | Neither visual resemblance nor optimizer output licenses a key assignment; no coherent target passage. |
| [Glyph alternatives](../codex-2026-09-27d/REPORT.md) | Image-grounded alternatives and planted-error controls recorded. | Optimizer-selected label changes remain unconfirmed; original transcription retained. |
| [Private-source pass](../codex-2026-09-27e/REPORT.md) | Specific Monroe Papers key and Brooklyn private-letter leads; finite Warden correspondence group. | Neither Livingston item was imaged or linked to the target by a controlled key test. |

No solver was rerun in this continuation. Earlier search failures do not exclude
the corresponding historical cipher families.

## Archive retrieval resumed

The immediate objective remains the **Livingston cipher-code key, 1803, James
Monroe Papers, Series 1, two indexed pages**. The source report cites the 1963
index, printed p.11 / PDF p.27, and the 1904 chronological catalogue, p.29.
The latter puts the cipher after the year-only 1803 items. This makes the end of
the 1803 segment on reel 3 a reasonable location to inspect, not a resolved frame.

This continuation opened the institution's [2023 finding aid](https://tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/ms009142/ms009142.pdf)
through the web reader. **Printed p.15 / PDF page 15** lists reel 3 as
1803 Oct. 9–1807 Jan. 16 with the availability flag **“Digital content available.”**
The series is arranged chronologically. Therefore an access failure here must not
be turned into a claim that the reel is undigitized or that a copy order is needed.
The finding aid does not identify the key's frame or certify this particular
item's inclusion in the scans.

Retrieval outcomes on 27 September 2026:

| Route | Observed result | Consequence |
|---|---|---|
| LOC item `https://www.loc.gov/item/mss33217003/` through web reader | Inaccessible | No image retrieved. |
| LOC item JSON, same item with `?fo=json`, through curl | HTTP 403 | Stopped direct requests to that host. |
| LOC resource `https://www.loc.gov/resource/mss33217.003/?sp=1094` through web reader | Inaccessible | No frame inspected. The frame number came from a search result and was not a proposed key location. |
| LOC collection about page through web reader | HTTP 403 | Search index exposes a featured undated cipher-key caption, but its identity and image location remain unresolved. Do not equate it with the indexed 1803 Livingston item. |
| Public GetArchive mirror of reel 3 | Web reader returned the public page and a thumbnail link; curl returned HTTP 403 | No verified key image or exact LOC frame obtained. No subscription or access control bypass attempted. |
| Two inferred direct tile/IIIF paths for frame 1 | HTTP 404 | Both paths were guesses and are invalid. They say nothing about the presence of the reel or key. Do not reuse them as citations. |
| Internet Archive OCR for the 1893 calendar, `cu31924032751665_djvu.txt` | HTTP 502 | Full OCR not obtained. Search snippets are not a substitute for checking the printed page. |
| LOC finding-aid PDF on `tile.loc.gov` | Web reader returned text, including the reel list | Holding and reel-level availability checked as above. |

Direct shell requests: `www.loc.gov` 1, `tile.loc.gov` 2,
`loc.getarchive.net` 1, `archive.org` 1. Web searches and reader calls were also
used; these counts describe shell requests only. No loops against blocked hosts.
No actual key image was saved, transcribed, or tested.

## Exact next work

1. Open the actual reel-3 viewer or its linked IIIF manifest from the institution's
   record. Locate the 1803/1804 boundary and inspect the immediately preceding
   year-only 1803 material. Record the **observed** frame numbers and image URLs.
2. Retrieve both faces of the Livingston item, including its docket. Keep
   “two indexed pages” separate from “two pages of key entries.”
3. Transcribe a small set of unambiguous code/plaintext pairs with image locations.
   Compare them with the existing THE=972 and WE028 tables. Do not assume WE027
   identity from the name Livingston.
4. Test any materially different key against independently deciphered contemporary
   correspondence before target transfer. A claimed target passage must respect
   repeated code groups and extend into material not used to select the key.
5. If image access remains blocked, use the already recorded Brooklyn specimen
   (CBH 1974.002, Box 1, Folder 25) or the Brant Box 37 request as separate inputs;
   do not rerun an unchanged numerical/glyph family solely because the chat changed.

Existing request register: [REQUEST.md](../REQUEST.md), sections 1–3;
ASKS.md row 80 already covers the Livingston retrieval need. No duplicate request
row, outward message, purchase, or status promotion was created.

## Submission and landing

Submitted as exactly one added file on `second-opinion/armstrong-resume`, based
on remote `main` commit `d134ed2d68eede9b88308aa37aa171f0380f7e20`.
The target directory at that commit contains the five earlier report folders
through `codex-2026-09-27e`; no `codex-2026-09-27f` directory is present.

The preceding local attempt had prepared two ROOM additions, but publication to
main was rejected by automatic approval review. Those local commits and ROOM
changes are excluded from this branch. This submission follows the user's
27 September 2026 instruction: one added file, task branch, tagged pull request;
no existing-file changes, shared-register writes, queue edits, direct main push,
or merge. The receiving landing worker may copy this file and close the pull
request without merging; that is the expected workflow.

No background solver or archive retrieval job is left running by this continuation.
