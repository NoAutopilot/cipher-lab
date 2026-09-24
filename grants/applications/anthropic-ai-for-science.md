# Anthropic AI for Science Program: application draft

## 1. The programme

- **Programme:** Anthropic's AI for Science Program (standard track, not the rare disease call).
- **Page:** https://support.claude.com/en/articles/11199177-anthropic-s-ai-for-science-program
- **Form:** https://docs.google.com/forms/d/e/1FAIpQLSfwDGfVg2lHJ0cc0oF_ilEnjvr_r4_paYi7VLlr5cLNXASdvA/viewform
- **Deadline:** rolling. The help page says "We evaluate submissions on the first Monday of each month." Next
  review: Monday 5 Oct 2026, then 2 Nov 2026.
- **Amount:** the help page says "up to $20,000 in API credits to your account for a 6-month period"; the form
  itself (read 24 Sept 2026) says "The AI for Science program offers extra usage credits, which can be used across
  all Claude.ai tools, including Claude Science. The maximum award for the AI for Science program is $50,000 in
  credits."
- **Eligibility, quoted from the page:** "The AI for Science program is designed for researchers attached to
  research institutions working on high-impact scientific projects, with a particular focus on biology and life
  sciences applications." The form adds: "The AI for Science program offers credits to qualified nonprofit and
  academic researchers, unless specified otherwise ... We welcome applications across the natural sciences and
  math, where AI can assist in rapidly accelerate discovery broadly."
- **Fit, honestly:** moderate. The project is historical cryptanalysis, which the form can hold only under "Math"
  plus its free "Other" box. The strong points are a clear AI integration, measurable results, and a public record.
  The weak point is affiliation: "attached to research institutions". Joining NCIS first (see
  `ncis-membership.md`) gives an affiliation to name. Apply anyway: the credits usable on Claude.ai are exactly
  what this project runs on, and a refusal costs nothing.

## 2. Every field on the form, in order (read from the live form, 24 Sept 2026)

| # | Field (form wording) | Required | Limit | Who fills it |
|---|---|---|---|---|
| 1 | Which program are you applying to? (option: Standard AI for Science program) | yes | choice | you: pick "Standard AI for Science program" |
| 2 | Which track are you applying to? (rare disease only) | shown only for the rare disease call | choice | skip |
| 3 | Name of primary contact | yes | | [your name] |
| 4 | Name of organization or research institution | yes | | see 3a |
| 5 | Position or title at organization | yes | | see 3a |
| 6 | What is your PI's academic or organization email address? ("If you are the PI, please enter your email address.") | no | | [your email] |
| 7 | Website of organization or research group, link to Google Scholar or GitHub | yes | | https://github.com/NoAutopilot/cipher-lab |
| 8 | Where did you hear about this program? | no | | see 3a |
| 9 | Project title | yes | | see 3b |
| 10 | Scientific field(s) (select all that apply): Biology / Life Sciences, Chemistry, Medicine/Healthcare, Environmental Science, Physics, Earth Science, Math, Other | yes | checkboxes | tick Math; Other: "Historical cryptanalysis (computational humanities)" |
| 11 | Which Organization ID would you like the credits applied to? ("claude.ai > accounts > settings") | yes | | [your Claude organization ID] |
| 12 | What type of Claude.ai account do you have? (Free, Pro/Max, Teams plan, Enterprise plan, Other) | no | choice | Pro/Max |
| 13 | In fewer than 100 words, please provide a description of the research team, including relevant expertise and credentials in both the scientific domain and AI/ML experience | yes | under 100 words | 3c, then add your credentials |
| 14 | Please provide links to Google Scholar profiles or other academic or professional profiles of key team members | no | | [your profile links] |
| 15 | In fewer than 500 words, please describe your research project, including: scientific question; methodology and approach; expected outcomes and deliverables; timeline for completion | yes | under 500 words | 3d |
| 16 | How specifically will Claude's capabilities be used in your research ... (200 words max) | yes | 200 words | 3e |
| 17 | Please describe the potential scientific impact of your research if successful (200 words max) | yes | 200 words | 3f |
| 18 | Does your research have potential applications beyond pure scientific discovery? ... (200 words max) | yes | 200 words | 3g |
| 19 | How do you plan to measure the success of using Claude in your research? ... (100 words max) | yes | 100 words | 3h |
| 20 | How much money in extra usage credits do you anticipate you will need? Please provide information on how this credit amount will lead to impact in your project. | yes | none stated | 3i |
| 21 | Does your research involve any of the following? (Pathogen research or virology; Drug resistance studies; Toxicology; Synthetic biology; None of the above) | yes | checkboxes | None of the above |
| 22 | If you checked any of the above, please explain the biosecurity safeguards ... (200 words max) | no | 200 words | leave blank |
| 23 | Is there anything else you would like the review committee to know about your application? | no | | 3j |
| 24 | Terms of Service ("Anthropic treats information submitted through this form as non-confidential ...") | yes | I agree | you |

