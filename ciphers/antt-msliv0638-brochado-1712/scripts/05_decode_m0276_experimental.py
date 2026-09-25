import csv

key = {}
grade = {}
for row in csv.DictReader(open('/home/user/cipher-lab/ciphers/antt-msliv0638-brochado-1712/key.tsv'), delimiter='\t'):
    key[row['code']] = row['value']
    grade[row['code']] = row['grade']

def decode(tokens):
    out = []
    for t in tokens:
        t0 = t.rstrip('±')
        if t0 in key:
            out.append((key[t0].upper() if grade[t0]=='C' else key[t0], grade[t0]))
        else:
            out.append(('_', 'U'))
    return out

runs = {
  'run1a': "55 17 12 23".split(),
  'run1b': "14 d f".split(),
  'run1c': "16 17 f f z 12".split(),
  'run1d': "5 z x d 12".split(),
  'run2a': "x z 55 52 15 26 y".split(),
  'run2b': "20 25 f 24".split(),
  'run2c': "3 17 20 a f 19".split(),
  'run2d': "m a d".split(),
}
for name, toks in runs.items():
    dec = decode(toks)
    letters = ''.join(l for l,g in dec)
    grades = ''.join(g for l,g in dec)
    print(f"{name:6s} tokens={toks}")
    print(f"       letters={letters}  grades={grades}")
