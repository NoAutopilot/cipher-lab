# AUDIT: the "four not printed" claim of the Eckert 1864 readings

Verifier session, 20 Sept 2026. Adversarial audit of the novelty claim in this folder (NOTES.md section 4,
reading.md summary, status.json, STATUS.md, dashboard.html as of commit 755a385): that of the twenty entries
of Huntington mssEC 19 read with Cipher No. 1, four (E4, E5, E6, E12) are "not printed" in the Official
Records, which the orchestrator passed on as "telegrams the Official Records never printed" and described to
the owner as "new readings". The audit was done by one verifier session with four subagents, none of which
had taken part in the solving session. Nothing in this file protects the earlier conclusions; where they were
wrong it says so. Levels N0-N5 are those of CLAUDE.md rule 10.

## 1. Executive verdict

| entry | telegram | prior plaintext | prior decipherment of this ledger copy | level |
|---|---|---|---|---|
| E4 | Fox to Butler, 21 Apr 1864 9.30 PM | not located in the sources searched; substance in print (Butler's reply, OR I/33 p.279; Fox to Ericsson, ORN I/9 p.667) | none found; 53 of its 63 words stand in clear on the Huntington page since 15 Mar 2018 | **N3** |
| E5 | Meigs to Butler, 22 Apr 1864 10.45 AM | not located in the sources searched; antecedent and follow-ups in print (Butler Corr. IV p.112; OR I/33 pp.938, 940) | none found; about 40 of its 60 words in clear on the Huntington page since 2018 | **N3** |
| E6 | Halleck to Sherman, 26 Apr 1864 3 PM | **yes**: OR ser. I vol 32 pt 3 p.498 (1891), word for word | none found | **N1** |
| E12 | Lincoln to Col. Frank Wolford, 4 Aug 1864 4.30 PM | **yes**: printed in 1864 (McClellan campaign pamphlet, p.21), Nicolay and Hay (1894, vol 2 p.558; 1905 ed. vol 10 pp.180-181), Basler, Collected Works vol 7 pp.479-480 (1953) | none found | **N1** |

Two of the four "not printed" telegrams were in print, one of them in the very series the solver searched and
the other in 1864 itself. The other two were not found, but their substance is public and most of their words
were never in cipher. **Nothing in this folder may be described as a first decipherment, previously unread,
newly recovered or unpublished plaintext.** The safe statement for the whole folder is: "twenty entries read
at grade H from the cipher book; seventeen agree word for word with the Official Records; one (E12) with the
printed Lincoln works; two (E4, E5) were not found in the sources listed in AUDIT.md."

The owner's suspicion was correct: "not in the Official Records" was conflated with "never published", and
even the narrower claim was wrong for E6.

## 2. What the repo claimed, and where

- NOTES.md section 4 (commit 045fbe2): "16 of the 20 are printed, 4 are not (E4 ... E12, which may be in the
  Collected Works)". The doubt about E12 was recorded and never resolved.
- reading.md summary table: "not printed" against E4, E5, E6, E12; below it "four (E4, E5, E6, E12) are not".
- status.json (targets note and log of 20 Sept 00:00): "four are unprinted", "four are telegrams never printed
  in the Official Records"; STATUS.md rows 24 and 37 and dashboard.html the same.
- Commit message 045fbe2: "four are not printed".
- The word "unpublished" or "new readings" does not occur in the repo; it was said in the orchestrator's report
  to the owner. The escalation happened in two steps: (a) "not matched by a sweep of 26 volume-parts" became
  "the Official Records never printed" (an absolute claim from a partial search), and (b) "not in the OR"
  became "new".

All of these sentences are corrected in this commit (section 11).

## 3. What the solver actually searched (from the repo, for the postmortem)

NOTES.md section 4 and reading.md: a subagent checked the 29 candidate entries "against the Internet Archive
full texts of 26 volume-parts of OR series I (vols 32-34, 36-43, 45, 52 ...) by date and plain phrases". The
identifiers and the grep commands were kept in a scratch file, or_check, that was never committed, so the
exact queries cannot be reproduced. No other series (OR series II-III, the Navy OR), no sender or recipient
edition (Butler, Fox, Meigs, Sherman, Grant, Lincoln), no full-text engine outside the Internet Archive and no
project source was searched before the four were reported as not printed. The Huntington page transcriptions
were used as a third witness for the transcription, but the fact that they publish most of each telegram in
clear was not weighed.

Probable cause of the E6 miss (inferred, not provable without or_check): the Internet Archive djvu text of
the OR prints "Saint Louis" and separates words with two spaces, and the OCR of p.498 reads "can he mounted";
a single-space grep for "St Louis", "3rd Iowa" or "Third Iowa Cavalry can be" returns nothing. The verifier's
first grep failed the same way until the whitespace was normalised.

## 4. Source-family log

Searched 20 Sept 2026. "Reachable" means from this environment through the agent proxy with curl and a
browser User-Agent, or through the Internet Archive full-text API (be-api.us.archive.org/fts/v1/search) and
the per-item "search inside" endpoint (fulltext/inside.php), both of which work and give page-level hits
even for lending-only items.

| # | family | reachable | what was searched | result |
|---|---|---|---|---|
| 1 | OR ser. I | yes (IA djvu full texts) | vols 32 pt 3 (two copies), 33, 34 pt 3, 36 pt 2, 38 pt 4, 39 pt 2; volume indexes for "Iowa Troops, Cavalry, 3d" and "Wolford"; phrase and date searches with whitespace normalised | E6 at I/32 pt 3 p.498; Butler's reply to E4 at I/33 p.279; Halleck to Butler 21 Apr (horses) I/33 p.938; Halleck to Grant 22 Apr I/33 p.940; no E4, E5, E12 |
| 1 | OR ser. II, III; General Index; Supplement | partly | ser. III vol 4 (IA warofrebellionco0004genf) searched inside for "cavalry depot", "instead of three regiments", "April 22, 1864"; ser. II vol 7 not located on IA; General Index only as the 1985 reprint, lending-only, not searched; OR Supplement (Broadfoot) has no online full text | no hit |
| 2 | ORN ser. I vols 9-10 | yes (IA officialrecordso0009unse, 0010unse) | "camels", "Tecumseh", "Pamlico Sound", "April 21, 1864", "your camels could be ready"; pp.647-651, 667, 682-683, 688 read | Fox to Ericsson 21 Apr 9.20 p.m. (p.667) and 22 Apr (p.683); Butler to Fox 21/22 Apr midnight (pp.650-651); E4 itself not printed |
| 3 | Butler, Private and Official Correspondence (1917) | yes (IA privateofficialc04butl, c03butl and Google scans) | vol 4 pp.112-120 (20-24 Apr 1864) read in full; vols 3-4 searched inside for Tecumseh, camels, Pamlico, cavalry depot, three regiments, four thousand, Meigs, Fox; index entries for Fox and Meigs | Halleck to Butler 21 Apr (p.112); Butler to Meigs 21 Apr (p.112, the "dispatch of last night" E5 answers); three Butler to Fox telegrams of 21 Apr (pp.113-115); no E4, no E5 |
| 3 | Fox, Confidential Correspondence (1918-19); Butler's Book (1892) | yes (IA) | Tecumseh, camels, 20-29 Apr 1864 | no hit |
| 4 | Lincoln: Basler CW; Nicolay-Hay; Lincoln Papers (LoC); Papers of Abraham Lincoln | see section 8 | phrase searches over IA ("know his reasons for making it", "inclosures from me", "wait till you hear from me again"); Basler vol 7 index | E12 in Basler 7:479, Nicolay-Hay, and the 1864 pamphlet |
| 5 | Grant Papers vol 10; Sherman's Civil War; Sherman Memoirs; Iowa regimental records | partly | IA full-text search hits Papers of U. S. Grant vol 10 (annotation quoting E6: "Cavalry can be mounted at St. Louis. Its last orders were for Vicksburg. Where shall it go."—Telegram, copies ...); the volume is lending-only, page not read; Sherman's Civil War lending-only, not searched; Sherman Memoirs vol 2 (IA) no hit; Roster and Record of Iowa Soldiers vol 4 and Ingersoll no hit. Re-checked 20 Sept 2026 (IA-login worker): identifier confirmed as `papersofulyssess0010gran` (IA, access-restricted/lending-only, 654 images). The page still could not be read — the IA_USER/IA_PASS login failed this session (IA_USER is not an email address; see Access playbook, CLAUDE.md §3). be-api full-text search re-confirms the annotation's presence but its `page_num` field equals the item's total imagecount (654) on every hit, not a real page locator, so no citable page number could be recovered by this route either. Re-checked 21 Sept 2026 (IA login worker 2): IA login still fails even with a corrected email-format IA_USER (`account_not_found`; see Access playbook); read via Google Books instead — volume id `7DAAxfRuXKoC` (ISBN 0809309807, confirmed by Open Library as *The Papers of Ulysses S. Grant, Volume 10*, SIU Press, 9 Apr 1982), full-phrase search for "Cavalry can be mounted at St. Louis" returns one hit with preview link `pg=PA562`; the rendered preview page (screenshot, page footer reads "562"/"563 not part of preview") carries the annotation in full, including its own citation "As printed in O.R., I, xxxii, part 3, 498" and an editorial note that USG's attribution appears erroneous since he was not in Washington on 26 Apr | E6 also quoted in PUSG 10 p.562 (Google Books preview, read in full); verdict unchanged, N1 stands on the OR I/32 pt 3 p.498 print already on record |
| 6 | Meigs / quartermaster | partly | OR ser. III vol 4 as above; no published Meigs letterbook located; Google Books API 429 (quota) | no hit |
| 7 | Huntington catalogue and item pages; Verso; Decoding the Civil War blog and Zooniverse | item JSON yes; huntington.org 429; Zooniverse API and Talk JSON yes; project blog yes (140 posts read); NHPRC proposal PDF yes; OAC finding aid via browser | every metadata field of pointers 8941, 8950, 9035 and object 9302; workflows and Talk boards; all blog posts | no decoded field anywhere; no decoding workflow; one prior Cipher No. 1 reading of an mssEC 19 entry on the blog (section 12); no reading of pages 49, 58, 142 |
| 8 | Cryptiana | yes (snapshot and live) | civilwar1.htm, unsolved.htm for Eckert, mssEC, Wolford, Tecumseh | book concordance only; no ledger readings |
| 9 | IA full text | yes | phrase searches listed above | as above |
| 9 | HathiTrust full text; Google Books | **unreachable**: HathiTrust 403 to curl; Google Books API 429; the repo's browser tool fails behind this proxy with ERR_CERT_AUTHORITY_INVALID (Chromium does not trust the proxy CA; the fix is to give Chromium the CA bundle, not to ignore certificate errors) | none | not searched |
| 10 | GitHub (Bourdeau, Aymeloglu, Bean), cipher blogs | github.com 403/400 to curl; WebSearch used instead; cipherbrain.de TLS error | "Eckert", "mssEC", "Cipher No. 1", "Decoding the Civil War" | nothing found |
| 11 | JSTOR / Google Scholar / dissertations | JSTOR client challenge (unreachable); Scholar via browser: "Thomas T. Eckert Papers" no articles; Blickhan and Van Hyning 2026 checked | nothing on the ledgers' decoding |

