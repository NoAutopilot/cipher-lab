R=[]
def L(line,codes,gl,page="100"):
    c=codes.split(); g=gl.split("|")
    assert len(c)==len(g),(line,len(c),len(g))
    for i,(a,b) in enumerate(zip(c,g)): R.append(("P25",page,line,i,a,b.strip()))
L("a","441 464 69 297 44","States Gen.|C.M.|was|with|their")
L("b","68 441 397 44 105 297 435 403 293 10 179","the|St.Gen.|had|their|war|with|prot.|the|pe|a|ce")
L("c","26 487 614 212 221","he|Paris|D.amb.|to|utter")
L("d","131 122","but|his")
L("e","122 3031 378 343 381","his|ma|ſ|t|ers")
L("f","230 88 231 233","if|my|lord|protector",page="101")
L("g","430 433","France|Sweden",page="101")
L("h","447","Sweden",page="101")
L("i","480 351 100","Cardinall|me|n",page="101")
L("j","56 141 87 72 332 108 215 250 181 364 448","they|were|l|e|vi|ed|ch|ar|ge|of|France",page="101")
L("k","119 430 26 92 435 261 10 277 281 68 547 359 13 124 403","by|France|He|thinks|the prot.|will|a|great|part|that|army|de|fe|nd|the",page="101")
L("l","317 10 179","pl|a|ce",page="101")
L("m","435 315 174 10 60 403 548 1600 374 339","the protector|make|re|a|dy|the|fleet|a yeare's|it|may",page="101")
L("n","413 212 91","put|to|ſea",page="101")
L("o","87 288 302 16 280","l|end|ing|mo|ny",page="101")
L("p","16 280","mo|nies",page="101")
with open("img_pairs_P25.tsv","w") as f:
  f.write("letter\tpage\tline\tpos\tcode\tgloss\tread\n")
  for r in R:
    note="clear"
    if r[4]=="3031": note="clear-print; 3031 out of range, M"
    if r[2]=="j": note="clear; numeral row partly clipped at crop edge, read from p101b top"
    f.write("\t".join(map(str,r))+"\t"+note+"\n")
print(len(R))
