#!/usr/bin/env python3
"""D2-HEIN: find runs of small numbers (1-70) in Heinsius Deel 2 OCR pages (rule in PREREG-D2-HEIN.md).

Usage: small_runs.py [--fetch] PAGE [PAGE ...]   (pages read from deel2_ocr/, fetched once with --fetch)
Prints one TSV row per candidate run: page, start offset, small tokens, codes 140-199, context.
"""
import html, os, re, subprocess, sys, time

D = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'deel2_ocr')
URL = 'https://resources.huygens.knaw.nl/retroapp/service_heinsius/02_163/html/heinsius_02_GS163_%s.html'
UA = 'cipher-lab research script (contact via repository)'
MONTHS = r'jan|januari|janv|janvier|febr|februari|fevr|févr|fevrier|février|maart|mars|maert|april|apr|avril|mei|may|mai|juni|juny|juin|juli|july|juillet|aug|augustus|aoust|août|sept|september|septembre|oct|okt|october|oktober|octobre|nov|november|novembre|dec|december|decembre|décembre|xbris|7bris|8bris|9bris'
UNITS = r'gl|gulden|guldens|fl|rd|rds|rijksd|ryksd|rijksdaelders|ducat|ducaten|dukaten|st|stuyvers|stuivers|pond|livres|ecus|écus|thaler|daelders|mijl|mijlen|uur|uren|dagen|weken|maanden|jaren|man|mannen|bataillon|bataillons|escadron|escadrons|regiment|regimenten|compagnie|compagnien|stukken|schepen|kanonnen|pieces|pièces|e|ste|de'
PRE = re.compile(r'(?:\bpp?\.|\bblz\.|\bnr?s?\.|\bno\.|n°|\bfol\.|\bf\.|\bart\.|§)\s*$', re.I)
NEXTW = re.compile(r'\s*\.?\s*(\w+)', re.U)
FN = re.compile(r'^\s*\d[\d ]{1,5}\.\s+\d+\.')
HEAD = re.compile(r'^\s*\d(?: ?\d){1,4} ?\.\s')

def page_text(p, fetch):
    f = os.path.join(D, 'heinsius_02_GS163_%s.html' % p)
    if not os.path.exists(f):
        if not fetch:
            sys.exit('missing %s (use --fetch)' % f)
        os.makedirs(D, exist_ok=True)
        code = subprocess.run(['curl', '-sS', '-A', UA, '-o', f, '-w', '%{http_code}', URL % p],
                              capture_output=True, text=True).stdout
        time.sleep(2.2)
        if code != '200':
            os.remove(f) if os.path.exists(f) else None
            sys.exit('HTTP %s for page %s' % (code, p))
    raw = open(f, encoding='utf-8', errors='replace').read()
    lines = html.unescape(re.sub(r'<[^>]+>', '', re.sub(r'<br\s*/?>', '\n', raw))).split('\n')
    keep = []
    for i, ln in enumerate(lines):
        if i == 0 and ln.strip().isdigit():
            continue
        if FN.match(ln):
            break                      # footnotes start: drop the rest of the page
        if HEAD.match(ln):
            continue                   # letter heading
        keep.append(ln)
    t = ' '.join(keep)
    t = re.sub(r'(?<![\w\d])(?:1[67]\d\d|1 [67] \d \d)(?![\w\d])', ' YEAR ', t)  # solid or digit-spaced years
    t = re.sub(r'(?<![\w ])(?:\w ){2,}\w(?![\w])', lambda m: m.group().replace(' ', '') if not re.search(r'\d', m.group()) else m.group(), t)
    t = re.sub(r'H\.\s?A\.\s?\d[\d ]*', ' HAREF ', t)
    return t

def runs(t):
    toks = []
    for m in re.finditer(r'(?<![\w\d])\d{1,3}(?![\w\d])', t):
        n = int(m.group())
        nw = NEXTW.match(t, m.end())
        w = nw.group(1).lower() if nw else ''
        small = 1 <= n <= 70 and not PRE.search(t[max(0, m.start() - 8):m.start()]) \
            and not re.fullmatch(MONTHS, w) and not re.fullmatch(UNITS, w) \
            and not re.search(r'(?<![a-z])(?:%s)(?![a-z])' % MONTHS, t[m.end():m.end() + 15].lower()) \
            and '/' not in t[max(0, m.start() - 2):m.end() + 2]
        code = 140 <= n <= 199
        if small or code:
            toks.append((m.start(), n, small))
    out, used = [], -1
    smalls = [x for x in toks if x[2]]
    for i in range(len(smalls) - 2):
        if smalls[i][0] <= used:
            continue
        if smalls[i + 2][0] - smalls[i][0] <= 40:
            j = i + 2
            while j + 1 < len(smalls) and smalls[j + 1][0] - smalls[j][0] <= 40 and smalls[j + 1][0] - smalls[i][0] <= 200:
                j += 1
            a, b = smalls[i][0], smalls[j][0]
            codes = [x[1] for x in toks if not x[2] and a - 40 <= x[0] <= b + 40]
            out.append((a, [x[1] for x in smalls[i:j + 1]], codes, t[max(0, a - 50):b + 50]))
            used = b
    return out

if __name__ == '__main__':
    args = sys.argv[1:]
    fetch = '--fetch' in args
    for p in [a for a in args if not a.startswith('--')]:
        for a, sm, codes, ctx in runs(page_text(p, fetch)):
            print('%s\t%d\t%s\t%s\t%s' % (p, a, ' '.join(map(str, sm)), ' '.join(map(str, codes)), ' '.join(ctx.split())))
