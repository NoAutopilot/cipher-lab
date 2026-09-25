import csv, json
from collections import defaultdict, Counter

rows = list(csv.DictReader(open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/plaintext_appendix.tsv'), delimiter='\t'))
tok_rows = list(csv.DictReader(open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/ciphertext_appendix.tsv'), delimiter='\t'))
entry_tokens = defaultdict(list)
for r in tok_rows:
    entry_tokens[(r['leaf'], r['entry_label'])].append(r['token'])

def norm(p):
    return p.lower() if len(p.rstrip('±'))==1 and p.rstrip('±').isalpha() else p

def segment(cipher_line, tokens):
    segs = []
    ptr = 0
    for chunk in cipher_line.split():
        pieces_raw = [p for p in chunk.split('.') if p != '']
        pieces = [norm(p) for p in pieces_raw]
        matched = False
        # try full chunk match
        n = len(pieces)
        if ptr+n <= len(tokens) and pieces == tokens[ptr:ptr+n] and n>0:
            segs.append(('CODE', pieces)); ptr += n; matched = True
        else:
            # try suffix match: maybe a leading piece (e.g. capital word) isn't code, rest is
            for skip in range(1, len(pieces)):
                sub = pieces[skip:]
                m = len(sub)
                if m>0 and ptr+m <= len(tokens) and sub == tokens[ptr:ptr+m]:
                    segs.append(('PLAIN', '.'.join(pieces_raw[:skip])))
                    segs.append(('CODE', sub))
                    ptr += m
                    matched = True
                    break
        if not matched:
            segs.append(('PLAIN', chunk))
    return segs, ptr

out = []
for r in rows:
    key = (r['leaf'], r['entry_label'])
    cl = r['cipher_line']
    if not cl.strip():
        continue
    tokens = entry_tokens[key]
    segs, consumed = segment(cl, tokens)
    if consumed != len(tokens):
        print("INCOMPLETE", key, consumed, len(tokens))
    out.append((key, segs, r['deciffrada_line']))

json.dump([(list(k), segs, d) for k,segs,d in out], open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/scripts/_segments.json','w'), ensure_ascii=False, indent=1)
print("done", len(out))
