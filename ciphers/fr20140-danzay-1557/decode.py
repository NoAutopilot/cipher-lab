#!/usr/bin/env python3
"""Apply Tomokiyo's 1557 Danzay key (key.tsv) to each leaf in LEAVES: f.35 (ciphertext.txt -> reading.txt,
reading_tokens.tsv) and f.36r line 1 (ciphertext_f36.tsv -> reading_f36.txt, reading_tokens_f36.tsv).

Grades per cipher token: H = sign read clearly and keyed to one value by Tomokiyo; M = sign identity
uncertain in the image, or a glyph Tomokiyo gives two values; U = sign not in his table. Clear-hand words
(w:) are not cipher tokens and are counted separately as 'clear'.
In reading.txt: keyed values in lowercase, nulls dropped, unkeyed signs as [code], clear words in CAPS,
a glyph Tomokiyo keys twice shows its first value (grade M), word signs as <word>.
--check: exit 1 if any committed reading / token file differs from what this script produces.
"""
import sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))

def load_key():
    key = {}
    for l in open(os.path.join(HERE, 'key.tsv'), encoding='utf-8'):
        if l.startswith('#') or l.startswith('sign\t') or not l.strip():
            continue
        s, _glyph, v, _src = l.rstrip('\n').split('\t')
        key[s] = v
    return key

# (transcription, reading, per-token grades) per leaf; f.35 outputs keep their original names.
LEAVES = [('ciphertext.txt', 'reading.txt', 'reading_tokens.tsv'),
          ('ciphertext_f36.tsv', 'reading_f36.txt', 'reading_tokens_f36.tsv')]

def load_ct(name='ciphertext.txt'):
    rows = []
    for l in open(os.path.join(HERE, name), encoding='utf-8'):
        if l.startswith('#') or l.startswith('line\t') or not l.strip():
            continue
        ln, pos, sign, conf = l.rstrip('\n').split('\t')[:4]
        rows.append((ln, int(pos), sign, conf))
    return rows

WORDS = {'le', 'et', 'luy', 'son?', 'le Roy de Dannemarch'}

def render(rows, key, name='ciphertext.txt'):
    lines = collections.OrderedDict()
    toks = ['line\tpos\tsign\tvalue\tgrade']
    counts = collections.Counter()
    for ln, pos, sign, conf in rows:
        if sign.startswith('w:'):
            out, val, g = sign[2:].upper(), sign[2:], 'clear'
        elif sign in key:
            val = key[sign]
            amb = '|' in val
            g = 'M' if (conf == 'M' or amb) else 'H'
            if val == 'null':
                out = ''
            elif amb:
                out = val.split('|')[0]
            elif val in WORDS:
                out = '<' + val + '>'
            else:
                out = val
        else:
            val, g, out = '', 'U', '[' + sign + ']'
        counts[g] += 1
        if val == 'null':
            counts['null'] += 1
        toks.append(f'{ln}\t{pos}\t{sign}\t{val}\t{g}')
        lines.setdefault(ln, []).append(out)
    txt = [f'# Mechanical reading of {name} with key.tsv (decode.py). Nulls dropped; [code] = unkeyed sign;',
           '# CAPS = clear-hand words in the letter; T and hk (keyed twice by Tomokiyo) shown as a and u; <w> = his word signs.']
    for ln, outs in lines.items():
        txt.append(f'{ln}\t' + ' '.join(o for o in outs if o))
    return '\n'.join(txt) + '\n', '\n'.join(toks) + '\n', counts

def main():
    key = load_key()
    paths, allcounts = {}, []
    for ct, rd, tk in LEAVES:
        reading, tokens, counts = render(load_ct(ct), key, ct)
        paths[rd], paths[tk] = reading, tokens
        allcounts.append((ct, counts))
    if '--check' in sys.argv:
        stale = [p for p, c in paths.items()
                 if not os.path.exists(os.path.join(HERE, p)) or open(os.path.join(HERE, p), encoding='utf-8').read() != c]
        if stale:
            print('STALE:', ', '.join(stale)); sys.exit(1)
        print('reading up to date'); return
    for p, c in paths.items():
        open(os.path.join(HERE, p), 'w', encoding='utf-8').write(c)
    for ct, counts in allcounts:
        cipher = counts['H'] + counts['M'] + counts['U']
        print(f"{ct}: cipher tokens {cipher}: H {counts['H']} (of which null {counts['null']}), M {counts['M']}, U {counts['U']}; clear words {counts['clear']}")

if __name__ == '__main__':
    main()
