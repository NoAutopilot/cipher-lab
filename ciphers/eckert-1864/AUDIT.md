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
| 5 | Grant Papers vol 10; Sherman's Civil War; Sherman Memoirs; Iowa regimental records | partly | IA full-text search hits Papers of U. S. Grant vol 10 (annotation quoting E6: "Cavalry can be mounted at St. Louis. Its last orders were for Vicksburg. Where shall it go."—Telegram, copies ...); the volume is lending-only, page not read; Sherman's Civil War lending-only, not searched; Sherman Memoirs vol 2 (IA) no hit; Roster and Record of Iowa Soldiers vol 4 and Ingersoll no hit | E6 also quoted in PUSG 10 |
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
  of the Navy] Fox". Code tokens H 9, M 1 ("Brenton"); 10 of about 63 words.
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
  of Ulysses S. Grant vol 10 (1982; IA full-text hit, page not read). Related: Halleck to Davidson 27 Apr, OR
  I/34 pt 3 p.309; Davidson to Sherman 29 Apr, OR I/32 pt 3 p.537.
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