Also searched: WebSearch on every distinctive phrase of the four plaintexts (no web page quotes E4, E5 or E6 as
decoded from the ledger; E12 hits are the printed Lincoln works and LoC).

## 5. E4: Fox to Butler, 21 April 1864, 9.30 PM

- Ledger: mssEC 19 p.49, CONTENTdm pointer 8941, telegram no. tel092; image images/mssEC19_p8941.jpg.
- Ciphertext (ciphertext.txt): "Geo D Sheldon Washn Apr 21st 1864 9.30 Pm / Rosetta, For, Knox, Unity, If, you,
  can, Block the Channel Baden Sidney so she can not get in to Pamlico Sound we will have some Camels made in a
  few days to lighten the Tecumseh Iron Clad so she can Cross the Bar at Hatter = as Platina feet and Protect
  all Navy of Baden Smyrna Yoke Asst Brenton[?] Fox How are you brave youths".
- Plaintext as read (reading.md): "For Maj Gen B. F. Butler. If you can block the channel Roanoke Island so she
  can not get into Pamlico Sound we will have some camels made in a few days to lighten the Tecumseh iron clad
  so she can cross the bar at Hatteras 8 feet and protect all navy of Roanoke Island. [signed] Asst [Secretary
  of the Navy] Fox". Code tokens H 11, M 0; 10 of about 63 words.
- Prior plaintext of this telegram: **not located** in OR I/33 (pp.278-279, 938-942), ORN I/9 (pp.647-690),
  Butler Corr. IV (pp.112-120), Fox Confidential Correspondence, Butler's Book, IA full-text search on
  "lighten the Tecumseh", "camels made", "cross the bar at Hatteras", "get into Pamlico Sound", "block the
  channel".
- Substance in print: Butler's reply, "Fort Monroe, April 21, 1864—12 p. m. (Received 3 a. m., 22d) ... She
  will have done all the mischief she can do, probably, before our obstructions and your camels could be ready
  ... Will send your telegram to Graham, with instructions to sink the obstructions if practicable", OR I/33
  p.279 (also ORN I/9 pp.650-651 dated 22 Apr; Butler Corr. IV pp.114-115, where the OCR reads "your cannon").
  Fox to Ericsson, Navy Department 21 Apr 9.20 p.m.: "A rebel ram has got into the sounds of North Carolina and
  is doing some damage. Can you have camels made to lift the Tecumseh so she will go over a bar with only 8
  feet of water on it?", ORN I/9 p.667; and 22 Apr, p.683. The 9.20 p.m. Ericsson telegram and the 9.30 p.m.
  Butler telegram are the same decision, sent ten minutes apart.
- Prior decipherment of the ledger copy: none found. The Huntington record for this page (created 15 Mar 2018,
  Decoding the Civil War consensus transcription) publishes the whole entry with the plain words in clear and
  the ten code words unresolved. The volunteers read "Waxy" where ciphertext.txt reads "Navy" (residual for the
  solver: check the image).
- Evidence quality: high for the negatives in the sources listed (page-level reads, not only greps); the
  unsearched sources are HathiTrust, Google Books, the OR Supplement, the Fox Papers (New-York Historical
  Society) and the War Department telegram copies in NARA RG 107, any of which could hold the plaintext.
- Classification: **N3**, confidence moderate. Not N4 because two full-text engines and the archival copies
  were not searched.
- Safe sentence: "The text of Fox's 9.30 p.m. telegram to Butler of 21 April 1864 was not found in the Official
  Records, the Navy Official Records, Butler's or Fox's printed correspondence; its content is known from
  Butler's reply (OR I/33 p.279) and from Fox's parallel telegram to Ericsson (ORN I/9 p.667); the ledger copy
  was read from the cipher book at grade H, and most of its words were already in clear on the Huntington page."
- Unsafe sentence: "A previously unknown telegram from Fox to Butler, deciphered for the first time."

## 6. E5: Meigs to Butler, 22 April 1864, 10.45 AM

- Ledger: mssEC 19 p.49, pointer 8941, telegram no. tel093.
- Ciphertext: "Geo. D. Sheldon Washn D.C. Apr. 22nd 1864 10.45 Am / Elizabeth, Harsh, Peach, For, Knave, Unity,
  Dispatch, of, last, night received I learn that there are Pension Waldo Spit here for Animal instead of
  Pebble Whips You have all the Whig and should send it up for them zebra Send also for a Purple Panama Spartan
  now at the Pacific queenly[?] here & ready to go to you Yoke Bender".
- Plaintext as read: "[22] For Maj Gen B. F. Butler. Dispatch of last night received. I learn that there are
  4000 men here for [Fort] Monroe instead of 3 regiments. You have all the transportation and should send it up
  for them. Send also for a 1000 cavalry horse[s] now at the cavalry depot here & ready to go to you. [signed]
  Quartermaster General". Code tokens H 20 of about 60 words.
