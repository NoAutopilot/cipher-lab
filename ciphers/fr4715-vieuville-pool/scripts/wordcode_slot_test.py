#!/usr/bin/env python3
"""Rule-3 test of the f.60r period glosses against no.44's word-code slots (GAPS-fr4715-vieuville-pool-2, 2 Oct 2026).

Statistic: for every no.44 word-code (witness/f67r_wordcodes_context.tsv, a slot class per group read from the clear
French at grade I) whose code is glossed on f.60r (key_wordcodes_f60r.tsv, grade C from the period interlinear
decipherment), does the gloss's class (person/title, place, common word, conjunction) fit the slot class?
REAL = fits / covered. CONTROL = the same count under 20 (default) value-shuffled keys: the gloss values are permuted
among the glossed codes (the shuffle moves which class lands on which code, so the control can vary on the
statistic's own axis -- CLAUDE.md rule 3, bCAS/AX-5799 lesson). Reports REAL, the shuffle mean/max, and how many
shuffles reach REAL.

    python3 ciphers/fr4715-vieuville-pool/scripts/wordcode_slot_test.py [--shuffles 20] [--seed 1]
"""
import argparse, csv, random, re, sys

KEY = 'ciphers/fr4715-vieuville-pool/key_wordcodes_f60r_all.tsv'   # every gloss incl. L/unsettled, so the shuffle has non-person classes to move
SLOTS = 'ciphers/fr4715-vieuville-pool/witness/f67r_wordcodes_context.tsv'

def slot_class(text):
    t = text.lower()
    if 'conjunction' in t: return 'conj'
    if 'place' in t or 'destination' in t: return 'place'
    if 'person' in t or 'title' in t or 'party' in t: return 'person'
    return 'other'

def fits(gloss_class, slot):
    # a person/title gloss fits a person slot; a place gloss fits a place slot; "person or means"/"person or party"
    # slots accept person; a common-word gloss fits nothing but a conjunction slot when it is a conjunction.
    if slot == 'person': return gloss_class in ('person',)
    if slot == 'place': return gloss_class in ('place', 'person')   # "aller [X]" may be to a person's court
    if slot == 'conj': return gloss_class == 'conj'
    return False

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--shuffles', type=int, default=20); ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    key = {}
    for r in csv.DictReader((l for l in open(KEY, encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        key[r['sign']] = (r['value'], r['class'])
    slots = []
    for r in csv.DictReader((l for l in open(SLOTS, encoding='utf-8') if not l.startswith('#')), delimiter='\t'):
        slots.append((r['group'], slot_class(r['context_class']), r['context_before'][-40:], r['context_after'][:40]))
    covered = [(g, s, b, af) for g, s, b, af in slots if g in key]
    def score(mapping):
        return sum(1 for g, s, _, _ in covered if fits(mapping[g][1], s))
    real = score(key)
    print(f'no.44 word-code slots: {len(slots)}; glossed on f.60r: {len(covered)} ({len(set(g for g,_,_,_ in covered))} distinct codes)')
    for g, s, b, af in covered:
        print(f'  {g:5} slot={s:6} gloss={key[g][0]!r:22} class={key[g][1]:7} fit={fits(key[g][1], s)}   ...{b} [{g}] {af}...')
    codes = sorted(key)
    rng = random.Random(a.seed); hits = []
    for _ in range(a.shuffles):
        vals = [key[c] for c in codes]; rng.shuffle(vals)
        hits.append(score(dict(zip(codes, vals))))
    n = len(covered)
    print(f'REAL {real}/{n} = {real/n if n else 0:.3f}; CONTROL {a.shuffles} value-shuffled keys: mean {sum(hits)/len(hits):.2f}/{n}, '
          f'max {max(hits)}/{n}, shuffles >= REAL: {sum(1 for h in hits if h >= real)}/{a.shuffles}')
    if n == 0: sys.exit(2)

if __name__ == '__main__':
    main()
