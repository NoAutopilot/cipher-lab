# LANE V4 verifier V3b: check second opinions SO-DANZAY-F35, SO-GRAMONT-F30 (Opus, cap $10)

Common rules: `.claude/briefs/runs/2026-09-24-lane-v4-common.md`. Precedent: `.claude/briefs/runs/2026-09-24-lane-v4-v2-so-gramont-f29r.md`
and the section "Second opinion SO-GRAMONT-F29R" in ciphers/fr2980-gramont/AUDIT.md (V2, 24 Sept 2026, 16:06 UTC), which is the
shape to copy. An outside model (ChatGPT) answered our adversarial prompts; one file per label sits on its branch at
<folder>/second-opinions/chatgpt-<date>.md. Do them in this order, one at a time, committing after each:
- SO-DANZAY-F35: pull request 3, branch second-opinion/SO-DANZAY-F35, folder ciphers/fr20140-danzay-1557
- SO-GRAMONT-F30: pull request 4, branch second-opinion/SO-GRAMONT-F30, folder ciphers/fr2980-gramont

Per label: `git fetch origin second-opinion/<label>` and read the file from that ref. Check every checkable claim against the
source it cites (fetch a text once, grep it; Google Books with the key and country=US; archive.org full text; the repo's own
files). For each claim: verdict (right / wrong / unverifiable) and what you did. Correct our files where it is right (AUDIT.md,
NOTES.md, PROMPT-chatgpt*.md, reading headers), never the reading itself (log a reading issue as a one-line suggestion in
NOTES.md). If a claim shows a prior print or decipherment of the item, reclass in AUDIT.md with the evidence; otherwise the class
stays. Append to the target's AUDIT.md a section "Second opinion <label> (ChatGPT, pull request N), checked <date -u>" with a
claims table. Copy the file from the branch into <folder>/second-opinions/ on main (same name; if a file of that name exists
from another label in the same folder, suffix the label). Set the label's SECOND-OPINIONS-QUEUE.tsv row to status `checked`
with the `outcome` column one short phrase. Update the target's status.json results row only if the class changes. Do not
merge, close or comment on the pull requests. ROOM done line `for LANE V4: <label> checked -- <outcome>` per label.
Stop at the cap with what is pushed; say which labels remain.
