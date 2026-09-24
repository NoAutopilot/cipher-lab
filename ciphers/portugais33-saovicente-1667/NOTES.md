open

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
