#!/usr/bin/env python3
"""Build the interlinear alignment files for rah-canada-1869 (RAH 9/6958, nº 117/2-3) from the aligner's reading.

The reading below was transcribed by eye from images/10137302.jpg and 10137303.jpg (LANE R R8, 24 Sept 2026),
not reconciled from passA/passB. Each cipher line is paired with the plaintext it enciphers, with the note's
abbreviations expanded as the cipher spells them out (Sr. D. -> Señor Don, S.M. -> Su Magestad, V.M. -> Vuestra
Magestad, A.L.R.P. de VV.MM. -> A los reales pies de Vuestras Magestades). The cipher runs on continuously and does
not break where the clear lines break, so the pairs are by enciphered text, not by page line.

Writes: ciphertext.tsv (line, idx, sign, conf; '/' = word break, '.' ',' = punctuation, not tokens),
plaintext.tsv (Spanish lines as written), plain_votes.tsv (line, pos, value: the plaintext letter each sign is
aligned to), key.tsv (sign -> value, grade H, with counts). Then run: python3 tools/decode_key.py ciphers/rah-canada-1869
Re-running this script must reproduce the committed files byte for byte (--check does that).
"""
import collections, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# private one-character transcription code -> atlas code (glyphs/atlas.md, addendum of 24 Sept 2026 for [g01]-[g11])
CODE = {'+': '[plus]', '~': '[loopn]', 'r': '[dot]', 'U': '[cross]', 'S': '[g01]', 'D': '[bigloop]', 'G': '[g02]',
        'L': '[circledot]', 'Q': '[g03]', 'C': '[dash]', 'F': '[equals]', 'Z': '[loopm]', 'H': '[g04]', 'P': '[g05]',
        'B': '[g06]', 'Y': '[g07]', 'A': '[g08]', 'E': '[g09]', '!': '[g10]', 'V': '[g11]',
        '0': '0', '2': '2', '3': '3', '4': '4', '5': '5', '6': '6', '7': '7', '9': '9'}
PUNCT = {'.': '.', ',': ','}   # '.' here is a punctuation dot; the r sign (also a dot) is written 'r' below

# (line id, cipher as read, plaintext it enciphers, conf notes {word index: 'M'})
LINES = [
 ('p302_c01', 'H9Y !V 3957+0Br+',                          'hoy 15 noviembre'),
 ('p302_c02', 'rU+G~ ~L. S+49r D93 LU7S G93Z~',            'ruega al señor don luis gonza'),
 ('p302_c03', 'L+Z Br~B9, H~G~ LL+G~r ~ 0~39S D+ SU 0~',   'lez bravo haga llegar a manos de su ma'),
 ('p302_c04', 'G+S6~D L~ r+73~, L~ C~r6~ QU+ +3 F9r',      'gestad la reina la carta que en for'),
 ('p302_c05', '0~, D+ 396~. SE +S6~0P~ ~ C93673U~C793',    'ma de nota se estampa a continuacion'),
 ('p302_c06', '+3 L9 CU~L D7SP+3S~r~ U3 A+4~L~D9',         'en lo cual dispensara un señalado'),
 ('p302_c07', '9BS+QU79 ~ SU P~r67CUL~r Y BU+3 ~07G9',     'obsequio a su particular y buen amigo'),
 ('p302_c08', '+L C93D+ D+ L~ C~4~D~',                     'el conde de la cañada'),
 ('p302_c09', 'S+49r~',                                    'señora'),
 ('p302_c10', '6+3G9 +L 0~S ~L69 H939r +3 F+L7C76~r',      'tengo el mas alto honor en felicitar'),
 ('p302_c11', '0UY C9rD7~L0+36+ ~ 5U+S6r~ 0~G+S6~D',       'muy cordialmente a vuestra magestad'),
 ('p302_c12', '+3 +L D7~ D+ SU, S~369. r+76+r~3D9 QU+ +L', 'en el dia de su santo reiterando que el'),
 ('p302_c13', '+3 QU+ PU+D~ H~C+rL9 +3 +S6+ P~7S Y S+3',   'en que pueda hacerlo en este pais y sen'),
 ('p302_c14', '6~D~ 5U+S6r~ 0~G+S6~D +3 +L 6r939 D+',      'tada vuestra magestad en el trono de'),
 ('p302_c15', 'S~3 F+r3~3D9 S+r~ +L 0~S F+L7Z D+',         'san fernando sera el mas feliz de'),
 ('p302_c16', '07 57D~',                                   'mi vida'),
 ('p302_c17', '0+ P+r0769 73D7C~r r+SP+6U9S~0+36+ ~',      'me permito indicar respetuosamente a'),
 ('p302_c18', '5U+S6r~ 0~G+S6~D QUE G~3~ P9r 090+369S',    'vuestra magestad que gana por momentos'),
 ('p302_c19', 'L~ 7D+~ D+ L~ 2US67S70~ r+S6~Ur~C793',      'la idea de la justisima restauracion'),
 ('p302_c20', 'Y QU+ 3~D7+ 0+ ~5+36~2~ +3 D+S+9S D+',      'y que nadie me aventaja en deseos de'),
 ('p302_c21', 'S+r U39 D+ L9S Pr70+r9S QU+ S+ 2U+GU+3',    'ser uno de los primeros que se jueguen'),
 ('p303_c22', 'SU 57D~ P9r LL+5~rL~ ~ F+L7Z 6+r0739',      'su vida por llevarla a feliz termino'),
 ('p303_c23', 'S+49r~',                                    'señora'),
 ('p303_c24', '~L9S r+~L++S P7+S D+ 5U+S6r~S',             'a_los reales pies de vuestras'),
 ('p303_c25', '0~G+S6~D+S Y r+~L F~07L7~ C93 +L',          'magestades y real familia con el'),
 ('p303_c26', '0~S Pr9FU3D9 r+SP+69 Y 5+3+r~C793',         'mas profundo respeto y veneracion'),
]
# signs the plaintext word has no letter for: (line, word index, sign index within word)
EXTRA = {('p303_c24', 1, 5)}   # 'reales' enciphered r e a l e e s: a second [plus] before s

