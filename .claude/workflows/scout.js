export const meta = {
  name: 'scout',
  description: 'Harvest candidate unsolved ciphers from every source, drop what is already solved, score the rest for this project, and file them in QUEUE.md',
  whenToUse: 'Weekly, or whenever the solver repositories or Cryptiana change. args: { date: "19 Sept 2026", languages: ["en"], max: 40 }',
  phases: [
    { title: 'Harvest', detail: 'five blind harvesters, one per source family' },
    { title: 'Filter', detail: 'dedupe and remove anything already solved or read' },
    { title: 'Score', detail: 'one scorer per candidate, cheap' },
    { title: 'File', detail: 'write QUEUE.md and commit' },
  ],
}

const date = (args && args.date) || 'date unknown'
const langs = (args && args.languages) || ['en']
const MAX = (args && args.max) || 40

const CANDIDATES = {
  type: 'object',
  properties: {
    source: { type: 'string' },
    checked: { type: 'array', items: { type: 'string' } },
    blocked: { type: 'string' },
    candidates: { type: 'array', items: { type: 'object', properties: {
      name: { type: 'string', description: 'sender to recipient, date' },
      shelfmark: { type: 'string' },
      year: { type: 'string' },
      language: { type: 'string', description: 'plaintext language, ISO code or "unknown"' },
      status_at_source: { type: 'string', description: 'the source\'s own status words, verbatim' },
      material: { type: 'string', description: 'what is online: images, transcription, printed figures, nothing' },
      key_lead: { type: 'string', description: 'any key, sibling decipherment or printed plaintext the source names' },
      size: { type: 'string', description: 'groups or pages if stated' },
      where: { type: 'string', description: 'file path or URL of the evidence' },
    }, required: ['name', 'year', 'language', 'status_at_source', 'material', 'key_lead', 'where'] } },
  },
  required: ['source', 'checked', 'blocked', 'candidates'],
}

const HARVESTERS = [
  { key: 'bourdeau', prompt: `Clone github.com/dbourdeau/cyphersolver shallowly (GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/dbourdeau/cyphersolver /tmp/cyphersolver) if not present. Harvest every target he lists as still open: the "Offline only", "Attempted and closed", "In progress" tables in README.md, the open rows of TARGETS.md, and the open entries of catalogue.json / CATALOGUE.md (skip anything marked solved, read, found-solved or explained). For each, capture his stated blocker and what would move it.` },
  { key: 'aymeloglu', prompt: `Clone github.com/aaymeloglu/unsolved-ciphers shallowly (git clone --depth 1 https://github.com/aaymeloglu/unsolved-ciphers /tmp/unsolved-ciphers) if not present. Harvest open candidates from SHORTLIST.md (Tier 1 and 2 and the status-check table), TARGETS.md rows that are open, partial or blocked, and CATALOGUE.md classes A and B with the "confirm before starting" note. Skip found-solved and solved rows.` },
  { key: 'tomokiyo', prompt: `Read the repository's own CATALOG.md and LANDSCAPE.md, and the Cryptiana snapshot at sources/cryptiana/web/unsolved.htm (render with python3 tools/html2text.py). Harvest every item still marked open or partial after the corrections in LANDSCAPE.md. Also read sources/cryptiana/blog/index.html for any 2026 blog post naming a new unsolved item (Tomokiyo posts new items on the blog before the list).` },
  { key: 'web', prompt: `Use WebSearch (WebFetch may be blocked; if so say so in "blocked" and work from snippets) to find unsolved historical ciphers discussed in 2026 outside the standard lists: Cipherbrain (Klaus Schmeh) posts, Cipher Mysteries, r/codes posts about archival ciphers, HistoCrypt 2026 papers naming unsolved material, and any archive blog announcing a cipher they cannot read. Prefer items with images or transcriptions online.` },
  { key: 'archives', prompt: `Use WebSearch to find archival series described as containing undeciphered or "in cipher" letters with images online and keys or decipherments nearby, in these catalogues: TNA Discovery (SP 106 ciphers, SP 105 letter-books), PARES (Simancas Estado, "cifrada", "sin descifrar"), Gallica/BnF Archives et manuscrits ("chiffre", "chiffré" without "déchiffrement"), DECODE at de-crypt.org (non-decrypted records with a key attached). Report series, not just single letters, with what stands between a reader and the text.` },
]

phase('Harvest')
const harvested = await pipeline(
  HARVESTERS,
  h => agent(
    `Date: ${date}. You are one of five blind harvesters building a queue of unsolved historical ciphers this project could attempt next. Your source family: ${h.prompt}\n\nReturn every candidate you find with the fields in the schema, using the source's own status words. Do not judge feasibility; that is a later stage. List every file or URL you examined in "checked".`,
    { label: `harvest:${h.key}`, phase: 'Harvest', schema: CANDIDATES },
  ),
)
const raw = harvested.filter(Boolean)
const all = raw.flatMap(r => r.candidates.map(c => ({ ...c, source: r.source })))
log(`${raw.length}/${HARVESTERS.length} harvesters returned, ${all.length} raw candidates; blocked: ${raw.filter(r => r.blocked).map(r => r.source).join(', ') || 'none'}`)

