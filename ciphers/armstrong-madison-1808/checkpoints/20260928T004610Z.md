# Armstrong–Madison checkpoint — retract false reel gap, locate January witness, verify cipher-transfer context

UTC: 20260928T004610Z
Objective: a defensible, reproducible decipherment of John Armstrong Jr. to James Madison, 20 February 1808.
Status: completed source-correction and source-verification batch. No target plaintext or recovered target key is asserted.

## Continuity and branch provenance

- Parent: https://github.com/NoAutopilot/cipher-lab/pull/59
- Parent immutable head: `2cd1ed003a25ebf7a1d9e7f8e8012c452ed3ee7a`
- Parent file: `ciphers/armstrong-madison-1808/checkpoints/20260928T003110Z.md`
- Follow parent #58 (`57dae1b983e46fc546a055592b380b3d839b5ebe`), #57 (`e378d4e942d854d29dd7be3a5b35dc32f5a357c5`), and their chain to bootstrap #44 (`58df6cf8c070c780df86faeec30900729f9229ba`).
- All-state PR discovery was checked at bootstrap and again before publication. #59 remained newest, open; #57 is closed unmerged and remains valid.
- New branch `second-opinion/armstrong-checkpoint-20260928T004610Z` was created from observed CURRENT remote main `493aa0d7273971226c9b2463034ad8c29f46d45c`, not a local main or an earlier checkpoint branch.
- No active lease for the source-location batch was retained by #59. The separately leased H18 campaign was not run or modified. No new running batch is retained here.
- No existing repository file, shared register, queue, or main branch was changed by this work. Exactly one new checkpoint file is the intended PR payload.

## Explicit retraction: the supposed January reel gap was our reading error

**Withdraw #59's section 3 source-location discrepancy and the missing-witness premise of its next action. Correct #58 section 5 accordingly.**

Frame 739 says **2 Feby 1806**, not 2 January. Frame 710 has a supplied February reading over the altered heading; the index independently lists Monroe to Madison, **2 February 1806, Series 1, 38 pages, with copies and covers** (1963 index, PDF page 28, printed p. 12). The 739→740 transition is therefore February 2 to February 5, not evidence of a missing January item. Frames 720–739 were the wrong chronological interval for the asserted inference.

This is a correction of our earlier error, not an archival discovery of a missing document or cryptanalytic breakthrough. Reproducing an image hash or running the old recovery assertions never validated the earlier paleographic reading. Do not repeat the alternate-surrogate/misfiling search proposed by #59 on that false premise.

A second factual correction: #58 section 3 calls Erving's 5 February 1806 letter **Paris**. Frame 740 clearly says **Madrid**. The verified WE028 examples from frames 742–743 are not changed by this place correction.

## Located and inspected: Armstrong to Monroe, 7 January 1806

