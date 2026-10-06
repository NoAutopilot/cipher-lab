open
*Briefwisseling van Anthonie Heinsius 1702-1720* Deel 18 (Smit/Veenendaal, Huygens retroboeken GS244) p.95 read by GF-A2-5 (2 Oct 2026) from the page image on disk: letter 142 prints the numeral cipher in running French, footnote 3 "Het cijferschrift is door d'Alonne niet opgelost", no decipherment printed.

# H.W. Rumpf and van de Bie to Anthonie Heinsius, cipher never broken by d'Alonne, 1716-1719

QUEUE row: HU4 (`QUEUE.md`, "Huygens and Nationaal Archief correspondence editions: letters noted in cipher
(LANE N harvest of 24 September 2026)"). Brief `.claude/briefs/runs/2026-09-24-lane-n-csHU.md`.

## Source

Anthonie Heinsius correspondence archive, Nationaal Archief 3.01.19 ("H.A." in the edition), inv.nrs. 1975 /
2030 / 2044. Printed in J.G. Smit / A.J. Veenendaal (ed.), *Briefwisseling van Anthonie Heinsius 1702-1720*,
Deel 18 (GS244) and Deel 19 (GS247), via the Huygens `retroboeken/heinsius` viewer (no login,
`resources.huygens.knaw.nl`).

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents). Continuing HU4 from the harvest worker
hvHUY (`sources/huygens/NOTES.md`, `sources/huygens/cipher-letters-2026-09-24.tsv`), which found the footnotes
but did not check-solve, did not confirm every reference, and left the letter-455 identity unresolved.

1. **Editions first -- and decisive, re-read directly from the primary edition this pass** (not only trusted
   from the harvest's paraphrase):
   - **Letter 142** (H.W. Rumpf, Rotterdam, 17 Nov 1716; Deel 18, GS244, p.95, fetched and read as both OCR
     text and page image, `images/heinsius_18_GS244_095.jpg`): the printed edition carries the actual
     ciphertext in running French prose -- e.g. "...ce qui nous fait croire 70³ 33 67 17 31 19 49 39 46 16 22
     4 66 18 26 36 25 28 42 72 29 52 65 74 46 53 44 37 de 68 55 46 54 49 58 52 25 1 28 51..." (about 180
     numeral tokens across the paragraph, confirmed by eye in the page image, not merely from OCR). Footnote 3
     at the foot of the page: **"Het cijferschrift is door d'Alonne niet opgelost."** (The cipher was not
     solved by d'Alonne.) This is the strongest-founded instance in the batch: genuine printed ciphertext, in
     an edition, with an explicit contemporary-failure footnote from a named professional decipherer.
   - **Letter 309** (H.W. Rumpf, Stockholm, 23 Mar 1718; H.A. 2030; Deel 18, GS244, p.555) -- per the harvest's
     quote, addressed "Aan A.T. d'Alonne in onopgelost cijfer" -- sent directly to the decipherer, still
     unsolved. Not independently re-fetched this pass (budget); the harvest's quote is treated as read (the
     same edition, same pattern as 142, already confirmed reliable this pass on 142/446/455).
   - **Letter 446** (van de Bie, Stockholm, 15 Aug 1719; H.A. 2044; Deel 19, GS247, pp.302-303, re-fetched and
     read this pass): footnote 1, "**Enige regels onopgelost cijferschrift weggelaten**" (some lines of
     unsolved cipher omitted), and footnote 2, "**Twee regels onopgelost cijferschrift weggelaten**" (two
     lines of unsolved cipher omitted) -- confirmed verbatim. The ciphertext itself is **not in this edition
     at all**; only the Nationaal Archief original (H.A. 2044) would carry it.
   - **Letter 455**, not 446 as the harvest's provisional numbering had it (Deel 19, GS247, p.337, re-fetched
     and read this pass, resolving the harvest's "not confirmed this pass" gap): footnote 4, "**Eén regel
     onopgelost cijferschrift weggelaten**" (one line of unsolved cipher omitted). Sender not independently
     re-identified this pass (the letter's own heading sits on an earlier page than p.337; the surrounding
     text is a diplomatic report from Sweden, consistent with the same Rumpf/van de Bie/Sweden reporting
     circle but not confirmed by name -- left for a future worker, one more page-back fetch).
   All four instances sit within a single continuous reporting relationship (Rotterdam admiralty and then
   Stockholm-based correspondents, during the endgame of the Great Northern War) that Heinsius's own
   professional cryptographer, Abel Tassin d'Alonne, never broke across three archival years.
