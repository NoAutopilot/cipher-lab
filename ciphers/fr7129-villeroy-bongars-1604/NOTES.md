# BnF fr.7129, f.268 — Nicolas de Neufville, seigneur de Villeroy, to Jacques Bongars, 2 November 1604

Status: blocked

**csBONG pass, 24 Sept 2026 21:5x UTC:** stays `blocked`. Tomokiyo's paper "Development of Ciphers under Henry IV
of France: A Case of Jacques Bongars: 1590-1611" (academia.edu/40982854), which the M9 lesson requires be read
before this letter can be called `open`, is not reachable by any route tried this pass. See "Tomokiyo's Bongars
paper — route search" below for the full log. Bongars' printed *Lettres* (1668/1695) remain unopened (would need a
copy, out of a copy-free lane's scope).
Anquez 1887, *Henri IV et l'Allemagne d'après les mémoires et la correspondance de Jacques Bongars* (Gallica
`bpt6k213732d`), full-text searched (Gallica ContentSearch) for "7129" (21 hits, all fr.7129 folios cited by
Anquez in his narrative), "268" (2 hits, neither this volume), and "novembre 1604" (5 hits, none this letter)
— fr.7129 f.268 not cited anywhere in the volume, letter absent.

Check-solved pass, 24 Sept 2026 (Sonnet, csKT/LANE N4, cap $5 shared with KT-02). Row KT-01 from
`sources/solver-diffs/2026-09-24-tomokiyo-vs-siblings.tsv` (scTOMO, LANE N4).

## Identification

- Image: Gallica `btv1b8555834s`, canvas f541 r (recto, 268r) / f542 v (268v), confirmed by the leaf's own
  "268" foliation and "1604" dateline (eye-checked 24 Sept 2026 by scTOMO, re-confirmed here).
- Native size: 3721x5914 (recto), 3726x5767 (verso).
- Image URLs: `https://gallica.bnf.fr/iiif/ark:/12148/btv1b8555834s/f541/full/full/0/native.jpg`,
  `https://gallica.bnf.fr/iiif/ark:/12148/btv1b8555834s/f542/full/full/0/native.jpg` — copy-free, full
  resolution, no login.
- Key: Bongars' Cipher no.3, BnF fr.7129 f.275 (table image `BnFfr7129f275.jpg`), described on
  `sources/cryptiana/web/bongars.htm` as used in Villeroy's letters to Bongars July-November 1604 (fr.7129
  f.253-f.268) and October 1605-August 1611 (fr.7131 f.19-f.219).

## Tomokiyo (`sources/cryptiana/web/bongars.htm`, local mirror), quoted verbatim

