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
