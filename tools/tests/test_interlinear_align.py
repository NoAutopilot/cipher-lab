#!/usr/bin/env python3
"""Offline test for tools/interlinear_align.py align (default mode and --floor/--clear-consumes).
Run: python3 tools/tests/test_interlinear_align.py"""
import csv, os, subprocess, sys, tempfile

TOOL = os.path.join(os.path.dirname(__file__), '..', 'interlinear_align.py')


def run(pairs, *opts):
    d = tempfile.mkdtemp()
    p = os.path.join(d, 'pairs.tsv')
    with open(p, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['plain_line', 'plain_raw', 'cipher_line', 'cipher_raw'])
        w.writerows(pairs)
    a, k = os.path.join(d, 'a.tsv'), os.path.join(d, 'k.tsv')
    subprocess.run([sys.executable, TOOL, 'align', p, a, k] + list(opts), check=True, capture_output=True)
    with open(k) as f:
        return {r['value']: r for r in csv.DictReader(f, delimiter='\t')}


def main():
    # letters 1-120 one letter each, 150 = a name; a clear word "le" written in the cipher line
    pairs = [
        ['1', 'que le conte jean est ici', '1', '16 36 81 le 150 85 26 31 101 71 101'],
        ['2', 'car le conte jean part', '2', '71 61 21 le 150 11 61 21 31'],
        ['3', 'et le conte jean vient', '3', '81 31 le 150 41 101 82 2 31'],
    ]
    key = run(pairs, '--floor', '121', '--clear-consumes')
    assert key['150']['meaning'] == 'contejean', key['150']
    assert int(key['150']['agree']) == 3, key['150']
    assert key['16']['meaning'] == 'q', key['16']
    # without --clear-consumes the clear 'le' takes nothing, so 150 absorbs it at least once
    key0 = run(pairs, '--floor', '121')
    assert key0['150']['meaning'] != 'contejean' or int(key0['150']['agree']) < 3
    # --prior seeds letters below the floor only; a seeded name code in the key file is ignored
    import tempfile as tf
    kp = os.path.join(tf.mkdtemp(), 'k.tsv')
    open(kp, 'w').write('code\tvalue\n16\tq\n36\tu\n81\te\n150\tzzz\n')
    key2 = run(pairs, '--floor', '121', '--clear-consumes', '--prior', kp)
    assert key2['150']['meaning'] == 'contejean', key2['150']

    # --code-prefix (26 Sept 2026, AX2-BRO4): a homophonic single-letter codebook mixing digit and
    # alpha codes, one clear word thrown in. Code 'x' (masked out of --prior) recovers 'c' from the
    # two sentences that both start with 'c', via the digit codes seeded around it.
    cp_pairs = [
        ['1', 'certo el', '1', '@x @2 @3 @1 @4 el'],
        ['2', 'corte', '2', '@x @4 @3 @1 @2'],
        ['3', 'trote', '3', '@1 @3 @4 @1 @2'],
    ]
    kp2 = os.path.join(tempfile.mkdtemp(), 'k.tsv')
    open(kp2, 'w').write('code\tvalue\n1\tt\n2\te\n3\tr\n4\to\n')
    key3 = run(cp_pairs, '--code-prefix', '@', '--clear-consumes', '--prior', kp2)
    assert key3['x']['meaning'] == 'c', key3['x']
    assert key3['1']['meaning'] == 't', key3['1']
    assert key3['4']['meaning'] == 'o', key3['4']

    # --wildcard / --null-cost (27 Sept 2026, fr4715-f61 H11): a markup with one character per sign, dashes
    # for unread signs. Code @n is always dashed (a null); @c/@a/@t carry letters. With the dashes kept as
    # wildcards and nulls free, @n takes only dashes (no meaning row) and @t reads t in all three lines.
    wc_pairs = [
        ['1', '-ca-t', '1', '@n @c @a @n @t'],
        ['2', 'ta-c-', '2', '@t @a @n @c @n'],
        ['3', '-a-t-c', '3', '@n @a @n @t @n @c'],
    ]
    key4 = run(wc_pairs, '--code-prefix', '@', '--wildcard', '-', '--null-cost', '0')
    assert 'n' not in key4, key4.get('n')
    assert key4['t']['meaning'] == 't' and int(key4['t']['agree']) == 3, key4['t']
    assert key4['c']['meaning'] == 'c' and int(key4['c']['agree']) == 3, key4['c']
    # the Thurloe default (dashes stripped, null -3) mis-assigns at least one of these codes
    key5 = run(wc_pairs, '--code-prefix', '@')
    assert 'n' in key5 or key5['t']['meaning'] != 't' or key5['c']['meaning'] != 'c', key5

    # --max-chunk / --seg-bonus / --len-prior (2 Oct 2026, NEXT-PAG): a syllabic code, two letters per code,
    # chunks not on word boundaries. With the length prior and a 4-letter cap, 1=la 2=pr 3=in 4=ce recover.
    sy_pairs = [
        ['1', 'la prince', '1', '1 2 3 4'],
        ['2', 'prince la', '2', '2 3 4 1'],
        ['3', 'ce la', '3', '4 1'],
        ['4', 'in ce', '4', '3 4'],
    ]
    key6 = run(sy_pairs, '--floor', '1', '--max-chunk', '4', '--seg-bonus', '0.5', '--len-prior', '0.5')
    for code, want in (('1', 'la'), ('2', 'pr'), ('3', 'in'), ('4', 'ce')):
        assert key6[code]['meaning'] == want, (code, key6[code])
    assert all(len(r['meaning']) <= 4 for r in key6.values()), key6
    # the Thurloe defaults (14-letter chunks, word-boundary bonus 1.0, no length prior) do not
    key7 = run(sy_pairs, '--floor', '1')
    assert [key7[c]['meaning'] for c in '1234'] != ['la', 'pr', 'in', 'ce'], key7
    # --digits 4 --word-prior (GAPS8 janssens, 2 Oct 2026): four-digit word codes, each once, against a plain copy;
    # a word prior from the gloss places them; a gloss value the plain copy does not support moves (1135 forte->force)
    wp_pairs = [['1', 'La force navale ennemie augmentee', '1', '739 1135 1183 1128 562']]
    d = tempfile.mkdtemp()
    kp = os.path.join(d, 'prior.tsv')
    with open(kp, 'w') as f:
        f.write('code\tvalue\n739\tLa\n1135\tforte\n1183\tnavale\n1128\tennemie\n562\taugmente\n')
    key8 = run(wp_pairs, '--floor', '0', '--digits', '4', '--prior', kp, '--word-prior')
    assert key8['1183']['meaning'] == 'navale' and key8['1128']['meaning'] == 'ennemie', key8
    assert key8['1135']['meaning'] == 'force', key8
    # without --digits 4 the four-digit groups are 'doubtful' and carry no value in the key
    key9 = run(wp_pairs, '--floor', '0', '--prior', kp, '--word-prior')
    assert '1183' not in key9, key9
    # --keep-fs: 7 reads f, 8 reads s; the default OCR fold merges both into s
    fs_pairs = [['1', 'fa sa', '1', '7 1 8 1'], ['2', 'fa sa fa', '2', '7 1 8 1 7 1'],
                ['3', 'sa fa', '3', '8 1 7 1']]
    keyf = run(fs_pairs, '--floor', '100', '--keep-fs')
    assert keyf['7']['meaning'] == 'f' and keyf['8']['meaning'] == 's', keyf
    # one sign 9 written over f twice and s once: kept apart it shows the conflict, folded it does not
    mix = [['1', 'fa', '1', '9 1'], ['2', 'fa', '2', '9 1'], ['3', 'sa', '3', '9 1']]
    km = run(mix, '--floor', '100', '--keep-fs')
    assert km['9']['agree'] == '2' and km['9']['others'] == 's:1', km
    kd = run(mix, '--floor', '100')
    assert kd['9']['agree'] == '3' and kd['9']['others'] == '', kd
    # --code-chunk 2 (JM-ALPHA, 4 Oct 2026): a prefixed sign @S standing for the syllable 'en' between clear words;
    # with the default (0-1 letters) it can never read 'en'
    cc_pairs = [['1', 'que en el', '1', 'que @S el'], ['2', 'de en la', '2', 'de @S la'],
                ['3', 'yo en su', '3', 'yo @S su']]
    kc = run(cc_pairs, '--code-prefix', '@', '--clear-consumes', '--code-chunk', '2', '--null-cost', '0')
    assert kc['S']['meaning'] == 'en', kc
    kc1 = run(cc_pairs, '--code-prefix', '@', '--clear-consumes', '--null-cost', '0')
    assert kc1.get('S', {}).get('meaning') != 'en', kc1
    # --word-code-prefix %: a word code missing from the table (%k) learns its word from the plain text
    wc2 = [['1', 'que alla en el', '1', 'que %k @S el'], ['2', 'de alla en la', '2', 'de %k @S la']]
    kw = run(wc2, '--code-prefix', '@', '--word-code-prefix', '%', '--clear-consumes', '--code-chunk', '2',
             '--null-cost', '0')
    assert kw['%k']['meaning'] == 'alla' and kw['S']['meaning'] == 'en', kw
    print('ok')


if __name__ == '__main__':
    main()
