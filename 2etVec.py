vh = open('crawl-300d-2M.vec')
x= 0
inp = input('somethn')
if len(inp) < 1 :
    exit()
else :
    pass
for eachline in vh :
    x += 1
    print(eachline)
    print('==============================================================')
    if x ==3 :
         break
