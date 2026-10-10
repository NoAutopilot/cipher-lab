"""THUR-V57: bm/v57_groups.tsv + the folder's known windows (index.tsv) + the image looks below -> bm/census_v5v7_all.tsv.
python3 bm/v57_final.py [--check]. Gloss: yes(image) only where a leaf was read; yes(ocr-probable) where the OCR detector or a 'decipher' word fired;
known = inside a folder P-window (not re-classed); else unknown (OCR rows of an interlinear print are not separable from numeral rows: see NOTES)."""
import csv, io, os, sys
H = os.path.dirname(os.path.abspath(__file__))
IMG = {  # (vol, line_first): (leaf, printed page read, note)   all leaves read by eye on strip crops (bm/v57crops/)
 ('7', 38856): ('n434', 'p.427', 'Downing, numeral rows with a smaller clear interlinear gloss line under each (Sweden/Dutch ambassador)'),
 ('7', 2323): ('n33', 'p.26~', 'Downing, spaced-letter interlinear gloss rows between numeral rows'),
 ('7', 11068): ('n137', 'p.130~', 'Downing, interlinear gloss rows (Portugal business)'),
 ('7', 15854): ('n188', 'p.181~', 'Downing, interlinear gloss words (Don John, French embassador)'),
 ('7', 48328): ('n522', 'p.515~', 'Downing, interlinear gloss rows (lord protector fleet, Nieuport); leaf matched by estimated page and content, line-to-leaf not proven'),
 ('7', 80371): ('n881', 'p.874 (Vol. lxvii p.290)', 'Downing envoy to Thurloe, interlinear gloss rows'),
 # THUR-V7LOOK (10 Oct 2026): leaves read by eye on strip crops (bm/v7lookcrops/); page = printed page number read on the header strip
 ('7', 37197): ('n420', 'p.413', 'Fauconberg to H. Cromwell (heading read on the leaf; OCR headingless): numeral rows each over a letter-by-letter gloss row; group located by span between the heading l.36387 and l.37730, not matched row by row'),
 ('7', 37263): ('n420', 'p.413', 'same Fauconberg letter as l.37197: letter-by-letter gloss rows; located by span, not matched row by row'),
 ('7', 37730): ('n421', 'p.414', 'top of p.414, end of the same Fauconberg letter (dated Sept. 28 1658): letter-by-letter gloss rows; OCR text "uffe rn oaddi ti ont oth" matches the strip; Clarges heading follows at l.37758'),
 ('5', 15486): ('n184', 'p.179', 'Montagu to Thurloe, 3 July 1656: whole-word and spaced-letter gloss over code runs (Mr. Burrell, interest, commands); the OCR page estimate 130 was wrong'),
 ('7', 27331): ('n319', 'p.312', 'Downing: whole-word and syllable gloss over numeral runs (Portugal ambassador, John Marlow)'),
 ('7', 38068): ('n425', 'p.418', 'Downing: phrase gloss rows above numeral runs (k. of Swede, relieve Copenhagen)'),
 ('7', 14646): ('n173', 'p.166', 'Downing, resident in Holland: gloss words over every code run (Fr. amb., Dr. Witt)'),
 ('7', 22027): ('n259', 'p.252', 'Downing: phrase gloss over code runs (Flanders, Dunkirk, Sir John Marlow)'),
 ('7', 19680): ('n234', 'p.227 and n235 p.228', 'Downing: gloss over code runs (Spa water; De Witt, Hemphlit); cipher mostly on p.228'),
 ('7', 40158): ('n447', 'p.440', 'Downing, Hague Oct 1658: phrase gloss over code runs (king of Sweden, Mufcovy); group continues past the strip read'),
 ('7', 39378): ('n438', 'p.431 (digit partly cut)', 'Downing, Hague 8br 18 1658 [N.S.], signed G. Downing: nearly the whole page numeral rows with phrase gloss rows; located by date and heading, not row by row'),
 ('7', 10092): ('n127', 'p.120', 'Downing letter (heading above the strip not read); p.120 numeral rows each with a gloss phrase; OCR l.10264 "I fent into Flanders" matches the strip; located by that phrase'),
 ('7', 10264): ('n127', 'p.120', 'same page as l.10092: gloss phrase under each code run ("that he will write")'),
 ('7', 82957): ('n909', 'p.902~', 'Downing, interlinear gloss rows (war between England and this state)'),
}
def main():
    idx = [r for r in csv.DictReader(open(os.path.join(H, '..', 'index.tsv')), delimiter='\t')]
    win = []
    for r in idx:
        v = {'collectionofstat05thur': '5', 'collectionofstat07thur': '7'}.get(r['identifier'])
        if v and '-' in r['window_lines']:
            a, b = map(int, r['window_lines'].split('-')); win.append((v, a, b, r['row']))
    out = []
    for r in csv.DictReader(open(os.path.join(H, 'v57_groups.tsv')), delimiter='\t'):
        v, a, b = r['vol'], int(r['line_first']), int(r['line_last'])
        kn = [w[3] for w in win if w[0] == v and b >= w[1] - 5 and a <= w[2] + 5]
        img = IMG.get((v, a))
        if kn: g, ev, note = 'known', 'folder', 'in folder window ' + '/'.join(kn) + '; not re-classed'
        elif img: g, ev, note = 'yes', 'image', 'leaf %s %s: %s' % img
        elif r['detector'] != 'no' or r['decipher_words']: g, ev, note = 'yes', 'ocr', 'OCR flag: %s %s (probable, not image-read)' % (r['detector'], r['decipher_words'])
        else: g, ev, note = 'unknown', 'ocr', 'no flag; numeral_lines %s, alternating gloss-like lines %s (detector not separable from interlinear print, see NOTES)' % (r['numeral_lines'], r['alt_lines'])
        out.append(dict(vol=r['vol'], djvu_line='%s-%s' % (r['line_first'], r['line_last']), page=r['page'], leaf=img[0] if img else '',
                        heading=r['heading'], date=r['date'], agent=r['agent'], key4166=r['key4166'], numerals=r['numerals'],
                        gloss=g, evidence=ev, note=note))
    buf = io.StringIO(); w = csv.DictWriter(buf, list(out[0]), delimiter='\t', lineterminator='\n'); w.writeheader(); w.writerows(out)
    p = os.path.join(H, 'census_v5v7_all.tsv')
    if '--check' in sys.argv:
        if not os.path.exists(p) or open(p).read() != buf.getvalue(): print('STALE'); sys.exit(1)
        print('ok'); return
    open(p, 'w').write(buf.getvalue())
    import collections; print(collections.Counter((o['gloss'], o['evidence']) for o in out))
main()
