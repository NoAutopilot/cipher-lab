#!/usr/bin/env python3
"""settle_dup.py -- applies PREREG_dupsettle.md (A3V3-ES132S, 4 Oct 2026): settles the f.89 letter's '?' tokens from the f.93-95
duplicate copy. Reads the frozen pre-settlement alignment (dup_settlements_pre.tsv, dup_align_pre.tsv, written by align_dup.py for
A3V3-ES9396) and the duplicate's blind passes (passes/f9*_passA/B.tsv, run2/decisions_*.tsv); rules R1-R3 and the 50-token control
exactly as the PREREG. Writes dup_settled.tsv (one row per settlement candidate: decision, old and new token) and dup_settle_result.json,
and applies the decisions to ciphertext_f89r/f89v/f90r/f91r.tsv (a dated header line names the settlement; old tokens kept in
dup_settled.tsv). --check: exit 1 if the outputs are stale or a ciphertext file does not carry the settled token at a settled position.
"""
import sys, json, re, random, difflib
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from test0 import load_key, load_lines, dec_tok
from test2 import load_pass

UNPRINTED = {'f89r', 'f89v', 'f90r', 'f91r'}
DUP = ['f93r', 'f93v', 'f94r', 'f94v', 'f95r']
ANCHOR = {'same', 'variant', 'notation'}
NOTATION_DUP = re.compile(r'^(14|0|rum|rom|\{R)')  # duplicate-side forms of align_dup.NOTATION (14, 0, cursive R)
HDR = '# SETTLED (A3V3-ES132S, 4 Oct 2026): f.89 \'?\' tokens settled from the f.93-95 duplicate by settle_dup.py per PREREG_dupsettle.md; old tokens in dup_settled.tsv.'


def agreed_positions():
    """{(page, line, 1-based idx): True if both blind passes wrote the token (equal opcode), as run2/reconcile_dup.py builds the line."""
    out = {}
    for pg in DUP:
        D = {}
        for l in open(HERE / f'run2/decisions_{pg}.tsv', encoding='utf-8'):
            if l.startswith('#') or not l.strip(): continue
            ln, i, dec = (l.rstrip('\n').split('\t') + [''])[:3]
            D[(ln, int(i))] = dec
        A, B = load_pass(HERE / f'passes/{pg}_passA.tsv'), load_pass(HERE / f'passes/{pg}_passB.tsv')
        R = load_lines(HERE / f'ciphertext_{pg}.tsv')
        for ln in sorted(set(A) | set(B)):
            a, b = A.get(ln, []), B.get(ln, [])
            sm = difflib.SequenceMatcher(None, [t.rstrip('?') for t in a], [t.rstrip('?') for t in b], autojunk=False)
            flags = []
            for op, i1, i2, j1, j2 in sm.get_opcodes():
                if op == 'equal': flags += [True] * (i2 - i1); continue
                d = D[(ln, i1 + 1)]
                n = {'A': i2 - i1, 'B': j2 - j1, 'A?': i2 - i1, 'B?': j2 - j1}.get(d, len(d.split()))
                flags += [False] * n
            assert len(flags) == len(R.get(ln, [])), (pg, ln)
            for k, f in enumerate(flags): out[(pg, ln, k + 1)] = f
    return out


def pos(s):
    p, ln, i = s.split(':'); return (p, ln, int(i))


def decide(xpos, x, y, ypos, cls, idx, align, AG):
    """returns (decision, new token or None)."""
    if not AG.get(pos(ypos), False): return ('keep:R1-not-agreed', None)
    if cls in ANCHOR: return ('flag-removed', x.rstrip('?'))
    prev = align[idx - 1][6] if idx > 0 else 'edge'; nxt = align[idx + 1][6] if idx + 1 < len(align) else 'edge'
    if prev not in ANCHOR or nxt not in ANCHOR: return ('keep:R3a-not-isolated', None)
    if NOTATION_DUP.match(y): return ('keep:R3b-notation-form', None)
    return ('replaced', y)