## 3. Drafted copy

### 3a. Organisation, position, how you heard

- Field 4: "Independent researcher (cipher-lab)" or, once a member, "National Coalition of Independent Scholars
  (NCIS), independent scholar".
- Field 5: "Principal investigator".
- Field 8: [how you heard; for example "Claude help center"].

### 3b. Project title (field 9)

Reading undeciphered historical cipher letters with Claude agents under a verifier protocol

### 3c. Research team (field 13, under 100 words; 66 words before your credentials)

> I am an independent researcher and the project's principal investigator. I direct a team of Claude Code agent
> sessions that scout archive catalogues, transcribe cipher letters from page images, recover keys, read the
> ciphers and verify novelty against printed editions. I wrote the project's rules, verification protocol and
> review of every result. [One sentence on your own background: languages, programming, statistics or history.]
> Public record: https://github.com/NoAutopilot/cipher-lab

### 3d. Research project (field 15, under 500 words; 423 words)

> **Question.** European archives hold diplomatic letters from about 1450 to 1870 whose ciphered passages were
> never deciphered, or whose decipherment sits in another box. Specialist lists (S. Tomokiyo's Cryptiana, the
> DECODE database) still mark hundreds unsolved. Which of these can be read today, and how can an AI-assisted
> project prove that a reading is correct and that it was not already in print?
>
> **Method.** Claude agent sessions do one job each. A scout harvests candidates from catalogues that DECODE does
> not cover (The National Archives, the British Library, the BnF, German and Dutch state archives). A check-solved
> sweep of six sources rules out items already read. Transcription runs twice from the page image and a script
> reconciles the passes. Key recovery aligns a surviving contemporary decipherment, or a key in a sibling letter,
> to the ciphertext; where there is none, statistical solvers (homophonic and nomenclator annealing with
> 16th-century Italian, French and Latin language models) attack the text. Every decoded token is graded: H from a
> key source, C from known plaintext, S cryptanalytic with a matched synthetic control, M uncertain. No negative
> is reported without a control of the same length and design. A script regenerates each reading and fails if the
> committed one is stale. Finally a separate verifier session searches editions, catalogues, full-text libraries
> and scholarship to disprove novelty and assigns a class from N0 (already known) to N5 (confirmed by the archive).
>
> **Results in the first week (17 to 24 Sept 2026).** Fifteen cipher passages from seven groups of letters
> (1530 to 1864) reached N4: no prior decipherment located after a logged search, two independent audits each. One
> was read without any key source (238 of 364 tokens at grade S). Thirteen candidates were shown to be already
> solved before solver time was spent, five catalogue entries were corrected, and three negatives with matched
> controls were recorded.
>
> **Deliverables in six months.** (1) Readings of the remaining items at the top of the queue, including the 23
> that need archive copies; (2) an audit file for each reading, with the full search log; (3) machine-readable keys
> and readings offered to Cryptiana, DECODE and the holding archives; (4) the reusable tools (33 scripts with
> offline tests) documented for other cipher projects; (5) a short methods paper on the verifier protocol and the
> over-claims it caught.
>
> **Timeline.** Months 1-2: clear the verification backlog and send the outreach for the fifteen N4 readings.
> Months 2-4: copy orders and transcription for the 23 copy-order candidates; key recovery and solving. Months
> 4-6: verification, datasets, methods paper.

### 3e. How Claude is used (field 16, 200 words max; 138 words)

> Claude does nearly all of the work under my direction. Claude Code sessions run as specialised workers: they
> query archive APIs and IIIF image servers, cut page images into line crops, transcribe cipher symbols in two
> independent passes, write and test the solver scripts, reason about nomenclator structure and 16th-century
> French, Italian, Latin and Dutch plaintext, and search editions for prior print. A verifier session, separate
> from the solver's, tries to disprove each claim. Scripts do the reading of large texts and Claude judges the
> hits, which keeps usage down. Without Claude this work would need a palaeographer, a cryptanalyst, a programmer
> and a research assistant with five languages. With it, one person produced fifteen audited readings in a week.
> The limit now is usage: my personal plan's window is spent within hours, and every session then stops.

