closed-negative

# Sigismund Schellhammer to Johann Georg Volckamer I, 10 December 1653 — UB Erlangen, Trew Briefsammlung

QUEUE row: TR-1 (`sources/solver-diffs/2026-09-24-lane-n3-trew.tsv`, LANE N3 scout scTREW, 24 September 2026,
Bavarikon faceted wildcard sweep of the whole Trew Briefsammlung). Check-solved run 24 September 2026 by LANE N3
csTR (session_017WAe73tDu7XTh9HXBXzHW6), brief `.claude/briefs/runs/2026-09-24-lane-n3-csTR.md`.

## Source

- `H62/TREWBR SCHELHAMMER_SIEGMUND[23`, `bav:UBE-TRE-00000BAV80017900`, Universitaetsbibliothek Erlangen-Nuernberg,
  Briefsammlung des Nuernberger Arztes Christoph Jacob Trew (~19,000 letters, digitised from December 2017).
  Catalogue title verbatim: "[Brief an Johann Georg Volkamer I] : vom 10.12.1653 : mit Siegel : mit verschiedenen
  Schluesseln fuer Geheimschriften auf der Adressseite" (with various keys for secret writings on the address
  side). Language Latin (letter body). CC0 (metadata) / PDM (digitisation).

**Sender:** Sigismund Schellhammer (also catalogued "Schelhammer"), one of 37 letters to Volckamer I in this
collection (`H62/TREWBR SCHELHAMMER_SIEGMUND[1`-`[37`, 1647-1656; see catalogue sweep below) — a Nuremberg-circle
physician correspondent, not otherwise identified this pass (out of scope for a check-solved run; a biographical
pass is a follow-up, not actioned here).

**Recipient:** Dr. Johann Georg Volckamer I (Nuremberg physician; same recipient as `ciphers/trew-posthius-1614-18`,
BV1). The Nuremberg physicians' circle around Volckamer I recurs across the Trew collection.

## What is on the leaves (eyeballed at full native IIIF resolution; NOT transcribed or decoded, per brief)

**Recto (`images/p1.jpg`, 2892x3869 native):** an ordinary Latin letter, dateline "Hamburgi" (Hamburg), opening
"Amplissime Vir Dominorum...", closing "salve iterum ac vale", signed with a flourish and what reads as
"Hamburgi. A.o.R. / A ne.im. / A.d.n.Rbb" under the signature block, addressed at top to "D. Joh. Georg.
Volckamero...". Ordinary correspondence content (a Dillherr letter forwarded, a physician's death and estate
reported, books from Cardinal Mazarin's library). **No cipher content, no key material, visible anywhere on this
page at native resolution.** This confirms and extends the scout's 1200px eyeball pass (which had not ruled out
smaller marginal cipher content) — the whole recto was reviewed at full 2892px width, nothing beyond ordinary
prose.

**Verso/address side (`images/p2.jpg`, 2892x3885 native; key region crop `images/p2_key_crop_rot.jpg`, native
region 0,0,1450,2200, rotated 270 degrees for upright reading):** address block ("...Volckamero, Fuernehmen
Practico und Medicinae Doctorn zu Nuernberg"), wax seal, and, top left of the leaf (written with the page turned
90 degrees relative to the address text, as is conventional for marginal notes), **three separate key blocks**,
confirmed and read more precisely than the scout's 1200px pass:

1. A small grid: "Kaqnl / lbrnu / mcson" over a rule, then "oeqqp / pfxrh" below it — five short columns, plain
   letters over what look like substitute letters, not a full 24-letter run.
2. The complete 24-letter Latin alphabet with no j/v, in its plain order, split across two lines: "abcdefghiklm"
   over "nopqrstuwxyz" (this is the SAME base alphabet as the "SALUTEM"-keyword table on the sibling
   trew-posthius-1614-18 1614 leaf, though here left in plain unkeyed order, not keyword-permuted) — with two
   further short lines below it, "qgeob" and "ptagbez" (or "ptagbc2"), that read as substitute-letter rows for
   part of that alphabet.
3. A third, smaller grid: "agntom / b.onpn / ci.pwqo" (a few cells carry an unclear mark rather than a letter).

**All three blocks are systematic plaintext-to-substitute tables — key material — not an enciphered message.**
No clear-text crib sits beside any of them (contrast the sibling trew-posthius-1614-18 1614 leaf, which pairs its
key with a 4-line cipher block AND a clear-text crib "Fridericus Henricus vocat[ur] recens natus Princeps"), no
word-length or sentence-length run of cipher symbols appears anywhere on either leaf, and no drawn glyphs (unlike
that sibling's 1618 leaf, whose left key block uses hand-drawn nomenclator symbols) — here every substitute is an
ordinary Latin letter. This is a **key-only leaf**: it teaches or records up to three cipher systems but carries
no hidden message of its own. Shape matches trew-posthius-1614-18's 1618 leaf (key/specimen material, no
concealed news) rather than its 1614 leaf (key plus an actual short ciphertext).

