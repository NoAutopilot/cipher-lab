#!/usr/bin/env python3
"""VIV-DECH3 (14 Oct 2026, PREREG-VIVDECH3.md): three-vote merge of the blind reads of the clerk decipherment pages.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/vote3.py            # write dec_<page>_merged3.txt and the *_norm3.txt streams
    python3 ciphers/fr16104-vivonne-spain-1572/tx/vote3.py --check    # exit 1 if any written file is stale
    python3 ciphers/fr16104-vivonne-spain-1572/tx/vote3.py --stats    # per-page agreement of pass C with A and B (prints only)

Rule (registered): A and B aligned word by word as tx/merge_dec.py does (difflib on merge_dec.norm); C aligned to A and to B the same way;
a word of A (B) is C-supported when it lies in an 'equal' block of the A-C (B-C) alignment. equal A=B block: A's words, agreed.
replace block: the side with more C-supported words (tie: merge_dec's doubt rule, ties to A), each word agreed iff C-supported.
delete / insert block: the words kept, each agreed iff C-supported. A word carrying '?' is never agreed. A page with no pass C
(tx/dec_<page>_passC.txt absent): merge_dec's two-vote rule unchanged (only equal-block words agreed).
`cmap` (page -> page whose pass C is used) is the PREREG's wrong-page null; it is used in memory only.
"""
import difflib, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import merge_dec as md  # noqa: E402

STREAMS = {  # stream file (two-vote, existing) -> pages in order; the three-vote twin is <name>3.txt
    'dec_norm.txt': ('f105v', 'f106r', 'f106v', 'f107r', 'f107v', 'f108r', 'f108v'),
    'dec67_norm.txt': ('f205r', 'f205v'),
    'dec67b_norm.txt': ('f206r', 'f206v'),
}
C_PAGES = ('f205r', 'f205v', 'f206r', 'f206v', 'f108r', 'f108v')
NULL_CMAP = {'f205r': 'f206v', 'f205v': 'f205r', 'f206r': 'f205v', 'f206v': 'f206r', 'f108r': 'f108v', 'f108v': 'f108r'}


def words(page, q):
    p = os.path.join(HERE, 'dec_%s_%s.txt' % (page, q))
    if not os.path.exists(p):
        return None
    ls = [l for l in open(p, encoding='utf-8').read().splitlines() if l.strip()]
    return [w for w in ' \n '.join(ls).split(' ') if w]


def supported(wx, wc):
    sm = difflib.SequenceMatcher(None, [md.norm(w) for w in wx], [md.norm(w) for w in wc], autojunk=False)
    s = set()
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            s.update(range(i1, i2))
    return s


def merge(page, cmap=None, stats=None):
    """[(word, agreed)] for one page under the three-vote rule (two-vote if no pass C)."""
    wa, wb = words(page, 'passA'), words(page, 'passB')
    wc = words((cmap or {}).get(page, page), 'passC')
    sm = difflib.SequenceMatcher(None, [md.norm(w) for w in wa], [md.norm(w) for w in wb], autojunk=False)
    sA = supported(wa, wc) if wc else set()
    sB = supported(wb, wc) if wc else set()
    out = []
    st = {'disputes': 0, 'to_A': 0, 'to_B': 0, 'neither': 0}
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == 'equal':
            out += [(w, True) for w in wa[i1:i2]]
            continue
        st['disputes'] += 1
        if op == 'replace':
            na = sum(1 for i in range(i1, i2) if i in sA)
            nb = sum(1 for j in range(j1, j2) if j in sB)
            if wc and na != nb:
                side = 'A' if na > nb else 'B'
            else:
                side = 'A' if md.doubt(wa[i1:i2]) <= md.doubt(wb[j1:j2]) else 'B'
            if not wc or na == nb == 0:
                st['neither'] += 1
            else:
                st['to_' + side] += 1
            if side == 'A':
                out += [(wa[i], wc is not None and i in sA) for i in range(i1, i2)]
            else:
                out += [(wb[j], wc is not None and j in sB) for j in range(j1, j2)]
        elif op == 'delete':
            out += [(wa[i], wc is not None and i in sA) for i in range(i1, i2)]
            st['to_A' if any(i in sA for i in range(i1, i2)) else 'neither'] += 1
        else:
            out += [(wb[j], wc is not None and j in sB) for j in range(j1, j2)]
            st['to_B' if any(j in sB for j in range(j1, j2)) else 'neither'] += 1
    if stats is not None:
        stats[page] = st
    return [(w, ag and '?' not in w) for w, ag in out]


