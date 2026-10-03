#!/usr/bin/env python3
"""F36-GLOSS (3 Oct 2026): align the clerk's interlinear gloss of fr.3252 f.36-37 (Opus eye read, two blind passes,
reconciled in gloss_recon.tsv) to the reconciled sign transcription (../f36/passD.tsv, F36-READ) with
tools/interlinear_align.py, giving a C-grade sign -> letter key from the period decipherment, with a shuffled-gloss
control per leaf (CLAUDE.md rule 3, merge paragraph).

  python3 align_f36.py            # writes pairs.tsv, align.tsv, ../../keys/key_ceppo_f36_clerk.tsv, control.tsv, conflicts.tsv
  python3 align_f36.py --check    # exit 1 if any committed output is stale (rule 7)

Line pairing: f.36v and f.37r gloss lines pair with the passD lines of the same name. f.36r: the gloss crops were cut on
re-centred lines r36n_L01-L14 (cut_gloss.py) while passD carries HARVEST-D's 15-row grid r36_L01-L15, which drifts from
about L08; each r36n gloss line is paired with the passD r36 line (same index or +1) whose printed-key decode is closer to
it (difflib ratio), and the chosen map is written to pairs.tsv. The printed key is used only to pair lines, never to set a
sign's value; the control uses the same pairing.
Unsettled signs ('?' in passD) become unique codes @U<n> (each takes 0-1 gloss letter, never counted). '?' in the gloss is
the wildcard. Statistic per leaf: share of aligned settled-sign tokens whose letter equals the sign's majority letter over
the whole letter (status 'agrees'), and share whose letter equals the printed Ceppo-Nevers value (a known-answer check:
the printed key is control-backed on this letter, F36-READ); control: the same with gloss lines shuffled among that leaf's cipher lines (200 seeds).
"""
import csv, difflib, json, random, subprocess, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / 'tools'))
import interlinear_align as IA  # noqa: E402

MAP = ROOT / 'ciphers/ceppo-nevers-fr3251-1570s/harvest/sign_id_map.json'
PASSD = HERE.parent / 'f36' / 'passD.tsv'
GLOSS = HERE / 'gloss_recon.tsv'
KEYOUT = HERE.parents[1] / 'keys' / 'key_ceppo_f36_clerk.tsv'
KW = dict(floor=0, code_prefix='@', null_cost=0.0, wildcard='?')


def printed():
    m = {e['id']: e['value'] for e in json.load(open(MAP))}
    m['X_THETA2'] = 'r'
    return m


def leaf(line):
    return 'f37r' if line.startswith('r37') else ('f36v' if line.startswith('v36') else 'f36r')


def build_pairs():
    sig = defaultdict(list)
    for r in csv.DictReader(open(PASSD), delimiter='\t'):
        sig[r['passage']].append(r['sign_id'])
    gl = {r['line']: r['gloss'] for r in csv.DictReader(open(GLOSS), delimiter='\t')}
    m = printed()
    dec = {k: ''.join(m.get(s, '?') if m.get(s) not in ('null', 'et') else '' for s in v) for k, v in sig.items()}
    pairs, used = [], set()
    for g, text in gl.items():
        if g.startswith('r36n'):
            i = int(g[-2:]); cands = [f'r36_L{j:02d}' for j in (i, i + 1) if f'r36_L{j:02d}' in sig and f'r36_L{j:02d}' not in used]
            flat = text.replace(' ', '')
            c = max(cands, key=lambda k: difflib.SequenceMatcher(None, flat, dec[k]).ratio())
        else:
            c = g
        used.add(c)
        n = 0; toks = []
        for s in sig[c]:
            if s == '?':
                n += 1; toks.append(f'@U{c}_{n}')
            else:
                toks.append('@' + s)
        pairs.append({'plain_line': g, 'plain_raw': text, 'cipher_line': c, 'cipher_raw': ' '.join(toks)})
    return pairs


PRINTED = None


def stat(pairs):
    prepared, results, counts, shown = IA.run_align(pairs, **KW)
    rows = IA.token_rows(prepared, results, counts, shown)
    per = defaultdict(Counter)
    for r in rows:
        if r[4].startswith('U') or r[3] != 'code' or not r[6] or r[6] == '?':
            continue
        per[leaf(r[0])]['n'] += 1
        per[leaf(r[0])]['agree'] += r[7] == 'agrees'
        pv = PRINTED.get(r[4])
        if pv and pv not in ('null', 'et'):
            per[leaf(r[0])]['pn'] += 1
            per[leaf(r[0])]['pagree'] += IA.fold(pv) == IA.fold(r[6])
    return rows, counts, shown, per


