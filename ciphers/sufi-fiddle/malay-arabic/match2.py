#!/usr/bin/env python3
"""GAPS93 Malay and Arabic word-list match on ciphertext_fig1.txt (see PREREG.md in this folder).

Same statistic, null, control and gate as ../tausug/match.py (imported, not copied); only the lists change.
Usage: match2.py --leipzig MSA_SENTENCES_TXT --quran TANZIL_TXT2 [--perms 1000] [--seed 1] [--out results.json]
Sources (URLs in manifest.json) are fetched to a scratch dir; neither is committed.
"""
import argparse, json, os, random, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'tausug'))
from match import read_target, score, permute, render, skelset, CLASSES  # noqa: E402

AR = {'ب': 'b', 'ت': 't', 'ث': 's', 'ج': 'j', 'ح': 'h', 'خ': 'h', 'د': 'd', 'ذ': 'd', 'ر': 'r', 'ز': 's',
      'س': 's', 'ش': 's', 'ص': 's', 'ض': 'd', 'ط': 't', 'ظ': 'd', 'غ': 'N', 'ف': 'p', 'ق': 'k', 'ك': 'k',
      'ل': 'l', 'م': 'm', 'ن': 'n', 'ه': 'h', 'ة': 'h'}
AR_NONJOIN = set('اأإآدذرزوؤةء')


def ar_skel(w):
    return ''.join(AR.get(c, '') for c in w)


def leipzig(path):
    rows = [l.rstrip('\n').split('\t', 1) for l in open(path, encoding='utf-8') if '\t' in l]
    rows.sort(key=lambda r: int(r[0]))
    cut = int(len(rows) * 0.8)
    tok = lambda rs: [w for r in rs for w in re.findall(r"[^\W\d_]+", r[1])]
    # held-out words: x -> ks before render() (render maps one letter to one class; Tausug had no x)
    return tok(rows[:cut]), [w.lower().replace('x', 'ks') for w in tok(rows[cut:])]


def quran(path, first_held):
    lst, held = [], []
    for l in open(path, encoding='utf-8'):
        p = l.rstrip('\n').split('|')
        if len(p) != 3 or not p[0].isdigit():
            continue
        ws = re.findall(r'[ء-ي]+', re.sub(r'[ً-ْٰـ]', '', p[2]))
        (held if int(p[0]) >= first_held else lst).extend(ws)
    return lst, held


def ar_render(words, target_cons, nlines, rng, noise):
    flat, cons = [], 0
    for w in words:
        g = []
        for ch in w:
            c = AR.get(ch, '')
            if c:
                if noise and rng.random() < noise:
                    c = rng.choice([x for x in CLASSES if x != c])
                g.append(c)
                cons += 1
            if ch in AR_NONJOIN:
                flat.append(g)
                g = []
        flat.append(g)
        if cons >= target_cons:
            break
    per = max(1, len(flat) // nlines)
    return [flat[i:i + per] for i in range(0, len(flat), per)]


def run_list(name, S, held, rend, target, tcons, a, rng):
    r = {'n_skeletons': len(S), 'held_out_words': len(held)}
    for minlen, tag in ((3, 'C3'), (2, 'C2')):
        c, chosen, single, _ = score(target, S, minlen)
        nulls = sorted(score(permute(target, rng), S, minlen)[0] for _ in range(a.perms))
        r[tag] = {'target': round(c, 4), 'chosen_spans_by_L': chosen, 'singleton_matches_by_L': single,
                  'null_mean': round(sum(nulls) / len(nulls), 4), 'null_p95': round(nulls[int(.95 * len(nulls))], 4),
                  'p': sum(x >= c for x in nulls) / len(nulls)}
    ctrl = {}
    for noise in (0.0, 0.1, 0.2):
        vals = []
        for _ in range(a.chunks):
            off = rng.randrange(0, len(held) - 400)
            lines = rend(held[off:], tcons, 7, rng, noise)
            t = score(lines, S, 3)[0]
            ge = sum(score(permute(lines, rng), S, 3)[0] >= t for _ in range(a.ctrl_perms))
            vals.append((t, ge / a.ctrl_perms))
        ctrl[str(noise)] = {'C3_mean': round(sum(v[0] for v in vals) / len(vals), 4),
                            'power_p<0.05': sum(v[1] < 0.05 for v in vals) / len(vals)}
    r['positive_control_C3'] = ctrl
    pw = ctrl['0.2']['power_p<0.05']
    r['gate'] = 'PASS' if (r['C3']['p'] < 0.05 and pw >= 0.8) else ('NON-TEST (power<0.8 at 20pct)' if pw < 0.8 else 'FAIL')
    return r


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--leipzig', required=True)
    ap.add_argument('--quran', required=True)
    ap.add_argument('--perms', type=int, default=1000)
    ap.add_argument('--ctrl-perms', type=int, default=200)
    ap.add_argument('--chunks', type=int, default=20)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--out')
    a = ap.parse_args()
    rng = random.Random(a.seed)
    target = read_target()
    tcons = sum(len(g) for gs in target for g in gs if g)
    ms_list, ms_held = leipzig(a.leipzig)
    first_held = 91
    ar_list, ar_held = quran(a.quran, first_held)
    if len(ar_held) < 1000:
        first_held = 78
        ar_list, ar_held = quran(a.quran, first_held)
    res = {'target_consonants': tcons, 'seed': a.seed, 'quran_held_out_from_sura': first_held, 'lists': {}}
    res['lists']['L_MS_leipzig_msa_wiki2021'] = run_list('ms', skelset(ms_list), ms_held, render, target, tcons, a, rng)
    S_ar = {s for s in (ar_skel(w) for w in ar_list) if len(s) >= 2}
    res['lists']['L_AR_tanzil_1to%d' % (first_held - 1)] = run_list('ar', S_ar, ar_held, ar_render, target, tcons, a, rng)
    js = json.dumps(res, indent=1)
    print(js)
    if a.out:
        open(a.out, 'w').write(js + '\n')


if __name__ == '__main__':
    main()
