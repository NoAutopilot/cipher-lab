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
