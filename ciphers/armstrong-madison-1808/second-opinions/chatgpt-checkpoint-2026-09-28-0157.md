# Armstrong–Madison checkpoint — bound the Barlow reply search

UTC: 20260928T015729Z
Objective: defensible, reproducible decipherment of Armstrong to Madison, 20 February 1808.
Target status: partial. Batch status: completed catalogue and public-text check. No decipherment, key match, or novelty claim.

## Parent, lease and publication provenance

- Parent: https://github.com/NoAutopilot/cipher-lab/pull/62
- Immutable parent head: `82615437594d70c8ef616e0f0579caad69c28cdc`
- Parent path: `ciphers/armstrong-madison-1808/checkpoints/20260928T015051Z.md`
- Parent normalized local UTF-8 SHA256: `93bae7f0ec2af38c87f7db803dff8bf8d7e8c74ac4b151200d2f3c5d15dccc1d`.
- Chain: #62 → #61 (`be687a68c63ee9b5f56ffc89c968ecda262a21c4`) → #60 → earlier checkpoints → bootstrap #44 (`58df6cf8c070c780df86faeec30900729f9229ba`). Closed unmerged predecessors remain valid.
- Fresh all-state discovery at start and before publication found #62 newest, open; parent files verified one added file, zero deletions. Parent reports no running batch; no active lease for this investigation appeared. Separate H18 not taken.
- Fresh branch `second-opinion/armstrong-checkpoint-20260928T015729Z`, based on current remote main `20d62cf4853614b630817747630380ea01b717d4` observed immediately before creation.
- Sole repository addition: `ciphers/armstrong-madison-1808/checkpoints/20260928T015729Z.md`. Never merge. Existing files, main, shared registers, TSV queues, other automations and outreach untouched.

## Completed: specific incoming and outgoing locators

The parent correctly left the sender/date of the cipher-key answer received on 14 June1813 unverified. This batch expands the catalogue search beyond Warden.

| OAC record | Catalogue description | Physical locator | Evidentiary limit |
|---|---|---|---|
|131321|Thomas Barlow → JQA, Paris, American Legation, **20 April1813**, 1p|MHS Adams Family Papers, reel415|Specific incoming candidate; text and receipt docket not read|
|131335|JQA → Thomas Barlow, St Petersburg, **22 April1813**, 2p|MHS letterbook copy, reel138|Outgoing witness candidate; not established as a reply to the letter dated two days earlier|
|131200|John C. Delprat → JQA, **Brodie, 23 March1813**, 1p|MHS Adams Family Papers, reel415|Potential transit evidence, not a read account of forwarding|
|131252|John C. Delprat → JQA, **Vienna, 7 April1813**, 1p|MHS Adams Family Papers, reel415|Potential forwarding evidence; contents unverified|
|131327|JQA → David B. Warden, St Petersburg, **21 April1813**, 2p|MHS letterbook copy, reel138|Parallel outgoing correspondence; contents unverified|

Each record was read in full at:
- https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=131321
- https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=131335
- https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=131200
- https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=131252
- https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=131327

The two April20/22 letters are **not established as a letter-and-reply pair**. Their catalogue proximity cannot bridge the Paris–St Petersburg transit time. The incoming April20 letter is a candidate for the answer received June14 solely because of date, place, author and subject context from the parent; actual content must decide.

## Completed: bounded coverage and source checks

1. General MHS catalogue query **1 March–14 June1813**, with num=1000, reported **1–480 of480** results. The downloaded full result page includes the five locators above, Warden4March already in #62, and Speyer correspondence. This replaces a narrow author assumption with an explicit date-bounded catalogue inventory. Broad date-span records are included;480 is the website's result count, not480 relevant letters.
2. Following the author link exposed by OAC131321, a **Thomas Barlow, either author or recipient, 1 January–31 December1813** query reported **1–2 of2** results: exactly OAC131321 and131335. This is catalogue scope only, not an assertion that only two Barlow letters survive anywhere.
3. **14June1813 line-a-day diary, vol23 p264**: full editorial entry mentions Romanzoff's invitation, Harris, garden walk and crowd; does not identify the incoming letter. **Vol49 p364** entry is a weather table, not an alternative correspondence diary. **22April1813 main diary, vol28 p475**: full editorial entry concerns Norman/Gosler passports, church service, newspapers and reading; does not identify the outgoing Barlow letter's contents. Manuscript images for these three entries were not inspected; these scoped negatives rely on the editorial text.
   - https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v23-1813-06-p264--entry14
   - https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v49-1813-06-p364--entry14
   - https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v28-1813-04-p467--entry22
