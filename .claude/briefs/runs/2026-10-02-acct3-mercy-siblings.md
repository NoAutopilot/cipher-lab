# MERCY-SIB (2 Oct 2026, written by account 3; runs on account 2): look for other cipher pieces of Mercy's 1648 mission

Model: Fable while it answers, else Opus 5.5. Cap USD 6, box 60 min. Search and catalogue job only: no decoding beyond step 5.

Why: our Mercy key (ciphers/espagnol142-mercy-1648/key.tsv; values 2-34 single letters + the Saint-Ibal box sign) is a small
mission key; key_crossmatch found no other ciphertext on disk it fits. Other cipher pieces of the same 1648 mission (Archduke
Leopold Wilhelm's secretariat <-> the abbé de Mercy; Brandenburg, Cleves, Konrad von Burgsdorff) are where it would open.
1. `python3 tools/room.py --start`; claim in ROOM.md.
2. AGR Brussels (Secrétairerie d'État et de Guerre): the SEE register t. LXIV f.16 (15 Apr 1648 instruction to Mercy, ASKS 60)
   and the "chiffres 1647-98" register named in KEY-OFFICES.tsv row for this key. Read the AGATHA/search.arch.be catalogue
   records (quote their availability flag and URL); note any item that is a Mercy dispatch or a key sheet of 1647-49.
3. Brandenburg side: "Urkunden und Actenstücke zur Geschichte des Kurfürsten Friedrich Wilhelm von Brandenburg" (archive.org
   full text; be-api fts for lending-only volumes) for Mercy, Merci, Mercy's mission, Burgsdorff with 1648; also GStA PK finding
   aids if reachable. Record every hit with volume and page.
4. AGS Estado (Flandes) 1648 legajos: catalogue only (PARES is dead from the cloud -- use the aaymeloglu cached PARES sweep if it
   covers it, cite it, do not copy code).
5. For any cipher piece found WITH an image online: fetch it once, transcribe a sample line, and apply our key.tsv with
   `tools/decode_key.py`-style substitution plus a shuffled-key control (200 shuffles). Report both numbers; no reading claims.
6. Write ciphers/espagnol142-mercy-1648/siblings_1648_hunt.md (search log per host, hits, what is reachable); a ROOM flag for any
   cipher piece found; append one "Remaining gaps" update line (siblings step) to NOTES.md's finish-or-blocker section and run
   `python3 tools/gaps_check.py espagnol142-mercy-1648`. Commit by explicit path; done line with request counts per host.
Rule 10 wording; never name the owner; never print credentials.
