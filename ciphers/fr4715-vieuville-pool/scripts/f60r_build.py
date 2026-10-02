#!/usr/bin/env python3
"""Build no.37 f.60r's files from the reconciled gloss table and the strong-model pass (GAPS-fr4715-vieuville-pool-2,
2 Oct 2026).

  witness/f60r_glosses_reconciled.tsv  (hand-written reconciliation of witness/f60r_gloss_pass.tsv, f60r_pass_c.tsv and
                                        the worker's own look at the crops: line, group, mark, gloss, grade, witnesses, note)
  witness/f60r_pass_c.tsv              (running transcription per line, [digits|mark]{gloss} tokens)
->
  witness/f60r_pairs.tsv               for tools/interlinear_align.py align: plain_raw = the glosses of the line in order,
                                        cipher_raw = the glossed groups in order (numeric, --floor 1 so every group is a word-code)
  f60r_ciphertext.tsv                  line, pos, token, conf, gloss (w:word for clear words; .NN for a barred/dotted group)
  key_wordcodes_f60r.tsv               sign (.NN), value, grade (C), class, source, note -- one row per glossed code

    python3 ciphers/fr4715-vieuville-pool/scripts/f60r_build.py
"""
import csv, re, os
D = 'ciphers/fr4715-vieuville-pool'
TOK = re.compile(r'\[([0-9?]+)\|(bar|dot|dot2|none|unsure)\](?:\{([^}]*)\})?|(\S+)')

def main():
    gl = list(csv.DictReader((l for l in open(f'{D}/witness/f60r_glosses_reconciled.tsv', encoding='utf-8') if not l.startswith('#')), delimiter='\t'))
    # pairs for interlinear_align
    by_line = {}
    for r in gl:
        if r['gloss'] in ('', '-', '?'): continue
        by_line.setdefault(r['line'], []).append(r)
    with open(f'{D}/witness/f60r_pairs.tsv', 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t'); w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        for line, rows in sorted(by_line.items()):
            w.writerow([line, ' '.join(r['gloss'].replace('?', '') for r in rows), line, ' '.join(r['group'] for r in rows)])
    # ciphertext from pass C
    conf_map = {}
    with open(f'{D}/f60r_ciphertext.tsv', 'w', encoding='utf-8', newline='') as f:
        f.write('# fr4715-vieuville-pool no.37 f.60r, clear lines only (L01-L05, L15-L24, L31): the strong-model pass C (witness/f60r_pass_c.tsv) tokenised;\n')
        f.write('# the two Sonnet passes (f60r_pass_a/b.tsv) read every line at L and are kept as the record of that failure, not merged (GAPS-fr4715-vieuville-pool-2, 2 Oct 2026).\n')
        f.write('# token: w:word = clear word; .NN = barred/dotted word-code group; NN = unmarked digit group; conf = the pass line confidence; gloss = period interlinear word as reconciled.\n')
        w = csv.writer(f, delimiter='\t'); w.writerow(['line', 'pos', 'token', 'conf', 'gloss'])
        glmap = {(r['line'], r['group']): r['gloss'] for r in gl}
        for r in csv.DictReader(open(f'{D}/witness/f60r_pass_c.tsv', encoding='utf-8'), delimiter='\t'):
            pos = 0
            for m in TOK.finditer(r['text']):
                pos += 1
                if m.group(1):
                    tok = ('.' if m.group(2) in ('bar', 'dot', 'dot2') else '') + m.group(1)
                    w.writerow([r['line'], pos, tok, r['conf'], glmap.get((r['line'], m.group(1)), '')])
                else:
                    w.writerow([r['line'], pos, 'w:' + m.group(4), r['conf'], ''])
    # key: key_wordcodes_f60r.tsv = C/M glosses on a single settled group (used by decode.json job 2);
    #      key_wordcodes_f60r_all.tsv = every gloss row incl. L and unsettled groups (for scripts/wordcode_slot_test.py's control)
    for fn, keep in (('key_wordcodes_f60r.tsv', lambda r: r['grade'] in ('C', 'M') and len(r['group']) <= 2),
                     ('key_wordcodes_f60r_all.tsv', lambda r: True)):
        with open(f'{D}/{fn}', 'w', encoding='utf-8', newline='') as f:
            f.write('# Word-code values read from the period interlinear glosses on no.37 f.60r (GAPS-fr4715-vieuville-pool-2, 2 Oct 2026).\n')
            f.write('# grade C = read the same by two witnesses and the worker eye from the period decipherment on this leaf (rule 4); M = legible in part, candidates in the note; L = a few letters. class: person|place|common|conj|unknown.\n')
            f.write('# ' + ('C/M glosses on a settled two-digit group only -- the decode key' if 'all' not in fn else 'every gloss row, for the slot test control only, never for decoding') + '\n')
            w = csv.writer(f, delimiter='\t'); w.writerow(['sign', 'value', 'grade', 'class', 'count', 'source', 'note'])
            seen = {}
            for r in gl:
                if r['gloss'] in ('', '-', '?') or not keep(r): continue
                seen.setdefault(r['group'], []).append(r)
            for k, rows in sorted(seen.items(), key=lambda kv: int(re.sub(r'\D', '', kv[0]) or 0)):
                best = sorted(rows, key=lambda r: 'CML'.index(r['grade']))[0]
                grade = best['grade']
                w.writerow(['.' + k, best['gloss'], grade, best['class'], len(rows), 'f.60r interlinear gloss ' + ','.join(r['line'] for r in rows),
                            '; '.join(sorted(set(r['gloss'] for r in rows))) + ' -- ' + best.get('note', '')])
    print('pairs, ciphertext, key written')

if __name__ == '__main__':
    main()
