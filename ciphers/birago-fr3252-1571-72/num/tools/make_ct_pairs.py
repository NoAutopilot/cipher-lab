"""BIRAGO-NUM-TOOLS (3 Oct 2026): write the two Nov 1571 numerical letters as two-digit code tokens for
tools/key_crossmatch.py, which otherwise sees only Tomokiyo's mark-laden ciphertext.txt as 8 whitespace tokens.
Plain runs are cut by phase.py's pooled hard-EM phase (pooled_tokens.txt, BIRAGO-NUM; stray single digits dropped
as nulls); dotted/marked two-figure groups (BIRAGO-NUM design finding 1) are emitted in place, mark stripped.
Phase is NOT settled (BIRAGO-NUM: 10-30% expected phase error) -- a crossmatch negative on these files is
conditional on it. python3 tools/make_ct_pairs.py  (run from num/)"""
import sys
sys.path.insert(0, '.')
import phase

def is_mark(x):
    return len(x) == 2 and x[0].isdigit() and x[1] in '.:~-+'

def stream(path, cut_runs):
    """Re-walk runs_from's logic, emitting cut plain runs and marked groups in document order."""
    t = open(path).read().split()
    out, cur, grp, ri = [], '', '', 0
    def flush_run():
        nonlocal cur, ri
        if cur:
            toks = cut_runs[ri]; assert ''.join(toks) == cur, (ri, cur, toks); ri += 1
            out.extend(x for x in toks if len(x) == 2)
            cur = ''
    def flush_grp():
        nonlocal grp
        if grp:
            out.append(grp if len(grp) != 1 else grp)  # single marked figure kept as-is
            grp = ''
    for k, x in enumerate(t):
        if x.isalpha() and x not in ('i', 'CLEAR'):
            continue
        nxt = k + 1 < len(t) and is_mark(t[k + 1]); prv = k > 0 and is_mark(t[k - 1])
        if x in ('|', 'CLEAR'):
            flush_run(); flush_grp(); out.append('\n'); continue
        if is_mark(x) or (x == 'i' and (nxt or prv)):
            flush_run()
            grp += '1' if x == 'i' else x[0]
            if len(grp) == 2: flush_grp()
            continue
        flush_grp()
        cur += '1' if x == 'i' else x
    flush_run(); flush_grp()
    assert ri == len(cut_runs), (ri, len(cut_runs))
    return out

def main():
    pooled = [l.split() for l in open('pooled_tokens.txt').read().split('\n')[:48]]
    r1, _ = phase.runs_from('f119_ct2_bourdeau.txt')
    jobs = [('f119_ct2_bourdeau.txt', pooled[:len(r1)], '../../birago-nevers-1571/ciphertext_f119_pairs.txt',
             'f.119 (fr.3251, 13 Nov 1571), Bourdeau ct2 transcription (cyphersolver, MIT / CC BY 4.0)'),
            ('f100_recon.txt', pooled[len(r1):], 'ciphertext_f100_pairs.txt',
             'f.100r (fr.3252 no.67, 8 Jan 1572), BIRAGO-NUM reconciled transcription')]
    for src, cut, dst, what in jobs:
        toks = stream(src, cut)
        lines, cur = [], []
        for x in toks:
            if x == '\n':
                if cur: lines.append(' '.join(cur)); cur = []
            else: cur.append(x)
        if cur: lines.append(' '.join(cur))
        n = sum(len(l.split()) for l in lines)
        hdr = (f'# {what}: two-digit code tokens, derived by num/tools/make_ct_pairs.py (BIRAGO-NUM-TOOLS, 3 Oct 2026)\n'
               f'# phase from num/pooled_tokens.txt (unsettled, ~10-30% phase error); strays dropped; marked groups in place; '
               f'wavy sign / clear text = line break. {n} tokens. Not a transcription: regenerate, do not edit.\n')
        open(dst, 'w').write(hdr + '\n'.join(lines) + '\n')
        print(dst, n, 'tokens', len(lines), 'lines')

if __name__ == '__main__':
    main()
