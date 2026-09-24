# Grants and compute-credit scouting

`GRANTS.tsv` lists 30 funding, credit and in-kind-access programmes checked against this project's
situation: an independent researcher with no institutional affiliation, running cipher-lab on a personal
Claude subscription, wanting more compute credits and modest funds for archive copy orders and journal
access, not a money-maker. Each row was read on its own page (not from memory), dated 24 Sept 2026, with
the URL that was read. Sorted by fit (1-5).

Rule 9: no personal data about the owner appears anywhere below or in GRANTS.tsv. Rule 10: nothing here
calls any project output "new", "first" or "unpublished" -- see README's own "What counts as a result"
and CLAUDE.md rule 10 for the only allowed wording, which stays with the audited items themselves, not
with a grant pitch.

## Top five by fit

1. **Bibliographical Society (UK) Major/Minor Grants** (fit 5) -- up to GBP 2,000, and its guidelines say
   it "particularly supports those who have no opportunity of gaining institutional support for their
   research." This is the single best match: cash for the exact costs the project already incurs (archive
   copies, images, travel to consult a manuscript), no affiliation gate, no membership wait.
2. **Hugging Face Community GPU Grants** (fit 4) -- free, in-kind GPU hardware (ZeroGPU/A10G) inside a
   Hugging Face Space, applied for from the Space's own settings page with no external portal. No
   affiliation requirement. Only useful for a public-facing demo/tool, not the private Claude API usage
   that is the actual bottleneck.
3. **Lambda Cloud Research Grant** (fit 4) -- up to $5,000 in GPU cloud credits, rolling applications, no
   institutional-affiliation requirement found on the pages read (though the application itself is
   competitive and its exact eligibility text was not independently confirmed). Like Hugging Face, it
   funds GPU training rather than the Claude API calls this project actually runs on.
4. **JPASS** (fit 4) -- not a grant but a $199/year personal JSTOR subscription, explicitly "designed for
   people doing research without access to JSTOR through a school or library." Worth keeping as a paid
   fallback for the verifier's scholarship pass if the JSTOR_USER/JSTOR_PASS credential in CLAUDE.md ever
   lapses.
5. **Folger Institute Short-Term Fellowships** (fit 4) -- $4,000-5,000/month, explicitly open to
   independent scholars, with a virtual option. The Folger's 15th-18th century British/European
   manuscript holdings overlap several of the project's English cipher targets, but this needs a
   Folger-specific target identified before it is worth an application.

Also worth noting even though it scored lower: the **National Coalition of Independent Scholars (NCIS)
Research Grants** (fit 4, $599 cash) are exactly aimed at this profile, but membership must be held for 15
consecutive months before a grant application -- worth joining now (a $60/year Full Membership) for a
2027 application, not a near-term source.

## Programmes that require an institutional affiliation

Several of the largest credit programmes checked are blocked purely on affiliation, not on merit or fit:

- **Anthropic AI for Science** -- up to $20,000 in API credits, the single largest amount found anywhere
  in this search, but its own help page states eligibility as "researchers attached to research
  institutions." This is the strongest case for a partnership: a library, university history department,
  or a body like the Bibliographical Society or NCIS naming the project as an affiliated or sponsored
  effort would likely unlock it.
- **OpenAI Researcher Access Program** ($1,000 in credits) requires "an active affiliation to an academic
  institution or other research organization, as well as nonprofits conducting research activities."
- **Google Cloud Research Credits** (up to $5,000) and **AWS Cloud Credit for Research** (uncapped for
  faculty/staff) both require the applicant to be faculty, staff, or a student "at an accredited research
  institution."
- **Modal for Academics** and the now-concluded **Microsoft AFMR** were both academic-institution-only even
  before Modal's academic tier was paused.
- **Gale State Papers Online** has no individual-purchase route at all -- it is sold only as an
  institutional subscription (one source cites roughly GBP 300,000 for a full university licence). Getting
  State Papers Online access at all, as opposed to the calendar summaries already used, requires a library
  partnership, not a grant application.

A fiscal sponsorship or a named partnership with a library, archive, or scholarly society (several of
which, like the Bibliographical Society and NCIS, are themselves built for independent researchers and
carry no institutional gate) is the practical route to the affiliation-gated tier above, if the owner ever
wants to pursue one. None of this requires deciding anything now; the two routes (apply directly to the
fit-5/4 rows above; consider a partnership later for the affiliation-gated rows) are independent and can be
pursued at whatever pace the owner chooses.

## What was checked and found not useful

The **American Cryptogram Association** has no grant, scholarship or research-funding programme at all --
it is a hobbyist cipher-solving membership organisation. The **DECRYPT project** (Swedish Research Council,
2019-2024) has already concluded and was never open to outside applicants; its practical legacy for this
project is the DECODE database and the HistoCrypt community, both already used per CLAUDE.md's access
playbook and outreach rules, not a funding source. **Sloan's Open Source in Science** programme explicitly
states it does not fund individual open-source projects, only ecosystem-level tooling and institutions.
**Mozilla's MOSS** programme and Fellowship are both currently closed or nomination-only. **Google for
Startups** requires an incorporated company, which this project is not and has no plan to become.

## Method

Each programme's own page was read directly (WebSearch to find the page, then read for the specific
eligibility sentence quoted in GRANTS.tsv) on 24 Sept 2026; nothing here is from memory. Where a page's
own wording was ambiguous about whether an unaffiliated individual qualifies, GRANTS.tsv says "unclear"
and quotes the sentence that leaves it open, rather than guessing. No personal data about the owner was
used in any search query.
