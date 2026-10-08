blocked
Berger de Xivrey/Guadet, Lettres missives de Henri IV viii (archive.org recueildeslettre08henruoft, djvu full text, year 1593 run pp.~490-504: 19 Dec Vernon to Châlons, 22 Dec Mante to Toulon, no letter to Nevers) and ix (recueildeslettre09henruoft, whole-volume grep "Nevers", "Decembre"/"1593", itinerary for Dec 1593) read by this worker, letter absent; Gomberville, Mémoires de Nevers ii (Gallica bpt6k64451005 ContentSearch "Mante", "Decembre", "Decembre 1593", "vingt-deuxiesme", "vingt-quatriesme": the Henri IV-to-Nevers letter run ends at 17 Nov 1593, PAG_371) read, letter absent; blocked because the secretary-of-state edition, Monts de Savasse, Gal and Soulingeas, *L'Europe d'Henri IV: la correspondance diplomatique du secrétaire d'État Louis de Revol, 1588-1593* (PUG 2004; HathiTrust mdp.39015060819482, search-only), could not be opened from the cloud (HTRC EF API HTTP 500 twice, 8 Oct 2026).

# BnF fr.3988 f.143r-144v (address f.145v): Henri IV to the Duke of Nevers, Mante, 22/24 Dec 1593 (key no.60)

- Holding: BnF Français 3988, Gallica ark btv1b9060634t, canvases 304-308 (cipher; c304 stamped "143", headed
  "24 de Dec 1593"), 309 the address leaf. BnF finding aid (cc504266) catalogues it as 22 Dec 1593, Mante; Tomokiyo
  league.htm no.76 "(fol.143) Henry IV to Duke of Nevers, Mante, 22 December 1593".
- Key: Nevers collection cipher no.60 (`tools/keys/key60.tsv`, Tomokiyo's reconstruction, Bourdeau's CC BY 4.0
  `nevers1593/key60.txt`). The key family for this leaf is not established: KHF-4's held-out tile test was a
  NON-TEST (the negative control also scored in-family), see `ciphers/fr3985-nevers-revol-1593/NOTES.md` "Keyhunt 7 Oct 2026".
- Prior work in this repo (all in fr3985 NOTES): KH1-B and KH1-F (7 Oct; no gloss on c304-307, Lettres missives
  iii-iv Dec 1593 entries read, letter absent); KHF-4 (NON-TEST); SA-G (c308 is the closing cipher page).
  Transcription passes on disk: `ciphers/fr3985-nevers-revol-1593/keyhunt_f143/passQ.tsv` (N=177), `passP.tsv` (N=466).
- Checked by KH-CS3 (account 2, session_01NaTaidASRG7Yz1ytE9HkMT), 02:12-02:4x UTC 8 Oct 2026 by date -u, brief
  `.claude/briefs/runs/2026-10-08-acct3-scout-jobs.md` section KH-CS3, following `.claude/briefs/check-solved.md`.

## Check-solved (KH-CS3, 8 Oct 2026)

1. **Print, sender side.** Lettres missives iii-iv: read by KH1-B/KH1-F on 7 Oct (fr3985 NOTES), not repeated.
   Supplement viii (Guadet 1872, `recueildeslettre08henruoft`): the 1593 run lists 11, 29, 30, 31 Jan ... 5 Oct,
   19 Dec (Vernon, to the maire of Châlons, which mentions Nevers "maintenant à Rome" but is not to him) and 22 Dec
   (Mante, to the consuls of Toulon); no letter to Nevers in Dec 1593. Supplement ix (Guadet 1876,
   `recueildeslettre09henruoft`): whole-volume grep for "Nevers"/"duc de Nevers" (no Dec 1593 hit), "1593" (the
   itinerary: Dec 1593 at Vernon/Mantes, letter counts only). Also checked: `bub_gb_m22_ykS5xqYC` is a second copy of viii.
2. **Print, recipient side.** Gomberville, *Les Mémoires de M. le duc de Nevers* (1665) ii, Gallica bpt6k64451005,
   ContentSearch: "Mante" 28 hits (latest dated letter "De Mantes le 4. iour Septembre 159[3]", PAG_316), "Decembre"
   37 and "Decembre 1593" 46 (Dec 1593 hits are the Rome-embassy discourse, PAG_454-472, a Paris narrative, PAG_693,
   and a consistory act, PAG_699; no royal letter of 22-24 Dec 1593), "vingt-deuxiesme" 130 and "vingt-quatriesme"
   (no Dec 1593 royal letter). The king-to-Nevers letter run in this volume ends "De Lignerolles ... 17. iour de
   Nouembre 1593" (PAG_371). OCR-dependent: a ContentSearch zero is a search result.
