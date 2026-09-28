# Armstrong–Madison checkpoint — Delprat dispatch and Paris cipher custody

UTC: 20260928T015051Z
Objective: defensible reproducible decipherment of Armstrong to Madison, 20 February 1808.
Status: completed source batch; target remains partial. No target plaintext or recovered key is claimed.

## Continuity and publication

Parent: https://github.com/NoAutopilot/cipher-lab/pull/61
Immutable parent head: `be687a68c63ee9b5f56ffc89c968ecda262a21c4`
Parent file: `ciphers/armstrong-madison-1808/checkpoints/20260928T010741Z.md`
Parent normalized local UTF-8 SHA256: `528af046a6d9e03ce947b6e6f1403958e8332ecd052019a0c35a4e9a08b3c158`.
Chain: #61 → #60 (`6b7c95c1c9e2b26731641d1ad773e0cd674cf2af`) → #59 → #58 → #57 and predecessors to bootstrap #44 (`58df6cf8c070c780df86faeec30900729f9229ba`). Read parent narrative and recovery instructions before any solver work.
All-state newest-first PR checks found #61 newest, open. Closed unmerged predecessors are valid. No active lease for this source batch appeared in the parent; separate H18 was not taken.
Fresh branch: `second-opinion/armstrong-checkpoint-20260928T015051Z`.
Observed current remote main immediately before branch creation: `1aace773cd4f3999fa05eb38aacdd854a80081b2`.
Exactly one intended addition: `ciphers/armstrong-madison-1808/checkpoints/20260928T015051Z.md`. Never merge. No existing repository file, shared register, queue or automation changed.

## Completed findings

1. **Dispatch date and two-copy design verified in manuscript.** Adams diary 14 February 1813, manuscript p457, says he gave Delprat two copies of a letter to the US chargé d’affaires at Paris: one enciphered to forward if detained, the other plain to deliver personally. Delprat departed that afternoon. Both editorial text and the actual page image were read.
   - https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v28-1813-02-p449--entry14
   - https://www.primarysourcecoop.org/projects/jqa/page-images/jqad28_457_lg.jpg
2. **Failure of delivery/key availability verified in manuscript.** Diary 15 June 1813, p490, says Delprat was detained at Vienna and forwarded the cipher copy by post; Adams received an answer on 14 June reporting no key. Adams had anticipated Barlow might lack the cipher formerly with his predecessor and had provided the plain duplicate. The manuscript does not name that predecessor or specify the table. This cannot identify the 1808 target key.
   - https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v28-1813-06-p485--entry15
   - https://www.primarysourcecoop.org/projects/jqa/page-images/jqad28_490_lg.jpg
3. **Likely outgoing letter locator, not yet identity proved.** MHS OAC131078: Adams to the chargé d’affaires at Paris, St Petersburg, **12 February 1813**, 2 pages, letterbook copy, **reel138**. Catalogue supplies **[David B. Warden]** in brackets. The chronological/destination fit makes this the specific candidate for Delprat's dispatch, but neither letterbook pages nor received cipher/plain copies were obtained. Do not upgrade catalogue identification to an inspected signature or a recovered pair.
   - https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=131078
4. **Custody evidence changes the next search.** Ford, *Writings of John Quincy Adams*, vol4, **Adams to John Speyer, 20 April 1813, pp474–475**, reports differences between **T. Barlow and Warden**. Adams supposes the legation's seal, cipher and archives properly remain with Barlow, while questioning both men's authority to act as chargé. He approves forwarding legation letters to Barlow. Actual printed pp474–475 were visually read, not merely OCR. This is Adams's stated view of custody, not proof which specific key Barlow possessed. It makes a Warden-only incoming-letter search unjustified.
   - https://archive.org/details/writingsofjohnqu04adam/page/n508/mode/2up
   - PDF https://archive.org/download/writingsofjohnqu04adam/writingsofjohnqu04adam.pdf
5. **Purpose and dating corroboration.** Same volume, Adams to Secretary of State, **16 February 1813, no106, pp441–444**, explains that Romanzoff asked him to establish the whereabouts of Russian embassy archives deposited with Joel Barlow. Adams wished also to ascertain who handled US affairs after Barlow's death. Names Delprat and confirms departure two days before the letter. All four printed pages visually read. This letter describes the mission; it is not the cipher/plain pair.
6. **Incoming candidate remains unverified.** MHS Warden-as-author query, 1 March–14 June1813, returned one result: **Warden to Adams, Paris, 4 March1813, 1p, reel415**, OAC131142. Its text was not obtained; no assertion it is the cipher-key reply.
   - https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=131142

