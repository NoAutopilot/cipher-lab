# Mercy 1648 mission: hunt for other cipher pieces (MERCY-SIB, 2 Oct 2026)

Worker MERCY-SIB (account 2, session_013og9Zxm3iWnEqMFXjdtfGy), 2 Oct 2026, 04:11-04:2x UTC (`date -u`).
Brief: `.claude/briefs/runs/2026-10-02-acct3-mercy-siblings.md`. Search and catalogue job only: no decoding, no
key, token, grade or class change. Status of the target is unchanged: `partial`, a cryptanalytic result (key `ours`).

Question: is there any other ciphertext of the 1648 Mercy mission (Leopold Wilhelm's secretariat <-> the abbé de
Mercy; Brandenburg, Cleves, Burgsdorff) that our `key.tsv` could be tried on?

**Answer: none reachable with an image online.** No cipher piece of the mission other than the target (BnF
Espagnol 144 f.22) was found in any catalogue or edition searched; the Brussels registers where Mercy's 1648
correspondence should sit (AGR SEE inv. 238-260, 576, 578) are catalogued with no digital object. Step 5 (fetch,
sample line, key vs 200 shuffled keys) therefore did not run: there was nothing to run it on.

## 1. AGR Brussels, Secrétairerie d'État et de Guerre (AGATHA)

`search.arch.be` is retired (R7-MSIB, `siblings_brussels.md` (2)); its successor AGATHA was used.

- Inventory record T 100, Gaillard & De Breyne, *Inventaire sommaire des archives de la Secrétairerie d'Etat et
  de Guerre* (1991): `https://agatha.arch.be/en/data/ead/BE-A0510_000027_002526`.
  - **Availability flag, quoted from the record page (2 Oct 2026):** "No digitised records exist for this
    inventory." and "Please note that non-digitised records also exist for this inventory." The page's generic
    consultation panel also carries "This item has been digitised but can only be consulted in the reading room
    of the National Archives." -- R7-MSIB (25 Sept) read that panel as the record's flag. The full EAD (below)
    has **no `<dao>` element on any of its 2,896 components**, which agrees with the first sentence, not the panel.
    So: **no item of T 100 is online; whether any is digitised for the reading room is not settled by AGATHA's
    page** (the panel text is shown for the inventory as a whole). ASKS row 60's wording "Digitised but
    reading-room-only per AGATHA" should be read with this caveat; ROOM flag raised, ASKS.md not edited here.
  - Full EAD fetched once: `https://agatha.arch.be/en/data/ead/BE-A0510_000027_002526.ead.xml` (941,486 bytes,
    sha256 2187aa48d089ef3f..., kept in the scratchpad, not committed; refetchable). Parsed offline; the items
    relevant to 1647-49 are in `siblings_1648_agr_items.tsv` (8 rows).
  - The printed inventory annexed to the record (`.../annexes/EP1548.pdf`, 71 pp., image-only scan, sha256
    9fd367cbebf52fdc...): pp. 45-46 read by eye. **No concordance from Lonchay's old tome numbers (t. LXIV,
    t. LXV) to the modern inventory numbers** on those pages or at the end (p. 71 ends at no. 2767); the EAD has
    none either (0 hits for "LXIV").
