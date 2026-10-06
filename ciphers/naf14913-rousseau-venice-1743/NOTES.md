partial
Souchon, Correspondance diplomatique du comte de Montaigu (1915, Gallica bpt6k935116v) pp. 257 and 268 read by this worker (GF4-BATCH14, 3 Oct 2026, page images + Gallica ContentSearch full text): p. 268 no. 2047, Lorenzi to Montaigu, Florence, 11 Jan 1744 -- the letter around f.206 -- quotes only its clear opening ("On m'assure que le motif du voyage de M. le duc de Modene ... a tous egards..."); the ciphered passage and Rousseau's decipherment of it are not printed.

## M21 — BnF NAF 14913 (Papiers Montaigu), Jean-Jacques Rousseau's decipherments, f.206/214/217/250/274

Check-solved pass, 24 September 2026 (LANE G check-solved worker, session per ROOM.md claim at 03:26 UTC).
Queue row: QUEUE.md M21. `date -u` read at session start: 2026-09-24 03:26 UTC.

### What is established

- Shelfmark BnF NAF 14913, ark:/12148/btv1b525174513 ("Papiers Montaigu"), part of the archival series
  NAF 14904-14937 (archivesetmanuscrits.bnf.fr, cc7393f). The finding-aid note (per QUEUE.md M21, not
  re-fetched this pass) reads: "Aux f. 206, 214, 217, 250 et 274, déchiffrement de dépêches diplomatiques
  de la main de Jean-Jacques Rousseau."
- The Comte de Montaigu was French ambassador to Venice 1743-1749; Jean-Jacques Rousseau was his private
  secretary from September 1743, with duties that explicitly included enciphering outgoing and
  deciphering incoming diplomatic correspondence (widely documented, e.g. in his own *Confessions* and in
  the secondary literature found this pass — see below).
