# AUDIT: George W. Erving to James Monroe, Lisbon 23 May 1806 (LOC Monroe Papers mss33217 reel 3 frames 0828-0830)

Verifier KHF-1 verifier (account 1, for acct3-orchestrator), 7 Oct 2026 20:58-21:2x UTC by `date -u`; brief
`.claude/briefs/runs/2026-10-07-acct1-khf1-verifier.md`. A session separate from the solver (KH4-D, LANE KH-4) and the
check-solved/grading worker (KHF-1, session_01LdaWpkFdQ4Q6GVN9huMpM7); it did not decode and does not protect their
conclusions.

Claim under audit (NOTES.md "Ciphertext and reading", "Grading (KHF-1...)"): five coded lines (34 groups) read under
the WE028 Monroe-Madison code table as "[Randolph asked] when Mister Monroe would return home -- the president
[answered] not until his successor arrives. [the other bluntly observed that he] Mister Monroe would be the next
president."; grades H29 M4 I1 of 34; shuffled-key control 0/200; en18 judge PASS at N=105; check-solved verdict `open`.

## Verdict

| item | N-class | key | prior plaintext | prior decipherment | depth |
|---|---|---|---|---|---|
| Erving to Monroe, 23 May 1806, coded lines L01-L05 (34 groups) | **N0** | `published` (WE028, Tomokiyo's modern transcription of the period Monroe-Madison table, cryptiana.web.fc2.com/code/WE028.txt, credited) | **yes** -- Irving Brant, *James Madison: Secretary of State, 1800-1809* (Indianapolis: Bobbs-Merrill, 1953; vol. IV of his *James Madison*), text at his note 12 of the chapter | **yes** -- Brant states the passage was received "in cipher and placed in his papers without an interlining. Deciphered a century and a half later, it reads: ..." | **D3**, about 85% (29/34 H) |

`text: known` (Brant 1953). The reading here is an independent re-decipherment of a passage already deciphered and
printed; it adds nothing to the known text except the per-group mapping and grades.

Brant's printed text (Google Books snippets, volume ids eJMOAQAAMAAJ and EZDg2pMJdYMC -- both are Brant vol. IV,
Google's metadata mislabels one as 1941/"Virginia revolutionist"; the same sentence is in IA `jamesmadison0000irvi`,
1953, by be-api full-text search): "Monroe received from George Erving in cipher and placed in his papers without an
interlining. Deciphered a century and a half later, it reads: 'It is said that Randolph asked when Mr. Monroe would
return home. The President answered, not until his successor arrives. The other bluntly observed that he, Mr. Monroe,
would be the next President.' [12] As far as it goes, that may well be correct, but it omits the salient fact that a
special envoy was soon to sail with authority to take Monroe's place." Page number not established (snippet view;
the IA copy is lending-only and be-api gives no page locator) -- a page check is the one open detail, not a blocker.

**Safe sentence:** "The coded passage in George W. Erving's letter to James Monroe of 23 May 1806 (LOC, Monroe Papers,
reel 3) reads, under the published WE028 Monroe-Madison code, 'when Mr. Monroe would return home -- the President
[answered] not until his successor arrives ... Mr. Monroe would be the next President'; the same passage was
deciphered and printed by Irving Brant, *James Madison: Secretary of State, 1800-1809* (1953), and our per-group
reading agrees with his text word for word."

**Unsafe sentences:** anything calling the reading new, unread, unpublished, a first decipherment or a discovery;
"key identified" or "key recovered" (the key is a published table, and Brant read the passage before us); "previously
undeciphered" (the 1891 and 1904 calendars do not read it, but Brant did); the check-solved verdict "open".

## 1. Extract

- Date/place: Lisbon, 23 May 1806. Sender George W. Erving (US chargé at Madrid, travelling via Lisbon). Recipient
  James Monroe (minister in London). Holding: Library of Congress, James Monroe Papers mss33217, Series 1, reel 3,
  frames 0828-0830 (coded lines on 0829, right page).
