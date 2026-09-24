# Anthropic External Researcher Access Program: application draft

## 1. The programme

- **Programme:** Anthropic's External Researcher Access Program (API credits for safety and alignment research).
- **Page:** https://support.claude.com/en/articles/9125743-what-is-the-external-researcher-access-program
- **Form:** https://forms.gle/pZYC8f6qYqSKvRWn9
- **Deadline:** rolling. The form says "We evaluate submissions on the first Monday of each month." Next review:
  Monday 5 Oct 2026.
- **Amount:** "If successful, we will apply $1000 API credits to the account. For rare special cases, we may
  approve a higher quantity of credits."
- **Eligibility, quoted from the form:** "This program provides free API credits for our standard model suite to
  researchers working on safety and alignment research topics we consider high priority." And: "Note that these
  credits are for API use and do not apply to Claude.ai."
- **Fit, honestly:** narrow but real. The project is not alignment research in the usual sense. What it does have
  is a week of logged evidence about AI agents over-claiming novelty in research, and a verifier protocol that
  catches it. That is a question about honesty and calibration of agents doing open-ended research, which is the
  angle this draft takes. Only apply if you are content to study that question in its own right, with a short
  public write-up at the end; do not apply to fund the cipher work under a safety label.
- **What a yes unlocks:** API credits run outside your Claude.ai usage window. They need an Anthropic Console
  account and an API key held by you; see section 6.

## 2. Every field on the form, in order (read from the live form, 24 Sept 2026)

| # | Field (form wording) | Required | Limit | Who fills it |
|---|---|---|---|---|
| 1 | Name of primary contact | yes | | [your name] |
| 2 | Name of organization (if applicable) | no | | "Independent researcher" or "NCIS" |
| 3 | Have you been recommended to this form by an Anthropic employee? (Yes / No) | yes | choice | No |
| 4 | If you have been referred to this form by an Anthropic employee, please enter their name here | no | | blank |
| 5 | Which Organization ID would you like the credits applied to? (console.anthropic.com/settings/organization; "If you have not yet set up an account, please set up an account at https://console.anthropic.com before submitting this form.") | yes | | [your Console organization ID] |
| 6 | In less than 200 words, please provide a brief description of the individual applicant or team, including the relevant expertise. | yes | under 200 words | 3a |
| 7 | In less than 300 words, please describe your research or request for free API credits, making sure to explain: the topic of the project or research; why free API credits are important for your team to complete this research/project | yes | under 300 words | 3b |
| 8 | Are you requesting more than $1000 API credits? If so, please enter the amount in 'Other' | yes | No / Other | No |
| 9 | Low quality of service is acceptable? ("I'm fine with receiving a low quality of service" / "My use case will require a standard quality of service") | no | choice | I'm fine with receiving a low quality of service |
| 10 | Please provide a link to your Google Scholar profile or github profile | yes | | [your GitHub profile] and https://github.com/NoAutopilot/cipher-lab |
| 11 | Additional Information (optional) | no | | 3c |
| 12 | Are you located within the United States? (tax and accounting) | no | Yes / No | [you] |
| 13 | Terms of Service | yes | I agree | you |

## 3. Drafted copy

### 3a. Applicant (field 6, under 200 words; 118 words plus your sentence)

> I am an independent researcher. Since 17 September 2026 I have directed a team of Claude Code agent sessions
> that read undeciphered historical cipher letters from European archives. The agents scout catalogues, transcribe
> page images, recover keys, solve ciphers and search printed editions. I designed the project's rules, among them
> a protocol that separates the agent that produces a reading from a second agent that tries to disprove its
> novelty, and a ledger that records every worker session, its cost and its outcome (about 375 rows so far).
> [One or two sentences on your own background: programming, statistics, languages, history.] Everything is
> public: https://github.com/NoAutopilot/cipher-lab

### 3b. Research and why credits matter (field 7, under 300 words; 262 words)

> **Topic: over-claiming by AI research agents, and a protocol that catches it.** Agents doing open-ended research
> are rewarded, implicitly, for finding something. In my project that pressure shows up as novelty claims: a
> solver agent that decodes a passage tends to call it "never printed" after checking one source. On 20 September
> 2026 four readings were called "never printed" because they were absent from one series of printed records; the
> sender-specific editions had not been searched. Since then the project has run a written rule: the solver may
> report only what it searched, and a separate verifier agent, working from the plaintext and the search log,
> tries to find the reading in print and assigns a class from N0 (already known) to N5 (confirmed by the archive).
> Fifteen readings have passed two such audits at N4 (no prior decipherment located); several earlier claims were
> downgraded, and thirteen candidates were shown to be already solved before any solver time was spent.
>
> I want to turn this record into a measured study: (1) code every solver claim and verifier verdict in the ledger
> and audit files by type of over-claim; (2) replay a sample of solver sessions with and without the rule-10
> wording in the brief, and with and without a verifier, and compare over-claim rates; (3) publish the coded
> dataset, the briefs and a short write-up.
>
> **Why credits.** The project runs on one personal subscription whose usage window already limits the cipher
> work. Replaying sessions for a controlled comparison would take that window away from the research itself. $1,000
> of API credits pays for the replay experiments at Sonnet and Opus prices without stopping the main project.

### 3c. Additional information (field 11)

> The audit files show the verifier protocol at work, with every source searched and every one unreachable, for
> example https://github.com/NoAutopilot/cipher-lab/blob/main/ciphers/fr2980-gramont/AUDIT.md and the
> project rules in https://github.com/NoAutopilot/cipher-lab/blob/main/CLAUDE.md (rule 10).

## 4. Fill-in checklist (rule 9: none of this goes in the repository)

- [ ] Create an Anthropic Console account at https://console.anthropic.com if you do not have one
- [ ] [your name] (field 1)
- [ ] [your Console organization ID] (field 5)
- [ ] [one or two sentences on your background] in 3a
- [ ] [your GitHub profile] (field 10)
- [ ] [US or not] (field 12)
- [ ] Tick "I agree" (field 13)

## 5. Documents

None. Text form only. If the committee asks, send `project-one-pager.md`.

## 6. How to submit, and what a yes needs

- Google Form, no portal. A Console account must exist first (field 5).
- A local agent can paste the fields while you watch; you press Submit. A cloud session must not submit.
- Using the credits means an API key. It must stay with you: store it in the environment's secrets, never in the
  repository, and never print it (CLAUDE.md, credentials handling rule). The project's briefs assume a Max
  subscription and no API key (BUDGETS.md, 24 Sept 2026), so a yes needs one line added there before any worker
  uses the key.
