closed-negative

# "Carta que foi por çifra" -- vice-roi de l'Inde (comte de São Vicente) to king Alphonse VI -- BnF Portugais 33

QUEUE row: M29 (`sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv`, LANE G2 worker F's archivesetmanuscrits
item-level sweep). First Portuguese-language candidate this lane has scored.

## Source

BnF, Portugais 33 (Suppl. français n. 4022), `ark:/12148/cc35168g`. One item ("no. 1") in a short series of
three letters from the Portuguese viceroy of India, **D. João Nunes da Cunha, count of São Vicente**, to king
**Afonso VI**, 1667-68, explicitly named apart from its two plain siblings: "Carta nº 1 que foi por çifra"
(letter sent in cipher), dated 1667, conveyed by the galleon São Bento (captain Jerónimo Carvalho). Not
fetched at gallica.bnf.fr or archivesetmanuscrits.bnf.fr this pass per the brief; catalogue text only, no
image viewed. Not in either solver repo's curated candidate list by this shelfmark (see Exclusion below) or
DECODE.

## Check-solved sweep (24 September 2026)

1. **Search engine.** `"Portugais 33" BnF vice-roi Inde Alphonse VI cifra 1667` -- surfaced the BnF Archives
   et manuscrits notice itself (`cc35168g`) and confirmed the catalogue description (viceroy São Vicente to
   Afonso VI, 1667-68, one item "por çifra"); no cipher-specific discussion, edition, or decipherment
   surfaced.
