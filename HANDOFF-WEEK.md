# Week handoff, 21 to 28 September 2026

Ryan is away this week. This file says what he must do before he goes, what a teammate can carry alone, and
what simply waits. Read `ONBOARDING.md` first if you are new, then `CLAUDE.md`, then this.

## Ten minutes from Ryan before he goes

These four unblock other people. Everything else can wait a week; these cannot.

1. **Rotate two passwords and fix one username.** The DECODE (de-crypt.org) and archive.org passwords were
   printed into worker transcripts on 20 September and both logins are currently rejected anyway. Rotate
   both, set `IA_USER` to the archive.org account **email address** rather than a username, and update
   `DECODE_USER`, `DECODE_PASS`, `IA_USER`, `IA_PASS` in the environment. This is the highest-value ten
   minutes available: it unblocks four items at once (Boswell 1628, the Cecil correspondents, record 8725 for
   the 1646 folio, and key record R4930 for Randolph 1570).
2. **Send the Spink email, or accept that it lapses.** The sale is 23 September, so this is the only hard
   deadline in the project. One line: does lot 1184 include a pocket dictionary? Contact is on the lot page.
3. **Decide who may write to archives.** The copy requests in each target's `REQUEST.md` are drafted and
   ready. If a teammate may send them from their own address, say so in `ASKS.md` and note that replies will
   go to that address, not Ryan's. If not, all four archive asks wait for his return.
4. **Decide about the twenty dollars.** The Kansas order for Stair 1710 needs a card. Either place it before
   leaving (three business days, so it would arrive while he is away) or it waits.

## What a teammate can carry alone this week

In priority order. None of these needs Ryan, a credential or a payment.

1. **Randolph to Sussex, 1570, native-resolution transcription.** The biggest real piece of work available.
   Images are already in `ciphers/randolph-sussex-1569/images/`. The first pass confirmed the structure but
   not the glyphs, because the image tool downscales crops well below native. The job is twenty to thirty
   narrow crops, each kept under about 2500px wide so no downscaling happens, then a glyph-exact
   transcription, then frequency analysis. `NOTES.md` section "What a next solver needs" is the brief.
   Budget about forty dollars, use the strongest model for reconciliation and Sonnet for the passes.
2. **Two print checks that the Google Books key now makes possible.** Calendar of State Papers Foreign
   volume 22 for Cobham 1588 (QUEUE rank 13) and Calendar of State Papers Domestic 1644-45 for Charles I to
   Rupert, 29 April 1645 (rank 11). Remember `&country=US` on every Books API call. A few dollars each.
3. **Check-solved sweeps on unswept queue items.** Nothing in the queue below the top ten has had the blind
   six-source sweep. Run it on the next five before anyone proposes spending money on them. This is the check
   that has already caught four items printed in clear since the 1800s.
4. **A scout refresh.** The last harvest was 19 September and the re-score was 21 September. A fresh harvest
   would pick up anything published in the meantime.
5. **If Ryan rotated the passwords:** the DECODE work above, starting with record 8725, because it decides
   whether the 1646 folio is a target at all.

## What waits, and why

- **Hamilton 1650** and **Stepney 1702**: quotes from Edinburgh and Kew. Nothing to do but wait.
- **Eckert**: the Huntington curator's reply to the 20 September enquiry decides whether the corpus pass is
  worth running. Parked until then.
- **The 1646 royalist intercepts**: the British Library's manuscript viewer has been offline since the 2023
  cyber attack. Genuinely blocked.
- **Whitworth 1707**: Ryan's call on whether one unread clause is worth a Kew order. Not urgent.

## What a teammate may decide without asking

- Which of the jobs above to run, in what order, and how to brief them.
- Spending plan usage on workers, within the caps in `CLAUDE.md`'s Usage section.
- Promoting a queue item to the board, **provided** a check-solved sweep set it to stage 2 first.
- Correcting anything in the repository that is wrong, including things Ryan or an agent wrote.

## What a teammate may not decide alone

- Spending money. Every copy order, quote acceptance and subscription goes to Ryan.
- Any external claim of novelty. Rule 10 stands: only a verifier assigns a class, and nothing is called new,
  first or previously unread without one.
- Publishing anything outside the repository, or contacting an archive in Ryan's name.

## Where state lives

`STATUS.md` for the board in prose, `status.json` for the same thing as data, the published page for the
picture, `ROOM.md` for what agents are doing right now, `ASKS.md` for anything blocked on a human,
`LEDGER.md` for what each worker cost and whether it delivered. Claim work in `ROOM.md` before starting it.