- Prior plaintext of this telegram: **not located** in OR I/33, I/36 pt 2, ser. III vol 4, Butler Corr. IV,
  IA full-text search ("instead of three regiments", "now at the cavalry depot", "you have all the
  transportation", "Dispatch of last night received", "four thousand men here", "4,000 men here").
- Substance in print: the antecedent, Butler to Meigs 21 Apr 1864: "I understand that there are three (3)
  Veteran Regts. of the 10 Army Corps at Alexandria, coming to join Gen'l Gillmore here. Will you send them, or
  shall we send up transportation?" (Butler Corr. IV p.112); the horses in Halleck to Butler 21 Apr 4.30 p.m.,
  "One thousand horses will be sent to you in preference to all others" (OR I/33 p.938; the ledger's p.48 entry
  is this telegram) and Halleck to Grant 22 Apr 2.30 p.m. (OR I/33 p.940; the ledger's p.50 entry).
- Prior decipherment of the ledger copy: none found; the Huntington page transcription (2018) carries the
  entry with about 40 words in clear.
- Evidence quality and unsearched sources: as for E4, plus the Meigs Papers (Library of Congress) and the
  Quartermaster General's letters sent in NARA RG 92.
- Classification: **N3**, confidence moderate.
- Safe sentence: "Meigs's telegram to Butler of 22 April 1864 was not found in the Official Records or in
  Butler's printed correspondence, which prints the telegram it answers; the ledger copy was read from the
  cipher book at grade H."
- Unsafe sentence: "An unpublished Meigs telegram recovered from cipher."

## 7. E6: Halleck to Sherman, 26 April 1864, 3 PM

- Ledger: mssEC 19 p.58, pointer 8950, telegram no. tel111.
- Ciphertext: "F. S. Van Valkenburg Washn D.C. Apr 26th 1864 / Growl , April, Harsh, Pledge, Imogene, For,
  Kitchen, Embrace, unity The third Antwerp Panama can be mounted at Gaul unity Its last orders were for girls
  where shall it go yoke Jacob Bates & Charlie are here".
- Plaintext as read: "[Washington] Apr 26 3 PM For Maj Gen W. T. Sherman, Nashville. The third Iowa Cavalry can
  be mounted at St Louis. Its last orders were for Vicksburg. Where shall it go? [signed] [General-in-Chief]
  Bates & Charlie are here". Code tokens H 14 of about 30 words.
- Prior plaintext: **yes.** OR ser. I vol 32 pt 3 (GPO, 1891), p.498: "WASHINGTON, D. C., April 26, 1864—3 p.
  m. Maj. Gen. W. T. SHERMAN, Nashville, Tenn.: The Third Iowa Cavalry can be mounted at Saint Louis. Its last
  orders were for Vicksburg. Where shall it go? H. W. HALLECK, Major-General, Chief of Staff." Word for word
  with the reading (OR "Saint Louis"; the operator's tail "Bates & Charlie are here" is not printed). Sherman's
  reply follows on the same page ("The Third Iowa should stop at Memphis ... W. T. SHERMAN", received 9.36
  p.m.). Verified in two IA copies, warofrebellion323unit (OCR line 42335-42346) and warofrebellion013203rootrich;
  the volume's index lists the regiment at pp.399, 436, 498, 537. Also quoted in an annotation of The Papers
  of Ulysses S. Grant vol 10 (SIU Press, 1982), p.562 (read in full via Google Books preview, volume id
  `7DAAxfRuXKoC`, 21 Sept 2026), which itself cites "O.R., I, xxxii, part 3, 498". Related: Halleck to Davidson
  27 Apr, OR I/34 pt 3 p.309; Davidson to Sherman 29 Apr, OR I/32 pt 3 p.537.
- Prior decipherment of the ledger copy: none found.
- Evidence quality: high (page read in two scans; exact match).
- Classification: **N1**, confidence high. The solver's sweep covered vol 32 pt 3 and missed the page.
- Safe sentence: "E6 is printed in OR I/32 pt 3 p.498; the ledger copy was read independently from the cipher
  book and agrees word for word."
- Unsafe sentence: "A Halleck telegram the Official Records never printed."

## 8. E12: Lincoln to Col. Frank Wolford, 4 August 1864, 4.30 PM

- Ledger: mssEC 19 p.142, pointer 9035, telegram no. tel266.
- Ciphertext: "Capt Sam Bruch Washn Aug 4th 1864 4.30 Pm / Growl Aug Pension Katy For Paradise Frank Wal ford
  Yours of yesterday received zebra Before interfering with the Judge Advocate Shelters order I should know his
  reasons for making it zodiac Mean while if you have not already started wait till you hear from me again
  zodiac Did you receive letter & inclosures from me Star Walrus Ingress Warm[?] & dear need rain".
- Plaintext as read: "[Washington] Aug 4 4.30 PM For Colonel Frank Wolford. Yours of yesterday received. Before
  interfering with the Judge Advocate General's order I should know his reasons for making it. Meanwhile if you
  have not already started wait till you hear from me again. Did you receive letter & inclosures from me?
  [signed] [President of the U.S.]". Code tokens H 11 of about 65 words.
- Prior plaintext: **yes, from 1864 on.**
  1. "Campaign documents. 'To whom it may concern.' The Crittenden resolution ... Colonel Frank Wolford—a
     statement. Gen. McClellan's letter of acceptance" (Osborne & Co., printers, [New York, 1864]; IA
     campaigndocument00unse), p.21: "Washington, D. C., August 4, 1864. To Colonel Frank Wolford, Louisville,
     Kentucky: Yours of yesterday received. Before interfering with the Judge Advocate General's order, I should
     know his reasons for making it. Meanwhile, if you have not already started, wait till you hear from me
     again. Did you receive letter and inclosure from me? ABRAHAM LINCOLN, President U. S." Printed with
     Wolford's telegram of 3 Aug ("The Judge Advocate has notified me to report immediately to him at
     Washington to be tried before a military commission ...") and his reply of 5 Aug. Wolford's statement
     was campaign material of September 1864.
  2. Nicolay and Hay, Complete Works of Abraham Lincoln (1894); 1905 Tandy edition vol 10 pp.180-181 (IA
     completeworksofa10lincuoft), "Telegram to Colonel Wolford", same text ("his reason").
  3. Basler, Collected Works of Abraham Lincoln vol 7 (1953) pp.479-480, "To Frank L. Wolford", headed
     "Cypher", War Department, Washington City, August 4, 1864: "Yours of yesterday received. Before
     interfering with the Judge Advocate General's order, I should know his reasons for making it. Meanwhile,
     if you have not already started, wait till you hear from me again. Did you receive letter and inclosures
     from me? A LINCOLN". Source line: "ALS, DNA WR RG 107, Presidential Telegrams, I, 122"; the footnote
     quotes Wolford's telegrams of 3 Aug and 5 Aug (DLC-RTL). Read in full from the Michigan digital edition
     through the Wayback Machine (quod.lib.umich.edu/l/lincoln/lincoln7/1:1055; the live site is 403 here) and
     confirmed by the IA full-text snippets. So the plaintext original is Lincoln's autograph, marked "Cypher"
     for encipherment, in the War Department's telegram files at the National Archives; the Huntington ledger
     holds the cipher clerk's copy. (Basler 7:447 is the letter to Wolford of 17 July 1864.) Nicolay and Hay
     first printed it in Complete Works (1894) vol 2 p.558 (IA abelinccompwks02lincrich).
  4. Library of Congress, Abraham Lincoln Papers: Wolford to Lincoln, telegram, 3 Aug 1864 (mal3507500) and
     5 Aug 1864 (mal3509900) are the two ends of the exchange; no Lincoln-to-Wolford item of 4 Aug is in DLC,
     consistent with Basler's NARA source. Not found in: Papers of Abraham Lincoln digital edition (no Wolford
     documents yet), OR I/39 pt 2 (Wolford only pp.98, 116, June 1864), OR II/7, Lincoln Day by Day and the
     Lincoln Log for 4 Aug 1864.
- Prior decipherment of the ledger copy: none found.
- Evidence quality: high (three independent printings read from the scans).
- Classification: **N1**, confidence high. The solver wrote "may be in the Collected Works" and did not look.
- Safe sentence: "E12 has been in print since 1864 and is Basler CW 7:479-480; the ledger copy was read
  independently from the cipher book and agrees word for word."
- Unsafe sentence: "An unprinted Lincoln telegram."

## 9. Evidence table

| entry | earliest print located | citation | identifier / URL | match |
|---|---|---|---|---|
| E4 | none for the telegram; reply 1891 | OR I/33 p.279 (Butler to Fox, 21 Apr 12 p.m.); ORN I/9 p.667 (Fox to Ericsson, 21 Apr 9.20 p.m.) | archive.org/details/warofrebellion33unit ; archive.org/details/officialrecordso0009unse | substance only |
| E5 | none for the telegram; antecedent 1917 | Butler Corr. IV p.112 (Butler to Meigs, 21 Apr); OR I/33 p.938 (Halleck to Butler, 21 Apr) | archive.org/details/privateofficialc04butl ; warofrebellion33unit | substance only |
| E6 | 1891 | OR I/32 pt 3 p.498 | archive.org/details/warofrebellion323unit ; archive.org/details/warofrebellion013203rootrich | word for word |
| E12 | 1864 | Campaign documents (Osborne & Co.), p.21; Nicolay-Hay 1905 vol 10 pp.180-181; Basler CW 7:479-480 | archive.org/details/campaigndocument00unse ; archive.org/details/completeworksofa10lincuoft ; archive.org/details/collectedworksof0007royp | word for word ("inclosure" / "reason" variants) |

## 10. Did we first-decipher any of them?

- E6: no. Plaintext in print since 1891; the reading is an independent re-decipherment of the ledger copy.
- E12: no. Plaintext in print since 1864; independent re-decipherment.
- E4, E5: no prior decipherment of the ledger copies was located, and no prior print of the telegrams was
  located in the sources searched. That is the strongest defensible statement. It is not "first ever":
  HathiTrust, Google Books, the OR Supplement and the archival copies (NARA RG 107 telegrams sent; the Fox and
  Meigs papers) were not searched, the Zooniverse Talk subject comments could not be keyword-searched, and
  Huntington staff or volunteers may have read these lines without publishing. The cipher covered only 10 of
  63 and 20 of 60 words; the rest has been public on the Huntington site since 2018.

Confidence: high that E6 and E12 are N1; moderate that E4 and E5 are N3 rather than N1 (the unsearched
full-text engines are the main risk) and certain that they are not above N3.

Residuals for the solver, not for this audit: (a) E4 "Navy" vs the volunteers' "Waxy"; (b) the project blog
("Bonkers", 12 Oct 2017) states that Cipher No. 1 was withdrawn after operators were captured in September
1864, while E15-E20 (Sept-Dec 1864) read cleanly with it here; the reading stands on the book, but the
statement should be reconciled in NOTES.md.

## 11. Postmortem

Which failures occurred, in order of weight:

1. **Absence from one canonical source treated as novelty.** A negative from a sweep of OR series I was passed
   upward as "the Official Records never printed" and then as "new readings". Rule 3 of CLAUDE.md already
   forbids a negative without a control; the same logic applies to a search negative: it means nothing beyond
   the sources and the method it names.
2. **Sender- and recipient-specific editions never searched.** Butler's Correspondence, the Navy OR, the Lincoln
   works, the Grant Papers: each is the first place a historian would look for the sender concerned, and each
   was known to the solver (NOTES.md even names the Collected Works as a possibility).
3. **No phrase search after decoding.** Once the plaintext existed, a quoted-phrase search on the Internet
   Archive full-text index would have found E6 and E12 in seconds; it was never run.
4. **A recorded doubt not resolved.** "which may be in the Collected Works" was written into NOTES.md and the
   claim was still reported as "not printed".
5. **A non-reproducible negative.** The or_check identifiers and commands were never committed, so the E6 miss
   cannot be diagnosed with certainty (rule 7 applies to negatives as much as to readings).
6. **The plain-word share not weighed.** These telegrams are mostly in clear on a public website; calling them
   "unpublished plaintext" was never defensible even if no print had existed.
7. **No separate verifier.** The solver, the orchestrator and the reporter were the same chain; nobody was
   tasked to disprove the claim before it reached the owner. CLAUDE.md rule 10 and the Verifier brief now
   require it.

Files and sentences corrected in this commit: NOTES.md section 1 ("decoded nowhere"), section 4 ("4 are not")
and section 7; reading.md summary table (four "not printed" cells) and the paragraph below it; status.json
(target note, worker job line, log line of 20 Sept 00:00); STATUS.md rows 24 and 37; dashboard.html
regenerated from status.json. Not touched: ciphers/eckert-1862/NOTES.md section 1 ("No decoded texts were
published by the project") is outside this brief but is contradicted by the project blog posts cited in
section 12 and should be softened to "no systematic decoding; single entries read on the blog".

## 12. Corpus question, kept separate

Written after sections 1-11 were committed (ae37197). This conclusion does not depend on the four-message
verdict and the four-message verdict does not depend on it.

**Question 1: has anyone systematically mapped the Eckert ledger entries (mssEC 1-35) to cipher system, key,
plaintext, provenance and prior publication?** Not found in the sources searched. What exists:

- The finding aid (Online Archive of California, ark:/13030/c86m3964, "Thomas T. Eckert Papers, 1861-1877",
  Huntington Manuscripts Department, 2014; reproduced as Appendix B of the NHPRC proposal) maps volumes to
  series and date ranges and says only: "These include telegrams both still in code and decoded (the sent
  messages are ciphered; the received telegrams are mostly decoded)." Series 1: fourteen received volumes
  (Feb 1862-Aug 1867) and seven sent volumes (Feb 1862-July 1867); series 5: 32 cipher volumes, "eight copies
  of cipher book #1 (1861-1862); two copies of cipher book #2 (approximately 1866); 18 copies of cipher book
  #5 (1865-1866); and 1 copy of cipher book #9 (approximately 1865)".
- The NHPRC proposal (archives.gov/files/nhprc/announcement/literacy-transcribing.pdf, 2014) gives per-volume
  page counts (Appendix C) and the estimate "15,922 telegrams, of which perhaps 5,400 (34 percent) are
  enciphered" (p.4). No per-entry cipher map.
- The Huntington item records give, per page, telegram numbers and a keyword field and the volunteer
  transcription; object 9302 (mssEC 19) carries "Approximately 824 telegrams, 4 of which have been partially
  or completely crossed out" and "Transcription text provided by the volunteers of Decoding the Civil War
  (2016-2017)". No field for cipher, key, plaintext or publication.
- Tomokiyo, civilwar1.htm, maps the cipher books (mssEC 37-67) to Stager's numbered ciphers, not the ledger
  entries; the project blog's "Happy Birthday General Grant!" (27 Apr 2017) lists Grant's arbitraries per
  cipher ("Cipher 1: Judah, John, Juno, Jupiter, Japan & Jersey"), which dates entries by marker words, the
  method NOTES.md section 2 uses.
- The project blog read single entries: mssEC 19 p.[47], Grant to Sherman 31 Mar 1864, with Cipher No. 1
  from mssEC 44 ("Now, Jesse", 26 June 2017, matched to OR I/32 pt 3 p.213); mssEC 15, Lincoln to McClellan
  21 Apr 1862, in "a code that has not survived" ("Reverse Engineering Lost Codebooks", 21 Apr 2017); an
  entry read with the mssEC 46 corrections ("Laughing Matter", 1 Sept 2017); and mssEC 19 pp.293-295, the
  1865 Stager/Lynch test ciphers, identified via OR I/47 pt 2 p.475 without a word-by-word reading
  ("Bonkers", 12 Oct 2017). No table linking entries to cipher number, key, plaintext and publication was
  found anywhere; this repo's eckert-1862 and eckert-1864 NOTES appear to be the first such attempt, and they
  cover 30 entries of about 16,000.

**Question 2: was the Decoding the Civil War decoding phase completed publicly, internally, partially, or not
at all?** Not at all in public; nothing found says it was done internally. The evidence in order:

1. Plan: NHPRC proposal (2014), p.10: "The project will first ask users to transcribe telegrams, and then
   give them the opportunity immediately thereafter to use cyphers from the Eckert Archive and the Friedman
   Collection ... When complete, the transcriptions and decoded messages will be ingested into the Huntington
   Digital Library." The Huntington's own pages (huntington.org/verso/decoding-civil-war, read through search
   snippets only, the site answers 429): "In the final phase, code books in the archive will be used to
   decipher the encoded telegrams."
