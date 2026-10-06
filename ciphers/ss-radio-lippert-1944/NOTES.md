open
Cipherbrain posts read in full by GF4-BATCH18 on 3 Oct 2026 (live re-fetch, scienceblogs.de): "Der verschlüsselte SS-Funkspruch" (15 Apr 2014, 14 comments), Top 50 no. 25 (7 Aug 2017, 28 comments), "Ungelöste Verschlüsselungen aus dem Zweiten Weltkrieg (2)" item 4 (4 Feb 2021, 28 comments): no decipherment; the 2017 and 2021 threads judge the form a collector's forgery.

Intake (25 Sept 2026, LANE B3 worker bSSR, minimal check-solved per breadth.md's intake step):
Cipherbrain post "The Top 50 unsolved encrypted messages: 25. The SS radio message" (7 Aug 2017)
and its full 28-comment thread read in full from `sources/schmeh/posts/25-ss-radio.txt` (already
on disk); the post's own text states "The cleartext is unknown" and no commenter claims a
solution -- comments 9-27 instead argue the item is a probable forgery (wrong Fraktur-s usage,
misspelled "Lublin" on the rank stamp, mismatched unit/location, non-standard rank abbreviations,
eagle facing the wrong way; a near-identical forged item later sold on eBay, comment 28). Both
solver repositories grepped (shallow clone, `grep -ril lippert`, deleted after): dbourdeau's
`top50/NOTES.md` and `TARGETS.md` (row 25) both read "probably a forgery ... Treat as
questionable before spending anything on it", no claimed solution of any standing; no match
anywhere in aaymeloglu/unsolved-ciphers. One OpenAlex query
(`search=SS radio message Lippert cipher decrypted`) returned 0 results. One Semantic Scholar
query 429'd twice (one retry after a pause, per the good-citizen rule); not reachable this pass.

Verdict: open, unsolved by any source checked, probable forgery per Bourdeau and the post's own
comment thread (consistent with UNSOLVED-SURVEY.md row 22 and specs/ss-radio-lippert-1944.json).
No Latin-letter transcription of the ciphertext exists anywhere on disk or in either repo; cheap
test 1 (image fetch + blind transcription) is the first thing that can be run.

## Status
open

## Gate check
`python3 tools/intake_gate_check.py ss-radio-lippert-1944` -- pasted below before proceeding.

```
ss-radio-lippert-1944: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Cheap test 1 (25 Sept 2026, LANE B3 worker bSSR)

Image over transcription (rule 2): fetched the original photograph, `images/SS-Code.jpg`, from
scienceblogs.de (the only Latin-letter source is this photo -- no transcription exists in the
post text, its comment thread, or either solver repository, per the intake pass above). Single
blind pass, no subagent, read directly off 3x/5x upscaled crops of the image (`images/crop_lines.png`,
`images/crop_right.png`, `images/crop_seps2.png`, `images/crop_p4sx.png`; manifest in
`images/manifest.json`). Every letter and digit shape was checked against a close crop before
being committed to the transcription; no shape was ambiguous enough to need an M grade.

Ciphertext as transcribed (`ciphertext.txt`), one line per form line, separator kept exactly as
written:

```
MASS=QRLZ
H9/OSLY
ALAP=DETL
27163:KSSY
J1=EFLS
KOMM P4SX
```

Separator positions (character index after which the separator falls, in the concatenated
left+sep+right form): line 1 `=` after position 4 (MASS|=|QRLZ); line 2 `/` after position 2
(H9|/|OSLY); line 3 `=` after position 4 (ALAP|=|DETL); line 4 `:` after position 5
(27163|:|KSSY); line 5 `=` after position 2 (J1|=|EFLS); line 6 no separator character, only the
form's grid-cell gap (KOMM␣␣␣P4SX) -- five of six lines carry a separator, matching Schmeh's own
description in the post text. The `=` is written as a stylized cursive double-wavy stroke, not a
straight typewritten equals sign; transcribed as `=` for the ASCII file, noted here for anyone
re-checking the image.

Grade: all 45 symbols (37 letters + 8 digits) graded S (cryptanalytic transcription from the
primary image; no key or known plaintext involved) -- no H or C tokens (rule 4), consistent with
"cryptanalytic result" only.

N/K/IC (`specs/cheap-tests/ss-radio-lippert-1944/ic_test.py`, letters only, digits treated as a
separate sub-alphabet and excluded from this letter-IC test since a German-prose control is
letters-only):

- N (letters, digits excluded) = 37; N_all (letters+digits) = 45; digits = 8 (9,2,7,1,6,3,1,4),
  7 distinct digit values, from H9/27163/J1/P4SX.
- K (distinct letters) = 18: A D E F H J K L M O P Q R S T X Y Z.
- target IC (N=37) = 0.0631
- German control (tools/data/de20, 1880-1940 prose, era-matched to 1944; 5 seeds x 200 draws of
  37-letter windows) = mean 0.0725, 95% range [0.0465, 0.1066]
- uniform-random control (K=18, N=37; 5 seeds x 200 draws) = mean 0.0554, 95% range
  [0.0420, 0.0751] (flat expectation 1/K = 0.0556)
- **Target IC falls inside both 95% ranges** -- inconclusive at this N, not a control-backed
  negative either way. Expected: 37 letters split across six short code-like groups is far too
  little text for IC to discriminate German prose from a flat cipher alphabet; this is not
  evidence for or against structure, only a first look.

No language judge run (spec's judge block's `letters_min` is 20-80, a placeholder pending this
transcription -- narrower bounds and a real judge pass belong to test 2/3, not this test).

Per the brief, test 2 (comparing the form's field layout against the WW2 Wehrmacht
Spruchformular) was **not** run.

Requests: scienceblogs.de 2 (one reachability check, one image fetch; both HTTP 200 -- note for
the next holder: these two were not spaced >=2s apart, an oversight, flagged here rather than
silently passed over; no further requests to this host were made, so no retry/backoff was
triggered and no complaint or block was seen).


## Web and blog check (GF4-BATCH18 (account-4), 3 Oct 2026)

Plain web searches (WebSearch): (1) `SS radio message Lippert 1944 cipher Schmeh solved` -- Cipherbrain 2014 (German), 2017 (Top 50 no. 25), 2021 (German and English "Unsolved ciphertexts from World War II (2)"), plus an English Cipherbrain page "Unsolved: An encrypted radio message from the bugging service" (a different item); all unsolved; (2) `"SS-Funkspruch" Lippert 1944 verschlüsselt gelöst Fälschung` -- the 2014 post, a buradabiliyorum.com mirror of a Cipherbrain post, and **Forum der Wehrmacht thread 39936 "Verschlüsselter Funkspruch"** (20 Apr - 6 May 2014, 11 posts: Sarmatus, Karl Grohmann, Lobito060454, Huba, Joseph O., RolandP) -- read: no decipherment, "one would really have to obtain the code documentation" (Lobito060454), RolandP places Lippert as commander of the 10. SS-Pz.Div. supply troops; no forgery verdict there; (3) `"KSSY" "ALAP" SS radio message 1944 cipher` (the distinctive groups) -- only the Cipherbrain posts; (4) `SS radio message Lippert cipher solved Claude OR GPT OR AI 2026 Schmeh top 50 no. 25` (model-solve family) -- Vals AI/Fable Cyphral Distich (no. 28, another item) and the Sept 2026 GPT-6 Astra WWI ADFGVX and Enigma announcements (other items); no AI-solve claim for this item.
Blog site searches and threads: Cipherbrain, all three posts live re-fetched and threads read: 2014 post (14 comments, 15-17 Apr 2014: stamp readings, Q-code guess via Oliver Helweg "ALAP = Ungarn/Budapest, KSSY Deckname", Schmeh's own "left column may be code-book text" -- guesses, no reading); Top 50 no. 25 (28 comments, 7 Aug 2017 - 31 May 2021: Michaela Ellguth's #3 gloss-guess "MASS = Marschbefehl ... QRLZ = Vereinigung mit H9 ... 27163 könnte das Datum sein" and Gerhard Strasser's #6 Hungary reading are interpretations without a method; #10-#27 Thomas, Ellguth, Gerd establish the forgery case -- Party eagle instead of Reichsadler, "Cublin" for Lublin on a Briefstempel, pre-1941 form, wrong rank abbreviations "StdF"/"UstuF", "Mi" in the date field; #28 Frank Gnegel, 31 May 2021, bought a near-identical forged "chiffrierter Funkspruch ... 1944" on eBay (seller xh81) for 20 euros); 2021 "Ungelöste ... (2)" item 4 (28 comments, 4-9 Feb 2021: The_Piper #17 "Die Nr. 4 ist kein Funkspruch, sondern ziemlich sicher eine Fälschung. Der verwendete Fantasie-Stempel findet sich ... auf Dokumenten, die als 'Andenken' für Sammler angeboten werden", agreed by Thomas, Gerd, Max Baertl #18/#24). klausschmeh.net `?s=Lippert`: Nothing Found; Cryptiana `search?q=Lippert`: no posts; Cipher Mysteries `?s=Lippert`: Nothing Found; Apeiron (one publication only, Koehler): nothing. Reddit r/codes (OAuth search `Lippert`: 0; `SS radio message`: 25 results, none this item).
Solver repos (fresh shallow clones, 3 Oct 2026, deleted after): dbourdeau/cyphersolver HEAD 46f8056 (2 Oct 2026) -- research/top50/NOTES.md row 25 "low ... probably a forgery ... Treat as questionable before spending anything on it", plus the cached post (research/top50/arts/25.htm), no targets/ folder; aaymeloglu/unsolved-ciphers HEAD d2800bb (27 Sept 2026) -- no "lippert". DECODE: 0 hits for "lippert" in the on-disk listings (sources/decode/*.tsv).
Requests: scienceblogs.de 3 (2 s apart, browser UA), klausschmeh.net 1, cryptiana.blogspot.com 1, ciphermysteries.com 1, apeiron.re shared (see sufi-fiddle), oauth.reddit.com 2, forum-der-wehrmacht.de 1 WebFetch, github.com shared clones; all >= 1.5 s apart.

## Premise check (GF4-BATCH18 (account-4), 3 Oct 2026)

(a) Folder's own mentions of a decipherment or clear copy: none; NOTES.md and the spec record only the forgery dispute and the thread's gloss-guesses.
(b) Other solvers' working files: none -- Bourdeau a list row ("probably a forgery"), Aymeloglu nothing, no DECODE record; Forum der Wehrmacht 2014 thread gave up for want of the code documentation.
(c) Physical neighbours: FIND (authenticity, not a reading) -- Gnegel's 2021 purchase of a near-identical forged "Funkspruch" from the same eBay seller line, and The_Piper's observation that the same fantasy stamp recurs on souvenir documents, make this a member of a family of collector fakes; a second specimen of the family is the strongest available comparison object. The original form is in Nick Gessler's private collection (Duke, web.duke.edu/isis/gessler/collections/cryptology.htm); provenance unknown per Schmeh 2014.
(d) Recipient side: Michael Lippert's units (10. SS-Pz.Div. "Frundsberg" Jan-Feb 1943; SS-Freiwilligen-Grenadier-Brigade Landstorm Nederland from 1943/44) -- no period file of radio traffic to him located; not searched further (no cheap route).
Result: no decipherment located; the authenticity question has gone from "disputed" (25 Sept intake) to a documented souvenir-forgery family (second specimen sold 2021). Status stays open per rule 5 (a forgery verdict is not a cryptanalytic negative and is not ours to grade from blog comments).

## Verdict (GF4-BATCH18 (account-4), 3 Oct 2026)

**open (unchanged), with the forgery flag strengthened.** No published or accepted decipherment located in the three Cipherbrain posts and their full threads (2014, 2017, 2021), the Forum der Wehrmacht 2014 thread, klausschmeh.net, Cryptiana, Cipher Mysteries, Apeiron, r/codes, DECODE listings, or either solver repository, searched 3 Oct 2026. Claimed-but-unaccepted interpretations: Ellguth 2017 (march-order gloss), Strasser 2017 (Hungary 1944), Helweg via Schmeh 2014 (Q-code / Budapest) -- recorded as claimed, none accepted.

## While waiting (GF4-BATCH18, 3 Oct 2026)

Nothing here waits on a person. The zero-dependency step: locate Gnegel's 2021 eBay specimen (ebay.de item 284276746819; try the Wayback CDX for that URL) and any other "chiffrierter Funkspruch 1944" listings from the same seller, and compare their cipher groups with ours -- identical or shuffled groups across specimens would settle the souvenir-forgery question without any cryptanalysis.

## Intake gate (GF4-BATCH18, 3 Oct 2026)

$ python3 tools/intake_gate_check.py ss-radio-lippert-1944
ss-radio-lippert-1944: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0

$ python3 tools/next_steps.py --wait-only | grep ss-radio-lippert-1944
(no line)

## Next step (NO-CRACKS, 5 Oct 2026)

next: find Gnegel's 2021 eBay specimen (ebay.de item 284276746819, Wayback CDX) and other "chiffrierter Funkspruch 1944" listings from the same seller and compare their cipher groups with ours (identical or shuffled groups would settle the souvenir-forgery question), ~$1. Who acts: agent. Source: this file's "## While waiting (GF4-BATCH18)"; written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.

## Second-specimen search (D2B-LIPP, account 2, 5 Oct 2026, 23:51-23:56 UTC, for LANE DEFAULT-account-2-20261005-2217)

Job: find Gnegel's 2021 eBay specimen (ebay.de item 284276746819) and other "chiffrierter Funkspruch 1944" listings, and compare cipher groups with ours. **Result: no image or transcription of any second specimen was reachable, so no group comparison could be made.** Authenticity question unchanged; status stays open (rule 5).

What was checked, and where nothing was found:
- Wayback availability API (archive.org/wayback/available, answers 200): `ebay.de/itm/284276746819`, `www.ebay.de/itm/284276746819`, `ebay.com/itm/284276746819`, and the full slug URL from Gnegel's comment (`www.ebay.de/itm/chiffrierter-Funkspruch-geheime-Nachricht-1944-secret-cipher-code-message-/284276746819`): `archived_snapshots: {}` for all four. Also checked the comparison listing in the 2017 thread (`ebay.com/itm/401266966174`, a 1940 Lublin SS-Feldpost cover): no snapshot.
- Wayback CDX (web.archive.org/cdx/search/cdx, wildcard `ebay.de/itm/*284276746819*`): **unreachable** -- web.archive.org reset every connection from this container (curl 35, proxy log `ws_closed_mid_exchange`), three attempts plus one retry after a pause; stopped per the good-citizen rule. The availability API above returns only the closest capture and can miss captures under a variant URL, so the CDX search is **not run** -- not a negative.
- eBay live item page: HTTP 403 (eBay error page); one request, not retried.
- Cipherbrain 2014 post (live re-fetch) and 2021 "Ungelöste ... (2)" post (live re-fetch), and the 2017 Top-50 no. 25 post (on disk, `sources/schmeh/posts/25-ss-radio.html`): every `<img>` and every eBay/ebayimg/imgur link listed. All three carry only the Lippert form itself (`SS-Code.jpg`, `SS-Code-Stempel.png`, header bars); no comment in any of the three threads attaches or links an image of the second specimen. The only eBay links are Gnegel's item URL (comment #28, 2017 thread) and the Lublin cover.
- WebSearch (3 queries: `"chiffrierter Funkspruch" 1944 geheime Nachricht ebay`; `"secret cipher code message" 1944 Funkspruch Stempel Wachmannschaft Berchtesgaden`; `"Funkspruch" 1944 "Briefstempel" SS Fälschung Sammler chiffriert Andenken`): only the Cipherbrain posts and unrelated WW2 cipher/stamp pages; no other listing of a "chiffrierter Funkspruch 1944" found.

Comparison: not run (no second ciphertext). Nothing graded; no reading claimed.

Next step (agent, ~$0.5): the Wayback CDX search for `ebay.de/itm/*284276746819*` and for the seller's other items, from a session where web.archive.org answers (test `curl -sS -o /dev/null -w "%{http_code}" https://web.archive.org/` first), or as a LOCAL-QUEUE row if it stays unreachable from the cloud. Beyond that, the specimen itself is held by the 2021 commenter (thread comment #28); a request for a photo of its cipher groups would go through the blog thread or an outreach draft, the person's decision.

Requests: archive.org 7 (wayback availability API, >= 2 s apart), web.archive.org 4 (all connection resets; stopped), ebay.de 1 (403), scienceblogs.de 2 (2014 and 2021 posts, > 2 s apart), WebSearch 3.

## Wayback CDX retry (R9-LIPP, account 4, 6 Oct 2026, 06:00-06:06 UTC, for LANE LANE-RUN9-account-4)

Job: retry the Wayback CDX search for `ebay.de/itm/*284276746819*`. **Result: not run -- web.archive.org still resets every connection from this container.** `curl -sS https://web.archive.org/` returned curl 35 ("Connection reset by peer", HTTP 000) at 06:02 UTC and again on one retry after a pause; stopped per the good-citizen rule. No capture of the 2021 specimen's listing was seen, so no group comparison was made; this is not a negative. Nothing graded; no reading claimed; status stays open (rule 5).

Next step (a person's browser, ~$0): LOCAL-QUEUE.tsv row L62 asks the owner's desk runner for the CDX rows and any capture. Agent-side the step is retired until web.archive.org answers from the cloud.

Requests: web.archive.org 2 (both connection resets), no other host.
