# Rufus King printed correspondence, vols III-IV (ARM3-LIVCODE U3, 26 Sept 2026)

*The Life and Correspondence of Rufus King* (ed. C.R. King, 1894-1900), public domain, fetched via
`_djvu.txt` on archive.org (note: `archive.org/download/<id>/<id>_djvu.txt` needs `-L` to follow a
redirect; a bare `curl -sS` without `-L` silently returns 0 bytes -- worth adding to the Access
playbook's own notes, not done here, out of this job's file list).

- Vol III: `lifecorresponden03king` (1,496,280 chars). Year histogram confirms this volume is almost
  entirely 1799-1801 material (313 hits for "1800", 271 for "1801", only 1-2 each for 1802-04) --
  **before** Robert R. Livingston arrived in Paris (Dec 1801), so it carries no Livingston-Paris
  cipher correspondence at all; every "Livingston" hit in this volume is either an unrelated New York
  political mention (Brockholst Livingston, Edward Livingston) or Robert R. Livingston discussed
  third-person before his appointment. 31 cipher/cypher hits, all 1798-1800, about King's own
  London-legation cipher with the Secretary of State and about "a new cipher & the counterpart of
  Mr. Jay's cipher" (1799, unrelated to WE027 or Livingston).
- Vol IV: `lifecorresponden04king` (1,538,691 chars). Year histogram centers on 1802-1804 (213/151/150
  hits for 1803/1804/1802) -- the right volume for this job's window. 6 cipher/cypher hits, all marked
  `* Italics in cipher.` -- **the editor (Charles R. King) already decoded these passages for
  publication and rendered them as ordinary italicized English text**, not as raw code groups. This is
  consistent with a period key already known to King's own family/editors (not this project's own
  recovery).

## The one raw, undeciphered specimen found

Page 98-99, letter **"King to Secretary of State, No. 61, London, April 7, 1802"** (King writing to
Madison, not to Livingston, but plausibly the same WE027 nomenclator per the Weber snippet above,
which explicitly ties WE027 to despatches "to Secretary of State James Madison"):

> "...*786 and others are likewise much dissatisfied with the cession `*Not deciphered.` of Louisiana
> to France; speaking with me concerning it a day or two ago he said Ceylon, Trinidad and the Cape
> were as nothing in comparison to Louisiana and the Floridas; and on my expressing my surprise that
> **128. 55. 28** should have known of the cession and yet advised the Peace, he said that **128. 55. 28**
> viewed the cession in the same light that he did, but that he knew nothing of it until after the
> conclusion of the Preliminaries."

Two distinct undeciphered items, both marked by the editor as "Not deciphered" (i.e. the editor's own
period key did not cover these particular values -- a direct, printed admission of an incomplete key,
the strongest kind of evidence that this is a real, still-partially-unbroken code, not fully solved
even by the family's own 1894-1900 edition):
- **786** -- a single group, standing for one word or name (context: someone dissatisfied with the
  Louisiana cession -- plausibly a British minister's name).
- **128. 55. 28** -- a *repeated* three-number group, both instances referring to the same person
  (used as "he" in the surrounding English both times) -- worth flagging structurally: a fixed
  three-number sequence standing for one referent is NOT the target's own one-group-per-word shape
  (ARM-DESIGN's verdict, HYPOTHESES.md), and could indicate WE027 uses a different (e.g. book/page-
  column-line) addressing convention for at least some entries, distinct from the target's flat
  1-1900 single-value system. Too small a sample (4 distinct values total: 786, 128, 55, 28) to run
  `signature_test.py`/`overlap_test.py` meaningfully -- reported as a specimen, not a screen.

No other raw (undeciphered) numeral groups found in either volume by the broad numeral-run regex
(`(?:\d{1,4}[\.\s]+){3,}\d{1,4}`) -- the only two other multi-number hits it caught were pound-sterling
sums ("1.083.990.3.8", a currency amount), not cipher.

## Requests

archive.org: 2 (advancedsearch.php for volume identifiers) + 2 (`_djvu.txt` downloads, vol III and IV,
both needed `-L` to follow a redirect that a bare fetch silently swallowed). All >=1.5s apart,
descriptive User-Agent, no 429/403/challenge. No logins, no credentials touched.
