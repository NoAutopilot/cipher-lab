#!/usr/bin/env python3
"""settle_f41r.py -- f.41r default-flag settlement (RUN3-ES41, 4 Oct 2026; rule in PREREG_f41r_settle.md, pushed 367f3428 first).

--build   writes run2/settle_f41r_items.tsv (what the blind Opus reader sees) and run2/settle_f41r_itemkey.tsv (unit/decoy map, not shown).
--apply   reads run2/settle_f41r_reads.tsv (id, choice 1|2|other, tokens, conf high|low), scores the decoy control, and writes
          ciphertext_f41r.tsv from ciphertext_f41r_pre.tsv (control PASS) or the _pre stream unchanged (control FAIL), plus
          f41r_settle_result.json and run2/f41r_settled.tsv.
--check   both steps' outputs regenerate byte-identically, else exit 1.
"""
import sys, re, json, random
from pathlib import Path
HERE = Path(__file__).resolve().parent
IMG = HERE / 'images'
SUBS = [(r'^21(?=\D|$)', '11'), (r'^11(?=\D|$)', '21'), (r'^12(?=\D|$)', '22'), (r'^22(?=\D|$)', '12'), (r'^14(?=\D|$)', '11'),
        (r'^20(?=\D|$)', '10'), (r'^10(?=\D|$)', '20'), (r'^13(?=\D|$)', '23'), (r'^23(?=\D|$)', '13'), (r'^24(?=\D|$)', '249'),
        ('ρ', 'σ'), ('σ', 'ρ'), (r'\+', ''), (r'\.', '+'), (r'^(\d+)(?=@|$)', r'\1+')]


def tsv(p):
    rows = [l.split('\t') for l in p.read_text(encoding='utf-8').splitlines() if l and not l.startswith('#')]
    return [dict(zip(rows[0], r + [''] * (len(rows[0]) - len(r)))) for r in rows[1:]]


def stream(p):
    return {l.split('\t')[0]: l.split('\t')[1].split() if '\t' in l else []
            for l in p.read_text(encoding='utf-8').splitlines() if l and not l.startswith('#')}


def decoy(t):
    for pat, rep in SUBS:
        d = re.sub(pat, rep, t, count=1)
        if d != t: return d
    return t + '+'


def crops(ln, pos, n):
    f = pos / max(1, n)
    s = ['s1'] if f < 0.4 else ['s2'] if f > 0.6 else ['s1', 's2']
    return ' '.join(f'images/f41r_{ln}_{x}.jpg' for x in s)


def build():
    pre = stream(HERE / 'ciphertext_f41r_pre.tsv')
    clean = lambda ts: ' '.join(t.rstrip('?') for t in ts) or '(line edge)'
    items = []
    for i, u in enumerate(tsv(HERE / 'run2/f41r_units.tsv')):
        ln, st, n = u['line'], int(u['start']), int(u['len'])
        items.append(dict(kind='unit', ref=f"U{i + 1:02d}", line=ln, st=st, n=n, o=[u['A'], u['B']]))
    firm = [f for f in tsv(HERE / 'run2/f41r_firm.tsv') if re.match(r'^\d', f['token']) and not re.match(r'^([4-9]\d|3[89]|\d{3})', f['token'])]
    for j, f in enumerate(sorted(random.Random(41).sample(firm, 20), key=lambda f: (f['line'], int(f['idx'])))):
        items.append(dict(kind='decoy', ref=f"D{j + 1:02d}", line=f['line'], st=int(f['idx']), n=1, o=[f['token'], decoy(f['token'])]))
    rng = random.Random(4141)
    rng.shuffle(items)
    out = ['id\tline\tcrops\tbefore\tafter\toption1\toption2']
    key = ['id\tkind\tref\tline\tstart\tlen\toption1\toption2']
    for k, it in enumerate(items):
        ln, st, n = it['line'], it['st'], it['n']
        o = it['o'][:] if rng.random() < 0.5 else it['o'][::-1]
        toks = pre.get(ln, [])
        show = lambda s: '(nothing)' if s == '-' else s
        out.append('\t'.join([f'I{k + 1:02d}', ln, crops(ln, st + n / 2, len(toks)), clean(toks[max(0, st - 3):st]),
                              clean(toks[st + n:st + n + 3]), show(o[0]), show(o[1])]))
        key.append('\t'.join(map(str, [f'I{k + 1:02d}', it['kind'], it['ref'], ln, st, n, o[0], o[1]])))
    return {'run2/settle_f41r_items.tsv': '\n'.join(out) + '\n', 'run2/settle_f41r_itemkey.tsv': '\n'.join(key) + '\n'}


