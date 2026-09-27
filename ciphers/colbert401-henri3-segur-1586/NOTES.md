found-solved
Bourdeau's cyphersolver repository (`targets/segur/NOTES.md`, `docs/segur.html`, `papers/histocrypt/segur1586.tex`, shallow-cloned and read in full by this worker) and Tomokiyo's `henryiii.htm` (on disk, read in full) plus its reconstructed-key image `henryiii_figure.png` (fetched and read by this worker) together settle the target; printed editions (Lettres de Henri III, Berger de Xivrey's Recueil) were not opened, since the finding below makes them moot for this verdict.

## Target

BnF, 500 (Cinq cents) de Colbert 401, f.321 (June 1586) and f.333 (10 July 1586): letters catalogued by Tomokiyo as "Henry III's letter to Messrs de Chruain[?], Ruivy[?] et Segur", with portions in numerical cipher and (f.321 only) an interlinear decipherment on the leaf itself. Gallica ark btv1b10035574w. QUEUE row: `| 1 | Henry III to Segur, BnF 500 de Colbert 401, f.321 (June 1586) + f.333 (10 July 1586) | KEY-ADJACENT.tsv row 1 (henryiii.htm) | cryptanalysis-adjacent (key from an interlinear decipherment on f.321 itself) | digits (numerical cipher) | key printed, from the same volume's own interlinear decipherment | yes, Gallica ark btv1b10035574w | $5, Sonnet | queued, key-adjacent, SCOUT-OWN-6 |`.

## Gallica ark confirmed (rule 2 / brief step 1)

`python3 tools/gallica_folio.py btv1b10035574w --folio 321` returned no folio-labelled canvases (440 canvases, all "NP"-style, no folio labels to anchor from), but the manifest itself was fetched and its `metadata` block read directly:

```
label: BnF. Département des Manuscrits. Cinq cents de Colbert 401
Shelfmark: Bibliothèque nationale de France. Département des Manuscrits. Cinq cents de Colbert 401
Title: « Négotiation de M. [Jacques] de Segur, baron de Pardaillan, pour le roi de Navarre avec les Princes
       protestans d'Allemagne. » (1584-1588.). I Années 1584-1586. — Lettres originales, copies et minutes.
Format: 396 feuillets
```

The ark resolves to Cinq cents de Colbert 401 exactly, and the manifest's own title independently confirms the sender/correspondence identified below: Ségur-Pardaillan's negotiation for the king of Navarre with the German Protestant princes, 1584-86.

## The specific question (Tomokiyo: (a), (b) or (c)?)

`sources/cryptiana/web/henryiii.htm` (grepped and read in full, lines 253-259), verbatim:

> "BnF, 500 de Colbert 401 (Gallica), f.321 is Henry III's letter to 'Messre de Chruain[?], Ruivy[?], et Segur' ([11?] June 1586) with some portions in numerical cipher. Interlinear decipherment allows reconstruction of the cipher."
> [image: henryiii_figure.png]
> "This allows deciphering another letter of Henry III at f.333 (10 July 1586)."

`f.333` does not otherwise recur on the page: no plaintext for f.333 is printed there, and the sentence is capability ("allows"), not a completed-past-tense claim. `henryiii_figure.png` was fetched (HTTP 200, one request) and read: it is a full nomenclator table captioned **"Cipher Reconstructed from 500 de Colbert 401, f.321"** — a homophonic letter alphabet (a 12-15, b 26, c 17-18 …), a syllabary (ba-vu, 63-142), and five nomenclature/word entries printed with their plaintext (`Le Roy de Navarre` = 162, `Prisers???` = 302, `vers?` = 315, `qui` = 317, `nous` = 322).

**Answer: (a).** Tomokiyo reconstructed the cipher key from f.321's interlinear decipherment and printed the full table. He did not himself decipher f.333 or print its plaintext (not (b)); this is more than a bare observation that it "could be" done, since the actual key is on the page (so not only (c)).

Per the brief's own rule, (a) makes this `found-solved` in principle. What settles it beyond Tomokiyo's page:

## Solver-repository finding (decisive)

`dbourdeau/cyphersolver` (shallow-cloned this session, `targets/segur/`, `docs/segur.html`, `papers/histocrypt/segur1586.tex`) has **already fully solved this exact target**, posted 16 September 2026 and updated 25 September 2026 — before this session and before SCOUT-OWN-6 filed it as "queued, key-adjacent" on 27 Sept 2026. Confirmed independently by web search (`dbourdeau.github.io/cyphersolver/segur.html` indexed live).

- **f.333 read with Tomokiyo's own f.321 key**, exactly the step the brief asked this worker to evaluate: "Tomokiyo's table (`key_321.json`) reads it almost completely: *[162] desire fort d'avoir des nouvelles de [204] de [189] [190] … et leur advis sur le chemin qu'il doit tenir et comment. … il fault avancer la levée et la faire marcher le plustost qu'on pourra.*" Three values Tomokiyo left blank were forced by the reading (24=f, 34=l, 36=m). f.333 is a news-sheet in the third person, signed *Henry* at La Rochelle, 10 July 1586, countersigned; 162 = *Le Roy de Navarre* is the king's own sign in his own cipher. This is a period-key reading (grade H: key read from Tomokiyo's own interlinear-derived source), not cryptanalysis.
- **Bourdeau's own correction to the catalogue entry** (also independently supported by the Gallica manifest title above): the letters are not Henry III's but **Henry of Navarre's** — signed *Henry* at Montauban and La Rochelle, "vostre affectionné maistre et parfait amy", speaking of "mon frere Mons.r le Prince" (Condé); the volume is Ségur-Pardaillan's négociation for Navarre. f.321 (addressed to Clervant, Buhy[?] and Ségur as "conseillers en mon conseil d'estat et surintendans de ma maison et finances") is Navarre's council, settling the sender for that pair too.
- Beyond f.321/f.333, Bourdeau **ciphertext-only broke the different, harder cipher** on four further letters in the same volume Tomokiyo separately lists as "in a different cipher" (ff.143, 233, 239, 288v — a homophonic alphabet plus 70-entry alphabetical syllabary, 461 tokens), with matched controls (structured annealer, 88.9-99% of letter tokens recovered against controls of the same shape), and found a sixth cipher-bearing leaf Tomokiyo does not list at all (f.366, partially read). A HistoCrypt 2027 short-paper draft (`papers/histocrypt/segur1586.tex`, anonymous-for-submission) documents the method.
- Lasry (per Bourdeau's NOTES.md, private communication cited there) independently solved the ff.233/239/288v cipher in 2024; unpublished.
- `aaymeloglu/unsolved-ciphers` (shallow-cloned, grepped for "colbert 401"/"colbert401"/"segur"/"pardaillan") has no hit on this item.

## What is left to hand on

Nothing needing solving. f.333 (this target's own second folio) already has a published period-key reading; f.321 stands on Tomokiyo's own interlinear ground truth (the figures are struck through by the decipherer's pen and cannot be independently re-transcribed from the image, per Bourdeau's own note). The correction to make in our own registers: `KEY-ADJACENT.tsv` row 1 and `QUEUE.md`'s row 1 ("queued, key-adjacent, SCOUT-OWN-6") both need a status update to found-solved/dropped, and the sender field corrected from "Henry III" to "Henry of Navarre" (both sources independently agree: Bourdeau's reading of the clear French, and the Gallica manifest's own title). This worker made that correction in the same push (see done line); no further campaign, transcription or key application belongs on this target.

## Search log (rule 1 order)

1. **Search engine.** `WebSearch`: `"Colbert 401" Henri III Segur cipher 1586` and `Bourdeau "segur1586" HistoCrypt Navarre cipher`, 27 Sept 2026. Both returned `dbourdeau.github.io/cyphersolver` pages (segur.html, index.html) live and indexed, confirming the repository finding above is public, not just a local clone artifact.
2. **Sender's/recipient's printed Lettres or Correspondance on the Internet Archive.** Not opened this session (see line 2 above): the solver-repository finding already settles the verdict, and reading the standard edition (Lettres de Henri III, Champion/François, or Berger de Xivrey's Recueil des lettres missives de Henri IV) would help a verifier's novelty class (N-grade) but not this check-solved verdict, which is about whether cryptanalytic work is still needed (it is not). Left as an open task for whichever session next touches this target's novelty question — not this one's to do, per the brief's cap.
3. **Calendars/state-paper series.** Not checked, same reasoning as above.
4. **Comment threads (Cryptiana blog, Cipherbrain).** Not checked this session; box/cap discipline given the decisive finding in step 5.
5. **DECODE (de-crypt.org).** `tools/decode_list.py` is a status-filtered crawl tool (RecordsList), not a free-text shelfmark search; a full crawl to find one 16th-century French shelfmark among DECODE's many records was judged disproportionate to the value once step 6 settled the verdict, and was not run. Logged as a gap, not a checked "no hit".
6. **Solver repositories (decisive).** `github.com/dbourdeau/cyphersolver` shallow-cloned, grepped case-insensitively for "colbert 401", "colbert401", "segur", "pardaillan": found `targets/segur/` (full NOTES.md, reading.md, decode_v4.txt, ct_233/239/288/143/333/366.txt, key_v4.json, key_321.json, solve.py, control.py, gloss_signs.py), `docs/segur.html` (published write-up), `docs/reveal/segur.json`, `docs/steps/segur.json`, `papers/histocrypt/segur1586.tex` (HistoCrypt 2027 draft) — read in full, quoted above. `github.com/aaymeloglu/unsolved-ciphers` shallow-cloned, same grep: no hit.

## Access log

Gallica: 1 request (IIIF manifest.json for btv1b10035574w). cryptiana.web.fc2.com: 1 request (henryiii_figure.png, HTTP 200). GitHub: 2 shallow clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers), no further requests. No 429/403 encountered; no host retried.

## Grades (rule 4)

Nothing read by this worker directly from an archive source; every fact above is **cited from Bourdeau's and Tomokiyo's published work** (grade per rule 4 would be H for the f.333 reading — Bourdeau's key source is Tomokiyo's own interlinear decipherment on f.321 — and this worker did not re-derive or verify it against the image). This worker's own contribution is the check-solved verdict and the correction to this repository's registers, not a new reading.

`python3 tools/intake_gate_check.py colbert401-henri3-segur-1586`:
```
colbert401-henri3-segur-1586: found-solved (line 1) -- edition/page or full-text-search citation found within 6 lines
```
exit 0.