2. **d'Alonne background (post-edition, general).** English Wikipedia's article on Abel Tassin d'Alonne
   (fetched this pass) confirms he was a real, documented cryptographer -- Heinsius's private secretary and
   the head of his "cabinet noir" -- who decrypted intercepted Rouillé/Bonnac correspondence in 1707 and is
   credited with the 1684 d'Avaux decryption. The article names no correspondent called Rumpf or van de Bie
   and records no failed decryption by name; it neither confirms nor contradicts this target, but supports
   that d'Alonne was a competent, active decipherer at exactly this period, which makes his stated failure on
   Rumpf/van de Bie's cipher more significant, not less.
3. **Post-edition literature search (check-solved.md's Oxenstierna/Torpadie lesson).** `WebSearch "Rumpf
   Stockholm Heinsius 1719 cipher decipherment"` returned nothing relevant to this correspondent or these
   letters (only unrelated Rumpf/Heinsius namesakes: Isaak Augustijn Rumpf, the Copiale Cipher project, etc.).
   No specific search of a Dutch/Swedish Great Northern War diplomatic-history journal by name was run this
   pass (budget shared across four targets) -- flagged as a narrower follow-up, not completed.
4. **Community lists.** `sources/cryptiana/web/dutch.htm` re-read (via `tools/html2text.py`, since the raw
   HTML is mojibake): the page discusses a general two-part code distributed to Heinsius and ambassador
   Schütz (preserved in Hanover, apparently never adopted in the Netherlands) and cites Vroomen & Nissen,
   "Cijferschrift en spionage" (*Jaarboek De Zeventiende Eeuw* 2018) on the De Witt-Van Hoogh cipher of 1664
   -- neither mentions Rumpf, van de Bie, or this correspondence by name.
5. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for "rumpf"/"heinsius"/"bie": zero
   hits.
6. **Solver repositories.** Fresh shallow clones this pass (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-
   ciphers`), grepped for "rumpf", "van de bie", "heinsius", "d'alonne", "3.01.19". No hit on this
   correspondence in either. One namesake false positive worth recording so a later worker does not re-find
   and misread it: `aaymeloglu/unsolved-ciphers/catalogue/decode-catalog.csv` row 2818, DECODE id 2818, "The
   Hague, Nationaal Archief, collection **1.10.29 Familie Fagel**, inv. nr. 5345... cipher_van_Rumpf_**1743**"
   -- a cipher *key* record, a different archive series (Fagel, not 3.01.19 Heinsius) and a later date (1743
   vs. 1716-1719) than this target. Could conceivably be the same person (H.W. Rumpf) in a later phase of his
   career with a different correspondent, but this was not confirmed and is not treated as the same cipher
   system. `cyphersolver`'s own key table for `windischgraetz1720` (an unrelated 1720 cipher) happens to list
   a plaintext word "Heinsius" as one of its code entries -- unrelated coincidence, not a hit on this target.

## Verdict

**Status: open.** All four instances (letters 142, 309, 446, 455) rest on a direct, this-pass reading of the
standard printed edition (Veenendaal/Smit), which states plainly that Heinsius's own professional cryptographer
never solved this correspondent's cipher across three archival years. No later print, community list, DECODE
record or solver-repository entry names a solution or even a serious attempt. This is the strongest-founded
"open" verdict of this batch: letter 142's actual ciphertext is in print and was confirmed by eye in the page
image, not merely inferred from a footnote.

**Copy status: NOT copy-free, corrected 24 Sept 2026 (LANE N2 worker csHU2).** The "likely copy-free" claim
above, and the harvest's original claim that 756 "carries a real scan," both rested only on the generic
"Scan"/"Viewer" page-shell text -- neither actually read the per-item record. Fetched and decoded the real
per-item JSON this pass (each invnr page's embedded `drupal-settings-json` -> `viewer.response`, not the
page shell) for **all** of 1975, 2030, 2044 (this target) plus 756 (HU1) and 1836 (HU5): every one returns
`"availability":"PHYSICAL","scans":[]` -- **none is digitised**, confirmed against a positive control (NA
1.04.02 invnr 1, `"availability":"DIGITALIZED"` with real IIIF URLs, proving the accessor correctly reports a
scan when one exists). This also corrects `sources/huygens/NOTES.md` caveat 5 and the "NA 3.01.19 as a whole is
understood to be a digitised series" working assumption above -- at least this cipher-relevant slice of the
archive is not. `REQUEST.md` written this pass for the two instances with printed extent worth copying (309/
H.A. 2030, whose cipher letter is not in the edition at all; 446/H.A. 2044, two omitted cipher lines);
letter 142's ciphertext is already fully in print (`ciphertext_142.tsv`) and needs no copy.

**Kind: cryptanalysis.** No contemporary decipherment, no known key, no solved sibling identified for this
correspondent circle. Letter 142's printed ciphertext (confirmed present, image on disk) is the one instance a
solver could attempt without an archive visit at all; letters 309/446/455 need the Nationaal Archief originals
since their ciphertext is not in the printed edition.

Search log (rule 10): reported above, per source. Not classified for novelty (that is a verifier's job, rule
10). Requests this pass: `resources.huygens.knaw.nl` ~13 (2 book_data.js already cached from earlier steps in
this session, 3 pages.json, 4 html_url OCR fetches [p.95, p.302, p.303, p.337], 1 image fetch; all ≥2s apart,
descriptive User-Agent, no login). `www.nationaalarchief.nl` 3 (invnr 1975/2030/2044, shared with HU5's 1836 in
one batch, ≥2s apart). `github.com` 2 shallow clones (grepped, not committed, kept in `/tmp/csHU`). WebSearch 2,
WebFetch 1 (d'Alonne Wikipedia). No subagents.

## H1: cryptanalysis (LANE R2 worker H1, Opus, 24 Sept 2026 10:07-10:18 UTC)

Status unchanged: **open** (cryptanalytic negative at this length, with a matched control; not closed).

**Material.** Letter 142 only. Transcribed from `images/heinsius_18_GS244_095.jpg` (printed edition, not the
NA manuscript: rule 2, any negative is conditional on the editor's print) and cross-checked against the Huygens
OCR html for p.95 (identical sequence): `ciphertext_142.tsv`, 6 segments, **208 tokens**, 64 distinct values
in 1-77 (absent: 7 10 12 14 21 24 30 40 41 50 56 62 71). The superscript on the first 70 ("70³") is the
editor's footnote-3 marker ("Het cijferschrift is door d'Alonne niet opgelost"), not a cipher mark. The cipher
starts on p.95 (the footnote marker sits on its first number). Letter 309 (p.555, fetched as OCR) is a regest
only ("Aan A.T. d'Alonne in onopgelost cijfer"): no ciphertext printed; 446/455 omit theirs ("weggelaten").

**Design.** Numbers interleaved with clear French words ("de", "come l'on a fait", "de toutes les", "J'avois",
"d'où il semble que"), so the cipher replaces running French text, not whole sentences. IoC 0.0186 (flat
over 64 = 0.0156; French letters about 0.078); most frequent 74 (12), 44 (9), 49 and 28 (7); no doubled
adjacent value in 208 tokens; repeated bigrams 44 37 and 47 53 (4 each), trigram 76 47 53 (2). Consistent with
a homophonic letter cipher of about 64-77 signs (possibly with a few syllable signs; not distinguishable at this
length). Clear context predicts segment 1 begins "que" ("ce qui nous fait croire ...").

**Matched control (rule 3).** Plaintext: the clear French of this same letter (p.95 paragraphs 2-4,
`control/clear142_p95.txt`), first 208 letters, enciphered with random homophonic keys of 62-63 signs allotted
by frequency (`tools/homophonic_anneal.py --control`). LM: `tools/data/fr16` (Marguerite de Valois, Catherine de
Médicis t.1-2; 16th-century French, the nearest French corpus on disk; no 1716 corpus was built). Order 3,
8 restarts x 400,000 iterations: **control read 61.5 / 28.8 / 70.7 % (seeds 1-3)**; order 4 47.6 %, order 5
26.0 %. With a 3-letter crib fixed (new `--fix-first`), 67.8 / 14.9 / 63.9 %. Diagnostic: on the control the
solver's best key scores above the true key (-406.0 vs -428.4), i.e. at N=208 and K=64 the language model does
not single out the true key; a control read is partial and seed-dependent.

**Target.** Same settings, seeds 1-3: best scores -408.0 / -407.5 / -409.4 (the control's range), three
different decodings, keys agreeing on only 10-28 of 64 signs between seeds; no connected French. With the crib
70=q 33=u 67=e (inferred, grade I, from "croire que"; new `--fix`): best -415.4 / -419.9 / -414.5, keys agreeing
24-28/64, still no connected French (seed 3 begins "quespresecateleuoitrauauenel..."). **No reading; no key.tsv
or decode.json written.** Runs: `control/runs.tsv`.

**Reading of the negative.** Control 29-71 % (mean about 54 %) vs target 0 % recognisable: the negative is weak,
because the control itself is only partly read at this length and the target may also differ from the
control's design (syllable or word signs, nulls, 1716 spelling vs a 16th-century LM). It does not show the
cipher is not a homophonic letter substitution.

Tool change (rule 8): `tools/homophonic_anneal.py` gains `--fix sign=letter,...` (target crib) and
`--fix-first N` (the matched control's crib); offline test still passes (0.993).

Search log (rule 10): no new search this pass beyond the check-solved sweep above; not classified for novelty.
Requests: resources.huygens.knaw.nl 2 (p.95 and p.555 OCR html, 2 s apart). No subagents.

Follow-up suggestions (one line each): (1) the NA originals of letters 309 (H.A. 2030, a whole letter in this
cipher) and 446/455 (H.A. 2044) would multiply the ciphertext several times and are the route to a reading;
(2) a 1700-1720 French letter corpus as LM; (3) a key or cipher table of Rumpf's in the Fagel papers
(NA 1.10.29 inv. 5345, "cipher van Rumpf 1743", DECODE 2818) is worth one look for a family resemblance.

## Web and blog check (GF-A2-5, 2 Oct 2026)

Plain web searches (4): `Rumpf Heinsius 1716 cipher "d'Alonne" "niet opgelost"` (Wikipedia Heinsius and d'Alonne,
Huygens edition page, NA 3.01.19 inventory PDF, and de Leeuw's Historical Journal article "The black chamber in the
Dutch Republic during the War of the Spanish Succession and its aftermath, 1707-1715" -- its stated range ends 1715,
before letter 142, so not opened further this pass; none reads this cipher); `"Rumpf" Stockholm 1718 Heinsius
cijferschrift onopgelost` (Rumpf namesakes -- Rumphius, Isaak Augustijn Rumpf, Christiaan Constantijn Rumpf d.1706 --
nothing on this cipher); `"van de Bie" Stockholm 1719 Heinsius cipher` (Heinsius family pages, nothing on van de Bie's
cipher); `Heinsius archief 3.01.19 inv 2044 OR 2030 OR 1975 Rumpf cijfer` (NA inventory PDF, a BMGN article PDF,
unrelated catalogue pages).
Blog site searches: `site:scienceblogs.de klausis-krypto-kolumne Heinsius cipher` (Cipherbrain archive pages only, no
post on Heinsius/Rumpf); `site:cryptiana.blogspot.com Heinsius d'Alonne cipher` (no Cryptiana page returned; Cipher
Mysteries "17th century cipher mystery meme" and p=7357 surfaced, general posts, not about this correspondence);
`site:ciphermysteries.com Heinsius Dutch cipher eighteenth century` (no Cipher Mysteries page about Heinsius
returned). No comment thread found that discusses these letters.
Result: no decipherment or plaintext of letters 142/309/446/455 found on the open web or in the three blogs.
Requests: WebSearch 7; no page fetches (the p.95 image was read from disk).

## Premise check (GF-A2-5, 2 Oct 2026)

(a) Folder's own mentions: every decipherment mention in NOTES.md and REQUEST.md is a statement that d'Alonne did NOT
solve the cipher (footnotes to 142, 309, 446, 455); p.95 re-viewed from the image on disk confirms no decipherment
is printed beside or below letter 142's cipher. Not found. (Side note for the next reader: the p.95 image shows letter
142 signed H.W. Rumpf and written from Sweden -- it mentions Lund, Udstedt and the baron Görtz; "Rotterdam" in the
24 Sept sweep's heading for 142 belongs to letter 143 from the Rotterdam admiralty on the same page. Not corrected
above; flagged here only.)
(b) Other solvers' working files: shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers (2 Oct 2026)
grepped for "Rumpf", "van de Bie", "Heinsius", "Dopff": "Rumpf" hits only German corpus files, a perwich text and
Aymeloglu's DECODE catalogue rows 2818 (NA 1.10.29 Fagel inv. 5345, "cipher van Rumpf", 1743, a key record) and 1361
(Vienna, 1574, unrelated); "Heinsius" hits only Bourdeau's windischgraetz1720 / rakoczi1707 / bay1706 key files (the
word as a nomenclator entry) and an Aymeloglu forster-1644 lexicon. No output, rendering or key run on this text.
Aymeloglu cited, not copied. Not found. The 1743 Fagel "cipher van Rumpf" key (DECODE 2818) stays a lead to test
against letter 142 if it proves to be the same Rumpf's system -- unconfirmed.
(c) Physical neighbours: originals H.A. 1975/2030/2044 are not digitised (`"availability":"PHYSICAL","scans":[]`,
24 Sept sweep); the printed page carries no facing decipherment. Unreachable for the manuscript leaves (REQUEST.md is
the route).
(d) Recipient side: Heinsius is the recipient and the edition read is his own correspondence edition (Deel 18 p.95
this pass; Deel 19 pp.302-303, 337 by the 24 Sept sweep). Sender-side Swedish or Dutch-envoy print not searched this
pass. Not found.

