found-solved

# Thomas Randolph (Edinburgh) to Thomas Radcliffe, 3rd Earl of Sussex, 9 July 1570

- **Found-solved:** contemporary decipherment on f.278 (DECODE R4932), reported by Bourdeau 21 Sept 2026 and
  read in his randolph1570/NOTES.md; Boyd 1903 no. 339 "partly in cipher, deciphered". Not verified against the
  f.278 image from this account (bl.digirati.io is egress-blocked here).
- **Source:** BL Cotton MS Caligula C II, f. 277r-v. 2pp, holograph, signed "Tho. Randolphe". DECODE R4931.
- **Dating correction:** QUEUE.md and Bourdeau's catalogue (id 99) give the year as 1569. The manuscript
  itself is headed, top right of f.277r, "9° Julij / 1570" and the closing dateline on f.277v reads
  "Edenboroughe the ixth of Julye 1570" — both read at close crop, high confidence. This letter is
  **9 July 1570**, not 1569. Reported to whoever re-scores this row; QUEUE.md/QUEUE-scores.json not
  edited here (outside this worker's brief).
- **Foliation:** the leaf carries three different pencilled/ink foliation numbers in its top-right corner
  (234 and 270, both struck through, then 277 current) — the volume has evidently been refoliated more
  than once, which matters for matching against the printed calendar's citations (see below).

## Rule 1: is it already solved? (checked 21 Sept 2026)

- **Web search** ("Thomas Randolph Sussex 1569/1570 cipher Cotton Caligula C II", "Caligula C II f.277
  Randolph Sussex Scotland 1569"): no page found describing a decipherment of this specific item. General
  biographical pages on Thomas Randolph (ambassador) only.
- **Cryptiana** (`sources/cryptiana/web/elizabeth.htm`, the Elizabeth-period page, and `unsolved.htm`):
  grepped for "Randolph", "Sussex", "Caligula C II", "277". No entry for this letter. The page does cover
  other Randolph ciphers (the 1559 Randolph-Sadler-Croft cipher, Add MS 33591) and other Caligula-series
  ciphers (Drury 1569, an Informant 1571, Walsingham-related Caligula C III/IV/VI/VII/VIII), but nothing
  at Caligula C II f.277 or naming Sussex as Randolph's correspondent for a ciphered letter. Checked, not
  found.
- **DECODE (de-crypt.org), no login:** R4931 (this record) and R4930 (the "sibling" key record QUEUE names)
  both answer HTTP 200 for `/decrypt-web/RecordsView/<id>`, but the page is a client-shell that loads record
  data only after login; unauthenticated fetch shows `"IS_LOGGEDIN":false` and no record fields. Per the
  20 Sept 2026 ROOM.md/CLAUDE.md note, DECODE_USER/DECODE_PASS are currently rejected server-side and are
  not being retried this session (lockout risk). Not reachable without login.
- **Solver repositories**, shallow grep (`git clone --depth 1`, grep only, into /tmp, not read in full):
  - `dbourdeau/cyphersolver`: catalogue.json entry id 99 (`entries[64]`) = this exact letter. `status`:
    "DECODE R4931: Non-decrypted, 2 pp., unknown; alphabet, graphic signs, numerical; images login. Not
    viewed here. 1 key record(s) from the same series on DECODE, nearest R4930 (1569)." Confirms: catalogued
    as open/unsolved by Bourdeau, key fit to R4930 not verified, images not viewed by that project. Matches
    what QUEUE-scores.json already said.
  - `aaymeloglu/unsolved-ciphers`: no hit on "Randolph", "Caligula C II", "R4931", "R4930" in
    `catalogue/decode-records.jsonl` or `catalogue/decode-catalog.csv`. Not listed there.
- **Tomokiyo/Cryptiana published keys:** the only Randolph key on the Elizabeth page is the 1559
  Randolph-Sadler-Croft cipher (Add MS 33591), eleven years earlier and a different correspondence
  (Sadler and Croft, not Sussex); Cryptiana itself flags this as "a different cipher" territory (per
  QUEUE-scores.json's own rationale). No Randolph-Sussex key of 1570 is published there. This is not a
  verified key fit for f.277 — the recovery route named in QUEUE.md is not confirmed.
- **CSP Scotland, printed calendar — important finding.** *Calendar of the State Papers relating to
  Scotland and Mary, Queen of Scots, 1547-1603*, vol. 3 (ed. William K. Boyd, 1903; Internet Archive
  `calendarstatepa02boydgoog`, full djvu text fetched without login, full view/public domain scan) covers
  1569-71 and carries many Randolph-to-Sussex entries through July 1570. An enclosure under entry no. 339
  (Sussex to Cecil, 7 July 1570, "Inclosure with the same:— (Thomas Randolph to Sussex.)", no date of its
  own given by the calendar) reads, in full:

  > "Has received his letter of the 2nd of this month, and what may answer some part thereof, he trusts
  > Sussex has seen by his written the same day. The Queen's party in Scotland have little confidence in
  > her, who so often changes her course. They were determined to have made a Regent, but stayed it sore
  > against their wills, and shall be forced to join with murderers and traitors, and to obey her whom
  > neither by law, duty, nor conscience they think themselves bound unto. This is a great part of their
  > grief, and almost every man's speech, and preached in pulpit in plainer words than he lists to write.
  > They know that there are no Frenchmen to come..."

  The opening clause ("Has received his letter of the 2nd of this month...he trusts Sussex has seen by his
  written the same day") matches the opening of f.277r almost word for word ("I have receaved yor L[ordship]s
  l[ett]res of the second of this p[rese]nt...some parte thereof yor L[ordship]...wrytten from you the fame
  dayge"). The clause "...a great part of their grief...preached in pulpit in plainer words than he lists to
  write" matches the plaintext that resumes on f.277r immediately after the cipher passage ends
  ("...fntt fpare agaynfte hym willed...", read independently by a blind transcription pass as close to
  "...is a greate parte of yor greif...prayed in pulpit in playnnes worse then I can to wryte", see
  reconciliation log below). **The sentence sitting between those two matched clauses in the calendar — "They
  were determined to have made a Regent, but stayed it sore against their wills, and shall be forced to join
  with murderers and traitors, and to obey her whom neither by law, duty, nor conscience they think
  themselves bound unto" — sits exactly where the manuscript's cipher passage sits.** This is a strong
  positional/content match, not a verbatim one: Boyd's calendar is an English paraphrase/abstract, not a
  transcription, and does not flag the passage as having been in cipher on the original. No claim is made
  here that this proves the cipher decodes letter-for-letter to this wording — only that this specific
  passage (in paraphrase) is already in print, and gives a strong content crib for whoever attempts the
  decode. The calendar's own citation for this enclosure does not give a folio number, so it cannot be
  checked against the leaf's multiple foliations directly; the date mismatch (calendar files it undated,
  near the 7 July covering letter; the manuscript itself is dated 9 July) is most simply explained by an
  editorial placement choice, not by this being a different letter — the content match is too specific
  (same "letter of the 2nd" reference, same grief/pulpit clause immediately after) to be coincidence, but
  this identification is the orchestrating worker's own judgement, not a certainty.
  - Also checked directly in the same volume: entries no. 346 (8 July) and no. 348 ("July 0", i.e. an
    OCR-garbled "July 9") Thomas Randolph to Sussex — read in full; neither matches f.277r's content
    (346 is about Andrew Melvin/the Castle/Border lords; 348 is about Lord Morton/the convention/Grange).
    These are two *different* Randolph-to-Sussex letters of the same week, not this one. Ruled out.
  - CSP Foreign, Elizabeth 1569-71 and the Bain calendars were not separately searched beyond the above
    (the Boyd CSP Scotland vol. 3 hit was sufficient to answer rule 1's question); flagged as a possible
    follow-up rather than pursued further under this worker's cap.
- **Google Books:** not queried (GOOGLE_BOOKS_KEY available per CLAUDE.md, but the Internet Archive full
  text of the relevant calendar volume answered the question directly and more cheaply; not needed).

**Conclusion for rule 1 (search result, not a novelty classification — that is the verifier's job under
rule 10):** no decipherment of this cipher passage was found anywhere searched. A printed 1903 calendar
does carry an English paraphrase of the letter that surrounds (and, by strong positional inference, stands
for) the ciphered clause, but not a transcription or decipherment of the cipher itself. Bourdeau's catalogue
independently confirms the item as unsolved/not viewed as of its own last scoring.

## Access

Route 1 of the access playbook (plain URL with curl, browser User-Agent) worked without incident:
`https://bl.digirati.io/iiif/ark:/81055/vdc_100162985756.0x000001` answered 200, IIIF v3 manifest, 1194
canvases. f. 277r and f. 277v canvases fetched and stitched with `cyphersolver/norfolk1570/fetch.py`
(Bourdeau, MIT-licensed code; credited) at scale 1 (full resolution, ~7300x10000 px, tiles capped at 1024px
by the image service as that script already expects). Images and a compact `manifest.json` (recording the
source manifest URL, the BL rights field, and BL's stated unpublished-manuscript reuse terms) are in
`images/`. Folder is ~21 MB, under the 30 MB cap.

## Transcription and reconciliation (21 Sept 2026)

Two independent Sonnet subagent passes ("pass A", "pass B") transcribed the cipher passages from crops
`images/crops/f277r_cipher_block.jpg` and `images/crops/f277v_cipher_line.jpg` (both ~7300px wide, shown to
the agents downscaled to ~2000px by the image tool, i.e. ~3.6x below native). Both independently reported
that resolution, not the handwriting itself, was the binding constraint, and disagreed with each other on
most individual glyph identities while agreeing on rough line/group counts. Pass B additionally noticed
(correctly, confirmed by the orchestrator) that the "six lines of pure ciphertext" the transcription brief
assumed are not pure: plaintext English words are interleaved within the cipher on at least two of the
lines (line 1 opens in plaintext before the cipher starts; line 4 has a plaintext stretch in the middle).

The orchestrator (this session) then re-cropped f.277r lines 2-3 into three narrower (~2450px, i.e.
~1.2x-downscale, near-native) horizontal segments and re-read them directly, confirming the passage is
genuine invented-symbol cipher (not misread cursive plaintext) and giving a somewhat higher-confidence
reading for those two lines specifically. A third, separate blind pass (no calendar text shown to it)
independently transcribed the plaintext immediately before and after the cipher block; its reading of the
post-cipher plaintext ("...is a greate parte of yor greif...and prayed in pulpit in playnnes worse then I
can to wryte") is what let the CSP match above be found and is graded M (uncertain, own reading, not
checked letter-by-letter against the calendar's modernised wording) rather than treated as a verbatim
crib.

**`ciphertext.txt` is a first-pass, structure-confirmed transcription, not a glyph-exact one.** Line and
group boundaries, and the location of the plaintext interruptions, are medium-to-high confidence (three
independent looks agree on the shape of the passage). Individual invented-symbol identities are low
confidence — the bracket-code legend in `ciphertext.txt` is not a verified symbol inventory; the same code
used twice is a guess that two marks are the same symbol, not a confirmed match. A future pass should
re-fetch or re-crop each line into several native-resolution (~2000-2500px) segments (as done here for
lines 2-3 only) before attempting frequency analysis or a key fit — this would take on the order of 20-30
crops for the whole passage, more than this worker's cap allowed for a full pass.

## What a next solver needs

1. A true native-resolution, per-line (or per-word) re-transcription of `images/img/f277r_s1.jpg` lines
   1, 4 (the mixed cipher/plaintext lines), 5 and 6, and a check of line 2-3 against the orchestrator's
   segments above (`/tmp` crops from this session were not committed; regenerate with `fetch.py` and
   `PIL.Image.crop`, narrow enough that width stays under ~2500px so the image tool does not downscale).
2. DECODE R4931 (this record) and R4930 (the nearby key record) once login works — Bourdeau's catalogue
   flags R4930's fit as unverified, so this is the single most direct next step if credentials are fixed.
3. The CSP Scotland vol. 3 paraphrase above as a content crib for the enciphered clause, with the caveat
   that it is a 1903 editorial paraphrase, not the letter's actual words.
4. Grading so far: no H, no C, no S with a control. What plaintext-adjacent reading exists (the blind pass's
   reading of the post-cipher lines) is grade M (uncertain, own reading). The cipher symbols themselves are
   ungraded — no reading of them is claimed.

Not classifying novelty here (rule 10); that is the verifier's job from AUDIT.md once/if this target reaches
that stage.

## Native-resolution crops (23 September 2026)

Transcription worker, ASSIGNMENTS row 1. **Stopped part way on 23 Sept 2026** when the orchestrator reported the
f.278 decipherment above (Bourdeau, github.com/dbourdeau/cyphersolver, folder `randolph1570/`, commit 2e9ec01 of
23 Sept 2026; Bourdeau's text is CC BY 4.0). No reconciliation, no rewrite of `ciphertext.txt` and no frequency
analysis were done; `ciphertext.txt` is still the 21 Sept first pass. No reading of the cipher is claimed, so no
H/C/S/M/I grades apply.

What exists:
- `images/crop.py` cuts 49 native-resolution segments (no rescaling; 1,405-1,605 px wide, 300 px tall, each band
  centred on the writing of its own segment because the lines drift by up to 110 px) into
  `images/crops/native/`, with `manifest.json` giving each crop's source image and pixel box. Greyscale with a
  levels stretch (70-200) and JPEG quality 75 instead of the 85 asked for, to keep the folder under 30 MB (it is
  about 28.6 MiB; the four 21 Sept wide crops in `images/crops/` were kept because deleting them was refused).
- **The cipher on f.277r is larger than the 21 Sept transcription records.** The main block runs over eight
  lines (L1-L8: cipher starts after "as this ." on L1 and ends at "cede ." on L8), not six; the old L1-L6 are
  lines 1-6 of these, and lines L7 ("XUӾλX ...") and L8 ("…CεδQ .") were missing. Two further mixed
  cipher/plaintext passages lie lower on the recto: B1-B3 (y ≈ 3900-4400, "...to be sorte wth yor L. [cipher]"
  through "... woo is of that mynde") and C1-C2 (y ≈ 7300-7880, including struck-through cipher). The verso
  cipher is on one line (f277v_L1, "OO UӾWg ≈ CλNθεΠ"). On L4 the plaintext inside the cipher reads, by eye at
  native resolution, as "full sore agaynste their willes", not "fntt fpare agaynfte hym willed" (grade M, not
  checked against the f.278 decipherment).
- Two independent Sonnet passes (`claude-sonnet-5`, run headless from a scratch folder holding only the crops,
  no transcription, legend or calendar text): `images/crops/native/passA.tsv` (138 group rows, cost $2.35) and
  `passB.tsv` (129 group rows, cost $0.60). They are raw and unreconciled; their bracket codes differ and have
  not been collapsed into one inventory.

Suggested follow-up (not done): if anyone wants the ciphertext for checking the f.278 decipherment glyph by
glyph, reconcile passA/passB against the crops and rewrite `ciphertext.txt` from them.