- **Leaf viewed, f.206r** (Gallica IIIF, canvas index 424, corner marked "206"): shows a pasted-in
  fragment of clean, legible running French prose in an 18th-century hand — **not ciphertext**:
  > "venitiens en faveur de la Reine de Hongrie et particulièrement de ceux les plus attachés aux
  > intérêts de cette princesse et qu'ils auroient tout au plus continué de donner sous main des
  > provisions a l'armée de M. le Prince de Lobkowitz."
  This matches the finding aid exactly: what survives at these five folios is the *decipherment*
  (plaintext), already produced by Rousseau in 1743-44, not an encrypted text for us to attack. There is
  no cryptanalysis to do here unless a corresponding ciphertext also survives elsewhere in the Montaigu
  papers (not checked this pass — out of budget) — this is a **transcription/recovery** target at best,
  exactly as QUEUE.md already flagged ("kind: recovery ... decipherment already present, high edition
  risk"), not a cryptanalysis target.

### Six-source sweep, editions first (all dated 24 Sept 2026)

1. **Sender's/recipient's printed edition** — found and confirmed to exist and to cover exactly this
   period: *Correspondance diplomatique du comte de Montaigu, ambassadeur à Venise (1743-1749)*, publiée
   par Joseph Souchon, Paris, 1915 (confirmed via Google Books API with `$GOOGLE_BOOKS_KEY`: 5 distinct
   catalogue entries, all dated 1915, `viewability: NO_PAGES` i.e. not full-text searchable through that
   API; also on Gallica, ark:/12148/bpt6k935116v, `.texteBrut` route 302-redirected to an altcha wall,
   not retried a second time — over the single-retry limit for a challenge page). This edition, by its
   own title, is exactly the ambassador's outgoing/incoming diplomatic correspondence for 1743-1749, the
   same span and same office as NAF 14913.
2. **Leigh's *Correspondance complète de J.-J. Rousseau*** (46 vols., 1965-1998): confirmed to include
   Rousseau's Venice-period letters; a Feb. 1744 letter to Amelot and a May 1744 dispatch to the king are
   both cited in secondary literature (Cairn, see below) as containing passages Rousseau himself
   enciphered — i.e. Leigh's edition is already known to engage with the cipher/decipherment question for
   this exact correspondence, not just the surrounding biography.
3. **Ceitac / "l'affaire des dépêches" literature and the "Dépêches de Venise" corpus**: web search
   surfaced a substantial modern critical-edition history for Rousseau's ~130 Venice dispatches
   ("Dépêches de Venise"): Bernard Gagnebin & Marcel Raymond's Pléiade *Œuvres complètes* vol. III
   (with Jean Starobinski discussing the encoding/decoding experience specifically), followed by a
   dedicated critical edition by **Catherine Labro** (Paris-Genève, Champion-Slatkine/Classiques Garnier,
   2012, in the *Œuvres complètes* vol. 4 project directed by Berchtold/Jacob/Séité), and an edition by
   **Fabrice Brandli** covering vol. 3 (1743-1747) of the same project, announced 2014 (Garnier). A 2015
   *Archives de Philosophie* article (Cairn, "Correspondance diplomatique de Jean-Jacques Rousseau.
   L'initiation à l'art politique dans les Dépêches de Venise") discusses this material at length; full
   text not retrieved (Cairn 403'd WebFetch), only search-result summary available.
   **This is the single strongest signal from this pass**: the primary-source corpus that NAF 14913
   belongs to has been the subject of at least four separate scholarly editions across more than a
   century (1915, ~1960s-90s Leigh, 1959-69 Pléiade, 2012 Labro, 2014 Brandli), specifically because it
   is one of Rousseau's own manuscripts and a famous episode in his biography (the "démêlés" with
   Montaigu, the subject of a whole 1904 book by a Montaigu descendant — see below). Material this
   heavily and repeatedly edited by name specialists is not a plausible "unread" cryptanalysis or even
   recovery target without a specific check against those editions.
4. **Secondary/biographical literature**: Auguste de Montaigu, *Démêlés du comte de Montaigu, ambassadeur
   à Venise, et de son secrétaire, Jean-Jacques Rousseau, 1743-1749* (Paris: Plon-Nourrit, 1904), full
   text on archive.org (`dmlsducomt00mont`, public domain, University of Toronto copy). Downloaded and
   grepped the full djvu text for "chiffr*": nine hits, all general discussion of the cipher dispute
   between Montaigu and Rousseau (Montaigu's incoming dispatches he could not read despite holding the
   ciphers; a later dispute over Rousseau allegedly altering "ses chiffres de correspondance") — this
   book does not itself print the f.206/214/217/250/274 decipherments, but confirms the episode is
   extensively documented from family archives by 1904, well before any of the later critical editions.
5. **Solver repositories**: fresh shallow clones of `dbourdeau/cyphersolver` and
   `aaymeloglu/unsolved-ciphers` (24 Sept 2026), grepped for "montaigu", "rousseau", "naf 14913",
   "naf14913" — no hit naming this as a cipher target in either repository (the isolated word hits found
   are unrelated corpus/source text files).
6. **DECODE (de-crypt.org)**: not logged in (credentials rejected as of 21 Sept 2026, single-attempt rule
   in CLAUDE.md respected, no further login attempt). Site-restricted web search for "Clairambault" OR
   "Montaigu" OR "NAF 14913" returned no relevant de-crypt.org record.
7. **Tomokiyo's Cryptiana**: no page found via web search naming this shelfmark or Rousseau's Venice
   decipherments specifically (Tomokiyo's corpus is mostly pre-1750 diplomatic/military ciphers of
   third-party chancelleries; Rousseau's own household cipher work for Montaigu was not found there).

### Verdict

**Open, but strongly flagged against promotion.** Not directly matched to a specific printed page this
pass (Gallica altcha-walled the Souchon 1915 edition's plain text; Cairn 403'd the 2015 article; Google
Books gives no full text for the Souchon volume; Labro 2012 and Brandli 2014 are recent copyrighted
editions, not checked for exact page content). But the evidence assembled — a named, repeatedly-edited
primary-source corpus (Souchon 1915; Leigh; Pléiade/Candaux; Labro 2012; Brandli 2014), all covering
exactly this ambassador, this secretary, and this 1743-1749 span, plus the leaf itself showing an
already-legible plaintext decipherment rather than ciphertext — makes this very likely **found-solved**
in substance even though no exact page match was confirmed. This is not a cryptanalysis candidate (no
ciphertext survives on the folios examined) and is a poor recovery candidate given the edition risk.

**Recommend:** do not promote to the board. If pursued at all, the next step is a print-check worker with
JSTOR/Cairn access reading the 2015 Archives de Philosophie article in full and checking Labro's 2012
edition (via WorldCat/library) for whether it transcribes f.206/214/217/250/274 specifically — not a
solving task, an editions-confirmation task.

### Access route

Gallica IIIF, public domain, no login; this manuscript (unlike Clairambault 1161) has full folio-level
labels in its IIIF manifest, so canvas-to-folio lookup was exact and reliable.

### Requests this pass (gallica.bnf.fr)

browser_fetch.js: 1 manifest fetch (success, first attempt), 1 full-resolution image fetch for f.206r
(success, first attempt). No curl attempts against this ark (manifest/image fetches went straight to
browser_fetch.js after the Clairambault 1161 pattern of curl failures on this host this pass). No
403/altcha/Cloudflare challenge seen. archive.org: 1 metadata call, 1 be-api full-text-search call, 1
djvu.txt download for the 1904 Montaigu book (all succeeded, all public-domain full-text, no login).
Google Books: 2 calls with `$GOOGLE_BOOKS_KEY` + `country=US` (credential not printed).

## NX-UNBLOCK (26 Sept 2026)

The recommended next step ("a print-check worker with JSTOR/Cairn access reading the 2015 Archives de
Philosophie article in full and checking Labro's 2012 edition") is really a paywalled-content read, not a
free-route job -- converted per CLAUDE.md's NX-UNBLOCK brief into: two JSTOR-QUEUE.tsv rows (family (i),
sender/recipient/place + cipher keyword; family (ii), the 2015 article's own title, no cipher keyword, in case
JSTOR independently indexes it or citing scholarship), and LOCAL-QUEUE.tsv row L25 (`edition-read`, the
owner's own Cairn access for the article itself, plus a WorldCat check for Labro 2012). No change to the
target's `open` status or its "do not promote" recommendation pending those reads.

queued JSTOR rows, 26 Sept 2026, QUEUE-FILL.

## JSTOR runner, 26 Sept 2026

Four queries run (ChatGPT JSTOR runner, [JSTOR-2026-09-26-2013], PR 28). The runner's browser was **not
logged in to JPASS** on this run, so three of the four candidate hits below could not actually be read online
(JSTOR showed a "Register for a free account" prompt or "This is a preview. Log in through your library"
instead of the reader) -- requeued in JSTOR-QUEUE.tsv as "reread needed", not `done`. See ASKS.md (row filed
this session) for the owner to re-log the runner in and re-fire, or read the four blocked candidates himself.

- `"Montaigu" AND "Rousseau" AND "Venise" AND (chiffre OR déchiffrement OR "dépêches")`: two **candidate prior
  print, unread** -- Antoine Hatzenberger, "Correspondance diplomatique de Jean-Jacques Rousseau: L'initiation
  à l'art politique dans les 'Dépêches de Venise'", Archives de Philosophie 78(2), 2015, pp. 323-342,
  https://www.jstor.org/stable/24719303 (blocked: "Register for a free account"); M. Thomas, "Nouvelles
  acquisitions latines et françaises du Département des manuscrits de la Bibliothèque nationale pendant les
  années 1965-1968", Bibliothèque de l'École des chartes 127(1), 1969, pp. 87-212,
  https://www.jstor.org/stable/42957196 (blocked: preview/library-login wall) -- the Thomas article covers
  NAF 14913's acquisition by the BnF, the Hatzenberger article's title names the "Dépêches de Venise" directly.
  Neither has been read; this is a search result (rule 10), not a verdict. Context only, not read: Delon 2020-21
  (stable/28022594), Roche & Launay 1968 (stable/40951201).
- `"Correspondance diplomatique de Jean-Jacques Rousseau" AND "Dépêches de Venise"`: same Hatzenberger 2015
  candidate as above, same block, reread needed.
- `"Rousseau" AND "Montaigu" AND Venise AND déchiffrement`: same two candidates (Hatzenberger 2015, Thomas
  1969) as the first query, same blocks, reread needed.
- `"venitiens en faveur de la Reine de Hongrie"`: no relevant hit (0 results).

For the parent/verifier: this target has two unread candidate prior-print articles (Hatzenberger 2015, Thomas
1969) -- route a check-solved/verifier read once the reread (logged-in) pass confirms what they say about the
NAF 14913 decipherments.

## CHECK-NAF (26 Sept 2026)

Free-route read of the two PR-LAND-8 candidates (ASKS 76 free-routes-first job), `date -u` read at claim,
21:45 UTC.

**Thomas 1969 -- READ, full text, free (Persée, no login).** M. Thomas, "Nouvelles acquisitions latines et
françaises du Département des manuscrits de la Bibliothèque nationale pendant les années 1965-1968",
*Bibliothèque de l'École des chartes* 127-1 (1969), pp. 87-212, https://www.persee.fr/doc/bec_0373-6237_1969_num_127_1_449826
(confirmed same DOI/pagination as the JSTOR-QUEUE row 88-91 candidate, stable/42957196). Persée serves this
article's full OCR text per page (`?pageId=T1_<n>`), no login, no paywall; fetched every page 89-212 (124
requests, 1.5s apart, one host at a time, no challenge) and grepped for "Montaigu", "Rousseau", "14913",
"déchiffr", "Venise".

The NAF 14913 entry is on p. 149, inside the full inventory of "14904-14937. Papiers Montaigu. I. --
Correspondance diplomatique du comte Pierre-François de Montaigu (14904-14931)":

> "IX-XIV (14912-14917). Lettres adressées au comte de Montaigu par les ambassadeurs et ministres du roi
> auprès des cours de : [...] X (14913). Constantinople et Florence (n°s 1972-2128). Aux ff. 206, 214, 217,
> 250 et 274, déchiffrement de dépêches diplomatiques de la main de Jean-Jacques Rousseau. -- 392 ff."

This is word-for-word the origin of the BnF finding-aid sentence already quoted in this file's 24 Sept
entry ("Aux f. 206, 214, 217, 250 et 274, déchiffrement de dépêches diplomatiques de la main de Jean-Jacques
Rousseau"): Thomas 1969 is a cataloguing/acquisition notice describing what physically survives at those
five folios (a decipherment in Rousseau's hand, folio count, format), not a transcription or quotation of
the deciphered text itself. No plaintext, extract or quoted passage from f.206/214/217/250/274 appears
anywhere in the 126-page article. The only other NAF-14913 mentions found: p. 89-90 (a one-sentence mention
of "les archives diplomatiques du comte de Montaigu ... dont Jean-Jacques Rousseau fut un temps le
secrétaire" in the article's general introduction, no folio detail); pp. 103-104 (the article's own
alphabetical name/place index: "Rousseau (Jean-Jacques). [...] Documents de sa main, n. a. fr. 14904-14905,
14913, 14917-14918, 14922, 14926-14927" and "Venise. [...] n. a. fr. 14904-14937" -- index entries, not
text); p. 148/150-151 (the rest of the same Montaigu inventory, other cotes, no further 14913 detail); p.
119, 157, 160 (unrelated items -- a different Rousseau letter of 1751 in an autograph album, Jean-Baptiste
Rousseau's own papers at n.a.fr. 15008, and an unrelated "Séjours ... à Venise" travel diary).

**Verdict: Thomas 1969 does not print, or cite anyone else's print of, the deciphered text of any of the
five folios.** It confirms the acquisition and the finding-aid wording, nothing more. This candidate is
resolved: read in full, negative for found-solved.

**Hatzenberger 2015 -- still UNREAD.** Cairn (shs.cairn.info) is DataDome-challenged from this container:
both a plain curl (403, JS-challenge page) and one `browser_fetch.js` pass (3 internal retries, all 403,
`Please enable JS and disable any ad blocker` / captcha-delivery interstitial) failed on the article page
(`shs.cairn.info/revue-archives-de-philosophie-2015-2-page-323`) and on the OpenAlex-listed green-OA PDF
(`shs.cairn.info/article/APHI_782_0323/pdf?lang=fr`, from `https://api.openalex.org/works/W1893805836`,
`open_access.oa_status: "green"`) -- one attempt each, not retried further per the good-citizen rule. No
other free host mirrors this article (OpenAlex, Semantic Scholar and Google Books searched; only the Cairn
copy is indexed as available). OpenAlex's own abstract (free, no login) reads: "En 1743-1744, Jean-Jacques
Rousseau servit comme secrétaire de l'ambassadeur de France à Venise. Le récit qu'il donne de ce séjour dans
les Confessions mentionne les 'célèbres amusements de cette ville' [...] Touchant aux questions des formes
de gouvernement et des relations internationales, les Dépêches de Venise peuvent se lire comme une
initiation à l'art politique" -- consistent with a discursive/interpretive study of the published despatches
(Pléiade/Leigh), giving no indication it transcribes the unpublished NAF 14913 decipherment folios
specifically, but this is an abstract, not the article, so the candidate stays formally unread. Remaining
route: JSTOR (stable/24719303), gated on ASKS 76 (JPASS login for the runner).

**Net effect on this target: no change to `open` status.** One of the two candidate prior prints
(Thomas 1969) is now read and closed out negative; the other (Hatzenberger 2015) is still blocked on the
JSTOR reread named in ASKS 76. Requests this pass: persee.fr ~127 (1 search, 2 doc/page loads, 124 page
fetches, 1.5s apart), api.openalex.org 2, googleapis.com/books 1, cairn.info/shs.cairn.info 3 (1 curl + 1
browser_fetch page fetch + 1 browser_fetch PDF fetch, all 403, no retry loop). No logins attempted.

Brief note (.claude/briefs/runs/2026-09-26-parent-check-naf.md) asked for "one AUDIT.md line in the
check-solved shape the file already uses" -- this target has no AUDIT.md (no verifier has run on it yet;
CLAUDE.md rule 10 reserves N-class assignment to a separate verifier session after a logged search, not to
this check-solved supply job). Per CLAUDE.md over the brief: not creating one here. A verifier taking this
up next has both candidates' status (one read negative, one still blocked) ready to cite.

## While waiting (27 Sept 2026, WAIT-PASS-B)

Waits on: a JSTOR reread of Hatzenberger 2015 (stable/24719303), gated on ASKS row 76 (JPASS login for the
runner), open since 26 Sept 2026 -- the JPASS credentials are reported in hand per the owner (26 Sept 2026
23:38 UTC), next run pending. LOCAL-QUEUE row L25 (Labro 2012 via WorldCat/Cairn) also pending since 26 Sept
2026.

- S: phrase-search f.206r's own quote ('venitiens en faveur de la Reine de Hongrie...') via Google Books/archive.org be-api -- only tried on JSTOR so far.
- M: fetch and read the four unviewed Gallica folios (f.214, f.217, f.250, f.274) via IIIF, the same free no-login route already used for f.206r -- tools/gallica_folio.py + tools/iiif_lines.py.
- S: full-text search Souchon 1915 (Gallica ark bpt6k935116v) inside the volume for the 1743-44 passage; only its catalogue entry has been checked so far, not the text itself.

## Web and blog check (GF4-BATCH14, account-4, 3 Oct 2026)

Plain web searches (WebSearch): (1) `Rousseau Montaigu Venise 1743 1744 déchiffrement "14913"` -- Hatzenberger 2015 (Cairn),
Larousse, Wikipedia chronology, BnF Editions "La Musique a Venise", Wikisource *Démêlés du comte de Montaigu*, rousseau-chronologie.com;
none prints a NAF 14913 decipherment; (2) `Rousseau secrétaire Montaigu déchiffrement dépêches chiffre Venise manuscrit BnF` --
the BnF finding aid NAF 14904-14937 (cc7393f), Cairn, Confessions VII on Wikisource (Rousseau's own "en moins de huit jours j'eus
dechiffre le tout"); (3) phrase `"venitiens en faveur de la Reine de Hongrie"` -- no hit for this text; (4) `Rousseau cipher
Venice Montaigu secretary deciphered dispatches` -- Confessions VII translations, generic Venetian-cryptology pages;
(5) model-solve query `Rousseau Venice cipher deciphered solves Claude OR GPT` -- only Cyphral Distich and Napoleon-letter news.
Blog site search: `Rousseau Montaigu chiffre site:scienceblogs.de OR site:ciphermysteries.com OR site:cryptiana.blogspot.com` --
no post on any of the three (Cipherbrain, Cipher Mysteries, Cryptiana) about this item; no comment thread to open.
Phrase searches on f.206's own text (Google Books API, key + country=US): `"en faveur de la Reine de Hongrie et particulièrement"`,
`"attachés aux intérêts de cette princesse"`, `"sous main des provisions"` -- no hit for this passage (the last finds only an
unrelated 1743 periodical, *Le Persan en Empire*, on Lobkowitz). Gallica ContentSearch inside Souchon 1915 for
`"attachés aux intérêts de cette princesse"`: 0. Pleiade *Oeuvres completes* III (1964, Google Books ORkFJd3jMloC, NO_PAGES):
snippets show Rousseau's own outgoing despatches (23 May 1744 to Du Theil, "Lobkowitz ... faute de provisions"), a different text.
Cabinet Noir (el-descifrador/cabinet-noir HEAD 47b6db9, CC BY 4.0) grep for 14913, rousseau, montaigu: nothing.

## Premise check (GF4-BATCH14, account-4, 3 Oct 2026)

(a) **Folder's own mentions -- FOUND: the item carries its own period decipherment.** The finding aid (Thomas 1969 p.149) and
the 24 Sept view of f.206r already say the five folios are Rousseau's *decipherments*. This pass looked at the leaves either
side: Gallica btv1b525174513 view 424 (**f.205v**) is a clear letter (Duc de Modene at Venice, the Masse succession, M. de
l'Hopital's Constantinople news) that ends in **numeral cipher groups** ("les idees des 648.326.722.154.444.303.67.66.22.31.");
view 427 (**f.207r**) opens with four more lines of numerals ("22.628.601.715.247.22.299 ...") before the clear text resumes
(Prince Charles of Lorraine's wedding feast "le 7", M. Viale's memoire to the Regency). View 425 (**f.206r**) is the small slip
in Rousseau's hand bound between them: "[...] venitiens en faveur de la Reine de Hongrie et particulierement de ceux les plus
attaches aux interets de cette princesse et qu'ils auroient tout au plus continue de donner sous main des provisions a l'armee
de M. le Prince de Lobkowitz." Its first word picks up the cipher's lead-in "les idees des" -- so f.206 is the period
decipherment of the numeral passage on ff.205v/207r (reading of the fit: grade I, from position and sense; no group-level
check run). Souchon p.268 identifies the letter as **no. 2047, Lorenzi, Florence, 11 Jan 1744**. **Correction to the 24 Sept
entry above** ("no ciphertext survives on the folios examined"): ciphertext does survive, on the leaves around the slip.
(b) **Other solvers' working files -- not found.** Bourdeau and Aymeloglu (24 Sept clones): no hit; Cabinet Noir: none.
(c) **Physical neighbours -- found, see (a).** Views 424-427 viewed at 600 px (enough to tell clear from cipher and to read the
slip); view 426 (f.206v) blank. Ff.214, 217, 250, 274 not viewed this pass.
(d) **Recipient's side -- partly checked.** Souchon 1915 is the recipient-side edition (letters *to* Montaigu): p.257 opens
NAF 14913's Constantinople letters (nos. 1972-2029), pp.267-275 the Florence letters (Lorenzi); p.268 prints no. 2047's clear
opening only. Leigh's *Correspondance complete* (Rousseau's own letters; not online, copyrighted) not checked -- the incoming
Lorenzi letter is not Rousseau's, so it is an unlikely home for it; Hatzenberger 2015 still unread (ASKS 76).

**Consequence (for the parent):** what the premise check describes is a cipher passage with a period decipherment bound beside it,
not an unread cipher. Nothing printed of the deciphered text was found (Souchon p.268, phrase searches), so this is not
`found-solved` under the brief's printed-or-posted test, and the status word stays **`open`** -- but it is a **calibration /
key-recovery item** (a period plaintext against a numeral code, the Lorenzi-Montaigu cipher of 1744), never a cryptanalysis target.
No novelty implied (rule 10).

Requests this pass: gallica.bnf.fr 26 (19 ContentSearch on Souchon, 1 NAF 14913 manifest, 4 NAF 14913 IIIF images, 2 Souchon
page images); googleapis.com/books 9; WebSearch 6. All >=1.5 s apart per host.

## While waiting

(Superseded 3 Oct 2026 by FT4's Remaining gaps below: the ff.214/217/250/274 image check is now its cheapest next step.)
Next step that depends on nobody: view ff.214, 217, 250, 274 and their facing leaves (Gallica btv1b525174513, IIIF, free) to
list which Lorenzi/Castellane cipher passages each Rousseau slip renders, and match them to Souchon's numbers (pp.257-275);
about $0.5, image check only, no transcription. (The JSTOR reread of Hatzenberger 2015, ASKS 76, and LOCAL-QUEUE L25 stay
where they are.)

Gate re-run (GF4-BATCH14, 3 Oct 2026): `python3 tools/intake_gate_check.py naf14913-rousseau-venice-1743` -> "naf14913-rousseau-venice-1743: open (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0 (was exit 1, no standard-edition citation). `python3 tools/next_steps.py --wait-only | grep naf14913-rousseau-venice-1743` -> no line.

## FT4-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (GF4-BATCH14 premise find, e20e9c77): key recovery from Rousseau's f.206r slip against the numeral passage on
f.205v (last line) and f.207r (lines 1-5). No cryptanalysis: every meaning comes from the period decipherment (grade C/M).

- **Images.** Gallica btv1b525174513, IIIF regions cut with `tools/iiif_lines.py` (commands run 03:36-03:38 UTC):
  `python3 tools/iiif_lines.py --ark btv1b525174513 --canvas 424 --region 1000,4430,3150,360 --out ciphers/naf14913-rousseau-venice-1743/images --prefix f205v --centres 180 --debug`
  (1 line, 2 crops); `... --canvas 427 --region 1000,520,3300,1180 ... --prefix f207r --debug` (5 lines, 10 crops);
  `... --canvas 425 --region 900,3780,3300,700 ... --prefix f206r --debug` (slip, 4 lines, 8 crops). Overviews v424/v425/v427_1000.jpg.
  The first two calls used `--ark ark:/12148/btv1b525174513`, which the tool doubles into a bad URL (HTTP 500, my error,
  2 requests); rerun with the bare id.
- **Transcription** (`ciphertext.txt`, `ciphertext.tsv`): 62 groups, 50 distinct, three-digit and two-digit numerals
  (10-834). Pass A (the worker, from the debug overlays) and pass B (one blind Sonnet subagent on the 12 numeral crops)
  agree on 59/62; reconciliation on a cut strip of the three groups: f.205v group 1 = **548** (B; A had 648), f.207r L1
  group 5 **247 or 217** and L2 group 6 **24 or 21** (cursive 4 vs 1, left M). The 5 of 635 is underlined in the MS.
  The slip (`slip_f206r.txt`) reads as the 24 Sept and GF4-BATCH14 passes; "particulierem.t" expanded for alignment.
- **`tools/interlinear_align.py`** (`align/pairs.tsv`, one pair: the whole passage against the slip). From a flat start
  on a single pair it only spreads the 192 letters evenly over the 62 groups (tried `--floor 0 --max-chunk 16` with
  `--len-prior` 0.3/0.6/1.0 x `--seg-bonus` 1/2, 10 iterations): repeated groups do not lock (22 took "de" twice, "n"
  and others elsewhere). With one pair there is nothing for hard-EM to agree with across pairs, so it is not a test
  of the key here. Not used for key.tsv.
- **Consistency search** (`align/consistency_search.py`, output `align/consistency_search.out`): the evidence a single
  pair offers is that a repeated group must take the same chunk at every occurrence. Seven values repeat (22 x6, 581
  x3, 66/279/336/501/722 x2: 19 occurrences). The search assigns chunks (1-9 letters) to the repeated values under
  exact coverage of the slip, and the statistic S = letters carried by repeated groups in the best fully consistent
  assignment. **Real: S = 42**, best maps 22=de, 66=r, 279=plus, 581=au, 722=ti, 501=eet (word boundary gives "et";
  the max-letters statistic prefers hongri|eet), 336 = de / in / pr (three maps tie).
  **Per-leaf pairing-shuffle control** (rule 3, per-unit; the statistic depends on where the repeats fall, so the
  shuffle can change it): 200 shuffles of the group order, same slip. 150 have no consistent assignment at all, 42
  complete with S 21-41 (max 41), 8 hit the 25 s per-shuffle limit and are counted as >= real (conservative).
  p95 35, shuffles >= real 8/200, **p = 0.045 -> PASS, thin** (the conservative timeout count is most of the tail).
  The gate (real S above shuffle p95) is written in the script's docstring; it was not committed before the run, so
  it is not pre-registered. A first run at a 4 s limit (34 timeouts counted >= real) gave p = 0.17, FAIL, an
  artefact of the time limit; a maxlen-6 run was infeasible for the real order ("la reine" is 7 letters in one group).
- **Key** (`key.tsv`, 50 codes): **C** for the six repetition-fixed values above and for four single groups standing
  between two fixed ones (31 = la reine, 628 = hongrie, 172 = qu'ils, 379 = [x]interets); **M** for the other 40
  codes, which are splits of multi-group stretches by word and syllable boundary (e.g. 548 ve / 326 ni; 715 + 247 =
  particulierement; 443 24 271 208 = princesse), and 336 = sous|pr unresolved.
  Internal checks that agree with the C values without being used to set them: 722 = ti in both veni-ti-ens and
  con-ti-nue, 581 = au in au(x), au(roient), (tout) au, 66 = r in faveu-r and au-r-oient.
- **Decode**: `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743` (decode.json) -> `reading.txt`,
  `reading_tokens.tsv`: **tokens 62: H 0, C 21, S 0, M 41, I 0, U 0**; `--check` -> "reading up to date", exit 0.
  This is a cryptanalytic-free key recovery, not an H reading: no key sheet. Judge not run (no spec for this target;
  the plaintext is the period decipherment itself, so a language judge would test Rousseau's French, not the key).
- **Design note** (inference): a French syllabic nomenclator of the 1740s, two- and three-digit groups, syllables (ve,
  ni, ti, au, r) beside whole words and phrases (plus, hongrie, la reine, qu'ils): the Lorenzi-Montaigu cipher of 1744.
- **Other leaves**: not looked at this pass. The finding aid names slips at ff.214, 217, 250, 274; whether their facing
  leaves carry numerals of this same key, and whether any leaf carries these numerals with no slip, is the next step
  (image check only).
- Requests: gallica.bnf.fr 11 (3 overview images, 2 info.json, 2 failed region fetches HTTP 500 from my ark error,
  3 region fetches for crops, 1.5 s+ apart). Vision: 1 blind Sonnet subagent pass (12 numeral crops) + 3 worker views
  (two overlays, one reconciliation strip of three groups, plus a reference strip).

Not found in: Souchon 1915 p.268 (clear opening only), the phrase searches logged above (GF4-BATCH14). Rule 10: this
reports what was read and where it was not found; no novelty class is assigned here.

## FT4b-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4's Verdict): image check of the ff.214/217/250/274 slips and their facing leaves for numerals of the f.206
key. No transcription. Canvases from `python3 tools/gallica_folio.py btv1b525174513 --folio N` (one constant offset,
k=14 over f15-f592: recto canvas = 2N-1+14). 16 leaves fetched at 1000 px wide (`images/lowres/`, manifest entries
`lowres_check`), cropped to the text block and set in two contact sheets of 8 (`sheet_214_217.jpg`,
`sheet_250_274.jpg`, 500 px per leaf), one vision call each (2 of 2 allowed). What the sheets show, by leaf:

| slip | leaf | what is on it (low-res view; group counts are line x groups-per-line estimates, not counts) |
|---|---|---|
| f.214 | 213v | numeral cipher, 3 lines at the top of the page (about 30 groups), then clear prose; the passage starts above, so it likely begins on 213r (not viewed) |
| f.214 | 214r | pasted slip, clear French, headed "Du 1er fevrier 1744": "Par la conqueste des 2 Siciles la Rep. de Venise garantissoit la possession actuelle ..." (about 9 lines) |
| f.214 | 214v, 215r | 214v: the slip's back (show-through only); 215r: clear prose, no numerals |
| f.217 | 216v | numeral cipher, about 9 lines (roughly 85-95 groups) after the clear words "Ma derniere lettre de", then clear prose |
| f.217 | 217r | pasted slip, clear French: "...Vienne, porte que la Rep. de Venise, considerant les grands troubles qui regnent par tout tachoit de se tenir dans un certain equilibre ..." (7 lines) -- the slip opens on the word the cipher passage needs ("Ma derniere lettre de / Vienne porte que") |
| f.217 | 217v, 218r | 217v: the slip's back (show-through); 218r: clear prose, no numerals |
| f.250 | 249v | numeral cipher, 4 lines at the top (about 50 groups), then clear prose ("Il arriva ici le soir du 26 ..."); may begin on 249r (not viewed) |
| f.250 | 250r, 250v | slip, clear French on both sides ("...Gnal Maulli avoit ecrit ... secourir la Reine de H. de la maniere ..." continuing on 250v to "... connoissance de la Maison de Bourbon") |
| f.250 | 251r | clear prose, end of a Lorenzi letter (signed), no numerals |
| f.274 | 273v, 274r, 274v, 275r | no numerals seen on any; 274r is a full letter page ending "Lorenzi", no pasted slip distinguishable at this resolution; 275r a new letter, Florence 15 Aug 1744. Not located. |

Same key, at grade M (read off the low-res sheet, not transcribed): values of FT4's C-graded codes appear in all three
new passages -- 22 and 722 and 501 on 213v; 22, 66, 306 and 326 on 216v; 22, 66, 24, 722, 279, 306 and 208 on 249v -- and
the hand, numeral size and dot separators match ff.205v/207r. So three more cipher+slip pairs exist under what looks
like the f.206 key: f.216v<->f.217r (the largest, about 90 groups), f.249v(+249r?)<->f.250r-v, f.213v(+213r?)<->f.214r.
f.274's pair was not found in these four leaves.

Requests: gallica.bnf.fr 16 (IIIF image API, 1000 px, 1.6 s apart, all HTTP 200) + 0 manifest (cached). Vision: 2 calls.

### Pre-registered gate for the f.206 key (written 3 Oct 2026, before any new passage is transcribed or scored)

Applies to the next job (and any later one) that transcribes a new cipher+slip pair from this volume and scores the
f.206 key against it. Fixed now so the threshold cannot be chosen after the numbers are seen.

- **Unit and statistic.** Per new pair (one cipher passage against its own slip), take the occurrences in the new
  passage of FT4's ten C-graded codes (22 de, 66 r, 279 plus, 581 au, 722 ti, 501 et, 31 la reine, 628 hongrie,
  172 qu'ils, 379 interets). Run `align/consistency_search.py` (extended to take a pair and fixed values as
  constraints) with every repeated code consistent and the C codes pinned to their f.206 values. **H =** the number of
  pinned C-code occurrences in the best fully consistent exact-coverage segmentation of the slip (0 if none exists).
- **Controls (both must be beaten).** (a) *Value permutation*: the same search with the ten f.206 values permuted
  among the ten codes (200 permutations, derangements only); this changes which value is pinned where, so it can move
  H. (b) *Pairing shuffle*: the new passage's group order shuffled (200 shuffles), the same pins; moves where the pins
  fall. A shuffle or permutation that times out is counted as >= real (conservative, as FT4).
- **Threshold.** PASS for the key on that pair: H >= 5 AND H > p95 of control (a) AND H > p95 of control (b). If the
  new passage carries fewer than 5 occurrences of the ten C codes, the pair is a **non-test** of the key (power floor),
  not a FAIL. FAIL on a pair with >= 5 occurrences: the f.206 key is not the key of that passage (different key or a
  key change); C grades in key.tsv stay as they are for the f.205v/207r passage only, and the key is not applied to
  other leaves.
- **Per-leaf before merging** (rule 3, Szembek paragraph): a new pair's own repetition-consistent values enter key.tsv
  only from a pair that PASSes; codes attested only on a non-test or FAIL pair stay out. A pooled re-run of FT4's
  shuffle control over f.206 + the new pair(s) then decides whether M codes move to C.
- **Order.** First pair to score: f.216v <-> f.217r (largest). Transcription per TRANSCRIPTION.md: line crops with
  `tools/iiif_lines.py`, two blind passes per crop set, reconciliation as a priced unit.

## FT4c-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4b's Verdict): transcribe f.216v + f.217r and score the f.206 key against FT4b's pre-registered gate, unchanged.

- **Crops** (commands run 04:28-04:29 UTC; canvases 446/447 from FT4b's offset):
  `python3 tools/iiif_lines.py --ark btv1b525174513 --canvas 446 --region 1700,3330,3034,1870 --out ciphers/naf14913-rousseau-venice-1743/images --prefix f216v --debug`
  (8 lines, 16 crops; a first cut at width 2950 clipped line 1's last group and was deleted and re-cut) and
  `... --canvas 447 --region 1100,250,3000,1950 ... --prefix f217r --debug` (9 bands, 18 crops; L01 is the "Lorenzi" header).
- **Transcription.** `ciphertext_f216v.txt`: 79 groups, 62 distinct (one blind Opus pass on the 16 numeral crops; it
  agrees with the worker's view of the debug overlay; three unsettled groups kept as a|b: 240|24v, 521|321, 369|569 --
  none is a C code and none repeats, so none can move H). `slip_f217r.txt`: one blind Opus pass on the 16 slip crops,
  "...Vienne, porte que la Rép.e de Venise, considerant ... sans rien conclurre avec personne./." (Rép.e expanded to
  Republique for alignment; 245 letters). The cipher's clear lead "Ma derniere lettre de" is followed by the slip's
  first word "Vienne". 2 of 3 vision calls used; the reconciliation call was not needed (no unsettled group can affect
  the statistic).
- **Pre-registration kept.** `align/gate_pair.py` (the registered statistic, controls and threshold; MAXLEN fixed at 12
  because the slip has an 11-letter word) and both transcriptions were committed and pushed (36dc751d) before the first
  score. Nothing in the gate was changed after.
- **Score** (`align/gate_f216v.out`, `python3 align/gate_pair.py --cipher ciphertext_f216v.txt --slip slip_f217r.txt --n 200 --limit 10`):
  C-code occurrences in the passage: 22 x3, 66 x1, 501 x1 = **5** (exactly the power floor, so a test, not a non-test).
  **Real H = 5**, all three codes pinned (22 de, 66 r, 501 et) in a fully consistent exact-coverage segmentation (found,
  no timeout). Control (a) value permutation, 200 derangements: mean 0.92, **p95 3**, max 4, all 200 hit the time limit
  and were counted at their highest relaxed-feasible pin set (conservative, high); >= real 0/200. Control (b) pairing
  shuffle, 200: mean 0.54, **p95 2**, max 4, 50 timeouts counted high; >= real 0/200. **GATE PASS** (H 5 >= 5, > 3, > 2).
  Thin: the passage carries the floor number of pinned occurrences, and only three of the ten C codes occur.
- **Key.** 22, 66 and 501 gain a second witness (key.tsv note column; grades unchanged, already C). New codes: none enter
  key.tsv. `align/forced_f216v.py` (`align/forced_f216v.out`) lists, with the three pins fixed, every chunk each of the
  12 repeated free codes can take: no code is forced to one value (63 x2 narrows to q/qu/que, "porte que" / "et que";
  232 to five; the rest 8-29). So the pair passes the key's gate but fixes no new value by itself; the pooled
  f.206 + f.216v run named in FT4b ("Per-leaf before merging") is the step that can.
- **Decode.** No reading changed: `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` ->
  "tokens 62: C 21, M 41 / reading up to date", exit 0 (H 0, C 21, S 0, M 41, I 0). The f.216v passage is not decoded
  into reading.txt (its codes are not in key.tsv beyond the three).
- Requests: gallica.bnf.fr 5 (info.json f446, f447; region fetches 446 twice, 447 once; 1.6 s+ apart, all HTTP 200).

Not found in: no print or phrase search was run this step (transcription and scoring only). Rule 10: no novelty class here.

## FT4d-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4c's Verdict): pooled f.206 + f.216v consistency run. Rule 3: a pooled re-run with new material (f.216v),
allowed once; a FAIL is logged and the next step names the f.249v/f.250r and f.213v/f.214r pairs as new material.

### Pre-registration (committed and pushed before the first scored run, 3 Oct 2026 ~05:15 UTC)

`align/pooled_gate.py` (docstring holds the full definition; nothing in it is changed after this commit):
- **Statistic Hp.** Both pairs at once (f.205v/207r vs f.206r slip, maxlen 9 as FT4; f.216v vs f.217r slip, maxlen 12 as
  FT4c), FT4's ten C codes pinned to their f.206 aligned chunks in both passages (379 pinned as `xinterets`, the chunk FT4
  aligned for "aux interets" -- key.tsv's bare "interets" makes the f.206 pins jointly infeasible with 581=au, found while
  writing this script, before any score). Hp = the largest sum of occurrences (both passages) of a set of non-C codes
  shared by the two passages that can be tied to one identical chunk across both, in segmentations that exist together
  (every repeated code still consistent within its passage). Shared non-C codes: 10, 121, 208, 306, 338, 420, 444, 781,
  824 (26 occurrences).
- **Controls, pooled N.** (a) value permutation: f.216v's non-C labels permuted among its own non-C distinct labels, 100;
  (b) pairing shuffle: both passages' group orders shuffled, 100. Time limit 4 s per control run (timeouts counted high),
  60 s per tied set for the real run (timeouts counted not reached); seed 7.
- **Gate.** PASS: Hp >= 5 AND Hp > p95(a) AND Hp > p95(b). Fewer than 5 shared non-C occurrences = non-test.
- **Key rule.** A shared code with exactly one joint chunk (relaxed, pins fixed: `forced-check` lines) that is also in the
  real best tied set enters key.tsv at C only on PASS; otherwise key.tsv is unchanged.

### Result (run 3 Oct 2026 05:05-05:07 UTC, `align/pooled_gate.out`, `python3 align/pooled_gate.py`, defaults n 100, limit 4, seed 7)

- **Real Hp = 23** of 26 shared non-C occurrences, no timeout: tied 208 se, 781 e, 306 s, 824 don, 444 n, 121 s, 10 a,
  420 t (338 is the one shared code left untied).
- Control (a) value permutation, 100: mean 12.84, **p95 18**, max 21; 98 of 100 hit the 4 s limit and were counted high
  (conservative); >= real 0/100 (p = 0.0099). Control (b) pairing shuffle, 100: every draw Hp 0 (with both orders
  shuffled the ten pins admit no exact-coverage segmentation in at least one passage), **p95 0**; >= real 0/100. This
  control could have scored (the statistic depends on order, and pin feasibility is part of it), but at this N it is
  weak: it says the pins themselves only fit the real order, which FT4/FT4c already showed. Control (a) is the one with
  teeth. **GATE PASS** (Hp 23 >= 5, > 18, > 0).
- **Forced codes** (relaxed, pins fixed; joint chunks feasible in both passages): 208 -> {se}, 338 -> {t}, 781 -> {e};
  every other shared code has 3-15 joint chunks (306 es/les/s, 824 d/do/don/donn, 444 five, 121 eight, 10 ten, 420
  fifteen). Key rule (registered): forced AND in the real tied set -> C. **208 = se** (C; was M "sse": f.206 princes|se,
  f.216v "tachoit de se tenir" = 22 208) and **781 = e** (C; already M "e"). 338 is forced to "t" only if tied, and it is
  not in the tied set (f.206 M "tout" stays; the two passages disagree on it under this model), so it stays M.
  271 re-split ce -> ces (M) so that 443..208 still reads "princesse"; the reading text is unchanged.
- **Decode:** `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 /
  reading up to date", exit 0 (H 0, C 23, S 0, M 39, I 0, U 0; was C 21 M 41).
- Requests: none (disk only). Vision calls: 0.

Not found in: no print or phrase search was run this step. Rule 10: no novelty class here.

## FT4e-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4d's Verdict): transcribe the f.249 cipher passage and the f.250 slip, score the per-pair FT4b gate
(align/gate_pair.py, unchanged), then the pooled three-pair run. Rule 3: this is the third pooled attempt with the same
instrument, and here it is used on new material (a third pair), not on a changed setting.

- **Material.** The passage starts on **f.249r**, not on f.249v as FT4b assumed: 5 numeral lines at the foot of 249r after the
  clear words "...vous citer mande par sa derniere que" (letter of Lorenzi, Florence 30 May 1744, red no. 2067, docket "repondue le
  6 Juin"), then 4 lines at the top of 249v before "Il arriva ici le soir du 26". 111 groups, 78 distinct (`ciphertext_f249.txt`).
  The slip, f.250r (12 lines) + f.250v (2 lines), is `slip_f250.txt`: "Le G.nal Marulli avoit écrit à sa Cour que quelques mouvemens
  qu'il se fût donnés pour engager la / la Rep.e de Venise à secourir la Reine de H. ... de la Maison de Bourbon ./." (355 letters
  after the expansions G.nal general, Rep.e republique, H. hongrie, P.ce princesse, and the line-break dittography "la / la" kept
  once, all fixed before scoring, grade I).
- **Crops** (05:22-05:23 UTC): `python3 tools/iiif_lines.py --ark btv1b525174513 --canvas 511 --region 650,4650,3050,1200 --out
  ciphers/naf14913-rousseau-venice-1743/images --prefix f249r --debug` (5 lines, 10 crops); `... --canvas 512 --region
  1450,1800,2950,900 ... --prefix f249v` (4 lines, 8 crops); `... --canvas 513 --region 380,600,2150,2650 ... --prefix f250r`
  (12 crops); `... --canvas 514 --region 2350,520,2000,480 ... --prefix f250v` (2 crops).
- **Transcription.** Numerals: pass A (worker, debug overlays) + pass B (one blind Opus subagent, 18 crops) agree on 108/111.
  One dispute was reconciled on a cut strip (`images/recon_strip3.jpg`, vision call 3): f.249r L03 253|255 is read as 253, because
  it repeats L01's 253 and has the same flat-top final digit. Two disputes are left as a|b (33|35, 833|835); neither is a C code
  nor a repeat. Slip: pass A (worker, 1000 px views) + pass B (one blind Opus subagent, 14 crops) agree word for word.
- **Pre-registration.** The transcriptions and `align/pooled_gate3.py` were committed and pushed (ae64c98d) before any score.
  The docstring lists the six changes needed to go from two pairs to three: "shared" = in at least 2 of 3 passages; ties span
  every passage; branch-and-bound search in place of subset enumeration, with timeouts counted high for controls; control (a)
  permutes pairs 2 and 3; control (b) shuffles all three; pair 3 at maxlen 12. It also adds **control (c)**, reported beside
  the gate and not gated: pair 3's slip is replaced by words drawn from the other two slips, with pair 3 unpinned in both the
  real and the control runs, so that the control can score.
- **Per-pair FT4b gate** (`align/gate_f249.out`, `gate_pair.py --cipher ../ciphertext_f249.txt --slip ../slip_f250.txt --n 200
  --limit 5`). There are 13 occurrences of the C codes (22 x5, 66 x3, 279, 722, 31, 628, 172), so this is a test. **Real H = 0**, with every
  pin set timed out or infeasible. I stopped the run after the REAL line, before the controls (an H of 0 cannot beat any
  control).
- **Why H = 0: the pair as transcribed has no fit under the model at all** (`align/f249_diag.py` -> `align/f249_diag.out`,
  a diagnostic run after the gate, not a gate). No exact-coverage segmentation of the slip exists with every repeated code
  consistent, **even with no pins** (proved False, not a timeout). Making a single repeated code's occurrences distinct
  restores a fit for exactly three codes: **253** (the reconciled group, f.249r L01/L03), **242** (f.249r L03 / f.249v L03) and
  **66** (f.249r L03, L05 and f.249v L01, the group both passes read as "66" through a b/6-like form). 14 other codes stay False, and 10/52/276
  time out at 40 s. So the most likely causes are one misread digit in one of those three codes, or a decipherer's
  departure from the cipher in the stretch they cover. This is a property of the transcription and slip, not evidence about the f.206 key.
- **Pooled three-pair gate as registered** (`align/pooled_gate3.out`, `python3 align/pooled_gate3.py`, n 100, limit 5, seed 7):
  29 shared non-C codes, 92 occurrences. **Real Hp = 0** (pair 3 cannot be segmented, see above). Control (a): p95 70, but all 100 runs
  timed out and were counted high. Control (b): every run scored 0, p95 0. **GATE FAIL by the registered rule (Hp 0 is not above 70)**.
  The FAIL is a **non-test of the key**, because the real statistic is 0 by construction once pair 3 has no consistent
  segmentation. Control (c), the wrong-slip decoys: **real-(c) Hc = 0** (unpinned and still infeasible); decoys p95 90, but all 100 timed out
  and were counted high. So (c) can vary (decoys reached the bound without being refuted, while the real slip is refuted
  outright), but at a 5 s limit it measures nothing either way. Recorded as a non-test.
- **Side finding, from forced-check lines in the registered output.** Under the ten f.206 pins, **208 has 0 joint chunks** across the three
  passages. On f.249r, "qu'il se fût" is cipher 172 208 ..., and with 172 pinned to "quils" (f.206 "et qu'ils auroient") 208 is forced to "e"
  here, against its FT4d C value "se" (f.206 "princes|se", f.216v "de se tenir"). One explanation is that 172 stands for *qu'il*, and that the
  plural s on f.206 is the decipherer's own inflection, or is carried by the next group. This is an inference (I), not tested. It means 172's C grade
  rests on f.206 alone and conflicts with f.249's slip. Forced elsewhere, at grade M only (no PASS): 10 a, 121 s, 338 t, 347 con, 599 bon,
  781 e.
- **Key and decode.** No PASS, so nothing enters or moves in key.tsv (registered key rule). `python3 tools/decode_key.py
  ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0 (H 0, C 23, S 0, M 39, I 0,
  U 0, unchanged).
- Requests: gallica.bnf.fr 9 (1 overview 249r at 1000 px, 4 info.json, 4 region fetches; 1.6 s+ apart, all HTTP 200).
  Vision: 2 blind Opus subagent calls (numerals, slip) + 1 reconciliation view (3 of 3), plus worker views of the four
  1000 px pages and two debug overlays.

Not found in: no print or phrase search was run this step. Rule 10: no novelty class here.

## FT4g-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4e's Verdict): native-resolution eye check of the f.249 groups 253, 242 and 66 at every occurrence, then
`align/gate_pair.py` and `align/pooled_gate3.py` re-run unchanged.

- **Crops** (06:00-06:02 UTC, cut from the native region files FT4e already fetched, no new request). Group pieces first:
  `python3 tools/iiif_lines.py --image src_ark_12148_btv1b525174513_f511_650_4650_3050_1200.jpg --out eye249 --prefix f249r --groups 20 --debug`
  (and the same with `..._f512_1450_1800_2950_900.jpg --prefix f249v`). The pieces split groups, so they served only to locate the groups on the
  debug overlays; the piece crops were deleted. One crop per group:
  `python3 tools/iiif_lines.py --image <src> --out eye249 --prefix cNN --region x,y,w,h --centres <h/2> --top-margin 70 --bottom-margin 70`.
  There are 12 crops (`images/eye249/c01-c12_L01.jpg`; boxes in `images/eye249/crop_key.tsv`), named neutrally so the readers stay blind. Seven
  target occurrences: 253 at f.249r L01 and L03; 242 at r L03 and v L03; 66 at r L03, r L05 and v L01. Five decoys of known form: 755, 605, 63, 65, 33|35.
- **Reads** (`images/eye249/READS.tsv`). Two blind Opus subagent passes saw only the crops, with no transcription; one Opus reconciliation
  worked on a labelled strip (`images/eye249/recon_c03_strip.jpg`). Both passes agree on 6 of the 7 target occurrences: 253 (r L01, high), 242 x2,
  66 x3 (v L01's looped "bb" form read as 66 by both). They split on one, r L03 "253": pass A 253 (alt 255), pass B 255 (alt 253), the same
  dispute FT4e had. The reconciliation reads the last digit as **3**, at medium. This is a flat-topped 3 with an entry tick and a mid cusp, not the
  plain diagonal 5 of the same group's middle digit or of 755. The same flat-top 3 form is the reconciler's reading of decoy 605 -> 603 and of 33|35 -> 33,
  but both blind passes read 605, so the decoy is left unchanged. **Result: every occurrence of 253, 242 and 66 is confirmed as transcribed.** No
  transcription change. The pre-registration was pushed before any score (`align/PREREG-FT4g.md`, commit 06dd399a).
- **Gates, re-run unchanged.** `gate_pair.py --cipher ../ciphertext_f249.txt --slip ../slip_f250.txt --n 200 --limit 5`
  (`align/gate_f249_FT4g.out`): **REAL H = 0**, and this time "timeouts on higher pin sets: False". Every pin set was refuted, not timed out.
  I stopped the run after the REAL line, as FT4e did. `pooled_gate3.py` (n 100, limit 5, seed 7; `align/pooled_gate3_FT4g.out`): **line for line
  identical to FT4e**. Hp 0; control (a) p95 70 (100/100 timed out, counted high); control (b) p95 0; **GATE FAIL by rule**. Hc 0 against
  decoy p95 90 (all timed out). The exit line was not captured; FT4e's was exit 1. Both results are still **non-tests of the key**, because the
  pair as transcribed has no repetition-consistent fit.
- **What this rules out.** It rules out the explanation that the infeasibility comes from a misread of 253, 242 or 66 (6 of 7 occurrences agreed blind, the 7th
  reconciled at medium). What remains (I, untested): the decipherer departed from the cipher in the stretch those codes cover; the slip
  does not cover exactly the numeral passage (a word dropped or added at an end or in the middle); or one of those codes is genuinely
  polyvalent in this key. Rule 3 third-attempt clause: the f.249 pair has now been scored twice by the same strict repetition-consistency instrument
  on a confirmed transcription. That instrument is **retired** for this pair. Only a different instrument (an alignment that allows one
  polyvalent code or one slip edit, with a control that can differ) or new material reopens it.
- Grades: no reading changed. `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> see Checks (FT4g) below.
- Requests: gallica.bnf.fr 0 (local native region files from FT4e). Vision: 3 of 3 (2 blind passes + 1 reconciliation), all Opus 5.5.

Not found in: no print or phrase search was run this step. Rule 10: no novelty class here.

## FT4h-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step 1 (FT4g's Verdict): native view of f.273r and f.274r for the f.274 slip's cipher passage.
- Canvases from `python3 tools/gallica_folio.py btv1b525174513 --folio 273` / `--folio 274`: 273r = f559, 273v = f560, 274r = f561,
  274v = f562 (labels; the volume's offset changes at f595, so labels, not the formula). 273r fetched at 1000 px (`images/lowres/v559_273r_1000.jpg`);
  273v/274r/274v re-read from FT4b's 1000 px files.
- Native regions: `python3 tools/iiif_lines.py --ark btv1b525174513 --canvas 561 --region 450,1700,3100,4250 --out ciphers/naf14913-rousseau-venice-1743/images/ft4h --prefix f274r --debug`
  (18 lines) and `... --canvas 559 --region 250,1150,3200,5400 ... --prefix f273r --debug` (13 lines). The worker read the debug overlays.
- **What is there.** Ff.273r-274r are one complete clear letter, Lorenzi to Montaigu, "A Florence le 8e Aoust 1744" (red number 2078, "M. le Comte de
  Montaigu" at the foot of 273r). It runs 273r -> 273v -> 274r without a break: 273v ends "...que ces batimens, aussi bien" and 274r opens "que ceux que le
  Commandant du detachement de l'escadre Angloise fait fretter a Civita Vecchia ...". It is signed "Lorenzi" on 274r. 274v is blank (show-through only).
  There are **no numeral groups** on any of the four pages: none in the text, none interlinear, none in the margins. There is **no pasted slip** on 273r or 274r,
  and the text on both is in the letter's own secretary hand, not the slip hand of ff.206r/214r/217r/250. Group count: 0. Clear copy: the whole letter is clear.
- So the finding aid's "f.274" has no cipher+slip pair on ff.273-274 as they are now bound. Untested possibilities (I): the slip was detached or moved;
  the finding aid's folio is off; or Rousseau's "decipherment" here means the clear text of 273r-274r itself, i.e. a fully ciphered letter whose clear
  copy replaced it (the hand is not the slip hand, so this is the weakest of the three). Not looked for this step: leaves outside 273r-275r.

Step 2 (Verdict's second step, run because step 1 ended well under 40 pct of cap): f.213r-v <-> f.214r transcription + gate_pair.py.
- Pre-registration `align/PREREG-FT4h.md` (commit b977f153) was pushed before any transcription or score. It sets FT4b's gate unchanged, MAXLEN 12, n 200,
  limit 20, seed 1.
- The passage starts on **f.213r**, not 213v. It follows the clear words "...plus puissante en Italie", runs 5 numeral lines on 213r and 3 on 213v, and
  ends before "Le passage en France du fils aine de Mr le Chevalier de St George". That gives **84 groups** (FT4b's 213v-only estimate was about 30).
  Crops: `... --canvas 439 --region 1100,3330,3050,1300 ... --prefix f213r`, `... --canvas 440 --region 650,650,3500,800 ... --prefix f213v`,
  `... --canvas 441 --region 200,2300,2500,2050 ... --prefix f214r` (all `--debug`, `images/ft4h/`).
- Reads: pass A was the worker's own read (`align/ft4h_passA.txt`); pass B was one blind Opus subagent on the crops only (`align/ft4h_passB.txt`). They agree on
  **83 of 84** first readings. The one split, 213v L01 g11 270|210, was reconciled to **270** from the crop. Kept a|b: 835|833, 573|513, 713|113. The 213r "2"
  is underlined in the MS. -> `ciphertext_f213.txt`.
- Slip f.214r ("M. Lorenzi. du 1er fevrier 1744", 9 lines, read by the worker) -> `slip_f214r.txt`, 262 letters. Expansions at grade I: 2 -> deux,
  Rep.e -> Republique, R. -> Roi, Sard.e -> Sardaigne.
- **Gate** (`align/gate_f213_FT4h.out`): the passage carries **6 occurrences** of the ten C codes (22 x3, 722 x2, 501 x1). That is at least 5, so this is not
  a non-test on the power floor. Result: **REAL H = 0, "timeouts on higher pin sets: False"**. The run was stopped after the REAL line, as FT4e and FT4g did,
  because no control can change a gate that H = 0 already fails.
- **Diagnostic** (`align/f213_diag.py`, a copy of f249_diag.py, not a gate; `align/f213_diag.out`): with the three pins the pair is not consistent (proved False).
  With **no pins** it is also not consistent (proved False). Each of 10 repeated codes made distinct one at a time still gives False. 8 others (52, 121, 306, 317,
  605, 689, 746, 835) time out at 40 s. So this pair, like f.249/f.250, has **no repetition-consistent exact-coverage fit as transcribed**. The H = 0 says
  nothing about the f.206 key: it is a **non-test of the key**, not a FAIL (rule 3: the instrument cannot fit the pair at all).
- Reading: 2 of the 3 new pairs (f.249, f.213) are infeasible under the strict model, while f.216v fits. Since the f.213 transcription agrees 83/84 blind,
  the model's assumptions are now the likelier fault than the reads (I, untested). Candidate faults: the slip's abbreviations and expansions (Roi/Sardaigne/
  Republique/deux may be coded otherwise, e.g. as single nomenclator groups for the abbreviated form, which exact coverage allows only if the expansion
  letters match); a slip that paraphrases or drops a word; or polyvalent codes. This is the first scoring of this pair, so the third-attempt clause does not apply.
- Grades: no reading changed; key.tsv untouched. Requests: gallica.bnf.fr 7 (2 x 1000 px: 273r, 213r; 5 iiif_lines native region fetches: 274r, 273r, 213r, 213v, 214r), >= 1.5 s apart, all HTTP 200.
  Vision: 1 subagent call (Opus 5.5) + the worker's own reads.

Not found in: no print or phrase search was run this step. Rule 10: no novelty class here.

## FT4i-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4h's Verdict): one-edit alignment on both infeasible pairs (f.213r-v/f.214r and f.249r-v/f.250r-v). This is a different
instrument from the retired strict-consistency one: exactly one edit is allowed per pair, either W (one group occurrence released, 0-12
letters: a misread digit, one polyvalent use, or an extra group at length 0) or D (one dropped group inserted, 1-12 letters). Free groups
take 1-12 letters, every repeated code takes one identical chunk, and there are no pins. Solver: an exact CP-SAT model (ortools 9.15,
installed in the container for this step), `align/one_edit.py`.
- **Pre-registration** `align/PREREG-FT4i.md` + `align/one_edit.py`, commit 6d373a56, pushed before any one-edit score. Solver sanity
  before the gate: E0 (no edit) is f216v True (2.1 s), f213 False (0.3 s), f249 False (4.2 s), which reproduces FT4c and the two
  FT4e/FT4h diagnostics. Gate: PASS if E_real = 1 AND each control (s: slip words shuffled; g: group order shuffled; n 40, 15 s per draw,
  timeouts counted E = 1) has an E=1 share <= 0.05. E_real = 1 with a share above that is NON-INFORMATIVE.
- **f.213/f.214r** (`align/one_edit_f213.out`, 07:02-07:07 UTC): E0 False; **E_real = 1 (proved fit, 27 s)**. Exactly **1 of 169**
  single edits gives a fit: **W at group 73 = the second occurrence of 368** (f.213v L02 "10 368 426", against f.213r L06 "468 368 46").
  Every other position is proved infeasible (0 timeouts). Control (s): 3/40 E=1, all 3 of them timeouts counted high, and 0 of 37 resolved
  draws fit. Control (g): 35/40 timeouts counted high, and 0 of 5 resolved draws fit. **GATE NON-INFORMATIVE by the registered rule** (shares 0.075, 0.875).
  Descriptively, no resolved control draw fits with one edit (0/42). The gate fails only because the controls time out, so this is a power limit
  at 15 s, not a fit that controls also reach.
- **f.249/f.250** (`align/one_edit_f249.out`, 07:07-07:17 UTC): E0 False; **E_real = 1 (proved fit, 35 s)**. **9 of 223** single edits
  give a fit, and all of them sit on FT4e's three suspect codes or next to them: W at group 2 (253, f.249r L01), 25 (242), 26 (253), 27 (66),
  28 (52), 95 (242, f.249v L03), and D before group 26, 27 or 28. 0 timeouts. So the fault is local to the f.249r L03 stretch "121 242 253
  66 52 605" or to a 253/242 repeat. Control (s): 40/40 timed out (counted high), 0 resolved. Control (g): not scored, because my
  590 s outer timeout cut the run off (exit 124; noted in the .out). **GATE NON-INFORMATIVE by the registered rule** (share 1.000).
- **What this shows.** Both pairs fit once a single edit is allowed. On f.213 the edit is pinned to one group (the second 368). On f.249 it
  is confined to one 4-group stretch or its two repeated codes. Whether wrong pairings fit just as often with one edit is **untested**:
  the controls time out at 15 s. The gate is therefore a non-test, not a negative and not a pass. Rule 3: this is the first attempt with this
  instrument on these pairs, so it is not retired. The named next step is the same controls with a longer limit (power), not a changed edit model.
- Key and grades: no change (registered key rule). `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens
  62: C 23, M 39 / reading up to date", exit 0 (H 0, C 23, S 0, M 39, I 0, U 0).
- Requests: none (disk only; pip fetched ortools from PyPI for the solver). Vision calls: 0. Subagents: 0.

Not found in: no print or phrase search was run this step. Rule 10: no novelty class here.

## FT4j-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Steps run (FT4i's Verdict): (1) a 1000 px sweep of ff.270-280 for the displaced f.274 pair; (2) FT4i's registered one-edit gates re-run with
the control draws at 60 s instead of 15 s (amendment in `align/PREREG-FT4i.md`, commit e27ad9dc, pushed before the re-run; timeout only).
- **(1) Sweep.** Canvases from `tools/gallica_folio.py btv1b525174513` (f15-f592 = 1r..289v, k = 14): 553-574 = 270r-280v; 17 new pages at
  1000 px (559-563 re-used from FT4b/FT4h), contact sheet `images/lowres/sheet_270_280.jpg`, one vision read. What is there: a run of clear
  Lorenzi-to-Montaigu letters from Florence, each opening with a red register number, ending "Lorenzi", with "M. le Comte de Montaigu" at the
  foot: 270r (25 July 1744) -> 271r; 272r (1 Aug) -> 272v; 273r-274r (8 Aug, FT4h); 275r (15 Aug) -> 276v; 277r (22 Aug) -> 278v; 279r
  (29 Aug) -> 280r (dates read at thumbnail size). Blank or show-through only: 271v, 274v, 280v. **No numeral groups, no pasted slip and no
  interlinear text on any of the 22 pages**; no page shows a block of figures. The f.274 pair is not on ff.270-280 as bound.
- **(2) f.213/f.214r** (`align/one_edit_f213_60s.out`, 07:32-07:44 UTC): real E0 False, E 1 (40 s), 1 of 169 single edits fits (W at group 73,
  the second 368), identical to FT4i. Control (s): 0/40 E=1, **all 40 resolved** (3 timeouts at 15 s). Control (g): 16/40 E=1, **all 16 are
  timeouts counted high; 0 of 24 resolved draws fit** (35 timeouts and 0 of 5 at 15 s). The control's p95 of E among resolved draws is 0
  (s 0/40, g 0/24), against the real E = 1. Registered shares 0.000 and 0.400 -> **GATE NON-INFORMATIVE by the registered rule** (g > 0.05).
  Resolved control draws rose from 42 to 64 of 80 at 4x the time.
- **(2) f.249/f.250** (`align/one_edit_f249_60s.out`, 07:44-~08:04 UTC): real E0 False, E 1 (74 s), the same 9 of 223 single edits as FT4i.
  Control (s): 37/40 E=1, all 37 timeouts counted high, **0 of 3 resolved draws fit** (0 resolved at 15 s). Control (g): **not scored**: the
  session harness's background time limit killed the run (my wrapper, started 07:34), and a re-run would have crossed 80 pct of the box.
  **GATE NON-INFORMATIVE** (share 0.925, g missing).
- **What this shows.** Across both pairs, 0 of 67 resolved control draws fit with one edit, while both real pairs do fit. But under the
  registered rule (timeouts count as E = 1) neither gate can pass until the shuffled controls resolve. Rule 3: this is the second run of the same
  instrument, changing only the time limit. The numbers moved toward resolution (f213 resolved draws 42 -> 64; f249 0 -> 3), so the instrument
  is not retired. A third time-only increase is not the next step, though: f249's (s) draws stay almost wholly unresolved at 60 s. The next step
  is (g) for f249 in its own box, then a pre-registered amendment that changes how draws are solved (multi-worker draws) or a resolved-only
  statistic with its own stated power.
- Key and grades: no change (registered key rule); `decode_key --check` is in the Checks line below. Requests: gallica.bnf.fr 17 (1000 px
  images, >= 1.5 s apart, all HTTP 200); PyPI (ortools, pillow, fresh container). Vision calls: 1 (contact sheet). Subagents: 0.

Not found in: ff.270-280 (f.274 pair). No print or phrase search was run this step. Rule 10: no novelty class here.

## FT4k-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4j's Verdict, first item): f.249/f.250 control (g) only, under `align/PREREG-FT4i.md` as amended (FT4j, e27ad9dc: 60 s per
draw; nothing else changed). `align/ctrl_g_only.py` imports `one_edit.py` unchanged and rebuilds the registered draws exactly
(random.Random(3) consumes the 40 (s) word shuffles first, then the 40 (g) group shuffles, as `one_edit.main()` does); draws run
single-worker under Pool(4), as registered. Foreground, two halves with a push after the first (15384644): draws 0-19 08:27-08:33 UTC
(`align/ctrl_g_f249_60s_h1.out`, 355 s), draws 20-39 08:33-08:39 UTC (`align/ctrl_g_f249_60s_h2.out`, 315 s); pooled
`align/ctrl_g_f249_60s_pooled.out`.
- **Control (g), n 40:** E=1 in 28 (0.700), all 28 are timeouts counted high; **0 of 12 resolved draws fit** (half 1: 15 timeouts, 0/5;
  half 2: 13 timeouts, 0/7). With FT4j's (s) (37 of 40 timeouts, 0 of 3 resolved fit), the f.249 gate is complete: E_real = 1, shares
  s 0.925 and g 0.700 -> **GATE NON-INFORMATIVE by the registered rule** (> 0.05).
- **Both pairs together at 60 s:** 0 of 79 resolved control draws fit with one edit (f213 s 0/40, g 0/24; f249 s 0/3, g 0/12), against
  E_real = 1 on both real pairs; but 81 of 160 draws are unresolved and the registered rule counts them as fits. Descriptive only; no pass.
- Rule 3: the 60 s amendment is the second time-only setting of this instrument; resolved draws rose (f249 g 12 resolved where FT4i
  resolved none), so the instrument is not retired, but a third time-only increase is not the next step (FT4j): the next step is a
  pre-registered amendment that changes how draws are solved or scored. Not written here (outside this step's brief).
- Key and grades: no change (registered key rule). Requests: PyPI only (ortools in a fresh container). Vision calls 0. Subagents 0.

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4l-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4k's Verdict): a pre-registered amendment for the unresolved control draws, changing how a draw is solved (third instrument on
these gates). Amendment FT4l in `align/PREREG-FT4i.md` + `align/one_edit_seg.py`, commit 75bf2422, pushed 09:30 UTC before any registered
draw was re-scored. Same statistic E, same seed-3 draws, same gate (unresolved counted E = 1); the solver is (i) an equivalent smaller
CP-SAT model (variables only for repeated-code occurrences, each run of free groups one gap constraint) and (ii) E by decomposition, one
exact subproblem per edit class (10 s each, Pool(4), early exit on a fit). Validation before the push: f216v E = 1; f213 real E = 1 with
exactly 1 of 107 edit classes fitting, W at group 73 (the second 368), as FT4i/FT4j (`align/real_f213_dec_classes.out`). Sizing on
unregistered seed-99 f249 draws only: two draws that time out at 60 s under one_edit.py resolved (0 fits, 90-131 s).
- **f.213/f.214r control (g), n 40** (`align/ctrl_g_f213_dec_q1.out`, `_q2.out`, `_h2.out`, `_h2b.out`, pooled `_pooled.out`; 09:30-09:55
  UTC, foreground, push dee4b9c8 after draws 0-19): **E=1 in 0 of 40, 0 unresolved** (3-116 s per draw). With FT4j's (s) 0 of 40 (all
  resolved): E_real = 1, shares s 0.000 and g 0.000 -> **GATE PASS** by the registered rule (<= 0.05). Matched control beside it: 0 of 80
  wrong pairings (shuffled slip words or shuffled group order) fit with one edit, while the real pair fits with exactly one, at one place.
- **What the PASS licenses.** The f.213 groups and the f.214r slip are the same passage up to one edit, and the one edit that works is the
  second 368 (f.213v L02 "10 368 426"): a misread digit, a polyvalent use of 368, or an extra group there. It does not license a key change
  (registered key rule: nothing moves in key.tsv) and it does not say which of the three the edit is; that is the image check.
- **f.249/f.250: not scored** (box). Its controls under this solver are 80 draws at roughly 0.5-2 min each.
- Rule 3: this is the third instrument; it resolved every draw it touched, so the "retire" branch did not arise.
- Key and grades: no change. Requests: PyPI (ortools, fresh container) only. Vision calls 0. Subagents 0.

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4m-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4l's Verdict): eye check of f.213v L02 group 73 (the second 368), the one edit that lets the f.213/f.214r pair fit.
- **Pre-registration** `align/PREREG-FT4m.md` + `align/eye73_variants.py`/`.out`, commit a9fb0bb8, pushed before any look. Pre-image
  deduction (one_edit_seg.solve unchanged, 60 s, all resolved): every single-digit variant of 368 (27) and every two-digit drop (36, 38, 68)
  gives **E0 False**; deleting group 73 gives **E0 True**. So the fit needs group 73 to carry **zero letters** of the slip: a misread digit
  and a polyvalent use of 368 (both carry >= 1 letter) are excluded by the model at MAXLEN 12, and the explanation left is an extra group.
- Crops: `python3 tools/iiif_lines.py --image ciphers/naf14913-rousseau-venice-1743/images/ft4h/src_ark_12148_btv1b525174513_f440_650_650_3500_800.jpg --out ciphers/naf14913-rousseau-venice-1743/images/ft4m --prefix f213v --debug`
  (3 lines) and the same for `..._f439_1100_3330_3050_1300.jpg --prefix f213r` (6 lines), from the native regions already on disk (FT4h; no
  Gallica request). From these regions, 5 single-group crops `images/ft4m/eye_1..5.jpg` (target + decoys 426, 689 on the same line, and the
  first 368 and 468 on f.213r L06), shuffled before the read; identities in `align/eye73_mask.tsv`.
- **Blind read** (1 Opus 5.5 subagent call, masked crops only; `align/eye73_read.tsv`): target **368, high confidence, marks none**; the
  first 368 also 368 high, none; decoys 689 (medium), and 426 / 468 read as 42 / 59 because those two crops clip a digit at the edge
  (a crop fault, not a reading conflict). Reader: "Different in kind: none ... no strike-through, overwriting, dots under, erasure or unusual spacing."
- **Outcome R2 (pre-registered):** the group is written plainly as 368, with no cancel or correction mark. The transcription stands, and so does
  the key. With the deduction above, the f.213/f.214r pair is the slip's text up to **one unmarked extra group, 368 at f.213v L02**. That is an
  encipherer's slip (an extra or null group) at grade I. Misread is not supported (read + E0 False for every variant). Polyvalent use is excluded
  by the model. Not tested: a slip that drops words the cipher carries at that point (the slip as a paraphrase), which the one-edit model also
  counts as "zero letters" for this group.
- Key and grades: no change. `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading
  up to date", exit 0. Requests: none to gallica.bnf.fr (native regions on disk); PyPI (numpy, pillow, scipy, ortools; fresh container).
  Vision: 1 subagent call (Opus 5.5); the worker viewed two reduced band images only to place the crop boxes.

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4n-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4m's Verdict, both halves; order swapped so the box cut would land on the long half). Pre-registration
`align/PREREG-FT4n.md` + the `--pair3/--drop` amendment to `align/pooled_gate3.py`, commit 4b43952c, pushed 10:32 UTC before any score.
- **A. Pooled key gate, f.213/f.214r as pair 3 with group 73 dropped** (`python3 align/pooled_gate3.py --pair3 f213 --drop 73`,
  n 100, limit 5, seed 7; `align/pooled_gate3_f213drop73.out`, 10:32-10:40 UTC): 27 shared non-C codes, 91 occurrences.
  **REAL Hp = 0 (search timed out at 75 s, nothing fully checked)**; control (a) mean 58.27, p95 67 (all 100 timed out, counted
  high); control (b) 0 for every shuffle (cannot vary: the pins fit only the real order, as FT4d/FT4e, stated in the PREREG);
  (c) reported only: Hc real 0 (timed out) vs decoy p95 87. **GATE FAIL** by the registered rule; nothing moves in key.tsv.
- **A, post-hoc diagnostic (not part of the gate; `align/ft4n_diag.py`, `align/ft4n_diag.out`):** the real 0 is not only a
  timeout. Each passage alone with the pins: f.206 and f.216v consistent; **f.213 with group 73 dropped is proved
  inconsistent** with its three pins (22 de, 501 et, 722 ti), in 1.5 s. Pin subsets: no pins, 22, 501, or 22+501 fit; **any set
  containing 722 = ti fails**. With all three pins, no single dropped group of the full 84 fits (84 runs, 15 s each, 0 fits,
  0 timeouts). Both 722s stand in "90 689 24 722" = garanti (garanti-ssoit, garanti-s par la), where ti is the slip's own
  letters, so the conflict comes from what ti forces elsewhere in the passage, not at 722 itself; not located this step.
  Reading: FT4m's "one unmarked extra group" holds for the UNPINNED one-edit model only; the f.206 key (722 ti) does not fit
  f.213 with that one edit, nor with any other single drop.
- **B. f.249/f.250 one-edit controls under the FT4l solver** (`one_edit_seg.py --dec`, seed 3, n 40, sublimit 10 s):
  real **E = 1** (27 s, `align/real_f249_dec.out`); **(s) draws 0-9: E = 1 in 0 of 10, all resolved** (13.7-116 s, about 90 s a
  draw; `align/ctrl_s_f249_dec_b1.out`, `_b2.out`); (s) draws 10-39 and all 40 (g) draws not run. Per the FT4l rule this
  pair is **not scored** (10 of 80 draws), not a partial gate. Stopped at 10:58 UTC: the session's rate-limit window read
  allowed_warning, and the full 80 draws need about 2 hours at this rate, an own box of ~2.2 h or four 45-min boxes.
- Key and grades: no change (`decode_key.py --check` exit 0). Vision 0, subagents 0, network: PyPI (ortools) only.

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4o-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4n's Verdict): locate what the f.206 pin 722 = ti forces in f.213. Pre-registration `align/PREREG-FT4o.md` + `align/ft4o_scan.py` (its "~11:15 UTC" was estimated, not read; the clock read 11:14 after the scans, so the push order is the record),
commit 3e896b2e, pushed before any scan. Model: `gate_pair.Scorer.consistent` (exact coverage of the f.214r slip, MAXLEN 12), pins 22 de /
501 et / 722 ti, group 73 dropped (edit 1, FT4m); edit 2 for each remaining group i: D (drop) or R (release to a unique free code), 6 s a run.
- **Known-answer control** (`align/ft4o_control.out`, seed 1, n 3): f.206 (fits all ten pins) with one injected overwrite; the scan put the
  injected index in its FIT set **3 of 3** (set sizes 1, 1, 3). The scan is a locator at f.206's length, so the f.213 result is read.
- **f.213** (`align/ft4o_f213_a.out`, `_b.out`; 166 runs, 5 timeouts = 3%, all at idx 7/10/11/34, none at 722): base NOFIT (as FT4n).
  **FIT set 13 indices** (post-drop idx; original = idx+1 from 73): R or D at 3 (63), 48 (444), 49 (664), 50 (63), 51 (306), 58 (664),
  69 (444); D only at 70-75 (329 207 10 426 90 689, the stretch just before the second 722 at idx 77). **Releasing either 722 (idx 18, 77)
  does not fit.**
- **Outcome O3 (pre-registered): FIT set > 5, location not identified by this model.** O1 (the conflict sits at 722 itself) is excluded:
  neither 722 occurrence released gives a fit, so the pin is not contradicted at its own groups. Post hoc, not registered: the fits cluster on
  the three codes that occur twice in f.213 (63, 444, 664: releasing either occurrence of any of them fits) and on drops in the stretch
  70-75. Read: pinning 722 = ti fixes the two "garanti" positions and leaves 63/444/664 no single chunk shared by both occurrences; whether a
  misread among those six groups is the cause is an image question.
- Key and grades: no change. Vision 0, subagents 0, network none (ortools not needed).

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4p-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Steps run (FT4o's Verdict, both items): (1) a 300 px thumbnail sweep for the displaced f.274 slip; (2) a blind eye check of the six f.213 groups
using codes 63/444/664.
- **(1) Sweep.** Canvases by the FT4j mapping (f15-f592 = 1r..289v): 533-552 = ff.260r-269v and 575-592 = ff.281r-289v, 38 pages at 300 px
  (`images/lowres/s300/`), one contact sheet `images/lowres/sheet_260_289.jpg`, read by the worker (one vision read). Gallica budget (40) did
  not cover ff.251v-259v (16 pages, canvases 516-532): **not swept**. What is there: clear Lorenzi-to-Montaigu letters from Florence (264r
  and 268r dated July 1744, 281r-289r Aug 1744-Jan 1745; the 289r date was read at thumbnail size), each signed "Lorenzi"; no numerals on
  any page except one. **f.266r carries a block of about 15 lines of numeral groups** inside a clear letter ("...se flatter de faire jouir
  les ports de Toscane..." then "Un de mes amis ordinairement bien informé me mande que" + groups + "...arrangemens sont aussi fondés que..."),
  and **f.265r is a small pasted slip in another hand** (clear French: "Les Regt.s ... les Esp(agn)ols ... les Gardes ... Bresse/Bresce ...
  plan d'armée ... Général"), with its own stamped folio **265** (native region read, 1 request); 265v blank. This is a slip + cipher passage
  laid out like the other four pairs (slip facing or next to the numerals). Whether it is the finding aid's "f.274" (folio off by 9) or a sixth
  slip the aid does not list is not settled here (I). Its text was not transcribed and the slip has not been matched to the groups.
- **(2) Eye check.** Pre-registration `align/PREREG-FT4p.md`, commit 48ba66a1, pushed before the read. Crops: `python3 tools/iiif_lines.py
  --image ciphers/naf14913-rousseau-venice-1743/images/ft4h/src_ark_12148_btv1b525174513_f439_1100_3330_3050_1300.jpg --out
  ciphers/naf14913-rousseau-venice-1743/images/ft4p --prefix f213r --debug` (6 lines) and the same for `..._f440_650_650_3500_800.jpg --prefix
  f213v` (3 lines); from those native regions 12 single-group crops `images/ft4p/eye_01..12.jpg` (6 targets, 6 decoys on the same lines;
  three decoy boxes widened before the read because they clipped a digit), shuffled (seed 4013), identities `align/eye_ft4p_mask.tsv`.
  One blind Opus 5.5 subagent read (`align/eye_ft4p_read.tsv`).
  - Control: **decoys 6 of 6 read as transcribed** (268, 306, 834, 746 high; 329, 347 medium) -> gate met (>= 5 of 6).
  - Targets: **all six read as transcribed at high confidence, no marks**: 63 (L02r), 444 / 664 / 63 (L06r), 664 (L01v), 444 (L02v).
  - **Outcome P1 (pre-registered):** the transcription stands; the f.206 pin 722 = ti does not fit f.213 (FT4n) and that conflict is **not a
    misread among the six 63/444/664 groups**. Logged as a key conflict per rule 4: 722 = ti rests on f.206 alone; f.213 (minus the unmarked
    extra 368) needs something else at one of FT4o's 13 locations. No file change; key.tsv untouched. Per P1 the next instrument is different
    (722 polyvalence tested against f.216v/f.249, or a slip-as-paraphrase alignment), not another eye check of these groups.
- Key and grades: no change. `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` in the Checks line. Requests:
  gallica.bnf.fr 40 (38 x 300 px pages + 2 native regions of 265r/266r corners), >= 1.6 s apart, all HTTP 200; PyPI (pillow, numpy, scipy).
  Vision: 1 subagent call (Opus 5.5) + the worker's own contact-sheet read; the worker also viewed reduced bands only to place crop boxes.

Not found in: ff.260-269 and 281-289 (no numerals except f.266r; no slip except f.265r). Not searched: ff.251v-259v. Rule 10: no novelty class here.

## FT4q-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Steps run (FT4p's Verdict, both items): (1) the 722 polyvalence test; (2) transcription of the fifth pair, slip f.265r / numerals f.266r.
- **(1) Pre-registration** `align/PREREG-FT4q.md` + `align/ft4q_poly.py`, commit f5d2e22c, pushed before any run. f.216v carries no 722, so it
  cannot vary on this question: a non-test by construction, not run (stated in the PREREG).
  - **Part 1, f.213** (`align/ft4q_part1.out`; Scorer.consistent, MAXLEN 12, group 73 dropped, pins 22 de / 501 et, 722 tied at both
    occurrences, 65 feasible slip chunks at 20 s, 0 timeouts): **only 722 = "i" fits**; "ti" NOFIT (as FT4n). In both "90 689 24 722" places
    (garant-i-ssoit, garant-i-s) f.213 needs 722 = i where f.206 needs ti (con-ti-nue, veni-ti-ens): the boundary with 24 moves by one letter.
  - **Part 2, f.249** (`align/ft4q_part2.out`; FT4l one-edit model, 722's one occurrence "347 722 476" pinned, sublimit 10 s; control 20 random
    same-length slip chunks, seed 3): **722 = ti: E 1** (14 s); control share **0.800** (16 of 20; 15 unresolved, counted high; of the 5 resolved
    draws 1 fits, "nu") -> s > 0.10: **non-test for ti** by the registered rule. **722 = i: E 1** (27 s); control: 12 of the first 12 draws E 1 (7 resolved fits), run stopped at draw 11 since s >= 12/20 = 0.60 > 0.10 whatever draws 12-19 give -> **non-test for i**.
  - **Outcome: Q3 shape but both controls fail their 0.10 floor, so per the PREREG part 2 is a non-test for both values (f.249 does not constrain the value at 722 at this solver's resolution); part 1 stands as a fact about f.213.** Nothing moves in key.tsv (registered). The data conflict stands as logged by FT4p (rule 4): 722 = ti rests on f.206
    (two occurrences, C); f.213 needs 722 = i at both of its occurrences under the one-unmarked-extra-368 reading; f.249 cannot decide at this
    solver's resolution. Fact for the next step, not scored: f.266r carries one more 722 ("180 722 180", L06).
- **(2) f.265r / f.266r.** Natives fetched once as regions (`tools/iiif_lines.py --ark btv1b525174513 --canvas 545 --region 450,1150,3950,3650
  --out ciphers/naf14913-rousseau-venice-1743/images/ft4q --prefix f266r --debug`, 16 lines, 32 crops; and `--canvas 543 --region
  150,2450,3750,3050 --prefix f265r --debug`, 13 bands, 26 crops; a first f265r region at x 600 clipped the slip's left edge and was refetched).
  - **Numerals f.266r** (`ciphertext_f266r.txt`): two blind Opus 5.5 passes, one call each, crops only (`align/ft4q_passA.txt`, `_passB.txt`):
    **171 groups each, 171/171 first readings agree**; alternatives raised: 35|33|55 (L04, L14), 534|334, 663|553, 636|696, 98|978. Marks both
    passes saw: strokes under 3 and 276 (L07) and 150 (L15), a faint stroke at 311 (L06), a double dot "63..188" (L08). The passage sits between
    the clear words "Un de mes amis ordinairement bien informé me mande que" and "Si ces arrangemens sont aussi fondés que j'ai lieu".
  - **Slip f.265r** (`slip_f265r.txt`): one blind Opus 5.5 read (`align/ft4q_slip265_read.txt`), reconciled by the worker on the debug overlay
    (no fourth vision call). 14 written lines (the cut missed physical line 7, "le Bressan et le Bergamasc. l'on m'a=", read from crop edges and
    the overlay). Text: Venice, having learnt that the Spanish had advanced to Oneglia, resolved to send a considerable corps to the Milanese
    border; learning they had withdrawn, it sent only three regiments to cover the Bresciano and Bergamasco; if the Infante's combined army
    enters Piedmont, the Republic will march more troops and make Brescia a place d'armes for the Provveditore Generale. Uncertain: d'envoier,
    Bergamasc, provediteur; struck words dropped for alignment.
  - Pairing at grade I, not gated: the slip opens "La Republique de Venise", the groups open 52 605 22 739, the same four groups f.213 and f.249
    open "la Republique de (Venise)" with. No key gate run on this pair (brief: next step).
- Images: folder was 29 MB; the 9 native source regions in images/ and the 2 new ones moved to `images/images_manifest_full.tsv` (sha256,
  IIIF URL) + `images/regen_images.sh` (regen of the f514 region tested byte-identical before deletion), f206r_full.png -> .jpg at the same
  dimensions; crops kept. Folder now 28 MB.
- Key and grades: no change. `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` in the Checks line. Requests:
  gallica.bnf.fr 4 (1 regen test + 3 native regions), >= 1.5 s apart, all 200; PyPI (ortools). Vision: 3 subagent calls (Opus 5.5); the worker
  viewed two 300 px thumbnails and the two debug overlays to place regions and reconcile the slip.

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4r-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4q's Verdict): the f.266r/f.265r pair gate with 722 = ti vs 722 = i as the registered question.
- **Pre-registration** `align/PREREG-FT4r.md` + `align/ft4r_pair.py`, commit 8a89e41e, pushed 12:25 UTC before any registered score. Same
  form as the f.213 gate that PASSed (FT4l: one-edit CP-SAT, decomposition per edit class, sublimit 10 s, controls (s)/(g) seed 3 n 40,
  unresolved counted high, PASS iff E_real 1 and both shares <= 0.05), with f.266r's single 722 (group 49, "180 722 180") pinned to 'ti' or
  'i' (the FT4q part-2 pinned model); no other pins. Outcomes O1-O4 for the 722 question were written in the PREREG before the run.
  Sizing before the push, on one UNREGISTERED draw (seed 99, (g), ti): unresolved at 63 s; so the PREREG put the two real scores first
  and the 160 control draws after them, only for a value whose real E resolved to 1.
- **Real scores** (`align/ft4r_real_ti.out`, `align/ft4r_real_i.out`; 171 groups, 493 slip letters): **722 = ti: E unresolved (61.7 s);
  722 = i: E unresolved (145.4 s).** No edit class gave a fit within 10 s, and some classes timed out, so neither run is a proof either way.
  By the registered rule both values are **NOT SCORED**; no control draw was run (the PREREG runs controls only after a real E of 1).
- **What this means for 722:** nothing. None of O1-O4 applies. f.266r/f.265r does not yet bear on the polyvalence question, and the
  pair's slip/cipher match stays at grade I. Rule 3: the PREREG names the next step as a different instrument, not a longer timeout
  (FT4j). This pair is 2x f.213 in groups and 3x in letters, and the solver did not resolve the real pair at the sublimit where f.213 resolved.
- Key and grades: no change. Requests: PyPI (ortools, fresh container) only. Vision calls 0. Subagents 0.

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4s-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4r's Verdict): anchored split of the f.266r/f.265r pair, then 722 = ti vs 722 = i on the segment holding group 49.
Second instrument on this pair (FT4r's whole-pair gate was the first); rule 3's third-attempt clause noted in the PREREG.
- **Pre-registration** `align/PREREG-FT4s.md` + `align/ft4s_seg.py`, commit 2f51d33d, pushed before any registered score (sizing on one
  unregistered seed-99 (g) draw only: resolved in 1.9 s). Anchor rule: cut at an f.206 C code whose group count equals its count as a
  whole slip word; only 501 'et' qualifies (groups 75, 139; words 45, 78). **S1 = groups 0-74 (75 groups) and the slip up to "...couvrir
  le Bressan" (251 letters)**, holding 722 at group 49 ("180 722 180"). Pins in S1, every occurrence, never released: 22 de, 66 r, 581 au,
  722 = X. Model: the FT4l/FT4r one-edit CP-SAT, decomposition per edit class, sublimit 10 s. Controls seed 3, n 40, (s)/(g), unresolved
  counted high. S2 (groups 76-138) and S3 (140-170) not scored this step.
- **Real** (`align/ft4s_real_ti.out`, `_i.out`): **722 = ti: E 1 (0.9 s); 722 = i: E 1 (2.1 s).** Both resolved.
- **Controls** (`align/ft4s_{ti,i}_{s,g}.out`, 160 draws, all but one resolved, 0.8-1.9 s each): **ti (s) 0/40, (g) 0/40; i (s) 1/40
  (share 0.025, the one an unresolved draw counted high; 0 of 39 resolved draws fit), (g) 0/40.** By the registered rule **GATE PASS for
  both values** (each share <= 0.05): outcome **O3**. The S1 segment is control-backed as the slip's passage (0 of 160 wrong pairings fit
  with one edit, the real one fits under either value): the f.265r/f.266r pairing moves from I to a control-backed match for S1 (groups
  0-74). **It does not decide 722**: both values fit, so the 722 data conflict stands as logged (rule 4: f.206 ti, C; f.213 needs i;
  f.249 and f.266r cannot decide). Nothing moves in key.tsv (registered).
- Post hoc, not registered (`align/ft4s_diag.py`, `align/ft4s_diag.out`): both values fit S1 with **no edit** at all under the four pins;
  with 722 = ti, 69 of 77 single-edit classes also fit (slack), with 722 = i only the three at 722 itself (D49, W48, W50 -- the 180s beside
  it). So the S1 context "180 722 180" admits both values; a context where the two values differ is still needed.
- Rule 3: this is the second instrument on the f.266r pair and it resolved, so the clause does not retire anything; the 722 question on
  this pair is answered "cannot decide at this model's resolution" (both values fit with zero edits), not by a further tuning of the gate.
- Key and grades: no change. Vision calls 0. Subagents 0. Requests: PyPI (ortools, fresh container) only.

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4t-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step run (FT4s's Verdict): the FT4s anchored split applied to the f.249/f.250 pair, then 722 = ti vs 722 = i on the segment holding its 722.
- **Pre-registration** `align/PREREG-FT4t.md` + `align/ft4t_seg.py` (imports ft4s_seg's solver unchanged), commit 49e1f5a9, pushed before
  any registered score (sizing on one unregistered seed-99 (g) draw: resolved, 1.2 s). Anchor rule as FT4s; over all twelve C codes only
  628 'hongrie' (group 38 / word 26) and 279 'plus' (group 101 / word 64) are count-matched (501 and 581 absent; 22 is 5 groups vs 6 words).
  **S = groups 39-100 (62 groups) and slip words 27-63 ("de la maniere ... derober le", 193 letters)**, 722 at f.249 group 76 ("347 722 476",
  slip "continuera"). Pins, every occurrence, never released: 22 de (1), 66 r (2), 722 = X. Controls seed 3, n 40, (s)/(g), unresolved high.
- **Real** (`align/ft4t_real_ti.out`, `_i.out`): **722 = ti: E 1 (0.7 s); 722 = i: E 1 (0.6 s).** Both resolved.
- **Controls** (`align/ft4t_{ti,i}_{s,g}.out`, 160 draws, 158 resolved): **ti (s) 1/40 (0.025), (g) 7/40 (0.175); i (s) 6/40 (0.150),
  (g) 20/40 (0.500; 2 unresolved counted high, 18 of 38 resolved fit).** Each value has at least one control share > 0.05, so by the
  registered rule **NON-INFORMATIVE for both values** (not a PASS, not a FAIL). Outcome **O3 with no gate**: S does not decide 722, and
  unlike f.266r S1 the S pairing itself is not control-backed at this length (193 letters over 62 groups, about 3.1 letters a group: wrong
  pairings fit with one edit too often). The resolved fits alone exceed the gate (7/40, 6/40, 18/38), so the two unresolved draws do not
  change the outcome. The four control runs were started together (4 x Pool(4) on 4 CPUs); contention may explain the two unresolved draws.
- Post hoc, not registered: control fit rates run higher under 722 = i than under ti (6 vs 1, 20 vs 7): a one-letter pin constrains less
  than a two-letter one, so a fit under i is weaker evidence than a fit under ti at equal length. This also bears on f.213's "fits only with
  i" (FT4q): that is a NOFIT for ti, not a positive control-backed i.
- **Can f.266r S2/S3 decide 722? No, by construction:** f.266r's only 722 is group 49, inside S1 (checked by index, `ft4r_pair.load`); S2
  (76-138) and S3 (140-170) carry none. Of the transcribed passages only f.206 (2), f.213 (2), f.249 (1) and f.266r (1) hold 722; every one
  has now been tried. The 722 conflict stays a rule-4 data conflict (f.206 ti, C; f.213 needs i as a ti-NOFIT; f.249 and f.266r cannot
  decide); deciding it needs new material (another slip pair with 722, e.g. the unswept ff.251v-259v) or a different instrument.
- Rule 3: second instrument on f.249 to resolve without a gate (FT4i/FT4q whole-pair one-edit: controls 0.80 / >= 0.60; FT4t segment:
  0.175 / 0.500). For the **722 question on f.249** the one-edit family is [retired] (untestable by this instrument at this length), not
  refuted; f.249's other gaps (open codes) are untouched.
- Key and grades: no change. Vision calls 0. Subagents 0. Requests: PyPI (ortools, fresh container) only.

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4u-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Steps run (FT4t's Verdict, items 1 and 2): (1) f.266r S2/S3 under the FT4s anchored split as second witnesses for codes other than 722;
(2) a 300 px thumbnail sweep of ff.251v-259v for further slip+cipher pairs or 722 occurrences.
- **(1) Pre-registration** `align/PREREG-FT4u.md` + `align/ft4u_seg.py` (imports ft4s_seg's solver unchanged), commit 9dbb1bd0, pushed
  before any registered score (sizing: one unregistered seed-99 (g) draw per segment, E 0 in 1.4 s / 0.6 s). Cut at 501 'et' (FT4s).
  **S2 = groups 76-138 (63) / "le bergamasc ... audits confins" (163 letters), pins 22 de x3, 66 r x3, 581 au x1; S3 = groups 140-170 (31)
  / "de faire de brescia ... sa residence" (75 letters), pins 22 de x2, 66 r x1.** Controls seed 3, n 40, (s)/(g), run serially.
- **Real** (`align/ft4u_real_S2.out`, `_S3.out`): **S2 E 1 (1.3 s); S3 E 1 (0.5 s).**
- **Controls** (`align/ft4u_S{2,3}_{s,g}.out`, `align/ft4u_summary.out`; 160 draws, all resolved): **S2 (s) 0/40, (g) 0/40 -> GATE PASS.
  S3 (s) 7/40 (0.175), (g) 3/40 (0.075) -> NON-INFORMATIVE** (75 letters over 31 groups is too short for this gate). So S2 is a control-backed
  passage of the slip, and with S1 (FT4s) groups 0-138 of f.266r's 171 are now control-backed against the f.265r slip.
  **Second witnesses (registered decisive outcome):** 581 'au' gets its first witness outside f.206 (1 occurrence pinned); 22 'de' and 66 'r'
  a third (after f.216v). key.tsv notes updated on those three rows only; no value or grade moved (they were C already). VERIFY flag for a
  separate verifier. S3 witnesses nothing.
- **Registered M readout on S2** (`align/ft4u_S2_mpin.out`; no controls, so no grade change): each M value pinned in addition to the C pins.
  **Consistent (E 1): 303 fa, 444 en, 347 con. Proved inconsistent with one edit (E 0): 121 ons, 188 lar, 834 kowitz, 344 mee, 24 in, 534 ches.**
  Some of these were expected from substring counts noted in the PREREG before any run (834 'kowitz' and 534 'ches' never occur in S2's text;
  121 has 3 occurrences against one 'ons'; 188 has 3 against one 'lar'); 344 'mee' (1 substring) and 24 'in' (3 substrings) were not. These are rule-4 disputes against M values inferred by word-boundary splits of f.206, conditional on the S2 pairing
  and the C pins; nothing moves in key.tsv. In particular 834 is not 'kowitz' wherever it stands in S2 (712+834 = Lobkowitz on f.206 is a split,
  not a witness).
- **(2) Sweep.** `tools/gallica_folio.py btv1b525174513 --folio 251/259 --side v` confirmed canvases f516 = 251v, f532 = 259v by label
  (manifest notes two offsets across the volume; labels used). 17 pages fetched at 300 px (`images/lowres/s300/v516..v532_*_300.jpg`, 17 HTTP
  200, >= 1.6 s apart), contact sheet `images/lowres/sheet_251_259.jpg`, one vision read: clear Lorenzi-to-Montaigu letters from Florence, June
  1744 (252r "6 Juin 1744", 256r "13 Juin", 258r "20 Juin"; 254r a short letter, 254v-255r blank or nearly), each signed Lorenzi; 251v, 255v, 257v
  dockets. **No pasted slip. One page with numerals: f.252r** carries, at the foot of the letter after "vous saurez, Monsieur, que le", **15 numeral
  groups** with a **clear interlinear gloss in a lighter, smaller hand** above them. One zoom (f517 at 1000 px, one request; crop
  `images/lowres/v517_252r_band.jpg`), second vision read, not a transcription (no line crops, one look, grade M throughout):
  groups `527 253 447 188 767 369 213 248 660 419 807 121 / 230 10 56`, then clear "Les commissaires des vivres de l'armee"; gloss read roughly
  "Gnal Mar(u?)elli est depuis p(lu)s(?) 3 jours de retour a Bologne". **No 722 among the 15 groups**, so the 722 conflict is not decided by it.
  It is a sixth cipher+clear pair (an interlinear decipherment, not a slip), short (15 groups), carrying 188 (M 'lar', disputed on S2 above),
  121 (M 'ons', disputed on S2), 10 (M 'a'), 369/213/248 (also on f.266r) -- material for a later transcription + alignment step.
- Rule 4: 722 stays a data conflict (f.206 ti, C; f.213 i as a ti-NOFIT; f.249, f.266r S1 cannot decide); every transcribed 722 tried, and the
  swept ff.251v-269v/270-289 add none. Rule 3: S3 non-informative is a length limit of this gate, logged, not a negative.
- Vision calls 2 (contact sheet; f.252r band). Subagents 0. Requests: gallica.bnf.fr 18 image + 2 manifest (gallica_folio.py); PyPI (ortools, pillow).

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4v-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step (FT4u's Verdict): the sixth pair, f.252r (canvas f517): 15 numeral groups at the foot of Lorenzi's 6 June 1744 letter and the
interlinear clear gloss above them. PREREG `align/PREREG-FT4v.md` pushed (d4f12f6b) before any pass or score.
- Crops: `python3 tools/iiif_lines.py --image images/f252r/src_f517_698_2951_3956_2620.jpg --out images/f252r --prefix f252r
  --centres 1190,1471 --debug` (native region fetched once; the auto profile merged gloss and numerals into one band, so the
  centres were set by eye on the debug overlay). 4 crops, 2400 px.
- Two blind Opus passes (one call each, crops only): **15/15 groups agree**, the same two doubts flagged by both (253 alt 233,
  419 alt 417); gloss agreed letter for letter. Reconciliation by eye on the crops: 253 (its middle digit has the shape of the 5 in
  527) and 419 (its 9 has a tail, like the 9 of 369). `ciphertext_f252r.txt`:
  `527 253 447 188 767 369 213 248 660 419 807 121 / 230 10 56`.
  Gloss (`slip_f252r.txt`): literal "G^al Marulli en depuis pl^rs jours de retour a Bologne". The superscript reads "rs"
  (plusieurs), not FT4u's one-look "plus 3", and "en" may be a cramped "est". Expanded (primary per PREREG): "general marulli en
  depuis plusieurs jours de retour a bologne", which reads "General Marulli has been back in Bologna for several days".
- Registered E (`align/ft4v_pair.py`, ft4s_seg solver unchanged; `align/ft4v_real*.out`, `ft4v_P10_*.out`):
  **P188 'lar': E 0, P121 'ons': E 0, PALL: E 0.** In each case the value does not occur as a substring of the gloss at all
  (nochunk), in the primary, literal and 'est' texts alike. This is a rule-4 dispute against 188 'lar' and 121 'ons', the second for
  each after FT4u's S2 readout. It is conditional on the gloss being a literal decipherment rather than a paraphrase. No key edit.
  **P10 'a': E_real 1, controls (s) 37/40 and (g) 40/40 -> NON-INFORMATIVE**, as registered for a common substring.
- Registered C readout (`align/ft4v_ambig.out`): no pins, no repeated code, so every group has 12-361 feasible chunks. **0
  unambiguous alignments, 0 C candidates**, and key.tsv is unchanged. The pair has no C code, so it adds no witness to the C key
  and none to 722 (absent).
- Observation (unscored): 15 groups for 52 expanded letters, about 3.5 letters per group, consistent with the syllabic/word
  nomenclator. 527 (2 other occurrences), 253 (8), 369 (7) and 213 (10) recur elsewhere. A later pooled run could pin chunks of
  this gloss jointly with those passages; that would be a new instrument, not registered here.
- Vision calls 3 (2 blind subagent passes + reconciliation by this worker on 2 crops) plus 1 debug-overlay look; subagents 2 (Opus).
  Requests: gallica.bnf.fr 2 (info.json, one native region).
Not found in: none searched this step. Rule 10: no novelty class here.

## FT4w-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step (FT4v's Verdict, first item): the f.249/f.250 one-edit control draws under the FT4l solver, unchanged
(`one_edit_seg.py --pair f249 --ctrl s|g --dec --draws i-j`, seed 3, n 40, sublimit 10 s). PREREG `align/PREREG-FT4w.md`
(run plan only, nothing new registered) pushed e1e50e46 at 13:55 UTC before any draw. Fresh container, ortools 9.15 (FT4n's
version not recorded). Blocks of 5, foreground, nothing else running; every block pushed as it finished.
- **(s), complete, n 40** (FT4n's 0-9 + `align/ctrl_s_f249_dec_b3.out`..`_b8.out`; pooled `align/ctrl_s_f249_dec_pooled.out`):
  **E = 1 in 16 of 40 = 0.400, every one an unresolved draw counted high; resolved fits 0 of 24.** Unresolved draws: 12, 20-26,
  28-31, 34-37 (138-205 s each); resolved draws 8.6-140 s.
- **(g), draws 0-19 only** (`align/ctrl_g_f249_dec_b1.out`..`_b4.out`; `align/ctrl_g_f249_dec_pooled_0-19.out`): E = 1 in 7 of 20,
  all unresolved; resolved fits 0 of 13. Draws 20-39 not run: g 20-24 started 15:52 and was stopped by the worker at 15:52:22 (driver log)
  because blocks took 6.5-15 min and it would likely cross the 16:04 line (PREREG-FT4w stop rule). **(g) not scored** (20 of 40).
- **Gate (registered, PREREG-FT4i/FT4l):** E_real = 1 (FT4n), but the completed (s) control alone is 0.400 > 0.05 counted high,
  so the f.249 one-edit gate **cannot PASS** whatever (g) 20-39 shows. Branch: the share comes from unresolved draws only (0 of
  37 resolved control draws fit across (s) and (g)), i.e. **NON-INFORMATIVE (power)**; the "real" branch (> 2 of 40 resolved fits)
  is reachable only if (g) 20-39 had 3+ resolved fits, which changes the subtype, not the non-PASS. By the FT4l rule-3 clause
  (third instrument) the one-edit gate is **[retired] for this solver on f.249** (untestable at this length by this instrument, not
  refuted). Next for the pair is new material or a different instrument (the pooled pin run below), not a fourth solver or more time.
- Note: FT4n's (s) draws 0-9 all resolved (13.7-116 s); here 16 of 30 later (s) draws timed out. Draw difficulty and the ortools
  version are not separable (FT4n did not record its version); either way the registered rule counts them high.
- Process note: the first (s) 10-14 output was lost because an intermediate commit's rebase rewrote that tracked file while the
  solver still wrote to it; the block was re-run from the same seed (draws are deterministic). Later blocks wrote to the scratchpad
  and were moved into align/ only when finished. Lesson: never commit a file a running job still has open.
- Key and grades: no change (registered); `decode_key.py --check` exit 0. Vision 0, subagents 0. Requests: PyPI (ortools) only.

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4x-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step (FT4w's Verdict): pooled pin run of f.252r with the passages sharing its codes, under a NEW instrument (the one-edit family
is [retired] for f.249): **exact match, zero edits**, one concatenated CP-SAT model (blocks joined by a separator pinned to '|',
so a code in two blocks carries one chunk; C pins 22/66/581; 722 free; M values not pinned). `align/ft4x_pool.py`, PREREG
`align/PREREG-FT4x.md` pushed 404d0f79 before any run; addendum 44d429e9 after stage 0 only.
- Stage 0 (`align/ft4x_stage0.out`): exact alone: f.266r S1 True, **S2 False**, f.249 FT4t segment True, f.252r True. S2 dropped
  (a block with no exact fit makes J nofit for real and control alike -- a non-test). Stage 0b (`align/ft4x_stage0b.out`):
  **S1 + f.249 segment jointly: nofit** (proved), so f.249 dropped by the registered rule; the pooled run is S1 + f.252r. Shared
  codes: 10, 121, 213, 248, 253, 369, 807 (527 occurs only after S2; 188/660 only in S2: not tested).
- Controls first (seed 3, n 40): **(s) 0/40, (g) 0/40**, all resolved (`align/ft4x_ctrl_s.out`, `_g.out`) -> the gate could pass.
- **Real: J nofit** (proved, 0.6 s; `align/ft4x_real.out`) -> registered branch: no PASS; a rule-4 conflict readout. The f.252r
  gloss as expanded cannot be exactly consistent with f.266r S1 under the C key. Secondary texts 'literal' and 'est': nofit too
  (`align/ft4x_readout.out`). Note: the controls are also nofit, so the nofit is not evidence against the pairing by itself; it is a
  proof of conflict between the two passages under exact match, conditional on both transcriptions and the gloss.
- Post hoc, NOT registered (`align/ft4x_readout*.out`): keep-one-shared-code: every single shared code fits except **253** (no
  exact-feasible S1 chunk for 253 is a substring of the gloss); dropping 253 plus one of **213, 248 or 369** fits, dropping 253 plus
  10/121/807 does not. Reading f.252r group 1 as its flagged alternative 233 (absent from S1) leaves the same one remaining conflict
  among 369/213/248. "213 248" is a consecutive pair in both S1 (groups 39-40) and f.252r (groups 6-7). So the conflict is at most
  two codes: 253 (a flagged doubtful read on f.252r) and one of 369/213/248.
- Also learned: S1 and the f.249 FT4t segment are themselves jointly inconsistent under exact match (shared codes 10/121/369/807
  and others), a further sign that M splits, polyvalence or misreads separate these passages beyond zero edits.
- Key and grades: no change (no decisive outcome registered); no VERIFY flag. `decode_key.py --check` exit 0. Vision 0,
  subagents 0. Requests: PyPI (ortools) 1.

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4y-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step (FT4x's Verdict): pre-registered blind eye re-check of the positions FT4x's post hoc readout implicates (PREREG
`align/PREREG-FT4y.md`, pushed 3b694072 before any vision call). 7 targets: f.252r g1 (253, flagged alt 233), g5 369, g6 213, g7 248;
f.266r S1 g39 213, g40 248, g46 369. 7 decoys: f.252r g0 527, g2 447, g3 188, g4 767; S1 g35 718, g42 63, g48 180. One group per
crop (`images/ft4y/`, cut with `tools/iiif_lines.py --image` from the on-disk f.252r source and the FT4q f.266r line crops, boxes from
the tool's `--groups` pieces), shuffled (seed 20261003), 2 Opus 5.5 vision calls (one per leaf), no expected values shown.
- Targets: **7/7 read as transcribed** (high 4, medium 3; 253 medium with 5/3 alternatives, no 233 reading). 0 HIGH changes.
- Decoys: 6/7 as transcribed; 1 medium change (f.252r g0 527 read 327, digit1 3 or 5) -- a doubt on a position outside the conflict,
  logged, not corrected (registered rule: medium/low = doubt only). 0 HIGH decoy changes, so the reader was not NOISY.
- Registered outcome **P1**: the FT4x exact-pooled conflict (253 plus one of 369/213/248) is not a misread at these positions at this
  reader's resolution (a third blind eye beside FT4v's two passes and FT4q's two). Logged as a rule-4 conflict between the f.252r gloss
  and f.266r S1 under the C key (gloss paraphrase, polyvalence or an M split). No FT4x re-run (no digit changed), no key change, no
  VERIFY flag. Reads: `align/ft4y_reads.tsv`. `decode_key.py --check` exit 0.

Not found in: none searched this step. Rule 10: no novelty class here.

## FT4z-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step (FT4y's Verdict): pre-registered pooled exact pin run of the passages that each fit with no edit (f.206, f.216v, f.266r S1)
on the disputed f.206 split values (PREREG `align/PREREG-FT4z.md` + `align/ft4z_pool.py`, pushed e2ad0f1a before any run; addendum
cc6cadd1 after stage 0 only). Instrument: FT4x's exact (0-edit) CP-SAT unchanged, C pins 22/66/581, 722 free, MAXLEN 12.
- Testability from occurrence counts (F206, F216V, S1): 121 (1, 5, 5), 534 (1, 0, 1); 188, 834, 344, 24 occur only in f.206 and
  253 only in S1 -> **not tested by this pool** (no joint pin exists; a fact of the material).
- Stage 0 (`align/ft4z_stage0.out`): each block alone fits exactly; **F206+F216V nofit, F206+S1 nofit**, F216V+S1 fit. By the FT4x
  addendum rule F206 was dropped (it would make every draw nofit by construction); pool F216V + S1, so 534 also became untestable.
- Controls first, seed 3, n 40, S1 perturbed: **(s) 0/40, (g) 0/40**, all resolved -> gate could pass.
- **REAL J fit -> GATE PASS.** Readout: of 306 substrings present in both f.216v and S1 slips, **121's only feasible chunk is 's'**
  (complete, 0 unresolved). Registered outcome: decisive, value change: key.tsv 121 ons (M) -> **s (C, "FT4z PASS, pending
  VERIFY")**; FT4d had already tied 121 s at M. Diagnostics (`align/ft4z_diag.out`): f.206 alone fits with 121 s (and with 363 sion);
  f.206 (338 released) + f.216v fits with 121 s and not with ons. 363 si -> **sion at I** (compensating re-split of pro|vi|?|s,
  not separately tested). Reading letters unchanged (PROVISIONS); grades now C 24, M 37, I 1.
- Secondary readout (registered, no gate, `align/ft4z_release.out`): F206+F216V regains an exact fit only by releasing 338 (tout;
  FT4d left it untied); F206+S1 is restored by no single release of its shared codes 10/114/121/123/271/347/534/722.
- Rule-4 conflicts logged with witnesses: 121 = s (f.216v + f.266r S1, control-backed) vs 'ons' (f.206 split, superseded) and vs
  f.252r gloss (FT4v, no 's'/'ons' chunk at its position; dispute stands); 534 ches (f.206 split) vs f.266r S2 (FT4u E 0), not tested
  here; 188/834/344/24 (f.206 split) vs S2 (FT4u) and 188 vs f.252r (FT4v), single-witness, not testable by pooling.
- Rule 3 count: the pooled-exact instrument's second use (FT4x on f.252r first); its first on 121. Not a third attempt.
`decode_key.py --check` exit 0. Not found in: none searched this step. Rule 10: no novelty class here.

## VERIFY-ROU121 (3 Oct 2026, account-4 verifier, key-row check only)

Claim audited: FT4z "pooled exact f.216v + f.266r S1 GATE PASS, 121 = s sole feasible chunk -> key 121 = s at C pending VERIFY".
Script `align/verify_rou121.py` (imports FT4z's blocks and FT4x's solve_exact unchanged); outputs `align/vr121_*.out`.
1. Reproduction, different seed: REAL F216V+S1 J fit; 121 feasible set ['s'] of 306 (complete, 0 unresolved). Controls seed 11,
   n 80: (s) 0/80, (g) 0/80, 0 unresolved -> gate reproduces.
2. Gate audit. Power: the real solution's ten 121 spans were replaced by a planted value in the slip text; planted 'ons' -> J fit,
   feasible set exactly ['ons'] of 313 (recovered, unique; 's' rejected), so the readout can tell s from ons on this pool
   planted 'qx' -> feasible exactly ['qx'] of 305 (recovered, unique). Per block: f.216v alone already forces s uniquely (1 of 2478 candidates);
   S1 alone admits e, i, l, n, s -- the pooled uniqueness rests mainly on f.216v (whose pair passed FT4c), S1 is consistent.
   F206 drop: not in the original PREREG text (its rule covered blocks that fail alone; F206 fits alone); added in the
   addendum commit cc6cadd1 (16:38:03 UTC) after stage 0 only, before the control and real outputs (9f97114f, 16:41:03).
   Stage 0 showed F206+F216V nofit for real data, so every control draw would be nofit by construction (rule 3, a control
   that cannot differ); the drop is the only way to a test and was decided on stage-0 facts, not on J_real. Accepted, noted
   as an addendum decision, not a pre-registered one.
3. Independent 121 witnesses (exact / one-edit, 121 free vs s vs ons; no controls, consistency only):
   f.206 (x1): exact fits free, s, ons -> untestable (FT4z's key note "not with ons" corrected: f.206 alone fits ons too).
   f.213 (x4): exact nofit for any; one-edit s fit, ons nofit -> agree (s; ons excluded).
   f.249 full (x4): exact nofit for any; one-edit s fit, ons nofit -> agree. f.249 FT4t segment (x1): exact s fit, ons nofit -> agree (weak, 1 occ).
   f.266r S2 (x3): one-edit s fit, ons nofit -> agree (FT4u's "121 ons inconsistent" is resolved by s).
   f.266r S3 (x2): exact s fit, ons nofit -> agree (S3 gate was NON-INFORMATIVE in FT4u; consistency only).
   f.252r (x1): exact s fit, ons nofit -> agree, weak (single occurrence, a lone 's' in the gloss); FT4v's dispute was against ons.
   Disagree: none. Untestable: f.206.
4. Verdict: CONFIRM. key.tsv 121 = s stays at C (period decipherment as known plaintext, control-backed pooled gate, reproduced
   at a second seed, power shown); "pending VERIFY" replaced by the confirmation. 363 sion stays I (compensating split, not
   separately tested -- not part of this check). `decode_key.py --check` exit 0 (tokens 62: C 24, I 1, M 37). No status change.

## FT4aa-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step (FT4z's Verdict): pre-registered two-release scan locating the two f.206 exact conflicts (PREREG `align/PREREG-FT4aa.md`, pushed
e7785f6d before any run; script `align/ft4aa_scan.py`). Instrument: FT4x/FT4z exact CP-SAT unchanged, C pins 22/66/581, 722 and 121
free (primary), MAXLEN 12, 30 s. Release = a code renamed in the F206 block only.
- Controls first, seed 3, n 40, partner perturbed: pair A (F206+F216V) (s) 0/40, (g) 0/40; pair B (F206+S1) (s) 0/40, (g) 0/40
  (`align/ft4aa_ctrl_{As,Ag,Bs,Bg}.out`). Gate condition met as registered. **Caveat (rule 3):** all 160 control draws were negative
  at the first screen (release-all nofit: a shuffled partner never fits exactly even with F206 fully decoupled), so the control never
  reached the release step; it shows a shuffled partner cannot be rescued by any release, not how specific a <=2-release is among
  blocks that fit alone. The PREREG's claim that the control "can differ" held in principle, not in practice (bMAT2 shape).
- REAL (`align/ft4aa_real.out`, no unresolved solves): pair A 0-release nofit; minimal <=2 restoring releases **exactly one: {338}**
  (0 of the 36 pairs without 338 restore). Pair B 0-release nofit; no single restores; minimal <=2 restoring releases **exactly one:
  {347, 534}** (1 of 28 pairs). Secondary with 121 = s pinned (`align/ft4aa_real_pin121.out`): identical ({338}; {347, 534}).
- Registered outcome: **decisive locator** for both pair-blocks. Mapping per PREREG: rule-4 conflict notes on key.tsv 338 tout (f.206
  split vs f.216v/f.217r) and 347 con + 534 ches (f.206 split vs f.266r S1); values and grades unchanged (all three M); no value change
  (a release says where, not what); VERIFY flag line in ROOM.md. 534 ches was already disputed against f.266r S2 (FT4u E 0); 347 con
  was consistent in FT4u's S2 readout (no controls) -- the S1 conflict needs both released, so either value or the f.206 boundary
  between them is the site.
- Rule 3 count: pooled-exact instrument, first use on the f.206 locator question. Reading letters unchanged; `decode_key.py --check` exit 0.
Not found in: none searched this step. Rule 10: no novelty class here.

## FT4ab-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Value readout on FT4aa's locators, pre-registered in `align/PREREG-FT4ab.md` (commit a1f13997, pushed before any run). Script
`align/ft4ab_readout.py`, output `align/ft4ab_readout.out`; instrument FT4x/FT4z/FT4aa's exact (0-edit) CP-SAT with a solution
loop (solve, read the code's chunk, forbid it, re-solve until INFEASIBLE). Pins 22 de, 66 r, 581 au, 121 s; 722 free; MAXLEN 12;
30 s per solve. Every enumeration below ended INFEASIBLE (complete), none unresolved.

| pair | released | code (side) | feasible chunks | unique |
|---|---|---|---|---|
| F206 + F216V | {338} | R338 (f.206) | 8: t, ienttout, enttout, nttout, ttout, tout, ut, out | no |
| | | 338 (f.216v, 2 occ.) | 1: tou | yes |
| F206 + S1 | {347, 534} | R347 (f.206) | 4: con, scon, uscon, luscon | no |
| | | 347 (S1) | 12: x, xc, xco, xcon, xconf ... xconfinsdumi | no |
| | | R534 (f.206) | 9: s, es, hes, ches, aches, taches, ttaches, attaches, sattaches | no |
| | | 534 (S1) | 1: che | yes |

Registered outcome: no F206-side value is unique (each released code occurs once in f.206, so its chunk trades letters with its
neighbours), so the registered witness check did not run and no VERIFY flag is raised; the key's current values (338 tout,
347 con, 534 ches) are each inside their f.206 set, and stay M, unchanged. FT4aa's controls were non-discriminating on two-release
specificity, so none of this is control-backed (no gate was run; a readout, not a negative or a gain).
Unregistered secondary (`--secondary`, `align/ft4ab_secondary.out`, diagnostic only, drives nothing): the two unique partner-side
values pinned alone in each block holding the code -- 338 = tou: f.216v fit, f.206 **nofit**; 534 = che: S1 fit, f.206 **nofit**,
f.266r S2 **nofit**. So neither partner value is witness-consistent: f.206 cannot take tou for 338 or che for 534 even alone, and
S2 rejects che. The f.206/f.216v and f.206/S1 conflicts are therefore not a mis-split of 338 or 534 alone: under the C pins
(121 = s included) f.206 needs a further change elsewhere (polyvalence of 338/534, an f.206 split error at a neighbouring code,
or a slip paraphrase) for the partner value to fit. Rule 4: 338, 347, 534 stay M, values unchanged, conflict notes extended.
Script only, 0 vision calls, 0 network requests (pip ortools only).

## FT4ac-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Single-release scan on f.206 alone, pre-registered in `align/PREREG-FT4ac.md` (commit 76666ab0, pushed before any run). Script
`align/ft4ac_scan.py`, outputs `align/ft4ac_ctrl_{Ts,Tg,Cs,Cg,p}.out`, `align/ft4ac_real.out`. Instrument: the exact (0-edit)
CP-SAT of FT4x-FT4ab unchanged (MAXLEN 12, 30 s). Arms H-T 338 = tou, H-C 534 = che, each with 121 s, 22 de, 66 r, 581 au pinned.
Candidate rows 22, 66, 581, 121, 279, 336, 501, 722 (release = every occurrence an independent token). Every solve resolved
(0 unresolved anywhere).

| run | base fit | release-all fit | false-decisive / unique-located |
|---|---|---|---|
| (s) H-T | 0/40 | 21/40 | 0/40 |
| (s) H-C | 0/40 | 26/40 | 0/40 |
| (g) H-T | 0/40 | 31/40 | 0/40 |
| (g) H-C | 0/40 | 29/40 | 0/40 |
| (p) planted, n 40 (37 redrawn as still fitting) | 0/40 | -- | contains-X 40/40; unique-located 22/40 = 0.55 |
| REAL H-T | nofit | fit | restoring set {581} (unique) |
| REAL H-C | nofit | fit | restoring set {581} (unique) |

Registered outcome: each arm has exactly one restoring row (581) and the null controls pass (0/40 false-decisive, release-all
fit in >= half of draws, so unlike FT4aa they could vary), but the planted known-answer control locates uniquely only 0.55 < 0.80:
**locator, not control-backed** (PREREG). No VERIFY flag; key values and grades unchanged. Descriptor: unpin-only (581's
repetition kept) is nofit in both arms, so 581 must take a different chunk at one occurrence.
Unregistered secondary (`align/ft4ac_secondary.py`, `.out`, diagnostic only): the occurrence is different per arm and is in each
case the hypothesis code's right-hand neighbour -- H-T frees 581 at group 36 only (groups 35-36 = 338 581, slip "tout au"),
H-C frees 581 at group 22 only (groups 21-22 = 534 581, slip "attachés aux"). So tou/che fit f.206 only if the left-over final
letter (t of tout, s of attachés) is taken by the next group, i.e. 581 = "tau" / "saux" at that one place, or the letter is
unencoded in f.206 (cf. key 379's note, the x of aux unencoded). That is a one-letter boundary question between 338/534 and 581
(I), not a wrong key row, and the exact instrument cannot tell an unencoded letter from a shifted chunk. Rule 4: 338, 534 stay M
(tout, ches), 581 stays C; conflict notes extended. Rule 3: fifth use of the exact CP-SAT on the f.206 conflict (FT4x, FT4z,
FT4aa, FT4ab, FT4ac), third locating attempt that does not decide (FT4aa, FT4ab, FT4ac): the exact instrument is [retired] for
the f.206 conflict. Script only, 0 vision calls, 0 subagents, 0 network requests (pip ortools only).

## FT4ad-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Blind eye check of the two f.206 boundaries FT4ac located (534 581 at groups 21-22, across the f.207r L01/L02 line break; 338 581
at groups 35-36, f.207r L03), pre-registered in `align/PREREG-FT4ad.md` (commit 83d7821d, pushed before any read). Crops
`images/ft4ad/C1-C8_L01.jpg` cut with `tools/iiif_lines.py --image` from the on-disk f.207r line crops (`--region` boxes from the
tool's own `--groups` pieces, each extended to half the gap either side, g21 to the line end, g22 from the line start); 4 targets
+ 4 adjacent decoys (420, 379, 279, 347), shuffled seed 20261003. One Opus 5.5 subagent vision call, crop paths only, no
transcription, key, slip or expected values. Reads: `align/ft4ad_reads.tsv`.

| | read as transcribed | HIGH changes | non-separator marks |
|---|---|---|---|
| targets (534, 581, 338, 581) | 4/4 (338 high; 534, 581, 581 medium: open-backed 5) | 0 | 0 |
| decoys (420, 379, 279, 347) | 4/4 (3 high, 1 medium) | 0 | 0 |

Registered outcome **P1**: every target group reads as transcribed and no boundary shows anything but the ordinary separator dot
(no clear letter, cancel, correction, extra or run-together sign; at g22 only faint offset/bleed-through strokes at the left
margin, read by the reader as not a group). The one-letter boundary FT4ac found (tout au / attachés aux) is not explained by the
image at this reader's resolution: it stays an unencoded-letter or shifted-chunk question (I); 338, 534 stay M, 581 stays C; no key,
grade or transcription change, no VERIFY flag. The reader's only doubt is the open-backed 5 (3 possible) in 534 and both 581s
(medium); none of the decoys carries a 5. 1 vision call, 0 network requests.

## GAPS204-naf14913-rousseau-venice-1743 (3 Oct 2026, account-4)

Step named in this worker's prompt: a pre-registered blind eye re-check of f.252r groups 1 and 5-7 (253 vs 233, 369, 213, 248) and
f.266r S1 groups 39-40/46. Not run: rule 3's third-attempt clause applies to every one of the seven groups. Count of blind looks
already on file, all Opus 5.5 vision reads of crops with no expected values shown:
- f.252r g1 253, g5 369, g6 213, g7 248: FT4v passes A and B (15/15 agree; 253 alt 233 flagged by both), then FT4y's single-group
  decoy-mixed re-check (PREREG-FT4y; 253 medium with 5/3 alternatives, no 233 reading) = **3 looks, all as transcribed**.
- f.266r S1 g39 213, g40 248, g46 369: FT4q passes A and B (171/171 agree), then FT4y = **3 looks, all as transcribed**.
FT4y was this exact protocol (single-group crops, equal decoys, shuffled, P1 outcome, decoy gate passed: 0 HIGH decoy changes), so a
re-run would be the same instrument on the same crops with no changed knob. Logged **[retired], instrument: blind Opus vision read
of the existing crops**, for these seven positions; the f.252r/S1 conflict stays a rule-4 data conflict (gloss paraphrase,
polyvalence or an M split), not a misread at this resolution. Only new material or a different instrument (native re-fetch at
higher resolution, or a person's eye on the leaf) reopens it. No PREREG written (no read run), 0 vision calls, 0 subagents,
0 network requests; key, grades and transcription unchanged.

## GAPS210-naf14913-rousseau-venice-1743 (4 Oct 2026, STALE4 for account 4, account 1 worker)

Step run (FT4ad/GAPS204 Verdict): the 300 px sweep of NAF 14913 leaves outside ff.205v-289v for numeral-group cipher passages.
Pre-registration `align/PREREG-GAPS210.md` (commit 657be1f7), pushed before any vision read. Scope this session: **ff.1r-205r
(canvases 15-423, 409 pages)**, fetched from f.205r backwards (`align/gaps210_fetch.py`; manifest with URL, bytes and sha1 in
`align/gaps210_fetch_manifest.tsv`; thumbnails kept out of git, folder already 32 MB). **ff.290r-392v (canvases 595-800, 206 pages)
not swept**: outside this session's request budget (good-citizen rule, a few hundred per host).
- Sheets (`align/gaps210_sheets.py`, seed 210): 30 contact sheets of 18 tiles (1800 x 1404 px), 14 sweep tiles + 4 controls at random
  positions per sheet, tiles labelled by random id only. Controls: POS-A f.205v (f.206 key's own cipher page), POS-B f.266r (numeral
  block inside a clear letter), POS-C f.252r (15 groups only), NEG f.206r (Rousseau's clear slip). Two blind Opus subagent calls
  (sheets 1-15, 16-30), sheet paths only. Mask `align/gaps210_mask.tsv` (written after both reads); per-tile results
  `align/gaps210_reads_masked.tsv` (reader rows not reproduced verbatim: only yes/maybe rows were kept; unlisted tiles = "no").
- **Control gate: 30/30 sheets PASS** (POS-A 30/30, POS-B 30/30 flagged yes). Sensitivity: POS-C (15 groups) 30/30 flagged. NEG
  false flag 0/30. Caveat: the second reader noticed that the same four pages recur on every sheet, so on later sheets the controls
  were recognisable (blinding of the controls weakened, not the sweep tiles).
- **Outcome O1: four sweep pages flagged yes** (`align/gaps210_flags.tsv`), two two-page cipher passages, laid out like the
  ff.205v-266r ones (clear letter, numeral block, clear continuation):
  - **ff.165r-165v** (canvases 343-344): a Florence letter, date read at thumbnail size as 1 Sept 1743 (I); about 4 numeral lines at
    the foot of 165r, about 13 at the head of 165v.
  - **ff.197v-198r** (canvases 408-409): about 18 numeral lines on 197v and 14 on 198r, clear prose around them.
  - ff.95r-95v (canvases 203-204) flagged maybe by the reader: in the worker's own look at the six flagged thumbnails these are notes
    with figure columns, accounts-like, not numeral-group cipher (M).
  No slip in Rousseau's hand was noticed beside either passage at this size (not checked at native resolution). Whether either
  passage uses the f.206 key and carries 338, 534 or 722 is unknown until transcribed.
- Not found in: ff.1r-205r other than the four pages above (no numeral-group block visible at 300 px, with a 15-group control detected
  on every sheet). Not searched: ff.290r-392v and the unlabelled canvases 1-14, 593-594, 801-816.
- Requests: gallica.bnf.fr 411 (409 pages + f.205v, f.206r), >= 1.5 s apart, all HTTP 200, no challenge. Vision: 2 Opus subagent
  calls + the worker's own look at one 6-thumbnail strip of the flagged pages and one sheet (sheet 1) to check legibility before the
  reads. Key, grades and transcription unchanged. Rule 10: no novelty class here.

## A3V2-ROUS-naf14913-rousseau-venice-1743 (4 Oct 2026, account 3 worker for LANE-A3V2)

Step run (GAPS210's Verdict, brief `.claude/briefs/runs/2026-10-04-acct3-a3v2-wave2.md` A3V2-ROUS): native-resolution line crops and
two blind passes of the two numeral passages GAPS210 flagged, counts of 338/534/722 and of every key.tsv code, and the f.206 key scored
with the registered gate and controls. Clock read 05:16-05:3x UTC.

- **Pages.** `tools/gallica_folio.py btv1b525174513 --folio 165/197/198`: canvases 343 (165r), 344 (165v), 408 (197v), 409 (198r), label
  offset k=14 as the manifest says. 1000 px views of the four pages (scratch only): both passages are numeral groups of 1-3 digits
  separated by points, in the same clerk hand as ff.205v-207r, inside clear Lorenzi letters. **f.165r is headed "Florence le 21 7bre 1743"**
  with the red edition number **2037** in the corner (GAPS210 read "1 Sept" at thumbnail size; 21 Sept at 1000 px) -- so this is Souchon
  1915 no. 2037 by the same red-number/edition pattern as f.206 (no. 2047), inferred (I), not checked in print this job. The cipher begins
  mid-sentence after "...la negociation, dont il avoit parle, entamee entre cette" and ends before "Je crois que M. le Mis Mari a eu ces memes
  avis". The f.197v passage begins after "...mande par sa derniere que" and ends on f.198r before "et j'ai d'autant plus lieu d'y ajouter foi,
  que l'auteur en vient en etat d'etre informe de ces sortes d'affaires plus que de toute autre" (the f.197r heading was not read).
  **No slip in Rousseau's hand and no interlinear gloss on any of the four pages** at native resolution (and none on the neighbouring
  leaves at the 300 px sweep, GAPS210): neither passage has a plain side.
- **Crops** (commands run 05:2x UTC, pasted as the brief requires):
  `python3 tools/iiif_lines.py --ark btv1b525174513 --canvas 343 --region 600,5080,3050,720 --out ciphers/naf14913-rousseau-venice-1743/images --prefix f165r --max-width 1600 --debug`
  (3 lines, 6 crops); `... --canvas 344 --region 1680,1800,2820,2460 ... --prefix f165v --max-width 1485 --debug` (11 lines, 22 crops);
  `... --canvas 408 --region 1830,1130,2780,3330 ... --prefix f197v --max-width 1465 --debug` (15 lines, 30 crops);
  `... --canvas 409 --region 680,670,2750,2250 ... --prefix f198r --max-width 1450 --debug` (10 lines, 20 crops). A first cut at the default
  --max-width 2400 gave two 2400 px segments overlapping by 1750 px on a ~3000 px region (a reader would have seen most of each line twice),
  deleted and re-cut with --max-width set to half the region plus 150, so every line is two segments with the tool's 150 px overlap; all
  four debug overlays checked (every band edge in whitespace; 3/11/15/10 lines as counted by eye). The four native source regions
  (downscaled to 1600 px by the tool, folder over 30 MB) and the overlays were deleted after cutting and are re-derivable:
  images/images_manifest_full.tsv rows + regen_images.sh. Folder 35 MB (was 32 MB before this job; the 78 new crops are 4.9 MB).
- **Transcription.** Eight blind Opus 5.5 subagent calls, one page per call, crop paths only (no key, no earlier transcription):
  two passes per page. `tools/reconcile_passes.py` per page (scratch): **f.165r 29/29, f.165v 139/139 (err_2reader 0/168 = 0.0%)**;
  **f.197v 171/179, f.198r 111/119 (16/298 = 5.4%)**; pooled 16/466 = 3.4% first-reading disagreement. Twelve of the sixteen splits are one
  glyph: a 1 written after a 2 or a 3 ligatures into a u-shape, so "2u7"/"3u7" (read 211/201/221/301/311 by the passes) is **217/317** --
  settled on a zoomed strip against this hand's "21", "214", "121" and the hooked 7 of "771"/"746" (scratch zoom_u_glyph.jpg), and the
  same reading the f.213 and f.249 workers already made ("the same hooked 7 as 746/317", ciphertext_f213.txt; "217 121 172 208",
  ciphertext_f249.txt). The other four: f197v L04 720 (hooked 7, not 120), L15 279 (not 219), f198r L02 767 and 70 (hooked 7s, not
  464/40), L03 270 (not 210; 270 is the f.213 reconciled form), L04 843/63 (round-top 3s), L05 121 (the "1241" both passes saw is "1 2u" with
  the ligature). Both passes also listed a lone "1" between 501 and 10 on f198r L02: the boundary zoom shows it is the clipped 1 of "501"
  at the left edge of segment 2 (the 1 at the right edge of segment 1 is the clipped 1 of "10"), removed. The reconciliation (the worker's
  own, 7 composite crop reads + 3 zooms) is the fifth priced unit. Files: `ciphertext_f165.txt` (168 groups, 105 distinct) and
  `ciphertext_f197v.txt` (296 groups, 159 distinct; one struck-through group [610] and one superscript ^52 recorded, not counted).
  a|b on 9 groups where both passes were doubtful and the crop does not settle it (none is a C code; 121|141 and 472|442 are the only
  ones touching a key.tsv code). MS marks: 311 carries a stroke beneath it at all 7 of its occurrences on ff.165-198 (and "311 14" is a
  recurring pair, 8 times), as do 338 (twice), 404, 442, 531, 635, 140, 717, 249, 369, 108 -- not read, recorded in the file headers.
- **Counts.** 338: f.165 x2 (both f.165v, L01 "347 22 338 121 306", L10 "52 338 66 476"), f.197v-198r x0. 534: 0 and 0. 722: 0 and 1
  (f198r L06 "140 722 134", one pass alt 422). Ten C codes: f.165 22 x7, 66 x1, 501 x4, 172 x1 = 13; f.197v-198r 22 x16, 66 x1, 279 x1,
  581 x2, 722 x1, 501 x5 = 26. Every key.tsv code: f.165 24 of 50 present, 46 occurrences (27.4% of groups); f.197v-198r 29 of 50, 94
  occurrences (31.8%); the per-code tables are `align/coverage_f165.out` and `align/coverage_f197v.out`.
- **Score against the f.206 key, registered gate (NOTES.md "Pre-registered gate", `align/gate_pair.py`): NON-TEST on both passages.**
  The registered statistic H is the pinned-C-code count in an exact-coverage segmentation of the passage's *slip*; with no plain side
  there is nothing to segment, so H is undefined -- not 0, not a FAIL. `align/gate_pair.py` gained a `--coverage` option (extended in
  place, no private copy) that says so first and then reports the counts above plus one **unregistered, vocabulary-level secondary**:
  K = occurrences of key.tsv codes, against (a) 200 passages of the same length drawn uniformly from 1..850 and (b) 200 drawn uniformly
  from the distinct codes of the other seven transcribed NAF 14913 passages (both controls can vary on the same axis, rule 3). Side by
  side, seed 1:

  | passage | groups | K (key.tsv occ.) | % | (a) uniform p95 / max | (b) vocabulary p95 / max | registered gate |
  |---|---|---|---|---|---|---|
  | ff.165r-165v (new) | 168 | 46 | 27.4 | 14 / 18 | 40 / 49 (>= real 2/200) | non-test (no slip) |
  | ff.197v-198r (new) | 296 | 94 | 31.8 | 23 / 28 | 70 / 88 | non-test (no slip) |
  | f.216v (FT4c PASS pair) | 79 | 22 | 27.8 | 8 / 11 | 19 / 21 | PASS H 5 |
  | f.213r-v (FT4h, no fit) | 84 | 28 | 33.3 | 9 / 11 | 20 / 24 | non-test (no fit) |
  | f.249r-v (FT4e, no fit) | 111 | 36 | 32.4 | 10 / 13 | 27 / 32 | non-test (no fit) |
  | f.266r (FT4u S2 PASS) | 171 | 51 | 29.8 | 15 / 17 | 40 / 45 | PASS (S2) |

  Reading: K is above both p95 for every passage, the two new ones included, **and it is in the same 27-33% band for the pair that PASSed
  the registered gate and for the two pairs that have no consistent fit** -- so the secondary separates "same nomenclator vocabulary" from
  random groups and nothing finer; it cannot say whether the f.206 *values* (338 = tout, 534 = ches, 722 = ti, or any other) hold on
  ff.165/197v. No key change (none is licensed; `key.tsv` untouched, `decode_key --check` unchanged). The two passages are cipher-only
  material: they add occurrences (338 x2, 722 x1, 22 x23, 311 x7) but no plain side, so they cannot enter `align/pooled_gate.py` or the
  rule-4 338/534/722 disputes until a plain side exists.
- **Recurring strings across passages** (observation, no reading): "52 605 22 739" opens f.197v and also stands in f.213 L03r and f.249 L02
  (and "52 605 24 311 14" on f.165v L05; "52 605 10 840" on f.198r L01); "311 14" 8 times on ff.165-198 and once on f.249; "443 24" (f.206
  "princesse" opens 443 24 271 208) on f.197v L08 "443 24 107 40"; "473 443 412 255" on f.165v L05 and f.197v L05 identically.
  A printed decipherment of either letter would turn these into C-grade key rows at once.
- **Not found in:** no print or phrase search this job (transcription and scoring only); Souchon 1915 not opened for nos. 2037 or the
  f.197 letter. Rule 10: no novelty class here.
- Requests: gallica.bnf.fr 16 (manifest cached; 4 views at 1000 px, 4 info.json + 4 region fetches at the first cut, 4 region refetches at
  the re-cut), >= 1.6 s apart, all HTTP 200, no challenge. Subagent calls: 8 (Opus 5.5, blind passes); the worker's own vision reads: 4 page
  views, 4 overlays, 6 crops + 1 zoom strip (f.165 reconciliation), 7 composites + 3 zooms (f.197v-198r reconciliation).

## A3V2-ROUS2-naf14913-rousseau-venice-1743 (4 Oct 2026, account 3, LANE-A3V2)

Brief: `.claude/briefs/runs/2026-10-04-acct3-a3v2-wave2.md` A3V2-ROUS2. Two parts, no vision calls, no key or reading change.

**(1) images/ back under 30 MB (AX2-SHRINK pattern).** Tracked bytes 34,761,612 (35 MB, after A3V2-ROUS's 78 crops) -> **29,128,731
(29.1 MB)**. `images/images_manifest_full.tsv` rebuilt to cover every tracked file in the folder (510 rows: file, bytes, sha256, kind,
source URL or derivation recipe, cited_by from a grep of NOTES.md/align/*.txt/*.tsv/manifest.json files, status), carrying over the 11
FT4q and 4 A3V2-ROUS rows for regions already deleted. Byte-identical regen tested before any deletion, one sample per class, plain
Gallica IIIF fetch at the recorded or pattern URL: `ft4h/src_..._f440_650_650_3500_800.jpg` identical, `lowres/v440_213v_1000.jpg`
(recorded URL) identical, `lowres/v439_213r_1000.jpg` (pattern URL) identical, `lowres/s300/v516_251v_300.jpg` identical. Deleted 57
files, 5,632,881 bytes: the 3 ft4h native regions (1,229,339 B; their crops and the eye_* masks that cite them stay), 37
`lowres/v*_1000.jpg` page views (4 FT4b/FT4h, 33 FT4j/GAPS210; the contact sheets and `v517_252r_band.jpg` stay) and the 17 FT4u
`lowres/s300/v516-v532_*_300.jpg` pages. **Kept after a failed identity test**: `f252r/src_f517_698_2951_3956_2620.jpg` (re-fetch 558 B
longer, 1,025,302 differing bytes from byte 830 -- Gallica re-encoded, or FT4v fetched it another way), `v424_1000.jpg` (69 B longer),
and the 38 GAPS210 `lowres/s300/v533-v592` pages (`v533_260r_300.jpg` re-fetch differs; GAPS210 never recorded its route, so the URL in
their rows is the pattern guess) -- these three groups were restored and are marked in the manifest; their byte-level difference is a
regen-route question, not an image question. `images/regen_images.sh` rewritten: re-fetches every deleted URL-sourced row still missing
(2 s apart, descriptive UA), and `regen_images.sh crop CROP` re-cuts one crop from its source using the box recorded in the manifest
(native-canvas px when the source was fetched with `--region`, else local px; JPEG q85 as iiif_lines.py writes). Debug overlays (23
files, 4.2 MB) are re-derivable by re-running the same iiif_lines.py line with `--debug` but not byte-identically, so they were not
deleted; they are the next candidates if the lane decides a non-identical regen is acceptable for an overlay. `tools/file_shrink_guard.py`
on the manifest and the script: ok. Requests this part: gallica.bnf.fr 7 (regen tests), >= 2 s apart. numpy/PIL are absent in this
container, so iiif_lines.py itself was not run; the crop recipe is documented, not re-executed.

**(2) Souchon 1915 print check for a plain side of the 168 + 296 groups** (one Opus 5.5 text subagent, no vision; Gallica ark
bpt6k935116v). Route: `texteBrut` is altcha-walled (302, twice), but **the ALTO endpoint answers from the cloud**:
`https://gallica.bnf.fr/RequestDigitalElement?O=bpt6k935116v&E=ALTO&Deb=<view>` (HTTP 200 for views 357-361 = printed pp.267-271,
view = page + 90); ContentSearch (43 calls) answered with no challenge. Souchon's Florence section ("4° Lettres de Florence. Années
1743 à 1748. N° 2030 à 2128", pp.267-271) is a calendar: "N° X. Lettre du même, <date>." followed by a one-line regest or a short
clear-text quotation, or by nothing.
- **ff.165r-165v (21 Sept 1743): Souchon p.267, N° 2031**, a bare date line: "N° 2031. Lettre du même, 21 septembre 1743." -- no regest,
  no quotation, no "chiffre" mark. **No printed decipherment or summary.** The red corner number read as 2037 on f.165r is **not**
  Souchon's number for this letter: his N° 2037 is "Lettre du même, 2 novembre 1743. Dans la crainte que l'armée espagnole, poursuivie
  par le Prince de Lobkowitz, ne se jette sur la Toscane, la Régence a décidé la formation d'un camp entre Arezzo et Cortone" (p.267),
  N° 2030 = 7 Sept, 2032 = 28 Sept, 2033-2035 = 5/12/19 Oct, 2036 = 26 Oct (OCR "20 octobre"), 2038 = 9 Nov 1743. So either the red
  numbers are an archival sequence that Souchon's numbering does not follow, or the corner read (1000 px, A3V2-ROUS) is off by
  six; the f.206 = "no. 2047" identification (GF4-BATCH14) rested on p.268's text, not on a red number, and stands. The red-number
  inference in `ciphertext_f165.txt`'s header is corrected below.
- **ff.197v-198r: not identified in Souchon.** Neither anchor phrase ("mande par sa dernière que", "d'autant plus lieu d'y ajouter
  foi") nor the f.165 anchors ("négociation ... entamée entre cette", "M. le Mis Mari a eu ces mêmes avis") occurs in pp.267-271
  (the only "Mari" is the marquis Mari at Calvi, p.274, a later year). Souchon's 1743-44 Florence letters with a regest or quotation:
  7 and 28 Sept, 26 Oct, 2, 9 and 30 Nov, 14 and 28 Dec 1743; 4, 11, 25 Jan, 1 and 8 Feb, 11 Apr, 9 and 16 May, 13 and 20 Jun, 11 Jul,
  1 Aug, 12 Sept 1744; the other 33 letters of the period are date lines only (list in the subagent report, not repeated). If the
  f.197 letter is one of the date-line letters, Souchon gives nothing of it, clear or cipher; its own clear heading on f.197r (not read
  yet) would settle which. Near-miss noted, not the same letter: p.271 N° 2088 (5 Apr 1745) quotes "...y eussent d'abord ajouté
  foi, d'autant plus que le bruit s'est ... répandu ... que M. de Gages vouloit leur capitale pour place d'armes".
- "chiffre"/"chiffré" hits in the volume: p.272 "M. Rota, secrétaire du chifre" (papal), sums of money, the introduction's "dépêches
  chiffrées" being spied on, view 584 "Voici l'énigme du chiffre" (context unread); "déchiffr": 0. None attaches to a Lorenzi passage.
- Consequence: **no plain side in print for either passage**, so the registered f.206 gate stays a non-test on both and is not run
  (the brief's conditional step does not trigger). Internet Archive: no Souchon volume (advancedsearch 2 calls; the one hit is an
  unrelated Rovère/Goupilleau correspondence). Google Books not needed.
- Requests (subagent): gallica.bnf.fr 51 (ContentSearch 43, texteBrut 2 walled, ALTO 5, Pagination 1), all >= 1.6 s apart;
  archive.org 2. Suggestion for the parent (CLAUDE.md hosts table, not edited by this worker): Gallica's ALTO endpoint gives page OCR
  from the cloud when texteBrut is walled.

Not found in: Souchon 1915 pp.267-271 (ALTO full text) for either passage's decipherment, regest or anchor phrase; Internet Archive
(no copy). Rule 10: a search result, no novelty class.

## A3V3-ROUSW-naf14913-rousseau-venice-1743 (4 Oct 2026, account 3 worker for LANE-A3V3)

Job: Remaining gaps next steps (a) native read of two heading/corner lines, (b) 300 px sweep of ff.290r-392v. Route: Gallica IIIF
(`gallica_folio.py` for canvases; native regions `0,0,4733,1600` of canvas 407 and `0,0,4616,1600` of canvas 343, viewed at half size).
- **(a) Native reads (I/M, nothing more).** f.197r (canvas 407): "A Florence le 21. Xbre 1743" -- Xbre read as December (M; the 7bre/Xbre
  month-from-number convention), red corner number **2044**, stamp 197. f.165r (canvas 343): "A Florence le 21. 7bre 1743" (21 Sept 1743,
  read at native resolution, M), red corner number **2031** (not 2037), stamp 165. Consequence: the red corner number on f.165r equals
  Souchon's N° 2031, the same letter A3V2-ROUS2 found as a bare date line; the "2037" in `ciphertext_f165.txt` header and ROUS2's
  "not his numbering or misread" came from the 1000 px read and was a misread. The f.197r letter at corner 2044 is then Souchon-numbered
  (run 2031...2047 is consistent with f.206 = 2047), so its Souchon entry is the next lookup (Souchon 1915 bpt6k935116v, N° 2044, 21 Dec 1743).
  No key, reading or grade changed; ciphertext_f165/f197v headers not edited by this worker.
- **(b) Sweep of ff.290r-392v: canvases 595-800 (206 pages, k=16 run in the manifest), 300 px thumbnails.** Pipeline as GAPS210
  (`align/A3V3-ROUSW_sheets.py`, seed 290): 15 sheets of 18 tiles (14 sweep + 4 controls, random tile ids, mask `align/A3V3-ROUSW_mask.json`
  written before any read), two blind Opus subagent calls (sheets 1-8, 9-15; sheet paths only). Controls: POS-A canvas 424
  (f.205v, full numeral block), POS-B f.266r (numeral lines inside a letter), POS-C f.252r (15 groups with interlinear gloss), NEG canvas 425
  (f.206r, Rousseau's pasted clear slip).
  - **Controls planted 60 (15 sheets x 4), found 60/60**: POS-A, POS-B, POS-C each flagged on all 15 sheets, the slip control flagged
    "slip" on all 15. Caveats: (1) the same four pages recur on every sheet and both readers noticed (blinding of the controls weak, not of
    the sweep tiles, as in GAPS210); (2) the prompt asked for slips, so the f.206r slip was a positive for that category, not a clean-negative
    false-flag test (GAPS210's 0/30 NEG figure is not repeated here); (3) POS-C carries an interlinear gloss but was reported as "numerals",
    so gloss-specific sensitivity is not shown by this control; (4) readers' tile counts: 144/144 and 122/126 (the second reader
    under-counted four tiles; the flags it returned are all accounted for by the mask).
  - **Sweep tiles flagged: 0 numeral-group, 0 slip, 0 gloss.** Five "maybe" rows (canvases 647, 741, 745, 753, 793) looked at by this worker at 300 px:
    647 and 793 ordinary prose; 741 a pasted docket strip at the top; 745 a dark folded/pasted strip over a clear letter; 753 a column
    of figures in the margin that is a small arithmetic sum, not numeral groups (M). None is cipher. Per page: `align/A3V3-ROUSW_sweep_290r-392v.tsv`
    (206 rows, flag none on all).
  - Letters read in passing at thumbnail size are clear Lorenzi/Florence dispatches to Montaigu of 1745-46 (dates seen: 15-25 Jan 1746), M.
- Not found in: ff.290r-392v at 300 px (no numeral-group block, pasted slip or interlinear gloss), with the sensitivity limits above (a short
  block of a few groups, as the control's 15, was detected; one or two numeral groups inside a prose line would not be at 300 px).
  Not searched: canvases 1-14, 593-594, 801-816 (unlabelled).
- Requests: gallica.bnf.fr 211 (206 thumbnails + 3 control thumbnails + 2 native regions), sequential, >= 1.5 s apart, all HTTP 200, no challenge.
  Subagent calls 2 (Opus 5.5 vision, one batch of sheets each). Thumbnails kept in scratchpad, not committed; images/ unchanged.
  Rule 10: no novelty class.

## Remaining gaps (FT4, 3 Oct 2026; revised FT4b, FT4c, FT4d, FT4e, FT4g, FT4h, FT4i, FT4j, FT4k, FT4l, FT4m, FT4n, FT4o, FT4p, FT4q, FT4r, FT4s, FT4t, FT4u, FT4v, FT4w, FT4x, FT4y, FT4z, FT4aa, FT4ab, FT4ac, FT4ad, GAPS204, 3 Oct 2026; A3V2-ROUS, A3V2-ROUS2, 4 Oct 2026)
Read so far: 1 of 5 Rousseau slips matched to its cipher passage (f.206r <-> ff.205v/207r, 62 groups, C 21 M 41); 3 more pairs located (FT4b); f.216v <-> f.217r (79 groups) transcribed and the f.206 key gate PASSed on it (FT4c, H 5 vs p95 3 / 2; 22, 66, 501 second witness; no new code forced); pooled f.206+f.216v gate PASS (FT4d, Hp 23 vs p95 18 / 0): 208 se and 781 e to C, reading C 23 M 39
- f.249r-v <-> f.250r-v pair (111 groups) - blocker: open-codes; transcribed and scored FT4e. Both gates are non-tests: the pair has no repetition-consistent fit (proved with no pins). FT4g eye check confirmed 253, 242 and 66 at all 7 occurrences. The strict-consistency instrument is [retired] for this pair. FT4i one-edit CP-SAT: E 1, with 9 of 223 single edits fitting, all at 253/242/66/52 or a dropped group before groups 26-28; gate NON-INFORMATIVE because the controls timed out (0 resolved draws); FT4j at 60 s: (s) 0 of 3 resolved draws fit, 37 timeouts; (g) not scored (harness time limit); FT4k (g) at 60 s: 28/40 timeouts, 0 of 12 resolved draws fit, gate NON-INFORMATIVE (s 0.925, g 0.700); FT4l amendment (decomposition solver, 75bf2422) not yet run on this pair (box); FT4n under `--dec`: real E 1, (s) 0 of 10 resolved draws fit (draws 0-9), FT4w: (s) complete 16/40 = 0.400, all unresolved, 0 of 24 resolved fit; (g) draws 0-19 7/20 all unresolved, 0 of 13 resolved fit, 20-39 not run (box) -> gate cannot PASS, NON-INFORMATIVE (power); the one-edit gate is [retired] for the FT4l solver on f.249 (third instrument, rule 3); FT4t anchored split (pre-registered 49e1f5a9, anchors 628 hongrie / 279 plus, S = groups 39-100, pins 22/66): real E 1 under 722 = ti and = i, controls ti 1/40, 7/40 and i 6/40, 20/40 -> NON-INFORMATIVE both, 722 undecided; for the 722 question the one-edit family is [retired] on f.249 (untestable at this length), open codes untouched
- f.213r-v <-> f.214r pair (84 groups) - blocker: open-codes; transcribed and scored FT4h (83/84 blind agreement). The strict gate gave H 0 with no fit even without pins (non-test). FT4i one-edit CP-SAT: E 1, with exactly 1 of 169 single edits fitting, W at group 73 (the second 368, f.213v L02); controls 0 of 42 resolved draws fit, but timeouts counted high made the gate NON-INFORMATIVE; FT4j at 60 s: (s) 0/40 with all draws resolved, (g) 16/40 timeouts and 0 of 24 resolved draws fit; still NON-INFORMATIVE by the registered rule; FT4l decomposition solver (75bf2422): (g) 0 of 40, all resolved -> **GATE PASS** (s 0/40, g 0/40, E_real 1); FT4m eye check (pre-registered a9fb0bb8): group 73 reads 368 plainly, no cancel mark (blind Opus, high), and only deleting it gives a no-edit fit, so the pair = slip up to one unmarked extra group (encipherer slip, grade I); FT4n pooled gate (pre-registered 4b43952c) with group 73 dropped: GATE FAIL, real Hp 0 (timed out) vs (a) p95 67; post hoc, f.213 minus group 73 is proved inconsistent with the pin 722 = ti (fits without it), and no single drop fits with all three pins: the f.206 key and this pair disagree beyond one edit; FT4o pinned two-edit scan (pre-registered 3e896b2e; known-answer control 3/3 located): FIT set 13 indices (O3, not located), not at 722 itself (O1 excluded); post hoc the fits cluster on the twice-used codes 63/444/664 and drops at 70-75; FT4p blind eye check (pre-registered 48ba66a1; decoys 6/6): all six 63/444/664 groups read as transcribed, high, no marks (P1) -- the 722 = ti conflict is not a misread there, logged as a key conflict (rule 4); FT4q polyvalence test (pre-registered f5d2e22c): f.213 fits only with 722 = i (ti NOFIT); f.249 fits with 722 = ti and with 722 = i (E 1 both) but the same-length controls are 0.80 and >= 0.60: non-test, f.249 cannot decide at this solver's resolution; f.216v has no 722 (non-test by construction); FT4r: f.266r/f.265r one-edit gate with 722 pinned is unresolved for both values (not scored); FT4s anchored split (pre-registered 2f51d33d): f.266r S1 (groups 0-74, pins 22/66/581) GATE PASS under both 722 = ti and 722 = i (controls 0/40, 0/40 and 1/40, 0/40), both fit with no edit: O3, f.266r cannot decide 722; next: the same anchored split on f.249/f.250 (501 or another count-matched f.206 C anchor, pins, 722 ti vs i on its segment, own (s)/(g) controls), pre-registered, script only, ~$2
- 172 qu'ils vs qu'il - blocker: open-codes; FT4e: 172 = quils forces 208 = e on f.249 against 208's C "se" (0 joint chunks); 172's C grade rests on f.206 alone
- f.274 slip's cipher passage - blocker: not-attempted; FT4h native view: ff.273r-274r are one complete clear Lorenzi letter of 8 Aug 1744, with 0 numeral groups, no slip, no interlinear text, and 274v blank. The finding aid's f.274 pair is not on ff.273-275 as bound; FT4j 1000 px sweep of ff.270-280 (22 pages): clear Lorenzi letters, 25 July-29 Aug 1744, no numerals, no slip; FT4p 300 px sweep of ff.260-269/281-289 (38 pages): **f.265r is a pasted clear-text slip (stamped 265) and f.266r carries ~15 lines of numeral groups** -- a fifth slip+cipher pair, either the aid's "f.274" with its folio off or a slip the aid does not list (I); ff.251v-259v swept at 300 px by FT4u (17 pages): clear Lorenzi letters of June 1744, no slip, but f.252r carries 15 numeral groups with an interlinear clear gloss (sixth pair, no 722; contact-band read only, M); FT4q transcribed the pair: f.266r 171 groups (two blind Opus passes, 171/171 agree), f.265r slip 14 lines (one blind pass + worker reconcile), pairing I (both open "la Republique de Venise" / 52 605 22 739); FT4r one-edit pair gate (pre-registered 8a89e41e, 722 pinned ti / i): real E unresolved for both (62 s / 145 s), NOT SCORED, no controls run; 722 question untouched; FT4s anchored split (pre-registered 2f51d33d, cut at 501 et): S1 = groups 0-74 / slip to "le Bressan" GATE PASS for both 722 values (ti: (s) 0/40, (g) 0/40; i: (s) 1/40, (g) 0/40), pairing for S1 now control-backed, 722 undecided (O3); FT4u (pre-registered 9dbb1bd0): S2 (groups 76-138, pins 22/66/581) GATE PASS (s 0/40, g 0/40) -> 581 2nd witness, 22/66 3rd; S3 (140-170) NON-INFORMATIVE (s 0.175, g 0.075, too short); groups 0-138 control-backed; S3 and the 32 groups 139-170 stay unwitnessed; next: none cheap on this pair beyond the M readout below
- M-graded splits of multi-group stretches (39 tokens) and 336 - blocker: open-codes; FT4d pooled run fixed 208 and 781, left 306/824/444/121/10/420 with 3-15 joint chunks and 338 untied; the third passage (f.249) can fix more once its fit is restored (FT4e); FT4u registered M readout on f.266r S2 (no controls, no grade change): 303/444/347 consistent; 121 ons, 188 lar, 834 kowitz, 344 mee, 24 in, 534 ches proved inconsistent with one edit under the C pins -- six f.206 split values disputed (rule 4); FT4v: f.252r transcribed (2 blind passes, 15/15) and scored: 188 'lar' and 121 'ons' E 0 (absent from the gloss; second dispute each), 10 'a' non-informative, 0 C candidates; FT4x pooled exact pin run (pre-registered 404d0f79): S1 + f.252r J nofit with controls (s) 0/40, (g) 0/40 -> no PASS, a conflict readout; post hoc the conflict is 253 (flagged doubtful read) plus one of 369/213/248; S2 and f.249 segment could not enter (no exact fit / S1+f.249 jointly nofit); FT4y blind eye re-check (pre-registered 3b694072; 7 targets + 7 decoys, 2 Opus vision calls): targets 7/7 as transcribed, decoys 6/7 (one medium doubt, f.252r g0 527/327), outcome P1 -- the conflict is not a misread at those positions; logged as a rule-4 conflict (gloss paraphrase, polyvalence or M split), exact-pooled f.252r test stays a conflict readout; FT4z pooled exact pin run (pre-registered e2ad0f1a): f.206 jointly nofit with f.216v and with S1 (dropped), F216V+S1 J fit, controls (s) 0/40 (g) 0/40 -> GATE PASS, 121 sole feasible chunk s -> key 121 = s at C pending VERIFY (363 sion at I); 188/834/344/24/253 single-block (not testable by pooling), 534 untestable once f.206 dropped; f.206 vs f.216v conflict sits at 338 (sole single release), f.206 vs S1 at no single code; FT4aa pre-registered two-release scan (e7785f6d), controls 0/40 x4 (all at release-all, non-discriminating on specificity): decisive locators F206+F216V {338} sole minimal, F206+S1 {347, 534} sole minimal (also with 121 = s pinned); rule-4 notes on 338/347/534, no value change, pending VERIFY; FT4ab value readout (pre-registered a1f13997, complete enumeration, 121 = s pinned): f.206-side chunks not unique (338: 8, 347: 4, 534: 9; the key values tout/con/ches inside each), partner side unique 338 = tou (f.216v) and 534 = che (S1), 347 12 chunks on S1; no registered VERIFY flag; unregistered secondary: tou and che each nofit in f.206 alone, che nofit in S2 -- the conflict is not a single-code mis-split; FT4ac single-release scan (pre-registered 76666ab0): both arms restore only by freeing 581 (null controls 0/40 x4, but planted unique-located 0.55 < 0.80 -> locator, not control-backed); post hoc the freed 581 is the right-hand neighbour in each arm (tout au / attachés aux), a one-letter boundary or unencoded-letter question, not a wrong row; the exact CP-SAT is [retired] for the f.206 conflict (fifth use, third undecided locating attempt, rule 3); FT4ad blind eye check (pre-registered 83d7821d, 4 targets + 4 decoys, 1 Opus vision call): all 8 read as transcribed, 0 HIGH changes, no mark beyond the separator dot at either boundary -> P1, the boundary is not explained by the image (I), no key change; next: new material only -- a further cipher passage carrying 338 or 534 (none among the transcribed blocks besides f.216v/S1/S2); GAPS210 (4 Oct 2026) found two untranscribed numeral passages, ff.165r-165v and ff.197v-198r (300 px flags, M); next: native fetch + two blind transcription passes of those four pages, then a 338/534/722 count, ~$4
- ff.165r-165v and ff.197v-198r cipher-only passages (168 + 296 groups, transcribed A3V2-ROUS, err_2reader 0.0% / 5.4%) - blocker: not-attempted; no plain side (no slip, no gloss at native resolution), so the registered f.206 gate is a non-test and the coverage secondary (27-33%, the same band as the no-fit pairs f.213/f.249) licenses nothing; next: read Souchon 1915 (Gallica bpt6k935116v, ContentSearch) at no. 2037 (f.165r, 21 Sept 1743) and at the f.197 letter's number for a printed decipherment or summary of the ciphered passage, which would be a C-grade plain side for 464 groups, ~$1.5 -- DONE A3V2-ROUS2 (4 Oct 2026): Souchon prints no decipherment, regest or anchor phrase of either passage (21 Sept 1743 = his N° 2031, a bare date line; his N° 2037 is 2 Nov 1743, so the red corner number is not his numbering or was misread); the f.197 letter is not identified in Souchon; gate stays a non-test. Next: (a) read the clear heading of f.197r and the f.165r corner at native resolution to date the second letter and settle the red-number question (one line crop each, ~$0.3, no transcription); (b) the 300 px sweep of ff.290r-392v (206 pages) for a slip or gloss that could be either passage's plain side, ~$3; a plain side is the only thing that makes the registered gate a test here -- (a) and (b) DONE A3V3-ROUSW (4 Oct 2026); Souchon N° 2044 (f.197r, 21 Dec 1743, p.268) and N° 2031 (f.165r, 21 Sept 1743, p.267) are bare date lines with no regest or decipherment (A3V3-SOU44, 4 Oct 2026; N° 2044 re-read R7-ROUS, 6 Oct 2026), so print gives no plain side. Next: fit check of Hatzenberger 2015 p.326's ambassadeur = 404 at its two f.165 occurrences (ciphertext_f165.txt lines 13 and 19) in context, plus his source note, ~$1; else a plain side only from new material (Montaigu's own deciphered file or a slip outside ff.1r-392v)
- Hatzenberger 2015 read - blocker: waiting-on ASKS row 76; Cairn is DataDome-blocked from the cloud, JSTOR reread stable/24719303 queued (CHECK-NAF) -- R8-ROUS2 (6 Oct 2026): fit check done on disk: his three values do not fit this cipher (République is 605 at 7/7 slip-backed occurrences, 136 absent; 219 and 404 stand on f.249 where the f.250 slip has no Sénat/ambassadeur); still waiting-on ASKS row 76 for his source note, which would say which cipher (likely Montaigu's own with the Court) the values belong to; R8-ROUS3 (6 Oct 2026) registered count-vector gate (PREREG 0ec1ce048): 605 = republique matches (2,1,2,2), unique of all codes, p_s 0.036, p_g 0.034, but the known-answer licence was NOT MET (0/3: de 22, et 501, se 208 all mismatch, function words spread over other groups), so NON-INFORMATIVE; 739 = venise NON-INFORMATIVE (4 tokens, min p 0.08, untestable at this N by this instrument); 52 = la FAIL (f.249/f.250 4 vs 5); no key entry

## Escalation (3 Oct 2026; revised FT4b)
- [x] siblings: (A3V2-ROUS, 4 Oct 2026: ff.165r-165v and ff.197v-198r transcribed at native resolution, 168 + 296 groups, two blind passes each, no slip or gloss on the four pages; ff.290r-392v still not swept) (GAPS210, 4 Oct 2026: ff.1r-205r swept at 300 px, controls 30/30 sheets, numeral passages ff.165r-165v and ff.197v-198r flagged, untranscribed; ff.290r-392v not swept) (FT4p: ff.260-269/281-289 swept at 300 px, slip f.265r + numerals f.266r found) ff.214/217/250/274 slips and facing leaves viewed at 1000 px (FT4b): three cipher+slip pairs found (216v/217r, 249v/250, 213r-v/214r), f.274's not found; FT4h native view of 273r/274r: a clear letter, no numerals
- [x] clear-pages: the f.206r slip is the clear text of this passage, used as the plain side
- [n/a] known-keys: no Lorenzi-Montaigu key table found in Souchon or the solver repositories
- [x] print: Souchon 1915 p.268 prints the clear opening only; phrase searches 0 (GF4-BATCH14) (A3V2-ROUS2, 4 Oct 2026: Souchon pp.267-271 read in full via the ALTO endpoint; the 21 Sept 1743 letter is N° 2031, date line only; no decipherment, regest or anchor phrase of the ff.165 or ff.197 cipher passages anywhere in the Florence calendar; no IA copy) (R8-ROUS2, 6 Oct 2026: f.206r slip phrases on Google Books API, 4 queries, and archive.org be-api, 3 queries plus a positive control at 6,893 hits: no hit for this passage)
- [x] key-rebuild: key.tsv rebuilt from the slip, repetition consistency plus shuffle control, C 21 M 41
- [x] image-check: f.205v, f.206r, f.207r cut and read in two passes, three splits reconciled
- [x] retry: (GAPS204: blind re-check of f.252r g1/5-7 and S1 g39-40/46 [retired], instrument blind Opus vision read of existing crops, 3 looks each already on file (FT4v/FT4q two passes + FT4y), all as transcribed; FT4ab: value readout on the locators, f.206 side not unique, f.216v forces 338 = tou and S1 534 = che, both nofit in f.206 alone, no flag; FT4aa: two-release scan, controls 0/40 x4 (release-all screen only), F206+F216V locator {338}, F206+S1 locator {347, 534}, rule-4 notes, no value change; FT4z: pooled exact f.216v+S1 GATE PASS, controls 0/40 0/40, 121 = s sole chunk, CONFIRMED by VERIFY-ROU121 (seed 11 n 80: 0/80, 0/80; planted ons recovered); f.206 jointly nofit with both; FT4y: blind eye re-check of 7 conflict positions + 7 decoys, 7/7 targets as transcribed, P1, no key change; FT4x: pooled exact pin run S1 + f.252r J nofit, controls 0/40 and 0/40, conflict at 253 + one of 369/213/248 post hoc, no key change; FT4w: f249 one-edit controls under FT4l, (s) 0.400 all unresolved, (g) 0-19 7/20, 0 of 37 resolved fit, gate cannot PASS, [retired] for this solver; FT4v: f.252r pair transcribed, 188/121 disputed (E 0), 10 non-informative, 0 C; FT4u: f.266r S2 GATE PASS (581/22/66 witnesses), S3 non-informative; M readout disputes 6 split values; ff.251v-259v swept, f.252r numerals+gloss found, no 722; FT4t: anchored split of f.249/f.250, both 722 values fit, controls NON-INFORMATIVE (ti 0.175, i 0.500), 722 undecided; f.266r S2/S3 hold no 722; FT4s: anchored split S1 of f.266r/f.265r, GATE PASS under 722 = ti and = i, 722 undecided; FT4r: f.266r/f.265r one-edit gate, 722 ti and i both unresolved, not scored; FT4q: 722 polyvalence test, f.213 needs 722 = i; f.249 non-test, control 0.80) f.206 key scored on f.216v<->f.217r (FT4c PASS, H 5); pooled f.206+f.216v run (FT4d PASS, Hp 23, 208/781 to C); f.249/f.250 scored FT4e as a non-test (pair infeasible as transcribed); FT4g eye check confirmed 253/242/66, and both gates re-run unchanged gave identical results (strict-consistency instrument [retired] for this pair); FT4i one-edit CP-SAT fitter on f.213 and f.249: both fit with one edit (f.213 only at group 73, 368), gate NON-INFORMATIVE (controls timed out); FT4j at 60 s: still NON-INFORMATIVE (f213: 0 of 64 resolved control draws fit; f249 (g) unscored); FT4k f249 (g) at 60 s: 0 of 12 resolved fit, gate NON-INFORMATIVE (0 of 79 resolved control draws fit across both pairs); FT4l decomposition solver: f213 (g) 0/40 all resolved, f213 one-edit gate PASS; FT4m eye check: the one edit is an unmarked extra 368 (f.213v L02); ff.270-280 swept, no f.274 pair; FT4n: f.213 drop-73 pooled gate FAIL (722 ti pin conflict, no single drop fits pinned), f249 FT4l controls 10 of 80 draws run, 0 fits, not scored; FT4o pinned two-edit scan on f.213: 13 locations fit (not located), none at 722
Verdict: keep going: 6 internal gaps; cheapest next: a verifier pass on 605 = republique (R9-ROUS4 key row, count-level C, pending VERIFY), then new material (a fifth slip-backed pair) for 739 = venise, which the count-vector instrument cannot test at this N (planted class recovery 13/40), ~$1.5 -- R9-ROUS4 (6 Oct 2026): re-registered gate (PREREG c962e56e5) with a same-class planted known-answer: 605 PASS (p_s 0.036, p_g 0.034; class 37/40 >= 32), entered key.tsv at C pending VERIFY, reading unchanged (605 is not in the decoded f.205v/207r passage); 739 NON-INFORMATIVE (p 0.085/0.079; class 13/40). Earlier: keep going: 6 internal gaps; cheapest next: a re-registered count-vector run whose known-answer control is of the candidates' own class (a synthetic plant of one rare whole-word code at 605's count profile into the four real passages and slips, to show the gate can recover it), then 605 = republique at C if it passes; 739 and 52 are not testable this way at this N; ~$1 -- else new material (a fifth slip-backed pair). R8-ROUS3 (6 Oct 2026): the registered gate ran; 605 MATCH unique p 0.036/0.034 but licence not met (known-answer 0/3), NON-INFORMATIVE; 739 NON-INFORMATIVE; 52 FAIL; no key change. Earlier: keep going: 6 internal gaps; cheapest next: a registered count-vector gate over the four slip-backed pairs (f.213/214, f.216v/217, f.249/250, f.266r/265) for whole-word codes, starting with 605 = république (R8-ROUS2: 1 of 195 codes matches the slips' vector 2,1,2,2) and 739 = venise, 52 = la, with a shuffle control, before any key.tsv entry, ~$1.5 -- R8-ROUS2 (6 Oct 2026): Hatzenberger 2015 p.326's 136/219/404 fit check done, contradicted for this cipher; f.206r phrase search on Google Books API and archive.org be-api 0 hits. Earlier: keep going: 6 internal gaps; cheapest next: fit check of Hatzenberger 2015 p.326's ambassadeur = 404 at its two f.165 occurrences (and Sénat = 219 once on f.249) in context, plus his source note, ~$1 -- R7-ROUS (6 Oct 2026): the Souchon N° 2044 / N° 2031 check was already done by A3V3-SOU44 (4 Oct 2026, both bare date lines, no plain side in print); N° 2044 re-read on p.268 (ALTO view 358) and confirmed, no 'chiffr' on the page -- A3V3-ROUSW (4 Oct 2026): f.197r read 21 Xbre 1743 corner 2044, f.165r 21 7bre 1743 corner 2031 (matches Souchon N° 2031; the earlier 2037 was a misread); ff.290r-392v swept at 300 px, controls 60/60 planted/found, no numeral block, slip or gloss on any of the 206 pages -- A3V2-ROUS2 (4 Oct 2026): Souchon 1915 pp.267-271 read in full (ALTO): no plain side in print for either passage, 21 Sept 1743 is Souchon N° 2031 not 2037, f.197 letter unidentified; images/ shrunk 34.76 -> 29.13 MB (57 URL-regenerable files deleted after byte-identical class samples, full-folder manifest + regen script; f252r src, v424 and the 38 GAPS210 s300 pages kept because their re-fetch is not byte-identical; the 23 debug overlays, 4.2 MB, are the next shrink candidates and need a lane decision since their regen is not byte-identical). Earlier: A3V2-ROUS (4 Oct 2026): ff.165r-165v (168 groups) and ff.197v-198r (296 groups) transcribed, 0.0% / 5.4% two-reader disagreement, no plain side, registered gate non-test on both, coverage secondary in the same 27-33% band as the no-fit pairs (licenses nothing), 338 x2 / 534 x0 / 722 x1, no key change. Earlier: GAPS210 (4 Oct 2026): 300 px sweep of ff.1r-205r, controls 30/30 sheets, two passages flagged. Earlier: FT4ad (3 Oct 2026): the blind eye check of f.206 groups 21-22 (534 581) and 35-36 (338 581) read all 4 targets and 4 decoys as transcribed with no mark beyond the separator dot (P1), so the one-letter boundary FT4ac located is not a visible correction; the exact CP-SAT stays [retired] for the f.206 conflict (rule 3); 121 = s stays C (VERIFY-ROU121); the other disputed f.206 splits (188, 834, 344, 24) and 253 occur in one no-edit passage only and need new material; the f.249 one-edit gate stays [retired]; the 722 conflict otherwise needs new material beyond ff.251v-289v (none found there). GAPS204 (3 Oct 2026): the f.252r g1/5-7 + S1 g39-40/46 blind re-check is [retired] (rule 3, three blind looks each on file, all as transcribed); not re-briefed without a different instrument.

Checks (FT4, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743:
keep going: 2 internal gap(s), 2 step(s) untried", exit 0. `python3 tools/intake_gate_check.py naf14913-rousseau-venice-1743` ->
"partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0. `python3 tools/decode_key.py
ciphers/naf14913-rousseau-venice-1743 --check` -> "reading up to date", exit 0. Status open -> partial (one passage read at C/M).

Checks (FT4b, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743:
keep going: 4 internal gap(s), 1 step(s) untried", exit 0. `python3 tools/intake_gate_check.py naf14913-rousseau-venice-1743` ->
"partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0. Status stays partial; no reading changed.

Checks (FT4c, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743:
keep going: 4 internal gap(s), 1 step(s) untried", exit 0. `python3 tools/intake_gate_check.py naf14913-rousseau-venice-1743` ->
"partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0. `python3 tools/decode_key.py
ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 21, M 41 / reading up to date", exit 0. Status stays partial.

Checks (FT4d, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 3 internal gap(s), 1 step(s) untried", exit 0; `python3 tools/intake_gate_check.py
naf14913-rousseau-venice-1743` -> "partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0.
`python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.

Checks (FT4e, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 1 step(s) untried", exit 0; `python3 tools/intake_gate_check.py
naf14913-rousseau-venice-1743` -> "partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0.
`python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.

Checks (FT4g, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0;
`python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.

Checks (FT4h, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0;
`python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.

Checks (FT4i, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0;
`python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.

Checks (FT4j, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0;
`python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.

Checks (FT4k, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0;
`python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.

Checks (FT4l, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0;
`python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.

Checks (FT4n, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0; `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.
Checks (FT4o, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0; `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.
Checks (FT4p, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0; `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.
Checks (FT4q, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0; `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.
Checks (FT4r, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0; `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.

Checks (FT4s, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0;
`python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.

Checks (FT4t, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743:
keep going: 5 internal gap(s), 0 step(s) untried", exit 0; `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` ->
"tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.
Checks (FT4w, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0; `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.
Checks (FT4x, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0; `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 23, M 39 / reading up to date", exit 0. Status stays partial.
Checks (FT4z, 3 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 5 internal gap(s), 0 step(s) untried", exit 0; `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 24, I 1, M 37 / reading up to date", exit 0. Status stays partial.
Checks (FT4aa, 3 Oct 2026): gaps_check exit 0 (OK keep-going, 5 internal gaps, 0 untried); decode_key --check exit 0 (tokens 62: C 24, I 1, M 37). Status stays partial.
Checks (FT4ab, 3 Oct 2026): gaps_check exit 0 (OK keep-going, 5 internal gaps, 0 untried); decode_key --check exit 0 (tokens 62: C 24, I 1, M 37). Status stays partial.
Checks (GAPS210, 4 Oct 2026): gaps_check exit 0 (OK keep-going, 5 internal gaps, 0 untried); decode_key --check exit 0 (reading up to date). Status stays partial.
Checks (A3V2-ROUS, 4 Oct 2026): `python3 tools/gaps_check.py naf14913-rousseau-venice-1743` -> "OK keep-going naf14913-rousseau-venice-1743: keep going: 6 internal gap(s), 0 step(s) untried", exit 0; `python3 tools/intake_gate_check.py naf14913-rousseau-venice-1743` -> "partial (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0; `python3 tools/decode_key.py ciphers/naf14913-rousseau-venice-1743 --check` -> "tokens 62: C 24, I 1, M 37 / reading up to date", exit 0 (key.tsv and reading untouched). Status stays partial.

## A3V3-SOU44-naf14913-rousseau-venice-1743 (4 Oct 2026, account 3 worker for LANE-A3V3)

Souchon 1915 (Gallica bpt6k935116v), ALTO endpoint `RequestDigitalElement?O=bpt6k935116v&E=ALTO&Deb=<view>`, views 357 and 358
(printed pp.267 and 268, view = page + 90), OCR text read directly, 2 requests, 2 s apart.
- **N° 2044 (the f.197r letter, corner 2044, "21 Xbre 1743"): p.268, a bare date line.** OCR: "N° 2044. Lettre du même, 21 décembre
  1743. — N° 2045. Lettre du même, 28 décembre 1743. L'envoyé lucquois va partir sans avoir réussi dans sa mission." The regest
  after 2045 belongs to 2045 (28 Dec), not 2044; the regest before it (p.267-268, "14 décembre 1743. La République de Lucques a
  envoyé ...") belongs to the 14 Dec letter (N° 2043). No quotation, no regest, no "chiffre" mark, no anchor phrase for f.197v-198r.
- **N° 2031 (f.165r, "21 7bre 1743"): p.267, a bare date line**, re-checked: "N° 2031. Lettre du même, 21 septembre 1743." Same as
  A3V2-ROUS2. Neighbouring lines (2030, 2032) carry no text bearing on the passages either.
- **Consequence:** no printed plain side exists for either ciphered passage (ff.165r-v, 168 groups; ff.197v-198r, 296 groups), so no
  group can be covered by a C-grade plain text from Souchon; the registered gate stays a non-test on both and was not run.
  Correction of an earlier line: the f.197 letter is now identified in Souchon (N° 2044), but as a date line only (A3V2-ROUS2 had
  "not identified").
Not found in: Souchon 1915 pp.267-268 at N° 2031 and N° 2044 (ALTO text, 4 Oct 2026). Rule 10: a search result, no novelty class.
Next (unchanged, needs new material): a plain side only from the recipient's archive copy (Montaigu's own deciphered file) or an
unprinted Lorenzi/Rousseau slip outside ff.1r-392v; ask-row candidate, not queued by this worker.
Checks (A3V3-SOU44, 4 Oct 2026): gaps_check run below.

## JSTOR runner, 4 Oct 2026

read 4 Oct 2026 (page viewer, no download), Hatzenberger 2015 https://www.jstor.org/stable/24719303: p.325 quotes Confessions VII (n.: p.349) on Rousseau deciphering the backlog ("en moins de huit jours j'eus déchiffré le tout"); p.326 states that in the diplomatic cipher "« République » s'écrivait « 136 », « Sénat » était retranscrit par « 219 » et « ambassadeur » par « 404 »" (source note not captured); p.329 "il chiffre et déchiffre"; pp.338-339 quote passages "chiffré par Rousseau" in deciphered form: letter to Amelot 29 Feb 1744 (n.53 DV p.1144), dispatch to the King 23 May 1744 "passage codé" (n.54 DV p.1195), letter to Amelot 9 Nov 1743 "un long paragraphe entièrement chiffré" (n.55 DV p.1069). Edition: "DV" pages in the 1000s with Candaux's introduction (n.17 "Candaux, p. ccxlix") -- i.e. the Pléiade Œuvres complètes III edition; full bibliographic note not viewed

## Lead from the JSTOR read (5 Oct 2026 03:30 UTC, account-3 orchestrator)

Hatzenberger 2015 p.326 gives three code values for the embassy's diplomatic cipher: République 136, Sénat 219,
ambassadeur 404 (his source note not captured). None is in key.tsv. Grep of ciphertext*.txt: 136 occurs 0 times, 219 once,
404 twice. Untested: whether "Sénat"/"ambassadeur" fit those positions in context, and which cipher Hatzenberger means
(Montaigu's own or the Foreign Ministry's). Next: a small fit check of the 3 occurrences against the reading (~$1), and
the source of Hatzenberger's note (DV, Pléiade III, ILL list item 13). Not applied to the key.

## R7-ROUS-naf14913-rousseau-venice-1743 (6 Oct 2026, account 2 worker for LANE-RUN7-account-2)

Brief: read Souchon 1915 at N° 2044 (f.197r letter) and N° 2031 (f.165r letter) for a printed plain side. Finding: this check was
already made by A3V3-SOU44 (4 Oct 2026, section above); the Verdict line had not been updated, so the lane re-briefed it.
- Re-read N° 2044: Souchon 1915 (Gallica bpt6k935116v) ALTO view 358 = printed p.268: "N° 2044. Lettre du même, 21 décembre 1743."
  followed directly by N° 2045 (28 Dec, its own regest on the Lucca envoy). The regest above it (14 Dec, Lucca's ambassador at Florence)
  belongs to N° 2043. No quotation, no regest, no occurrence of "chiffr" anywhere on p.268. Agrees with A3V3-SOU44.
- N° 2031 (p.267, ALTO view 357): the fetch answered HTTP 429; per the good-citizen rule the host was not retried. Not re-read this
  job; the bare date line rests on A3V2-ROUS2 and A3V3-SOU44 (two reads, 4 Oct 2026).
- Result: no printed plain side for ff.165r-v (168 groups) or ff.197v-198r (296 groups) in Souchon; no crib; nothing to align.
- Next named instead: Hatzenberger 2015 p.326 gives ambassadeur = 404, and 404 occurs twice in ciphertext_f165.txt (lines 13, 19) and
  Sénat = 219 once in ciphertext_f249.txt; a fit check in context plus his source note, ~$1 (gap line and Verdict updated).
Not found in: Souchon 1915 p.268 (N° 2044), ALTO text, 6 Oct 2026. Rule 10: a search result, no novelty class.
Requests: gallica.bnf.fr 2 (view 357 HTTP 429, view 358 HTTP 200), 2 s apart; host stopped after the 429. Key and reading untouched.
Checks (R7-ROUS, 6 Oct 2026): gaps_check exit 0 (OK keep-going, 6 internal gaps, 0 untried); decode_key --check exit 0 (reading up to date); file_shrink_guard ok. Status stays partial.

## R8-ROUS2-naf14913-rousseau-venice-1743 (6 Oct 2026, account 2 worker for LANE-RUN8-account-2)

Brief: fit check of Hatzenberger 2015 p.326's values (République 136, Sénat 219, ambassadeur 404) against the transcriptions on disk, then
the f.206r phrase search. Pre-registration `align/PREREG-R8-ROUS2.md` pushed (34dbf54aa) before the run; script `align/r8rous2_fit.py`,
output `align/r8rous2_fit.out`.
Checks (R8-ROUS2, 6 Oct 2026): gaps_check exit 0 (OK keep-going, 6 internal gaps, 0 untried); decode_key --check exit 0 (reading up to date).
- **Count correction.** 404 occurs once on ff.165r-v (f165v L02, group 48), not twice: the second "occurrence" in the 5 Oct lead was the
  header comment of `ciphertext_f165.txt`. 404 also occurs once on f.249 (Lv1 g1); 219 once on f.249 (Lv3 g12); 136 nowhere on disk.
- **République.** Over the four slip-backed pairs (f.213/f.214r, f.216v/f.217r, f.249/f.250, f.266r/f.265r) the slips write République
  2, 1, 2, 2 times. Exactly one code of the 195 that occur in those passages has the same count vector: **605** (2, 1, 2, 2); 136 has
  0, 0, 0, 0. Chance-match control: 1 of 195 codes for this vector. 605 also stands in "52 605 22 739" (la République de Venise) on
  f.165r L02, f.197v, f.213, f.249, and "52 605 24 311 14" on f.165v L05. Grade for 605 = république: I (count-level, not aligned per
  token, not entered in key.tsv this job). Hatzenberger's 136 is contradicted for the Lorenzi-Montaigu cipher.
- **Sénat 219, ambassadeur 404.** The f.250 slip (period decipherment of ff.249r-v) contains neither word, yet 219 and 404 each occur once
  in the f.249 groups (219 inside "...208 242 219 70 405 114..." six groups before 279 = plus (C), where the slip runs "qui se pourront derober le plus"; 404 at the head
  of f.249v where the slip runs about "desesperoit neantmoins d'y pouvoir reussir"). Both values contradicted on f.249. On f.165v
  (no plain side) 404 stands in "420 268 121 63 506 [404] 14 168 114 501 715": context alone cannot grade it; no grade given.
- **Reading of the result.** Hatzenberger's values most likely come from a different table (Montaigu's own cipher with the Court, which
  Rousseau ciphered and deciphered as secretary), not from Lorenzi's letters to Montaigu; inferred (I), to be settled by his source note
  (ASKS row 76, JSTOR stable/24719303 reread). Key source of his values: `published` (Hatzenberger 2015), grade for this cipher: none.
- **Phrase search, f.206r slip.** Google Books API (key + country=US), 4 quoted phrases ("venitiens en faveur de la Reine de Hongrie",
  "auroient tout au plus continué", "provisions a l armée de M. le Prince de Lobkowitz", "les plus attachés aux intérets de cette
  princesse"): top-10 snippets are scattered-word matches only (Burchard's Diarium, Histoire de Venise, Biographie universelle on
  Lobkowitz 1742, Sophie of Hanover), no hit for this passage. archive.org be-api full-text search, 3 quoted phrases: 0 hits each;
  positive control "en moins de huit jours" 6,893 hits, so the route answers quoted phrases.
Not found in: Google Books API (4 queries) and archive.org be-api full text (3 queries), 6 Oct 2026. Rule 10: a search result, no
novelty class.
Requests: www.googleapis.com 4, be-api.us.archive.org 4, each 2 s apart, all HTTP 200. Key and reading untouched.

## R8-ROUS3-naf14913-rousseau-venice-1743 (6 Oct 2026, account 2 worker for LANE-RUN8-account-2)

Brief: a registered count-vector gate over the four slip-backed pairs for whole-word codes, 605 = republique, 739 = venise, 52 = la, with a
shuffle control, before any key.tsv entry. Pre-registration `align/PREREG-R8-ROUS3.md` pushed (0ec1ce048) before the run; script
`align/r8rous3_countgate.py`, output `align/r8rous3_countgate.out` (2000 draws per control, seed 8, disk only).
- Statistic: per candidate, the code's count vector over the four passages (84, 79, 111, 171 groups) against the word's count vector over
  the four slips (57, 52, 72, 102 tokens; "la reine" merged per 31 = la reine, C). Controls: (s) slip tokens redealt across pairs,
  (g) cipher groups redealt across pairs -- both can break or create the match. Known-answer: C whole-word values with >= 3 slip tokens.
- **Known-answer control: 0 of 3 recovered** -> licence NOT MET. 22 de (3,3,5,7) vs (4,3,6,7); 501 et (1,1,0,2) vs (0,1,0,2); 208 se
  (0,1,4,0) vs (0,1,2,0). The only eligible C values are short function words, which the cipher also writes inside other groups or as
  syllables, so they cannot match exactly; the control was of the wrong class to show power for a long rare word (stated post hoc).
- 605 = republique: code (2,1,2,2) = word (2,1,2,2), the only code with that vector, p_s 0.036, p_g 0.034; per pair 2/2, 1/1, 2/2, 2/2.
  Would PASS on its own numbers; registered verdict **NON-INFORMATIVE** (licence not met). No key entry; stays I (R8-ROUS2).
- 739 = venise: (1,1,1,1) both, unique, p_s 0.085, p_g 0.079: **NON-INFORMATIVE**; four single tokens cannot reach p <= 0.05 under
  these controls, so untestable at this N by this instrument.
- 52 = la: code (4,1,4,3), word (4,1,5,3): **FAIL** (the f.249/f.250 pair has one more "la" than 52s; 3 of 4 pairs match).
- Secondary scan (no key entry): 20 slip words with >= 3 tokens, 6 with a unique exact code match; none under the Bonferroni threshold
  0.05/6 (best 689 = des, p 0.032/0.025). Note (M, unregistered): 501's vector matches "un" (1,1,0,2) exactly, not "et" (0,1,0,2);
  506 matches both "dans" and "en". Logged for a verifier as a rule-4 observation on 501 (C et), no value change.
- Per-unit (rule 3): every primary candidate's match is spread over all four pairs (no 0/0 pair for 605, 739, 52), so no single pair
  carries the match.
Checks (R8-ROUS3, 6 Oct 2026): decode_key --check exit 0 (key and reading untouched); gaps_check exit 0 (OK keep-going, 6 internal gaps, 0 untried).
Requests: none (disk only).

## R9-ROUSV-naf14913-rousseau-venice-1743 (6 Oct 2026, account 2 verifier for LANE-RUN9-account-2)

Brief: verify R8-ROUS3's unregistered note that 501 (C "et") has the count vector (1,1,0,2) of "un", not "et" (0,1,0,2). Disk only,
no new cryptanalysis: each slip-backed 501 read against its slip transcription and its cipher neighbours (verifier, not the solver).
Slip-backed occurrences of 501: 7 (f.206r 2, f.213 1, f.216v 1, f.249 0, f.266r 2; ff.165/197v have no plain side, not counted).
| Pair | 501 in context | Slip at that point | Verdict |
|---|---|---|---|
| f.205v-207r / f.206r | 628 **501** 715 | "Hongrie et particulierement" (628 = hongrie, C) | et, as before |
| f.205v-207r / f.206r | 208 **501** 172 | "cette princesse et qu'ils" (172 = quils, C) | et, as before |
| f.216v / f.217r L06 | 536 **501** 63 242 | "quelque parti et que pour" | et (63 = que by context only, I) |
| f.266r / f.265r L08 | 582 **501** 755 663 | "le Bressan et le Bergamasc" | et (755 = le by context only, I) |
| f.266r / f.265r L13 | 121 **501** 22 753 22 | "audits confins et de faire de" (121 = s, 22 = de, C; 22 753 = "de faire" also in L11 "dans la disposition de faire") | et |
| f.213 / f.214r L01v | 46 / **501** 781 664 746 317 755 552 22 95 | "ont ete cedes par le Traite de Worms" (781 = e, C; 746 = des, M; 317 = par fits both "317 52" = "Par la" / "par la meme") | "et" as the syllable of été: 501 781 664 746 = et-e-ce-des |
- Every one of the 7 is consistent with 501 = et; 6 are the word "et", 1 (f.213) the letters et inside "été". No occurrence is
  better read "un": f.214r's single "un" ("y trouveroit un autre avantage") stands about ten words before "ete cedes"; on f.217r and
  f.265r the slips' "un" and "et" counts are equal (1/1, 2/2), so those pairs cannot tell the two apart.
- Why the count vector says "un": R8-ROUS3's statistic counts whole slip words, and the only pair where "et" and "un" counts differ is
  f.213/f.214r, where 501 enciphers a syllable, not a word. The match is an artefact of whole-word counting (the same cause R8-ROUS3
  gave post hoc for its known-answer 0/3), not a second witness for "un". No data conflict under rule 4 (no two witnesses disagree).
- Grade: 501 = et stays C (f.206r slip as known plaintext; consistent at all 7 slip-backed occurrences). key.tsv, reading.txt untouched;
  no AUDIT.md exists for this folder and SECOND-OPINIONS-QUEUE.tsv has no row for it (0 rows, grep 6 Oct 2026), so nothing to propagate.
  The context values 63 = que, 755 = le, 317 = par are noted at I only, not entered in key.tsv (not this job's brief).
Checks (R9-ROUSV, 6 Oct 2026): decode_key --check exit 0; gaps_check exit 0 (keep-going); file_shrink_guard ok. Requests: none (disk only).

## R9-ROUS4-naf14913-rousseau-venice-1743 (6 Oct 2026, account 2 worker for LANE-RUN9-account-2)

Brief: re-run R8-ROUS3's count-vector gate with known-answer controls of the candidates' own class, so the licence can be met. Pre-run
listing (slip words of >= 5 letters with 4-8 tokens over the four slips): only republique and venise, the candidates themselves, so no
real same-class known answer exists on disk; a planted one was registered instead. Pre-registration `align/PREREG-R9-ROUS4.md` pushed
(c962e56e5) before the run; script `align/r9rous4_plantgate.py` (imports R8-ROUS3's units, normalisation and controls), output
`align/r9rous4_plantgate.out`.
- Planted known-answer: per candidate, 40 plants (seed 9) of a synthetic word into the slips and a synthetic code over random
  non-protected groups of the passages, vector drawn from the candidate's class (every pair 1..3, total within +/- 1 of the candidate's);
  full gate re-run per plant with fresh 2000-draw (s) and (g) controls. Recovery can fail on the plant's own vector, on uniqueness after
  planting, and on the redealt pools, so it is not a copy of the candidate's numbers (rule 3).
- **605 = republique: PASS.** Candidate (unplanted, seed 8, reproduces R8-ROUS3): code (2,1,2,2) = word (2,1,2,2), unique, p_s 0.036,
  p_g 0.034. Class (totals 6-8, 45 vectors): 37/40 plants recovered (licence 32/40 MET). The three misses: two at (1,1,1,3) with p
  0.056-0.064, one at (2,1,2,2) not unique because 605 itself already holds that vector.
- **739 = venise: NON-INFORMATIVE.** p_s 0.085, p_g 0.079; class (totals 4-5): 13/40 recovered, licence NOT MET. Untestable by this
  instrument at this N.
- Key: 605 = republique entered in key.tsv at C (period slip as known plaintext, count-level, not aligned per token; note "pending
  VERIFY"). reading.txt unchanged: 605 does not occur in the decoded f.205v/207r passage (decode_key: tokens 62, C 24, I 1, M 37, as
  before). It now gives "52 605 22 739" on f.165r, f.197v, f.213, f.249 the reading "la republique de [739]" where those passages are
  decoded. ROOM flag for a verifier. Key 501 untouched. 739 and 52 not entered.
- Limits: the plant models a whole-word code written at every occurrence; a word sometimes spelled out is a MATCH failure, which the
  gate reports as FAIL, not PASS. The class-recovery figure is power for a true value of this count profile, not evidence that 605 is
  the value; the evidence is the candidate's own unique vector and its two shuffle p-values.
Checks (R9-ROUS4, 6 Oct 2026): decode_key --check exit 0; gaps_check exit 0 (OK keep-going, 6 internal gaps, 0 untried).
Requests: none (disk only).