## Coverage, failures and corrections

- Full main diary entries 12 February and 14 June read. February12 concerns courier passport arrangements; June14 does not mention the cipher reply. Neither supplies the answer's sender/date. Do not infer that no incoming answer survives.
- February catalogue general query fetched first100 results only; not exhaustive. Warden query explicitly reports 1 of1 for its stated author/date scope.
- Public diary navigation API returns numeric date_when values, not ISO strings. Its doc_beginning fields are snippets, not full diary entries. No negative corpus claim follows from searching them.
- Diary image paths derived from public page-images client code plus facs attributes. No authentication or bypass used.
- Search-engine exact-date queries produced mainly irrelevant results; no absence conclusion. Commons search snippet linked vol1 in upload history; actual current source field identifies writingsofjohnqu04adam. Wrong-item metadata (filename ford4-metadata.json) is vol1 and is retained only as an audit artifact, not evidence about1813. Correct volume metadata and PDF obtained.
- PDF leaf numbering caution: actual PDF 1-based pages475–478 show printed441–444; PDF508–509 show printed474–475. An initial +1 assumption rendered475/476 instead of474/475; corrected before reading. Use verified printed labels.
- Python requests unavailable; urllib succeeded. This is an implementation issue, not a source block.
- No failed historical endpoints from earlier checkpoints were repeated. No solver searches were rerun.
- Preserve #60's correction: supposed January1806 reel gap was a February/January error. Armstrong–Monroe7Jan1806 already read as prose. Preserve #61 distinction between Adams's temporary private1809 cipher and requested official Department cipher.

## Uncertainty and exact next action

**Next bounded action:** identify and read the incoming Paris answer received by Adams on **14 June1813**, searching **T. Barlow as well as Warden**, using MHS catalogue date-limited correspondence and public printed sources. The outgoing **12Feb1813 OAC131078/reel138** is the matching witness candidate to check against that answer. Do not assume the bracketed Warden identification settles the correspondent. If a manuscript/printed answer dates the encrypted dispatch, follow that exact reference to the actual cipher and clear duplicate; only then attempt a key reconstruction.

No work remains running. Actual letterbook pages, the received cipher/plain pair and the incoming answer are not yet acquired. These are source gaps, not a reason to restart completed solvers. No user action is required by this batch. Target still has366 numeric groups/216 distinct; inherited transcription SHA256 `c4ba5db4b1d7bc509b6ab531f6ba90dc9be4d06a3e62b43159c431742e0bc9b2`; no target tokens changed or assigned. Provisional1841/1843 and203/200 readings remain provisional. Restore saved solver results from #44/#61 chain rather than rerunning searches.

## Recovery capsule and verification

The code below contains exact URLs, byte lengths and SHA256s for **23 downloaded inputs**. Recovery script SHA256: `cf38d62167475e1ff29c715d42830058117f9bb73a82d7941311fcd7af8e94bf`.
Extract this Python fence programmatically into a scratch file outside the repository. Run `python recover.py /path/to/input-directory` for offline validation, or `python recover.py --fetch --render` to reacquire and render. Recovery always writes to a fresh temporary directory. Dynamic metadata may change; hash mismatch stops for review, not a historical contradiction.
Executed offline recovery successfully:23 input hashes/lengths and9 semantic checks passed. Visual review performed separately: diary457/490 and Ford printed441–444/474–475. Semantic checks prove source fixture consistency, not cryptanalytic success.
Branch/commit/file/PR verification will be recorded in the PR body after publication.

