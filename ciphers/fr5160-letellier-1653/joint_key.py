#!/usr/bin/env python3
"""Joint key from f.86 + f.88, 24 Sept 2026.

f.86 is aligned to f.87 paragraph 1 (align_f86.segments), f.88 and its canvas 173 tail to f.87 paragraph 2 from
"de Savoye" to "quoy y pense" (split at the clear "mais" and "car ce ne peut"), with the same hard-EM/Viterbi aligner (align_f86.em).

  python3 joint_key.py              joint EM on f.86+f.88; write key_1659.tsv (grade C) and align_f88.tsv; print the
                                    changes against the committed f.86-only key (key_1659_f86only.tsv)
  python3 joint_key.py --holdout    mirror of holdout_f88.py: key from f.88 only, f.86 aligned under it, compared
                                    with a letter-shuffled f.87 paragraph 1 control (seeds 0-4); writes holdout_f86.tsv
"""
import csv, math, random, sys
from collections import Counter, defaultdict
import align_f86 as A


def f88_segments():
    """f.88 (L01-L08) and its tail on canvas 173 (L09-L16), cut at the clear words: T1 "de Savoye ... beaucoup de
    bien" | [mais] | T2 "lalliance ... celle la, et il seroit bon ... la fantesie" | [car ce ne peut] | T3 "estre
    quauoir ... quoy y pense" | [je suis,]. Unread groups ('?') and clear punctuation are left out without a cut."""
    rows = list(csv.DictReader(open('ciphertext_f88.tsv'), delimiter='\t'))
    lines = open('dechiffre_f87.txt').read().split('\n')[14:]
    p2 = ' '.join(lines)
    p2 = p2[p2.index('de Savoye'):p2.index('quoy y pense') + len('quoy y pense')]
    before, after = p2.split('mais', 1)
    mid, tail = after.split('car ce ne peut', 1)
    parts, cur, prev_clear = [], [], False
    for r in rows:
        g = r['group']
        if g == '[je]':
            break
        if g in ('[.]', '[,]') or (g == '?' and 'gutter' not in r['note']):
            continue   # punctuation; a struck-through group
        if g.startswith('['):
            if cur and not prev_clear:
                parts.append(cur); cur = []
            prev_clear = True
            continue
        prev_clear = False
        if g != 'M.r':
            cur.append((r['line'], int(r['pos']), g))
    parts.append(cur)
    assert len(parts) == 3, len(parts)
    return [('T1', parts[0], A.norm(before)), ('T2', parts[1], A.norm(mid)), ('T3', parts[2], A.norm(tail))]


# A group hidden in the binding ('?' with a gutter note) is a wildcard: it may carry 0-4 plaintext letters at half the
# cost of leaving them uncarried, and it never enters the key.
_make_score = A.make_score


def make_score(counts, tot, alpha=0.05):
    s = _make_score(counts, tot, alpha)
    return lambda g, chunk: A.SKIP * len(chunk) / 2 if g == '?' else s(g, chunk)


A.make_score = make_score


def first_part(s88):
    """f.88 L01-L08 only (T1 and the head of T2 to "celle la"), as aligned in the previous joint key."""
    t1, t2, _ = s88
    head = [t for t in t2[1] if t[0] <= 'L08']
    text = t2[2][:t2[2].index('cellela') + len('cellela')]
    return [t1, ('T2', head, text)]


def em_warm(segs, first, iters=40):
    """Warm start: EM on the segments restricted to the groups of `first` (f.86 + f.88 L01-L08, the previous joint key),
    then continue on the full segments from those counts. A cold hard-EM lets a new tail group's first, arbitrary
    assignment reinforce itself (e.g. 4 'c' in "chose" pushed onto 53)."""
    counts, _ = A.em(first, iters=iters)
    counts.pop('?', None)
    tot = Counter({g: sum(c.values()) for g, c in counts.items()})
    res = []
    for it in range(iters):
        score = A.make_score(counts, tot)
        newc, newt, res = defaultdict(Counter), Counter(), []
        for name, toks, text in segs:
            al, _ = A.viterbi([t[2] for t in toks], text, score)
            res.append((name, toks, al))
            for t, a in zip(toks, al):
                newc[t[2]][a] += 1; newt[t[2]] += 1
        if newc == counts:
            break
        counts, tot = newc, newt
    return counts, res


def em_unseeded(segs, iters=40):
    """align_f86.em without the hand seeds (they were read from f.86 and would leak it into an f.88-only key)."""
    saved = A.SEEDS
    A.SEEDS = {}
    try:
        return A.em(segs, iters=iters)
    finally:
        A.SEEDS = saved


def num(g):
    b = g.lstrip('_')
    return (int(b) if b.isdigit() else 999, g.startswith('_'), g)


def write_key(counts, per_folio):
    with open('key_1659.tsv', 'w') as f:
        f.write('code\tvalue\tgrade\tevidence\toccurrences\tother_values\tnote\tev_f86\tev_f88\n')
        for g in sorted(counts, key=num):
            c = counts[g]
            v, n = c.most_common(1)[0]
            tot = sum(c.values())
            other = ','.join(f'{k or "0"}:{m}' for k, m in c.most_common()[1:])
            note = 'conflict' if other and n / tot < 0.75 else ('minor conflict' if other else '')
            if n == 1 and tot == 1:
                note = 'single attestation'
            val = {'#': 'M.', '': '0'}.get(v, v)
            e86 = f'{per_folio["f86"][g][v]}/{sum(per_folio["f86"][g].values())}'
            e88 = f'{per_folio["f88"][g][v]}/{sum(per_folio["f88"][g].values())}'
            f.write(f'{g}\t{val}\tC\t{n}\t{tot}\t{other}\t{note}\t{e86}\t{e88}\n')


