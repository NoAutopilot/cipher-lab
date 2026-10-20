#!/usr/bin/env python3
"""MONL-C269C (20 Oct 2026): the generic span rule of PREREG-MONL-C269C.md for c269 (f.138v) bands against the ff.140r-141r clear text.

Usage: python3 span_rule.py --bands c269_reconciled.tsv,c269b_reconciled.tsv[,c269c_reconciled.tsv] [--band K] [--window-only]
       python3 span_rule.py --calib            (power and specificity checks on committed tokens, see PREREG)

Clear lines are numbered in reading order over clear_f140.tsv (f.140r L01 = 1 ... f.141r L11 = 67). One joint alignment
(align_c268.py's DP, scores and folds, key.tsv) of the concatenated stream of the given bands, against the clear letter after c268's
own aligned end (as align_c269.py), free start and end. For band K (default: the last given):
  prev_end   = clear line of the last clear letter taken by a band K-1 token in the joint alignment of bands 1..K-1 (band K NOT
               included: a first draft that let band K revise that end passed the wrong-band specificity check, --calib, before any
               L23-L33 data existed);
  indep_start = clear line of the first clear letter taken by a band K token when band K alone is aligned against the WHOLE clear
               letter (free start; score_c269.py's whole-letter span);
  PASS iff |indep_start - prev_end| <= 1.
--window-only: with bands 1..K-1 only, print the registered score window for band K: from (band K-1's joint end line - 1) to f.141r:L11.
Prints one JSON object; writes nothing.
"""
import argparse, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import align_c268 as A


def key():
    k = {}
    for l in list(open(HERE.parent / 'key.tsv', encoding='utf-8'))[1:]:
        f = l.rstrip('\n').split('\t'); k[f[0]] = f[2]
    return k


def band_tokens(path, band, k):
    ls = [l.rstrip('\n').split('\t') for l in open(path, encoding='utf-8')]
    h = ls[0]
    return [{'line': f[h.index('line')], 'pos': int(f[h.index('pos')]), 'sign': f[h.index('sign')], 'conf': f[h.index('conf')]
             if 'conf' in h else '', 'band': band,
             'value': A.fold(k[f[h.index('sign')]]) if k.get(f[h.index('sign')]) else None} for f in ls[1:] if f and f[0]]


def c268_tokens(lines, band, k):
    rows = [l.rstrip('\n').split('\t') for l in open(HERE.parent / 'ciphertext_c268.tsv', encoding='utf-8')][1:]
    return [{'line': f[0], 'pos': int(f[1]), 'sign': f[2], 'conf': f[3], 'band': band,
             'value': A.fold(k[f[2]]) if k.get(f[2]) else None} for f in rows if f[0] in lines]


def line_map():
    words = A.load_clear()
    order = []
    for w in words:
        lab = f'{w[0]}:{w[1]}'
        if lab not in order:
            order.append(lab)
    allrows = [l.split('\t')[:2] for l in list(open(HERE.parent / 'clear_f140.tsv', encoding='utf-8'))[1:]]
    num = {f'{p}:{l}': i + 1 for i, (p, l) in enumerate(allrows)}
    per = []
    for w in words:
        per += [f'{w[0]}:{w[1]}'] * len(w[2])
    return words, per, num


def c268_end(clear):
    _, _, _, end = A.align(A.load_tokens(), clear)
    assert clear[end - 13:end] == 'entendansquel', clear[end - 13:end]
    return end


def joint(toks, off_clear, off):
    _, path, _, _ = A.align(toks, off_clear)
    first, last = {}, {}
    for ti, a, b in path:
        if b > a:
            bd = toks[ti]['band']
            first.setdefault(bd, a + off); last[bd] = b - 1 + off
    return path, first, last


def indep_start(toks, clear):
    _, path, _, _ = A.align(toks, clear)
    for ti, a, b in path:
        if b > a:
            return a
    return None


def rule(bands_toks, K):
    words, per, num = line_map()
    clear = ''.join(w[2] for w in words)
    off = c268_end(clear)
    _, _, last = joint([t for bt in bands_toks[:K - 1] for t in bt], clear[off:], off)
    _, first, _ = joint([t for bt in bands_toks[:K] for t in bt], clear[off:], off)
    pe = num[per[last[K - 1]]]
    st = indep_start(bands_toks[K - 1], clear)
    lab = {v: k for k, v in num.items()}
    return {'band': K, 'prev_end': lab[pe], 'prev_end_n': pe, 'joint_start': lab[num[per[first[K]]]],
            'indep_start': lab[num[per[st]]], 'indep_start_n': num[per[st]], 'delta': num[per[st]] - pe,
            'pass': abs(num[per[st]] - pe) <= 1}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--bands'); ap.add_argument('--band', type=int); ap.add_argument('--window-only', action='store_true')
    ap.add_argument('--calib', action='store_true')
    a = ap.parse_args()
    k = key()
    if a.calib:
        # power: c268 L21-L30 after c268 L01-L20 (one leaf, true continuation); c269 L01-L10 after c268 L01-L30 needs c268 inside
        # the joint stream, so it is run on the whole clear letter (offset 0). Specificity: c268 L01-L10 placed after c269 L01-L10.
        words, per, num = line_map(); lab = {v: kk for kk, v in num.items()}
        clear = ''.join(w[2] for w in words)
        out = {}
        for name, b1, b2 in (
                ('power_c268_L21-30_after_L01-20', c268_tokens({f'L{i:02d}' for i in range(1, 21)}, 1, k),
                 c268_tokens({f'L{i:02d}' for i in range(21, 31)}, 2, k)),
                ('power_c269_L01-10_after_c268', c268_tokens({f'L{i:02d}' for i in range(1, 31)}, 1, k),
                 band_tokens(HERE / 'c269_reconciled.tsv', 2, k)),
                ('wrong_c268_L01-10_after_c269_L01-10', band_tokens(HERE / 'c269_reconciled.tsv', 1, k),
                 c268_tokens({f'L{i:02d}' for i in range(1, 11)}, 2, k))):
            _, _, last = joint(b1, clear, 0)
            pe = num[per[last[1]]]; st = num[per[indep_start(b2, clear)]]
            out[name] = {'prev_end': lab[pe], 'indep_start': lab[st], 'delta': st - pe, 'pass': abs(st - pe) <= 1}
        out['chance_uniform_start'] = round(3 / len(num), 4)
        print(json.dumps(out)); return
    files = a.bands.split(',')
    bt = [band_tokens(HERE / f, i + 1, k) for i, f in enumerate(files)]
    if a.window_only:
        words, per, num = line_map(); lab = {v: kk for kk, v in num.items()}
        clear = ''.join(w[2] for w in words); off = c268_end(clear)
        _, first, last = joint([t for b in bt for t in b], clear[off:], off)
        pe = num[per[last[len(bt)]]]
        print(json.dumps({'next_band': len(bt) + 1, 'prev_end': lab[pe], 'window': f'{lab[pe - 1]}-f.141r:L11'})); return
    print(json.dumps(rule(bt, a.band or len(bt))))


if __name__ == '__main__':
    main()
