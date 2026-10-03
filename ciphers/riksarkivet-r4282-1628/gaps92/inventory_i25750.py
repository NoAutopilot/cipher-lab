#!/usr/bin/env python3
"""GAPS92: R4284 image I25750 LEFT page (letter cipher, Bourdeau "ignored") -- reconciled transcription and its
sign inventory vs R4282's 34 reconciled labels (GAPS38). Disk only, no reading.

Inputs: passA_opus.tsv, passB_opus.tsv (two blind Opus passes on lc_L01-L07, prompt_pass.md), rec/ (reconcile_passes),
../tx2/ciphertext_reconciled.tsv (R4282), ../r4284_leaf/passC_reconciled.tsv (R4284 key-test strip), ../gaps89/results.json.
Settlements (GAPS92 reconciliation from the crops, one look): the 4 slots A=8/B=6 (L03 31, L05 21, L06 26, L07 5) are one
small sideways-loop sign, the shape R4282's transcriptions label 8 ("hM8L" p1_L02, "f38bga" p1_L07) -> 8; L07 col 14 A=9 /
B=z3 is a ʒ-like 3 -> z3; A's kappa = B's k (small k without ascender) -> k; fheavy = fbar (first cipher sign, L01) -> f.
Label map to R4282's convention (Bourdeau's R4282 header / GAPS38): lambda L, delta T, sqx B, eps E, phi F, alpha A, mu M,
d D (R4282 has no plain d; its D is the looped-ascender d), z3 3, longs S (R4282's S is the long s; first run mapped it to f, corrected after the 4-gram check showed 3 f/S splits), fbar/fheavy f, kappa k; y^m -> y + mark (^).
Statistic: shared labels, share of R4282 tokens they cover, share of the page's tokens inside R4282's inventory, and
cosine of the two unigram profiles. Controls that can differ on it (from GAPS89): R4284 numeric body 5 labels (19.5%),
R4284 key-test strip 11 labels (35.5%), 4307 p.4 16 labels. --check exits non-zero if results.json is stale.
"""
import csv, json, math, os, re, sys, collections, random, gzip
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(H)
SETTLE = {('L03', 31): '8', ('L05', 21): '8', ('L06', 26): '8', ('L07', 5): '8', ('L07', 14): 'z3'}
MAP = {'lambda': 'L', 'delta': 'T', 'sqx': 'B', 'eps': 'E', 'phi': 'F', 'alpha': 'A', 'mu': 'M', 'd': 'D', 'z3': '3',
       'longs': 'S', 'fbar': 'f', 'fheavy': 'f', 'kappa': 'k', '6': '8'}

def norm(s):
    s = s.split('^')[0]
    return MAP.get(s, s)

def page_tokens():
    out = []
    for r in csv.DictReader(open(os.path.join(H, 'rec/ciphertext_draft.tsv')), delimiter='\t'):
        key = (r['line'], int(r[[k for k in r if k in ('col', 'pos', 'position')][0]]))
        s = SETTLE.get(key, r['sign'])
        if s in ('/', '.', '-', '') or s.startswith('[clear'):
            continue
        out.append(norm(s))
    return out

def cos(a, b):
    ks = set(a) | set(b)
    return sum(a[k] * b[k] for k in ks) / math.sqrt(sum(v * v for v in a.values()) * sum(v * v for v in b.values()))

