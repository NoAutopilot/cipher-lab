LEADS REQUEST, label SO-MATIGNON-LEADS

We are an AI-assisted open cipher-research repository (github.com/NoAutopilot/cipher-lab; a person plus AI
agents). We are NOT asking you to verify a reading -- we want leads, because our own cryptanalysis has stalled
on this target after several tries. Be concrete: named archives, named editions, named scholars, and what you
would try first if this were your own project.

THE ITEM
- Correspondence: Forget / duc de Mayenne / maréchal de Matignon, League-period cipher, 1585-86.
- Manuscript: Bibliothèque nationale de France, ms. français 15572 (main leaves) + fr.15571 f.177/f.179
  (Cipher-3, a related sign inventory, not yet aligned to any leaf).
- Key: recovered and published by Daniel Bourdeau (github.com/dbourdeau/cyphersolver, folder `matignon1586/`,
  commit fc0c9e8, CC BY 4.0 text / MIT code) from the manuscript's own contemporary decipherments on ff.14v/15r,
  18-21/19 and the f.78v/79r margin. 87 codes; about half remain unresolved ("+") in his key.
- Our reading with that key by straight substitution: H 10,074 / M 1,648 (ambiguous codes) / U 1,272 (unkeyed),
  against a fr16 (16th-c. French) language judge: target score -1.371 vs a scrambled-order control -1.786
  (3 seeds), word coverage 0.814 vs 0.678 -- a real, reproducible margin over the control, but the judge itself
  still FAILs the target (real-prose p05 is -0.837). Several independent attempts (native-image line-order
  checks, two hand-alignment passes of the f.78v/79r margin against known-answer controls, an M/U beam search)
  have not moved a single one of the 1,272 unkeyed codes to a confirmed value; every known-answer control run
  against this specific margin decipherment has failed its own pre-registered gate (9/20, 11/20, 8/8-with-one-
  miss across three seeds). Full log: AUDIT trail in NOTES.md below.
- Our files: reading (with U codes unresolved) https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/matignon-mayenne-1586/reading.txt,
  ciphertext https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/matignon-mayenne-1586/ciphertext.txt,
  key (Bourdeau's, reformatted) https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/matignon-mayenne-1586/key.tsv,
  full notes and search log https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/matignon-mayenne-1586/NOTES.md.

WHAT WE HAVE ALREADY CHECKED (do not just repeat these)
- Tomokiyo's own page (`cryptiana.web.fc2.com`, henryiii.htm) still lists every leaf here as undeciphered.
- Bourdeau's own repository notes: "no printed decipherment of these despatches was found" (searches on the
  BnF catalogue and on the literature, 17 Sept 2026).
- Internet Archive full text of both 1916 Labande editions of "Correspondance de Montaigne avec le maréchal
  de Matignon (1582-1588)" (`correspondancede00montuoft`, `correspondanc00mont`): zero hits for 1585, 1586,
  Mayenne, or Forget anywhere in either volume.
- No printed correspondence edition of Mayenne, and no Société de l'Histoire de France "Lettres de Henri III"
  volume, found on Internet Archive at all.
- Both solver repositories (dbourdeau/cyphersolver, aaymeloglu/unsolved-ciphers) grepped, OpenAlex and
  Semantic Scholar queried: no hit.

WHAT WOULD ACTUALLY HELP (leads, not a verdict)
1. Known cipher keys of the same chancery, decade or correspondents: is there a published key or partial
   nomenclator for the Mayenne/League cipher family of the 1580s-90s, or for Matignon's own chancery, beyond
   what Bourdeau already recovered from this manuscript's own margins?
2. Printed editions or calendars that might cover this exact correspondence even without naming "cipher":
   Guise-League correspondence editions, a Bibliothèque nationale finding aid or catalogue note for fr.15571/
   15572 that names a modern edition, any 19th/20th-century Ligue-period documentary collection (Documents
   inédits sur l'histoire de France; a regional archival society bulletin for Basse-Normandie/Alençon, since
   Matignon was governor there).
3. Sibling letters in the same volume (fr.15571/15572) or a related volume with their OWN period decipherment
   already printed alongside the cipher -- these would give us more known-answer key material the way ff.14v/
   15r and 18-21/19 already did, which is exactly what our stalled M/U beam search needs.
4. A scholar who has written specifically on this cipher, this correspondence, or 1580s French League ciphers
   generally (a name, an article, a thesis) -- even one we could contact.
5. What would you try first, given everything above, to move the 1,272 still-unkeyed codes?

HOW TO REPORT
- Write your answer as one Markdown file at `ciphers/matignon-mayenne-1586/second-opinions/chatgpt-leads-2026-09-26.md`
  in github.com/NoAutopilot/cipher-lab. Do not touch any other file. Create branch
  `second-opinion/SO-MATIGNON-LEADS` and open a pull request titled exactly
  `[SO-MATIGNON-LEADS] leads: Matignon/Mayenne cipher, BnF fr.15572`.
- Header: `label: SO-MATIGNON-LEADS`, `model: <your model name and version>`, `date: <UTC date>`,
  `prompt: PROMPT-chatgpt-leads.md in this folder`, then your leads under headings matching items 1-5 above.
- Every citation needs author, title, year, volume/page and a URL (Google Books, HathiTrust, Internet Archive,
  Gallica, a publisher, or an archive catalogue record) or mark it "unverified". Never invent a page number.
- We are not asking you to confirm or deny that this is a first decipherment -- only a separate verifier on
  our side makes that call. Leads only.
