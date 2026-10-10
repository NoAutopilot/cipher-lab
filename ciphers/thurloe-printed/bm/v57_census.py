"""THUR-V57: classify vol 5/7 hit groups (bm/v57_hits.tsv) by agent and OCR gloss evidence. Pure text; no decoding.
python3 bm/v57_census.py [--check]  (B146_CACHE as b146/sweep57.py) -> bm/v57_groups.tsv (OCR-evidence columns; agent/key by heading rules)"""
import csv, os, re, sys, io
HERE = os.path.dirname(os.path.abspath(__file__)); C = os.environ['B146_CACHE']
ID = {'5': 'collectionofstat05thur', '7': 'collectionofstat07thur'}
AGENTS = [  # (heading regex, agent, 4166 key section)
 (r'Down[il]?[ni]?[fng]|Dowjiing|Downifig', 'Downing', 'R4896/R4895 f.113-116'),
 (r'Blank|Marf|Marsh', 'Blank Marshall', 'R4897 f.117'),
 (r'Meadow|Medow', 'Meadowe', 'R4890 f.102-103'),
 (r'Fauc[oe]|Faueon', 'Fauconberg', 'none (Fauconberg-H.Cromwell, folder P16-P24)'),
 (r'Lockh|Lpckh', 'Lockhart', 'none in 4166 (folder key_lockhart)'),
 (r'Jeph[fs]|Jcph|Jepb', 'Jephson', 'none in 4166'),
 (r'Mount?agu|Montagu|Blake', 'Montagu/Blake', 'R4883-R4885 (folder P8-P14)'),
 (r'Barwick|Hyde|Maffey|Massey|Mafley|Maflcy', 'Barwick/Massey-Hyde (royalist)', 'R4886 Hyde f.92-93 (undecoded per Tomokiyo)'),
 (r'Sidney|Sydney', 'Sidney', 'R4902 f.124-125 (different code per Tomokiyo)'),
 (r'Monck|Monke', 'Monck', 'R4899 f.120 (army list; name lead only)'),
 (r'Steele', 'Steele', 'none in 4166 (folder key_steele)'),
 (r'Cromwell|Coote|Broghill|Swift|Barkftead|Gookin|Bampfyl|Stayner|Daviffon|Morland|Errington|Corker|Rowe|Gerbier', 'other English', 'none'),
]
def agent(h):
    for pat, a, k in AGENTS:
        if re.search(pat, h, re.I): return a, k
    return ('unattributed' if not h.strip() or 'to' not in h else 'other (' + h[:30] + ')'), 'none'
def stats(lines, a, b):
    seg = lines[a - 1:b]
    num = [i for i, l in enumerate(seg) if sum(1 for t in l.split() if re.match(r'^\d{1,4}[.,;:\-]?$', t)) >= 6]
    def free(j): return 0 <= j < len(seg) and seg[j].strip() and not re.search(r'\d', seg[j]) and len(seg[j].split()) >= 3
    alt = sum(1 for i in num if free(i - 1) or free(i + 1))
    txt = ' '.join(lines[max(0, a - 400):b + 40])
    words = sorted(set(m.lower() for m in re.findall(r'de-?\s?c[iy]\s?ph\w*|dec\s?y\s?ph\w*|the\s+same\s+de\w+', txt, re.I)))
    return len(num), alt, ';'.join(words)[:60]
def main():
    L = {v: open(os.path.join(C, i + '_djvu.txt'), encoding='utf-8', errors='ignore').read().split('\n') for v, i in ID.items()}
    known = {('5', 'P25')}
    out = []
    for r in csv.DictReader(open(os.path.join(HERE, 'v57_hits.tsv'), encoding='utf-8'), delimiter='\t'):
        a, b = int(r['line_first']), int(r['line_last'])
        ag, key = agent(r['heading'])
        nl, alt, dw = stats(L[r['vol']], a, b)
        out.append(dict(vol=r['vol'], page=r['page'], line_first=a, line_last=b, heading=r['heading'][:60], date=r['date'][:30], agent=ag, key4166=key,
                        numerals=r['numerals'], numeral_lines=nl, alt_lines=alt, decipher_words=dw, detector=r['printed_decipherment']))
    cols = list(out[0]); buf = io.StringIO(); w = csv.DictWriter(buf, cols, delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(out)
    p = os.path.join(HERE, 'v57_groups.tsv')
    if '--check' in sys.argv:
        if not os.path.exists(p) or open(p).read() != buf.getvalue(): print('STALE'); sys.exit(1)
        print('ok'); return
    open(p, 'w').write(buf.getvalue()); print(len(out), 'groups')
main()
