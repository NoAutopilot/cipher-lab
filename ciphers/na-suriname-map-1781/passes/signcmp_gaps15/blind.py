import json,random,sys
from PIL import Image, ImageDraw
S=sys.argv[1]
c1=json.load(open(S+'/cc1.json')); c2=json.load(open(S+'/cc2.json')); t0=json.load(open(S+'/tiles.json'))
def cc(d,reg,i): f,lst=d[reg]; return f,tuple(lst[i])
Q={'g_e3':cc(c1,'e',3),'g_f8':cc(c1,'f',8),'g_m':cc(c2,'mg',1),'g_61':cc(c1,'b61',8),'q_e5':cc(c1,'e',5),
'y_a2':cc(c1,'a',2),'y_a9':cc(c1,'a',9),'ud_a3':cc(c1,'a',3),'b_b2':cc(c1,'b',2),'b_l4':cc(c1,'l',4),
'th_a0':cc(c1,'a',0),'th_m1':cc(c1,'m',1),'th_f4':cc(c1,'f',4),'hb_f0':cc(c1,'f',0),'lad_61':cc(c1,'b61',6),
'MM_61':cc(c2,'mm61',2),'xd_61':cc(c2,'mm61',3)}
K='images/inv86_0003_left_native.jpg'
R={k:(v[0],tuple(v[1])) for k,v in t0.items() if k.startswith('R_') and k!='R_Ok'}
R['R_Ax']=(K,(410,465,475,530)); R['R_Fw']=(K,(300,1060,385,1140))
rng=random.Random(20261002)
qk=list(Q); rng.shuffle(qk); rk=list(R); rng.shuffle(rk)
key={'queries':{f'Q{i+1}':[k,*Q[k]] for i,k in enumerate(qk)},'refs':{f'R{i+1}':[k,*R[k]] for i,k in enumerate(rk)}}
json.dump(key,open(S+'/blind_key.json','w'),indent=1)
def tile(f,b,pad=6,H=120):
    im=Image.open(f).convert('L'); x0,y0,x1,y1=b; im=im.crop((max(0,x0-pad),max(0,y0-pad),x1+pad,y1+pad))
    s=H/im.size[1]; return im.resize((max(20,int(im.size[0]*s)),H))
def sheet(items,prefix,out,W=1500):
    ims=[(lab,tile(f,b)) for lab,(k,f,b) in items]
    x=y=0; rows=[]; H=120
    canvas=Image.new('L',(W,2000),255); d=ImageDraw.Draw(canvas)
    for lab,im in ims:
        w=max(im.size[0],60)
        if x+w+16>W: x=0; y+=H+36
        canvas.paste(im,(x,y+22)); d.rectangle([x-1,y+21,x+im.size[0],y+22+H],outline=128); d.text((x+2,y+4),lab,fill=0); x+=w+16
    canvas.crop((0,0,W,y+H+30)).save(out,quality=90)
sheet([(k,(v[0],v[1],tuple(v[2]))) for k,v in key['queries'].items()],'Q',S+'/blind_queries.jpg')
sheet([(k,(v[0],v[1],tuple(v[2]))) for k,v in key['refs'].items()],'R',S+'/blind_refs.jpg')
print(len(qk),len(rk))
