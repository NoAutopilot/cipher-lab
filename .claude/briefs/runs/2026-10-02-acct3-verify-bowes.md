# VERIFY-BOWES-584 (2 Oct 2026, written by account 3; runs on account 2): re-audit after NEXT-BOW (rule 10 propagation)

Model: Fable while it answers, else Opus 5.5. Cap USD 5, box 45 min. You are a verifier (CLAUDE.md "Verifier brief"), a session
separate from NEXT-BOW (session_01GGhhpUV2rrk233PjMRrtVc), and you do not protect its conclusions.

Claim under audit: NEXT-BOW (2 Oct 2026, ciphers/bowes-walsingham-1583 NOTES.md latest step, csp6_584_snippets.tsv,
align_ccxl.py) read Boyd's CSP Scotland vi (1910) no.584 pp.566-568, where a blank+asterisk stands for a cipher word of the Cotton
original, and placed F8 = Glencarne, F9 = his..Ruthen (now grade C, 9 tokens) and F10 = 223 as cipher digit signs, giving
97 of 100 tokens read (S 73, M 12, I 3, C 9). AUDIT.md section 10 says the p.566 asterisk words cannot be read; that is now
contradicted.
1. `python3 tools/room.py --start`; claim.
2. Re-derive: check each placement against Boyd's own text (Google Books API with country=US and the key, one request at a time,
   1.5 s apart, under 40 requests) and the order control NEXT-BOW reports (6 of 24, floor 0.042, weak); say whether the C grade
   holds for each of the 9 tokens or should be M. `python3 ciphers/bowes-walsingham-1583/check.py` must exit 0.
3. Update AUDIT.md: a dated section superseding section 10, the class unchanged unless the evidence moves it (state why), and the
   safe sentence with the new counts; propagate to any SECOND-OPINIONS-QUEUE.tsv row for this target and to CONTRIBUTIONS.md if
   its row quotes the old counts (rule 10, last paragraph). Do not message anyone.
4. `python3 tools/file_shrink_guard.py <paths>`; commit by explicit path; `python3 tools/room.py --push`; done line.
