found-solved
The Selected Papers of John Jay, vol. 2, 1780-1782 (ed. Elizabeth M. Nuxoll, Charlottesville: University of Virginia Press, 2012), pp. 315-316, read via its Founders Online document page (founders.archives.gov/documents/Jay/01-02-02-0126): the full letter printed with the coded passages decoded by the editors.

## QUEUE row
B1, "Book-code candidates (18 Oct 2026)" (SCOUT-BOOKCODE, account 4): John Jay to Silas Deane, 27 Oct 1780, Columbia RBML Papers of John Jay (doi:10.7916/tgw6-j233, EJ: 90295), catalogued "(Part in cipher which has not been decoded.)". Job: check-solved against the modern Jay edition per `.claude/briefs/check-solved.md`, before any decoding (CHECK-JAYDEANE).

## Premise check (CHECK-JAYDEANE, 18 Oct 2026)
(a) The folder's own mentions: none before this job -- folder created by this job.
(b) Other solvers' working files: shallow-cloned `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` (github.com, two clones) and grepped case-insensitively for "silas deane", "jay.*deane", "deane.*jay", and "jay" (word-bounded): no hit naming John Jay or Silas Deane in either repository. Neither solver has this item (expected -- it is not a cryptanalysis target, see Verdict).
(c) Physical neighbours / the cipher's own canvas: the item has 2 canvases (IIIF manifest `dlc.library.columbia.edu/iiif/3/presentation/10.7916/tgw6-j233/manifest`), fetched at low resolution (768x678 and 684x768, IIIF level0 fixed sizes, `triclops.library.columbia.edu/iiif/2/standard/ldpd:85139` and `.../ldpd:85137`). Page 1 (canvas "Page 1") is the draft letter itself, in Jay's hand, dated "Madrid 27 Oct 1780", with two coded clauses inline: "738.843.520." (one struck-through word of plaintext interlined above it, "sat verbum") and "586. 512.53.855.536.198." (also with struck-through interlined words). Page 2 (canvas "Page 2") is blank except for the docket on the back: "To Mr Deane 27 Oct [1780] In ans. to 9 Inst." and an archival mark "B.42" -- no separate decipherment slip or facing-page gloss is pasted in; the only text is the draft itself, matching Founders Online's citation ("Dft, NNC... partly in code, not decoded" -- i.e. not decoded *in the manuscript*, decoded by the modern editors).
(d) Recipient's side: Silas Deane's own papers (Deane Papers, NYHS Collections 1886-90, vol. 4 covers 1780) were not opened this job (see "Not checked" below); not needed to settle the verdict, since the sender-side modern scholarly edition already prints the full decoded text with its key named.

## Which cipher Jay used with Deane in 1780, and whether the key is printed
Founders Online's editorial note "John Jay's Use of Codes and Ciphers" (founders.archives.gov/documents/Jay/01-02-02-0003; Selected Papers of John Jay vol. 2, pp. 7-13) states Jay and Deane used a **nomenclator code** "as early as 1780" -- not a book code keyed to Entick's dictionary (the family `ciphers/sherwood-cossit-1781` and the rest of the SCOUT-BOOKCODE sweep target). "Early nomenclators were written out longhand, such as the Deane code found in Jay's code memorandum [NNC EJ: 7590]." The letter's own page (01-02-02-0126) footnotes the decoded passages: "Coded passages decoded by the editors using the Jay-Deane code, NNC (EJ: 7590, https://dlc.library.columbia.edu/jay/ldpd:50180)." That key document (Jay's code memorandum, Columbia EJ: 7590) is the period key; it is held at Columbia, not confirmed as imaged/transcribed in this repository (not opened this job -- would only matter if the reading needed independent re-derivation, which it does not for a check-solved verdict).

## Cipher form and size (from the low-resolution page-1 image)
Numeral nomenclator code: groups of 1-3 digit numbers separated by periods, written inline in the draft (not a separate cipher column or table). Two coded clauses on the one surviving page: "738.843.520." (3 groups) and "586. 512.53.855.536.198." (6 groups). Jay interlined plaintext guesses above part of the first group ("sat verbum", a Latin tag, not a decode of the numbers) and struck through draft wording near both clauses -- ordinary authorial revision, not a second hand's gloss. No image of a separate key sheet is in this item; the key is NNC EJ: 7590 (Jay's code memorandum), cited above, not this item's own canvases.

