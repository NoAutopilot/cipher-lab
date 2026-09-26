# Cryptiana source snapshot

Unmodified copies of pages from S. Tomokiyo's site *Cryptiana: Articles on Historical Cryptography*
and its companion blog, downloaded on 19 September 2026. Copyright remains with the author.

- `web/` — pages from https://cryptiana.web.fc2.com/code/ under their original filenames.
  `unsolved.htm` is the index page ("Unsolved Historical Ciphers", last modified 19 September 2026)
  and every other file here is something it links to. Pages are Shift_JIS encoded; the `.txt` files
  are Tomokiyo's transcriptions of specific ciphertexts.
- `blog/` — posts from https://cryptiana.blogspot.com/ linked from the index page. UTF-8.

Do not edit these files. Working notes and transcriptions belong under `ciphers/`.

To read a page as text:

    python3 tools/html2text.py sources/cryptiana/web/unsolved.htm | less

## Additions, 24 September 2026 (ASSIGNMENTS row 26, Tomokiyo bibliography check)

`bongars.htm`, `spanish3C.htm`, `eleanor1476.htm` fetched from cryptiana.web.fc2.com (one request at a
time, 1.5s apart, descriptive UA, all HTTP 200) as reference for the academia.edu papers listed in
`PAPERS.tsv` -- none is an exact mirror of an academia.edu paper's own text, only a related article by
the same author on a nearby subject; see PAPERS.tsv for the distinction. Tomokiyo's academia.edu profile
(https://independent.academia.edu/SatoshiTomokiyo) itself returned HTTP 403 on the one permitted fetch;
per the good-citizen rule that host was not retried, and the paper list in `PAPERS.tsv` was built instead
from `web/crypto.htm`'s own table of contents (which links out to academia.edu for papers with no htm
counterpart) plus web search snippets of academia.edu's own listing pages. See `PAPERS.tsv` and
`READABLE.tsv`.

## Added 24 September 2026 (ciphers/fr2980-gramont, key images)

| File | URL | Fetched | Bytes | For |
|---|---|---|---|---|
| `web/francisGramont.png` | https://cryptiana.web.fc2.com/code/francisGramont.png | 24 Sep 2026, before 00:17 UTC | 121175 | Tomokiyo's "Gramont's Cipher (1530)" table, embedded in francis.htm (ciphers/fr2980-gramont) |
| `web/GL/BnF_fr3071_f17.png` | https://cryptiana.web.fc2.com/code/GL/BnF_fr3071_f17.png | 24 Sep 2026, before 00:17 UTC | 34169 | Lasry's key table for the same cipher (BnF fr.3071 f.17, dated 04/11/2023), embedded in francis.htm and GL.htm |

## Added 24 September 2026 (ciphers/fr20140-danzay-1557, Cryptiana Discussion Forum gap)

The AUDIT.md "N4 decision (final families)" of 24 Sept 2026 named one family never searched: the Cryptiana
Discussion Forum post announcing Tomokiyo's Danzay article, and its comments. Blogger's JSON feed
(`/feeds/posts/default?alt=json&q=Danzay`, and `&q=20140`, both `sources/cryptiana/blog/`-adjacent, not saved,
one-shot API calls) found exactly one matching post; a WebSearch `site:cryptiana.blogspot.com Danzay` cross-check
agreed and additionally surfaced `.../2025/09/`, a monthly archive index page, fetched and checked (below) and
found not to mention Danzay at all -- a search-snippet false positive, not a second post.

| File | URL | Fetched | Bytes | For |
|---|---|---|---|---|
| `blog/2026_02_reconstruction-of-cipher-used-by.html` | https://cryptiana.blogspot.com/2026/02/reconstruction-of-cipher-used-by.html | 24 Sep 2026, ~07:2x UTC | 85129 | The post itself ("Reconstruction of a Cipher used by Charles de Danzay, French Ambassador to Denmark", posted 22/02/2026), the only post matching "Danzay" or "20140" on this blog |
| `blog/2026_02_reconstruction-of-cipher-used-by.comments.json` | https://cryptiana.blogspot.com/feeds/2892705715433739646/comments/default?alt=json | 24 Sep 2026, ~07:2x UTC | 1299 | Blogger comment feed for the same post: `openSearch$totalResults` = 0. The rendered page independently shows "No comments:" |

