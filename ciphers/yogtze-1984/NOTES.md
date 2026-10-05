open
Staatsanwaltschaft Hagen statement of 3 Apr 2025 as reported by zdfheute ("Wende im Yogtze-Fall nach 41 Jahren", 4 Apr 2025, read by GF4-BATCH17 on 3 Oct 2026): death closed as a self-caused traffic accident; prosecutor Gerhard Pauli on the letters, "In keiner Sprache der Welt ergebe dies einen Sinn", and "Der berühmte Zettel zählt nicht zu den Asservaten, sondern ist verschwunden" -- the note was never deciphered and the slip is lost; Cipherbrain's three YOGTZE posts (2015, 104-comment thread; 2017 Top 50 no. 21; 2021) read with their threads, no accepted reading.
Previous line 1 remainder (kept): below any unicity (N=6) per UNSOLVED-SURVEY.md row 26 -- this is a lexical/crib-search problem, not a cryptanalytic one.
Previous line 2 (25 Sept 2026, kept): Read in full: Cipherbrain post 21 (sources/schmeh/posts/21-yogtze.txt, fetched 25 Sept 2026 by bSPEC2, re-read in full 25 Sept 2026) and its 8-comment thread (13 Sept 2017 - 7 Oct 2021), none of which claims a solution -- all speculation (a possibly-non-original slip photographed for the Allmystery forum; an upside-down/mirrored reading; a Russian-reversal pun; a link to a German Wikipedia talk page). Both solver repositories grepped for "yogtze" (shallow clone, grep, delete, 25 Sept 2026): aaymeloglu/unsolved-ciphers has no mention; dbourdeau/cyphersolver's own status tracker (top50/NOTES.md line 32, top50/TARGETS.md line 207) reads: "Closed as a case, April 2025. Hagen police and prosecutors closed the death as a single-vehicle accident; investigators doubt the slip of paper ever existed. Seven characters, never a cipher" -- no source citation is given in that file for the April 2025 claim, so this is reported as a repo finding, not confirmed independently this pass. This does not constitute a decipherment of the word (nothing in that note or elsewhere proposes a reading of "YOG'TZE"); it is evidence the underlying death case is closed and that the existence of the paper itself is doubted by investigators, which bears on the target's value, not its solved/unsolved status for rule 5 purposes. One OpenAlex query ("YOG'TZE solved decrypted", 25 Sept 2026): 0 hits. One Semantic Scholar query (same terms, 25 Sept 2026): 363 results, top 5 read, none relevant (generic cryptography/encryption papers, no mention of the case).

Status word: open (unchanged from spec). flag for LANE B3 orchestrator: the dbourdeau "case closed April 2025 / paper's existence doubted" note is new information not in specs/yogtze-1984.json when bSPEC2 wrote it; worth a citation check (a German-language news search for "Yogtze Hagen 2025") before the survey row or spec's status line repeats it as fact.

## Intake gate

```
$ python3 tools/intake_gate_check.py yogtze-1984
yogtze-1984: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit: 0
```


## Web and blog check (GF4-BATCH17 (account-4), 3 Oct 2026)

