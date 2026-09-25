#!/usr/bin/env python3
"""Build the decode inputs for tools/decode_key.py (ZX-DEC349, 25 Sept 2026).

Inputs (committed beside this script): key_alpha.tsv, key_nomen.tsv (the key as transcribed, unchanged),
ciphertext.tsv (line, position, sign, gloss, confidence; gloss = the contemporary interlinear decipherment).
Outputs:
  key_decode.tsv    the two key tables flattened to one code -> value table tools/decode_key.py reads: letters lower
                    case, I/J as i, V as u (the gloss writes u; V's codes carry the vowel far more than the consonant),
                    a DOUBLES pair as its letters, NULLES as NULL, a word code as the word; `source` = M where the key
                    cell is graded M. Homographs stay 'a|b' (decode_key.py grades them M); every homograph token is
                    then settled per position in exceptions.tsv by the rules below.
  gloss_votes.tsv   line, position, gloss (raw), vote: the gloss normalised to the key's convention (lower case,
                    j=i, v=u, long s=s; a crossed-z gloss over an I code = i; a gloss that is the key value's prefix,
                    such as po for pour or q for que, = the key value; a single letter over a DOUBLES code = the pair).
                    decode_key.py grades a token C (voted_grade) where the vote equals the key value.
  exceptions.tsv    line, position, value, grade, reason: every homograph token (rule and count in NOTES.md), every
                    token whose gloss disagrees with the key (key value kept at M unless a named systematic
                    transcription confusion applies, then the gloss value at I), and every unkeyed token that carries
                    a gloss (gloss value at I). An unkeyed token with no gloss stays U.
`--check` exits 1 if any output is stale. Nothing is fetched.
"""
import collections, csv, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def rd(name):
    return list(csv.DictReader(open(os.path.join(HERE, name), encoding='utf-8'), delimiter='\t'))


def key_rows():
    rows = []
    for r in rd('key_alpha.tsv'):
        if r['kind'] == 'void':
            continue
        v = r['letter']
        if v.startswith('DOUBLES:'):
            v = re.sub(r'\(.*\)', '', v.split(':', 1)[1]).rstrip('?')
            v = 'sc' if v == 'sc' else v
        elif v.startswith('NULLES'):
            v = 'NULL'
        else:
            v = {'I/J': 'i', 'V': 'u'}.get(v, v).lower()
        rows.append((r['code'], v, r['grade'], r['letter']))
    for r in rd('key_nomen.tsv'):
        if r['code'] in ('', '?'):
            continue
        rows.append((r['code'], r['word_or_phrase'], r['grade'], r['section'] + ':' + r['word_or_phrase']))
    return rows


def flat_key():
    key = collections.OrderedDict()
    for code, v, g, src in key_rows():
        if code in key:
            pv, pg, ps = key[code]
            if v not in pv.split('|'):
                key[code] = (pv + '|' + v, 'M', ps + '+' + src)
        else:
            key[code] = (v, g, src)
    return key


def norm(s):
    s = s.lower().replace('ſ', 's').replace('j', 'i').replace('v', 'u')
    return re.sub(r"[^a-z']", '', s)


def vote_for(gloss, value):
    """The gloss normalised to the key's convention, or '' when there is no usable gloss."""
    g = norm(gloss)
    if not g:
        return ''
    alts = value.split('|') if value else []
    for a in alts:
        na = norm(a)
        if not na:
            continue
        if g == na:
            return a
        if g == 'z' and na == 'i':                       # crossed-z gloss = i/j (line 01 'J'ay')
            return a
        if len(na) > 1 and len(g) >= 1 and na.startswith(g) and len(set(na)) > 1:   # po = pour, q = que
            return a
        if len(na) == 2 and na[0] == na[1] and g == na[0]:  # one letter over a DOUBLES pair
            return a
    return g


# Homograph rules, each supported by the gloss (counts in NOTES.md, ZX-DEC349 step 1).
def homograph(sign, gloss, nxt_val, alone):
    """(value, rule) for a homograph code, from the token's own gloss when it has one, else from the rule."""
    g = norm(gloss)
    if sign == '22':
        return 'pour', 'rule 22=pour (gloss po/pu 7 of 9 glossed; never sc)'
    if sign == 'S37':
        return 't', 'rule S37=t (gloss t 32 of 35; never fit)'
    if sign == '9':
        if g in ('s', 'ss'):
            return 'c', 'gloss read s over 9, but the word needs c (receu 01, escrire 02, ce 03): 9=c, the gloss s is a c'
        return 'c', 'rule 9=c (gloss c 22 of 33; the 3 glossed s sit in receu/escrire/ce; never the round-ss double)'
    if sign == '5':
        if g in ('d', 'l'):
            return g, 'gloss %s over 5 (D and L share 5; gloss d 21, l 10)' % g
        return 'd|l', 'no gloss: 5 is D or L (gloss d 21, l 10; no positional rule separates them)'
    if sign == 'S32':
        if g.startswith('que'):
            return 'que', 'gloss %s over S32: Q standing for que' % g
        if nxt_val == 'u':
            return 'q', 'rule S32=q before a V code (gloss q 9)'
        return 'que', 'rule S32 not before V = que (gloss que/quel 8; never n\'aye)'
    if sign == 'S17':
        if g.startswith('f'):
            return 'fist', 'gloss f over S17: fist (Monsr/fist homograph)'
        return 'fist|Monsr [ ]', 'S17 gloss %r settles neither fist nor Monsr' % gloss
    return None


