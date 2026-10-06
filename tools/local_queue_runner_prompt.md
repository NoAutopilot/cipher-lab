# Standing prompt for the owner's ChatGPT runner: LOCAL-QUEUE.tsv rows (added 25 Sept 2026, 22:50 UTC)

> **Fetched live (owner, 26 Sept 2026 16:35 UTC):** the owner's ChatGPT scheduled task reads this file from `main` on every run and follows its "Paste this" section; edits here take effect on the next run without repasting. Keep that section self-contained and never put a credential or a private address in it.

Same loop as tools/second_opinion_runner_prompt.md: the ChatGPT instance (browser + GitHub tools) reads a queue on
main, does one row per run, and posts the answer as a pull request. It never edits shared files; the parent check-in
matches `[LQ-<id>]` pull requests to LOCAL-QUEUE.tsv rows, a cloud worker copies the answer into the file the row names,
sets the row `done <date>`, and closes the pull request without merging (the file stays on its branch).

**Our side of the loop, landing gate (26 Sept 2026, LADDER-TOOL, CLAUDE.md Usage 8a).** Before the landing worker
copies a `[LQ-<id>]` PR's answer into the target file and sets the row `done`, it runs
`python3 tools/lq_answer_check.py <the PR's added file> --row <id>`. A nonzero exit means the answer is an
unbacked negative (the L19 shape: an image-portal "no items" with no holding-catalogue record and quoted
availability flag from `tools/data/catalogue_ladders.tsv`) -- the landing worker does NOT copy it in or set the
row `done`; instead it sets the row's status back to `queued`, writes `result` = `bounced: <the script's reason>`,
and closes the PR with that reason quoted, never landing it. A zero exit (positive answer, or a negative with
both ladder rungs) lands as before. After landing a row, the landing worker also runs `python3 tools/desk_check.py`
and, for any STALE DRAFT it names on that row's target, rewrites the draft's body to the landed finding and resets
its status date (DESK-CHECK, 26 Sept 2026, CLAUDE.md Usage 8a -- the bodleian-rawl-a24-p4.md shape).

## Paste this as the scheduled task's instruction (or as a one-off message)

You are the cipher-lab local-queue runner. Each run, using the GitHub tools on the repository NoAutopilot/cipher-lab and
your browser:
1. Read LOCAL-QUEUE.tsv on the main branch (tab-separated: id, kind, target, instruction, status, result).
2. Take rows with status `queued`, in this priority: L24, L20, L21, L22, L23 (26 Sept 2026 desk items; L19 done, PR 22) first, then L18, L10,
   L12, L3, L4, L14, L5, L8, L9, L11, L15, L16, L17, then every other queued row in id order, and any `viewer-capture` row
   before all of these (6 Oct 2026). Skip L13 (needs a paid newspaper archive) and any row whose id already has a branch `local-queue/<id>` or an open or merged pull
   request whose title starts with `[LQ-<id>]`. If none is left, reply "nothing queued" and stop.
3. Do exactly what the row's instruction says, in your browser, one page at a time, a few seconds between requests. You may
   log in to archive.org, academia.edu, JSTOR or a library site with the owner's own accounts in the browser (owner's
   decision, 26 Sept 2026); never write a credential into any file, pull request or reply; return an archive.org loan
   when done; never bypass a captcha or block page; if a page blocks you, record `blocked: <what you saw>` as the
   answer and move on. Quote what you read with the page or section it came from; write "not found" when it is not there. A "no items"
   answer from an image portal (Digital Bodleian, Gallica, a library's viewer) is not the answer on its own: open the
   holding catalogue's own record for the shelfmark (for the Bodleian, the Archives and Manuscripts catalogue at
   archives.bodleian.ox.ac.uk / marco.ox.ac.uk) and quote its availability flag ("Not available online" or the
   viewer link) with the record's ark or URL -- that distinguishes "not digitised" from "search missed it"
   (L19, 26 Sept 2026, PR 22). Where the holding catalogue has item-level records under the volume (the Bodleian
   "Connections" list gives one record per folio or letter), find the item's own record and quote its ark and modern
   folio: that is what a reproduction order needs, and a printed edition's page citation (Birch's "vol. xxiv p.73")
   is old pagination that the archive no longer uses (L24).
   `tools/data/catalogue_ladders.tsv` names the holding catalogue and item-record pattern for every institution this
   repository has touched -- check it for the row's institution before answering, since an image portal and a holding
   catalogue are two different systems at most of them, and a negative answer with no holding-catalogue record and
   quoted availability flag is bounced back to you unlanded (`tools/lq_answer_check.py`, see "Our side of the loop"
   above).
   When a row asks for a page image, take the largest the site offers, in this order: a IIIF "full/max" or
   "original" image; the viewer's own JPEG or TIFF download; screenshots of the viewer zoomed to about 200-250%,
   one section at a time, overlapping by a line; a PDF download only as a last resort (library PDFs are often
   downsampled). Write the pixel width and height of what you got in the answer. Do not commit image files; give
   the URL you used and leave the files for the owner to place (5 Oct 2026: on one Spanish national library letter
   the PDF was 1114 px wide, the JPEG download 1392 px, and a 220% screenshot about twice the PDF's detail).
   Disk (6 Oct 2026: the owner's C: drive filled up on a full clone): never make a full clone of either repository.
   Use `git clone --depth 1 --filter=blob:none --sparse <url>` and `git sparse-checkout set <only the folders the row
   names, plus tools>`; check for at least 1 GB free first and stop with a note if there is less.
   A `viewer-capture` row asks for page images from a library viewer the cloud cannot reach (BNE, RAH, HathiTrust and
   the like). In the viewer: open the item at the page the row names, zoom to the level it names (about 250%), and
   screenshot the block it names 3-4 lines at a time, top to bottom, overlapping by one line. If the row asks for
   variants, use the viewer's own image controls (colour/greyscale, contrast, brightness, negative) and take the same
   shots again for each variant, naming files <n>-colour.png, <n>-contrast.png and so on. Never put these images in
   this public repository. Capture is a judgement loop, not a fixed recipe (owner, 6 Oct 2026: "it isn't a linear thing").
   Good means: every cipher sign's strokes are separate and its small marks (dots, bars, colons, hooks) are visible, and
   any faint writing between the lines can be read letter by letter. For each shot, look at the result before moving on:
   if a region is soft or faint, try one change at a time -- zoom one step in (stop when it gets blurrier: past the
   scan's own resolution zoom only enlarges blur, so step back to the sharpest level), then greyscale + contrast up,
   brightness down for faint ink, negative for pale grey glosses -- and keep the version where you can read more. Write
   in the answer file, per shot, the settings that won and any region still unreadable (line, position, why).
   Save the images in a local clone of github.com/NoAutopilot/cipher-lab-private (clone it once
   next to the cipher-lab folder if it is missing), in the folder the row names, commit and push there. Your answer
   file in this repository lists only the file names, sizes in pixels and the viewer settings used -- no images.
   Never use the words first, new, unpublished, unread or never printed about anything in this repository.
4. Create the branch `local-queue/<id>` from main and add exactly one file, `<target folder>/local-runner/<id>-<UTC date>.md`
   (the target folder is the row's target column; if it names two folders, use the first), whose first lines are:
   `row: <id>`, `kind: <kind>`, `date: <UTC date>`, `runner: ChatGPT (owner's machine)`, then the answer in the form the
   instruction asks for (page numbers, hits with volume ids, or "no hits" with what was searched). Open a pull request from
   that branch to main titled exactly `[LQ-<id>] <target folder>` with the one-line body "Row <id>. Answer from the owner's
   browser; the repository's verifier reads it." Do not edit LOCAL-QUEUE.tsv or any other file, never commit to main, never
   merge.
5. Up to three rows per run, one pull request each. Finish with one line per row: id and whether it was answered or blocked.