def text(ws):
    return ' '.join(w for w, _ in ws).replace(' \n ', '\n').replace('\n ', '\n')


def stream(name, cmap=None):
    """(normalized letter string, per-letter agreed mask) of a three-vote stream."""
    txt, mask = '', []
    for p in STREAMS[name]:
        ws = merge(p, cmap)
        page = md.norm(text(ws))  # whole-page normalization, as merge_dec writes the streams ({del:...} groups span words)
        wt, wm = '', []
        for w, ag in ws:
            n = md.norm(w)
            wt += n
            wm += [ag] * len(n)
        pm = [False] * len(page)  # per-word mask mapped onto the page letters as the builders' clerk_mask does
        for a, b, size in difflib.SequenceMatcher(None, wt, page, autojunk=False).get_matching_blocks():
            for t in range(size):
                pm[b + t] = wm[a + t]
        txt += page
        mask += pm
    return txt, mask


def outputs():
    files = {}
    for p in C_PAGES:
        if words(p, 'passC') is not None:
            files['dec_%s_merged3.txt' % p] = text(merge(p)) + '\n'
    for name in STREAMS:
        files[name.replace('.txt', '3.txt')] = stream(name)[0] + '\n'
    return files


def cstats():
    for p in C_PAGES:
        wa, wb, wc = words(p, 'passA'), words(p, 'passB'), words(p, 'passC')
        if wc is None:
            print('%s: no pass C' % p)
            continue
        real = lambda ws: [w for w in ws if w != '\n']
        nA, nB, nC = len(real(wa)), len(real(wb)), len(real(wc))
        cA = sum(1 for i in supported(wa, wc) if wa[i] != '\n')
        cB = sum(1 for j in supported(wb, wc) if wb[j] != '\n')
        sm = difflib.SequenceMatcher(None, [md.norm(w) for w in wa], [md.norm(w) for w in wb], autojunk=False)
        eqA = [i for op, i1, i2, j1, j2 in sm.get_opcodes() if op == 'equal' for i in range(i1, i2) if wa[i] != '\n']
        sA = supported(wa, wc)
        st = {}
        merge(p, stats=st)
        s = st[p]
        print('%s: words A %d B %d C %d; C agrees with A %d (%.3f of A), with B %d (%.3f of B); on A=B words C agrees %d/%d (%.3f); '
              'A/B disputes %d -> C sides with A %d, B %d, neither %d'
              % (p, nA, nB, nC, cA, cA / nA, cB, cB / nB, sum(1 for i in eqA if i in sA), len(eqA),
                 sum(1 for i in eqA if i in sA) / max(1, len(eqA)), s['disputes'], s['to_A'], s['to_B'], s['neither']))


def main():
    if '--stats' in sys.argv:
        cstats()
        return
    files = outputs()
    if '--check' in sys.argv:
        stale = [n for n, w in files.items() if not os.path.exists(os.path.join(HERE, n)) or open(os.path.join(HERE, n), encoding='utf-8').read() != w]
        print('stale: ' + ', '.join(stale) if stale else 'ok: %d files current' % len(files))
        sys.exit(1 if stale else 0)
    for n, w in files.items():
        open(os.path.join(HERE, n), 'w', encoding='utf-8').write(w)
        print('wrote tx/' + n)


if __name__ == '__main__':
    main()
