# RESTRICTED: Adirondack History Museum scans of Debosnys's clear-text writings

Recorded 28 Sept 2026 by parent worker MAIL-3 from the museum's reply to the project mailbox (28 Sept 2026,
18:09 UTC; read in full by the owner-account orchestrator, not by this worker).

**Holder.** Adirondack History Museum (Essex County Historical Society), Elizabethtown NY.

**What they sent.** Scans of Henry Debosnys's clear-text writings, about 43 images, shared through a Google
Drive folder. The museum marked the collection **restricted**: "do not share or publish without permission ...
only use the scans for reference/research".

**Rules for this repository and every session, cloud or local (binding until the museum's written permission
says otherwise):**

1. No image, crop, thumbnail, transcription, OCR output, glyph sheet or quotation of these scans goes into this
   repository, into any artifact, second-opinion prompt, issue, email or any other public or shared place.
   The repository is public (CLAUDE.md rule 9).
2. Findings derived from the scans (a crib, a key, a reading of the cryptograms that leans on them) are
   published only after the museum's written permission. Until then they are held off-repo (a named private
   destination per CLAUDE.md rule 9a; if none exists, the worker stops and says so), and NOTES.md may say only
   that such a finding exists and is held pending permission.
3. Work on the scans is reference/research only: read from the owner's Drive or a session's scratch space,
   never committed. `ciphers/debosnys-1883/restricted/` is git-ignored for local working copies; nothing in it
   is ever force-added.
4. The scans are listed here by file name only (name, no content, no description of what each shows). The
   list is not yet filled: MAIL-3 did not open or download the folder (its brief forbade the download); the
   first job that lists the Drive folder writes the names below.

| # | file name |
|---|---|
| -- | not yet listed (MAIL-3, 28 Sept 2026) |

**Key question answered.** The museum found no key or cipher alphabet among Debosnys's papers (ASKS row 52).

## Audit, 5 Oct 2026 23:3x UTC (account-3 orchestrator, owner's request)
- tools/restricted_guard.py on every tracked file: clean (35,312 files, 47 fingerprints).
- Every file in the private repository's Debosnys material (1,138 files, incl. the 43 museum scans) hashed and
  compared byte for byte with every object in this repository's entire git history: no scan, crop or derived file
  present. The single identical object is a 49-byte empty Google Books search response, not museum material.
- No file under a `restricted/` path has ever been committed; no museum scan's file name appears anywhere in history.
- The 85 Debosnys image paths ever committed are the public cryptogram images (Debosnys-Cryptogram-*, Poem, Poem-verso,
- Both Debosnys sorter pages (artifacts PJeZjH4CR3DNKbKT1ksMRf, 3HcBvFdR7EJ17VFy8uE7sM, private) opened 5 Oct: every tile (1,315) and every context page comes from c1, c2a, c2b, c3, c4a, c4b -- the four published cryptogram images; no museum scan.
  per images/manifest.json), crops/strips/sheets cut from those (c1-c4b), and two printed cipher-key figures.