4. Public 1913 AAS pamphlet **Correspondence of John Quincy Adams,1811–1814**, Charles Francis Adams, IA `correspondenceof01adam`: metadata and full OCR acquired; introduction describes familiar family correspondence between Russia and Quincy. Case-insensitive searches for Barlow, Delprat, cypher, cipher returned zero. This is one OCR witness, not proof that a diplomatic letter is absent from all printed editions. No image-backed negative claimed.
   - https://archive.org/details/correspondenceof01adam
5. Parent recovery fence extracted programmatically and its script hash checked. Existing scratch copies of parent context-feb/context-june, Ford4 OCR/PDF were verified against the parent's embedded exact input hashes before reuse. No old solver or search was rerun.

## Source failures and uncertainty

- Search-engine queries for exact Barlow/Adams dates returned mostly irrelevant material and did not locate letter text. No absence inference.
- A search result for the SHAFR newsletter PDF `https://jewlscholar.mtsu.edu/bitstream/mtsu/5989/1/pass%2032_04_ocr.pdf` appeared relevant to Barlow/Warden custody, but direct retrieval failed with a local proxy connection error, and the web reader returned403. The article was **not read** and no finding relies on it. Do not repeat unchanged endpoint attempts.
- Earlier blocked endpoints and weak solver approaches were not repeated.
- Catalogue pages expose collection and microfilm references, not images of these letters. No cipher values were seen in this batch. No target token assignments were made (H/C/S target counts remain0 for this batch).
- Do not elevate #62's likely12February1813 outgoing dispatch locator (OAC131078, reel138; bracketed Warden attribution) to a proved pair.
- Preserve #61's distinction between the temporary Adams private1809 cipher and official Department cipher. Preserve #60's retraction of the false January1806 reel gap. No connection between the1813 witness and the1808 target key is established.
- Target transcription unchanged:366 groups,216 distinct, SHA256 `c4ba5db4b1d7bc509b6ab531f6ba90dc9be4d06a3e62b43159c431742e0bc9b2`;1841/1843 and203/200 remain provisional.

## Exact next action

**Retrieve the contents or receipt docket of MHS OAC131321, Thomas Barlow to JQA, Paris20April1813, reel415, using a public image or printed witness.** Check whether it explicitly names the February dispatch and lack of key, and whether its receipt is dated14June. If public access cannot be located, check the adjacent **Delprat7April1813, OAC131252/reel415** or **Adams22April1813, OAC131335/reel138** for the cipher/clear-copy reference. Do not requery the completed catalogue scopes or assume identity from chronology. No archival request or other outreach is authorized.

Completed: catalogue inventories, five exact holdings records, three diary-text checks, one bounded printed-source OCR check, recovery verification. Running: none. Blocked: actual incoming letter/receipt docket and cipher/plain duplicate not yet acquired. There is no material blocker requiring user action. Continue with another public witness route rather than restarting old solver searches.

## Minimal reproducible recovery

Exact URLs, byte lengths and SHA256 hashes for **12 acquired inputs** are embedded below. Parent input hashes remain in #62. Recovery writes only to a fresh temporary directory outside the repository. Extract this fence programmatically; run `python recover.py /directory/with/inputs` for offline validation or `python recover.py --fetch`. Dynamic source changes stop for review. Offline validation executed successfully:12 input hashes,8 catalogue assertions and four scoped OCR zero-count checks. These validate saved evidence and coverage, not a decipherment.

Recovery script SHA256: `4b789e426be1f07e4e660051f655b4f3b3d1df666fa3ac909b59acf2b8d1179a`.
Post-publication one-file/parent/equality checks will be recorded in the PR body.