The item is normally filed in [LOC Monroe Papers reel 3](https://www.loc.gov/resource/mss33217.003/?sp=687), frames **687–689**:

| Frame | Observed content | Identity/control |
|---|---|---|
| [687](https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0687/full/pct:50/0/default.jpg) | First letter page, printed image label 2012 | Heading reads 7th Jan. 1806, Paris; prose discusses the Spanish negotiation, the proposed surrender of three fourths of a claim, and several million dollars. |
| [688](https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0688/full/pct:50/0/default.jpg) | Two-page continuation spread, label 2013 | John Armstrong signature; addressee Mr. Monroe, London; expected arrival of the Emperor and urgency about an occasion appear in the prose. |
| [689](https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0689/full/pct:50/0/default.jpg) | Docket/reverse, with show-through | Partly clipped 7 Jany 1806 / General Armstrong docket agrees with heading and closing. |

These controls jointly match the 1904 calendar's printed-p.18 summary and the 1963 index's four written pages. **Three image frames contain three text pages plus docket writing** because frame 688 is a spread. Written-page counts cannot be treated as image-frame counts.

All three complete images were viewed. They are ordinary prose; no numerical/geometric encoded passage or explicit cipher-key exchange was identified. This bounds this witness only; it does not establish that Armstrong never used a private cipher with Monroe. This is not a certified full transcription. The prose descriptions above are orientation/identity controls, not target cribs.

Navigation retained to prevent another scan of the same interval: acquired 681, 683, 685, 686, 690, 692–695, 705, 710. Frames 681/683 were acquired but not individually read. Inspected anchors included Sullivan's January 6 docket at 686, the January 8 Purviance docket at 692, the January 10 Bath heading at 693, a supplied January 20 date on Bowdoin material at 705, and the February 2 heading at 710. These are locators, not a survey proving no cipher throughout the interval.

## Verified in an open printed source: the Adams cipher transfer

A specific continuation lead in #57 was Adams to Armstrong, 27 November 1809, Huntington **mssHM 22922**, whose catalogue mentions a cipher but has no image. This batch located a bibliographic route and directly checked the separate printed transmission evidence cited in modern discussions.

### Ford, Writings of John Quincy Adams, volume 3

Complete open scan: https://upload.wikimedia.org/wikipedia/commons/c/c2/The_Writings_of_John_Quincy_Adams_Volume_03.pdf
Source item: https://archive.org/details/fordsjohnadams03adamrich
600 PDF pages; 40,949,509 bytes; SHA-256 `8d0389febaf39cd8e70d3870abbdffd842f780a9c45d6a1c05d378f9b754aefa`.

The relevant pages were extracted and visually checked, not adopted from a modern web summary:

- **Printed pp. 322, 327–328 / PDF pp. 352, 357–358:** the cipher instructions are within **Secretary of State to William Short, 8 September 1808**, reused for Adams. Ford's p.322 footnote explains that Adams received copies of instructions supplied to Short and Armstrong. Therefore the words on p.328 must not be represented as a newly composed, independently dated 1809 Smith instruction merely because that page's running header says 1809.
- The instructions distinguish the cipher already supplied, shared with the minister in London, from a copy of Armstrong's cipher to be obtained in Paris. They explicitly describe ciphers known to the Department, allowing forwarded intelligence to be read without reciphering.
- **Printed pp.369–370 / PDF pp.399–400:** Adams's despatch No.8 to Robert Smith is dated **St. Petersburg, 3 January 1810**. It acknowledges letters dated 31 July from Smith and Graham, and a passport, forwarded by J. S. Smith from Stockholm. With those papers Adams acknowledges receiving a copy of Armstrong's cipher and expecting to use it immediately.

This verifies documentary transmission context and its exact date. It does **not** recover a code table, identify THE=972 directly from these pages, establish that every Adams letter used one key, or connect that official cipher to the mixed numerical/geometric private target of February 1808. It supplies no justification for rerunning the completed WE028 or THE=972 target searches.

### Newly precise but still unread: the 1941 publication lead

A bibliographic citation points to Edward H. Tatum Jr., ed., **“Ten Unpublished Letters of John Quincy Adams 1796–1837,” Huntington Library Quarterly 4(3), April 1941**, with the November 27 letter cited at p.376. Crossref's primary deposited record confirms DOI **10.2307/3815711**, the title, volume/issue, authors, and article range **369–388** (not the 369–385 range in one secondary bibliography).

- DOI: https://doi.org/10.2307/3815711
- Deposited metadata: https://api.crossref.org/works/10.2307/3815711
- Primary resource: https://www.jstor.org/stable/3815711
- Citation locator only: https://www.researchgate.net/publication/249376888_The_Monroe_Doctrine_and_Russia_American_Views_of_Czar_Alexander_I_and_Their_Influence_upon_Early_Russian-American_Relations

The article text was **not acquired**. The p.376 link between article and letter remains a secondary citation locator, not independently checked contents. The Huntington catalogue and that citation do not establish what cipher was requested. JSTOR returned a client challenge; it was not passed, bypassed, or treated as article text. No outreach or account login occurred.

Exact retrieval snapshots (metadata/access evidence, not manuscript evidence):

| Input | Bytes | SHA-256 |
|---|---:|---|
| Crossref title-query result, query.title=Ten Unpublished Letters of John Quincy Adams, rows=5 | 8058 | `ece1aa70b472d2c2e535b8ba64b31534269806fda06bf81c6242a4d01290b99e` |
| Crossref /works/10.2307/3815711 | 2767 | `c6b90ab59e418d3c38fd0c49b7cee0656f850b272dd87e48a5db2030822135c2` |
| JSTOR client-challenge HTML | 3038 | `32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea` |

Crossref is mutable metadata; exact future HTTP bytes may change. The durable selected fields are DOI=10.2307/3815711; title as above; volume=4; issue=3; pages=369-388; resource=https://www.jstor.org/stable/3815711. No article plaintext is embedded in this checkpoint.

## Exact source inputs and recovery

The recovery manifest below contains the exact URLs as well as all sizes/hashes. LOC JPEGs are the complete 50% IIIF renditions. The inherited index and calendar hashes were checked before reuse. No target transcription or key table was edited or recomputed in this batch.

| Asset | Bytes | SHA-256 | Dimensions/type |
|---|---:|---|---|
| 0681.jpg | 315189 | `769545e6d7d710bae2139267224372fb5cbc5d6fdb35316c0f3b2cb6046b6556` | 1189×1448 |
| 0683.jpg | 96515 | `02bdd2fd954adb860e112edaafe4b4daf6512f94e23d0d66056b9a10ca82b789` | 1426×1149 |
| 0685.jpg | 351181 | `64d5479279522d2498865cb843481141b510065d69b0c36b0d4fd1e6f1374e18` | 2288×1439 |
| 0686.jpg | 251903 | `d5fa2b8d3fc3038046c1234f9328739d007d7f656f37785e624f435a77b0b7cb` | 1446×1297 |
| 0687.jpg | 409671 | `aac9fd52e4cb25a4bc9b5c539142102340ebb7d2330e694973a534449dfcd81f` | 1208×1777 |
| 0688.jpg | 713916 | `9cf74bc97dc2d080320e5d926adc754f40a29a74e82531711b05000d3f6a96dd` | 2341×1777 |
| 0689.jpg | 325025 | `18eba39ebe108264216280793576d7a4e4b88cb08071d0d7db783da488925b34` | 1764×1209 |
| 0690.jpg | 300182 | `0624073eb726d47a43e2691de4c535b6e59380450fceb083a23d7fc87f584206` | 1193×1523 |
| 0692.jpg | 142372 | `e5978238337d6d9bdf2a5b735ea3b829715556d3021882c14f54a1ba4cd321d3` | 1455×1149 |
| 0693.jpg | 329914 | `160d9d7ccb2a9e8246ebf77bfcae4f851f597519b54c2f38e5ef97994b871b12` | 1189×1429 |
| 0694.jpg | 587697 | `ba5695a99e6cfb43d4d503d832e05b54c7eb7c079f1cb5118f7c316faa883bd4` | 2330×1426 |
| 0695.jpg | 570311 | `2bf88b487bda8b4823536dd6fdc7251fa5d176c7493b615bd40ff6dcc9f66be0` | 2295×1415 |
| 0705.jpg | 268245 | `577abc2cfc9ee85fd4f0468633801ccbb43ec4d99a7ae1066110fe71516ec2a1` | 1113×1339 |
| 0710.jpg | 334194 | `acf438f979cdf958fb7039a9096eacfdd6d6a750d5bea08d06b5902676db01ec` | 1200×1447 |
| r3-0739-50.jpg | 68718 | `174a5ee5e6374c4ed167ee06183245a107576fd61f0e056f4e079f0c303d32f9` | 1269×1001 |
| r3-0740-50.jpg | 298353 | `37d17b5015bf0141c1684f58832e5658a05840263a3257fbd60559475f488609` | 1127×1310 |
| index-1963.pdf | 4500678 | `d8c172a37adeebd9239232339cd2f7fe968b3213eae3f364bbece20cd060db16` | PDF |
| calendar-correspondence-1904.pdf | 14285555 | `8d7ee3c392727f3bdb633f32c30bef85317877dc504f27563082d966003dc300` | PDF |
| ford3.pdf | 40949509 | `8d0389febaf39cd8e70d3870abbdffd842f780a9c45d6a1c05d378f9b754aefa` | PDF |

Inherited target, unchanged and not used for a new search here: 366 decimal groups, 1,885 UTF-8 bytes, SHA-256 `c4ba5db4b1d7bc509b6ab531f6ba90dc9be4d06a3e62b43159c431742e0bc9b2`. The 1841/1843, 203/200, and graphic allograph uncertainties remain. The provisional Livingston readings and suffix ambiguity in #57 are unchanged.

## Completed, running, blocked, and uncertainty

- **Completed:** locate and inspect frames 687–689; retract the false reel-gap inference; correct Erving's city; independently verify the printed index's February entry; acquire and visually verify Ford's instructions/acknowledgement; identify the exact Tatum DOI; execute the recovery capsule, verifying 19 static assets and its text assertions.
- **Running:** none retained after this checkpoint.
- **Locally blocked:** Tatum's text/original Huntington letter remains unread through the attempted endpoints. This is not a total research blocker.
- **Uncertain:** no target-compatible private cipher key; handwriting observations are by the same modern reader, not independent confirmations. SHA checks establish byte identity, not historical interpretation.
- **No new target candidate:** neither a plaintext nor a fitted key emerged. Do not describe source correction or bibliography as decryption.

## Access failures and exclusions

- LOC viewer opens at reel3 sp=739 and sp=690 failed through the web reader. Public tile images were accessible; no authentication or bypass was used.
- Reel3 frame691 50% transfer timed out after 40 seconds with zero bytes (curl 28); it was not retried or used. It is unrelated to the complete 687–689 witness.
- Archive.org metadata for fordsjohnadams03adamrich returned HTTP502. The separately published Commons PDF was successfully acquired. The web PDF reader refused its 40.9 MB size; ordinary download and local rendering succeeded.
- JSTOR stable/3815711 failed via the web reader; direct HTML was a client challenge, not the article. Do not retry unchanged challenge routes.
- Search results, catalogue prose, and OCR were not substituted for manuscript text. No prior stochastic solver or weak-control experiment was rerun.

## One concrete next action

Use the **MHS Adams Papers correspondence/letterbook calendar** to locate a publicly accessible retained copy of **Adams to Armstrong, 27 November 1809** (the precise Huntington mssHM22922 / Tatum DOI lead above). Inspect the request's actual wording and any cited prior cipher exchange before pursuing more generic prose letters. Keep this separate from the verified official cipher acknowledgement of 3 January 1810. A link to the February1808 target requires actual matching symbols, mechanics, or an explicit private-key reference; correspondent overlap alone is insufficient. Do not retry the false January reel gap, unchanged JSTOR challenge, or completed key-family searches.

## Recovery capsule

Save only the following Python block outside the repository. It performs no solver search or Git operation. It verifies 19 static inputs and regenerates the index/letter/date views and five Ford pages for manual review. Dependencies: Python3, Pillow, Poppler. Output is restricted to a new subdirectory of the system temporary directory and refuses Git ancestors.

Executed script SHA-256: `f64522cab07d715380f72f5a1f113e5504468496984c4dd44b7030f84b8cebef`.
Recovery completed successfully: 19 input byte/hash checks, dimensional checks for 16 JPEGs, four documented machine assertion classes; manual interpretation remains explicitly manual.

~~~python
#!/usr/bin/env python3
"""Verify source bytes and regenerate manual-review views outside any repository.
Dependencies: Python 3, Pillow, pdftotext and pdftoppm (Poppler).
No cryptanalysis; byte assertions do not certify handwriting interpretations.
"""
import argparse
import hashlib
import json
import re
import subprocess
import tempfile
import urllib.request
from pathlib import Path
from PIL import Image

MANIFEST = json.loads(r'''{
  "0681.jpg": {
    "bytes": 315189,
    "sha256": "769545e6d7d710bae2139267224372fb5cbc5d6fdb35316c0f3b2cb6046b6556",
    "dimensions": [
      1189,
      1448
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0681/full/pct:50/0/default.jpg"
  },
  "0683.jpg": {
    "bytes": 96515,
    "sha256": "02bdd2fd954adb860e112edaafe4b4daf6512f94e23d0d66056b9a10ca82b789",
    "dimensions": [
      1426,
      1149
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0683/full/pct:50/0/default.jpg"
  },
  "0685.jpg": {
    "bytes": 351181,
    "sha256": "64d5479279522d2498865cb843481141b510065d69b0c36b0d4fd1e6f1374e18",
    "dimensions": [
      2288,
      1439
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0685/full/pct:50/0/default.jpg"
  },
  "0686.jpg": {
    "bytes": 251903,
    "sha256": "d5fa2b8d3fc3038046c1234f9328739d007d7f656f37785e624f435a77b0b7cb",
    "dimensions": [
      1446,
      1297
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0686/full/pct:50/0/default.jpg"
  },
  "0687.jpg": {
    "bytes": 409671,
    "sha256": "aac9fd52e4cb25a4bc9b5c539142102340ebb7d2330e694973a534449dfcd81f",
    "dimensions": [
      1208,
      1777
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0687/full/pct:50/0/default.jpg"
  },
  "0688.jpg": {
    "bytes": 713916,
    "sha256": "9cf74bc97dc2d080320e5d926adc754f40a29a74e82531711b05000d3f6a96dd",
    "dimensions": [
      2341,
      1777
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0688/full/pct:50/0/default.jpg"
  },
  "0689.jpg": {
    "bytes": 325025,
    "sha256": "18eba39ebe108264216280793576d7a4e4b88cb08071d0d7db783da488925b34",
    "dimensions": [
      1764,
      1209
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0689/full/pct:50/0/default.jpg"
  },
  "0690.jpg": {
    "bytes": 300182,
    "sha256": "0624073eb726d47a43e2691de4c535b6e59380450fceb083a23d7fc87f584206",
    "dimensions": [
      1193,
      1523
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0690/full/pct:50/0/default.jpg"
  },
  "0692.jpg": {
    "bytes": 142372,
    "sha256": "e5978238337d6d9bdf2a5b735ea3b829715556d3021882c14f54a1ba4cd321d3",
    "dimensions": [
      1455,
      1149
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0692/full/pct:50/0/default.jpg"
  },
  "0693.jpg": {
    "bytes": 329914,
    "sha256": "160d9d7ccb2a9e8246ebf77bfcae4f851f597519b54c2f38e5ef97994b871b12",
    "dimensions": [
      1189,
      1429
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0693/full/pct:50/0/default.jpg"
  },
  "0694.jpg": {
    "bytes": 587697,
    "sha256": "ba5695a99e6cfb43d4d503d832e05b54c7eb7c079f1cb5118f7c316faa883bd4",
    "dimensions": [
      2330,
      1426
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0694/full/pct:50/0/default.jpg"
  },
  "0695.jpg": {
    "bytes": 570311,
    "sha256": "2bf88b487bda8b4823536dd6fdc7251fa5d176c7493b615bd40ff6dcc9f66be0",
    "dimensions": [
      2295,
      1415
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0600:0695/full/pct:50/0/default.jpg"
  },
  "0705.jpg": {
    "bytes": 268245,
    "sha256": "577abc2cfc9ee85fd4f0468633801ccbb43ec4d99a7ae1066110fe71516ec2a1",
    "dimensions": [
      1113,
      1339
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0700:0705/full/pct:50/0/default.jpg"
  },
  "0710.jpg": {
    "bytes": 334194,
    "sha256": "acf438f979cdf958fb7039a9096eacfdd6d6a750d5bea08d06b5902676db01ec",
    "dimensions": [
      1200,
      1447
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0700:0710/full/pct:50/0/default.jpg"
  },
  "r3-0739-50.jpg": {
    "bytes": 68718,
    "sha256": "174a5ee5e6374c4ed167ee06183245a107576fd61f0e056f4e079f0c303d32f9",
    "dimensions": [
      1269,
      1001
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0700:0739/full/pct:50/0/default.jpg"
  },
  "r3-0740-50.jpg": {
    "bytes": 298353,
    "sha256": "37d17b5015bf0141c1684f58832e5658a05840263a3257fbd60559475f488609",
    "dimensions": [
      1127,
      1310
    ],
    "url": "https://tile.loc.gov/image-services/iiif/service:mss:mss33217:003:0700:0740/full/pct:50/0/default.jpg"
  },
  "index-1963.pdf": {
    "bytes": 4500678,
    "sha256": "d8c172a37adeebd9239232339cd2f7fe968b3213eae3f364bbece20cd060db16",
    "dimensions": null,
    "url": "https://tile.loc.gov/storage-services/service/gdc/gdclccn/62/06/00/06/62060006/62060006.pdf"
  },
  "calendar-correspondence-1904.pdf": {
    "bytes": 14285555,
    "sha256": "8d7ee3c392727f3bdb633f32c30bef85317877dc504f27563082d966003dc300",
    "dimensions": null,
    "url": "https://upload.wikimedia.org/wikipedia/commons/8/82/Calendar_of_the_correspondence_of_James_Monroe_%28IA_calendarofcorres00monr%29.pdf"
  },
  "ford3.pdf": {
    "bytes": 40949509,
    "sha256": "8d0389febaf39cd8e70d3870abbdffd842f780a9c45d6a1c05d378f9b754aefa",
    "dimensions": null,
    "url": "https://upload.wikimedia.org/wikipedia/commons/c/c2/The_Writings_of_John_Quincy_Adams_Volume_03.pdf"
  }
}''')

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--assets", nargs="*", default=[])
    ap.add_argument("--fetch", action="store_true")
    args = ap.parse_args()
    out = Path(args.out).resolve()
    temporary_root = Path(tempfile.gettempdir()).resolve()
    if not out.is_relative_to(temporary_root) or out == temporary_root:
        raise ValueError("Output must be a NEW subdirectory of the system temp directory.")
    if any((p / ".git").exists() for p in (out, *out.parents)):
        raise ValueError("Refusing output inside a repository.")
    out.mkdir(parents=True, exist_ok=False)
    downloads = out / "assets"
    downloads.mkdir()
    roots = [Path(p).resolve() for p in args.assets]
    verified, paths = {}, {}
    for name, item in MANIFEST.items():
        candidates = [root / name for root in roots if (root / name).is_file()]
        p = candidates[0] if candidates else downloads / name
        if not p.exists() and args.fetch:
            with urllib.request.urlopen(item["url"], timeout=55) as resp:
                data = resp.read()
            p.write_bytes(data)
        data = p.read_bytes()
        actual = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
        assert actual == {k: item[k] for k in actual}, (name, actual)
        if item["dimensions"] is not None:
            with Image.open(p) as im:
                assert list(im.size) == item["dimensions"], name
        verified[name] = actual
        paths[name] = p
    def pdf_text(name):
        return subprocess.check_output(["pdftotext", "-layout", str(paths[name]), "-"], text=True)
    def render(name, page, prefix, dpi=180):
        subprocess.run(["pdftoppm", "-f", str(page), "-l", str(page), "-r", str(dpi),
                        "-png", "-singlefile", str(paths[name]), str(out / prefix)],
                       check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    index = pdf_text("index-1963.pdf")
    assert re.search(r"\*ARMSTRONG JOHN TO JM2\s+1806 JA\s+1\s+4", index)
    # OCR drops the January day 7: manually inspect the rendered row.
    assert re.search(r"MADISON JAMES FR JM2\s+1806 FE\s+2\s+1\s+38", index.split("\f")[27])
    render("index-1963.pdf", 18, "index-p18", 300)
    render("index-1963.pdf", 28, "index-p28", 180)
    with Image.open(out / "index-p18.png") as im:
        im.crop((0, 0, 1500, 1100)).save(out / "armstrong-index-row.png")
    calendar = " ".join(pdf_text("calendar-correspondence-1904.pdf").split())
    assert "1806, January 7. Negotiations with Spain" in calendar
    ford = pdf_text("ford3.pdf").split("\f")
    norm = lambda x: " ".join(x.split())
    assert "SECRETARY OF STATE TO WILLIAM SHORT" in norm(ford[351])
    assert "September 8th, 1808." in norm(ford[351])
    assert "cyphers known to this Department" in norm(ford[357])
    assert "ST. PETERSBURG, 3 January, 1810." in norm(ford[398])
    assert "Armstrong's cypher" in norm(ford[399])
    for page in (352, 357, 358, 399, 400):
        render("ford3.pdf", page, f"ford3-pdf-{page}")
    crops = {
        "january-date.png": ("0687.jpg", (650, 50, 1140, 190)),
        "january-continuation-left.png": ("0688.jpg", (0, 0, 1200, 1777)),
        "january-continuation-right.png": ("0688.jpg", (1160, 0, 2341, 1777)),
        "february-docket.png": ("r3-0739-50.jpg", (160, 20, 660, 200)),
        "erving-madrid-date.png": ("r3-0740-50.jpg", (30, 30, 1040, 310)),
    }
    for name, (source, box) in crops.items():
        with Image.open(paths[source]) as im:
            im.crop(box).save(out / name)
    audit = {
        "verified_assets": verified,
        "machine_assertions": [
            "Index lists Armstrong to Monroe in January 1806 (day must be checked visually)",
            "Index PDF28 lists Monroe to Madison, 2 February 1806, 38 pages with copies/covers",
            "Ford's quoted instructions are headed to William Short, 8 September 1808",
            "Ford's 3 January 1810 despatch acknowledges receipt of Armstrong's cipher"
        ],
        "manual_observations_to_recheck": [
            "LOC reel3 frames687-689 identify Armstrong to Monroe, Paris, 7 January 1806",
            "Frame688 is a two-page spread; no encoded passage observed in the full witness",
            "Frame739 reads 2 Feby 1806, not January",
            "Frame740 reads Madrid, not Paris",
        ],
        "not_established": [
            "No recovered cipher table or target plaintext",
            "No evidence equating the shared official cipher with the February 1808 private target"
        ]
    }
    (out / "audit.json").write_text(json.dumps(audit, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"verified_assets": len(verified), "machine_assertions": audit["machine_assertions"],
                      "manual_review_required": True}, indent=2))

if __name__ == "__main__":
    main()
~~~

Example recovery after context loss (new, nonexistent output directory):

~~~sh
python recovery60.py --out /tmp/armstrong-checkpoint60-recovery --fetch
~~~

To reuse independently hashed local assets without re-downloading, add `--assets /absolute/read-only/source1 /absolute/read-only/source2`; no writes occur in those source directories. The navigation frames 681/683 remain unread locators even though their bytes verify.
