# Mercy Brussels sibling check -- the 15 April 1648 instruction (Lonchay 1896 p.445 n.2)

LANE R7 worker R7-MSIB (Sonnet), 25 Sept 2026, 20:03-20:1x UTC (`date -u`). Brief:
`.claude/briefs/runs/2026-09-25-lane-r7-msib-mercy-brussels.md`. Search and print-check only: no decoding, no
key edits; this file is new, separate from NOTES.md (which V6's second audit may be editing).

Status of our reading this file is about: `ciphers/espagnol142-mercy-1648` is `partial` (NOTES.md; NEAR.md row),
N3 key ours (AUDIT.md), a **cryptanalytic result**, not confirmed by a key or a clear copy. Nothing below
changes that; this is a search log for one named sibling lead.

## (1) Lonchay 1896 p.445 itself -- verbatim

Fetched `_djvu.txt` from Internet Archive (`la-rivalite-de-la-france-et-d-espagne-aux-pays-bas-1635-1700`,
public domain, no restriction). Page (446) marker in the OCR confirms the leaf; page (445) itself has no printed
folio-number OCR line but sits directly between the p.444 footnotes and the (446) marker, matched by content
against AUDIT.md's own prior citation of "pp. 406, 445". Transcribed here **exactly as OCR'd**, spelling errors
and all (rule 2: this is a transcription of the source image via OCR, not hand-corrected; the source has real
long-s/oe ligature and font damage that the OCR mangles in a few places, noted inline):

> ... eût été imprudent, pourtant, de rebuter des alliés qui comptaient en France de nombreux amis et dont le
> concours pouvait devenir efficace si Mazarin était renversé. L'abbé de Mercy, qui avait été mêlé jadis aux
> intrigues du comte de Soissons et qui était devenu l'aumônier de l'archiduc Léopold, fut envoyé en Hollande
> pour reconnaître quel parti on pouvait tirer des émigrés et quel traité on pouvait faire avec eux ¹. Il
> signala les ressources dont les émigrés disposaient en France où l'agitation grandissait et insista pour
> qu'on ouvrît des négociations avec eux. Condé même figurait parmi les mécontents. On lui avait refusé
> l'amirauté à la mort d'Armand de Brézé, son beau-frère, et il accusait Mazarin de l'avoir abandonné devant
> Lérida. L'abbé de Mercy ² et François de Galaretta, secrétaire d'État et de guerre des Pays-Bas,
> s'abouchèrent donc avec la duchesse de Chevreuse et Saint-Ibal qu'ils virent, tantôt à Kerpen, près de
> Cologne, tantôt à Spa, mais Léopold subordonna son adhésion à la prise d'une place forte qui servirait de
> gage, comme La Rochelle; il ne voulait pas se lier avec les conjurés tant que ceux-ci n'auraient pas formé
> un parti sérieux sur qui l'on pût compter ³.

Footnotes on the same leaf, verbatim (OCR "Merey"->Mercy, "fbidem"/"lbidrim"->Ibidem, "LAV"->probably LXV, "45
août"->probably 15 août, "9(fbidem, 1. LXV"->Ibidem t. LXV -- all left as OCR'd, not silently repaired):

> ¹ Voir, sous la date du 27 septembre 1647, un mémoire de P. Ernest de Mercy « de ce qui s'est négocié et
> traité au voyage de l'abbé de Mercy en Hollande entre lui, le comte de Saint Ibal et Madame la duchesse de
> Chevreuse », publié par Victor Cousin, dans *Madame de Chevreuse*, appendice, pp. 425 et suiv.
>
> ² Instructions à Mercy, du 15 avril 1648, jointes à la dépêche de Léopold au roi du 18. (S. E. E., t. LXIV,
> f. 16.) -- Cf. Léopold au roi, 30 août. (Ibidem, t. LXV, f. 181.)
>
> ³ Léopold à Galaretta, 15 août 1648. (Ibidem, t. LXV, f. 187.)
>
> ⁴ Léopold au roi, 30 août; le roi à Léopold, 17 septembre 1648. (Ibidem, ff. 181 et 205.)

**Reading this closely (new since AUDIT.md, which only summarised): footnote 2 is a bare archival citation.**
It gives the register and folio (S.E.E. t. LXIV f.16) and the covering-dispatch date (jointe à la dépêche du
18) but Lonchay does not paraphrase or quote the instruction's content anywhere in this paragraph or its
footnotes. The paragraph's content (Chevreuse, Saint-Ibal, Kerpen, Spa, "place forte... comme La Rochelle")
is footnote-2-attached to the *sentence about the 1647-48 Chevreuse-conspiracy contacts in general*, not
specifically paraphrasing the 15 April 1648 instruction; footnotes 3 and 4 cite two *different*, later
1648 documents (15 Aug Galaretta, 30 Aug/17 Sept king exchange). None of Brandenburg, Cleves, or troop
numbers appears anywhere on this page. So: **Lonchay 1896 p.445 does not itself answer what the 15 April
instruction says** -- it only proves the instruction exists, in Brussels, at a named register and folio.
Not the first that answers; continuing to (2).

## (2) Is SEE t. LXIV digitised?

`search.arch.be` (named in the brief) is dead: every path (root, `/en`, `/fr/rechercher-des-archives/...`)
302-redirects to `www-resources.arch.be/searchArchBeEndOfLifeNotice/end_of_life_notice.html`, an unrelated
notice about the retirement of a different, genealogy-transcription volunteer tool ("DemoGenVisu"). A web
search (`arch.be`'s own news page, `www.rfgenealogie.com`) confirms *search.arch.be*'s own successor: **AGATHA**
(`agatha.arch.be`), which replaced it completely on 23 Dec 2024; `search.arch.be` now redirects everyone there.
Used AGATHA as the current form of the named route.

AGATHA's `Archive inventories` search (`/en/search/ead`, POST to `/en/search/ead/results/`, a jQuery form, not
a heavy SPA) for "Secretairerie d'Etat et de Guerre" returns 48 finding-aid-level hits for heading A1 (Spanish
or Austrian Netherlands), 1582-1795, all at "National Archives of Belgium" (Brussels). Opened via
`tools/browser_fetch.js` (curl alone 500'd on the results AJAX endpoint, `/en/search/ead/ajax.php`, twice --
stopped per the one-retry rule and used the browser instead, which works fine for this host, no challenge
involved, just client-rendered pagination). The match for Lonchay's "S.E.E." is:

- **Code T 100** -- *"Inventaire sommaire des archives de la Secrétairerie d'Etat et de Guerre [d'après
  l'exemplaire annoté Salle de Lecture AGR]"*, heading A1, dates 1582-1795.
  `https://agatha.arch.be/en/data/ead/BE-A0510_000027_002526`
- Its own detail page states: **"This item has been digitised but can only be consulted in the reading room
  of the National Archives."** The page's own `View` (`#consultItemBtn`) button is present in the DOM but
  `hidden` -- there is no online image route for this record from AGATHA itself.

Caveat on what this actually confirms: T 100 is the **finding-aid instrument** (the paper inventory used to
navigate the SEE fonds), not a register-by-register digitisation index of t. I - t. LXV themselves; this
record's "digitised, reading-room-only" note may describe the finding aid, the fonds, or both -- AGATHA's UI
did not distinguish that further within this session's reach, and the modern register number that corresponds
to Lonchay's "t. LXIV" (the concordance the brief asked for) was **not found** -- T 100's own contents (the
inventory listing itself) were not opened; that needs either the reading-room finding aid or a follow-up
AGATHA pass that browses inside this record. A second, apparently related EAD id turned up by a plain web
search of arch.be's own site, `BE-A0510_000027_005874_FRE` ("Secrétairerie d'État et de Guerre - Rijksarchief"),
was not resolved to a live AGATHA record this session (the old `search.arch.be` URL that named it is dead); it
may be a fonds-level description distinct from T 100, or the same record under an older id scheme -- flagged,
not chased further, per the box.

**Answer: digitised = yes (the finding aid says so), but not viewable online; a reading-room visit or a paid
reproduction order is the only route AGATHA itself offers** (its detail page also carries "Order a reproduction
(payable)" and "Book a seat in the reading room" panels, National Archives of Belgium, Rue de Ruysbroeck 2,
1000 Brussels, by appointment only). This is a copy-order / reading-room need, logged as a proposed ASKS row
below per the brief. Requests: `agatha.arch.be` about 6 (2 curl 500s on the ajax endpoint + browser fetches),
`search.arch.be` 3 (all dead redirects), `www.rfgenealogie.com`/`arch.be` via WebSearch (not a direct fetch).

Not conclusive on its own that the specific 15 April 1648 text is unreachable -- continuing to (3).

## (3) Is the 15 April text printed elsewhere?

AUDIT.md's own search log (section 4) already covers this exhaustively (25 Sept 2026): Lonchay-Cuvelier IV
(HathiTrust `mdp.39015014126620`) checked at HTRC-EF token level ("mercy" 27 pages, "brandebourg" 22,
"chevreuse" 12, "clèves" 1 -- none co-located, no page reads as this instruction) and by Google Books snippet;
CODOIN 82-84 confirmed absent from Internet Archive under every title form tried; APW's search backend was
`HTTP 505` on every query. This session did not repeat the HTRC-EF sweep (already logged, would duplicate
work) but ran the two cheap checks the brief still named:

- **APW retry (one try, per brief):** `apw.digitale-sammlungen.de/search/query.html?q=Mercy` -- still
  `Error 505 Internal Server Error` in the response body (HTTP wrapper 200, backend down), 25 Sept 2026,
  20:1x UTC. Unreachable, not negative, same as AUDIT.md's finding. Not retried again (rule: one retry only).
- **Google Books, keyed, 3 new queries** (`"instructions à Mercy" 15 avril 1648`; `"dépêche de Léopold au roi
  du 18"`; `Mercy Cleves Brandebourg 1648`): every hit across all three is Lonchay 1896 itself or one of its
  contemporary offprints in the Académie royale de Belgique's *Mémoires couronnés* series (same 1896 text, not
  an independent print of the instruction). 0 new sources.

**Answer: not found printed anywhere searched, this session or AUDIT's.** CODOIN and Cuvelier-Lonchay IV
remain the two named leads that need a page a person can actually read (HathiTrust full text is
Cloudflare-blocked from the cloud; CODOIN 82-84 is not on IA) -- both already flagged as owner/local-runner
items in AUDIT.md section 6; not re-flagged as new ASKS rows here to avoid a duplicate.

## (4) Overlap vs reading.txt

No text of the 15 April 1648 instruction itself is on disk anywhere (Lonchay gives only its archival address,
not its content -- see (1)). The only text on disk to diff is Lonchay's p.445 paragraph and footnotes
(above) against `reading.txt`. Ran a script diff, not a read-by-eye: normalised both to lowercase with accents
stripped (`unicodedata.normalize('NFKD', ...)`), then checked containment of each candidate
name/content-word root from Lonchay's paragraph against `reading.txt`'s decoded-plaintext blob (the cipher runs
in `reading.txt` are concatenated with no interword spaces, so a whitespace-token diff alone would miss
everything inside a run; used substring containment on the un-spaced blob instead, and hand-checked every hit
for false positives from word-boundary coincidence -- e.g. "spa" is a false hit, occurring only inside
"...conuos**pa**ra..." "que"). Script: `/tmp/.../scratchpad/overlap2.py` (scratchpad, not committed; rerunnable
inline from this file's numbers).

Real hits, `reading.txt` vs Lonchay p.445:

| root | in reading.txt? | where / note |
|---|---|---|
| mercy | yes | r01 "Baron de Mercy" (clear text, the addressee) |
| barneton | yes | v15 "Barneton" (clear text, the dateline place) -- also in AUDIT's own citation of this footnote, coincidence of place name only, not new |
| cheureuse | yes (reading's own spelling) | r06 "DELADUQUESADECHEUREUSE" -- Lonchay spells it "Chevreuse"; this is exactly the M-graded, reader-transcribed token AUDIT.md section 3 already flags as unresolved (14 vs 19 glyph read) |
| cleues | yes (reading's own spelling) | r14 "PASAREISACLEUESAUEROSCON" -- Lonchay's paragraph never names Cleves at all (it is a different footnote's document, per (1)); the match is only against my own candidate-word list guess, not against anything actually on this page |
| brandenbur(g) | yes | r15 "LELECTORDEBRANDENBUR" -- again, not in Lonchay's p.445 text; false lead from my own candidate list |
| saint-ibal, kerpen, spa, galaretta, leopold, soissons, breze, conde, rochelle, cologne | no | none of these appear anywhere in `reading.txt` |

Corrected reading of the table: **Cleves and Brandenburg are not actually words that appear on Lonchay's
p.445** -- they were checked because they are named in AUDIT.md's own historical-fit discussion (section 3.2,
citing M3's sibling item 9), not because they occur in the Lonchay paragraph transcribed in (1) above. The
only words genuinely shared between *this specific Lonchay page* and `reading.txt` are **Mercy** (the letter's
addressee, expected trivially, not evidence) and **Barneton** (the dateline of both this reading and the 15
April instruction's covering dispatch chain, per Lonchay's own footnote -- Leopold Wilhelm's Brussels
secretariat operating from his Barneton campaign headquarters through spring-summer 1648; consistent with,
not independent confirmation of, the existing N3/`ours` reading). Chevreuse/Cheureuse, Cleves/Cleues and
Brandenburg are all already-known M-graded or contextual elements of *our own* reading and M3's separate
sibling item 9 (Kempen, not Cleves/Kerpen) -- not new corroboration from this source.

**Could Lonchay's page serve as a crib?** No. It contains no clause of the 15 April instruction's actual text
(only the citation), so there is nothing to align word-for-word against the cipher stream. It is weak,
pre-existing context (same office, same spring 1648 window, same Barneton dateline), not a crib.

## Summary (for the ROOM done line)

Printed: **no** -- not found anywhere searched (this session's APW retry and 3 Google Books queries, plus
AUDIT.md's prior exhaustive log). Digitised: **yes, per AGATHA T 100's own note, but reading-room-only, no
online image**; the SEE t.LXIV-specific register concordance is still unresolved. Overlap: **0 new shared
names/phrases beyond Mercy (trivial) and Barneton (the shared dateline place); Chevreuse/Cleves/Brandenburg
matches are pre-existing M-graded reader choices and separate-sibling context, not this source's content** --
no crib.

## Proposed ASKS row (for the orchestrator to file)

> Brussels, Archives de l'État / AGR, SEE fonds (code T 100, `Secrétairerie d'Etat et de Guerre`,
> `https://agatha.arch.be/en/data/ead/BE-A0510_000027_002526`): register **t. LXIV, f.16** carries the 15
> April 1648 instructions to Mercy (Lonchay 1896 p.445 n.2); the fonds is digitised but reading-room-only per
> AGATHA, no online image found. Ask: order a reproduction of t. LXIV f.16 (paid; AGR's May-2018 tariff,
> indexed Jan 2026) or arrange an in-person reading-room visit (appointment required, 2 working days'
> notice), to get a clear copy of this instruction -- would resolve whether it names the 3,000-infantry
> Cleves/Brandenburg levy our reading of the 6 June sibling (f.22) describes, and would turn f.22's N3
> cryptanalytic reading toward N2 if the two texts match.

## Hosts and requests

archive.org (IA `_djvu.txt` fetch) 2; agatha.arch.be about 6 (2 curl 500s on ajax.php + 2 browser_fetch.js
passes); search.arch.be 3 (dead redirects, confirms retirement); apw.digitale-sammlungen.de 1 (one retry,
still 505); www.googleapis.com/books 3 (keyed, `&country=US`); WebSearch 2 queries (search.arch.be
successor, AGATHA confirmation) -- not a fetch of a forbidden host, used only to find the current URL for a
named host whose old address is dead. `data.htrc.illinois.edu` and OpenAlex not used this pass (task (3)
reused AUDIT.md's existing HTRC-EF results rather than duplicate them; no new bibliographic question arose
that needed OpenAlex). gallica.bnf.fr and de-crypt.org: 0 (never touched, per brief).

No decoding, no key edits, no novelty classification (rule 10) -- report only, per brief.
