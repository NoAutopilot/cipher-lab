# Copy request: British Library, Add MS 72438 (Weckherlin cipher-keys and intercepted royalist correspondence)

Take the exact contact route from bl.uk ("Manuscripts" > "Requesting items" / "Copying at the British Library")
rather than from here. The BL's online systems have been unreliable since the 2023 cyber attack; expect a
slower, quote-based process. See `NOTES.md` for the full catalogue findings behind this list.

## The order, in priority order

1. **f.11** — the folio already identified (19 Sept 2026 scout) as the likely contemporary decipher of f.10's
   letter, or at minimum more of Digby key no. 129. This is the first thing to request; it directly finishes
   f.10's partial reading.
2. **ff.100-101, 102-103, 105-106, 108-109** — catalogued as further royalist cipher-key items in this volume
   ("unidentified royalist keys" at 105-106 and 108-109; King & Queen at 100-101; Digby/Walsingham at 102-103).
   None of these have been matched to a name or tried against f.9 or f.10 yet. Any could be the rest of key
   no. 129, or the smaller key f.9 uses (where 226 = London). Ask for all of them in one order alongside f.11.
3. **f.104** — "Royalist intercepted letter almost wholly in undecoded cipher, n.d." **Do not request this yet.**
   DECODE record 8725 for this folio is marked Status: Decrypted (unlike f.9/f.10, both "Non-decrypted") — see
   `NOTES.md`'s "Scout addition" section. A DECODE login is needed to read record 8725 and settle this before
   ordering. **Still blocked, 20 Sept 2026:** the login flow now works (`CLAUDE.md` Access playbook item 3,
   `tools/decode_fetch.sh`), but the `DECODE_USER`/`DECODE_PASS` credentials set in this environment were
   rejected by the server ("Incorrect user name or password") — see NOTES.md's "DECODE record 8725, read
   20 Sept 2026" section. Getting credentials the server accepts is the person's action now, not a technical
   one; do not keep retrying the same pair (lockout risk). If it turns out to be a stale/incorrect status flag
   and f.104 is genuinely unread, add it to this order; if DECODE already has a plaintext or decipherer on
   file, there is nothing to solve.

## Also worth checking in print, free, before ordering

- Bodleian Tanner MSS 59-60 and TNA SP 16/514 for a contemporary decipher of f.10 (already noted in QUEUE.md,
  not yet done).
- Evelyn 1857 vol. 4 (already the source for ~45 values of key 129) for any further royalist cipher material
  from this circle that might cover the ff.100-109 keys.

## Log

| Date | Action | Result |
|---|---|---|
| 20 Sept 2026 | Catalogue checked at searcharchives.bl.uk (catalog/040-001967027) for the whole volume and ff.100-109; DECODE record 8725 checked by raw HTML for f.104 | Volume identified as Weckherlin's cipher-keys and intercepted royalist correspondence, 1625-1647, images unavailable. f.104 confirmed catalogued "almost wholly in undecoded cipher, n.d." but DECODE marks it Status: Decrypted — resolve before ordering (see above). ff.100-109 confirmed as further uninvestigated key items. |
| | f.11 + ff.100-109 request sent | |
| 20 Sept 2026 | DECODE login check on record 8725 (`tools/decode_fetch.sh 8725 /tmp/decode/8725`) | Login flow confirmed working technically, but `DECODE_USER`/`DECODE_PASS` rejected ("Incorrect user name or password"); record 8725 not fetched. Waiting on the person for credentials the server accepts. |
| | Images/answer received | |