```python
import pathlib, tempfile, urllib.request, hashlib, json, re, html, subprocess, sys
# This capsule always creates a new temporary directory outside the repository.
out=pathlib.Path(tempfile.mkdtemp(prefix="armstrong-delprat-recovery-"))
manifest=[{'name': 'diary15.html', 'url': 'https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v28-1813-06-p485--entry15', 'bytes': 44540, 'sha256': 'a7834fff1ad5cc2baac9c27c98b86c6200d7fae41172422ab47da6ac992d7152'}, {'name': 'diary0210.html', 'url': 'https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v28-1813-02-p449--entry10', 'bytes': 33207, 'sha256': 'dbf5f6fdee429e953d49c4f81268dcd150246691abad213c2ee1a6f274e0be20'}, {'name': 'diary0212.html', 'url': 'https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v28-1813-02-p449--entry12', 'bytes': 33826, 'sha256': 'b05205b275ff2bc1b6ea62717019f49213e0bc6a656365235a0a495aec293734'}, {'name': 'diary0214.html', 'url': 'https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v28-1813-02-p449--entry14', 'bytes': 35534, 'sha256': '259ae838f3d9f763f51295b338ef31416ab85c9348a53d14d6827568c83c9570'}, {'name': 'diary0614.html', 'url': 'https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v28-1813-06-p485--entry14', 'bytes': 31686, 'sha256': 'f94df1ac4caf660f5f316e97c3fa8bcdef0a851630943c4a69a2c286acd66f93'}, {'name': 'diary457.jpg', 'url': 'https://www.primarysourcecoop.org/projects/jqa/page-images/jqad28_457_lg.jpg', 'bytes': 1200288, 'sha256': '029f6021ebc45478bfd87261bc91cbfd4a14328f31bb838af520d50b004c6e1b'}, {'name': 'diary490.jpg', 'url': 'https://www.primarysourcecoop.org/projects/jqa/page-images/jqad28_490_lg.jpg', 'bytes': 1020868, 'sha256': '766f843d49ab01615844b61f317904ddd15e51af48649feabdf01cb43a570436'}, {'name': 'document-vue.js', 'url': 'https://www.primarysourcecoop.org/publications/template/js/document-vue.js?v=2108', 'bytes': 5749, 'sha256': 'c3d8a091f767b940b0789244aa87ae540a9fa113913f0d01f93384d343e76f3b'}, {'name': 'custom.js', 'url': 'https://www.primarysourcecoop.org/projects/jqa/customize/custom.js?v=2108', 'bytes': 1726, 'sha256': 'c98c553b15ee74106fe9fdbfcd8a87dad045f30838e58a3572aefffc38347751'}, {'name': 'page-images.js', 'url': 'https://www.primarysourcecoop.org/publications/template/js/page-images-vue.js?v=101', 'bytes': 2775, 'sha256': '3378adc81015178a50df4581dbc1357f7c41d12352006ea1b5f92c88f8443a8d'}, {'name': 'nextprev.js', 'url': 'https://www.primarysourcecoop.org/publications/template/js/nextprev-vue.js?v=101', 'bytes': 7451, 'sha256': '1ec612d8f37990204439091f156862cd0e3aee657e32109b223c68f589825e02'}, {'name': 'context-june.json', 'url': 'https://www.primarysourcecoop.org/publications/jqa/context?configRows=3000&date=18130615&project=jqa', 'bytes': 499242, 'sha256': '67c4c4c57a445eb6e8573f38ec9387df234285ac8e4d6d31cf0020454ed4537b'}, {'name': 'context-feb.json', 'url': 'https://www.primarysourcecoop.org/publications/jqa/context?configRows=3000&date=18130212&project=jqa', 'bytes': 524675, 'sha256': '8dd9064c7ee29933a9be19e31f4b23109961d13e4c7672e5293bae5b55ded320'}, {'name': 'search-feb1813.html', 'url': 'https://www.masshist.org/adams-resources/slipfile/search.php?ds_m=02&ds_d=01&ds_y=1813&de_m=02&de_d=28&de_y=1813&form=sbya&num=100', 'bytes': 48975, 'sha256': 'f03f01f83407514d744a9ae23f47e554ba0e4e3af9e730da9560847919d286ea'}, {'name': 'slip131078.html', 'url': 'https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=131078', 'bytes': 3510, 'sha256': '4a8ef5cb29453bcab01fae42c0b29dbcffe8f641073c7a14411a55d8598fc4ff'}, {'name': 'search-warden1813.html', 'url': 'https://www.masshist.org/adams-resources/slipfile/search.php?addP%5B%5D=warden-david-bailie&addPT%5B%5D=author&addPD%5B%5D=David%20Bailie%20Warden&ds_m=03&ds_d=01&ds_y=1813&de_m=06&de_d=14&de_y=1813&form=sbya&num=100', 'bytes': 6088, 'sha256': 'ab12ccb2779b6c69f05742aa4b57c65e850814e593c34106819afe413c0fd7b8'}, {'name': 'slip131142.html', 'url': 'https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=131142', 'bytes': 3532, 'sha256': 'c8bed48538c448b05c28d9eed706cbdbf658d5f260f84855b74cf51162f1b442'}, {'name': 'ford4-metadata.json', 'url': 'https://archive.org/metadata/fordsjohnadams01adamrich', 'bytes': 104805, 'sha256': 'bd3159cb8608d2f01daddda197626fa87b1f9a69de2376a75f4cd9eeebe64d75'}, {'name': 'ford4-search.json', 'url': 'https://archive.org/advancedsearch.php?q=title%3A%28Writings%20of%20John%20Quincy%20Adams%29%20AND%20volume%3A4&fl%5B%5D=identifier%2Ctitle%2Cvolume&rows=20&output=json', 'bytes': 1339, 'sha256': '2ebfc146de2f18596bec7d1e5f91334e2124ef753edcc6228d80dd863522568c'}, {'name': 'ford4-correct-metadata.json', 'url': 'https://archive.org/metadata/writingsofjohnqu04adam', 'bytes': 109260, 'sha256': '7dcafa7140c9516fab5758a54bd7eca5ccb1ac61bea34dff429d4f4c17ac8ed1'}, {'name': 'ford4-ocr.txt', 'url': 'https://archive.org/download/writingsofjohnqu04adam/writingsofjohnqu04adam_djvu.txt', 'bytes': 1203832, 'sha256': '9b0a13760f3766e53526e312dc9a963ed96276c32a6cf20e981a4ce3e719ab1c'}, {'name': 'ford4-scandata.xml', 'url': 'https://archive.org/download/writingsofjohnqu04adam/writingsofjohnqu04adam_scandata.xml', 'bytes': 296610, 'sha256': '78ba5a9ea334f96fc25e19362678885ac9a6ea9824948994f8158e1c1b0dcdb8'}, {'name': 'ford4.pdf', 'url': 'https://archive.org/download/writingsofjohnqu04adam/writingsofjohnqu04adam.pdf', 'bytes': 32084361, 'sha256': '0bce37e7d248279a084733bf46f07244435605d5b45f8830d4482342c65bc3c5'}]
fetch="--fetch" in sys.argv
if fetch:
    for item in manifest:
        with urllib.request.urlopen(item["url"], timeout=90) as response:
            data=response.read()
        (out/item["name"]).write_bytes(data)
        if hashlib.sha256(data).hexdigest()!=item["sha256"]:
            raise SystemExit("Input changed; inspect before use: "+item["name"])
else:
    # Offline verification: give the directory holding the downloaded inputs.
    src=pathlib.Path(sys.argv[1]).resolve()
    for item in manifest:
        data=(src/item["name"]).read_bytes()
        assert len(data)==item["bytes"]
        assert hashlib.sha256(data).hexdigest()==item["sha256"],item["name"]
        (out/item["name"]).write_bytes(data)
def flat(name):
    text=(out/name).read_text()
    return re.sub(r"\s+"," ",html.unescape(re.sub("<[^>]*>","",text)))
assert "two Copies of a letter" in flat("diary0214.html")
assert "One in Cypher" in flat("diary0214.html")
assert "other uncyphered" in flat("diary0214.html")
assert "no key to the cypher" in flat("diary15.html")
assert "reel 138" in flat("slip131078.html")
assert "reel 415" in flat("slip131142.html")
assert "Showing 1 to 1 of 1 results" in flat("search-warden1813.html")
text=flat("ford4-ocr.txt")
assert "seal, cypher, and archives" in text
assert "custody of Mr. Barlow" in text
# Printed page numbers were checked visually. PDF pages are 1-based here.
# Scandata leafNum is NOT safely convertible with a universal +1 rule.
if "--render" in sys.argv:
    for page in [475,476,477,478,508,509]:
        subprocess.run(["pdftoppm","-f",str(page),"-l",str(page),"-scale-to","1700","-png",str(out/"ford4.pdf"),str(out/"ford4")],check=True)
print(json.dumps({"directory":str(out),"verified_inputs":len(manifest),"semantic_checks":9,"visual_review_required":["diary457.jpg","diary490.jpg","Ford printed pp441-444,474-475"]}))
```
