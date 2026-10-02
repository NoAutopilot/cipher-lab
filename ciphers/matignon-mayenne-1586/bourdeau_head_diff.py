#!/usr/bin/env python3
"""Diff Bourdeau's HEAD key.json and 13 Cipher-1 transcriptions (snapshot
sources/cyphersolver/2026-10-02/matignon1586/, fetched 2 Oct 2026 03:36 UTC from
raw.githubusercontent.com/dbourdeau/cyphersolver/main/targets/matignon1586/) against this
folder's key.tsv (his key.json at fc0c9e8) and ciphertext.txt (his transcriptions at fc0c9e8).

Credit: Daniel Bourdeau, dbourdeau/cyphersolver, text CC BY 4.0 / code MIT.

Usage: python3 bourdeau_head_diff.py [--check]
  --check  exit 1 if the committed openings/bourdeau_head_diff.json differs from a fresh run.
"""
import json, sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
SNAP = os.path.join(HERE, '..', '..', 'sources', 'cyphersolver', '2026-10-02', 'matignon1586')
OUT = os.path.join(HERE, 'openings', 'bourdeau_head_diff.json')
FILES = {'f110': 'f110_cipher.txt', 'f123r': 'f123r_cipher.txt', 'f123v': 'f123v_cipher.txt',
         'f124r': 'f124r_cipher.txt', 'f124v': 'f124v_cipher.txt', 'f143r': 'cipher_f143.txt',
         'f143v': 'f143v_cipher.txt', 'f150': 'f150_cipher.txt', 'f154': 'f154_cipher.txt',
         'f173': 'f173_cipher.txt', 'f196': 'f196_cipher.txt', 'f201': 'f201_cipher.txt',
         'fr15571-f177': 'f177_cipher.txt'}

def load_key_tsv():
    key = {}
    with open(os.path.join(HERE, 'key.tsv')) as fh:
        hdr = fh.readline().rstrip('\n').split('\t')
        for line in fh:
            if not line.strip():
                continue
            r = dict(zip(hdr, line.rstrip('\n').split('\t')))
            key[r['code']] = r
    return key

def load_ciphertext():
    leaves = collections.OrderedDict()
    with open(os.path.join(HERE, 'ciphertext.txt')) as fh:
        for line in fh:
            line = line.rstrip('\n')
            if not line.strip() or line.startswith('#'):
                continue
            lid, toks = line.split('\t')[0], line.split('\t')[1]
            leaf = lid.rsplit('-', 1)[0]
            leaves.setdefault(leaf, []).append(toks.split())
    return leaves

def main():
    head = json.load(open(os.path.join(SNAP, 'key.json')))
    ours = load_key_tsv()
    res = {'key': {}, 'transcriptions': {}}
    added = {c: v for c, v in head.items() if c not in ours}
    removed = [c for c in ours if c not in head]
    changed = {}
    for c, v in head.items():
        if c in ours:
            ov = ours[c]['value'].split('|')
            if ov != v:
                changed[c] = {'ours': ov, 'head': v}
    res['key'] = {'head_rows': len(head), 'ours_rows': len(ours), 'added_at_head': added,
                  'removed_at_head': removed, 'changed': changed}
    ct = load_ciphertext()
    # all labels used in our ciphertext, with counts, and whether keyed at HEAD / ours
    counts = collections.Counter(t for leaf in ct.values() for line in leaf for t in line)
    res['labels_unkeyed_both'] = {t: n for t, n in counts.most_common()
                                  if t not in head and t not in ours}
    res['labels_keyed_head_only'] = {t: {'n': n, 'head': head[t]} for t, n in counts.most_common()
                                     if t in head and t not in ours}
    for leaf, fn in FILES.items():
        path = os.path.join(SNAP, fn)
        his = [l.split() for l in open(path).read().split('\n') if l.strip()]
        mine = ct.get(leaf, [])
        his_tok = sum(len(l) for l in his); my_tok = sum(len(l) for l in mine)
        same = his == mine
        diffs = []
        if not same:
            for i in range(max(len(his), len(mine))):
                a = his[i] if i < len(his) else None
                b = mine[i] if i < len(mine) else None
                if a != b:
                    diffs.append({'line': i + 1, 'head_tokens': len(a) if a else None,
                                  'ours_tokens': len(b) if b else None,
                                  'head': ' '.join(a) if a else None, 'ours': ' '.join(b) if b else None})
        res['transcriptions'][leaf] = {'file': fn, 'head_lines': len(his), 'ours_lines': len(mine),
                                       'head_tokens': his_tok, 'ours_tokens': my_tok,
                                       'identical': same, 'line_diffs': diffs}
    if '--check' in sys.argv:
        old = json.load(open(OUT))
        if old != res:
            print('STALE: openings/bourdeau_head_diff.json differs from a fresh run'); sys.exit(1)
        print('bourdeau_head_diff.json up to date'); return
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(res, open(OUT, 'w'), indent=1, ensure_ascii=False)
    k = res['key']
    print(f"key.json HEAD rows {k['head_rows']} vs key.tsv {k['ours_rows']}; added at HEAD {len(k['added_at_head'])}, "
          f"removed {len(k['removed_at_head'])}, changed {len(k['changed'])}")
    for c, v in k['added_at_head'].items(): print('  + ', c, v)
    for c in k['removed_at_head']: print('  - ', c, ours[c]['value'])
    for c, v in k['changed'].items(): print('  ~ ', c, v)
    print('labels in ciphertext keyed at HEAD only:', res['labels_keyed_head_only'])
    print('unkeyed in both (top 15):', list(res['labels_unkeyed_both'].items())[:15])
    for leaf, t in res['transcriptions'].items():
        print(f"{leaf:6} {t['file']:18} lines {t['head_lines']}/{t['ours_lines']} tokens {t['head_tokens']}/{t['ours_tokens']} "
              f"{'identical' if t['identical'] else str(len(t['line_diffs']))+' line diffs'}")

if __name__ == '__main__':
    main()