def main():
    key = load_key()
    AG = agreed_positions()
    align = [l.rstrip('\n').split('\t') for l in open(HERE / 'dup_align_pre.tsv', encoding='utf-8') if not l.startswith('#')]
    at = {(r[0], r[3]): k for k, r in enumerate(align)}
    rows, dec = [], {}
    for l in open(HERE / 'dup_settlements_pre.tsv', encoding='utf-8'):
        if l.startswith('#'): continue
        xpos, x, y, ypos, act, kind = l.rstrip('\n').split('\t')
        k = at[(xpos, ypos)]
        if kind != 'unprinted':
            d, new = 'not-applied:teulet-f90v-known-answer', None
        else:
            d, new = decide(xpos, x, y, ypos, align[k][6], k, align, AG)
        rows.append([xpos, x, y, ypos, act, d, new or x])
        if new is not None: dec[pos(xpos)] = (x, new)
    # control: 50 firm f.89 tokens on unprinted pages aligned 1:1 to an unflagged duplicate token
    pop = [k for k, r in enumerate(align) if r[0] != '-' and r[3] != '-' and pos(r[0])[0] in UNPRINTED
           and not r[1].endswith('?') and not r[4].endswith('?')]
    def ctl(ks):
        ch = sum(decide(align[k][0], align[k][1], align[k][4], align[k][3], align[k][6], k, align, AG)[0] == 'replaced' for k in ks)
        return dict(n=len(ks), replaced=ch, unchanged_share=round(1 - ch / len(ks), 4))
    sample = sorted(random.Random(1578).sample(pop, 50))
    C50, Call = ctl(sample), ctl(pop)
    gate = C50['unchanged_share'] >= 0.95
    if not gate:  # PREREG: R3 replacements not applied; only R2 flag removals
        for r in rows:
            if r[5] == 'replaced': r[5] = 'pointer:control-failed'; r[6] = r[1]; dec.pop(pos(r[0]))
    # apply to ciphertext files (positions read against the PRE-settlement tokens)
    outs, grades = {}, {}
    for pg in sorted(UNPRINTED):
        f = HERE / f'ciphertext_{pg}.tsv'
        lines = f.read_text(encoding='utf-8').split('\n')
        before = load_lines(f)
        new = []
        for l in lines:
            if l.startswith('#') or '\t' not in l: new.append(l); continue
            ln, b = l.split('\t', 1); toks = b.split()
            for i in range(len(toks)):
                if (pg, ln, i + 1) in dec:
                    old, nw = dec[(pg, ln, i + 1)]
                    if toks[i] == old: toks[i] = nw
                    elif toks[i] != nw: raise SystemExit(f'position mismatch {pg} {ln} {i+1}: {toks[i]} vs {old}')
            new.append(ln + '\t' + ' '.join(toks))
        if HDR not in new: new.insert(max(k for k, l in enumerate(new) if l.startswith('#')) + 1, HDR)
        outs[f.name] = '\n'.join(new)
        after = {ln.split('\t')[0]: ln.split('\t')[1].split() for ln in new if '\t' in ln and not ln.startswith('#')}
        def g(L):
            ks = [dec_tok(t, key)[1] for v in L.values() for t in v]
            return dict(M=sum(k == 'key' for k in ks), U=sum(k in ('code', 'bad') for k in ks),
                        q=sum(t.endswith('?') for v in L.values() for t in v))
        # 'before' is the pre-settlement file: on --check after applying, rebuild it from dup_settled rows
        grades[pg] = dict(after=g(after))
    cnt = {}
    for r in rows: cnt[r[5]] = cnt.get(r[5], 0) + 1
    readable = sum(1 for r in rows if r[5] in ('flag-removed', 'replaced') and dec_tok(r[6], key)[1] == 'key')
    res = dict(prereg='PREREG_dupsettle.md', candidates=len(rows), decisions=cnt,
               settled_unprinted=sum(r[5] in ('flag-removed', 'replaced') for r in rows),
               settled_now_key_decodable=readable,
               control_50=C50, control_all_firm=Call, control_gate_pass=gate, grades_after_per_page=grades)
    outs['dup_settled.tsv'] = ('# settle_dup.py (A3V3-ES132S): f89_pos f89_tok_old dup_tok dup_pos align_action decision f89_tok_new\n'
                               + '\n'.join('\t'.join(r) for r in rows) + '\n')
    outs['dup_settle_result.json'] = json.dumps(res, indent=1, ensure_ascii=False) + '\n'
    if '--check' in sys.argv:
        stale = [k for k, v in outs.items() if (HERE / k).read_text(encoding='utf-8') != v]
        print('STALE ' + ' '.join(stale) if stale else 'OK: committed outputs match'); sys.exit(1 if stale else 0)
    for k, v in outs.items(): (HERE / k).write_text(v, encoding='utf-8')
    print(json.dumps(res, ensure_ascii=False))


if __name__ == '__main__':
    main()
