open
Sattler, *Geschichte des Herzogthums Würtenberg unter der Regierung der Herzogen*, Theil 6 and 7 (1774; IA `10003243bsb`, `10003244bsb`, the volumes covering 1608-1637), read by this worker (GF4-BATCH19, 3 Oct 2026) by full-text grep of both djvu OCR files for Osiander / Diarium / Tagebuch: one Osiander mention (Th. 7, his sermon cited in the 1628-29 regency dispute), no diary, no cipher; no printed edition of the diary itself is known (csDA2 24 Sept, GF-A2-7 2 Oct, this pass).

# Lukas Osiander, "Diarium Rerum Wirtenbergicarum et Variarum" 1627-1630 — symbol cipher — HStA Stuttgart

QUEUE row: DA11 (sources/solver-diffs/2026-09-24-lane-n2-dea.tsv, "German state archives, online finding aids
(LANE N2 scout of 24 September 2026)").

## Source

Hauptstaatsarchiv Stuttgart, **J 7 Bü 66** (Sammlung Pregizer — Johann Ulrich Pregizer III, Stuttgart archivist,
1647-1708). Lukas Osiander (1571-1638), theologian and Tübingen university chancellor, kept this diary
8 May 1627 - 30 Aug 1630, chronicling Württemberg and general events. Deutsche Digitale Bibliothek's item
description (checked 24 Sept 2026) states multiple entries across 1627, 1628 and 1629 are written wholly or
partly in a symbol-based secret script, plus individual Hebrew words/letters in some 1628-29 entries. One
snippet dates a symbol-cipher entry to "17. Mai 162[?]".

**This is a diary, not correspondence** — a different design class from DA7-DA10 (probably a private notation
system for guarded personal opinions, not a diplomatic nomenclator), and the "cipher" is stated as
symbol-based, not numeric.

## Check-solved sweep (24 September 2026)

1. **Editions.** WebSearch ("Lukas Osiander Diarium Pregizer Geheimschrift Symbolen 1627"; "Diarium Rerum
   Wirtenbergicarum Osiander Edition gedruckt Württembergische Geschichtsquellen") found no printed edition of
   this diary. Lukas Osiander the theologian has substantial theological-controversy literature about him
   (Wikipedia English page "Lucas Osiander the Elder"), but nothing ties a print edition to this specific
   Pregizer-collection diary manuscript. Württembergische Vierteljahrshefte für Landesgeschichte (the standard
   regional-history journal named in the brief) was not searched directly this pass — a real gap; its own
   index/search interface was not reached this budget.
2. **Printed decipherment / catalogue note.** DDB's description gives no indication that the symbol cipher has
   been read or that a key survives with the diary.
3. **Community lists.** `sources/cryptiana/` grepped for "Osiander": no hits.
4. **DECODE.** `sources/decode/` grepped for "Osiander", "Pregizer", "Wirtenbergicarum", "Diarium": no hits.
5. **Solver repositories.** Fresh shallow clones, 24 Sept 2026. No target folder for Osiander in either repo;
   `grep -rli osiander` across both trees: zero matches.
6. **General web search.** As (1). No result names an attempt to read the symbol cipher in this diary.

**Copy status.** Not independently re-tested this pass against LABW's viewer. Scout's original sweep
(sources/solver-diffs/2026-09-24-lane-n2-dea.tsv) recorded "none tested (no digitisation link)" for this row.
**Copy-order**, pending a direct re-check. See REQUEST.md.

**Host requests this pass:** WebSearch 2, github.com 1 shallow clone each of both repos (shared across this
run's six targets); no direct LABW request this pass.

## Verdict

**Status: open, stage 2 (verified unsolved).** No edition, catalogue gloss, community list, DECODE record, or
solver-repository entry describes or reads the symbol cipher in this diary. Design notes for a future solver:
a symbol-based system in a personal diary (not a diplomatic dispatch) is a different attack surface than the
numeric nomenclators typical of DA7-DA10 — word-boundary and glyph-repertoire analysis on the image (once
copied) come first, per LESSONS.md's "structure before search."

**Recommended next steps (not run this pass):** (1) search Württembergische Vierteljahrshefte für
Landesgeschichte's own index for "Osiander" + "Diarium"/"Tagebuch"; (2) re-test LABW's viewer for J 7 Bü 66
directly; (3) once a copy is in hand, count distinct symbols and check against the diary's other known code
uses (the Hebrew-letter entries) for a shared design.

## csDA2: edition lead (24 September 2026, close-out pass)

Closing the *Württembergische Vierteljahrshefte für Landesgeschichte* lead flagged above. The run is long —
archive.org's `advancedsearch` for the journal title returns 121 items (Neue Folge issues from `whv11p`/1902
through `whv3940c`/1933-34, plus scattered Google Books scans of the 1870s-90s Alte Folge) — and archive.org's
metadata `text:` search field is not a full-OCR index (confirmed by a control query for "Pregizer", the diary's
own archival collection name: it returned zero relevant hits, only unrelated items whose *titles* happen to
contain the string). Reading all 121 volumes' `_djvu.txt` individually is outside this target's share of the
$5 pass cap and the lane's fan-out limits. WebSearch for the diary's own terms ("Pregizer" "Osiander" "Diarium"
"site:archive.org"; "Württembergische Vierteljahrshefte" + "Osiander" + "Pregizer" + "Geheimschrift") surfaced
only the DDB catalogue description already in this file and the LABW J 7 Sammlung Pregizer finding-aid preface
(fetched via WebFetch: no mention of the diary J 7 Bü 66, a printed edition, or its cipher) — no hit naming a
WVH volume, article, or Gesamtregister/index that covers this diary.

**Verdict: blocked.** The named lead could not be searched exhaustively through this pass's authorised routes
within budget — not because any one volume refused to load, but because the run is too large for a keyword
search without a full-text index this pass could reach. The nomination stays HELD. A worker with a specific
volume/year to check (e.g. from a citation elsewhere, or willing to spend a larger budget working through the
run), or access to the WVH's own website search (not attempted this pass — out of the named lead's route),
would close this properly.

Host requests this section: archive.org 1 (advancedsearch, 121 hits, no further fetches), WebFetch 1 (LABW
Pregizer Vorwort), WebSearch 3.

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## JSTOR runner, 26 Sept 2026

- `"Lukas Osiander" AND Diarium AND Württemberg AND Geheimschrift`: no relevant hit (0 results, none about the letter).
- `"Diarium Rerum Wirtenbergicarum et Variarum"`: no relevant hit (0 results, none about the letter).

## Web and blog check (GF-A2-7, 2 Oct 2026)

Plain web searches (WebSearch, standard): (1) `Lukas Osiander Diarium 1627 1630 Geheimschrift Pregizer` -- only
biographies (deutsche-biographie.de sfz73870, pnd117154547; ADB), nothing on the diary or a cipher; (2) `"J 7 Bü 66"
Osiander` -- no hit on the shelfmark (Osiander family GND/dikon records, the HAdW Andreas Osiander edition project,
which is the 16th-c. Andreas, not this diary); (3) `Osiander Tagebuch Dreißigjähriger Krieg Württemberg Tübingen
Kanzler Diarium Edition` -- Wikipedia, evangelisch.de (2021, 2024) on Lucas Osiander, the 2010 Tübingen Festgabe
Merten; none names a diary edition; (4) `Osiander diary cipher symbols 1628 Stuttgart Hauptstaatsarchiv` -- same
biographies plus de.wikisource ADB; nothing; (5) `"Diarium Rerum Wirtenbergicarum" Osiander` (the folder's
descriptive title) -- no hit on the title; one related lead: Hiram Kümper, "Das »Diarium Wirttembergicum« -- eine
unbekannte historiografische Schrift von Christoph Bidembach († 1622)", Zeitschrift für württembergische Landesgeschichte (2021) pp. 395-403
(madoc.bib.uni-mannheim.de/60109, record page only, no full text there) -- a different, earlier Württemberg diary;
whether it discusses Osiander's continuation is not known (next: read it, the lead is listed here only).
Blog site searches: Cipherbrain (scienceblogs.de/klausis-krypto-kolumne) `Osiander Tagebuch Geheimschrift` -- only
unrelated diary posts (Agatha Highfield, Isdal, Erba, WWI diary); Cryptiana (cryptiana.blogspot.com,
cryptiana.web.fc2.com) `Osiander diary cipher` -- no results; Cipher Mysteries (ciphermysteries.com) `Osiander cipher
diary` -- "Enciphered diaries" (2009/01/12) and unrelated posts; the 2009 post's subject list (Potter, Wesley, etc.)
does not include Osiander. No hit named this diary, so no comment thread needed reading. Result: no decipherment or
plaintext of the diary's cipher entries found on the open web or the three blogs.

## Premise check (GF-A2-7, 2 Oct 2026)

(a) Folder's own mentions: NOTES.md and REQUEST.md mention no decipherment, gloss, key or clear copy; the only
related content is the DDB description's "individual Hebrew words/letters" in some 1628-29 entries (a script, not a
decipherment). Not found. (b) Other solvers' working files: fresh shallow clones 2 Oct 2026 (dbourdeau/cyphersolver
head 2 Oct 2026, aaymeloglu/unsolved-ciphers head 27 Sept 2026), `grep -rliE` for osiander, pregizer, "J 7 B[uü]",
"Diarium Rerum": zero hits in either (cited, nothing copied). Not found. (c) Physical neighbours: no image of J 7 Bü 66
is on disk or known online (scout: "no digitisation link"); the leaves around the cipher entries cannot be viewed --
unreachable until a copy exists (REQUEST.md); the rest of the Sammlung Pregizer was not opened. (d) Recipient side: a
private diary has no recipient; the nearest equivalent, a printed edition or study of the diary or of the Pregizer
collection, was not found (searches above, and csDA2's 24 Sept pass); the Kümper ZWLG 2021 article above is the one
untried lead. Not found.
Gate note: the status line still lacks an edition citation because no printed edition of this diary is known to exist
to read; that line is left as it is (this worker read no edition), so the target stays held at the intake gate.

## Edition citation and new-publication check (GF4-BATCH19, 3 Oct 2026)

No edition of J 7 Bü 66 exists to read (three passes now agree). The citation under the status word is the standard
printed history of the duchy for these years, Christian Friedrich Sattler's *Geschichte des Herzogthums Würtenberg
unter der Regierung der Herzogen* (Theil 6, 1608-28, and Theil 7, 1628-37, Ulm/Tübingen 1774; BSB scans on IA
`10003243bsb` and `10003244bsb`), whose author was the ducal archivist and printed from the same Stuttgart archive:
both `_djvu.txt` files fetched once and grepped (long-s forms `Oſiander`/`Ofiander` included) for Osiander, Diarium,
Tagebuch, Pregizer. Result: Theil 7 once cites "D. Ofianders Predigt" in the 1628-29 regency dispute; nothing on a
diary or a cipher. A search result for the log, not a novelty verdict (rule 10).
Kümper, ZWLG 80 (2021) pp. 395-403 (GF-A2-7's lead on the Bidembach *Diarium Wirttembergicum*): the article PDF
(journals.wlb-stuttgart.de/index.php/zwlg/article/download/6367/6256/11734) answers curl with WLB's Anubis page;
the browser tool cleared the challenge but the server then started a download that neither `browser_fetch.js` nor
one Playwright download handler captured (4 requests, stood down per the good-citizen rule). It concerns a different
author's diary (Bidembach, d. 1622); next: a desk-browser read of its 9 pages for any mention of Osiander's
continuation (LOCAL-QUEUE candidate, not filed here).
**Cabinet Noir** (github.com/el-descifrador/cabinet-noir, HEAD 47b6db9, shallow clone 3 Oct 2026): 24 project
folders, none Württemberg/Osiander/1627-30. **Apeiron** (apeiron.re front page): no publication list served; only
known publication is Koehler. Solver repos re-grepped 3 Oct 2026 (Bourdeau HEAD a439937, Aymeloglu HEAD d2800bb):
no osiander/pregizer hit. No decipherment or plaintext of the diary's cipher entries located on 3 Oct 2026.

Gate re-run (GF4-BATCH19, 3 Oct 2026; supersedes the GF-A2-7 gate note above): `hstas-osiander-1627: open (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0 (was exit 1).

## While waiting (RUN4-WAITBF, 4 Oct 2026)

- Action that depends on nobody: recommended step (2), still unrun -- re-test LABW's online viewer for HStAS J 7 Bue 66 directly (one or two requests) to settle whether the diary is digitised before any copy order; ~$0.5 (estimate). The Bidembach-diary article read stays a desk-browser (LOCAL-QUEUE candidate) step.