Under Cipher no.3's description: *"This cipher can solve an undeciphered letter, dated 2 November 1604 and
signed by Villeroy, in BnF fr.7129, f.268 (see below [#unsolved])."*

Under the page's own item-by-item section:

> **BnF fr.7129, f.268**
> Dated 2 November 1604 and signed by Villeroy.
> Can be deciphered with Bongars' cipher no.3.

No reading is offered anywhere on the page. Contrast the next item down, fr.7131 f.256 (8 Feb 1603, signed
Beaumont), which Tomokiyo tags "can be (for the most part) deciphered" with cipher no.3 — f.268 carries no
such partial-reading language, only "can be deciphered", i.e. a claim about key applicability, not a claim
that anyone has applied it.

## Tomokiyo's Bongars paper — route search (csBONG, 24 Sept 2026)

Job: read "Development of Ciphers under Henry IV of France: A Case of Jacques Bongars: 1590-1611" for what it
says about this letter, by a route other than the academia.edu page (403 to two separate workers now: scTOMO's
original check and this pass's own `WebFetch`, same result). Routes tried, all negative:

1. **OpenAlex** (`Authorization: Bearer $OPENALEX_KEY`). `works?search=Development of Ciphers under Henry IV of
   France Bongars` returns 2 results, neither Tomokiyo's paper (an unrelated Princeton book chapter, an unrelated
   history-of-cryptography survey). `works?search=Tomokiyo Bongars cipher` returns 0 results. The paper is not
   indexed in OpenAlex under any query tried.
2. **Semantic Scholar** (`x-api-key: $S2_KEY`, >=1.1 s apart). `paper/search?query=Development of Ciphers under
   Henry IV of France Bongars` returns 0 results. `author/search?query=Tomokiyo` finds Satoshi Tomokiyo
   (authorId 83148217); his indexed paper list (`author/83148217/papers`) holds exactly 3 items — "How I
   reconstructed a Spanish cipher from 1591" (Cryptologia 2018), "Identifying Italian ciphers from
   continuous-figure ciphertexts (1593)" (Cryptologia 2018), "Deciphering Mary Stuart's lost letters from
   1578-1584" (Cryptologia 2023, with Lasry and Biermann) — the Bongars/Henry IV paper is not among them. This
   confirms the paper was never placed in a venue Semantic Scholar or Cryptologia's own index covers; it is an
   academia.edu-only upload, not a published article with a second host.
3. **Tomokiyo's own site.** `sources/cryptiana/PAPERS.tsv` (already on disk, built by an earlier pass) records
   for this exact paper: "no (bongars.htm ... is a related but distinct catalogue article, not the same text)" —
   i.e. cryptiana.web.fc2.com hosts no PDF or htm mirror of this paper, only the related-but-different catalogue
   page already quoted above. `crypto.htm` (Tomokiyo's own index of his papers, in repo) links this paper's title
   only to the same academia.edu URL, no alternate host.
4. **Cryptiana blog.** WebSearch for `site:cryptiana.blogspot.com Bongars` surfaces one post, "Henry IV's Cipher
   from 1590" (2020/08); fetched directly (`WebFetch`) and asked specifically for any mention of this letter,
   its date, f.268, or Bongars' Cipher no.3 — none found; the post covers Maisse's Venice cipher instead, not
   Bongars. No other blog post matched "Bongars" in search. No post after `bongars.htm`'s own date discusses
   this letter.
5. **HAL / ResearchGate / Cryptologia landing pages** (WebSearch). Two queries (`"Development of Ciphers under
   Henry IV" Tomokiyo hal.science OR researchgate.net`; `Tomokiyo Bongars Cryptologia Jacques Bongars cipher
   article`) return only the same academia.edu URL, Tomokiyo's academia.edu profile, and his three *actual*
   Cryptologia articles (none is this paper) — no HAL, ResearchGate or Cryptologia hit for this title.
6. **Wayback Machine.** `web.archive.org` is unreachable from this session at the transport level: every request
   (CDX API for the academia.edu URL, a direct wayback snapshot URL via `WebFetch`, and a bare fetch of
   `https://web.archive.org/`) returned `curl: (35) Recv failure: Connection reset by peer` / HTTP `000` via the
   agent proxy (`ws_closed_mid_exchange`), including after the one permitted retry-after-pause — this is an
   egress-level block (CLAUDE.md: "`000` means the egress policy blocks it"), not a site challenge, so no
   further retries were made this pass.

**Conclusion: the paper is not reachable by any route available to this worker.** It exists only as an
academia.edu upload (403 to unauthenticated fetches) with no second host, no journal placement, and no archived
snapshot reachable from this container. Verdict stays `blocked` per the M9 lesson (the paper is named as
possibly deciding this letter and has still not been read) — this is not converted to `open`.

## Six sources + editions, 24 Sept 2026

1. **Web search.** "Villeroy Bongars 2 novembre 1604 lettre chiffre fr.7129" and "Bongars Villeroy
   correspondance 1604 déchiffrement Tomokiyo": both return only general biographical/catalogue pages
   (Wikipedia, archivesetmanuscrits.bnf.fr record pages, a 2014 Cairn.info article on Bongars' diplomatic
   language, a Tomokiyo academia.edu paper "Development of Ciphers under Henry IV of France: A Case of
   Jacques Bongars: 1590-1611" — 403 Forbidden when fetched, not read) and Bourdeau's/Aymeloglu's project
   sites in the results list themselves, no third-party reading of this letter. No hit naming this letter as
   solved.
2. **Print: Anquez 1887** (see above, edition actually opened this pass by full-text search, not quoted from
   another worker). Also checked but not chased further given the date mismatch and no letter-specific hit:
   Bongars' own printed *Lettres* (français/latines, 1668/1695 Hague and Strasbourg editions) — these are
   Bongars' own outgoing correspondence, not letters received from Villeroy, so a priori unlikely to carry
   this incoming letter; not opened this pass (would need a copy, not free full-text online found by search).
   *Lettres missives de Henri IV* t.6 is the king's own correspondence, a different sender, and Anquez's
   citation of it for the same week (13 Nov 1604, Le roi à Beaumont) is a different letter to a different
   recipient — not this item.
3. **Cryptiana blog / Cipherbrain.** `sources/cryptiana/web/bongars.htm` quoted above (this is the Cryptiana
   page itself, not a blog post). WebSearch of scienceblogs.de/klausis-krypto-kolumne for "Bongars" "Villeroy"
   "chiffre" returns no matching post; the one plausible-looking hit ("Wer löst diesen verschlüsselten Brief
   aus dem französischen Nationalarchiv", 2016) is about a different French-archive cipher, not fr.7129 f.268
   (title and category page content, no BnF fr.7129 mention).
4. **DECODE files on disk.** Grepped `sources/decode/records-decrypted-2026-09-24.tsv`,
   `records-non-decrypted-2026-09-24.tsv`, `records-non-decrypted-2026-09-24-diff.tsv` for "bongars",
   "villeroy", "7129", "7131": no hit in any of the three local DECODE sweep files (the numeric strings 7129/
   7131 elsewhere in DECODE's catalogue, checked via `aaymeloglu/unsolved-ciphers`'s cached
   `catalogue/decode-catalog.csv`, are unrelated Florence Archivio di Stato items and a different Villeroy
   record, R4157 = BnF fr.15564 f.30, 1587, a different manuscript already tracked in Bourdeau's repo as
   `r4157/`). fr.7129/fr.7131 are not DECODE holdings at all as far as this file set shows.
5. **Bourdeau shallow clone** (`github.com/dbourdeau/cyphersolver`, fresh shallow clone this pass, commit at
   clone time 24 Sept 2026). Grepped all folder READMEs/NOTES for "bongars", "villeroy", "7129", "7131": no
   folder or NOTES hit references this letter (only generic "Villeroy" mentions as a historical figure named
   in unrelated targets' background, e.g. nevers/lorraine/matignon items where he is a contemporary minister,
   not this cipher).
6. **Aymeloglu clone** (`github.com/aaymeloglu/unsolved-ciphers`, fresh shallow clone). `TARGETS.md` line 22
   names Bongars volumes fr.7129/7131 only in passing, for a *different*, unrelated target (Cocquet -> Mangot,
   Clairambault 369 f.317, Nov 1616, blocked): *"no period key from Bongars volumes fr. 7129/7131 fits"* — this
   confirms Aymeloglu has looked at fr.7129/7131 material for key-fitting purposes elsewhere, not that this
   specific letter (f.268) has been read. No dedicated folder for fr.7129 f.268 anywhere in the clone.

## Leaf check (24 Sept 2026, this pass, confirming scTOMO's eye-check)

Both sides at native resolution: cipher runs to the foot of 268r and the top of 268v, no interlinear or
marginal decipherment anywhere on the leaf (per csKT-COMMON rule 15, the key-list warning). Neighbouring
folios not re-scanned this pass (scTOMO's claim covers the leaf itself only); no sibling-duplicate search of
the volume was run this pass (out of brief scope for a check-solved row — flagged as a follow-up below).

## Verdict

**blocked** — Anquez 1887 (the standard modern edition built specifically from BnF fr.7125-7132, the Bongars
volumes) read by full-text search, letter absent; no hit in Bourdeau, Aymeloglu, DECODE files on disk, or
general web search; but Tomokiyo's own Bongars paper (academia.edu/40982854), which he cites as the source for
this letter's "can be deciphered" tag, is not reachable by any route tried (see "Tomokiyo's Bongars paper —
route search" above) — per the M9 lesson, a verdict of `open` requires that paper to have been read, not merely
searched around. Held `blocked` until the paper is read (the owner may be the only remaining route: a personal
academia.edu login, or an email to Tomokiyo).

Follow-up suggestion (not pursued, out of this brief's scope): a ±10-folio thumbnail scan of fr.7129 around
f.268 for an unlisted duplicate or minute (Luzerne-rule sweep), and a look at fr.15571-73 (Villeroy's outgoing
letterbook) for a copy of this same dispatch.

Grades: none (no reading attempted). Novelty: not assessed (rule 10 — this is a check-solved verdict, not a
verifier pass).
