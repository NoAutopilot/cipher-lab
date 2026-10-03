"""Align our transcription (pool/pooled.tsv) with D. Bourdeau's malsburg1637 transcription, token by token,
and decode our tokens under his key (key.txt). Verifier job VERIFY-MALSBURG-BOURDEAU, 3 Oct 2026.

Usage: python3 align.py BOURDEAU_TARGET_DIR   (a checkout of dbourdeau/cyphersolver targets/malsburg1637)
Writes align_summary.tsv and decode_ours_under_his_key.txt beside this script. Bourdeau's files are read, not
copied (his code is MIT, text CC BY 4.0; credit: Daniel Bourdeau, github.com/dbourdeau/cyphersolver).
"""
import re, sys, csv, difflib, os
from collections import OrderedDict
HERE = os.path.dirname(os.path.abspath(__file__))
B = sys.argv[1]

def norm(t):
    t = t.rstrip("'?_")
    t = {'z1': 'Z', '7?': '7'}.get(t, t)
    return t

# ours, per image
ours = OrderedDict()
for r in csv.DictReader(open(os.path.join(HERE, '..', 'pool', 'pooled.tsv')), delimiter='\t'):
    img = r['line'][:19]           # hstam_4_h_1411_0003
    ours.setdefault(img[-4:], []).append(r['sign'])

def his_tokens(path, start_marker=None):
    toks, on = [], start_marker is None
    for line in open(path, encoding='utf8'):
        if line.startswith('#'):
            if start_marker and start_marker in line: on = True
            if 'letter-cipher' in line: break
            continue
        if not on: continue
        line = re.sub(r'\{[^}]*\}', ' ', line)
        toks += [t for t in line.split() if t != '/']
    return toks

K = {}
for line in open(os.path.join(B, 'key.txt'), encoding='utf8'):
    if not line.startswith('#'):
        for kv in line.split():
            k, v = kv.split('='); K[k] = v
codes = {}
for line in open(os.path.join(B, 'codes.txt'), encoding='utf8'):
    if line.strip() and not line.startswith('#'):
        p = line.split('\t'); codes[p[0]] = p[1].lstrip('=')

def dec(t):
    t = norm(t)
    if re.fullmatch(r'\d\d', t): return K.get(t, '?')
    if t in K and not t.isdigit(): return K[t].upper()
    if t in codes: return '[' + codes[t] + ']'
    if re.fullmatch(r'\d+', t) and len(t) >= 3: return '[' + t + ']'
    if re.fullmatch(r'\d', t): return t
    return '{' + t + '}'          # clear word or open sign

rows, dec_out = [], []
for img, ot in ours.items():
    hp = os.path.join(B, f'f{img[1:]}.txt')
    ht = [norm(t) for t in his_tokens(hp)]
    on = [norm(t) for t in ot if re.fullmatch(r"[0-9A-Z][0-9#]*|z1", t)]  # cipher signs only, drop clear words
    sm = difflib.SequenceMatcher(None, ht, on, autojunk=False)
    matched = sum(b.size for b in sm.get_matching_blocks())
    # restrict his side to the span ours covers
    blocks = [b for b in sm.get_matching_blocks() if b.size]
    h0, h1 = blocks[0].a, blocks[-1].a + blocks[-1].size
    span = h1 - h0
    ops = {'replace': 0, 'delete': 0, 'insert': 0}
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag != 'equal' and h0 <= i1 <= h1: ops[tag] += max(i2 - i1, j2 - j1)
    rows.append([img, len(on), len(ht), span, matched, f'{matched/len(on):.3f}', ops['replace'], ops['delete'], ops['insert']])
    dec_out.append(f'===== image {img}: our {len(on)} cipher tokens under Bourdeau key.txt (his file f{img[1:]}.txt)')
    lines = OrderedDict()
    for r in csv.DictReader(open(os.path.join(HERE, '..', 'pool', 'pooled.tsv')), delimiter='\t'):
        if r['line'][15:19] == img: lines.setdefault(r['line'], []).append(r['sign'])
    for ln, ts in lines.items():
        dec_out.append(ln + '\t' + ''.join(dec(t) for t in ts))
with open(os.path.join(HERE, 'align_summary.tsv'), 'w') as f:
    f.write('image\tours_cipher_tokens\this_tokens_on_image\this_span_aligned\tmatched\tmatched_share_of_ours\treplace\this_only\tours_only\n')
    for r in rows: f.write('\t'.join(map(str, r)) + '\n')
open(os.path.join(HERE, 'decode_ours_under_his_key.txt'), 'w').write('\n'.join(dec_out) + '\n')
print(open(os.path.join(HERE, 'align_summary.tsv')).read())

# disagreement listing for the two H-graded leaves (ff.3, 12): show both readings decoded under his key
with open(os.path.join(HERE, 'disagreements_ff3_12.tsv'), 'w') as f:
    f.write('image\this_tokens\tours_tokens\this_decoded\tours_decoded\tcontext_his_decoded\n')
    for img in ('0003', '0012'):
        ht = [norm(t) for t in his_tokens(os.path.join(B, f'f{img[1:]}.txt'))]
        on = [norm(t) for t in ours[img] if re.fullmatch(r"[0-9A-Z][0-9#]*|z1", t)]
        sm = difflib.SequenceMatcher(None, ht, on, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == 'equal' or (tag == 'delete' and (i1 == 0 or i2 == len(ht))): continue
            ctx = ''.join(dec(t) for t in ht[max(0, i1-6):i2+6])
            f.write('\t'.join([img, ' '.join(ht[i1:i2]), ' '.join(on[j1:j2]),
                               ''.join(dec(t) for t in ht[i1:i2]), ''.join(dec(t) for t in on[j1:j2]), ctx]) + '\n')
