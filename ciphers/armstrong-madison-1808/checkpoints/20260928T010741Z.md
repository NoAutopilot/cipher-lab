# Armstrong–Madison checkpoint — read the Adams temporary-cipher enclosure letter

UTC: 20260928T010741Z
Objective: a defensible, reproducible decipherment of John Armstrong Jr. to James Madison, 20 February 1808.
Status: completed bounded source-retrieval batch. This is documentary evidence and a better-directed witness search, not a target plaintext, recovered target key, or claim of cryptanalytic novelty.

## Continuity and publication provenance

- Parent: https://github.com/NoAutopilot/cipher-lab/pull/60
- Parent immutable head: `6b7c95c1c9e2b26731641d1ad773e0cd674cf2af`
- Parent path: `ciphers/armstrong-madison-1808/checkpoints/20260928T004610Z.md`
- Parent chain: #59 (`2cd1ed003a25ebf7a1d9e7f8e8012c452ed3ee7a`), #58 (`57dae1b983e46fc546a055592b380b3d839b5ebe`), #57 (`e378d4e942d854d29dd7be3a5b35dc32f5a357c5`), and their predecessors to bootstrap #44 (`58df6cf8c070c780df86faeec30900729f9229ba`, `ciphers/armstrong-madison-1808/checkpoints/2026-09-27-continuity.md`).
- All-state PR discovery at the start and just before publication found #60 newest, closed unmerged. That is a valid checkpoint under the user's landing workflow.
- No active lease for this source batch appeared in the parent. No separate H18 batch was taken or modified; no running work is retained here.
- Fresh branch: `second-opinion/armstrong-checkpoint-20260928T010741Z`, created from CURRENT remote main `4de43de132a6498b3ceee8c30f08c6c94df61a76` observed immediately before creation. Earlier main observations were not used.
- Sole intended repository addition: `ciphers/armstrong-madison-1808/checkpoints/20260928T010741Z.md`. No existing file, queue, shared register, main branch or automation was changed. Do not merge this PR.

Preserve #60's explicit retraction: the supposed January1806 reel gap was a February/January reading error. Armstrong–Monroe 7Jan1806 is already located at reel3 frames687–689 and read as prose. Erving 5Feb1806 is Madrid, not Paris. Do not restore the superseded #58/#59 conclusions or repeat those searches.

## 1. Exact retained-copy and printed-source locators

The parent asked for the actual wording of Adams to Armstrong, 27 November1809, Huntington HM22922, rather than another catalogue paraphrase. The MHS Online Adams Catalog supplied both a retained-copy locator and an older open printing.

Search used the actual public form's date fields, 27Nov1809–27Nov1809 with strict date restriction; seven results:
https://www.masshist.org/adams-resources/slipfile/search.php?ds_m=11&ds_d=27&ds_y=1809&de_m=11&de_d=27&de_y=1809&drest=on&form=sbyn&num=100

| OAC record | What the catalogue establishes | What it does not establish |
|---|---|---|
| [120595](https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=120595) | JQA to General John Armstrong, St.Petersburg,27Nov1809,3pages; original Huntington HM22922. Cites Tatum1941 pp.374–376 and Morrison second series vol.I pp.10–12. | No original image supplied; the Tatum article remains unread. |
| [120596](https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=120596) | Same dated letter,3pages; letterbook copy in Adams Family Papers, **MHS microfilm reel135**. | Locator is not a scan of the letterbook; no enclosure image supplied. |

The MHS guide https://www.masshist.org/collection-guides/view/fa0279 independently places JQA's private letterbook7Oct1801–5June1812 (also8Feb1814) on reel135. Its public1809–1812 letterbook is reel136, not the retained copy's actual locator. The guide locates **Ciphers and cipher keys on reel602**.

This refines #60: the exact November27 letter is cited in Tatum at374–376, rather than just a secondary locator to376; the article itself was not acquired.

## 2. Read and visually checked: Morrison1893, second series, Volume I (A–B), pp.10–12

Correct open holding:
https://wellcomecollection.org/works/wxfrbpzs

Published public IIIF collection:
https://iiif.wellcomecollection.org/presentation/v2/b24871709

Volume1 manifest:
https://iiif.wellcomecollection.org/presentation/v2/b24871709_0001

