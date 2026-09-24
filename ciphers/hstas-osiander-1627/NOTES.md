open

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