## Edition comparison (the decode as printed, Founders Online 01-02-02-0126)
"Your Favor of the 9th. Inst has come to my Hands, havg as usual been inspected--[spain wants mississippi, true they are participatin in it,] sat verbum--1 Whenever you write to me do it in full Expectation that your Letter will be opened before I get it, this being the Case with almost all I recieve--The Language of [our minister john adams] will never do--if your Suspicions prove true, Excuses will be drawn from every little Circumstance capable of affording the most trifling-- Adieu" (square-bracketed clauses are the editors' decode of the numeral groups, per the edition's own orthography note: "encrypted words and passages are indicated by small capitals... Instances of decoding that is by the editors... are enclosed in square brackets"). This matches the image: two coded clauses, two decoded clauses, same letter, same date, same two correspondents.

## Web and blog check (CHECK-JAYDEANE, 18 Oct 2026)
(a) Plain web searches: `"Jay" "Deane" cipher "27 October 1780"` (web); `"spain wants mississippi" Jay Deane` (web) -- both return only the Founders Online document page (01-02-02-0126), its Columbia source record (ldpd:85142), and surrounding Jay-Deane correspondence; no third-party discussion found.
(b) Site searches: `site:scienceblogs.de klausis-krypto-kolumne Jay Deane cipher` (Cipherbrain) -- no post mentions Jay or Deane; `site:ciphermysteries.com John Jay Silas Deane` -- returned no ciphermysteries.com pages at all (site search found nothing to open).
(c) No comment thread opened (none of the above surfaced one). `sources/cryptiana/web/bookcode.htm` (Tomokiyo, on disk, re-checked this job) documents the Jay-Deane nomenclator-code family generally ("he and Silas Deane used one as early as 1780" per the Founders editorial note it is itself cited by) but was already confirmed by SCOUT-BOOKCODE (18 Oct 2026) to have no entry for 27 Oct, 1 Nov 1780 or any date matching this letter specifically -- grepped again this job for "OCT27"/"27 Oct", no hit.

## Not checked (budget; cap $3)
Deane Papers (NYHS Collections 1886-90, vol. 4); Johnston 1890-93; Wharton's *Diplomatic Correspondence*; DECODE cache (de-crypt.org) grep. None of these can outrank the sender-side modern critical edition (Selected Papers of John Jay, 2012) that already prints the decoded text with its editors' key citation -- the "Known answer first" rule (`.claude/briefs/README.md` common tail) is already satisfied by the edition reading itself.

## Verdict
**found-solved.** The Selected Papers of John Jay, vol. 2 (2012), prints this letter's two coded clauses decoded by the editors, using the Jay-Deane code recorded in Jay's own code memorandum (NNC EJ: 7590) -- a period key, not a cryptanalytic recovery. The Columbia RBML catalogue record for the manuscript itself (doi:10.7916/tgw6-j233) still reads "(Part in cipher which has not been decoded.)", which describes the *manuscript's own state* (undecoded by the clerk/archivist), not the state of scholarship: the modern edition decoded it over a decade before this job. This is the same shape the parent already logged for sibling QUEUE row B2 (Livingston to Jay, 28 Nov 1781): "a catalogue note naming old editions is not a check of the modern edition."

**Who did not know (F-grade, README "What counts as a result"): F1.** The plaintext is in print (Selected Papers of John Jay vol. 2, pp. 315-316, 2012; freely readable on Founders Online since publication), but the specialist catalogue -- the Columbia RBML digital-library record for this exact manuscript -- does not link to that decipherment and still describes the item as undecoded. Contribution: a catalogue correction lead for Columbia RBML (cite 01-02-02-0126 against ldpd:85142's MODS record), logged here, not acted on by this worker (outreach gates, CLAUDE.md "Outreach").

**Key source:** period (Jay's own code memorandum, NNC EJ: 7590, used by the edition's editors — not recovered by this project).

```
$ python3 tools/intake_gate_check.py jay-deane-1780
jay-deane-1780: found-solved (line 1) -- edition/page or full-text-search citation found within 6 lines
exit: 0
```

## Next step
No cheap test open: the target is already found-solved by a modern critical edition with a named period key, not a cryptanalysis or recovery candidate. Recommend: (1) do not promote to the board (rule 3, "editions are dropped" -- this is now an edition-read item); (2) optional F1 catalogue-correction note to Columbia RBML, gated through the Outreach rules (AUDIT.md/N-class first) if the orchestrator wants the contribution credited in CONTRIBUTIONS.md; (3) QUEUE.md's B1 row should be struck/updated to found-solved, matching B2.

## While waiting
Nothing here is blocked on an outside party; no wait-only action applies.
