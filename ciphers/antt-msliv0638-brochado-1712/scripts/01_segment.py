import csv, json
from collections import defaultdict, Counter

rows = list(csv.DictReader(open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/plaintext_appendix.tsv'), delimiter='\t'))
tok_rows = list(csv.DictReader(open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/ciphertext_appendix.tsv'), delimiter='\t'))
entry_tokens = defaultdict(list)
for r in tok_rows:
    entry_tokens[(r['leaf'], r['entry_label'])].append(r['token'])

def norm(p):
    return p.lower() if len(p.rstrip('±'))==1 and p.rstrip('±').isalpha() else p

def code_shaped(piece):
    """A piece that can only be a code symbol: a bare number, or a single letter, either
    possibly flagged '±' -- never a real multi-letter Portuguese word."""
    bare = piece.rstrip('±')
    return bare.isdigit() or (len(bare) == 1 and bare.isalpha())

def segment(cipher_line, tokens):
    """PX-BROKEY2 fix (25 Sept 2026): two appendix entries (Carta 74, Carta 92) turned out to be
    coded letter-for-letter with NO plain words at all (confirmed by hand-check against the image --
    every space-separated chunk in their cipher_line is dot-joined digits/single letters); their stored
    ciphertext_appendix.tsv token row had drifted out of sync with cipher_line (a transcription-pass
    inconsistency between the two tables), so the old exact-match-against-tokens[] logic fell through to
    treating a 16-token code run as one giant unmatched 'PLAIN word'. Multi-piece chunks that are entirely
    code-shaped (all digits/single letters) are now treated as CODE from their own pieces even when they
    don't line up with the stored token stream -- ciphertext_appendix.tsv stays the record of what a
    *correct* re-split should look like, but a genuinely code-shaped chunk is never misfiled as PLAIN.
    Single ambiguous one-piece chunks ('a', 'e', 'o' -- real one-letter Portuguese words as well as code
    symbols) still go through the token-list check first, since that is the only signal that disambiguates
    them."""
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
        if not matched and n >= 2 and all(code_shaped(p) for p in pieces):
            # whole-line-coded entry: trust the chunk's own pieces over a stale token-list position
            segs.append(('CODE', pieces))
            matched = True
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