`2025/09/` (the monthly archive page WebSearch also listed) was fetched and grepped for `danz` (case-insensitive):
no hits. Not saved, since it is a generic archive index with no Danzay content -- not part of this family.

## Added 24 September 2026 (CITATIONS.md, board hall-of-fame worker)

The committed `web/unsolved.htm` (fetched 19 Sept 2026) predates Tomokiyo's 24 Sept credit for the Bowes 1583
sign table (CONTRIBUTIONS.md row of 23 Sept; ciphers/bowes-walsingham-1583/NOTES.md "Specialist reply"). One
request, browser UA, HTTP 200: `web/unsolved-2026-09-24.htm` is the page as of that fetch and carries the credit
in the "Ciphers related to Sir Francis Walsingham" section -- it names "Ryan Turner" (not the owner's own name,
consistent with rule 9) and links `https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/bowes-walsingham-1583`.
The undated `web/unsolved.htm` is left as is (a distinct earlier snapshot); CITATIONS.md cites the dated file as
evidence.

## Added 26 September 2026 (Tomokiyo's reply to the owner's 24 Sept email, parent worker TOMO-REPLY)

Tomokiyo replied on 26 Sept 2026 to `outreach/tomokiyo-gramont-danzay.md`: he wrote up the Raince/Carpi letter
(ciphers/dupuy452-carpi-1520, digest in that target's own NOTES.md) and named Armstrong-Madison 1808 as his
preferred next target for us (ciphers/armstrong-madison-1808). All three fetches one at a time, 2s apart,
descriptive User-Agent, all HTTP 200.

| File | URL | Fetched | Bytes | sha1 | For |
|---|---|---|---|---|---|
| `blog/2026-09-a-cipher-between-louise-of-savoy-and.html` | https://cryptiana.blogspot.com/2026/09/a-cipher-between-louise-of-savoy-and.html | 26 Sep 2026, ~06:36 UTC | 89594 | 82ba3461600e937c4eefd85f0c2700f2ae28e5aa | Tomokiyo's post on the Raince/Carpi letter, citing our AUDIT.md (via "Ryan Turner", the pseudonym already in use per rule 9) |
| `blog/2026-06-undecoded-armstrongs-letter-1808-sent.html` | https://cryptiana.blogspot.com/2026/06/undecoded-armstrongs-letter-1808-sent.html | 26 Sep 2026, ~06:36 UTC | 85731 | 1e3c9b03b05ac7b1e80caa351a4dd731eb9cc6b6 | Tomokiyo's 4 June 2026 post pointing at his updated `web/madison_armstrong.htm` article (already on disk from an earlier sweep) |
| `blog/dbourdeau-cyphersolver-armstrong.html` | https://dbourdeau.github.io/cyphersolver/armstrong.html | 26 Sep 2026, ~06:36 UTC | 36000 | fde7d4c764f53a2e05a97a976f038333550d80dc | Bourdeau's write-up of a *different* Armstrong-Madison letter (the 30 Aug 1808 postscript, code THE=972) -- named in ciphers/armstrong-madison-1808/NOTES.md as the source of the THE=972 sibling-code table |

## Added 26 September 2026 (ciphers/fr3625-lauriere-1593, NX-LAU2 desk search)

| File | URL | Fetched | Bytes | For |
|---|---|---|---|---|
| `web/nevers_no57.png` | https://cryptiana.web.fc2.com/code/nevers_no57.png | 26 Sep 2026, ~09:34 UTC | 930301 | BnF fr.3995 no.57's key table image (fol.102, "Mons. de Laveriere" to Nevers) -- a candidate period key for fr.3625's Laurière cipher, structurally compatible on its face with Bourdeau's twelve already-published code meanings; not confirmed as the same system. See ciphers/fr3625-lauriere-1593/NOTES.md "NX-LAU2" section. |