phase('Filter')
const FILTERED = {
  type: 'object',
  properties: {
    kept: { type: 'array', items: { type: 'object', properties: {
      name: { type: 'string' }, shelfmark: { type: 'string' }, year: { type: 'string' }, language: { type: 'string' },
      material: { type: 'string' }, key_lead: { type: 'string' }, size: { type: 'string' },
      sources: { type: 'array', items: { type: 'string' } }, where: { type: 'string' },
      status_summary: { type: 'string', description: 'one line merging the sources\' statuses' },
    }, required: ['name', 'year', 'language', 'material', 'key_lead', 'sources', 'where', 'status_summary'] } },
    dropped: { type: 'array', items: { type: 'object', properties: { name: { type: 'string' }, reason: { type: 'string' } }, required: ['name', 'reason'] } },
  },
  required: ['kept', 'dropped'],
}
const filtered = await agent(
  `Date: ${date}. Here are ${all.length} raw candidates from five harvesters (JSON):\n${JSON.stringify(all, null, 1)}\n\nMerge duplicates (same letter or series under different names or shelfmarks) into one entry listing all its sources. Then DROP any candidate that is solved, read, found-solved or explained in either solver repository (check /tmp/cyphersolver/README.md and SOLVED_CATALOGUE.md, /tmp/unsolved-ciphers/TARGETS.md; clone them if absent) or in this repository's LANDSCAPE.md. Keep closed-negative and offline-only items: they are open, just blocked. Record every drop with its reason.`,
  { label: 'filter', phase: 'Filter', schema: FILTERED },
)
log(`${filtered.kept.length} kept, ${filtered.dropped.length} dropped as already solved or duplicate`)
const toScore = filtered.kept.slice(0, MAX)
if (filtered.kept.length > MAX) log(`Scoring only the first ${MAX} of ${filtered.kept.length}; raise args.max to score all`)

phase('Score')
const SCORE = {
  type: 'object',
  properties: {
    name: { type: 'string' },
    language_fit: { type: 'integer', minimum: 0, maximum: 3, description: `3 = plaintext in one of ${langs.join('/')}; 1 = other language readable with AI help; 0 = unknown script or language` },
    material: { type: 'integer', minimum: 0, maximum: 3, description: '3 = images or full transcription online free; 2 = printed figures; 1 = login needed; 0 = nothing online' },
    key_lead: { type: 'integer', minimum: 0, maximum: 3, description: '3 = key or decipherment located; 2 = sibling with decipherment; 1 = design known; 0 = nothing' },
    size: { type: 'integer', minimum: 0, maximum: 3, description: '3 = enough text or a key so a reading is checkable; 0 = below unicity with no key lead' },
    competition: { type: 'integer', minimum: 0, maximum: 3, description: '3 = nobody has it on a tracker; 1 = on a solver repo tracker as open; 0 = someone reports active work' },
    weight: { type: 'integer', minimum: 0, maximum: 3, description: 'historical interest of the content, 3 = decision of state or changes a known account' },
    next_step: { type: 'string', enum: ['archive-request', 'transcription', 'cryptanalysis', 'search-print', 'blocked'] },
    next_step_detail: { type: 'string', description: 'the single concrete action, with the shelfmark or URL' },
    rationale: { type: 'string' },
  },
  required: ['name', 'language_fit', 'material', 'key_lead', 'size', 'competition', 'weight', 'next_step', 'next_step_detail', 'rationale'],
}
const scored = await pipeline(
  toScore,
  c => agent(
    `Date: ${date}. Score this candidate for a single researcher who reads ${langs.join(' and ')} only, has no institutional archive access but can send copy requests and pay small fees, and works with AI agents that can transcribe and run solvers. Candidate (JSON):\n${JSON.stringify(c, null, 1)}\n\nUse the evidence given and, if needed, the two solver repositories under /tmp. Apply CLAUDE.md rule 1: if the material is a transcription only, say so in the rationale. Score every axis with the schema's definitions and name the single next step.`,
    { label: `score:${c.name.slice(0, 40)}`, phase: 'Score', schema: SCORE, effort: 'low' },
  ),
)
const ranked = scored.filter(Boolean).map(s => ({
  ...s,
  total: s.language_fit * 3 + s.material * 2 + s.key_lead * 3 + s.size * 2 + s.competition * 2 + s.weight,
})).sort((a, b) => b.total - a.total)
log(`${ranked.length} candidates scored; top: ${ranked.slice(0, 3).map(r => `${r.name} (${r.total})`).join('; ')}`)

phase('File')
const filed = await agent(
  `Date: ${date}. Write QUEUE.md at the repository root from this ranked list (JSON):\n${JSON.stringify(ranked, null, 1)}\n\nAnd this list of drops with reasons:\n${JSON.stringify(filtered.dropped, null, 1)}\n\nFormat: a short header stating the date, the scoring formula (language_fit x3 + material x2 + key_lead x3 + size x2 + competition x2 + weight, max 39) and the reader profile (${langs.join('/')} only, no archive access, copy requests possible). Then three tiers by total: A (28 and up), B (20 to 27), C (below 20), each a table with columns Rank, Target, Year, Lang, Next step, Detail, Total, Sources. Then a "Dropped this sweep" table with name and reason. Then a "Sources unreachable" line if any harvester reported a blocked source: ${JSON.stringify(raw.filter(r => r.blocked).map(r => r.source + ': ' + r.blocked))}. Keep existing entries' folder links if ciphers/<name> already exists (check with ls ciphers). Commit as "scout: refresh QUEUE.md, ${date}" without pushing. Return the counts per tier.`,
  { label: 'file', phase: 'File', schema: { type: 'object', properties: { tierA: { type: 'integer' }, tierB: { type: 'integer' }, tierC: { type: 'integer' } }, required: ['tierA', 'tierB', 'tierC'] } },
)
return { ...filed, scored: ranked.length, dropped: filtered.dropped.length }
