# Browser-agent probe for the owner's ChatGPT instance (5 Oct 2026)

Purpose: find out which hosts that block our cloud sessions the owner's ChatGPT browser agent can reach, so desk cards
can move from the owner to it ("runner before owner", .claude/briefs/parent.md). One attempt per host, no bypassing.
Results land as one pull request; images never go into the public repository.

## Paste this

You are the cipher-lab browser runner. This is a short capability test, not research. Rules: one attempt per site
(one retry after a pause at most); if you meet a captcha, a "verify you are human" page or a login wall, do not try
to get past it -- record `blocked: <what you saw>` and move on. Never put an image, PDF or screenshot into the public
repository NoAutopilot/cipher-lab. Never write a password or the owner's personal details anywhere.

Tests (record for each: reached yes/no, what you saw, the largest image size in pixels you could get, and how):
T1. Spanish National Library viewer: open http://bdh.bne.es/bnesearch/detalle/bdh0000186627 (letter of Ferdinand,
    4 Nov 1478). Open the viewer, go to page 1, zoom in to about 200-250%, and take one screenshot of the first 4-5
    lines of the squiggly cipher (it starts after the words "soy maravillado"). Note the pixel size of the screenshot
    and of the largest download the viewer offers (JPEG/TIFF/PDF).
T2. HathiTrust: open https://babel.hathitrust.org/cgi/pt?id=uc1.b4213431&seq=9 (any page view is fine). Reached, or
    a Cloudflare / "verify you are human" page?
T3. Real Academia de la Historia: open https://bibliotecadigital.rah.es/es/consulta/registro.do?id=100000 . Reached,
    or an "Anubis" / challenge page?
T4. Uploading: can you add a file to the PRIVATE repository NoAutopilot/cipher-lab-private (GitHub tools or the
    browser)? If yes, upload the T1 screenshot as bne20211-ferdinand-1478/images-123-shots/runner-probe-1.png. If you
    cannot, say so -- that is a useful answer.
T5. Downloads: if the owner pastes a file-share link into this chat (Hightail or similar), can you download the file
    and do T4 with it? Skip if no link was pasted.

Report: create branch chatgpt-probe/2026-10-05 from main in NoAutopilot/cipher-lab, add ONE text file
tools/data/runner-probe-2026-10-05.md (first lines `label: RUNNER-PROBE`, `model: <your model>`, `date: <UTC date>`,
then a table T1-T5: test | reached | what you saw | largest pixels | how), and open a pull request titled
`[RUNNER-PROBE] browser agent capability test, 5 Oct 2026`. Text only. Never commit to main, never merge. End with
one line per test.
