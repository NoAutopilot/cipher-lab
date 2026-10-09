#!/usr/bin/env python3
"""MANT-ABBO (9 Oct 2026): is a 694/08 leaf's letter printed in Acta Borussica, Behoerdenorganisation I (1894)?
Check 4 only (prior-print grep on OCR text, no image, no decode). Usage:
  python3 abbo_check.py DJVU_DIR [--out abbo_check.tsv] [--check]
DJVU_DIR holds the IA _djvu.txt files (fetched once; ids in VOLS). Printed-item table PRINTED is the list of Manteuffel reports
BO I prints, found by OCR-tolerant search for the name; every anchor must still be found in the djvu (else exit 2).
hit = y (a phrase of the leaf's own inventory note is in the printed text), date (same date +-2 days as a printed report, content
not matched), n. A search result, not a novelty verdict (rule 10). OCR of Fraktur is noisy: 'n' means 'not found by this method'."""
import re, sys, os, datetime as dt

VOLS = {  # id -> (BO volume, covered period from its own title page)
 'diebehrdenorgan01posngoog': ('I', '1701-June 1714'),
 'diebehrdenorgan00posngoog': ('II', 'July 1714-1717'),
 'bub_gb_fnM5AQAAIAAJ': ('II (2nd copy)', 'July 1714-1717'),
 'bub_gb_5nM5AQAAIAAJ': ('III', 'Jan 1718-Jan 1725'),
 'bub_gb_U3Q5AQAAIAAJ': ('IV.1', '1725'),
 'bub_gb_rHQ5AQAAIAAJ': ('IV.2', '1726-1729'),
 'bub_gb_P3Y5AQAAIAAJ': ('VI.2', '1740-1745'),
 'bub_gb_b3Y5AQAAIAAJ': ('VII', '1746-May 1748'),
 'bub_gb_cno5AQAAIAAJ': ('VIII', '1748-1750'),
 'bub_gb_O3s5AQAAIAAJ': ('IX', '1750-1753'),
 'bub_gb_83U5AQAAIAAJ': ('XI', 'later'),
}
# printed Manteuffel reports in BO I for 1712 (anchor = OCR string that must occur; id = BO I Nr.; dates = report dates)
PRINTED = [
 ('Nr.64 pp.204-207', 'Berlin 4. Juni 1712 (full text)', ['1712-06-04'], r'Serlin 4\. 3uni 1712|Serlin\s+4\.\s+3uni'),
 ('Nr.64 fn/text (editor quotes)', '29 May 1712', ['1712-05-29'], r'am 29\. 9Wai 1712'),
 ('Nr.64 fn/text (editor quotes)', '7 Jun 1712 (quote, Grumbkow mercuriale)', ['1712-06-07'], r'am 7\. guni 1712'),
 ('Nr.64 fn/text (editor quotes)', '18 Jun 1712 (quote)', ['1712-06-18'], r'am 18\. 3uni fc\^rieb'),
 ('Nr.64 fn/text (editor quotes)', '25 Jun 1712 (quote)', ['1712-06-25'], r'am 25, Sunt'),
 ('fn p.214 (Nr.65/66)', 'Berlin 12 Sept 1712 (footnote cite)', ['1712-09-12'], r'12\. \(Ecptember 1712'),
 ('Nr.72 pp.256-258', '4 Oct 1712 (quote)', ['1712-10-04'], r'am 4\. October bat'),
 ('Nr.72 pp.256-258', '7 Oct 1712 (quote)', ['1712-10-07'], r'am 7\. Dctober 1712'),
 ('Nr.72 pp.256-258', '20 Oct 1712 (cited, 2 lines)', ['1712-10-20'], r'20\. Cctobcr'),
 ('Nr.72 pp.256-258', '23 Oct 1712 (quote)', ['1712-10-23'], r'am 23\. Dctober'),
 ('Nr.82 (before Nr.83)', 'Berlin 23 Nov 1712', ['1712-11-23'], r'Berlin 23\. Hopembn'),
 ('Nr.83', 'Berlin 3 and 9 Dec 1712', ['1712-12-03','1712-12-09'], r'3\. unb 9\. December 1712'),
 ('Nr.84', 'Berlin 12 Dec 1712, 21 Jan, 5 Feb 1713', ['1712-12-12'], r'Berlin \\2\. Dccember'),
]
# leaves: id -> (date label, [iso dates], direction, note-derived phrase regexes (OCR-tolerant), keywords)
M, F = 'Manteuffel->Flemming', 'Flemming->Manteuffel'
LEAVES = {
 '0108': ('4 Jun 1712 (head of No. 40, per V-MANT0109)', ['1712-06-04'], M, [], []),
 '0109': ('4 Jun 1712 (positive control)', ['1712-06-04'], M, [r'Blaspil', r'Grumbkow'], []),
 '0110': ('after 4 Jun 1712 (undated neighbour of 0109)', [], M, [], []),
 '0088': ('31 May 1712 (No. 35)', ['1712-05-31'], M, [], ['Kurakin']),
 '0114': ('7 Jun 1712', ['1712-06-07'], M, [r'Laverne'], ['Laverne']),
 '0117': ('11 Jun 1712 (endorsement)', ['1712-06-11'], M, [], []),
 '0127': ('14 Jun 1712 (No. 41)', ['1712-06-14'], M, [], []),
 '0213': ('17 Jun 1712 (No. 54?)', ['1712-06-17'], M, [], []),
 '0173': ('2 Jul 1712', ['1712-07-02'], F, [], []),
 '0176': ('2 Jul 1712', ['1712-07-02'], M, [], ['Golowkin', 'Custrin']),
 '0200': ('stamp 152 (~Jul 1712)', [], M, [], ['Laverne', 'Lippe']),
 '0247': ('6 Aug 1712 (No. 63)', ['1712-08-06'], M, [], []),
 '0282': ('stamp 219 (draft; Aug-Sep 1712)', [], 'draft', [], ['Britton']),
 '0318': ('stamp 247 (~Sep 1712)', [], M, [], ['Schlippenbach']),
 '0323': ('stamp 257 (draft; ~Sep 1712)', [], 'draft', [r'Alliance [Dd]eff'], []),
 '0348': ('stamp 274 (draft; ~Sep 1712)', [], 'draft', [], []),
 '0377': ('8 Oct 1712', ['1712-10-08'], F, [], []),
 '0382': ('?7 Oct 1712 P.S. (note reads "le pauvre ... fort malade de chagrin ... rendre ses comptes")', ['1712-10-04','1712-10-07'], M,
          [r'malade de chagrin', r'rendre ses comptes', r'Maillette'], []),
 '0387': ('7 Oct 1712 (to the Count of Fl.)', ['1712-10-07'], M, [r'trembler'], []),
 '0390': ('10 Oct 1712', ['1712-10-10'], M, [], []),
 '0391': ('13 Oct 1712 (P.S. to 0390)', ['1712-10-13'], M, [], []),
 '0398': ('15 Oct 1712', ['1712-10-15'], F, [], []),
 '0408': ('17 Oct 1712', ['1712-10-17'], M, [], []),
 '0423': ('stamp 334 (~Oct 1712)', [], M, [], ['Ahlefeld']),
 '0426': ('23 Oct 1712', ['1712-10-23'], M, [], []),
 '0433': ('stamp 342 (~Oct-Nov 1712)', [], M, [], ['Withworth', 'Whitworth']),
 '0442': ('stamp 349 (~Nov 1712)', [], M, [], ['Wolffrath', 'Mecklenburg']),
 '0447': ('stamp 354 (~Nov 1712)', [], M, [], ['Withworth', 'Marlborough', 'Breton']),
 '0453': ('stamp 361-ish (~late Oct-Nov 1712)', [], M, [r'Stanislas', r'renoncer'], []),
 '0454': ('stamp 361 (~late Oct-Nov 1712)', [], M, [r'Stanislas', r'renoncer'], []),
 '0474': ('stamp 379 (~Nov 1712)', [], M, [], ['Breton', 'Marlborough']),
 '0482': ('Nov 1712 (Flemming side)', [], F, [], []),
 '0485': ('Nov 1712 (ff.384v-385; 0487 cites letter of 12 Nov)', [], M, [], []),
 '0489': ('15 Nov 1712', ['1712-11-15'], M, [], ['Schlippenbach']),
 '0494': ('stamp 395 (~Nov-Dec 1712)', [], M, [], ['Breton', 'Danois']),
 '0499': ('stamp 400 (draft; ~Dec 1712)', [], 'draft', [r'Treve|Tr.ve'], []),
}

