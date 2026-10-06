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
Beaumont), which Tomokiyo tags "can be (for the most part) deciphered" with cipher **no.16** [corrected 27 Sept
2026, CS-BONGARS7131: this line previously read "cipher no.3", which is f.268's own key, not f.256's -- see
`ciphers/fr7131-beaumont-bongars-1603/NOTES.md`] — f.268 carries no such partial-reading language, only "can be
deciphered", i.e. a claim about key applicability, not a claim that anyone has applied it.

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

## IMG-FETCH: +/-10-folio thumbnail sweep of fr.7129 around f.268 (26 Sept 2026)

Per NEXT-STEPS.tsv's named follow-up (not pursued before this pass): fetched a recto-only thumbnail
(400px wide) for every folio 258-278 of fr.7129 (`btv1b8555834s`; canvas = 2*folio+5 for recto,
confirmed against the manifest), saved to `images/sweep/` with `manifest.json`. 27 gallica.bnf.fr
requests (1 manifest + 21 thumbnails, 5 needing one retry after `Recv failure: Connection reset by
peer`), all >=1.8s apart. No cipher reading performed; this is a look for an unlisted duplicate
letter, a docket naming the target, or other cipher material nearby -- not a decode.

**Folio by folio:**
- **258:** a different ciphered letter (digit-group cipher mixed with clear French), item numbered
  "18" in the margin -- not the target, no docket naming Villeroy or Bongars.
- **259:** blank.
- **260:** another ciphered letter (digit groups), dated in the body ("22 [...] du mois d'octobre"),
  red wax/ink seal -- a different item, not the target.
- **261:** a docket/closing leaf, plain French: "de Monsr de Lomenie a plr Dieu... fait le [blank]
  de septembre 1604" -- a different sender (Loménie) and month (September, not November); no
  cipher on this leaf.
- **262:** a ciphered letter (digit groups) addressed "Monsieur," -- likely the Loménie letter
  continuing from f.261's docket; not the target.
- **263:** ciphered letter continuation (digit groups throughout).
- **264:** plain French continuation of the same letter, ending in a signature flourish -- no
  cipher, no docket naming the target.
- **265:** blank.
- **266:** a docket/closing leaf, plain French, red seal -- no cipher, no docket naming the target.
- **267:** a plain-French letter closing "Monsieur vre... serviteur... a Fontainebleau le 19e
  [8bre] 1604" (19 October 1604) -- close in date to the target (2 Nov 1604) but a different,
  uncoded letter; no docket naming Villeroy or Bongars.
- **268:** the target letter itself (recto) -- confirmed present and unchanged, cipher block at
  the foot, red seal; not re-read here (already documented elsewhere in this repo).
- **269:** blank.
- **270:** **not a letter -- a multi-column tabular page of code words and short glyphs/numbers**
  (place names, titles, ordinary words each paired with a short code), i.e. cipher key/nomenclator
  material, sitting two folios after the target.
- **271:** continuation of the same tabular key material as f.270 (more columns of words paired
  with codes).
- **272:** blank -- the table ends at f.271.
- **273:** blank.
- **274:** **a distinct cipher key page: a full alphabet-substitution grid (columns headed by
  letters, two-digit numbers below each) plus a separate list of titles ("Roy d'Espagne", "Roy
  d'Angleterre", etc.) each paired with a number code** -- a second, differently-shaped key table
  from the one at f.270-271.
- **275:** continuation of key material, this time with single symbolic glyphs in the left margin
  paired with code groups -- a third distinct-looking key/nomenclator table.
- **276:** blank (foxed).
- **277:** blank (foxed).
- **278:** blank.

**Result: no unlisted duplicate or minute of the target letter, and no docket naming Villeroy,
Bongars or 2 November 1604, found in this +/-10-folio range.** The two nearby uncoded letters
(f.264-267, f.261-266) are dated September and 19 October 1604 and signed/addressed to different
correspondents, not a copy of the target. **However, three folios in this same range (270-271,
274, 275) carry what look like cipher key or nomenclator tables** (word/code pairs, an alphabet-
substitution grid, and a symbol-code list respectively) rather than letters -- not identified here
as *the* key for the target's cipher no.3 (that would need actual decoding, out of scope for this
pass and not attempted), but flagged as material worth a solver's attention given its proximity (2
and 6 folios from f.268) and its presence in the same bound volume. No novelty or cryptanalytic
claim is made (rule 10); this is a description of what four thumbnail pages show, nothing more.

