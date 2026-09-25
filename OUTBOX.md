# Outbox — everything blocked on the owner, in one sitting

Written 25 Sept 2026 22:42 UTC (parent worker OUTBOX), consolidating every `open` row in `ASKS.md`, every
`queued` row in `JSTOR-QUEUE.tsv` and `LOCAL-QUEUE.tsv`, and the drafts they cite. Nothing here invents a fact:
every folio, reference and cost is copied from the target's own `REQUEST.md`/`NOTES.md`/`AUDIT.md` or from
`ASKS.md` itself. Sign-offs are left as `[owner's name]`; recipient addresses that were not independently
confirmed say so.

---

## 1. One local runner session

Start one Claude Code session on your own computer — Claude Desktop, or `claude remote-control` in a clone of
this repo (full one-time setup in `tools/local_runner_brief.md`) — logged into JSTOR, HathiTrust, DECODE,
archive.org and Google Books in its `.runner-profile` browser. Give it this as your first message, then type
`/loop 20m` so it repeats every twenty minutes while your machine is on:

> You are the cipher-lab local + JSTOR runner on my computer. Read CLAUDE.md rule 10 and the good-citizen rule,
> then read `tools/local_runner_brief.md` and `tools/jstor_runner_brief.md` in full and follow both. Work
> through every row with status `queued` in `LOCAL-QUEUE.tsv` **except L7** (a cloud worker is already
> borrowing that item — see OUTBOX.md §5), then every row with status `queued` in `JSTOR-QUEUE.tsv`, one at a
> time, a few seconds apart, in the `.runner-profile` browser; stop on any block page and write it down rather
> than retrying. Commit and push each result by explicit path as you go (never `git add -A`); append a
> `ROOM.md` line with `tools/room.py` when you start and when you stop. Never bypass a challenge, never print a
> password or my name, never call a reading new/first/unpublished. Stop when no `queued` row is left that you
> can do, and tell me what's left and why.

**What it covers — LOCAL-QUEUE.tsv (12 rows, L7 excluded, see §5):**

| id | target | what it does |
|---|---|---|
| L3 | fr2980-gramont | HathiTrust full-text search for three AUDIT.md phrases + "Gramont Villandry 1530" |
| L4 | eckert-1864 | HathiTrust full-text search for the E4/E5 telegram phrases |
| L5 | fr2980-gramont | Read Camusat 1619 and Champollion-Figeac 1847 in full via Gallica's texteBrut endpoint |
| L8 | fr4687-paleologue-nevers | Read Ferrari 1999 (academia.edu) for Marguerite Paleologue's ciphered letters |
| L9 | fr16092-maisse-1582 | Check Boucher's *Lettres de Henri III* vols V-VI for a decipherment note |
| L10 | antt-linhares-chave | Read the two Banco de Portugal OCPEP-7 volumes for the Linhares cipher letter |
| L11 | clairambault1225-paget-1714 | AN Marine sous-série B7 inventory, 1714-16 Paget items, digitisation status |
| L12 | oldenbarnevelt-brederode-1605 | Read Megyesi et al. 2022 (Cryptologia) for a Dutch 1600-1610 key |
| L13 | catokwacopa-1875 | Verify the working transcription against the original BNA newspaper scans |
| L14 | sp53-16-78 / sp53-16-79 | HathiTrust pp.211-212 of Boyd's Calendar vol.8 — deciphered or still in cipher? |
| L15 | specs/powers-1991.json | Read Thomas 2006 for a completed name-by-name key to the 32 triplets |
| L16 | pro3055-clinton-1779 | Google Books search-inside (logged-in) for the Cornwallis-Clinton cipher passages |

**And every `queued` JSTOR-QUEUE.tsv row (22 queries across 12 targets):** clair1108-duvergier (1),
fr5160-letellier-1653 (2), jan-van-nassau-1572-75 (3), trew-posthius-1614-18 (2), antt-linhares-chave (3),
vanbeuningen-dewitt-1657 (1), bl-charles-digby (1), specs/powers-1991.json (1), antt-fcc-costacabral-1865 (1),
espagnol142-mercy-1648 (4), clair349-este-guise-1556 (3) — full query text is in the file, nothing to retype
here.

---

## 2. Emails ready to paste

Sign off each with your own name in place of `[owner's name]`. Record the date sent in the ASKS row named.

### BnF, Département des Manuscrits (ASKS 49, 54)

