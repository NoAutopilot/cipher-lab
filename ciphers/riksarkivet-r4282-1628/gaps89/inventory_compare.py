#!/usr/bin/env python3
"""GAPS89: R4284 cipher-body sign inventory vs R4282's 34 reconciled sign labels (disk only, no reading).

Inputs: ../r4284_transcription_bourdeau.txt (the two numeric-body sections; the letter-cipher strip at the end
is excluded -- it is the key-test strip GAPS79/GAPS85 already used), ../tx2/ciphertext_reconciled.tsv (R4282,
GAPS38, 1,090 signs), ../r4284_leaf/passC_reconciled.tsv (the R4284 key-test strip, GAPS79, letter-shape signs).
Statistic: shared sign labels and the share of R4282's tokens those labels cover. Controls that can differ on
that axis: the R4284 key-test strip (a letter-shape cipher on the same leaf; high overlap expected if the
statistic works) and the earlier key-record overlaps on file (4307 p.4, 4327, 4263, 4275). A second, design-level
statistic: the share of body tokens that are multi-glyph numbers (R4282 has none: every token is one sign).
--check exits non-zero if results.json is stale.
"""
import csv, json, re, sys, collections, os
H = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(H)

def r4284_body():
    toks, on = [], False
    for line in open(os.path.join(P, 'r4284_transcription_bourdeau.txt'), encoding='utf-8'):
        if line.startswith('## '):
            on = 'numeric' in line or 'left page' in line
            continue
        if not on or line.startswith('#'):
            continue
        line = line.split('(sic')[0]
        line = re.sub(r'\[[^\]]*\]', ' ', line)
        for t in line.split():
            t = t.rstrip('?')
            if t.isdigit():
                toks.append(t)
    return toks

def main():
    body = r4284_body()
    r82 = collections.Counter(r['sign'] for r in csv.DictReader(open(os.path.join(P, 'tx2/ciphertext_reconciled.tsv')), delimiter='\t'))
    strip = collections.Counter()
    for r in csv.DictReader(open(os.path.join(P, 'r4284_leaf/passC_reconciled.tsv')), delimiter='\t'):
        for s in r['codes'].split():
            strip[s] += 1
    n82 = sum(r82.values())
    glyphs = collections.Counter(ch for t in body for ch in t)
    codes = collections.Counter(int(t) for t in body)
    single = {d: codes[d] for d in range(10) if codes[d]}
    def share(labels):
        lab = sorted(set(labels) & set(r82))
        return {'shared_labels': lab, 'n_shared': len(lab), 'r4282_tokens_covered': sum(r82[l] for l in lab),
                'r4282_coverage': round(sum(r82[l] for l in lab) / n82, 4)}
    caps = [l for l in r82 if l.isupper()]
    res = {
        'r4282': {'tokens': n82, 'labels': len(r82), 'multi_glyph_token_share': 0.0,
                  'digit_labels': sorted(l for l in r82 if l.isdigit()), 'capital_labels': sorted(caps)},
        'r4284_body': {'tokens': len(body), 'distinct_codes': len(codes), 'code_min': min(codes), 'code_max': max(codes),
                       'multi_glyph_token_share': round(sum(1 for t in body if len(t) > 1) / len(body), 4),
                       'glyph_inventory': dict(sorted(glyphs.items())), 'single_digit_codes': single,
                       'letter_or_capital_signs': 0,
                       'vs_r4282_glyph_level': share(glyphs),
                       'vs_r4282_as_standalone_single_digit_codes': share(str(d) for d in single),
                       'r4282_capitals_reached': sorted(set(caps) & set(glyphs))},
        'control_r4284_keytest_strip': {'tokens': sum(strip.values()), 'labels': len(strip), **share(strip)},
        'control_key_records_on_file': {'4307p4': '16 shared signs / 456 tokens (GAPS3)',
                                        '4327': '7 shared signs (GAPS)', '4263': '5-9 shared signs / 121-221 tokens (GAPS30)',
                                        '4275': '4-7 shared signs / 81-157 tokens (GAPS27)'},
    }
    out = json.dumps(res, indent=1, ensure_ascii=False) + '\n'
    f = os.path.join(H, 'results.json')
    if '--check' in sys.argv:
        if not os.path.exists(f) or open(f).read() != out:
            print('results.json stale'); sys.exit(1)
        print('results.json current'); return
    open(f, 'w').write(out); print(out)

main()