Status unchanged: `blocked` (per the M9 gate: Tomokiyo's paper still unread). file_shrink_guard
clean on NOTES.md and images/sweep/*.

## KEY-7129: full-resolution capture of the three key tables + a shape test on the target's cipher block (26 Sept 2026)

Per `.claude/briefs/runs/2026-09-26-parent-key-7129.md`. **No reading claim, no status change** -- status stays
`blocked` (the M9 gate is unaffected by this pass).

### Step 1: prior-print check

Re-grepped `sources/cryptiana/web/bongars.htm` (the only local Tomokiyo mirror) for "7129", "270", "274",
"Villeroy", "1604", "Bongars". Confirms, verbatim, what was already quoted in this file's Identification
section from an earlier pass -- no new print found, but the passage matters enough to restate plainly for
this job's purpose:

> **no.1 (f.270-271)**: "Full two pages of code words for names and common words." Used in a 1609 Henry IV
> letter and in Bongars' own 1602 letters, "along with the cipher of no.3" -- not named for the target.
>
> **no.2 (f.274)**: "Cipher alphabet with Arabic figures and Latin letters... Substitution alphabet includes
> 'k'... (but lacks 'n'!)... **I have not seen an actual use of this cipher.** According to Desenclos and Vial
> (2014), this cipher was used at least in the first letters of Henry IV in 1594." -- Tomokiyo explicitly has
> never seen this cipher (no.2, f.274) actually applied to any letter, and dates its known use to 1594, a
> decade before the target.
>
> **no.3 (f.275) "Bongars' Cipher (1604-1611)"**: "Cipher alphabet with Latin letters and other symbols.
> Graphic symbols, Latin letters with an umlaut, Arabic figures (6-99; 1-43 with an overbar) for names and
> common words... This cipher is used in letters from Villeroy to Bongars in July to November 1604 (BnF
> fr.7129, f.253-f.268)... **This cipher can solve an undeciphered letter, dated 2 November 1604 and signed by
> Villeroy, in BnF fr.7129, f.268** (see below)."

**No decipherment of f.268 is printed anywhere on the page** -- this confirms rather than lifts the M9 gate
(unchanged from the earlier pass). But it is worth being explicit here because this job's own brief named
f.274 (no.2) as the primary transcription target and f.275 (no.3) as lower priority ("gets a description and a
row count only unless time remains"): **Tomokiyo's own text says the opposite of what a naive read of the
folio order suggests** -- no.2/f.274 is a cipher he has never seen used, dated eleven years too early, while
no.3/f.275 is the one he names, by folio and date, as the actual key for this exact letter. This job followed
the brief's step order (f.274 fully, f.270-271 and f.275 partially) since it was already committed to by the
time this was re-confirmed, but the finding changes what the shape test in step 4 should be read to mean (see
below) and should steer any future pass's priority to f.275 first.

### Step 2: full-resolution fetch

6 Gallica IIIF `native.jpg` fetches (browser UA, >=2s apart, one retry after a `Recv failure: Connection reset
by peer` on f.271r): f.268r (canvas 541), f.268v (542), f.270r (545), f.271r (547), f.274r (553), f.275r
(555). Recto only (the tables read as complete on the recto in every case checked; verso not fetched this
pass to stay well under the 12-image cap). Saved to `images/keys/` with `manifest.json`. Native sizes 3669-4510
x 5914 px -- all far over the 2500px reading limit, so every transcription pass below worked from a further
crop, not the full page. `file_shrink_guard.py` run on this folder before the final push (see done line).

### Step 3: key capture

**f.274 (Tomokiyo's no.2).** `keys/key_f274.tsv`: the primary alphabet-substitution row, all 22 header letters
(a,b,c,d,e,f,g,h,i,k,l,m,o,p,q,r,s,t,u,x,y,z -- skips j, n, w, matching Tomokiyo's "includes k... lacks n").
Each plaintext letter's code is either a two-digit-style Arabic numeral or another single Latin letter written
in the same hand, mixed deliberately (matches Tomokiyo's "Arabic figures and Latin letters"). A second,
partial homophone layer (a smaller second letter + a second numeral per column) was transcribed where legible
and marked "?" where the second value could not be resolved this pass (columns under d, f, h, k, m have an
unresolved second numeral). A blind second read of the primary row was run this pass (Sonnet subagent, given
only `f274_topgrid_L.jpg`/`f274_topgrid_R.jpg`, no theory, no access to this worker's own reading): it agreed
on 20 of 22 primary-row cells exactly (a=6, c=7, d=u, e=8, f=x, h=y, i=z, k=Z, l=3, m=b, o=c, p=5, q=d, r=i,
s=e, t=a, u=f, x=h, y=g, and independently read b=t matching this worker's own read); it flagged the same two
cells this worker was already unsure of as ambiguous (g: digit "9" vs letter "g", both passes leaned 9; z: no
confident code legible, possibly cut off or a symbol). `keys/key_f274_names.tsv`: 45 of an estimated ~74 title/
dignitary codes (26-79, plus 40-58 from a second list at the foot of the page) -- names and their numeric codes
for the King, Queen, princes, marshals, and foreign rulers, cited by which of the four columnar blocks on the
page they came from. Not independently blind-checked (out of this pass's time).

**f.270-271 (Tomokiyo's no.1).** `keys/key_f270.tsv`: this table's hand is markedly harder to read than
f.274's ruled grid (a dense secretary hand with no ruled cells), and this pass captured only a structural
description plus two very-low-confidence sample pairs, not a row count of confident transcriptions -- flagged
honestly as such rather than padded. The load-bearing finding is structural, not row-by-row: the table is
built entirely from short pronounceable code-*words* (2-6 letters) paired with plain-French meaning-words, in
about 8 repeated column-pairs across the two folios -- **no numerals appear anywhere in this table** in either
crop viewed. `tools/key_design.py`'s fresh build marks this file `usable=no` ("only 1 codes carry a readable
value with this loader"), correctly reflecting that this pass did not produce a real key table, only a
description; a future pass transcribing it properly should expect this to flip to `usable=yes` once populated.

**f.275 (Tomokiyo's no.3, "Bongars' Cipher 1604-1611", the one Tomokiyo names for the target letter).**
Description only, per this brief's own scoping (time did not remain to transcribe it after the above), but
worth recording in more than one line since it corroborates the shape test below: the page carries (a) a
left-margin column of roughly 24-27 unique **graphic symbols** (not letters, not digits -- glyphs resembling
crosses, hooks, alchemical/planetary-style marks), each paired with a one- or two-digit number, functioning as
the alphabet/short-value layer; (b) a large two-sub-column table of **plain French words paired with two-digit
numbers running from roughly 1 to 99** (place names, common words, function words); (c) a name/title list in
the same style as f.274's, using the same symbol set as (a) rather than plain numerals for some entries. This
matches Tomokiyo's description of no.3 field-for-field ("Graphic symbols, Latin letters with an umlaut, Arabic
figures (6-99; 1-43 with an overbar) for names and common words") and, importantly, **matches the target's own
cipher-block shape far better than f.274 does** (see step 4).

### Step 4: shape test (not a reading)

`ciphertext_candidate.txt`: a first-pass, admittedly rough transcription of the 6-line cipher block at the
foot of f.268r (candidate only -- a later transcription lane makes the file of record). 97 tokens counted
programmatically: ~39 numeral-shaped tokens (7 of them written with an overbar, matching Tomokiyo's "1-43 with
an overbar" for no.3), ~37 letter-shaped tokens (several with what reads as a doubled dot/diaeresis mark,
matching no.3's "Latin letters with an umlaut"), 8 occurrences of one recurring curled hook glyph (matching
no.3's "symbols for doubling/cancelling the preceding letter"), and the rest unclear. **This shape --
overlined and plain numerals mixed with umlaut-marked letters and a recurring non-alphabetic symbol -- matches
f.275 (no.3)'s design, not f.274 (no.2)'s (a clean per-column numeral/letter alphabet grid with no overlines,
no diacritic marks, and no recurring symbol).**

Per the brief's own step 4 instruction, the test was run against `key_f274.tsv` since that is what was fully
captured this pass: `shape_test_f274.py` decodes `ciphertext_candidate.txt` against `key_f274.tsv` and against
20 class-shuffled copies of the same key (values reshuffled among the same codes -- coverage itself cannot
differ under this shuffle, since it depends only on the code set, not the values, so the discriminating
statistic is the `fr` NgramModel score of the decoded letter-stream, per the bCAS/AX-5799 lesson about
controls that cannot vary on the axis being measured):

```
tokens: 97
coverage (tokens whose code is in key_f274.tsv, tier-agnostic): 0.268
decoded letter-stream length: 26
fr16 NgramModel score of the real decode: -1.7444
20 class-shuffled keys (rule 3 control): mean score -2.1019, sd 0.1898
z (real vs shuffled-key control): 1.88
```

**z=1.88 is below both `key_crossmatch.py`'s own "weak" bar (z_shuffled>=3) and its "hit" bar (>=4); coverage
at 0.268 is low.** This is a control-backed negative for f.274 against this cipher block, consistent with (not
contradicted by) step 1's finding that Tomokiyo has never seen no.2 used and dates it to 1594, and consistent
with the shape match pointing at f.275 instead. It is not evidence against the letter being solvable --
Tomokiyo names f.275 (no.3) as the correct key, which this pass did not have time to capture into a testable
key file.

### What a solver (or the next KEY-7129-style pass) should do next

Transcribe `key_f275.tsv` (the symbol table, cipher no.3) first -- it is the cipher Tomokiyo names for this
exact letter, its shape matches the target's cipher block far better than f.274's does, and this pass's
control-backed negative on f.274 removes it as a live candidate for a first attempt. A proper transcription of
`ciphertext_candidate.txt` (this pass's version is a rough first read, not the file of record) should precede
any real decode attempt against whichever key is captured. Status stays `blocked` regardless (M9 gate).

Requests this pass: gallica.bnf.fr 6 (1 retry). No other host. No credentials. 1 Sonnet subagent (blind
alphabet-grid read). Files: `images/keys/{manifest.json,f268r_canvas541.jpg,f268v_canvas542.jpg,
f270r_canvas545.jpg,f271r_canvas547.jpg,f274r_canvas553.jpg,f275r_canvas555.jpg}`, `keys/{key_f274.tsv,
key_f274_names.tsv,key_f270.tsv}`, `ciphertext_candidate.txt`, `shape_test_f274.py`, KEY-DESIGN.tsv (rebuilt),
KEY-OFFICES.tsv (+1 row).

## Reading attempt (VB-DECODE, 26 Sept 2026): gate NOT met

Per `.claude/briefs/runs/2026-09-26-parent-vb-decode.md`. Status unchanged: `blocked` (the M9 gate). No class, no
novelty wording (rule 10). No grades are given to any token (rule 4), because the control gate below was not cleared.

**1. Transcription of record (`ciphertext.txt`).** 13 lines: 8 at the foot of f.268r (from "mais") and 5 at the top of
f.268v. Two blind Sonnet passes on line crops (no key, no candidate) gave 341 and 299 tokens; pass B slipped a line on
recto 4-8. The worker reconciled from the crops into 362 tokens. **Caveat:** the reconciliation was key-aware. The
glyph families (plain y, tailed 3, hooked Z, the crossed-ff/pi ligature, round d, and the hook with minims) cannot be
separated without the f.275 key and the f.228 look-alike table, so sign ids were assigned with both in view. Per-token
agreement with the blind passes, on normalized forms: both passes 123, pass A only 101, pass B only 26, neither 112
(34% both, 69% at least one). The unresolved count is effectively the 112 with neither pass behind them, plus every
token in the ambiguous families. `ciphertext_candidate.txt` is marked superseded.

**2. Key of record (`keys/key_f275.tsv`, 214 rows, 86 unclear).** f.275r is written sideways (read rotated 90 deg).
Layout, all read this pass:
- a homophonic alphabet (a-z less j/k/v/w, plus a last column read as con/com) with 2-5 signs each;
- alphabetical word lists: plain 6-99 (combat, comme, cela ... que; paix, Holande and Flandres get symbols), overbarred
  1-43 (qui, quoy, quand ... Zelandois), and dotted letters for a-/b- words (Ambassadeur ... ceulx);
- drawn symbols for about 60 names (not transcribed; none identified in the block);
- notes: a doubling sign ("... doublera son prochain") and null signs ("tout ce qui sera entre deux ... sera nul").

Sources: blind reads A and B of the crops (B's alphabet is offset by one column on the left half; A's alphabet is
unusable; both misaligned the word numbers across columns), the worker's third read, and **BnF fr.7131 f.228r**
(Gallica `btv1b10509420g`, canvas f469; 2 gallica requests). f.228 is the period look-alike table Tomokiyo names: signs
grouped under the letter they resemble, with the plaintext below. It is written up in `keys/aid_f228.tsv` (one read,
the worker's own). It independently confirms most of the f.275 alphabet column by column (for example y/3/x = a,
6/3/dagger-t = t, b/m/co/ba = u, a/Z/circle-dot = s, ri/sin = z, b-bar/ur/ut = the last column). Registered in
KEY-OFFICES.tsv; KEY-DESIGN.tsv rebuilt; `tools/key_design.py --check` passes.

**3. Control, run before the decode was read** (`python3 decode_f275.py --control`; the fr16 4-gram model of
`tools/judge_plaintext.py`, Lettres de Catherine de Medicis t.1, over the letters of the decode; N=566 letters):

```
real key score -1.4003; 20 class-shuffled keys mean -1.4768 sd 0.0720 min -1.5903 max -1.3578; z 1.06; rank 4 of 21
per line z (real line vs the same line under the 20 shuffled keys):
r1 0.87  r2 -0.39  r3 1.63  r4 0.04  r5 -0.32  r6 -0.86  r7 0.29  r8 1.53  v1 2.44 (rank 1)  v2 0.06  v3 3.34 (rank 1)  v4 -1.28  v5 -0.21
```
`tools/judge_plaintext.py` on the decode (a scratch spec, language fr): `FAIL language: score=-1.4, null_p99=-1.88,
real_p05=-0.886, real_median=-0.784, N=566`. The decode is above the letter-shuffle null but far below real French.

About the leave-one-line-out gate: `tools/interlinear_align.py` needs a plaintext span, and there is none for this
block. A period key is also fixed, so no line can be "predicted from the others". The per-line z above is the nearest
honest analogue: 2 of 13 lines beat all 20 shuffled keys (v1, v3), and 11 do not.

**4. The decode (`reading.txt`, from `decode_f275.py`; 358 of 362 tokens map to a key value, 4 [?]).** It is not a
reading. Fragments look like French: v1 has "le s Espagnols ... en com en t tous i?urs qui l est tout a leur de ... est",
and "tous ... iours" needs the 9-shaped g read as o (the aid's G family allows g = f or o). Most lines are noise. The
plain 7 decodes as "comme" about ten times and the overbarred 7 as "feu" eight times, far above any plausible rate.
That suggests single digits in the block (at least 7, 9 and 6) are letter signs rather than word codes: f.228 already
lists 3, 4, 5 and 6 as letters. It also suggests the ambiguous families are mis-assigned. The check-solved phrase sweep
was not run (the brief runs it only on a cleared gate).

**Named next step (the stuck rule, one different thing): a glyph-matching transcription pass against the period
aid.** A subagent is shown f.228's cells as the reference sheet plus one line crop at a time. It reports, per token, the
f.228 cell (family, upper sign) it matches, or "no match", and digits are kept apart from letter-signs. This makes the
reconciliation's key-aware step explicit and repeatable instead of the worker's eye, then `decode_f275.py --control`
runs unchanged. Not run this pass, to stay inside the USD 15 cap. Cost: 13 line units
x 2 blind passes + 1 reconciliation, at about USD 0.6 per Sonnet crop call (this job's own four reads), about USD 16 if
run in full; the verso alone (5 lines, where v1/v3 already lead) costs about USD 6.
A matched control that would make any later result mean something: the same key applied to a sibling letter in the
same cipher (f.253-f.267 per Tomokiyo; the IMG-FETCH sweep shows cipher letters at f.258, f.260 and f.262-263). If
one carries an interlinear decipherment, it is a known-plaintext check of the key and the transcription method.

Files: `ciphertext.txt`, `keys/key_f275.tsv`, `keys/aid_f228.tsv`, `decode_f275.py`, `reading.txt` (candidate decode,
not a reading). No image was added to the folder: it already held 29, over the 20 cap, before this job. Crops and the
fr.7131 f.228 image are in the worker's scratch and can be re-fetched from the URLs above. Requests: gallica.bnf.fr 3
(1 SRU, 1 manifest via gallica_folio.py, 1 native image). Subagents: 4 Sonnet (two blind cipher passes, two blind key
reads).

## Glyph-matched re-transcription and key-cell pass (VB-DECODE2, 27 Sept 2026): gate NOT met

Per `.claude/briefs/runs/2026-09-26-parent-vb-decode2.md`, the stuck-rule try named above. Status unchanged: `blocked`
(the M9 gate). No class, no novelty wording, no grades (the gate was not cleared). **Verso only; the recto was not
reached** (stopped on cost, 13 Sonnet calls, before the box ran out).

**1. Transcription (`ciphertext_v2.txt`, verso 5 lines, 136 tokens).** Padded native crops of each line (two
overlapping halves; scratch only, no image added to the folder). Two independent Sonnet passes per line. Each pass was
shown the line crops, BnF fr.7131 f.228 and the f.275 alphabet block as pictures, and chose ids from a fixed inventory,
with digits kept apart from letter-signs and diacritics as separate marks. The merge is mechanical and there was no
eye reconciliation (rule in the file header). Agreement per line, then how much of v1 (`ciphertext.txt`, key-aware
reconciliation) is found again in v2:

| line | pass A / B tokens | v2 tokens | A = B | v1 tokens re-found in v2 |
|---|---|---|---|---|
| v1 | 26 / 28 | 27 | 17 (63%) | 17 of 27 (63%) |
| v2 | 27 / 32 | 27 | 17 (63%) | 15 of 31 (48%) |
| v3 | 31 / 28 | 29 | 15 (52%) | 16 of 34 (47%) |
| v4 | 27 / 24 | 24 | 12 (50%) | 13 of 29 (45%) |
| v5 | 29 / 29 | 29 | 16 (55%) | 16 of 29 (55%) |
| verso | | 136 | 77 (57%) | 77 of 150 (51%) |

Glyph matching did not raise agreement: 57% two-pass agreement against v1's 69% at-least-one-pass figure, and v2
re-finds only half of v1. The big hook-and-curl family (the Hr/Hu/Hun/HZ hooks and the new stand-alone Ch hook) and
the y / tailed-3 pair were marked l or m by every pass on every line. That is the unresolved part.
The first line-4 A pass transcribed the wrong line (the brief's prompt said "top line", and the padded crop shows the
foot of line 3). It was rerun after the prompt was fixed, and only the rerun is used.

**2. Key cells (`keys/key_f275_v2.tsv`; `key_f275.tsv` untouched).** Scoped to the letter-sign alphabet block, not
all 86 cells, because word-code values cannot move the letter-stream score under the class shuffle. Two Sonnet reads
(left half a-m, right half n-z plus con) against f.228, plus the worker's own read of the same crops. A cell changed
only where two reads agreed. Unclear 86 -> 80, counting 2 new rows: 8 cells confirmed and 1 cell changed. Changes:
- x4 (crossed 4): f -> **g** (both reads place it in column g, row 2).
- 3, ab, v, q, p, mt, 6, m: unclear -> clear. The column was confirmed by two reads.
- **7: comme -> null (still unclear).** The f.275 notes say *"Nulles 7 et [circle with a cross on top]"*. The word
  list also shows a 7-shape beside "Comme" (and a 6 with a C above beside "Combat"), so which form the block uses is
  unresolved.
- Added **Cx** (circle with a cross on top) as null, from the same note.
- Added **Ch** (a large C-hook standing alone) as the sign that *"doublera son prochain"*, from the note. It is a new
  decoder kind, `double`, and still unclear.
- Crossed ff (xff) is **not** changed. The left-half read puts it under d and the right-half read under r, so the
  reads conflict.
- Defect found, not fixed in v2: the key has sign 6 twice (letter t, word combat) and sign 8 twice (letter b, word
  cela). The loader keeps the last row, so every 6 and 8 decodes as a word, in v1 too. The diagnostic below drops
  the two word rows.

**3. Control, run before any decode was read.** `decode_f275.py --control --side v` (options added this pass; the
defaults are unchanged and `reading.txt --check` is still current). 20 class-shuffled keys, fr16 model, verso lines:

| transcription + key | verso z | rank /21 | v1 | v2 | v3 | v4 | v5 |
|---|---|---|---|---|---|---|---|
| v1 + v1 (VB-DECODE) | 1.16 | 3 | 2.44 | 0.06 | 3.34 | -1.28 | -0.21 |
| v1 + 7 as null only | 1.54 | 2 | 2.31 | 0.07 | 2.38 | -1.39 | -0.07 |
| v1 + key v2 | 1.45 | 2 | 2.48 | 0.06 | 2.27 | -1.21 | -0.02 |
| v2 + v1 | 0.86 | 7 | 1.63 | -1.16 | 2.11 | 0.17 | -0.89 |
| **v2 + key v2** | **0.84** | **5** | 1.66 | -1.60 | 2.38 | -0.01 | -1.42 |
| v1 + key v2 without word rows 6/8 | 1.52 | 4 | 2.76 | -0.08 | 2.23 | -0.94 | -0.20 |
| v2 + key v2 without word rows 6/8 | 1.04 | 4 | 2.38 | -1.77 | 1.23 | 0.41 | -0.83 |

Over the whole block (both sides, v1 transcription), z goes from 1.06 (key v1) to 1.47 (7 as null only) to 1.77
(key v2). fr16 judge (`tools/judge_plaintext.py`, scratch spec, language fr) on the verso decodes:
v2+key v2 `FAIL language: score=-1.358, null_p99=-1.789, real_p05=-0.899, real_median=-0.779, N=227`; v1+key v1
`FAIL language: score=-1.387, null_p99=-1.822, real_p05=-0.906, real_median=-0.794, N=233`.

**4. Gate not met.** No verso line reaches z 3 in any row above. The only line above z 2 in both transcriptions and
every key is v1, and verso line 3's z 3.34 does not survive the fresh transcription or the key change. No
reading_v2.txt was written, and the check-solved sweep was not run. `decode_v2_verso.txt` is the mechanical decode
for the record, not a reading.
**The weaker leg is the transcription.** Replacing the transcription moved the verso z by -0.30 (key v1) and -0.61
(key v2). Replacing the key moved it by +0.29 (v1 transcription) and -0.02 (v2 transcription).
The glyph-matched blind passes re-find only half of the key-aware v1. So v1's two leading lines may partly reflect
the key being in view during reconciliation, and are not yet evidence of the key.

**Next step (a different instrument, not a third pass at the same crops):** a known-plaintext check. Take a sibling
letter in the same cipher (f.253-f.267; the IMG-FETCH sweep shows cipher letters at f.258, f.260 and f.262-263) that
carries an interlinear or marginal decipherment. It would fix which hook and tailed-3 forms are which letter, and
settle 7/comme, 6/combat and xff d/r, before f.268 is transcribed again.

Requests: gallica.bnf.fr 1 (fr.7131 f.228 native image, scratch). Subagents: 13 Sonnet (10 used line passes, 1
discarded wrong-line pass, 2 key reads). Files: `ciphertext_v2.txt`, `keys/key_f275_v2.tsv`, `decode_v2_verso.txt`,
`decode_f275.py` (options `--cipher/--key/--out/--side`, kind `double`).

## VB-KP known-plaintext calibration (27 Sept 2026)

Per `.claude/briefs/runs/2026-09-27-parent-vb-kp.md`. Not a third pass at f.268. Status unchanged: `blocked` (the M9
gate). No class, no novelty wording, no grades.

**Verdict (b):** the key of record plus our pipeline does not read the sibling at the brief's bar. The n-gram judge
gives z -0.78, and the decode agrees with the clerk on 47% of letters (bar: z 3 or 70%). But the clerk comparison
beats all 20 shuffled keys (z 5.50). So the key carries real signal: most numeral word codes are right, and overbars
lost in transcription explain several misses. The letter-sign alphabet and a few word-list cells are contradicted.
The next step is a key re-read of those families against the clerk-aligned sibling, not a re-transcription of f.268.

**1. Sibling chosen.** Recto canvases of f.258, f.260, f.262 and f.263 were fetched at width 1500 to the scratchpad.
All four carry a contemporary interlinear decipherment: a clerk's plaintext written letter by letter above the cipher
signs, with marginal glosses of names and code words (f.258 "Toutesfois", "Max.", "Palsborn"; f.263 "paix d'Angl.").
f.258 was chosen. Its gloss is the most evenly spaced, and its first cipher block has 7 lines under "...faire paix."
Lines 2-6 were taken. The folio carries two more blocks lower on the page (3 and 1 lines), not used.

**2. Transcription.** Native crops (`tools/iiif_lines.py` was run for the overlay; the bands it found split gloss and
cipher rows unevenly, so each line was cut by hand as gloss row plus cipher row, in two overlapping segments,
scratch only). Two blind Sonnet passes per cipher line used the VB-DECODE2 method (f.228 and the f.275 alphabet as
pictures, fixed inventory `sibling/passes/inventory.txt`, digits apart, no key values) and were merged mechanically
by `sibling/merge_passes.py` into `sibling/ciphertext_f258.txt`:

| line | A / B tokens | merged | A = B |
|---|---|---|---|
| 2 | 31 / 35 | 32 | 22 (69%) |
| 3 | 30 / 39 | 31 | 22 (71%) |
| 4 | 35 / 37 | 35 | 19 (54%) |
| 5 | 30 / 33 | 32 | 22 (69%) |
| 6 | 34 / 36 | 34 | 25 (74%) |
| all | | 164 | 110 (67%) |

This is 10 points above VB-DECODE2's 57% on f.268v.
Caveat: the gloss sits within a few pixels of the signs and stays in the crop. The passes were told to ignore it and
had no key, so the gloss cannot steer a sign id towards a key value.
The clerk's text had two blind passes too (`sibling/passes/PlainA`, `PlainB`), with letter agreement per line of 89,
77, 74, 33 and 62%. Pass A put the right halves of lines 5 and 6 on the wrong lines, so B's line assignment is used.
The merge rule is in the header of `sibling/plaintext_f258.txt`.

**3. Control first, then the clerk.** `python3 decode_f275.py --control --cipher sibling/ciphertext_f258.txt --key
keys/key_f275_v2.tsv` was run before the decode was read:
```
letters in decode: 254
real key score -1.5195; 20 class-shuffled keys mean -1.4614 sd 0.0749 min -1.5776 max -1.3340; z -0.78; rank 17 of 21
per line: r2 z -0.99 | r3 -0.59 | r4 -2.48 (rank 21) | r5 1.43 (rank 2) | r6 0.01
```
`sibling/compare_clerk.py` normalizes both texts to one convention (lower case, & -> et, j/v -> i/u, letters only). It
aligns decode and clerk per line and runs the same 20 class-shuffled keys (same seed) as the control:
```
letter agreement with the clerk: real key 0.467; 20 class-shuffled keys mean 0.285 sd 0.033 max 0.357; z 5.50; rank 1 of 21
tokens with a key value: 158; confirmed by the clerk (whole span matched): 63 (40%)
per line matched clerk letters: 2 42% | 3 40% | 4 42% | 5 62% | 6 48%
```
Using pass A's clerk text instead gives 0.344 against 0.258 +- 0.029, z 2.92, rank 1: the sign of the result
holds, and the size depends on the clerk transcription. Full output: `sibling/compare_f258.txt`. The mechanical
decode is `sibling/decode_f258.txt` (a candidate, not a reading).

**4. Which families the clerk contradicts (all at f.258r, block 1).**
- *Numeral word codes (plain):* 20 of the 35 numeral tokens read a word the clerk's line contains: 26 en (x9),
  15 de, 16 du, 48 je, 57 leur, 78 nous, 55 le, 39 grand (l.5), ^22 sur. Three more are notation or clerk-pass gaps,
  not errors: 76 mil, which the clerk abbreviates "ml" (l.4); and 99 que and 25 est, which pass A reads "qu'il est"
  (l.5). **Contradicted:** 77 = nostre, but the clerk has "mo[n]" (l.6, "prise en mon alliance"). 90 = protestans,
  but the clerk has "Suisses" (l.5; both passes read 90). 24 = Escossois, but the clerk has "fumee"/"mespris"
  (l.2). 72 is blank in the key. Each rests on a single occurrence.
- *Overbar lost in transcription (not a key error):* l.4 opens 29 18 35, with the marginal gloss "Toutesfois" and
  "si [v]ous" above. That is ^29 toutesfois, ^18 si and ^35 vous in the key, so both passes dropped three overbars.
  39 on l.3 sits under "du voyage", which is ^39 voyage. These four tokens decode wrong only because the bar was
  missed. The next transcription prompt must ask about the bar on every number.
- *Letter signs:* the clerk contradicts, among others: y (key a; clerk n/nt, l.2), oo (key y; clerk u, l.3), f (key o;
  clerk s/se, l.4), qo (key h; clerk t, l.4), r (key e; clerk m, l.5), q (key e; clerk f and o, l.5-6), and 8 (key
  b/cela; clerk l(es), l.5). The line openings show the d-family is where it breaks. Line 2 "et tournent" reads
  pH/do ab d b d k r y, which needs the first d-form = o and the second = r. Line 6 "prise" reads g/cc y/pH p d r,
  which needs g = p, y = r and d = s. The key has d = r, do = o, g = f and y = a. So the d, g and y forms each hide more
  than one sign, as f.228 warns, and our inventory does not separate them.

No `keys/key_f275_v3.tsv` was written. Every candidate correction above rests on one occurrence in a transcription
that agrees 67% between passes. A cell change needs the same sign to disagree with the clerk at two independent places.

**Named next step (b):** re-read the key against the sibling. Use known-plaintext alignment of f.258's three blocks
and f.260 (about 30 cipher lines under a full clerk gloss) with `tools/interlinear_align.py`, treating the clerk's
letters as the plaintext span. This gives grade C key cells for the letter-sign families, above all the d/g/y forms,
and for the word-list numbers 77, 90, 24 and 72. The transcription prompt must ask about the overbar on every
numeral. Only then should f.268 be re-transcribed.

Requests: gallica.bnf.fr 6 (4 rectos at width 1500, f.258r native, fr.7131 f.228r at width 1800), all to the
scratchpad; no image added to the folder. Subagents: 12 Sonnet (10 cipher line passes, 2 clerk passes).
Files: `sibling/{ciphertext_f258.txt,plaintext_f258.txt,decode_f258.txt,compare_f258.txt,merge_passes.py,
compare_clerk.py,passes/}`.

## VB-KEY known-plaintext key re-derivation (27 Sept 2026): hold-out bar NOT met, f.268 not decoded

Per `.claude/briefs/runs/2026-09-27-parent-vb-key.md`. Status unchanged: `blocked` (the M9 gate). No class, no
grades, no reading. **Over cap:** 18.53 USD by get_session against a cap of 10 (8 Sonnet calls; the wave-2 passes each
ran 58-77 zoom/tile tool calls inside one call, which the call count did not price).

**1. Known plaintext.** f.260r (canvas f525, native, scratch crops only), lower cipher block, lines 1-12 (native y
2381-4355; line 1 is the one under "aitreueillez & peutestre"), each cut as gloss row plus cipher row in two halves
split at an ink gap. Two blind Sonnet passes per line. Each pass wrote the sign id (inventory.txt) and the gloss
letters standing directly above that sign (`sibling/passes/f260_S<set><A|B>.tsv`). Not reached: f.260 upper block and
the rest of f.258. Merged by `sibling/kp_key_v3.py merge` into `sibling/ciphertext_f260.txt`, `plaintext_f260.txt`
and `aligned_f260.tsv` (A=B kept, else pass A; a pass line whose sign column mostly repeats its gloss is dropped):
568 merged sign tokens, 231 A=B (41%). Per line: 51, 63, 35, 31, 0, 34, 49, 52, 40, 67, 39, 29%. Line 5 pass A read
the gloss row as cipher and was dropped. Pass S4A says it looked at other passes' files for sign vocabulary, so set 4
is not fully blind. The signs match on only 41%, well below f.258's 67%. The gloss pairing agrees far less:
only 28 positions have the same sign and the same gloss in both passes. So the direct per-sign pairing is not usable
evidence on its own.
Known plaintext in the test: 1,475 clerk letters over 29 line observations (f.258 lines 2-6; f.260 lines 1-12 per pass).

**2. Key v3 (`keys/key_f275_v3.tsv`).** Instrument: a hard-EM line alignment in `kp_key_v3.py`, not
`tools/interlinear_align.py`, because that tool's floor rule is built for numeral groups. The alignment gives each
sign a chunk of its line's clerk letters: 0-1 for a letter sign, 0-2 for a syllable sign, 0-12 for a number. v2's
values seed round 1, then six rounds. Cells: 40 changed against v2, 29 v2-unclear given another value, 23 confirmed,
11 confirmed-unclear, 53 new, 111 v2-kept (never attested). 88 are attested by 2 or more occurrences.
**No changed cell reaches 0.6 agreement, so every change is marked unclear=1.** v2's letter cells hold up best where
counts are large: s=i (22/72), p=i (19/64), o=e (20/50), r=e (17/35), m=u (14/37), b=u (11/46), e=p (10/26),
26=en (10/34).

**3. Hold-out, control first (`python3 sibling/kp_key_v3.py holdout-em`).** Each line is decoded with a key built
without it. The control is 20 class-shuffled copies of that key (decode_f275.shuffled, seed 20260926).
```
EM key, held out:   502/1475 = 0.340; shuffled mean 0.246 sd 0.010 max 0.263; z 9.90
key v2, same lines: 490/1475 = 0.332; shuffled mean 0.248 sd 0.019;          z 4.46
per-pass pairing (holdout, f.260 lines 1-6 only, earlier run): 0.273 vs 0.221, z 2.13; on f.258: 0.335 vs v2's 0.467
```
The key carries real signal against its control, but **0.340 is far under the 0.70 bar**, and the key re-derived from
the clerk reads the held-out lines no better than v2 (+0.008). Per rule 3's "same knob" clause, the limit is the
sign transcription, not the key values.
Step 4 was not run: no f.268 decode, no reading_v3.txt, no check-solved sweep.

**Sign families that still fail** (count, share of the majority value; see the note column in key v3):
- the 9-shaped g: 43 occurrences, 0.14, spread over p, e, r, t, s, o;
- stand-alone 9: 38, 0.16;
- f: 29, 0.14;
- u: 30, 0.17;
- y: 31, 0.29, spread over r, a and t, as VB-KP saw;
- ff/xff: 29, 0.34;
- single digits 1, 2, 4, 6, 7, 8 and ^7: 0.20-0.43;
- the d family (d, do, Zt, ls): 0.25-0.44;
- word codes 99 and 18: the alignment cuts their spans wrongly, 0.17-0.20.

In short, the families that VB-KP and VB-DECODE2 flagged are still the ones the blind passes cannot separate by
shape.

**Next step (a different instrument, not a third crop pass):** transcribe a few f.260 lines with the clerk's own
decipherment in view, aligned per sign by one careful reader and checked by a second, instead of blind shape-only
passes. That gives grade-C sign pairs for the g/9/y/f/u/d families directly. Also, a pass must not see any other
pass's output.
Requests: gallica.bnf.fr 3 (f.258r and f.260r native, 1 connection-reset retry), scratch only; no image added to the
folder. Subagents: 8 Sonnet.

## While waiting (27 Sept 2026, WAIT-PASS-A)

Waits on nobody outside the repository: the M9 hold-out gate (0.340 vs 0.70 bar) means the block is on
instrument choice, not access, since 27 Sept 2026 (VB-KEY).

- Transcribe f.260 lines with the clerk's decipherment in view, sign-aligned by one reader and checked by a second -- a different instrument than the two blind passes tried. L.
- [done 6 Oct 2026, R12D-VILL: no signal at this coverage, see section below] Decode f.268 restricted to key v3's high-confidence cells only (23 confirmed, cells attested by 2+ occurrences such as s=i, p=i, o=e, r=e, m=u, b=u, e=p, 26=en), leaving the rest as `[MARK]` -- a partial, honestly-graded reading testable now with no new material. M.
- Re-run the known-plaintext alignment through `tools/interlinear_align.py` (the general shared tool) on the same f.260 pairs, instead of the private `kp_key_v3.py`, to check whether the shared tool's hard-EM separates the g/9/y/f/u/d families any better. M.

## Next step (READ2-RELABEL, 3 Oct 2026)
The images are not the blocker. On disk: images/keys/ holds the native Gallica captures of f.268 r and v (canvases 541, 542, 3721x5914, copy-free, no login) and of the three key tables f.270r, 271r, 274r and 275r (manifest.json), and images/sweep/ holds the f.258-f.267 thumbnails. Only f.260 itself is not on disk at full size (its native crops from the 27 Sept 2026 known-plaintext pass were scratch only). The next step is the first "While waiting" bullet above, a different instrument from the two blind crop passes: re-fetch f.260r (canvas 525) at native size with tools/iiif_lines.py, cut line crops, and transcribe the lower and upper cipher blocks with the clerk's decipherment in view, sign-aligned by one reader and checked by a second, then run the alignment through tools/interlinear_align.py; ~$8-10 at the per-pass rate. The status line above stays `blocked` for the Tomokiyo paper route (paper still unread); that is a separate gap and does not stop this step.

## Restricted-key decode of f.268 (R12D-VILL, 6 Oct 2026): no signal at this coverage

Account 4, LANE LANE-RUN12-account-4; the second "While waiting" bullet. Disk only, no requests, no subagents. Status
unchanged: `blocked`. Pre-registered in `PREREG-R12D-VILL.md` (pushed a6bdb8fce before the scored run). Script
`decode_restricted.py` (`--check` exits 0), output `reading_restricted.txt` (a mechanical decode, not a reading).

**Set.** key v3 rows flagged confirmed/confirmed-unclear (f.275 value of record = clerk-alignment majority) with count
>= 2: 30 cells (letters 3/x/Hr=a, ls=d, r/q/o=e, qo=h, s/p/un=i, Hun=l, Hu=m, k/cc=n, do=o, e=p, d=r, a/Z/od=s,
Zt/t=t, b/m=u; words 15 de, 26 en, 61 la, 76 mil, ^16 sa). The secondary set (adding unclear=0 cells) decodes
identically: its extra cells (20, 5, ...) do not occur in f.268.

**Coverage and grades (rule 4).** ciphertext.txt (13 lines, 362 tokens): H 6, M 168, U ([MARK]) 188 -- 48.1% decoded,
no C, no S. ciphertext_v2.txt (verso, 136): H 5, M 62, U 69. The clerk alignment's own agreement for the cells as used
in f.268 averages 0.417 (v1) / 0.410 (v2): by the sibling evidence, more than half of the decoded tokens are expected
to be wrong. "Cryptanalytic result" at best; nothing here is a reading.

**Control (200 class-shuffled restricted keys, seed 20261006; coverage and run positions fixed, only run letters vary).**
Runs of >= 4 letters: v1 4 runs / 18 letters, v2 2 runs / 12 letters.
```
v1 fr16: real -1.4358; shuffled mean -1.9125 sd 0.4738 max -0.7472; z 1.01; rank 38 of 201
v1 fr17: real -1.3618; shuffled mean -1.9150 sd 0.4802 max -0.7320; z 1.15; rank 22 of 201
v2 fr16: real -2.2715; shuffled mean -1.9560 sd 0.4824 max -0.8224; z -0.65; rank 148 of 201
v2 fr17: real -1.9396; shuffled mean -1.9313 sd 0.5085 max -0.9431; z -0.02; rank 112 of 201
```
Gate (z >= 3, rank 1 on fr16) not met. Rule 7 judge on the run text (runs joined, N=189): fr16 `FAIL language:
score=-1.495, null_p99=-1.831, real_p05=-0.9, real_median=-0.777`; fr17 `FAIL language: score=-1.438, null_p99=-1.776,
real_p05=-0.888, real_median=-0.775` (pre-registered as expected and uninformative: the runs are fragments).
Corpus note: fr16 (c.1560-1615) is the nearest era for 1604, fr17 (1617-1644) the nearest register; neither is exact,
and with 18 scorable letters the corpus is not the limit.

**What it shows.** Restricting to the confirmed cells marks every other sign in the block, which breaks the decode into
runs of 1-3 letters: the test has almost nothing to score (18 letters), so "no signal" here is a non-test of the key at
this coverage, not a negative. Fragments such as v1 "EN EN t ... urs" (the "tous ... iours" VB-DECODE noted) recur, but
two runs do not license anything. This confirms VB-KEY: the families that would join the runs (g, 9, y, f, u, the d
family, single digits) are exactly the unconfirmed ones, so the limit is still sign transcription.
Next step unchanged: the first "While waiting" bullet / READ2-RELABEL (f.260 transcribed with the clerk's decipherment in
view, one reader + one checker, then tools/interlinear_align.py), ~$8-10; it needs f.260r re-fetched from Gallica.