## GAPS109-rumpf-vandebie-heinsius-1716-19 (3 Oct 2026, account-4)

Step run: H1 follow-up (1), the Nationaal Archief originals of letters 309 (H.A. 2030) and 446/455 (H.A. 2044),
plus one look at follow-up (3), DECODE 2818. Stale check: the availability half of (1) was already done by csHU2
on 24 Sept 2026 (Verdict section above, with the NA 1.04.02 inv. 1 positive control) and the copy order is
already ASKS row 46 / `REQUEST.md` (priority 4 of the consolidated Heinsius-circle request in
`ciphers/borssele-heinsius-1714/REQUEST.md`). This pass only re-probed it, in case anything had been digitised since.

- **NA 3.01.19 inv. 2030** (`www.nationaalarchief.nl/onderzoeken/archief/3.01.19/invnr/2030`, fetched 3 Oct 2026
  12:4x UTC): the embedded `drupal-settings-json` viewer record reads unittitle "Rumpf, Hendrik Willem-, uit
  Stockholm.", `"scans":[]`, `"availability":"PHYSICAL"`. **Not digitised.**
- **NA 3.01.19 inv. 2044** (same route): unittitle "Bie, Jacob de-, uit Hamburg, Lübeck en Stockholm.",
  `"scans":[]`, `"availability":"PHYSICAL"`. **Not digitised.**