- Ciphertext (`ciphertext.txt`): 34 WE028 groups in five lines, inside clear text ("Randolph asked", "answered",
  "the other bluntly observed that he"). Re-checked here: `python3 ciphers/erving-monroe-1806/decode.py --check`
  exits 0 (rule 7); every group's value checked by grep against `tools/data/uscodes-1800/WE028.tsv` (34/34 as
  `reading.txt` gives them); the debug overlay `images/f829_lines_debug.jpg` and crop `f829_L04.jpg` viewed: the clear
  words in brackets are on the page as NOTES.md says; L04's middle group is overwritten with "137" interlined and its
  last group is at the crop edge, as graded.
- Distinctive phrases searched: "until his successor arrives", "would be the next President", "bluntly observed",
  "Erving to Monroe" + "May 23, 1806", "placed in his papers", "Erving in cipher".
- What the solver/check-solved searched (NOTES.md): 1904 and 1891 calendars, Preston vol. 5 table of contents,
  Hamilton *Writings* IV, Founders Online (Madison), DECODE dumps, Bourdeau and Aymeloglu clones, six web searches,
  three blog site searches, Google Books phrase queries (reported "no result" for "Monroe would be the next
  President").

## 2. Search log (this session, 7 Oct 2026)

| family | what was searched | result |
|---|---|---|
| (a) canonical series / calendars | not re-run (1891 calendar entry "Remarks about Randolph in cipher" and 1904 calendar p.39 stand as quoted by KHF-1) | list the letter, do not read the cipher |
| (b) sender/recipient editions; Monroe and Madison biographies | Google Books API (key, country=US) phrase queries; IA be-api full text in Ammon, *James Monroe: The Quest for National Identity* (`jamesmonroequest00ammo`, `jamesmonroequest0000ammo`), McGrath, *James Monroe: A Life* (`jamesmonroelife0000mcgr`), Brant 1953 (`jamesmadison0000irvi`) | **Brant 1953 prints the deciphered passage** (above). Ammon and McGrath: no quotation of this passage found by "Erving", "successor", "next president" |
| (b') Preston, *Papers of James Monroe* vol. 5 annotation | not reachable this session (KHF-1: Google Books PARTIAL with a captcha on search-inside; not on IA/HathiTrust) | unreachable; moot for the class -- Brant already settles N0 |
| (c) Randolph literature | IA be-api "Erving" in Adams, *John Randolph* (`johnrandolphhenr00adamrich`), Bruce, *John Randolph of Roanoke* (`johnrandolphofro0002bruc`, `randolphroanoke02brucrich`), Garland (`lifejohnrandolp07garlgoog`): no hit. Google Books "Monroe would be the next President": 7 hits, among them Brant (both ids), *History of American Presidential Elections 1789-1968* (1971; the 1808 essay, which carries the same sentence and goes on to Randolph's followers urging Randolph's appointment to London), MacPhee, *The Tertium Quid Movement* (1959, note 86), Tolles, *George Logan of Philadelphia* (1953; a different context) | Brant is the decipherment; the 1971 and 1959 hits repeat the content (not read past the snippet) |
| (c') Weber, *United States Diplomatic Codes and Ciphers 1775-1938* (IA `unitedstatesdipl0000webe`; Google Books -LPDbMLRY2wC) | be-api "Erving", "Lisbon", "Randolph" | **cites this very letter** as a use of the Monroe-Madison code: "After Monroe's April 1806 dispatch, George Erving wrote to Monroe from Madrid in the code ... Erving to Monroe, Madrid, February 5, 1806 and Lisbon, May 23, 1806, in JMP, R 3." No decipherment of it in the snippets. KHF-1's log calls Weber "WE028 background, not this letter" -- corrected in NOTES.md |
| (d) holding archive / project pages | LOC item (viewed by the solver, no interlining -- consistent with Brant's "without an interlining"); UMW Papers of James Monroe pages not re-fetched | -- |
| (e) full text IA, Google Books | IA be-api global: "until his successor arrives" (281 hits, all modern), "Erving" "23 May 1806" (47, none this letter), "Erving to Monroe" 1806 Lisbon (Weber, McGrath), "Erving to Monroe" "May 23, 1806" (Cox, *West Florida Controversy* -- other letters); Google Books 11 queries (above) | Brant, Weber |
| (f) solver repositories, blogs | not re-cloned (KHF-1 grep at named commits stands); Tomokiyo's WE028 page `sources/cryptiana/web/state.htm`: no Erving-Monroe item (KHF-1, by grep) | no decipherment there |
| (g) scholarship | not run: the class is settled by a printed decipherment (N0); OpenAlex/S2 cannot lower it further. JSTOR: two rows queued (below) | -- |

JSTOR-QUEUE.tsv rows added (step 2g, both families): (i) `Erving AND Monroe AND 1806 AND (cipher OR code) AND
Randolph`; (ii) `"not until his successor arrives"`. They cannot change N0 and may be waived.

Requests this session: be-api.us.archive.org 26 (two returned no JSON, logged as unreachable for that query);
archive.org 7 (advancedsearch 5, metadata 2); www.googleapis.com/books 11. No 403/429.

## 3. Classification reasoning

N0: the plaintext and a decipherment of this very passage are in print -- Brant (1953) says Monroe received it "in
cipher ... without an interlining" and that it was "deciphered a century and a half later", then prints the clear text.
Brant's words match this project's reading group for group ("when Mr. Monroe would return home ... not until his
successor arrives ... he, Mr. Monroe, would be the next President"), so this is the same item, not a sibling.
Evidence quality: high (verbatim match of a 20-word passage, same sender, recipient, cipher, archive). Confidence: high.

## 3a. Depth (rule 4a)

29 of 34 groups H (85.3%); M 4, I 1; no unread group. Check used: a non-statistical external check -- Brant's printed
decipherment agrees with every one of the 34 groups' values as read (including the four M and the one I token: N, ar,
X, mon, ter all fit Brant's words) -- plus the shuffled-key matched control (0/200). D3 ("largely deciphered, about
85%"). Not D4: five tokens are below H/C/S on the solver's grades and no fresh rule-7 re-derivation has been run. The
M and I tokens could be regraded C against Brant's text (rule 4: known plaintext) by a solver session; with a fresh
rule-7 re-derivation that would meet D4 -- a suggestion, not done here.

Depth sentence (true, specific): Erving reported to Monroe, in code, that Randolph had asked the President when Monroe
would come home, was told not until his successor arrived, and retorted that Monroe would be the next President.

## 4. Postmortem

Failure: check-solved returned `open` on a passage whose decipherment is printed in a standard Madison biography.
The phrase search on the decoded words -- the one the brief's step 2 names -- finds Brant in one Google Books call
("successor arrives" Monroe Randolph), and KHF-1's own log says its Google Books query "Monroe would be the next
President" returned no result, while the identical query here returned seven, two of them Brant. Either the query
differed or the call failed silently; either way a "no result" from one call was logged as a negative without a
positive control. Second miss: Weber was found and set aside as background although his note cites this very letter.
Lesson: for a reading whose topic is a known historical episode (the 1806 Randolph-Monroe succession talk), search the
decoded clear-text phrases in the standard biographies of all three principals (Madison as well as Monroe and
Randolph) before calling the item open; the recipient's edition (Preston) was not the only place it could be printed.

Corrections made: NOTES.md status line `open` -> `found-solved` with the Brant citation; the "Web and blog check"
Weber line and the check-solved verdict annotated; NOTES.md "Ciphertext and reading" gains a pointer here. No
SECOND-OPINIONS-QUEUE.tsv row (N0, below N3). status.json not touched (the parent's file): suggested fields
`novelty: N0`, `key: published`, `text: known`, `depth: D3`, `depth_pct: 85`, `decode_status: Partially decrypted`,
claim scope "independent re-decipherment of a printed reading (Brant 1953)" -- not a counted result.