def main():
    pg = collections.Counter(page_tokens())
    r82 = collections.Counter(r['sign'] for r in csv.DictReader(open(os.path.join(P, 'tx2/ciphertext_reconciled.tsv')), delimiter='\t') if r['sign'] != '^')
    strip = collections.Counter()
    for r in csv.DictReader(open(os.path.join(P, 'r4284_leaf/passC_reconciled.tsv')), delimiter='\t'):
        for s in r['codes'].split():
            if s != '/':
                strip[s] += 1
    n82, npg = sum(r82.values()), sum(pg.values())
    sh = sorted(set(pg) & set(r82))
    g89 = json.load(open(os.path.join(P, 'gaps89/results.json')))
    res = {
        'page': {'tokens': npg, 'labels': len(pg), 'inventory': dict(pg.most_common())},
        'vs_r4282': {'shared_labels': sh, 'n_shared': len(sh), 'of_r4282_labels': len(r82),
                     'r4282_tokens_covered': sum(r82[l] for l in sh), 'r4282_coverage': round(sum(r82[l] for l in sh) / n82, 4),
                     'page_tokens_in_r4282_inventory': round(sum(pg[l] for l in sh) / npg, 4),
                     'page_labels_not_in_r4282': sorted(set(pg) - set(r82)),
                     'r4282_labels_absent_from_page': sorted(set(r82) - set(pg)),
                     'capitals_reached': sorted(l for l in sh if l.isupper()),
                     'unigram_cosine': round(cos(pg, r82), 4)},
        'controls': {'r4284_keytest_strip': {'n_shared': g89['control_r4284_keytest_strip']['n_shared'],
                                             'r4282_coverage': g89['control_r4284_keytest_strip']['r4282_coverage'],
                                             'unigram_cosine': round(cos(strip, r82), 4)},
                     'r4284_numeric_body': {'n_shared': g89['r4284_body']['vs_r4282_glyph_level']['n_shared'],
                                            'r4282_coverage': g89['r4284_body']['vs_r4282_glyph_level']['r4282_coverage']},
                     '4307p4': '16 shared signs / 456 tokens (GAPS3)'},
    }
    # Calibration (seed 92, 2,000 draws each, N = the page's token count): ceiling = R4282 contiguous windows vs the rest of
    # R4282 (same text, same sign system); letter-shape null = la17 Latin plaintext windows (labels read as letters) vs R4282.
    rng = random.Random(92)
    seq = [r['sign'] for r in csv.DictReader(open(os.path.join(P, 'tx2/ciphertext_reconciled.tsv')), delimiter='\t') if r['sign'] != '^']
    la = re.sub('[^a-z]', '', gzip.open(os.path.join(P, '../../tools/data/la17/epistolaecelebe00grotgoog.txt.gz'), 'rt', errors='ignore').read().lower().replace('j', 'i').replace('v', 'u'))
    def q(xs):
        xs = sorted(xs); return {'mean': round(sum(xs) / len(xs), 4), 'p05': round(xs[int(.05 * len(xs))], 4), 'p95': round(xs[int(.95 * len(xs))], 4)}
    ceil, null = [], []
    for _ in range(2000):
        i = rng.randrange(len(seq) - npg); w = collections.Counter(seq[i:i + npg]); rest = collections.Counter(seq[:i] + seq[i + npg:])
        ceil.append(cos(w, rest))
        j = rng.randrange(len(la) - npg); null.append(cos(collections.Counter(la[j:j + npg]), r82))
    res['calibration'] = {'r4282_window_vs_rest_N%d' % npg: q(ceil), 'la17_latin_window_vs_r4282_N%d' % npg: q(null),
                          'page_cosine_rank_in_ceiling': round(sum(1 for c in ceil if c <= res['vs_r4282']['unigram_cosine']) / len(ceil), 4),
                          'null_draws_ge_page': sum(1 for c in null if c >= res['vs_r4282']['unigram_cosine'])}
    # Identity check: is the page a copy of part of R4282? (page vs R4282 p2 sequence; crop pixels vs tx2/crops p2_*)
    import difflib
    p2 = [r['sign'] for r in csv.DictReader(open(os.path.join(P, 'tx2/ciphertext_reconciled.tsv')), delimiter='\t') if r['sign'] != '^' and r['line'].startswith('p2')]
    pseq = page_tokens(); sm = difflib.SequenceMatcher(None, pseq, p2, autojunk=False)
    from PIL import Image
    pix = []
    for i in range(1, 8):
        a = Image.open(os.path.join(P, 'tx2/crops/p2_L0%d.jpg' % i)).convert('L'); b = Image.open(os.path.join(H, 'lc_L0%d.jpg' % i)).convert('L')
        pix.append(a.size == b.size and a.tobytes() == b.tobytes())
    res['identity_vs_r4282_p2'] = {'r4282_p2_signs': len(p2), 'page_signs': len(pseq), 'sequence_ratio': round(sm.ratio(), 4),
                                   'differences': [[pseq[o[1]:o[2]], p2[o[3]:o[4]]] for o in sm.get_opcodes() if o[0] != 'equal'],
                                   'crops_pixel_identical_to_tx2_p2': '%d of 7' % sum(pix)}
    out = json.dumps(res, indent=1, ensure_ascii=False) + '\n'
    f = os.path.join(H, 'results.json')
    if '--check' in sys.argv:
        if not os.path.exists(f) or open(f, encoding='utf-8').read() != out:
            print('results.json stale'); sys.exit(1)
        print('results.json current'); return
    open(f, 'w', encoding='utf-8').write(out); print(out)

if __name__ == '__main__':
    main()
