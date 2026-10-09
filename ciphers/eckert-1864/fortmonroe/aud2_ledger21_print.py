#!/usr/bin/env python3
"""AUD2-LEDGER-21 (9 Oct 2026, account 4): phrase grep for E278/E289 over three IA djvu texts fetched once to SCRATCH_DIR
(warofrebellion421unit = OR I/42 pt 1; diaryofgideonwel02welluoft = Welles diary vol. 2; cu31924020416180 = Autobiography of George
Dewey, 1913). Usage: aud2_ledger21_print.py SCRATCH_DIR > aud2_ledger21_print.out. A miss is a search result (rule 10)."""
import os, re, sys
P = {
 'warofrebellion421unit': ['Webster', 'few remaining', r'fleet (left|sailed)', r'(left|sailed from) (Hampton Roads|Fort(ress)? Monroe)', 'Ingalls'],
 'diaryofgideonwel02welluoft': ['Dewey', r'court.martial', 'Captain Taylor', r'W\. ?R\. Taylor', r'November 30, Wednesday', r'December [123], '],
 'cu31924020416180': [r'court.martial', 'Taylor', 'Juniata', r'Fort Fisher', r'Agawam'],
}
for vol, pats in P.items():
    t = re.sub(r'\s+', ' ', open(os.path.join(sys.argv[1], vol + '.txt'), errors='ignore').read())
    for p in pats:
        ms = list(re.finditer(p, t, re.I))
        print(f'## {vol}\t{p}\t{len(ms)}')
        for m in ms[:6]:
            print('   ', t[max(0, m.start() - 200):m.end() + 200])
