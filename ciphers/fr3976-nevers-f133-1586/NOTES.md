# BnF fr.3976, ff.133-134 -- unnamed Paris informant to the Nevers household, 6 June 1588

found-solved

BnF finding aid for fr.3974-3995 (cached copy of `archivesetmanuscrits.bnf.fr`'s own notice, read in full by
this worker for the fr.3976 section) gives piece 71, Fol.133, as an unsigned cipher letter of 6 June 1588.

## Summary (read this first)

CS-FR3976 (parent worker, 27 Sept 2026). Queued by `SCOUT-OWN-7` (QUEUE.md "SCOUT-OWN-7 key-adjacent
candidates" row 2, `KEY-ADJACENT.tsv` row 10) from Tomokiyo's `nevers.htm`, which quotes cipher no.7 (BnF
fr.3995 fol.15, dated 1586 in the catalogue's own numbering) as used "in some passages in papers in BnF fr.3976,
fol.131, 133, 139", adding of fol.133 specifically: "The second remains undeciphered but can be read with this:
'roy', 'Nevers', 'La Cassine', ....". Quoted verbatim from `sources/cryptiana/web/nevers.htm` (local mirror).

**`dbourdeau/cyphersolver` has already read this exact letter in full, published, live.** Per this repo's own
lesson from CS-CLAIR331 and CS-BONGARS7131 the same morning, the solver repositories were shallow-cloned and
grepped for "3976" before any deep work. `targets/r3708/` (catalogue item 186, DECODE R3708) is titled "Paris
informant to the Nevers household, 6 June 1588: BnF fr. 3976 ff. 133-134" and its own NOTES.md opens: "Status:
read. All 18 cipher runs read (226 of 230 signs certain, 98.3%, measured from `ciphertext.txt`/`reading.tsv`);
four signs read from context only." The key was rebuilt from the sibling letters on the same informant's f.62
(R3705, `targets/nevers1588/`, glossed on the leaf) and f.131 (also glossed on the leaf, matching the finding
aid's "avec chiffre et déchiffrement" note on piece 70/fol.131 immediately before our piece), then confirmed
independently against the 9 June letter (f.139, piece 74, itself carrying a contemporary interlinear
decipherment). Bourdeau's own published write-up is live and was checked directly, not taken on the repository's
word: `curl -sS -o /dev/null -w '%{http_code}' https://dbourdeau.github.io/cyphersolver/r3708.html` returned
`200` (27 Sept 2026), and the fetched page text contains "fr. 3976" and "133-134". Also listed in
`cyphersolver/CATALOGUE.md` line 207, `cyphersolver/SOLVED_CATALOGUE.md` line 303, `cyphersolver/SOLVED_RANKING.md`
line 244 and `cyphersolver/README.md` line 101 (class C, read 22 Sept 2026) -- four independent listings inside
the one repository, not a single stray file.

`aaymeloglu/unsolved-ciphers`: no dedicated hit for "3976" content (only catalogue/index files list the DECODE
record numbers 3705/3708/3709 as raw rows, with no reading or write-up); grepped fresh, no target folder.

**Date correction.** `KEY-ADJACENT.tsv`/`QUEUE.md` both carry "1586-era" for this row, following cipher no.7's
own catalogue date in `nevers.htm` (fol.15 of fr.3995, dated 1586). The letter actually on fr.3976 fol.133 is
dated 6 June 1588 by its own text ("Ce 6. Juing a 10 heures du soir") and by the BnF finding aid's own listing
(piece 71, under the fr.3976 section, immediately after piece 70/fol.131 "Le 4 juing 1588" and before piece
72/fol.135 dated "VIIme jour de juing"). Tomokiyo's no.7 cipher (reconstructed from a 1586 letter, fr.3995
fol.15) was evidently reused for at least these three 1588 letters in fr.3976 -- the cipher's *origin* is 1586,
its *use on this leaf* is 1588. Corrected in `KEY-ADJACENT.tsv` row 10 and `QUEUE.md` row 2 in this push; the
folder name (`fr3976-nevers-f133-1586`) is kept as filed by the scout/orchestrator rather than renamed, since
renaming a live-claimed folder path is outside this worker's brief.

**Found-solved grade (README F0/F1/F2): F0.** `dbourdeau/cyphersolver` -- a specialist database of exactly this
kind of material, already the repo this project defers to for the public DECODE catalogue's own read status --
already links this manuscript (fr.3976 ff.133-134, DECODE R3708) to its full decipherment, published and dated
22 Sept 2026, five days before this check-solved pass. No contribution to make; this repo does not repeat the
reading. Tomokiyo's own `nevers.htm` did not have the plaintext (he explicitly calls fol.133 "undeciphered" and
gives only three glossed words), so the correction here is against our own queue row, not against Tomokiyo.

**Same cipher as the fr.3251 keys on disk? No.** `ciphers/ceppo-nevers-fr3251-1570s/keys/` and
`ciphers/nevers-birago-fr3251-1572/keys/` come from Tomokiyo's `nevers.htm` section "More Ciphers from Further
Sources" -> BnF fr.3251 (`<H3 id=BnFfr3251>`, line 763 of the mirror), described as "letters partially in cipher
from Lodovico Birago to Duke of Nevers (1570-1572)" -- a wholly separate manuscript and cipher family from the
page's main "Catalogue of Ciphers in BnF fr.3995" (no.1 through no.7 and beyond), where cipher no.7 (fol.15,
1586) lives. The two families are never conflated in `nevers.htm`'s own structure; confirmed by reading both
sections directly, not inferred from naming alone.

