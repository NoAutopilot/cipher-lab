# EXHIBIT-1: three museum-style displays for our three most interesting readings, as a private mock-up (account 4, Opus 5.5, cap USD 12, box 100 min)

Written 9 Oct 2026 22:37 UTC by date -u by the orchestrator (account-4), session_012sGNgiddCpz4QUhQsMyoPU, on the owner's direction at
22:3x UTC (clock-checked 22:37 UTC; earlier drafts wrote 22:4x-22:5x by estimate, wrong): "think about it as if you went to a museum and they set up a display to talk about whatever our cipher is about ... for our
three most interesting solves ... think like the people who make the displays: what are they trying to convey, what are they concerned
about, what are they excited about; for the people who view it: why are they viewing it, what are they hoping to get out of it, why do
they find it interesting, how would it become more interesting for them -- arrangement, assets. Show portraits of the key people."
Earlier in the hour: "exceptionally too wordy; show, not tell; connect the cipher to the history, the key people, places, moments and
events; let me see the cipher, or pieces of it, really easily." Nothing public: a private mock-up for the owner (GitHub Pages is off);
output under research/mockups/exhibit/ only, never docs/. The catalogue mock-up job (CATALOGUE-SITE-1, Amendments 1-4) is separate; reuse
its tools/build_catalogue.py loaders, not its layout.

The three displays (each one self-contained HTML page, plus research/mockups/exhibit-2026-10-09.html that holds all three inline):
1. Gramont at Rome, 1530 (ciphers/fr2980-gramont, Montmorency letter fr.3040 ff.18-19 and Villandry letter fr.2980 f.29r; N4, two audits):
   a French cardinal's cipher from Rome in the weeks the Pope suspended Henry VIII's divorce suit. People: Gabriel de Gramont, Clement VII,
   Henry VIII, Anne Boleyn, Francis I, Anne de Montmorency, Rochefort (as the audit and the reading name them).
2. Manteuffel at Berlin, 1712 (ciphers/sachsstaatsarchiv-manteuffel-1712, f.410 N4 and frame 0391 N3): a Saxon envoy's postscripts on
   what London would and would not do to pacify the North, read with an 1893 manuscript key. People: Ernst Christoph von Manteuffel,
   Jakob Heinrich von Flemming, Augustus II, Frederick I of Prussia, Queen Anne, Robert Harley earl of Oxford, Henry St John viscount
   Bolingbroke, Stanislas Leszczynski, Charles XII, Heusch (the Hanoverian resident).
3. The Nassau brothers at Dillenburg, 1573 (ciphers/lodewijk-van-nassau-1573-74, WVO 5797 N4 and the four 1573-74 letters): the blanks
   a 19th-century edition left in the Orange-Nassau correspondence, filled. People: William of Orange, Louis (Lodewijk) of Nassau, Jan of
   Nassau, Landgrave Wilhelm IV of Hesse, Elector Palatine Frederick III, Groen van Prinsterer (the editor).

Curatorial brief (write this reasoning into research/mockups/exhibit/CURATOR.md before building; two short lists, then the plan):
- The maker conveys ONE story per display (a moment, a secret, a reveal), is concerned about accuracy, attribution and not over-claiming
  (rule 10 wording; the audit's class and depth visible; every image credited and licensed), and is excited by the object itself and the
  reveal -- the cipher line and what it says.
- The visitor comes for a story and a secret; wants to see the real object, to watch the secret open, to recognise faces and a moment they
  half know (a king's divorce, a war's end, a revolt), to try a sign themselves, and to leave with one sentence they can repeat. It gets
  more interesting with: a hero object first; faces; a dated moment; a map; layering (headline, then panel, then proof); a hands-on element.
Display anatomy, in order on the page: (a) HERO: the clearest cipher line crop from the folder's images/, with a reveal (CSS toggle, no
scripts beyond plain inline JS if needed) that writes the reading under the signs token by token, grades as a colour mark; (b) HEADLINE:
one sentence the visitor remembers, licensed by the audit's safe sentence and the depth sentence; (c) FACES: portraits of the key people
from Wikimedia Commons -- public-domain paintings or prints only (PD-Art/PD-old), fetched once through the Commons API (`action=query&
prop=imageinfo&iiprop=url|extmetadata`, descriptive User-Agent, 1.6 s apart, at most 25 requests), saved under research/mockups/exhibit/
portraits/ with a manifest.tsv (file, Commons title, artist, date, licence as extmetadata says, URL) and a caption under each portrait with
five words of role and what that person was doing that month; a person without a PD image gets a labelled silhouette, never a
non-free image; (d) THE MOMENT: a dated strip of the three to five events around the letter (absolute dates, one line each) and a small
map (an inline SVG with the two or three places; no tile service); (e) THE SECRET: the gist once, marked interpretation, with the two or
three cipher words that carry it shown as crops; (f) TRY IT: three signs from the key, click to reveal the value (from key.tsv); (g) HOW
WE KNOW: the proof as badges -- class and depth with their one-line definitions, the two audit dates, grade counts as a bar, the
regenerate script and control as links, "whose key" with the credit (Tomokiyo, the 1893 key, Groen) -- no paragraph over two sentences.
Content rules unchanged: rule-10 wording, nothing restricted, no internal job names, costs or session ids, every image with source and
licence, owner never named. Colours pass tools/cvd_check.py; phone width works. Done line "for orchestrator (account-4)": the single-file
path first, portraits fetched (count, any missing), requests to commons.wikimedia.org, what is left if the cap stopped you; stage by
path (research/mockups/exhibit/**, the single file); never force-push; never AskUserQuestion; never print credentials; no ciphers/ edit.

## Addition (orchestrator, clock 22:38 UTC 9 Oct; the owner): three layers per reading line
Cipher crop; the plain text as read in its own language, aligned to the signs with the grade marks; an English rendering underneath labelled
"English (translation, interpretation)" so anyone can read it. The audited line carries the grades; the English never does.
