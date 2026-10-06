#!/usr/bin/env python3
"""Build the clear-text focus sheet for decode-1162 (D1-DEC1162F, 6 Oct 2026).

Reads ../doubts_R10B.tsv (rows marked stays / read-doubtful / RAISED) and boxes.tsv (word x-range per row, placed by eye
on ruler views of ../../images/clear/*.jpg; row a = upper half of the line crop, b = lower half, c = lower half of the
3-line address crop), writes tiles/<id>_word.png and tiles/<id>_line.jpg, check_contact.png (5 random tiles boxed on
their line images, seed 1162) and focus-sheet.html (self-contained, images embedded, no runtime capability).
Usage: python3 build_focus.py   (run from anywhere)
"""
import base64, csv, html, io, os, random
from PIL import Image, ImageDraw, ImageOps
H = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(H, '..', '..', 'images', 'clear')
KEEP = {'stays', 'read-doubtful', 'RAISED'}

def rows(p):
    with open(p, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def yrange(row, h):
    return {'a': (0, int(h * .62)), 'b': (int(h * .38), h), 'c': (int(h * .5), h)}[row]

doubts = [r for r in rows(os.path.join(H, '..', 'doubts_R10B.tsv')) if r['verdict'] in KEEP]
boxes = rows(os.path.join(H, 'boxes.tsv'))
assert len(doubts) == len(boxes), (len(doubts), len(boxes))
bykey = {(d['page'], d['line'], d['new_text']): d for d in doubts}
assert len(bykey) == len(doubts)
os.makedirs(os.path.join(H, 'tiles'), exist_ok=True)
items = []
for b in boxes:
    d = bykey[(b['page'], b['line'], b['word'])]
    assert d['page'] == b['page'] and d['line'] == b['line'] and d['crop'].startswith(b['crop']), (d, b)
    im = Image.open(os.path.join(IMG, b['crop'] + '.jpg')).convert('L')
    w, h = im.size
    y0, y1 = yrange(b['row'], h)
    x0, x1 = max(0, int(b['x0']) - 25), min(w, int(b['x1']) + 25)
    word = ImageOps.autocontrast(im.crop((x0, y0, x1, y1)))
    word = word.resize((word.width * 2, word.height * 2), Image.LANCZOS)
    line = ImageOps.autocontrast(im.crop((0, y0, w, y1))).convert('RGB')
    ImageDraw.Draw(line).rectangle([x0, 2, x1, y1 - y0 - 3], outline=(220, 0, 0), width=4)
    wp, lp = os.path.join(H, 'tiles', b['id'] + '_word.jpg'), os.path.join(H, 'tiles', b['id'] + '_line.jpg')
    word.save(wp, quality=85); line.save(lp, quality=80)
    ctx = [r for r in rows(os.path.join(H, '..', 'clear_text.tsv')) if r['page'] == d['page'] and r['line'] == d['line']]
    items.append(dict(b, **{k: d[k] for k in ('passA', 'passB', 'verdict', 'new_text', 'note', 'word_in_clear_text')},
                      context=ctx[0]['text'] if ctx else '', wp=wp, lp=lp, box=(x0, y0, x1, y1)))

random.seed(1162)
pick = random.sample(items, 5)
panels = []
for it in pick:
    im = Image.open(os.path.join(IMG, it['crop'] + '.jpg')).convert('RGB')
    ImageDraw.Draw(im).rectangle(it['box'], outline=(220, 0, 0), width=4)
    ImageDraw.Draw(im).text((10, 10), it['id'] + ' ' + it['word'], fill=(0, 0, 255))
    panels.append(im)
cc = Image.new('RGB', (max(p.width for p in panels), sum(p.height for p in panels)), 'white')
y = 0
for p in panels:
    cc.paste(p, (0, y)); y += p.height
cc.save(os.path.join(H, 'check_contact.png'))
print('check tiles:', ' '.join(i['id'] for i in pick))

def b64(p):
    mime = 'image/png' if p.endswith('.png') else 'image/jpeg'
    return 'data:%s;base64,%s' % (mime, base64.b64encode(open(p, 'rb').read()).decode())

e = html.escape
cards = []
for it in items:
    cards.append(f'''<section class="card" data-id="{e(it['id'])}">
<h2>{e(it['id'])} &middot; p.{e(it['page'])} line {e(it['line'])} <span class="tag">{e(it['verdict'])}</span></h2>
<img class="word" src="{b64(it['wp'])}" alt="word crop {e(it['id'])}">
<img class="line" src="{b64(it['lp'])}" alt="line {e(it['line'])}, word boxed in red">
<table><tr><th>Text now</th><td><code>{e(it['new_text'])}</code></td></tr>
<tr><th>Blind pass A</th><td><code>{e(it['passA'])}</code></td></tr>
<tr><th>Blind pass B</th><td><code>{e(it['passB'])}</code></td></tr>
<tr><th>Crop note</th><td>{e(it['note'])}</td></tr>
<tr><th>Line as transcribed</th><td><code>{e(it['context'])}</code></td></tr></table>
<label>Your reading <input type="text" data-k="read"></label>
<label>Sure? <select data-k="conf"><option></option><option>sure</option><option>probable</option><option>cannot tell</option></select></label>
</section>''')
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Modena 1162 word read</title><style>
:root{{--bg:#fbfaf7;--fg:#1d1d1b;--mut:#666;--card:#fff;--line:#ddd;--acc:#a33}}
@media (prefers-color-scheme:dark){{:root:not([data-theme="light"]){{--bg:#161616;--fg:#eee;--mut:#aaa;--card:#222;--line:#444;--acc:#e77}}}}
:root[data-theme="dark"]{{--bg:#161616;--fg:#eee;--mut:#aaa;--card:#222;--line:#444;--acc:#e77}}
body{{background:var(--bg);color:var(--fg);font:16px/1.45 system-ui,sans-serif;margin:0 auto;max-width:980px;padding:16px}}
.card{{background:var(--card);border:1px solid var(--line);border-radius:8px;padding:12px;margin:14px 0}}
h2{{font-size:1.05rem;margin:0 0 8px}} .tag{{color:var(--acc);font-weight:600}}
img{{display:block;max-width:100%;height:auto;background:#fff;margin:6px 0}} img.word{{max-height:220px}}
table{{border-collapse:collapse;width:100%;font-size:.92rem}} th{{text-align:left;color:var(--mut);width:11em;vertical-align:top;padding:2px 6px 2px 0}}
td{{padding:2px 0;word-break:break-word}} label{{display:inline-block;margin:8px 12px 0 0}} input{{width:14em}}
button{{font:inherit;padding:6px 12px}} textarea{{width:100%;height:8em}}
</style></head><body>
<h1>Modena 1162: 22 words for a person's read</h1>
<p>DECODE R1162 (Modena, Amb. Ung. b.2/20 no.6), clear text of the letter, not the cipher. Two blind machine passes and a
reconciliation left these 22 words split. Each card shows the word (top, enlarged) and its line with the word boxed in red.
Abbreviation notation: <code>^</code> superscript, <code>~</code> tilde or macron, <code>?</code> doubtful, <code>[?]</code> unread.
Write what the letters show; leave a box empty when you cannot tell. Card F19 is the month of the date line (February or
September). When done, press the button and send the text below it.</p>
{''.join(cards)}
<p><button id="dump">Make the answer list</button></p><textarea id="out" readonly></textarea>
<script>
const K='m1162-focus';let s={{}};try{{s=JSON.parse(localStorage.getItem(K)||'{{}}')}}catch(e){{}}
document.querySelectorAll('.card').forEach(c=>{{const id=c.dataset.id;c.querySelectorAll('[data-k]').forEach(f=>{{
const k=id+'.'+f.dataset.k;if(s[k])f.value=s[k];f.addEventListener('input',()=>{{s[k]=f.value;try{{localStorage.setItem(K,JSON.stringify(s))}}catch(e){{}}}})}})}});
document.getElementById('dump').onclick=()=>{{const rows=['id\\treading\\tconfidence'];document.querySelectorAll('.card').forEach(c=>{{
const g=k=>c.querySelector('[data-k="'+k+'"]').value.replace(/\\t/g,' ');rows.push(c.dataset.id+'\\t'+g('read')+'\\t'+g('conf'))}});
document.getElementById('out').value=rows.join('\\n')}};
</script></body></html>'''
open(os.path.join(H, 'focus-sheet.html'), 'w').write(page)
print('wrote focus-sheet.html, %d cards, %d bytes' % (len(items), len(page)))