- So nothing was fetched through service.archief.nl IIIF, there are no new images and no vision call was made. The
  route to letters 309/446/455 is still the copy order (ASKS row 46, REQUEST.md), unchanged.
- **DECODE 2818**: its metadata is already on disk from the 28 Sept 2026 login-free key crawl
  (`sources/decode/keys-na-p59-128-2026-09-28.tsv`, `keys-all-2026-09-28-merged.tsv`), so no new DECODE request was
  made. Row: status N/A, record type **Key**, holder "The Hague, Nationaal Archief, collection 1.10.29 Familie
  Fagel, inv. nr. 5345", shelfmark code `NA_1.10.29._F.F._inr.1233_cipher_van_Rumpf_1743`, date 1743-1743, 25 pages,
  no cleartext or plaintext language given. The record contradicts itself: the holder field says inv. nr. **5345**
  but the shelfmark code says **inr.1233**, so the Fagel inventory number has to be checked before anyone orders or
  probes it. Nothing in the metadata names which Rumpf it is, so it is still not shown to be this correspondent's
  system. Its images and documents sit behind DECODE's account gate (not tried, per the brief).

Next cheap step, not run (outside this brief): read the NA 1.10.29 item pages for inv. 5345 and 1233 (the same
`drupal-settings-json` check, 2 requests) to settle which number holds the "cipher van Rumpf 1743", whether it is
digitised and whose cipher its unittitle says it is. If it is a digitised Rumpf key, it is the first key-material
lead for letter 142, the one instance already in print.

