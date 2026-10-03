#!/usr/bin/env python3
"""Person word sheet for no.44 f.67r's remaining L clear-French words (GAPS100-fr4715-vieuville-pool, 3 Oct 2026).

After the GAPS-9 L-word pass (two blind Opus readers + one reconciliation, slot agreement 41/123), f67r_ciphertext.tsv
still carries its clear words at conf L. A further model pass at the same crops is not the next instrument (NOTES.md,
GAPS-9), so this builds a sheet for a person: every run of consecutive L clear words is a numbered slot [Pn] (current
L set, via scripts/f67r_lword_pass.py's slots()); each line shows its crops (images/, relative links) and the line with
the H/M words and cipher groups as context. Under each line a table gives the machine's current L reading and the two
GAPS-9 blind readers' strings for the old slot(s) it overlaps (witness/f67r_lpass_slots.tsv, f67r_lpass_A/B.tsv), as
hints only; the person writes what the image shows.

The person fills the `person` column of witness/f67r_person_answers.tsv (blank = not read; `?` for a letter not read;
`=` = the current reading is right as it stands). --apply then writes the answers into f67r_ciphertext.tsv: `=` moves
the slot's words to H; a different string replaces the slot's words at H with a note giving the old reading; nothing
else (cipher groups, H/M words) is touched. --apply is not run by this worker: no person read exists yet.

  python3 scripts/f67r_person_sheet.py --build      # witness/f67r_person_sheet.md + witness/f67r_person_answers.tsv
  python3 scripts/f67r_person_sheet.py --check      # exit 1 if the committed sheet/answers are stale against the tsv
  python3 scripts/f67r_person_sheet.py --apply witness/f67r_person_answers.tsv [--write]
"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
from f67r_frame_fold import rows, bylines, norm
from f67r_lword_pass import slots, readpass, CT

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W = os.path.join(HERE, 'witness')
SHEET = os.path.join(W, 'f67r_person_sheet.md')
ANS = os.path.join(W, 'f67r_person_answers.tsv')
TAG = 'GAPS100 person read'


def old_slots():
    out = []
    for ln in open(os.path.join(W, 'f67r_lpass_slots.tsv'), encoding='utf-8'):
        p = ln.rstrip('\n').split('\t')
        if p[0].startswith('S') and p[0] != 'slot':
            out.append(dict(id=p[0], line=p[1], words=[norm(w) for w in p[4].split()]))
    return out


def current():
    ss = slots()
    olds = old_slots()
    A = readpass(os.path.join(W, 'f67r_lpass_A.tsv'))
    B = readpass(os.path.join(W, 'f67r_lpass_B.tsv'))
    for i, s in enumerate(ss, 1):
        s['pid'] = 'P%d' % i
        s['text'] = ' '.join(r['token'][2:] for r in s['rows'])
        mine = {norm(r['token'][2:]) for r in s['rows']} - {''}
        hit = [o for o in olds if o['line'] == s['line'] and mine & set(o['words'])]
        s['old'] = ','.join(o['id'] for o in hit)
        s['A'] = ' | '.join(A.get(o['id'], '') for o in hit)
        s['B'] = ' | '.join(B.get(o['id'], '') for o in hit)
    return ss


def render():
    ss = current()
    sid = {(r['line'], r['pos']): s for s in ss for r in s['rows']}
    md = ['# no.44 f.67r -- person word sheet (GAPS100, 3 Oct 2026)', '',
          'BnF Français 4715 f.67r, Montholon, Tours, 15 April 1590. The letter is mostly clear French; the words below',
          'are the ones the machine readers could not settle (conf L). For each [Pn], look at the crops and write what',
          'the hand says into the `person` column of `f67r_person_answers.tsv` (same folder): `=` if the current reading',
          'is right, the corrected words otherwise (period spelling as written, `~` for a tilde/abbreviation mark, `?`',
          'for a letter you cannot read), blank if you skip it. The "current", "reader A" and "reader B" columns are',
          'machine guesses, given as hints only -- the image decides. `<n>` is a cipher group and `<.n>` a marked',
          'word-code; leave those alone. No rush, never blocking: ~%d slots, %d words.' %
          (len(ss), sum(len(s['rows']) for s in ss)), '']
    for line, rs in bylines(rows(CT)).items():
        mine = [s for s in ss if s['line'] == line]
        if not mine:
            continue
        parts, seen = [], set()
        for r in rs:
            s = sid.get((r['line'], r['pos']))
            if s:
                if s['pid'] not in seen:
                    seen.add(s['pid'])
                    parts.append('**[%s]**' % s['pid'])
            else:
                parts.append(r['token'][2:] if r['token'].startswith('w:') else '`<%s>`' % r['token'])
        segs = sorted({k for s in mine for k in s['segs']})
        md.append('## %s' % line)
        md.append('')
        for k in segs:
            md.append('![%s s%d](../images/f67r_%s_s%d.jpg)' % (line, k, line, k))
        md.append('')
        md.append(' '.join(parts))
        md.append('')
        md.append('| slot | crop | current (L) | reader A | reader B |')
        md.append('|---|---|---|---|---|')
        for s in mine:
            md.append('| %s | s%s | %s | %s | %s |' % (s['pid'], ',s'.join(map(str, s['segs'])), s['text'],
                                                       s['A'] or '-', s['B'] or '-'))
        md.append('')
    ans = ['slot\tline\tpositions\tcrops\tcurrent\treaderA\treaderB\told_slots\tperson']
    for s in ss:
        ans.append('\t'.join([s['pid'], s['line'], ','.join(r['pos'] for r in s['rows']),
                              ','.join('f67r_%s_s%d.jpg' % (s['line'], k) for k in s['segs']),
                              s['text'], s['A'], s['B'], s['old'], '']))
    return '\n'.join(md) + '\n', '\n'.join(ans) + '\n', ss


def build():
    md, ans, ss = render()
    open(SHEET, 'w', encoding='utf-8').write(md)
    if os.path.exists(ANS) and any(l.rstrip('\n').split('\t')[-1].strip()
                                   for l in open(ANS, encoding='utf-8').readlines()[1:]):
        sys.exit('refusing to overwrite %s: it carries person answers' % ANS)
    open(ANS, 'w', encoding='utf-8').write(ans)
    print('slots %d, L words %d, lines %d, crops %d' % (len(ss), sum(len(s['rows']) for s in ss),
          len({s['line'] for s in ss}), sum(len(s['segs']) for s in ss)))


def check():
    md, ans, ss = render()
    stale = open(SHEET, encoding='utf-8').read() != md
    cur = [l.rstrip('\n').split('\t')[:-1] for l in open(ANS, encoding='utf-8')]
    stale |= cur != [l.split('\t')[:-1] for l in ans.rstrip('\n').split('\n')]
    print('stale' if stale else 'ok: sheet and answers match f67r_ciphertext.tsv (%d slots)' % len(ss))
    sys.exit(1 if stale else 0)


def apply(path, write=False):
    ss = {s['pid']: s for s in current()}
    got = {}
    for l in open(path, encoding='utf-8').readlines()[1:]:
        p = l.rstrip('\n').split('\t')
        if len(p) >= 9 and p[8].strip():
            s = ss.get(p[0])
            if not s or s['text'] != p[4]:
                sys.exit('%s: slot no longer matches f67r_ciphertext.tsv (rebuild the sheet)' % p[0])
            got[p[0]] = p[8].strip()
    conf = sum(1 for v in got.values() if v == '=')
    print('person answers %d of %d slots: %d confirmed (=), %d corrected' % (len(got), len(ss), conf, len(got) - conf))
    if not write:
        return
    rows_by = {(r['line'], r['pos']): pid for pid, s in ss.items() if pid in got for r in s['rows']}
    keep, out, done = [], [], set()
    for ln in open(CT, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('line\t'):
            keep.append(ln)
    keep.insert(len(keep) - 1, '# %s (scripts/f67r_person_sheet.py --apply): a person\'s read of the L slots from '
                'witness/f67r_person_sheet.md; "=" -> H, a corrected string replaces the slot at H.\n' % TAG)
    for line, rs in bylines(rows(CT)).items():
        pos = 0
        for r in rs:
            pid = rows_by.get((r['line'], r['pos']))
            if pid and got[pid] != '=':
                if pid in done:
                    continue
                done.add(pid)
                for w in got[pid].split():
                    pos += 1
                    out.append([line, str(pos), 'w:' + w, 'H', '%s: %s replaced (old %s)' % (TAG, pid, ss[pid]['text'])])
                continue
            pos += 1
            c, note = r['conf'], r['note']
            if pid:
                c, note = 'H', (note + '; ' if note else '') + TAG + ': confirmed'
            out.append([line, str(pos), r['token'], c, note])
    with open(CT, 'w', encoding='utf-8') as f:
        f.writelines(keep)
        for o in out:
            f.write('\t'.join(o) + '\n')
    print('wrote', CT, '-- now rerun the folder decode --check and rebuild this sheet')


if __name__ == '__main__':
    a = sys.argv
    if '--build' in a:
        build()
    elif '--check' in a:
        check()
    elif '--apply' in a:
        apply(a[a.index('--apply') + 1], '--write' in a)
    else:
        print(__doc__)
