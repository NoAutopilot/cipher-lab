open
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

Next step that depends on nobody: view ff.214, 217, 250, 274 and their facing leaves (Gallica btv1b525174513, IIIF, free) to
list which Lorenzi/Castellane cipher passages each Rousseau slip renders, and match them to Souchon's numbers (pp.257-275);
about $0.5, image check only, no transcription. (The JSTOR reread of Hatzenberger 2015, ASKS 76, and LOCAL-QUEUE L25 stay
where they are.)

Gate re-run (GF4-BATCH14, 3 Oct 2026): `python3 tools/intake_gate_check.py naf14913-rousseau-venice-1743` -> "naf14913-rousseau-venice-1743: open (line 1) -- edition/page or full-text-search citation found within 6 lines", exit 0 (was exit 1, no standard-edition citation). `python3 tools/next_steps.py --wait-only | grep naf14913-rousseau-venice-1743` -> no line.