2. Phase 1 done: blog "Phase 1 Transcription Complete! Huzzah! Huzzah! Huzzah!", 15 Nov 2017; Zooniverse
   workflow 1874 (experimental_marking_flow) finished 15 Nov 2017 with 12,921 subjects retired; project record
   (api/projects?slug=zooniverse/decoding-the-civil-war): state "finished", 131,170 classifications.
3. Phases 2 and 3 designed: blog "Decoding the Civil War: Phase 2, Two Work Flows, Your Choice", 28 Sept 2017:
   "The first work flow, Code Words, is marking the arbitraries, or code words, for those messages in code.
   These coded telegrams will then be fed into Phase 3, the final decoding of the telegrams." Phase 2 ran only
   as a beta (Talk, "Phase 2 Beta Test 2!", Nov 2017). Every production workflow (ids 1452, 1874, 2126, 3309,
   6156, 6162) is a transcription workflow; none marks code words or decodes.
4. Pause: Zooniverse Talk thread 667515, Mario Einaudi, 19 June 2018: "Phase 2 is in the wings almost ready to
   launch. We continue to work on glitches in the programming."
5. End: blog "Decoding the Civil War: End", 31 July 2019 (also Talk thread 1075645): "Decoding the Civil War
   has been on pause since January 2018. We first attempted to build a new crowdsourcing interface, called
   Phase 2 ... However, this tagging of individual telegrams ran into significant technical difficulties.
   Therefore ... it was decided this past June follow a new path. We will instead extract through text mining
   the data required." Phase 3 is not mentioned; the text mining concerns sender, recipient and date.
6. Aftermath to 20 Sept 2026: the Huntington records carry no decoded field; no dataset, paper or report on
   the text-mining path or on any decoding was found (WebSearch 2022-2026; Google Scholar "Thomas T. Eckert
   Papers" returns no articles; Blickhan and Van Hyning 2026 does not mention the project; no NHPRC final
   report online). The Zooniverse Talk subject comments (about 6,000) could not be keyword-searched through the
   API, so a volunteer's decoding of a particular entry there cannot be excluded.

So: the decoding phase was planned (2014), announced as Phase 3 (Sept 2017), never launched, and dropped
without mention when the project closed (July 2019). Whether Huntington staff decoded anything after 2019
could not be determined; nothing published says so. Sources unreachable for this section: huntington.org
(429), JSTOR (client challenge), scienceblog.zooniverse.org (proxy 502), ArchiveGrid (403), OAC full-text
search (JavaScript challenge; the base finding-aid page was read).

Implication for the target, independent of sections 1-11: the ledgers remain a transcription-only corpus in
public. Reading them from the surviving books is straightforward where a book survives (Cipher No. 1, 2, 5,
9) and the value lies in the entries whose plaintext is not otherwise in print, which can only be established
entry by entry with the search of section 4, never assumed. The project's own statement that Cipher No. 1 was
withdrawn after the September 1864 captures ("Bonkers") should be tested against the Sept-Dec 1864 entries
this folder reads with it.

## Second audit (adversarial), 24 Sept 2026

A separate verifier session (brief from the orchestrator, session_01EFmUvFAifLKGdBSsW9mjEG), working 02:54-03:10
UTC. It took no part in the solving or the first audit. Its only job was to find E4 and E5 in print. It did not
decode. Claim under audit: sections 1, 5 and 6 above, "E4 and E5 N3, no prior print or decipherment located".

### Verdict

| entry | prior plaintext | prior decipherment | class | change |
|---|---|---|---|---|
| E4 Fox to Butler, 21 Apr 1864 9.30 PM | no (not located in 13 printed volumes read by full text, nor in the 10 volumes of OR Supplement pt I by token count, nor by Google Books phrase search, nor in the Lincoln Papers) | no; both Huntington ledger copies are ciphertext with the code words unresolved | **N3** | confirmed, not raised |
| E5 Meigs to Butler, 22 Apr 1864 10.45 AM | no (same families) | no; as E4 | **N3** | confirmed, not raised |

Not raised to N4 for two reasons. JSTOR was not searched. HathiTrust full-text search, across the whole
library, could not be run (Cloudflare); only the token counts of named volumes were checked. The same rule was
applied to Dupuy 468 and Gramont f.29r. Not lowered either: nothing in print carries either telegram.

### What this audit found that the first did not

