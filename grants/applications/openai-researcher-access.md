# OpenAI Researcher Access Program: application draft

## 1. The programme

- **Programme:** OpenAI Researcher Access Program (API credits).
- **Page and portal:** https://openai.smapply.org/prog/openai_researcher_access_program/ (SurveyMonkey Apply)
- **Deadline:** rolling, reviewed quarterly. Page: "applications are reviewed once every 3 months (in March,
  June, September, and December). Grants may take up to 4 weeks to credit to awardees after they receive their
  application decision." The September round is under way on 24 Sept 2026; aim for the December round and submit
  by 30 Nov 2026.
- **Amount:** "Researchers can apply for up to $1,000 of OpenAI API credits to support their work. Credits are
  valid for a period of 12 months and they can be applied towards any of our publicly available models."
- **Eligibility, quoted from the page:** "We encourage applications from early stage researchers in countries
  supported by our API, and are especially interested in subsidizing work by researchers with limited financial
  and institutional resources." The help center FAQ (via search, 24 Sept 2026; the page itself returned 403 to
  this session) adds that applicants need "an active affiliation to an academic institution or other research
  organization, as well as nonprofits conducting research activities". NCIS membership would supply the
  affiliation (see `ncis-membership.md`).
- **Areas of interest listed on the page:** Alignment; Fairness and representation; Societal impact;
  Interdisciplinary research ("How can AI development draw on insights from other disciplines such as philosophy,
  cognitive science, and sociolinguistics?"); Interpretability; Misuse potential; Robustness; Other.
- **Fit:** moderate. The strongest framing is "Interdisciplinary research" and "Societal impact": what AI agents
  can and cannot do reliably in humanities research, measured on a public record. The credits would also let the
  project run a second model family as an independent verifier, which is useful in its own right: a verifier from
  a different model family is less likely to share the solver's blind spots.

## 2. The form's fields

The application form sits behind a SurveyMonkey Apply login, so this session could not read its fields (no
account; the good-citizen rule forbids creating one for you). What the programme page asks applicants to address:
the research question, the area of interest, why subsidised access is needed, and agreement to the sharing and
publication policy (https://openai.com/policies/sharing-publication-policy/#research).

**Step for you or a local agent with you watching:** register on the portal, open the application, and paste the
field list into this file (field wording, order, limits) before filling it. The copy below is written to be cut to
whatever limits the form sets.

Fields every SM Apply credit form of this kind has asked for, in likely order, with drafted copy below:

| Likely field | Draft |
|---|---|
| Name, email, country | [your name], [your email], [your country] |
| Institution or organisation, role | 3a |
| Project title | 3b |
| Area of interest (from the list above) | Interdisciplinary research; Societal impact |
| Project abstract or summary | 3c |
| Research description, methods, timeline | 3d |
| How the API credits will be used, amount requested | 3e |
| Publication and sharing plan | 3f |
| Links (GitHub, Google Scholar, CV) | https://github.com/NoAutopilot/cipher-lab; [your profile]; CV from `cv-skeleton.md` |
| OpenAI organization ID for the credits | [your OpenAI organization ID] |
| Agreement to policies | you |

## 3. Drafted copy

### 3a. Organisation and role

"Independent researcher (cipher-lab); principal investigator." Once a member: "National Coalition of Independent
Scholars (NCIS)".

### 3b. Project title

Measuring what AI research agents get right in historical cryptanalysis: graded readings, matched controls and a
cross-model verifier

### 3c. Abstract (about 150 words)

> European archives hold diplomatic letters from the 15th to the 19th century whose ciphered passages were never
> deciphered, or whose decipherment is filed elsewhere. Since September 2026 I have directed a team of AI agent
> sessions that find, transcribe, read and verify these letters. Every decoded token is graded by its evidence,
> every negative has a matched synthetic control, and a separate verifier agent searches printed editions to
> disprove novelty. In one week, fifteen passages reached the class "no prior decipherment located after a logged
> search", and thirteen candidates were shown to be already solved before any solver time was spent. This project
> asks what such agents do reliably in humanities research and where they fail: over-claiming novelty, transcription
> errors, false negatives. I will use OpenAI models as an independent verifier from a second model family, measure
> agreement with the first family's claims, and publish the coded dataset and the protocol.

### 3d. Description, methods and timeline (about 400 words)

> **Background.** Specialist lists (S. Tomokiyo's Cryptiana, the DECODE database) still mark hundreds of
> historical cipher items unsolved. The project's public repository (https://github.com/NoAutopilot/cipher-lab)
> holds its rules, tools, readings and audit files.
>
> **Methods.** Agent sessions do one job each: scouting catalogues, a six-source check that an item is unsolved,
> two independent transcription passes from page images, key recovery by aligning surviving contemporary
> decipherments, statistical solving with period language models, and verification. Tokens are graded H (from a
> key source), C (known plaintext), S (cryptanalytic, with a matched control), M (uncertain) or I (inferred). A
> script regenerates every reading and fails if the committed text is stale. The verifier assigns a novelty class
> from N0 (already known) to N5 (confirmed by the holding archive) after a logged search of editions, catalogues,
> full-text libraries and scholarship.
>
> **The question for this grant.** Today the solver and the verifier come from the same model family. Do they
> share blind spots? I will run an OpenAI model as a third, independent reviewer on three tasks where ground truth
> exists: (1) re-grading a sample of decoded tokens against the key and the page image; (2) re-running the novelty
> search for readings already classed, and comparing its verdict with the first verifier's; (3) judging which of
> the solver's sentences over-claim. Ground truth comes from items whose decipherment is known (contemporary
> decipherments on the leaf, printed editions) and from the project's logged over-claims.
>
> **Timeline.** Months 1-2: build the evaluation set from the audit files and the ledger (about 375 logged worker
> sessions). Months 3-6: run the cross-model reviews. Months 7-9: analysis. Months 10-12: write-up and release of
> the dataset.
>
> **Why it matters beyond ciphers.** Humanities projects are starting to use agents for archive work. They need
> evidence about where agents can be trusted and a protocol that catches the rest. This project already produces
> that evidence as a by-product; the grant makes it a measured result.

### 3e. Use of credits and amount

> $1,000, the programme's maximum. Estimated use: about 60 verification runs (re-grading and novelty searches) at
> $8-12 each on a strong model, about $600; about 200 sentence-level over-claim judgements and agreement checks on
> a smaller model, about $150; the remainder for re-runs and the analysis. I have limited financial and
> institutional resources: the project runs on one personal subscription and no institution funds it.

### 3f. Publication and sharing

> Everything is published under the repository's open terms: the evaluation set, the prompts, the model outputs,
> the coded disagreements and a short write-up. I will follow OpenAI's sharing and publication policy for research
> and name the models and dates used.

## 4. Fill-in checklist (rule 9: none of this goes in the repository)

- [ ] Register at https://openai.smapply.org/ ([your email], a password you choose)
- [ ] [your name], [your country] (must be a supported API country)
- [ ] [your affiliation]: independent, or NCIS once a member
- [ ] [your OpenAI organization ID] from platform.openai.com settings (needs an OpenAI API account)
- [ ] [your CV] from `cv-skeleton.md`, completed on your own machine, if the form asks for one
- [ ] Copy the form's real field list into section 2 of this file and trim the drafts to its limits

## 5. Documents

Possibly a CV (use `cv-skeleton.md`). The project summary in `project-one-pager.md` can be pasted into any
"supporting information" box.

## 6. How to submit

- Portal: SurveyMonkey Apply, account needed (register on the page above).
- A local agent in your own browser can fill the form while you watch; you press Submit. A cloud session must not
  register accounts or submit.
- A yes needs an OpenAI API key used by the verifier runs. Keep it in the environment's secrets, never in the
  repository, never printed.