The manifest was linked in the accessible catalogue HTML and explicitly marks access open/public domain. No challenge was passed and no login was used. Five complete1600-pixel-wide images were acquired and viewed: half-title0005, full title0007, and printed pp.10,11,12 at canvases0018,0019,0020. Full title0007 confirms **1893, VolumeI, A–B**. Page10 identifies the letter, place, date and three-page autograph description. Pages10–12 print it through the closing.

### The key distinction in the letter

Printed p.11 says Adams had not received Armstrong's Department-of-State cipher before his hurried departure from America. It describes the intended copying of that official cipher and why sharing it would avoid a second encipherment for transmissions to Washington. Adams then says that he is sending a **different, temporary cipher**, retaining its corresponding part, while awaiting Armstrong's public cipher.

Exact relevant paragraph, manually checked against printed p.11 (line wrapping normalized; transcription of the1893 printing, **not** certification against the autograph):

> A Mr. Waters, a citizen of the United States, and one of my townsmen, being on the point of departure from this place, going at least as far as Rotterdam, and perhaps to Paris, I avail myself of this occasion to enclose to you a copy of a cypher, the corresponding part of which I retain in my possession, and which may be used between us untill you may meet a trusty hand by whom to furnish me a copy of your public cypher. In the use of this there will not indeed be the convenience of a common key between us and the department of State; but neither, on the other hand, will there be the danger of detection to the cypher arising from a multiplication of its copies in various hands.

This is stronger source evidence than the Huntington catalogue's generic “need for a cipher.” It identifies an asserted enclosure and a retained counterpart. It does **not** reproduce the enclosed table or identify its mechanics.

Keep three objects distinct:

| Object | Source-grounded status | Target relevance |
|---|---|---|
| Armstrong's public/Department cipher sought by Adams | Explicit in the27Nov1809 printing; receipt acknowledged3Jan1810 in Ford, verified by #60. | No new basis to rerun completed THE=972/WE028 transfers. |
| Temporary cipher sent by Adams with27Nov1809 letter | Explicitly enclosed; counterpart retained by Adams; Department did not share this key. | Potential private-key witness, but no table acquired and no established connection to February1808. |
| Armstrong–Madison mixed numerical/geometric target,20Feb1808 | Existing unresolved transcription and controlled-test record unchanged. | Predates this letter by21months; recipient overlap and the word “private” cannot equate the keys. |

No numeric mapping, shape assignment, crib, or plaintext candidate is licensed by these passages.

## 3. Surviving Adams key material: exact catalogue controls, not recovered target keys

Dated keyword searches1790–1815 returned70 catalogue records for `cipher` and22 for `cypher`. They search catalogue metadata, not full manuscript text, and broad date-span matches were allowed. They are **not** a complete undated-key inventory. Relevant complete record HTML was acquired:

| OAC ID | Catalogue description and date caution | Locator |
|---|---|---|
| [081697](https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=081697) | Undated, conjecturally1797–1803;2pages, sliding-strip lock/key, endorsed V.M./W.V.M./Cypher.W.V.Murray. Not an Armstrong label. | reel602,TS Ciphers JQA |
| [120623](https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=120623) | Cipher sheets and explanations, mixed with an interest table.7Dec1809 appears **only on p.12**. Catalogue note distinguishes two folders and a possibly rejected earlier attempt; later subset is associated with the TBA letterbook explanation. Different-size/paper sheets may not belong together. | reel602,TS Ciphers JQA |
| [120693](https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=120693) | Four-page lock/key explanation; undated, conjecturally1809–1812. | reel602,TS Ciphers JQA |
| [130946](https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=130946) | Two-page sliding-strip cipher;1812 endorsement is in an unidentified hand. Catalogue says same cipher as p.1 of120623; paper watermark C Burbank1804. | reel602,TS Ciphers JQA |
| [120739](https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=120739) | Three-page JQA-to-TBA instructions, **conjecturally8–17Jan1810**, redated by catalogue note12May2026 from its letterbook position. | reel135 |

None of these catalogue descriptions identifies the specific November27 enclosure. Do not date every sheet in120623 to7December1809 or assume “corresponding part” proves a sliding strip.