1. **A second ledger copy of both telegrams.** The Huntington's collection-wide full-text search (CONTENTdm
   dmQuery on p16003coll11, the words "camels", "Pamlico", "Tecumseh", "cavalry depot") returns, besides mssEC
   19 p.49 (pointer 8941), **mssEC 25 p.77 (pointer 5621, tel153)**. That page holds E4 again: "Geo D Sheldon
   Washington April 21 1864 Geo D Sheldon Ft Monroe Rosetta for Knots unity if you can block the channel Baden
   Sidney ... Yoke ass Buxton Fawks how fie you brave youths Thos T Eckert". **mssEC 25 p.79 (pointer 5623)**
   holds E5 again: "Geo D Sheldon Washington April 22 1864 ... Elizabeth harsh peach for Knave unity dispatch of
   last night received ... yoke Bender Thos T Eckert". Both are ciphertext, with the same code words left
   unresolved in the volunteers' transcription. So this is not a prior decipherment and does not change the
   class. It does mean the plain words of both telegrams have been public twice on the Huntington site, not
   once. The same search also found the other ends of the exchange, in clear: Fox to Ericsson 21 Apr 9.40 PM
   (mssEC 18 p.50, pointer 9716, printed ORN I/9 p.667), and Butler's midnight reply as received (mssEC 10
   p.118, pointer 10260; mssEC 25 p.79 top, printed OR I/33 p.279).
   *Residual for the solver, not for this audit:* mssEC 25 is a second witness for the transcription. It reads
   "Buxton" where ciphertext.txt has "Brenton[?]", the one M token in E4 (applied 24 Sept 2026: ciphertext.txt now
   reads Buxton, grade H, E4's M count now 0 -- see NOTES.md "Second reader E4/E5, Applied, 24 Sept 2026"). It also
   reads "Knots" for "Knox" and "Spartans" for "Spartan" (Spartans applied). The volunteers read "waxy" where the
   ledger has "Navy" (applied), on both pages.
2. **OR I/33 prints the reply but not the telegram.** Read in context at p.279 (IA warofrebellion33unit):
   Butler to Fox, 21 Apr 12 p.m., ends "Will send your telegram to Graham". No Fox-to-Butler telegram of 21 Apr
   is printed on that page or anywhere else in the volume. The Google Books full-text copies of vol. 33
   (KHdYYXjL-X4C, wJgtAAAAIAAJ, House documents PM381btVBG0C) agree: they return the reply for "camels" +
   "April 21, 1864", and nothing else.
3. **Butler Corr. IV pp.111-116 read in context.** The 21 Apr sequence is: Halleck (horses); Butler to Meigs
   (three regiments, the message E5 answers); Butler to Fry, Shepley and Dahlgren; three Butler-to-Fox
   telegrams; Butler to Heckman, Palmer and Grant. None of the telegrams sent to Butler on 21 or 22 Apr by Fox
   or Meigs is printed.
4. **The secondary literature cites the Ericsson telegram, never the Butler one.** A search-within of each book
   gave these results. Hoogenboom, *Gustavus Vasa Fox of the Union Navy* (2008, JmDZ0QcCFgUC), paraphrases Fox
   to Ericsson; "Butler camels" returns 0 hits. Browning, *From Cape Charles to Cape Fear* (1993,
   TAMEDAAAQBAJ), pp.105-106, is the same. Newsome, *The Fight for the Old North State* (2020, 8h-uEAAAQBAJ),
   has "camels" only for the Albemarle's own floats (p.420) and "Tecumseh" 0 times. Still, *Confederate
   Ironclads at War* (dUCIDwAAQBAJ), has nothing on this exchange.

### Source-family log (24 Sept 2026)

All Internet Archive fetches used the metadata API and then the item's `_djvu.txt`, one fetch per volume, 1.5 s
apart. Texts were whitespace-normalised before grepping, which avoids the double-space trap of section 3. The
patterns searched were: camels; lighten the Tecumseh; block the channel; Pamlico Sound we; into Pamlico Sound;
bar at Hatteras; protect all; Roanoke Island so; instead of (three|3) regiments; cavalry depot( here)?; all the
transportation; (4,000|four thousand) men here; ready to go to you; (1,000|thousand) cavalry horses; dispatch of
last night received; here for (Fort )?Monroe. Two further checks: date-and-hour headers for 21 Apr 9.30 p.m. and
22 Apr 10.45 a.m.; and every "M. C. MEIGS" signature within 300 characters of a date of 21-23 April 1864.

| family | reachable | searched | result |
|---|---|---|---|
| (a) OR ser. I vol 33 | yes, IA warofrebellion33unit | all patterns; p.279 read in context | reply only (p.279); "cavalry depots" hits are Hagerstown etc. and Halleck to Grant 16 Apr; no E4, no E5 |
| (a) OR ser. I vol 36 pts 1-3 | yes, IA warofrebellion361unit, 362unit, 363unit | all patterns | only "all the transportation" in May 1864 contexts; no E4, no E5 |
| (a) OR ser. I vol 51 pt 1 (Union supplement) | yes, IA warofrebellion511unit | all patterns; every "April 21/22, 1864" header | Heckman order 21 Apr p.1159, Ninth Corps 22 Apr; no E4, no E5 |
| (a) OR ser. III vol 4 | yes, IA warofrebellionco0004genf | all patterns | Giesborough cavalry depot (administrative); no E5 |
| (a) OR Supplement (Broadfoot) pt I vols 1-10 | search-only on HathiTrust (record 002912198); HTRC Extracted Features per-page tokens | pages carrying "camels"; pages carrying "Meigs" or "Tecumseh" + Butler/Fox, with co-occurring tokens | "camels" on no page of any volume; no page has Meigs + Butler + April + 1864; the pt I v.6 pp.523-524 pair (Meigs/Monroe; Tecumseh/Butler/transportation) lacks "camels", "April" and "1864" |
| (a) ORN ser. I vols 9, 10 | yes, IA officialrecordso0009unse, 0010unse | all patterns | Fox to Ericsson (p.667), Butler to Fox (pp.650-651), Welles to Lee "into Pamlico Sound" (question, not E4); no E4 |
| (b) Butler, Private and Official Correspondence vol 4 | yes, IA privateofficialc04butl | all patterns; pp.111-116 read in context | antecedent to E5 (p.112) and reply to E4 (pp.114-115) only |
| (c) Fox, Confidential Correspondence vols 1-2 | yes, IA confidentialcorr01foxg, 02foxg | all patterns; every "April 21/22, 1864" | "camels" = Mobile/Tennessee (Farragut); no April 1864 Butler letter |
| (c) Meigs papers, printed | none exists (no printed Meigs letterbook located, as in section 4) | n/a | not searchable in print; Meigs Papers (LoC) and NARA RG 92 are unpublished archives |
| (d) LoC Lincoln Papers | yes, loc.gov collections JSON | dates 1864-04-21/22 (all items listed); q "Tecumseh camels"; q "Meigs cavalry horses Butler" 1864-04/05 | 21-22 Apr items are unrelated (Ford, Forney, Fry, Stanton, Brayman ...); keyword queries return one unrelated item each |
| (d) LoC Butler Papers | not digitised at item level | loc.gov search for the collection with online text | only books and other people's papers returned; item-level search impossible |
| (e) Huntington mssEC 19 p.49 metadata | yes, CONTENTdm API pointer 8941 | every field | title, callid, telkwd "tel092 : Hatteras", telnum; no decoded field |
| (e) Huntington collection full text | yes, dmQuery p16003coll11 | camels (6 pp), Pamlico (6), Tecumseh (12), cavalry depot (42), Roanoke (99); the camels and Pamlico pages opened | mssEC 25 pp.77, 79 duplicate ciphertext copies (above); nothing decoded |
| (f) Google Books API (key, country=US) | yes | 15 phrase queries (lighten the Tecumseh; camels made in a few days; block the channel + Roanoke Tecumseh camels; cross the bar at Hatteras; get into Pamlico Sound; protect all the navy; instead of three / 3 regiments; now at the cavalry depot; 4,000 men here; four thousand men here for; you have all the transportation; dispatch of last night received + Meigs Butler; Meigs Butler "April 22, 1864" horses; Fox Butler "April 21, 1864" camels), 7 combination queries, 11 search-within-volume queries in 5 books | 0 hits for every distinctive E4/E5 phrase; generic phrases hit unrelated texts; OR vol 33 copies return only the reply |
| (g) HathiTrust | catalog Bibliographic API and HTRC EF yes; full-text search no (Cloudflare, not tried again) | OR Supplement pt I vols 1-10, as above | negative at token level |
| (h) Solver repositories | yes, anonymous git clone: dbourdeau/cyphersolver c85ece1 (23 Sept 2026), aaymeloglu/unsolved-ciphers 2495c45 (23 Sept 2026) | grep eckert, mssEC, tecumseh, camels, Meigs | Bourdeau: only the Cryptiana list line on the Decoding the Civil War project; Aymeloglu: nothing |
| (h) Cryptiana | via the Bourdeau snapshot of unsolved.htm | as above | project mention only; no ledger readings |
| Web | WebSearch | "Fox" "Butler" "camels" "Tecumseh" "Pamlico Sound" 1864 telegram | nothing on this telegram |
| Not searched | — | JSTOR (credential session's task, outreach gate 2); HathiTrust whole-library full text; NARA RG 107 telegrams sent and RG 92 QMG letters sent (archival, not printed); Zooniverse Talk comments (not keyword-searchable, section 12) | — |

Request count, per host: archive.org 25; hdl.huntington.org 16; loc.gov 8; googleapis.com 22; books.google.com
11; catalog.hathitrust.org 1; data.htrc.illinois.edu 10; github.com (git) 2.

### Classification

**E4, Fox to Butler, 21 Apr 1864, 9.30 PM: N3.** Prior plaintext: none located. Prior decipherment: none; the
two Huntington transcriptions (mssEC 19 p.49 and mssEC 25 p.77) leave the code words unresolved. Evidence:
full-text negatives in every printed series where an editor would have put it (OR I/33, where the reply is
printed; ORN I/9, where the Ericsson twin is printed; Butler Corr. IV; Fox Corr.); a negative at token level in
the OR Supplement; phrase negatives on Google Books. Quality high for print. Confidence that it is not in print:
moderate to high. Confidence that no one has read the code words: moderate, since internal and archival work is
not excluded.
- Safe sentence: "Fox's 9.30 p.m. telegram to Butler of 21 April 1864, of which two ledger copies survive in the
  Huntington's Eckert Papers (mssEC 19 p.49, mssEC 25 p.77), was read from the surviving cipher book at grade H.
  No printed text of it was located in the Official Records (army, navy, supplement), Butler's or Fox's printed
  correspondence, or by Google Books phrase search (logged in AUDIT.md). Its substance is known from Butler's
  reply (OR I/33 p.279) and Fox's parallel telegram to Ericsson (ORN I/9 p.667). Most of its words were already
  public in clear in the Huntington transcriptions."
- Unsafe sentence: "A lost Fox telegram, deciphered for the first time and never before published."

**E5, Meigs to Butler, 22 Apr 1864, 10.45 AM: N3.** Prior plaintext: none located. Prior decipherment: none; the
two transcriptions (mssEC 19 p.49, mssEC 25 p.79) leave the code words unresolved. Evidence as for E4. No
printed Meigs edition exists, so the sender-side family is archival only. Confidence: moderate to high for print,
moderate for no reading at all.
- Safe sentence: "Meigs's telegram to Butler of 22 April 1864 (Huntington mssEC 19 p.49 and mssEC 25 p.79) was
  read from the surviving cipher book at grade H. No printed text of it was located in the Official Records,
  including series III and the supplement, in Butler's printed correspondence (which prints the telegram it
  answers, vol. 4 p.112), or by Google Books phrase search (logged in AUDIT.md)."
- Unsafe sentence: "An unpublished Meigs telegram recovered from cipher for the first time."

To reach N4, three things remain: the credential session's JSTOR queries on the E4 and E5 phrases and on
Fox-Butler, Albemarle and camels; a HathiTrust whole-library full-text search, from a browser that passes the
challenge or from the person; and, optionally, a look at the Meigs Papers finding aid. Until then no sentence
may use "first decipherment" or "previously unread", even with a qualifier.

### Postmortem

The first audit's N3 holds. It did miss the second ledger copy in mssEC 25, because it searched the item
records for p.49 and not the collection's full text. The miss changes no class. It does double the public
witnesses of the plain words, and it gives the solver a second witness for the one M token. Corrections in this
commit: the board's results entry ("N3, single audit" becomes "N3, two audits; N4 pending"), NOTES.md section 4
(adds the second copy and the second audit), and status.json's eckert-1864 target note. STATUS.md carries no
sentence about E4 or E5 that over-claims; the orchestrator adds the result line when it republishes the board.

## Toward N4, 24 Sept 2026 (gap worker)

A gap-closing worker, not a verifier (brief from LANE V orchestrator session_01B5x2Dshzz71xBzbJqFnXYQ), working
03:09-03:22 UTC. Its job was to close, or log as unreachable, the three items the second audit named as remaining
for N4. It assigns no class and did not decode. Claim under audit unchanged: E4 and E5, N3.

### 1. HathiTrust whole-library full-text search

Unreachable, confirmed again. `curl` to `babel.hathitrust.org/cgi/ls?q1=...&anyall1=phrase&field1=ocr&a=srchls&ft=ft`
(the phrase "camels made in a few days") returns HTTP 403. `tools/browser_fetch.js` against the same URL was
tried once: the headless Chromium session ran to its 60-second timeout without rendering a result, and the
agent-proxy log for that command shows a rejected CONNECT to `brunhild.challenges.cloudflare.com:443`
("organization policy" / could not reach the destination) — the same Cloudflare challenge the 20 and 23 Sept
sessions hit on `babel.hathitrust.org` and `manuscripts.nls.uk`. Not retried, per the one-retry-after-a-pause
limit and because the failure mode (a proxy-level block on the challenge host, not a transient timeout) would not
change on a second try. A Wayback Machine capture was not attempted: `web.archive.org` mirrors pages that were
crawled, and a dynamically-generated full-text-search results page for this exact multi-word phrase query was
never going to have been crawled and cached — there is nothing to look up in the CDX index for a URL no one else
has ever requested, so this route was ruled out on reasoning rather than tried and logged as a further failure.
**Status: unreachable (proxy-level Cloudflare block, consistent with three prior sessions on two different
HathiTrust-adjacent hosts).**

### 2. Meigs Papers (Library of Congress) and NARA RG 92 / RG 107, by finding aid and catalogue API

**Meigs Papers (LoC).** The Library of Congress's Montgomery C. Meigs Papers collection (`hdl.loc.gov/loc.mss/eadmss.ms006021`,
digitised at `loc.gov/collections/montgomery-c-meigs-papers/`) is searchable through the `loc.gov` JSON API
(`?fo=json`) scoped with `fa=partof:montgomery c. meigs papers`. A query for `letterbooks` (21 hits) surfaces a
digitised item exactly matching the month in question:

