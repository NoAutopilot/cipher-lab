# BnF Clairambault 331 (1530), f.15 / f.149 / f.156 -- three "undeciphered" Italian letters per Tomokiyo

found-solved

dbourdeau/cyphersolver (shallow clone, commit 648309e, fetched 27 Sept 2026) read in full by this worker for
`targets/rangone1530/` and `targets/joachim1530/`: two of this candidate's three letters (f.15 and f.156) are
already read there, publicly, since 22-23 Sept 2026 -- before this scouting pass. The third (f.149) was checked
by that same project as a sibling and found to be a different, unattempted cipher.

## Summary (read this first)

This target was queued by `SCOUT-OWN-7` (QUEUE.md "SCOUT-OWN-7 key-adjacent candidates" row 3, 27 Sept 2026,
07:5x UTC) from `KEY-ADJACENT.tsv` row 3, on the strength of Tomokiyo's `francis.htm` page (`sources/cryptiana/
web/francis.htm`, section "BnF Clair.331 (1530)"), which the scout's own row summary paraphrased as "key printed
(Gramont's cipher, 1530); a decode.json config for Gramont's cipher already exists". **That paraphrase is wrong**
(see "Correction to KEY-ADJACENT.tsv / QUEUE.md" below) -- but the search this brief required turned up something
the scout pass did not check at all: **George/David Bourdeau's solver repository (`github.com/dbourdeau/
cyphersolver`, one of the two repositories CLAUDE.md rule 1 requires searching) has already read two of the three
letters**, ciphertext-only, published on its GitHub Pages site since 22-23 Sept 2026:

| Letter (Tomokiyo) | Bourdeau target | Status there | Fraction read | Bourdeau's own date |
|---|---|---|---|---|
| f.15, Guido Rangone to Montmorency, "10 Feb 1530" (Tomokiyo's heading text); Clair.331 copy of the original BnF fr.3070 f.81, dated 10 Jan 1530 | `targets/rangone1530/` (paired with the sibling Clair.330 f.206 = BnF fr.3082 f.42, 24 Dec 1529) | "read in part" | 232/264 signs, 87.9% | 22 Sept 2026 |
| f.149, Signor [Jean] Joachim to Montmorency, 13 March 1530 | checked as a sibling inside `targets/joachim1530/` ("reopened manuscript f. 149, Gallica f141; its Greek/geometric inventory is different... does not supply this account's key") | **not read** -- different, unattempted cipher | -- | 23 Sept 2026 |
| f.156 (Tomokiyo's heading), full extent f.156r-157v, "from London to the King or Montmorency", "a list of sums" | `targets/joachim1530/` (Bourdeau's own title: "Passano's account of Wolsey's assets, London, March 1530"; catalogue item 281) | "read" (meets the repository's own >=95% bar for a partial key) | 386/402 tokens coherent, 96.02% | 23 Sept 2026 |

So of the three letters this candidate bundled together, **two are already substantially read by a public
solver repository this project is required to check**, and the third (f.149) is confirmed by that same project's
own sibling check to be a *different* cipher inventory that nobody -- including Bourdeau -- has attempted. This
target is not a fresh cryptanalysis or recovery opportunity as scoped; f.149 alone might still be one, but it
would need its own target folder and its own campaign, not a shared one with the other two.

Per CLAUDE.md rule 10, this worker reports what was found and where; it does not classify novelty (N0-N5) --
that is a verifier's job, and nothing here should be read as a novelty verdict for Bourdeau's readings or for
f.149.

## (a) What Tomokiyo's francis.htm actually says (not what KEY-ADJACENT.tsv/QUEUE.md paraphrased)

Read in full (`sources/cryptiana/web/francis.htm`, on disk, lines ~121-150; raw HTML re-read for section
structure, not just the flattened text, since the flattened text loses which `<H3>`/`<H4>` heading a paragraph
sits under):

- H3 "BnF Clair.330 (1529)" (line 121, Gallica `btv1b9000769q`): "The following three letters can be read with
  **Bayonne's Cipher (1529)**" -- f.16, f.71, f.85, all Bishop of Bayonne to Montmorency. This is a *different*
  cipher (Jean du Bellay, Bishop of Bayonne's own, broken by Lasry in 2022) from either Gramont cipher below.
- Nested inside that same Clair.330 section, H4 "**Gramont's Cipher (1529)**" (line 128): f.53 (Gramont to
  Montmorency, 5 Oct 1529, broken by Lasry 2022, reused in fr.3040 f.16 and fr.3091 f.45), and immediately below
  it, still under this H4, **f.206 (24 Dec 1529) Conte Guy [Guido] Rangone to Montmorency** (line 138) -- i.e.
  Tomokiyo files Rangone's own Clair.330 letter under "Gramont's Cipher (1529)", not under Bayonne's Cipher.
- H3 "**BnF Clair.331 (1530)**" (line 143, Gallica `btv1b9000761d`): "There are three undeciphered letters in
  Italian." f.15 (10 Feb 1530 per the page heading; the same line also gives "10 January 1530" for the letter's
  own date -- Tomokiyo gives both, unresolved by him) **"(The cipher seems to be the same as the one used in BnF
  Clair.330 above.)"** f.149 (13 March 1530), f.156 (15 March 1530, "a list of sums", explicitly "a different
  style from others presented in this article").
- H3 "**BnF fr.2980 (1530)**" (line 190, Gallica `btv1b9059991d`): f.29/f.30 (Gramont to Villandry, 20 May 1530)
  "can be read with **Gramont's cipher (1530)** below."
- H3 "**BnF fr.3019**" (line 213, Gallica `btv1b9059994n`): f.20 (Gramont to Grand Master, 31 Aug, no year given
  on this page) is where "the cipher (called **Gramont's Cipher (1530)** herein) can be reconstructed as
  follows" -- this is the cipher this repository's `ciphers/fr2980-gramont/` and `tools/tests/decode_configs/
  fr2980-gramont.json` already implement (confirmed by reading `ciphers/fr2980-gramont/NOTES.md` lines 1-40 and
  `key.tsv`'s header rows, which cite "Lasry"/"Tomokiyo" and the fr.3019/fr.2980 reconstruction, not Clair.330).

**So Tomokiyo names two distinct "Gramont" ciphers on this one page**, one dated 1529 (Clair.330 f.53/f.206,
fr.3040, fr.3091) and one dated 1530 (fr.3019, fr.2980) -- he gives them different names precisely because they
are different substitution alphabets. Clair.331 f.15's parenthetical says only "the same as the one used in BnF
Clair.330 above", which -- given Clair.330 itself carries *two* named ciphers (Bayonne's 1529 for the Bishop's
own letters, and Gramont's 1529 for f.53 and for **Rangone's own other letter, f.206**) -- most plausibly means
the Gramont's Cipher (1529)/f.206 cipher, since f.15 is also a Rangone letter (same sender as f.206). Either
way, it is **not** "Gramont's cipher (1530)" (the fr.3019/fr.2980 cipher): that cipher is never mentioned in
connection with Clair.331 anywhere on the page. Bourdeau's independent, ciphertext-only key recovery for f.15
(see above) confirms this reading is right: his homophonic ~50-sign Italian key for fr.3070 f.81/fr.3082 f.42
(Clair.331 f.15's original / Clair.330 f.206's original) is not the Gramont's-cipher-1530 key on file in
`ciphers/fr2980-gramont/key.tsv` (a different sign set, different language pairing target -- Gramont's is French,
Rangone's is Italian).

Tomokiyo prints **no plaintext** of f.15, f.149 or f.156 anywhere on this page (confirmed: no `<TABLE>` of
symbol->letter values and no decoded prose anywhere in the Clair.331 section or the two Gramont sections; the only
image tied to Clair.331 is `francisBnFClair331f157.png`, a photograph of the ciphertext itself, captioned as an
example of the "different style" third letter, not a decipherment). He does print a reconstructed **key** (as an
image, `GL/BnF_Clair330_f53_decipher.png`) for Gramont's Cipher (1529) -- the cipher f.15 probably shares -- but
that is a key, not a plaintext, and per this brief's own instructions ("a printed key with no plaintext leaves
the item open as key-adjacent") that alone would leave f.15 `open`, not `found-solved`. It is Bourdeau's
independent ciphertext-only work, not anything on Tomokiyo's page, that actually reads f.15 and f.156.

## (b) Is `ciphers/fr2980-gramont`'s key the same cipher Tomokiyo names for Clair.331?

**No.** `ciphers/fr2980-gramont/NOTES.md` (lines 1-19) and `key.tsv` (header rows, e.g. `x A H Lasry A...`)
describe the cipher Tomokiyo calls "Gramont's cipher (1530)" (his own H3 "BnF fr.3019" section, reconstructed by
Tomokiyo/Lasry from fr.3019 f.20 and applied to fr.2980 f.29-30, both French-language Gramont-to-royal-official
letters). Clair.331 f.15's own parenthetical points at "the one used in BnF Clair.330 above" (Bayonne's Cipher
1529, or -- more likely, as argued in (a) -- the separately-named Gramont's Cipher 1529 used for f.53 and for
Rangone's own f.206), never at the 1530/fr.3019 cipher. These are two different ciphers by Tomokiyo's own
naming and dating. Confirmed independently: Bourdeau's ciphertext-only key for f.15 (homophonic, ~50 signs,
Italian, `targets/rangone1530/key.json`) does not match `ciphers/fr2980-gramont/key.tsv` (which is French,
different sign inventory, different homophone counts). **The existing fr2980-gramont decode config cannot be
reused for f.15/f.149/f.156**, and there was never a reason to price a decode pass against it for this target.

## (c) Editions read by this worker (not by citation)

- **Decrue, *Anne de Montmorency ... a la cour, aux armees et au conseil du roi Francois Ier* (1885).** Full
  view on Google Books (id `gTUOAAAAQAAJ`, `viewability: ALL_PAGES`, found via `www.googleapis.com/books/v1/
  volumes?q=%22Decrue%22+%22Anne+de+Montmorency%22&country=US&key=$GOOGLE_BOOKS_KEY`) and separately digitised
  on Internet Archive (`archive.org/details/annedemontmorenc00decruoft`, 1885, and three related IA copies/
  editions of the same title, 1885 and 1889). Google Books' search-within-volume endpoint
  (`tools/gbooks_search_within.py gTUOAAAAQAAJ Rangone Joachim Passano`, one call, both terms) hit: "Rangone" on
  printed pp.181, 182, 222, 239, 269, 286, and the index at p.447 ("RANGONE (Guido, comte), 181, 222, 239, 269,
  82, 286"); p.182's snippet reads **"... Rangone (Clai-rambault, 330, 2751; fr. 3070, 81)"** -- i.e. Decrue in
  1885 already knew and cited by shelfmark both the Clairambault copy and the fr.3070 original of the very
  letter Bourdeau independently rediscovered and read in 2026. "Joachim"/"Passano" hit only pp.57 and 93 (index:
  "Joachim de Passano, seigneur DE, 57, 93"), nowhere near the March 1530 London material (ff.156-157) or a
  page number matching f.149. I could not read the full page text itself (`books.google.com` page/text view is
  captcha-blocked from the cloud per CLAUDE.md's host table; the IA scan `annedemontmorenc00decruoft`'s own
  `_djvu.txt`, fetched and grepped directly, has **zero** hits for "Rangone" or any OCR-garbled variant tried,
  against Google's own confirmed hits on the same title -- a scan/OCR-quality discrepancy between the two
  copies, not a negative; the pp.181-182 footnote content itself is unread by this worker). This is evidence
  Decrue cites the shelfmark, not evidence he printed a decipherment or that the cipher passage itself was
  ever deciphered by him -- flagged here for whoever eventually does the N-class/AUDIT.md pass on f.15, not
  resolved by this worker (rule 10: this is check-solved, not verification).
- **Catalogue des actes de Francois Ier**: not opened this pass (not located as a single full-view/full-text
  volume by title search in the time available; named as an unopened next step below, low priority given the
  Bourdeau finding already answers the check-solved question for f.15/f.156).
- **Le Glay, *Negociations diplomatiques entre la France et l'Autriche*** (1845): not opened this pass, same
  reason.
- **Calendar of State Papers Spanish / Letters and Papers Henry VIII, March 1530**: not opened this pass. Note
  Bourdeau's own `targets/joachim1530/NOTES.md` records that *Letters and Papers Henry VIII* IV no.6307 covers a
  related Passano dispatch dated **4 April 1530** (not this March account) and states this was checked and
  ruled out as the plaintext of the London account.
- These three editions are named `open, not read` rather than `blocked`: no attempt to open them was made this
  pass (time/cap), not a failed attempt. If the parent wants f.149 pursued as its own target, opening these for
  the March 1530 London/Joachim material specifically (not just Rangone) is the named next step.

## (d) DECODE (login-free listing)

The existing full crawl (`sources/decode/records-non-decrypted-2026-09-24.tsv`,
`sources/decode/records-decrypted-2026-09-24.tsv`, both dated 24 Sept 2026, `tools/decode_list.py`, no login)
was grepped rather than re-crawled (both files already cover the whole catalogue by status; re-running
`decode_list.py` would just reproduce the same rows at cost). No hit for "Clairambault 331", "Clair.331", or
"331" combined with "Rangone"/"Joachim"/"Passano" in either file; Clairambault 325, 328 and 417 are present,
331 is not. DECODE has no record at all for this target's three letters, decrypted or not (Bourdeau's own
`rangone1530/NOTES.md` separately confirms it worked from DECODE record **R4249**, which is the *original*
BnF fr.3070 f.81, catalogued there as "Non-decrypted" before Bourdeau's own read -- not the Clairambault copy).

## (e) Solver repositories (rule 1)

Both cloned shallow (`git clone --depth 1`) to the session scratchpad and grepped, not re-derived from
citation:

- **`github.com/dbourdeau/cyphersolver`** (commit `648309e`, fetched 27 Sept 2026): see Summary table above.
  `targets/rangone1530/` and `targets/joachim1530/` read in full (NOTES.md, reading.md/READING.md,
  profile.json). Cross-checked against `CATALOGUE.md` (items 181, 281), `SOLVED_CATALOGUE.md` (rows 109, 120)
  and `SOLVED_RANKING.md` (rows p122, p135) -- all consistent with the target-folder NOTES.md, all dated 22-23
  Sept 2026, all with a public write-up at `dbourdeau.github.io/cyphersolver/{rangone1530,joachim1530}.html`
  (confirmed reachable independently by `WebSearch`, not just present in the clone -- both pages surfaced
  unprompted in two separate queries, "Clairambault 331 Rangone Montmorency cipher" and "Passano Wolsey London
  1530 cipher Clairambault decipher"). Bourdeau's code is MIT-licensed, his text CC BY 4.0 (CLAUDE.md rule 8):
  the summary table above and the direct quotes are attributed, nothing copied as our own.
  Side note, out of this brief's scope: a Bourdeau GitHub PR/issue title surfaced by the same web search
  ("Catalogue 328 (BnF fr.2980 nos. 21-22, Gramont, Rome, 20 May 1530): partial readings with the Gramont 1530
  key") suggests Bourdeau's project has also independently worked fr.2980 (this repository's own
  `ciphers/fr2980-gramont`, status `partial`) -- not investigated further here (out of scope for a check-solved
  worker on a different target), flagged for whoever next touches that target.
- **`github.com/aaymeloglu/unsolved-ciphers`** (commit `2495c45`, fetched 27 Sept 2026): grepped for
  "Clairambault 331", "Clair. 331", "Rangone", "Passano", "Joachim" across every `.md`/`.tsv`/`.csv`/`.json`
  file. No hit anywhere in the repository (the only "Passano" hit anywhere in either clone's non-Bourdeau
  material was an unrelated PARES catalogue row, `catalogue/pares-ranked.md` line 162, "Comisión conferida por
  los genoveses a Felipe de Passano" -- a different, 1579 Passano, unrelated). No licence on this repository
  (CLAUDE.md rule 8): cited, nothing copied.

## (f) Web search (rule 1, first source)

`WebSearch`, two queries: `Clairambault 331 Rangone Montmorency cipher` and `"Passano" Wolsey London 1530
cipher Clairambault decipher`. Both returned Bourdeau's own GitHub Pages write-ups and PR/issue titles as the
top cipher-relevant hits (see (e)); no independent (non-Bourdeau) decipherment, edition or announcement located.
Per check-solved.md's added source family, also considered "solves"+"Claude"/"GPT" model-announcement searches:
not run separately this pass, since the only genuine hits either query returned were Bourdeau's own work,
already covered in full above; no AI-lab or evaluation-company blog post about this target surfaced in either
query.

## (g) Cryptiana comment threads / DECODE / Cipherbrain (rule 1)

Not separately searched this pass beyond the two Tomokiyo pages already read (`francis.htm` in full) and the
DECODE listing snapshot -- given the Bourdeau finding already settles the check-solved question for f.15/f.156,
and f.149 (the one open letter) has no cipher-family match anywhere found so far, a Cipherbrain/comment-thread
sweep was judged lower priority than reporting this finding promptly. Named as an unopened step if f.149 is
later spun out as its own target.

## Correction to KEY-ADJACENT.tsv / QUEUE.md

`KEY-ADJACENT.tsv` row 3 and `QUEUE.md`'s "SCOUT-OWN-7 key-adjacent candidates" row 3 both describe this
candidate's key status as **"key printed (Gramont's cipher, 1530)"** and cite "a decode.json config for
Gramont's cipher already exists in tools/tests/decode_configs" as a reason it looked cheap. Per (a)/(b) above,
this is a scout-pass misreading: the sentence "These undeciphered letters can be read with Gramont's cipher
(1530) below" appears on `francis.htm` under the **BnF fr.2980 (1530)** heading, about fr.2980 f.29/f.30, not
under Clair.331 -- the row's own "Description" column concatenates text from both sections without preserving
which heading each sentence sits under. `francis.htm` never names Gramont's cipher (1530) in connection with
Clair.331 anywhere. This worker did not edit `KEY-ADJACENT.tsv`/`QUEUE.md`'s row text directly (out of this
brief's scope, and the row's job -- flagging a candidate for a scout pass -- is now moot once this folder
exists); the parent should retire or correct that row when it reads this NOTES.md, since a later scout pass
could otherwise re-queue the same wrong premise for a different target that also cites row 3.

## What's actually left (f.149)

f.149 (Signor Joachim to Montmorency, 13 March 1530) is the one genuinely open item. Per Bourdeau's own sibling
check (`targets/joachim1530/NOTES.md`, "siblings" escalation line): "reopened manuscript f. 149, Gallica f141;
its Greek/geometric inventory is different. Its heading/body dating is inconsistent. It does not supply this
account's key." That is the only description of f.149's cipher on file anywhere (Tomokiyo does not describe its
sign system at all, only that it exists). Nobody -- not this project, not Bourdeau -- has attempted f.149 as a
cryptanalysis target. If pursued, it needs: (1) its own transcription from the Gallica image (canvas ~141,
`btv1b9000761d`, offset unconfirmed -- Bourdeau's own note flags "heading/body dating is inconsistent" as a
live uncertainty about which canvas is f.149 itself vs. its neighbours), (2) the three unopened editions in (c)
above read specifically for March 1530 London/Joachim material, and (3) its own target folder and check-solved
pass, separate from this one (this folder's verdict covers f.15 and f.156 as found-solved; f.149 should not
inherit that verdict by being bundled in the same folder).

## Sources checked (date, method) -- CLAUDE.md rule 1 order

1. Search engine (web): 27 Sept 2026, `WebSearch`, two queries, see (f). Found Bourdeau's public write-ups.
2. Sender's/recipient's printed correspondence: 27 Sept 2026, Decrue 1885 (Google Books full view + IA scan),
   see (c). Shelfmark citation found, page content unread.
3. Calendars/state-paper series: 27 Sept 2026, not opened this pass (Catalogue des actes de Francois Ier, Le
   Glay 1845, CSP Spanish/L&P Henry VIII) -- named next step for f.149 only, see "What's actually left".
4. Comment threads (Cryptiana blog, Cipherbrain): not separately swept this pass, see (g).
5. DECODE (de-crypt.org): 27 Sept 2026, existing 24 Sept crawl grepped, see (d). No record for Clair.331.
6. Solver repositories, both: 27 Sept 2026, shallow-cloned and grepped in full, see (e). Bourdeau: two of
   three letters already read. Aymeloglu: no hit.
7. Tomokiyo's own text: 27 Sept 2026, `sources/cryptiana/web/francis.htm` read in full (both the flattened
   text and the raw HTML for section structure), see (a).

## Requests

gallica.bnf.fr: 1 (manifest.json fetch for `btv1b9000761d`, to confirm the ark and shelfmark before citing it;
confirmed "BnF. Departement des Manuscrits. Clairambault 331", "1530, janvier-mars", 237 canvases, no folio
labels on this manuscript -- like fr.16092, per-folio anchoring would need eye-checked `--anchor` pairs, not
attempted this pass). archive.org: 2 (advancedsearch for the Decrue IA copies; one `_djvu.txt` fetch). Google
Books API: 2 (`volumes?q=...` search, `gbooks_search_within.py` one call with three words). GitHub: 2 shallow
clones (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`), no API rate limit concern (git protocol).
All well under any per-host cap; no 429/403 encountered.

## intake_gate_check.py

```
$ python3 tools/intake_gate_check.py clair331-rangone-montmorency-1530
clair331-rangone-montmorency-1530: found-solved (line 3) -- edition/page or full-text-search citation found within 6 lines
```
exit 0.
