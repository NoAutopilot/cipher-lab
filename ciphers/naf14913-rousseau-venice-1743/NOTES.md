status: open

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