def apply():
    key = {r['id']: r for r in tsv(HERE / 'run2/settle_f41r_itemkey.tsv')}
    units = tsv(HERE / 'run2/f41r_units.tsv')
    reads = {r['id']: r for r in tsv(HERE / 'run2/settle_f41r_reads.tsv')}
    pick = lambda r, k: (k['option1'] if r['choice'] == '1' else k['option2'] if r['choice'] == '2' else None)
    ctl = dict(firm_high=0, decoy_high=0, firm_low=0, decoy_low=0, other=0, missing=0, n=0)
    for i, k in key.items():
        if k['kind'] != 'decoy': continue
        ctl['n'] += 1; r = reads.get(i)
        if not r: ctl['missing'] += 1; continue
        p = pick(r, k)
        if p is None: ctl['other'] += 1; continue
        is_firm = p == _firm_token(k)
        ctl[('firm_' if is_firm else 'decoy_') + ('high' if r['conf'] == 'high' else 'low')] += 1
    ok = ctl['firm_high'] >= 18 and ctl['decoy_high'] <= 1
    pre = stream(HERE / 'ciphertext_f41r_pre.tsv')
    new = {ln: list(ts) for ln, ts in pre.items()}
    rows, tally = ['id\tunit\tline\tstart\tA\tB\tchoice\tconf\tresult\trule'], {}
    unit_items = sorted((k for k in key.values() if k['kind'] == 'unit'), key=lambda k: (k['line'], -int(k['start'])))
    for k in unit_items:
        r = reads.get(k['id']); u = units[int(k['ref'][1:]) - 1]
        st, n = int(k['start']), int(k['len'])
        if not r: res, rule = None, 'none'
        else:
            p = pick(r, k)
            if p is None: res, rule = [t + '?' for t in r['tokens'].split()], 'S3'
            elif r['conf'] == 'high': res, rule = ([] if p == '-' else p.split()), 'S1'
            else: res, rule = ([] if p == '-' else [t + '?' for t in p.split()]), 'S2'
        side = '' if not r else ('A' if r and pick(r, k) == u['A'] else 'B' if r and pick(r, k) == u['B'] else 'other')
        tally[rule] = tally.get(rule, 0) + 1; tally['side_' + (side or 'none')] = tally.get('side_' + (side or 'none'), 0) + 1
        if ok and res is not None: new[k['line']][st:st + n] = res
        rows.append('\t'.join([k['id'], k['ref'], k['line'], str(st), u['A'], u['B'], r['choice'] if r else '', r['conf'] if r else '',
                               ' '.join(res) if res is not None else '(unchanged)', rule]))
    hdr = [l for l in (HERE / 'ciphertext_f41r_pre.tsv').read_text(encoding='utf-8').splitlines() if l.startswith('#')]
    hdr.append('# Default-flag settlement RUN3-ES41 (4 Oct 2026, PREREG_f41r_settle.md, settle_f41r.py): ' +
               (f"applied; control PASS {ctl['firm_high']}/20 firm-high, {ctl['decoy_high']}/20 decoy-high" if ok else
                f"NOT applied (control FAIL {ctl['firm_high']}/20 firm-high, {ctl['decoy_high']}/20 decoy-high); stream = _pre"))
    body = [ln + '\t' + ' '.join(new[ln]) for ln in sorted(new)]
    nq = lambda s: sum(t.endswith('?') for ts in s.values() for t in ts)
    res = dict(prereg='PREREG_f41r_settle.md', control=ctl, control_gate='PASS' if ok else 'FAIL', applied=ok, units=len(unit_items),
               tally=dict(sorted(tally.items())), tokens_pre=sum(map(len, pre.values())), tokens_after=sum(map(len, new.values())),
               flagged_pre=nq(pre), flagged_after=nq(new))
    return {'ciphertext_f41r.tsv': '\n'.join(hdr + body) + '\n', 'run2/f41r_settled.tsv': '\n'.join(rows) + '\n',
            'f41r_settle_result.json': json.dumps(res, indent=1, ensure_ascii=False) + '\n'}


def _firm_token(k):
    """The decoy item's firm token: the one present at that position in the pre stream."""
    pre = stream(HERE / 'ciphertext_f41r_pre.tsv')
    return pre[k['line']][int(k['start'])]


def main():
    outs = {}
    if '--build' in sys.argv or '--check' in sys.argv: outs.update(build())
    if ('--apply' in sys.argv or '--check' in sys.argv) and (HERE / 'run2/settle_f41r_reads.tsv').exists(): outs.update(apply())
    if '--check' in sys.argv:
        stale = [f for f, s in outs.items() if not (HERE / f).exists() or (HERE / f).read_text(encoding='utf-8') != s]
        print('stale:' if stale else 'OK: committed outputs match', *stale); sys.exit(1 if stale else 0)
    for f, s in outs.items(): (HERE / f).write_text(s, encoding='utf-8')
    print(*outs, sep='\n')
    if 'f41r_settle_result.json' in outs: print(outs['f41r_settle_result.json'])


if __name__ == '__main__':
    main()
