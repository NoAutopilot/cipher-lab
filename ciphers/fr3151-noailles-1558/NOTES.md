open

Charrière, Négociations de la France dans le Levant, tome II (Paris, 1848; archive.org `ngociationsdel02charuoft`) read as full text (grep, whole volume) by this worker for "Noailles"/"Acqs"/date and place terms, 26 Sept 2026: no decipherment or clear-text rendering of this letter. Ribier, Lettres et mémoires d'estat (Paris, 1666), both tomes, already cached full text on disk (`sources/ia-fulltext/print-check/bub_gb_{bOnmNv2ZLVoC,qWTswSr32NYC}_djvu.txt.gz`) re-grepped by this worker for "Noailles"/"d'Acqs": zero hits in either tome.

# BnF fr. 3151 no. 33 — François de Noailles (Venice) to the Cardinal de Lorraine, 13 Nov 1558

QUEUE row: G10 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`), catalogue item 10 at
dbourdeau.github.io/cyphersolver/catalogue.html. This target and `ciphers/fr3151-seure-1558` (Seure, nos. 39-44)
and La Guiche fr. 3138 no. 22 share Bourdeau's catalogue entry 10 but are three separate items/keys. This job
(LANE NX, `.claude/briefs/runs/2026-09-26-lane-nx-3151n33.md`) covers only no. 33. Do not edit
`ciphers/fr3151-seure-1558/`.

**Correction to the job brief's guess of the addressee.** The brief guesses "likely Montmorency"; Bourdeau's own
`guiche1551/NOTES.md` (fetched fresh from GitHub raw, `dbourdeau/cyphersolver@main`, 26 Sept 2026 08:52 UTC, so
current, not the stale 21 Sept snapshot) identifies the letter precisely: **"Noailles → Cardinal de Lorraine,
Venice, 13 Nov 1558 (fr. 3151 no. 33)."** François de Noailles, bishop of Dax (Acqs), was French ambassador at
Venice from Sept 1557 (WebSearch, confirmed against Charrière's introduction to his correspondence, tome II
p.405-406: Henri II's 26 Sept 1557 letter names him taking over the Venice post from the bishop of Lodève).

## Six-source search log (26 Sept 2026, this worker)

1. **Standard edition / calendar.** François de Noailles's Venice correspondence with **La Vigne** (his
   opposite number at Constantinople) is printed at length in Charrière's *Négociations de la France dans le
   Levant* (4 vols, 1848-1860); tome II covers 1547-1566 and includes about 20 "Venise, [date] 1558" letter
   headers running January-November 1558 (lines located by grep: 10 janv., 1 févr., 26 févr., 4/26 avril, 8/28
   juin, 5 juil., 23/30 juil., 18/27 août, 20/28 sept., 7 nov., 15 nov. 1558). None is dated 13 November, and none
   of the surrounding correspondence (which is Noailles-La Vigne Ottoman-affairs traffic, not Noailles-to-Lorraine)
   mentions Candia, Corfu or the Levant galleys in the terms Bourdeau's note describes for no. 33. Full-volume grep
   for "chiffr"/"déchiffr" finds no printed decipherment near any 1558 Venice letter (one hit, "mectre en chiffre"
   in the 4/26 April letter, is Noailles asking to *have something enciphered*, not a printed clear reading).
   Ribier (1666, both tomes) never names Noailles or "d'Acqs" at all (zero hits either tome) — consistent with
   `ciphers/fr3151-seure-1558/NOTES.md`'s prior finding that Ribier does not cover this ambassador. Vertot/Villaret,
   *Ambassades de Messieurs de Noailles en Angleterre* (1763), is Antoine/Gilles de Noailles's **England** embassy,
   a different brother and a different posting (WebSearch turns up nothing connecting it to François at Venice);
   not opened this pass, flagged if this target is promoted. **Cuisiat's 1998 edition of the Cardinal de Lorraine's
   own letters (*Lettres du cardinal Charles de Lorraine, 1525-1574*, Droz) is his outgoing correspondence, not
   letters he received** (per the publisher's and reviewers' description, WebSearch) — the wrong direction for a
   letter Noailles *sent to* the Cardinal, so it is not a candidate edition for this item even though the
   correspondent matches; not opened (no accessible full text found this pass; flagged, not claimed as read).
2. **Tomokiyo (sources/cryptiana/ on disk).** No page for François de Noailles's Venice posting or fr. 3151 found
   in the local mirror. henryiii.htm covers François de Noailles's *later* Constantinople embassy (from 1571) and
   his cipher there (BnF fr. 16142) — a different posting, different cipher, more than a decade later; not the
   same key. The one "3151"-adjacent string match (codebreaking.htm, "31511" inside a Zimmermann-telegram code
   group) is a false positive.
3. **Lasry's publications.** No Lasry solution of fr. 3151 or a Noailles/Venice 1558 cipher found via Tomokiyo or
   web search.
4. **DECODE + both solver-repo clones.** No DECODE record for fr. 3151 in the local snapshot (`sources/decode/`)
   or in Aymeloglu's DECODE catalogue scrape (`catalogue/decode-catalog.csv` in his repo, re-cloned this pass —
   the one numeric "3151" hit there is DECODE record id 3151, an unrelated 1919 US postcard). Bourdeau's repository
   (re-fetched fresh from GitHub raw at 08:52 UTC and from the live catalogue page at 08:55 UTC, both 26 Sept
   2026, so current): `guiche1551/NOTES.md` §2 states plainly for no. 33 — "Read at the time; the cipher itself
   (about 150 signs, a different symbol alphabet) was not attacked. A full reading would need the page opened
   flat, or a solve using the visible gloss words as cribs." The live catalogue's item-10 row (fetched 08:55 UTC)
   repeats this unchanged: "Noailles (no. 33) read at the time: see guiche1551/" — confirms the escalation log's
   "not-attempted" for the cipher itself still holds as of today, not stale. Aymeloglu's `unsolved-ciphers` repo
   (re-cloned shallow, 26 Sept 2026): no fr.3151/Noailles hit (the two string matches, "3151" in the DECODE-catalog
   CSV and "noailles" in a French word-frequency lexicon file, are both unrelated).
5. **Web-search / model-solve announcements.** "fr.3151" + Noailles/Venice cipher: no hit (only unrelated Venetian
   cryptography scholarship, e.g. Pasini 1872, Amadi manuscript studies). Vals AI / "Claude solves" model-solve
   coverage since Sept 2026: the only historical-cipher item found is Claude Fable 5.1's Urquhart *Cyphral
   Distich*/*Octastich* (1653, unrelated target, unrelated cipher).
6. **Ciphertext confirmed present, and the marginal gloss independently read from the image (this worker, step 2
   below).**

## Verdict

**Open.** No source of the six, nor a fresh direct check of the live Bourdeau catalogue, shows the ~150-sign
cipher of no. 33 itself ever attacked or solved; only the manuscript's own contemporary marginal decipherment
of parts of the two short cipher blocks exists (confirmed independently from the image, see below), and it does
not by itself constitute a modern reading of the cipher. Rule 10: no novelty claim made; this is a search result,
not a verifier's classification.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 10, `guiche1551/`
working folder), CC BY 4.0 — identified the letter, its addressee and date, and the marginal gloss; not an attempt
at the cipher itself.

`python3 tools/intake_gate_check.py fr3151-noailles-1558` output:
```
fr3151-noailles-1558: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit: 0
```
