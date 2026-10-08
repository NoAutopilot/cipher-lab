#!/usr/bin/env python3
"""DEPTH-AD (8 Oct 2026): collect u*/summary.json into ../DEPTH-AD-2026-10-08.tsv. Linhares (u04) H(K) is by hand (book code)."""
import csv, json, math, os
H = os.path.dirname(os.path.abspath(__file__))
def lib_split(tok, V):
    m = u = 0.0
    for i, r in enumerate(csv.reader(open(tok, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE)):
        if i == 0 or len(r) < 6: continue
        if r[5] == 'M': m += math.log2(max(2, len(r[4].split('|'))))
        elif r[5] == 'U': u += math.log2(V)
    return round(m, 1), round(u, 1)
def above(d, src='contexts.tsv'):
    out = {}
    p = os.path.join(H, d, src)
    for i, r in enumerate(csv.reader(open(p, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE)):
        if i == 0: continue
        o = out.setdefault((r[0], r[1]), [0, 0, 0]); o[0] += 1; o[1] += r[7] == 'True'; o[2] += r[10] == 'True'
    return out
def cc(d, src='contexts.tsv', only=None):
    hits = [(f'{c}={v} {w}/{n} (flanks {f})', f) for (c, v), (n, w, f) in sorted(above(d, src).items())
            if w >= 2 and (only is None or c in only)]
    cc.flank_ok = any(f >= 2 for _, f in hits)
    return '; '.join(h for h, _ in hits) if hits else 'none'
U = [  # unit, results idx, folder, item, design, corpus, shuffle, tokens file
 ('u01_gramont_f29', 11, 'fr2980-gramont', 'f.29r no.21', 'letter homophonic + nulls + few syllable signs (published key, Tomokiyo/Lasry)', 'fr16', 'all'),
 ('u02_gramont_f30', 38, 'fr2980-gramont', 'f.30r-v no.22', 'as f.29r, key.tsv + key_extension_f30 (11 S signs)', 'fr16', 'all'),
 ('u03_thurloe_P4', 51, 'thurloe-printed', 'P4 Stamford 13 Mar 1655', 'numeral letter cipher + a few code numerals, printed numeral stream (key aligned from P5+P6/P7 print, C)', 'en18', 'classes'),
 ('u04_linhares_m0002', 3, 'antt-linhares-chave', 'm0002', 'dictionary (book) code: page/column/rank + trim subscript, Vieyra 1809', 'pt18 (R only)', 'n/a'),
 ('u05_danzay', 13, 'fr20140-danzay-1557', 'f.35r-36r', 'letter homophonic + nulls + word/name signs (published key, Tomokiyo)', 'fr16', 'all'),
 ('u06_bla', 56, 'huntington-blathwayt-madrid-1728', 'BLA 184+186+191(a)', '4-digit syllabic nomenclator, key rebuilt from period glosses (C)', 'fr18', 'classes'),
 ('u07_wvo5551', 2, 'jan-van-nassau-1572-75', 'WVO 5551', 'letter cipher + nulls + name codes (Lodewijk 1574 table, key_full)', 'de1600', 'classes'),
 ('u08_gravel', 125, 'decode-2678-bnf-colbert127-gravel-1665', 'Gravel 29 Jan 1665', 'number+mark syllabic nomenclator (published 1672 key, Tomokiyo)', 'fr17', 'classes'),
 ('u09_lodewijk4', 60, 'lodewijk-van-nassau-1573-74', 'WVO 4610/4611/4612/4616', 'letter cipher + nulls + name/word codes (key_full aligned from 4613/4615, C)', 'fr16', 'classes'),
 ('u10_lodewijk5797', 0, 'lodewijk-van-nassau-1573-74', 'WVO 5797 22 Oct 1573', 'as WVO 4610 (key_full)', 'de1600', 'classes'),
 ('u11_baluze_chavigny', 189, 'baluze167-davaux-1637', 'Baluze 170 f.229r-v Chavigny 25 Aug 1640', 'syllabic nomenclator, number+mark (published key, Tomokiyo)', 'fr17', 'classes'),
]
NOTE = {
 'u01_gramont_f29': 'alt run passes through M-graded nulls/letters; stat(i) word-segmentation 91 vs shuffle p95 101',
 'u02_gramont_f30': '63 U tokens alone add 289 bits to H(K)',
 'u03_thurloe_P4': 'runs never bridge a printed clear word (--break-lines); bridged across clear words the longest H/C run is 96 letters, still < AD 118; code 67=england above p95 and flanks in both contexts',
 'u04_linhares_m0002': 'H(K) by hand: book identity <= 10^4 candidate dictionaries/editions 13.3 bits + 4 counting conventions (bold-line rule, homograph merge, divider rule, end-trim) 4 bits + M liberties justa 1, cagar log2(10)=3.3, para 1 = 22.6 bits; AD = 1.5*22.6/1.785 = 19.0 letters (10.0 at R 3.4); run 33 > AD while H(K) < 39.3 bits; trims are given by the cipher subscript, not liberties',
 'u05_danzay': '74 U tokens add 348 bits; code LRD=le Roy de Dannemarch 8/8 contexts above p95 on the window, 5/8 on flanks',
 'u06_bla': 'code clause on the window statistic only (53=affaire 2/2), flanks 0/2: borderline; no other code above in 2 contexts',
 'u07_wvo5551': 'no code recurs in the 32 tokens; on-file D3-5551 run (nulls classed as code) read run 6, AD 87.7 at 100 seeds; nulls blanked here, same run',
 'u08_gravel': '15 tokens; no code recurs',
 'u09_lodewijk4': 'reading regenerated from current key_full (v3), 3052 H/C of 4243 = 71.9% (the on-file 62.6% is the DEPTH-REGRADE C 2512 of 4012 basis); 478 U tokens add 2192 bits',
 'u10_lodewijk5797': 'current key_full reading 17 H/C of 73 = 23.3% (on-file 11.1% basis is axmerge3/v2); no code recurs inside 5797; pooled with the four letters (pooled_with_u09/): 153=pfaltzgraf 2 of 3 contexts above p95 (both outside 5797; the 5797 context below on window, above on flanks), 161=landgraf 1 of 2 (5797 context below); the 5550 interlinear contexts the audit cites have no tokens file in the repo',
 'u11_baluze_chavigny': '258 of 366 tokens M (letter signs read with ?): alt run 94 vs AD 524; codes 14:=madame 2/2 and 73==Bavier 2/3 above p95, both with flanks',
}
cols = ['unit', 'results_idx', 'folder', 'item', 'design', 'cipher_class', 'corpus', 'shuffle', 'tokens', 'hcs_pct', 'V', 'distinct_cipher_codes',
        'H_design_bits', 'H_lib_M_bits', 'H_lib_U_bits', 'H_K_bits', 'R', 'AD_letters', 'AD_at_R3_4', 'run_bar_letters', 'run_alt_M_through_letters',
        'code_clause', 'outcome_bar', 'outcome_alt', 'note']
rows = []
for u, idx, folder, item, design, corpus, sh in U:
    s = json.load(open(os.path.join(H, u, 'summary.json')))
    tok = os.path.join(H, u, 'tokens.tsv')
    if u == 'u04_linhares_m0002':
        tok = os.path.join(H, '../../ciphers/antt-linhares-chave/reading_tokens.tsv')
        Hd, M, Uu = 17.3, 5.3, 0.0; HK = 22.6; AD = round(1.5 * HK / s['R'], 1); AD34 = round(1.5 * HK / 3.4, 1)
        ccl = 'n/a (word code; whole-word values)'; V = 'n/a'; dc = 26
    else:
        M, Uu = lib_split(tok, s['V']); Hd, HK, AD, AD34, V, dc = s['H_design'], s['H_K'], s['AD'], s['AD_R3_4'], s['V'], s['distinct_cipher_codes']
        ccl = cc(u)
    flank_ok = cc.flank_ok
    if u == 'u10_lodewijk5797':
        own = {r[2].rstrip('?') for i, r in enumerate(csv.reader(open(tok, encoding='utf-8'), delimiter='\t', quoting=csv.QUOTE_NONE)) if i}
        ccl = 'none in-item; pooled, codes of 5797 only: ' + cc('u10_lodewijk5797/pooled_with_u09', only=own)
    rb, ra = s['primary_run'], s['primary_run_m_through']
    code_ok = ccl not in ('none',) and not ccl.startswith('n/a') and not ccl.startswith('none in-item; pooled: none')
    def outc(run):
        if run > AD: return 'D2 holds (cipher clause)'
        if code_ok:
            q = [] if cc.flank_ok else ['window statistic only, flanks below']
            if u == 'u10_lodewijk5797': q.append('contexts outside the item')
            return 'D2 holds (code clause' + ('; ' + '; '.join(q) if q else '') + ')'
        return 'D1 under the bar'
    rows.append([u, idx, folder, item, design, s['cipher_class'] if u != 'u04_linhares_m0002' else 'all (word code)', corpus, sh, s['tokens'], s['hcs_pct'],
                 V, dc, Hd, M, Uu, HK, s['R'], AD, AD34, rb, ra, ccl, outc(rb), outc(ra), NOTE[u]])
with open(os.path.join(H, '..', 'DEPTH-AD-2026-10-08.tsv'), 'w', encoding='utf-8') as f:
    f.write('\t'.join(cols) + '\n')
    for r in rows: f.write('\t'.join(str(x) for x in r) + '\n')
for r in rows: print(r[0], r[15], r[17], r[19], r[20], '|', r[21][:80], '|', r[22], '|', r[23])