def load(d, ident):
    return open(os.path.join(d, ident + '.djvu.txt'), errors='ignore').read()

def pages(t):
    """even-page running heads sit at a line start ('\\n204  Nr. 64. ...'); odd pages are not reliably OCR'd.
    anchors = increasing even numbers, step <= 4."""
    best = []; last = None
    for m in re.finditer(r'\n(\d{3})\s{2,}\S', t):
        n = int(m.group(1))
        if n % 2 or not 2 <= n <= 700: continue
        if last is None or 0 < n - last <= 4:
            best.append((m.start(), n)); last = n
    return best

def page_of(anchors, pos):
    pg = None
    for p, n in anchors:
        if p <= pos: pg = n
        else: break
    return '%s-%s' % (pg, pg + 1) if pg else None

def main():
    d = sys.argv[1]
    out = 'abbo_check.tsv'
    if '--out' in sys.argv: out = sys.argv[sys.argv.index('--out') + 1]
    t1 = load(d, 'diebehrdenorgan01posngoog')
    anc = pages(t1)
    # printed items
    items = []
    for nr, lab, dates, rx in PRINTED:
        m = re.search(rx.replace(' ', r'\s+'), t1)
        if not m:
            print('ANCHOR MISSING', nr, lab, rx); sys.exit(2)
        items.append((nr, lab, [dt.date.fromisoformat(x) for x in dates], m.start()))
    # positive control
    ctl = [i for i in items if i[0].startswith('Nr.64 pp')][0]
    pg = page_of(anc, ctl[3])
    print('positive control 0109: anchor found at', ctl[3], 'page marker', pg, '(expect 204)')
    if pg is None or not pg.startswith('204'): print('CONTROL PAGE OFF'); sys.exit(2)
    # control also: Blaspil/Grumbkow names near it
    near = t1[ctl[3]:ctl[3] + 3000]
    assert 'Blaspil' in near and 'Grumbkow' in near, 'positive control phrases missing'
    rows = []
    for lf, (lab, dates, direc, phr, kws) in LEAVES.items():
        ds = [dt.date.fromisoformat(x) for x in dates]
        hit = 'n'; nrpg = ''; snip = ''
        # phrase hits inside a printed item window (item pos .. +6000)
        for rx in phr:
            for it in items:
                w = t1[it[3] - 1500: it[3] + 6000]
                m = re.search(rx, w)
                if m and lf not in ('0109',):
                    pass
        if lf in ('0108', '0109'):
            hit = 'y'; nrpg = 'AB BO I Nr.64 pp.204-207'; snip = 'Blaspil / Grumbkow report of Berlin 4 June 1712 (control; V-MANT0109 AUDIT)'
        elif lf == '0382':
            m = re.search(r'Le\s+pauvre\s+Kranit\s+est\s+fort\s+malade\s+de\s+chagrin', t1)
            if m:
                hit = 'y'; nrpg = 'AB BO I Nr.72 p.%s' % page_of(anc, m.start())
                snip = re.sub(r'\s+', ' ', t1[m.start():m.start() + 230])
        else:
            # date match
            cand = []
            for it in items:
                for pd in it[2]:
                    for d0 in ds:
                        if abs((pd - d0).days) <= 2: cand.append((it, pd, d0))
            if cand and direc != M:
                nrpg = 'AB BO I %s (printed date within 2 days, but the leaf is %s and BO I prints Manteuffel reports)' % (cand[0][0][0], direc)
                snip = 'direction/draft mismatch: not a date hit'
            elif cand:
                it, pd, d0 = cand[0]
                hit = 'date'
                nrpg = 'AB BO I %s p.%s' % (it[0], page_of(anc, it[3]))
                snip = 'printed report %s; leaf date %s; content not matched (phrase check: %s)' % (it[1], d0, ('none run' if not phr else 'no phrase hit'))
        # keywords across BO I
        kwtxt = []
        for k in kws:
            ms = [m.start() for m in re.finditer(k, t1)]
            kwtxt.append('%s:%d' % (k, len(ms)))
            if ms and hit == 'n':
                inmant = [p for p in ms if any(abs(p - it[3]) < 6000 for it in items)]
                if inmant:
                    hit = 'kw'; nrpg = 'AB BO I near %s' % items[[abs(inmant[0] - it[3]) for it in items].index(min(abs(inmant[0] - it[3]) for it in items))][0]
                    snip = re.sub(r'\s+', ' ', t1[inmant[0] - 100:inmant[0] + 140])
        rows.append((lf, lab, direc, 'BO I', hit, nrpg, snip + ((' | kw ' + ' '.join(kwtxt)) if kwtxt else '')))
    # other volumes: cover check
    ovr = []
    for ident, (v, per) in VOLS.items():
        if ident == 'diebehrdenorgan01posngoog': continue
        try: t = load(d, ident)
        except Exception: ovr.append((ident, v, per, 'missing')); continue
        n_m = len(re.findall(r'[tl][ec]u[fs]{1,2}[ecl]', t)); n_b = len(re.findall(r'Blaspi', t)); n_1712 = len(re.findall(r'1712', t))
        ovr.append((ident, v, per, 'teuff-like %d, Blaspi %d, 1712 %d' % (n_m, n_b, n_1712)))
    with open(out, 'w') as f:
        f.write('# MANT-ABBO (9 Oct 2026, LANE FAMILY-A2h): 694/08 leaves vs Acta Borussica, Behoerdenorganisation I (IA diebehrdenorgan01posngoog _djvu.txt, 1894, covers 1701-June 1714; later volumes start July 1714). Generated by mant0608/abbo_check.py. hit: y = phrase of the leaf matches printed text; date = same date +-2 days as a printed Manteuffel report, content not matched; kw = distinctive clear word occurs in a printed Manteuffel item window; n = not found by this method (OCR of Fraktur is noisy: a search result, not a negative). Page = last printed page marker before the position in the OCR (+-1).\n')
        f.write('leaf\tdate\tdirection\tvolume\thit\tNr_page\tsnippet\n')
        for r in rows: f.write('\t'.join(r) + '\n')
    with open(out.replace('.tsv', '_vols.tsv'), 'w') as f:
        f.write('ident\tBO_volume\tcovers\tsearch (name Manteuffel-like / Blaspi / 1712 counts)\n')
        for r in ovr: f.write('\t'.join(r) + '\n')
    for r in rows: print('\t'.join(r)[:260])
    if '--check' in sys.argv:
        print('check: --check regenerates only from the djvu files; compare with git diff on', out)
main()