- **"Montgomery C. Meigs Papers: Correspondence, Military Orders, and Related Matter, 1853-1892; Letterbooks;
  1864, Apr."** — item id `mss325400076` (`loc.gov/item/mss325400076/`), digitised, 229 page images
  (`tile.loc.gov/image-services/iiif/service:mss:mss32540:mss32540-020:0127/...`), `online_format: ["image"]`,
  **no OCR or transcription layer** (the item JSON's `resources[0]` carries only `image`/`files`/`caption`, no
  text field). This is Meigs's own outgoing letterbook covering 22 April 1864, the date of E5; if a retained
  copy of his telegram to Butler survives anywhere in his own papers, page-by-page image review of this item
  (not attempted here — 229 unindexed images is a transcription-scale job, outside this brief) is where to look.
  A direct query for "Butler" against the whole Meigs Papers collection returns **zero** hits (the collection's
  finding-aid metadata does not index correspondent names within letterbooks), so the collection cannot be
  narrowed further by API search alone.
- No Meigs item titled or dated to suggest a separate "letters received" or "telegrams" series distinct from
  the chronological letterbooks was found; the finding aid groups his outgoing correspondence by date only.
- **Status: archival pointer only, not searched to text.** `loc.gov` requests: 13, sequential, ≥1.5 s apart, UA
  `cipher-lab research script (contact via repository)`.

