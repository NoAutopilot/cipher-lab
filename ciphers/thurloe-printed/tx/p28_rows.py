R=[]
def L(line,codes,gl,page="409"):
    c=codes.split(); g=gl.split("|")
    assert len(c)==len(g),(line,len(c),len(g))
    for i,(a,b) in enumerate(zip(c,g)): R.append(("P28",page,line,i,a,b.strip()))
L("0","1016","Colen")
L("1","324 86 522 136 343 498 411 350 353 66 43 293 160 517 334 460 372","I|had|ne|wee|s|that|ON|ei|l|was|eſ|ca|pe|d|and|att|the")
L("2","72 365 570 354 111 293 40 295 353","Ha|ge|you|muſt|be|ca|re|fu|l")
L("3","148 176 41 493 442 148 225 387 424 219 434","Sir|T.|B|lo|there|ſir|Fr.|Vi.|n|c|ent")
L("4","251 383 124 278 41 217 597 424 164 406 337 365 531 337 566 587 522 580","C|ol.|Ad|am|B|ro|w|n|were|en|ga|ge|d.|Ga|r|di|ne|r")
L("5","89 598 216 73 411 476 311 343 129","now|your|pr|iſ|on|er|know|s|it")
L("6","598 573 391 404 562 54 146 466 367 191 411 292 500 304 72 580","Your|de|cl|are|ing|a|pe|na|l|tie|on|an|y|who|ha|r")
L("7","55 481 372 160 245 411 343 324 100 466 60 238 177 570 346 111 313","b|or|the|pe|rſ|on|s|I|have|na|m|ed|to|you|will|be|off")
L("8","226 379 124 275 494 166 196","hi|gh|ad|va|nt|ag|e")
with open("img_pairs_P28.tsv","w") as f:
  f.write("letter\tpage\tline\tpos\tcode\tgloss\tread\n")
  for r in R: f.write("\t".join(map(str,r))+"\tclear\n")
print(len(R))
