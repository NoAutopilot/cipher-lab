status: blocked, waiting on you

# Access request -- Beinecke GEN MSS 109 (Spinelli Archive), the enciphered sign pool

Written 28 Sept 2026 by the campaign runner (session_01213SyYPVrRii7MWRZbyU3S, step H17). No personal data here (rule 9).

## Why

The one cipher letter online (Tommaso Spinelli to Canon Leonardo, Barcelona 7 Sept 1519, Filza 163, catalog OID
10844890) carries 259 coded signs. Every solver test on it fails its own design-matched control: a synthetic Italian
cipher of the same length, sign count and design (one hook-shaped sign family standing for several letters, about a
fifth of the tokens nulls) reads 0.12-0.20 for the repository's annealer against a 0.6 gate (HYPOTHESES.md rows of
28 Sept 2026, steps H22/H27/H30), while the same design at a projected pool of 2,000 signs read 0.706 once (N=2000,
iterations scaled) and single seeds read 0.59-0.83 from 1,000 signs up (H26; noisy, see NOTES.md). The route that
remains for a reading is length: more ciphertext in the same hand and key. The selection rule in CLAUDE.md asks for a
pool of 2,000 or more signs of one sender, office and key family.

The finding aid (`sources/archives-yale/11076_spinelli_archive_finding_aid.txt`, pp. 13 and the b. 126 entries)
names exactly that pool, none of it online (H18/H20c, 28 Sept 2026: of the 86-letter Tommaso bundle only folders
2566-70, 1492-1509, are digitised, and every one of those pages is plain):

| box, folders | what the finding aid says | date | pages |
|---|---|---|---|
| b. 126, f. 2571-87 | Spinelli, Tommaso. [the rest of his] 86 letters; Anversa, Vinegia, Bononia, Roma, Bruggia, Londra, Borsella, Mallino, Lilla, Caltray, Tornaco, Gandavio, Barchenonia, Seragosa, Villafrancha, Giranto (the run is chronological, 1492-1522; f. 2566-70 = 1492-1509 are online and plain, so f. 2571-87 hold the 1510-1522 letters) | 1510-1522, n.d. | the whole run is 254 pp.; the 1510-22 part is most of it |
| b. 126, f. 2560-65 | Spinelli, Piero. 30 letters; Anversa, Bruggia, Rignalla, Venezia. **part in cipher.** | 1514-26 | 90 pp. |

Domnina 2015 (the paper this target rests on; NOTES.md "Tomokiyo, verbatim") describes the brothers' correspondence
as enciphered from January 1515, and Kaulfersch 2025 reads her as saying Spinelli used one key throughout (H24), so
both runs are candidates for the same key as the 1519 letter. The finding aid flags "part in cipher" for Piero's
folders and for the 1519 letter only; Tommaso's 1510-22 folders are not flagged either way (the aid flags per
folder group, and the 1519 letter's own group is flagged), so the request asks for both.

## The order (free of charge, per Yale Library's own page)

Yale Library's "Request Digitization" page (https://library.yale.edu/find-request-and-use/use/using-special-collections/request-digitization,
read 28 Sept 2026) says: **"There are no charges for the services listed below"**; order limit for unbound documents
**up to 4 folders per request**; formats PDF 300 ppi or TIFF 400-600 ppi 24-bit RGB; delivery by MASV file transfer;
turnaround for documents **10-14 weeks**, no rush orders. The finding aid (p. 13) gives the alternative route: "To
order reproductions from this collection, please send an email with the call number, box number(s), and folder
number(s) to beinecke.images@yale.edu."

**Route A (the form, no cost, 4 folders per request):** in Archives at Yale, open the b. 126 folder-level records
under https://hdl.handle.net/10079/fa/beinecke.spinelliarchive (Spinelli Family Papers I > Filze > Filza 168? --
navigate to "b. 126, f. 2560-65" and "b. 126, f. 2571-87"), click Request, Continue, log in, then in Unsubmitted
Requests choose "Request Digitization", format **TIFF** (the sign shapes are the data: the atlas needs native pixels,
300 ppi PDF is a fallback), page count per folder as the aid gives it, and in Notes: "cipher research; please image
every leaf including blank versos and the address leaves". Four folders per request means about six requests for the
23 folders; place Piero's six folders first (f. 2560-65, "part in cipher", 90 pp.), then f. 2571-74, 2575-78,
2579-82, 2583-87.

**Route B (email, if the form will not take folder-level requests for this collection):** to
beinecke.images@yale.edu, quoting "GEN MSS 109, Spinelli Archive, box 126, folders 2560-2565 and 2571-2587", asking
for a quote for TIFF (or 300 ppi PDF) reproductions of every leaf, and whether the no-charge digitization service
applies. A subject line, recipient line and sign-off are left for you; the recipient address above is the one the
finding aid itself prints (28 Sept 2026).

**Preferred citation (the aid's own words):** The Spinelli Archive. General Collection, Beinecke Rare Book and
Manuscript Library.

## What happens when it arrives

The images go through the same pipeline as the 1519 letter (`tools/iiif_lines.py --image`, `glyphs/prepare.py`,
`tools/glyph_atlas.py`, Opus blind pass pairs per the H29b/H29c protocol, `passes/reconcile_opus.py`), and only
then does the design-matched control (H22's `--param merge= nulls=`) say whether the pool is long enough for the
solver route; a per-folder cipher census first tells how many signs there are. Nothing is promised about a reading.
