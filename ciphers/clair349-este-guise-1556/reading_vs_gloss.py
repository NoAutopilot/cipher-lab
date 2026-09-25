#!/usr/bin/env python3
"""Reading vs the interlinear gloss, per token (ZX-DEC349 step 3, 25 Sept 2026).

Reads reading_tokens.tsv (tools/decode_key.py output), ciphertext.tsv (gloss column) and exceptions.tsv. Both sides are
normalised to one convention first (CLAUDE.md rule 3, PX-BRODEC lesson): lower case, j=i, v=u, long s=s, no
punctuation; a crossed-z gloss over an i = i; a gloss that is a prefix of a word value (po/pour, q/que) or one letter of
a doubled pair counts as agreeing. Two figures: (a) every glossed token; (b) only tokens whose value came from the key
(tokens where exceptions.tsv took the value from the gloss itself are left out, since they agree by construction).
Writes reading_vs_gloss.tsv (every disagreement with its likeliest cause) and prints pooled and per-line agreement.
`--check` exits 1 if reading_vs_gloss.tsv is stale.
"""
import collections, csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def rd(n):
    return list(csv.DictReader(open(os.path.join(HERE, n), encoding='utf-8'), delimiter='\t'))


def norm(s):
    s = s.lower().replace('ſ', 's').replace('j', 'i').replace('v', 'u')
    return re.sub(r'[^a-z]', '', s)


def agree(value, gloss):
    v = norm(value.split('|')[0])
    g = norm(gloss)
    if not v or not g:
        return False
    if g == v or (g == 'z' and v == 'i'):
        return True
    if len(v) > 1 and v.startswith(g) and len(set(v)) > 1:
        return True
    if len(v) == 2 and v[0] == v[1] and g == v[0]:
        return True
    return False


def run():
    gl = {(r['line'], r['position']): r for r in rd('ciphertext.tsv')}
    exc = {(r['line'], r['position']): r for r in rd('exceptions.tsv')}
    keyg = {r['code']: r['grade'] for r in rd('key_decode.tsv')}
    tot = collections.Counter(); ok = collections.Counter(); totk = collections.Counter(); okk = collections.Counter()
    rows = ['line\tposition\tsign\tvalue\tgrade\tgloss\tcause']
    causes = collections.Counter()
    for t in rd('reading_tokens.tsv'):
        k = (t['line'], t['pos'])
        g = gl[k]['gloss'].strip()
        if not g or g == '?' or t['value'] == 'NULL':
            continue
        from_gloss = k in exc and ('gloss taken' in exc[k]['reason'] or 'from its gloss' in exc[k]['reason']
                                  or exc[k]['reason'].startswith(('S40', 'S16', '68', '10 ', 'lone 4', 'S35')))
        a = agree(t['value'], g)
        tot[t['line']] += 1; ok[t['line']] += a
        if not from_gloss:
            totk[t['line']] += 1; okk[t['line']] += a
        if a:
            continue
        v, s = t['value'], t['sign']
        if t['grade'] == 'U' or s not in keyg:
            c = 'transcription (sign not in the key)'
        elif '|' in v:
            c = 'homograph (unresolved)'
        elif len(norm(g)) > len(norm(v)) and len(norm(g)) >= 3:
            c = 'gloss abbreviation / gloss spans more than one token'
        elif keyg.get(s) == 'M':
            c = 'key cell (graded M)'
        elif gl[k]['confidence'] == 'M':
            c = 'transcription (token settled at M) or gloss misread'
        else:
            c = 'gloss misread or transcription (token agreed blind)'
        causes[c] += 1
        rows.append('\t'.join([t['line'], t['pos'], s, v, t['grade'], g, c]))
    lines = sorted(tot)
    rep = ['line\tglossed\tagree\tshare\tkey_only_glossed\tkey_only_agree\tkey_only_share']
    for ln in lines:
        rep.append(f'{ln}\t{tot[ln]}\t{ok[ln]}\t{ok[ln]/tot[ln]:.2f}\t{totk[ln]}\t{okk[ln]}\t'
                   f'{(okk[ln]/totk[ln]) if totk[ln] else 0:.2f}')
    T, O, TK, OK = sum(tot.values()), sum(ok.values()), sum(totk.values()), sum(okk.values())
    rep.append(f'pooled (a) all glossed tokens: {O}/{T} = {100*O/T:.1f}%')
    rep.append(f'pooled (b) key-derived values only: {OK}/{TK} = {100*OK/TK:.1f}%')
    rep.append('disagreements by likeliest cause: ' + '; '.join(f'{c} {n}' for c, n in causes.most_common()))
    return '\n'.join(rows) + '\n', '\n'.join(rep)


if __name__ == '__main__':
    text, rep = run()
    p = os.path.join(HERE, 'reading_vs_gloss.tsv')
    if '--check' in sys.argv:
        ok = os.path.exists(p) and open(p, encoding='utf-8').read() == text
        print('reading_vs_gloss.tsv', 'current' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(p, 'w', encoding='utf-8').write(text)
    print(rep)
