# Gustaf Celsing letter-drafts to Sillén with cipher key, 1755-1764

**Status: blocked**
No standard edition identified or opened for Gustaf Celsing's letter-drafts to Sillen; archive.org full-text search for Celsing+Sillen+chiffer returned 52 hits (army lists, Historisk tidskrift snippet about Celsing as royal secretary, unrelated) and none naming the cipher key, and the Riksarkivet record is recorded as not digitised (onlyDigitisedMaterials false, 24 Sept 2026 worker).

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


## Web and blog check (CS-A2-C, 2 Oct 2026)

WebSearch queries (standard) and what they returned:
- Gustaf Celsing Sillen 1755 chiffernyckel brevkoncept Konstantinopel (biographical and museum pages only)

Blogs: Cipherbrain, Cryptiana blog and Cipher Mysteries were covered by the restricted web searches above and a local grep of `sources/cryptiana` and `sources/ciphermysteries`; 0 hits for the sender, recipient or shelfmark; no comment thread opened because no hit was relevant.

archive.org full-text (be-api, one request at a time, 2 s apart, unquoted-token behaviour so counts are upper bounds):
- Celsing Sillen chiffer (52, none relevant)

Solver repositories (shallow clones, grep only, 2 Oct 2026): celsing: only Bourdeau roell1809/turk_inv.txt (unrelated Dutch inventory); sillen: only coincidental substring files; Ekeblad/Nensen 0. Aymeloglu cited, no code used.

DECODE: local grep of sources/decode (records-non-decrypted 24 Sept 2026 and later key lists) for the sender/recipient names: 0 rows; the 2 Oct 2026 login-free crawl (801 rows) by CS-A2-B is the same list. Live de-crypt.org not queried by this worker.

## Premise check (CS-A2-C, 2 Oct 2026)

- (a) found, unread: the catalogue note says "Med chiffernyckel" (key filed with the drafts); no decipherment mentioned.
- (b) not found: no Celsing/Sillen working file in either solver repo.
- (c) unreachable: not digitised (Riksarkivet record SE/RA/721512/II/II 1/II 1 B/4); no neighbour leaf viewable.
- (d) not found/unreachable: Swedish recipient-side editions (Rikskansliets and Hattarnas-era publications) were not identified; next: search Historisk tidskrift and Svenska riksarkivets publications for Celsing's Porte correspondence.

Verdict: blocked. No solution, key, plaintext or documented attempt was found in anything searched, but no edition could be opened, so this is a search result for the log and not a statement that none exists. Status was `open` before this pass and failed the intake gate.