**To:** manuscrits@bnf.fr, or the SINDBAD form (www.bnf.fr/fr/une-question-pensez-sindbad) if that address bounces
**Subject:** Demande de reproduction — Collection Clairambault (574, 575, 579, 1161)

> À l'attention du Département des Manuscrits,
>
> Je souhaiterais obtenir une reproduction numérique couleur (usage recherche) des documents suivants,
> conservés dans la Collection Clairambault :
>
> 1. Clairambault 575, p.1209 (et la page en regard ou suivante) — "Lettre chiffrée adressée à l'un des
>    plénipotentiaires à l'occasion du traité de Münster" ;
> 2. Clairambault 574, f.3-4 ("Chiffre employé par Brasset") ;
> 3. Clairambault 579, p.341 ("Double du chiffre de Mazarin avec M. d'Estrades").
>
> Ces trois documents ne semblent pas numérisés sur Gallica.
>
> Une quatrième question, sur un volume déjà numérisé cette fois : votre instrument de recherche
> (ark:/12148/cc137837/cd0e35310) situe la pièce "Avis de Flandre, chiffrés" à "fol. 106 et suiv." dans
> Clairambault 1161, mais sur la version numérisée (ark:/12148/btv1b90010063), ni l'image correspondant à ce
> foliotage ni le reste du volume (vérifié en entier) ne contiennent de document chiffré à cet endroit.
> Pourriez-vous m'indiquer où se trouve réellement cette pièce, et m'en fournir une image si elle existe ?
>
> Je vous remercie de bien vouloir m'indiquer la procédure et le tarif applicables pour les trois premiers
> documents.
>
> Bien cordialement,
> [owner's name]

### Hessisches Staatsarchiv Marburg (ASKS 48)

**To:** marburg@hla.hessen.de (phone +49 6421 9250 0, read from the archive's own page 25 Sept 2026)
**Subject:** Reference request: old signature "4f Nld. 165" (Glawischnig 1973), Nassau-Dillenburg papers

> Dear Hessisches Staatsarchiv Marburg,
>
> I'm researching a letter of 17 April 1574 (Jan/Johann VI. von Nassau to Wilhelm von Oranien, written from
> Köln) and I'm trying to trace a second copy of it that Rolf Glawischnig cites in his 1973 study
> (*Niederlande, Kalvinismus und Reichsgrafenstand 1559-1584*) under the old shelfmark "4f Nld. 165" (Bestand
> "4 f Niederlande", Paket/item 165). I can see in Arcinsys that this fonds has been reorganised into "4 f
> Staaten N > 5 Nassau-Dillenburg, Fürsten", but I haven't been able to match the old item "165" to its current
> Arcinsys signature.
>
> Could you help with:
> 1. What is the current Arcinsys signature for the item Glawischnig cited as "4f Nld. 165"?
> 2. Is that item digitised in Arcinsys (several neighbouring items in the same series already are)?
> 3. If digitised, could you point me to the image, or share a screen-quality photograph? I'm especially
>    interested in whether the two enciphered lines at the top of page 3 carry an interlinear or marginal
>    period decipherment.
> 4. If not digitised, what would a reading-room photograph of that item cost?
>
> Thank you very much for your help.
>
> Kind regards,
> [owner's name]

### NARA College Park (ASKS 55a)

**To:** archives2reference@nara.gov — confirm this is still current on archives.gov/contact before sending
**Subject:** Reference request: RG 65, Class 105, File 9673 ("Kohler, Walter")

> Dear NARA reference staff,
>
> I'm researching Walter Koehler, a Western Union operator turned German agent in New York in 1944 (his cipher
> messages to the Abwehr's Paris radio station are described in David Kahn's "German Spy Cryptograms,"
> *Cryptologia* 5(2), 1981, pp.65-66). Your own released FBI name-index lists a personal file: RG 65 (FBI),
> Class 105, File 9673 ("Kohler, Walter"), Sections 001 and EBF 003, Box 156, location 230 86/16/05,
> declassified around 2004 under the Nazi War Crimes Disclosure Act.
>
> Could you tell me whether this file has been digitised or is available for reproduction, whether it
> discusses his February-April 1944 wireless messages or how they were enciphered, and what a copy would cost?
>
> Thank you for your help.
>
> Kind regards,
> [owner's name]

### Adirondack History Center Museum (ASKS 52)

**⚠ Confirm this address independently first** (a search engine or phone check) — it was read from two
third-party pages (nyheritage.org, iloveny.com), not the museum's own site, which this environment cannot reach.

**To:** echs@adkhistorycenter.org (518-873-6466, 7590 Court Street, Elizabethtown NY 12932)
**Subject:** Henry Debosnys papers — a question about a possible cipher key

(Reused verbatim from `outreach/debosnys-museum.md`, drafted 25 Sept 2026.)

> Dear Adirondack History Center Museum / Essex County Historical Society,
>
> I'm researching the four cryptograms Henry Debosnys left behind during his 1882-83 imprisonment in Essex
> County, alongside his clear-text poems and drawings, which I understand are held in your collection together
> with material connected to his case. As far as I have been able to establish (searching Cheri Farnsworth's
> *The Adirondack Enigma*, Craig Bauer's *Unsolved!*, Klaus Schmeh's Cipherbrain blog, Cipher Mysteries, and the
> usual cryptography literature and databases), none of the four cryptograms has ever been decrypted, and no
> key or cipher alphabet for them has been published.
>
> I have two questions, and would be very grateful for whatever you're able to tell me even if the answer to
> both is no:
>
> 1. Among Debosnys's papers, is there anything that looks like a key, a symbol-to-letter table, or a cipher
>    alphabet — something separate from the four encrypted pages themselves? Even a single sheet like this
>    could make it possible to read the cryptograms for the first time.
>
> 2. Would it be possible to get scans or photographs of his clear-text poems and other papers (not just the
>    four cryptograms, which I understand are already reproduced in Farnsworth's book and on Cipherbrain)?
>    Comparing the line lengths, vocabulary and handwriting of his known clear-text writing against the
>    cryptograms is one of the more promising routes to reading them, and a fuller set of his papers than
>    what's already published would help with that.
>
> I'd be happy to share back anything useful that comes out of this research. Thank you for your time, and for
> preserving this very unusual piece of Adirondack history.
>
> Sincerely,
> [owner's name]

### Koninklijk Huisarchief, Den Haag (ASKS 31)

**No confirmed contact address on file** — KHA material is consulted through the Nationaal Archief reading
room in The Hague; check knhuisarchief.nl's own contact page, or the Nationaal Archief front desk, before
sending.

**Subject:** Reproduction request — A 11/XIV B/15-43 (Willem van Hessen to Willem van Oranje, 28 January 1567)

> Dear Koninklijk Huisarchief,
>
> I'm researching a letter from Willem van Hessen to Willem van Oranje, 28 January 1567 (written from Kassel),
> part of which is in an as-yet unsolved cipher. Your own online correspondence database (WVO,
> resources.huygens.knaw.nl/wvo, briefnr 1127) lists the original as held under your shelfmark
> A 11/XIV B/15-43, with a note that part of it is "in onopgelost cijferschrift" (in unsolved cipher). Only a
> draft of this letter, held in Marburg, is available online; no image of your original is.
>
> Could I ask for a digital scan or photograph of A 11/XIV B/15-43 (both the plain and enciphered passages)?
> The draft is said to give the complete text, so comparing it against your original could make it possible to
> read the cipher for the first time.
>
> Thank you very much for your help.
>
> Kind regards,
> [owner's name]

### AGR (Archives générales du Royaume), Brussels (ASKS 60)

**No confirmed contact address on file** — look up the AGR's own reproduction-request or reading-room-
appointment contact at arch.be before sending.

**Subject:** Reproduction request / signature check — Secrétairerie d'État et de Guerre, t. LXIV f.16

> Dear Archives générales du Royaume,
>
> I'm researching a 1648 instruction to the abbé de Mercy, cited by Henri Lonchay (1896, p.445 n.2) as
> "Secrétairerie d'État et de Guerre, t. LXIV f.16" (15 April 1648), part of fonds T 100 (AGATHA reference
> BE-A0510_000027_002526). AGATHA shows this register as digitised but reading-room-only, with no online image.
>
> Could you first confirm the modern register number for Lonchay's citation "t. LXIV" (his 1896 volume
> numbering may not match your current one), and then let me know how to order a reproduction of f.16 (and
> f.16v) — or the process and notice period for a reading-room appointment, if that's the only option?
>
> Thank you very much for your help.
>
> Kind regards,
> [owner's name]

### William L. Clements Library, University of Michigan (ASKS 58)

**No direct reference email found on file** — the library's own site is blocked from this environment; register
at clements.umich.edu ("New Request") or send this first, per clements.umich.edu/research/duplication-and-use.

**Subject:** Reproduction request — Clinton Papers vol. 64:14 and 64:15

> Dear William L. Clements Library,
>
> I'm researching an intercepted, still-enciphered 1779 letter and would like reference copies of two items in
> your Clinton Papers:
> - vol. 64:14 — Admiral d'Estaing to Gérard, Martinique, 30 April 1779 (the ciphered letter itself, forwarded
>   home by Sir Henry Clinton in July 1779);
> - vol. 64:15 — d'Estaing's clear letter to Jean Holker of the same date (both copies you hold).
>
> Could you tell me whether these can be supplied as reference images, and what the process and any cost would
> be?
>
> Thank you very much for your help.
>
> Kind regards,
> [owner's name]

---

## 3. Paid orders, ranked

Ranked by unblocked check-solved-open targets per pound/dollar. Recommended top three: **Clements Library**
(free), **Stair-Townshend 1710** (~$20 or less), and **the single first Heinsius photograph, H.A. 1836** (cheap
and possibly decisive outright) — three low-cost orders that between them test three different targets fast,
before committing to the larger BL/TNA/Arsenal batches.

| Rank | Order | Cost | What arrives | Unblocks | Expected value |
|---|---|---|---|---|---|
| 1 | **Clements Library** (ASKS 58, `destaing-gerard-1779`) | Reference JPEG/PDF: **free**; only publication-quality scans carry a fee | Two 1779 letters, vol. 64:14 (ciphered) + 64:15 (clear, same sender/day) | 1 target | Free is free; register first (see §2 email) |
| 2 | **Stair-Townshend 1710** (ASKS 4, `stair-townshend-1710`) | $0.25-1 for PDF reference copies of all 4 images; ~$20 for the full TIFF set | The ciphered page plus its neighbours | 1 target | Cheapest paid order on the list; a PDF reference copy of just the ciphered page may be enough for a first read |
| 3 | **Heinsius NA, item 1 only** (ASKS 46, `borssele-heinsius-1714`, H.A. 1836) | Not yet quoted; NA's standard reproduction fee for ~2-3 leaves (historically modest) | The cipher letter, plus the dossier's own possible "oplossing" (decipherment) on the same leaf | 1 target, **but the edition's footnote says a decipherment may already be on the same leaf** — could close the item outright | Highest payoff-per-photograph on the list; order this one leaf before the rest of the Heinsius batch |
| 4 | **SP 78 France** (ASKS 15, `sp78-france-1583`) | £19.84 for two TNA page-checks (£9.92 each), then a copying quote | SP 78/111/93, /135 and SP 78/113/57(+1) | 1 target | TNA's daily page-check cap was already hit once (23 Sept) — submit early in the UK morning |
| 5 | **TNA batch** (ASKS 57, eight targets) | £9.92 per item page-check across many items in 8 targets (order named items per target's REQUEST.md), plus copying quotes after | SP 87 (Chesterfield, Newcastle, Further 1712, Brunswick), SP 90 (Raby/Whitworth), SP 35 (Townshend), SP 54 (Maclean), SP 53 (f.52) | 8 targets | Best raw target count; two items carry their own enclosed/candidate key (`sp35-townshend-key-1719`, `sp53-22-f52`) |
| 6 | **BnF/Arsenal batch** (ASKS 35 + 38, five targets) | Not yet quoted (Arsenal microfilm cote R-242218, or BnF reproduction service) | Arsenal Ms-6314 (cipher+decipherment pair), Ms-6829, Ms-6334 (**with its own Feb 1650 key on file**), Ms-4764/11639, Clairambault 528 | 5 targets | Ms-6334's own key makes this batch worth a quote even before Ms-6314's images arrive |
| 7 | **Heinsius NA, remainder** (ASKS 46, priorities 2-4) | Not yet quoted; ~16-30 more leaves across `heinsius-hermitage-1704`, `heinsius-dopff-1702`, `heinsius-vanhaersolte-1703`, `rumpf-vandebie-heinsius-1716-19` | Four more Heinsius-circle cipher letters plus one candidate key (H.A. 2317) | 4 targets | Natural follow-on once item 1's quote is in hand, not a first move on its own |
| 8 | **BL batch** (ASKS 56, six targets) | Not yet quoted (Imaging Services); BL says it cannot scan an original without an existing microfilm surrogate, so some may need a reading-room visit instead | `bl-james-1669` (own partial key), `bl-sacchetti-nunzio-1623`, `bl-gualterio-1700`, `maurice-rupert-1645`, `sp90-raby-1704`, `harley-287-1587` (finishes an existing partial reading) | 6 targets | Most targets after the TNA batch, but least certain cost/route |
| 9 | **Monck BL quote** (ASKS 6, `monck-1660`) | Not yet quoted | Add MS 32093 f.423 | 1 target | Lowest priority: single target, no distinguishing lead |

---

## 4. Decisions, one line each

- **DECODE login retry (ASKS 1/42):** don't retry the login again — three rejections already, and the real
  blocker is the account-wide image-permission block, not the login itself. *If you say nothing:* it stays
  waiting on DECODE's reply to the role-upgrade email already sent 24 Sept 2026.
- **FNMT root certificate (ASKS 28):** add it to the environment's trust store — a trust addition, not
  disabling verification, same fix already used for the proxy CA; opens pares.cultura.gob.es and other Spanish
  archives. *If you say nothing:* Spanish archive searches keep needing a person's own browser.
- **Whitworth 1707 (ASKS 7):** waive the Kew order for now — "one unread clause" is speculative next to the
  paid orders ranked in §3. *If you say nothing:* the target stays as-is, nothing ordered, nothing blocked.
- **GitHub Pages (ASKS 8):** enable it (main branch, `/docs` folder) — no cost, one click, gives the whole team
  visibility into the board. *If you say nothing:* the board stays visible only via the private artifact link.
- **Collaborators (ASKS 9):** add write-access collaborators — the "several people work in this repository"
  model in CLAUDE.md needs it to function at all. *If you say nothing:* teammates keep working around missing
  access.
- **JSTOR/outreach-gate rows to run or waive (ASKS 17, 26, 32, 33, 36, 37, 39, 40, 41, 44, 49, 54):** run them
  via the local runner in §1 rather than waiving — it costs nothing (already-logged-in browser), and several
  are one query away from letting a verifier draft the Tomokiyo/Huygens/Bourdeau outreach that's already
  written. *If you say nothing:* they stay queued and that outreach stays undrafted-to-send.
- **Danzay Daussy 2001 chapter (ASKS 26):** waive it — a single confirmatory chapter for a target already at
  N4; an ILL/copy order likely costs more than it's worth. *If you say nothing:* N3/N4 stands without it (the
  ask itself already names this as an acceptable fallback).

---

## 5. Nothing needed from the owner

- **Five IA lending-only borrows are in progress right now**, not waiting on you: a cloud worker (`parent
  worker IA-BORROW`, ROOM.md 22:34 UTC) claimed all five obfuscated-page reads that used to sit in ASKS/
  LOCAL-QUEUE — **ASKS 53** (Köhler, `sim_cryptologia_1981-04_5_2`), **ASKS 55b** (Farago, `gameoffoxesuntol
  00fararich`), **ASKS 59** (Mercy 1648, `correspondancede0006jose`), **L7/ASKS 18** (Hamilton 1650,
  `supplementaryrep0000grea`), and **the Dorabella breadth test / ASKS 50** (`edwardelgarmemor0000mrsr`). The
  local-runner prompt in §1 already excludes L7 so it isn't duplicated; the other four never had a
  LOCAL-QUEUE/JSTOR row to begin with.
- **Four open-index queries no longer need your machine.** `OPENALEX_KEY` and `S2_KEY` are now set and
  confirmed working from the cloud (CLAUDE.md's Access playbook, "Key probe, 25 Sept 2026": both keys answer
  HTTP 200 with real result counts) — CLAUDE.md itself says "no owner-machine row is needed for OpenAlex or
  Semantic Scholar" once the keys are present. That covers **ASKS 40**'s two remaining queries ("Pareti
  Marchmont 1728", "Ripperda Segovia escape 1728") and **ASKS 41**'s two ("Fox Butler 1864 camels Tecumseh",
  "Meigs Butler 1864 cavalry depot"); a cloud worker/verifier should run these, not the local runner.
- **ASKS 44's own gates are already both met**, so nothing further is owed there: its open-index pass ran from
  the cloud on 24 Sept 2026 (one relevant hit, already read by verifier V6), and its three JSTOR READ rows
  (Mignet 1867, Hauser 1923, Philippson 1908) show `done 24 Sept 2026` in `JSTOR-QUEUE.tsv` lines 68-70 — none
  prints or discusses the letters. The Tomokiyo, Huygens and Bourdeau-issue-1 drafts are gate-clear and ready
  for you to send whenever convenient; they just weren't on the brief's named list for §2.

---

*ASKS.md row added: "OUTBOX.md consolidates rows [see this file]; act from OUTBOX.md".*