2. **Printed correspondence / calendars.** `"São Vicente" "Documentos Remettidos da Índia" OR "Monções do
   Reino" 1667 vice-rei Alfonso VI` -- the Bulhão Pato/Academia das Ciências de Lisboa edition of *Documentos
   Remettidos da Índia ou Livros das Monções* is the standard published series for exactly this kind of
   viceroy-to-crown correspondence, but the volumes found and sampled this pass (a 1625-1627 Internet Archive
   volume, several Macau-library tomes) cover an earlier reign window; no volume covering 1667 (Afonso VI's
   reign, São Vicente's viceroyalty) was located or opened -- the edition's later-volume coverage was not
   confirmed either way this pass, a genuine gap, not a checked-and-clear result.
3. **Cryptiana.** Local snapshot grepped for "Portugais 33", "São Vicente", "cifra": no hit.
4. **Cipherbrain.** No dedicated query run; this is the lane's first Portuguese-language item and no prior
   Cipherbrain coverage of Portuguese colonial cipher correspondence is known to this repo.
5. **DECODE.** Aymeloglu's cached `catalogue/decode-catalog.csv` (10,107 rows) grepped for "portugais",
   "vicente", "vice-roi", "viceroy": zero hits for any. This repo's own local harvest also has no matching row.
6. **Solver repositories.** Fresh shallow clones of both repos grepped for "Portugais 33" and the ark
   (`cc35168g`) exactly. **One non-curated hit**: `dbourdeau/cyphersolver/gallica_sweep/sru_chiffre_desc.json`
   carries a raw, unfiltered Gallica SRU scrape entry for "Portugais 33" (Gallica ark `btv1b104629623`,
   distinct from the archivesetmanuscrits ark `cc35168g` above -- the two identifier spaces for the same
   physical item) with a matching description ("Lettres du roi Alphonse VI au viceroi de l'Inde... 17 décembre
   1667"). This item was already flagged by the M22-M34 harvest pass's own Exclusion section: it appears only
   in Bourdeau's raw unfiltered scrape, **not** in his curated candidate list (`gallica_sweep/bnf_candidates.
   txt`, checked again this pass -- zero hits for "Portugais 33" or "6829"/"4764"/etc.), so it is kept per the
   established convention that only the curated list counts as "already on his radar". No hit in
   `aaymeloglu/unsolved-ciphers` for the shelfmark or either ark.

## Verdict

**Open, stage 2 verified unsolved (conditional).** Not found in a search engine, Cryptiana, DECODE's cached
catalogue, or either solver repository's curated list (present only in Bourdeau's raw, uncurated scrape data,
already logged and excluded from counting as prior coverage), searched by shelfmark and both arks on 24 Sept
2026. Conditional because the Documentos Remettidos da Índia edition series' coverage of the 1667-68 window was
not confirmed -- a future worker should check whether a later Bulhão Pato tomo (or a successor editor's
continuation) reaches Afonso VI's reign before treating this as clear of print.

Requests: WebSearch 2 queries. github.com 0 new (reused clones). No gallica.bnf.fr, no
archivesetmanuscrits.bnf.fr fetch. No subagents.

## Digitisation check (24 Sept 2026, LANE G2 worker O)

**Digitised: yes, ark `btv1b104629623`, item at canvas f263 (label "129r" checked).** The archivesetmanuscrits
finding aid (`https://archivesetmanuscrits.bnf.fr/ark:/12148/cc35168g`) links the digitised copy directly (a
static href, "Consultable sur gallica" / "Voir le document numérisé"), stated as "Numérisation effectuée à
partir d'un document original : Portugais 33" -- the whole volume, matching our target's shelfmark exactly.
The finding aid's own item list places "Carta n° 1 que foi por çifra por via de Olanda e Inglaterra..." at
**F. 129-141** (item "a" under item 3, "Série de lettres...1667 et...1668"). `tools/gallica_folio.py
btv1b104629623 --folio 129` found a single constant offset (k=6) across all 520 labelled canvases and returned
canvas **f263**, labelled "129r" (3476x5051), confirming folio 129 recto. Status stays open (a capture worker
can now proceed; not blocked).

Requests this section: gallica.bnf.fr 1 (`gallica_folio.py` manifest fetch).

## Capture and passes (24 Sept 2026)

**No cipher text present in the pinned item -- the whole thing is read as plain running Portuguese secretary
hand.** Fetched 1000px views of every canvas of the pinned item (f263-f288, folio 129r-141v, the finding aid's
item 3a "F.129-141") from `https://gallica.bnf.fr/iiif/ark:/12148/btv1b104629623/f{canvas}/full/1000,/0/native.jpg`
and read each one by eye (images in `images/overview/`, manifest in `images/manifest.json`). No numerals,
symbols, or any non-alphabetic ciphertext appear on any of the 26 canvases; every recto carries ordinary
Portuguese cursive prose, and every verso is either blank or shows only ink bleed-through/offset from the
facing page. Per-canvas summary:

| canvas | folio | content |
|---|---|---|
| f263 | 129r | Letter opens "N°.1", marginal "Snor" note: "Por Via de Olanda e Ingraterra remeto estas cartas..." -- the viceroy explaining he sends duplicate letters by the Holland/England route "porque não he seguro" the overland route; India-fleet and Canará news. Plain prose throughout. |
| f264 | 129v | Continues: Bombaim, Mogor, Danda affairs. Plain. |
| f265 | 130r | Continues: Mombaça, Canará, China/"Iquam" affairs. Plain. |
| f266 | 130v | Letter closes "Goa 21 de Setembro de 667"; a new dated paragraph follows ("Depois de ter dado a VMg^e conta..."), a postscript/continuation to the same numbered letter. Plain. |
| f267 | 131r | Postscript continues: India's poverty, Cochim/Cananor. Plain. |
| f268 | 131v | Postscript continues: Dutch/English trade, Dom Jeronimo Manoel, Mogor. Plain. |
| f269 | 132r | Postscript ends ("Comfirm Utilidade"), Angola discovery news; blank lower two-thirds; page numbered "1" bottom-right, marking the start of a fresh internal item. Plain. |
| f270 | 132v | Blank except faint bleed-through of f271's text; page numbered "8" top-right (end of an 8-page enclosure). |
| f271 | 133r | New heading "Copia do escrito que o S. Conde V.Rey [fez] a Relação sobre os papeis de Bombaim", dated Goa 1 Julho 1667 -- a copied enclosure, not the letter itself. Plain. |
| f272 | 133v | Continues: copied opinions ("pareceres") of the chanceler, juiz dos feitos, on the Bombaim dispute. Plain. |
| f273 | 134r | Continues: more copied "pareceres"/petições on Bombaim jurisdiction; a wax-stamp/library seal reproduced mid-page. Plain. |
| f274 | 134v | Continues: Bombaim capitulação clauses. Plain. |
| f275 | 135r | Continues: Bombaim/Mayim jurisdiction, Dona Ines de Miranda's claims. Plain. |
| f276 | 135v | Continues: same dispute, named individuals (Bernardim de Tavora etc). Plain. |
| f277 | 136r | Continues: same dispute, more named individuals. Plain. |
| f278 | 136v | Continues: same dispute; ends with a long witness list (dozens of names). Plain. |
| f279 | 137r | Notarial "Justificações" certifying the witnesses' signs/signatures, Tanna, 6 Junho 1667. Plain. |
| f280 | 137v | Blank except faint bleed-through of f281. |
| f281 | 138r/138 | "Copia do assento do conselho do governo", Panelim 27 Abril 1667 -- council minute on the Bombaim handover. Plain. |
| f282 | 138v | Blank recto-side, only mirrored bleed-through of f281 visible. |
| f283 | 139r/139 | Headed "a cuja a carta seg.° N°.1° [capítulo] [primeira]" -- the viceroy's own reply letter re Anglo-Dutch relations, Bombaim, Olanda. Plain. |
| f284 | 139v | Continues: Mogor, Turco, Holandezes/Ingrezes in Azia. Plain. |
| f285 | 140r/140 | Closing lines only ("...com tanto que VS se emmende...esfavorecelo"), rest of page blank. Plain. |
| f286 | 140v | Blank except faint bleed-through of f287. |
| f287 | 141r/141 | "Copia a n°1 do primeiro [capítulo]", marginal "C.rua El Rey Carlos 2°" -- a copy of a letter from Charles II of England to Afonso VI re Bombay's transfer. Plain. |
| f288 | 141v | Blank except faint mirrored bleed-through of f142r (start of the next, sibling item in the series). |

**Reading of the evidence.** The finding aid's note "Carta n° 1 que foi por çifra por via de Olanda e Inglaterra"
describes how the letter was *conveyed* (enciphered, sent via the Holland/England route rather than overland,
for security), not what survives here. What is bound at F.129-141 is a legible plain-language chancery copy of
that letter plus its enclosures (Bombaim-dispute papers, a council minute, a copy of Charles II's letter) --
consistent with the ordinary practice of a viceroy's secretariat keeping a readable register/minute copy of a
letter that was enciphered only for the journey. No ciphertext object (numerals, a nomenclator, symbol
substitution, or any non-alphabetic notation) appears anywhere in the 26 canvases making up this item. There is
therefore nothing here for a cryptanalytic or key-recovery campaign to work on; steps 2 and 3 of the brief
(crops, blind transcription passes, `dechiffre.txt`) do not apply -- there is no cipher leaf to crop and no
decipherment to transcribe, since the surviving document already is the plain text.

This is a capture-stage finding (rule 2, image over transcription: read from the page image, not the
catalogue's transcription/description), not a claim about the letter's content or novelty (rule 10 not engaged
-- no reading is being reported, cryptanalytic or otherwise). Status set to `closed-negative`: the campaign on
this specific digitised item is closed because it carries no ciphertext, not because a cipher resisted attack
(rule 3's matched-control requirement does not apply to an item that contains no cipher at all). If a matching
enciphered original of this letter survives elsewhere (e.g. among Overseas Council or Conselho Ultramarino
papers, or in a different Lisbon/Goa fundo), it was not searched for this pass; a future worker could widen the
search past this one digitised codex if the person wants that pursued, but Portugais 33 itself is exhausted for
this letter.

Requests this section: gallica.bnf.fr 28 (26 canvas fetches + 2 retries after `ws_closed_mid_exchange` tunnel
resets on f263 and f271/f279, one retry each per the good-citizen rule, all eventually HTTP 200). No
archivesetmanuscrits.bnf.fr, no subagents. Images kept in `images/overview/` (5.3 MB, under the 30 MB cap);
`images/manifest.json` records the fetch. Well under the $6 cap.