## Search log (rule 1 order, dated 27 Sept 2026)

1. **Search engine on the cipher's name / target**: not run separately this pass (superseded by the solver-repo
   hit below, found before a web search was needed; the key sentence is quoted directly from `nevers.htm`, not
   the scout's paraphrase, per this morning's CS-CLAIR331/CS-BONGARS7131 corrections).
2. **Sender's printed Lettres/Correspondance on Internet Archive**: not applicable -- the letter's sender is
   unidentified even by the BnF finding aid ("Autre lettre semblable", no author named for piece 70 or 71, unlike
   the surrounding pieces which all name a correspondent); Bourdeau's own reading likewise leaves the sender
   unidentified ("Who the letter goes to is open" -- and who sends it is not resolved either). No printed
   Correspondance to search under a name.
3. **Calendars and state-paper series**: not run -- superseded by the direct finding-aid read (below) and the
   solver-repo hit, per this repo's "whole volume, not one page range" and "stated next step" lessons: once a
   solver repository's own dated, published write-up is confirmed live, further calendar search would only
   duplicate a verdict already settled at F0.
4. **Comment threads (Cryptiana blog, Cipherbrain)**: not checked this pass (time/cap; not needed for the F0
   verdict, which rests on the solver-repo hit and the finding aid, both independently confirmed).
5. **DECODE at de-crypt.org**: checked via the existing 24 Sept 2026 crawl on disk (`sources/decode/`), not a
   fresh login. `records-non-decrypted-2026-09-24-diff.tsv` line 520: record 3708, "Français 3976 fol. 133-134",
   catalogue status "Non-decrypted", but the diff's own annotation column already reads
   `nevers1588[read];r3708[read]` -- i.e. this repo's own prior crawl-diff tooling had already flagged that
   Bourdeau's repository reads this DECODE record, before this worker's session. `records-decrypted-2026-09-24.tsv`
   lines 672-677 list the sibling folios (f.66, f.60, f.56, f.52, f.131 as "Decrypted") and record 3709 (f.139) also
   "Decrypted" on DECODE's own catalogue.
6. **The two solver repositories**: `dbourdeau/cyphersolver` (shallow clone, `--depth 1`) and
   `aaymeloglu/unsolved-ciphers` (shallow clone, `--depth 1`), grepped for "3976", "Nevers", "1586" as the
   brief's own first step. Full detail above.

Also read directly (rule 1's "in this order" is a floor, not a ceiling; the finding aid and the ark check are
both required by the brief and independent of the solver-repo hit):
- **BnF finding aid** (`archivesetmanuscrits.bnf.fr`, fr.3974-3995 composite notice, cached in
  `cyphersolver/research/gallica_sweep/notice_cc504266_cd0e37708.html` and confirmed against the live
  archivesetmanuscrits.bnf.fr host returning HTTP 403 to a direct curl this session -- read the cached copy
  instead of refetching, since the notice's own content is what needed reading, not a live re-fetch): the
  fr.3976 section (composite notice offset 31370-45627 of the cached HTML) gives piece 71, "Autre lettre
  semblable. 'Ce 6 juing, à 10 heures du soir', 1588", Fol.133, immediately after piece 70 ("Lettre, avec chiffre
  et déchiffrement, contenant des nouvelles des événements qui ont suivi la journée des Barricades. 'Le 4
  juing' 1588", Fol.131) and before piece 72 (Fol.135, the Paris échevins' letter of 7 June). This is an
  independent read of the primary catalogue record, not a citation of Bourdeau's own citation of it.
- **Gallica ark**: `btv1b9060548h` resolves to "BnF. Département des Manuscrits. Français 3976" (IIIF manifest
  `label` field, fetched and cached this session, `sources/gallica-manifests/btv1b9060548h.json`) -- confirmed
  before citing it, per the brief. `tools/gallica_folio.py btv1b9060548h --folio 133` finds no canvas carrying a
  folio label (0 of 399 canvases labelled; this manuscript's manifest carries no per-canvas folio labels, the
  same "all NP" shape as fr.16092 noted in CLAUDE.md's Access playbook) -- an anchor pair was not fitted this
  session (Bourdeau's own `targets/r3708/NOTES.md` already states "f. 133r = canvas 223 ... foliation checked on
  the leaves", an eye check this worker did not need to repeat for a check-solved verdict).

## Requests

gallica.bnf.fr: 2 (manifest fetch, cached; `tools/gallica_folio.py` attempt). archivesetmanuscrits.bnf.fr: 1
(direct curl, 403 -- not retried, cached finding-aid copy used instead). GitHub shallow-clone x2
(dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers). dbourdeau.github.io: 2 (HTTP-code check + content fetch
of `r3708.html`, confirming the write-up is live). All well under the 1-3 request budgets named in the brief;
no 429/403 loop, no retry beyond the single archivesetmanuscrits attempt.

## Next step

None -- F0, no campaign. If the parent later wants a standalone contribution (a machine-readable key/reading
copied and credited, per CLAUDE.md rule 8, Bourdeau's code MIT/text CC BY 4.0), that would be priced as a
contribution, not a solve; not attempted here.

## intake_gate_check

```
$ python3 tools/intake_gate_check.py fr3976-nevers-f133-1586
fr3976-nevers-f133-1586: found-solved (line 3) -- edition/page or full-text-search citation found within 6 lines
```
