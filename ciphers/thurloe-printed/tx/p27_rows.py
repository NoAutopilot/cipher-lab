R=[]
def L(line,codes,gl,page="383"):
    c=codes.split(); g=gl.split("|")
    assert len(c)==len(g),(line,len(c),len(g))
    for i,(a,b) in enumerate(zip(c,g)): R.append(("P27",page,line,i,a,b.strip()))
L("1","324 278 89 211 1016 535 365 594 63 306 102 343 511 192 540","I|am|now|for|Collen|Lord|Ge|ra|rd|and|Ma|ſ|ſi|went|this")
L("2","545 500 306 264 127 464 576 75 316 576 346 399 273 237 372 1007 343","da|y|and|all|fa|il|ing|not|th|ing|will|ſe|rve|but|the|prot.|s")
L("3","46 261 259 170 306 1007 343 56 443 127 367 446 413 257 259 411","m|u|rt|her|and|prot.|s|do|un|fa|l|at|co|u|rt|on")
L("4","318 264 284 211 51 443 343 505 300 342 217 97 259 50 149 237","who|all|miſ|for|t|un|s|are|put.|Prince|Ro|be|rt|ſent|to|but")
L("5","570 92 213 89 264 411 386 49 51 261 203 285 372 423 343 1005 73","you|ſhall|k|now|all|on|the|re|t|u|rn|of|the|letter|s.|Ch.St.|is")
L("6","1030 517 149 244 2372 1017 460 46 122 245 96 593 183 261 259 266 424","deſign|d|to|meet|the|prince|at|In|we|rs|ab|out|fo|u|rt|ee|n")
L("7","545 528 343 198 1014 1015 404 264 506 403 556 46 454 226 465 230","da|ye|s|hence.|Wilmot|Armoror|are|all|in|Engl.|yet|mrs.|P|hi|li|ps")
L("8","307 407 292 110 419 429 51 285 1014 320 326 285 372 40 343 51","can|give|an|ac|co|un|t|of|Wilmot|and|moſt|of|the|re|ſ|t")
L("9","306 418 324 100 597 133 51 197 103 307 116 597 391 210 49 587 357","and|end:|I|have|w|ri|t|for|none|can|make|ſo|cl|ea|r|di|ſ")
L("10","419 331 13 418 484","co|veri|es|as|they")
L("11","403 1005","England|Ch. Stew.")
import csv
with open("img_pairs_P27.tsv","w") as f:
  f.write("letter\tpage\tline\tpos\tcode\tgloss\tread\n")
  for r in R:
    note="clear"
    if r[4]=="2372": note="clear-print; 2372 out of range (372=the elsewhere), M"
    if r[2]=="11" and r[4]=="1005": note="clear; gloss set over the line start, only numeral on the line"
    f.write("\t".join(map(str,r))+"\t"+note+"\n")
print(len(R))
