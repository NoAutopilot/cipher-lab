#!/usr/bin/env python3
"""TXE3-8 SHEET (PREREG-txeng3-8.md; runs PREREG-txeng2-21 SHEET-H2 as registered): the sheet-form test on Birago 1572
no.87 dev_tune (f178v L01-L12), arm P = pictured sheet (sign_sheet_blind_1572.png + blind_pass_brief_1572.md as is),
arm T = the same 51 cells as a value-blind text list (sheet_text_1572.md + brief_T.md, byte-identical but for the sheet).

  python3 run.py prep RUN       # RUN in P1 P2 T1 T2: scratch dirs r/RUN_{A,B}{1,2}/ (crops L01-06 | L07-12, sheet, task.txt)
  python3 run.py reconcile RUN  # read.tsv x4 -> reads/RUN_pass{A,B}.tsv; reconcile_passes --keep-alts; queue; packets p/RUN_P??/
  python3 run.py assemble RUN   # packets' out.tsv -> outputs/passZ_RUN.tsv + adjud_out_RUN.tsv
  python3 run.py score RUN      # the ONE tx_bench call (refuses to run twice) -> scores/RUN.txt

Readers and adjudicators see only scratch copies (no repository path). Eval lines L13-L23 are never copied or named.
"""
import csv, os, re, shutil, subprocess, sys
from collections import Counter, OrderedDict
R = '/home/user/cipher-lab'
HERE = os.path.dirname(os.path.abspath(__file__))
SCR = '/tmp/claude-0/-home-user-cipher-lab/9eed2e56-8724-5863-8815-a1a0c2fa2241/scratchpad'
CROPS = R + '/ciphers/nevers-birago-fr3251-1572/harvest/f178v'
PNG = R + '/ciphers/nevers-birago-fr3251-1572/harvest/sign_sheet_blind_1572.png'
TXT = HERE + '/sheet_text_1572.md'
DEV = ['L%02d' % i for i in range(1, 13)]
CHUNKS = {'1': DEV[:6], '2': DEV[6:]}
OVERLAP = ('Each crop is one horizontal segment (s1, s2, s3, left to right) of one manuscript line, upscaled 2x; segments overlap by '
           'about 100 px at the 2x scale (50 px native), so a sign at the right edge of one segment and the left edge of the next is ONE sign.')


def arm(run): return run[0]
def sheet_path(run, d): return os.path.join(d, 'sign_sheet_blind_1572.png' if arm(run) == 'P' else 'sheet_text_1572.md')
def sheet_line(run, d):
    if arm(run) == 'P':
        return 'Sign sheet (a PICTURE of the sign inventory: 51 cells labelled T10..T98, each one sign of this hand; view it first and use ONLY its labels): ' + sheet_path(run, d)
    return 'Sign list (a TEXT LIST of the sign inventory: 51 cells labelled T10..T98, one shape description each; read it first and use ONLY its labels): ' + sheet_path(run, d)


def copy_crops(lines, d):
    out = []
    for ln in lines:
        for s in (1, 2, 3):
            fn = 'f178v_%s_s%d.jpg' % (ln, s); assert ln in DEV, ln
            shutil.copy(os.path.join(CROPS, fn), os.path.join(d, fn)); out.append(os.path.join(d, fn))
    return out


def prep(run):
    brief = open(HERE + '/brief_%s.md' % arm(run)).read()
    for p in 'AB':
        for c in '12':
            d = os.path.join(SCR, 'r', '%s_%s%s' % (run, p, c)); os.makedirs(d, exist_ok=True)
            shutil.copy(PNG if arm(run) == 'P' else TXT, sheet_path(run, d))
            crops = copy_crops(CHUNKS[c], d)
            lines = ' '.join(CHUNKS[c])
            task = ('You are a blind reader in a transcription test. Follow the brief below exactly. Read ONLY the files listed here; '
                    'do not open, list or search any other file or directory.\n\n' + sheet_line(run, d) +
                    '\n\nCrops (in order; three overlapping segments s1, s2, s3 per line):\n' + '\n'.join(crops) +
                    '\n\nYou read lines %s only (passage ids as the line ids: %s). The page is cipher throughout.\n\n'
                    'Output file: %s/read.tsv\n\nWhen done, reply with the short paragraph the brief asks for (counts only, no sign values beyond cell labels).\n\n---- BRIEF ----\n\n' % (lines, lines, d) + brief)
            open(os.path.join(d, 'task.txt'), 'w').write(task)
            print(d)