PLAIN = [  # the Spanish clear lines as written (accents not transcribed; ñ kept), page line order
 ('p302_P01', 'Hoy 15 Noviembre'), ('p302_P02', 'Ruega al Sr. D. Luis Gonzalez Bra-'),
 ('p302_P03', 'bo, haga llegar a manos de S. M. la Reina, la'),
 ('p302_P04', 'carta que en forma de nota se estampa a conti-'),
 ('p302_P05', 'nuacion, en lo cual dispensara un señalado obse-'),
 ('p302_P06', 'quio a su particular y buen amigo = El'), ('p302_P07', 'Conde de la Cañada-'),
 ('p302_P08', 'Señora:'), ('p302_P09', 'Tengo el mas alto honor en felicitar'),
 ('p302_P10', 'muy cordialmente a V. M. en el dia de'),
 ('p302_P11', 'su santo; reiterando que el en que pueda'),
 ('p302_P12', 'hacerlo en este pais y sentada V. M. en el'),
 ('p302_P13', 'trono de San Fernando sera el mas feliz'), ('p302_P14', 'de mi vida.'),
 ('p302_P15', 'Me permito indicar respetuosa-'), ('p302_P16', 'mente a V. M. que gana por momentos'),
 ('p302_P17', 'la idea de la justisima restauracion y'), ('p302_P18', 'que nadie me aventaja en deseos de ser'),
 ('p302_P19', 'uno de los primeros que se jueguen su vida'), ('p302_P20', 'por llevarla a feliz termino-'),
 ('p302_P21', 'Señora'),
 ('p303_P01', 'Va-'), ('p303_P02', 'A. L. R. P. de V. V. M. M. y'),
 ('p303_P03', 'Real familia con el mas profun-'), ('p303_P04', 'do respeto y veneracion'),
]


def build():
    ct, votes = [], []
    pairs = collections.defaultdict(collections.Counter)
    for line, cip, plain in LINES:
        cw, pw = cip.split(' '), plain.split(' ')
        assert len(cw) == len(pw), (line, cw, pw)
        idx = 0
        for wi, (c, p) in enumerate(zip(cw, pw)):
            if wi:
                ct.append((line, idx, '/', '')); idx += 1
            signs = [ch for ch in c if ch not in PUNCT]
            extra = [si for (l, w, si) in EXTRA if l == line and w == wi]
            letters = list(p.replace('_', ''))   # '_': the cipher writes these words with no break
            for si in sorted(extra):
                letters.insert(si, None)
            if p == '15':
                letters = ['1', '5']
            assert len(signs) == len(letters), (line, c, p)
            k = 0
            for ch in c:
                if ch in PUNCT:
                    ct.append((line, idx, PUNCT[ch], '')); idx += 1
                    continue
                code = CODE[ch]
                ct.append((line, idx, code, ''))
                if letters[k] is not None:
                    votes.append((line, idx, letters[k]))
                    pairs[code][letters[k]] += 1
                idx += 1; k += 1
    return ct, votes, pairs


def outputs():
    ct, votes, pairs = build()
    out = {}
    out['ciphertext.tsv'] = ('# rah-canada-1869 cipher lines as read by the aligner (R8) from the page images; generated by '
                             'build_align.py.\n# sign: glyphs/atlas.md codes; / = word break, . , = punctuation '
                             '(not tokens)\nline\tidx\tsign\tconf\n' +
                             ''.join(f'{l}\t{i}\t{s}\t{c}\n' for l, i, s, c in ct))
    out['plain_votes.tsv'] = ('# plaintext letter each cipher sign is aligned to (abbreviations expanded as enciphered); '
                              'generated by build_align.py\nline\tpos\tvalue\n' +
                              ''.join(f'{l}\t{i}\t{v}\n' for l, i, v in votes))
    out['plaintext.tsv'] = ('# Spanish clear lines of RAH 9/6958 nº 117/2-3 as written; generated by build_align.py\n'
                            'line\tspanish\n' + ''.join(f'{l}\t{t}\n' for l, t in PLAIN))
    rows = []
    for code, c in sorted(pairs.items(), key=lambda kv: (-sum(kv[1].values()), kv[0])):
        v, n = c.most_common(1)[0]
        other = '; '.join(f'{x} x{m}' for x, m in c.items() if x != v)
        rows.append(f"{code}\t{v}\tH\tinterlinear plaintext\t{n} aligned{'; also aligned to ' + other if other else ''}\n")
    out['key.tsv'] = ('# Key read from the note\'s own interlinear plaintext (grade H); generated by build_align.py\n'
                      'code\tvalue\tgrade\tsource\tnote\n' + ''.join(rows))
    return out


if __name__ == '__main__':
    check = '--check' in sys.argv
    stale = 0
    for name, text in outputs().items():
        p = os.path.join(HERE, name)
        if check:
            if not os.path.exists(p) or open(p, encoding='utf-8').read() != text:
                print('STALE:', name); stale = 1
        else:
            open(p, 'w', encoding='utf-8').write(text)
    sys.exit(stale)
