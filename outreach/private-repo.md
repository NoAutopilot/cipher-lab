status: done 24 Sept 2026 (cipher-lab-private created and attached; grants/ and mail/ pushed at 16:07 UTC)
subject: Create one private repository for grants and correspondence (one click), then tell me
to: github.com/new (your account; no email)

You asked (13:41 and 13:52 UTC) that grants material and the email correspondence stay out of this public repository. A cloud session cannot create repositories (the GitHub app returns 403), so this is yours:

1. github.com/new: name `cipher-lab-private`, Private, tick "Add a README". Create.
2. github.com/apps/claude/installations/select_target: add `cipher-lab-private` to the Claude app's repository access and save.
3. Tell me "private repo ready".

What goes there: `grants/` (the scout's table, application drafts, plan, your fill-in checklists) and `mail/` (outbox drafts with recipient addresses, sent copies, filed replies, the address book). What stays here: CONTRIBUTIONS.md rows by date, institution and class with no addresses; a one-line stub per draft in outreach/ with `status: ready` so the card still shows what is waiting for your tick, and the tick still counts as the send. Even in the private repository, your own personal fields stay placeholders until you submit an application, and mail credentials never go in either repository (environment variables only).

Update, 24 Sept 2026 14:20 UTC: the grants scout (session 019HSXApEw1FQvwqDTcnuSUN) and the applications worker
(session 014o1Q2GRr539B86vvKbgrnP) pushed `grants/` (table, plan, seven drafts) and six `outreach/grant-*.md` stubs to
this public repository at 058b9c6 and after, against the directive above. The parent removed them from the tree in the
commit carrying this note; no name, address or email was in them (checked by grep before removal: only the repository
URL). They remain in this repository's history until the owner's sanctioned purge (`tools/purge_history.sh`) runs;
add `grants/` and `outreach/grant-*.md` to that purge's path list. The content is in the two private artifacts
"cipher-lab grants scout table" and "cipher-lab grants applications" and will be committed to `cipher-lab-private`
once it exists.
