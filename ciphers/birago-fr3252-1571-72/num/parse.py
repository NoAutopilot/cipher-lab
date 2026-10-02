"""Parse Bourdeau's ct2 notation (also used for f.100r here) into items. BIRAGO-NUM, 2 Oct 2026."""
import re
MARKS = '~-:.+'
def items(text):
    out = []
    for tok in text.split():
        if tok in ('|', 'CLEAR'):
            out.append(('W', tok)); continue
        if tok[0] in 'i1' and len(tok) <= 2 or tok[0].isdigit():
            d = '1' if tok[0] == 'i' else tok[0]
            mark = tok[1:] if len(tok) > 1 else ''
            out.append(('M' if mark else 'D', d + mark)); continue
        if tok.isalpha():
            out.append(('L', tok)); continue
        out.append(('?', tok))
    return out
def digits(its, keep_marked=True):
    return ''.join(v[0] for k, v in its if k == 'D' or (keep_marked and k == 'M'))
