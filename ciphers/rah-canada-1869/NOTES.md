open

# "Nota cifrada del Conde de la Cañada" — RAH Sig. 9/6958 (1869)

QUEUE row: N2, "Digitised candidates outside the BnF (scout of 24 September 2026)" (RAH section). Single
named ciphered note inside an exchange between Queen Isabel II (in exile since the September 1868
revolution) and her former Minister of the Interior Luis González Bravo. RAH Sig. 9/6958, Legajo XIX, Nº
117, record id 14495, Real Academia de la Historia, Madrid. Different reign/collection from rah-morillo-1817
in this same batch; no key lead found in the QUEUE scoring pass, and not checked against that cluster's
material there either.

## Editions-first check (24 September 2026)

No dedicated documentary edition of Isabel II's exile correspondence with González Bravo, nor a biography of
either that names this specific note, was found. WebSearch (`"Conde de la Cañada" cifrada Isabel II González
Bravo 1869`; `Isabel II correspondencia cifrada 1869 exilio González Bravo clave`) returned only general
histories of the 1868 revolution and Isabel II's exile (Historia Contemporánea articles on "el primer exilio
de Isabel II" and "González Bravo o el final de la era isabelina"), numismatic/philatelic pages (1869 coins
and stamps bearing Isabel II's image — noise), and one archival lead worth recording: the Real Academia
Española (RAE, a different institution from the RAH holding this target) catalogues "Copias de cartas de
Isabel II de los años 1869 a 1871" at `archivo.rae.es/copias-de-cartas-de-isabel-ii-de-los-anos-1869-1871`.
One WebFetch attempt on that page returned HTTP 403 (not retried, per the good-citizen one-retry rule); its
contents (whether it holds copies of this exact exchange, or mentions a cipher) are unchecked. Neither of
the two Historia Contemporánea articles found by search was fetched in full this pass (budget; both are
general political narratives of the exile period, not archival catalogues, and neither surfaced in a snippet
mentioning cipher or Cañada).

## Six-source sweep (24 September 2026)

1. **Web.** Covered above under editions-first (the two searches serve both purposes for this small,
   single-item target).
2. **Print.** No CSP/HMC-equivalent calendar exists for this collection; no biography of Isabel II or
   González Bravo found describing a ciphered note at this shelfmark.
3. **Community lists.** `sources/cryptiana/` grepped for "Cañada"/"Canada" (accent-insensitive), "González
   Bravo", "Isabel II": all hits are false positives on the country name Canada (John A. Macdonald's
   ciphered telegrams, the Slater/Bolton codebooks) in `unsolved.htm`, `civilwar1.htm`, `codebreaking.htm`,
   `blog/index.html` — none is the Spanish title "Conde de la Cañada." No genuine match.
4. **DECODE.** No login attempted (broken, ASKS row 1). Aymeloglu's cached DECODE/BNE/PARES catalogues
   (`unsolved-ciphers/catalogue/*.jsonl`, `*-ranked.md`) grepped for "Cañada", "González Bravo", "Isabel
   II", "9/6958", "14495": no match.
5. **Bourdeau's repository.** Fresh shallow clone, 24 Sept 2026 (shared with the rest of this batch). No
   target folder or catalogue mention; the handful of "Cañada"/"Canada" hits in the tree
   (`napoleon/unsolved.txt`, `cobham1588/wordfreq.tsv`, `gallica_sweep/sru_results.json`, corpus/source
   files) are all incidental (the country name in period French/English/Spanish corpus text, or a
   frequency-table row), not this target.
6. **Aymeloglu's repository.** Fresh shallow clone, 24 Sept 2026 (shared). No target folder, no README/
   TARGETS/SHORTLIST/CATALOGUE mention, no PARES/BNE/DECODE scrape row.

**Google Books sweep (24 September 2026, LANE S worker H, holding the Google Books slot — key+country=US,
filter=full):** 3 queries run, >=2s apart. `Isabel II González Bravo 1869 nota cifrada clave` and `"9/6958"
RAH Isabel II` returned zero results. `"Conde de la Cañada" Isabel II cifrada` returned 2 hits, both
*Diario de las sesiones de Cortes* (Spain, Congreso de los Diputados, 1860) — parliamentary session records
that separately mention "Isabel II" and a different "conde de la Cañada" (a deputy's title, in an 1860
procedural context) with no connection to a ciphered note or to 1869; a coincidental co-occurrence of both
search terms, not a hit on this item.

## Verdict