# Systematic transcription confusions named by ZX-TR349D / ZX-KEY349 where the gloss is taken over the code.
CONFUSION = {
    ('S40', 'r'): 'S40 (Z) glossed r: the R-loop S33 matched to S40 (ZX-TR349D lead 3)',
    ('S16', 'd'): 'S16 (Le Duc de Guyse) glossed d/du in running text: an atlas confusion with a d-form; gloss taken',
    ('S16', 'du'): 'S16 (Le Duc de Guyse) glossed d/du in running text: an atlas confusion with a d-form; gloss taken',
    ('68', 'll'): '68 is not a key code; the Doubles ll code is 69',
    ('10', 'u'): '10 is not a key code: a split 102/104 (V)',
    ('4', 's'): 'lone 4 glossed s: S36 (S) per ZX-TR349D lead 1',
    ('4', 'f'): 'lone 4 glossed f: S02 (F) or S36 per ZX-TR349D lead 1',
    ('S35', 'uo'): 'S35 glossed vo: the vous word sign (S51) matched to S35',
    ('S35', 'uos'): 'S35 glossed vos: the vous word sign (S51) matched to S35',
    ('S35', 'so'): 'S35 glossed so: the vous word sign (S51) matched to S35 (secretary v read s)',
}
CONF_VALUE = {('S35', 'uo'): 'vous', ('S35', 'uos'): 'vous', ('S35', 'so'): 'vous', ('10', 'u'): 'u',
              ('68', 'll'): 'll', ('S16', 'du'): 'du'}


NOMEN = {r['code'] for r in rd('key_nomen.tsv')} - {'S37', 'S32', '22', 'S17'}


def build():
    key = flat_key()
    ct = rd('ciphertext.tsv')
    by = collections.defaultdict(list)
    for r in ct:
        by[r['line']].append(r)
    kout = ['code\tvalue\tgrade\tsource\tnote']
    for code, (v, g, src) in key.items():
        kout.append('\t'.join([code, v, g or 'H', 'M' if g == 'M' else 'key', src]))
    vout = ['line\tposition\tgloss\tvote']
    xout = ['line\tposition\tsign\tvalue\tgrade\treason']
    for ln, rows in by.items():
        signs = [r for r in rows]
        for i, r in enumerate(signs):
            s, gl = r['sign'], r['gloss'].strip()
            if s == '|':
                continue
            kv = key.get(s, (None,))[0]
            nxt = signs[i + 1]['sign'] if i + 1 < len(signs) else '$'
            prv = signs[i - 1]['sign'] if i > 0 else '^'
            nxt_val = key.get(nxt, ('',))[0]
            alone = prv in ('|', '^') and nxt in ('|', '$')
            vote = vote_for(gl, kv) if gl and gl != '?' else ''
            if vote:
                vout.append('\t'.join([ln, r['position'], gl, vote]))
            h = homograph(s, gl, nxt_val, alone) if kv and '|' in kv else None
            if h:
                val, why = h
                glossed_ok = vote and norm(vote) == norm(val)
                grade = 'C' if glossed_ok else ('M' if '|' in val else 'I')
                xout.append('\t'.join([ln, r['position'], s, val, grade, why]))
                continue
            if kv is None:
                if vote:
                    xout.append('\t'.join([ln, r['position'], s, CONF_VALUE.get((s, norm(gl)), vote), 'I',
                                           CONFUSION.get((s, norm(gl)), 'unkeyed sign %s; value from its gloss' % s)]))
                continue
            if kv == 'NULL' or not vote:
                continue
            if norm(vote) == norm(kv):
                continue                                   # C via gloss_votes.tsv
            c = CONFUSION.get((s, norm(gl)))
            if c:
                xout.append('\t'.join([ln, r['position'], s, CONF_VALUE.get((s, norm(gl)), norm(gl)), 'I', c]))
            elif s in NOMEN and len(norm(gl)) <= 2 and not norm(kv).startswith(norm(gl)):
                xout.append('\t'.join([ln, r['position'], s, norm(gl), 'I',
                                       'word code %s (%s) inside spelled text, glossed %r: atlas confusion, gloss taken'
                                       % (s, kv, gl)]))
            else:
                xout.append('\t'.join([ln, r['position'], s, kv, 'M',
                                       'gloss %r disagrees with key %s=%s; key kept' % (gl, s, kv)]))
    return {'key_decode.tsv': '\n'.join(kout) + '\n', 'gloss_votes.tsv': '\n'.join(vout) + '\n',
            'exceptions.tsv': '\n'.join(xout) + '\n'}


if __name__ == '__main__':
    out = build()
    stale = []
    for name, text in out.items():
        p = os.path.join(HERE, name)
        if '--check' in sys.argv:
            if not os.path.exists(p) or open(p, encoding='utf-8').read() != text:
                stale.append(name)
        else:
            open(p, 'w', encoding='utf-8').write(text)
            print('wrote', name, text.count('\n') - 1, 'rows')
    if '--check' in sys.argv:
        print('STALE: ' + ', '.join(stale) if stale else 'build_decode outputs current')
        sys.exit(1 if stale else 0)
