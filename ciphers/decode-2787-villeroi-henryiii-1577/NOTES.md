# decode-2787-villeroi-henryiii-1577

Status: found-solved

## What this is

DECODE R2787: Nicolas de Neufville, Sieur de Villeroi, to Henry III of France, private collection, 1577-1577,
French (Partially decrypted status, 2 images, one attached document tagged `[key]`, titled "Preliminary
Assignment"). QUEUE.md row DC3 ("DECODE non-decrypted records with images", LANE N diff of 24 Sept 2026),
flagged as a recovery lead because of that attached key document. Checked as part of LANE N check-solved
batch DC1 (`.claude/briefs/runs/2026-09-24-lane-n-csDC1.md`).

## Check-solved sweep, 24 September 2026

1. **Tomokiyo.** `sources/cryptiana/web/henryiii.htm` carries a dedicated section "Nicolas de Neufville, Sieur
   de Villeroi (1577)" describing exactly this item: "A letter in cipher from Villeroi to Henry III of France
   was sold at an auction. It is wholly in cipher except for the complimentary ending: 'Sire ie prie dieu
   conserver vre mté en parfaicte santé / De Bergerac ce viiie jour de sepbre 1577' and the signature ... in
   Villeroi's hand." This matches DECODE R2787's date range (1577-1577), sender (Nicolas de Neufville, Seigneur
   de Villeroi), holder (private collection) and language (French) exactly. The very next sentence: "This was
   solved by George Lasry in 2022 (see another article)." with a linked image `GL/GL_Villeroy.png`.
2. **Tomokiyo's GL.htm** (also in `sources/cryptiana/web/`) repeats the same description under its own
   heading "Villeroi to Henry III (1577)" and adds three further images of the decipherment itself:
   `GL/GL_Villeroy_decipher.png`, `GL/GL_Villeroy_decipher2.png`, `GL/GL_Villeroy_decipher3.png`.
3. **Solver repos.** Fresh shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers: neither
   repo's catalogue files key on DECODE id 2787 (id 2788, a different item — Catherine de Médicis to Philibert
   du Croc, private collection — is QUEUE.md's DC20, not this target, and is unrelated). The solve is credited
   to Lasry directly via Tomokiyo, not to either repository's own work.
4. **Web.** Tomokiyo's own citation (traces-ecrites.com auction listing) matches DECODE's holder field
   "private?" — the same physical object.
5. **DECODE.** R2787's own status "Partially decrypted" with an attached "[key] Preliminary Assignment"
   document (read by a prior LANE N worker this session, QUEUE.md DC3 row) is consistent with this: DECODE's
   own catalogue already has a start on this item, though its status field was never updated to "Decrypted"
   and its RecordsView page alone (without checking Tomokiyo) did not reveal that a full published solution
   already exists.
6. **Community lists.** Tomokiyo's own site is the community list of record for this correspondent
   (`henryiii.htm`); no separate forum thread was found or needed.

## Verdict

**Found-solved.** George Lasry solved this letter in 2022; Tomokiyo's site publishes the reading with three
decipherment images. Grade **F0** (README vocabulary): a specialist source any worker should check before
campaigning (Tomokiyo's henryiii.htm/GL.htm) already links this exact item — same sender, recipient, date and
the distinctive Bergerac complimentary close quoted above — to its decipherment. No contribution here beyond
correcting QUEUE.md's DC3 row, which proposed it as a "finish-existing-key" recovery lead without knowing the
key was already finished and published four years earlier.

Requests this pass: WebSearch 0 (resolved entirely from files already in the repo), github.com 0 (reused this
session's shared shallow clones, logged in ROOM.md). No fresh DECODE login (RecordsView was already read by
the prior LANE N worker, cited above). No promotion, no decoding beyond citing Tomokiyo's own published
images, no novelty wording (rule 10 — this is a check-solved verdict, not a verifier's N-class).
