# Armstrong–Madison continuation: public source audit and a bounded Warden corpus check

UTC 20260927T224411Z. Objective: a defensible, reproducible decipherment of Armstrong to Madison, 20 February 1808. This batch completes #54's next image inspection, locates a specific 1808 Yale catalogue item, and audits accessible Warden metadata. No target plaintext or new key assignment is asserted.

Parent: [#54](https://github.com/NoAutopilot/cipher-lab/pull/54), immutable head `8a65a8576fba6a9f649867c8b6211067ae2a2d52`, path `ciphers/armstrong-madison-1808/checkpoints/20260927T221154Z.md`. Follow its parent chain through #53–44; the bootstrap remains #44 at `58df6cf8c070c780df86faeec30900729f9229ba`. All-state checks before and after research found #54 newest. #54 has no retained active lease. No batch was taken from another worker.

## Completed manuscript checks

1. LOC mcc.036, Madison to Jefferson, 23 May 1789, page 3: acquired the native 4616×5656 image and viewed the full leaf. It continues in ordinary prose through the closing; no visible encoded span supplies a deletion or non-final doubling control. This is a bounded observation about that leaf. Page 4 was not acquired. #54's page-2 final-letter doubling example remains unchanged.
2. LOC mtjbib001701, resource mtj1.004_1009_1009, Jefferson's 1785–87 Barbary memorandum catalogued as shorthand: acquired the resource metadata and its linked 1093×1033 image. The visible writing contains conventional cursive letters, abbreviations, superscripts and corrections. It does not supply an annotated geometric alphabet or a secure Armstrong glyph match. No shorthand system was identified or excluded. Its catalogue description alone is insufficient for a recognition control.

Both visual observations are one-reader provisional. No new blind control, numerical accuracy estimate, or decipherment follows from them. The supplementary look at the page-2 plural-like marks did not authenticate an affix rule and was not added to the fixture.

## A specific 1808 catalogue lead, not a plaintext crib

[Yale MS 857 finding aid](https://ead-pdfs.library.yale.edu/4476.pdf), PDF page 17 (zero-based 16), box 4 folder 116, lists a 25 April 1808 statement and covering memorandum about an Armstrong letter concerning the purchase of Florida. The catalogue's tentative attributions are [Smith, John, 1735–1816?] and [John?] Armstrong. The manuscript itself was not acquired. Neither its subject nor its date establishes a link to the cipher dated 20 February.

The same aid's Erving series explicitly says his correspondence is not preserved there. Its 1805–1808 memoranda book is box 5 folder 164; folder 169 holds copies/translations of Decres-to-Armstrong letters dated 24 December 1806 and 20 March 1807. Do not mistake these descriptions for an encoded witness. Digitization flags on other folders do not establish that folder 116 is digitized. The canonical handle yielded no usable page in this run; no public image emerged from the exact-item searches.

## Warden holdings and public data: distinguish the sources

- [LOC finding aid](https://tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/ms012085/ms012085.pdf): box 1 includes the alphabetical A correspondence; box 23 contains papers relating to the case against Armstrong; box 25 includes consular material for 1806–1810 and an 1800–1810 letterbook. This confirms the existing LOC lead. No manuscript in those boxes was read.
- [NARA's microfilm catalogue](https://www.archives.gov/nhprc/projects/catalog/david-bailie-warden) describes a **Maryland Historical Society** edition, eight reels and a 21-page guide. This is not LOC box 25. The [current MCHC MS 0871 catalogue](https://mdhistory.libraryhost.com/repositories/2/resources/120) is accessible, replacing the failed legacy MDHS address. It describes outgoing letterbooks beginning in 1807 and letters received beginning in 1804; access is restricted to microfilm. Its own public tree endpoint, obtained from the page's linked JavaScript, returns zero children and zero waypoints. That means this public inventory exposes no item records, not that the physical collection is empty.
- The [APS catalogue](https://as.amphilsoc.org/repositories/2/resources/2314), indexed primary-source snippet, identifies its copy as Mss.Film.1290, reels 1–8, and describes letterbooks for 1811–1844 and registers for 1807–1815. The direct page did not load. The numbers of particular volume types in secondary guide records remain unverified; do not turn those snippets into manuscript evidence.
- The Maryland Historical Society's own survey by William D. Hoyt Jr., [1941, pp. 302–314](https://msa.maryland.gov/megafile/msa/speccol/sc5800/sc5881/000001/000000/000143/pdf/msa_sc_5881_1_143.pdf), distinguishes the Washington and Baltimore holdings and reports that they complement one another. Its [1943 continuation, p. 69](https://msa.maryland.gov/megafile/msa/speccol/sc5800/sc5881/000001/000000/000149/pdf/msa_sc_5881_1_149.pdf) describes twenty Armstrong letters dated 1804–1810, including office instructions written while travelling. These are an archivist's descriptions, not a full edition or proof of an 1808 cipher key. PDF zero-based pages 66 and 75 locate the relevant descriptions. No positive cipher/shorthand evidence was found in the inspected descriptions.

### Reproducible check of the linked Newcastle pilot

The [Newcastle project description](https://research.ncl.ac.uk/atnu/projects/transatlanticintellectualnetworks/) says its pilot uses a selected 1817–1845 corpus. Its main transcription site returned HTTP 502. Following its public link to Sharon Howard's visualizations located the accessible [source repository](https://github.com/sharonhoward/dbw/tree/b800c530221c6c6936471ac00aefecd6b7073dd7), pinned here at immutable commit `b800c530221c6c6936471ac00aefecd6b7073dd7`.

The repository contains metadata and network analysis, not the complete correspondence transcription. Its recursive tree was complete, not truncated. I audited both letter metadata files:

| Input | Raw rows | Numeric year range after trimming | Undated rows | Nonempty query flag |
|---|---:|---|---:|---:|
| dbw2_letters_metadata_20200719.csv | 535 | 1817–1831 | 0 | 14 |
| dbw3_letters_metadata_20200719.csv | 576 | 1832–1846 | 97 | 7 |

These are raw records, not a claim that every row is a transcribed letter. The author's analysis excludes nonempty query flags and performs additional date corrections. The 1846 value is present in the metadata even though the general project description says 1845.

Neither file has “Armstrong” in the sender/recipient fields or a 1800–1809 year in the three date fields. An initial whole-row search found “1808” only inside object identifiers, which is not a date match. Leading/trailing spaces in year fields must be trimmed (61 dbw2 rows have a trailing space). The recovery code implements the corrected field-specific check.

This bounds the accessible subset only. Ninety-seven undated rows remain; absent Armstrong names in these fields do not exclude mentions in unacquired letter bodies. A secondary citation to an 1801 object on the main pilot site could reflect wider coverage, but that object was not acquired. Do not claim the entire project or Maryland archive excludes 1808 material.

## Other catalogue routes bounded this run

- [NYHS Rufus King MS 1660](https://findingaids.library.nyu.edu/nyhs/ms1660_rufus_king_papers/all/): 1802 correspondence at box 8 folder 9; letterbook E, volume 67, covers 8 January 1802–12 April 1803. The acquired HTML text has no whole-word cipher/cypher/code occurrence. That is a catalogue keyword result, not a manuscript audit.
- [NYHS Erving–King MS 204](https://findingaids.library.nyu.edu/nyhs/ms204_erving_king_family/all/): box 3 E16-A general Erving correspondence, 1801–1850; E16-C photocopied Monroe correspondence, 1802–1816 and undated. No Armstrong item was established.
- [FDR Hudson River manuscripts aid](https://www.fdrlibrary.org/documents/356632/390886/findingaid_roos_hudsonmanuscripts.pdf/5b0e08ba-5f8c-48f4-a801-3835452fec2a), PDF pp. 17–18: Aldrich family/Rokeby material is one microfilm roll, roughly 200 items, over half concerning the French ministry. The collection-specific entry requires family-owner permission despite the general cover's unrestricted wording. No access request was made.
- [William & Mary catalogue item](https://scrcguides.libraries.wm.edu/repositories/2/archival_objects/290725): the indexed description of Conway Whittle papers, box 3 folder 13, includes William Lewis correspondence/orders and a dispatch list dated 15 April 1808. Direct access returned 403; manuscript and possible relationship to the target remain unread.
- Gale's [Warden product catalogue](https://gale.com/product-catalog/16612947) identifies an Archives Unbound manuscript product and institutional access. No institutional session was assumed or accessed.

The current Schmeh target article was rechecked; its visible comments still ended at 31 August 2026. No verified full solution or new key emerged. Another commenter's stated archive request is not an action by this worker. Earlier unsupported cribs and shorthand identifications were not adopted.

## Access outcomes to preserve once

Do not repeat unchanged failures as progress: the Cryptiana June-2026 link led to a Google challenge; Founders returned robots restrictions; SNAC 36007662 and the legacy MDHS MS 871 address returned 403; the Yale handle yielded an empty local response; the William & Mary item and USNA manuscript index returned 403. APS direct access returned 403 locally / timeout through search. Newcastle /home returned 502, a potentially transient failure, not a reason to disable continuation. The search tool could not open Howard's redirected page, but its explicitly linked public GitHub Pages address and pinned source repository were accessible.

A raw GitHub search URL was rejected as an unsupported connector argument; the supported repository-search tool worked. No access controls, login screens or challenges were bypassed. No outreach, archive request, or new automation was initiated.

## Recovery and exact inputs

The Python capsule below embeds all 18 acquired input URLs, byte counts and SHA-256 hashes. Save it outside a repository as recover_sources.py. Obtain assets at the URLs in DATA, keeping each name, then run:

`python recover_sources.py /scratch/input-directory /scratch/new-output-directory`

It hashes every available asset, fails on a changed asset, separately reports missing assets, reproduces the two metadata audits and checks the MS 0871 public-tree response. It writes only outside repositories. Static image/PDF URLs can be reacquired; HTML/JSON may change. A changed live response requires a fresh source review, not silently replacing the recorded hash. Immutable GitHub CSVs are pinned independently.

The capsule was executed against all 18 captured inputs: all hashes matched, no input was missing, both metadata fixtures and the zero-child tree check passed. This verifies byte identity and computations, not historical interpretation. No blind solver, old failed search, or expensive winning-result search was rerun.

```python
import csv, hashlib, json, re, sys
from pathlib import Path
DATA = [{"name":"mcc036-3.jpg","url":"https://tile.loc.gov/image-services/iiif/service:mss:mssmcc:036:0003/full/pct:100/0/default.jpg","bytes":2697547,"sha256":"f4ae4c3e2cf63efbd5419e72612306d6d0d5226b04f8f3b7598677b5c354ef14"},{"name":"barbary.json","url":"https://www.loc.gov/resource/mtj1.004_1009_1009/?fo=json","bytes":28840,"sha256":"ca7f5e192ca7a47e72f29d9269160f09d264aa626b55d1615c2d4c65740474f4"},{"name":"barbary.jpg","url":"https://tile.loc.gov/storage-services/master/mss/mtj/mtj1/004/1000/1009.jpg","bytes":109626,"sha256":"61c1c17ddd10942cc4bd6256951caac62082bc9db94d1c2045db22e934e4d305"},{"name":"yale-ms857.pdf","url":"https://ead-pdfs.library.yale.edu/4476.pdf","bytes":542494,"sha256":"d653fdc854a1f1bf2957517fb2a308f2ce27c93451f1adb912c4c5d6764d53b4"},{"name":"warden-findingaid.pdf","url":"https://tile.loc.gov/storage-services/service/gdc/gdcfindingaidpdfs/ms012085/ms012085.pdf","bytes":124556,"sha256":"4c6d0fcefa2a7ada38a5d07cdf606a07e8a51638ac5e15b415b9ed23ca7f13f5"},{"name":"fdr-hudson-findingaid.pdf","url":"https://www.fdrlibrary.org/documents/356632/390886/findingaid_roos_hudsonmanuscripts.pdf/5b0e08ba-5f8c-48f4-a801-3835452fec2a","bytes":952161,"sha256":"700f74d4b023cbfe99eb957950b8a3177c01e9f7fee4486c8a650d17030ee633"},{"name":"king-findingaid.html","url":"https://findingaids.library.nyu.edu/nyhs/ms1660_rufus_king_papers/all/","bytes":328971,"sha256":"83f1e2504a393b706b31659aa5508f4641be1bae568c7c439ef8cba5adb51809"},{"name":"erving-king-findingaid.html","url":"https://findingaids.library.nyu.edu/nyhs/ms204_erving_king_family/all/","bytes":298489,"sha256":"c37bf7c1efe0cef892389d77b28171c3db823731b708345032ea9d1919d04e7b"},{"name":"warden-nhprc.html","url":"https://www.archives.gov/nhprc/projects/catalog/david-bailie-warden","bytes":36461,"sha256":"eef8ed9d2575b8377d42fef3b947f0a00727ceca5ede9aa78e606de8ba58f462"},{"name":"warden-ms871.html","url":"https://mdhistory.libraryhost.com/repositories/2/resources/120","bytes":35534,"sha256":"e832f0e1835fb7cbbad96f02e353584dbf78c66169b59c4e2138898defee0466"},{"name":"warden-tree.js","url":"https://mdhistory.libraryhost.com/assets/largetree-49dd3ef557a761c55c8324e47f5b7bfe81dac60557571bae017a8cadc7c85135.js","bytes":11816,"sha256":"49dd3ef557a761c55c8324e47f5b7bfe81dac60557571bae017a8cadc7c85135"},{"name":"warden-tree-root.json","url":"https://mdhistory.libraryhost.com/repositories/2/resources/120/tree/root","bytes":260,"sha256":"b6e3480031bfe2f20ef73a23a7da3a286212c0fa496dc90360b1b18a4b792911"},{"name":"warden-1941.pdf","url":"https://msa.maryland.gov/megafile/msa/speccol/sc5800/sc5881/000001/000000/000143/pdf/msa_sc_5881_1_143.pdf","bytes":8605117,"sha256":"6bc782d81c6bec595c56224e5d7a4560e273f3076f74017db14887464e71978c"},{"name":"warden-1943.pdf","url":"https://msa.maryland.gov/megafile/msa/speccol/sc5800/sc5881/000001/000000/000149/pdf/msa_sc_5881_1_149.pdf","bytes":7479659,"sha256":"de171c53b8152cc399d743e8394e11ca9ad59304427ccab98ae6bea468836eb7"},{"name":"warden-project.html","url":"https://research.ncl.ac.uk/atnu/projects/transatlanticintellectualnetworks/","bytes":17634,"sha256":"a2b1bf7f4a7e87fc9be545f4f5b475f706e50ff31107c3577e7154f4999567d9"},{"name":"warden-d3.html","url":"https://raw.githubusercontent.com/sharonhoward/dbw/b800c530221c6c6936471ac00aefecd6b7073dd7/docs/dbw_networks_d3_0715.html","bytes":39682,"sha256":"f949183f52639093d59bf915b1d1f26cca78fa255d504759fec7d35e99869822"},{"name":"dbw2_letters_metadata_20200719.csv","url":"https://raw.githubusercontent.com/sharonhoward/dbw/b800c530221c6c6936471ac00aefecd6b7073dd7/data/dbw2_letters_metadata_20200719.csv","bytes":79375,"sha256":"a7f0006ab0b6208c52205814a76ac86a83855ffd0721fb379dee5d1fe42247eb"},{"name":"dbw3_letters_metadata_20200719.csv","url":"https://raw.githubusercontent.com/sharonhoward/dbw/b800c530221c6c6936471ac00aefecd6b7073dd7/data/dbw3_letters_metadata_20200719.csv","bytes":75523,"sha256":"8c53b989e7befdc4f68e184371bcf0675ec915c579a1bdab516613f76a5f2de1"}]
src, dst = map(lambda x: Path(x).resolve(), sys.argv[1:3])
for p in (src, dst):
    assert not any((q/".git").exists() for q in (p, *p.parents)), "Use scratch outside repositories"
assert not dst.exists(), "Use a new output directory"
verified, missing = [], []
for a in DATA:
    p = src/a["name"]
    if not p.exists():
        missing.append(a["name"])
        continue
    b = p.read_bytes()
    assert len(b) == a["bytes"] and hashlib.sha256(b).hexdigest() == a["sha256"], a["name"]
    verified.append(a["name"])
summary = {}
for part, expected in [(2, (535, 1817, 1831, 0, 14)), (3, (576, 1832, 1846, 97, 7))]:
    name = f"dbw{part}_letters_metadata_20200719.csv"
    if name not in verified:
        continue
    rows = list(csv.DictReader((src/name).open(encoding="utf-8", newline="")))
    years = [int(r["year"].strip()) for r in rows if r["year"].strip().isdigit()]
    actual = (len(rows), min(years), max(years), sum(r["year"].strip()=="Undated letters" for r in rows), sum(bool(r["query"]) for r in rows))
    assert actual == expected, (name, actual)
    early = [r["obj_id"] for r in rows if any(re.search(r"\b180[0-9]\b", r[k]) for k in ("year", "date_sent", "date_when"))]
    armstrong = [r["obj_id"] for r in rows if "armstrong" in (r["sender1"]+" "+r["recipient1"]).lower()]
    assert early == [] and armstrong == []
    summary[name] = dict(zip(("raw_rows", "minimum_year", "maximum_year", "undated_rows", "query_flagged_rows"), actual))
    summary[name].update(date_1800_1809_rows=early, armstrong_sender_recipient_rows=armstrong)
if "warden-tree-root.json" in verified:
    tree = json.loads((src/"warden-tree-root.json").read_text())
    assert tree["child_count"] == 0 and tree["waypoints"] == 0
    summary["ms871_public_tree_children"] = 0
dst.mkdir(parents=True)
result = {"verified_assets":verified, "missing_assets":missing, "metadata_audit":summary,
          "caution":"This verifies the captured bytes and bounded metadata counts, not manuscript readings or a target decipherment."}
(dst/"audit.json").write_text(json.dumps(result, indent=2)+"\n")
print(json.dumps(result, indent=2))

```

## State and one concrete next action

Completed: #54 page-3 audit; unrelated shorthand memorandum inspection; exact Yale catalogue locator; holdings/access distinctions; Warden public metadata audit and runnable recovery.

Running: none. Active lease: none retained. Blocked components: unacquired Brant complete Livingston key, Warden/Armstrong manuscripts, and Yale folder 116. No material blocker requiring a new user action was established; publicly available annotated Livingston material remains useful.

**Next action:** expand one still-unresolved historical control in the existing September 17, 1803 Livingston witness, not the already-completed September 11 batch. Start from #43's `SEP17-middle` crop of `pool/liv/img/mjm014121_p_1064.jpg`, coordinates `[1870,910,3576,1430]`. Re-read only the interlinear over the preserved run `1011 911 408 1105 1456 968 1426 1133 1221 978`, focusing on `1426 1133` and `978`, and locate a separate plaintext/copy witness if available. Preserve faint readings and all modifying marks; do not fill the gap from an attractive English sentence. #43's “been” remains faint, and #53's 1583/full restriction still applies. Save the new crop/alignment even if only one entry becomes defensible. This is an authenticated-source/control task, not permission to transfer that key to Armstrong.

Keep the #48 target event alignment and transcription alternatives; do not restart from the article's old transcription. Recover saved solver winners from #44 instead of rerunning. Keep routine negative results in checkpoints without an “unsolved” notification. Notify only for a defensible decipherment, a substantial independently supported candidate requiring verification, or a material blocker needing user action.

## Append-only delivery constraints

This branch was created from the observed current remote main `5f2818d51142a9386ac6273fd411e9a8e60a2969`: `second-opinion/armstrong-checkpoint-20260927T224411Z`. Intended repository change is exactly one new file, `ciphers/armstrong-madison-1808/checkpoints/20260927T224411Z.md`. No existing repository file was edited; main was not written or pushed; no merge was performed. The landing worker may copy the checkpoint and close the PR unmerged. Before treating delivery as complete, the worker verifies the commit parent, one ADDED file, zero deletions, and byte-for-byte remote text. Any later continuation must create another fresh branch from then-current remote main and another single new checkpoint; never edit this file, ROOM.md, STATUS.md, status.json, or queue TSVs.