3. **Print, office side (unread -> blocked).** The Desenclos open texts on disk (`sources/desenclos/2026-10-04/raw/ft/`,
   grepped by this worker, inline, without rewriting `search-log.tsv`) cite Monts de Savasse, Gal and Soulingeas,
   *L'Europe d'Henri IV: la correspondance diplomatique du secrétaire d'État Louis de Revol, 1588-1593*, Grenoble,
   PUG 2004 (OCLC 57372956; reviewed in BEC 2005, OpenAlex W979243454). Desenclos and Lasry (`dl-1592.txt`) cite it for
   the symbol ciphers of the king's diplomatic letters. Revol was the secretary of state who countersigned the king's
   letters to Nevers at Rome (Gomberville's Revol hits are royal countersignatures), so this edition may print or
   calendar f.143, possibly with a decipherment. The edition is not named anywhere else in this repository (grep, 8 Oct 2026).
   Routes tried: Google Books API (`isbn:9782706112447`, title and author queries, `country=US` + key): 0 volumes;
   HathiTrust Bibliographic API: record 004994854, htid mdp.39015060819482, "Limited (search-only)"; HTRC Extracted
   Features `ef-api/volumes/mdp.39015060819482/pages`: HTTP 500 "No primary node is available" twice, 20 s apart
   (server-side, one retry spent); OpenEdition search: no hit. Not opened.
4. **Solver repositories.** Fresh shallow clones on 8 Oct 2026. dbourdeau/cyphersolver at 1fb3c46 (7 Oct 2026):
   `targets/nevers1593/NOTES.md` l.126 lists "fr. 3988 ff. 99, 119, 143" only as the interlined Henri IV letters from
   Tomokiyo's no.60 list. There is no transcription, decode or next-step line for f.143 (grep 3988, f.143, nevers1593,
   btv1b9060634t over the repository). aaymeloglu/unsolved-ciphers at d2800bb (27 Sept 2026): the only "3988" hits are
   DECODE record 3988 (TNA SP 53/23, unrelated) and a PARES id; no Nevers or fr.3988 row. Cited, nothing copied.
5. **DECODE.** On-disk listing (`sources/decode/`): "3988" occurs only as record ids in the key lists, with no BnF fr.3988
   record. Not queried live (no login needed for this check).
6. **Web and blogs.** See "`python3 tools/next_steps.py --wait-only | grep fr3988` (8 Oct 2026): no line (grep exit 1).

## Web and blog check" below; no decipherment or plaintext of this letter found.

Verdict: `blocked`, on the unread Revol edition only. Every other source family returned "letter absent" (search
results, not novelty statements, rule 10).

## Premise check (KH-CS3, 8 Oct 2026)

- **(a) the folder's own mentions: found, none a decipherment of f.143.** Tomokiyo henryiv2.htm (on disk,
  `sources/cryptiana/web/henryiv2.htm`) lists "(fol.143) Henry IV to Duke of Nivernois, Mante, 22 December 1593 /
  Interlined deciphering." under BnF fr.3988. The same page lists "(fol.143) Henry IV to Duke of Nivernois, Dieppe,
  26 November 1593 / Interlined deciphering." under fr.3987, so the two f.143 entries may have been conflated.
  Tomokiyo's note was answered on the image. c304 is stamped "143" and headed "24 de Dec 1593". Its clear opening
  ("Mon Cousin, Il y a aujourd'huy quinze jours ...", about 10 lines) is followed by about 30 cipher lines. This worker
  cut strip crops with `python3 tools/iiif_lines.py --ark btv1b9060634t --canvas 304 --region 560,1650,3460,3700
  --out <scratch>/crops304 --debug --lines-per-crop 2` (39 lines, 20 bands x 2 segments; crops in scratch, not
  committed). Two contrast-raised strips (L03_s1, L14_s2) were viewed at native resolution. The interline space holds
  only ascenders and descenders, with no pale or cursive gloss. This agrees with KH1-F (c304-307 unglossed). Tomokiyo's
  "Interlined deciphering" does not describe this leaf as the image shows it.
