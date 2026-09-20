export const meta = {
  name: 'check-solved',
  description: 'Establish whether a cipher target is still unsolved by sweeping six independent sources, then write the verdict into its NOTES.md',
  whenToUse: 'Before any campaign on a target in ciphers/, or when a catalogue row may be stale. args: { target: "<folder name under ciphers/>", description: "<one line: who, to whom, date, shelfmark>" }',
  phases: [
    { title: 'Sweep', detail: 'six searchers, one per source type, each blind to the others' },
    { title: 'Reconcile', detail: 'one agent merges the evidence and writes the verdict' },
  ],
}

const target = args && args.target
const desc = (args && args.description) || ''
if (!target) throw new Error('args.target is required: the folder name under ciphers/')

const HIT = {
  type: 'object',
  properties: {
    source: { type: 'string' },
    checked: { type: 'array', items: { type: 'string' }, description: 'exact queries, URLs or files examined' },
    found: { type: 'boolean', description: 'true if a solution, key, plaintext or serious prior attempt was found' },
    evidence: { type: 'array', items: { type: 'object', properties: {
      what: { type: 'string' }, where: { type: 'string' }, who: { type: 'string' }, when: { type: 'string' },
      status: { type: 'string', enum: ['solved', 'partial', 'closed-negative', 'blocked', 'attempted', 'listed-only'] },
    }, required: ['what', 'where', 'status'] } },
    blocked: { type: 'string', description: 'if a source could not be reached, say which and why; empty otherwise' },
  },
  required: ['source', 'checked', 'found', 'evidence', 'blocked'],
}

const SOURCES = [
  { key: 'web', prompt: `Search the open web for any solution, decipherment, key or serious attempt on this cipher. Use WebSearch with several phrasings: the sender and recipient names with "cipher", the shelfmark, the year plus "undeciphered", and "solved". Read the top results that look relevant with WebFetch where it works; if WebFetch is blocked (returns an egress error), rely on the search snippets and say so in "blocked".` },
  { key: 'print', prompt: `Check whether the plaintext is already in print. Search the Internet Archive and HathiTrust catalogues (via WebSearch if direct fetch is blocked) for the sender's printed Letters or Correspondance, the relevant Camden Society, HMC or Calendar of State Papers volume, and any 19th-century edition that might print the letter in clear. Report the volume, page and whether the cipher passage is printed deciphered, undeciphered, or omitted.` },
  { key: 'lists', prompt: `Check the community lists and their comment threads: Cryptiana (cryptiana.web.fc2.com/code/unsolved.htm and the blog cryptiana.blogspot.com), Klaus Schmeh's Cipherbrain, Nick Pelling's Cipher Mysteries, MysteryTwister, and r/codes. The repository has a snapshot of Cryptiana at sources/cryptiana/ which you can read locally with python3 tools/html2text.py; use it if the live sites are blocked. Report any mention, especially solution claims in comments.` },
  { key: 'decode', prompt: `Check the DECODE database at de-crypt.org: search for the record by sender, recipient, shelfmark and year, and report the record id, its status field, and whether any attached file looks like a key or a decipherment. If the site is blocked from this environment, say so in "blocked" and report whatever the repository's own files (CATALOG.md, LANDSCAPE.md, ciphers/<target>/NOTES.md) already say about DECODE records for this item.` },
  { key: 'bourdeau', prompt: `Check Daniel Bourdeau's repository github.com/dbourdeau/cyphersolver. Clone it shallowly if not present: GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/dbourdeau/cyphersolver /tmp/cyphersolver. Read README.md, TARGETS.md, SOLVED_CATALOGUE.md and any folder whose name matches this target, and report his status and evidence verbatim with the file path. Also check the docs/ site pages if a write-up exists.` },
  { key: 'aymeloglu', prompt: `Check Andrew Aymeloglu's repository github.com/aaymeloglu/unsolved-ciphers. Clone it shallowly if not present: git clone --depth 1 https://github.com/aaymeloglu/unsolved-ciphers /tmp/unsolved-ciphers. Read README.md, TARGETS.md, SHORTLIST.md, CATALOGUE.md and any matching folder, and report status and evidence verbatim with the file path. Also check Robert Pitt's repositories on GitHub (github.com/robertpitt) for a matching name.` },
]

const VERDICT = {
  type: 'object',
  properties: {
    status: { type: 'string', enum: ['open', 'partial', 'solved', 'closed-negative', 'found-solved', 'blocked', 'offline-only'] },
    summary: { type: 'string', description: 'three to six sentences a reader can act on' },
    notes_section: { type: 'string', description: 'the exact markdown appended to NOTES.md' },
    unreachable: { type: 'array', items: { type: 'string' } },
  },
  required: ['status', 'summary', 'notes_section', 'unreachable'],
}

phase('Sweep')
log(`Sweeping six sources for ciphers/${target}`)
const results = await pipeline(
  SOURCES,
  s => agent(
    `Target: ciphers/${target}. ${desc}\n\nFirst read ciphers/${target}/NOTES.md for the shelfmark, dates and people involved.\n\nYour single job, blind to the other searchers: ${s.prompt}\n\nBe literal about what you checked: list every query and URL in "checked". Set found=true only for a real solution, key, plaintext, or a documented attempt with a stated status. Never infer a solution from a title; quote the evidence.`,
    { label: `sweep:${s.key}`, phase: 'Sweep', schema: HIT },
  ),
)
const hits = results.filter(Boolean)
const unreachable = hits.filter(h => h.blocked).map(h => `${h.source}: ${h.blocked}`)
log(`${hits.length}/${SOURCES.length} searchers returned; ${hits.filter(h => h.found).length} found something; ${unreachable.length} reported a blocked source`)

phase('Reconcile')
const verdict = await agent(
  `Target: ciphers/${target}. ${desc}\n\nSix independent searchers reported as follows (JSON):\n${JSON.stringify(hits, null, 2)}\n\nReconcile them. Decide the target's status using the repository's vocabulary in CLAUDE.md rule 5. Then write a markdown section titled "## Check-solved sweep, ${(args && args.date) || 'date unknown'}" for ciphers/${target}/NOTES.md that lists, per source, what was checked and what was found, names the people and dates for any prior work, and ends with a one-line verdict. Sources that were unreachable are listed as unchecked, never as negative. Append that section to ciphers/${target}/NOTES.md with a Bash heredoc or the Edit tool, update the Status line at the top of the file if the verdict changes it, and commit with the message "check-solved: ${target}" (do not push). Return the verdict object.`,
  { label: `reconcile:${target}`, phase: 'Reconcile', schema: VERDICT },
)
return verdict
