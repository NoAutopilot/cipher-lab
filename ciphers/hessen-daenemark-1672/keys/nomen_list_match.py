#!/usr/bin/env python3
"""GAPS176 (3 Oct 2026): does any key table on disk carry this letter's 1672 nomenclator?

For every key file tools/key_crossmatch.py discovers (all ciphers/**/key*.tsv plus the published tables it globs),
count how many of the letter's gloss-pinned nomenclator codes (key_gloss.tsv, C/M rows; I rows excluded) map in that
key to a value matching the gloss (normalised name stem). Control (rule 3): the same key scored against the glosses
reassigned at random among the same codes (1000 shuffles) -- a shuffle changes which value each code is checked
against, so the control's count can differ from the real one. A key is a candidate only if real >= 3 and real exceeds
the shuffle p99. Usage: python3 nomen_list_match.py [--check | --selftest]
"""
import csv, os, random, re, sys, unicodedata
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
os.chdir(ROOT)
import key_crossmatch as kx

# gloss -> stems that count as the same referent (German/Latin/French spellings of the period)
STEMS = {
 'Berlin': ['berlin'], 'alliance': ['allian', 'bundni', 'foedus'], 'Hertzog': ['hertzog', 'herzog', 'duc', 'dux'],
 'von_Ploen': ['ploen', 'plon', 'plön'], 'Kayser': ['kayser', 'kaiser', 'keyser', 'imperat', 'empereur'],
 'Dennemarck': ['denne', 'dene', 'dane', 'dän', 'dan', 'dania'], 'Konig_in_Dennemarck': ['denne', 'dane', 'dän', 'dania'],
 'K.Dennemarck': ['denne', 'dane', 'dän', 'dania'], 'Cur_Brandenburg': ['brandenb', 'brandeb'],
 'Cur_Brand.': ['brandenb', 'brandeb'], 'Cur_Brandenb.': ['brandenb', 'brandeb'], '?_Ahlefeldt': ['ahlef', 'alef'],
 'Bleinenk?l': ['blein'], '?ueco': ['suec', 'schwed', 'swed', 'suede'], 'Holland': ['holl'],
 'Gen._Staaten': ['staat', 'staten', 'etats', 'ordines'], 'Rex_Daniae': ['denne', 'dane', 'dän', 'dania'],
 'Franckreich': ['franck', 'frank', 'franc', 'galli'],
}

def norm(s):
    s = unicodedata.normalize('NFKD', str(s)).lower()
    return s

def load_gloss():
    rows = []
    with open(os.path.join(HERE, '..', 'key_gloss.tsv'), encoding='utf-8') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['grade'] in ('C', 'M'):
                rows.append((r['code'], r['value'].strip('[]')))
    return rows

def hits(key, pairs):
    n = 0
    for code, gl in pairs:
        v = key.get(code)
        if v is None: continue
        v = norm(v)
        if any(st in v for st in STEMS[gl]): n += 1
    return n

def selftest(pairs):
    # positive control: a decoy key (the largest-coverage key on disk is irrelevant; use a blank key) carrying
    # k of the letter's own gloss values at their codes plus 300 filler rows, scored exactly like the real keys
    codes = [c for c, _ in pairs]; gls = [g for _, g in pairs]
    rnd = random.Random(1760)
    for k in (3, 4, 6, 9):
        key = {str(1000 + i): 'filler%d' % i for i in range(300)}
        for c, g in rnd.sample(pairs, k): key[c] = g.replace('_', ' ')
        real = hits(key, pairs); ctrl = []
        for _ in range(1000):
            g2 = gls[:]; rnd.shuffle(g2); ctrl.append(hits(key, list(zip(codes, g2))))
        ctrl.sort()
        print(f'positive control k={k}: real {real}, shuffle mean {sum(ctrl)/1000:.2f}, p99 {ctrl[989]} ->',
              'CANDIDATE' if real >= 3 and real > ctrl[989] else 'no')

def main():
    pairs = load_gloss()
    if '--selftest' in sys.argv:
        selftest(pairs); return
    codes = [c for c, _ in pairs]; gls = [g for _, g in pairs]
    rnd = random.Random(176)
    out = []
    for kp in kx.find_key_files()[0]:
        rel = os.path.relpath(str(kp), ROOT)
        if 'hessen-daenemark-1672' in rel: continue
        try:
            key, _meta = kx.load_key_meta(kp)
        except Exception:
            continue
        if not key: continue
        key = {str(k).strip(): (v.get('value', '') if isinstance(v, dict) else v) for k, v in key.items()}
        cov = sum(1 for c in codes if c in key)
        real = hits(key, pairs)
        ctrl = []
        for _ in range(1000):
            g2 = gls[:]; rnd.shuffle(g2)
            ctrl.append(hits(key, list(zip(codes, g2))))
        ctrl.sort()
        p99 = ctrl[989]; mean = sum(ctrl) / len(ctrl)
        out.append((rel, len(key), cov, real, round(mean, 2), p99, 'CANDIDATE' if real >= 3 and real > p99 else 'no'))
    out.sort(key=lambda r: (-r[3], -r[2]))
    path = os.path.join(HERE, 'nomen_list_match.tsv')
    body = 'key_path\tkey_rows\tglossed_codes_present\treal_hits\tshuffle_mean\tshuffle_p99\tverdict\n' + \
        ''.join('\t'.join(map(str, r)) + '\n' for r in out)
    if '--check' in sys.argv:
        ok = open(path, encoding='utf-8').read() == body
        print('nomen_list_match.tsv', 'up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(path, 'w', encoding='utf-8').write(body)
    print(f'gloss pairs {len(pairs)}; keys scanned {len(out)}; candidates {sum(r[6]=="CANDIDATE" for r in out)}')
    for r in out[:12]: print('\t'.join(map(str, r)))

if __name__ == '__main__':
    main()
