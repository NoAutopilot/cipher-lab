# BnF fr.16092 — Dépêches de la Cour à André Hurault de Maisse, ambassadeur à Venise, août 1582-décembre 1585

Status: open

Check-solved pass, 24 September 2026 (Sonnet, orchestrator brief for M13-M16). Not a full six-source check-solved
run; this is the editions-first + one-leaf pass the brief asked for. A formal check-solved (blind, six sources)
is still owed before this goes on the board at stage 2.

## What the target is

Gallica ark `btv1b90612993`, 932 canvases (all labelled `NP`, no 1:1 folio map). Full title/description via
`services/OAIRecord`:

> Dépêches originales de la Cour à André Hurault de Maisse, ambassadeur à Venise (1581-1588 et 1592-1596)... I
> Août 1582-décembre 1585. Très nombreuses lettres orig. de Henri III, 1582-1585 (f.12, etc.) — et de Nicolas de
> Neufville [Villeroy], 1582-1585 (f.7, etc.) ; Nombreuses lettres orig. de Catherine de Médicis, 1582-1585
> (f.15, etc.) ; ... Instructions orig. données à Mr de Maisse, août 1582 (f.1), et février 1583 (f.54) : Chiffre
> de la correspondance de Mr de Maisse (f.5).

This is the *first* of a two-volume run (fr.16092 = 1582-85, fr.16093 = 1586-96); the two are catalogued and
digitised separately.

## Checked (24 Sept 2026)

- Tomokiyo, "French ciphers during the Reigns of Charles IX and Henry III" (`henryiii.htm`), mirrored without a
  fresh fetch in `sources/cryptiana/web/` is absent, so read via a fresh shallow clone of
  `dbourdeau/cyphersolver` (`gallica_sweep/src/henryiii.txt` carries a full-text mirror of the same page).
  Verbatim: *"BnF fr.16092 (Gallica) contains 'La Clef du chiffre de Mr de Maisse Ambassadeur a Venise' (f.5).
  It is a numerical cipher as follows, but I have not seen its actual use. The many letters in BnF fr.16092 from
  Henry III (countersigned Neufville (i.e., Villeroy)) to de Maisse in 1582-1585 employs the following cipher,
  which is typical of the French ciphers at the time. The same cipher is also used in many letters in 1586 to
  May 1587 in BnF fr.16093 (ff.1-159)."* Per rule 10, this is quoted rather than paraphrased: Tomokiyo has
  reconstructed the key from the image but states plainly he has not confirmed it against an actual ciphertext
  passage in this volume.
- Fresh shallow clone of `dbourdeau/cyphersolver` (24 Sept 2026): the only Maisse work is `maisse1592/`, which
  covers fr.16093 (**not** fr.16092), a different, later cipher (1592-93), broken by aligning the ciphertext
  against clean 17th-c. clerk copies in Fonds Brienne (NAF 6984 = "Brienne Ms. 13") via the Berger de Xivrey
  pièce-number index — a different method (contemporary sibling clear copy) from what would be needed here (a
  cipher key never yet matched to a ciphertext passage). No hit on "16092" anywhere in the repo.
- Fresh shallow clone of `aaymeloglu/unsolved-ciphers` (24 Sept 2026): no hit on "16092", "Maisse" outside
  unrelated filenames.
- WebSearch: `"fr. 16092" OR "fr.16092" Maisse Venise Henri III chiffre clef` surfaced a GitHub PR
  (`dbourdeau/cyphersolver#7`, "Henri IV to Maisse, Venice 1592-93...") — confirms the above, still fr.16093.
  Also surfaced the archivesetmanuscrits.bnf.fr catalogue confirming fr.16092 covers Aug 1582-Dec 1585.
- Editions: *Lettres de Henri III, roi de France*, ed. Champion/François/Boucher, tome V (8 Apr 1580-31 Dec
  1582) and tome VI (4 Jan 1583-20 Mar 1585) cover exactly this volume's date range and are both published
  (2000, 2006). **Not resolved this pass**: whether Boucher's edition already prints any of these specific
  letters in clear (e.g. from a lost contemporary decipherment, the way Bourdeau found for fr.16093/Brienne).
  This is the single biggest open risk before committing a transcription budget — check her apparatus for
  "chiffré"/"déchiffré" source notes on fr.16092 items before transcribing.
- Gallica IIIF, one leaf and three extra probes (932-canvas volume, no reliable folio map; costs logged under
  Requests below): canvas 12 = the key itself, "La clef du chiffre de Mr. de Maisse Ambassadeur a Venise" (a
  numeral nomenclator: numbers 12-65 for names/places/words, a letter alphabet a-y as figures 40-61, nulls) —
  image saved `images/f12.jpg`. Canvas 20 = a plain-French clear extract of a royal letter, 1 Feb 1583
  (`images/f20.jpg`). Canvas 30 = folio 14, Villeroy to Maisse, clear French, no cipher (`images/f30.jpg`).
  Canvas 70 = folio 21, Villeroy to Maisse, 21 Jan 1583, clear French, no cipher (`images/f70.jpg`). **No actual
  ciphertext passage was located in this four-leaf sample** — consistent with, not contradicting, Tomokiyo's own
  "I have not seen its actual use." Folio-to-canvas offset is uncalibrated (canvas 12 sits near the key's stated
  f.5-f.9 but canvas 70 = folio 21, i.e. offset ≈ +49, similar to the +48/+49 offset Bourdeau found for the
  neighbouring fr.16093), so this is not a systematic sweep.

## Verdict

Open at stage 2 is **not yet safe to set** — the modern edition check is incomplete (see above), and this pass
did not confirm ciphertext actually appears in the volume, only that a key and several clear letters do. Grade:
no reading attempted, nothing to grade.

Cheapest next step, in order: (1) check whether Boucher tomes V/VI print any fr.16092 letter from a lost
decipherment (a few hours against her critical apparatus, no image fetches needed); (2) if that comes back
negative, page further into the volume (real folios roughly 25-105, i.e. canvas range roughly 74-154 at the
offset above) looking for actual numeral groups matching the f.5-f.9 key range, before transcribing anything.
This is exactly the fr.16093/Brienne pattern (Bourdeau, `maisse1592/NOTES.md`) one volume earlier — worth
checking whether an earlier Brienne volume (COLLECTION DE BRIENNE 11-12, before NAF 6984 = vol.13) covers
1582-85 and could do the same alignment trick here.

## Sources

- Gallica: `https://gallica.bnf.fr/ark:/12148/btv1b90612993`, OAI record via
  `https://gallica.bnf.fr/services/OAIRecord?ark=btv1b90612993`.
- S. Tomokiyo, "French ciphers during the Reigns of Charles IX and Henry III", cryptiana.web.fc2.com/code/henryiii.htm,
  read via `dbourdeau/cyphersolver`'s mirror (`gallica_sweep/src/henryiii.txt`), not our own `sources/cryptiana/`
  mirror (that copy does not include this page).
- github.com/dbourdeau/cyphersolver, `maisse1592/NOTES.md` (fr.16093, cite only, code MIT / text CC BY 4.0).
- github.com/aaymeloglu/unsolved-ciphers (checked, no relevant content; no licence, cite only, nothing copied).
- Champion/François/Boucher, *Lettres de Henri III, roi de France*, tomes V-VI (2000, 2006) — bibliographic
  identification only, text not consulted this pass.

## Requests this pass

gallica.bnf.fr: 1 OAI record + 4 IIIF image fetches (one connection reset on a later attempt for a different
target, not this one). github.com: 2 shallow clones (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers, both
deleted after grep). WebSearch: 2 queries.
