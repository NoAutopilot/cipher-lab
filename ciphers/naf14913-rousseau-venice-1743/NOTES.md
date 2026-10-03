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

## Remaining gaps (FT4, 3 Oct 2026; revised FT4b, FT4c, FT4d, FT4e, FT4g, 3 Oct 2026)
Read so far: 1 of 5 Rousseau slips matched to its cipher passage (f.206r <-> ff.205v/207r, 62 groups, C 21 M 41); 3 more pairs located (FT4b); f.216v <-> f.217r (79 groups) transcribed and the f.206 key gate PASSed on it (FT4c, H 5 vs p95 3 / 2; 22, 66, 501 second witness; no new code forced); pooled f.206+f.216v gate PASS (FT4d, Hp 23 vs p95 18 / 0): 208 se and 781 e to C, reading C 23 M 39
- f.249r-v <-> f.250r-v pair (111 groups) - blocker: open-codes; transcribed and scored FT4e. Both gates are non-tests: the pair has no repetition-consistent fit (proved with no pins). FT4g eye check confirmed 253, 242 and 66 at all 7 occurrences (2 blind passes + reconciliation). Both gates re-run unchanged gave identical results (H 0 proved, Hp 0). The strict-consistency instrument is [retired] for this pair; next: a one-edit/one-polyvalent-code alignment with a control that can differ, script only, ~$1.5
- f.213v(+213r?) <-> f.214r pair (about 30+ groups) - blocker: not-attempted; located FT4b; next: transcription + gate_pair.py, ~$3
- 172 qu'ils vs qu'il - blocker: open-codes; FT4e: 172 = quils forces 208 = e on f.249 against 208's C "se" (0 joint chunks); 172's C grade rests on f.206 alone
- f.274 slip's cipher passage - blocker: not-attempted; not on 273v/274r/274v/275r at 1000 px (FT4b); next: view 273r and 274r at native resolution for a pasted slip, ~$0.5
- M-graded splits of multi-group stretches (39 tokens) and 336 - blocker: open-codes; FT4d pooled run fixed 208 and 781, left 306/824/444/121/10/420 with 3-15 joint chunks and 338 untied; the third passage (f.249) can fix more once its fit is restored (FT4e)
- Hatzenberger 2015 read - blocker: waiting-on ASKS row 76; Cairn is DataDome-blocked from the cloud, JSTOR reread stable/24719303 queued (CHECK-NAF)

## Escalation (3 Oct 2026; revised FT4b)
- [x] siblings: ff.214/217/250/274 slips and facing leaves viewed at 1000 px (FT4b): three cipher+slip pairs found (216v/217r, 249v/250, 213v/214r), f.274's not found
- [x] clear-pages: the f.206r slip is the clear text of this passage, used as the plain side
- [n/a] known-keys: no Lorenzi-Montaigu key table found in Souchon or the solver repositories
- [x] print: Souchon 1915 p.268 prints the clear opening only; phrase searches 0 (GF4-BATCH14)
- [x] key-rebuild: key.tsv rebuilt from the slip, repetition consistency plus shuffle control, C 21 M 41
- [x] image-check: f.205v, f.206r, f.207r cut and read in two passes, three splits reconciled
- [x] retry: f.206 key scored on f.216v<->f.217r (FT4c PASS, H 5); pooled f.206+f.216v run (FT4d PASS, Hp 23, 208/781 to C); f.249/f.250 scored FT4e as a non-test (pair infeasible as transcribed); FT4g eye check confirmed 253/242/66, and both gates re-run unchanged gave identical results (strict-consistency instrument [retired] for this pair)
Verdict: keep going: 5 internal gaps; cheapest next: view f.273r and f.274r at native resolution for the f.274 slip's pasted cipher passage, ~$0.5 (then f.213v/214r transcription + gate_pair.py, ~$3; f.249 relaxed alignment, ~$1.5)

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