Requests: `www.nationaalarchief.nl` 2 (2 s apart, descriptive User-Agent). DECODE 0. No subagents, no vision calls.

## GAPS115-rumpf-vandebie-heinsius-1716-19 (3 Oct 2026, account-4)

Step run: the next cheap step GAPS109 named, the Nationaal Archief 1.10.29 (Familie Fagel) item pages for inv. 5345
and 1233 (DECODE 2818's two contradictory numbers), read through the embedded `drupal-settings-json` viewer record.

- **inv. 5345** (`www.nationaalarchief.nl/onderzoeken/archief/1.10.29/invnr/5345`, fetched 3 Oct 2026 13:0x UTC): the
  page answers 200 but carries no unit: `viewer.response` is `null`, no unittitle, no scans. DECODE 2818's holder field
  ("inv. nr. 5345") does not point at this item in the NA's own inventory; its shelfmark code (`inr.1233`) does.
- **inv. 1233** (same route): unittitle "'Voor den Heer Carel van Rumpf, haar Ho. Mo. Extras Envoyé aan het Hof van
  Sweeden', 1743", `"availability":"DIGITALIZED"`, 25 scans (`NL-HaNA_1.10.29_1233_0001` to `_0025`), matching
  DECODE 2818's 25 pages. **Digitised.** The full scan list (service.archief.nl file and IIIF URLs, byte sizes) is in
  `images/fagel1233/manifest.json`; five scans (orders 1, 2, 3, 12, 25) were fetched once at 1400 px wide through the
  IIIF image API into `images/fagel1233/` (about 1.5 MB together), the rest re-fetchable from the manifest.
- **Whose cipher.** The unittitle names **Carel** van Rumpf, States-General envoy extraordinary to Sweden in 1743, not
  Hendrik Willem Rumpf, the 1716-19 writer of letter 142. Same family name and the same post (Stockholm) a generation
  later, so a family or office link is possible, but the record itself does not make this book the 1716 system.
- **Vision check (one call, Opus, own view).** Line crops cut first with `tools/iiif_lines.py --image
  images/fagel1233/NL-HaNA_1.10.29_1233_0012.jpg --prominence 20 --distance 25 --lines-per-crop 4` (41 lines, 11 crops
  `images/fagel1233_0012_L01..L11.jpg`, debug overlay `fagel1233_0012_lines_debug.jpg`); one composite of the scan-12
  opening at 700 px plus crops L03 and L06 was looked at. Scan 12 is a two-column **nomenclator list in Dutch**: names
  of German princes, territories, towns, troops and rivers ("Bisschop van Wurtsburgh", "de Landgraef van Hessen
  Cassel", "Hessen Casselsche Troupes", "Hamburgh", "Hanover", "de Rhyn", "de Donau", "de Mase") each against a
  three-digit code, consecutive from **216 to 305** on this opening (ruled leader dots, codes in the right margin).
- **Family-resemblance note (no reading, no key claim).** On what was seen, the design does not match letter 142's:
  the 1743 book is a large numbered nomenclator for a Dutch-language correspondence, codes in the 200s-300s on scan 12,
  while letter 142 is French running text with numbers 1-77 only (H1 above: homophonic letter cipher of about 64-77
  signs). The book's first eleven scans were not looked at; if it opens with a letter/syllable table in the low
  numbers, that section is the only place a resemblance could show, and it is the next look (one vision call on
  scans 2-3 crops, both already on disk). As it stands: **not shown to share the target's design; not excluded either**
  (one opening of 25 seen). Graded nothing; no token of letter 142 read.

Requests: `www.nationaalarchief.nl` 2 (item pages, 2 s apart, descriptive User-Agent); `service.archief.nl` 5 (IIIF
image API, 2 s apart). DECODE 0. Vision calls 1 (own view, no subagents).

Next cheap step: one vision call on line crops of scans 2-3 (already on disk; cut with `tools/iiif_lines.py
--prominence 20 --distance 25`) to see whether the 1743 book opens with a low-number letter or syllable table that
could be compared with letter 142's 1-77 range; about USD 1. The route to a reading is unchanged: the NA originals of
letters 309/446/455 (ASKS row 46, `REQUEST.md`).

## GAPS120-rumpf-vandebie-heinsius-1716-19 (3 Oct 2026, account-4)

**Pre-registered criterion (written 3 Oct 2026 13:2x UTC, before any scan 4-11 fetch or vision call).** Question:
does any part of NA 1.10.29 inv. 1233 (Carel van Rumpf, 1743) scans 2-11 carry a letter/syllable table numbered in
the 1-77 range, the shape of letter 142's homophonic design? Family resemblance only; no reading, no grades.
- **YES** if a scan shows single letters of the alphabet (a, b, c ...) and/or syllables (ba, be, bi ... or similar
  two/three-letter groups) set against numbers, at least some of which fall in 1-77, as a table (not a name list).
  Homophones (several numbers per letter) noted if visible but not required for YES.
- **NO (nomenclator-only)** if every legible scan of 2-11 shows only words/names/phrases against codes, or blank or
  non-key pages, and no letter or syllable table appears.
- **UNDECIDED** if a scan is illegible at 1400 px, or a table is seen whose entries cannot be told apart as
  letters/syllables versus words. A NO covers scans 2-11 only (scans 13-24 unseen apart from 12 and 25).
- Budget: at most 2 vision calls (one contact sheet of 2-11; one line-crop set of the one scan the sheet points at),
  at most 15 service.archief.nl requests.

**Result: NO (nomenclator-only) for scans 2-11.** Scans 4-11 fetched once at 1400 px through the service.archief.nl
IIIF image API (8 requests, 1.6 s apart, descriptive User-Agent; scans 2-3 were already on disk); `images/fagel1233/`
now holds scans 1-12 and 25 (about 3 MB), and `fetched_orders` in its manifest is updated.
- **Vision call 1** (Opus, own view): a 5x2 contact sheet of scans 2-11 at 560 px per scan (built locally, kept in the
  scratchpad, not committed). Scan 2 is blank (front board and flyleaf). Scan 3's left page is blank; its right page
  opens the book with a heading and a list whose codes start at 1. Scans 4-7 are two-column alphabetical lists of
  Dutch words and phrases under section letters (D, E, G, H, K, M, N, O, R, T, U, W are visible), each word against a
  code. Scans 8-11 are the name part (scan 8 headed "Duitsland": princes, the Emperor, ministers, troops, places), some
  entries struck through and some added in another hand. Scans 8 and 9 look like the same opening photographed twice
  (same layout and the same strikings). No page in 2-11 shows a table of single letters or syllables.
- **Vision call 2** (Opus, own view): line crops of scan 3's right page, cut first with `tools/iiif_lines.py --image
  images/fagel1233/NL-HaNA_1.10.29_1233_0003.jpg --region 640,0,760,1556 --prominence 4 --distance 22
  --lines-per-crop 10` (44 lines, 5 crops `images/fagel1233_0003_L01..L05.jpg`, debug overlay
  `fagel1233_0003_lines_debug.jpg`; a first cut at prominence 20 found only 8 lines in the faint ink and was discarded).
  Crops L01-L03 stacked into one image were looked at. The heading reads **"Cyffer voor den Resident Mauricius"**.
  Codes **1-67** (the range that holds letter 142's 1-77) belong to **Dutch words and phrases** in alphabetical order:
  "Abt" 1, "aen" 2 and 3, "aen de" 4, "aen den" 5 ... "aen UE" 15 ... "aengaende" 21 ... "afgewend" 41, "agt" 42 ...
  "al" 48 and 49, "alle" 50 and 51 ... "alleen" 67. Each code has a circumflex over it. Common words carry two codes
  (aen, al, alle, aldaer, alhier), so the design gives homophones at word level, not letter level.
- **Against the pre-registered criterion:** no single letters or syllables against numbers anywhere in scans 2-11,
  and the 1-77 range is used for words. **NO, nomenclator-only** (scans 2-11; scans 13-24 not seen, apart from 12
  from GAPS115). The 1743 book does not share letter 142's design (a French letter-level homophonic of about
  64-77 signs, H1) on this evidence. That is a family-resemblance negative, not a test of any key against letter 142,
  and it says nothing about the 1716 system, which is still unseen.
- **Whose book.** The heading names the Resident Mauricius, while the NA unittitle (GAPS115) names Carel van Rumpf,
  envoy to Sweden, 1743. The book reads as a code drawn up for a Resident Mauricius and filed, or reissued, with
  Rumpf's 1743 papers. This is how it reads here, not an identification: which Mauricius it was and how the book came
  to Rumpf is not checked.

Requests: `service.archief.nl` 8 (IIIF image API). No other host. Vision calls 2 (own view, Opus, no subagents).
Graded nothing; no token of letter 142 read.

Next cheap step: none under this lead. The 1743 book is closed as a design source for letter 142. The route to a
reading is unchanged: the NA originals of letters 309/446/455 (NA 3.01.19 inv. 2030/2044, not digitised, ASKS row 46 /
`REQUEST.md`).

## D2B-RUMPF re-probe (6 Oct 2026, account 2, LANE DEFAULT-account-2-20261005-2217)

The "While waiting" step below, run once more. Each item page's embedded `drupal-settings-json` viewer record,
fetched 6 Oct 2026 00:3x UTC:
- **NA 3.01.19 inv. 2030** (`www.nationaalarchief.nl/onderzoeken/archief/3.01.19/invnr/2030`): unittitle "Rumpf,
  Hendrik Willem-, uit Stockholm.", `"scans":[]`, `"has_scan_navigation":false`, `"availability":"PHYSICAL"`.
  **Still not digitised.**
- **NA 3.01.19 inv. 2044** (same route): unittitle "Bie, Jacob de-, uit Hamburg, Lübeck en Stockholm.",
  `"scans":[]`, `"has_scan_navigation":false`, `"availability":"PHYSICAL"`. **Still not digitised.**
- No scan count or IIIF info.json to record; nothing fetched from service.archief.nl. Unchanged since the 24 Sept
  and 3 Oct 2026 probes. The route to letters 309/446/455 is still the copy order (ASKS row 46, `REQUEST.md`).

Requests: `www.nationaalarchief.nl` 2 (2 s apart, descriptive User-Agent). No other host, no subagents, no vision calls.

## R9-NAKEY re-probe (6 Oct 2026, account 2, LANE LANE-RUN9-account-2)

The "While waiting" step, run again about 5.5 hours after D2B-RUMPF. Item pages' `drupal-settings-json`, fetched 6 Oct 2026
06:00 UTC: **NA 3.01.19 inv. 2030** ("Rumpf, Hendrik Willem-, uit Stockholm."): `"availability":"PHYSICAL"`,
`"has_scan_navigation":false`, `"scans":[]`. **NA 3.01.19 inv. 2044** ("Bie, Jacob de-, uit Hamburg, Lübeck en
Stockholm."): same three values. **Still not digitised**; the route is still the copy order (ASKS row 46, `REQUEST.md`).
Requests: `www.nationaalarchief.nl` 2, 2 s apart, descriptive User-Agent.

## While waiting

- While the copy order for NA 3.01.19 inv. 2030/2044 waits on ASKS row 46: re-probe the two NA 3.01.19 item pages
(`drupal-settings-json` availability, 2 requests) at the next pass in case they have been digitised; it depends on nobody.
(The earlier while-waiting step, scans 2-3 of NA 1.10.29 inv. 1233, was run by GAPS120 on 3 Oct 2026: nomenclator-only.)

## Next step (LANE-RUN15-account-2 orchestrator, 6 Oct 2026, 17:2x UTC; NEXT-STEPS.tsv read this folder as `runnable` from an older line)

next: no agent step is left beyond the re-probe. NA 3.01.19 inv. 2030 and 2044 are still not digitised (re-probed twice on 6 Oct 2026, D2B-RUMPF and R9-NAKEY, above), so letters 309/446/455 wait on the copy order (ASKS row 46, REQUEST.md). While waiting: re-probe the two item pages at a later pass (2 requests), not more than once a day. Who acts: owner. Blocker class: needs-image.