**NARA catalog (catalog.archives.gov).** The v2 REST API (`/api/v2/records/search`) requires an API key (free
registration at archives.gov/developer; not in this environment's credential set, and registering one is the
person's decision, not logged as a blocker here since the brief asks for pointers, not the key itself). The
public search UI is a client-rendered SPA that returns the same HTML shell to `curl` regardless of query
(confirmed: identical ~in an HTTP 200 response with no result data). `tools/browser_fetch.js` renders it
correctly (no Cloudflare challenge on this host). Six browser fetches, ≥2 s apart:

1. `q=Quartermaster General telegrams sent 1864` (unfiltered) returns 4,023 hits, all Confederate QMG (RG 64/109)
   letter-and-telegram-book reels — wrong service, filtered out by record group in the next query.
2. `q=Meigs telegrams sent 1864&f.recordGroupNo=92` (RG 92, Records of the Office of the Quartermaster General)
   surfaces, at rank 1-2, two file units in a *different* record group that the search still returns as top hits:
   **"1864: Meigs (1 of 2)"** (NAID 295511864) and **"1864: Meigs (2 of 2)"** (NAID 295513365), both container
   "Roll 281" of **Record Group 107 (Records of the Office of the Secretary of War), series "Telegrams Sent by
   the Field Office of the Military Telegraph and Collected by the Office of the Secretary of War"** — this is
   the National Archives' own microfilm edition (M504) of the Secretary of War's copy of the Military Telegraph
   office's traffic, i.e. the institutional twin of the Huntington's Eckert Papers, filed by the *recipient's*
   surname rather than chronologically by ledger page. NAID 295513365's item page: 332 images, digitised from
   microfilm, downloadable as `M504-281A.pdf` / `M504-281B.pdf` (300 MB), **0/334 pages transcribed, no
   extracted text** — image only, exactly like the Huntington ledgers.
3. A phrase query `"1864: Butler"` scoped to RG 107 (130 hits) finds the corresponding file units for the
   *recipient* side of E4/E5: **"1864: Butler, B. F. (1 of 2)"** (NAID 295441024, Roll 237) and **"(2 of 2)"**
   (NAID 295442525, Roll 237), plus **"1864: Butler, B. F. THRU By (1 of 2)"** (NAID 295442927, Roll 238) and
   **"(2 of 2)"** (NAID 295444428, Roll 238) — same series, same record group. NAID 295441024's item page: **1,500
   images**, 0/1,500 transcribed. If a War Department telegraph copy of Fox's or Meigs's telegram to Butler was
   filed under the addressee's name (the normal practice for this series, per its own title), it is somewhere in
   these roughly 3,000+ un-indexed page images across rolls 237-238 and 281 — a transcription-scale search, not
   attempted here.
4. An unscoped `q=Butler telegrams&f.recordGroupNo=107` (23,243 hits) was tried first and returned an unrelated
   RG 92 personnel-index series ("Butler, Thomas A" etc., WWI-era burial records keyed on the surname "Butler");
   ruled out by inspection, not counted as informative.
- **Status: archival pointer only, not searched to text.** These are the concrete "NARA RG 92/RG 107 telegrams
  sent April 1864" identifiers the second audit named as unsearched; they now have NAIDs, roll numbers, and PDF
  download URLs on record, but no one has opened the images. Flag for whichever session next works this target:
  reading roll 281 ("1864: Meigs") around image ~150-200 (April, alphabetically-then-chronologically filed
  within the year, exact position not established) and the corresponding stretch of rolls 237-238 ("1864:
  Butler, B. F.") is the single most promising untried route to N4, more so than JSTOR or HathiTrust, because it
  is the other institution's copy of the same message traffic, not a printed edition — a match there would be
  N4 evidence of prior transcription-readiness, not proof of prior *publication*, so would still need framing
  carefully under rule 10 if pursued.

### 3. Secondary literature (Google Scholar / WebSearch)

Four WebSearch queries for the Fox-Butler-Ericsson "camels" exchange of 21-22 April 1864 and its Albemarle/Tecumseh
context: `Fox Ericsson "camels" Tecumseh Butler April 1864 monitor Albemarle`; `"Gustavus Fox" Butler Ericsson
camels ironclad dissertation Albemarle 1864`; `"Tecumseh" "camels" ironclad "Hatteras" 1864 telegram Butler
quartermaster`; `"Meigs" "Butler" "cavalry depot" April 1864 quartermaster transportation regiments Bermuda
Hundred`. No dissertation, article, or secondary source discussing this specific telegram exchange (Fox's "camels"
proposal to lift the Tecumseh over the Hatteras bar, or Meigs's 22 April transportation telegram) was found; hits
were general ship-history and campaign pages (Battlefield Trust, Wikipedia, NHHC, USNI Proceedings) that do not
mention Butler, Fox, or Meigs in this exchange. Consistent with the second audit's book-level search-within
results (Hoogenboom, Browning, Newsome: no hit on this exchange). No new source found; this negative adds
web-search coverage to the book-level negative already on record, not a new family.

### 4. JSTOR

One reachability probe, as the second audit and Gramont/Bowes/Courten audits already established for this
account: `curl` to `jstor.org/action/doBasicSearch?Query=...` returns HTTP 200 but the body is JSTOR's "Client
Challenge" interstitial (3,038 bytes), not search results — the same block recorded in ASKS.md row 17. Not
retried. **Status: unreachable from this environment, as before.**

Per the brief, the exact queries a person (or a session with a working JSTOR login) should run are recorded here
as a suggestion, not written into ASKS.md directly: `"Fox" AND "Butler" AND "Ericsson" AND camels AND 1864`;
`"Tecumseh" AND "camels" AND Hatteras`; `Meigs AND Butler AND "cavalry depot" AND 1864`; `"Army of the James" AND
Butler AND telegram AND April 1864`; `Eckert AND "Military Telegraph" AND cipher`. A corresponding suggestion line
is added to NOTES.md for whoever next edits ASKS.md row 17.

### Source-family log addendum (24 Sept 2026, gap worker)

| # | family | reachable | searched | result |
|---|---|---|---|---|
| 9 | HathiTrust whole-library full-text search | no (Cloudflare `brunhild.challenges.cloudflare.com` rejected by agent proxy policy) | one browser_fetch.js attempt, one curl 403 | not searched |
| 4 | LoC Meigs Papers (loc.gov JSON API) | yes | `letterbooks`, `Butler`, `letters sent`, `official correspondence`, `War Department correspondence`, item detail for mss325400076 | 1864 Apr. letterbook located (229 images, no OCR); no "Butler" hit; not read page-by-page |
| 6 | NARA catalog (catalog.archives.gov), browser | yes (no Cloudflare on this host) | `Meigs telegrams sent 1864` + RG92 filter; `"1864: Butler"` + RG107 filter; item pages for NAIDs 295513365, 295441024 | four "1864: Butler, B.F." file units (rolls 237-238) and two "1864: Meigs" file units (roll 281), all RG 107 series "Telegrams Sent by the Field Office of the Military Telegraph and Collected by the Office of the Secretary of War" (M504); ~3,000+ page images total, none transcribed; not read |
| 5, 11 | Secondary literature (WebSearch) | yes | four phrase queries on the Fox-Ericsson-Butler exchange and its ships | no source found discussing this exchange |
| 11 | JSTOR | no (Client Challenge, one probe) | `doBasicSearch` | not searched; suggested queries logged in NOTES.md for ASKS.md row 17 |

Request counts, per host: babel.hathitrust.org 1 curl + 1 browser attempt; loc.gov 13; catalog.archives.gov 6
(browser); jstor.org 2 (curl); WebSearch 4 (not host-limited). No logins, no credentials used or printed, no
decoding, no subagents, no changes to ciphertext.txt/reading.md/key material.

### Conclusion

None of the three named gaps closes N3 to N4 this pass. HathiTrust and JSTOR remain unreachable from this
environment by the routes available (same conclusion as 20-24 Sept prior sessions on other targets). The Meigs
Papers and, especially, the NARA RG 107 M504 series are now **concrete, citable archival pointers** rather than
the vague "archival, not printed" of the second audit — real NAIDs, rolls, and download URLs for the recipient-
and sender-side institutional copies of this exact message traffic — but they are unread; opening them is a
transcription-scale task for a future worker, not something this brief covers. E4 and E5 stay **N3**. No sentence
in this folder may use "first decipherment," "previously unread," "unpublished," or "never printed" for E4 or E5
until one of: (a) HathiTrust or JSTOR access is restored and searched, (b) the NARA M504 rolls named above are
read and either found empty of these telegrams (moving toward N4) or found to hold a prior transcription (moving
toward N0/N1), or (c) the Meigs 1864 April letterbook is read page-by-page for the 21-22 April dates.

## Open-index scholarship pass (24 Sept 2026)

Worker session (Sonnet, cap $8, orchestrator session_01EFmUvFAifLKGdBSsW9mjEG), replacing JSTOR as the
scholarship-coverage gate (CLAUDE.md, JSTOR-QUEUE.tsv rows 20-22; this covers the same JSTOR gap the gap worker
above named, run through the open indexes rather than JSTOR itself, per the owner's 24 Sept note). Not a
verifier session: does not move the N3 class for E4/E5, does not decode. Full per-host results in
`OPEN-INDEX-RESULTS.tsv` rows 20-22.

**OpenAlex and Semantic Scholar unreachable** for this whole pass (shared-IP daily anonymous budget exhausted /
429 on repeated attempts; identical failure across all five targets this pass covered, exact error text in
fr2980-gramont/AUDIT.md's equivalent section of this date). Logged as unreachable, not as a negative.

**CrossRef, Persée and HAL: no hit on E4, E5 or the Eckert ledgers.** CrossRef returns only keyword-collision
noise: several unrelated "Who Was Who"/ODNB entries whose subjects happen to have a birth or death date of "22
April" in some year (matched on the date string, not the 1864 telegram); Vernam's real but much-later and
unrelated 1926 AIEE paper "Cipher printing telegraph systems" (a one-time-pad paper, matched on "cipher
telegraph"); 1864-dated Scientific American telegraph-patent notices. Persée returns unrelated telegraph-history
articles (Chappe semaphore, transpacific and Indo-British submarine cables, the Ottoman sultan's telegraph) —
none on Eckert, the Military Telegraph office, or Cipher No. 1. HAL returns 0 hits for all three queries.

**`www.persee.fr` unreachable for rows 20-21 specifically** (its own two queries, "Fox Butler 1864" and "Meigs
Butler 1864"): both the scheduled request and the one allowed retry failed with `Recv failure: Connection reset
by peer`, no HTTP response either time. Row 22's Persée query succeeded normally in the same run, so this looks
like a transient per-request failure on those two specific queries rather than a host-wide block; not retried
further per the good-citizen rule. Logged as unreachable for those two rows only.

**Google Scholar (via WebSearch):** no source located for either E4 (Fox to Butler, 21 Apr 1864) or E5 (Meigs to
Butler, 22 Apr 1864) beyond what the first and second audits above already found — OR I/33 p.279 prints only
Butler's reply to E4, and ORN I/9 p.667 prints Fox's parallel telegram to Ericsson; Halleck's cavalry-to-Giesboro
instruction (already cited as OR I/33 p.938) is the only adjacent hit for E5. Row 22's query confirms only facts
already extensively documented in section 12 above (the Huntington's own collection description: 35 volumes,
~16,000 telegrams, roughly one-third enciphered) — no scholarly article on the ledgers' decoding was found on
any host, consistent with section 12's own finding that Decoding the Civil War's Phase 3 was never launched and
no paper or dataset followed it.

**Verdict for this pass:** no hit on any of the six hosts adds a print or decipherment of E4 or E5, or narrows
the JSTOR/HathiTrust gap named in the "Toward N4" sections above. This substitutes for, but does not close,
family (11)'s JSTOR gap and the second audit's "N4 requires: JSTOR queries... HathiTrust whole-library search...
Meigs Papers finding aid" list — the Meigs Papers and NARA RG 107 M504 pointers already located by the prior gap
worker remain the most concrete untried route. **E4 and E5 stay N3; the verifier does not move the class from a
scholarship-pass worker's report.**

Requests: api.openalex.org 8 (all 429, shared budget). api.semanticscholar.org 6 (all 429). api.crossref.org 3
(200 each). api.archives-ouvertes.fr 6 (3 combined-query 0-hit attempts, 3 narrower follow-ups). www.persee.fr 3
scheduled (1 succeeded 200; 2 failed with connection reset, each retried once per the single-retry rule, both
retries also reset). WebSearch 3 queries. No logins, no credentials, no decoding, no subagents, no changes to
ciphertext.txt/reading.md/key material.

## N4 decision, 24 Sept 2026

A fresh verifier session (LANE V, orchestrator session_01B5x2Dshzz71xBzbJqFnXYQ), 04:45-04:55 UTC. It did none
of the solving, auditing or gap work and did not decode. Question: does the logged coverage now meet rule 10's
N4 ("N3 with the principal editions, catalogues and project pages covered, internal or unpublished work not
excluded") for E4 (Fox to Butler, 21 Apr 1864 9.30 PM) and E5 (Meigs to Butler, 22 Apr 1864 10.45 AM)?

**Answer: no, not yet. E4 and E5 stay N3.** All principal printed editions and the holding archive's catalogue
are now covered. One principal project family is not: the Decoding the Civil War Zooniverse Talk subject
comments. This is the one public place where a volunteer's reading of these ledger entries could have been
posted, and this environment cannot reach it. Closing it takes a person with a browser and three searches (ASKS
row 27). If that search is negative, both telegrams go to N4 with no further work.

### 1. Principal families and coverage

| family | principal? | covered | where AUDIT.md shows it |
|---|---|---|---|
| OR ser. I (army), vols 33, 36 pts 1-3, 51 pt 1 | yes | yes, full text, p.279 read in context | s.4 row 1; second audit (a) rows |
| OR ser. III vol 4 (and ser. II) | yes (III); II marginal (prisoners) | III yes; II not located, not principal for a QMG/Navy telegram | s.4 row 1; second audit (a) |
| OR General Index | no, redundant: the volumes it indexes were full-text searched | not searched | s.4 row 1 |
| OR Supplement (Broadfoot) pt I vols 1-10 | yes | yes, at token level (HTRC EF): "camels" on no page; no Meigs+Butler+April+1864 page | second audit (a) Supplement row |
| ORN ser. I vols 9-10 | yes (E4 is Navy Dept traffic) | yes, full text, pp.647-690 read | s.4 row 2; second audit (a) ORN row |
| Butler, *Private and Official Correspondence* vols 3-4 | yes (recipient) | yes, vol 4 pp.111-120 read in context | s.4 row 3; second audit (b) |
| *Butler's Book* (1892) | yes (recipient) | yes | s.4 row 3 |
| Fox, *Confidential Correspondence* vols 1-2 | yes (sender E4) | yes | s.4 row 3; second audit (c) |
| Meigs, printed papers | sender E5 | none exists in print; archival only | s.6; second audit (c); Toward N4 s.2 |
| Lincoln Papers (LoC) and Basler, *Collected Works* | yes (period edition) | yes: LoC by date 21-22 Apr 1864 and keyword; Basler/Nicolay-Hay by phrase | s.4 row 4; second audit (d) |
| *Papers of Ulysses S. Grant* vol 10 (Jan-May 1864) | yes: the documentary edition whose annotations print RG 107 telegram copies around Butler, April 1864 (pp.338-345 on Plymouth) | **yes, this session** (Google Books search-within, 7DAAxfRuXKoC): "camels" 0, "Hatteras" 0, "lighten" 1 (p.253, Sherman, unrelated), "dispatch of last night" 7 (none Meigs/Butler), "cavalry horses" 9 (none E5), "4000 men" 3 (none E5); index: Tecumseh 372n, Pamlico 338n, Fox 166-7n, 224n, 345n, Meigs entries; no hit is E4 or E5 | this section, s.2 |
| Huntington catalogue: item records pointers 8941, 5621, 5623; object 9302 | yes (holding archive) | yes, every field | s.4 row 7; second audit (e) |
| Huntington collection full text (CONTENTdm, p16003coll11) | yes | yes, found the mssEC 25 duplicates; nothing decoded | second audit (e) |
| Huntington Verso / huntington.org project pages | yes | partly: huntington.org answered 429 on 20 Sept; read through search snippets; the same statements are in the NHPRC proposal and the blog, which were read | s.12 |
| Decoding the Civil War blog (WordPress) | yes (project) | yes: 140 posts read on 20 Sept; **this session** WordPress REST search of posts and comments (96 comments on the site) for camels, Tecumseh, Pamlico, Meigs, cavalry depot, Fox, Butler, Roanoke, Albemarle, Hatteras, mssEC 19, mssEC 25; hits read: "What Lies Beneath" (15 Oct 1864 Halleck telegram), "Those Must Have Been Some Terrible Horses" (Meigs, June 1863), other Butler/Tecumseh hits other dates; comment search 0 for every term | s.4 row 7; this section, s.2 |
| Zooniverse project records, workflows, Talk boards | yes (project) | yes, workflows and boards | s.4 row 7; s.12 |
| **Zooniverse Talk subject comments (about 6,000)** | **yes (project; the one public place a volunteer's reading of p.49 or mssEC 25 pp.77/79 could sit)** | **no**: not keyword-searchable through the API on 20 Sept; this session `talk.zooniverse.io` is refused by the egress proxy (CONNECT 502, organization policy), one retry after a pause, same result; WebSearch for the subject file names (mssEC_19_049, mssEC_25_077, mssEC_25_079) and for Talk + camels/Tecumseh/Pamlico/Meigs found no relevant page | this section, s.2 |
| Meigs Papers, LoC (1864 Apr letterbook, mss325400076) | no for N4: archival, unpublished, image-only | pointer only | Toward N4 s.2 |
| NARA RG 107 M504 rolls 237-238, 281 | no for N4: archival microfilm, not a publication; rule 10 N4 expressly leaves "internal or unpublished work not excluded" | pointer only | Toward N4 s.2 |
| HathiTrust whole-library full text | no for N4: a search engine, not an edition or catalogue. Every volume in which an editor would print these telegrams is covered above by IA full text, Google Books or HTRC token counts; the engine's remaining value is breadth over minor books, where Google Books phrase search (0 hits for every distinctive phrase) and IA full text stand in | unreachable (Cloudflare challenge host refused by proxy) | Toward N4 s.1 |
| JSTOR | no for N4: scholarship, not an edition or catalogue; per CLAUDE.md (24 Sept 2026) a queued JSTOR row never blocks N3 or N4 on its own. It is outreach gate 2 | unreachable; rows 20-22 queued | Toward N4 s.4; JSTOR-QUEUE.tsv rows 20-22 |
| Open indexes (OpenAlex, Semantic Scholar, CrossRef, Persée, HAL, Scholar) | no for N4 (scholarship); yes for outreach gate 2 | CrossRef, HAL, Scholar yes; Persée 1 of 3; **OpenAlex and Semantic Scholar still 429 this session** (3 queries each, one pass) | Open-index section; OPEN-INDEX-RESULTS.tsv |
| Solver repositories, Cryptiana | yes (cipher community) | yes | second audit (h) |
| Google Books phrase search, IA full text | yes (template family e) | yes | s.4 row 9; second audit (f) |

### 2. This session's search log

- Papers of U. S. Grant vol 10 (Google Books 7DAAxfRuXKoC, search-within endpoint on books.google.com, browser
  User-Agent): camels, Tecumseh, Pamlico, cavalry depot, three regiments, Fox, "Meigs, Montgomery", lighten,
  Hatteras, cavalry horses, 4000 men, "transportation and should", "dispatch of last night", "Roanoke Island".
  Snippets read; none is E4 or E5. The volume prints Grant to Butler 22 Apr noon (p.340) and Fox's ironclad
  news (p.345); it does not print Fox to Butler or Meigs to Butler.
- Decoding the Civil War blog: public-api.wordpress.com wp/v2 posts and comments search, 12 terms, plus one
  sanity query (comments "cipher" returned 4, so comment search works). No post or comment on these telegrams.
- Zooniverse: panoptes API reachable (project 2125, state finished; subject 2323456 = mssEC_15_151, a WebSearch
  hit, unrelated). talk.zooniverse.io refused by the egress proxy twice (04:46 and 04:49 UTC). Two WebSearch
  queries, nothing relevant.
- OpenAlex (3 queries): 429 "Rate limit exceeded". Semantic Scholar (3 queries): 429. Not retried in a loop.

Requests per host: api.openalex.org 3; api.semanticscholar.org 3; www.zooniverse.org 2; talk.zooniverse.io 2
(both refused at the proxy); public-api.wordpress.com 31; books.google.com 14; www.googleapis.com 1 (key check,
key not printed); WebSearch 4.

### 3. Decision per telegram

**E4, Fox to Butler, 21 Apr 1864 9.30 PM: N3 (not raised).** All principal editions are negative:
OR army/navy/supplement, Butler, Fox, Lincoln and Grant. The holding archive's catalogue and full text show the
entry twice, still in cipher. Of the project pages, the blog and the boards are negative. The Talk subject
comments are unsearched. The Talk is the family most likely to hold a prior decipherment, as opposed to a
print, because the volunteers had the cipher-book images and the blog shows staff decoding single entries with
Cipher No. 1 ("Now, Jesse", 26 June 2017). So it cannot be waived as non-principal.

**E5, Meigs to Butler, 22 Apr 1864 10.45 AM: N3 (not raised).** Same reasons. There is no printed Meigs
edition, so the sender side is archival only and does not count against N4.

Condition for N4, both telegrams: a keyword search of the Decoding the Civil War Talk
(zooniverse.org/projects/zooniverse/decoding-the-civil-war/talk, search box) for "camels", "Tecumseh" and
"Pamlico" (E4) and "cavalry depot" and "Elizabeth harsh" (E5), plus the Talk pages of the subjects for mssEC 19
p.49 and mssEC 25 pp.77 and 79, all negative. A person in a browser can do this (ASKS row 27), or any session
whose egress reaches talk.zooniverse.io. The verifier who logs that result may then set N4 without re-auditing
anything else.

Safe sentences, for use once N4 is set (not before):
- E4: "Fox's 9.30 p.m. telegram to Butler of 21 April 1864 (Huntington mssEC 19 p.49 and mssEC 25 p.77) was
  read from the surviving cipher book at grade H; no prior decipherment located, and no printed text of it
  located in the Official Records (army, navy, supplement), the Butler, Fox, Lincoln or Grant editions, the
  Huntington catalogue or the Decoding the Civil War project pages (search log in AUDIT.md). Its substance is
  known from Butler's reply (OR I/33 p.279) and Fox's parallel telegram to Ericsson (ORN I/9 p.667), and most
  of its words have been public in clear in the Huntington transcriptions since 2018. Unpublished archival
  copies (NARA M504, Meigs Papers) were not searched."
- E5: the same form, with "Meigs's telegram to Butler of 22 April 1864 (mssEC 19 p.49, mssEC 25 p.79)" and
  "Butler's printed correspondence prints the telegram it answers (vol. 4 p.112)".
- Unsafe, both: "A lost telegram, deciphered for the first time and never before published", or "first
  decipherment" without the qualifier "no prior decipherment located".

The safe sentences until then are the N3 ones in the second audit's Classification section.

### 4. Outreach gates (CLAUDE.md Outreach 1-6), for E4 and E5

| gate | met? | why |
|---|---|---|
| 1 verifier's class in AUDIT.md | yes | N3, three audits |
| 2 second adversarial audit; open-index pass; Google Books; JSTOR rows answered or waived | **no** | adversarial audit yes (second audit); Google Books yes; open-index pass only partly (OpenAlex and Semantic Scholar unreachable twice); JSTOR-QUEUE rows 20-22 `queued`, neither answered nor waived by the owner |
| 3 message is the audit's safe sentence, states prior print, links AUDIT.md | not yet drafted; satisfiable (the safe sentences name the prior print: OR I/33 p.279, ORN I/9 p.667, Butler Corr. IV p.112) | |
| 4 rule 10 wording | satisfiable with the N3 sentences; the N4 wording only after row 27 | |
| 5 logged in CONTRIBUTIONS.md before sending | no (nothing posted) | |
| 6 verifiable links (folder, primary image, printed edition at page) | satisfiable, not assembled: repo folder; Huntington CONTENTdm pointers 8941, 5621, 5623; IA warofrebellion33unit p.279, officialrecordso0009unse p.667, privateofficialc04butl p.112 | |

No post may go out on E4 or E5 until gate 2 is met.

### 5. Postmortem

Nothing over-claims. status.json and the board say "N3 ... N4 pending JSTOR and HathiTrust full text". That
names the wrong blockers for N4: JSTOR and HathiTrust are outreach and breadth items, not N4 blockers. The real
N4 blocker is the Talk subject comments. The orchestrator should correct that phrase when it next writes the
eckert-1864 row. This session did not edit status.json, because the class did not change.
