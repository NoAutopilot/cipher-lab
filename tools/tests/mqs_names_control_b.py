#!/usr/bin/env python3
"""MQS-NAMES control (b): Eckert 1864 cipher-book person code words (English, H), under tools/name_candidates.py.
Pre-registered in tools/tests/PREREG-MQS-NAMES.md, "Amendment 1" (pushed before this script's 'score' ran).

  python3 tools/tests/mqs_names_control_b.py freeze   # sample codes, build masked OR index pages, freeze one pool per code
  python3 tools/tests/mqs_names_control_b.py score    # score from the frozen pools -> fixtures/name_candidates/eckert/

Contexts: ciphers/eckert-1864 md-blocks readings through tools/holder_export.py's MdBlocks (read-only), neighbours
rendered by their meanings. Index: the Official Records volumes cached in sources/ia-fulltext/print-check/, split into
pages; MASK: every page sharing >= 2 folded word 4-grams with the decoded text of ANY telegram that carries the tested
code (the OR prints those telegrams in clear). The pool never takes names from the folder's key.md (the cipher book)."""
import gzip, glob, json, os, random, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import name_candidates as nc  # noqa: E402

ECK = os.path.join(ROOT, 'ciphers', 'eckert-1864')
OUT = os.path.join(ROOT, 'tools', 'tests', 'fixtures', 'name_candidates', 'eckert')
SCR = os.environ.get('MQS_SCRATCH') or '/tmp/mqs_names_eckert_pages'  # page split: regenerated, never committed
OR = sorted(glob.glob(os.path.join(ROOT, 'sources', 'ia-fulltext', 'print-check', 'warofrebellion*_djvu.txt.gz')) +
            glob.glob(os.path.join(ROOT, 'sources', 'ia-fulltext', 'print-check', 'officialrecordso*_djvu.txt.gz')))
PERSON = re.compile(r'^([A-Z][a-z]+)(?: [A-Z]{1,2}){1,3}$')  # the cipher book's "Grant U S", "Porter D D"
N_SAMPLE, SEED, NULLS = 10, 1, 100


def contexts():
    return nc.contexts_from_mdblocks(ECK, width=8)


def meanings():
    """code word -> meaning, from the md-blocks tokens (used only to pick person codes and their truth; never pooled)."""
    import importlib.util
    from pathlib import Path
    spec = importlib.util.spec_from_file_location('holder_export', os.path.join(ROOT, 'tools', 'holder_export.py'))
    md = importlib.util.module_from_spec(spec); spec.loader.exec_module(md)
    mb = md.MdBlocks(Path(ECK))
    out, text = {}, {}
    for iid in mb.items:
        toks = mb.tokens(iid)
        text[iid] = ' '.join(t[2] for t in toks if t[3] in ('H', 'C', 'S', 'M') and t[2])
        for _, w, m, g, k in toks:
            if k == 'word' and g in ('H', 'C'):
                out.setdefault(w, m)
    return out, text


def sample():
    ctx = contexts()
    mean, _ = meanings()
    persons = sorted(w for w, m in mean.items() if PERSON.match(m) and len(ctx.get(w, [])) >= 2)
    rng = random.Random(SEED)
    return persons, sorted(rng.sample(persons, min(N_SAMPLE, len(persons))))


def grams(s):
    w = [nc.fold(x) for x in re.findall(r'[A-Za-z]+', s)]
    w = [x for x in w if x]
    return {' '.join(w[i:i + 4]) for i in range(len(w) - 3)}


def pages():
    out = []
    for p in OR:
        t = gzip.open(p, 'rt', encoding='utf-8', errors='replace').read()
        for i, pg in enumerate(t.split('\x0c')):
            if len(pg) > 200:
                out.append((os.path.basename(p).split('_djvu')[0], i, pg))
    return out


def write_index(code, ctx, text, all_pages):
    letters = {x['letter'] for x in ctx[code]}
    g = set().union(*(grams(text[l]) for l in letters)) if letters else set()
    os.makedirs(SCR, exist_ok=True)
    man = os.path.join(SCR, f'index_{code}.tsv')
    kept = masked = 0
    with open(man, 'w') as f:
        f.write('path\tletters\tdate\n')
        for vol, i, pg in all_pages:
            hit = len(grams(pg) & g) >= 2
            fp = os.path.join(SCR, 'pages', f'{vol}_{i:04d}.txt')
            if not os.path.exists(fp):
                os.makedirs(os.path.dirname(fp), exist_ok=True)
                open(fp, 'w').write(pg)
            f.write(f'{fp}\t{"MASKED" if hit else ""}\t1864\n')
            masked += hit; kept += not hit
    return man, kept, masked


def argv_for(code, mean, man, extra):
    sur = PERSON.match(mean[code]).group(1)
    return [ECK, '--code', code, '--mdblocks', '--lang', 'en', '--date', '1864-06-01', '--sender', 'Eckert telegrams',
            '--recipient', 'Eckert telegrams', '--index', man, '--mask-letters', 'MASKED', '--truth', sur] + extra


def freeze():
    persons, codes = sample()
    ctx = contexts()
    mean, text = meanings()
    allp = pages()
    res = dict(n_person_codes_n2=len(persons), sample=codes, pools={})
    for c in codes:
        man, kept, masked = write_index(c, ctx, text, allp)
        r = nc.run(nc.parser().parse_args(argv_for(c, mean, man, ['--freeze-pool', os.path.join(OUT, f'pool_{c}.tsv'),
                                                                    '--freeze-only'])))
        res['pools'][c] = dict(sha256=r['pool_sha'], pool=r['pool'], pages_kept=kept, pages_masked=masked,
                               n_contexts=len(ctx[c]))
        print(c, r['pool'], r['pool_sha'], kept, masked)
    json.dump(res, open(os.path.join(OUT, 'pools.json'), 'w'), indent=1)


def score():
    pj = json.load(open(os.path.join(OUT, 'pools.json')))
    mean, _ = meanings()
    rows = []
    for c in pj['sample']:
        man = os.path.join(SCR, f'index_{c}.tsv')
        s = nc.run(nc.parser().parse_args(argv_for(c, mean, man, ['--pool', os.path.join(OUT, f'pool_{c}.tsv'),
                                                                   '--nulls', str(NULLS)])))['summary']
        cn = s['context_null'] or {}
        rows.append([c, mean[c], s['n_contexts'], s['pool'], s['coverage'], s['truth_rank'], s['truth_score'],
                     cn.get('p95_score'), s['beats_null_p95'], (s['decoy_null'] or {}).get('decoy_beat_share'),
                     ' | '.join(s['top'][:5])])
    with open(os.path.join(OUT, 'control_b.tsv'), 'w') as f:
        f.write('code\tmeaning\tn_contexts\tpool\tcoverage\ttruth_rank\ttruth_score\tnull_p95\tbeats_p95\t'
                'decoy_beat_share\ttop5\n')
        for r in rows:
            f.write('\t'.join(str(x) for x in r) + '\n')
            print('\t'.join(str(x) for x in r))
    passed = sum(1 for r in rows if r[4] and r[5] and r[5] <= 5 and r[8])
    print(f'gate: {passed}/{len(rows)} person codes covered, top 5 and above own null p95 (gate >= 5)')


if __name__ == '__main__':
    {'freeze': freeze, 'score': score}.get(sys.argv[1] if len(sys.argv) > 1 else '', lambda: print(__doc__))()
