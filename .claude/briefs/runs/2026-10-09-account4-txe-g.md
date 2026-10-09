# TXE-G: what document-recovery teams do (LANE TX-ENGINEER, idea O5; account 4, Opus 5.5; cap 6, box 75 min; WebSearch allowed, no other host)

Read `.claude/briefs/runs/2026-10-09-account4-txe-COMMON.md` first, then research/TX-TAXONOMY-2026-10-09.md and
research/TX-IDEAS-2026-10-09.md row O5. Why this job exists: the owner asked (lane brief Amendment 1, item 5) what expert
document-recovery teams do with a damaged or faint page, so the lane tests their methods rather than reinventing them.
Our material: RGB JPEG scans from Gallica at native resolution (about 40 px a sign), iron-gall ink on paper, some bleed-through,
no multispectral capture possible; the readers are vision models that see a crop or a tile; the errors are the taxonomy's
three classes (look-alike pairs, crop geometry, thin strokes).

## Do
1. A literature pass (WebSearch, standard mode first; 20-40 queries, each logged with date and the page it found) across:
   forensic document examination practice (faded-ink recovery on RGB scans); digital palaeography and document image analysis
   (binarisation families: Otsu, Niblack, Sauvola, Wolf, Howe, DIBCO winners; bleed-through removal; pseudo-multispectral and
   channel-separation tricks on RGB; stroke-width normalisation; super-resolution for text; dewarping/deskew); HTR pipelines
   (Transkribus, eScriptorium/Kraken, PyLaia) and what their preprocessing does; ICDAR/ICFHR competition methods for
   historical handwriting; and anything specific to cipher-sign or symbol transcription (Cryptologia, DECRYPT/DECODE project
   papers on image-to-sign transcription, Lasry-Biermann-Tomokiyo 2023 on Mary Stuart's transcription practice).
2. Write `research/TX-RECOVERY-PRACTICE-2026-10-09.md`: (a) a table of methods found (method, what it fixes, evidence cited,
   runnable here on an RGB scan with numpy/Pillow/OpenCV? yes/no, licence of any code named); (b) THE THREE methods most
   applicable to our tiles in Claude Code, each with: the mechanism it attacks in our taxonomy, a concrete recipe (parameters),
   the cheapest read-free test (the TXE-D proxy: atlas top-1 err on dev_tune under the rendering vs plain, gate paired p < 0.01),
   and its estimated cost; (c) methods explicitly NOT applicable and why (multispectral, physical treatment, models needing a
   download the container cannot make). Cite every source with URL and date; copy no code from an unlicensed repository
   (CLAUDE.md rule 8): describe, then implement from the description in `tools/tx_prep.py` as flags ONLY if TXE-D's tool
   exists on main by then (fetch and check); otherwise write each recipe as a ready-to-paste flag spec for the lane.
3. Where a method is implementable in under 40 lines with numpy/Pillow/OpenCV (Sauvola binarisation, a bleed-through mask from
   channel difference, stroke thickening, unsharp mask), implement it as `tools/tx_prep.py --setting <name>` (rebase onto
   TXE-D's file if it exists; else a standalone `tools/tx_recovery.py` with --help and test) and run the read-free proxy on
   dev_tune exactly as TXE-D's brief describes (atlas classify holding out all of no.87, label-blind box mapping, commit before
   scoring). No vision call in this job: the reads, if any, are the lane's to brief after the proxy.

## Report
RESULTS block at the end of the research note: methods tested read-free with their paired numbers vs plain (or "not tested:
<why>"), and a one-line recommendation of which one deserves the single read. One row per method in the Results log of
research/TX-IDEAS-2026-10-09.md (id O5-<method>; rebase before editing). Hosts: web search only, 1.5 s apart, no scraping of
paywalled sites, no login. Cap 6; stop at 80% of cap or box. Report in a short paragraph (first line: the three methods and
whether any passed the proxy) and stop.
