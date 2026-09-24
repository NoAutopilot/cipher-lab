status: ready
subject: Create one private repository for grants and correspondence (one click), then tell me
to: github.com/new (your account; no email)

You asked (13:41 and 13:52 UTC) that grants material and the email correspondence stay out of this public repository. A cloud session cannot create repositories (the GitHub app returns 403), so this is yours:

1. github.com/new: name `cipher-lab-private`, Private, tick "Add a README". Create.
2. github.com/apps/claude/installations/select_target: add `cipher-lab-private` to the Claude app's repository access and save.
3. Tell me "private repo ready".

What goes there: `grants/` (the scout's table, application drafts, plan, your fill-in checklists) and `mail/` (outbox drafts with recipient addresses, sent copies, filed replies, the address book). What stays here: CONTRIBUTIONS.md rows by date, institution and class with no addresses; a one-line stub per draft in outreach/ with `status: ready` so the card still shows what is waiting for your tick, and the tick still counts as the send. Even in the private repository, your own personal fields stay placeholders until you submit an application, and mail credentials never go in either repository (environment variables only).
