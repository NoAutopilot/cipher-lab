#!/usr/bin/env python3
"""Merge transcription/p1-p3_ciphertext.tsv into ciphertext.tsv and build key_gloss.tsv from the period glosses.

GAPS163 (3 Oct 2026, account-4). ciphertext.tsv: one row per group, line id 'pN_L' (page, line on that page), the
reconciled sign and its confidence, the gloss copied from the page file. key_gloss.tsv: the 3- and 4-digit nomenclator
values pinned by the letter's own bold-hand glosses (rule 4: C where the gloss is legible and both blind passes read
it, M where it is the reconciler's alone, partly unread, or a pair-gloss split by inference). Codes the 1666 letter
table (key.tsv) already keys are not repeated here. Run with --check to exit 1 if either committed file is stale.
"""
import csv, os, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = ['p1', 'p2', 'p3']

# code -> (value, grade, note). Values from transcription/pN_ciphertext.tsv gloss columns; see NOTES.md GAPS163.
GLOSS = {
    '229': ('[Berlin]', 'C', 'glossed Berlin p2:17, p3:5 (2/2 agree); key 255 (1666) reads 229 = Frankreich: different list, HYPOTHESES.md'),
    '303': ('[alliance]', 'M', 'glossed allian?e p3:26 (one letter unsettled); key 255 reads 303 = Munster (preview read, M): different list'),
    '437': ('[Hertzog]', 'M', 'pair 437 641 under one gloss "Hertzog von Ploen" p3:25 (C as a pair); split between the two codes inferred'),
    '641': ('[von_Ploen]', 'M', 'second code of the pair 437 641, see 437'),
    '447': ('[Kayser]', 'C', 'glossed Kayser p3:26 after a struck word'),
    '601': ('[Dennemarck]', 'C', 'glossed Dennemarck p3:3, p3:17 (2/2 agree)'),
    '602': ('[Konig_in_Dennemarck]', 'M', 'gloss "Der Konig in Dennemarck" p3:1 read by the reconciler only (crop edge); p3:26.3 unglossed'),
    '605': ('[K.Dennemarck]', 'C', 'glossed K. Dennemarck p2:2'),
    '651': ('[Cur_Brandenburg]', 'C', 'glossed Cur Brandenburg p2:3, p2:25 (2/2 agree)'),
    '653': ('[Cur_Brand.]', 'C', 'glossed Cur Brand. p2:9; a second code for Kurbrandenburg (variant, not merged)'),
    '681': ('[Cur_Brandenb.]', 'C', 'glossed Cur Brandenb p3:6; a third code for Kurbrandenburg (variant, or 651 misread; sign M)'),
    '634': ('[Holstein]', 'I', 'unglossed in-line; the marginal gloss "disgustirt / unvertanin / Holstein" beside run 1 (p3:15-17) aligns its third word with the run\'s only nomenclator group before 601: inferred, not read'),
    '690': ('[Bleinenk?l]', 'M', 'glossed Bleinenk?l p1:21 and p2:25 (p2 sign a reconciler override from 650); person, name unidentified'),
    '768': ('[?ueco]', 'M', 'glossed ?ueco / s?cco p3:20 (Sueco?), unsettled'),
    '774': ('[Holland]', 'C', 'glossed Holland p2:28'),
    '775': ('[Gen._Staaten]', 'C', 'glossed Gen. Staden p2:28'),
    '834': ('[Rex_Daniae]', 'C', 'glossed Rex Daniae p3:26'),
    '5756': ('[Franckreich]', 'C', 'glossed Franckreich p3:2; 4-digit group (sign M: 575+6 or 57+56 possible)'),
}


def rows():
    out = []
    for p in PAGES:
        with open(os.path.join(HERE, 'transcription', f'{p}_ciphertext.tsv'), encoding='utf-8') as f:
            for r in csv.DictReader(f, delimiter='\t'):
                out.append([f'{p}_{r["line"]}', r['pos'], r['sign'], r['conf'].strip(),
                            (r.get('gloss') or '').strip(), (r.get('gloss_grade') or '').strip()])
    return out


def render():
    ct = 'line\tpos\tsign\tconf\tgloss\tgloss_grade\n' + ''.join('\t'.join(r) + '\n' for r in rows())
    kg = 'code\tvalue\tgrade\tsource\tnote\n' + ''.join(
        f'{c}\t{v}\t{g}\tletter gloss (bold hand), transcription/pN_ciphertext.tsv\t{n}\n' for c, (v, g, n) in GLOSS.items())
    return {'ciphertext.tsv': ct, 'key_gloss.tsv': kg}


def main():
    check = '--check' in sys.argv
    bad = 0
    for name, text in render().items():
        path = os.path.join(HERE, name)
        if check:
            cur = open(path, encoding='utf-8').read() if os.path.exists(path) else None
            if cur != text:
                print(f'STALE {name}'); bad = 1
        else:
            open(path, 'w', encoding='utf-8').write(text)
            print(f'wrote {name} ({text.count(chr(10)) - 1} rows)')
    sys.exit(bad)


if __name__ == '__main__':
    main()