**open**, stage 2 verified unsolved (conditional: the RAE letters catalogue and the two Historia
Contemporánea articles found by search are unread, and Google Books is outstanding). No source in this
sweep identifies, quotes, or describes the content of this note. Single item, no key lead identified in the
same collection (unlike rah-morillo-1817's item 2 in this batch, whose covering letter names an "adjunta
clave"): a genuine cryptanalysis candidate if pursued, though the RAE letters catalogue is worth a look
first (route 2 of CLAUDE.md's Access playbook, browser tool, since the plain GET returned 403) in case it
turns out to hold a plaintext copy of the same exchange.

## Access notes and interlinear decipherment (24 September 2026, LANE R worker R4)

**Working image route (bypasses the site's Anubis bot-challenge):** every plain path on
`bibliotecadigital.rah.es` (`registro.do`, `catalogo_imagenes/grupo.do`, `resultados_busqueda.do`, and the
`imagen_id.do` image endpoint itself) sits behind the site's Anubis JS proof-of-work challenge -- curl always
gets a 307 to `/.within.website/?redir=...` (confirmed again this pass) and never solves it. The site's own
OAI-PMH endpoint (`/oai/oai.do`) is **not** behind Anubis and answers plain curl. `verb=GetRecord` with
`metadataPrefix=didl` (not the default `oai_dc`, which only gives the `grupo.do` group-viewer link) returns a
`didl:Resource` entry per page image, each `ref` a direct `.../i18n/catalogo_imagenes/imagen_id.do?idImagen=NNNNNNNN`
URL:
```
curl -A "Mozilla/5.0 ..." "https://bibliotecadigital.rah.es/oai/oai.do?verb=GetRecord&identifier=oai:bibliotecadigital.rah.es:14495&metadataPrefix=didl"
```
Those `imagen_id.do` URLs are themselves still behind Anubis for curl. A real headless Chromium
(`tools/browser_fetch.js`) clears the challenge, but intermittently -- of about 8 attempts this pass, one
returned the real page/image on the first try, several returned Anubis's own unsolved challenge page ("Anubis
could not load its JavaScript. The server may be overloaded."), one returned a bare "upstream request
failed". `tools/browser_fetch.js` gained a `--binary` option this session (saves the navigation response's
raw body instead of `page.content()`, retrying the navigation up to `--retries` times, default 3, until the
content-type isn't `text/html`) which made the five image fetches reliable:
```
NODE_PATH=$(npm root -g) node tools/browser_fetch.js "<imagen_id.do URL>" OUT.jpg --profile /tmp/rah_profile --binary
```
This route is worth reusing for `rah-morillo-1817` (already has three record ids and a note that
`imagen_id.do` serves real JPEGs but was "not opened") and for E1 `rah-xiquena-1868` (whose `grupo.do` viewer
"did not yield a static image URL to curl" -- the OAI didl route should).

**The record is two items, not one.** `record id=14495`'s five page images (`images/manifest.json`) are: pp.1-3
(`10137299`-`10137301`) Luis González Bravo's covering letter to the Queen, clear Spanish, Biarritz, 18 Nov
1869 ("La mejor respuesta que puedo dar ... es el envio de la adjunta nota del Conde de la Cañada. La remito
tal y como ha sido recibida" -- "I send it exactly as received"); pp.4-5 (`10137302`-`10137303`, foliated
"Leg. XIX, nº 117/2" and "/3") the "nota cifrada" itself.

**The nota cifrada is interlinear: the plaintext is already in the document.** Every clear Spanish
line/sentence on 117/2-3 is followed directly below it, same hand, by that same sentence's own cipher
encoding (digits plus a set of pen-drawn marks -- see `glyphs/atlas.md`). E.g. "Ruega al Sr. D. Luis Gonzalez
Bravo, haga llegar a manos de S.M. la Reina, la carta que en forma de nota se estampa a continuación..." each
have a cipher line beneath them; the note closes "Señora: Tengo el mas alto honor en felicitar muy
cordialmente á V.M. en el dia de su santo... A.L.R.P. de V.V. Ms.M. y Real familia con el mas profundo respeto
y veneracion." This means the plaintext for this item does not need to be searched for in print or
cryptanalysed -- it is written on the same leaf as the cipher, so a straightforward alignment (grade C, from
known plaintext) reads the whole nomenclator once the two are lined up. Flagged in ROOM.md 2026-09-24 05:17
UTC per this brief's instruction ("if there is any interlinear or separate decipherment... that makes this
recovery"); **not decoded or aligned by this worker** (out of this brief's scope -- access + transcription
only).

**Symbol set.** Mixed Arabic digits (0-9) and roughly a dozen recurring pen marks (a raised dot, a
cross/dagger, a plain plus, a circle-with-interior-mark, a plain circle/oval, an equals sign, a short dash,
one- and two-hump cursive loops, a larger looping flourish, a small hooked stroke, an accent tick) -- see
`glyphs/atlas.md` for the working legend built before the two blind passes, and `images/inventory.tsv` for
the per-page breakdown. Not yet an established codebook (no key or table found on these five pages;
González Bravo's letter gives no indication one exists elsewhere in this small file) -- the interlinear
plaintext supplies the reading without one.

## Transcription passes (24 September 2026, LANE R worker R4)

Two blind Sonnet subagent passes from `images/10137302.jpg` and `10137303.jpg`, each given only the shared
symbol legend (`glyphs/atlas.md`) and not shown the other's output or this worker's own reading:
`passA.tsv` (26 cipher lines: p302_c1-c21, p303_c1-c5; 115 tokens) and `passB.tsv` (25 cipher lines:
p302_c1-c20, p303_c1-c5; 113 tokens) -- the one-line difference on page 1 is a boundary call both passes
flagged independently (whether a short cipher fragment that shares a row with the next sentence's opening is
its own line or the tail of the previous one). `tools/reconcile_passes.py passA.tsv passB.tsv --crops images`
(Needleman-Wunsch, default settings): **10/131 aligned columns agree (7.6%)**, well below every other target's
first-pass agreement in this repo (Gramont f.30: 59.5%) -- `disagreements.tsv` (121 rows), `ciphertext_draft.tsv`
and `agreement.tsv` written, not settled (out of this brief's scope; a reconciler pass belongs to whoever picks
this target up next). Distinct atomic symbol codes seen across both passes: 24 (digits 0-7 and 9 -- no pass
transcribed an 8 anywhere on these two pages; literal `.` `,` `+` `-` `=` where a pass read a mark as ordinary
punctuation; and ten `glyphs/atlas.md` bracket labels: `[bigloop] [circle] [circledot] [cross] [dash] [dot]
[equals] [hook] [loopm] [loopn]`). Both passes independently named the same handful of look-alike pairs as
their main source of disagreement before any reconciliation was run: a hooked/flag-shaped stroke read as
digit 1 by one pass and flagged as "could be 7" by the other; a curling mark read as digit 9 by both but
flagged uncertain by one; and the general `[circle]`-vs-digit-`0` distinction the atlas itself warned about.
Neither pass needed a new `[gNN]` label. **No key or additional decipherment table found anywhere in these
five pages** beyond the interlinear plaintext itself (see Access notes above) -- the covering letter gives no
indication a separate key exists in this small file.

## Copy status

Copy-free (per the 23-24 Sept scout): `bibliotecadigital.rah.es`, public domain / CC PDM, no login. Record
page re-checked reachable this pass (`registro.do?id=14495`, HTTP 307, consistent with the site's session-
redirect behaviour noted in QUEUE.md's caveats; not followed further, no image opened). No REQUEST.md
needed.

## Request counts (this target)

WebSearch: 2. archivo.rae.es: 1 (WebFetch, HTTP 403, not retried). bibliotecadigital.rah.es: 1 (record-page
reachability only; shared with rah-morillo-1817's budget in this batch — 4 of the 20-request cap used across
both RAH targets this session). github.com: shared clone with the rest of this batch. No TNA Discovery calls
(n/a). www.googleapis.com/books: 3 (24 Sept 2026, LANE S worker H, key+country=US, never printed; see Google
Books sweep above).

**24 Sept 2026, LANE R worker R4 (access + transcription pass):** bibliotecadigital.rah.es: curl ~9 (4 OAI-PMH
calls -- Identify, ListMetadataFormats, GetRecord oai_dc, GetRecord didl, all 200 with no challenge; 5 direct
path attempts -- registro.do, catalogo_imagenes/grupo.do, resultados_busqueda.do -- all 307 to the Anubis
challenge, confirming the playbook note, none retried beyond the one-retry limit); `tools/browser_fetch.js`
(headless Chromium) ~14 (7 HTML/page navigations while diagnosing the Anubis flakiness, most either the
challenge page or a transient "upstream request failed"; 7 `--binary` image fetches for the 5 target images,
2 needing a retry). All >=1.5 s apart, single fetcher, descriptive UA except where the site's own challenge
needed a browser UA per the playbook. No login, no other host touched this pass. 2 Sonnet subagents (the two
blind transcription passes), within the $8 cap.