```python
import pathlib,tempfile,urllib.request,hashlib,json,re,html,sys
out=pathlib.Path(tempfile.mkdtemp(prefix="armstrong-barlow-recovery-"))
manifest=[{'name': 'catalog-mar-jun1813.html', 'url': 'https://www.masshist.org/adams-resources/slipfile/search.php?ds_m=03&ds_d=01&ds_y=1813&de_m=06&de_d=14&de_y=1813&form=sbya&num=1000', 'bytes': 198878, 'sha256': '085630e25351dc9b64ce0de7f9825ecf4c1fe5d8668beb817ab781cd5be34213'}, {'name': 'catalog-barlow1813.html', 'url': 'https://www.masshist.org/adams-resources/slipfile/search.php?addP%5B%5D=barlow-thomas&addPT%5B%5D=either&addPD%5B%5D=Thomas%20Barlow&ds_m=01&ds_d=01&ds_y=1813&de_m=12&de_d=31&de_y=1813&form=sbya&num=1000', 'bytes': 6419, 'sha256': '27779d72e0a902e5e86b18de51a7e8aacc88cc9dec375df10b8cf96be98daf75'}, {'name': 'correspondence-metadata.json', 'url': 'https://archive.org/metadata/correspondenceof01adam', 'bytes': 23175, 'sha256': 'a48a0582c7a01b509ec6d88e3c65f3622405dcca3fe642257b5dfd838fc528b2'}, {'name': 'correspondence-ocr.txt', 'url': 'https://archive.org/download/correspondenceof01adam/correspondenceof01adam_djvu.txt', 'bytes': 194622, 'sha256': '8d99cd78b2c92f2287ef0702700c126965449c449a606c4f2e47ddeccdeec394'}, {'name': 'slip131321.html', 'url': 'https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=131321', 'bytes': 3527, 'sha256': '49794de0b3bdbdc8cae5f7cf68a6e4f749d9b4fac715f5c1b41dd240e8face9f'}, {'name': 'slip131335.html', 'url': 'https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=131335', 'bytes': 3424, 'sha256': 'd4191a6ef7e2d9f179162ab69cba7b2ff973a8f3945edb2a20c3dcce48276c40'}, {'name': 'slip131200.html', 'url': 'https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=131200', 'bytes': 3498, 'sha256': 'c8ad2e7905f9cb1aed19c8c8560621e98d81366c4409c82e1ada6218eb53f83c'}, {'name': 'slip131252.html', 'url': 'https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=131252', 'bytes': 3496, 'sha256': '2b5dda8ed58df7a2a5479888d5dcb9961cb05372d98c7bfd4688d7080b0dcf7f'}, {'name': 'slip131327.html', 'url': 'https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=131327', 'bytes': 3464, 'sha256': '3417f756abee1556b6d94f9cd0aa22bd3df20a37b2985f77d86c51a309c5afd3'}, {'name': 'diary0614-v23.html', 'url': 'https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v23-1813-06-p264--entry14', 'bytes': 30952, 'sha256': '1e3a387b8353e9d53056079381f85272f4cdad276788389c564027dc272ad86f'}, {'name': 'diary0614-v49.html', 'url': 'https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v49-1813-06-p364--entry14', 'bytes': 32543, 'sha256': '398ac37ed289bb47f90b8750db8d879b93c98dd938bfd923eb3fddda2e9a3f8e'}, {'name': 'diary0422.html', 'url': 'https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v28-1813-04-p467--entry22', 'bytes': 32258, 'sha256': '7fd073e678d3d58044b056868663d034c1a830e5b28ca420986b90d40f7d5fb4'}]
for item in manifest:
    if "--fetch" in sys.argv:
        with urllib.request.urlopen(item["url"],timeout=60) as response:data=response.read()
    else:data=(pathlib.Path(sys.argv[1])/item["name"]).read_bytes()
    assert len(data)==item["bytes"],item["name"]+": length changed"
    assert hashlib.sha256(data).hexdigest()==item["sha256"],item["name"]+": source changed; review required"
    (out/item["name"]).write_bytes(data)
def text(n):
    s=(out/n).read_text()
    return re.sub(r"\s+"," ",html.unescape(re.sub("<[^>]*>"," ",s)))
assert "Showing 1 to 480 of 480 results" in text("catalog-mar-jun1813.html")
assert "Showing 1 to 2 of 2 results" in text("catalog-barlow1813.html")
expected={131321:("20 April 1813","reel 415"),131335:("22 April 1813","reel 138"),131200:("23 March 1813","reel 415"),131252:("7 April 1813","reel 415"),131327:("21 April 1813","reel 138")}
for ident,needles in expected.items():
    s=text("slip"+str(ident)+".html")
    assert all(n in s for n in needles),(ident,needles)
# This is a catalogue-scope assertion only; no assertion about letter contents.
barlow_ids=re.findall(r'href="view_slip.php\?id=(\d+)"',(out/"catalog-barlow1813.html").read_text())
assert sorted(set(barlow_ids))==["131321","131335"]
ocr=(out/"correspondence-ocr.txt").read_text()
matches={term:len(re.findall(term,ocr,re.I)) for term in ["barlow","delprat","cypher","cipher"]}
assert all(v==0 for v in matches.values())
(out/"verification.json").write_text(json.dumps({"catalogue_rows_reported":480,"barlow_ids":barlow_ids,"ocr_search_counts":matches,"incoming_reply_identity":"unverified"},indent=2)+'\n')
print(json.dumps({"out":str(out),"verified_assets":len(manifest),"catalogue_assertions":8,"ocr_scope":"one 1913 AAS family-correspondence pamphlet only"}))
```
