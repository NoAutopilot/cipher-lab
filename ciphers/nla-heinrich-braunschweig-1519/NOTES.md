open

# Two enciphered letters of Heinrich der Jüngere, Herzog von Braunschweig-Lüneburg — NLA Bückeburg

QUEUE row: DA7 (sources/solver-diffs/2026-09-24-lane-n2-dea.tsv, "German state archives, online finding aids
(LANE N2 scout of 24 September 2026)").

## Source

Niedersächsisches Landesarchiv, Abt. Bückeburg, L 1:
- **Nr. 548**, 1519: "Schreiben des Herzogs Heinrich von Braunschweig-Lüneburg betr. Militärisches
  (Geheimschrift)."
- **Nr. 562**, 1522: "Politische Absichten des Herzogs Heinrich d. M. von Braunschweig-Lüneburg (Geheimschrift)."

Heinrich der Jüngere / Heinrich der Mittlere (1489-1568), Duke of Braunschweig-Lüneburg and Prince of
Braunschweig-Wolfenbüttel, 1514-1568. 1519 falls at the start of the Hildesheimer Stiftsfehde (1519-23), in
which Heinrich won a large part of the Hildesheim cathedral territory; 1522 is within the same feud's
aftermath/consolidation period. **Note the archive:** the bulk of Heinrich's own political archive is held at
Wolfenbüttel, not Bückeburg — these two items being at NLA Abt. Bückeburg (the former Schaumburg-Lippe
archive) suggests they reached that repository via a collateral line or a later provenance not established
this pass.

## Check-solved sweep (24 September 2026)

1. **Editions.** Friedrich Koldewey wrote on Heinrich der Jüngere ("Heinz von Wolfenbüttel", 1883) and is the
   standard modern-era historian of this duke, but no edition of his correspondence citing either 1519 or 1522
   letter, or a cipher, was located by WebSearch ("Koldewey Heinrich der Jüngere politisches Archiv Briefe 1519
   1522 Hildesheimer Stiftsfehde"). Hortleder's *Der Römischen Keyser- und Königlichen Maiesteten... Handlungen*
   is a Schmalkaldic War-era (1540s) collection by scope; checked by date range against the Hildesheimer
   Stiftsfehde (1519-23, Wikipedia/dewiki confirmed) and judged the wrong period for these two items, not opened.
   **Havemann's *Geschichte der Lande Braunschweig und Lüneburg*** (3 vols., 1837-57) is the actual standard
   19th-c. narrative history covering this exact feud (confirmed by WebSearch: vol. 2 treats 1519-23) and is
   digitised (MDZ bsb11684618/19; several Google-Books-sourced copies on archive.org, e.g. `10019400bsb`,
   `bub_gb_b2EAAAAAcAAJ_2`) — identified but **not opened this pass** (budget). It is a narrative secondary
   history, not itself a Lettres/Correspondance edition of Heinrich der Jüngere (none such was found to exist),
   so its absence does not by itself block a verdict per rule 9, but it is the strongest concrete lead for
   finding out whether either letter (or its cipher) was ever quoted or described in print, and should be the
   first thing the next pass on this target opens. No calendar or Regesten for NLA Abt. Bückeburg L 1 for this
   date range located.
2. **Printed decipherment / catalogue note.** The finding-aid titles give no indication of an attached key or
   contemporary decipherment for either item.
3. **Community lists.** `sources/cryptiana/` grepped for "Brunswick", "Lüneburg", "Heinrich": all hits
   (habsburg.htm, german.htm, louisxiv.htm, crypto.htm) concern a different, later duke — **Augustus/August,
   Duke of Brunswick-Lüneburg (1579-1666)**, the cryptography author "Gustavus Selenus" and the subject of
   Cryptiana's own "Triplet Cipher" page — not Heinrich der Jüngere (1489-1568) and not either 1519/1522 item.
   Quoted for the record, per the M9 lesson: cryptiana's habsburg.htm says only "a cipher of Augustus of
   Brunswick-Lüneburg (see Triplet Cipher)" — a different person, a different, already-published system.
4. **DECODE.** `sources/decode/` grepped for "Braunschweig", "Lüneburg", "Heinrich", "Bückeburg": no hits.
5. **Solver repositories.** Fresh shallow clones, 24 Sept 2026. No target folder for Braunschweig, Lüneburg, or
   Heinrich der Jüngere in either repo. `grep -rliE "brunswick.{0,3}l[uü]neburg|heinrich.{0,3}(der )?j[uü]ngere"`
   across both trees: only the Cryptiana-sourced Augustus/Gustavus Selenus references noted above (same
   person as (3), irrelevant), no target.
6. **General web search.** As (1). No result names either shelfmark or attempts a reading of either letter.

**Copy status.** Not independently tested this pass against Arcinsys Niedersachsen's viewer (the scout's
original sweep, sources/solver-diffs/2026-09-24-lane-n2-dea.tsv, found "125 raw hits across 2 terms (page 1
only)" for Arcinsys with no digitisation link recorded for DA7). **Copy-order**, pending a direct re-check.
See REQUEST.md.

**Host requests this pass:** WebSearch 2, github.com 1 shallow clone each of both repos (shared across this
run's six targets); no direct Arcinsys Niedersachsen request this pass (relied on scout's same-day check).

## Verdict

**Status: open, stage 2 (verified unsolved), with one open edition gap.** No printed correspondence, catalogue
gloss, community list, DECODE record, or solver-repository entry names either letter. The provenance question
(why two Heinrich der Jüngere items sit in the Bückeburg, not Wolfenbüttel, holdings) and the unopened Hortleder
edition are the two loose threads that should be closed before a copy order, since either could turn up a
printed text or a sibling.

**Recommended next steps (not run this pass):** (1) open Havemann vol. 2 (*Geschichte der Lande Braunschweig
und Lüneburg*, 1839, MDZ bsb11684619 or the IA copies) for 1519/1522 and phrase-search for "Geheimschrift" /
"Chiffre" / either letter's content; (2) ask why L 1 (Bückeburg) holds these two Heinrich der Jüngere items — a
family/provenance note might also surface a sibling letter or a key; (3) re-test the Arcinsys Niedersachsen
viewer directly for these two signatures before copy-ordering.
