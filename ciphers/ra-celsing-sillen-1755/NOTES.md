# Gustaf Celsing letter-drafts to Sillén with cipher key, 1755-1764

**Status: open**

## Item

Letter-drafts ("brevkoncept") by Gustaf Celsing (1723-1789, Swedish minister to the Ottoman Porte at
Constantinople) to Georg Wilhelm af Sillén, 1755-1757 and 1760-1764 (some undated), with a further draft to
Count Ekeblad (3 May 1763) and one undated to Nensén, filed with a cipher key ("Chiffernyckel") in the same
volume. Shelfmark SE/RA/721512/II/II 1/II 1 B/4 ("Beskickningsarkivet från Biby", sub-series "Beskickningarna
till Konstantinopel 1737-1779 / Korrespondens / Korrespondens med hemlandet"), Riksarkivet i Stockholm/Täby.
Same fonds as R1 (father and son, one archive: Gustaf Celsing 1723-1789 is Ulric Celsing's father). Found by the
LANE S scout of 24 September 2026, QUEUE.md row R2, kind: recovery. Catalogue note in full: "Brevkoncept av
Gustaf Celsing till Georg Wilhelm af Sillén 1755-1757, 1760-1764, odat. Med ett brevkoncept av Gustaf Celsing
till greve Ekeblad 3 maj 1763 samt ett odaterat till Nensén. Med chiffernyckel."

No transcription or image exists in this repository; `ciphertext.txt` is not created (rule 2 — no transcription
exists to transcribe from).

## Check-solved sweep, 24 September 2026

Run directly by this worker, per `.claude/briefs/check-solved.md`'s six sources. 6/6 checked, 0/6 found a
solution, key transcription, or documented prior attempt.

**Editions first:** no published edition of Gustaf Celsing's correspondence with Sillén, Ekeblad or Nensén was
located. The Svenskt Biografiskt Lexikon article on Gustaf Celsing (`sok.riksarkivet.se/sbl/Artikel/14753`,
fetched directly) notes only that "Riksarkivet förvarar hans talrika ämbetsskrivelser" (the National Archives
preserves his numerous official writings) with no mention of Sillén or a cipher, and no reference to a printed
edition. A period narrative (Verner von Heidenstam's *Karolinerna*, `runeberg.org/karolin/102.html`, surfaced by
web search) fictionalises an episode of Celsing's Constantinople mission but is a literary work, not an edition
of his letters, and does not mention Sillén or a cipher either. No 18th/19th-century calendar or diplomatic
correspondence series specific to this legation's home correspondence was identified this pass.

**Web:** WebSearch "Gustaf Celsing Sillén brevkoncept chiffernyckel" — results are biographical only (SBL,
runeberg.org, Wikipedia on unrelated Celsing family members), no mention of this correspondence or cipher.

**Community lists:** `sources/cryptiana/` grepped for "celsing" and "sillén"/"sillen" — no hits (a "sillen"
substring hit in `matignon1586/lm_v1.pkl` inside the solver-repo grep below is a binary false positive, not a
real match, checked by eye).

**DECODE:** not logged separately from R1 — same session, same negative result (no login attempted per this
brief; `site:de-crypt.org` web search for these names returned no indexed de-crypt.org pages at all).

**Bourdeau:** same shallow clone as R1. `grep -rli "celsing"` matches only `roell1809/turk_inv.txt` (see R1's
NOTES.md — an unrelated Dutch inventory naming G. Celsing as a real 1750s-60s figure, not this item).
`grep -rli "sillén\|sillen"` matches `labbe1582/segment_sweep.tsv` and `matignon1586/lm_v1.pkl` — both checked
by eye and are coincidental substring matches inside frequency/model data files, not references to Sillén.

**Aymeloglu:** same shallow clone, same greps, no matches.

**Riksarkivet digitisation check:** same query as R1 (`text=chiffernyckel Celsing&type=Record`, 2 hits, one 200
after one retried transient `SSL_ERROR_SYSCALL`). This item's record, SE/RA/721512/II/II 1/II 1 B/4:
`onlyDigitisedMaterials: false` — **not digitised**. No IIIF manifest or image link.

**Verdict:** open. No prior solution, key transcription, or attempt found anywhere searched. As with R1, the
catalogue explicitly files a cipher key with the letters (LESSONS.md's "key beside the letter" pattern), which
is the strongest lead — unconfirmed until the physical volume is seen, since the note does not say which
specific letters the key applies to.

**Not digitised — copy order needed.** See REQUEST.md.

## Request log

24 Sept 2026: no personal data logged here.