- What the catalogue gives instead:
  - **inv. 238-260**, "L'archiduc Léopold-Guillaume d'Autriche. Correspondance avec Philippe IV. 1647-1656."
    (23 parts, each dated only 1647/1656). Lonchay's "S.E.E. t. LXIV f.16" (the 15 April 1648 instruction to
    Mercy, joined to Leopold's dispatch to the king of the 18th) and "t. LXV ff. 181, 187, 205" (Aug-Sept 1648)
    must lie in this run, since it is the governor-to-king series for exactly those years; *which* part is not
    resolvable from the catalogue (inference, grade I). A reproduction order should cite "T 100 inv. 238-260,
    the part containing Leopold Wilhelm to Philip IV, 18 April 1648, f.16 (Lonchay's t. LXIV)".
  - **inv. 576**, "L'archiduc Léopold-Guillaume. Correspondance avec divers. 1647-1655." -- the likeliest home
    of Mercy's own 1648 reports to Brussels (inference).
  - **inv. 578**, "Don Martin Galarreta Ocariz, secrétaire. Correspondance avec divers. 1648-1672." (Lonchay
    p.445: Mercy and Galarreta acted together in 1648.)
  - **inv. 550**, "Don Ferdinand d'Espagne, cardinal-infant. Correspondance avec l'abbé de Mercy. 1639-1641." --
    a Mercy correspondence, but under the previous governor, seven years earlier (same years as BnF Espagnol 144
    items 4 and 6, both clear); not this key's period.
  - **inv. 2**, "Chiffre de la correspondance secrète. Liasse de chiffres divers. 1647-1698." -- the bundle
    already read in full through DECODE R958-R965 (NOTES.md U1, H17): no period key for this letter.
  - No item title in the whole inventory names Brandenburg, Cleves or Burgsdorff (0 hits).
- Requests: agatha.arch.be 4 (record page, EAD XML, PDF twice -- the first PDF request got a 302 without `-L`).

## 2. Brandenburg side

- *Urkunden und Actenstücke zur Geschichte des Kurfürsten Friedrich Wilhelm von Brandenburg*: **already searched
  in full by earlier passes, not repeated** (Usage 2-4): Bd. 1, 2, 4, 5 IA djvu grep and Bd. 6-13, 15, 17, 19 be-api
  fts (AUDIT.md section 4 row (b)); Bd. 3, 14, 16, 18 (AUDIT.md S2 item 7); Burgsdorf passages Bd. 1-6 (NOTES.md
  H43, H51). Hits with volume and page as recorded there: Bd. 4, Instruction für den Oberkammerherrn Conrad von
  Burgsdorf, Cleve 9 Febr. 1647, and the Spanish governor of Guelders' letter of 13 Feb 1647 forwarded to him; Bd. 2,
  Wicquefort to Lionne, Cleve 14 Jan 1648, and Schwerin to Wicquefort, Cleve 20 Feb 1648 ("M. le grand-chambellan");
  Bd. 1, a copy sent to Burgsdorf "nach Cleve", Königsberg 7 Oct 1648; Bd. 14 pt 2 index "Mercy, Franz, Freiherr,
  Feldherr" (the general, not the abbé). No volume names the abbé de Mercy, a Spanish envoy at Cleves in 1648, or a
  cipher. (Page numbers are in `h43/` and `h43/h51_hits.txt` where the earlier passes recorded them.)
- GStA PK finding aids: **unreachable from the cloud, 2 Oct 2026** -- `www.archivdatenbank.gsta.spk-berlin.de`
  CONNECT tunnel 502; `www.gsta.spk-berlin.de` connection reset. One request each, not retried.
- Archivportal-D (the national portal that carries GStA PK finding aids): plain curl gets the Anubis challenge
  (2 requests); `tools/browser_fetch.js` clears it but the search answers "Interner Serverfehler - 500" for
  `objekte?query=Mercy+Leopold+1648` and, after a 15 s pause, for `objekte?query=Burgsdorf` (2 requests). Stopped
  per the one-retry rule. **Unreachable, not negative.** (DDB_API_KEY is unset on this account, per `room.py --start`.)
- Europeana (keyed, 3 queries): `"abbé de Mercy"` 1 hit and `Mercy AND Leopold AND 1648` 1 hit -- both are BnF
  `btv1b10035717h`, the volume holding our own target (a positive control for the search); `Burgsdorf AND 1648` 0.

## 3. AGS Estado (Flandes) 1648

PARES is dead from the cloud (CLAUDE.md host table). Used the cached PARES sweep in Aymeloglu's repository
(github.com/aaymeloglu/unsolved-ciphers, `catalogue/pares-hits.jsonl` 1,115 rows, `pares-pages.jsonl` 501,
`pares-images.jsonl` 536; shallow clone at d2800bb, 27 Sept 2026; data grepped, no code used or copied -- the
repository has no licence; credit to A. Aymeloglu). Its queries are cipher terms only ("carta cifrada", "cartas
cifradas", "en cifra", cifrada, cifradas, descifrada), 422 AGS rows. **No row names Mercy/Merci, Brandenburg,
Cleves, Burgsdorff or Leopoldo Guillermo** (whole-word match; "merc-" hits are all *mercaderes*). The 1645-1650 rows
are AGS EST leg. 3600 and 3602 (Genoa), AHNob Osuna/Frías (Rome, Naples) and AHN Estado 1152 (Castel Rodrigo-
Peñaranda 1649-68): none is the Flanders secretariat or the Mercy mission. So the sweep **does not cover** AGS Estado
Flandes 1648 (its query set would only catch legajo-level descriptions using a cipher word). The AGS Estado Flandes
legajos for 1648 remain unchecked at catalogue level; next step needs PARES from a non-cloud browser (LOCAL-QUEUE
route), not attempted here.

## 4. What this leaves

- No sibling ciphertext to try the key on. The key's only test material remains f.22 itself.
- The two archival places a sibling would be (AGR SEE inv. 238-260 part for April 1648, and inv. 576/578) have no
  online image; a reproduction order or reading-room visit is the only route (ASKS row 60; the draft
  `outreach/agr-mercy-quote-form.md` can now cite the modern inventory numbers above instead of Lonchay's tome).
- AGS Estado Flandes 1648 and GStA PK are uncatalogued here: both need a route the cloud lacks.

## Request counts (2 Oct 2026)

agatha.arch.be 4; archivportal-d.de 4 (2 curl, 2 browser); archivdatenbank.gsta.spk-berlin.de 1; gsta.spk-berlin.de
1; api.europeana.eu 3; github.com 1 (shallow clone). No credential printed.
