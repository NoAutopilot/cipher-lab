#!/usr/bin/env python3
"""MONL-ADH (15 Oct 2026): the pre-registered W:adhuc re-run (PREREG-MONL-ADH.md, part 1).

Usage: python3 adh_run.py [--check]

Replaces c268 L11:6-10 (K66 K49 ?h_bar K35 K15) by one W:adhuc token in the committed token stream (ciphertext_c268.tsv as it stood
at MONL-L11, i.e. without the W:adhuc change; if score_c268.py has since written W:adhuc, the five tokens are restored from its
pass_a column first; likewise the part-2 relabel L11:23 K12 is set back to K04) and runs align_c268.py's alignment. Matched control: every other window of 5 consecutive tokens within one line of
L11-L15, not overlapping L11:6-10 and holding no W: token, collapsed into one W: token the same way; gain = share - baseline.
Also align_c268.py's shuffled-clear control (200 draws, seed 140) on the W:adhuc stream. Writes results_adh.json; --check exits 1 when stale.
"""
import argparse, json, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import align_c268 as A  # noqa: E402

TARGET = ('L11', 6, 10)
ORIG = ['K66', 'K49', '?h_bar', 'K35', 'K15']


def base_tokens():
    toks = A.load_tokens()
    out = []
    for t in toks:
        if (t['line'], t['pos']) == ('L11', 6) and t['sign'] == 'W:adhuc':  # restore the pre-change stream
            for k, s in enumerate(ORIG):
                v = {r[0]: r[2] for r in (l.rstrip('\n').split('\t') for l in list(open(HERE / 'key.tsv', encoding='utf-8'))[1:])}.get(s)
                out.append({'line': 'L11', 'pos': 6 + k, 'sign': s, 'conf': 'M', 'value': A.fold(v) if v else None})
        elif (t['line'], t['pos']) == ('L11', 23) and t['sign'] == 'K12':  # the MONL-ADH sort relabel came after this run: pass A's K04
            out.append({**t, 'sign': 'K04', 'value': 'd'})
        elif (t['line'], t['pos']) == ('L11', 14) and t['sign'] == 'K12':  # the MONL-CTL sort relabel came after this run: K04
            out.append({**t, 'sign': 'K04', 'value': 'd'})
        elif (t['line'], t['pos']) == ('L06', 18) and t['sign'] == 'K12':  # the MONL-SORT2 relabel came after this run: K04
            out.append({**t, 'sign': 'K04', 'value': 'd'})
        elif int(t['line'][1:]) > 15:  # MONL-L16 (15 Oct 2026): L16-L20 came after this run; the run is on L01-L15
            continue
        elif (t['line'], t['pos']) == ('L15', 18) and t['sign'] == 'K11':  # MONL-L16 eye re-check came after this run: MONL-L11's K62
            v = {r[0]: r[2] for r in (l.rstrip('\n').split('\t') for l in list(open(HERE / 'key.tsv', encoding='utf-8'))[1:])}.get('K62')
            out.append({**t, 'sign': 'K62', 'value': A.fold(v) if v else None})
        else:
            out.append(t)
    got = [t['sign'] for t in out if t['line'] == 'L11' and 6 <= t['pos'] <= 10]
    assert got == ORIG, got
    return out


def collapse(toks, line, p1, p2, sign):
    out, done = [], False
    for t in toks:
        if t['line'] == line and p1 <= t['pos'] <= p2:
            if not done:
                out.append({'line': line, 'pos': p1, 'sign': sign, 'conf': 'M', 'value': None}); done = True
            continue
        out.append(t)
    return out


def share(toks, clear):
    _, path, _, _ = A.align(toks, clear)
    rows = A.classify(toks, clear, path)
    return A.stats(rows), rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    toks = base_tokens()
    words = A.load_clear()
    clear = ''.join(w[2] for w in words)
    base, _ = share(toks, clear)
    tt = collapse(toks, *TARGET, 'W:adhuc')
    tgt, rows = share(tt, clear)
    chunk = next(r['clear'] for r in rows if r['sign'] == 'W:adhuc')
    gain = round(tgt['confirm_share'] - base['confirm_share'], 4)
    # null: other 5-token windows within one line of L11-L15
    by_line = {}
    for t in toks:
        if t['line'] >= 'L11':
            by_line.setdefault(t['line'], []).append(t)
    null = []
    for ln, ts in sorted(by_line.items()):
        for i in range(len(ts) - 4):
            w = ts[i:i + 5]
            if any(x['sign'].startswith('W:') for x in w):
                continue
            if ln == 'L11' and not (w[-1]['pos'] < 6 or w[0]['pos'] > 10):
                continue
            s, _ = share(collapse(toks, ln, w[0]['pos'], w[-1]['pos'], 'W:window'), clear)
            null.append({'line': ln, 'p1': w[0]['pos'], 'p2': w[-1]['pos'], 'gain': round(s['confirm_share'] - base['confirm_share'], 4)})
    gains = sorted(x['gain'] for x in null)
    p95 = gains[int(0.95 * (len(gains) - 1))]
    ge = sum(g >= gain for g in gains)
    rng = random.Random(140)
    ws = [w[2] for w in words]
    shuf = []
    for _ in range(200):
        rng.shuffle(ws)
        shuf.append(share(tt, ''.join(ws))[0]['confirm_share'])
    shuf.sort()
    cw = set()
    pos = 0
    bounds = set([0])
    for w in words:
        pos += len(w[2]); bounds.add(pos)
    trow = next(r for r in rows if r['sign'] == 'W:adhuc')
    whole = bool(chunk) and trow['cpos'] in bounds and trow['cpos'] + len(chunk) in bounds
    keep = gain > p95 and ge <= 0.05 * len(gains) and sum(s >= tgt['confirm_share'] for s in shuf) == 0 and bool(chunk)
    res = {'baseline': base, 'w_adhuc': tgt, 'chunk': chunk, 'chunk_whole_words': whole, 'gain': gain,
           'null_windows': len(null), 'null_gain_mean': round(sum(gains) / len(gains), 4), 'null_gain_p95': p95,
           'null_gain_max': gains[-1], 'null_ge_gain': ge,
           'shuffled_clear': {'draws': 200, 'seed': 140, 'mean': round(sum(shuf) / len(shuf), 4), 'p95': shuf[int(0.95 * 199)],
                              'max': shuf[-1], 'ge_real': sum(s >= tgt['confirm_share'] for s in shuf)},
           'keep': keep, 'null': null,
           'w_adhuc_neighbourhood': [{k: r[k] for k in ('line', 'pos', 'sign', 'value', 'clear', 'kind')} for r in rows
                                     if r['line'] == 'L11' and r['pos'] <= 16]}
    out = json.dumps(res, indent=1, ensure_ascii=False) + '\n'
    f = HERE / 'results_adh.json'
    if a.check:
        ok = f.exists() and f.read_text(encoding='utf-8') == out
        print('adh_run: OK' if ok else 'adh_run: STALE'); sys.exit(0 if ok else 1)
    f.write_text(out, encoding='utf-8')
    print(json.dumps({k: v for k, v in res.items() if k not in ('null',)}, indent=1, ensure_ascii=False))


if __name__ == '__main__':
    main()