def main(check=False):
    global PRINTED
    PRINTED = printed()
    pairs = build_pairs()
    rows, counts, shown, per = stat(pairs)
    m = printed()
    out = {}
    out['pairs.tsv'] = ['plain_line\tplain_raw\tcipher_line\tcipher_raw'] + ['\t'.join(p[k] for k in ('plain_line', 'plain_raw', 'cipher_line', 'cipher_raw')) for p in pairs]
    out['align.tsv'] = ['cipher_line\tidx\traw\tkind\tvalue\trepair\tplain_chunk\tstatus'] + ['\t'.join(map(str, r)) for r in rows]
    key = ['sign\tclerk\tn\tagree\tothers\tprinted\tgrade\tnote']
    conf = ['sign\tclerk\tn\tagree\tprinted\tkind']
    for v in sorted(k for k in counts if not str(k).startswith('U')):
        cnt = counts[v]; top, topn = IA.top_of(cnt); n = sum(cnt.values())
        others = ','.join(f'{a}:{b}' for a, b in sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[1:])
        pv = m.get(v, '-')
        grade = 'C' if topn >= 2 and topn / n >= 0.6 else 'M'
        note = 'fills a sign the printed table lacks' if pv in ('-', 'null') else ('agrees with printed' if IA.fold(pv) == top else 'CONFLICT with printed')
        key.append(f'{v}\t{top}\t{n}\t{topn}\t{others}\t{pv}\t{grade}\t{note}')
        if pv not in ('-',) and IA.fold(pv) != top and grade == 'C':
            conf.append(f'{v}\t{top}\t{n}\t{topn}\t{pv}\t' + ('printed null' if pv == 'null' else 'value'))
    # control: shuffle gloss lines among the same leaf's cipher lines
    ctl = ['leaf\tstatistic\treal_n\treal_k\treal_share\tshuf_mean\tshuf_p95\tshuf_max\tgate']
    by = defaultdict(list)
    for i, p in enumerate(pairs):
        by[leaf(p['cipher_line'])].append(i)
    shuf = defaultdict(list)
    for seed in range(200):
        rnd = random.Random(seed); sp = [dict(p) for p in pairs]
        for lf, idx in by.items():
            texts = [pairs[i]['plain_raw'] for i in idx]
            perm = texts[:]
            while len(perm) > 1 and perm == texts:
                rnd.shuffle(perm)
            for i, t in zip(idx, perm):
                sp[i]['plain_raw'] = t
        _, _, _, ps = stat(sp)
        for lf in by:
            shuf[(lf, 'self')].append(ps[lf]['agree'] / max(1, ps[lf]['n']))
            shuf[(lf, 'printed')].append(ps[lf]['pagree'] / max(1, ps[lf]['pn']))
    for lf in sorted(by):
        for stn, k, n in (('self', 'agree', 'n'), ('printed', 'pagree', 'pn')):
            s = sorted(shuf[(lf, stn)]); real = per[lf][k] / max(1, per[lf][n])
            p95 = s[int(0.95 * len(s)) - 1]
            ctl.append(f"{lf}\t{stn}\t{per[lf][n]}\t{per[lf][k]}\t{real:.3f}\t{sum(s)/len(s):.3f}\t{p95:.3f}\t{s[-1]:.3f}\t{'PASS' if real > s[-1] else ('above p95' if real > p95 else 'TIE/FAIL')}")
    out['control.tsv'] = ctl
    out['conflicts.tsv'] = conf
    files = {HERE / k: v for k, v in out.items()}
    files[KEYOUT] = key
    stale = []
    for p, lines in files.items():
        txt = '\n'.join(lines) + '\n'
        if check:
            if not p.exists() or p.read_text() != txt:
                stale.append(p.name)
        else:
            p.parent.mkdir(exist_ok=True); p.write_text(txt)
    if check:
        print('stale: ' + ', '.join(stale) if stale else 'ok'); sys.exit(1 if stale else 0)
    print('\n'.join(ctl)); print(len(key) - 1, 'signs in key;', len(conf) - 1, 'C conflicts with printed')


if __name__ == '__main__':
    main('--check' in sys.argv)