## Catalogue sweep for other Schellhammer/Volckamer letters that might carry the matching ciphertext

Per brief, since this leaf is keys-only: searched `www.bavarikon.de` (plain curl, no browser needed, 200 OK) for
every other letter in this correspondence, to see whether the enciphered message these keys serve might sit on a
*different* leaf.

- `terms=Schellhammer&holding_institution=Universit%C3%A4tsbibliothek+Erlangen-N%C3%BCrnberg&object_category=Briefe`
  → 37 hits, all `H62/TREWBR SCHELHAMMER_SIEGMUND[1`-`[37`, all "[Brief an Johann Georg Volkamer I]", dated
  26.10.1647-15.04.1656. Only **[23]** (this item, bav80017900) mentions keys/Geheimschriften in its title. One
  other item of note but not cipher: **[21]**, `bav:UBE-TRE-00000BAV80017898`, 06.08.1653, "mit Abschrift eines
  Berichtes ueber die politische Lage in Holland auf S. 3" (a copy of a report on the political situation in
  Holland enclosed) — a news-carrying letter from the same short run of 1653 correspondence as [22] (03.12.1653)
  and [23] (10.12.1653, this item), i.e. political/diplomatic content is present in this exchange around the same
  weeks the keys leaf was sent, but its own catalogue title does not claim cipher content.
- `terms=Schelhammer&holding_institution=Universit%C3%A4tsbibliothek+Erlangen-N%C3%BCrnberg&object_category=Briefe`
  (alternate spelling, per the collection's inconsistent transliteration) → 30 hits: 17 from a different sender,
  Christoph Schelhammer, to Volckamer I (1642-1651, `SCHELHAMMER_CHRISTOPH[1`-`[16`), and 13 from Guenther
  Christoph Schelhammer, mostly to Volckamer I and one to Johann Moritz Hoffmann (1682-1709,
  `SCHELHAMMER_GUENTHER_CHRISTOPH[1`-`[13`) — apparently family members of the addressee's correspondent circle,
  not the same sender as TR-1. None of these 30 titles mentions keys or Geheimschrift either.
- The prior scTREW pass (24 Sept 2026, logged in QUEUE.md) already ran an exhaustive `geheim*`/`Schluessel*`/
  `chiffr*`/`verschluesselt*`/`kryptogr*`/`Ziffer*`/`cifr*`/`steganograph*`/`geheimzeichen*` wildcard sweep against
  the **entire** ~19,563-record Trew facet (not just this sender), and found cipher/key mentions in exactly two
  records: BV1 (trew-posthius-1614-18, both leaves) and this one (TR-1). That sweep already rules out any other
  Trew letter's *catalogue title* claiming cipher content, sender-independent.

**No other letter in this correspondence, or in the collection, is catalogued as carrying a matching enciphered
passage.** If a message using these keys survives, it is either uncatalogued as such (bavarikon's descriptions are
terse and do not always flag cipher content, as this sweep's own false positives/negatives on wildcard terms show)
or was never committed to paper in this collection. Not investigated further this pass (would mean opening
individual letter images beyond the <=15-bavarikon-request/check-solved budget and brief scope — flagged below as
a follow-up for a recovery-lane worker, not actioned here).

## Verdict

**closed-negative** as a cryptanalysis target: a key-only leaf, no enciphered running text found on either page
of the digitised item at full native resolution. Not promoted to stage 2, not decoded, no novelty claim (rule
10) — nothing here to classify as read or unread.

**Kept as a possible key source** for the Nuremberg physicians' circle (Volckamer I recurs as recipient across
this collection, including trew-posthius-1614-18/BV1): if any *other* Trew letter to or from Volckamer I turns
out to carry unexplained ciphertext, these three tables (and BV1's SALUTEM-keyword table) are candidate keys to
test against it, in the shape of the sibling target's 1618 leaf. Not itself a target for a solver.

## Host requests this pass

`api.digitale-sammlungen.de`: 6 (2 `info.json` reachability/size probes, 2 full-page images at 2000px, 2
native-resolution region crops of the key block — one unrotated, superseded and deleted, one at IIIF rotation=270
kept). `www.bavarikon.de`: 2 (Schellhammer, Schelhammer catalogue searches, plain curl, no browser UA needed, no
challenge/429/403 seen) — well under the 15-request cap. No `kalliope-verbund.info`, no WebSearch, no WebFetch, no
github.com clones needed (six-source protocol not run — brief's conditional: keys-only skips it). No credentials
used, no subagents.

## Next steps (flagged, not actioned this pass)

- Biographical identification of Sigismund Schellhammer (not run this pass).
- If a solver/recovery worker later finds unexplained ciphertext on another Volckamer I letter in this
  collection (start with [21], the Holland-report letter from the same 1653 run), test these three key tables
  against it before assuming a new key is needed.
- The three key blocks here were read by eye for shape (grid dimensions, alphabet-vs-substitute rows), not
  transcribed cell-by-cell; a solver pass would need a proper transcription first.