- **(b) other solvers' working files: not found.** Bourdeau has key60.txt and decode60.py and ran them on fr.3986
  f.146v/f.157v, not on f.143. Aymeloglu has nothing for this leaf. In this repo, keyhunt_f143 passes exist, but no
  decode was run (KH1-F's atlas gate failed; KHF-4 NON-TEST).
- **(c) physical neighbours: not found (decipherment); two glossed siblings ruled out as duplicates.** KH1-F viewed
  302-303, 309 and 310 (no decipherment). SA-G says 308 is the closing cipher page with the "Henry" signature. This
  worker confirmed the estimated canvases by eye:
  - c210 = f.99, "Dupp^ta 22 de Dec 1593", Revol, opening "Monseigneur", with interlinear gloss;
  - c254 = f.119, "Dupp^ta 23 de Dec 1593", opening "Mon Cousin, J'ay eu ...", glossed;
  - c216 = f.102, glossed continuation;
  - c256 = f.120, a blank or endorsement leaf.

  f.143 has a different clear opening, no "Duplicata" mark and a different date, so it duplicates neither glossed
  letter (compared on clear opening lines only, one view).
- **(d) recipient's side: unreachable.** Gomberville ii was read and the letter is absent. The office-side edition
  (Revol 2004, above) could not be opened. This is the one premise gap and the reason for `blocked`.

## Intake gate

`python3 tools/intake_gate_check.py fr3988-henri4-nevers-1593` (KH-CS3, 8 Oct 2026):
```
fr3988-henri4-nevers-1593: blocked (line 1) -- already terminal, nothing to gate
exit 0
```
Exit 0 here means `blocked` is a terminal verdict for the gate, not a licence for deep work. Brief note for the
orchestrator: the follow-up F3988-DT is conditioned on this gate. The verdict word is `blocked`, so it should wait
until the Revol edition is checked (While waiting, below).

## While waiting

Re-run the HTRC Extracted Features word-count test on mdp.39015060819482 once data.htrc.illinois.edu answers
(no owner or key needed): look for pages carrying "Nevers" with "décembre" and "1593", or "Mante(s)" with "chiffre".
A page that carries them is a probable entry for this letter. A queue row can then ask the owner's local runner
for a HathiTrust search-only query of "Nevers" "décembre 1593" in that volume.

## Web and blog check (KH-CS3, 8 Oct 2026)

Plain web searches (WebSearch, 8 Oct 2026):
1. `Henri IV duc de Nevers Mantes 22 décembre 1593 lettre chiffre`: hits were Desenclos and Lasry 2024 (the 1592 digit
   letter, fr.3620 f.70-71; dspace.ut.ee), an SHPF inventory (Mantes 28 Apr 1593 to Pisany), arcsi.fr. Nothing on this letter.
2. `"fr. 3988" BnF chiffre Nevers`: BnF catalogue and CCFr Nevers municipal-library records, unrelated.
3. `Henry IV Nevers cipher no.60 December 1593 deciphered Tomokiyo cryptiana`: Desenclos and Lasry 2024; HistoCrypt
   paper (De Thou collection 1588-1594); Cipherbrain 14 Jun 2020 "A king's encrypted letter on Satoshi Tomokiyo's
   list". Opened with its 14 comments: it is about Charles I 1648, with no Henri IV, fr.3988 or Dec 1593 mention.
4. `"L'Europe d'Henri IV" Revol correspondance diplomatique 1588-1593 sources BnF Nevers` (the descriptive search):
   a dealer listing (livre-rare-book.com) and Wikipedia's Louis de Revol. Not openable.

Blog site searches: `site:cryptiana.blogspot.com Nevers 1593 Henri IV` and `site:ciphermysteries.com Nevers Henri IV
cipher 1593` returned no page from either site. Tomokiyo's own pages were read on disk (henryiv2.htm, league.htm).
The Cipherbrain hit above was opened with its comments.
No decipherment or plaintext of fr.3988 f.143 found in any comment thread.

Requests (this worker, fr.3988 part): gallica.bnf.fr IIIF about 8 (c304, c216, c256 views; the iiif_lines region
of c304; c210; c254, one connection reset and one retry; the c304 top) and ContentSearch 9; archive.org 17
(advancedsearch 5, metadata 6, djvu text 6); googleapis 4; api.openalex.org 2; openlibrary.org 2;
catalog.hathitrust.org 1; data.htrc.illinois.edu 2 (both HTTP 500); search.openedition.org 2; github.com 2 clones.
Report what was found and where it was not found; no novelty classification here (rule 10).
