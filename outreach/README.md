# Outreach: standing rules (26 Sept 2026)

1. Every draft states plainly, in its first paragraph, who is responsible and how the work is divided: one person
   directs the project and sends every message; the reading, the searches of the editions and the audits are done by
   AI agents (Claude models) working in this open repository, every step logged. An editor of the WVO asked for this
   in so many words on 26 Sept 2026 (outreach/huygens-nassau-saxony.md, Reply, item 5). The first Huygens email did
   not say it; do not repeat that.
1a. **Voice, not just disclosure (26 Sept 2026).** Write every sentence after the disclosure in the voice of
   who actually did it: "I" for what the person decides, asks or sends (the request itself, the sign-off);
   "we" for what the agents did (searched, transcribed, compared, checked, ruled out) -- never smooth a "we"
   describing agent work into "I", and never let the whole letter read as a report addressed to the person
   rather than sent by them. Lesson of 26 Sept 2026: MAIL-PREP's first six drafts read like a report and were
   rewritten in first person by the parent, and the rewrite itself needed a second check (OUT-CHECK-V) because
   three drafts had smoothed an agent-authored "we" into "I". Write it this way the first time; a drafting
   worker unsure which voice a sentence takes defaults to "we" and lets gate 7 correct it.
2. A reading that rests on a recovered key (no key source) is presented as a proposed reading, with the share of
   uncertain signs stated, never as a text (same reply, item 4).
3. Unseen witnesses (minutes, drafts, later copies the database lists) are named in every summary of a result, with
   the sentence that they may carry the text in clear or a prior decipherment (same reply, items 1-2).
4. Dates and sequences quoted from an edition are checked against the edition's own item, not paraphrased from the
   audit (item 3: "within days" for Kluckhohn nr. 148 was wrong by six weeks).
5. The person sends; the draft's status line records sent and reply dates; CONTRIBUTIONS.md carries the row.
6. Email drafts are written unwrapped: one paragraph per line, blank line between paragraphs, no hard line breaks
   inside a paragraph, and the metadata header (status/to/subject) above a blank line. Hard-wrapped Markdown pastes
   into a mail client as broken lines (26 Sept 2026).
7. A draft in a language other than English carries, in the email itself, a separator line and the full English
   version beneath it, so the person can review what he signs and the recipient can read either. The mailbox
   draft is signed the way the person signs his own sent mail (his name and the project name), supplied from the
   mailbox, never written into this repository (rule 9). Owner's ask, 26 Sept 2026.
8. Prior contact first (owner's rule, 26 Sept 2026). Before drafting to any person or institution, the drafter
   searches the project mailbox (Gmail: to:/from: the address and the institution's domain, all folders) and
   CONTRIBUTIONS.md (Recipient column) for earlier correspondence. If any exists, the draft is a reply in that
   thread (the mailbox draft carries replyToMessageId of the last message), opens by referring to the earlier
   exchange in one sentence, and does not repeat what that thread already said; a cold email to a known
   correspondent is a defect. The md header records `prior_contact:` with the thread id and date, or `none`
   (searched <date>). The pre-send fact check verifies the thread choice. Earlier mail the person sent from his
   own account (Huygens, Tomokiyo) is known only from CONTRIBUTIONS.md: a reply to those goes from his account
   in his thread, not from the mailbox.


## Project mailbox (26 Sept 2026)

The owner created cipherlab.research@gmail.com and connected it to the parent through the Gmail connector on both accounts. The parent places each ready draft in the mailbox as a Gmail draft (from `outreach/mailbox/<slug>.json`, prepared by a worker with the recipient address verified on the institution's own page that day and the CONTRIBUTIONS.md row written first); the owner reviews and presses send, so the 23 Sept 2026 directive (emails stay the person's) is unchanged. The sign-off is substituted in the mailbox only; the repository never carries the owner's name (rule 9). Replies are read by the parent at check-ins and recorded in the draft's file and CONTRIBUTIONS.md before anyone answers; the parent that owns the draft's target answers, the other only routes.

Gate 7 (26 Sept 2026): no mailbox draft is sent until a separate checking session has written a `checked:` line in the draft's header (CLAUDE.md Outreach gate 7); the parent replaces the Gmail draft with the checked text before telling the owner it is ready.

**Send log (26 Sept 2026, RETRO-2026-09-26j.md item 4).** The moment a send is confirmed -- whichever way it happened -- it is recorded in this exact shape, so a target is never recorded as sent twice in two different phrasings, and `tools/desk_check.py`'s (f) SENT MISMATCH check can tell a real send from a stale draft:
- the draft's `status:` line becomes `sent <UTC timestamp> by the person from the project mailbox (<how the send was confirmed>); reply pending`, keeping the prior value after a `Was:`. `<how the send was confirmed>` is either "Gmail Sent, read by parent `<session>` `<UTC timestamp>`" (a parent noticed the message in the mailbox's Sent folder -- armstrong-madison-editors.md is the worked example) or "SEND-QUEUE row `<id>`, receipt `<target>/outreach-receipts/<id>-<UTC date>.md`" (the owner's send-queue runner, `tools/send_queue_runner_prompt.md`);
- CONTRIBUTIONS.md's row for the same slug gets `sent by the person <UTC timestamp> from the project mailbox (gate 7 checked <the checked: line's timestamp(s)>; <same parenthetical as above>); reply pending` in its status cell;
- the ASKS.md row it answers is marked `sent, awaiting reply`.

Either parent may see the confirmation first (both accounts share the one Gmail connector, and either may land a `[SENT-<id>]` PR); whichever one does writes all three in this shape rather than guessing at the other's wording. A `sent` status with no matching CONTRIBUTIONS.md row, or a `mailbox-draft`/stale-conditional header after the send already landed, is what `desk_check.py` (f) flags at every check-in.

## Owner-side rule (owner's directive, 26 Sept 2026, OPTIMIZATION-2026-09-26.md (a))

The owner does nothing that requires reading this repository. A draft is not `ready` until it is self-contained:
the recipient (or the Gmail-draft mailbox slug it already sits in), the subject, and the sign-off line to fill in
are all in the draft's own header or the Gmail draft itself, not "see the target's REQUEST.md" as the only
instruction. If telling the owner to act needs him to open a NOTES.md or AUDIT.md file first, the ask is wrong: the
worker preparing the draft copies the needed fact into the draft instead of pointing at the repository for it. This
is `.claude/briefs/parent.md` duty 3b, restated here because outreach drafts are the other half of the owner's desk
(ASKS.md rows are the other half; `tools/desk_check.py --cap 5`).
