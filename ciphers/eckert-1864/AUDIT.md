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
  [Note 24 Sept 2026, V3a: superseded by the mssEC 25 collation (NOTES.md): "navy" is now "Waxy" = [South] (H) and
  the tail "Asst Buxton Fox" = Asst [Secretary of Navy] Fox (H); reading.md is the current text.]
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
   (mssEC 18 p.50, pointer 9716, printed ORN I/9 p.667) [note 24 Sept 2026, V3a: ORN I/9 p.667 prints "9:20 p. m." (IA
   officialrecordso0009unse text); 9.40 is the ledger time as transcribed here, not rechecked against the image], and Butler's midnight reply as received (mssEC 10
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

## Talk gap, second attempt (LANE W, 24 Sep 2026, 05:10 UTC)

LANE W orchestrator (session_011UFnhZnyCntZ8Bn9FpKyTq). No decoding, no reclassification. Goal: close the one
principal gap left by 'N4 decision' (Zooniverse Talk subject comments) through the Internet Archive.

- Subject ids, from the panoptes API (subject sets 4729 mssEC_19, 4705 mssEC_25; 10 requests):
  mssEC_19_049 = subject 2880207 (telegrams tel080, tel081); mssEC_25_077 = 2317144 (tel142-144);
  mssEC_25_079 = 2317146 (tel147, tel148). Talk pages:
  zooniverse.org/projects/zooniverse/decoding-the-civil-war/talk/subjects/{2880207,2317144,2317146}.
- Wayback CDX `url=talk.zooniverse.io/*`: `[]`, no captures of the Talk API host at all. Talk comments are served
  only by that host, so an archived copy of a zooniverse.org Talk page cannot replay its comments. The Wayback
  route cannot close this gap.
- Wayback CDX for the zooniverse.org Talk prefix and the three subject URLs: one answered `[]` (the bare
  zooniverse.org form of 2880207); the rest reset by web.archive.org (6 resets, 05:07-05:09 UTC). Stopped per the
  good-citizen rule.
- talk.zooniverse.io live: CONNECT refused by the egress proxy again (05:10 UTC, one request).
- WebSearch: the three subject ids; "decoding the civil war" talk + camels/Tecumseh/Pamlico/Butler. No relevant
  page.

**Result: gap not closed. E4 and E5 stay N3.** ASKS row 27 remains the route; it now carries the three direct
subject links. Requests: www.zooniverse.org 11; web.archive.org 8 (6 reset); talk.zooniverse.io 1 (refused);
WebSearch 2.

## Gap search, LANE W worker D, 24 Sept 2026

LANE W worker D (Sonnet, session_01F234Ho27aPryLTBhTerxbK), parent LANE W orchestrator session_011UFnhZnyCntZ8Bn9FpKyTq.
Rerun of OpenAlex and Semantic Scholar, per brief, alongside the same recheck for thurloe-printed P4 (see that
target's AUDIT.md "Gap search" section for the full method). No decoding, no reclassification. Clock read
06:43-06:50 UTC.

- **OpenAlex**: `Decoding the Civil War Huntington telegram` -- 429, "Insufficient budget... shared by everyone
  on your network's IP address... resets at midnight UTC" (whole-day, whole-IP exhaustion, same message as the
  "Open-index scholarship pass" section above). `Eckert cipher book Union telegraph 1864` -- 429, same message.
  Not retried per-query beyond the one retry already spent on the parallel P4 query (see thurloe-printed
  AUDIT.md); the message itself states the exhaustion is IP-wide and day-wide, so a second retry on each Eckert
  query would be the same known result, not new information.
- **Semantic Scholar**: `Decoding the Civil War Huntington telegram` -- 429 "Too Many Requests". `Eckert cipher
  book Union telegraph 1864` -- 429, same message.

**Result: both APIs still unreachable, confirming the "Open-index scholarship pass" and "N4 decision" findings
above rather than closing them.** No titles or DOIs to report. This does not change any class in this file.

Requests this session (shared with the thurloe-printed pass): api.openalex.org 2 for these two queries (429,
no retry, per the IP-wide exhaustion message already confirmed once this session); api.semanticscholar.org 2
for these two queries (429). One at a time, >=2s apart, no logins.

## Talk gap closed via talk.zooniverse.org (LANE W2 worker E1, 24 Sept 2026)

LANE W2 worker E1 (Sonnet, cap $5, for LANE W2 session_01CLm9uFwyau9hRmDcm2vALE), 11:00-11:05 UTC. No decoding,
no reclassification (per brief). The blocker in 'N4 decision' and 'Talk gap, second attempt' above was that
`talk.zooniverse.io` is refused by the egress proxy. `talk.zooniverse.org` (the same API on the plain `.org`
domain, not `.io`) answers plain curl with HTTP 200 JSON and is not blocked; this closes the gap without a
person in a browser (ASKS row 27).

**Method.** Comments and discussions endpoints direct on the three subjects, then a project-wide keyword search
via `/searches?section=project-<id>&query=<term>`. Project id 2125 confirmed via
`www.zooniverse.org/api/projects?slug=zooniverse/decoding-the-civil-war` (matches the id already recorded in
this file's 'N4 decision' search log). One request at a time, >=1.5 s apart.

**Per-subject direct check** (`/comments?focus_id=<id>&focus_type=Subject` and `/discussions?focus_id=<id>&focus_type=Subject`):

| subject | telegram(s) | comments | discussions |
|---|---|---|---|
| 2880207 (mssEC_19_049) | E4 tel080, E5 tel081 | 0 | 0 |
| 2317144 (mssEC_25_077) | E4 (second ledger copy) | 0 | 0 |
| 2317146 (mssEC_25_079) | E5 (second ledger copy) | 0 | 0 |

No volunteer or staff ever commented on, or opened a discussion thread on, any of the three subject pages that
carry E4 or E5.

**Project-wide keyword search** (`/searches?section=project-2125&query=<term>`), camels/Tecumseh/Pamlico/cavalry
depot/Elizabeth harsh from ASKS row 27, plus four more distinctive phrases from the E4/E5 readings (reading.md):

| query | hits | any on subject 2880207/2317144/2317146? | what the hits actually are |
|---|---|---|---|
| camels | 1 | no (subject 2880486) | an unrelated April 1865 Lincoln-Weitzel telegram where "Camel" is a misreading of "Campbell" (Judge Campbell) |
| Tecumseh | 2 | no (subjects 2323008, 2317286) | Sherman's own name (William Tecumseh Sherman) and a hashtag `#uss_tecumseh` on an unrelated ironclad-roster subject |
| Pamlico | 0 | -- | -- |
| cavalry depot | 0 | -- | -- |
| Elizabeth harsh | 0 | -- | -- |
| brave youths | 0 | -- | -- |
| Hatteras | 1 | no (subject 2316177) | an unrelated telegram about a bottle picked up off Hatteras |
| block the channel | 0 | -- | -- |
| cavalry horses | 9 | no (subjects 2313957, 2314422, 2314473, 2322487, 1959475, 2315656, 2315589, 2316617, 2881579) | nine unrelated telegrams about cavalry remounts (Rosecrans, Grant, Longstreet, Canby, etc.), none Meigs-to-Butler and none is E5's "1000 Cavalry Horses now at the Cavalry Depot" |

Every hit lands on a different subject from the three that carry E4 or E5, and every hit's content is a
different telegram. **No Talk comment anywhere in the project discusses, quotes, or offers a decipherment of
either E4 or E5.**

**Wayback CDX**, one request at a time, >=3 s apart (the three lost to resets in 'Talk gap, second attempt'
above): the zooniverse.org Talk prefix now has captures (it did not on 20 Sept per that section) --
`cdx/search/cdx?url=zooniverse.org/projects/zooniverse/decoding-the-civil-war/talk*` returns 7 rows, but every
captured discussion path (429/436984, 429/65061, 433/110335) is a different discussion id from the ones behind
subjects 2880207, 2317144, 2317146. The three subject-specific URLs
(`.../talk/subjects/{2880207,2317144,2317146}`) each still return `[]`, no captures at all -- consistent with
the live API's own 0 comments/0 discussions for all three: there is nothing on those pages for Wayback to have
captured. No resets this pass (4/4 CDX requests HTTP 200).

**Result: gap closed, negative.** Zooniverse Talk (comments, discussions, and a project-wide keyword search
across camels/Tecumseh/Pamlico/cavalry depot/Elizabeth harsh/brave youths/Hatteras/block the channel/cavalry
horses) carries no comment on subjects 2880207, 2317144 or 2317146, and no comment anywhere in the project that
discusses or decodes E4 or E5. Per 'N4 decision' above, this was the one uncovered principal family; not
reclassifying here (that is the verifier's call), but nothing found by this search stands in the way of N4 for
E4 and E5. Files: `sources/talk/{talk_2880207_p1,talk_2880207_disc,talk_2317144_comments,talk_2317144_disc,
talk_2317146_comments,talk_2317146_disc,search_queries.json}` (comment bodies, ids, created_at, discussion/board
ids only; no user names or ids kept, and the three subject/comment endpoints returned 0 rows so there was
nothing to redact there); `sources/talk/cdx/{talk_prefix,subject_2880207,subject_2317144,subject_2317146}.json`.

Requests: talk.zooniverse.org 15 (6 direct comments/discussions + 9 searches), www.zooniverse.org 1 (panoptes
project lookup), web.archive.org 4 (all HTTP 200, no resets). No subagents.

## N4 set (LANE W2 worker E2, 24 Sept 2026)

Verifier session (LANE W2 worker E2, session_012JuvHFkfXf9jFvxziRfhXo, for LANE W2 session_01CLm9uFwyau9hRmDcm2vALE),
11:24-11:27 UTC. Not the solver, not an earlier auditor, not the Talk searcher. No decoding. Question: with the
Talk gap reported closed by worker E1, does E4 and E5's coverage now meet rule 10's N4?

**Answer: yes. E4 and E5 are N4 (no prior decipherment located).**

### 1. Adversarial check of E1's Talk search (from sources/talk/ and one control)

| check | result |
|---|---|
| Were the per-subject endpoints returning data, not an empty shell? | E1 logged no positive control for them. **Control run this session:** `talk.zooniverse.org/comments?focus_id=2880486&focus_type=Subject` (the subject of E1's "camels" hit) returned HTTP 200, count 2, both comments `section: project-2125`. The same endpoint E1 used does return comments when a subject has them, so E1's `count: 0` on the three subjects is a real zero. |
| Was the search endpoint live? | Yes, its own positive control is in E1's JSON: search_queries.json holds real hits (camels 1, Tecumseh 2, Hatteras 1, cavalry horses 9) with bodies, all on subjects other than E4/E5's, and every hit is on board 429 or others in section project-2125. Stemming works ("camels" matched "Camel"). |
| Were the subject ids right? | Yes. Panoptes `api/subjects/{id}` this session: 2880207 = mssEC_19_049 (tel080; tel081), set 4729; 2317144 = mssEC_25_077 (tel142-144), set 4705; 2317146 = mssEC_25_079 (tel147; tel148), set 4705; all `links.project` 2125. Matches 'Talk gap, second attempt'. |
| Was the search limited to the right project? | Yes: `section=project-2125`, and project id 2125 = zooniverse/decoding-the-civil-war (E1's slug lookup; 'N4 decision' s.2). |
| Saved JSON consistent with the table? | Yes: six files, each `count: 0`, `page_count: 0`; the E4/E5 2880207 comments file is named `talk_2880207_p1.json` rather than `_comments`, same content form. |
| Residual | A comment that discusses these pages without any of the nine search terms and sits on a subject other than the three would be missed. The three subjects carry no comments at all, and the terms include both telegrams' distinctive words, so this residual is small. |

Requests this session: talk.zooniverse.org 1 (control); www.zooniverse.org 3 (panoptes subjects); >=2 s apart.

### 2. Is any other principal family open?

Re-read 'N4 decision' s.1 table, the second audit's source-family log and 'Toward N4'. The second audit named
JSTOR, HathiTrust full text and the Meigs finding aid as needed for N4. 'N4 decision' ruled that JSTOR is
scholarship (CLAUDE.md: a queued JSTOR row never blocks N4), HathiTrust's engine is breadth over the minor books
already covered by IA full text, Google Books and HTRC token counts, and Meigs and NARA M504 are archival
(N4 leaves "internal or unpublished work not excluded"). I agree with all three rulings. The one row marked
"partly" and principal, the huntington.org project pages (429 on 20 Sept), describes the project and not
individual telegrams. Its statements were read through the NHPRC proposal and the blog, and the holding archive's
catalogue and full text (CONTENTdm) were covered in full. I accept it as covered. The Talk was the only open
principal family, and it is now closed negative. **No principal family is open.**

### 3. Verdict

| item | telegram | prior plaintext | prior decipherment | evidence quality | confidence | class |
|---|---|---|---|---|---|---|
| E4 | Fox to Butler, 21 Apr 1864 9.30 PM (mssEC 19 p.49; mssEC 25 p.77) | not located; substance in print (Butler's reply OR I/33 p.279; Fox to Ericsson ORN I/9 p.667); 53 of 63 words in clear on the Huntington transcription since 2018 | none located (editions, catalogue, project blog, boards, Talk) | high for print and project pages; archival copies (NARA M504, Meigs Papers) unread | moderate to high | **N4** |
| E5 | Meigs to Butler, 22 Apr 1864 10.45 AM (mssEC 19 p.49; mssEC 25 p.79) | not located; the telegram it answers is printed (Butler Corr. IV p.112), follow-ups OR I/33 pp.938, 940; about 40 of 60 words in clear since 2018 | none located | as E4; no printed Meigs edition exists | moderate to high | **N4** |

Safe sentences (the 'N4 decision' s.3 forms, now in force):
- E4: "Fox's 9.30 p.m. telegram to Butler of 21 April 1864 (Huntington mssEC 19 p.49 and mssEC 25 p.77) was
  read from the surviving cipher book at grade H; no prior decipherment located, and no printed text of it
  located in the Official Records (army, navy, supplement), the Butler, Fox, Lincoln or Grant editions, the
  Huntington catalogue or the Decoding the Civil War project pages and Talk (search log in AUDIT.md). Its
  substance is known from Butler's reply (OR I/33 p.279) and Fox's parallel telegram to Ericsson (ORN I/9
  p.667), and most of its words have been public in clear in the Huntington transcriptions since 2018.
  Unpublished archival copies (NARA M504, Meigs Papers) were not searched."
- E5: "Meigs's telegram to Butler of 22 April 1864 (Huntington mssEC 19 p.49 and mssEC 25 p.79) was read from the
  surviving cipher book at grade H; no prior decipherment located, and no printed text of it located in the
  Official Records (army, series III, supplement), the Butler, Lincoln or Grant editions, the Huntington catalogue
  or the Decoding the Civil War project pages and Talk (search log in AUDIT.md). Butler's printed correspondence
  prints the telegram it answers (vol. 4 p.112), and most of its words have been public in clear in the
  Huntington transcriptions since 2018. Unpublished archival copies (NARA M504, Meigs Papers) were not searched."
- Unsafe, both: "A lost telegram, deciphered for the first time and never before published"; "first
  decipherment" or "previously unread" without "no prior decipherment located"; any sentence that omits the
  prior print of the substance or the clear words.

### 4. Outreach gate 2

Still open. JSTOR-QUEUE.tsv rows at file lines 20, 21, 22 (ciphers/eckert-1864) are `queued`, neither answered
nor waived. Open-index pass: CrossRef, HAL and Scholar done; Persée 1 of 3 (2 reset); OpenAlex and Semantic
Scholar 429 on every attempt (OPEN-INDEX-RESULTS.tsv rows 110-133). New ASKS row 41 (run or waive) and an update
line in outreach/gramont-jstor-waive.md. Gate 1 is met; gates 3-6 are as in 'N4 decision' s.4. No post until
gate 2 is met.

### 5. Postmortem

The only failure: E1 logged no positive control for the per-subject endpoint. It is now run, and it did not change
the result. Corrections in this commit: NOTES.md status lines (the N3 line and s.7 "No entry ... at N4"),
status.json's eckert-1864 target note ("N4 pending JSTOR and HathiTrust full text" named the wrong blockers) and
its results row (grade and gap), and ASKS row 41. ASKS row 27 was already marked answered. SECOND-OPINIONS-QUEUE
(SO-ECKERT-E4E5) and second-opinions/PROMPT-chatgpt.md exist, so they are not touched.

## Second opinion SO-ECKERT-E4E5 (ChatGPT, pull request 2), checked 24 Sept 2026, 16:30 UTC

Verifier V3a (Opus, for LANE V4, session_017iueT2nBBNcQkKp8Se8pcP). Input: `second-opinions/chatgpt-2026-09-24.md`
("GPT-6 (Codex)", copied from branch `second-opinion/SO-ECKERT-E4E5`, PR 2, unmerged). It reports no prior print and
no prior decipherment of E4 or E5, low confidence because its own access failed (IA, Butler IV scan), and seven remarks
on our apparatus. Each checkable claim was checked below. No decoding.

| # | claim | source checked | verdict | correction made |
|---|---|---|---|---|
| 1 | no page-verified print of either telegram; the surrounding traffic is Fox to Ericsson ORN I/9 p.667 (21 Apr, 9:20 p.m.) and p.683, Butler's reply OR I/33 p.279 and ORN I/9 pp.650-651 | IA `officialrecordso0009unse` djvu text, fetched once: "Navy Department, April 21, [1864]—9:20 p. m. A rebel ram has got into the sounds ... Can you have camels made to lift the Tecumseh ... G. V. Fox" to Ericsson; "April 22, 1864 ... before we can get our camels ready" to Ericsson; index "Ericsson, J. 667, 683"; no "camels made in a few days", "lighten the Tecumseh" or Fox-to-Butler telegram of 21 Apr in the volume | **right** (agrees with s.5 and the N4 set) | "Second audit" item listing "Fox to Ericsson 21 Apr 9.40 PM" now carries a note that ORN prints 9:20 p.m. (the 9.40 is the mssEC 18 ledger time as transcribed, not rechecked) |
| 2 | Butler Corr. IV p.114 holds Butler's 21 Apr reports to Fox and Halleck; Butler to Meigs IV p.112 | s.4 row 3 (vol 4 pp.112-120 read in full, three Butler-to-Fox telegrams pp.113-115) | **right**, already recorded | none |
| 3 | Fox, *Confidential Correspondence* I-II: not excluded by the second opinion (OCR failed) | second audit (c): both volumes searched on IA, every "April 21/22, 1864", "camels" = Mobile | **its gap, not ours**: covered | none |
| 4 | *Civil War Naval Chronology* (mirror): the "camels" hit is the Tennessee at Mobile | IA full-text API on `civilwarnavalchr0000vari_e2h9` (1971, lending-only): the only "camels" snippet is "over the Mobile bar using watertight caissons or 'camels'" | **right**; family now logged as searched (snippet level) | none |
| 5 | Tsapina, "Now, Jesse", 26 June 2017: Cipher No. 1 read on a mssEC 19 entry (Grant to Sherman, 31 Mar 1864), not E4/E5 | NOTES.md l.20-21 and s.12 already cite it the same way | **right**, already recorded | none |
| 6 | E5 header 10.45 AM vs derived 10.30 AM | reading.md block (`{time: 10.30 AM}`), key.md Elizabeth = 10.30 AM (TIME page, 315); NOTES.md already records the observation | **right**, already recorded in NOTES; the prompt did not say it | PROMPT-chatgpt.md now gives both times; reading.md E5 summary row states both |
| 7 | E4 signer: summary still says "Brenton" (M) while the derived reading renders Asst [Secretary of Navy] Fox, H 11 | reading.md summary table row E4 said `signer word "Brenton" (M)`; ciphertext.txt l.50 reads "Asst Buxton Fox" since the mssEC 25 collation; `decode.py --check` exit 0 | **right** | reading.md summary row and reconciliation note updated (Buxton, H); AUDIT s.5 plaintext line annotated (also its "navy" -> Waxy = [South]); the two E4/E5 summary rows now say N4, not N3 |
| 8 | the prompt's "eighteen other entries matched the Official Records" is wrong: 17 OR + E12 elsewhere | reading.md l.36-40, AUDIT s.8 (E12 in Lincoln's works, not the OR) | **right** | PROMPT-chatgpt.md corrected |
| 9 | the prompt's "dated at Fort Monroe" is wrong: the entries are headed Washington, addressed to Butler at Fort Monroe | ciphertext.txt headers "Washn Apr 21st 1864", "Washn D.C. Apr. 22nd 1864" | **right** | PROMPT-chatgpt.md corrected |
| 10 | "Roanoke Island" rests on "Inland [sic: Island]"; the correction is editorial | reading.md block and l.54 | **right**, already marked in the reading | prompt now says so |
| 11 | the two "she" have different antecedents (ram, then Tecumseh); Albemarle is contextual | the plaintext itself | **right** | prompt corrected |
| 12 | H grades cover code words, not clear words or identifications | key.md and decode.py grade only code tokens | **agrees**; no change | none |

**Families it named that no audit had logged, closed this session.** Plum, *The Military Telegraph during the Civil
War* (1882), vols 1-2 (IA `cu31924092908742`, `cu31924092908759`, full djvu text) and Bates, *Lincoln in the
Telegraph Office* (1907, IA `lincolnintelegra00bates`): no "camels", "Tecumseh", "cavalry depot", "instead of three"
or April 21/22 1864 hit; Plum names Geo. D. Sheldon only as an operator (Newport News). Elliott, *Ironclad of the
Roanoke* (1994, `_jt3AAAAMAAJ`) and Miller, *Second Only to Grant* (2000, `QtB2AAAAMAAJ`) are snippet-only on Google
Books and were located but not searched within: the host was held by a sibling verifier. **Residual, non-blocking**
(biographies, not editions).

**Its leads, one line each.** (1) NYHS Naval History Society collection MS 439, series 17 (Fox): archival; rule 10 N4
leaves unpublished work open; pointer for the person, not a class matter. (2) Meigs Papers, LoC: already a pointer
(Toward N4 s.2). (3) NARA RG 107 M504: already pointers (rolls 237-238, 281). (4) ORN as enclosures: vol 9 read in
context (pp.647-690). (5) mssEC 19 p.49 vs mssEC 25 pp.77, 79: done (NOTES.md collation, 24 Sept 2026).

**Class.** No check found a prior print or decipherment. **E4 and E5 stay N4** ("no prior decipherment located").
E6 and E12 untouched (N1).

**Postmortem.** The second opinion's reading remarks were right and all concern our apparatus, not the reading: a
summary row and a first-audit plaintext line not refreshed after the mssEC 25 collation changed two tokens, and a
prompt that turned the destination into the place of origin, counted the Lincoln print as an OR match and glossed
both "she" as the ram. Lesson (same as SO-GRAMONT-F29R): regenerate prompt facts and summary rows from the current
reading, not from earlier sections.

Requests: archive.org 11 (3 advancedsearch, 4 metadata, 4 djvu downloads), be-api.us.archive.org 4 (full-text
API), www.googleapis.com 2 (title lookups). No Gallica, no logins, no subagents.

## JSTOR (owner's machine, 24 Sept 2026)

Recorded by the JSTOR runner on the owner's machine (logged-in JSTOR account, built-in browser, one search per queue row, 6 s apart, no block page). First-page hits for every row are in `JSTOR-QUEUE.tsv`; only the hits that could print, calendar or discuss the letter were opened. No class is changed here; the verifier moves it.

Rows 20-22 answered (3 queries; rows 20 and 21 no hits). One hit opened:

- Roscoe Pound, "The Military Telegraph in the Civil War", *Proceedings of the Massachusetts Historical Society*, 3rd ser., 66 (1936-1941), pp. 185-203, https://www.jstor.org/stable/25080325 (read online). In-document search: "Eckert" 3 hits (pp. 195, 197), all on the Military Telegraph's independence from field commanders (Eckert's report praising Caldwell, OR ser. I vol. 51 pt 1 p. 200; Van Duzer answerable only to Eckert; Eckert holding up Grant's orders to Thomas), drawn from the Official Records. Nothing on Fort Monroe, Cipher No. 1, the Huntington ledger or the April 1864 Fox and Meigs telegrams.

## Outreach gate 2: JSTOR family and open indexes (verifier V5, 24 Sept 2026)

Verifier V5 (Opus, for LANE V4, session_01UBQ2tN51FBuKTx41RqnGAK), 24 Sept 2026 17:24 UTC. Triage of the JSTOR runner's first-page hits (JSTOR-QUEUE.tsv) by title, snippet and what the runner read; no decoding, no class change unless stated.

3 rows (file lines 20-22), 1 candidate read by the runner (Pound 1936-41, stable/25080325), negative. Context only: Wilhelm 1999 (telegraph as strategic means), Halstead 1944 (Myer, Signal Service 1861-63). No candidate unread.

JSTOR family: searched on the owner's machine 24 Sept 2026, 3 rows, 1 candidate read, result clean. **Gate 2's JSTOR condition is met for E4 and E5.**

Open indexes: the owner ran this target's two queries on OpenAlex (API) and Semantic Scholar (site search) from their own machine on 24 Sept 2026 (ASKS row 34, `outreach/openalex-s2-owner-queries.md`): no relevant hit. V5's single cloud retry at about 17:21 UTC was 429 on both and is superseded. **Gate 2 is met for this target**: JSTOR family clean, open-index pass done, Google Books and the second adversarial audit done earlier (this file's earlier gate table left only the JSTOR rows and the open-index pass open). The outward draft carrying it is `status: ready` (for Thurloe P4, issue 2 of outreach/bourdeau-issues.md; for Eckert and Blathwayt, outreach/huntington-eckert-blathwayt.md).

Outward drafts written this session (status drafted, nothing sent): see `outreach/` and CONTRIBUTIONS.md.

## Open-index queries, cloud, 25 Sept 2026 (parent worker FOLLOWUP-2315)

ASKS.md row 41's open-index sub-item, re-run from the cloud with OPENALEX_KEY / S2_KEY (Access playbook; earlier
audits recorded OpenAlex and Semantic Scholar both 429 every time from the cloud, OPEN-INDEX-RESULTS.tsv rows 110-133).

| query | host | result |
|---|---|---|
| "Fox Butler 1864 camels Tecumseh" | OpenAlex (`works?search=`) | no relevant hit (1 result: a book's "Subject Index" entry, California, not a discussion of the letter) |
| "Meigs Butler 1864 cavalry depot" | OpenAlex (`works?search=`) | no relevant hit (16 results, general American Civil War scholarship -- Owen Johnston Hopkins diaries, Milroy/Winchester, Grant-Meade command relationship, Camp Chase/Libby Prisons, Battle of the Crater -- none naming Fox, Meigs or Butler's April 1864 correspondence) |
| "Fox Butler 1864 camels Tecumseh" | Semantic Scholar (`graph/v1/paper/search`) | no relevant hit (0 results) |
| "Meigs Butler 1864 cavalry depot" | Semantic Scholar (`graph/v1/paper/search`) | HTTP 429 on first call and on one retry after a 5s pause; good-citizen rule (single retry) -- not queried further this session |

Requests: api.openalex.org 2 (1.5s apart, key as `Authorization: Bearer`), api.semanticscholar.org 2 (key as
`x-api-key`, 1.2s and 5s apart), no credential printed. Three of four queries answered clean with no relevant hit;
the fourth (S2, Meigs/Butler) is unresolved from the cloud, left for a later session or the owner's machine.
JSTOR-QUEUE.tsv rows (file lines 20, 21, 22) stay with the ChatGPT/owner runner, per the brief.

## Gate 2 (JSTOR rows re-read, 26 Sept 2026, V-GATE2)

Verifier V-GATE2 (Opus, session_01DfYRf9UUmHn1yoNHVw6HeE, for parent 7i), 26 Sept 2026, 17:53-18:10 UTC (`date -u` read). Separate session from every solver and from the earlier auditors of this folder. Re-read every `JSTOR-QUEUE.tsv` row for this target after PR 21 landed the last 15 rows (16:34-17:00 UTC); every row is now `done`. Classification of each hit: (a) about this letter, (b) a prior decipherment or plaintext, (c) unrelated or context only. No decoding; no reading, key or status.json touched.

Rows read: 3 (file lines 20-22). Hits classified: row 20 no hit; row 21 back matter 1889, (c); row 22 Pound 1941 (read by the
runner, negative), Wilhelm 1999, Halstead 1944, a subject index, Appletons', an 1867 periodical: all (c). No (a), no (b).
Open-index pass: present (24 Sept owner's run; 25 Sept cloud re-run, 3 of 4 answered). Second adversarial audit: present.

**Verdict: gate 2 closed** for E4 and E5 (as V5 found; nothing new landed for this target in PR 21). Classes unchanged: **E4 N4,
E5 N4**. Reply: the Huntington note of 24 Sept 2026 (outreach/huntington-eckert-blathwayt.md) has no reply on file; nothing moves.

## Depth (DEPTH-REGRADE, 4 Oct 2026)

Verifier DEPTH-REGRADE (account 3, session_015eezFKYThEoRKoeamyhxSD), rule 4a / verifier step 3a; nothing decoded or changed. % = cipher tokens graded H/C/S (clear text excluded; counts as the cited reading file or audit gives them, nulls excluded where the file marks them); when evidence for a level is not on file the level below is given.
- **Huntington mssEC 19 p.49, E4 (Fox to Butler, 21 Apr 1864)**: **D4** (Decrypted; outward "deciphered"), 100.0% (code words E4 H 11, E5 H 20; plain words are clear, ungraded). Check: period cipher book mssEC 41 (H) for every code word; second ledger copy mssEC 25 pp.77/79; blind second reader (96% token agreement) and decode.py --check. Sentence: "Fox asks Butler to block the channel at Roanoke Island against the ram, and Meigs tells Butler that 4,000 men rather than three regiments are here for Fort Monroe, with 1,000 cavalry horses at the depot."

## AUDIT (propagation, AM-ECKV)

Verifier AM-ECKV (account 2, for LANE LANE-AM-0914), 7 Oct 2026, 10:54-11:00 UTC by `date -u`; a separate session from
AM-ECK64N2 and AM-ECK64K, the two solvers. Scope: the two Cipher No. 2 entries reading-no2.md gained after every earlier
section of this file was written (rule 10 propagation, flags of 10:21 and 10:39 UTC in ROOM.md). Nothing else decoded.

### 1. Re-derivation (rule 7)
- `python3 decode_no2.py --check` from a fresh clone of origin/main: "reading-no2.md is current", exit 0.
- Each code word of both entries checked by script against key-no2.md (word, value, grade, book page): N2-L Hunter,
  Ogden, Reliance, Lapland, Nutmeg x2, Crowd, Wharf, Altar, Wafer, Prospect, Wiley, Lady = **13 H**; N2-M Hannah,
  Hawkins, Farmer x2, Tulip, Talbot, Holly, Warner, Stanhope, Wiley, Burglar, Famish, Mastiff = **13 H** (10 in the
  message, 3 in the post-signature service line "use Farmer Famish Mastiff for Can"). No value differs from the solvers'.
- Image: mssEC 19 p.90 (pointer 8982) fetched once at 2400 px (scratch), crop step `tools/iiif_lines.py --image
  p8982.jpg --region 180,1140,2040,640 --centres 60,160,260,360,460,560 --lines-per-crop 2` (3 crops), read by this
  session: every word of the N2-M block in ciphertext-no2.txt agrees (Hannah, Hawkins, Farmer, tulip, talbot, Holly,
  "Sleeve port", warner, Stanhope, wiley, Burglar, Farmer Famish Mastiff, "for Can"). p.61 (N2-L) not re-fetched: its
  13 tokens are each fixed independently by O9-AE's reading and the OR print of the same order.
- Caveat carried forward: the key row for Burglar reads "Quarter[?] Master General" with the book's own [?]; the
  QMG value is corroborated in context (below), not by the book alone.

### 2. Search log (7 Oct 2026)
| family | searched | result |
|---|---|---|
| OR ser. I vol. 34 pt 4 (IA warofrebellion344unit, djvu full text, whitespace-normalised) | "find the gauge", "what is it", every "gauge", every "June 11, 1864" date line (44), the three Washington 11 June items read | not printed. Washington 11 June: Halleck to Canby 4 p.m. (officers), G.O. 210, Meigs to Allen (saw-mills for Canby). Meigs to Canby 17 June 1864 1.30 p.m. prints "I have telegraphed you twice to inform me of the gauge"; Canby to the QMG 24 June gives it |
| OR ser. III vol. 4 (IA warofrebellionco0004genf, djvu full text) | "find the gauge"; "gauge" near Vicksburg/Shreveport/Canby | no hit |
| OR ser. I vol. 34 pt 3 p.358 (via reading-no9.md, O9-AE) | N2-L's order | printed word for word (Halleck to Banks and Steele, 30 Apr 1864, 10.30 p.m.) |
| Google Books API (key, country=US) | "cannot find the gauge"; "can not find the gauge"; "find the gauge of the Vicksburg"; "gauge of the Vicksburg and Shreveport" Meigs Canby | no Civil War hit for the first three; the fourth returns only OR (1891), the 17-24 June Meigs/Canby exchange |
| Huntington CONTENTdm item info, pointer 8982 | every metadata field | volunteer transcription of the ledger text (code words in clear form, undecoded); keywords tel178 "Shreveport"; no decoded field, no gauge/QMG reading |
| Earlier families of this file (Zooniverse Talk, project blog, solver repositories, open indexes; 20-26 Sept) | not re-run for this entry | no decoded field anywhere on the project as of those passes |
| Meigs letter books (LoC), NARA RG 92/107, M504 | not reachable as text | unread (as for E5) |
Requests: hdl.huntington.org 2 (image, item info), archive.org 3 (two djvu texts, one advancedsearch), googleapis.com 4; all 200.

### 3. Classification
- **N2-L** (mssEC 19 p.61, Buckley "(No 2)", Halleck to Banks at New Orleans with a copy to Steele, 30 Apr 1864, 10 pm):
  **N1**, key `period` (key-no2.md from Cipher No. 2, mssEC 47), text `known`. Its plain is O9-AE's order, printed in OR
  I/34 pt 3 p.358; our reading is an independent re-decipherment of a second cipher copy. Safe sentence: "The Cipher No. 2
  copy of Halleck's 30 April 1864 order to Banks and Steele reads, with the period book, to the text printed in the
  Official Records." Unsafe: any wording that the order's content was unknown.
  Depth **D4**, 100% (13/13 code words H; plain words clear), check: OR print of the same order (non-statistical),
  O9-AE twin under key-no9.md, decode_no2.py --check re-derived here. Sentence: "Halleck orders that no troops be
  withdrawn from the operations against Shreveport and on the Red River, which are to continue under the senior officer
  in command until further orders."
- **N2-M** (mssEC 19 p.90, Kimber, Washington to Canby at Vicksburg, 11 June 1864, 1 PM, signed with the QMG code word):
  **N3**, key `period`. No prior plaintext or decipherment located after the search above; the OR prints the 17 June
  sequel that mentions two earlier gauge telegrams, not this one. Not N4: the Meigs letter books and NARA RG 92 copies,
  the principal places a QMG telegram would be filed, are unread. The clear words ("I can not find the gauge ... what is
  it") have been public on the volunteer transcription since 2018, as for E4/E5. Safe sentence: "Read at grade H with
  the period Cipher No. 2 book; no prior decipherment or printed text of this telegram located in OR I/34 pt 4, OR III/4,
  Google Books or the Huntington record (searched 7 Oct 2026)." Unsafe: "first", "unpublished", "never printed".
  Depth **D4**, 100% (13/13 H; "Sleeve port" = Shreveport is clear-word spelling, not a cipher token), check: OR I/34
  pt 4 pp.424-425 (Meigs to Canby 17 June, "telegraphed you twice ... the gauge") and Canby's 24 June reply to the QMG
  (non-statistical, fixes Burglar = QMG in context), image re-read and decode_no2.py --check here. Sentence: "On 11 June
  1864 the Quartermaster-General telegraphs Canby at Vicksburg that he cannot find the gauge of the Vicksburg and
  Shreveport Railroad and asks what it is."
- SECOND-OPINIONS-QUEUE.tsv: SO-ECKERT-E4E5 quotes no N2 counts, unchanged; new row **SO-ECKERT-N2M** for N2-M (N3),
  prompt second-opinions/PROMPT-chatgpt-n2m.md. No row for N2-L (N1).

### 4. Postmortem
No over-claim found: reading-no2.md and NOTES.md say "a search result only, no novelty claimed" for N2-M and tie N2-L to
O9-AE's print. The gap was propagation only (two entries had no AUDIT class); closed here.

## AUDIT (propagation, ECK64-NO2 verifier)

Verifier ECK64-NO2-V (account 1, for the account-3 orchestrator), 7 Oct 2026, from 11:55 UTC by `date -u`; a separate
session from the ECK64-NO2 solver and not protecting its conclusions. Scope: the eight Cipher No. 2 entries N2-N..U that
reading-no2.md gained in section "Eight further Beckwith/Caldwell entries, February-June 1864 (ECK64-NO2, 7 Oct 2026)".
Nothing decoded; the derived block and ciphertext-no2.txt are left as the solver committed them (one correction below is
logged for the solver to apply).

### 1. Re-derivation (rule 7)
- `python3 decode_no2.py --check`: "reading-no2.md is current", exit 0.
- Every code word of N2-N..U looked up by script in key-no2.md (word or its stem + inflection: Kindles, suppers, Nutmegs,
  Silvers, swindling, Nuptials, radicals): every value and grade agrees with the derived block. The one C token is
  "radicals" in N2-T (Radical = Officer, C, alignment fixed by N2-B against the OR). The eight I tokens are the clerk's forms
  of key-no2.md section 8: yard (N2-Q, N2-S, N2-T), stick (N2-S, N2-T, N2-U), Balm (N2-O), Slumberations (N2-T). Count:
  N 17 H; O 12 H + 1 I; P 10 H; Q 19 H + 1 I (as committed); R 9 H; S 23 H + 2 I; T 19 H + 1 C + 3 I; U 11 H + 1 I = H 120,
  C 1, I 8, M 0, as the solver states.
- The three new section-8 rows (Balm, stick, Slumberations) are graded I with their single-context evidence written out;
  honest. The Slumber = Operations witness against the inferred Religion = Operations on [25B] is stated, not resolved.
- Conflicts stated, not hidden: N2-Q date words April 22 vs header 23rd and Julia 4 PM vs 4.15; N2-T Mark = July vs header
  June 6th. Both are in reading-no2.md and NOTES.md.
- Caveat: N2-O's "Chart[?]" carries the solver's own [?] and is counted H; the OR print (I/32 pt 2 p.494, "Major-General
  Grant") fixes the addressee, so the count stands.

### 2. Correction to the reading (N2-Q "Ann Apple is")
The Papers of Ulysses S. Grant, vol. 10 (Jan. 1-May 31, 1864), p.343, prints this telegram from the National Archives copy
(RG 107): "On April 23, 1864, 4:00 P.M., Maj. Gen. Ambrose E. Burnside telegraphed to USG. 'Troops all started from
Annapolis Second Ohio Cavalry not yet mounted Is it intended that all the horses now here ... before the second is mounted It
has been waiting a long time and I have no cavalry except the third New Jersey'" (Google Books snippets, volume id
mD4fAQAAMAAJ, queries "Troops all started from Annapolis", "before the Second is mounted", "no cavalry except the Third New
Jersey"). So the ledger's "Ann Apple is" is the clear word Annapolis written in three pieces, not Ann + Apple (= Tennessee,
H) + "is". The committed reading "[Troops] all started from Ann [Tennessee] is" is wrong at that place: Apple is a plain
syllable here and should not be counted H, and "Ann" is not an unread token. Corrected counts used below: N2-Q H 18, I 1;
the eight H 119, C 1, I 8, M 0; the 21-entry total H 418, C 7, I 18, M 1. The derived block still shows the old value
until the solver marks the entry `plain: Ann Apple` in ciphertext-no2.txt and re-runs `decode_no2.py` (a one-line change;
next step for the target, not done here because a verifier does not decode). PUSG's 4:00 P.M. agrees with the date-group
time word Julia = 4 PM; its April 23 agrees with the header, against the date words' 22.

### 3. Search log (7 Oct 2026)
| family | searched | result |
|---|---|---|
| OR djvu full texts on IA, whitespace- and hyphen-normalised: I/32 pt 2, I/32 pt 3, I/33, I/34 pt 2, I/36 pt 3, I/40 pt 2 (solver's cache) and, fetched here, I/34 pt 1 (warofrebellion341unit), I/36 pt 1 (warofrebellion361unit), I/37 pt 1 (warofrebellion371unit), III/4 (warofrebellionco0004genf) | P: "transfer troops from", "Steele's command unless", "unless at your request"; Q: "Second Ohio Cavalry", "no cavalry except/but", "not yet mounted", "hurry up", "Third New Jersey"; R: "co-operation from Warrenton", "I will postpone", "cannot send the party", "Point of Rocks", every Augur/Meade item of 25-27 Apr 1864 in I/33; T: "French officers", "two French", "to observe the military", "keep them away", "let them go to the front", "does not want them"; and the N, O, S, U texts | N2-N printed I/32 pt 2 p.407 (head "407" above the item), N2-O p.494 (the next head, "495", follows the item), N2-S I/36 pt 3 p.207 (between heads 207 and 208), N2-U I/40 pt 2 p.47 (between 47 and 48): all four confirmed, word for word as the solver says. P, Q, R, T: not in any of the ten volumes. I/33 p.722 has Halleck to Grant of 24 Mar on Burnside's request for the dismounted Second Ohio (context only). I/36 pt 1 p.91 (page from the next running head, 92) prints Dana to Stanton, Cold Harbor, 7 June 1864, 9 a.m.: "With regard to the French officers, General Grant says he does not want them. He will send formal declaration if you wish" -- the answer to N2-T, not N2-T itself |
| Google Books API (key, country=US), 25 queries | P: "not transfer troops from Steele's command", "This Department will not transfer troops", "Steeles Command unless at your request"; Q: "no cavalry except the Third New Jersey", "before the Second is mounted", "Troops all started from Annapolis", Burnside + "April 23, 1864"; R: "some co-operation from Warrenton", "cannot send the party as I wish", Augur + Meade + "Point of Rocks" + "April 26, 1864", "I will postpone" + names; T: "two French officers" + Stanton/Dana 1864, "French officers" + "Grant's headquarters", "anxious to go to General Grant's headquarters", "holding them back for a week", "go to the front or keep them away", "French officers" + "Papers of Ulysses S. Grant" | **P printed**: PUSG vol. 10, "This Department will not transfer troops from General Steeles Command unless at your request." ALS (telegram sent), DNA, RG 107, Telegrams Collected (Bound) (page not shown in the snippet). **Q printed**: PUSG vol. 10 p.343 (above). R: no hit. T: no print of the query; only Dana's 7 June reply (OR I/36 pt 1) |
| IA full-text search (be-api fts), PUSG volumes | vol. 10 "Steeles Command" (positive control: 1 hit), vol. 10 "Point of Rocks" (0), vol. 11 "French officers" quoted and unquoted (0; vol. 11 indexed, "Dana" 1 hit) | P control works; R and T not in PUSG vols. 10-11 by fts |
| Huntington CONTENTdm item info, pointers 8915, 8944, 8948, 8979 (solver's cached fetch of 7 Oct, read here) | every metadata field | volunteer transcription (code words undecoded), notes on pencilled words, keywords (tel044 Chickahominy, tel100 Annapolis); no decoded field |
| Earlier families of this file (Zooniverse Talk, project blog, solver repositories, open indexes; 20-26 Sept) | not re-run for these entries | no decoded field anywhere on the project as of those passes |
| Augur's and Meade's letters sent (NARA RG 393), Meade papers (HSP), Stanton papers (LoC), NARA RG 107 telegrams (M473/M504) | not reachable as text | unread |
Requests: archive.org 6 (4 djvu texts, 1 advancedsearch, 1 metadata), be-api.us.archive.org 6 (fts), googleapis.com 25, hdl.huntington.org 0 (solver's cache read); all 200.

### 4. Classification (key `period` for all eight: key-no2.md from Cipher No. 2, mssEC 47)
- **N2-N** (p.10, Halleck to Grant, 16 Feb 1864, 3.30 PM): **N1**, text `known` (OR I/32 pt 2 p.407). Depth **D4**, 100%
  (17/17 H), check: OR print, re-derivation here. Safe: "The Cipher No. 2 ledger copy reads, with the period book, to the
  text printed in OR I/32 pt 2 p.407." Unsafe: anything implying the content was unknown. Sentence: "Halleck tells Grant
  that the Secretary of War wants Ellet's Marine Brigade assigned to protect the leased plantations on the Mississippi."
- **N2-O** (p.14, Halleck to Grant, 29 Feb 1864, 3.30 PM): **N1**, `known` (OR I/32 pt 2 p.494). Depth **D3**, 92% (12 H,
  1 I: Balm), check: OR print. Not D4 while Balm is I. Safe/unsafe as N2-N. Sentence: "Halleck asks Grant for any
  further information of Longstreet's retreat."
- **N2-P** (p.23, the Secretary of War to Grant, 18 Mar 1864, 3.30 PM): **N1**, `known` (PUSG vol. 10, from the RG 107
  telegram sent). The solver's "not located" was true of the OR volumes searched; the text is printed in the Grant
  Papers. Depth **D4**, 100% (10/10 H), check: PUSG print. Safe: "Reads, with the period book, to the text printed in The
  Papers of Ulysses S. Grant, vol. 10." Unsafe: "not printed". Sentence: "Stanton tells Grant the War Department will not
  transfer troops from Steele's command unless Grant asks."
- **N2-Q** (p.52, Burnside to Grant, 23 Apr 1864): **N1**, `known` (PUSG vol. 10 p.343). Depth **D3**, 95% (18 H, 1 I:
  yard; Apple removed as plain, section 2), check: PUSG print. Safe: "Reads to the text printed in PUSG vol. 10 p.343,
  except that the ledger's 'Ann Apple is' is Annapolis." Unsafe: "started from Tennessee"; "not printed". Sentence:
  "Burnside tells Grant his troops have all left Annapolis, the Second Ohio Cavalry is not yet mounted, and he has no
  cavalry but the Third New Jersey."
- **N2-R** (p.56, Augur to Meade, 26 Apr 1864, 11.30 AM): **N3**. No prior plaintext or decipherment located after the
  search above. Not N4: Augur's and Meade's letters-sent books and the NARA telegram series, where such a telegram would
  be copied, are unread. Depth **D3**, 100% (9/9 H) with the period key book as the external source of every value and the
  date words confirming the header's 26th; not D4, because no print or sequel checks the content. Safe: "Read at grade H
  with the period Cipher No. 2 book; no prior decipherment or printed text located in OR I/33 or I/37 pt 1, Google Books,
  PUSG vol. 10 or the Huntington record (searched 7 Oct 2026)." Unsafe: "first", "unpublished", "never printed".
  Sentence: "Augur tells Meade he cannot send the party without co-operation from Warrenton and from Point of Rocks, and
  will postpone it if Meade cannot give the force now."
- **N2-S** (p.79, Halleck to Grant, 26 May 1864, 10.30 AM): **N1**, `known` (OR I/36 pt 3 p.207). Depth **D3**, 92% (23 H,
  2 I), check: OR print. Sentence: "Halleck tells Grant his instructions went to Butler and Hunter and that 4,000 or 5,000
  re-enforcements will go to Port Royal, though water transportation is short."
- **N2-T** (p.87, the Secretary of War to Dana, 6 June 1864, 10 AM): **N3**. The query itself was not located; Dana's
  answer of 7 June (OR I/36 pt 1 p.91) is printed and shows the subject was in the record, so a summary of the exchange is
  known while this text is not. Not N4: Stanton papers and RG 107 telegrams sent unread. Dana's 7 June answer also supports
  the ledger header (June 6) against the date word Mark = July. Depth **D3**, 87% (19 H, 1 C, 3 I), check: Dana's printed
  reply. Safe: "Read at grade H/C with the period Cipher No. 2 book; the query is not located in OR I/36 pts 1 and 3, III/4,
  Google Books or PUSG vol. 11; Dana's printed reply of 7 June answers it (searched 7 Oct 2026)." Unsafe: "first",
  "unknown episode". Sentence: "Stanton asks Dana to learn from Grant whether two French officers, a colonel and a captain
  sent to observe the operations, may go to the front."
- **N2-U** (p.93, Lincoln to Grant, 15 June 1864, 7 AM): **N1**, `known` (OR I/40 pt 2 p.47; also a widely quoted Lincoln
  text). Depth **D3**, 92% (11 H, 1 I), check: OR print. Sentence: "Lincoln tells Grant: I begin to see it. You will
  succeed. God bless you all."

### 5. Postmortem and corrections
- Failure: the solver searched only OR volumes, not the sender-/recipient-specific edition (The Papers of Ulysses S.
  Grant), the same gap as the Eckert 1864 precedent at the top of this file; two of the four "not located" entries are
  printed there. Corrected: reading-no2.md ECK64-NO2 table and token notes (P and Q now "printed in PUSG vol. 10"; the
  "Ann" note replaced by the Annapolis correction) and NOTES.md ECK64-NO2 (a correction paragraph). The solver's wording
  was search-result only, so no novelty over-claim; the over-claim was the N2-Q token Apple = Tennessee (H).
- Next step for the solver: `plain: Ann Apple` on N2-Q in ciphertext-no2.txt, re-run decode_no2.py, update the counts.
- SECOND-OPINIONS-QUEUE.tsv: SO-ECKERT-N2R and SO-ECKERT-N2T added (N3). No rows for the N1 items.

## AUDIT 2 (second adversarial, D12-V2T)

Verifier D12-V2T (account 2, for LANE DEFAULT-account-2-20261007-1210), 7 Oct 2026, 12:18-12:3x UTC by `date -u`; a
separate session from the ECK64-NO2 solver and from its verifier (ECK64-NO2-V), not protecting either. Scope: **N2-T only**
(mssEC 19 p.87, pointer 8979, the Secretary of War to Dana, Washington, 6 June 1864, 10 AM, two French officers).
CLAUDE.md Outreach gate 2: try to find it in print by every family the first audit did not cover. Nothing decoded.

### 1. Re-derivation (rule 7) and image check
- `python3 ciphers/eckert-1864/decode_no2.py --check`: "reading-no2.md is current", exit 0.
- Image: one IIIF fetch, `hdl.huntington.org/digital/iiif/p16003coll11/8979/full/2400,/0/default.jpg` (scratch, regenerable);
  crop step run before reading: `python3 tools/iiif_lines.py --image $S/img/p8979.jpg --out $S/crops --prefix t --region
  120,1240,2120,900 --centres 50,150,250,350,450,550,650,750,850 --lines-per-crop 3 --max-width 2400` (3 crops, read by this
  worker). Every word of ciphertext-no2.txt N2-T agrees with the strip crops, header "S. H. Beckwith Wash'n June 6th 1864
  10 am" included; the Huntington volunteer text of pointer 8979 agrees too.
- Every code word looked up by script in key-no2.md: Hunter = Washington, Mark = July, Dawson = 6, Emily = 10 AM, Saturn =
  Dana C A, Arnold = 2, Pike = comma, Allen = 1, Pearl = Colonel, Interest = Captain, Madrid = Grant U S, Snake = Head
  Quarters, Magic = Grant U S, Sexton = Front, Beach = Secretary of War (all H); radicals = Officer (C); yard, stick,
  Slumberations (I, section 8). Counts as committed: H 19, C 1, I 3, M 0.

### 2. Gaps in the first audit's log for N2-T, and what was searched here
First audit covered: OR I/36 pts 1 and 3, III/4 by phrase; Google Books (6 T queries); PUSG vol. 11 by be-api fts
"French officers"; Huntington item info for 8979. Not covered: Dana's own book; OR by date/correspondent index; OR beyond
June (a sequel); the Huntington's full text across the whole collection; Zooniverse Talk for this entry; the War Department
telegraph-office books; open indexes; JSTOR.

| family | searched | result |
|---|---|---|
| OR I/36 pt 3 (warofrebellion363unit djvu), index by correspondent | "Dana, Charles A. Correspondence with Edwin M. Stanton" | one page only, 722 (Stanton's telegram on the "lying report" about Meade), not N2-T. No other Stanton-to-Dana item in the volume |
| OR I/36 pt 1 (warofrebellion361unit djvu), index + phrase | "Dana, Charles A" (63-96: Dana's dispatches to Stanton, his side only); "French" (0 relevant); "not want them" | p.91, Dana's 7 June reply, OCR garbled ("fend fnr™i d"), so a phrase search of this copy alone cannot exclude; the index shows the volume prints Dana's side only |
| OR I/40 pt 1 (warofrebellion401unit djvu), sequel window | "French officers", "glad to have them" | **sequel printed**: Dana to Stanton, City Point, Va., 18 June 1864, 8 a.m., pp.24-25 (between running heads 24 and 26): "With regard to the two French officers who wish to come here, General Grant now desires me to say that he will be glad to have them, but wishes them to understand that the campaign is carried on under the greatest inconveniences as respect personal comfort." A second answer, not the query |
| Dana, *Recollections of the Civil War* (1898; recollectcivilwa00danarich djvu) | "French" | one hit, the French Broad river (Knoxville 1863); nothing on French officers |
| PUSG vol. 11 (papersofulyssess0011gran, be-api fts) | "French" (4 hits: Loring/French, Fred's lessons, index "French, Samuel G."), "France" (Kearsarge), "observers", "foreign officers", "keep them away", "French colonel", "Dana" (July letters only) | not in PUSG 11 |
| Bates, *Lincoln in the Telegraph Office* (1907, telegraphoffice00baterich); Plum, *The Military Telegraph during the Civil War* (1882, militarytelegra03plumgoog, militarytelegra04plumgoog), djvu text | "French officer" | 0 |
| Huntington CONTENTdm, whole mssEC collection (p16003coll11), `CISOSEARCHALL` page level over the volunteer transcriptions | "French" (129 pages), "Slumberations", "producing them back", "radicals" (16 pages) | N2-T's text occurs on one page only, pointer 8979 itself (code words undecoded). Dana's 7 June reply is on 10396 (mssEC "Received" vol. 10550, p.254) and the 18 June sequel on 10429 (p.287), both in clear. The "Dana" book (4147) has no copy. No decoded copy of N2-T anywhere in the collection |
| Zooniverse Talk, Decoding the Civil War (project 2125, `/searches`) | "French officers" (4 hits, none this page), "Saturn" (0), "Slumberations" (0) | nothing on this entry |
| Google Books API (key, country=US), 6 queries | "French officers" Stanton Dana "June 6, 1864"; "sent here to observe the military operations"; "I have been holding them back for a week"; "whether I shall let them go to the front"; "two French officers" Grant 1864 Dana; "French officers" "Grant's headquarters" 1864 Stanton | only OR (I/36 pt 1 Dana's 7 June reply; I/40 pt 1 Dana's 18 June sequel) and its House-documents reprint; no print of the query |
| loc.gov JSON search | "French officers" Stanton Dana 1864 | 2,103 results, newspapers only; the Stanton papers are not full-text searchable here |
| OpenAlex (key), Semantic Scholar (key), CORE (key) | French officers / military observers + Grant 1864 / Stanton Dana | nothing on the episode (OpenAlex 96, S2 321, CORE 0; top results off-topic) |
| CrossRef | French officers observers Army of the Potomac 1864 | empty response body, unreachable this pass (not retried) |
| JSTOR-QUEUE.tsv | 4 rows appended 7 Oct 2026: family (i) "French officers" AND (Stanton OR Dana) AND Grant AND 1864; family (ii) "to observe the military operations" AND French AND 1864, "whether I shall let them go to the front", "he will be glad to have them" AND French | queued; never block the class |
| Stanton papers (LoC), NARA RG 107 telegrams sent (M473), Dana's papers | not reachable as text | unread: manuscripts, not editions |

Requests: archive.org 9 (djvu 7, advancedsearch 3, counted with be-api separately), be-api.us.archive.org 11 (the last
three answered non-JSON; host stopped, not retried), hdl.huntington.org 6 (1 IIIF image, 5 dmQuery, one empty reply on a
`%20` query, rerun as single-word queries), googleapis.com 6, talk.zooniverse.org 3, loc.gov 1, api.openalex.org 1,
api.semanticscholar.org 1, api.core.ac.uk 1, api.crossref.org 1.

### 3. Classification
**N2-T: N4** (raised from N3). The principal editions for a Stanton-Dana telegram of June 1864 (OR ser. I vols. 36 pts 1
and 3 and 40 pt 1 by phrase and by correspondent index, ser. III vol. 4; PUSG vols. 10-11; Dana's *Recollections*; Bates;
Plum), the holding catalogue's full text across the whole collection, and the transcription project's Talk pages are now
covered, and no prior plaintext or decipherment of the query was located. What is printed is the other side of the exchange:
Dana's replies of 7 June (OR I/36 pt 1 p.91) and 18 June (OR I/40 pt 1 pp.24-25). Internal or unpublished work (the
Stanton papers at LoC, NARA RG 107 telegrams sent) is not excluded, as N4 allows. Key: `period` (key-no2.md from Cipher No.
2, mssEC 47). Text: not `known` (the query); the episode is known from Dana's printed replies.
Depth **D3**, 87% (19 H + 1 C of 23 code words; 3 I: yard, stick, Slumberations; no name codes unread). Not D4 while three
tokens are I. Check: Dana's two printed replies, the second of which shows the request went on.
Sentence: "Stanton asks Dana to learn from Grant whether two French officers, a colonel and a captain sent to observe the
operations and held back a week, may go to Grant's headquarters at the front; Grant first declined (7 June), then agreed
(18 June)."
Safe: "Read at grade H/C with the period Cipher No. 2 book; no prior decipherment located (OR, The Papers of Ulysses S.
Grant, Dana's Recollections, Bates, Plum, the Huntington's full text and the Zooniverse project, searched 7 Oct 2026);
Dana's two replies are printed in OR I/36 pt 1 p.91 and I/40 pt 1 pp.24-25." Unsafe: "first", "unpublished", "never
printed", "an unknown episode" (the episode is in the OR through Dana's replies), "new".

### 4. Postmortem
No over-claim found in reading-no2.md, NOTES.md or the first AUDIT for N2-T. The first audit's gap was family breadth (no
date/correspondent sweep, no sequel window, no whole-collection Huntington search); the sweep found a second printed answer
(18 June) and no copy of the query. Corrections: status.json N2-T row (grade N4, `audit_status` 'two audits', the sequel
in `depth_check`). SECOND-OPINIONS-QUEUE.tsv SO-ECKERT-N2T and its prompt quote no class or count, unchanged. PROGRESS.tsv
has no N2-T row.
## AUDIT 2 (second adversarial, D12-V2M)

Verifier D12-V2M (account 2, for LANE DEFAULT-account-2-20261007-1210), 7 Oct 2026, 12:18-12:29 UTC by `date -u`. Scope: N2-M
only (mssEC 19 p.90, Kimber, Washington to Canby at Vicksburg, 11 June 1864, 1 PM). A separate session from the solver
(AM-ECK64K) and the first auditor (AM-ECKV). Outreach gate 2: try to find the item in print by every family the first audit
did not cover. Nothing decoded.

### 1. Gaps in the first audit's log (read before searching)
AM-ECKV searched OR I/34 pt 4 by phrase and by every 11 June date line, OR III/4 by phrase, Google Books (4 queries) and the
Huntington item record for p.90. Not covered: The Papers of Ulysses S. Grant vol. 11; the Meigs letter books (named as the N4
blocker); Canby's papers; the OR by correspondent over 8-14 June; the Huntington's full text across the whole collection (a second
copy of the same telegram in another ledger); IA full text across all items; Zooniverse Talk for this subject; the open indexes
(OpenAlex, Semantic Scholar, CORE, CrossRef); JSTOR rows.

### 2. Re-derivation and image (rule 7)
- `python3 decode_no2.py --check`: "reading-no2.md is current", exit 0.
- Key rows re-read in key-no2.md for all 12 code-word types (Hannah, Hawkins, Farmer, Tulip, Talbot, Holly, Warner, Stanhope,
  Wiley, Burglar, Famish, Mastiff): every value as in reading-no2.md.
- Image: p.90 (pointer 8982) fetched once at 2400 px to scratch; crop step `python3 tools/iiif_lines.py --image p8982.jpg --out
  crops --prefix V2M --region 180,1140,2040,640 --centres 60,160,260,360,460,560 --lines-per-crop 2` (3 crops), read by this
  session: "Kimber Vicksburg / Washn June 11 1864 / Hannah June Hawkins to Farmer tulip / I can not find the gauge / talbot Holly
  & Sleeve port warner / what is it Stanhope wiley Burglar / use Farmer Famish Mastiff for Can". Agrees word for word with
  ciphertext-no2.txt.
- New corroboration of the one caveat (Burglar's key row carries the book's own "[?]"): the Huntington full-text search (below)
  found the cipher copy of Meigs's 17 June 1864 1.30 p.m. telegram on mssEC 19 p.94 (pointer 8986, Kimber, volunteer text): it is
  addressed "For Mastiff" (one of the three Canby words N2-M's service line names) and signed "Windham Meigs Buggy" (the line then runs on into an operator's note, "We have Gondola hurrah ..."). Windham =
  Signed and Buggy = Quarter[?] Master General (key-no2.md, Buggy is the right-hand word of the same book row p.12 l.21 as
  Burglar); OR I/34 pt 4 p.425 prints that telegram's signature "M. C. MEIGS, Quartermaster-General". So the row's value is fixed
  by a print through its twin word, not only by context. Read from the volunteer text of p.94, not image-checked; corroboration,
  no grade changed (all 13 tokens were already H).

### 3. Search log (7 Oct 2026)
| family | searched | result |
|---|---|---|
| OR ser. I vol. 34 pt 4 (IA warofrebellion344unit djvu, whitespace-normalised) by date and correspondent | every date line 8-14 June 1864 (356 June-date lines scanned) within 200/300 chars of Meigs/Quartermaster-General and Canby/Vicksburg/Shreveport/railroad; every "gauge" | the window prints Meigs to Allen 11 June (p.305, saw-mills for Canby) and Hardie to Canby, Washington 13 June 8 p.m. (p.331-332: Canby's 4 June telegram to Meigs on the Vicksburg-Monroe railroad referred to Grant); Canby to the QMG, 4 June, printed. No 11 June QMG-to-Canby gauge telegram. The gauge sequence printed: Meigs 17 June (pp.424-425, "telegraphed you twice"), Canby 24 June (two, New Orleans and Vicksburg), Meigs's reply |
| OR ser. III vol. 4 (IA warofrebellionco0004genf) by date | the 25 date lines 8-14 June 1864 against Meigs/QMG + Canby/railroad | no hit |
| IA full text, all items (be-api fts) | "find the gauge of the Vicksburg" (0); "can not find the gauge" (0); "cannot find the gauge" (1, a 20th-c. wind-turbine book); "gauge of the Vicksburg and Shreveport" (8: all OR I/34 pt 4 copies, the 17 June print) | not printed in any IA-indexed item |
| The Papers of Ulysses S. Grant vol. 11 (June-Aug 1864; IA papersofulyssess0011gran, fts) | gauge (0); "Vicksburg and Shreveport" gauge (0); Shreveport (5 hits); "Vicksburg and Shreveport Railroad"; Canby railroad Meigs | index "Vicksburg and Shreveport Railroad, 436-37": Calendar, 27 June 1864, USG endorsement on Canby's correspondence about rebuilding the road ("I do not think it advisable to build the Shreveport and Vicksburg railroad ..."). Grant is not a party to N2-M and the volume does not print it; Shreveport hits are a positive control that the volume is indexed |
| Huntington CONTENTdm, whole collection p16003coll11 (CISOSEARCHALL, page level) | gauge (25 pages); Shreveport (13 objects) | 1864 gauge pages read from the item text: mssEC 19 p.90 (N2-M itself), p.94 (the 17 June Meigs telegram, cipher copy, above), mssEC 18 p.317/321 (Beckwith, March-April 1865, unrelated), object 10550 p.327 (Canby to Halleck, New Orleans 23 June, on Halleck's telegram of the 11th, i.e. the printed 4 p.m. one, not N2-M), object 4849 p.305 (Canby's 24 June reply to Meigs, received copy). No second copy of N2-M in any ledger the volunteers transcribed |
| Library of Congress, Montgomery C. Meigs Papers (digitised 2024; loc.gov collection API) | "gauge Shreveport" (0), "Canby 1864" (0), the Letterbooks series listed | the digitised personal letterbooks have no volume for June 1864 (folders 1861 Apr-1862 Feb, then "1864, Apr.", then 1857-1889 others); the first audit's "Meigs letter books" blocker is closed for the LoC series: there is no June 1864 letterbook in it. Not opened page by page |
| Canby papers | not located as a digitised or edited series in this pass | not searched beyond the OR, which prints his side of the exchange |
| NARA RG 92 (QMG telegrams sent) and RG 107 (Telegrams Collected) | no NARA API key (CLAUDE.md host table) | unreachable; archival copies, unpublished |
| Google Books API (key, country=US) | "gauge of the Vicksburg & Shreveport" (0); "find the gauge" Canby (243, none of them this telegram: OR 1891 Canby 23-24 June, unrelated books); "Vicksburg and Shreveport" gauge Meigs "telegraphed you twice" (0); "Vicksburg and Shreveport" railroad Meigs Canby 1864 gauge (4: OR and the 1892 House-documents reprint, the 24 June items) | not printed |
| Zooniverse Talk (talk.zooniverse.org, project 2125) | gauge (5 comments), Shreveport (4), Burglar (0) | none on mssEC_19_090; the gauge comments are on mssEC_16_302, mssEC_24_082 and a Sept 1863 Louisville item; no decoding of N2-M on the project |
| Open indexes | OpenAlex `"Vicksburg and Shreveport" railroad` (6, none on the 1864 gauge), OpenAlex "Meigs Canby 1864 railroad gauge telegram" (0); Semantic Scholar (429, one retry after 5 s, 200: 0); CORE `"Vicksburg and Shreveport" AND gauge` (0); CrossRef bibliographic query (top 8 unrelated) | no scholarship quoting the 11 June telegram |
| JSTOR | two rows appended to JSTOR-QUEUE.tsv, families (i) and (ii) | queued; never blocks |
Requests: hdl.huntington.org 8 (1 image, 2 searches, 5 item info), archive.org/be-api 14, googleapis.com 4, api.openalex.org 2,
api.semanticscholar.org 2 (one 429), api.core.ac.uk 1, api.crossref.org 1, loc.gov 6 (one 403 on /search/ with a browser UA,
then 200 with the descriptive UA), talk.zooniverse.org 4, www.zooniverse.org 2.

### 4. Classification
- **N2-M: N4**, key `period` (key-no2.md from Cipher No. 2, mssEC 47), text not known in print. Raised from N3: the principal
  editions (OR ser. I vol. 34 pt 4 by phrase, date and correspondent; OR ser. III vol. 4; PUSG vol. 11), the catalogues (the
  Huntington's own full text across every mssEC ledger; the LoC Meigs Papers, which have no June 1864 letterbook) and the project
  pages (Zooniverse Talk) are covered, with IA full text, Google Books and four open indexes. Internal or unpublished work is not
  excluded: the NARA RG 92/107 copies are unread (no API key), and the JSTOR rows are queued. The clear words ("I can not find the
  gauge ... what is it") have been public on the volunteer transcription since 2018, as for E4/E5; what the period book adds is
  the addressee (Canby), the place (Vicksburg), "Rail-road" and the signature (the Quartermaster-General).
- Safe sentence: "Read at grade H with the period Cipher No. 2 book; no prior decipherment located (OR ser. I vol. 34 pt 4 by
  phrase, date and correspondent, OR ser. III vol. 4, Papers of U. S. Grant vol. 11, the Huntington's full ledger text, the LoC
  Meigs Papers, Zooniverse Talk, IA and Google Books full text and four open indexes, searched 7 Oct 2026); its 17 June sequel and
  Canby's 24 June reply are printed in OR I/34 pt 4." Unsafe: "first", "new", "unpublished", "never printed", or any wording that
  the telegram's text was unknown (its clear words were public).
- Depth **D4**, 100% (13/13 code words H, 10 in the message, 3 in the service line), unchanged; checks: OR I/34 pt 4 pp.424-425
  (the 17 June sequel) and the p.94 twin-row signature against the same print (non-statistical), image re-read and
  `decode_no2.py --check` re-derived here. Sentence unchanged: "On 11 June 1864 the Quartermaster-General telegraphs Canby at
  Vicksburg that he cannot find the gauge of the Vicksburg and Shreveport Railroad and asks what it is."
- SECOND-OPINIONS-QUEUE.tsv: SO-ECKERT-N2M and its prompt quote no class or count; unchanged.

### 5. Postmortem
No over-claim found in reading-no2.md, NOTES.md or status.json. The first audit's N4 blocker ("Meigs letter books unread") rested
on a series that has no June 1864 volume in its digitised form; the real remaining unread copies are NARA's, which rule 10's N4
does not require.
## AUDIT 2 (second adversarial, D12-V2R)

Verifier D12-V2R (account 2, for LANE DEFAULT-account-2-20261007-1210), 7 Oct 2026, 12:18-12:30 UTC by `date -u`. A separate
session from the ECK64-NO2 solver and from the ECK64-NO2 verifier (first audit, "AUDIT (propagation, ECK64-NO2 verifier)" above).
Scope: **N2-R only** (mssEC 19 p.56, pointer 8948, Augur to Meade, 26 Apr 1864, 11.30 AM; CLAUDE.md Outreach gate 2). Nothing decoded.

### 1. Re-derivation and image (rule 7)
- `python3 decode_no2.py --check`: "reading-no2.md is current", exit 0.
- Code words looked up in key-no2.md by hand: Florence = 11.30 AM (TIME page), Oliver = 20 and Clarke = 6 (fly leaf; = 26th),
  Mohawk = Meade G G, Harlot = Warrenton, tulip = Period, Trinity = Point, Salem = Force, Lantern = Augur C C: 9 H, as committed.
- Image: IIIF `hdl.huntington.org/digital/iiif/p16003coll11/8948/full/2400,/0/default.jpg` (scratch, regenerable), crop step
  `python3 tools/iiif_lines.py --image $S/img/p8948.jpg --out $S/crops --prefix p8948 --region 120,1590,2120,700 --lines-per-crop 2
  --max-width 2400` (6 lines found, 3 crops). Every word of ciphertext-no2.txt N2-R agrees with the strip crops; the header day is
  overwritten ("2[6?]" as transcribed) and the date words fix 26. The pencilled interlinear guesses (doing, did, get, man, change,
  may, partake, 90) are a later hand, as reading-no2.md says. No correction.

### 2. Gaps in the first audit's log for N2-R, and what was searched here
First audit covered: OR I/33 phrases and Augur/Meade items 25-27 Apr; I/37 pt 1 and the others of its table; Google Books (4 R
queries); PUSG vol. 10 fts "Point of Rocks"; the Huntington item record. Not covered for N2-R: date window +/-3 days by
correspondent; OR I/51 pt 1 (Union supplementary correspondence); Meade's own printed papers; the Huntington full text across the
whole collection; all-of-IA full text; Zooniverse Talk for this page; the open indexes; JSTOR rows.

| family | searched (7 Oct 2026) | result |
|---|---|---|
| OR I/33 (warofrebellion33unit djvu, hyphen/space-normalised) | every item dated 23-29 Apr 1864 naming Augur with Meade/Humphreys; phrases "co-operation from Warrenton", "send the party", "without some co", "postpone", "Point of Rocks" | N2-R not printed. Context only: Sheridan (HQ Army of the Potomac) to Augur, 26 Apr, rec. 9.10 p.m., on the Eighth Illinois Cavalry; Tyler (Fairfax C.H.) to Taylor and to Augur, 26 Apr: "The party from Washington should start from here. I learn that the cavalry which were at Warrenton have gone to Culpeper", Lowell to command the cavalry; Tyler to Augur 27 Apr, "The cavalry will start at daylight". These show the "party" was a Department of Washington expedition of 27-28 Apr, which supports the reading's sense; they do not print N2-R |
| OR I/51 pt 1 (warofrebellion511unit) | same phrases; items 23-29 Apr 1864 naming Augur or Meade | none |
| IA full text, all items (be-api fts, no identifier) | "co-operation from Warrenton", "cooperation from Warrenton", "some co-operation from Warrenton", "cannot send the party as I wish", "some also from Point of Rocks", "give the force now"; positive control "very anxious to get the Eighth Illinois Cavalry" | 0, 0, 0, 0, 0, and 1 unrelated (The Telegrapher 1864, "will give the force now in each" office); control 5 hits (OR I/33 copies), so the route works |
| Meade, Life and Letters vol. 2 (1913, IA lifelettersofgeo02mead djvu) | "Augur", "Point of Rocks", "Warrenton", letters of 24-26 Apr 1864 | not printed; letters to his wife of 24 and 26 Apr are about visitors; 1 May: "Augur happened to be in my tent" (context) |
| PUSG vols. 10-11 | first audit's fts (vol. 10 "Point of Rocks" 0); Augur-to-Meade is outside PUSG's scope except in notes | not re-run |
| Huntington CONTENTdm, whole mssEC collection (p16003coll11), CISOSEARCHALL with full-text flag | "Point of Rocks" (53), "co operation from Warrenton" (0), "cannot send the party" (10 incl. 8948), "post pone" (4 incl. 8948), "Augur Meade" (4); item info read for 64 hits and grepped for Warrenton/Harlot + Rocks/Trinity/Mohawk/Lantern/the phrases | only 8948 itself carries the telegram; no second ledger copy, no decoded field (2772 = June 1863, 8104 = Sept 1862, unrelated) |
| Zooniverse Talk (project 2125), subject 2880214 = mssEC_19_056 (tel094-096) | comments and discussions on the subject; project search "Point of Rocks", "Harlot", "Lantern", "Augur", "mssEC_19_056", "postpone" | subject: 0 comments, 0 discussions; search hits all on other subjects |
| Google Books API (key, country=US), 9 queries | "co-operation from Warrenton"; "cooperation from Warrenton" Augur; "Point of Rocks" Augur Meade "April 26"; "I will postpone" Augur Meade 1864; Augur Meade "Point of Rocks" Warrenton expedition Lowell Mosby; Meade "Life and Letters" Augur; positive control "Eighth Illinois Cavalry" Giesborough Augur; two intitle:"Supplement to the Official Records" queries | no N2-R; control found OR I/33 (Sheridan to Augur 26 Apr); Supplement to the OR (Hewett) returns 0 even for intitle + Augur, so it is not indexed there: unreachable |
| Open indexes: OpenAlex, Semantic Scholar, CORE, CrossRef (keys) | "Eckert cipher telegrams Huntington"; "Augur Mosby expedition April 1864 Point of Rocks"; "Union military telegraph cipher ledger decipherment" | nothing on this telegram; OpenAlex's "Gray ghostbusters" (OSU dissertation 1988, OhioLINK ETD PDF read by pdftotext, "Point of Rocks" contexts) does not print it |
| JSTOR | two rows queued in JSTOR-QUEUE.tsv: (i) Augur AND Meade AND "Point of Rocks" AND 1864 AND telegram/cipher/dispatch; (ii) "co-operation from Warrenton" bare | pending (never blocks) |
| Unreachable / unread | Supplement to the OR (not on IA or Google Books full text); NARA RG 393 Dept. of Washington telegrams sent, RG 107 M473/M504; Augur papers | unread |

Requests: archive.org 5 (2 advancedsearch, 3 djvu texts: I/33, I/51 pt 1, Meade vol. 2), be-api.us.archive.org 7,
hdl.huntington.org 72 (1 image, 6 searches, 65 item-info, one empty reply not retried), googleapis.com 11, api.openalex.org 4,
api.semanticscholar.org 3, api.core.ac.uk 3, api.crossref.org 3, rave/etd.ohiolink.edu 2, talk.zooniverse.org 8,
www.zooniverse.org 1; no 429/403/challenge.

### 3. Classification
- **N2-R: N3 kept.** No prior plaintext or decipherment located after the search above (both audits). Not raised to N4: the
  Supplement to the Official Records, a principal edition for the war, could not be searched (not in any full-text index
  reachable from the cloud), and the JSTOR rows are pending; everything else in the principal families (OR incl. the I/51
  supplement, PUSG, Meade's printed letters, the Huntington catalogue in full text, the Zooniverse project pages, IA, Google
  Books, the open indexes) is covered. Next step for N4: a Supplement-to-the-OR check (owner's machine or a library index) for
  26 Apr 1864 Augur/Meade, ~$1.
- Key: `period` (key-no2.md, Cipher No. 2 book, mssEC 47).
- Depth: **D3**, 100% (9/9 H), check: period key book for every value, date words confirm the 26th, and the OR I/33 Tyler
  telegrams of 26-27 Apr independently show the Department of Washington "party" and its cavalry movement in those days; not D4
  (no print or sequel of the text itself). Sentence unchanged: "Augur tells Meade he cannot send the party without co-operation
  from Warrenton and from Point of Rocks, and will postpone it if Meade cannot give the force now."
- Safe: "Read at grade H with the period Cipher No. 2 book; no prior decipherment or printed text located in the Official
  Records (I/33, I/51 pt 1), the Grant Papers, Meade's Life and Letters, the Huntington collection's full text, the Zooniverse
  project pages, Internet Archive or Google Books full text, or the open scholarship indexes (searched 7 Oct 2026, two audits)."
- Unsafe: "first", "unpublished", "never printed", "previously unknown".

### 4. Postmortem
No over-claim found: the first audit's wording was search-result only and its class stands. The first audit's search for N2-R
lacked the +/-3-day correspondent window, the I/51 supplement, Meade's printed letters, the Huntington full-text search and the
Talk page; all now done, none prints it. SO-ECKERT-N2R row (N3) needs no correction.

## AUDIT (propagation, D12-VP)

Verifier D12-VP (account 2, LANE DEFAULT-account-2-20261007-1210), 7 Oct 2026, 12:54-13:1x UTC by `date -u`; a separate
session from D12-E1..E4 and every earlier eckert-1864 solver, not protecting their conclusions. Scope: the 30 Cipher No. 2
blocks reading-no2.md gained after the last AUDIT.md propagation: N2-V..AC (D12-E2), N2-AD..AK (D12-E1), N2-AL..AR (D12-E3),
N2-AS..AY (D12-E4). Nothing decoded; reading-no2.md, ciphertext-no2.txt and key-no2.md are left as the solvers committed them.

### 1. Re-derivation (rule 7) and image spot-check
- `python3 decode_no2.py --check`: "reading-no2.md is current", exit 0 (12:5x UTC).
- Per-block counts summed by script from the derived block: D12-E2 H 115, **C 10**, I 2, M 0 (the solver's section says C 11;
  the derived block gives C 10 -- V 1, X 1, Z 1, AA 1, AC 6 -- a one-token slip in the prose, no reading changes);
  D12-E1 H 269, C 6, I 5, M 1; D12-E3 H 215, C 14, I 11, M 0; D12-E4 H 237, C 9, I 4, M 0, each as stated. The 30: H 836,
  C 39, I 22, M 1.
- One strip crop per solver from the 2400 px IIIF image (`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/
  default.jpg`, scratch), crop step `python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out $S/crops --prefix p<page>
  --region <x,y,w,h> --lines-per-crop 2 --max-width 1600` with the solvers' own regions: 8915 (N2-Y, E2) 120,2110,2120,400;
  8910 (N2-AJ, E1) 120,2020,2160,440; 8944 (N2-AP, E3) 120,200,2120,640; 8956 (N2-AU, E4) 160,320,2160,1030. Lines read on
  the crops: "Happy Elizabeth Morgan For Magic Egypt Pleas[e] / me precisely when you will reach here"; "Viola For Palermo
  Ingalls Yardstick / Crowd will be down to / the Persia Talbot Annal to"; "Caldwell Hdqrs AP Washn Apl 23 / Elizabeth Berth
  Tulip Please Whiff"; "Harriet Belly Lawn has received over Cla[rke] / wagons Downing or Edwards Medical wagons & over".
  Every word agrees with ciphertext-no2.txt.

### 2. Print confirmation by script (28 entries located in print)
OR pages from the IA djvu full texts fetched once here (warofrebellion322unit, 323unit, 33unit, 342unit, 343unit, 362unit,
363unit, 371unit, 511unit): the phrase is found, and its page is bounded by the nearest standalone page-number lines before
and after it ("a-b" below where a page-number line is missing in the OCR). PUSG vol. 10 (papersofulyssess0010gran) and Basler
vol. 7 (collectedworksof0007royp) by IA full-text search (be-api), which gives the sentence; a page is given only where the
snippet itself runs into a running head.

| entry | print | phrase found (script) | page check | class |
|---|---|---|---|---|
| N2-V | OR I/34 pt 2 p.606 | "Curtis applies to retain", "every furloughed regiment" | 606 | N1 |
| N2-W | OR I/32 pt 3 p.72-73 | "last autumn", "detriment to the service" | 72 | N1 |
| N2-X | PUSG 10 (note) | "The operations of Captain Jenkins at Louisville require investigation" (Stanton to USG) | page not established | N1 |
| N2-Y | PUSG 10 | "favorable arrangements for your family at Willards." ALS, then the p.214 running head | p.213 (the snippet runs into the p.214 head) | N1 |
| N2-Z | OR I/33 p.699 | "Longstreet is now with Lee" | 699 | N1 |
| N2-AA | OR I/33 p.718 | "not in review" | 718 | N1 |
| N2-AB | PUSG 10 (note) | "order all such persons to rendezvous at Annapolis?" ALS (telegram sent), DNA, RG 107 | page not established | N1 |
| N2-AC | OR I/32 pt 3 p.300-301 | "to meet any contingency" | 300-301 | N1 |
| N2-AD | OR I/33 p.486 | "Early is advancing" | 486 | N1 |
| N2-AE | OR I/32 pt 2 (McPhail telegram) | "(Forwarded to Generals Grant and Schofield, February 15.)" | 392-393 (the forwarding line on 393) | N1, see below |
| N2-AF | OR I/32 pt 2 p.410 | "concert of action" | 410 | N1 |
| N2-AG | OR I/33 | "rejoin Lee", "forwarded to General Butler" | **615** (solver: 614) | N1 |
| N2-AH | OR I/33 p.650 | "Dumfries is a bad place" | 650 | N1 |
| N2-AK | Basler, Collected Works of Lincoln vol. 7 | "Unless there be strong reason to the contrary, please send Gen. Kilpatrick to us here, for two or three days. A. Lincoln" | page not established | N1 |
| N2-AL | OR I/33 p.897 | "Camp Dennison", "Sixth Minnesota" | 897 | N1 |
| N2-AM | OR I/33 p.907 | "almost indispensable" | 906-908 | N1 |
| N2-AN | OR I/34 pt 3 p.234-235 | "Iowa delegation" | 234 | N1 |
| N2-AO | OR I/33 p.940 | "fragments of the Tenth Corps" | 940 | N1 |
| N2-AP | OR I/33 p.949 | "armed with carbines" | 949-950 | N1 |
| N2-AQ | OR I/32 pt 3 p.489; I/34 pt 3 p.278 | "garrison at Plymouth"; "Grand Ecore, April 14" | 489-490; 278 | N1 |
| N2-AR | OR I/33 p.966-967 | "notice to the French" | 966 | N1 |
| N2-AS | PUSG 10 | "shall I move them on at once? I think time will be saved by completing the organization tomorrow Please answer" | page not established | N1 |
| N2-AT | OR I/33 p.1002-1003 | "stripped of almost everything" | 1002 | N1 |
| N2-AU | OR I/36 pt 2 p.352 | body OCR too damaged for a phrase; the volume's own index: "Quartermaster-General's Office, U. S. A. Correspondence with ... Grant, U. S 352" | 352 (by index) | N1 |
| N2-AV | OR I/36 pt 2 p.781 | "Resaca" (hit on 781) | 781 | N1 |
| N2-AW | OR I/37 pt 1 p.493 | "three victories" | 493-496 | N1 |
| N2-AX | OR I/36 pt 2 p.907 | "work up the Rappahannock" | 907 | N1 |
| N2-AY | OR I/36 pt 3 p.4 | "Aquia Creek Railroad", "wounded men in Fredericksburg" | 4 | N1 |

All 28: **N1**, key `period` (Cipher No. 2, mssEC 47), text `known`. Safe sentence for each: "The Cipher No. 2 ledger copy reads,
with the period book, to the text printed in <print, page>." Unsafe: anything implying the content was unknown. Notes:
- N2-AG: page correction 614 -> 615 (the hit sits between the 615 and 616 page lines of warofrebellion33unit).
- N2-AE: the McPhail telegram and its forwarding line are printed (I/32 pt 2 pp.392-393; also I/33 p.558 per D12-E1). The
  covering lines and Baldwin's short telegram to Eckert ("this information is obtained on request of Colonel Sharpe by Marshal
  McPhail who sent a reliable man as blockade runner") are not located (I/32 pt 2 and I/33 by "reliable man as blockade",
  "blockade runner", "Eckert": 0 hits). A two-line office note inside an N1 entry; not classed separately, logged here.
- N2-AK: Basler prints "strong reason" (singular), the ledger "strong reasons"; one plain word, not graded.
- Page numbers marked "page not established" need a person's read of PUSG vol. 10 (IA lending copy); the text is certain.

Depth (rule 4a), per entry, % = (H+C)/code-word tokens (script over the derived block), external check the print and the
re-derivation above. **D4** (every code-word token H or C): N2-V, W, Y, Z, AA, AB, AG, AH, AK, AM, AN, AP, AS, AU, AV, AX, AY
(100% each). **D3** (I or M tokens remain): N2-X 92%, AC 97%, AD 93%, AE 97%, AF 97% (1 M, Chumb), AL 95%, AO 97%, AQ 93%,
AR 93%, AT 98%, AW 95%. Outward words: D4 "deciphered", D3 "largely deciphered (about N%)"; text `known` for all 28.

### 3. The two entries not located in print: full search (7 Oct 2026)
- **N2-AI** (p.18, pointer 8910, Capt. Wm. T. Howell, A.Q.M., to Brig. Gen. Ingalls, 8 Mar 1864 3.30 PM, operator A. H. Caldwell):
  Rucker has sent all available water transportation to Yorktown and Biggs at Fort Monroe is ordered to send all there;
  Kilpatrick's order left with Rucker; a large steamer ordered from New York; enough transportation at Yorktown for 1,000 men
  and horses by tomorrow evening; the 1,400 cavalry horses being purchased, the first lot tomorrow; Captain Feilner notified.
- **N2-AJ** (p.18, pointer 8910, Augur to Ingalls, 9 Mar 1864, header 12 noon, time word Viola = 12 midnight, conflict logged by
  the solver): "Lieut Gen Grant will be down to the Army of the Potomac tomorrow."

| family | searched | result |
|---|---|---|
| OR I/33 full text (djvu), date window 5-12 Mar 1864 by correspondent | phrases "Rucker informs me", "1,400 cavalry", "sufficient transportation at Yorktown", "will be down to the Army of the Potomac", "down to the Army of the Potomac to-morrow"; every "March 8/9/10, 1864" item naming Ingalls, Howell, Yorktown or Augur; the index: Ingalls's correspondents (Devereux, Meade, QMG Office, Rucker) and Augur's (no Ingalls); "Howell" (only John H. Howell, p.483) | no AI, no AJ; positive control N2-AH ("Dumfries is a bad place") found at p.650 in the same file |
| OR I/51 pt 1 (Union supplementary correspondence, warofrebellion511unit) | "Rucker informs", "Howell" (25 hits: William T. Howell only as a later disbursing officer), "1,400 cavalry", "will be down to the Army", March 8 and 9, 1864 items | no AI, no AJ |
| PUSG vol. 10 (IA fts) | "down to the Army of the Potomac" (0); "Howell" (M. D. Howell, May 1864, unrelated); "Ingalls" (USG to Ingalls 16 Feb only); "Rucker" (index only) | no AI, no AJ; controls N2-X, Y, AB, AS all found in the same volume |
| Huntington CONTENTdm, whole collection p16003coll11, CISOSEARCHALL with full-text flag | "Howell" (18), "Yorktown Ingalls" (4), "Augur Ingalls" (2); item info read for all 24 and grepped for 1864/Ingalls/Howell/Rucker/Augur | only 8910 itself carries either telegram; the other hits are 1862-1865 pages (Howell as a 1865 cipher word on mssEC 25, City Point 1865 traffic); no decoded field |
| Google Books API (key, country=US), 7 queries | "Rucker informs me that he has sent"; "available water transportation to Yorktown"; "sufficient transportation at Yorktown"; "steamer has been ordered from New York" Kilpatrick; "will be down to the Army of the Potomac to-morrow"; Augur Ingalls "March 9, 1864" Grant; Howell Ingalls Kilpatrick Yorktown March 1864; control "Dumfries is a bad place" Kilpatrick | no AI/AJ text (loose matches only); control found the OR |
| OpenAlex (key) | "Kilpatrick Yorktown transportation Ingalls 1864" | 0 works |
| JSTOR | four rows queued in JSTOR-QUEUE.tsv, both families per entry | pending (never blocks) |
| Unreachable / unread | Supplement to the OR (Hewett; not full-text searchable from the cloud, as D12-V2R found); NARA RG 92 (Quartermaster General, consolidated correspondence; Howell's and Ingalls's letters), RG 393 (Dept. of Washington telegrams sent), RG 107 M473/M504; Ingalls papers; HathiTrust full text | unread |
Requests (this whole job): archive.org 9 (djvu texts), be-api.us.archive.org 13 (fts), hdl.huntington.org 31 (7 searches, 24 item
info) + 4 IIIF images, googleapis.com 8, api.openalex.org 1; all 200 except one be-api reply that was not JSON (retried once, 200).

### 4. Classification of N2-AI and N2-AJ (key `period`)
- **N2-AI**: **N3**. No prior plaintext or decipherment located after the search above. Not N4: the Quartermaster records
  (RG 92) and RG 107 telegram copies, where a QM's telegram to Ingalls would be kept, and the Supplement to the OR are unread.
  Depth **D3**, 100% (40/40 H), check: the period key for every value and agreement with the printed sequel of the same days
  (Kilpatrick's command shipped from Yorktown to Alexandria, OR I/33 pp.650, 662: Ingalls to Meade 7 Mar on boats, Kilpatrick
  9 Mar "orders to embark my command for Alexandria"); not D4, no print of this text. Safe: "Read at grade H with the period
  Cipher No. 2 book; no prior decipherment or printed text located in OR I/33 or I/51 pt 1, PUSG vol. 10, the Huntington
  collection's full text, Google Books or OpenAlex (searched 7 Oct 2026)." Unsafe: "first", "unpublished", "never printed".
  Sentence: "Captain Howell tells Ingalls that Rucker has sent all available water transportation to Yorktown, enough for
  1,000 men and horses by the next evening, and that the first of the 1,400 cavalry horses being bought arrives tomorrow."
- **N2-AJ**: **N3**. Same search; not N4 for the same unread series (RG 393 Dept. of Washington telegrams sent). Depth **D3**,
  100% (9/9 H), check: the period key, and the content agrees with the printed sequel: OR I/33 (p.663-664, between the
  page lines in warofrebellion33unit), Humphreys's circular of 10 March 1864 "Lieutenant-General Grant has arrived at his
  headquarters", and Stanton to Burnside the same day "General Grant has gone to the front"; not D4, no print of this text, and the time word (Viola = midnight) conflicts with the header's noon.
  Safe: as N2-AI. Unsafe: "first", "unknown". Sentence: "Augur tells Ingalls that Lieutenant-General Grant will come down to the
  Army of the Potomac tomorrow." Note: a one-sentence telegram whose content (Grant's 10 March visit) is well known; N3 is
  about this text, not the event.
- SECOND-OPINIONS-QUEUE.tsv: SO-ECKERT-N2AI and SO-ECKERT-N2AJ added in this session, with prompts in second-opinions/.
  status.json: one result row each.

### 5. key-no2.md section 8 conflicts recorded by the solvers (logged, not resolved here)
- Religion = Operations ([25B], I): further witnesses N2-X (Grant Papers "The operations of Captain Jenkins") and N2-AW (OR
  "operations in that department"), with ECK64-NO2's Slumber(ations) = operations in N2-T; the [25B] row alignment stays I
  as the key row stands. Two words cannot both own Operations in a one-part book unless one is the clerk's; open.
- Nuptial = Smith (H, book p.19 l.8) in N2-AL and four times in N2-AQ, each = Smith in the print; but N2-AQ "Nuptial Princeton
  and the Sheffields" = OR I/34 pt 3 p.278 "Steele's command and the gun-boats". The derived block reads Smith; the print says
  Steele. Logged (the operator's own note "Harding & Nuptial both arbitraries" bears on it).
- N2-AT "yawl": the book's Yawl = Signed; the OR has a sentence break there and the message runs on to Lamb (H W Halleck) at the
  foot of p.60; marked plain by the solver so the decoder does not end the message. Logged.
- Also logged by the solvers and seen here, not resolved: Pine = Communicate vs N2-AE "Snake Pine Talbot Argus" = "Hdqrs. Army
  of the Potomac"; time/number words against print (N2-AA Gertrude 12 noon vs OR 12.30; N2-AH Elizabeth 10.30 vs OR 10.50;
  N2-AJ Viola midnight vs header noon; N2-AQ date words 26 vs 25; N2-AR 11.30 AM vs OR p.m.; N2-AX 9.30 vs OR 10 p.m.; N2-AY
  300 vs OR 3,000 wounded and the second Castor = Rappahannock).

### 5a. Postmortem
- No novelty over-claim in the four solvers' sections: each says "located"/"not located" only. Corrections: D12-E2's C 11 is
  C 10 (section 1); N2-AG page 615, not 614; N2-AE "about p.392" is pp.392-393. Not edited in reading-no2.md (a solver file);
  this section is the record.

## AUDIT 2 (second adversarial, D4-V2AI)

Verifier D4-V2AI (account 4, LANE DEFAULT-account-4-20261007-1335), 7 Oct 2026, 13:43-13:5x UTC by `date -u`; a separate session
from the solver (D12-E1) and from the first auditor (D12-VP), not protecting either. One entry: **N2-AI** (mssEC 19 p.18, pointer
8910, Capt. Wm. T. Howell, A.Q.M., to Brig. Gen. Ingalls, Washington 8 Mar 1864 3.30 PM, operator A. H. Caldwell). Nothing decoded
beyond re-running the committed script; reading-no2.md left as committed.

### 1. Re-derivation (rule 7) and image check
- `python3 ciphers/eckert-1864/decode_no2.py --check`: "reading-no2.md is current", exit 0. N2-AI: 40 code-word tokens, H 40, no C/S/M/I.
- Strip crop from the 2400 px IIIF image (`hdl.huntington.org/digital/iiif/p16003coll11/8910/full/2400,/0/default.jpg`, scratch, not
  committed): `python3 tools/iiif_lines.py --image $S/img/p8910.jpg --out $S/crops --prefix p18 --region 120,240,2160,1560
  --lines-per-crop 4 --max-width 1600` (17 lines, 5 bands x 2 segments). All 16 message lines read on the crops agree word for word
  with ciphertext-no2.txt (Imogene ... Rucker in forms / Optic water Weasel / Hug ... Pearl Biggs at Bunyan / Trinity / Stephen
  Milans / Yardstick / Wayworn ... Bunyan / Waltzer ... Girdle Tulip / Waltzer from Granada ... Weasel / Hulk for Allen Seward Summer
  and Silvers / Optic by Wedlock evening Yacht / Kirby Douglas Pekin Silvers / Wedlock ... Cap Feilner / Spencer).
- Every code word checked against key-no2.md (book page and line): Hug and Hulk both Yorktown (p.16 l.26 L/R), Girdle and Granada
  both New York (p.15 l.16 L/R), Weasel and Wayworn both Transportation (p.24 l.23 R/L), Bunyan Monroe, Pearl Colonel, Optic
  Available, Waltz(er) Steam, Milan(s) Kilpatrick J, Silver(s) Horse, Allen 1 + Seward 1000, Kirby 14 + Douglas 100 (= 1,400),
  Pekin Cavalry, Summer Men, Wedlock Tomorrow, Spencer Information, Stephen Left, Trinity Point, Spark General, Palermo Brig. General,
  Tulip Period, Imogene 3.30 PM (agrees with the header "3.30 PM"). No conflict found.

### 2. Families D12-VP section 3 did not cover, searched here (7 Oct 2026)
| family | searched | result |
|---|---|---|
| IA full text, whole corpus (be-api fts, no identifier) | phrases "Rucker informs me that he has sent", "1,400 cavalry horses", "all his available water transportation", "transportation at Yorktown for", "Captain Feilner"; boolean Howell AND Ingalls AND Yorktown AND Kilpatrick (AND Rucker); Feilner AND Ingalls AND Kilpatrick | 0 hits for every message phrase; "Captain Feilner" 93 hits, all John Feilner as naturalist / with Sully 1864, none this text. Positive control "Dumfries is a bad place" (N2-AH): 9 items incl. OR I/33 |
| Butler, Private and Official Correspondence vol. 3 (Feb 1863-Mar 1864; IA privateoffice03butlrich, djvu read) | Howell, Feilner, Rucker, Ingalls, Biggs, Kilpatrick, Yorktown, transportation, steamer | no N2-AI text. Prints the surrounding traffic: Butler to Kilpatrick at Yorktown, 5 Mar 1864, "Transports for your cavalry will be at Newport News" (p.492-493), and Lt. Col. H. C. Biggs as Butler's chief quartermaster -- independent agreement with the decoded "Colonel Biggs at Monroe" (Pearl, Bunyan) and "Yorktown" (Hug/Hulk) |
| OR I/36 pt 1 (warofrebellion361unit, djvu): Ingalls's own report as chief QM (No. 7) | Howell, Feilner, Yorktown, Ingalls | no N2-AI text; the report starts in May 1864; Howell hits are other Howells |
| OR ser. III vol. 4 (QM correspondence 1864-65) | IA advancedsearch for the volume (rootrich series has ser. 3 vols 1-2 only); Google Books API "Ingalls Yorktown Kilpatrick Series III quartermaster 1864" | **not reachable as full text** from the cloud on this date; Google Books gave only ser. I hits and QM annual reports (no snippet of this text) |
| Google Books API (key, country=US), 11 further queries | "Captain Howell" Kilpatrick Yorktown; Howell quartermaster Ingalls Yorktown steamers; "1,400 cavalry horses"; "1400 cavalry horses" 1864; "Rucker informs me"; Feilner cavalry horses 1864; Biggs "Fort Monroe" Yorktown Kilpatrick "March 8, 1864"; "Wm. T. Howell" quartermaster; Kilpatrick Dahlgren raid Yorktown transports Ingalls (two 503s, each retried once after a pause, 200) | no N2-AI text. Context only: Wm. T. Howell appears as Ingalls's assistant QM at City Point, Jan 1865 (OR ser. I), and in later QM registers; QM General's annual report 1865 prints Cavalry Bureau horse purchases from July 1864 (after this date) |
| Semantic Scholar (key) | "Kilpatrick Yorktown transportation Ingalls March 1864 cavalry" | 0 |
| CORE (key) | Kilpatrick AND Yorktown AND Ingalls (first call 500, one retry 200) | 0 |
| CrossRef | "Kilpatrick Dahlgren raid Yorktown transportation 1864" | top hits a Confederate-newspaper anthology chapter "The Dahlgren Raid" (10.2307/jj.26193459.36) and 1864 newspaper items; none bears on a Union QM telegram |
| OpenAlex (key) | "Howell Ingalls Yorktown water transportation 1864" | 0 |
| JSTOR | rows 312-313 (families i and ii) already queued by D12-VP; one more family (ii) row added: "Rucker informs me that he has sent" | pending (never blocks) |
| Unreachable / unread (unchanged) | NARA RG 92 (QM General consolidated correspondence; Howell's and Ingalls's letters), RG 107 (M473/M504 telegrams), RG 393; the Supplement to the OR; OR ser. III vol. 4 full text; Ingalls papers; HathiTrust full text | unread |
Requests: be-api.us.archive.org 10, archive.org 6 (advancedsearch 4, metadata 1) + 2 djvu downloads, googleapis.com 13, api.semanticscholar.org 1,
api.core.ac.uk 2, api.crossref.org 2, api.openalex.org 1, hdl.huntington.org 1 (IIIF image).

### 3. Classification (key `period`)
- **N2-AI: N3, held.** No prior plaintext or decipherment located after both audits' searches. Not N4: the series where a QM's
  telegram to Ingalls would be kept or printed (RG 92, RG 107, the Supplement, OR ser. III vol. 4) are still unread, and those are
  the principal places the text could be. Not lowered: nothing found in print or in another decipherment.
- **Depth: D4 (raised from D3).** Rule 4a's D4 criteria, item by item: every cipher-letter token H (40/40, period book mssEC 47); no
  residue; a non-statistical external check (the image agrees with the transcription word for word, and printed traffic of the same
  days independently confirms specific decoded values: Biggs as the Fort Monroe chief QM, transports for Kilpatrick's cavalry at
  Yorktown -- Butler Correspondence vol. 3 pp.492-493; Kilpatrick's command shipping from Yorktown, OR I/33 pp.650, 662); and a
  fresh rule-7 re-derivation by a session other than the solver's (section 1). D12-VP held D3 because "no print of this text"; that
  is a novelty fact, not a depth criterion. Outward words: "deciphered". decode_status Decrypted.
- Safe sentence: "Read at grade H with the period Cipher No. 2 book; no prior decipherment or printed text located in the Official
  Records (ser. I vols 33, 36 pt 1, 51 pt 1), the Grant Papers vol. 10, Butler's printed Correspondence vol. 3, the Huntington
  collection's full text, Internet Archive full text, Google Books, OpenAlex, Semantic Scholar, CORE or CrossRef (searched 7 Oct
  2026, two audits)." Unsafe: "first", "unpublished", "never printed", "unknown".
- Depth sentence (unchanged, checked against the derived block): "Captain Howell tells Ingalls that Rucker has sent all available
  water transportation to Yorktown, enough for 1,000 men and horses by the next evening, and that the first of the 1,400 cavalry
  horses being bought arrives tomorrow."

### 4. Postmortem
- No over-claim in D12-E1's or D12-VP's text for N2-AI. One understatement corrected: depth D3 -> D4 (section 3). The
  SO-ECKERT-N2AI prompt quotes no class or depth, so it needs no change. status.json row updated (two audits, D4).
- Context, not a finding: "Cap Feilner" is most likely Capt. John Feilner, 1st U.S. Cavalry (Pope to Halleck, April 1864, in the
  Mereness Calendar names him); not used in the grading.

## AUDIT 2 (second adversarial, D4-V2AJ)

Verifier D4-V2AJ (account 4, LANE DEFAULT-account-4-20261007-1335), 7 Oct 2026, 13:44-13:5x UTC by `date -u`; a session separate
from the solver (D12-E1) and the first auditor (D12-VP), not protecting either. Scope: **N2-AJ** only (mssEC 19 p.18, pointer
8910, second entry, Augur to Ingalls, 9 Mar 1864). Nothing decoded; reading-no2.md and ciphertext-no2.txt left as committed.

### 1. Re-derivation and image check
- `python3 ciphers/eckert-1864/decode_no2.py --check`: "reading-no2.md is current", exit 0 (13:46 UTC). Block: 9 code words, H 9.
- Crop step (2400 px IIIF image, scratch): `python3 tools/iiif_lines.py --image $S/img/p8910.jpg --out $S/crops --prefix p18
  --region 120,2020,2160,440 --lines-per-crop 2 --max-width 1600` (5 lines, 6 crops) and the header line `--region
  120,1950,2160,110 --lines-per-crop 1`. Read on the crops: "Viola For Palermo Ingalls Yardstick / Crowd will be down to / the
  Persia Talbot Annal to / more row Wiley Lantern Sharks" -- every word agrees with ciphertext-no2.txt.
- **Header correction.** The header's time, read at native resolution (IIIF region 4800,5050,700,250 of the 6215 x 7200
  master), is **"12. midn"** (m, dotted i, looped d, n: midnight), not "12. noon" as ciphertext-no2.txt, reading-no2.md (block
  title and line 296), the SO prompt and D12-VP section 3/4 have it. So the time word Viola = 12 midnight (key-no2.md, TIME page
  555) **agrees** with the header; the "Viola midnight vs header noon" conflict logged by the solver and by D12-VP (section 5)
  was a transcription slip of the plain header, not a key or ledger conflict. Midnight 9/10 March also fits the content: "to-
  morrow" is 10 March, the day Humphreys's circular says Grant arrived at Meade's headquarters. Not edited in the solver's files
  (ciphertext as transcribed is not silently repaired); flagged in ROOM.md for the solver side to correct ciphertext-no2.txt's
  header and regenerate; the reading's 9 code words are unchanged. (NOTES.md's "Viola 12.30 PM" at lines 453 and 513 belongs to
  the old vocabulary, key-no9, not to Cipher No. 2.)

### 2. Families D12-VP section 3 did not cover, searched here
| family | searched | result |
|---|---|---|
| OR I/33 by date and correspondent (warofrebellion33unit djvu, fetched once) | every item dated 9 and 10 March 1864 in the Union correspondence (pp.659-665): Meade/Williams orders, Stanton's Washington-defences order to Canby, Halleck relieved, Stanton to Grant "Hdqrs. Army of the Potomac" 1.40 p.m., Humphreys circular, Burnside/Stanton, Tyler to Taylor (Dept. of Washington) | no Augur-to-Ingalls item; Ingalls's index entries (596, 647, 650, 651, 852-853, 856, 921) none on 9-10 Mar |
| OR ser. III vol. 4 (in.ernet.dli.2015.171703 djvu; poor OCR) | items dated 6-12 March 1864 (lines 14124-15982 of the OCR): Augur, Ingalls, Grant, Quartermaster, "Potomac" | none; the volume's March items are recruiting/furlough orders. (in.ernet.dli.2015.165578, labelled ser. III vol. 4, is a different volume -- no 1864 March items) |
| PUSG vol. 10 (IA fts, papersofulyssess0010gran), further terms | "Augur" (5 snippets: Comstock to Augur 26 Mar, USG to Augur 25 Mar etc., none 9 Mar); "Ingalls" (16 Feb letter, 13 Apr report); "midnight"; "will be down"; "Army of the Potomac tomorrow"; "to the front" | no N2-AJ text and no editorial note quoting it |
| IA full text, whole archive (be-api fts, no identifier) | "will be down to the Army of the Potomac"; "Grant will be down to the Army"; "down to the Army of the Potomac to-morrow" | 0, 0, 0; positive control "General Grant has gone to the front" (Stanton to Burnside, OR I/33 p.664) 21 hits |
| Huntington CONTENTdm p16003coll11, CISOSEARCHALL, full-text flag | "Grant down Potomac" (4), "Augur Grant" (22); item info of all 26 read and grepped for Ingalls / "will be down" / Mch 9 | no second copy (plain or cipher) of this telegram; the two Ingalls hits (pointers 10525, 7832) are Ingalls's own later telegrams |
| Google Books API (key, country=US), 4 queries | "will be down to the Army of the Potomac" (loose matches only, OR formal reports, Army and Navy Journal); "Grant will be down" Augur Ingalls; Augur Ingalls "March 9, 1864" telegram Grant; control "General Grant has gone to the front" Burnside | no N2-AJ text; control found OR I/33 and House documents |
| Open indexes | OpenAlex (key) phrase: 0 works; CrossRef bibliographic: only a chapter "Grant as General in Chief" in Taaffe, *Commanding the Army of the Potomac* (doi 10.2307/j.ctv7n0c2r.11), a narrative secondary work, text not read; CORE (key): noise only; Semantic Scholar: HTTP 429 twice (one retry after a pause), unreachable this session | nothing |
| JSTOR | JSTOR-QUEUE.tsv rows for N2-AJ already exist in both families: (i) "Augur" AND "Ingalls" AND "March 9, 1864" ...; (ii) "will be down to the Army of the Potomac" | pending (never blocks) |
| Unreachable / unread | NARA RG 393 Dept. of Washington telegrams sent (Augur's own book, the most likely place a copy survives), RG 92 Quartermaster General (Ingalls's received telegrams), RG 107 M473/M504; Ingalls papers; Supplement to the OR (Hewett); HathiTrust full text (Cloudflare) | unread |

Requests: archive.org 9 (6 djvu downloads incl. one 403 on a wrong identifier and one empty first try, 3 metadata/search) + be-api.us.archive.org 12, hdl.huntington.org 31 (3 IIIF images, 1 info.json,
2 searches x2, 26 item info), googleapis.com 4, api.openalex.org 1, api.crossref.org 1, api.core.ac.uk 2 (one 500, retried once),
api.semanticscholar.org 2 (429, 429); all others 200.

### 3. Class (key `period`)
**N2-AJ stays N3.** No prior plaintext or decipherment located after the searches of D12-VP section 3 and this section. Not N4:
Augur's Department of Washington telegrams-sent book (RG 393), where the sender's copy would sit, and the Supplement to the OR
are unread, the same reason D12-V2R kept N2-R at N3. Depth **D3**, 100% (9/9 H), check: the period key for every value, the
header time now agreeing with the time word, and the content agreeing with the printed events of 10 March (Humphreys circular,
Stanton "General Grant has gone to the front", OR I/33 pp.663-664); not raised to D4, since no print of this text exists to
check it against. Safe sentence: "Read at grade H with the period Cipher No. 2 book; no prior decipherment or printed text
located in OR I/33, I/51 pt 1 or ser. III vol. 4, the Grant Papers vol. 10, the Huntington collection's full text, Internet
Archive full text, Google Books, OpenAlex or CrossRef (two audits, 7 Oct 2026)." Unsafe: "first", "unpublished", "never
printed", "previously unknown" -- the event (Grant's visit of 10 March) is well known; N3 is about this telegram's text.
Sentence: "At midnight on 9 March 1864 Augur tells Ingalls that Lieutenant-General Grant will come down to the Army of the
Potomac the next day."
- **Depth raised D3 -> D4** after reading D4-V2AI's section 3 (same lane, same page): rule 4a's D4 items are met -- every
  cipher-letter token H (9/9), no residue, a non-statistical external check (the image agrees word for word; the header time
  agrees with the time word; printed traffic of 10 March independently confirms the decoded content, Grant at Meade's
  headquarters that day, OR I/33 pp.663-664), and a fresh rule-7 re-derivation by a session other than the solver's (section 1).
  "No print of this text" (the D3 reason above and in D12-VP) is a novelty fact, not a depth criterion; the D3 line above is
  superseded. Outward words: "deciphered". decode_status Decrypted.

### 4. Postmortem
- Over-claim: none; the solver and D12-VP say "not located". Error caught: the header "12. noon" is "12. midn"; the logged
  time-word conflict for N2-AJ in reading-no2.md line 296, D12-VP sections 3, 4 and 5, the SO prompt and status.json is void.
  Corrected here, in the SO prompt (row SO-ECKERT-N2AJ, still queued) and in status.json; the solver files are flagged, not
  edited.

## AUDIT (propagation, D4-VP2)

Verifier D4-VP2 (account 4, LANE DEFAULT-account-4-20261007-1335), 7 Oct 2026, 14:21-14:3x UTC by `date -u`; a separate session
from D4-E5 (solver of N2-AZ..BF), D4-E5H and every earlier eckert-1864 solver, not protecting their conclusions. Scope: the seven
Cipher No. 2 blocks reading-no2.md gained after the last propagation (N2-AZ..BF, mssEC 19 pp.86-105, June-July 1864), the six
key-no2.md section 8 clerk's forms D4-E5 added, and D4-E5H's N2-AJ header correction. Nothing decoded; the solvers' files untouched.

### 1. Re-derivation (rule 7) and image check
- `python3 decode_no2.py --check`: "reading-no2.md is current", exit 0 (14:2x UTC).
- Per-block code-word counts from the derived block: N2-AZ H 15, I 2; N2-BA H 32; N2-BB H 49, C 4, I 3; N2-BC H 27, C 3, I 2;
  N2-BD H 54, C 1; N2-BE H 56, C 3, I 4; N2-BF H 59, C 4, I 3. Sum H 292, C 15, I 14, M 0, as D4-E5 states.
- Strip crops from the 2400 px IIIF images (`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`,
  scratch, regenerable), crop step `python3 tools/iiif_lines.py --image $S/img/p<pointer>.jpg --out $S/crops/<d> --prefix p<page>
  --region <x,y,w,h> --lines-per-crop 3 --max-width 1600` with the solver's regions: 8983 (N2-AZ) 120,200,2200,1520, 8 lines read;
  8988 (N2-BC) 150,150,2250,1550, 4 lines; 8996 (N2-BE) 150,1730,2250,900, 4 lines + header. Every word read agrees with
  ciphertext-no2.txt, the code words included: Imogene Hawkins Mars tulip Crowd stick yard Behead Chart rockland (N2-AZ); hang Morgan
  Hannah Crowd Bridle tulip Whims World Bermuda pedlar Meriden raven Meriden's virtue (N2-BC); Hunter Mark Fisher Henrietta Chant
  Tulip Famish whiffs Ginger Mark Brooks Clarke Dwight Summer Richard Bunyan (N2-BE): 40 code-word tokens, 40 agree. N2-AZ's
  pencilled glosses over line 1 ("flor", "weida", "frame", "help") are seen as the solver describes and are not transcribed.

### 2. Print confirmation by script
OR pages from the IA djvu full texts fetched once here (warofrebellion344unit, 363unit, 371unit, 372unit, 402unit; also 361unit,
401unit, 511unit for N2-AZ): each phrase is found and its page is the last running-head page number before it (the head is the
first line of each page in these OCR files; curly apostrophes in the OCR were matched by shorter phrases). PUSG vol. 11
(papersofulyssess0011gran) by IA full-text search (be-api), which gives the sentence but not the page.

| entry | solver's citation | phrase found (script) | page here | class |
|---|---|---|---|---|
| N2-AZ | PUSG 11 by Google Books snippet, page not established | be-api: "hope General Grant will not put too much confidence in, Barnard", "practical military affairs", "deplorable results", "proper comprehension of practical purposes", "If General Grant trusts to his own judgment we are safe, but trust in Barnard is" | page not established | N1 |
| N2-BA | OR I/34 pt 4 p.424-425 | "I learn that the gauge" (p.424), "locomotive builders", "can be had ready built" (p.425) | 424-425 | N1 |
| N2-BB | OR I/40 pt 2 p.117, also I/37 pt 1 p.645 | "German engineer", "6th and 7th", "well supplied with provisions", "verified by others" | **I/40 pt 2 p.116; I/37 pt 1 p.644** (each whole telegram between the 116/117 and 644/645 heads) | N1 |
| N2-BC | OR I/37 pt 1 p.650-651 | "possession of Staunton" (650), "superior to Hunter's", "extremely perilous", "communication to him from this side" (651) | 650-651 | N1 |
| N2-BD | OR I/34 pt 4 p.528 | "limited to the defensive", "shortest time to serve" | 528 | N1 |
| N2-BE | OR I/37 pt 2 p.119 | "telegraphs from New Orleans", "Monocacy.", "2,496", "Maryland Heights, at Hagerstown", "considerable alarm in" | 119 | N1 |
| N2-BF | OR I/36 pt 3 p.569-570 | "June 4, 1864 -- 2.20 p.m." head, "6,683", "remounted here", "About 1,000 more", "5,000 more men", "Lewisburg", "moving against Marietta" | **569** (the whole telegram lies between the 569 head and the next page's head, whose number the OCR lost) | N1 |

N2-AZ beyond the solver's log: not in OR I/36 pt 1 (where Dana's own reports are printed), I/36 pt 3, I/40 pt 1, I/40 pt 2 or
I/51 pt 1 by "confidence in Barnard", "practical military affairs", "deplorable results", "McClellan's blunders" (0 hits each;
controls "6,683" and "German engineer" found in 363unit and 402unit). The ledger's "is in large degree" against the printed draft's
"is ne smal degree" (struck words kept by PUSG) is the solver's observation and agrees with the be-api snippet.

All seven: **N1**, key `period` (Cipher No. 2, mssEC 47), text `known`. Safe sentence for each: "The Cipher No. 2 ledger copy reads,
with the period book, to the text printed in <print, page>." Unsafe: anything implying the content was unknown. No N3 or better, so
no SECOND-OPINIONS-QUEUE.tsv row. Page corrections (not edited in reading-no2.md or key-no2.md, solver files; this section is the
record): N2-BB OR I/40 pt 2 **p.116** (not 117) and I/37 pt 1 **p.644** (not 645); N2-BF OR I/36 pt 3 **p.569** (not 569-570).
The same three page numbers recur in key-no2.md section 8's citations for Dorming, Pene and Sprage.

Depth (rule 4a), % = (H+C)/code-word tokens from the derived block, external check the print and the re-derivation above:
**D4** (every code-word token H or C): N2-BA (32/32), N2-BD (55/55). **D3**: N2-AZ 88% (2 I: the clerk's split "Barn = yard"),
N2-BB 95%, N2-BC 94%, N2-BE 94%, N2-BF 95% (every I token the short period form yard or stick, per D4-E5). Outward words: D4
"deciphered", D3 "largely deciphered (about N%)"; text `known` for all seven.

### 3. key-no2.md section 8: the six clerk's forms (C), each checked against the print here
| form | value | witness in the ledger | print phrase found (script) |
|---|---|---|---|
| Dorming | 7 | N2-BB twice | "left Lee's army June 7", "on the 6th and 7th" (OR I/40 pt 2 p.116) |
| Pene | Army | N2-BB "Jaunts Pene well seasoned" | "Lee's army is well supplied with provisions" (I/40 pt 2 p.116) |
| plantation | communication | N2-BC | "to get any communication to him from this side" (I/37 pt 1 p.651) |
| Meridians | Hunter D | N2-BC "superior to Meridians" | "superior to Hunter's" (I/37 pt 1 p.651) |
| Mindins | Hunter D | N2-BE | "Hunter's army move's so slow" (I/37 pt 2 p.119) |
| Sprage | 1000 | N2-BF "Caldwell Sprage more" | "5,000 more men" (I/36 pt 3 p.569) |
All six stand at C as single-context or two-context clerk's forms; carried into this audit with the page corrections above.
Plantation and Mindins have one witness each; their C rests on the print alone.

### 4. N2-AJ header correction (D4-E5H, commit 1c88589f1), carried into D12-VP's sections 3-5
D12-VP's text above is left as written; this note supersedes it where it says otherwise. The p.18 (pointer 8910) N2-AJ header
reads "12. midn" (D4-V2AJ, D4-E5H, each on a native-resolution crop), not "12 noon". Therefore: in section 3, read N2-AJ's
header as "12 midn" and drop "time word Viola = 12 midnight, conflict logged by the solver"; in section 4, the clause "and the
time word (Viola = midnight) conflicts with the header's noon" no longer holds (time word and header agree); in section 5, delete
"N2-AJ Viola midnight vs header noon" from the time/number-word list. The class (N3), depth and safe sentence are unchanged
(D4-V2AJ's AUDIT 2 already raised depth to D4 and reads the header as midn). Checked here: status.json's N2-AJ row already reads
"12. midn"; SECOND-OPINIONS-QUEUE.tsv and the second-opinions/ folder carry no "noon" or "Viola" for N2-AJ (grep).

### 5. Search log and requests
Families: OR (IA djvu full text, eight volumes named above); PUSG vol. 11 (IA be-api fts, 6 queries); the solver's Google Books
snippet for N2-AZ not repeated (the be-api snippet is the same text). Not searched (not needed for N1 entries): JSTOR, OpenAlex,
NARA. Requests: archive.org 9 (8 djvu texts, 1 advancedsearch), be-api.us.archive.org 6, hdl.huntington.org 4 (one empty reply, retried once
after a pause, 200); all others 200.

### 6. Postmortem
- No novelty over-claim in D4-E5's section: it says "located"/"not located" and "a search result only". Corrections: the three
  page numbers in section 2; D4-E5's NOTES.md "65-entry total from the decoder" is the 58-entry total (the derived block says
  "Totals over the 58 entries"; 58 `### N2-` blocks in ciphertext-no2.txt). Not edited in the solver's files.
- PROGRESS.tsv carries no eckert-1864 row; none added (one-row-per-leaf register, not this job's to open).

## AUDIT (LS-V1)

Verifier LS-V1 (account 1, LANE ST-LEDGER), 7-8 Oct 2026, 23:38-00:1x UTC by `date -u`; a separate session from the solver
(LS-R1), not protecting its conclusions. Scope: LS-R1's entries **E21-E29** (mssEC 19, Cipher No. 1, key.md = mssEC 41). Nothing
decoded beyond re-running the committed script. Key source for every item: `period` (the War Department's own Cipher No. 1 book).

### 1. Re-derivation (rule 7) and image spot-check
- `python3 ciphers/eckert-1864/decode.py --check`: "reading.md is current", exit 0. E21-E29 derived block: H 175, C 3 by the decoder;
  LS-R1's hand regrading (E25 "pike" H -> M, E27 "Grunt" H -> M) checked against key.md and accepted: net H 173, C 3, M 2.
- Strip crops from the 2400 px IIIF images (`hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg`, scratch,
  not committed): `python3 tools/iiif_lines.py --image $S/img/p9053.jpg --out $S/crops/9053 --prefix p9053 --region 0,100,2400,1400
  --centres 50,150,...,1350 --lines-per-crop 4 --max-width 2400` and the same for 9115 with `--region 0,930,2400,1200 --centres
  50,...,1150`. E26 (9053) lines "that a large stock of revolvers & offal / imported recently for copper heads in Alden is / stored at
  No lampoon plank Walker St frog / awaiting to be forwarded wicoff" and E29 (9115) lines "Tappan Dudley Harris Port land Adam Pekin
  Lamp Person or / Leg years old has a bull dog look Pedlar snuffs / up his nose squints with his left eye Pekin dark / hair slightly
  tinged with gray bright dark eyes with a" agree word for word with ciphertext.txt.

### 2. Entries LS-R1 located in print: page confirmed by script (a check, not a search)
| ID | printed at | how confirmed |
|---|---|---|
| E22 | ORN ser. I vol. 26 p.92 | IA `officialrecordso0026unse` djvu: "neither general smith nor his force will be withdrawn ... red river" (exact) |
| E24 | OR ser. III vol. 4 **p.392** (Seward to Adams, 18 May 1864 12.30 p.m., "Same to William L. Dayton"), also Papers relating to Foreign Affairs 1864 and Bates, Lincoln in the Telegraph Office | IA `warofrebellionco0004genf` djvu, exact, between the p.391 and p.393 running heads; LS-R1 had "page not fixed" -- now fixed. IA full-text (all items) also hits Bates and two press-freedom histories |
| E25 | OR ser. I vol. 37 pt 2 p.501 (Halleck to Wallace, 29 July 1864 12.20 p.m.) | IA `warofrebellion013702rootrich` djvu: text before the p.502 running head; Wallace's own relay to Tyler of the same day prints "Edwards and Conrad's Ferries, with 400 cavalry and three pieces of artillery ... Wright's trains on the Rockville and Frederick pike" |

### 3. Entries LS-R1 did not locate: search families (7-8 Oct 2026)
Phrases (decoded wording): E21 "Van Vliet has chartered steamers", "double decked steam barges", "Helen Getty Metamora Champion";
E23 "commissioned to investigate only not to prosecute", "Solicitor Whiting gave his opinion"; E26 "42 Walker street", "disguised as
hardware stationery", "revolvers and ammunition imported recently"; E27 "Jewett and Siebert", "James Gemmell crossed the Potomac",
"supposed to be rebel agents", "Miss Gardner"; E28 "proxy of the sailors at the ensuing election", "disposal of the New York election
agents", "election agents"; E29 "Dudley Harris", "has a bull dog look", "snuffs up his nose", "tavern keeper Brooklyn". Run with
`tools/print_check.py` (scratch target; exact + proximity match on each djvu text) plus hand queries.

| family | searched | result |
|---|---|---|
| OR by date and correspondent, +/- 3 days (IA djvu, whole volume) | ser. I vols 33 (E21), 36 pt 2 (E21, E23), 37 pt 2, 39 pt 2 (E26), 42 pts 2-3, 43 pts 1-2 (E26-E29), 51 pt 1 | no hit for any E21/E23/E26-E29 phrase. Context only: I/33 p.915 prints Wise's report from Philadelphia, 19 Apr 1864, to Meigs (Matilda, Highland Light, Champion among the side-wheel boats); I/39 pt 2 p.295 prints Carrington, Indianapolis, 24 Aug 1864: 400 revolvers and 135,000 rounds seized at Dodd's office, "large invoices of arms are en route, variously disguised" |
| OR ser. II (political prisoners, Aug 1864 onward) | vols 7 and 8 (IA `warofrebellion0207rootrich`, `0208rootrich`): phrases and Gemmell, Dudley Harris, Jewett, Siebert, Massie, Hawthorne, Olcott, Biggs, Van Vliet, Walker St; Dix correspondence pp.69, 441, 501 read | no hit (Olcott hits are Lt. Col. E. Olcott, a different man) |
| OR ser. III vol. 4 | IA `warofrebellionco0004genf`, all phrases | only E24 (above) |
| ORN | ser. I vol. 26 (Western Waters, 1864) | only E22. Context for E28: Pennock as Fleet Captain commanding at Mound City, Porter absent at Perth Amboy, N.J., Sept 1864 |
| Sender/recipient papers | Confidential Correspondence of G. V. Fox vols 1-2 (E23); Diary of Gideon Welles vol. 2 (E22/E23/E28); Life of Thurlow Weed vol. 2, Barnes memoir (E28); Memoirs of John Adams Dix vol. 2 (E26, E29); Butler, Private and Official Correspondence vol. 4 (E21, Biggs was Butler's chief QM) -- all IA djvu, every phrase | no hit |
| PUSG / Lincoln Collected Works | not searched by text: no E21/E23/E26-E29 sender or addressee is Grant or Lincoln, and no phrase hit in the IA-wide search (which covers the IA copies of both) | not applicable by correspondent |
| Huntington full text (CONTENTdm p16003coll11, `CISOSEARCHALL`) | Gemmell, "Dudley Harris", "Thurlow Weed", Siebert, "Walker St", Olcott, "Van Vliet" | Gemmell, Dudley Harris, Thurlow Weed, Siebert: only the ledger's own pages (9091, 9115). "Walker St" also on 1862 pages (8176-8202, 9392-9393): E. J. Allen (Pinkerton), 43 Walker St -- unrelated. No plain copy of any of the six |
| Zooniverse Talk snapshot (sources/talk) and the solver repositories' local snapshots (sources/cyphersolver) | the same names | no hit |
| IA full text, all items (be-api fts) | every phrase above | no hit bearing on these telegrams (hits are unrelated: law reports, yearbooks, directories) |
| Google Books API (key, country=US) | every phrase; plus Gemmell "Old Capitol" 1864; "Dudley Harris" Portland rebel; Olcott "navy yard" Fox Whiting 1864; Weed Pennock sailors vote 1864; Dix "Walker street" arms Indiana 1864; Biggs Meigs "Van Vliet" steamers April 1864; Turner "Judge Advocate" Jewett Siebert; Massie Hawthorne Dix arrest November 1864 | **E29: hit.** Mason Philip Smith, *Confederates Downeast* (1985), snippet: "Dudley Harris, who used the aliases Spencer and Barbour. Harris, a relative of Colonel Martin in Boston, operated in Portland, Maine. He was about 35 to 40 years old. Jones said he had '... a bulldog look; snuffs up his nose ...'"; James D. Horan, *Confederate Agent* (1954; 2015 reprint), snippet: "He [Jones] reports their names and stations as follows: 'Portland, Me. ... Major Dudley Harris'". E21: only OR context (Van Vliet, QM New York, 5 Apr 1864). Nothing for E23, E26, E27, E28 |
| OpenAlex (key), CrossRef | every phrase | no relevant hit |
| Semantic Scholar | blocked: HTTP 429 on the first call, not retried in a loop | unreachable this session |
| CORE (key) | "Dudley Harris" Portland 1864; "Walker street" revolvers 1864 Dix; Olcott "navy yard" 1864; "Thurlow Weed" sailors vote 1864 Pennock | no relevant hit |
| JSTOR | 10 rows appended to JSTOR-QUEUE.tsv (families i and ii, E21, E23, E26, E27, E28) | pending (never blocks) |
| Unreachable / unread | NARA RG 107 (M473 telegrams sent by the Secretary of War, M504), RG 92 (Meigs's letter books), RG 45 (Navy), RG 59 (State); Stanton Papers (LoC); Weed Papers (Rochester); Dix Papers (Columbia); Fox Papers (NYHS); Olcott's 1864 Navy Yard reports (congressional documents not searched page by page); New York newspapers Aug-Nov 1864; the Supplement to the OR; HathiTrust full text | unread |
Requests: archive.org 52 (19 djvu downloads by print_check, 11 advancedsearch, 22 metadata), be-api.us.archive.org 40,
www.googleapis.com 35, api.openalex.org 20, api.crossref.org 20, api.semanticscholar.org 1 (429), api.core.ac.uk 4,
hdl.huntington.org 13 (2 IIIF images, 7 CONTENTdm searches, 4 item infos); reachability probes: Cornell MOA 2 (search now
redirects to HathiTrust), quod.lib.umich.edu 1 (403), babel.hathitrust.org 1 (403).

### 4. Classification (key `period` for all nine)
| ID | N-class | text known? | depth | depth_pct | check |
|---|---|---|---|---|---|
| E21 Meigs to Biggs, 19 Apr 1864 | **N3** | unknown | D4 | 100 (37/37 H) | image (LS-R1), fresh re-derivation (here), OR I/33 p.915 Wise's 19 Apr report from Philadelphia names Matilda, Highland Light and Champion, the vessels the decode lists |
| E22 Welles to Porter, 26 Apr 1864 | N1 | known (ORN I/26 p.92) | D4 | 100 (21/21 H) | word for word with the print |
| E23 Fox to Olcott, 2 May 1864 | **N3** | unknown | D3 | 100 (7/7 H) | image (LS-R1), re-derivation; no external print check of a decoded value made here |
| E24 Seward to Adams, 18 May 1864 | N1 | known (OR III/4 p.392) | D4 | 100 (9/9 H) | word for word with the print |
| E25 Halleck to Wallace, 29 Jul 1864 | N1 | known (OR I/37 pt 2 p.501) | D3 | 94.1 (13 H + 3 C of 17; 1 M) | print agrees but for "pike" (M) |
| E26 Stanton to Dix, 21 Aug 1864 | **N3** | unknown | D4 | 100 (24/24 H) | image crop checked here word for word; OR I/39 pt 2 p.295 (Indianapolis seizure, arms "variously disguised") independently agrees with "a portion was seized last night in Indianapolis" and "it may be disguised" |
| E27 Turner to 'beverage', 10 Oct 1864 | **N3** | unknown | D3 | 93.3 (14/15 H, 1 M; the addressee word "beverage" is outside the book, a name code) | image (LS-R1), re-derivation |
| E28 F. W. Seward to Weed, 11 Oct 1864 | **N3** | unknown | D3 | 100 (15/15 H, one flagged "Pilgrim[?]" = Captain) | image (LS-R1), re-derivation; ORN I/26 Sept 1864 (Pennock commanding the station, Porter absent) fits the decoded "in temporary command"; held at D3 because the flagged token was not re-checked on the image here |
| E29 Dana to Dix, 5 Nov 1864 | **N2** | content and distinctive wording in print | D4 | 100 (33/33 H) | image crop checked here; Confederates Downeast (1985) quotes the same description ("a bulldog look; snuffs up his nose"), aliases and Colonel Martin from the informant Jones's report |

- **N3 (E21, E23, E26, E27, E28)**: no prior plaintext or decipherment located after the logged search. Not N4: the series where each
  telegram's text would most likely be kept or printed (NARA RG 107/92/45/59, the senders' and recipients' papers, the 1864 New York
  press, HathiTrust full text) are unread, and JSTOR rows are pending. Safe sentence (each): "Read at grade H with the period Cipher
  No. 1 book; no prior decipherment or printed text located in the Official Records (ser. I, II, III and the Navy series by date and
  correspondent), the senders' and recipients' printed papers, the Huntington collection's full text, Internet Archive full text, Google
  Books, OpenAlex, CrossRef or CORE (searched 7-8 Oct 2026)." Unsafe: "first", "unpublished", "never printed", "unknown telegram".
- **E29: N2**, not N3. The decoded description is in print (Smith 1985, quoting Jones; Horan 1954 prints Jones's list with "Major
  Dudley Harris" at Portland); whether either quotes Dana's telegram itself or only Jones's report behind it is not established. No prior
  mapping of this ciphertext to that text was found. Safe: "Read at grade H with the period book; its content, including the wording of
  the description, is printed in Smith, Confederates Downeast (1985), from the informant's report." Not counted.
- **E22, E24, E25: N1** (independent re-decipherments of printed texts). Not counted.
- Depth sentences (D2+ each, checked against the derived block):
  E21 "The Quartermaster-General tells Lt. Col. Biggs at Fort Monroe that three ferry boats and three tugs leave Washington at once,
  and that Captain Wise and Major Van Vliet have chartered side-wheel steamers, propellers, tugs and barges, all ordered to Fort
  Monroe." E23 "Assistant Secretary Fox tells Olcott he is commissioned to investigate the New York Navy Yard only, not to prosecute,
  which the Secretary of the Navy will do." E26 "Stanton orders Dix to search No. 42 Walker Street, New York, for revolvers and
  ammunition imported for Copperheads in Indiana, some of which was seized at Indianapolis the night before." E27 "Judge Advocate
  Turner reports that two men, Jewett and Siebert, came from Richmond the week before and are supposed to be rebel agents, and that
  James Gemmell, who crossed the Potomac with them, is in the Old Capitol." E28 "Frederick Seward tells Thurlow Weed that Captain
  Pennock, in temporary command of the Mississippi Squadron, will put a boat at the disposal of the New York election agents to take
  the sailors' votes or proxies."

### 5. Postmortem
- No over-claim found in LS-R1's section or reading.md: every not-located entry is worded as "not located in" a named source, and
  E29 already says its content is in print. One gap filled: E24's page (OR III/4 p.392), carried into reading.md's summary row.
- One understatement noted, not a correction: LS-R1 did not search OR ser. II or the sender/recipient papers; both are done here
  and changed nothing for the N3 five.
- E29 should not be read as an unlocated text in any outward line: its description is in print (section 4).
- status.json: one result row per N3 entry (E21, E23, E26, E27, E28); SECOND-OPINIONS-QUEUE.tsv rows SO-ECKERT-E21, -E23, -E26, -E27,
  -E28 with prompts in second-opinions/.

## AUDIT 2 (second adversarial, AUD2-LS-A)

Verifier AUD2-LS-A (account 4, session_01LV7WeHWhnyLBant2EkbE1k, for the account-3 orchestrator), 8 Oct 2026, 00:39-00:5x UTC by
`date -u`. Scope: **E21, E23, E26** only (the three of LS-V1's five N3 entries in brief runs/2026-10-08-acct3-aud2-ls.md part A). A
separate session from the solver (LS-R1) and the first auditor (LS-V1); tried to find each text in print, not to confirm LS-V1.

### 1. Re-derivation and image check
- `python3 ciphers/eckert-1864/decode.py --check`: "reading.md is current", exit 0.
- 2400 px IIIF images of pointers 8934, 8935, 8955, 9053 (scratch, not committed), entry regions cropped with PIL and read by eye:
  E21 (p.42 bottom "Geo D. Sheldon Ft Monroe, Washington Apl 19th 1864" through p.43 "Egg Belcher"), E23 (p.63 "Horner, Wash. May 2
  1864 9 PM", "Rosalie for paradise H. S. Ol- cott Frog ... Sig G. Fox Asst buxton") and E26 (p.159, at quarter scale; LS-V1 had
  already checked it word for word) agree with ciphertext.txt. E23's seven code words (Rosalie, paradise, Frog x2, Burton, wick,
  buxton) are those the reading grades H.
- E21 "Will chart her Warrior": "Warrior" is a vessel name, not an unread code word -- the sibling Cipher No. 9 telegram in
  reading-no9.md has Meigs telling Van Vliet to "Charter the Warrior and the double decked propellers". Counts unchanged.

### 2. Families LS-V1 did not cover, searched here (8 Oct 2026)
| family | searched | result |
|---|---|---|
| 1864 press (LS-V1: "New York newspapers Aug-Nov 1864 unread") | IA full text (be-api) `"No. 42 Walker"`, `"42 Walker street"`; loc.gov Chronicling America `"42 Walker" revolvers` 1864 (6 pages); NY Herald 24 Aug 1864 p.4 OCR (loc.gov ALTO full text); Philadelphia *Press* 24 Aug 1864 and *New-York Weekly Tribune* 3 Sep 1864 djvu text (IA `per_the-press_the-press_1864-08-24_1`, `newyorkweekly18640903gree`) | **E26: substance in print.** NY Herald 24 Aug 1864 p.4: "Thirty-two cases, each containing from four to six dozen revolvers, of the Savage Arms Company patent, stored at No. 42 Walker street, were seized on Monday by Marshal Murray. It is stated that these revolvers were part of a lot purchased in this city for the Sons of Liberty in Indiana. The cases were marked 'Stationary.' A quantity of similar arms had been sent from the same store to Indianapolis, where they were also seized." The *Press* and the Weekly Tribune ("were stored at No. 42 Walker-street, where the seizure took place, awaiting shipment") print the same report; Chronicling America also lists the NY Daily Tribune 24 Aug, Davenport Democrat 24 Aug, Ottumwa Courier 25 Aug and Burlington Hawk-Eye 27 Aug 1864 pages (not opened). None prints Stanton's order or says it came from the War Department. E21, E23: nothing |
| Olcott's own account and the Navy Department's (E23) | Olcott, "The War's Carnival of Fraud", *Annals of the War* (1879; IA `annalsofwar00philrich`, whole essay): quotes Fox's letter of 18 Feb 1864 to "Colonel H. S. Olcott, Special Commissioner, Navy Department" and Stanton's of 21 May 1864, not the 2 May telegram; Fox's letter to Welles communicated to the Senate, March 1865 (*Rebellion Record* vol. 9, IA `rebellionrecord09moor`, Doc. on Olcott): narrative only; Google Books snippets of House Misc. Docs 1876 (Navy Department investigation, Olcott/Veeder papers) and *American Secretaries of the Navy* (1980) | no hit for "investigate only", "not to prosecute", "Solicitor Whiting", "Do not proceed against". The 1876 House Misc. Doc. was seen only in snippet (Olcott's reports of 1864-65 printed there), not read through: unread |
| OR ser. I vol. 33 read through (E21) | IA `warofrebellion33unit` djvu, every occurrence of Van Vliet, Biggs, Highland Light, Getty, Metamora, Leary, double-decked | context only: p.915 Wise's Philadelphia list of 19 Apr (Matilda, Highland Light, Champion among 17 side-wheel boats) and Meigs to Wise of 16 Apr; no George Leary, Helen Getty, Metamora, Richland, no double-decked barges, no Meigs-to-Biggs of 19 Apr. Annual Report of the Secretary of War / QMG 1865 (Google Books snippets) list Helen Getty and Highland Light among chartered vessels: vessel data, not the telegram |
| Secondary studies (Sons of Liberty, Navy Yard frauds, Meigs) | Google Books (key, country=US): `"Walker street" revolvers Indianapolis 1864` (hits: Stidger *Treason History* 1903, Klement *Dark Lanterns* 1989, *Democratic Opposition to the Lincoln Administration in Indiana* (1973) -- snippets about the Indianapolis seizure, no Walker St order), `"Indianapolis" "marked stationery" 1864` (Ayer, *The Great Treason Plot in the North*, 1895: Indianapolis testimony), Towne/Surveillance, Olcott Fox Navy Yard, Meigs Biggs Van Vliet April 1864, "Helen Getty" steamer 1864, Metamora "Highland Light" 1864 | no printed text of E21, E23 or E26 |
| Semantic Scholar (LS-V1: 429) | key, 3 queries (Olcott Navy Yard 1864; Sons of Liberty arms New York 1864 Walker Street; Meigs transports Fort Monroe April 1864) | 2 answered 200, nothing relevant; third 429, not retried |
| IA full text, all items, fresh quoted phrases | "Van Vliet has chartered", "double-decked steam barges", "three ferry boats and three tugs", "Helen Getty" Metamora Champion, "not to prosecute" Olcott, Olcott "Solicitor Whiting" (hits only Welles diary, read by LS-V1), "Olcott were temporarily obtained" | no text of E21, E23, E26 |
| JSTOR-QUEUE.tsv | rows 327-332 (LS-V1) cover E21, E23, E26 in families (i) and (ii) | pending, never blocks; no row added |
| Unreachable / unread | NARA RG 107 (M473), RG 92, RG 45; Stanton, Dix, Fox, Meigs manuscript papers; House Misc. Doc. 1876 read through; chroniclingamerica.loc.gov OCR host (403; the loc.gov ALTO route worked); HathiTrust full text; the Supplement to the OR | unread |
Requests: be-api.us.archive.org 12, archive.org 9, www.googleapis.com 16, api.semanticscholar.org 3, www.loc.gov 2, tile.loc.gov 1,
chroniclingamerica.loc.gov 2 (403), hdl.huntington.org 4 (IIIF images).

### 3. Classification (key `period` for all three)
| ID | LS-V1 | AUDIT 2 | depth | why |
|---|---|---|---|---|
| E21 Meigs to Biggs, 19 Apr 1864 | N3 | **N3 (kept)** | D4 kept, 100 (37/37 H) | no printed text; OR I/33 p.915 prints Wise's Philadelphia list, which the telegram summarises in part (Matilda, Highland Light, Champion), but not the telegram, Van Vliet's New York charters (George Leary, Helen Getty, Metamora, Richland, Warrior) or the double-decked cattle barges. Image re-checked here |
| E23 Fox to Olcott, 2 May 1864 | N3 | **N3 (kept)** | D3 kept, 100 (7/7 H) | Olcott's own 1879 account and Fox's 1865 Senate letter, the two places it would most likely be quoted, do not quote it. Image re-checked here. Not raised to D4: no external check of a decoded value |
| E26 Stanton to Dix, 21 Aug 1864 | N3 | **N2 (lowered)** | D4 kept, 100 (24/24 H) | the order's whole substance is in the 1864 press: arms bought for the Sons of Liberty in Indiana stored at No. 42 Walker Street awaiting shipment, the cases marked "Stationary", a portion sent from the same store and seized at Indianapolis, the 22 Aug seizure by Marshal Murray (NY Herald 24 Aug 1864 p.4 and others). Stanton's wording is not printed, so this is the E29 kind of N2 (content in print, the telegram itself not located), not N1 |

- **E21, E23 safe sentence (each)**: "Read at grade H with the period Cipher No. 1 book; no prior decipherment or printed text located after
  two independent searches (7-8 Oct 2026) of the Official Records, the senders' and recipients' printed papers and accounts, the
  Huntington collection's full text, Internet Archive full text (newspapers included), Google
  Books and the open scholarship indexes." Unsafe: "first", "unpublished", "never printed", "unknown telegram". Not N4: NARA RG 107/92/45,
  the manuscript papers and HathiTrust full text are unread and JSTOR rows are pending.
- **E26 safe sentence**: "Read at grade H with the period Cipher No. 1 book: Stanton's order to Dix to search No. 42 Walker Street; the
  seizure it led to, and the facts the order gives, were reported in the New York press on 24 August 1864." Unsafe: "unknown order",
  "previously unread", any outward line that presents the arms at 42 Walker Street as new. **Not counted** (below N3).
- Depth sentences: LS-V1's stand for E21 and E23 (checked here against the image). E26's stands as written and is now also
  externally checked against the NY Herald 24 Aug 1864 p.4 (address, Indiana, "Stationary", Indianapolis seizure).

### 4. Postmortem
- One over-claim corrected: E26 was N3 because the 1864 New York press was on LS-V1's own unread list; the press search took four
  requests. The phrase searches missed it because the papers print "No. 42 Walker-street" / "No. 42 Walker street" while the queries
  were "42 Walker street" next to decoded words such as "revolvers". Lesson: for a telegram about an event that would have been
  public (an arrest, a seizure, a raid), search the press for the event (place and date, the number and street) before setting N3,
  not only the telegram's wording.
- status.json: E21, E23 rows `audit_status` "two audits"; E26 row grade N2, `audit_status` "two audits", not counted.
  SECOND-OPINIONS-QUEUE.tsv: SO-ECKERT-E26 withdrawn (N2); its prompt's context line names the Herald report. SO-ECKERT-E21 and -E23
  unchanged (class and counts unchanged). reading.md summary row for E26 notes the Herald report (decode.py --check still exit 0).

## AUDIT 2 (second adversarial, AUD2-LS-B)

Verifier AUD2-LS-B (account 4, for the account-3 orchestrator, brief `.claude/briefs/runs/2026-10-08-acct3-aud2-ls.md`), 8 Oct 2026,
00:41-00:5x UTC by `date -u`. This session is separate from the solver (LS-R1) and the first auditor (LS-V1) and does not protect
either one's conclusions. Two entries: **E27** (Judge Advocate L. C. Turner to 'beverage', 10 Oct 1864) and **E28** (F. W. Seward to
Thurlow Weed, 11 Oct 1864 11.30 AM), both mssEC 19 p.197, pointer 9091. Nothing was decoded beyond re-running the committed script.

### 1. Re-derivation (rule 7) and image check
- `python3 ciphers/eckert-1864/decode.py --check`: "reading.md is current", exit 0.
- Image: `hdl.huntington.org/digital/iiif/p16003coll11/9091/full/2400,/0/default.jpg` (scratch, not committed);
  `python3 tools/iiif_lines.py --image $S/img/p9091.jpg --out $S/crops --prefix p9091 --region 0,200,2400,1800 --centres
  50,150,...,1750 --lines-per-crop 3 --max-width 1800` (6 bands x 2 segments), plus two hand crops of the E28 opening line
  (x 1000-2300, y 1310-1440). Every E27 line (header "Horner N.Y. No. 1 Washn. Octo. 10. 1864" through "L C Turner Judge Advo.")
  and every E28 line (header "Horner N.Y. No 1 Washn Oct 11th 1864" through "F W Seward Asst Byron") agrees word for word with
  ciphertext.txt. The token LS-R1 flagged as "Pilgrim[?]" is clearly written **"Pelgrim"** on the image: a clerk's misspelling of the
  book word Pilgrim = Captain (key.md p.18 l.26 R). Pennock's rank is Captain in ORN I/26 throughout 1864 ("Captain A. M. Pennock,
  U. S. Navy"), so the reading is confirmed independently. "Grunt" (E27) is clearly "Grunt" on the image, not a misread of Growl. The
  M grade stands, since the book gives Warrenton and the telegram was sent from Washington.

### 2. Families LS-V1 section 3 did not cover, searched here (8 Oct 2026)
| family | searched | result |
|---|---|---|
| `tools/print_check.py` fresh phrase pass (scratch target, 10 phrases: E27 "Jewett and Siebert came from Richmond", "supposed to be rebel agents", "James Gemmell crossed the Potomac", "is now in Old Capitol", "A Miss Gardner was with them", "she was going to Norwich"; E28 "in temporary command of the Mississippi squadron", "at the disposal of the New York election agents", "receive the vote or proxy of the sailors", "all the facilities will be furnished by the naval officer") | listed: F. W. Seward, *Seward at Washington* vol. 3 1861-72 (IA williamhsewardau03sewa); F. W. Seward, *Reminiscences of a War-Time Statesman* 1916 (reminiscencesofw00sewauoft); Benton, *Voting in the Field* 1915 (votinginfieldfor00bent); L. C. Baker, *History of the U.S. Secret Service* 1867 (historyofuniteds00bake); Williamson, *Prison Life in the Old Capitol* 1911 (prisonlifeoldcap00willrich); Bates, *Lincoln in the Telegraph Office* (lincolnintelegra00bates); ORN I/26; OR II/7. Unasked: IA full text (all items), Google Books, OpenAlex, CrossRef | no hit in any listed source. IA-wide and Google Books hits checked by snippet: "in temporary command of the Mississippi Squadron" appears only in Garrison, *Unusual Persons of the Civil War* (1996) and *Ohio History* 107 (1998), both general accounts of Pennock, not this telegram. "is now in Old Capitol" appears in OR II/8 (Ingraham, 31 May 1865), another case. The rest are unrelated hits on common words |
| **Diary of Gideon Welles vol. 2** (IA diaryofgideonwel02welluoft, djvu read by date, not only by phrase) | entry of 11 Oct 1864 | **E28: content in print.** p.175: "October 11, Tuesday. The President and Seward called on me this forenoon relative to New York voters in the Navy. Wanted one of our boats to be placed at the disposal of the New York commission to gather votes in the Mississippi Squadron. ... directed commanders to extend facilities to all voters." LS-V1 searched this volume by phrase only, and the wording differs from the telegram's, so the entry was missed |
| **Abraham Lincoln Papers, LoC** (Knox College transcriptions, online since 1999; loc.gov JSON API) | Weed + Pennock; Weed + Seward + sailors + votes, 1864 | **E28: request and sequel in print online.** Thurlow Weed to Lincoln, New York, 10 Oct 1864 (mal3709900): "I am anxious about the vote of the Sailors on the Mississippi, and have written to Frederick Seward advising him to obtain a Government Steamer for our Agents to go from Cairo down the River to the different Gun Boats". The editors' note cites Welles's diary p.175 and *Collected Works* VIII p.43. J. Springsteed (a New York commissioner for the sailors' votes) to Weed, Cairo, 21 Oct 1864 (mal3747400), enclosed in Weed to F. W. Seward, 28 Oct 1864, says he "went up to Capt Pennocks Head Quarters Mound City". Neither quotes E28's text or names Pennock as the officer giving the boat |
| Lincoln Lore (IA abrahamlincolnsalinc_4; Google Books dates the issue 1979) | IA full text: Springsteed, Frederick Seward, Mississippi Squadron, Pennock | narrates the episode: Weed's request to Frederick Seward, Welles's 11 Oct entry, Springsteed at Cairo, the "squadron of fifty boats". No Pennock and no telegram text |
| *Collected Works of Abraham Lincoln* vol. VIII (IA collectedworksof0008royp_m9a6, volumeviiicollec0000unse; be-api full text, lending-only) | Pennock; "Thurlow Weed" AND sailors; Mississippi AND sailors AND vote; Welles AND "election agents"; "Navy vote"; "Frederick Seward" AND Weed AND October | no E28 text; p.43 (cited by the Lincoln Papers editors) could not be read page by page (lending-only) |
| ORN ser. I vol. 26 (IA officialrecordso0026unse djvu, read by date and correspondent, not only by phrase) | Pennock, Oct-Nov 1864; election, vote, proxy, Weed | no E28 text and no election traffic. **External check for E28:** S. P. Lee, Mound City, 2 Nov 1864 (p.541-542), refers to papers "sent to the Department by Captain Pennock while he was in command of this squadron", and Pennock reports directly to Welles in Sept 1864 (Mound City, 14 Sept 1864, near p.560). Both agree with the decoded "Captain Pennock ... of Cairo in temporary command of the Mississippi squadron" |
| Chronicling America (loc.gov collections API; chroniclingamerica.loc.gov now 308-redirects there) | 1864: Gemmell + "Old Capitol"; Jewett Siebert; Pennock sailors election Weed; Oct-Nov 1864: Gemmell; sailors vote Mississippi squadron New York | Gemmell 0; Jewett/Siebert 3 pages, unrelated; sailors' vote 47 pages (NY Herald 6 and 12 Nov 1864 and others), listed but not read page by page; none surfaced E27 or E28 text in the result descriptions |
| Huntington CONTENTdm (`CISOSEARCHALL`, page level, p16003coll11) | Pennock (16 pages), Jewett (5), Springsteed (0), "election agents" (1) | only the ledger's own p.197 (9091) for E27/E28. The other Pennock and Jewett pages (received and sent books 1862-64, e.g. 9414, 9515, 10249, 2727) are other telegrams. No plain copy of either entry |
| Google Books API (key, country=US), 6 further queries | "James Gemmell" 1864; Siebert Jewett Richmond "rebel agents" 1864; "Miss Gardner" Norwich Richmond 1864 Turner; Springsteed sailors votes Cairo 1864; "Frederick Seward" Weed Pennock sailors vote 1864; Pennock "Mississippi Squadron" "New York" sailors vote proxies 1864 | E27: nothing (other James Gemmells: Montana, Ontario, Clydesdale). E28: only Lincoln Lore (above) |
| CORE (key) | Gemmell AND "Old Capitol"; "Thurlow Weed" AND sailors AND vote AND 1864 | 0, 0 |
| Semantic Scholar (key) | one query | HTTP 429 at print_check's call and again on one retry after a pause; **unreachable** this session, not retried in a loop |
| JSTOR | rows 333-336 (LS-V1: family i for E27 and E28; family ii "Jewett and Siebert", "proxy of the sailors") read. Two family (ii) rows added: "gather votes in the Mississippi Squadron" (E28, the printed diary's own wording) and "James Gemmell" (E27) | pending (never blocks) |
| Unread / unreachable | NARA M797 (case files of investigations by Levi C. Turner and Lafayette C. Baker, RG 94), the most likely home of E27's subjects; RG 107 (M473); RG 59 domestic letters (E28); Weed and Seward Papers (Rochester); *Collected Works* VIII p.43 page image; HathiTrust full text; the 47 Chronicling America pages on the sailors' vote, not read page by page | unread |
Requests: hdl.huntington.org 7 (1 IIIF image, 6 CONTENTdm), archive.org 9 (advancedsearch 5, 2 djvu downloads, 1 metadata, + print_check 8),
be-api.us.archive.org 12 (+ print_check 30), www.googleapis.com 7 (+ print_check 10), www.loc.gov 7, tile.loc.gov 3, api.core.ac.uk 2,
api.semanticscholar.org 1 (429; print_check's 2 also 429), api.openalex.org 10 and api.crossref.org 10 (print_check).

### 3. Classification (key `period` for both)
- **E27: N3, held.** No prior plaintext or decipherment located after both audits' searches. Not N4: NARA M797 (the Turner-Baker
  investigation files, where Jewett, Siebert, Gemmell and Miss Gardner would be recorded), RG 107 and HathiTrust full text are
  unread, and Semantic Scholar was unreachable. Not lowered: nothing about these four people or the telegram was found in print.
  - **Depth: D3, held.** 14/15 code words H, 1 M ("Grunt": the book gives Warrenton, but the telegram was sent from Washington,
    confirmed on the image). The addressee word "beverage" is outside the book (a name code). D4 needs every cipher-letter token
    H/C/S, so the M token blocks D4 until a period source settles "Grunt". depth_pct 93.3 unchanged. Outward words: "largely
    deciphered (about 93%)".
  - Safe sentence: "Read at grade H with the period Cipher No. 1 book (one place word M, the addressee code unread); no prior
    decipherment or printed text located in the Official Records (ser. I, II, III and the Navy series), the senders' and recipients'
    printed papers, F. W. Seward's and L. C. Baker's memoirs, the Old Capitol prison memoirs, the Lincoln Papers, Chronicling America,
    the Huntington collection's full text, Internet Archive full text, Google Books, OpenAlex, CrossRef or CORE (searched 7-8 Oct
    2026, two audits)." Unsafe: "first", "unpublished", "never printed", "unknown rebel agents".
  - Depth sentence (unchanged, checked against the derived block): "Judge Advocate Turner reports that two men, Jewett and Siebert,
    came from Richmond the week before and are supposed to be rebel agents, and that James Gemmell, who crossed the Potomac with
    them, is in the Old Capitol."
- **E28: lowered N3 -> N2.** The telegram's substance is in print: the Navy's decision to place a boat at the disposal of the New
  York commission gathering sailors' votes in the Mississippi Squadron, with facilities extended to voters. It is in Welles's
  *Diary* vol. 2 p.175 (11 Oct 1864, the day of the telegram, the decision it relays), in Weed's request to Lincoln of 10 Oct 1864
  naming Frederick Seward as the man asked (Lincoln Papers, annotated transcription), and in Lincoln Lore's account of the episode.
  This is the same shape as E29 (LS-V1) and E26 (AUD2-LS-A): content in print, no prior mapping of this ciphertext to it found. The
  telegram's own text and Pennock as the officer were not located in print. That is a search result and does not make the item N3.
  Not counted.
  - **Depth: D4 (raised from D3).** Rule 4a's D4 criteria, item by item: every cipher-letter token H (15/15); no residue; a
    non-statistical external check (the image agrees word for word, the flagged token is "Pelgrim" = Pilgrim = Captain, ORN I/26
    pp.541-542 has Captain Pennock in command of the squadron in autumn 1864, and Welles's diary and Weed's letter independently
    give the boat for the New York agents); and a fresh rule-7 re-derivation by a session other than the solver's (section 1).
    LS-V1 held D3 only because the flagged token had not been checked on the image. It has been checked here. Outward words:
    "deciphered". decode_status Decrypted.
  - Safe sentence: "Read at grade H with the period Cipher No. 1 book; the telegram's substance (a Mississippi Squadron boat for the
    New York agents collecting sailors' votes) is printed in the Diary of Gideon Welles (1911) vol. 2 p.175 and in the Lincoln Papers'
    transcriptions (Weed to Lincoln, 10 Oct 1864); the telegram's own wording was not located in print." Unsafe: "first",
    "unpublished", "unknown", "previously unread", or any N3 wording.
  - Depth sentence (unchanged, checked against the derived block): "Frederick Seward tells Thurlow Weed that Captain Pennock, in
    temporary command of the Mississippi Squadron, will put a boat at the disposal of the New York election agents to take the
    sailors' votes or proxies."

### 4. Postmortem
- Over-claim corrected: E28 was N3 in LS-V1 section 4, status.json and the SO-ECKERT-E28 prompt. The miss was a phrase-only search
  of a volume (Welles vol. 2) that LS-V1 did search. The diary paraphrases the decision rather than quoting the telegram, so the
  telegram's wording could not find it. The lesson matches AUD2-LS-A's for E26: when a telegram reports a decision or an event,
  read the obvious diary or edition **by date** for the event, and search the recipient's correspondence with the head of state
  (here the Lincoln Papers), before setting N3.
- Understatement corrected: E28 depth D3 -> D4 (section 3).
- status.json: E27 row `audit_status` "two audits", class, depth and line unchanged except the safe line's source list. E28 row grade
  N2 (`plaintext_novelty` N2, `mapping_novelty` N3), `audit_status` "two audits", depth D4, not counted.
  SECOND-OPINIONS-QUEUE.tsv: SO-ECKERT-E28 withdrawn (N2), and its prompt's context line names the Welles and Lincoln Papers prints.
  SO-ECKERT-E27 unchanged (class and counts unchanged).

## AUDIT (LS-V3)

Verifier LS-V3 (account 1, LANE ST-LEDGER, session_01Sg3MsAogd98jwqoVTLY6Mk), 8 Oct 2026, 01:10-02:0x UTC by `date -u`; a separate
session from the solver (LS-R3), not protecting its conclusions. Scope: LS-R3's entries **E37-E46** (mssEC 19, Cipher No. 1, key.md =
mssEC 41). Nothing decoded beyond re-running the committed script. Key source for every item: `period` (the War Department's own
Cipher No. 1 book).

### 1. Re-derivation (rule 7) and image spot-check
- `python3 ciphers/eckert-1864/decode.py --check`: "reading.md is current", exit 0. E37-E46 derived block: H 161, C 1 by the decoder,
  no hand regrading by LS-R3; checked here, accepted. Code words left unread and not graded by LS-R3 are counted here as unread tokens
  for depth: E37 "Wreath", E40 "nick", E43 "Waymorners" (one each).
- Strip crops from the 2400 px IIIF images (scratch, not committed): `python3 tools/iiif_lines.py --image $S/img/p9130.jpg --out
  $S/crops/9130 --prefix p9130 --region 100,1400,2250,480 --centres 50,147,244,341,438 --lines-per-crop 5 --max-width 2400`, the same
  with `--region 100,1850,2250,220 --centres 50,147 --lines-per-crop 2` for its last lines, and `python3 tools/iiif_lines.py --image
  $S/img/p9110.jpg --out $S/crops/9110 --prefix p9110 --region 100,1800,2250,900 --centres 60,157,...,836 --lines-per-crop 5
  --max-width 2400`. E46 (9130), all seven lines, and E37 (9110) lines 1-5 ("Grapes Eugenia Nov Peach for Princess Be F. Man = erie /
  Provost Mare shall Platina District Frog zebra Confidential zodiac You / had better imm'y with draw as a candid eight for / Congress
  or re sign as Provost Mare shall Pekin I") agree word for word with ciphertext.txt. One doubt, not a correction: E46's last-line
  first word, transcribed "youth", has a cut descender on the crop and could be "north"; it is a check/end word outside the plain text
  and changes no reading.

### 2. Entry LS-R3 located in print: page confirmed by script (a check, not a search)
| ID | printed at | how confirmed |
|---|---|---|
| E44 | ORN ser. I vol. 11 **p.68** ([Telegram.] Washington, November 16, 1864, Fox to Porter) | IA `officialrecordso0011unse` djvu: "See if you have any shaky steamer that will carry 300 tons. It will save time. Otherwise I will get a blockade runner. We will go on with this. General Butler left this evening and will cooperate. G. V. Fox", before the p.69 running head; word for word with the decode |

### 3. Entries LS-R3 did not locate: search families (8 Oct 2026)
Phrases (decoded wording): "withdraw as a candidate for Congress or resign as provost marshal", "I advise the former"; "remittance was
this day forwarded from Halifax", "Alex Keith Jr the rebel agent", "N. Ferris No. 10 North Market", "Gordon Bruce & Co", "Mitchell
Kenner & Co Montreal"; "Detain the schooner Princess", "Detain the Princess and her cargo"; "ask him to cooperate with you"; "winds and
waves control barges and sail vessels", "requisition for 100 saddle horses"; "City of Albany and Ranger left here today", "move cattle
and horses up the Pamunkey"; "every available steamer and propeller"; "chief conspirator for the burning of New York", "send on a man
to identify him". Run with `tools/print_check.py` (scratch target, `--only ia,ia-global,gbooks,openalex,crossref`), plus hand queries
by name and by event (AUD2-LS-A's lesson: search the press for the event, not only the decoded wording).

| family | searched | result |
|---|---|---|
| OR by date and correspondent, +/- 3 days (IA djvu, whole volume, regex on normalized text) | ser. I vols 33 (E42), 36 pt 3 (E43), 42 pt 3 (E45), 43 pt 2 (E45, E46); ser. II vols 7 and 8 (E38-E40, E46); ser. III vol. 4 (E37, E42) -- names Manierre, Keith, Ferris, Palfrey, Wakeman, Princess, Tassara, Evarts, Newport, Kennedy, Rucker, City of Albany, "chief conspirator", "superintendent of police", and every phrase | no hit for any E37-E43, E45, E46 telegram. Context only: I/36 pt 3 prints Biggs' answer of 30 May 1864 ("Tell General Rucker will return the City of Albany and Ranger soon as I can get hold of them", index p.367), which confirms the request in E43's last sentence but is not E43; I/43 pt 2 prints Butler's and Gordon's notes to John A. Kennedy, Superintendent of Police, New York, 7-11 Nov 1864 (E46's addressee and title); III/4 lists the steamer City of Albany p.916 (QMG report) |
| ORN | ser. I vol. 11 | only E44 (above) |
| Sender/recipient papers | Butler, Private and Official Correspondence vols 4-5 (E42, E43, Biggs was Butler's chief QM); William H. Seward autobiography/letters vol. 3 (E38-E41); Bates, Lincoln in the Telegraph Office (E38-E40, E44); Papers relating to Foreign Affairs 1864, 38th Cong. 2nd sess. (IA `papersrelatingto04unit`, E41); Headley, Confederate Operations in Canada and New York (1906, E46) -- all IA djvu | no hit for any telegram. Context: Bates prints the Dec 1863 Keith cipher letters intercepted by Wakeman "who had been instructed by the authorities to keep a sharp lookout for communications addressed to Keith" (the watch E38-E40 belong to, eight months later); Foreign Affairs 1864 prints the Arguelles correspondence (Tassara, Savage at Havana, F. W. Seward, April-May 1864), titles agreeing with E41's list -- the telegram's purpose is plausibly that affair, inferred, not checked |
| Contested-election record (E37) | Dodge vs. Brooks, House Misc. Doc., 39th Cong. 1st sess. (IA `unitedstatescon739offigoog`, `11037420bsb`) | **outcome in print, telegram not**: Brooks's notice of contest prints "B. F. Manierre was the republican candidate for Congress in the eighth district. As provost marshal of that district he had great influence ... You or your friends induced Mr. Manierre to retire"; witnesses are asked about "Mr. Manierre's ceasing to be a candidate". No mention of Fry or of any War Department telegram (no "Fry" in either copy) |
| 1864 press (loc.gov Chronicling America JSON, `www.loc.gov/collections/chronicling-america/?fo=json`, ALTO text via `tile.loc.gov`) | E37: "Manierre withdraw Congress" 1864 (7 pages); New-York Daily Tribune 1 Nov p.4, 3 Nov p.5, 4 Nov p.8 read in OCR; E38-E40: "schooner Princess" and "Keith Halifax letter remittance" Aug-Sept 1864; E46: "Old Capitol incendiary identify" Nov-Dec 1864; E41: Tassara Savage Havana Oct-Nov 1864 | E37: **New-York Daily Tribune, 4 Nov 1864, p.8, "Mr. Manierre Declines"** prints his withdrawal letter (New-York, Nov. 2, 1864, signed Benj. F. Manierre) recounting the negotiations with Dodge's committee and recommending support for "W. E. Dodge, the Union candidate for Congress"; it gives no War Department instruction (OCR scrambled across columns; read for Fry, provost, Washington, War Department: none). Other queries: section 3a |
| Huntington full text (CONTENTdm p16003coll11, `CISOSEARCHALL`) | Manierre, Keith, Ferris, Tassara, Wakeman, Palfrey, Newport, Kennedy | Ferris, Palfrey: only 9045 (E38-E39's page); Tassara: only 9097 (E41's page); Manierre: 0. Keith also on 9042 (p.149: 11 Aug 1864 to Wakeman, the watch on Keith's mail ordered), 9816-9817 and 9819 (pp.150-153 of another volume: Stanton to Gilpin, Dana to Walborn, 10-11 Aug 1864, "Spare no means to catch Keith who purchased the locomotives"; a 13 Aug follow-up to Wakeman on the Gordon Bruce & Co remittance) -- sibling telegrams of the same affair, not plain copies of E38-E40 |
| IA full text, all items (be-api fts) | every phrase; plus "Manierre" "candidate for Congress", "Alexander Keith" "rebel agent" Halifax, "schooner Princess" Halifax 1864, "chief conspirator" "Old Capitol", Tassara Savage Havana consul 1864; inside Larabee, The Dynamite Fiend (Keith's biography, `dynamitefiendchi0000lara`: Ferris, Princess, 1864) | no hit on any telegram; the Dodge vs. Brooks hit above; The Dynamite Fiend names Keith as the Confederate agent in Halifax in 1864, nothing on the August remittances (Ferris, Princess: 0) |
| Google Books API (key, country=US) | every phrase (print_check, top 10 each); hand: Manierre provost marshal Congress Dodge 1864; "Manierre" Fry withdraw; Keith Halifax remittance Ferris Boston 1864; "Alexander Keith" Halifax locomotives Seward; Keith "Gordon, Bruce"; "Old Capitol" "Evening Post" incendiary 1864; Tassara Savage Minor Havana Seward Evarts 1864; Rucker Biggs "City of Albany" Ranger Benham | no hit on any telegram (phrase queries return loose matches on common words); only the OR I/36 pt 3 Biggs reply (E43 context) |
| OpenAlex (key) | every phrase | no relevant hit |
| CrossRef | first phrases | 2 answered, no relevant hit; then HTTP 429, stopped (unreachable for the rest) |
| CORE (key) | "Alexander Keith" Halifax 1864 remittance; "Manierre" provost marshal 1864; "Tassara" Havana 1864 Seward; "schooner Princess" 1864; "Old Capitol" "burning of New York" 1864 | no relevant hit |
| Semantic Scholar (key) | 3 event queries | 2 answered, no relevant hit; 1 HTTP 429 |
| JSTOR | 8 rows appended to JSTOR-QUEUE.tsv (families i and ii: E37, E38-E40, E41, E42, E46), commit 7b8c2fa6 | pending (never blocks) |
| Unread / unreachable | NARA RG 107 (M473 telegrams sent by the Secretary of War; Fry's Provost Marshal General letters sent, RG 110), RG 92 (Meigs, Rucker), RG 59 (State: Seward's domestic letters, M40), RG 60/21 (the Arguelles prosecution); Seward Papers (Rochester); Stanton Papers (LoC); New York Evening Post 28 Nov 1864 (E46's own reference); New York newspapers Aug 1864 page by page; HathiTrust full text | unread |

### 3a. Press queries by date window (loc.gov Chronicling America, `dates=` filter; pages read in ALTO OCR via tile.loc.gov)
| query, window | pages | result |
|---|---|---|
| "schooner Princess", 12-31 Aug 1864 | 0 | no hit |
| Keith Halifax letter remittance, 12 Aug-15 Sept 1864 | 1 (Chicago Tribune 3 Sept p.1) | read: an advertisement of Keith, Faxon & Co, Chicago; unrelated |
| Old Capitol incendiary identify, 28 Nov-15 Dec 1864 | 6; read Evening Star (Washington) 29 Nov p.2 and 1 Dec p.2, New York Herald 29 Nov p.4 | **E46's reference is in print, the telegram's fact is not**: the Evening Star of 29 Nov quotes "Last evening's N. Y. Post" (Monday 28 Nov): Superintendent Kennedy's detectives arrested a man holding the baggage of "the chief conspirator", who "is said to have left the city last night ... He is young and firm-looking and is believed to be a lieutenant in the rebel army" -- the description E46 names. The Herald of 29 Nov p.4 ("The phosphorus incendiaries in Washington") reports a suspect seen in Washington the week before. Neither, nor the Star of 1 Dec (Old Capitol committals: three of Mosby's men), says a suspect is held in the Old Capitol or that New York was asked to identify him |
| Tassara Savage Havana, Oct-Nov 1864 | 0 | no hit |

### 4. Classification (key `period` for all ten)
| ID | N-class | text known? | depth | depth_pct | check |
|---|---|---|---|---|---|
| E37 Fry to Manierre (and to W. E. Dodge), 2 Nov 1864 | **N3** | unknown (the outcome, Manierre's withdrawal in Dodge's favour, is in print: Tribune 4 Nov 1864 p.8; Dodge vs. Brooks) | D3 | 95.7 (22/23 H; "Wreath" unread) | image crop checked here (lines 1-5); the printed withdrawal letter of the same day agrees with the decoded instruction's outcome |
| E38 Seward to Palfrey, 12 Aug 1864 | **N3** | unknown | D3 | 100 (13/13 H) | re-derivation; Huntington 9042, 9816-9819 (sibling telegrams of 10-13 Aug on Keith's mail) and Bates (Wakeman's standing watch on Keith) agree with the decoded context |
| E39 Seward to Wakeman, 12 Aug 1864 | **N3** | unknown | D3 | 100 (22/22 H) | as E38; the 13 Aug follow-up on 9819 names the same Gordon Bruce & Co remittance |
| E40 Seward to Murray; Harrington to Barney, 13 Aug 1864 | **N3** | unknown | D3 | 92.3 (12/13 H; "nick" unread) | re-derivation; one flagged token "Seward[?]" in the signature |
| E41 F. W. Seward to C. A. Seward, 15 Oct 1864 | **N3** | unknown | D3 | 100 (10/10 H) | re-derivation; Foreign Affairs 1864 confirms the titles (Savage vice consul general at Havana, Tassara Spanish minister) |
| E42 Meigs to Biggs, 25 Apr 1864 | **N3** | unknown | D3 | 100 (28/28 H) | re-derivation; no external print check of a decoded value made here |
| E43 Rucker to Biggs, 29 May 1864 | **N3** | unknown (the reply, OR I/36 pt 3, 30 May, prints only that the two boats will be returned) | D3 | 95.2 (19 H + 1 C of 21; "Waymorners" unread) | re-derivation; OR I/36 pt 3 Biggs's reply of 30 May names City of Albany and Ranger and Benham's boats, as decoded |
| E44 Fox to Porter, 16 Nov 1864 | N1 | known (ORN I/11 p.68) | D4 | 100 (15/15 H) | word for word with the print |
| E45 Rucker to Newport, 29 Nov 1864 | **N3** | unknown | D3 | 100 (11/11 H) | re-derivation; header time conflict (Fanny = 11 AM vs 10.45) as LS-R3 says |
| E46 '? Govr' to John A. Kennedy, 30 Nov 1864 | **N3** | unknown (the Evening Post description it cites is reprinted in the Evening Star, 29 Nov 1864 p.2; the Old Capitol prisoner is not located) | D3 | 100 (9/9 H; the signature words "M wise well wily" unread, a name) | image crop checked here, all lines; OR I/43 pt 2 confirms Kennedy as Superintendent of Police, New York, Nov 1864 |

- **N3 (E37-E43, E45, E46)**: no prior plaintext or decipherment located after the logged search. Not N4: the series where each
  telegram would most likely be kept or printed (NARA RG 107/110/92/59, the Seward and Stanton papers, the 1864 New York press page by
  page, HathiTrust full text) are unread, and JSTOR rows are pending. Safe sentence (each): "Read at grade H with the period Cipher
  No. 1 book; no prior decipherment or printed text located in the Official Records (ser. I, II, III and the Navy series by date and
  correspondent), the senders' and recipients' printed papers, the Huntington collection's full text, the 1864 press through Chronicling
  America, Internet Archive full text, Google Books, OpenAlex or CORE (searched 8 Oct 2026)." Unsafe: "first", "unpublished", "never
  printed", "unknown telegram".
- **E37 is the weakest N3**: its outcome is printed (Manierre withdrew on 2 Nov 1864 and backed Dodge; Brooks's 1865 contest says
  Dodge's friends induced it). What is not located is the Provost Marshal General's instruction itself (withdraw or resign, "I advise
  the former") and its copy to Dodge. A second audit should read the contested-election testimony and the Tribune/Herald of 2-5 Nov 1864
  in full for a mention of Fry before this is counted; if the instruction is reported there, E37 drops to N2 (the E26 rule of AUD2-LS-A).
- **E46 is the second weakest**: the description it cites (the chief conspirator, young, believed a rebel lieutenant) is printed in the
  Evening Star of 29 Nov 1864 from the Evening Post of 28 Nov; that a man answering it was held in the Old Capitol on 30 Nov, and that
  Kennedy was asked to send a man to identify him, is not located. A second audit should read the Washington and New York press of
  30 Nov-10 Dec 1864 for the Old Capitol identification before this is counted.
- **E44: N1** (independent re-decipherment of a printed text; the date word Gas = 16 agrees with the ORN, the ledger header's 15th
  does not). Not counted.
- Depth sentences (D2+ each, checked against the derived block):
  E37 "The Provost Marshal General tells Capt. B. F. Manierre, provost marshal of the 8th District, New York, to withdraw at once as a
  candidate for Congress or resign as provost marshal, advising the former, and sends the same text to W. E. Dodge." E38 "Seward tells
  the Boston postmaster that a letter with a remittance from Alexander Keith Jr, the rebel agent at Halifax, is on its way to N. Ferris,
  10 North Market Street, Boston, and must be seized and sent to the State Department." E39 "Seward tells the New York postmaster to
  seize three remittances sent by Keith from Halifax -- to Ferris in Boston, to J. B. Hunter & Co and to Gordon Bruce & Co in New York,
  the last for Mitchell Kenner & Co of Montreal -- and to report on the addressees' business." E40 "Seward orders the U.S. Marshal at
  New York to detain the schooner Princess and her cargo, and the Acting Secretary of the Treasury orders the Collector to detain her
  and examine her cargo with the marshal's help." E41 "Frederick Seward sends C. A. Seward in New York the names and posts of W. T.
  Minor and Thomas Savage at Havana, William Hunter of the State Department and Tassara, the Spanish minister, and asks him to see
  Mr Evarts and ask his cooperation." E42 "Meigs tells Biggs that winds and waves hold up the barges and sailing vessels, that 1,000
  horses are being shipped, that his request for 100 saddle horses went to the Cavalry Bureau, and that he is to send for the mules."
  E43 "Rucker asks Biggs whether the coal for the York and Pamunkey has been sent, as it is needed at White House at once, and asks for
  the steamers City of Albany and Ranger back to move cattle and horses up the Pamunkey." E45 "Rucker tells Colonel Newport at
  Baltimore to send every steamer and propeller he can spare to Washington at once and to give their names." E46 "Kennedy, New York's
  police superintendent, is told that a man believed to be the chief conspirator of the attempt to burn New York, as described in
  Monday's Evening Post, is in the Old Capitol Prison, and asked to send someone to identify him."

### 5. Postmortem
- No over-claim found in LS-R3's section or reading.md: every not-located entry is worded as "not located in" a named source; E44's
  page and date were right. Understatements filled: LS-R3 did not search OR ser. II/III, the senders' papers, the press or the
  Huntington full text; done here and they changed no class, but they put E37's outcome in print (section 4).
- Rows: status.json one result row per N3 entry (E37, E38, E39, E40, E41, E42, E43, E45, E46); SECOND-OPINIONS-QUEUE.tsv rows
  SO-ECKERT-E37 ... -E46 (not E44) with prompts in second-opinions/. Requests: listed in the ROOM done line.

## AUDIT (LS-V4)

Verifier LS-V4 (account 1, LANE ST-LEDGER), 8 Oct 2026, 01:47-02:1x UTC by `date -u`; a separate session from the solver (LS-R4),
not protecting its conclusions. Scope: LS-R4's entries **E47-E54** (mssEC 19, Cipher No. 1, key.md = mssEC 41). Nothing decoded
beyond re-running the committed script. Key source for every item: `period` (the War Department's own Cipher No. 1 book).

### 1. Re-derivation (rule 7) and image spot-check
- `python3 ciphers/eckert-1864/decode.py --check`: "reading.md is current", exit 0. E47-E54 derived block: H 104, C 1 by the decoder;
  LS-R4's hand grade I 1 (E47 "Vintur" = Vinton, Quartermaster) accepted, and now supported by a second ledger copy (section 3, E47).
  Words left unread and not graded by LS-R4 are counted here as unread tokens for depth: E50 "amirs", "ham"; E54 "Toby" (one each);
  E48 "Season" (addressee name word). "zbra" (E51) is the period word zebra and counts as read.
- Strip crops from the 2400 px IIIF images (scratch, not committed): `python3 tools/iiif_lines.py --image $S/img/p9117.jpg --out
  $S/crops/9117 --prefix p9117 --region 100,2020,2300,640 --centres 50,148,246,344,442,540 --lines-per-crop 3 --max-width 2400` and
  `python3 tools/iiif_lines.py --image $S/img/p9135.jpg --out $S/crops/9135 --prefix p9135 --region 100,170,2300,820 --centres
  50,148,246,344,442,540,638,736 --lines-per-crop 4 --max-width 2400`. E52 (9117), all six lines, and E54 (9135), all eight lines,
  agree word for word with ciphertext.txt (header to signature; E54 "Kidnap's Oyster unity", "Toby landed", "Palsy chief" as
  transcribed). No correction.

### 2. Entries LS-R4 located in print: page confirmed by script (a check, not a search)
| ID | printed at | how confirmed |
|---|---|---|
| E48 | OR ser. I vol. 37 pt 1 **p.891** (Washington, May 5, 1864 -- 11.30 a.m., Halleck to Wallace) | IA `warofrebellion371unit` djvu: the telegram sits between the running heads 890 and 892; "Two more (four in all) regiments of Ohio militia have been ordered to report to you in Baltimore. Porter's regiment of New York Heavy Artillery will be held in readiness to take the field, either as artillery or infantry. H. W. HALLECK, Major-General and Chief of Staff." Word for word with the decode except "of Ohio militia" (no ledger word). The ledger's signature code word reads "General-in-Chief" by the key; the print signs Halleck as Chief of Staff (May 1864), so the key value is the office word, not Halleck's title that day |
| E53 | OR ser. III vol. 4 **p.925** (Washington, D. C., November 12, 1864, to Maj. W. R. Price, Acting Inspector, Cavalry Bureau, Nashville) | IA `warofrebellionco0004genf` djvu: between the running heads 925 and 926; "Consolidation of the Second and Fifth Kentucky Cavalry approved. The Secretary of War authorizes enlistment of loyal Alabamians in the First Alabama Cavalry, but without bounties." signed (OCR "JORR ELCRON") Assistant Adjutant-General = J. C. Kelton; word for word. LS-R4's "page not fixed" is now fixed; the print's "W. R. Price" settles LS-R4's "R[?]" as R |

### 3. Entries LS-R4 did not locate: search families (8 Oct 2026)
Phrases (decoded wording): "Send Salvor to Annapolis", "not under engagements making the trip a serious loss"; "expedition sixteen
thousand strong", "removing stores and wounded to a new base"; "provision and water the Continental", "hour of sailing"; "accept
promptly without question the proposed", "greatly increased powers better advantages"; "calling himself Dr. Hamilton", "passed
through Elmira on his way south", "light hair, mustache and whiskers, and fine teeth"; "to hold these supplies on board vessel", "all
ordnance supplies which have been ordered for Sherman's army". IA full text and Google Books by script (scratch `q.py`), plus hand
queries by name and event.

| family | searched | result |
|---|---|---|
| OR by date and correspondent, +/- 3 days (IA djvu, whole volume, regex on normalized text) | ser. I vols 33 (E47), 35 pt 2 (`warofrebellion352unit`, Dept of the South: E47, E50), 36 pt 3 and 40 pt 2 (E49), 39 pt 3 (E51), 42 pt 2 (E50), 42 pt 3 (`warofrebellion423unit`, E54), 43 pt 2 (E52), 44 (E54); ser. III vol. 4 (all) -- names and words Salvor, Hilton Head + coal, sixteen thousand, 16,000 strong, new base or hospital, Continental + provision/water, hour of sailing, Whiton, Adna Anderson + inspector, inspector-generalship, Hamilton + Elmira, William/Dr. Hamilton + agent, fine teeth, Edson, "ordnance supplies which have been ordered", "hold these supplies", Arnold + Hilton Head | no hit for any E47, E49-E52, E54 telegram. Context only: I/33 prints a Fort Monroe reply "Will give Salvor eight days' coal and twelve of water" (the steamer at Biggs's disposal that spring); III/4 names W. H. Whiton "in charge of the office, Washington" of the U.S. Military Railroads (McCallum's report, index p.953) -- E51's signer; I/42 pt 3 prints Dyer to Butler, Dec 1864, "One hundred tons mining powder ... to Captain Edson, at Fortress Monroe, who is ordered to hold the same subject to your order" and Butler to Edson 4-5 Dec 1864 (E54's addressee and week, not E54); I/44 "Lieutenant Arnold goes to Hilton Head about the ordnance" (E54's Lt Arnold) |
| Huntington full text (CONTENTdm p16003coll11, `CISOSEARCHALL`) | Salvor, Whiton, Hamilton, Edson, Continental | **E47: a second ledger copy of the same telegram** at pointer 5595 ("Page 51" of another volume, headed "Ft Monroe April 6 . 1864 Geo D Sheldon": "Biggs vinton appian send Salvor to Ann a pole is if still at Animal & not under Engagements making the trip a serious loss unity order a purple tons of coal a float at appian if it can be spared to hill town head ..."), in cipher like mssEC 19; it is a second ciphertext witness, not a decipherment, and its "vinton" confirms LS-R4's I-grade repair of "Vintur". **E52**: siblings 9116 (p.222, 5 Nov 1864 11 PM to 'Season' at Baltimore; volunteer text, code words not decoded here: "William Hamilton is wicked on what seems trust worthy evidence asa walnut agent") and 9890 (5 Nov 1864, to 'Submit'; volunteer text: "... named walnut agent and the seizure of his papers Paradise Wm Hamilton") -- a William Hamilton named as a "walnut" (= rebel, as in E52) agent at Baltimore two days earlier; same affair by inference, not E52. Edson: 9902 (p.236, Dyer 1 Dec 1864, the mining powder, = the I/42 pt 3 text above) and 9903 (Dyer 3 Dec, sand-bags to Edson) -- siblings, not E54. Whiton: 9098 is E51's own page; Continental: 9042 is E50's own page |
| 1864 press (loc.gov Chronicling America JSON, `dates=1864-11-03/1864-12-15`) | E52: "Hamilton rebel agent Elmira" (6 pages), "Hamilton rebel agent arrested Baltimore" (168) -- result lists only | pages not read (budget); no title matched on its face. Unread, next step below |
| IA full text, all items (be-api fts) | every phrase above | 0 hits for each that answered; "not under engagements ...", "removing stores and wounded ...", "provision and water the Continental", "light hair, mustache ...", "all ordnance supplies ..." returned HTTP 502 (not retried: unreachable this session) |
| Google Books API (key, country=US) | every phrase above; hand: "ordnance supplies which have been ordered for" Sherman Edson; "hold these supplies on board" Arnold Hilton Head; Whiton "Adna Anderson" inspector 1864; Hamilton rebel agent Elmira 1864 Dana Wallace | no hit on any telegram (phrase queries return loose matches on common words). **E51 context**: Proceedings of the American Society of Civil Engineers (1888/1889), memoir of Adna Anderson: "from ... 1864, to July, 1866, he was Chief Superintendent and Engineer of all the [military railroads ...]", with Whiton on the memoir committee -- the outcome of the offer E51 urges him to accept is in print; the telegram is not (snippet only, page not read) |
| OpenAlex, S2, CORE, CrossRef | not run (lane cap nearly spent) | unreached this session |
| JSTOR | 5 rows appended to JSTOR-QUEUE.tsv (E51, E52, E54; families i and ii) | pending (never blocks) |
| Unread / unreachable | NARA RG 107 (M473 telegrams sent by the Secretary of War), RG 92 (Meigs, Quartermaster General letters sent), RG 156 (Ordnance, Dyer), U.S. Military Railroads records (RG 92); the Baltimore and Washington press of 3-15 Nov 1864 page by page (E52); the ASCE Anderson memoir page; HathiTrust full text | unread |

### 4. Classification (key `period` for all eight)
| ID | N-class | text known? | depth | depth_pct | check |
|---|---|---|---|---|---|
| E47 Meigs to Biggs, 6 Apr 1864 | **N3** | unknown | D3 | 92.9 (13 H + 1 I of 14) | re-derivation; a second ledger copy (Huntington 5595) agrees word for word in its plain words and gives "vinton" for the repaired code word |
| E48 Halleck to Wallace, 5 May 1864 | N1 | known (OR I/37 pt 1 p.891) | D4 | 100 (20/20 H; "Season" an addressee name word) | word for word with the print |
| E49 Meigs to Biggs, 12 June 1864 | **N3** | unknown | D3 | 100 (4/4 H; mostly in clear) | re-derivation; time word Julia = 4 PM agrees with the header 4.10 PM (LS-R4) |
| E50 Meigs to Biggs, 11 Aug 1864 | **N3** | unknown | D3 | 89.5 (17/19 H; "amirs", "ham" unread) | re-derivation; OR I/42 pt 2 prints the related order sending the Continental to Fort Monroe through Biggs |
| E51 Whiton to Adna Anderson, 21 Oct 1864 | **N3** | unknown (the outcome, Anderson's chief-superintendent post from 1864, is in print: ASCE memoir 1888/89) | D3 | 100 (11/11 H) | re-derivation; OR III/4 confirms W. H. Whiton in charge of the Military Railroads office, Washington |
| E52 Dana to Wallace, 7 Nov 1864 | **N3** | unknown | D3 | 100 (9 H + 1 C of 10) | image crop checked here, all lines; Huntington 9116 and 9890 (5 Nov, a "walnut agent" Wm Hamilton at Baltimore, volunteer text) agree with the decoded subject |
| E53 Kelton to W. R. Price, 12 Nov 1864 | N1 | known (OR III/4 p.925) | D4 | 100 (20/20 H) | word for word with the print |
| E54 Dyer to Edson, 5 Dec 1864 | **N3** | unknown | D3 | 90.9 (10/11 H; "Toby" unread) | image crop checked here, all lines; OR I/42 pt 3 and I/44 name Edson at Fort Monroe and Lt Arnold at Hilton Head on ordnance, same weeks |

- **N3 (E47, E49, E50, E51, E52, E54)**: no prior plaintext or decipherment located after the logged search. Not N4: NARA RG 107/92/156,
  the 1864 Baltimore/Washington press page by page, the ASCE memoir page, HathiTrust full text and the open scholarship indexes are
  unread, and JSTOR rows are pending. Safe sentence (each): "Read at grade H with the period Cipher No. 1 book; no prior decipherment or
  printed text located in the Official Records (ser. I and III by date and correspondent), the Huntington collection's full text,
  Internet Archive full text or Google Books (searched 8 Oct 2026)." Unsafe: "first", "unpublished", "never printed", "unknown telegram".
- **E51 is the weakest N3** (the E37 shape): Anderson's acceptance is printed in his ASCE memoir; the telegram urging it is not
  located. A second audit should read the memoir page (and McCallum's report in OR III/5) for a quotation of Whiton's message; if it
  is quoted, E51 drops to N2.
- **E52 is the second weakest**: the 5 Nov sibling telegrams name a rebel agent William Hamilton at Baltimore (inferred from their volunteer text, not decoded here); the
  press of 7-20 Nov 1864 (the six and 168 Chronicling America pages listed above) may report an arrest with this description. A
  second audit should read them before this is counted.
- **E48, E53: N1** (independent re-decipherments of printed texts). Not counted.
- Depth sentences (D2+ each, checked against the derived block):
  E47 "Meigs tells Biggs at Fort Monroe to send the steamer Salvor to Annapolis if she can be spared and to send coal afloat at Fort
  Monroe to Hilton Head, saying how much, so that he can replace it from the North." E49 "Meigs warns Biggs that an expedition sixteen
  thousand strong is to embark at White House the next day and tells him to send there every vessel fit to help, and to move stores
  and wounded to a new base or hospital." E50 "Meigs tells Biggs to provision and water the Continental, bring her from the Department
  of the South, and send her to Hilton Head with a dispatch the General-in-Chief is preparing, reporting her hour of sailing." E51
  "W. H. Whiton urges Adna Anderson, Government Railroads, Nashville, to accept the proposed inspector-generalship promptly, saying it
  is all right and carries greatly increased powers and better advantages." E52 "Dana tells Wallace at Baltimore that a rebel agent
  calling himself Dr Hamilton passed through Elmira going south on Thursday last, six feet two, with light hair, moustache and
  whiskers and fine teeth, and to catch him." E54 "Dyer, Chief of Ordnance, tells Capt. Edson at Fort Monroe to send at once to
  Hilton Head all ordnance supplies ordered for Sherman's army, and to write to Lt Arnold there to hold them on board until ordered
  where to land them."

### 5. Postmortem
- No over-claim found in LS-R4's section or reading.md: every not-located entry is worded as "not located in" a named source. Two
  understatements filled: E53's page (p.925) and E47's second ledger copy (5595), which LS-R4's Huntington-free search could not see.
  One reading note, not a correction: E48's signature code word gives the office "General-in-Chief" while the print signs Halleck as
  Chief of Staff; LS-R4's "Halleck (signed General-in-Chief)" is accurate as a transcription of the code word.
- Rows: status.json one result row per N3 entry (E47, E49, E50, E51, E52, E54); SECOND-OPINIONS-QUEUE.tsv rows SO-ECKERT-E47, -E49,
  -E50, -E51, -E52, -E54 with prompts in second-opinions/. Requests: listed in the ROOM done line.

## AUDIT 2 (second adversarial, AUD2-LS-D)

Verifier AUD2-LS-D (account 2, session_01STRHCzJtyQ9kBmyHiNY5Yk, for the account-3 orchestrator; brief
`.claude/briefs/runs/2026-10-08-acct3-ledger2.md`, shape of `runs/2026-10-08-acct3-aud2-ls.md`), 8 Oct 2026, 03:12-03:4x UTC by
`date -u`. Scope: **E42, E43, E45, E46, E47** only. This session is separate from the solvers (LS-R3, LS-R4) and the first auditors
(LS-V3, LS-V4). It tried to find each text in print and did not protect either audit's conclusion. Nothing was decoded beyond
re-running the committed script. Depth ruled under `.claude/briefs/runs/2026-10-08-acct3-depth-bar.md`.

### 1. Re-derivation (rule 7) and image check
- `python3 ciphers/eckert-1864/decode.py --check`: "reading.md is current", exit 0.
- 2400 px IIIF images `hdl.huntington.org/digital/iiif/p16003coll11/<ptr>/full/2400,/0/default.jpg` for 8945 (E42), 8975 (E43),
  9129 (E45), 8922 (E47) and 5595 (E47's second copy), in scratch, not committed. The entry regions were cropped with PIL and read by eye
  (E42 y 1880-2720, E43 y 290-1230, E45 y 1240-1900, E47 y 1880-2700, full width). LS-V3 and LS-V4 had checked none of these four
  pages; LS-V3 had checked E46 (9130) word for word, so it was not re-cropped here. Every line from header to signature agrees with
  ciphertext.txt. Notes, none of which changes a reading:
  - E42: the tail word is written "Benders", transcribed "Bender". It is outside the plain text.
  - E43: "Waymorners" is as transcribed. The line-end "Windsors[?]" runs into the gutter and stays uncertain.
  - E45: the header time "10 45 am" is written above "Sampson Balto.", so the "[?]" on the header time can go. The time word Fanny
    still gives 11 AM, the conflict LS-R3 noted. The twin message to "S H Beckwith City Pt" on the same page (10 am) has the same
    text and is not read.
  - E47: the page has a marginal "Sent from Book 4 PM", and its header reads 3.30 PM. Pencil glosses in a later hand sit above the
    header words ("again", "day", "8", "6", "small", "given", "4", "10", "2") and under the last line ("Run 3", "5", "was", "your",
    "9", "rush", "7", "once", "him", "here"). They sit over route and blind words, not plain text (NOTES.md already records them).
    They are not ledger text and not a decipherment of the message.

### 2. Families LS-V3 / LS-V4 did not cover, searched here (8 Oct 2026)
| family | searched | result |
|---|---|---|
| Butler, *Private and Official Correspondence* vols 4-5 (IA `privateofficialc04butl`, `privateofficialc05butl`, djvu whole volume, regex) -- LS-V3 read them for E42/E43, LS-V4 not at all (E47: Biggs was Butler's QM) | Biggs, Meigs, Rucker, Salvor, Hilton Head, coal, saddle, Cavalry Bureau, mules, City of Albany, Pamunkey, Newport, propeller, Kennedy, Old Capitol, Evening Post, by date +/- 3 days | no text of any of the five. Context for **E42**: Halleck to Butler, 21 Apr 1864, "One thousand horses will be sent to you in preference to all others" (vol. 4 p.112; also OR I/33), and Butler to the Secretary of War, 19 Apr, asking for "at least one thousand" cavalry horses, the shipment E42 reports under way |
| ORN ser. I vols 9, 10, 11 (North Atlantic) and 15 (South Atlantic, Hilton Head) -- not read by LS-V4 for E47, nor by LS-V3 for E43, E45 | same names and phrases | none. "Salvor" occurs only as "salvors" (a salvage claim) |
| OR read by date and correspondent again: I/33 (E42, E47), I/36 pt 3 (E43), I/42 pt 3 and I/43 pt 2 (E45, E46), III/4 | every Biggs, Rucker, Newport entry on 4-7 Apr, 23-27 Apr, 27-30 May, 27 Nov-5 Dec 1864 | no telegram of the five. **E47 context:** OR I/33 p.814 prints Biggs to Meigs, Fort Monroe, 6 Apr 1864 (received 1.30 p.m.): "Can spare a thousand tons coal, and have ordered it sail as soon as weather will possibly admit. Can spare more which is afloat ... Will give Salvor eight days' coal and twelve of water". It reached Washington before E47 was sent (header 3.30 PM, "Sent from Book 4 PM"), so it answers an earlier request. E47's "Purple" = 1,000 tons of coal is Meigs acting on that offer. The order to send Salvor to Annapolis and the coal's destination (Hilton Head) are not in it. **E45:** Rucker's correspondence in I/43 pt 2 is with J. G. C. Lee (27 Nov, Alexandria depot guards) and Whytal, nothing on steamers; no twin to City Point or Baltimore in I/42 pt 3 |
| 1864 press (loc.gov Chronicling America JSON, `dates=` window; page OCR via `tile.loc.gov` word-coordinates service), mandatory per entry | **E46**: `"Old Capitol" incendiary` and `conspirator "Old Capitol" New York fires`, 30 Nov-12 Dec 1864 (28 and 6 result pages listed). Read in OCR: NY Tribune 30 Nov pp.4-5, NY Herald 30 Nov p.4, Evening Star 5 Dec p.2, Phila. Evening Telegraph 3 Dec p.1, Cleveland Leader 30 Nov p.1, Worcester Spy 30 Nov p.2, and five weekly pages (Muscatine 2 Dec, Canton 5 Dec, Sunbury 3 Dec, Potter 7 Dec, Bradford 1 Dec). **E42**: horses shipped Fortress Monroe, 22-30 Apr (21 pages listed; NY Tribune 29 Apr p.1 and Nat. Intelligencer 28 Apr p.3 read for "Cavalry Bureau", "saddle horses", "winds and waves"). **E43**: `"City of Albany" Ranger`, 25 May-10 June (0). **E45**: steamers propellers Baltimore quartermaster, 28 Nov-5 Dec (5 pages, commercial; none on its face). **E47**: Salvor, 1-25 Apr (53 listed; Evening Star 21 Apr p.4 read) | **E46: no report located** of a suspect held in the Old Capitol or of a New York man sent to identify him. Read pages: the Old Capitol in these days holds Roger A. Pryor (NY Tribune and Herald 30 Nov), and the incendiary news is from New York (rewards, the Muscatine weekly's "one of the chief conspirators to burn the city has been arrested" -- in New York, an early report). E42, E43, E45: nothing. E47: Salvor appears only in the New York and Washington Steamship Company's advertisement (Evening Star 21 Apr p.4), the line's ships |
| Huntington CONTENTdm (`CISOSEARCHALL`, p16003coll11) | City of Albany, Pamunkey, Benham, "saddle horses", Newport, propeller, Old Capitol, conspirator, Salvor | object-level hits only (9302 = mssEC 19 itself, and 4849, 4953, 5952, 10074, 10550 and other volumes, which LS-V3/LS-V4 had already worked page by page for Salvor, Kennedy, Old Capitol); no plain copy of any of the five located. E47's second ledger copy (5595, LS-V4) was fetched and is a ciphertext witness, as LS-V4 says |
| `tools/print_check.py` fresh phrase pass (scratch target, 14 new phrases: E42 "every exertion is being made winds and waves", "referred to Cavalry Bureau which supplies saddle horses", "not sent here transportation enough for the infantry"; E43 "coal up the York and Pamunkey", "these two boats back here at once"; E45 "every available steamer and propeller you have", "ascertain at once and give names of those you send"; E46 "described in the New York Evening Post of Monday", "is in the Old Capitol prison send on a man to identify him"; E47 "Send Salvor to Annapolis", "order a thousand tons of coal afloat", "that I may replace it from the North", and others), listed sources Butler vols 4-5, ORN I/9, I/10, I/15 | no hit in any listed source; IA-wide 0; Google Books returns loose word matches only (checked by title and snippet); OpenAlex and CrossRef keyword searches give nothing relevant |
| Google Books API (key, country=US), 6 hand queries | `"Old Capitol" "chief conspirator" 1864`; `Kennedy "Old Capitol" identify incendiary 1864`; `"Salvor" Annapolis Meigs 1864`; `"City of Albany" Ranger Pamunkey Rucker`; `Rucker Newport "every available" steamer propeller 1864`; `"winds and waves" Meigs barges 1864 Biggs` | only the OR I/36 pt 3 Biggs reply (E43 context, known to LS-V3); Harper's Weekly 10 Dec 1864 has the incendiary plot in general (snippet). No text of the five |
| CORE (key) | `"Salvor" AND Annapolis AND 1864` (0); `Rucker AND Newport AND quartermaster AND 1864` (0); `"Old Capitol" AND "burn New York"` (HTTP 500, not retried) | nothing |
| Semantic Scholar (key) | three event queries (Meigs coal Hilton Head April 1864; Rucker steamers Baltimore Nov 1864; Old Capitol prisoner New York plot); print_check's call | HTTP 429 on every call; **unreachable** this session, not retried in a loop |
| JSTOR-QUEUE.tsv | existing: E42 "winds and waves control" (ii), E46 "chief conspirator" AND "burning of New York" AND "Old Capitol" (i). Added: E42 (i); E43 (i) and (ii); E45 (i) and (ii); E46 (ii); E47 (i) and (ii) | pending (never blocks) |
| Unread / unreachable | NARA RG 92 (QMG letters and telegrams sent: Meigs, Rucker), RG 107 (M473), RG 393 (Dept of Washington, Old Capitol prison records, E46's sender), the NY Evening Post itself (not in Chronicling America), Kennedy's police papers; Meigs Papers (LoC); HathiTrust full text; Semantic Scholar | unread |
Requests: hdl.huntington.org 14 (5 IIIF images, 9 CONTENTdm), archive.org 22 (metadata + djvu, 11 volumes) + print_check 5,
be-api.us.archive.org print_check 14, www.googleapis.com 6 + print_check 14, www.loc.gov about 25, tile.loc.gov about 15, api.openalex.org
print_check 16, api.crossref.org print_check 3, api.core.ac.uk 3, api.semanticscholar.org 4 (all 429).

### 3. Classification (key `period` for all five)
| ID | first audit | AUDIT 2 | depth | why |
|---|---|---|---|---|
| E42 Meigs to Biggs, 25 Apr 1864 | N3 (LS-V3) | **N3 (kept)** | D3 kept, 100 (28/28 H) | no printed text. Print shows only the order it follows (Halleck, 21 Apr: 1,000 horses to Butler), not Meigs's report of the shipping, the referral of the 100 saddle horses to the Cavalry Bureau or the transport complaint. External check added here (LS-V3 had none): the code value read 1,000 ("Plug Promise") with "[Horse]'s" agrees with Halleck's 1,000 horses for Butler (OR I/33; Butler vol. 4 p.112). Not D4: "saddle" is left plain against the book's value Guard, a reading liberty outside the listed name/code residue |
| E43 Rucker to Biggs, 29 May 1864 | N3 (LS-V3) | **N3 (kept)** | D3 kept, 95.2 (19 H + 1 C of 21; "Waymorners" unread) | the reply (OR I/36 pt 3, 30 May) prints only that the two boats will be returned. Rucker's coal question and his reason (cattle and horses up the Pamunkey) are not in print. Image checked here |
| E45 Rucker to Newport, Baltimore, 29 Nov 1864 | N3 (LS-V3) | **N3 (kept)** | D3 kept, 100 (11/11 H) | no printed text and no press report of a call for Baltimore steamers. External check added here: the signature code words "palate" (Brigadier General) and "Vinton" (Quartermaster) agree with Rucker's rank and office in print that autumn ("Brig. Gen. D. H. Rucker, Chief Quartermaster", OR I/43 pt 2, 19 Oct 1864). Not D4: the time word Fanny (11 AM) conflicts with the written header 10.45 AM, confirmed on the image |
| E46 to John A. Kennedy, 30 Nov 1864 | N3 (LS-V3, "second weakest") | **N3 (kept)** | D3 kept, 100 (9/9 H; signature name words unread) | the press read here for 30 Nov-12 Dec 1864, as LS-V3 asked, has no report of a suspect answering the Evening Post's description held in the Old Capitol, and no request to New York to identify him. The description itself is in print (Evening Star 29 Nov 1864, LS-V3). Still not N4: the NY Evening Post itself and RG 393 / Old Capitol records are unread |
| E47 Meigs to Biggs, 6 Apr 1864 | N3 (LS-V4) | **N3 (kept)** | D3 kept, 92.9 (13 H + 1 I of 14) | the related exchange is in print (OR I/33 p.814: Biggs, received 1.30 p.m. the same day, can spare a thousand tons of coal; Salvor's coal and water). That reply precedes this telegram and does not contain its two orders: Salvor to Annapolis, and the coal to Hilton Head. The content is not the telegram's, so this is not the E26/E28 kind of N2. External check added here: "Purple" = 1,000 (tons) and "Appian"/"Animal" = Monroe agree with Biggs's printed offer from Fort Monroe. Image checked here. Not D4: one I-grade token (Vintur) |

- **N3 (all five), safe sentence (each):** "Read at grade H with the period Cipher No. 1 book; no prior decipherment or printed text located
  after two independent searches (8 Oct 2026) of the Official Records (ser. I, II, III and the Navy series, by date and correspondent),
  the senders' and recipients' printed papers (Butler's correspondence included), the Huntington collection's full text, the 1864 press
  through Chronicling America, Internet Archive full text, Google Books, OpenAlex, CrossRef or CORE." Unsafe: "first", "unpublished",
  "never printed", "unknown telegram". Not N4: NARA RG 92/107/393, the Meigs Papers, the NY Evening Post itself and HathiTrust full
  text are unread, Semantic Scholar was unreachable, and the JSTOR rows are pending.
- **Depth under the 8 Oct depth bar.** The code clause is met for every entry. Each of these code values reads sensibly in at least two
  of these independent telegrams: "Spaffords" = Horses (E42, E43); "Pandora" = Colonel (E42, E45, E47); "Appian"/"Animal" = Monroe
  (E43, E47); "upton" = Post (E45 "your Post", E46 "Evening Post"); "sligo" = "In the" (E45, E46). Each depth sentence below was written
  by LS-V3/LS-V4 from the reading. It was re-checked here against the derived block (and, except E46, against the image) and stands (D2). D3 holds for each:
  at least 80% of tokens are H/C, and each has an external check named in the table (E42, E45 and E47 checks added here; E43 and E46
  from LS-V3). None is raised to D4: each has one listed liberty (E42 "saddle", E45 time word, E47 I token), or residue beyond name codes
  (E43 "Waymorners"). E46 was not image-checked by this session. Outward words: "largely deciphered (about N%)".

### 4. Postmortem
- No over-claim found: all five hold N3 after the families neither audit covered (Butler's correspondence for E47, ORN for E43/E45/E47,
  the press for E42/E43/E45/E47, and the press of 30 Nov-12 Dec 1864 for E46).
- Understatements filled: three D3 rulings (E42, E45, E47) had no named external check under the 8 Oct depth bar. One is now named for
  each (section 3). E45's header time is confirmed on the image.
- One near-miss, recorded for the next auditor: for E47, OR I/33 p.814 prints a same-day Fort Monroe reply about the same coal and the
  same steamer. A telegram in the same exchange printed beside the target is the place to look for the target itself. Here it was
  read and is not E47, but LS-V4 had listed it only as "context".
- status.json: E42, E43, E45, E46, E47 rows `audit_status` "two audits", `audit_refs` and the gap line updated; class, depth and
  depth_pct unchanged. SECOND-OPINIONS-QUEUE.tsv: SO-ECKERT-E42, -E43, -E45, -E46, -E47 unchanged (class and counts unchanged).
  JSTOR-QUEUE.tsv: 8 rows added (section 2).

## AUDIT 2 (second adversarial, AUD2-LS-C)

Verifier AUD2-LS-C (account 4, session_01K4wJpQYBt4oo4LhLZpi8pk, for the account-3 orchestrator; brief
`.claude/briefs/runs/2026-10-08-acct3-ledger2.md`, shape of `runs/2026-10-08-acct3-aud2-ls.md`), 8 Oct 2026, 03:37-04:1x UTC by
`date -u`. Scope: **E37, E38, E39, E40, E41** only. This session is separate from the solver (LS-R3) and the first auditor (LS-V3);
it tried to find each text in print and did not protect LS-V3's conclusion. Nothing decoded beyond re-running the committed script.
Depth ruled under `.claude/briefs/runs/2026-10-08-acct3-depth-bar.md`.

### 1. Re-derivation (rule 7) and image check
- `python3 ciphers/eckert-1864/decode.py --check`: "reading.md is current", exit 0.
- 2400 px IIIF images `hdl.huntington.org/digital/iiif/p16003coll11/<ptr>/full/2400,/0/default.jpg` for 9045 (E38, E39), 9046 (E40),
  9097 (E41), 9110 and 9111 (E37), in scratch, not committed; read at page scale and in PIL crops (9045 y 1300-1700 and 2280-2700,
  9046 x 180-1300 y 600-820, 9110 y 1950-end). LS-V3 had checked only E37 lines 1-5 (9110). Every line of all five entries, header to
  signature, agrees with ciphertext.txt. Notes, none of which changes a reading:
  - E39: the last two ledger lines are written interleaved (the second set in a smaller hand under the first): "be your authority &
    you will white to Post / master shelter webster Byron will call see you soon", as transcribed.
  - E40: the signature word transcribed "Seward[?]" (volunteer text "Benard") reads as a looped "Seward" on the crop; the "[?]" stays,
    as no count changes. The header has no written time; the 3 PM comes from the time word Imogene, as decoded.
  - E37: 9111 lines 1-3 ("you had better with draw immy ... violet youth Jas B Fry") and 9110 lines 6-9 agree; "youth" is clear on 9111
    (LS-V3's "north" doubt was for E46, not this entry). "wrangled" is written short ("wrangld"), as LS-R3 read it.

### 2. Families LS-V3 did not cover (or covered thinly), searched here (8 Oct 2026)
| family | searched | result |
|---|---|---|
| 1864 press for **E37**, the weakest, as LS-V3 asked (loc.gov Chronicling America JSON `dates=` window, OCR via the `tile.loc.gov` word-coordinates service; IA `sim_new-york-times_*` djvu) | `Manierre` 25 Oct-15 Nov 1864 (15 pages, all opened: NY Daily Tribune 1 Nov pp.4-5, 2 Nov p.5, 3 Nov pp.5, 7, 4 Nov pp.2, 5, 8, 5 Nov p.4, 11 Nov p.2, 15 Nov p.2; NY Dispatch 30 Oct pp.8, 10, 6 Nov p.5, 13 Nov p.5); `"provost marshal" Dodge withdraw Congress` 28 Oct-20 Nov (6 pages listed, none NY); `Manierre` 16 Nov 1864-30 June 1866 (88 pages, listed; Feb 1866 hits opened: his election as Police Commissioner); NYT 3, 4, 5 Nov 1864 (be-api full text, `Manierre`, `Fry`), NYT 4 Nov 1864 djvu read | **no mention of Fry, the War Department or any instruction.** NYT 4 Nov 1864 prints "Withdrawal of Hon. B. F. Manierre" (dated Nov. 2, 1864, the day of E37), which presents the withdrawal as his own decision after failed negotiations with Dodge's committee and the State Central Committee ("Having exhausted every honorable means ... I now withdraw from the contest"), recommending Dodge; the Tribune of 4 Nov p.5 says "Mr. Roosevelt and Mr. Manierre having thus both voluntarily retired"; the Dispatch of 6 Nov says the two "have left the field". The printed accounts give the outcome and a different reason; the order is not in them |
| Contested-election record (E37), read for every Manierre passage, not only "Fry" | *Dodge vs. Brooks* papers, House Misc. Doc. 39th Cong. 1st sess. (IA `unitedstatescon739offigoog`, whole djvu, every "Manier", "provost marshal", "War Department", "Secretary of War", "telegra") | Brooks's notice (Dodge's friends "induced Mr. Manierre to retire", the soldiers' votes transferred) and Sherwood's cross-examination on "Mr. Manierre's ceasing to be a candidate"; Manierre is no. 58 on a witness list but no testimony of his was found. No word of a War Department or Provost Marshal General instruction |
| 1864 press for **E38-E40** (Keith's remittances, schooner Princess) | Chronicling America: `Princess schooner detained` 12 Aug-10 Sept 1864 (3 pages opened: unrelated Princess Alexandra, Lake Erie, and Princesses royal); `Princess Murray seized cargo` (0); `Keith Halifax rebel agent` 10 Aug-30 Sept (5 listed, 3 opened: a Vermont vote table, a marriage notice; one read failed); NYT 13-26 Aug 1864 (12 issues, IA djvu, local regex for schooner Princess, Princess + detain/seize/cargo/marshal, Ferris, Alex(ander) Keith, Keith ... Halifax, Gordon Bruce, Kenner, Hunter & Co) | nothing on the remittances, the Ferris letter or the Princess (only the Ferris Female Institute's advertisement and an estate case) |
| 1864 press for **E41** (Arguelles affair context) | Chronicling America `Arguelles` 15 Sept 1864-31 Jan 1865 (27 listed; NY Dispatch 6 Nov p.4, Tribune 2 Jan 1865 p.3 index, Nat. Intelligencer 3 Dec p.3 opened); `Arguelles Murray indictment` June 1864-June 1865 (13 listed, June-July 1864); NYT 15-26 Oct 1864 (11 issues, IA djvu, Tassara, Arguelles, Savage ... Havana, Evarts with Spanish/Arguelles/Murray) | campaign references to the case (Belmont's Cooper Institute speech) only; nothing of Seward's 15 Oct list or a call on Evarts |
| Sender/recipient printed papers not read by LS-V3 | *Papers relating to Foreign Affairs* 1865 vol. (IA `papersrelatingtof00unit`, whole djvu: Keith x22, Princess x3, Wakeman, Evarts, Minor, Savage); F. W. Seward, *Seward at Washington* (IA `sewardatwashingt0000fred`: djvu text not served, 170 bytes; unreachable as text); Barrows, *William M. Evarts* (1941; IA `williammevartsla0000ches`, be-api full text: Arguelles, Tassara, Murray) | Foreign Affairs: Keith only in the Chesapeake affair (Halifax, Dec 1863-Jan 1864, the Wade rescue) and as T. A. Keith in the Dec 1863 intercepted cipher letter; the Princess there is a British steamer at Malaga (March 1864). Barrows treats the Arguelles case in narrative; nothing of the October list. No text of E38-E41. **Check for E40 found here:** the 1865 Foreign Relations volume prints "GEORGE HARRINGTON, Acting Secretary of the Treasury", Treasury Department, 5 Aug 1864 (Google Books snippet), the office the code word Barnard is read as in E40's signature |
| Huntington CONTENTdm (`CISOSEARCHALL`, p16003coll11), terms LS-V3 did not run | Princess (99, mostly the code word Princess = Captain), Barney (14), Harrington (13), Evarts (2: 9097, 6851), Savage (8), Dodge (65); item info read for 9820, 9047, 9063, 6851 | **two sibling ledger telegrams of the same affair, ciphertext transcriptions only, not decipherments and not E38-E40:** 9820 (mssEC 18 p.154, Horner, 13 Aug 1864, to Robt Murray: Gordon Bruce & Co are supplying machinery for Alex Keith Jr at Halifax, to be shipped to Mitchell Kenner & Co, Montreal; find out what it is) and 9047 (mssEC 19 p.154, 14 Aug 1864 11.10 AM, to Murray: whether the Schr Princess "was detained as directed yesterday or whether she got off"). They agree with E39's addressees and E40's order of the 13th; neither prints E38-E40's text. 9097 is E41's own page; 6851 is an unrelated 1863 page |
| IA full text, all items (be-api) | `"Manierre" "provost marshal" Fry`, `"Manierre" "General Fry"`, `"Manierre" "War Department" Dodge`, `"Manierre" Brooks Dodge "provost"`, `"Manierre" withdraw candidate Congress 1864`, `"Manierre" "Fry" withdraw`; `"schooner Princess" Barney 1864`, `"schooner Princess" "New York" August 1864 detained`, `"Princess" Harrington Barney collector detain 1864`, `"Gordon, Bruce" Keith Halifax`, `"Mitchell, Kenner"`, `"Clarence A. Seward" Evarts Arguelles Murray 1864` | no text of any of the five (Manierre hits: the 1863 draft-riot accounts, Fry's 1863 correspondence with Seymour, the NYT of 24 Aug 1863, the Dodge vs. Brooks record) |
| `tools/print_check.py` fresh phrase pass (scratch target, 12 phrases, `--only ia-global,gbooks,openalex,crossref`) | E37 "had better immediately withdraw as a candidate for Congress", "withdraw at once as a candidate for Congress or resign as provost marshal"; E38 "letter containing a remittance was this day forwarded from Halifax", "very important to the Government to get possession of that letter"; E39 "remittance by the same person to J. B. Hunter", "ship immediately to Mitchell Kenner", "information as to the trade business or occupation of the parties"; E40 "Detain the Princess and her cargo for further orders", "with aid of U. S. Marshal examine her cargo", "Let the Boston message go forward"; E41 "See Mr. Evarts and ask him to cooperate with you", "Thomas Savage vice consul general Havana Tassara" | IA-wide: no hit (one phrase HTTP 502). Google Books: loose word matches only, checked by title (the E41 names hit the 1865 Foreign Affairs volumes, the Arguelles correspondence LS-V3 read). OpenAlex: nothing relevant. CrossRef: 2 answered (nothing relevant), then HTTP 429, stopped |
| Google Books API (key, country=US), 13 hand queries | Manierre with provost marshal / Fry / Dodge / War Department / Congressional Globe / withdrew; Keith Halifax remittance Ferris Palfrey; "Alexander Keith" Halifax remittances intercepted; schooner Princess New York Murray detained / Barney Harrington; Arguelles Murray indictment Evarts C. A. Seward (one HTTP 503); Tassara Savage Minor Havana Evarts; "George Harrington" "Acting Secretary of the Treasury" August 1864 | no text of any of the five; Harrington's office in Aug 1864 confirmed (above) |
| CORE (key) | `"Alexander Keith" AND Halifax AND 1864 AND Seward`; `"Manierre" AND Dodge AND 1864`; `Arguelles AND extradition AND 1864 AND Murray` | 0 each |
| Semantic Scholar (key) | Keith Halifax Confederate agent 1864 (HTTP 429, not retried); Arguelles extradition 1864 Seward (0) | nothing; partly unreachable |
| JSTOR-QUEUE.tsv | existing (LS-V3): E37 (i) and (ii), E38-E39 (i) and (ii) "No. 10 North Market", E40 (i), E41 (i). Added: E37 (i) Manierre AND Fry; E40 (ii) "Detain the Princess and her cargo"; E39 (ii) "Mitchell, Kenner"; E41 (ii) "See Mr. Evarts and ask" | pending (never blocks) |
| Unread / unreachable | NARA RG 107 (M473), RG 110 (Fry's letters sent), RG 59 (Seward's domestic letters, M40), RG 28 (Post Office), RG 36 (NY Collector), RG 21 (the Princess, if libelled); Seward Papers (Rochester), Stanton Papers (LoC); NY Herald and World of 2-5 Nov and 13-20 Aug 1864 page by page (not opened here; the Herald is in Chronicling America but no query hit it); HathiTrust full text; *Seward at Washington* text; Semantic Scholar in part | unread |
Requests: www.loc.gov about 32, tile.loc.gov about 26, archive.org 30 (metadata, advancedsearch, djvu), be-api.us.archive.org about 40
(incl. print_check 12), www.googleapis.com about 26 (incl. print_check 12), api.openalex.org 12, api.crossref.org 3 (429),
api.core.ac.uk 3, api.semanticscholar.org 2 (one 429), hdl.huntington.org 15 (5 IIIF images, 6 dmQuery, 4 dmGetItemInfo).

### 3. Classification (key `period` for all five)
| ID | first audit | AUDIT 2 | depth | why |
|---|---|---|---|---|
| E37 Fry to Manierre and to Dodge, 2 Nov 1864 | N3 (LS-V3, "weakest") | **N3 (kept)** | D3 kept, 95.7 (22/23 H; "Wreath" unread) | the press of 1-15 Nov 1864 (Tribune, Dispatch, NYT) and the contested-election record were read as LS-V3 asked: the withdrawal is printed, Manierre's own letter of the same day gives the failed negotiations as its reason, and the Tribune calls it voluntary. The Provost Marshal General's order (withdraw or resign, "I advise the former") and its copy to Dodge are not located. This is not the E26/E28 kind of N2: the print carries the outcome, not the telegram's content. External check added here: the code words Platina and Paddle, read 8, agree with "Eighth District -- Capt. Benj. F. Manierre, No. 1,303 Broadway" in the provost marshals' list printed in the NY Dispatch, 13 Nov 1864 p.5 (the same list in the Tribune of 11 and 15 Nov p.2, OCR garbled). All lines image-checked |
| E38 Seward to Palfrey, 12 Aug 1864 | N3 | **N3 (kept)** | D3 kept, 100 (13/13 H) | no press report, no printed text. Context only: the Huntington sibling 9820 (13 Aug, to Marshal Murray) names Keith, Gordon Bruce & Co and Mitchell Kenner & Co |
| E39 Seward to Wakeman, 12 Aug 1864 | N3 | **N3 (kept)** | D3 kept, 100 (22/22 H) | as E38; 9820 agrees with E39's Gordon Bruce / Mitchell Kenner addressees and is not E39 |
| E40 Seward to Murray; Harrington to Barney, 13 Aug 1864 | N3 | **N3 (kept)** | D3 kept, 92.3 (12/13 H; "nick" unread) | no press report of the Princess's detention. The 14 Aug follow-up (9047) asks Murray whether the Princess "was detained as directed yesterday" -- it confirms the order was sent on the 13th and is not its text. LS-V3 named no external check for D3; one is named here: the code word Barnard read as "[Acting Secretary of the] Treasury" in Harrington's signature agrees with "George Harrington, Acting Secretary of the Treasury", 5 Aug 1864, printed in the 1865 Foreign Relations volume |
| E41 F. W. Seward to C. A. Seward, 15 Oct 1864 | N3 | **N3 (kept)** | D3 kept, 100 (10/10 H) | no printed text. The names and titles are in print in the Arguelles correspondence (LS-V3), the telegram's list and its call on Evarts are not. Image checked here |

- **N3 (all five), safe sentence (each):** "Read at grade H with the period Cipher No. 1 book; no prior decipherment or printed text located
  after two independent searches (8 Oct 2026) of the Official Records (ser. I, II, III and the Navy series, by date and correspondent),
  the senders' and recipients' printed papers (Papers relating to Foreign Affairs included), the Huntington collection's full text, the
  1864 press through Chronicling America and the New York Times, Internet Archive full text, Google Books, OpenAlex or CORE." For E37
  add: "Manierre's withdrawal itself was printed on 4 Nov 1864, without the instruction." Unsafe: "first", "unpublished", "never
  printed", "unknown telegram", and for E37 "secret order that forced Manierre out" (the reading shows advice to withdraw or resign;
  what moved him is not established). Not N4: NARA RG 107/110/59/28/36, the Seward and Stanton papers, the Herald and World page by
  page, HathiTrust full text are unread, Semantic Scholar was partly unreachable, JSTOR rows pending.
- **Depth under the 8 Oct depth bar.** Code clause met for each entry: these code values read sensibly in at least two of these
  independent telegrams -- France = New York (E37 Dodge copy, E39, E40), Shelby / shelter = General (E37 "Pro Mar Shelby", E38 "Post
  Mr Shelby", E39 "Post master shelter", E41 "vice Consul Shelby", "Consul shelter"), quadrant = Department (E38 "State Quadrant", E41
  "state quadrant"), Byron = Secretary of State signature (E38, E39). LS-V3's depth sentences were re-checked against the derived block
  and the images and stand (D2). D3 holds for each: at least 80% of tokens H/C and an external check named (E37 and E40 added here;
  E38, E39, E41 from LS-V3). None raised to D4: E37 and E40 carry an unread code word, and E38/E39/E41's checks are context or plain-word
  agreements, not a non-statistical check of a decoded code value. Outward words: "largely deciphered (about N%)".

### 4. Postmortem
- No over-claim found. E37, flagged weakest, holds after the press and the contested-election record were read for the order itself:
  the printed record gives the withdrawal a different, public reason, which is the gap between "outcome in print" and "content in
  print" that separates N3 from the E26/E28 N2s.
- Understatements filled: E40 had no named external check for D3 (now named); E37's lines 6-9 and the 9111 copy, and E38-E41 entirely,
  were image-checked for the first time. Near-misses recorded for the next auditor: the Huntington siblings 9820 (mssEC 18) and 9047
  (mssEC 19 p.154) belong to the same 12-14 Aug 1864 Keith/Princess exchange and are not in the ledger's entry list (`E` ids); they
  are ciphertext transcriptions, not printed decipherments, and were not decoded here.
- status.json: E37-E41 rows `audit_status` "two audits", `audit_refs` and gap line updated, E37 and E40 `depth_check` extended; class,
  depth and depth_pct unchanged. SECOND-OPINIONS-QUEUE.tsv: SO-ECKERT-E37 ... -E41 unchanged (class and counts unchanged).
  JSTOR-QUEUE.tsv: 4 rows added.

## AUDIT 2 (second adversarial, AUD2-LS-E)

Verifier AUD2-LS-E (account 1, session_017DD1zMQNaLVJmncdeynvfA, for the account-3 orchestrator; brief
`.claude/briefs/runs/2026-10-08-acct3-ledger2.md`, shape of `runs/2026-10-08-acct3-aud2-ls.md`), 8 Oct 2026, 03:42-04:3x UTC by
`date -u`. Scope: **E49, E50, E51, E52, E54** only. This session is separate from the solver (LS-R4) and the first auditor (LS-V4).
It tried to find each text, or its substance, in print and did not protect either's conclusion. Nothing was decoded beyond
re-running the committed script. Depth ruled under `.claude/briefs/runs/2026-10-08-acct3-depth-bar.md`.

### 1. Re-derivation (rule 7) and image check
- `python3 ciphers/eckert-1864/decode.py --check`: "reading.md is current", exit 0.
- 2400 px IIIF images `hdl.huntington.org/digital/iiif/p16003coll11/<ptr>/full/2400,/0/default.jpg` for 8983 (E49), 9042 (E50),
  9098 (E51), 9117 (E52) and 9135 (E54), in scratch, not committed; entry regions cropped with PIL (E49 y 1800-2420, E50 y 250-930,
  E51 y 230-860, E52 y 2000-2700, E54 y 160-1000, full width) and read by eye. LS-V4 had checked only E52 and E54; E49, E50 and E51
  are checked here for the first time. Every line from header to signature agrees with ciphertext.txt. Notes, none changing a reading:
  - E49: "No. 1" is pencilled above the header (Cipher No. 1), and the header time "4 10 pm" is pencilled above the date; the time
    word Julia (4 PM) agrees, as LS-R4 noted.
  - E50: the word transcribed "ham" (reading.md "[Report] ham of sailing") looks on the crop more like "hour" or "hom"; it is not
    corrected here (a reading question for the solver, outside this audit), but the depth sentence's "her hour of sailing" already
    assumes it. "Meigs" is written "Migs"; "Belcher[?]" reads Belcher.
  - E51, E52, E54: as transcribed (E52 "Plague" and "Plank", the 6 and 2 of the height; E54 "Toby landed").

### 2. Families LS-V4 did not cover, searched here (8 Oct 2026)
| family | searched | result |
|---|---|---|
| OR read again by date for the exchange around each telegram (IA djvu, whole volume): I/36 pt 3 (E49), I/42 pt 2 (E50), I/44 (E54); new: ser. II vol. 7 (political prisoners and spies, Aug 1864-Jan 1865; E52) and McCallum's Military Railroads report (IA `reportsofbvtbrig00unit`, `unitedstatesmili00unit`; the text OR ser. III vol. 5 reprints; E51) | every Meigs, Pitkin, Ingalls, Biggs, Halleck, Dyer entry on 11-13 June, 9-12 Aug and 4-6 Dec 1864; Hamilton, Elmira, "calling himself", Whiton, Anderson | **E49: substance printed.** OR I/36 pt 3 **p.769**: "WHITE HOUSE, June 12, 1864. (Received 2.15 p.m.) Brig. Gen. M. C. MEIGS, Quartermaster-General: Transportation by water for 16,000 troops will be required from this place to-morrow. The movement is very important, and it is necessary that all vessels suitable for transporting troops, which have been sent from this place to Washington and Alexandria, be returned at once, together with such other vessels as can be spared. General Ingalls authorized me to telegraph you. P. P. PITKIN, Captain, Assistant Quartermaster." E49, sent by Meigs to Biggs at 4.10 PM the same day, relays it: 16,000, embark at White House, tomorrow, every vessel fit to aid. Grant to Biggs the same day (same page and next) refers to "the amount of transportation to the White House heretofore called for". Not in print: Meigs's own wording and his clause on vessels for removing stores and wounded to a new base or hospital. LS-V4 searched I/36 pt 3 for the decoded words; the print says "16,000 troops" and "to-morrow", not "sixteen thousand strong" or "expedition". **E54: substance printed.** OR I/44 **p.627**: "WASHINGTON, D. C., December 5, 1864. SURGEON-GENERAL U. S. ARMY: The Secretary of War directs that all supplies, stores, and material for General Sherman's army be immediately sent to Hilton Head, S. C., to be landed at such place, or places, as may be there ordered. Competent officers of each department should be at that place to forward and issue stores without delay. H. W. HALLECK ... (Copies to the Chief of Commissary Department, Chief Engineer, Chief of Ordnance, and the Quartermaster-General)". E54 is the Chief of Ordnance (Dyer) passing that order to his officer at Fort Monroe the same afternoon (2.30 PM), down to "to be landed ... at such place or places as may be ... ordered". Not in print: Dyer's wording, Edson, and the instruction to write to Lt Arnold to hold the stores on board. LS-V4 searched I/44 for "Edson", "hold these supplies" and "ordnance supplies which have been ordered"; the print says "supplies, stores, and material". **E50:** I/42 pt 2 prints only Ingalls to Meigs, City Point, 10 Aug 1864: "I have ordered Continental to Fort Monroe. She draws too much water for this place and Washington. Please cause your orders to be given to her through Colonel Biggs" (LS-V4's context). It precedes E50 and is the reason E50 goes to Biggs; it does not carry E50's orders (provision and water her, send her to Hilton Head with the General-in-Chief's dispatch, report her hour of sailing). **E51:** McCallum lists "A. Anderson, general superintendent, to November 1" and "E. L. Wentz, general superintendent, after November 1" (1864), and names Anderson "chief superintendent and engineer"; no telegram or offer quoted. **E52:** OR II/7, nothing on a Hamilton at Elmira or Baltimore |
| Papers of Ulysses S. Grant (IA be-api full text, lending-only items searched inside): vol. 11 (`papersofulyssess0011gran`, June-Aug 1864; E49, E50), vol. 12 (`papersofulyssess0012gran`, Aug-Nov 1864; E51, E52) | Biggs, Salvor, Continental, Edson, Whiton, "Adna Anderson", Elmira, "sixteen thousand", "16,000 strong", "removing stores", "every vessel", Meigs | vol. 11 prints Grant to Biggs, Cold Harbor, 12 June 1864 (the OR I/36 pt 3 text above, with notes citing the same Ingalls/Biggs exchange, "Ibid., p. 725"); no E49 or E50 text. Vol. 12: nothing for E51, E52. **Vol. 13 (Nov 1864-Feb 1865; E54) unreachable**: not on IA; the publisher's open copy at scholarsjunction.msstate.edu answered a Cloudflare challenge to curl (one request each for three volumes; not retried, no challenge bypassed) |
| Sender's/recipient's printed papers and memoirs | Dana, *Recollections of the Civil War* (IA `recollectionsofc00danauoft`) and Wallace, *Autobiography* vol. 2 (`lewwallaceautobi00wall`) for E52; Haupt, *Reminiscences* (1901, prints Military Railroads correspondence) for E51 | nothing for E52 (no Hamilton, Elmira or rebel agent in Dana; Wallace only a county and a correspondent); nothing for E51 (Haupt left the service in 1863) |
| ASCE memoir of Adna Anderson (IA `sim_american-society-of-civil-engineers-proceedings_january-december-1889_15`, be-api full text; Google Books snippet) | "November, 1864", Whiton, inspector, telegram | "From November, 1864, to July, 1866, he was Chief Superintendent and Engineer of all the military railroads"; no Whiton message quoted (LS-V4's next step for E51, done) |
| 1864 press (loc.gov Chronicling America JSON, `dates=` window; page OCR via the page's `fulltext_file`), mandatory per entry | E49: `"sixteen thousand" "White House"` 12-25 June (2 pages), `expedition "White House" embark Smith` 12-20 June (15); E50: `steamer Continental "Hilton Head"` 10-31 Aug (6); E51: `"Adna Anderson"` 15 Oct-31 Dec (1); E52: `"Dr. Hamilton" rebel` (1), `Hamilton Elmira rebel agent` (5), `"calling himself" Hamilton` (4), `Hamilton arrested Baltimore rebel` (107), 3 Nov-20 Dec, fifteen pages sent for OCR, seven answered; E54: `Edson "Fortress Monroe" ordnance` (1), `ordnance stores "Hilton Head" Sherman` 5-31 Dec (17) | **E51: outcome in print.** *Nashville Daily Union*, 9 Nov 1864, p.3: "Adna Anderson, Esq., General Superintendent of U.S. Military R.R., Division of the Mississippi, has been appointed General Inspector of U.S. Military Rail Roads, and E. L. Wentz General Superintendent of Transportation and Repairs of M.R.R. Division of the Mississippi." This is the post E51 urges him to accept ("Inspect or [General] ship"), so it is an external check of the decoded code word; Whiton's urging, the "greatly increased powers" and the offer itself before acceptance are not in it. **E52:** no report located in the seven pages that answered (Daily National Intelligencer 14 Nov p.3, Chicago Tribune 14 Nov p.3, Evening Star 9 Nov p.2, Portland Daily Press 28 Nov p.2, NY Herald 6 Dec p.8, Staunton Vindicator 2 Dec p.2, Daily National Republican 19 Nov p.2): their Hamiltons and Elmiras are a navy death list, advertised letters, advertisements, shipping news and a Virginia list of prisoners at Elmira. The other eight (NY Herald 10 Nov p.2, which matched `"calling himself" Hamilton`; Portland Daily Press 5 and 12 Dec p.2; Dollar Weekly Mirror 3 Dec p.2; Evening Star 8, 17, 18 Nov p.2; Daily National Republican 18 Nov p.2) failed with HTTP 503/520 after one retry each or timed out. One try for two of them through chroniclingamerica.loc.gov redirected to www.loc.gov, which answered HTTP 403. The background batch was still running at that point and sent its last four page requests a few minutes after the 403 (one answered); nothing was sent to loc.gov after the batch ended. Recorded as a lapse in the one-retry rule, not repeated. **E52's press pass is incomplete** (next step below). E49, E50, E54: result lists only (troop movements, the Savannah campaign); nothing on their faces carries a telegram's text, and the OR prints above already settle E49 and E54 |
| Huntington CONTENTdm (`CISOSEARCHALL`, p16003coll11), terms LS-V4 did not run | Elmira, Adna, "sixteen thousand", "fine teeth", Kidnap, Arnold, "White House" | Elmira: 9117 (E52's own page), 9901 (29 Nov 1864, reserves to Elmira, prisoners), 9212 (Apr 1865), 7279 (1863), 12989, 13037 (operators' leaves) -- none about a rebel agent Hamilton; Adna and "fine teeth": only the entries' own pages (9098, 9117); "sixteen thousand", Kidnap, Arnold, "White House": object-level lists (37, 68, 65, 249 hits), the entries' own pages and other volumes already worked by LS-V4; no plain copy of any of the five |
| `tools/print_check.py` fresh phrase pass (scratch target; 12 decoded phrases; listed sources Grant Papers 11-12, OR II/7, McCallum, Wallace vol. 2, Dana, three OpenAlex and one CrossRef keyword searches) | e.g. "expedition sixteen thousand strong is to embark at White House", "provision and water the Continental", "accept promptly without question the proposed inspector generalship", "a rebel agent calling himself Dr Hamilton", "all ordnance supplies which have been ordered for Sherman's army" | no hit in any listed source; IA-wide 0; Google Books loose word matches only (three phrases HTTP 503); OpenAlex/CrossRef nothing relevant; Semantic Scholar HTTP 429 |
| Google Books API (key, country=US), 8 hand queries | `"Dr. Hamilton" rebel agent Elmira 1864`; `Hamilton "rebel agent" Baltimore Wallace November 1864`; `"Adna Anderson" "general inspector" military railroads`; `Whiton "Adna Anderson" 1864 inspector`; `"16,000 troops" "White House" Pitkin Meigs Biggs`; `"Continental" steamer "Hilton Head" August 1864 Biggs`; `Dyer Edson "Hilton Head" ordnance Sherman December 1864 Arnold`; `"supplies, stores, and material for General Sherman"` | the two OR prints above (I/36 pt 3, I/44) come back on their own wording; the ASCE memoir; nothing else |
| CORE (key) | `"Adna Anderson" AND 1864`; `Whiton AND "military railroads"`; `"Elmira" AND "rebel agent" AND 1864`; `"Continental" AND "Hilton Head" AND 1864`; `Dyer AND ordnance AND "Hilton Head" AND Sherman AND 1864` | 0 each |
| Semantic Scholar (key) | five topic queries | three answered (railroads, Elmira prison studies; nothing relevant), two HTTP 429 |
| JSTOR-QUEUE.tsv | existing: E51 (i), (ii); E52 (i), (ii); E54 (ii). Added: E49 (i), (ii); E50 (i), (ii); E54 (i) | pending (never blocks) |
| Unread / unreachable | Grant Papers vol. 13 (Cloudflare); NARA RG 92 (Meigs letters sent), RG 107 (M473), RG 156 (Ordnance, Dyer), RG 393 (Middle Department, Wallace), U.S. Military Railroads records; the Meigs Papers (LoC); HathiTrust full text; the Baltimore press of 7-20 Nov 1864 beyond Chronicling America | unread |
Requests: hdl.huntington.org 15 (5 IIIF images, 7 CONTENTdm queries, 5 item records -- some counted twice), archive.org about 14
(metadata and djvu, 9 volumes) + print_check 5, be-api.us.archive.org about 26 + print_check 36, scholarsjunction.msstate.edu 4
(1 listing, 3 challenged), www.loc.gov about 11 searches + about 30 page-JSON and OCR requests for 15 pages (two 403s at the end), chroniclingamerica.loc.gov 4 (2 redirects, followed once), www.googleapis.com 8 +
print_check 12, api.openalex.org print_check 15, api.crossref.org print_check 4, api.core.ac.uk 5, api.semanticscholar.org 5 + 2 (four 429).

### 3. Classification (key `period` for all five)
| ID | first audit (LS-V4) | AUDIT 2 | depth | why |
|---|---|---|---|---|
| E49 Meigs to Biggs, 12 June 1864 | N3 | **N2 (lowered)** | D3 kept, 100 (4/4 H) | the telegram's substance is printed: Pitkin's request from White House, received by Meigs 2.15 PM (OR I/36 pt 3 p.769), which E49 relays to Biggs at 4.10 PM -- 16,000 troops to embark at White House tomorrow, all suitable vessels to be sent. Meigs's wording and his stores-and-wounded clause were not located in print. The E26/E28 kind of N2 (content in print, no prior mapping of this ciphertext to it), not N1. External check added: the code words read Embark ("quorum") and Tomorrow ("Whelp") agree with Pitkin's "required from this place to-morrow" for "transportation by water" of troops. Image checked here |
| E50 Meigs to Biggs, 11 Aug 1864 | N3 | **N3 (kept)** | D3 kept, 89.5 (17/19 H; "amirs", "ham" unread) | the related print (Ingalls, 10 Aug, OR I/42 pt 2: Continental ordered to Fort Monroe, orders to go through Biggs) precedes E50 and does not contain its orders; the E47 shape, not E26/E28. Image checked here; "ham" may be "hour" on the crop (section 1) |
| E51 W. H. Whiton to Adna Anderson, 21 Oct 1864 | N3 ("weakest") | **N3 (kept, weakest)** | D3 kept, 100 (11/11 H) | the outcome is printed -- Anderson "appointed General Inspector of U.S. Military Rail Roads" (*Nashville Daily Union* 9 Nov 1864 p.3; ASCE memoir 1889; McCallum: general superintendent to 1 Nov 1864) -- but neither the offer nor Whiton's urging and reasons are; LS-V4's own test (Whiton's message quoted in the memoir or McCallum) was run and it is not quoted. The E37 shape (outcome in print, message not). Held at N3 with the outcome named in the safe sentence. External check added: "Inspect or [General] ship" (code word Shelter = General) agrees with the post named in the press. Image checked here |
| E52 Dana to Wallace, 7 Nov 1864 | N3 ("second weakest") | **N3 (kept)** | D3 kept, 100 (9 H + 1 C of 10) | no printed text and no press report located; Dana's *Recollections*, Wallace's *Autobiography* vol. 2, OR II/7 and the Grant Papers vol. 12 are silent. The press pass LS-V4 asked for is only partly done (seven of fifteen pages read; eight unreachable this session), so this N3 rests on an incomplete press search and stays flagged. Image re-viewed here |
| E54 Dyer to Edson, 5 Dec 1864 | N3 | **N2 (lowered)** | D3 kept, 90.9 (10/11 H; "Toby" unread) | the telegram's substance is printed: Halleck's order of the same day, copied to the Chief of Ordnance, that all supplies for Sherman's army go at once to Hilton Head "to be landed at such place, or places, as may be there ordered" (OR I/44 p.627). E54 is Dyer passing it to Edson. Dyer's wording, Edson and the Lt Arnold instruction were not located in print. E26/E28 kind of N2. External check added: "Kidnap's" = Sherman's agrees with the printed order. Not D4: "Toby" unread. The print's "to be landed" sits where E54 has "Toby landed", which supports LS-R4's note (NOTES.md) that "Toby" stands for "to be"; not regraded here |

- **N3 kept: E50, E51, E52.** Safe sentence (each): "Read at grade H with the period Cipher No. 1 book; no prior decipherment or
  printed text located after two independent searches (8 Oct 2026) of the Official Records (ser. I, II, III, by date and correspondent),
  the Papers of Ulysses S. Grant (vols 11-12), the senders' and recipients' printed papers and memoirs, the Huntington collection's full
  text, the 1864 press through Chronicling America, Internet Archive full text, Google Books, OpenAlex, CrossRef or CORE." For E51 add:
  "Anderson's appointment as General Inspector of the Military Railroads, which the telegram urges him to accept, was reported in the
  Nashville Daily Union on 9 November 1864; the telegram itself was not located." Unsafe: "first", "unpublished", "never printed",
  "unknown telegram", and for E51 any line implying the appointment is unknown. Not N4: Grant Papers vol. 13, NARA RG 92/107/156/393, the
  Meigs Papers and HathiTrust full text are unread, Semantic Scholar was partly unreachable, and the JSTOR rows are pending.
- **N2: E49, E54.** Safe sentences: E49 "Read at grade H with the period Cipher No. 1 book; the telegram relays Capt. Pitkin's request
  from White House, printed in the Official Records (ser. I vol. 36 pt 3 p.769), for water transport for 16,000 troops the next day;
  Meigs's own wording was not located in print." E54 "Read at grade H with the period Cipher No. 1 book; the telegram passes on Halleck's
  order of the same day, printed in the Official Records (ser. I vol. 44 p.627), that all supplies for Sherman's army go to Hilton Head;
  Dyer's own wording and his instruction to Lt Arnold were not located in print." Unsafe: "unknown order", "previously unread", any N3
  wording. **Not counted** (below N3).
- **Depth under the 8 Oct depth bar.** Code clause met for each: Belcher = Quartermaster General reads as Meigs's signature in E49 and
  E50 (E49); Pandora = Colonel and Vinton = Quartermaster (E50 with E45, E47); Fanny = 11 AM (E51, header 11 am, with E45);
  Florence = 11.30 AM (E50, E52, E53, each with an 11.30 header) (E52); Animal = Monroe (E54 with E43, E47). Stop and signature
  marks (zebra, zodiac, yoke) are not counted for the clause. Each depth sentence (LS-V4's, section 4) was re-checked here against
  the derived block and the image and stands (D2). D3 holds for each: at least 80% of tokens H/C, and an external check is named in the
  table (E49, E51, E54 checks added here; E50, E52 from LS-V4). None raised to D4: E50 and E54 have unread words, E51 and E49 were not
  put through a separate D4 ruling here (no brief for it), and E52 is held at D3 as LS-V4 ruled. Outward words: "largely deciphered (about N%)".

### 4. Postmortem
- Over-claims corrected: E49 and E54 were N3 (LS-V4 section 4, status.json, SO-ECKERT-E49 and -E54). In both, the order the telegram
  relays is printed in the very OR volume LS-V4 searched, a few hours earlier the same day, in another officer's words: Pitkin's
  "16,000 troops ... to-morrow" (I/36 pt 3 p.769) and Halleck's "supplies, stores, and material ... to be landed" (I/44 p.627). A
  phrase search on the decoded wording ("sixteen thousand strong", "ordnance supplies which have been ordered") cannot find them. The
  lesson is AUD2-LS-A's and AUD2-LS-B's again, in a third form: for a telegram that **forwards** an order or a request (QMG to his
  depot officer, Chief of Ordnance to his officer), read the same volume by date for the order being forwarded, from the officer above
  or the one asking, before setting N3.
- Understatements filled: E49, E51 and E54 now have a named external check; E49, E50 and E51 were image-checked for the first time.
- E51 stays the weakest N3 and is flagged for any third look: its outcome is in print in two places; only the message is not.
- Next step, E52: read the eight Chronicling America pages listed in section 2 that did not answer (and the Baltimore American / Sun of
  7-20 Nov 1864, not in Chronicling America) for a Dr Hamilton stopped at Baltimore; about 15 requests on a day loc.gov is answering.
- status.json: E49 and E54 rows grade N2 (`plaintext_novelty` N2, `mapping_novelty` N3), `audit_status` "two audits", not counted;
  E50, E51, E52 rows `audit_status` "two audits", `audit_refs`, gap and safe line updated; depth and depth_pct unchanged.
  SECOND-OPINIONS-QUEUE.tsv: SO-ECKERT-E49 and -E54 withdrawn (N2), their prompts' context lines name the prints; SO-ECKERT-E51's
  prompt gains the Nashville Daily Union line; -E50, -E52 unchanged. JSTOR-QUEUE.tsv: 5 rows added (section 2).

## AUDIT (LS-V2c)

Verifier LS-V2c (account 1, LANE ST-LEDGER-2), 8 Oct 2026, 04:17-04:4x UTC by `date -u`; a separate session from the reader (LS-R2c)
and from every other reader of the batch, not protecting its conclusions. Scope: LS-R2c's entries **E30-E36** (mssEC 19 pp.157-166,
McCaine at Harper's Ferry / Charlestown, Aug 1864, Cipher No. 1, key.md = mssEC 41). Nothing decoded beyond re-running the committed
script after the image corrections below. Key source for every item: `period` (the War Department's own Cipher No. 1 book).

### 1. Re-derivation (rule 7) and image check (three entries, the longest among them)
- `python3 ciphers/eckert-1864/decode.py --check`: "reading.md is current", exit 0, before and after the corrections below.
- Strip crops from the 2400 px IIIF images (scratch, not committed): `python3 tools/iiif_lines.py --image $S/img/p9055.jpg --out
  $S/crops/9055 --prefix p9055 --region 100,300,2300,1000 --lines-per-crop 3 --overlap 0 --max-width 2400 --debug` (auto centres
  121..936); `python3 tools/iiif_lines.py --image $S/img/p9060.jpg --out $S/crops/9060 --prefix p9060 --region 100,200,2300,680
  --centres 86,163,240,317,394,471,548,625 --lines-per-crop 3 --max-width 2400` plus two PIL crops of the same file (rows 280-420 and
  700-960, the header and the closing lines); `python3 tools/iiif_lines.py --image $S/img/p9056.jpg --out $S/crops/9056 --prefix
  p9056 --region 100,300,2300,1400 --centres 84+79k (k=0..15) --lines-per-crop 4 --max-width 2400`.
- **E33 (9055)**, all ten body lines: word for word with ciphertext.txt ("Camel Thayer", "Quicken ment", "Reading - ped wal - rus.",
  "Chisel plane ax saw" as transcribed). No correction.
- **E34 (9056, the longest entry, 15 lines)**: every line read agrees with ciphertext.txt ("federal out", "Fits shew Happy", "Sperry
  will and Thorn towns", "Bore Did you get letter yet"); the faint pencil glosses above line 1 (a later hand) are not transcribed, as
  LS-R2c said. No correction.
- **E36 (9060)**, all eight lines: two corrections, both places where LS-R2c's text follows the volunteer transcription against the
  image. (a) Line 3 opens **"More cool and careful"**, not "Move" (the final letters match "whore" in line 7). (b) The word written
  above the struck "signed" in line 7 is **"walrus"**, not "wolves"; key.md p.23 l.18 gives Walrus = Signature, so the clerk replaced
  the plain word with its code word (H). Both are confirmed by the print found in section 3 ("cool and careful reports ..."). Applied
  to ciphertext.txt; `decode.py --write`, `--check` exit 0.
- Tokens graded I/M: LS-R2c graded none. Reading the decode against the print (section 2) finds code-word values that the print
  contradicts; they are regraded here (not H):
  E35 "Govern whore B Rough" = Governor Brough and "John B Rough" = John Brough (the print signs "JNO. BROUGH"), "rely abel" = reliable --
  the decoder had read Govern as the numeral 18, John as Grant and abel as Vermont; now in the block's `plain:` line (C from the
  print), E35 code-word H 30 -> 27. E36 "Govern whore B rough" the same (plain); with walrus added, E36 stays H 14.
  E32 "aaron" (key: Rhode Island) stands where the print has "Two more regiments **on** their way" -- M (value contradicted by the
  print); "Grant" (left plain by LS-R2c) stands where the print has Warrenton, i.e. the code word Grunt (key p.14) misspelt -- I.
  E31 "vincent" (key: Quartermaster) stands where the print has the colon after "reports as follows" -- M (probably for violet =
  quotation). E36 "polecat" (not in key.md) = "Commandant", from the Mereness Calendar quotation -- C. E33 "Reading - ped" = Reading
  (key: Equip) + ped = "equipped", H by the key though the decoder leaves it plain because of the split.

### 2. Entries LS-R2c located in print: page confirmed by script (a check, not a search)
IA `warofrebellion431unit_0` (OR ser. I vol. 43 pt 1) `_djvu.txt`, whitespace-normalized, phrase regex, page from the nearest running heads.
| ID | printed at | how confirmed |
|---|---|---|
| E30 | OR I/43 pt 1 **p.859** (Augur to Sheridan, Charlestown, 20 Aug 1864) | between the heads "UNION. 857/858" and "859", end of p.859 before the head "860": "Major Waite, Eighth Illinois Cavalry, left Muddy Branch at 12 m. to-day, on his scout toward the gaps. He has about 650 men. I directed him to carry out the orders of General Grant, which you sent me, as far as he could, but not to let it interfere with his scouting. I have no report yet from Lazelle." Word for word with the decode (ledger has no "yet") |
| E31 | OR I/43 pt 1 **pp.871-872** (Augur to Sheridan, 21 Aug 1864, 7.30 a.m.) | "Lazelle has returned, and reports as follows: There are at Warrenton about 2,000 infantry and about 500 cavalry, and a large force of 10,000 men, cavalry and infantry, at Culpeper, moving up toward Warrenton. The rebels are using the roads between Warrenton and Chester Gap and Manassas Gap ... He does not mention how he ascertained these figures. He has most probably depended upon reports of citizens. I will learn more definitely and inform you." Word for word; ledger tail "sent long letter Cumberland issue directed" is a clerk's note, not in print |
| E32 | OR I/43 pt 1 **p.872** (Augur to Sheridan, OCR "August 27, 1864 -- 9.30 p.m.") | the item follows E31 directly among the 21 Aug items (the next one reads OCR "August 31" for 21), so the OCR "27" is 21 misread; "Lazelle says he received his information concerning the enemy's forces at Culpeper from a citizen who had just left there. He also informed him about the forces at Warrenton. Colonel Gansevoort, with his regiment, the Thirteenth New York Cavalry, goes out to-morrow to scout in the vicinity of those places. The Forty-first New York arrived here from Hilton Head to-day, about 400 men. Two more regiments on their way." Word for word but for the two tokens regraded above; ledger time 10 PM against print 9.30 p.m. |
| E34 | OR I/43 pt 1 **p.897** (Augur to Sheridan, Harper's Ferry, 24 Aug 1864) | between heads 896 and 898: "I have no news from the Eighth Illinois Cavalry, or from Gansevoort. A refugee just in from Culpeper ... Fitzhugh Lee, with his cavalry, about 3,000, and part of Longstreet's corps, about 10,000, left there to join Early last Friday a week. He thinks they went through Sperryville and Thornton's Gap. Mosby, with two pieces of artillery, attacked the small cavalry force at Annandale this morning ... The force there is in a stockade." Word for word |
| E35 | OR I/43 pt 1 **p.951** (Brough to Stanton, Columbus, 28 Aug 1864, received 10 a.m. 29th); also OR I/39 pt 2 (IA `warofrebellion392unit`) | end of p.951 before the head "952": "Our military agent at Gallipolis telegraphs me this morning, 'I have reliable information of Breckinridge's advance into the Kanawha Valley with 8,000, via Lewisburg.' General Heintzelman left for Chicago this morning under your order. I have telegraphed him on the way. I have the State battery at Camp Dennison and three regiments of National Guard at Gallipolis. No general officer in the State. JNO. BROUGH." The ledger copy is the War Department's relay of Brough's telegram to Sheridan's army; word for word but for the three plain words the decoder had misread |

### 3. Entries LS-R2c did not locate: search (8 Oct 2026)
| family | searched | result |
|---|---|---|
| OR by date and correspondent, +/- 3 days | ser. I vol. 43 pts 1-2 (`warofrebellion431unit_0`, `432unit`), vol. 39 pt 2 (`392unit`), ser. III vol. 4 (`warofrebellionco0004genf`), whole volumes, regex on normalized text: discredit, Gallipolis, cool and careful, hundred/100-days, valley open, Brough (every hit read); Twenty-fifth New York Cavalry, train of forges/wagons, forges, Thayer, equipped, dismounted men, 375, 350 men, escorted by | **E36: not printed in the OR**, but its context is: Stanton to Brough 29 Aug (I/43 pt 1, "If the report of your agent be true Sheridan has been very much deceived"), Stanton to Brough 30 Aug (Sheridan asks the removal of the Gallipolis agent "as an alarmist or a Copperhead"), Brough to Stanton 30 Aug ("perhaps I was too quick in acting on it"), and I/39 pt 2 Heintzelman to Halleck, Chicago 30 Aug: "Commander at Gallipolis reports that rumors do not bear investigation, and thinks the reports of an advance in the valley a canard" -- the same report by another channel. **E33: no hit**; context only, I/43 pt 1 brigade itinerary: "August 24 ... the Twenty-fifth New York Cavalry was assigned to the brigade" (Sheridan's cavalry), consistent with E33's regiment "ordered to you" on 22 Aug |
| Google Books API (key, country=US) | E36: "careful reports from Gallipolis", "discredit the telegraph of this morning", "leaves the valley open" Gallipolis, "return of the hundred days men" Gallipolis 1864, Brough Stanton Gallipolis "no advance" 1864, "cool and careful reports", "Commandant of the Posts here thinks" (503); E33: "small train of forges" (503 once, then answered), "forges and other wagons" 1864 / Thayer, "Twenty-fifth New York Cavalry" with 350 men, dismounted 25th NY Cavalry Aug 1864 | **E36 in print: _The Mereness Calendar: Federal Documents on the Upper Mississippi Valley, 1780-1890_ (Illinois Historical Survey; G. K. Hall, 1971), Google Books id NlwPAQAAMAAJ, snippet only: "... cool and careful reports from Galipolis discredit the telegram of this morning. Commandant of the Posts here thinks no advance is making but the return of hundred days men leaves the valley open". 0-24. C. W.D. L.R. ..."** -- the calendar quotes the telegram from the War Department letters/telegrams received file; volume and page not read (snippet view), the quoted words agree with the decode token for token. E33: no hit |
| 1864 press (loc.gov Chronicling America JSON) | E36: "careful reports from Gallipolis" 29 Aug-15 Sept (0), Gallipolis Breckinridge discredit 29 Aug-10 Sept (1: Cumberland Civilian & Telegraph 8 Sept p.3, read by script: a soldier's letter about the Gallipolis hospital, not this), "leaves the valley open" (0), Gallipolis Breckinridge Kanawha 29 Aug-6 Sept (0), Brough Gallipolis canard (0); E33: "small train of forges" 22 Aug-10 Sept (0), "Twenty-fifth New York Cavalry" Harper (0, one connection reset), Augur train forges Harper (0) | no hit for either telegram |
| IA full text, all items (be-api fts) | "careful reports from Gallipolis" (0), "leaves the valley open" (0), "discredit the telegraph" (502, not retried), "small train of forges" (0), "forges and other wagons" (2, a modern book about another campaign), "all mounted and equipped" "Twenty-fifth New York" (0) | no hit |
| Sender's and recipient's papers | E36: Brough's own papers are the Ohio governor's telegram books (Ohio History Connection), not read; the Mereness Calendar covers the War Department file. E33: sender unread (signature group "Chisel plane"), recipient Sheridan: Sheridan's Personal Memoirs and the Sheridan Papers (LOC) not read page by page | unread (E33) |
| OpenAlex, Semantic Scholar, CORE (keys) | Twenty-fifth / 25th New York Cavalry 1864 Harper's Ferry / Shenandoah, forges train | OpenAlex 28 results, S2 29, none about this; CORE returned no usable answer (one call, not retried) |
| JSTOR | 2 rows appended to JSTOR-QUEUE.tsv for E33, families (i) and (ii) | pending (never blocks) |
| Unread / unreachable | NARA RG 107 (telegrams received/sent by the Secretary of War; Augur's Dept of Washington letters sent, RG 393), the 25th New York Cavalry's regimental books and any regimental history page by page, HathiTrust full text, the Mereness Calendar page itself | unread |

### 4. Classification (key `period` for all seven)
| ID | N-class | text known? | depth | depth_pct | check |
|---|---|---|---|---|---|
| E30 Augur to Sheridan, 20 Aug 1864 | N1 | known (OR I/43 pt 1 p.859) | D4 | 100 (22/22 H) | word for word with the print |
| E31 Augur to Sheridan, 21 Aug 1864 7.30 AM | N1 | known (OR I/43 pt 1 pp.871-872) | D3 | 96.7 (29 H of 30; vincent M) | print |
| E32 Augur to Sheridan, 21 Aug 1864 10 PM | N1 | known (OR I/43 pt 1 p.872) | D3 | 96.9 (31 H of 32; aaron M; Grant = Grunt I) | print |
| E33 to McCaine for Sheridan's cavalry, 22 Aug 1864 | **N3** | unknown | D3 | 93.3 (28 H of 30; signature "Chisel plane" unread; "ax saw" closing group not counted, as LS-R2c) | image crop checked here, all lines; fresh re-derivation; OR I/43 pt 1 itinerary: 25th New York Cavalry assigned to the cavalry brigade 24 Aug 1864 |
| E34 Augur to Sheridan, 24 Aug 1864 | N1 | known (OR I/43 pt 1 p.897) | D4 | 100 (37/37 H) | image crop checked here; word for word with the print |
| E35 Brough to Stanton, 28 Aug 1864, relayed 29 Aug | N1 | known (OR I/43 pt 1 p.951; OR I/39 pt 2) | D4 | 100 (27/27 H after regrading Govern/abel/John as plain, C) | word for word with the print |
| E36 Brough to Stanton, 29 Aug 1864, relayed 8 PM | **N1** | known (Mereness Calendar 1971, snippet) | D3 | 100 (14/14 H; polecat = Commandant C) | image crop checked here, all lines; the calendar quotation agrees token for token |

- **E33: N3** -- no prior plaintext or decipherment located after the logged search. Not N4: the sender is unread, NARA RG 107/393,
  the regimental records, HathiTrust full text and the Sheridan Papers are unread, JSTOR rows pending. Safe sentence: "Read at grade H
  with the period Cipher No. 1 book; no prior decipherment or printed text located in the Official Records (ser. I vols. 39, 43 and
  ser. III vol. 4 by date and correspondent), the 1864 press in Chronicling America, Internet Archive full text or Google Books
  (searched 8 Oct 2026)." Unsafe: "first", "unpublished", "never printed". It is the weak kind of N3 (an operational routine message,
  the regiment's movement is in print as an itinerary line); a second audit should read the 25th New York Cavalry's record and
  Augur's letters-sent for 22 Aug before it is counted outward.
- **E36: N1, not N3.** LS-R2c's "not located" was a search result in the OR; the telegram's own words are quoted in the Mereness
  Calendar. The ledger copy is our independent re-decipherment of a printed text.
- **E30-E32, E34, E35: N1**, independent re-decipherments of telegrams printed in OR I/43 pt 1 (E35 also I/39 pt 2). Not counted.
- Depth sentence for E33 (D2+, checked against the derived block): "On 22 Aug 1864 Washington tells McCaine at Harper's Ferry, for
  Sheridan, that a small train of forges and other wagons for his cavalry left the day before, escorted by the 25th New York Cavalry,
  350 men, ordered to him, together with a detachment of 375 men belonging to the 1st and 3rd Cavalry Divisions, all mounted and
  equipped." Code clause: Panama = Cavalry reads sensibly in E33 three times and in E31, E34 (independent contexts); the H stretch
  "Stomach here yesterday for Camel Thayer Escorted by the harsh plaster frog pacific pebble prolong & mansion spits" is a contiguous
  run of H/plain past the authentication distance.

### 5. Postmortem
- One under-search: E36 was reported "not located" after the OR and two Google Books queries; a quoted-phrase Google Books query on
  the decoded words found it in a printed calendar. The press-and-calendar step of the brief is what moved it; the OR-only search would
  have counted it N3.
- Two transcription errors carried from the volunteer text (E36 "Move", "wolves"), corrected from the image; LS-R2c's own NOTES said
  E36 lines 1-4 only were read at crop resolution, which is where the reading stopped trusting the image.
- Grade over-claim corrected: the decoder's H on plain words split by the clerk (E35 Govern, abel, John; E36 Govern) and on values the
  print contradicts (E31 vincent, E32 aaron). E35 H 30 -> 27 by `plain:` lines in ciphertext.txt; E31/E32 are recorded here as M/I
  (not edited in the source, since the code word is what the clerk wrote).
- Rows: status.json one result row for E33 (N3, audit_status "one audit"); SECOND-OPINIONS-QUEUE.tsv row SO-ECKERT-E33 with its prompt
  in second-opinions/; two JSTOR-QUEUE.tsv rows. Requests: in the ROOM done line.

## AUDIT (LS-V5)

Verifier LS-V5 (account 1, LANE ST-LEDGER-2), 8 Oct 2026, 04:17-04:4x UTC by `date -u`; a separate session from every reader (LS-R5 read
these entries), not protecting its conclusions. Scope: LS-R5's entries **E55-E64** (mssEC 19, all Cipher No. 1, key.md = mssEC 41).
Nothing decoded beyond re-running the committed script. Key source for every item: `period`. Depth under
.claude/briefs/runs/2026-10-08-acct3-depth-bar.md.

### 1. Re-derivation (rule 7) and image check
- `python3 ciphers/eckert-1864/decode.py --check`: "reading.md is current", exit 0. E55-E64 derived block H 136, C 1 (as LS-R5).
- Strip crops from the 2400 px IIIF images (scratch, not committed), regions as LS-R5's: `python3 tools/iiif_lines.py --image $S/img/p9038.jpg
  --out $S/crops/9038 --prefix p9038 --region 100,270,2300,2060 --centres 30,142,235,328,422,515,608,701,794,888,981,1074,1167,1260,1354,1447,1540,1633,1726,1820,1913
  --lines-per-crop 3 --max-width 2400`; `... p9003 --region 100,600,2300,900 --centres 60,168,272,368,464,560,652,740,828 --lines-per-crop 3`;
  `... p8927 --region 100,260,2300,780 --centres 40,140,252,348,448,540,628,712 --lines-per-crop 4`; plus single bands for the I/M re-reads:
  `p8932 --region 100,1700,2300,820 --centres 500,596,692,772 --lines-per-crop 4`, `p8951 --region 100,1040,2300,720 --centres 50,192 --lines-per-crop 2`,
  `p9036 --region 100,1100,2300,1000 --centres 40,...,912 --lines-per-crop 5`.
- Word for word, header to tail: **E64** (9038, the longest, all 21 lines), **E60** (9003, all 9 lines), **E57** (8927, all 8 lines) agree with
  ciphertext.txt. Small notes only: E64 line 18 reads "formed in to [to]" with the second "to" written over/struck (transcribed "in to"); E64 line 19 the
  struck "you" is confirmed; E57's tail "Bender his on one" carries pencil glosses "over game tide" (the clerk's check group, not message text).
- Re-read from the image, every I/M token and every image-vs-volunteer word LS-R5 lists: E58 "pembroke", "Tinkers" (as written, line 9; a separate
  marginal entry "draft tonnage of them" sits beside it, not part of E58); E59 "Susan" (as written; header "1130 am" -- the key's 11.30 PM stays M);
  E63 "money" is a pencil interlineation over "peasant ... ca - cy" (= "via Monocacy", which the print confirms); E64 "Sapan Rape" and "Dismiss" as
  written; E57 "collared", "Ann a / pol is", "whisky", "his on one" as written; E64 "nick" (not "wick"). No transcription correction.

### 2. Entries located in print: page confirmed by script (a check, not a search)
| ID | printed at | how confirmed |
|---|---|---|
| E55 | OR ser. I vol. 39 pt 2 **p.304** (Washington, August 26, 1864 -- 11 a.m., to Lieut. Col. C. H. Howard, Louisville, Ky.) | IA `warofrebellion392unit` djvu, before the running head 305: "A dispatch just received from General Canby states that General A. J. Smith's command has already been detached to co-operate with General Sherman. H. W. HALLECK, Major-General and Chief of Staff." Word for word with the ledger's plain and code words. Two derived-block notes: the pencil interlineation "leopard" over "Gen Canby" (carried by LS-R5 as `<ins>`) decodes to [Maj Gen S. A. Hurlbut], which is not in the print -- a later gloss, not message text; the signature code word "Jew" = General-in-Chief, the print signs Halleck as Chief of Staff (the E48 shape). "Lol" = Louisville (plain abbreviation) |
| E56 | OR ser. I vol. 43 pt 2 **p.682** (Washington, D. C., November 28, 1864, to Major-General Sheridan, "Copy to Major-General Thomas, Nashville") | cached `warofrebellion432unit` djvu, after the running head 682: "General Grant directs me to say that it is not expected of you to give to the major-generals ordered to report to you commands of more than divisions. H. W. HALLECK." LS-R5 searched I/45 pt 2 and missed it in the volume it already held. **Corrections**: "eggs peck dead" is *expected* (print), not "expedient" as LS-R5's table has it; "or dear ed to nick to you" is "ordered to report to you", so the unread word "nick" is *report* (also E64, below) |
| E58 | **Papers of Ulysses S. Grant vol. 10** (Jan.-May 1864), a note printing the telegram "received, DNA, RG 107, Telegrams Collected (Bound)" and ending "Please acknowledge this.", followed by "On the same day, 3:00 P.M., USG telegraphed to Townsend. '11 a.m. dispatch received. Papers refered to will be sent in the morning'" | Google Books API (key, country=US), snippet only, two copies of PUSG vol. 10 (ids 7DAAxfRuXKoC, mD4fAQAAMAAJ); page not read. E58 is Townsend's 11 AM telegram to Grant of 19 Apr 1864 ending "Please acknowledge this" and asking for papers (the Jeffery letter), so the note is taken to print E58; class N1 on that identification. A reader of PUSG 10 should confirm the page |
| E60 | Collected Works of Abraham Lincoln (Basler, 1953) **vol. 7**; Nicolay and Hay, Complete Works (1894); OR ser. III vol. 4 (1900) | Google Books API snippets (three queries): "John Hay, Astor House, New York. Executive Mansion, Washington, July 16, 1864. Yours received. Write the Safe-conduct, as you propose, without waiting for one by mail from me. If there is, or is not, any thing in the affair, I wish to know it, without unnecessary delay. A. LINCOLN" (Basler cites ALS, DNA WR RG 107, Presidential Telegrams I, 98). **Correction**: the addressee is **John Hay at the Astor House, New York** (the Greeley-Niagara peace affair), not Grant: "John" in "For John Hay Asthore house" is Hay's name in clear, which the decoder took for the Grant code word. Ledger "with the safe conduct" against the print's "Write the safe-conduct" (image: "with"; a clerk's slip or mishearing, not a misread) |
| E61 | OR ser. I vol. 36 pt 2 **p.587** (War Department, May 9, 1864 -- 4 p.m., to Major-General Butler) | cached `warofrebellion362unit` djvu, between the running heads 587 and 588 (OCR damaged: "A dispatch from General Grant has just been received ... EDWIN M. STANTON"); full wording from the Google Books snippet of the same volume: "... his whole army to form a junction with you, but had not determined his route. Another dispatch from him is being translated. EDWIN M. STANTON." Also in Private and Official Correspondence of Gen. Benjamin F. Butler vol. 4 (1917) |
| E63 | OR ser. I vol. 43 pt 1 **p.709** (Washington, D. C., August 6, 1864 -- 11.30 a.m., to Lieutenant-General Grant, Monocacy) | IA `warofrebellion431unit_0` djvu (fetched once to scratch, 3.96 MB), before the running head 710: "One brigade of Torbert's division of cavalry left last night and another will start this morning for Harper's Ferry, via Monocacy. As your telegram of last night says, 'Send all cavalry yet to arrive,' &c., I presume you allude to the division expected from City Point. Do you want an order issued making a military division of the four departments, or shall it await your return here? H. W. HALLECK, Major-General and Chief of Staff." Word for word; the signature "Sugar Ben - jam - in" is Halleck's |
| E64 | OR ser. I vol. 43 pt 1 **p.719** (Washington City, August 7, 1864 -- 12 m., and 12.15 p.m., both to Major-General Sheridan, signed U. S. Grant) | same djvu, between the running heads 719 and 720: both telegrams of the entry, word for word ("Do not hesitate to give commands to officers in whom you repose confidence ... give Averell some other command, or relieve him from the expedition, and order him to report to General Hunter ..." and "The Departments of Washington, the Middle, the Susquehanna, and of Western Virginia, have been formed into a military division called the Middle Division ..."). The print settles LS-R5's unread and M words: "Dismiss" = Averell (a name code word not in key.md), "Sapan" in "relieve Sapan Rape" = "him from the" (Rape = Expedition), "nick" = report, Mutton = Hunter (as decoded), "confide = ants" = confidence |

LS-R5 had marked E55, E63, E64 "NOT searched in the right volume" and E60, E61 "not located": all five are in print. LS-R5's own correction note
(431unit "not the volume I took it for") was right about the scratch cache but wrong as a gap: `warofrebellion431unit_0` is I/43 pt 1 (LS-R2c used it the same morning).

### 3. Entries not located: search families (8 Oct 2026) -- E57, E59, E62
Phrases (decoded wording): E57 "good staunch steamer", "load of colored troops" + Relief + Annapolis; E59 "of no use at Lexington", "its efficiency is
being impaired", Eleventh Michigan Cavalry + "sent to the field"; E62 "Montauk and other two propellers", "plenty of coal as it is probably scarce",
"report daily any arrivals of steamers". Script in scratch (`q.py`, `ca.py`), plus hand queries.

| family | searched | result |
|---|---|---|
| OR by date and correspondent, +/- 3 days (IA djvu, normalized text, regex) | E57, E62: ser. I vol. 33 (cached), vol. 35 pt 2 (`warofrebellion352unit`, Dept. of the South, Apr 1864), ser. III vol. 4 (`warofrebellionco0004genf`) -- Relief, staunch, colored troops + Annapolis, Spaulding, Montauk, two propellers, coal supply, Meigs/Biggs/Thomas 5-9 Apr; E59: ser. I vol. 32 pt 3 (`warofrebellion323unit`, Chap. XLIV, Kentucky Apr 1864) -- Cavalry Bureau, Eleventh Michigan, Lexington, 25-29 Apr | **no hit for the three telegrams**. Context only: I/35 pt 2 pp.37-38 prints Halleck's memorandum of 5 Apr ("two colored regiments (1,800 men) at Annapolis to be sent to South Carolina"), Meigs to Biggs 5 Apr 3 p.m. ("Send the Spaulding to Annapolis immediately to take a colored regiment thence to Hilton Head") and Biggs's reply ("Spaulding is at New Berne ... I have the Montauk and two other similar propellers ... carry 800 men"); I/33 p.814 prints Biggs's 6 Apr reply (received 1.30 p.m.: "Propeller Montauk has broken valve-crank ... Spaulding not yet arrived. Will give her orders as soon as she comes in") -- the exchange around E57 and E62, not their text. I/32 pt 3 has the Eleventh Michigan Cavalry at Lexington under Hobson in April (E59's subject), not E59 |
| Sender's/recipient's printed papers | E59: PUSG and Sherman by Google Books phrase queries; E57/E62: Meigs (no printed papers found), Butler correspondence vol. 4 by phrase | no hit |
| Huntington full text (CONTENTdm `CISOSEARCHALL`) | Jeffery (only 8932 = E58), staunch (3227 mssEC 05 gunboats 1862; 9382 Oct 1862 -- unrelated; 8927 = E57), Lexington (88 leaf hits, titles only, not read), Montauk (empty reply, not retried) | no second copy of E57/E59/E62 found |
| 1864 press (loc.gov Chronicling America JSON, by date window) | E57 "steamer Relief Annapolis colored troops" 7-20 Apr (11 pages: Worcester Daily Spy, Chicago Daily Tribune, Springfield Weekly Republican, Muscatine Weekly Journal); E62 "Montauk propellers Annapolis Hilton Head" 5-20 Apr (0); E59 "Eleventh Michigan Cavalry Lexington" 25 Apr-15 May (1: Cleveland Morning Leader 29 Apr p.4) | result lists only; the page OCR fetch (`tile.loc.gov` ocr.txt) failed (400/stub), pages not read. Unread, next step below |
| IA full text, all items (be-api fts) | every phrase above | 0 relevant hits where it answered; four phrase calls returned HTTP 502 (not retried) |
| Google Books API (key, country=US) | every phrase above (12 queries for these three, 2 returned 503) | no hit on any of the three telegrams (loose matches on common words only) |
| OpenAlex, CORE, Semantic Scholar | 4 queries each (Meigs/Biggs April 1864 transports; Eleventh Michigan Cavalry Lexington; the Eckert ledger) | nothing relevant; S2 answered 429 once |
| JSTOR | 6 rows appended to JSTOR-QUEUE.tsv (E57, E59, E62; families i and ii) | pending (never blocks) |
| Unread / unreachable | NARA RG 92 (QMG telegrams sent, April 1864), RG 107 (M473); the press pages listed above; HathiTrust full text; ORN (not run for these three: army transports, no naval correspondent) | unread |

### 4. Classification (key `period` for all ten)
Depth counts: `depth_pct` = H / (H + I + M + unread message code words); clerk's tail check groups ("Bender his on one", "Tall oaks from little acorns grow")
are not message text and are not counted.

| ID | N-class | text known? | depth | depth_pct | check |
|---|---|---|---|---|---|
| E55 Halleck to C. H. Howard, 26 Aug 1864 | N1 | known (OR I/39 pt 2 p.304) | D4 | 100 (11/11 H; the "leopard" gloss excluded) | word for word with the print |
| E56 Halleck (for Grant) to Sheridan, copy Thomas, 28 Nov 1864 | N1 | known (OR I/43 pt 2 p.682) | D4 | 100 (13/13 H; "nick" = report by the print) | word for word with the print |
| E57 Meigs to Capt. Thomas, quartermaster, 8 Apr 1864 | **N3** | unknown | D3 | 80.0 (8 H + 2 I of 10) | image checked here, all lines; external: OR I/35 pt 2 p.37 (Halleck's memo, Meigs's 5 Apr orders) prints the plan this telegram executes -- colored troops at Annapolis to be carried to Hilton Head |
| E58 Townsend to Grant, 19 Apr 1864 | N1 | known (PUSG vol. 10, note; identification by snippet) | D3 | 85.7 (12/14 H + M; "pembroke", "Tinkers" M) | identification by Grant's printed reply to the "11 a.m. dispatch" |
| E59 Halleck (General-in-Chief code word) to Sherman, Nashville, 27 Apr 1864 | **N3** | unknown | D3 | 92.3 (12 H + 1 M of 13) | header image checked here; external: OR I/32 pt 3 places the Eleventh Michigan Cavalry at Lexington, Ky., under Hobson in April 1864 |
| E60 Lincoln to John Hay, Astor House, 16 Jul 1864 | N1 | known (Basler vol. 7; OR III/4) | D4 | 100 (7/7 H after the "John" correction) | word for word with the print, but for "with" / "Write" |
| E61 Stanton to Butler, 9 May 1864 | N1 | known (OR I/36 pt 2 p.587) | D4 | 100 (6/6 H) | word for word with the print |
| E62 Meigs to Biggs, Fort Monroe, 6 Apr 1864 | **N3** | unknown | D3 | 90.9 (10 H + 1 I of 11) | re-derivation; external: Biggs's printed replies of 5 Apr (OR I/35 pt 2 pp.37-38, "the Montauk and two other similar propellers") and 6 Apr (OR I/33 p.814, "Montauk has broken valve-crank ... Spaulding not yet arrived. Will give her orders") answer the ships and orders this telegram names |
| E63 Halleck to Grant, Monocacy, 6 Aug 1864 | N1 | known (OR I/43 pt 1 p.709) | D4 | 100 (21/21 H; "money" = Mono-) | word for word with the print |
| E64 Grant to Sheridan, two telegrams, 7 Aug 1864 | N1 | known (OR I/43 pt 1 p.719) | D4 | 94.7 (35 H + 1 C of 38; "Sapan Rape" 1 M; "Dismiss" = Averell, unread name code) | word for word with the print |

- **N3 (E57, E59, E62)**: no prior plaintext or decipherment located after the logged search. Not N4: NARA RG 92/107, the press pages listed,
  HathiTrust full text and the Meigs letterbooks are unread, and JSTOR rows are pending. Safe sentence (each): "Read at grade H with the period
  Cipher No. 1 book; no prior decipherment or printed text located in the Official Records (ser. I and III by date and correspondent), the Huntington
  collection's full text, Internet Archive full text, Google Books, OpenAlex or CORE (searched 8 Oct 2026)." Unsafe: "first", "unpublished",
  "never printed", "unknown telegram".
- **E62 is the weakest N3** (the E47/E37 shape): the exchange around it is in print (Meigs 5 Apr, Biggs 5 and 6 Apr), and Biggs's 6 Apr reply answers
  it. If a second audit finds Meigs's 6 Apr wording quoted (e.g. in a Quartermaster's report or RG 92 edition), it drops to N2/N1.
- **E57**: the plan is printed (Halleck's 5 Apr memo); the Relief order to Captain Thomas is not located.
- **E55, E56, E58, E60, E61, E63, E64: N1** (independent re-decipherments of printed texts). Not counted. E58's N1 rests on a snippet identification
  (PUSG vol. 10): a second audit should read the page.
- Depth sentences (D2+ each, checked against the derived block): E57 "Meigs tells Captain Thomas, quartermaster, that if on examination the
  Relief proves a good staunch steamer she is to call at Annapolis for a load of colored troops, and if she is not needed there, to go on to Hilton
  Head and report for duty." E59 "Washington tells Sherman at Nashville that the Cavalry Bureau reports the 11th Michigan Cavalry is of no use at
  Lexington, that its efficiency is being impaired there, and that it ought to be sent to the field." E62 "Meigs tells Biggs at Fort Monroe to order
  the Spaulding on to Hilton Head to report to the quartermaster there, to send the Montauk and the other two propellers to Annapolis to carry troops
  to Hilton Head with plenty of coal, and to report his coal on hand, the coal expected within a fortnight, and every steamer arrival daily."

### 5. Postmortem
- Over-claims and errors corrected in LS-R5's section (a correction note is appended there): E60's addressee (John Hay at the Astor House, not Grant;
  the decoder's [Maj Genl U.S. Grant] for "John" is wrong here, so E60 is H 7, not 8); E56 "eggs peck dead" = expected, not expedient; E55's
  [Hurlbut] comes from a later pencil gloss, not the message. Five of LS-R5's "not located / not searched" entries are printed (E55, E60, E61, E63,
  E64) and a sixth (E56) sat in a volume LS-R5 had already cached; E58 is in PUSG 10. The filter's `or_cov` passed all seven; the fault is the
  ranking (LS-PRE's calibration: recall 0.90 at 60+ words, and these are short or famous), and a Sonnet reader's paraphrased phrases (LS-R5's own
  note) -- a verbatim phrase from the decoded line found five of them in one call each.
- Not changed in ciphertext.txt / reading.md (no decoding in a verifier's brief): the E60 header "to Grant (code word John)" and the decoder's
  reading of "John" there. Next: a reader adds a `plain: John` line to E60 and a header fix, ~$0.2.
- Rows: status.json one result row per N3 entry (E57, E59, E62), audit_status "one audit"; SECOND-OPINIONS-QUEUE.tsv rows SO-ECKERT-E57, -E59,
  -E62 with prompts in second-opinions/; JSTOR-QUEUE.tsv six rows. Requests: in the ROOM done line.

Correction carried (LS-FIX, 8 Oct 2026, commit f4dba16ec): E60 header now Lincoln to John Hay at the Astor House, "John" plain in clear (H 7); no class change.

## AUDIT (LS-V6)

Verifier LS-V6 (account 1, LANE ST-LEDGER-2), 8 Oct 2026, 04:16-04:4x UTC by `date -u`; a separate session from every reader of the
batch (LS-R6), not protecting its conclusions. Scope: LS-R6's eleven blocks **N2-BG..N2-BM** (ciphertext-no2.txt, key-no2.md = mssEC 47
Cipher No. 2), **E65** (ciphertext.txt, key.md) and **O9-AH..O9-AJ** (ciphertext-no9.txt, key-no9.md = mssEC 67), plus LS-R6's step-2 1865
verdict. Nothing decoded beyond re-running the committed scripts and looking up E65's eight code words in key-no2.md (section 2).
Key source for every item: `period`. Depth under .claude/briefs/runs/2026-10-08-acct3-depth-bar.md.

### 1. Re-derivation (rule 7) and image check
- `decode.py --check` "reading.md is current", `decode_no2.py --check` "reading-no2.md is current", `decode_no9.py --check`
  "reading-no9.md is current": exit 0 each.
- Strip crops from the 2400 px IIIF images (scratch, not committed; S = session scratch):
  `python3 tools/iiif_lines.py --image $S/img/p8966.jpg --out $S/crops/8966 --prefix p8966 --region 100,1560,2300,1180 --centres
  90,180,270,365,460,550,645,740,835,930,1030,1120 --lines-per-crop 3 --max-width 2400`; p8967 `--region 100,150,2300,700 --lines-per-crop 3`
  and `--region 100,780,2300,480 --centres 60,150,240,330,420 --lines-per-crop 5`; p9011 `--region 100,1560,2300,1000 --lines-per-crop 5`;
  p8958 `--region 100,180,2300,1080 --lines-per-crop 6`; p9104 `--region 100,1330,2300,950 --lines-per-crop 10`; p9139 `--region
  100,1580,2300,900 --lines-per-crop 10`; p8907 `--region 100,230,2300,1700 --lines-per-crop 9`.
- **Three entries word for word** (header to signature): **N2-BG** (the longest, 213 words, pp.74-75), **N2-BI**, **E65**. All agree with the
  committed transcription except: N2-BG line 9 the image has "has has so whimpered" (a doubled plain "has"; transcription "has so") -- no
  effect on the reading; N2-BI the addressee reads **"Bickford"** on the image (capital B, as the volunteer text), not LS-R6's "Pickford"
  (header word, ungraded; left M). N2-BG's last line ("brought off yawl Buggy How are you long saved fraternity") is cut at the crop foot;
  first words checked, the rest left as LS-R6 read it.
- I/M tokens and image-vs-volunteer words re-read from the image: N2-BG "crowded" is a plain word on the page (the decoder's
  `[Lieut Gen U.S. Grant]ed` is a stem artifact, not a code word); N2-BH "desires", "New Haven" plain (and C from the print, section 3),
  "Wasel" on the image (transcription "Weasel", same code word = Transportation, confirmed by the print's "transportation"); N2-BI
  "I presume ree [sweden]" -- "presume" is plain on the image (the decoder reads it as the key row Presume = "Hotly [?]"; plain word, not a code word), time word "Fanny" against the
  header "10 am" confirmed; N2-BK "spoud" (= espoused) as transcribed; O9-AI/AJ "Ida", "Camden", "Hannah", "Deborah", "Quadroon" as
  transcribed, the AJ header "noon" and tail "noon Mch 4th" confirmed (the time word Deborah's 3 AM disagrees, M stands); E65 "Wedlock",
  "Salems", "altar", "Shark", "Costume", "blubber" as transcribed -- and see section 2.

### 2. Correction: E65 is in Cipher No. 2, not Cipher No. 1 (over-claim in LS-R6's section and reading.md)
LS-PRE's tsv guessed cipher 2 for 8958/66/0; LS-R6 overrode it as "Cipher No. 1 vocabulary, mostly plain". Looking up the eight code words
in both keys: key.md gives Blubber = City Point, Salem = Force, Altar = (none), Shark = Government, Wedlock = Track, Costume = Jefferson,
Viola = 12.30 -- which is why the committed reading says "proceed immy to City Point ... the forces on the altar ... Government Canby will
start for there Track afternoon ... Jefferson". key-no2.md gives **Blubber = Cairo** (p.12 l.15), **Salem = Force** (p.21 l.18), **Altar = Red R**
(p.10 l.18), **Shark = General** (p.22 l.3), **Wedlock = Tomorrow** (p.25 l.1), **Costume = Secretary of War** (p.13 l.24), **Viola = 12
midnight** (time page): "The service requires that you should proceed immediately to Cairo to make arrangements for the transmission and
receipt of intelligence between that point and the forces on the Red River. General Canby will start for there tomorrow afternoon. You
had better join him ... [signed] Secretary of War", sent at midnight 6 May 1864. Every value fits; "Growl" (opening word) is left
unresolved here. The No. 2 values are confirmed externally, word for word in part: **W. R. Plum, *The Military Telegraph during the Civil War
in the United States* (Chicago 1882), vol. 2 p.47** (IA `militarytelegra02plumgoog`, djvu text, OCR running head 47): "On the 6th of May, at
midnight, Colonel Stager was ordered by Secretary Stanton, to meet and proceed with General E. R. S. Canby (who was about to relieve
Banks) to Cairo, Ill., to arrange 'for prompt transmission and receipt of intelligence between that point and the forces on Red River.'"
OR ser. I vol. 34 pt 3 (`warofrebellion343unit`) prints Canby at Indianapolis 10 May ("I leave for Cairo in the first train. Colonel Stager
is with me") and Stager's own reports from Cairo, 11-12 May. **The committed E65 reading is wrong in five code words (City Point, Government,
Track, Jefferson, and "altar" left as a plain word) and must be re-filed in ciphertext-no2.txt and re-read with key-no2.md** (a reader's job,
not this verifier's; flagged in ROOM). Until then E65's H 7 count in reading.md stands for a wrong key.

### 3. Entries located in print: page confirmed by script (a check, not a search)
| ID | printed at | how confirmed |
|---|---|---|
| N2-BH | OR ser. I vol. 43 pt 2 **pp.467-468** (Adjutant-General's Office, Washington, October 26, 1864, to Major-General Sheridan, Strasburg; signed E. D. Townsend) | IA `warofrebellion432unit` djvu: the telegram starts before and ends after the running head "468 OPERATIONS IN N. VA., W. VA., MD., AND PA."; "The Secretary of War desires you to order the Eighteenth Connecticut Volunteers to be at New Haven the 2d of November, and the Second Eastern Shore Maryland Regiment to be at Baltimore by the 4th of November; the quartermaster to furnish them transportation; the regiments to be replaced at Martinsburg by others ordered by you from elsewhere. Acknowledge receipt." Word for word with the decode (the ledger's "repeat" = the print's "order" by the code word). LS-R6's "p.468" corrected to pp.467-468 |
| N2-BG | **substance**: F. H. Garrison, *John Shaw Billings, a memoir* (New York 1915) **p.93** (IA `johnshawbillings00garr`, Billings's war diary, 21 May 1864) | "8 A.M. Dispatch received by Genl. Ingalls from Genl. Meigs stating that steamboats and covered barges had been started to Fredericksburg to carry off the wounded. Two large steamers are to be at Tappahannock to be loaded from the lighter vessels. All the wounded are to be taken away even if it crowds the vessels. Cavalry posted on the bluffs from Port Royal to Fredericksburg to cover the movement." -- a summary of N2-BG (Meigs to Ingalls, 20 May 10 PM) by the Army of the Potomac's medical inspector who saw it the next morning; not the telegram's text |
| E65 | **substance and a quoted phrase**: Plum vol. 2 p.47 (section 2) | as quoted above |

### 4. Entries not located: search families (8 Oct 2026)
Phrases (decoded wording): N2-BI "depreciation of vouchers", "short supply of money", "checked deliveries", "cavalry horses which are on
hand"; N2-BJ "pluck and gallantry", "son of the Senator", "Sheridan's staff", Wade + New Orleans; N2-BK "most capable and most worthy",
"chief quartermaster to your army", "revoke the assignment"; N2-BL "make sure of a supply", forage + Pensacola; N2-BM "do you need more
mules", "obliged to stop shipments", "stop shipments of horses"; O9-AH "fully coaled", "thirty thousand men ... two thousand horses", "fresh
for their morning", "Astor House", "chartered a number of vessels"; O9-AI/AJ "no further shipments of gold", "ship no more coin", Cheesman.

| family | searched | result |
|---|---|---|
| OR by date and correspondent +/- 3 days (IA djvu, whole volume, regex on flattened text) | ser. I vols 33 (O9-AH), 34 pt 3 (N2-BL, E65), 36 pt 1 and pt 3 (N2-BG, N2-BJ), 40 pt 3 (`warofrebellion403unit`: N2-BI, N2-BM -- **the volume LS-R6 did not search**; both are addressed "for Brig. General Ingalls", City Point, in the decoded plain, not to a quartermaster "at Pickford/Palestine" as LS-R6's table says), 43 pt 2 (N2-BK); ser. III vol. 4 (all) | no hit for N2-BI, BJ, BK, BL, BM, O9-AH, O9-AI/AJ. I/40 pt 3 has telegrams to Ingalls of 26-31 July 1864 (Butler, Meade, Paine, Sheridan's cavalry), none from Meigs on horses or mules; I/36 pt 1 (medical report) mentions the State of Maine and Connecticut at Fredericksburg (N2-BG context) |
| 1864 press, Chronicling America (loc.gov JSON, `dates=` window from the telegram's date) | every phrase above (11 queries) | 0 results for every quoted phrase except "fresh for their morning" (9 pages, June 1864; common phrase, no title matched O9-AH on its face, not read) and "Stager Cairo Canby telegraph" (1 page, Chicago Tribune 12 May 1864, unread -- E65 is placed by Plum anyway) |
| Sender's and recipient's printed papers | Billings's diary (Garrison 1915) for N2-BG (found, section 3); Plum's Military Telegraph vol. 2 for E65 (found); Meigs, Ingalls, Holabird, Sheridan, Dana, Chase/Treasury: no printed letter-book exists for Meigs or Ingalls; Sheridan's *Personal Memoirs* and Dana's *Recollections* not read; Chase Papers (Niven) via Google Books: 0 for Cheesman + gold + London | not located |
| IA full text, all items (be-api fts) | every phrase above | N2-BI "depreciation of vouchers": 2 items, one is M. R. Wilson, *The Business of Civil War* (2006), quoting a manufacturer's letter to the Quartermaster General ("because of the recent severe depreciation of vouchers and certificates, 'We in common with other ...'") -- the same phrase in the same office and summer, not N2-BI; others 0 or loose matches |
| Google Books API (key, country=US) | every phrase above + 5 hand queries | Billings memoir (N2-BG, found above); Wilson 2006 (as above); no telegram located; 503 on four queries (not retried) |
| OpenAlex, Semantic Scholar, CORE (keys) | 6 name/event queries (Cheesman gold 1864; Meigs Ingalls horses 1864; Stager Cairo Canby; J. F. Wade Sheridan staff; Holabird Pensacola forage; Van Vliet Butler transports) | nothing relevant; S2 429 on two |
| JSTOR | 12 rows appended to JSTOR-QUEUE.tsv (N2-BI, BJ, BK, BL, BM, O9-AH; families i and ii) | pending (never blocks) |
| Unread / unreachable | NARA RG 92 (Meigs, telegrams sent), RG 107 (Stanton, M473), RG 56 (Treasury, telegrams to the Assistant Treasurer, San Francisco); the Washington and San Francisco press page by page (O9-AI/AJ gold); Sheridan's and Dana's memoirs; HathiTrust full text | unread |

### 5. Classification (key `period` for all)
| ID | N-class | text known? | depth | depth_pct | check |
|---|---|---|---|---|---|
| N2-BG Meigs to Ingalls, 20 May 1864 | **N2** | substance known (Billings diary, Garrison 1915 p.93) | D3 | 97.9 (47 H + 1 I of 48 code words; "crowded" is plain) | image, all lines; re-derivation; Billings's summary agrees point by point |
| N2-BH Townsend to Sheridan, 26 Oct 1864 | N1 | known (OR I/43 pt 2 pp.467-468) | D4 | 100 (29 H + 2 C) | word for word with the print |
| N2-BI Meigs to Ingalls, 24 July 1864 | **N3** | unknown | **D2** | 96.7 (29 H + 1 I of 30 code words; the decoder's H on "presume" is a plain word) | image, all lines; re-derivation; Wilson 2006 prints the same "depreciation of vouchers and certificates" complaint to the QMG that summer |
| N2-BJ Secretary of War to Dana, 4 June 1864 | **N3** | unknown | **D2** | 95.7 (22 H + 1 I of 23) | re-derivation |
| N2-BK Meigs to Sheridan, 12 Dec 1864 | **N3** | unknown | **D2** | 90.9 (8 H + 2 C + 1 I of 11) | re-derivation; image of the I/M words |
| N2-BL Meigs to Holabird, 8 Apr 1864 | **N3** | unknown | **D2** | 100 (17 H) | re-derivation |
| N2-BM Meigs to Ingalls, 27 July 1864 | **N3** | unknown | **D2** | 100 (10 H) | re-derivation |
| E65 Stanton to Stager, 6 May 1864 | **N2** | substance and one quoted clause known (Plum 1882 II p.47) | not rated: committed reading uses the wrong key (section 2) | -- | -- |
| O9-AH Meigs? to Capt. G. D. Wise, 20 Apr 1864 | **N3** | unknown | **D2** | 100 (14 H; mostly in clear) | re-derivation; image as transcribed by LS-R6 |
| O9-AI, O9-AJ (to D. W. Cheesman, 1 and 4 Mar 1864) | N3 (no prior text located) | unknown | **D1** | 33.3 (1 H of 3 code words; "Ida", "Camden" M) | image checked here. The text is written in clear in the ledger; the decipherment adds three code words, two uncertain, so no result row is filed |

- **N3 (N2-BI, N2-BJ, N2-BK, N2-BL, N2-BM, O9-AH)**: no prior plaintext or decipherment located after the logged search. Not N4: NARA RG 92/107,
  the press page by page, Sheridan's and Dana's memoirs and HathiTrust are unread; JSTOR pending. Safe sentence (each): "Read at grade H with
  the period Cipher No. 2 book (O9-AH: the War Department's older vocabulary, mssEC 67); no prior decipherment or printed text located in the
  Official Records (ser. I and III by date and correspondent), the 1864 press through Chronicling America, Internet Archive full text, Google
  Books, OpenAlex, Semantic Scholar or CORE (searched 8 Oct 2026)." Unsafe: "first", "unpublished", "never printed", "unknown telegram".
- **Depth D2, not D3, for the six N3 entries**: rule 4a and the depth bar put D3 on an external check or AD + a matched control; these have
  a fresh re-derivation and a contiguous H stretch well past the authentication distance, but no outside source that checks a code value
  (Wilson 2006 for N2-BI is context, not a check). N2-BG is D3 because Billings's diary checks its code values (Fredericksburg, wounded,
  Port Royal, cavalry, Tappahannock) point by point. Outward words for the six: "partially deciphered (about N%)".
- **Weakest N3s**: N2-BJ (Wade's appointment to Sheridan's staff, if made, will be in Sheridan's or Dana's papers and in Heitman; a second audit
  should read Dana's *Recollections* and Sheridan's *Memoirs* for June 1864); N2-BK (the revoked assignment of a chief quartermaster to the
  Middle Military Division, Dec 1864, may be in OR I/43 pt 2 correspondence under another wording or in ser. III vol. 4 Meigs's annual report).
- **N2-BG, E65: N2** (substance known elsewhere, no prior mapping of this ciphertext). **N2-BH: N1.** Not counted.
- Depth sentences (D2+ each, written from the derived block): N2-BI "Meigs tells Ingalls that about a thousand cavalry horses on hand will
  be sent with the artillery horses, more as they come in, that depreciation of vouchers and certificates and short money have lately checked
  deliveries, and that 3,962 cavalry horses have been issued at Washington since 1 July." N2-BJ "The Secretary of War asks Dana to find out
  whether Sheridan will take on his staff Lieutenant Colonel Wade, the Senator's son, a former cavalry captain of the Army of the Potomac just
  back from New Orleans, whom Meade knows." N2-BK "Meigs tells Sheridan that the Secretary of War has been asked to revoke an assignment,
  made because the officer was already acting in that capacity, and asks whether Sheridan's army needs a chief quartermaster and who is most
  capable and worthy." N2-BL "Meigs tells Col. Holabird, chief quartermaster at New Orleans, to send a vessel loaded with forage to Pensacola to
  make sure of a supply there by 1 May, since forage sent from New York may be delayed by storms." N2-BM "Meigs asks Ingalls whether, under
  changed circumstances, he needs more mules, says about 500 have been shipped and the rest held until he hears, and that shipments of horses
  to him have been stopped." O9-AH "Captain Wise at the Astor House, New York, is told to work with Major Van Vliet on the vessels chartered for
  the expedition, all to reach Fort Monroe by the 24th and be coaled by the 25th, because Butler means to move thirty thousand men, two
  thousand horses, ten batteries and a hundred wagons."

### 6. LS-R6 step 2 (the 1865 rows): is the 0.077 gap within the control's spread?
Re-run of `ls_r6_no1_1865.py` at 04:2x UTC: the 1865 rows are unchanged (n=108, median 0.276) but the control is now **n=34, median 0.395**
(E30-E36 were marked `already_read` by LS-R2c after LS-R6 ran), diff **-0.119**, so the script's own verdict flips to "does not read". Spread
(scratch `spread.py`): control split-half |median difference| p95 0.092; bootstrap 95% interval of the difference -0.185 to -0.041 (excludes
0); the 1865 median sits at the control's 9th percentile. And the statistic does not separate the ciphers: the rows already read as **Cipher
No. 2 or old vocabulary** (N2-*, O9-*, n=88) score median **0.374**, as high as the No. 1 control -- the code-word column of key.md is common
English words, so the share measures plain-word overlap, not which book was used. One line: **the 0.077 gap is not within the control's
spread on the current control (0.119, bootstrap interval excludes 0), and in any case the test is a non-test -- a known non-No.-1 control
passes it -- so neither verdict is licensed; whether No. 1 reads the 1865 rows is untested by this statistic (rule 3).**

### 7. Postmortem
- Over-claims corrected: (1) E65's reading (wrong key; LS-R6's table "proceed at once to City Point", "Canby will start tomorrow" and "sender
  not decoded; Jefferson?") -- a correction note is added under LS-R6's section in NOTES.md; reading.md is left as derived until a reader
  re-files E65 in No. 2 (rule 7: never hand-edit the derived block). (2) The step-2 verdict "No. 1 reads 1865 rows" is withdrawn as a
  non-test. (3) N2-BI/N2-BM addressees: the decoded plain names Ingalls; LS-R6's table "to the quartermaster at (Pickford/Bickford)" and
  "to a quartermaster ('Palestine')" describe header words, and the OR volume searched (I/37 pt 2, I/39 pt 2) was the wrong theatre; I/40 pt 3
  searched here. (4) N2-BH page p.468 -> pp.467-468. (5) N2-BI addressee header "Bickford" on the image.
- Lesson for readers: when LS-PRE's cipher_guess disagrees with the reader's choice of book, look up three code words in both keys before
  decoding; the wrong book still yields fluent-looking plain words in a mostly-plain telegram.
- Rows: status.json one result row per N3 entry (N2-BI, N2-BJ, N2-BK, N2-BL, N2-BM, O9-AH), audit_status "one audit"; SECOND-OPINIONS-QUEUE.tsv
  rows SO-ECKERT-N2BI, -N2BJ, -N2BK, -N2BL, -N2BM, -O9AH with prompts in second-opinions/. Requests: in the ROOM done line.

Correction carried (LS-FIX, 8 Oct 2026, commit f4dba16ec): E65 withdrawn from ciphertext.txt and re-filed as N2-BO in ciphertext-no2.txt, decoded with key-no2.md; no class change.

## AUDIT (LS-V7)

Verifier LS-V7 (account 1, LANE ST-LEDGER-2, session_01PmcWWeEJMai2xhq5hXiB77), 8 Oct 2026, 04:48-05:2x UTC by `date -u`; a separate session
from every reader (LS-R7 read these entries), not protecting its conclusions. Scope: LS-R7's batch: **E66, E67, E68, E70, E72, E73, E74**
(ciphertext.txt, Cipher No. 1, key.md = mssEC 41), **N2-BN** (ciphertext-no2.txt, Cipher No. 2, key-no2.md = mssEC 47), and the two "key not in
hand" rows E69, E75 (counts only). Nothing decoded beyond re-running the committed scripts and looking code words up in the three key files.
Key source for every item: `period`. Depth under .claude/briefs/runs/2026-10-08-acct3-depth-bar.md.

**ID settled.** The files carry **N2-BN** (ciphertext-no2.txt, reading-no2.md, entries-mssEC19.tsv `already_read` "LS-R7 N2-BN (as E71)"); there is
no E71 block anywhere, and LS-R7's NOTES table already says N2-BN. "E71" was only the brief's slot; it stays unassigned. No file change needed.

### 1. Re-derivation (rule 7), which book, image check
- `decode.py --check`, `decode_no2.py --check`, `decode_no9.py --check`: exit 0 each.
- **Which book (LS-V6's E65 lesson).** Each block was decoded under all three keys (key.md, key-no2.md, key-no9.md) with decode.py's own
  machinery (scratch script, not committed); share-of-tokens alone does not separate the books (LS-V6 section, 0.374 vs 0.353), so the test is
  which key gives a sentence. H counts No. 1 / No. 2 / No. 9: E66 33/28/11, E67 14/10/4, E68 17/17/4, E70 13/12/3, E72 16/12/5, E73 9/9/3,
  E74 2/4/0 (the No. 2 "4" reads "Sanders [McLamores Cove] was an enormous blunder" -- nonsense), N2-BN 10/16/3. Under No. 1 every E-block reads as
  continuous prose with the No. 1 markers (zebra/zodiac/unity = period, yoke/webster/walrus = signed, Growl/Grapes = blind words); under No. 2
  N2-BN alone does (Coldwell "2" header, Yacht = period, Yawl = signed). **No mis-keyed entry in this batch.**
- **Image.** 2400 px IIIF images of the eight pointers to scratch; strip crops with the reader's regions, e.g.
  `python3 tools/iiif_lines.py --image $S/img/p9151.jpg --out $S/crops/9151 --prefix p9151 --region 100,1700,2300,1066 --centres 120,260,380,490,610,730,850,960 --lines-per-crop 2 --max-width 2400`,
  likewise 9075 `100,1380,2300,740`, 8985 `100,1640,2300,860`, 9118 `100,250,2300,720` (2 lines per crop) and 9039 `100,250,2300,920`, 9071
  `100,1800,2300,700`, 8914 `100,240,2300,800` (3 lines per crop); two PIL close-ups of 9151 (y 1900-2090) for "Weaselira".
  Word for word, header to tail: **E66** (9151, the longest, 12 lines), **E72** (9075, 9 lines, faint pencil), **E70** (8985, 10 lines): all agree
  with ciphertext.txt except E70 line 1, where the image reads **"Pockaing"** (c-k), not "Polkaing" (the volunteer text's form); the transcription is
  left as is (a reader's file) and the token is graded I below.
- **M tokens re-read from the image** (E68 9039, E73 9118, E74 9071 lines 1-2 and tail, plus the E66/E72/E70 ones above): every one is written as
  transcribed ("Jones", "platation", "polkers", "utopia ... utopia)", "Sand hers", "Coox Edwards", "Waymomers", "Weaselira", "Banditte",
  "Vain fleet", "Stephen son", "see see Awe gear"). What changes is the reading, from the key (section 4).

### 2. Entry located in print: confirmed by script
| ID | printed at | how confirmed |
|---|---|---|
| E67 | **ORN ser. I vol. 11** (Washington, December 3, 1864, 12:30 p.m., H. A. Wise, Chief of Bureau, to Rear-Admiral D. D. Porter), printed after Porter's telegram to Assistant Secretary Fox | IA `officialrecordso0011unse` djvu (scratch): "Your telegram to Mr. Fox of this a. m. received. Everything is being done by the bureau with the utmost vigor. The moment the Baltimore arrives she will leave again with Jeffers and Rodman to assist in fitting out the Louisiana. The Stromboli is on her way to you with [80] torpedoes on board and [2] of Beardslee's clock movements. If you have not Beardslee near you, let me know." Word for word with the ledger (page number not read: the OCR has no running head near it). **N1.** |

### 3. Entries not located: search families (8 Oct 2026)
Phrases were taken verbatim from the decoded lines (LS-V5's lesson: paraphrase misses prints). Context found on the way is listed as
context, not as a location of the entry.

| family | searched | result |
|---|---|---|
| OR / ORN by date and correspondent, +/- 3 days (IA djvu, whole volume, normalized-text regex; scratch, not committed) | E66: OR I/46 pt 2 (`warofrebellion462unit`, Jan 1865); E68, E70: OR I/39 pt 2 (`warofrebellion392unit`); E72: I/43 pt 2 (cached); E73: ORN I/26 (`officialrecordso0026unse`) and I/27 (`officialrecordso0027unse`); N2-BN: OR I/33 (cached); E74: I/43 pt 2 and I/39 pt 2 | **No entry located.** Context: **E66** -- OR I/46 pt 2 **p.28** prints Van Vliet's two replies from New York of 3 Jan 1865 to Meigs ("There are but few steamers available here at present. The Ericsson ... the Rapidan ...", received 1 p.m. and 5.30 p.m.) and the 2 Jan Stanton-Grant exchange ("there are no transports at Baltimore ... inquiry made as to transports available at New York", "probably 4,000"): the question E66 asks is answered in print, its own text is not. **E72** -- OR I/43 pt 2 **pp.142-143** prints Augur to Sheridan, 22 Sept 1864, 9.45 p.m.: "Four thousand nine hundred and twenty-four men will leave here for Winchester to-morrow morning." **E73** -- ORN I/26 **pp.209-211** prints the Bureau of Navigation's circular to commanders of squadrons of April 1864 (C. H. Davis to Porter, Mississippi Squadron): to mask signals "all succeeding signals will be made by adding 10 to the number as shown and subtracting 10 from the number as read". **N2-BN** -- OR I/33 **pp.616-617** prints Humphreys to Benham, 29 Feb 1864: "cause to be constructed as soon as practicable an advance guard train ... Twenty-four canvas pontoons ... Each chess-wagon loaded with 42 chesses" -- the order N2-BN reports on ("as ordered in your letter of the [29] ult"). **E68** -- Sam Bruch is the military-telegraph officer at Louisville/Cincinnati writing to Eckert, and Burbridge commands the District of Kentucky (I/39 pt 2), nothing on Surgeon Ferry. **E70** -- I/39 pt 2 shows Callender shipping guns from St. Louis (July 1864) and Carrington at Indianapolis, no 16 June ordnance order. OR ser. III vol. 4 (`warofrebellion0304rootrich`) "Item not available" on IA, ser. III vol. 5 an error page: **unreachable** this session. ORN I/12 (`officialrecordso0012unse`) HTTP 500 (as for LS-R7). |
| Sender's/recipient's printed papers | Lincoln (Basler) and the "Tycoon"/Sanders telegram (E74) via Google Books; Mereness Calendar (Upper Mississippi Valley War Department telegrams; Indiana) for E70 by Google Books queries; Welles diary not opened | no hit (Google Books returned the Mereness Calendar only for a different Carrington item of 8 June 1864); Mereness itself not searched inside |
| 1864-65 press (loc.gov Chronicling America JSON by date window; the old chroniclingamerica.loc.gov search API now answers 404) | E74 "Sanders despatch Stanton" 8-30 Sept 1864: 7 pages (Richmond Enquirer 13 Sept p.4 read by its OCR XML: a note on Maj. Reid Sanders' death, not the despatch; NY Herald 21 Sept p.5, Fremont Journal 9 Sept p.2, Wilmington Journal 29 Sept p.3, Burlington Free Press 30 Sept p.3 not read); E68 "Surgeon Ferry" Aug 1864: 366 loose pages (not read); N2-BN "canvas pontoon Benham" Mar-Apr 1864: 0; E66, E70, E72, E73 and E74's quoted "enormous blunder": loc.gov timed out (one try each, not retried) | no entry located; pages listed above unread |
| IA full text, all items (be-api fts) | "was an enormous blunder" Stanton; "Sanders despatch"; "signal numbers made"; "canvas pontoons will be completed"; "surgeon ferry" Burbridge; "construction corps" "coal and water" | no relevant hit (signal manuals only for "signal numbers made") |
| Google Books API (key, country=US) | 17 phrase queries over the seven entries (3 answered 503, one retry each) | no hit on any entry; for E73 the ORN I/26 circular above |
| OpenAlex, Semantic Scholar, CORE (keys) | one query per entry each (S2 answered 429 on five, not retried) | nothing relevant |
| JSTOR | 10 rows appended to JSTOR-QUEUE.tsv for E66, E68, E70, E74, N2-BN, families (i) and (ii) | pending (never blocks) |
| Unread / unreachable | NARA RG 92 (QMG telegrams sent), RG 107 (M473), RG 156 (Ordnance) and RG 45 (Navy); OR ser. III vols. 4-5; ORN I/12; the press pages listed; HathiTrust full text; Lincoln's Collected Works page search; Stanton Papers | unread |

### 4. Grades (rule 4) after the image and key re-reads
The reader's M list mostly resolves from the books; the decoder also overgrades four plain words. Per entry, H = decoder H less the plain words
it read as code; I = a book word in a clerk's spelling or a phonetic split, inferred; plain names are not cipher tokens.
- **E66** H 33, I 4, M 1. I: "Banditte" = Banditti = **Baltimore** (key.md p.11 l.8; the decoder misses the spelling), so "4000 troops from Baltimore to
  sea"; "Vain fleet" = **Van Vliet** (Brig. Gen. Stewart Van Vliet, quartermaster at New York, who answers on p.28 of I/46 pt 2); "Weaselira" =
  Weasel (Steam) + -ers, **steamers** ("report of steamers available in New York", which is the wording of Van Vliet's printed reply); the date
  (3 Jan 1865, confirmed by the printed reply). M: "Waymomers". "Pandora Wise" is **Colonel** Wise, i.e. Col. George D. Wise, quartermaster at
  Baltimore (I/46 pt 2: "Colonel Wise is in Baltimore"), **not** H. A. Wise of the Navy Bureau as LS-R7's date note says; the signature Belcher =
  Qr Master Genl U.S. (H).
- **E67** H 13, C 1 ("tar pedro" = torpedoes), "Fox" plain. N1.
- **E68** H 16, I 1, M 1. The decoder's [5] for "person" ("in person") is plain (the block needs a `plain: person` line), so H 17 -> 16. I:
  "platation" = Plate (**Communicate**) + -ation, "if you deem his **communication** trustworthy" (key.md p.19 l.12; key-no2.md logs "plantation" =
  communication as C in N2-BC). "Burr" + "patent" (Bridge, H) = Burbridge (a plain name split). M: "Jones" ("insert Jones cipher stop").
- **E70** H 11, I 1. "Ramsay" read [Effect] is the signer's plain name (H 13 -> 12 as LS-R7 says); "Polkaing" is **"Pockaing"** on the image, so
  [Commanding] rests on the clerk's slip for Polka (I, H 12 -> 11).
- **E72** H 15, I 0. "Stephen son" is **Brig. Gen. John D. Stevenson**, commanding at Harper's Ferry (OR I/43 pt 2, I/46 pt 2), a phonetic split:
  the decoder's [In the] for "Stephen" is wrong (H 16 -> 15). The signature "see see Awe gear" = **C. C. Augur** (phonetic, plain), consistent
  with Augur's printed telegram of the night before. The tail's Palate ([Brigadier General]) is the clerk's group after the name.
- **E73** H 8, I 3, M 1. I: "polkers" = Polka + -ers, **commanders**; "utopia" twice = **Utophia = Parenthasis** (key.md p.22 l.17) -- the clerk wrote
  the parentheses as well. M: "squadron", which the decoder reads [Marine] (Squadron = Marine, key.md p.21 l.25) but which reads better plain in a
  Navy telegram to a squadron commander.
- **E74** H 2 (Webster = signed, Brutus = Secretary of War), the rest clear text; "Sand hers" = Sanders (a name, unidentified), "call Coox Edwards"
  the clerk's tail. LS-R7's own note stands: the sense is read from the page, not from the key.
- **N2-BN** H 15, I 0. "Humphreys" is plain (**A. A. Humphreys**, Chief of Staff, Army of the Potomac, who wrote the order of 29 Feb): the decoder's
  [Wilmington] (Humphrey, key-no2.md) is wrong, H 16 -> 15. "Oliver Ellsworth" = 20 + 9 = **29** (H, key-no2.md fly leaf) is right and matches the
  printed order's date, so LS-R7's M on it is lifted. "The patent pewter whig of Canvass udders" = "The **[Advance] [Bridge] [Train]** of canvas
  **[Pontoon]s**" (H): the printed order calls it an "advance guard train"; LS-R7's table reading "patent pontoon bridge train" is wrong on "patent".
  "Oscar brooks" = **[42]** chess per wagon, the printed order's figure.
- **E69, E75 (key not in hand, counts only).** Over the whole transcriptions: E69 (70 tokens) H 10 under No. 1, 10 under No. 2, 4 under No. 9; E75
  (46 tokens) 7, 11, 6. None of the three gives a sentence (E69: "press the [Embark]/[Defeat] on this [Front]/[Evacuation]"; E75 "pass through
  [President of the U.S.]/[Beauregard]"). **None of the three keys reads them**; LS-R7's verdict stands.

### 5. Classification (key `period` for all)
`depth_pct` = H / (H + I + M) over the message's cipher tokens (plain names, the clerk's tail groups and check words excluded).

| ID | N-class | text known? | depth | depth_pct | check |
|---|---|---|---|---|---|
| E66 QMG (Belcher) to Horner for Van Vliet, New York, 3 Jan 1865 | **N3** | unknown | D3 | 86.8 (33 H of 38) | image, all 12 lines; external: Van Vliet's printed replies (OR I/46 pt 2 p.28) answer it: steamers available at New York, same day |
| E67 H. A. Wise to Porter, 3 Dec 1864 | N1 | known (ORN I/11) | D4 | 100 (13 H + 1 C of 14) | word for word with the print |
| E68 Stanton to Bruch, Louisville, for Burbridge, 7 Aug 1864 | **N3** | unknown | D3 | 88.9 (16 H of 18) | M/I lines re-read on the image; external: Bruch the military-telegraph officer and Burbridge commanding the District of Kentucky (OR I/39 pt 2) |
| E70 Ramsay to Capt. Smith, St Louis, for Callender, 16 Jun 1864 | **N3** | unknown | D3 | 91.7 (11 H of 12) | image, all 10 lines; external: Callender at the St Louis arsenal shipping guns, Carrington at Indianapolis (OR I/39 pt 2) |
| E72 Augur to Stevenson, Harper's Ferry, 23 Sept 1864 | **N2** | substance known (OR I/43 pt 2 pp.142-143) | D3 | 100 (15 H of 15) | image, all 9 lines; Augur's printed telegram of 22 Sept 9.45 p.m. (same troops, same morning) |
| E73 Bureau (B. F. Greene) to S. P. Lee, Mound City, 7 Nov 1864 | **N2** | substance known (ORN I/26 pp.209-211) | D2 | 66.7 (8 H of 12) | M/I lines re-read on the image; the Bureau of Navigation circular of April 1864 prints the add/subtract rule |
| E74 Stanton (Brutus) to Chas Armond, 11 Sept 1864 | **N3** | unknown | D1 | 100 (2 H of 2) | image lines 1-2 and tail; two code words only, the text is clear |
| N2-BN Benham to Humphreys, 16 Mar 1864 | **N3** | unknown | D3 | 100 (15 H of 15) | image, M lines; external: Humphreys' printed order of 29 Feb (OR I/33 pp.616-617): advance guard train, canvas pontoons, 42 chesses per chess-wagon |

- **N3 (E66, E68, E70, N2-BN; E74 at D1, not a counted solve)**: no prior plaintext or decipherment located after the logged search. Not N4: NARA
  RG 92/107/156, OR ser. III vols. 4-5, the press pages listed and HathiTrust full text are unread, JSTOR rows pending. Safe sentence (each): "Read
  at grade H with the period Cipher No. 1 book (No. 2 for N2-BN); no prior decipherment or printed text located in the Official Records (Army and
  Navy, by date and correspondent), Internet Archive full text, Google Books, OpenAlex, Semantic Scholar or CORE (searched 8 Oct 2026)." Unsafe:
  "first", "unpublished", "never printed", "unknown telegram".
- **E66 and N2-BN are weak N3 (the E62/E57 shape)**: the other half of each exchange is printed (Van Vliet's reply; Humphreys' order). A second
  audit should read the Quartermaster General's and the Engineer Brigade's letters sent, and the Meigs/Benham reports, before either is counted twice.
- **E72, E73 at N2 (the E49 precedent, AUD2-LS-E)**: the substance is printed -- E72's troop movement by the same sender the evening before, E73's
  signal rule in the Bureau's own April circular. Not counted.
- **E74 at D1**: two code words (the signature) are the whole cipher content; no clause above the authentication distance exists. N3 as a text,
  not a counted solve. "Sanders" and "Chas Armond" unidentified.
- Depth sentences (D2+, written from the reading, checked against the derived block): **E66** "On 3 Jan 1865 the Quartermaster General's office
  tells Van Vliet at New York that Colonel Wise has called for steamers to take 1,000 men of the construction corps of the U.S. Military Railroads
  from Baltimore to Savannah, and that 4,000 more troops are to go from Baltimore to sea with coal and water for fifteen days, destination not
  reported; he is to report the vessels he can send and dispatch them unless countermanded." **E68** "On 7 Aug 1864 Stanton has Captain Bruch at
  Louisville pass to General Burbridge an order to see Surgeon Ferry in person and hear his statement, to send its substance by cipher telegraph if
  he finds the communication trustworthy and important, and to send Ferry to Washington under a guard that will see he does not escape if a personal
  interview seems important." **E70** "On 16 Jun 1864 the Chief of Ordnance orders Major Callender, commanding the St Louis arsenal, to issue at once
  to General Carrington at Indianapolis four 12-pounder howitzers with implements and equipments complete and 400 rounds of assorted ammunition,
  100 of them canister, sent by a special messenger, and to report the issue by telegraph." **E72** "On the morning of 23 Sept 1864 Augur tells
  Brigadier General Stevenson at Harper's Ferry that nearly 5,000 troops leave Washington for Winchester that morning and that transportation must
  be ready for their rapid march on arrival." **E73** "On 7 Nov 1864 the Navy's bureau tells S. P. Lee, via Cairo, to have the commanders in his
  squadron make all important signals by adding a number set in his order to the signal numbers made and subtracting it from those received."
  **N2-BN** "On 16 Mar 1864 Benham reports to Humphreys that the advance bridge train of canvas pontoons ordered on 29 February will be ready that
  day, with 50 chess on each chess wagon though they can be reduced to 42, and the additional wagons sent if still needed."

### 6. Postmortem
- Corrections to LS-R7's section (a note is appended there): E66's Wise is Colonel (George D.) Wise of the Quartermaster's Department at Baltimore,
  not H. A. Wise of the Navy, and "Vain fleet", "Banditte", "Weaselira" read from the key (Van Vliet, Baltimore, steamers); E72's "Stephen son" is
  Stevenson and its signature is C. C. Augur; E73's "polkers" and "utopia" are book words (commanders, parenthesis); E68's "platation" is
  communication and "person" is plain; E70's image reads "Pockaing"; N2-BN's "patent" is [Advance], "Humphreys" plain, "Oliver Ellsworth" = 29 is H.
  Of LS-R7's 13 M tokens, 11 are resolved here (2 left: E66 "Waymomers", E68 "Jones"), and four decoder H on plain words are withdrawn.
- Not changed (no decoding in a verifier's brief): ciphertext.txt / reading.md. Next, for a reader, ~$0.3: `plain: person` (E68), `plain: Stephen`
  (E72), `plain: Humphreys` (N2-BN), `plain: Ramsay` (E70), "Banditte"/"Weaselira"/"polkers"/"utopia" variant rows or plain notes, and E70's
  "Pockaing" as the image has it.
- The filter's catch here: 1 of 8 in print word for word (E67, ORN), 2 with their substance printed (E72, E73), 2 with the other side of the
  exchange printed (E66, N2-BN). Navy traffic (E67, E73) is in ORN, which LS-PRE's or_cov never checked; a Navy row should be checked against ORN
  before it is read.
- Rows: status.json one result row per N3 entry (E66, E68, E70, E74, N2-BN), audit_status "one audit"; SECOND-OPINIONS-QUEUE.tsv rows
  SO-ECKERT-E66, -E68, -E70, -E74, -N2BN with prompts in second-opinions/; JSTOR-QUEUE.tsv 10 rows. Requests: in the ROOM done line.

## AUDIT 2 (second adversarial, AUD2-LS-G)

Verifier AUD2-LS-G (account 2, for the account-3 orchestrator), 8 Oct 2026, 05:13-05:4x UTC by `date -u`. Scope: **N2-BI, N2-BJ, N2-BK,
N2-BL, N2-BM, O9-AH** only, the six blocks LS-V6 classed N3 with one audit. This session is separate from the reader (LS-R6) and the first
auditor (LS-V6) and does not protect either's conclusion. Key source for all six: `period` (mssEC 47 Cipher No. 2; O9-AH mssEC 67).

### 1. Re-derivation (rule 7) and image check
- `python3 ciphers/eckert-1864/decode_no2.py --check` "reading-no2.md is current", `decode_no9.py --check` "reading-no9.md is current": exit 0 each.
- 2400 px IIIF images `hdl.huntington.org/digital/iiif/p16003coll11/<ptr>/full/2400,/0/default.jpg` for 9019 (N2-BM), 8925 (N2-BL), 8979, 9139,
  8937 (scratch, not committed). Crop step: `python3 tools/iiif_lines.py --image $S/img/p9019.jpg --out $S/crops/9019 --prefix p9019 --region
  150,230,1900,780 --centres 80,180,280,380,480,580,680 --lines-per-crop 4 --max-width 2400`; `python3 tools/iiif_lines.py --image
  $S/img/p8925.jpg --out $S/crops/8925 --prefix p8925 --region 150,1270,2050,970 --centres 40,120,230,330,430,530,630,740,840 --lines-per-crop 5
  --max-width 2400`.
- **N2-BM** (LS-V6 had not image-checked it): header to signature word for word with ciphertext-no2.txt ("Helen for Palestine In galls Vermont
  stop ... Stanhope About Dayton Snyder have been shipped ... Silvers to you wiley Buggy Does the star spangled banner"). **N2-BL** (not
  image-checked before): every code word as transcribed (Hunter, April, Edwards, Henrietta, Pearl, Vermont, Quotient, Talbot, Ginger, Tulip,
  Parston, Yardstick, Rusty, Brown, Yacht, Ruffle, Girdle, yawl, Buggy); the image has a small mark after "Chief" (no effect) and the hyphenated
  "Hola-bird" as transcribed. N2-BI was checked word for word by LS-V6 and not repeated.

### 2. Families searched (the ones LS-V6's section 4 did not cover first, then the press of the day)
| family | searched | result |
|---|---|---|
| OR volumes LS-V6 did not search (IA djvu, whole volume, regex on flattened text) | **ser. I vol. 32 pt 3** (`warofrebellion323unit`, Sherman's division, Apr 1864; N2-BL), vol. 35 pt 2 (`warofrebellion352unit`, Pensacola; N2-BL), vol. 37 pt 2 (`warofrebellion372unit`, July 1864; N2-BI), vol. 51 pt 1 (`warofrebellion511unit`, supplement; all six); re-read: vol. 33 (O9-AH), 34 pt 3, 36 pt 1 and pt 3 (N2-BJ), 40 pt 3 (N2-BI, N2-BM), 43 pt 2 (N2-BK, including the index), ser. III vol. 4 (`warofrebellionco0004genf`) | **N2-BL: substance printed**, OR I/32 pt 3 **p.300**: "WASHINGTON, April 8, 1864 -- 3.30 p. m. Lieutenant-General GRANT: I have to-day ordered 40,000 bushels of grain and 700 tons of hay from eastern ports to Pensacola under sealed orders. First shipment to be made by steam, to arrive by the 1st of May; all by the 10th. Also sent by Mississippi and Atlantic orders to Colonel Holabird, chief quartermaster New Orleans, to send a cargo of forage from New Orleans to Pensacola, to be there by the 1st of May to meet any contingency. M. C. MEIGS, Quartermaster-General." N2-BL is the order that sentence reports, sent an hour earlier (2.30 PM) "Via Cairo, copy via N. Y." (= "by Mississippi and Atlantic"). **N2-BM: the reply is printed**, OR I/40 pt 3 **p.555**: "CITY POINT, VA., July 28, 1864 -- 10 a. m. (Received 3.30 p. m.) Quartermaster-General U. S. Army: There is no necessity for more mules until the Nineteenth Corps arrives here. ... RUFUS INGALLS" -- the answer to N2-BM's "do you need more mules?"; N2-BM's own text (500 shipped, the rest held, horse shipments stopped) is not printed. **O9-AH: context printed**, OR I/33 (Halleck to "Capt. G. D. Wise, Assistant Quartermaster, Baltimore", 16 Apr 1864, 5 p.m.): proceed to Philadelphia and New York, consult Colonel Crosman and Major Van Vliet, send light-draught steamers and vessels to Fort Monroe -- the errand O9-AH (20 Apr) continues; O9-AH's text (Butler's 30,000 men, 2,000 horses, ten batteries, coaled by the 25th) not printed. I/43 pt 2's index lists no Quartermaster-General correspondence with Sheridan (N2-BK). Nothing for N2-BI, N2-BJ, N2-BK |
| Papers of Ulysses S. Grant (ed. J. Y. Simon), IA be-api full text inside lending-only items | vol. 10 (`papersofulyssess0010gran`, Jan-May 1864: Pensacola, Holabird, contingency, cargo of forage, Van Vliet, G. D. Wise, Butler/Fort Monroe), vol. 11 (`papersofulyssess0011gran`: more mules, cavalry horses, vouchers, depreciation, Wade/Senator, Dana/Wade), vol. 12 (`papersofulyssess0012gran`: chief quartermaster/Sheridan/revoke). Vol. 13 (Nov 1864-Feb 1865, N2-BK) is not on IA; the publisher's open PDFs at scholarsjunction.msstate.edu answered HTTP 403 to one request per volume (vols 10-13), not retried | **vol. 10 prints the same Meigs telegram as OR I/32 pt 3 p.300** in a note ("... orders to Col. Holabird Chief Quarter Master New Orleans to send a cargo of forage from New Orleans to Pensacola to be there by 1st first May to meet any contingency" LS (telegram sent), DNA, RG 107; index: Holabird 267n), with Grant's request to Meigs to "make provision at Pensacola Florida for five thousand (5000) cavalry for twenty (20) days" that prompted it. Vol. 11: Meigs's June report of cavalry horses shipped to White House (not N2-BI); nothing for N2-BI's 24 July figures, N2-BM or N2-BJ. Nothing for O9-AH, N2-BK (vol. 12) |
| Sender's and recipient's printed papers | Butler, *Private and Official Correspondence* vols 3-4 (IA `privateofficialc03butl`, `privateofficialc04butl`; Jan-May 1864; O9-AH); Dana, *Recollections of the Civil War* (`recollectionsofc00danauoft`; N2-BJ); Sheridan, *Personal Memoirs* vol. 1 (Gutenberg 2651 via IA; N2-BJ, N2-BK); Heitman, *Historical Register* vol. 1 (`historicalregist01heitrich`; N2-BJ) | Butler: Van Vliet appears only on 1 May 1864 (Weitzel), no O9-AH text; Dana and Sheridan: nothing on Wade's appointment; Heitman: "Wade, James Franklin. Ohio ... 6 cav 3 Aug 1861; lt col 6 U S c cav 1 May 1864; col 19 Sept 1864 ... bvt capt 9 June 1863 for gal and mer ser in the battle of Beverly Ford" -- agrees with N2-BJ's "[Lieutenant] [Colonel] Wade ... served as [Captain] of [Cavalry] in the [Army of the Potomac] & distinguished himself for pluck & gallantry" (biographical context, not the telegram) |
| 1864 press, Chronicling America (loc.gov JSON, `dates=` window), keyword queries unlike LS-V6's quoted phrases | N2-BJ `Colonel Wade Sheridan staff` 1 Jun-15 Jul (30 pages) and `Wade son of Senator Wade cavalry` May-Aug (330); O9-AH `Van Vliet chartered vessels Fortress Monroe` 15 Apr-5 May (3); N2-BL `Holabird Pensacola` Apr-Jun (0); N2-BI `Meigs cavalry horses depreciation vouchers` 15 Jul-31 Aug (0); N2-BK `quartermaster Sheridan chief quartermaster assignment revoked` Dec (0) | the three O9-AH pages (NY Daily Tribune 16 Apr p.5, 25 Apr p.6, 5 May p.7) read through their OCR: Van Vliet's advertisements for cavalry and artillery horses, not the telegram; the N2-BJ result lists are war news (Wade Hampton, Trevilian), nothing on their faces about J. F. Wade's appointment; not read page by page |
| Google Books API (key, country=US), quoted phrases | "most capable and most worthy" quartermaster; "chief quartermaster to your army"; "son of the Senator" Wade Sheridan staff; "fresh for their morning"; "depreciation of vouchers and certificates"; "need more mules" Ingalls; "cargo of forage" Pensacola Holabird; "thirty thousand men" "two thousand horses" Butler | the Holabird telegram in OR (1891, the I/32 pt 3 text above) and in the Grant Papers; the Ingalls reply (OR 1892, I/40 pt 3); Wilson 2006 (LS-V6's context for N2-BI); nothing for N2-BI's, N2-BJ's, N2-BK's or O9-AH's own wording; two 503s (not retried) |
| OpenAlex, Semantic Scholar, CORE | not re-run: LS-V6's six name/event queries cover these entries, and every lowering in this round came from print, not scholarship | -- |
| JSTOR | LS-V6's 12 rows (families i and ii) stand; none added | pending (never blocks) |
| Unread / unreachable | NARA RG 92, RG 107 (Meigs's and Stanton's telegrams sent); Grant Papers vol. 13 (403); the press page by page; HathiTrust full text | unread |

### 3. Classification (key `period`)
| ID | LS-V6 | AUD2-LS-G | depth | reason |
|---|---|---|---|---|
| N2-BI Meigs to Ingalls, 24 July 1864 | N3 | **N3 held** | D2 kept, 96.7 | no prior text located in the families above; Halleck's 24 July orders to send surplus horses to the Army of the Potomac (OR I/37 pt 2, I/40 pt 3) are context only |
| N2-BJ Secretary of War to Dana, 4 June 1864 | N3 | **N3 held** | D2 kept, 95.7 | Dana, Sheridan, the Grant Papers and OR I/36 carry nothing on the appointment; Heitman agrees with the decoded rank and service (lt col of colored cavalry from 1 May 1864, cavalry service and brevet for gallantry in 1863) but is a register, not a check of this telegram's code values; not raised |
| N2-BK Meigs to Sheridan, 12 Dec 1864 | N3 | **N3 held** | D2 kept, 90.9 | OR I/43 pt 2 (text and index) and Sheridan's memoirs: nothing; Grant Papers vol. 13 unreachable (the weakest remaining gap; named below) |
| N2-BL Meigs to Holabird, 8 Apr 1864 | N3 | **N2 (lowered)** | **D3 (raised with the check)**, 100 (17 H) | substance printed: OR I/32 pt 3 p.300 and Grant Papers vol. 10 (note to p.267) quote Meigs's report to Grant of the same afternoon -- orders to Colonel Holabird, chief quartermaster New Orleans, to send a cargo of forage to Pensacola to be there by 1 May to meet any contingency, with grain and hay from eastern ports. The E26/E28/E49 kind of N2 (content in print, no prior mapping of this ciphertext), not N1: the print is Meigs to Grant, not N2-BL; N2-BL's "storms may delay it" and "confidential" are not in it. External check: the code words read Colonel (Pearl), Quarter Master (Vermont), New Orleans (Ginger), Forage (Rusty), 1 (Brown) and New York (Girdle; the print's "eastern ports") agree with the print; image checked here. Not counted |
| N2-BM Meigs to Ingalls, 27 July 1864 | N3 | **N3 held** | D2 kept, 100 | Ingalls's reply of 28 July 10 AM is printed (OR I/40 pt 3 p.555, "no necessity for more mules until the Nineteenth Corps arrives"); it shows the question was asked but does not give N2-BM's text (500 shipped, the rest held, horse shipments stopped). The reply checks the plain words, not a code value ([Brig. General], [Quarter Master] only as Ingalls's own signature), so depth is not raised; image checked here |
| O9-AH to Capt. G. D. Wise, New York, 20 Apr 1864 | N3 | **N3 held** | D2 kept, 100 | OR I/33 prints Halleck's 16 Apr order sending Wise to New York to work with Van Vliet on vessels for Fort Monroe, which agrees with the code words Captain, Quartermaster, Major and Fort Monroe; Butler's Correspondence and the Grant Papers carry nothing of O9-AH's figures. Kept at D2: the 16 Apr text checks the addressee's errand, not the telegram's content; a later verifier may weigh it as the external check (it is the same kind LS-V1 used for E21) |

- **N3 held (N2-BI, N2-BJ, N2-BK, N2-BM, O9-AH)**: no prior plaintext or decipherment located after both audits' searches. Not N4: NARA RG 92/107,
  Grant Papers vol. 13 (N2-BK), the press page by page and HathiTrust are unread; JSTOR pending. Safe sentence (each): "Read at grade H with the
  period Cipher No. 2 book (O9-AH: the War Department's older vocabulary, mssEC 67); no prior decipherment or printed text located in the
  Official Records (ser. I and III by date and correspondent), the Papers of Ulysses S. Grant vols 10-12, the senders' and recipients' printed
  papers, the 1864 press through Chronicling America, Internet Archive full text, Google Books, OpenAlex, Semantic Scholar or CORE (searched
  8 Oct 2026; two audits)." N2-BM adds: "Ingalls's reply is printed (OR I/40 pt 3 p.555)." Unsafe: "first", "unpublished", "never printed".
- **N2-BL: N2.** Safe sentence: "Read at grade H with the period Cipher No. 2 book; the order it carries is reported in Meigs's telegram to Grant
  of the same afternoon, printed in the Official Records (ser. I vol. 32 pt 3 p.300) and the Papers of Ulysses S. Grant vol. 10; N2-BL's own
  wording was not located in print." Unsafe: "unknown telegram", "not in print".
- Next step for N2-BK (the one family that could still move it): Grant Papers vol. 13 for Dec 1864 (a person's browser at scholarsjunction.msstate.edu
  or a library copy).

### 4. Postmortem
- Over-claim corrected: N2-BL was N3 (LS-V6 section 5, status.json, SO-ECKERT-N2BL). LS-V6 searched I/34 pt 3 (the Gulf) for the date and
  correspondent; the print is in I/32 pt 3, under the recipient Meigs reported to (Grant), not the recipient of the cipher (Holabird). Lesson
  (the same as E49/E54): search the volume of the person the sender reported to that day, not only the cipher's recipient's theatre.
- Understatements filled: N2-BL now has an external check (D3); N2-BM has its printed reply; N2-BL and N2-BM were image-checked for the first time.
- Rows: status.json N2-BL grade N2 (`plaintext_novelty` N2, `mapping_novelty` N3), depth D3, not counted; N2-BI, N2-BJ, N2-BK, N2-BM, O9-AH
  `audit_status` "two audits"; SECOND-OPINIONS-QUEUE.tsv SO-ECKERT-N2BL withdrawn (N2); the other five stay queued (class unchanged).

## AUDIT 2 (second adversarial, AUD2-LS-F)

Verifier AUD2-LS-F (account 4, for the account-3 orchestrator), 8 Oct 2026, 05:37-05:5x UTC by `date -u`; brief
`.claude/briefs/runs/2026-10-08-acct3-ledger2.md` "AUD2-LS-F / -G". A separate session from the readers (LS-R2c, LS-R5) and the first
auditors (LS-V2c for E33, LS-V5 for E57, E59, E62); not protecting any of their conclusions. Nothing decoded beyond `--check`. Key source
for all four: `period` (the War Department's Cipher No. 1 book, key.md = mssEC 41).

### 1. Re-derivation (rule 7) and image check
- `python3 ciphers/eckert-1864/decode.py --check`: "reading.md is current", exit 0.
- Huntington IIIF `hdl.huntington.org/digital/iiif/p16003coll11/<pointer>/full/2400,/0/default.jpg` for 9055, 8927, 8951, 8921 (scratch,
  not committed); PIL strip crops of each entry's body (9055 rows 250-1330; 8927 rows 260-1060; 8951 rows 1180-1720; 8921 rows 1760-2640),
  read by eye against ciphertext.txt:
  - **E33 (9055)**, all ten lines from "McCaine H. Ferry ... Aug 22 1864" to "Reading - ped Wal - rus. Chisel plane ax Saw": agree.
  - **E57 (8927)**, header "Geo W. Baldwin (1) navy Plan Progress ... Washn Apr 8th 1864" and all seven body lines ("Julia , For , Pilgrim ,
    Thomas , Vinton , Unity , If" ... "duty Yoke Meigs Bender his on one"): agree; pencil interlinear glosses ("wanted", "Beecher",
    "Progress", "over game on file") are the clerk's, not message text, as LS-V5 said.
  - **E59 (8951)**, header "F S Van Valkenburg ... Washn 1130 am Apl 27 1864" and the five body lines: agree, including "there" struck
    through after "Efficiency" (the reading omits it).
  - **E62 (8921)**, lines 4-8 at full resolution ("to take Whist to Hilt on head Unity Give her" ... "any arrivals of Weasel hers
    Confidential South Meigs Belcher Viola") and lines 1-3 at contact-sheet resolution: agree; margin "93 or dy gps sent 12.30 PM Tinker",
    the 12.30 tail time the reading carries.
  No transcription correction.

### 2. Families LS-V2c / LS-V5 did not cover (or could not read), searched here (8 Oct 2026)
| family | searched | result |
|---|---|---|
| 1864 press, Chronicling America (loc.gov JSON, `dates=` window), **pages read through their ALTO OCR** (LS-V5's OCR fetch had failed) | E57 "steamer Relief Annapolis colored troops" 7-20 Apr: all **17** result pages read (Memphis Appeal, Worcester Spy 13 and 14 Apr, Springfield Weekly Republican, Chicago Tribune 13/14/16/20 Apr, NY Tribune 14 Apr, Natl Intelligencer 20 Apr, Muscatine Journal, NY Herald 15 Apr, St Paul Pioneer, Portland Press, Evening Star 19 Apr, NY Dispatch, Litchfield Enquirer); E59 "Eleventh Michigan Cavalry" 25 Apr-20 May (45 pages, first 15 read, 2 truncated), including LS-V5's Cleveland Morning Leader 29 Apr p.4; E62 "Montauk Spaulding Fortress Monroe" 5-20 Apr (0 pages); E33 "Twenty-fifth New York cavalry Harper's Ferry" 20 Aug-10 Sept (54 pages, 11 read; then loc.gov answered HTTP 429 and the pass stopped there, per the good-citizen rule) | **no hit for any of the four.** E57: every "Relief" hit is a relief society, a Confederate dispatch or an advertisement; nothing about the steamer Relief or colored troops embarking at Annapolis. E59: the Cleveland Leader page is a 4th Michigan Cavalry desertion story; the Evening Star 18 May page carries a Cavalry Bureau horse advertisement (Ekin), not E59. E33: nothing on the forge train or the 25th New York Cavalry |
| OR volumes the first audits did not search (IA djvu, whole volume, regex on flattened text) | ser. I **vol. 38 pt 4** (`warofrebellion384unit`, Sherman, May 1864; E59), **vol. 51 pt 1** (`warofrebellion511unit`, supplement; all four), **vol. 43 pt 2** (`warofrebellion432unit`; E33, LS-V2c read pt 1 and 2 by narrower terms); re-read vol. 32 pt 3, vol. 33, vol. 35 pt 2, vol. 43 pt 1 with the regexes: Eleventh/11th Michigan Cavalry + Cavalry Bureau/efficiency/impaired/no use/sent to the field; steamer Relief/staunch/Montauk/Spaulding/two propellers/arrivals of steamers/Hilton Head (Apr 4-9); train of forges/forges and other/Twenty-fifth or 25th New York Cavalry/mounted and equipped/First and Third Cavalry Divisions | **no hit for the four texts.** Context only, as the first audits found: I/32 pt 3 has the 11th Michigan Cavalry at Camp Nelson and Lexington under Hobson in March-April ("one of the most efficient regiments in the service", Sturgis's roster report) and Hobson to Col. S. B. Brown, Lexington, 27 Apr (fugitive negroes in his camp) -- the same day as E59, but not its subject; I/33 p.814 Biggs's 6 Apr reply (received 1.30 p.m.) -- one hour after E62's 12.30 send time, and it answers E62's "report your supply of coal" ("Can spare a thousand tons coal") and "orders to Spaulding" ("Spaulding not yet arrived. Will give her orders as soon as she comes in"), i.e. Biggs's reply is printed, Meigs's E62 is not; I/43 pt 1 itinerary (25th NY Cavalry assigned 24 Aug) and pt 2 (the regiment at Smithfield 6 Sept) |
| Grant Papers (the person the senders reported to; AUD2-LS-G's lesson), IA be-api full text inside lending-only items | vol. 10 (`papersofulyssess0010gran`, Jan-May 1864): "Michigan Cavalry", Montauk, Spaulding, "staunch steamer", Relief Annapolis; vol. 12 (`papersofulyssess0012gran`, Aug-Nov 1864): forges, "25th N.Y. Cav"; two further vol. 12 phrase calls returned a non-JSON (5xx) reply, not retried | vol. 10: only the 7th Michigan Cavalry (Feb 1864), nothing for E57, E59, E62; vol. 12: nothing for E33 |
| Regimental / state records | Phisterer, *New York in the War of the Rebellion* vol. 2 (`newyorkinwarofre02phisrich`), 25th Cavalry sketch (E33) | context only: "at Washington, D. C., 22d Corps, from July 7, 1864; in the 4th Brigade, 1st Division, Cavalry, Army of Potomac, from August, 1864" -- agrees with E33's regiment leaving Washington for Sheridan's cavalry in late August; not the telegram |
| Huntington full text (CONTENTdm `CISOSEARCHALL`, coll11) | forges, Montauk (LS-V5's call returned empty; re-run), Spaulding, Thayer | forges: 3 leaves -- 9055 (E33 itself), **9827 = mssEC 18 p.161**, McCaine, 26 Aug 1864 ("The forges coal &c had [?] sent from here ... he will get ready") -- a later telegram that refers to the same forges, not a copy of E33; 10184 (mssEC 10, a raid report, unrelated). Montauk 21 and Spaulding 17 leaf hits by title only (pages in mssEC 05-19, not read one by one; 8920 = mssEC 19 p.28 is the neighbouring leaf of E62's p.29); Thayer 48 (leaves of 1865 books, not read) | no second copy of the four texts found |
| IA full text, all items (be-api fts), fresh quoted phrases | "of no use at Lexington", "its efficiency is being impaired", "good staunch steamer", "Montauk and two other", "other two propellers", "probably scarce at Annapolis", "report daily any arrivals", "load of colored troops" Annapolis, "train of forges", "forges and other wagons", "Eleventh Michigan Cavalry" Lexington Halleck | only Biggs's 5 Apr reply in five OR copies ("Montauk and two other similar propellers") and unrelated modern uses; nothing for the four texts |
| Google Books API (key, country=US), fresh quoted phrases | "Michigan Cavalry is of no use"; "Eleventh Michigan Cavalry" "of no use" and "efficiency is being impaired" cavalry 1864 (each 503 once, answered on the one retry); "Relief" "staunch steamer" Annapolis; "call at Annapolis" "colored troops" 1864 Meigs; "Montauk and other two propellers"; "plenty of coal" Annapolis Meigs Biggs 1864; "small train of forges"; "Twenty-fifth New York Cavalry" August 1864 forges; "25th New York Cavalry" "350 men" | loose matches on common words (OR reports of other dates, Army and Navy Gazette, regimental histories, Lee's Bold Plan for Point Lookout on the 25th NY's July 1864 dismounted service); nothing for any of the four texts |
| OpenAlex, Semantic Scholar, CORE | not re-run: the first audits' name/event queries cover these entries, and every lowering in this round came from print or the press, not scholarship | -- |
| JSTOR | the first audits' 8 rows (E33 2, E57/E59/E62 6; families i and ii) stand; none added | pending (never blocks) |
| Unread / unreachable | NARA RG 92 (QMG telegrams sent, Apr 1864), RG 107 (M473), RG 393 (Augur's letters sent); the Meigs letterbooks; Sherman's printed correspondence page by page (*Sherman's Civil War*, 1999; not on IA full text); the 11th Michigan Cavalry's *Record of Service*; the remaining E59 (30) and E33 (43) Chronicling America result pages (loc.gov 429); HathiTrust full text (Cloudflare) | unread |

### 3. Classification (key `period`)
| entry | class | prior plaintext | depth | % H/C/S (unchanged) | check |
|---|---|---|---|---|---|
| E33 to McCaine for Sheridan, 22 Aug 1864 | **N3** (held) | none located | D3 (held) | 93.3 | image all lines, fresh `--check`; OR I/43 itinerary and Phisterer agree with the regiment's move; mssEC 18 p.161 (26 Aug) refers to the same forges |
| E57 Meigs to Capt. Thomas, quartermaster, 8 Apr 1864 | **N3** (held) | none located | D3 (held) | 80.0 | image all lines; Halleck's 5 Apr memo (OR I/35 pt 2 p.37) prints the plan |
| E59 Washington (General-in-Chief) to Sherman, 27 Apr 1864 | **N3** (held) | none located | D3 (held) | 92.3 | image all lines; OR I/32 pt 3 places the regiment at Lexington under Hobson that week |
| E62 Meigs to Biggs, Fort Monroe, 6 Apr 1864 | **N3** (held, weakest) | none located; the reply is printed | D3 (held) | 90.9 | image; OR I/33 p.814 Biggs's reply, received 1.30 p.m., one hour after E62's 12.30 send, answers its coal and Spaulding clauses |

- **All four held at N3**: no prior plaintext or decipherment located after two logged searches. Not N4: NARA RG 92/107/393, the Meigs
  letterbooks, Sherman's printed correspondence page by page, the remaining Chronicling America pages and HathiTrust full text are unread,
  and JSTOR rows are pending. No depth raised or lowered; the depth sentences in LS-V2c and LS-V5 section 4 stand (each is a true, specific
  sentence the reading supports, checked against reading.md; the authentication-distance figures are the first audits', not recomputed here).
- **E62** stays the weakest: its answer is in print, timed one hour after it, and answers two of its clauses. That is evidence the telegram was
  sent and received as read, not a printing of it. If Meigs's 6 Apr text turns up in RG 92's letters-sent edition or a Quartermaster's
  report, it drops to N2/N1. E57 is the same shape one step removed (the plan printed, the order not).
- Safe sentence (each): "Read at grade H with the period Cipher No. 1 book; no prior decipherment or printed text located in the Official
  Records (ser. I and III by date and correspondent, including the supplement vol. 51 pt 1), the Grant Papers, the 1864 press in Chronicling
  America (pages read in OCR), the Huntington collection's full text, Internet Archive full text or Google Books (two audits, 8 Oct 2026)."
  Unsafe: "first", "unpublished", "never printed", "new", "unknown telegram".

### 4. Postmortem
- No over-claim found in the four rows. LS-V5's press family was a result list, not a read (its OCR fetch failed); this audit read the pages
  through `page[].url` (text/xml ALTO) on the loc.gov resource JSON, which works where `tile.loc.gov` `ocr.txt` did not -- the route for the
  next audit. loc.gov rate-limited at about 45 page fetches inside ten minutes; pace one page per 3 s or spread over sessions.
- Rows: status.json E33, E57, E59, E62 `audit_status` "two audits", audit_refs and gap updated, class and depth unchanged;
  SECOND-OPINIONS-QUEUE.tsv rows SO-ECKERT-E33/-E57/-E59/-E62 stay queued (no count or class changed).

## AUDIT 2 (second adversarial, AUD2-LS-H)

Verifier AUD2-LS-H (account 2, for the account-3 orchestrator), 8 Oct 2026, 06:12-06:4x UTC by `date -u`; brief
`.claude/briefs/runs/2026-10-08-acct3-ledger2.md` "AUD2-LS-H". A separate session from the reader (LS-R7) and the first auditor (LS-V7);
not protecting either's conclusion. Scope: **E66, E68, E70, N2-BN** only (E74 stays D1, not audited). Nothing decoded beyond `--check`.
Key source for all four: `period` (Cipher No. 1, key.md = mssEC 41; Cipher No. 2, key-no2.md = mssEC 47, for N2-BN).

### 1. Re-derivation (rule 7) and image check
- `python3 ciphers/eckert-1864/decode.py --check`: "reading.md is current", exit 0; `decode_no2.py --check`: "reading-no2.md is current", exit 0.
- Huntington IIIF `.../p16003coll11/<pointer>/full/2400,/0/default.jpg` for 9151, 9039, 8985, 8914 (scratch, not committed); PIL strip crops
  (9151 rows 1700-2766; 9039 rows 250-1170; 8985 rows 1640-2500; 8914 rows 240-1040), read by eye against ciphertext.txt / ciphertext-no2.txt:
  **E66** all 11 lines header to "counter man dead before they start yoke Belcher all sober": agree. **E68** header and lines 1-9 ("Grapes Topsy
  postpone ..." to "adequate saddle that will take care he does"): agree (the tail line below the crop was eye-checked by LS-V7). **E70** all 9
  lines: agree, and line 1 reads **"Pockaing"** as LS-V7 found (the transcription's "Polkaing" stays a reader's file; graded I as LS-V7 did).
  **N2-BN** header "Coldwell "2" Wash D.C. Mar. 16. 1864" and all 7 lines to "H. W. Benham Br. Genl.": agree. No transcription correction.

### 2. Families LS-V7 did not cover (or could not read), searched here (8 Oct 2026)
| family | searched | result |
|---|---|---|
| OR volumes the first audit did not open (IA djvu, whole volume, regex on flattened text) | ser. I **vol. 47 pt 2** (`warofrebellion014702rootrich`, Jan 1865; E66), **vol. 44** (`warofrebellion0144rootrich`, Dec 1864; E66, N2-BN), **vol. 52 pt 1** (supplement), **vol. 51 pt 1** (supplement), **vol. 38 pt 5** (Aug 1864; E68: Bruch-Eckert correspondence pp.716, 740, 789, 800), **vol. 36 pts 1-2** (Benham's engineer reports; N2-BN); ser. II **vol. 7** (`warofrebellion0207rootrich`, prisoners/political arrests, June-Dec 1864; E68, E70). Regexes: construction corps / Van Vliet / military railroads ... Savannah / coal and water for fifteen / 4,000 men ... Baltimore / steamers available / Colonel Wise; Surgeon Ferry / Dr. Ferry / Bruch / personal interview with me / adequate guard; Callender / Carrington ... howitzer / special messenger; canvas pontoon / advance (guard/bridge) train / chess-wagon / 42 or 50 chess | **no hit for any of the four texts.** Context only: **E66** -- I/47 pt 2 **pp.59-60**, Sherman to Grant, Savannah, 16 Jan 1865: "The Secretary told me I would surely receive 4,000 men from Baltimore to garrison Savannah. They are not heard of here yet" (and later in the volume, p.68, "The first installment of General Grover's division, which is to garrison Savannah, has just arrived"); I/44 **p.834**, McCallum to Sherman, 29 Dec 1864: "I am instructed to send military railroad operatives to Savannah ... Col. W. W. Wright ... will shortly leave for Savannah with a sufficient force". Both confirm E66's two movements (the 4,000 troops from Baltimore, the construction corps to Savannah) as events; neither prints E66, the Quartermaster General's request to Van Vliet for vessels. **E68** -- Bruch's I/38 pt 5 telegrams to Eckert are about lines and repairs; nothing on Surgeon Ferry. **N2-BN** -- I/44 and I/47 pt 2 canvas-pontoon passages are of Dec 1864 and Feb 1865 |
| Huntington full text (CONTENTdm `CISOSEARCHALL`, coll11) -- sibling telegrams | Ferry, "surgeon ferry", Ferry+Bruch, Ferry+Burbridge; Carrington; Callender; Van Vliet, Horner+Vliet, Vliet+construction, Vliet+steamers+Baltimore, Wise+steamers+Savannah, construction+Savannah; Benham, Benham+canvas, Benham+chess, Humphreys+pontoon, canvas+pontoon, pontoon | **E70: a sibling copy states its substance in clear.** Pointer **9760**, page 94 of the volume "United States Military Telegraph, War Department. Sent, Jany. 21, 1864 -- Dec. 7, 1865" (parent 10074), "JW Wallach 12 M Indianapolis Washn June 16th 1864", carries in the Huntington's public transcription two telegrams of Ramsay's of the same day and hour: to Capt. J. M. Wittemore, commanding the Indianapolis arsenal ("Four mountain howitzers complete with ammunition have been ordered to Genl Carrington ... Render him all the aid you can"), and **"another to Genl Carrington period I have ordered to be Sent you from St Louis Arsenal with quick dispatch and by special messenger four mountain howitzers complete with four hundred rounds of ammunition signed Brig Genl Ram say"** -- E70's order (St Louis arsenal, quick dispatch, special messenger, four howitzers complete, 400 rounds) in plain words, without the canister split, the implements and equipments, or Callender's name. Also **12537** (vol. 3, Telegrams Received, Maj. Eckert, June 10 - July 25 1864, leaf 101): Geo H. Smith, St Louis, 20 June, "Cipher message for Callender was recd through the Commercial Office ... one word short ... sent by mounted orderly to arsenal" -- the receiving end of E70 (and the "Capt Smith" of its header), manuscript only. **E66, E68, N2-BN: no sibling copy found**: Horner+Vliet's 18 leaves are 1864 forage/transport traffic (e.g. 9699, 9710: Apr 1864), 9766/9874/9923 undated in the snippet and on other subjects; Benham's chess/canvas leaves (5471, 7486, 8426, 8428, 7505) are Oct-Nov 1863 Humphreys-Benham traffic; 7781 is Feb 1865; the Ferry hits are places (Harper's, Conrad's, Budd's Ferry) |
| 1864-65 press, Chronicling America (loc.gov JSON `dates=` window; pages read through their ALTO OCR, `page[].url` text/xml, one page per 3 s) | E66: "Van Vliet" 2-20 Jan 1865 (12 pages; 3 read: Worcester Spy 14 Jan p.2 -- Van Vliet's brevet in a promotions list; NY Tribune 16 Jan p.7 and NY Dispatch 8 Jan p.8 -- advertisements/lodge notices; Natl Intelligencer 15 Jan p.2 answered 429, not retried); "Grover Baltimore Savannah steamers" 2-25 Jan 1865 (56 pages; Evening Star 13 Jan p.1, Natl Intelligencer 2 and 5 Jan p.3, Wheeling Intelligencer 4 Jan p.1, Portland Press 5 Jan p.2 read for "from Baltimore": railway timetables only); "construction corps Savannah" (114 pages, not read). E68: "Surgeon Ferry Burbridge" 5 Aug-15 Sept 1864, all **9** pages (8 read; Natl Intelligencer 23 Aug p.2 timed out): every "Ferry" is Harper's or Turner's Ferry, except Burlington Hawk-Eye 20 Aug p.5 on **Capt. J. H. Ferry** of the quartermaster's department appointed colonel -- a different man and office; "Surgeon Ferry Louisville" (98 pages, not read). E70: "howitzers Carrington Indianapolis" 14 Jun-20 Jul 1864: **0** pages. N2-BN: "canvas pontoons" 10 Mar-15 Apr 1864, all **6** pages read (Chicago Tribune 1 and 14 Apr, National Democrat 2 Apr, Trinity Journal 19 Mar, NY Herald 14 Apr p.8): **0** OCR hits for "canvas pontoon"; "pontoon train Benham": 0 pages | **no hit for any of the four** |
| Sender's/recipient's printed papers | Grant Papers vol. 13 (Jan 1865; E66) by IA be-api: the item answered 0 for a "Sherman" control query, so this route does not index it -- **unreachable** this way; Mereness Calendar (E70): not on IA by title search; Lincoln, Stanton, Meigs, Benham, Humphreys: no printed letterbook for these dates found | unreachable / none |
| IA full text, all items (be-api fts), fresh quoted phrases | "coal and water for fifteen days" (502 twice, not retried further); construction corps + military railroads + Baltimore + Savannah + Van Vliet; "steamers available" + Van Vliet + Wise; "Surgeon Ferry"; "adequate guard" Ferry; "twelve-pounder howitzers" Carrington Indianapolis; "mountain howitzers" Carrington Indianapolis 1864; "canvas pontoons" Benham Humphreys March 1864; "chess-wagon" Benham | nothing for the four texts ("Surgeon Ferry" only a 1906 Tampa quarantine officer and modern items; "chess-wagon" Benham only field-fortification textbooks and OR I/33, the Cornell copy LS-V7 read) |
| Google Books API (key, country=US), fresh quoted phrases | "coal and water for fifteen days"; "construction corps" "Baltimore to Savannah"; "Surgeon Ferry" 1864; "see Surgeon Ferry"; "Surgeon Ferry" Burbridge; "Surgeon Ferry" Stanton 1864; "four 12-pounder howitzers" Carrington; "howitzers" Carrington Callender 1864; "one hundred of which to be canister"; "canvas pontoons will be completed"; "advance bridge train" canvas pontoons 1864; "fifty chess" OR "50 chess" pontoon Benham | loose matches on common words only (Medical and Surgical History, registers, a 1927 Farmer's Weekly); nothing for any of the four |
| OpenAlex, Semantic Scholar, CORE | not re-run: LS-V7 ran one query per entry each, and every lowering in this round came from print, the press or a sibling copy, not scholarship | -- |
| JSTOR | LS-V7's rows (JSTOR-QUEUE.tsv rows 394-403: E66, E68, E70, N2-BN in both families (i) and (ii)) stand; none added | pending (never blocks) |
| Unread / unreachable | OR ser. III vols. 4-5 (not on IA; HathiTrust coo.31924079575373/-365/-381 Cloudflare; the HTRC Extracted Features API answered HTTP 500 "No primary node is available" twice); NARA RG 92, RG 107 (M473), RG 156, RG 77 (Engineers); the Huntington Sent volume read page by page around 3 Jan 1865, 7 Aug 1864 and 16 Mar 1864 (only its full-text index was searched); the unread Chronicling America result pages listed above; HathiTrust full text | unread |

### 3. Classification (key `period`)
| entry | class | prior plaintext | depth | % H/C/S (unchanged) | check |
|---|---|---|---|---|---|
| E66 QMG (Belcher) to Horner for Van Vliet, 3 Jan 1865 | **N3** (held, weak) | none located; the replies (I/46 pt 2 p.28) and both movements as events (I/47 pt 2 pp.59-60, I/44 p.834) are printed | D3 (held) | 86.8 | image all lines, fresh `--check` |
| E68 Stanton to Bruch for Burbridge, 7 Aug 1864 | **N3** (held) | none located | D3 (held) | 88.9 | image lines 1-9, fresh `--check`; Surgeon Ferry unidentified in OR I/38 pt 5, I/39 pt 2, II/7 and the press |
| E70 Ramsay to Capt. Smith for Callender, 16 Jun 1864 | **N2** (lowered from N3) | **substance known**: Ramsay's same-hour telegram to Carrington, in plain words in the Huntington's public transcription of the War Department Sent book p.94 (pointer 9760) | D3 (held) | 91.7 | image all lines, fresh `--check`; the received side 12537 (Smith, 20 June) confirms delivery |
| N2-BN Benham to Humphreys, 16 Mar 1864 | **N3** (held, weak) | none located; the order it answers is printed (I/33 pp.616-617) | D3 (held) | 100 | image all lines, fresh `--check` (No. 2) |

- **E70 lowered to N2 (the E72/E49 precedent).** The plaintext substance of E70 -- four howitzers complete with 400 rounds, sent from the St Louis
  arsenal with quick dispatch by special messenger to Carrington at Indianapolis -- is public: Ramsay's own telegram to Carrington of the same
  hour, transcribed in clear on the Huntington site (Sent book p.94). Our reading adds the canister split, "implements and equipments", the
  instruction to report by telegraph and the addressee Callender; no prior mapping of E70's ciphertext to its text was found. Not counted as a solve
  at N3. Safe: "Read at grade H with the period Cipher No. 1 book; the order's substance is in Ramsay's same-day telegram to Carrington (Huntington,
  War Department telegrams sent, p.94), no prior decipherment of this entry located." Unsafe: "first", "unpublished", "unknown order".
- **E66, E68, N2-BN held at N3**: no prior plaintext or decipherment located after two logged searches. Not N4: OR ser. III vols. 4-5, NARA RG
  92/107/77, the Huntington Sent volume page by page, the remaining press pages and HathiTrust full text are unread, and JSTOR rows are pending.
  **E66** stays weak and is weaker than after LS-V7: its reply and both its movements are in print as events; if the Sent volume carries a clear
  copy of the 3 Jan message (the E70 shape), it drops to N2. **N2-BN** stays weak (the order it answers is printed). E68 is the strongest of the
  four: Surgeon Ferry is unidentified in every family searched.
- Depth: no depth raised or lowered; LS-V7's section 5 depth sentences stand (each re-read against reading.md / reading-no2.md and true of the
  reading; the authentication-distance figures are LS-V7's, not recomputed here). E70's depth stays D3 (depth is independent of the N-class).
- Safe sentence (E66, E68, N2-BN): "Read at grade H with the period Cipher No. 1 book (No. 2 for N2-BN); no prior decipherment or printed text
  located in the Official Records (ser. I and II by date and correspondent, with the supplements), the Huntington collection's full text, the
  1864-65 press in Chronicling America (pages read in OCR), Internet Archive full text or Google Books (two audits, 8 Oct 2026)." Unsafe: "first",
  "unpublished", "never printed", "new", "unknown telegram".

### 4. Postmortem
- One drop, from a family neither LS-R7 nor LS-V7 searched: the **Huntington's own transcriptions of the War Department's sent books**, which
  carry same-hour sibling telegrams in clear. A first audit of a mssEC 19 entry should run `CISOSEARCHALL` on the addressee's and the subject's
  names across coll11 and read every same-date hit before classing N3 (here: "Carrington", 3 hits, one the sibling). The route costs a few calls.
- Rows: status.json E66, E68, N2-BN `audit_status` "two audits", audit_refs and gap updated, class and depth unchanged; E70 `grade` N2,
  `audit_status` "two audits", line and gap rewritten. SECOND-OPINIONS-QUEUE.tsv: SO-ECKERT-E70 withdrawn (N2); SO-ECKERT-E66, -E68, -N2BN stay
  queued (no count or class changed). No JSTOR row added.

## AUDIT 2 (second adversarial, D2V-E74)

Verifier D2V-E74 (account 2, LANE DEFAULT-account-2-20261008-0710, session_01GWXLUH2ZBG9tHhixnLF26u), 8 Oct 2026, 07:21-07:4x UTC by `date -u`;
a separate session from the reader (LS-R7) and from LS-V7, not protecting either. Scope: **E74 only** (mssEC 19 p.177 printed / p.179,
pointer 9071). Nothing decoded beyond `decode.py --check` (exit 0). Outreach gate 2 emphasis: search to disprove novelty.

### 1. The two open pointers, identified
- **"Sanders' despatch"** = George N. Sanders' telegram from St Catharines, C.W., 1 Sept 1864, to "Hon. D. Wier, Halifax": "Platform and
  Presidential nominee unsatisfactory. Vice President and speeches satisfactory. Tell Philmore not to oppose. Geo. N. Sanders." It was made
  public by **Seward in his Auburn speech of 3 Sept 1864**, which read it out as evidence of a Chicago-Richmond compact (Daily National
  Intelligencer, Washington, 8 Sept 1864, p.2, read through its ALTO OCR, loc.gov resource sn83026172/1864-09-08/ed-1 sp=2); the Portland
  Daily Press of 9 Sept p.2 reprints it as "a despatch to his co-laborer ... in the British Provinces", and the Philadelphia Evening Telegraph
  of 12 Sept p.1 prints Sanders' "intercepted dispatch" reply to Seward from Clifton House, 9 Sept. The Danville Quarterly Review (1864)
  quotes it too (Google Books snippet). So the date fits exactly: published 3-8 Sept, E74 on 11 Sept. The Tycoon/Niagara pointer of the
  brief is the right man (Sanders of the Clifton House), but the despatch is the 1 Sept Halifax telegram, not the July Niagara letters.
  Whether "Tycoon" here is Lincoln (Hay's usage) or Seward, who spoke, the page does not say; not settled here.
- **"Chas Armond"** = a War Department telegraph operative sent to Halifax. Huntington CONTENTdm full text (`CISOSEARCHALL^armond`,
  p16003coll11, 4 leaves): mssEC 29 (Vol. 4, Telegrams Received, Maj. Eckert, 25 Jul-16 Sep 1864) leaf 341 (pointer 12323): "St John [N.B.]
  Sept 2 ... Maj Eckert We arrived here this Eve ... Shall reach our destination tomorrow noon ... Armond . D H Opr"; leaf 348 (12330):
  "Halifax Sept 3, Maj TT Eckert, We arrived this evening ... Armond"; mssEC 18 p.169 (9835): "Chas Armond Halifax Washn Sept 6th 1864 ...
  Your [wrangle] rec'd & I'm obliged to you tis very important to watch [Shelby] ... who he associates with how he talks and what he is at
  ... for I think he means mischief on the Pacific coast [signed] [Bruno]" (cipher, not decoded here). Armond reached Halifax on 3 Sept,
  the day Seward published a telegram addressed to a Confederate agent at Halifax: E74 is the War Department telling its man there that
  the publication (which exposed the interception) was not its doing. Context only, from catalogue transcriptions; not a print of E74.

### 2. The deciding finding: E74's text is already public
The Huntington's own catalogue record for pointer 9071 (dmGetItemInfo `transc` field; transcribers M. Underwood, K. Peck; digitised
23 Nov 2015; Zooniverse "Decoding the Civil War" subject 2880343) carries E74 word for word: "Chas Armond Washn 8 pm Sept 11th 1864 | The
public = nation of Sand hers despatch was an enormous blunder Twas done by the Tycoon without my knowledge I did not know he had seen it
until too late and four saw the consequences would be very bad It cannot happen again Webster Brutus call Coox Edwards". For a cipher
entry the public transcription is ciphertext; for E74 it is the plaintext, except the two signature code words. The only thing our reading
adds is "Webster Brutus" = "[signed] [Secretary of War]" (key.md p.10 l.19, H), from a period key that is itself digitised. So the
plaintext is published by the holding archive: **N1** (the E70 shape of AUD2-LS-H, but stronger: this item's own record, not a sibling).

### 3. Search log (8 Oct 2026)
| family | searched | result |
|---|---|---|
| Huntington CONTENTdm full text (`CISOSEARCHALL`, coll11) | armond (4), Tycoon (1 = 9071), blunder (17, only 9071 relevant), Sanders (12: none Sept 1864), Sanders+despatch (0), Sanders+Weir (0), Wier (1, 1862, unrelated); item info for 9071, 9835, 12323, 12330, 8728, 8754, 3036 | **9071's public transcription = E74's text**; Armond's three sibling leaves (section 1) |
| 1864 press, Chronicling America (loc.gov JSON `dates=` window, ALTO OCR, 3 s apart) | "Sanders despatch" 1-12 Sept (14 pages; 6 read: Evening Star 6 Sept p.1, Worcester Spy 9 Sept p.4, Portland Press 9 Sept p.2, Phila Evening Telegraph 12 Sept p.1, Wheeling Intelligencer 6 Sept p.3, Fremont Journal 9 Sept p.2); "Philomons" (1 = Portland); "Sanders Chicago platform satisfactory" 28 Aug-30 Sep (54 pages; Natl Intelligencer 8 Sept p.2 read; Dayton Empire 6 Sept, NY Herald 7 and 13 Sept answered 429) | Sanders' despatch and Seward's use of it located (section 1); E74 itself, or any report of the War Department disowning the publication, not found in the 7 pages read. First request of the session met a Cloudflare page; one retry after a pause answered; stopped on the 429 |
| IA full text (be-api fts) | "enormous blunder" Tycoon; Sanders despatch "enormous blunder"; "without my knowledge" Tycoon Stanton 1864; "cannot happen again" Stanton Tycoon | nothing relevant |
| Sender's/recipient's printed papers | Lincoln, Collected Works vol. 8 (Basler; IA `collectedworksab08linc`, `collectedworksof0008royp_m9a6`, be-api per item, "Sherman" control answered): "Halifax" 0, "Armond" 0, "enormous blunder" 0; Bates, *Lincoln in the Telegraph Office* (1907, IA `lincolnintelegra00bates` djvu, whole text grep): Armond, Tycoon, Wier, Philmore, "enormous blunder" 0 (Halifax only for the Keith/Nov 1864 matters); Stanton papers: no printed letterbook for Sept 1864 found | no print of E74 |
| Google Books API (key, country=US) | 5 queries ("enormous blunder" Sanders Seward Auburn; "Tell Philmore not to oppose"; "Armond" Halifax 1864 Eckert; Stanton Sanders Wier Halifax intercepted; "done by the Tycoon" -- 503, not retried) | 1 hit, Danville Quarterly Review 1864, for Sanders' telegram only |
| OpenAlex, Semantic Scholar (keys) | 2 queries each (Sanders telegram Halifax interception; Seward Auburn speech Sanders telegram) | nothing relevant |
| JSTOR | families (i) and (ii) already queued (JSTOR-QUEUE.tsv rows 400-401, LS-V7); one family (i) row added for "Armond" AND Halifax AND 1864 | pending (never blocks) |
| Unread / unreachable | Zooniverse "Decoding the Civil War" Talk boards (where volunteers may have discussed the entry); the Huntington blog; NARA RG 107; HathiTrust full text; the 429'd press pages; Seward's Works vol. 5 (the speech, context only) | unread |

### 4. Classification
| ID | N-class | text known? | key | depth | check |
|---|---|---|---|---|---|
| E74 Stanton ([Secretary of War]) to Chas Armond, Halifax, 11 Sept 1864 | **N1** (lowered from N3) | **known**: the Huntington's public transcription of pointer 9071 | period | D1 (unchanged) | `--check` exit 0; catalogue `transc` field read against ciphertext.txt E74: identical but for the struck "the", which the Huntington keeps as plain "the" |

- Safe sentence: "E74 is clear text signed with two Cipher No. 1 code words, read at grade H as '[signed] [Secretary of War]' with the period
  book; its text is in the Huntington's public transcription of mssEC 19 (pointer 9071). The 'Sanders despatch' is George N. Sanders'
  1 Sept 1864 telegram to D. Wier at Halifax, which Seward read out at Auburn on 3 Sept; 'Chas Armond' is the War Department operative at
  Halifax who telegraphed Eckert on 2-3 Sept (Huntington mssEC 29 leaves 341, 348)." Unsafe: "unknown telegram", "previously unread",
  any word implying the text was not available.
- Depth: D1 stands (2 cipher tokens, no clause above the authentication distance). Not a counted solve, and not an N3.
- Postmortem: LS-V7 classed the text "unknown" without reading the item's own public transcription; for an entry that is mostly clear text
  that record is the first place a print check should look. The identifications in section 1 are this audit's; they rest on press OCR
  and catalogue transcriptions, not on images read here.
- Rows: status.json results[179] grade N1, text known, audit_status "two audits"; SO-ECKERT-E74 withdrawn (N1: second opinions are queued
  only at N3 or better). Requests: Huntington 14, loc.gov about 21 (1 challenge, 3 answered 429; stopped), be-api 14, archive.org 3, Google
  Books 5, OpenAlex 2, Semantic Scholar 2.