### 3f. Scientific impact (field 17, 200 words max; about 115 words)

> Each reading gives historians of diplomacy a checked text of a passage for which no prior decipherment was located: Gramont's reports from Rome
> to Villandry and Francis I in May 1530, the Danish mission of Danzay in 1557, the
> correspondence of William of Orange and his brothers in the 1560s and 1570s, English intelligence from Spain in
> the 1720s, and Union telegrams of 1864. The keys and datasets let other researchers check and extend the work.
> The project also produces evidence about AI in research: how often agents over-claim novelty, what catches it,
> and what a reproducible, graded reading looks like. That record is public and can be reused by any humanities
> project that uses AI agents.

### 3g. Applications beyond discovery (field 18, 200 words max; 94 words)

> Archives get corrected catalogue entries and machine-readable readings of items in their care. The cipher-history
> community (Cryptiana, DECODE, the open solver repositories) gets keys and audited readings it can build on. The
> tools are general: a IIIF line cropper, a transcription reconciler, a key-application and grading script, a
> printed-cipher detector for scanned editions, and a novelty verification protocol. They scale to the thousands
> of undeciphered cipher items in European archives. The protocol itself (graded tokens, matched controls, a separate
> verifier) is a practical safeguard any team can adopt when AI agents make research claims.

### 3h. Measuring success (field 19, 100 words max; 56 words)

> 1. Number of readings classed N3 or better by a separate verifier (baseline 15 at N4 after one week).
> 2. Cost per verified reading in credits.
> 3. Over-claims caught before any result leaves the repository.
> 4. Items shown already solved before solver time is spent.
> 5. Keys, readings and corrections accepted by archives, Cryptiana or DECODE.

### 3i. Credits requested (field 20)

> **$20,000 in extra usage credits over six months.** Line items, in API-equivalent usage:
>
> | Line | Estimate | Basis |
> |---|---|---|
> | Solver and key-recovery sessions (strongest model) | $8,000 | about 40 targets at $150-250 each, from the project's ledger of worker costs |
> | Verifier sessions (strongest model, two audits per reading) | $5,000 | about 50 readings at $50-100 per audit |
> | Transcription passes and catalogue sweeps (Sonnet) | $4,000 | two passes per letter; sweeps of TNA, BL, BnF and German archive catalogues |
> | Orchestration and reconciliation | $3,000 | one orchestrator session per working day |
>
> How this leads to impact: the project's measured output in its first week was fifteen N4 readings on one
> personal plan, and every day the plan's usage window runs out several hours before the work does. The credits
> would roughly double the sessions that can run, so the readings in the queue (23 waiting on archive copies,
> about 25 copy-free) can be read and verified in six months instead of a year or more.

### 3j. Anything else (field 23)

> The project follows a written rule that no reading is called new or first by the session that produced it. A
> separate verifier assigns the novelty class after a logged search, and results are described outside the
> repository only with the verifier's safe sentence. All audit files are public, for example
> https://github.com/NoAutopilot/cipher-lab/blob/main/ciphers/fr2980-gramont/AUDIT.md

## 4. Fill-in checklist (personal fields; none of this goes in the repository, rule 9)

- [ ] [your name] (field 3)
- [ ] [your email] (field 6)
- [ ] [your Claude organization ID] from claude.ai > Settings > Account (field 11)
- [ ] [your affiliation]: "Independent researcher" or "NCIS" once a member (field 4)
- [ ] [one sentence on your background] in field 13
- [ ] [your profile links] (field 14): GitHub profile, any personal page
- [ ] Check the numbers in 3d against `status.json` on the day you submit
- [ ] Tick "I agree" (field 24)

## 5. Documents

None are uploaded; the form is text only. Keep `project-one-pager.md` and `cv-skeleton.md` ready in case the
committee writes back.

## 6. How to submit

- Google Form, no portal account needed, but you need a Claude account (for the organization ID) and a Google
  sign-in may be asked for.
- A local agent (Claude in Chrome, or a local Claude Code session with a browser) can paste each field while you
  watch and you press Submit. A cloud session must not submit it.
- Keep a copy of the text you submitted on your own machine; Google Forms sends no copy unless the form is set to.
