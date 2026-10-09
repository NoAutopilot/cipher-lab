#!/usr/bin/env python3
"""MANT-CENSUS (9 Oct 2026): writes inv08d.tsv from the sheet key (read after the five sheets were classified), my blind sheet reads
and the eye-check results. Usage: gen_inv08d.py SHEET_KEY_D.TSV SHA.TXT > inv08d.tsv"""
import csv, sys
key = list(csv.DictReader(open(sys.argv[1]), delimiter='\t'))
sha = {l.split()[1][:4]: l.split()[0][:16] for l in open(sys.argv[2])}
m = {'c': 'code', 'p': 'possible', 'n': 'none'}
spec = """1: 1c 2n 3n 4n 5p 6p 7n 8n 9n 10n 11n 12p
2: 1n 2n 3n 4p 5p 6n 7c 8p 9n 10p 11n 12n
3: 1p 2n 3n 4n 5p 6n 7n 8p 9n 10c 11n 12n
4: 1n 2n 3n 4n 5n 6n 7p 8p 9p 10p 11p 12p
5: 1p 2n 3p 4p 5n 6c 7p 8n 9n 10p 11p 12p"""
reads = {}
for line in spec.splitlines():
    s, rest = line.split(':')
    for t in rest.split():
        k = ''.join(ch for ch in t if ch.isdigit()); reads['D%s-%s' % (s.strip(), k)] = m[t[len(k):]]
eye = {  # frame: (code, glossed, density, est_tokens, note) -- eye check at ~1100 px
 '0027': ('y', 'n', 'light', '6-8', 'f.10, Berl. 17 Feb 1712; runs ~12.?.17 and 2?.33.13 at the foot of the right page'),
 '0087': ('y', 'partly', 'light', '12-18', 'stamp 64; runs with 55.44 and 11.60 and a 12.35.60 run in the lower text; small glosses over some'),
 '0089': ('y', 'partly', 'heavy', '100-140', 'stamp 66; digit runs in most lines of both pages (17.1, 55.44, 7.60 and long runs), small words above some'),
 '0103': ('y', 'y', 'medium', '50-70', 'stamp 76; runs with interlinear glosses (a name abbreviation, "Negociation par ...") in the right-page text'),
 '0113': ('y', 'y', 'heavy', '150-220', 'stamp 84; dense runs over the lower half of both pages, marginal and interlinear gloss'),
 '0116': ('y', 'n', 'light', '5', 'stamp 33; one run 17.60.39.21.72 in line 4 of the left page'),
 '0123': ('y', 'n', 'light', '8-12', 'Berl. 11 Jun 1712, stamp 92; runs 17.1.35.44 and 7.60 in the text'),
 '0110': ('y', 'n', 'medium', '60-90', 'f.81, 0109 neighbour; inline groups 7.60 55.44 11.60 1.44 14.23.12.8; ALREADY in abbo_check.tsv (MANT-ABBO), not an unseen frame'),
 '0108': ('?', '?', '', '', 'already seen: head of 0109 (MANT-0109); sheet read only, not eye-checked here'),
}
print('# MANT-CENSUS (9 Oct 2026, LANE FAMILY-A2i account 2): Loc. 694/08 unseen frames 0003-0130 (first 50 of the 190 in frame order; 0108 and 0110 were already in abbo_check.tsv) + planted controls. www.archiv.sachsen.de frames.tsv full-size URLs, 56 requests (50 targets + clear control 0125 + the 5 date-only AB BO frames of the first part), 2.2 s apart, all HTTP 200 image/jpeg; images in scratch only (sha256 prefixes below; re-fetch from images/loc694-08-09/frames.tsv). 5 sheets of 12 tiles (10 targets + a code control + the clear control 0125), sheets_d.py seed 6084, key read after all five were classified. sheet_read = blind read at 600 px; a frame read code or possible was eye-checked at ~1100 px (code column = that result); a sheet "none" is NOT eye-checked (weak evidence: light single codes can be missed).')
print('loc\tframe\tkind\tsheet_label\tsheet_read\tcode\tglossed\tdensity_eye\test_tokens\tnote\thttp\tsha256_16')
for r in key:
    fr = r['frame']; rd = reads[r['label']]
    if r['kind'] == 'target':
        if fr in eye: c, g, d, e, n = eye[fr]
        elif rd == 'possible': c, g, d, e, n = 'n', '-', '', '', 'sheet possible; eye check: no code groups seen at ~1100 px'
        else: c, g, d, e, n = 'n', '-', '', '', 'sheet none; not eye-checked (weak evidence)'
    else:
        c, g, d, e, n = ('y' if r['kind'] == 'control+' else 'n'), '-', '', '', 'planted control (%s), sheet read %s' % (r['kind'], rd)
    print('\t'.join(['694/08', fr, r['kind'], r['label'], rd, c, g, d, e, n, '200 image/jpeg', sha.get(fr, '')]))
