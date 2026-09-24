# Grants plan: order, calendar, and what a yes unlocks

Written 24 Sept 2026 by the grants applications worker, from `grants/GRANTS.tsv` (the scout's 30 rows) and the
programme pages read the same day. Drafts are in `grants/applications/`; each has a card in `outreach/grant-*.md`.
Nothing here is sent by an agent: you submit every application yourself, or a local agent fills it while you
watch. Personal details (name, address, CV, bank or card) never go in the repository (rule 9).

## Recommended order

| # | Do | When | Why this order | Draft |
|---|---|---|---|---|
| 1 | Anthropic AI for Science | before Mon 5 Oct 2026 (monthly review) | largest credit award found (help page: up to $20,000 for 6 months; form: up to $50,000, usable across Claude.ai), exactly the usage this project runs on; 30 minutes to paste | `applications/anthropic-ai-for-science.md` |
| 2 | NCIS membership | this week | gives an affiliation to name on 1, 3 and 5, letters of introduction to archives, and discounted JPASS; starts the 15-month clock for NCIS grants | `applications/ncis-membership.md` |
| 3 | Anthropic External Researcher Access | before Mon 5 Oct 2026 (monthly review), only if you accept the study framing | $1,000 API credits for a measured study of agent over-claiming; needs a Console account and API key | `applications/anthropic-external-researcher-access.md` |
| 4 | Bibliographical Society Minor Grant | any time; send in October | £300 cash for copy orders, no affiliation needed, one referee | `applications/bibsoc-grants.md` |
| 5 | Huntington short-term fellowship | by 15 Nov 2026 (ask your referee by 18 Oct) | best subject fit (Eckert, Blathwayt, Destouches are Huntington collections), $4,000 a month; only if you can spend 1-3 months in San Marino in 2027-28 | `applications/huntington-short-term-fellowship.md` |
| 6 | OpenAI Researcher Access | by 30 Nov 2026 for the December review | $1,000 API credits for a cross-model verifier study; better with the NCIS affiliation in hand | `applications/openai-researcher-access.md` |
| 7 | Bibliographical Society Major Grant | cycle opens Nov 2026; deadline expected mid-Jan 2027 | up to £2,000 for copies and a Kew or BL visit; two referees | `applications/bibsoc-grants.md` section 4 |
| 8 | NCIS Research Grant ($599) | earliest 1 Feb 2028 (15 months of Full membership) | small cash, for copy orders | `applications/ncis-membership.md` section 4 |

## Calendar

| Date | What |
|---|---|
| 5 Oct 2026 (Mon) | Anthropic monthly review (AI for Science; External Researcher Access): submit before this |
| October 2026 | NCIS membership; Bibliographical Society Minor Grant |
| 18 Oct 2026 | ask the Huntington referee (four weeks before the deadline) |
| 2 Nov 2026 (Mon) | next Anthropic review, if you miss 5 Oct |
| November 2026 | Bibliographical Society Major Grant form published |
| 15 Nov 2026, 11:59 PM PST | Huntington short-term fellowship deadline |
| 30 Nov 2026 | OpenAI Researcher Access, in time for the December review |
| mid-Jan 2027 (check) | Bibliographical Society Major Grant deadline (2026's was 16 Jan) |
| March 2027 | Huntington and Bibliographical Society decisions |
| 1 Feb 2028 | earliest NCIS Research Grant deadline if you join in October 2026 |

## What a yes unlocks (in-kind and credits first)

1. **Anthropic AI for Science (credits on Claude.ai):** more sessions in the same window. On the first week's
   rate (fifteen N4 readings on one plan) a $20,000 award would roughly double the solver and verifier sessions for
   six months: the 23 copy-order and about 25 copy-free candidates in the queue could be read and verified in that
   time.
2. **Anthropic External Researcher Access ($1,000 API):** API usage outside the five-hour window, for the replay
   study. Needs an API key kept in the environment's secrets; add a line to BUDGETS.md before any worker uses it,
   since the briefs now assume no API key.
3. **OpenAI Researcher Access ($1,000 API):** a verifier from a second model family, checking whether the solver
   and verifier share blind spots.
4. **NCIS membership:** an affiliation for the credit forms that ask for one, letters of introduction for archives,
   and discounted JPASS for the verifier's JSTOR rows (now 60-odd rows in `JSTOR-QUEUE.tsv`, which block outreach
   at gate 2 until run or waived).
5. **Bibliographical Society (£300 now, up to £2,000 later):** cash for copy orders, which are the stage-2 to
   stage-7 blocker for most of the queue.
6. **Huntington fellowship ($4,000 a month):** time at the Eckert cipher books and ledgers, the Blathwayt and
   Destouches originals; a full concordance of the Eckert sent ledgers is the output.

## Considered and not drafted

| Programme (GRANTS.tsv) | Why not now |
|---|---|
| Folger short-term fellowship (fit 4) | no Folger manuscript on the project's list yet; an application needs specific materials. Revisit when a scout finds a Folger cipher item. |
| Lambda Cloud Research Grant, Hugging Face GPU grants (fit 4) | GPU credits; the project's cost is Claude usage and its solvers run on CPU. No practical gain. |
| JPASS at full price (fit 4) | buy it at the NCIS member discount instead, if JSTOR_USER's free 100 reads a month run short. |
| NEH Public Scholars (fit 2) | 2026 deadline (22 Apr 2026) passed; applicants must have published a nonfiction book with a university or trade press; the 2026 round was limited to American history and Western civilization. Revisit in early 2027 only if you meet the book requirement. |
| Google Cloud, AWS research credits (fit 2) | faculty, student or accredited-institution only. |
| Newberry Weinberg fellowship (fit 3) | 9-12 months in residence in Chicago; no Newberry target. |
| Royal Historical Society, Society of Antiquaries, IHR Scouloudi | membership or UK-citizen gates; check your own eligibility. |
| Experiment.com crowdfunding (fit 3) | possible later for a named copy-order campaign; not a grant. |

## Rules that apply to every draft

- Wording about readings is rule 10 wording only: "no prior decipherment located after a logged search" (N4).
  Never new, first, unread or unpublished.
- Numbers in the drafts are from `status.json` (24 Sept 2026, 13:28 UTC) and the AUDIT.md files. Refresh them on
  the day you submit.
- Submission is yours: by you, or by a local agent in your browser with you watching. Never a cloud session.
