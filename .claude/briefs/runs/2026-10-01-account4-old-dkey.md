# OLD-DKEY: oldenbarnevelt-brederode-1605 -- DECODE listing search for a Dutch key dated 1600-1610

Written 1 Oct 2026 23:5x UTC (clock read) by the account-4 parent (session_01SEzoee67SivPooFpTkxMme).
Role field for ROOM.md lines: `OLD-DKEY (account-4)`. Model: Fable 5.1 (Opus 5.5 if Fable fails). Cap: USD 3. Box:
30 minutes. Hosts: de-crypt.org listing only, through `tools/decode_list.py` (login-free; NO login attempt -- the
playbook reserves it), one request at a time, >= 1.5 s apart, at most 40 requests; stop on any 403/429/challenge.

## The job, in one line

The folder's named next step (NOTES.md "Local runner L12 recheck", 26 Sept 2026, which closed the Megyesi paper as a
lead but "does not rule out an individual" DECODE key): search the DECODE record listing by date and country for any
key record (type key/nomenclator) dated 1600-1610 whose origin or holder is Dutch / States General / Holland, and
report what exists, with record ids, so a later worker knows whether route A (a period key) has any candidate at all.

## Steps

1. `python3 tools/room.py --start`; last 30 ROOM.md lines; claim line.
2. Read NOTES.md items 5 and the L12 section; read `python3 tools/decode_list.py --help` and `sources/decode/NOTES.md`
   for the listing's fields and the local cache (if a full listing snapshot is already on disk under sources/decode/,
   use it and make zero requests -- say so).
3. Filter: type key, date 1595-1615 (a margin either side), country/origin Netherlands or any Dutch-named holder
   (Nationaal Archief, KHA, Koninklijke Bibliotheek, Museum ...), language nl/la/fr. Also search the free-text name
   field for Brederode, Oldenbarnevelt, Staten, Holland, Praag/Prague, Kaiser/Emperor. Write `decode_keys_1600s.tsv`
   (record id, name, date, holder, language, type, URL) into the folder, and one paragraph in a dated NOTES.md
   section "## OLD-DKEY (1 Oct 2026, account-4)": how many candidates, which look like States-General keys, and the one
   named next step (a LOCAL-QUEUE row for the owner's desk runner to open the record's images, since full-size
   images are account-blocked -- draft the row text in NOTES.md, do not file it yourself).
4. Commit by explicit path, rebase on origin/main, `python3 tools/restricted_guard.py --outgoing`, push to main. Done
   line with the candidate count and the request count. Stop.

Rule 10 wording only. The common tail of `.claude/briefs/README.md` applies in full.