def load_read(fn):
    """read.tsv (passage pos sign_id alt conf note) -> OrderedDict line -> [(sign, alt, conf)]; runs L03.1/L03.2 joined in order."""
    runs = {}
    with open(fn, newline='') as f:
        for r in csv.DictReader((l for l in f if l.strip()), delimiter='\t'):
            ln, _, run = r['passage'].strip().partition('.')
            s = (r.get('sign_id') or '').strip()
            if not s: continue
            c = ((r.get('conf') or 'M').strip().upper()[:1]) or 'M'; c = c if c in 'HML' else 'M'
            runs.setdefault((ln, int(run or 0)), []).append((int(r['pos']), s, (r.get('alt') or '').strip(), c))
    out = OrderedDict()
    for k in sorted(runs):
        out.setdefault(k[0], []).extend((s, a, c) for _, s, a, c in sorted(runs[k]))
    return out


def reconcile(run):
    for p in 'AB':
        rows = OrderedDict()
        for c in '12':
            d = os.path.join(SCR, 'r', '%s_%s%s' % (run, p, c))
            shutil.copy(d + '/read.tsv', HERE + '/reads/%s_%s%s_raw.tsv' % (run, p, c))
            for ln, seq in load_read(d + '/read.tsv').items():
                assert ln in CHUNKS[c], (run, p, c, ln); rows.setdefault(ln, []).extend(seq)
        with open(HERE + '/reads/%s_pass%s.tsv' % (run, p), 'w') as f:
            f.write('line\tpos\tsign\talt\tconf\n')
            for ln in DEV:
                for i, (s, a, c) in enumerate(rows.get(ln, []), 1): f.write('f178v_%s\t%d\t%s\t%s\t%s\n' % (ln, i, s, a, c))
        print(p, sum(len(v) for v in rows.values()), 'signs on', len(rows), 'lines')
    rd = HERE + '/rec/' + run; os.makedirs(rd, exist_ok=True)
    out = subprocess.run([sys.executable, R + '/tools/reconcile_passes.py', HERE + '/reads/%s_passA.tsv' % run, HERE + '/reads/%s_passB.tsv' % run,
                          '--keep-alts', '--out-dir', rd], capture_output=True, text=True)
    print(out.stdout[-1500:], out.stderr[-800:])
    draft = {}
    for r in csv.DictReader(open(rd + '/ciphertext_draft.tsv'), delimiter='\t'):
        draft.setdefault(r['line'], {})[int(r['position'])] = r['sign']
    q = []
    for kind, fn in (('disagree', 'disagreements.tsv'), ('uncertain', 'uncertain.tsv')):
        for r in csv.DictReader(open(rd + '/' + fn), delimiter='\t'):
            c = int(r['col']); d = draft[r['line']]
            cands = [r['A'], r['B']] if kind == 'disagree' else [r['A']]
            cands = ' | '.join(x if x != '-' else '(no sign)' for x in cands)
            L = ' '.join(d[i] for i in range(c - 3, c) if i in d); Rr = ' '.join(d[i] for i in range(c + 1, c + 4) if i in d)
            q.append((r['line'], c, kind, cands, L, Rr))
    q.sort(key=lambda x: (x[0], x[1]))
    with open(HERE + '/packets/%s_queue.tsv' % run, 'w') as f:
        f.write('line\tcol\tkind\tcandidates\tleft_neighbours\tright_neighbours\n')
        for x in q: f.write('\t'.join(map(str, x)) + '\n')
    dis = [x for x in q if x[2] == 'disagree']
    print(len(q), 'queue rows,', len(dis), 'disagree')
    tmpl = open(HERE + '/adjud_task_template.txt').read()
    for i in range(0, len(dis), 16):
        P = 'P%02d' % (i // 16 + 1); pk = dis[i:i + 16]
        d = os.path.join(SCR, 'p', '%s_%s' % (run, P)); os.makedirs(d, exist_ok=True)
        shutil.copy(PNG if arm(run) == 'P' else TXT, sheet_path(run, d))
        lines = sorted({x[0] for x in pk}); crops = copy_crops([l.replace('f178v_', '') for l in lines], d)
        with open(d + '/queue.tsv', 'w') as f:
            f.write('line\tcol\tkind\tcandidates\tleft_neighbours\tright_neighbours\n')
            for x in pk: f.write('\t'.join(map(str, x)) + '\n')
        shutil.copy(d + '/queue.tsv', HERE + '/packets/%s_%s_queue.tsv' % (run, P))
        open(d + '/task.txt', 'w').write(tmpl.replace('{SHEET}', sheet_line(run, d)).replace('{LINES}', ', '.join(lines))
                                         .replace('{CROPS}', ', '.join(crops)).replace('{N}', str(len(pk))).replace('{DIR}', d).replace('{OVERLAP}', OVERLAP))
        print(P, len(pk), lines, d)


def assemble(run):
    rd = HERE + '/rec/' + run; rdr = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
    dis = {(r['line'], int(r['col'])): r for r in rdr(rd + '/disagreements.tsv')}
    adj = {}
    for P in sorted(os.listdir(os.path.join(SCR, 'p'))):
        if not P.startswith(run + '_'): continue
        d = os.path.join(SCR, 'p', P); shutil.copy(d + '/out.tsv', HERE + '/packets/%s_out.tsv' % P)
        pq, po = rdr(d + '/queue.tsv'), rdr(d + '/out.tsv')
        assert [(r['line'], r['col']) for r in pq] == [(r['line'], r['col']) for r in po], P
        for r in po: adj[(r['line'], int(r['col']))] = dict(r, packet=P.split('_')[1])
    assert set(adj) == set(dis), ('row sets differ', len(adj), len(dis))
    cls = {}
    for k, a in adj.items():
        s = a['sign'].strip(); A, B = dis[k]['A'], dis[k]['B']
        cls[k] = 'NONE' if s.upper() == 'NONE' else 'A' if s == A else 'B' if s == B else 'other'
    out, changed, pos = [], 0, {}
    for r in rdr(rd + '/ciphertext_draft.tsv'):
        k = (r['line'], int(r['position'])); s, c = r['sign'], r['confidence']
        if k in adj:
            if cls[k] == 'NONE': continue
            ns = adj[k]['sign'].strip(); changed += ns != s; s, c = ns, (adj[k]['conf'].strip() or 'M')
        pos[k[0]] = pos.get(k[0], 0) + 1; out.append((k[0], pos[k[0]], s, c))
    with open(HERE + '/outputs/passZ_%s.tsv' % run, 'w') as f:
        f.write('# TXE3-8 SHEET-H2 run %s: arm %s, two blind Opus 5.5 passes + reconcile_passes --keep-alts + Sonnet packets (PREREG-txeng3-8)\nline\tpos\tsign\tconf\n' % (run, arm(run)))
        for x in out: f.write('\t'.join(map(str, x)) + '\n')
    with open(HERE + '/adjud_out_%s.tsv' % run, 'w') as f:
        f.write('line\tcol\tpacket\tA\tB\tverdict\tclass\tconf\tviewed\tnote\n')
        for k in sorted(dis, key=lambda k: (k[0], k[1])):
            a = adj[k]; f.write('\t'.join([k[0], str(k[1]), a['packet'], dis[k]['A'], dis[k]['B'], a['sign'].strip(), cls[k], a['conf'].strip(), a['viewed'].strip(), (a.get('note') or '').strip()]) + '\n')
    print('passZ_%s %d signs; disagree %d viewed-yes %d; classes %s; conf %s; changed vs draft %d' % (
        run, len(out), len(adj), sum(a['viewed'].strip() == 'yes' for a in adj.values()), dict(Counter(cls.values())), dict(Counter(a['conf'].strip() for a in adj.values())), changed))


def score(run):
    fn = HERE + '/scores/%s.txt' % run
    if os.path.exists(fn): sys.exit('refusing: %s already scored once' % run)
    cmd = [sys.executable, R + '/tools/tx_bench.py', HERE + '/outputs/passZ_%s.tsv' % run, HERE + '/reads/%s_passA.tsv' % run, HERE + '/reads/%s_passB.tsv' % run,
           '--bench', R + '/BENCHMARK-TX.tsv', '--item', 'birago1572-no87', '--coverage-diagnostic', '--exclude-flagged', '--strict',
           '--paired', R + '/benchmark-tx/txeng/units/labels_dev_tune.tsv']
    out = subprocess.run(cmd, capture_output=True, text=True, cwd=R)
    open(fn, 'w').write(' '.join(cmd) + '\n\n' + out.stdout + out.stderr)
    for l in out.stdout.splitlines():
        if ('<-' in l) or ('confus' in l.lower()): continue  # truth values stay in the file, not on the worker's screen
        print(l)


if __name__ == '__main__':
    {'prep': prep, 'reconcile': reconcile, 'assemble': assemble, 'score': score}[sys.argv[1]](sys.argv[2])
