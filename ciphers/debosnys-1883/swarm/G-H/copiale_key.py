"""Knight, Megyesi & Schaefer 2011, Figure 6, restated in the Figure 2 transcription names.
Used only to check that the two public line datasets align; the blind pipeline never reads it."""
KEY = {
 'p.':'a','n.':'a','h.':'a','fem':'a',          # A (fem also Ä)
 'sqp':'b','bas':'c','pi':'d','z':'d',
 'ah':'e','eh':'e','ih':'e','oh':'e','uh':'e','grr':'e','zzz':'e',
 'sqi':'f','del':'g','x.':'g','hd':'h','gam':'h','car':'j','c.':'l','plus':'m',
 'mu':'n','ru':'n','nu':'n','g':'n','tri':'o','o.':'o','no':'ö','d':'p',
 'r.':'r','three':'r','j':'r','bar':'s','grc':'s','lam':'t','ni':'u','ki':'u','grl':'ü',
 'mal':'v','y..':'i','ns':'i','iot':'i','m.':'w','f':'x','inf':'y','s.':'z','cross':'sch','hk':'st','arr':'ch','uu':'en',
}
SPACE = set('a b c ds e f ft gs h i k l m n o p q r s longs t u v w x y zs'.split())
LOGO = set('tri.. o.. star bigx lip nee smil smir gat toe'.split())  # large symbols: logograms, no letter value
def decode(tokens):
    out=[]; prev=''
    for t in tokens:
        if t in SPACE: out.append(' '); continue
        if t==':': out.append(prev[-1:] if prev else ''); continue
        v=KEY.get(t,'?'); out.append(v); prev=v
    return ''.join(out)