def joint():
    s86, s88 = A.segments(), f88_segments()
    old = {r['code']: r for r in csv.DictReader(open('key_1659_f86only.tsv'), delimiter='\t')}
    if '--cold' in sys.argv:
        counts, res = A.em(s86 + s88)
    else:
        counts, res = em_warm(s86 + s88, s86 + first_part(s88))
    counts.pop('?', None)
    per = {'f86': defaultdict(Counter), 'f88': defaultdict(Counter)}
    for name, toks, al in res:
        folio = 'f88' if name.startswith('T') else 'f86'
        for t, a in zip(toks, al):
            if t[2] != '?':
                per[folio][t[2]][a] += 1
    write_key(counts, per)
    with open('align_f86_joint.tsv', 'w') as f:   # f.86 as aligned in the joint EM (the key the readings use)
        f.write('seg\tline\tpos\tgroup\tplain\n')
        for name, toks, al in res:
            if not name.startswith('T'):
                for t, a in zip(toks, al):
                    f.write(f'{name}\t{t[0]}\t{t[1]}\t{t[2]}\t{a}\n')
    with open('align_f88.tsv', 'w') as f:
        f.write('seg\tline\tpos\tgroup\tplain\n')
        for name, toks, al in res:
            if name.startswith('T'):
                for t, a in zip(toks, al):
                    f.write(f'{name}\t{t[0]}\t{t[1]}\t{t[2]}\t{a}\n')
    new = {r['code']: r for r in csv.DictReader(open('key_1659.tsv'), delimiter='\t')}
    changed = [g for g in old if g in new and old[g]['value'] != new[g]['value']]
    added = [g for g in new if g not in old]
    was_conf = [g for g in old if old[g]['note'] == 'conflict']
    resolved = [g for g in was_conf if new[g]['note'] != 'conflict']
    became = [g for g in new if g in old and new[g]['note'] == 'conflict' and old[g]['note'] != 'conflict']
    single_old = sum(1 for g in old if old[g]['note'] == 'single attestation')
    single_new = sum(1 for g in new if new[g]['note'] == 'single attestation')
    fmt = lambda g: f"{g} {new[g]['value']} {new[g]['evidence']}/{new[g]['occurrences']} (f86 {new[g]['ev_f86']}, f88 {new[g]['ev_f88']})"
    print(f'groups: old {len(old)} new {len(new)}; conflicts old {len(was_conf)} new {sum(1 for g in new if new[g]["note"] == "conflict")}; '
          f'single attestations old {single_old} new {single_new}')
    print('value changed:', '; '.join(f"{g} {old[g]['value']}->{fmt(g)}" for g in sorted(changed, key=num)) or 'none')
    print('conflict resolved:', '; '.join(fmt(g) for g in sorted(resolved, key=num)) or 'none')
    print('newly conflict:', '; '.join(fmt(g) for g in sorted(became, key=num)) or 'none')
    print('new groups:', '; '.join(fmt(g) for g in sorted(added, key=num)) or 'none')


def holdout():
    s86, s88 = A.segments(), f88_segments()
    out = []
    for label, counts in (('unseeded', em_unseeded(s88)[0]), ('seeded (seeds read from f.86: leaks, supporting only)', A.em(s88)[0])):
        counts.pop('?', None)
        key = {g: c.most_common(1)[0][0] for g, c in counts.items()}
        tot = Counter({g: sum(c.values()) for g, c in counts.items()})
        score = A.make_score(counts, tot)
        same = keyed = n = 0
        split = Counter()   # seed-group vs other-group matches, since the hand seeds were read from f.86
        rows = []
        for name, toks, text in s86:
            gs = [t[2] for t in toks]
            al, _ = A.viterbi(gs, text, score)
            for t, a in zip(toks, al):
                n += 1
                if t[2] in key:
                    keyed += 1; same += key[t[2]] == a
                    k = 'seed' if t[2] in A.SEEDS else 'other'
                    split[k + '_keyed'] += 1; split[k + '_same'] += key[t[2]] == a
                rows.append((name, t[0], str(t[1]), t[2], key.get(t[2], '?'), a))
        ctl = []
        for seed in range(5):
            r = random.Random(seed); s2 = o2 = 0
            for name, toks, text in s86:
                gs = [t[2] for t in toks]
                al, _ = A.viterbi(gs, ''.join(r.sample(text, len(text))), score)
                s2 += sum(1 for g, a in zip(gs, al) if g in key and key[g] == a)
                o2 += sum(1 for g, a in zip(gs, al) if g in key and g not in A.SEEDS and key[g] == a)
            ctl.append(f'{s2} (other {o2})')
        print(f'[{label}] f.88-only key: {len(key)} groups; f.86 groups {n}, keyed {keyed}, key value = aligned letters {same} '
              f'(seed groups {split["seed_same"]}/{split["seed_keyed"]}, other groups {split["other_same"]}/{split["other_keyed"]}); '
              f'control (shuffled para 1, seeds 0-4): {ctl}')
        if not out:
            out = rows
    with open('holdout_f86.tsv', 'w') as f:
        f.write('seg\tline\tpos\tgroup\tf88_key_value_unseeded\taligned_to_f87_para1\n')
        for r in out:
            f.write('\t'.join(r) + '\n')


if __name__ == '__main__':
    holdout() if '--holdout' in sys.argv else joint()