Plain web searches (WebSearch): (1) `Yogtze Günther Stoll Zettel 2025 Fall abgeschlossen` -- de/en Wikipedia "YOGTZE-Fall", ak-kurier, ms-aktuell "Vom rätselhaften Tod 1984 bis zur Aufklärung 2025", podcast "Mord auf Ex" no. 277 "Gelöst: Der YOG'TZE-Fall", NamuWiki, True Crime Database: the *death* was closed by police and the Staatsanwaltschaft Hagen on 3 Apr 2025 as a self-caused accident; the letters were declared irrelevant to the cause of death, not explained; (2) `YOGTZE case solved meaning note Günther Stoll` -- en Wikipedia ("The meaning of YOG'TZE remains unknown"; closed as accidental Apr 2025), Medium, historicmysteries, Grunge, themunicheye; none gives a reading of the letters; (3) `"YOGTZE" Aktenzeichen XY Zettel existiert nicht Polizei Hagen` -- t-online, zdfheute (4 Apr 2025, read in full via fetch: prosecutor Gerhard Pauli, "In keiner Sprache der Welt ergebe dies einen Sinn"; "Der berühmte Zettel zählt nicht zu den Asservaten, sondern ist verschwunden" -- the widow threw it away), regionalheute, rlptoday, wikixy (XY broadcast 12 Apr 1985); police spokesman Tino Schäfer (Hagen) quoted; whether the slip ever existed is questioned. This confirms the dbourdeau note bSPEC2 flagged ("case closed April 2025 / paper's existence doubted") from primary news reporting -- it closes the death case, not the letters.
Blog site searches: Cipherbrain (scienceblogs.de `?s=Yogtze`): "YOGTZE-Fall: So könnte es gewesen sein" (20 Sept 2015; Schmeh's accident hypothesis, which the 2025 finding broadly matches; thread read, 76 numbered comments as served, 20 Sept 2015 - 31 Dec 2017 -- readings proposed: coordinates 25.157N 20.265E, upside-down "321606", ZYGOTE, a yoghurt brand; none accepted) and "Ein Krypto-Klassiker: Der YOG'TZE-Fall" (6 Feb 2021; 5-6 comments to 11 Jun 2023: Dutch-plate doubt, upside-down "321,904"; none accepted; Schmeh: the paper is lost and the wife's memory of it uncertain), plus Top 50 no. 21 (on disk, 8 comments to 7 Oct 2021, re-read 25 Sept 2026); klausschmeh.net `?s=Yogtze` / `?s=YOGTZE`: no post on it (no 2026 solve announcement); Cryptiana blog `?q=Yogtze`: no posts; Cipher Mysteries `?s=Yogtze`: Nothing Found; Reddit r/codes (OAuth search `YOGTZE`): 0 hits.
Solver repos (fresh shallow clones 3 Oct 2026): dbourdeau/cyphersolver HEAD 841111b -- no "yogtze" in targets/ or TARGETS.md (the earlier note's top50 status line is in research/top50, not re-grepped as a hit this time); aaymeloglu/unsolved-ciphers HEAD d2800bb -- no mention. DECODE: no hit in the on-disk listings; outside scope (a 1984 note).
Requests: scienceblogs.de 1 curl + 2 WebFetch, klausschmeh.net 2, cryptiana.blogspot.com 1, ciphermysteries.com 1, zdfheute.de 1 WebFetch, oauth.reddit.com shared with koehler search call, github.com shared clones; all >=1.5 s apart.

## Premise check (GF4-BATCH17 (account-4), 3 Oct 2026)

(a) Folder's own mentions: found, not a decipherment -- the earlier flag ("case closed April 2025 / paper's existence doubted") is confirmed by the prosecutor's statement; no folder file mentions any decipherment.
(b) Other solvers' working files: not found -- Bourdeau has a list/status line only; Aymeloglu nothing; no working files anywhere.
(c) Physical neighbours: unreachable by nature -- the slip is not in the evidence and is lost (Staatsanwaltschaft Hagen, 2025); the six letters survive only as the widow's recollection reported about six months after the event. No image exists to view.
(d) Investigator side: found -- Staatsanwaltschaft Hagen / Polizei Hagen 2025 review (new reports, reconstruction): the letters are "in no language" meaningful and irrelevant to the death; no decipherment by the authorities.
Result: no decipherment exists anywhere; the "ciphertext" has no physical witness. Status word stays open per this job's rule (no accepted decipherment); for the parent's decision: the text is a hearsay six-letter string with no original (CLAUDE.md rule 2), which fits `blocked` (no witness to the ciphertext) better than `open`, but the change is the parent's to make.

## Verdict (GF4-BATCH17 (account-4), 3 Oct 2026)

**open (unchanged), flagged.** Not deciphered in: the Hagen prosecutor's 2025 closing statement (zdfheute 4 Apr 2025), Wikipedia (de/en), Cipherbrain's three posts and their threads, klausschmeh.net, Cryptiana, Cipher Mysteries, Reddit r/codes, both solver repositories, searched 3 Oct 2026. Claimed-but-unaccepted readings (comment threads 2015-2023: coordinates, ZYGOTE, inverted digits) recorded as claimed. The 1984 death is solved (accident, Apr 2025); the letters are not, and authorities consider them meaningless.

## While waiting (GF4-BATCH17, 3 Oct 2026)

Nothing to wait on and nothing to transcribe (the slip is lost). The one zero-dependency step: a lexical crib search of the six letters against German/Dutch licence-plate prefixes and food-technology abbreviations of 1984, logged as a search (UNSOLVED-SURVEY row 26), or the parent re-labels the target per the premise note above.

## Intake gate (GF4-BATCH17, 3 Oct 2026)

$ python3 tools/intake_gate_check.py yogtze-1984
yogtze-1984: open (line 1) -- edition/page or full-text-search citation found within 6 lines
exit 0

$ python3 tools/next_steps.py --wait-only | grep yogtze-1984
(no line)

## Next step (NO-CRACKS, 5 Oct 2026)

next: a lexical crib search of the six letters against 1984 German/Dutch licence-plate prefixes and food-technology abbreviations, logged as a search (UNSOLVED-SURVEY row 26), ~$0.5; or the parent re-labels the target per the premise note. Who acts: agent. Source: this file's "## While waiting (GF4-BATCH17)"; written by NO-CRACKS (account 3) because tools/next_steps.py found no next-step line in this file.
