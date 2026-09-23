found-solved

# Charles I (Oxford) to Prince Rupert, 29 April 1645 — BL Add MS 18983 f.14, DECODE R4921

- Source: QUEUE.md rank 11 (score 34), scored 20 September 2026; catalogued from the DECODE record page
  (de-crypt.org/decrypt-web/RecordsView/4921) and Bourdeau's `cyphersolver` repository harvest.

## Check-solved sweep (23 September 2026)

1. **Web search.** "Charles I" "Prince Rupert" 1645 cipher decrypted DECODE R4921 BL Add MS 18983 — no page
   names this exact record as solved. "Charles I Rupert Add MS 18983 f.14 cipher Cryptiana Tomokiyo" — surfaces
   Tomokiyo's Cryptiana `charlesi.htm` page and the two solver repositories but no explicit claim for this
   record. found=false from open web search alone.

2. **Print.** Warburton, *Memoirs of Prince Rupert* vol. 3 (1849, archive.org `memoirsofprincer03warbuoft`) and
   CSP Domestic 1644-45 (archive.org `sim_great-britain-public-record...1644-1645`) were already grepped for
   late-April 1645 material in the 20 September 2026 search-print pass recorded in QUEUE.md: no letter dated 28
   or 29 April under the King's own signature in Warburton, and CSP Domestic calendars TNA SP, not this BL Add
   MS 18983 transcript stream. Re-confirmed, not re-run, this sweep. Google Books: not available in this
   environment (no key set here; per CLAUDE.md Access playbook item 3, GOOGLE_BOOKS_KEY is unset in this
   account's environment). HathiTrust Bibliographic API: not queried this sweep (superseded by finding #5 below).
   found=false in print.

3. **Community lists.** `sources/cryptiana/web/charlesi.htm` (grepped locally, never edited) documents the whole
   family of Charles I / Rupert / Digby / Ormonde / Nicholas ciphers of 1644-45 in detail (the June 1644
   King-Rupert cipher reused by Digby to Rupert 27 April 1645; the Nicholas-Rupert cipher of July 1645) but does
   **not** mention BL Add MS 18983 f.14 or a decipherment of the 29 April letter specifically. Web search
   restricted to scienceblogs.de/cipherbrain.de for "Prince Rupert cipher solved Cobham Harley 287 Bowes
   Walsingham" returned no matching post; a full fetch of a candidate 2015 Cipherbrain post
   ("Eine ungelöste Verschlüsselung aus dem Jahr 1645", scienceblogs.de/klausis-krypto-kolumne/2015/03/20/...)
   was attempted and blocked by this environment's egress policy (`EGRESS_BLOCKED domain=scienceblogs.de`), so
   its content could not be read; its title alone ("An unsolved encryption from 1645") is consistent with, but
   does not confirm, this item. found=false confirmed in Cryptiana; unread/unreachable on Cipherbrain.

4. **DECODE.** `curl -A "Mozilla/5.0" https://de-crypt.org/decrypt-web/RecordsView/R4921` — connection refused
   at the egress proxy (`CONNECT tunnel failed, response 403`, HTTP code reported as 000; proxy status:
   `connect_rejected — organization policy`). de-crypt.org is not reachable at all from this account's
   environment, not merely Cloudflare-gated; no login was attempted (DECODE_USER/DECODE_PASS are also unset in
   this account's environment, per the 23 Sept 2026 15:20 orchestrator note in ROOM.md). Source: **unreachable**.
   (Aymeloglu's `catalogue/decode-ranked.md`, scraped separately, records R4921's own DECODE metadata as "key
   attached; inline cleartext", consistent with finding #5 but not itself a reading.)

5. **Bourdeau (`github.com/dbourdeau/cyphersolver`, shallow clone 23 Sept 2026, MIT code / CC BY 4.0 text).**
   **found=true.** `cyphersolver/rupert1645/` (catalogue item 71) reads this exact record: "read 21 Sept 2026
   with Lasry's King-Queen key SP106-5 (R929); the artillery train and Rupert's march"
   (`CATALOGUE.md` line 300; write-up published at
   https://dbourdeau.github.io/cyphersolver/rupert1645.html). `rupert1645/profile.json` gives `fraction_read:
   0.95` (305 cipher groups, ~15 unread — mostly code words at phrase ends read only from context) and
   `outcome.class: "read"`. Method: George Lasry's previously reconstructed homophonic + nomenclator key for
   the Charles I / Henrietta Maria "King-Queen" cipher family (DECODE R929, TNA SP106-5, originally built for a
   different letter) applied unchanged to R4921's 305 groups, after two sibling keys (the Duke of Richmond
   cipher of R4922, and the Digby-Walsingham key R8724) were tried and ruled out. `rupert1645/NOTES.md` records
   that no printed decipherment of this specific letter was found (Warburton 1849, Bromley 1787, web) — i.e.
   Bourdeau's own project ran the same search-before-solving step this sweep repeats, with the same negative
   result, before applying the key. Reading (from `rupert1645/NOTES.md`): the King, hemmed in at Oxford, cannot
   move his artillery train to Rupert without horses and a convoy, has sent for Goring, and asks Rupert to march
   to fetch it — consistent with Digby's letters of 27 and 30 April 1645 on the same subject and with Rupert's
   move on Oxford in May.

6. **Aymeloglu (`github.com/aaymeloglu/unsolved-ciphers`, shallow clone 23 Sept 2026; no licence, cite only, no
   code copied).** No target folder for this item; `catalogue/decode-ranked.md` line 45 lists DECODE record 4921
   in its scraped ranking table ("key attached; inline cleartext") — a catalogue description of the DECODE
   record's own metadata, not a decipherment claim. found=false (no reading in this repository).

## Verdict

**found-solved.** Bourdeau's project (Claude Fable 5.1 / Opus 5 in Claude Code, per that repository's own
`conditions.human_role` field) read this letter on 21 September 2026 by applying George Lasry's previously
published DECODE key for the Charles I / Henrietta Maria cipher family (R929, TNA SP106-5) — not a new
cryptanalytic break of R4921 itself, but a real, working key-application reading, publicly committed to
`github.com/dbourdeau/cyphersolver/rupert1645/` (MIT code, CC BY 4.0 text) with a write-up at
https://dbourdeau.github.io/cyphersolver/rupert1645.html. About 95% of the 305 cipher groups are read; roughly
15 code-word groups remain open or are read only from surrounding sense. No printed decipherment of this
specific letter exists in Warburton (1849), Bromley (1787) or CSP Domestic 1644-45 — this reading is
cryptanalytic/key-recovery, not a rediscovery of a printed source. Per rule 10, novelty (whether this counts as
a first decipherment) is a verifier's question, not stated here; this NOTES.md records only that the item is no
longer an open target for this project. QUEUE.md row 11 moved to Dropped (see below); no Stage 2 line applies.