The public Rotunda early-access transcription headed [8January1810](https://rotunda.upress.virginia.edu/founders/default.xqy?keys=FOEA-print-03-03-02-1786) was read through the web reader. It describes a sliding lock/key, four alternating letter columns, accented syllables and capital-letter word entries. It is explicitly a raw, pre-editing transcription; its rendered examples have missing/ambiguous accents and internal inconsistencies. The catalogue's later8–17January dating must be retained. **No implementation or cryptanalytic exclusion was made from this weakly rendered control.** Direct curl returned403, so no direct HTML hash is claimed for Rotunda.

A separate date-bounded author search27Nov1809–31Dec1810 yielded one catalogue hit, Armstrong to JQA6Aug1810,5pages with enclosure, [OAC121104](https://www.masshist.org/adams-resources/slipfile/single_slip_viewer.php?id=121104), reel410. No image or cipher-key description was provided. One search hit is not evidence that only one letter was written or survives.

## 4. A specific next paired-witness lead

The [MHS digital diary edition for15June1813](https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v28-1813-06-p485--entry15), at the text transition to manuscript p.490, reports that Adams sent a cipher letter toward Paris through Delprat, with a clear duplicate to be delivered personally. Delprat was detained and sent the coded copy by post; Paris's answer, received the previous day, said the key was unavailable. Adams says the key had been with Barlow's predecessor.

This was read as the holding institution's **editorial transcription**, not checked against the diary image in this batch. Neither copy of the described letter has yet been located. The passage does not identify the cipher with the1809 enclosure, with Armstrong's official key, or with the1808 target. “Predecessor” must not be silently expanded into a recovered key attribution.

**Concrete next action:** identify the exact date/addressee of the Delprat-carried cipher letter and its clear duplicate by following the diary's14June1813 received-answer entry and the earlier Delprat-dispatch entries, then locate those two witnesses in the Adams correspondence catalogue. Prefer obtaining an actual ciphertext/plaintext pair or associated key image over new blind target fitting. First verify the diary's relevant manuscript image. If both forms survive, preserve exact images and do a bounded transcription before assigning any cipher family. Do not repeat the now-completed November27 printing search.

## Exact inputs and recovery

Target unchanged and not re-searched:366decimalgroups,1885UTF-8bytes, SHA-256 `c4ba5db4b1d7bc509b6ab531f6ba90dc9be4d06a3e62b43159c431742e0bc9b2`. The1841/1843,203/200 and graphical-allograph uncertainties remain. #44's winning controls/results and subsequent provisional Livingston restrictions remain recoverable from their existing capsules; do not rerun to restore them.

Required static image inputs:

| Asset | Bytes | SHA-256 | Pixels |
|---|---:|---|---|
| morrison-full-title.jpg | 229196 | `8cf8e8ff4e4eeac671e85c2905476c9e591f6a7758a93fbe4e63500207dc2d72` | 1600×2230 |
| morrison-p10.jpg | 697036 | `f342d4c59ff88b4bc4cfea9d56c07bd9293c16493a04cb9865a2c74826890a99` | 1600×2513 |
| morrison-p11.jpg | 772676 | `ac1fefe3fd3a1b82c6e24e717f41abdd49ebdc2abdd364ba2b629331299ee511` | 1600×2513 |
| morrison-p12.jpg | 733402 | `48ca0ca3b2f4074e20bef66376a68502aa5f72fb0ef370f99a556367bbf26a46` | 1600×2513 |

All **24 acquired inputs**, including dynamic HTML/JSON, the half-title and the wrong-volume PDF used only for exclusion, have exact URLs, bytes and hashes in the embedded recovery ledger. The script checks every supplied ledger asset, and can fetch the four missing required static images. Optional mutable snapshots are not silently refreshed or substituted. It writes only to a newly created system-temporary directory, refuses a Git ancestor, and runs no solver or Git operation.

The exact embedded code was executed on the acquired inputs: **24/24 byte/hash checks passed; all five JPEG dimensions checked; four required images restored.** Script SHA-256: `84a44c2c95c04a1673660c4fa7a628a19d010abe54a1f0619b37563ee943f151`. These checks establish reproducible source bytes, not independent confirmation of the interpretation.

## Source failures, exclusions and state

- MHS guide web-reader open returned502; direct public HTML succeeded.
- Internet Archive advancedsearch for creator Morrison,Alfred returned502; no result set was inferred.
- Commons/IA `cu31924092469711` is the **Hamilton and Nelson Papers**, VolumeI1756–1797, not the A–B volume. Its title page was rendered and visually checked; excluded from letter evidence. This is why catalogue metadata alone was insufficient.
- Wellcome's interactive items page showed a JavaScript/bot challenge in the web reader. It was not passed or retried. The separately published catalogue and its explicitly linked open IIIF service returned the correct pages without credentials.
- MHS keyword request lacking date bounds returned500; complete dated form requests succeeded. Both the category-only link and the full blank-date category form returned500. Do not repeat these unchanged endpoints or interpret them as no key records.
- The second undated cypher request in a shell chain was **not run** after the first request's500. It is not an independent access failure. Both dated spelling variants were subsequently retrieved.
- A local convenience parser was unavailable; reading HTML directly succeeded. No package installation was needed.
- Rotunda direct403 versus web-reader success is recorded above. JSTOR's previously blocked challenge was not retried. No outreach, login, credential extraction, bypass or paid access occurred.
- **Completed:** MHS exact-date lookup; retained-copy locator; acquisition and visual reading of correct printed letter; catalogue key-location/date audit; source distinctions; diary paired-copy lead; recovery test.
- **Running:** none retained.
- **Source-limited:** actual November27 autograph/letterbook and cipher enclosure images unacquired; reel602 key records are metadata only; Tatum text unread;1813 pair not yet located. These are not a total task blocker.
- **Uncertainty:** no proven bridge from any retrieved Adams key material to the February1808 target, and no target-compatible key or plaintext candidate. Do not promote this source work into a decipherment.

Publication must be verified after upload: one ADDED file, zero deletions, sole commit parent equal to the remote-main base above, and exact remote-file equality. This file is append-only; corrections belong in a future checkpoint.

## Recovery capsule

Save the following block outside the repository as `recover61.py`. Requires Python3 and Pillow. Run `python recover61.py INPUT_DIR`, adding `--fetch` if required images are absent. No old search is rerun.

~~~python
#!/usr/bin/env python3
"""Restore inspected source images outside any Git repository; no cipher search.
Python 3 + Pillow. Run: python recover61.py INPUT_DIR [--fetch]
Creates a fresh temporary output directory. --fetch retrieves missing required images.
Optional mutable HTML/JSON is only checked if supplied, never silently substituted.
"""
import argparse, hashlib, json, tempfile, urllib.request
from pathlib import Path
from PIL import Image
ASSETS = json.loads(r'''[{"name":"catalog.html","bytes":23623,"sha256":"1e91562256eb68cb7ad8a472837cae3d748fad9ce52179030f14c96a795b8fa5","url":"https://www.masshist.org/adams-resources/slipfile/catalog.php","required":false},{"name":"diary-18130615.html","bytes":44540,"sha256":"a7834fff1ad5cc2baac9c27c98b86c6200d7fae41172422ab47da6ac992d7152","url":"https://www.primarysourcecoop.org/publications/jqa/document/jqadiaries-v28-1813-06-p485--entry15","required":false},{"name":"mhs-guide.html","bytes":232418,"sha256":"a58a5cc3ce8aaea7e91dc01b517c86acb39dbc3d68c7003488705a4eede70f75","url":"https://www.masshist.org/collection-guides/view/fa0279","required":false},{"name":"morrison-full-title.jpg","bytes":229196,"sha256":"8cf8e8ff4e4eeac671e85c2905476c9e591f6a7758a93fbe4e63500207dc2d72","size":[1600,2230],"url":"https://iiif.wellcomecollection.org/image/b24871709_0001_0007.jp2/full/1600,/0/default.jpg","required":true},{"name":"morrison-p10.jpg","bytes":697036,"sha256":"f342d4c59ff88b4bc4cfea9d56c07bd9293c16493a04cb9865a2c74826890a99","size":[1600,2513],"url":"https://iiif.wellcomecollection.org/image/b24871709_0001_0018.jp2/full/1600,/0/default.jpg","required":true},{"name":"morrison-p11.jpg","bytes":772676,"sha256":"ac1fefe3fd3a1b82c6e24e717f41abdd49ebdc2abdd364ba2b629331299ee511","size":[1600,2513],"url":"https://iiif.wellcomecollection.org/image/b24871709_0001_0019.jp2/full/1600,/0/default.jpg","required":true},{"name":"morrison-p12.jpg","bytes":733402,"sha256":"48ca0ca3b2f4074e20bef66376a68502aa5f72fb0ef370f99a556367bbf26a46","size":[1600,2513],"url":"https://iiif.wellcomecollection.org/image/b24871709_0001_0020.jp2/full/1600,/0/default.jpg","required":true},{"name":"morrison-title.jpg","bytes":182044,"sha256":"708c5e5796e9ee19f63d06900c2cb3e06e92c17a081bb9f4c137c125a4ee9202","size":[1600,2513],"url":"https://iiif.wellcomecollection.org/image/b24871709_0001_0005.jp2/full/1600,/0/default.jpg","required":false},{"name":"morrison.pdf","bytes":10326455,"sha256":"03160a741360e214bd070e294911130851d918d458ab1ba84f1121db31d81109","url":"https://upload.wikimedia.org/wikipedia/commons/4/41/Catalogue_of_the_collection_of_autograph_letters_and_historical_documents_formed_..._by_Alfred_Morrison_.._%28IA_cu31924092469711%29.pdf","required":false},{"name":"search-18091127.html","bytes":8908,"sha256":"827d387ed4c9b7dbb487c75300a352e3ac340e137bb02bdc89564caba01fa9eb","url":"https://www.masshist.org/adams-resources/slipfile/search.php?ds_m=11&ds_d=27&ds_y=1809&de_m=11&de_d=27&de_y=1809&drest=on&form=sbyn&num=100","required":false},{"name":"search-armstrong-replies.html","bytes":6069,"sha256":"22547e350f2d73b9bd9380a464355831d8809bd032ee184a4c8cbd77d06b6d4f","url":"https://www.masshist.org/adams-resources/slipfile/search.php?addP[]=armstrong-john&addPT[]=author&addPD[]=John%20Armstrong&ds_m=11&ds_d=27&ds_y=1809&de_m=12&de_d=31&de_y=1810&form=sbya&num=100","required":false},{"name":"search-cipher-dated.html","bytes":35543,"sha256":"4ad87410fd0ca8c2cb64db5a979ffe1d04022208f46035c10b4af73fde5f7e2c","url":"https://www.masshist.org/adams-resources/slipfile/search.php?ds_m=01&ds_d=01&ds_y=1790&de_m=12&de_d=31&de_y=1815&slip_words=cipher&form=sbya&num=100","required":false},{"name":"search-cypher-dated.html","bytes":14544,"sha256":"d1f6b681c4ab7ce41b856bfc5879ac6d0eed4d632fc2b06b7b0802a75bdd89f6","url":"https://www.masshist.org/adams-resources/slipfile/search.php?ds_m=01&ds_d=01&ds_y=1790&de_m=12&de_d=31&de_y=1815&slip_words=cypher&form=sbya&num=100","required":false},{"name":"slip-081697.html","bytes":3949,"sha256":"279dc864a10fab8d6aac558802d829aa530df0e6371f66f14ce50cc58c2e2bfd","url":"https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=081697","required":false},{"name":"slip-120595.html","bytes":3776,"sha256":"a902291e9e9627018d3ca61c7df09164fccda0483626c66e1759076b611feb18","url":"https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=120595","required":false},{"name":"slip-120596.html","bytes":3400,"sha256":"652ddb2f314e3dd3784e94e2362caa3f29cb108f6fe1434ce66b71fb8633250b","url":"https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=120596","required":false},{"name":"slip-120623.html","bytes":4061,"sha256":"baa5d2c76cc331a83dc787888cfc267cf43fbd510515935bcac3998b2d44b8c6","url":"https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=120623","required":false},{"name":"slip-120693.html","bytes":3080,"sha256":"50fad10f59337d3c3ae1a713e7fa2092e1b5e2cc6c7818db5d7aba9b3740418e","url":"https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=120693","required":false},{"name":"slip-120739.html","bytes":3816,"sha256":"a002bb9df32073aef34333462116299337f55c6c22e77028980f8a3800b9397b","url":"https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=120739","required":false},{"name":"slip-121104.html","bytes":3484,"sha256":"c040e6270eac825dfa922a39097affd5b719eef1287e89c28bf58fd856ad1a02","url":"https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=121104","required":false},{"name":"slip-130946.html","bytes":3111,"sha256":"8ebe496f940570d520ccfc44cedb9343dd2b77a54ae130fe561678225aefc320","url":"https://www.masshist.org/adams-resources/slipfile/view_slip.php?id=130946","required":false},{"name":"wellcome-collection.json","bytes":2637,"sha256":"8634b3951f37cb462570f438ea8971daac6e8f037582e390aa2fc4b5cabc465f","url":"https://iiif.wellcomecollection.org/presentation/v2/b24871709","required":false},{"name":"wellcome-v1.json","bytes":1319314,"sha256":"cb5fa1e1ee0eb9af666e78bb675ca2a556d5e855bdc7663916b33bc8527be0ed","url":"https://iiif.wellcomecollection.org/presentation/v2/b24871709_0001","required":false},{"name":"wellcome.html","bytes":114297,"sha256":"9db79ddfc8fd00db319c3cde852da5ac716e709c5973d4dcd682acb2aadbd5d4","url":"https://wellcomecollection.org/works/wxfrbpzs","required":false}]''')
FACTS = {
 "objective": "Armstrong to Madison, 20 February 1808",
 "letter": {"date":"1809-11-27","sender":"John Quincy Adams","recipient":"John Armstrong",
  "printed_source":"Morrison, second series, volume I (A-B), 1893, pp.10-12",
  "letterbook_locator":"MHS OAC120596, microfilm135",
  "original_locator":"Huntington HM22922, MHS OAC120595",
  "observed":"Printed p.11 says Adams encloses a temporary cipher, retaining its corresponding part, pending receipt of Armstrong's public cipher.",
  "key_table_recovered":False,"target_connection_established":False},
 "catalogue_keys": [
  {"id":"081697","reel":602,"date":"undated [1797-1803?]","association":"William Vans Murray"},
  {"id":"120623","reel":602,"date":"7 Dec1809 on p12 only; later subset tied to Jan1810","association":"lock/key sheets, explanations, mixed paper"},
  {"id":"120693","reel":602,"date":"undated [1809-1812?]","association":"four-page explanation"},
  {"id":"130946","reel":602,"date":"1812 endorsement in unidentified hand","association":"catalogue says same cipher as p1 under120623"},
  {"id":"120739","reel":135,"date":"conjectural8-17Jan1810","association":"TBA instruction letter; catalogue redating12May2026"}],
 "next_lead":{"source":"Adams diary15June1813, manuscript-page490 in edition",
  "observed_from_editorial_transcript":"Adams reports a cipher letter sent by Delprat and a clear duplicate withheld for personal delivery; Paris reported lacking the key.",
  "manuscript_image_inspected":False,"paired_witnesses_located":False},
 "manual_observations_not_automatically_proved":True
}
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("inputs",type=Path)
 ap.add_argument("--fetch",action="store_true")
 args=ap.parse_args()
 temp=Path(tempfile.gettempdir()).resolve()
 if any((p/".git").exists() for p in [temp,*temp.parents]):
  raise SystemExit("Temporary output must be outside a repository")
 out=Path(tempfile.mkdtemp(prefix="armstrong-recover61-",dir=temp))
 verified=[]; absent=[]
 for a in ASSETS:
  f=args.inputs.resolve()/a["name"]
  if not f.exists() and a["required"] and args.fetch:
   req=urllib.request.Request(a["url"],headers={"User-Agent":"cipher-source-audit/1.0"})
   with urllib.request.urlopen(req,timeout=45) as r: b=r.read()
   assert len(b)==a["bytes"] and hashlib.sha256(b).hexdigest()==a["sha256"],a["name"]
   f=out/a["name"]; f.write_bytes(b)
  if not f.exists():
   if a["required"]: raise SystemExit("Missing required source: "+a["name"])
   absent.append(a["name"]); continue
  b=f.read_bytes()
  assert len(b)==a["bytes"] and hashlib.sha256(b).hexdigest()==a["sha256"],a["name"]
  if "size" in a:
   with Image.open(f) as im:
    im.load(); assert list(im.size)==a["size"],a["name"]
  if a["required"] and f.parent!=out: (out/a["name"]).write_bytes(b)
  verified.append(a["name"])
 audit={"verified":verified,"optional_missing":absent,"manual_facts":FACTS}
 (out/"audit.json").write_text(json.dumps(audit,indent=2)+"\n")
 (out/"asset-ledger.json").write_text(json.dumps(ASSETS,indent=2)+"\n")
 print(json.dumps({"verified":len(verified),"required":sum(a["required"] for a in ASSETS),"output":str(out)}))
if __name__=="__main__": main()

~~~
