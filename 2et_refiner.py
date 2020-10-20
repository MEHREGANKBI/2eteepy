from refine_helper import weirdCharFinder

weirdCharsList = weirdCharFinder()
fh = open('2et.txt', encoding = 'UTF-8').read()
fh = fh.replace('\n', 'newlinecommand')
for i in range(len(fh)) :
    if fh[i] in weirdCharsList :
        fh = fh.replace(fh[i], ' ')
fh = fh.replace('newlinecommand', '\n')

#------------------------------------ no weird char till now

fh = fh.split('new2etcoming')
for i in range(len(fh)) :
    fh[i] = fh[i].strip()
    if fh[i].find('https') == -1 :
        fh[i] = fh[i] + '\n new2etcoming \n'
        continue
    else :
        fh[i] = fh[i][ : fh[i].find('https')]
        fh[i] = fh[i] + '\n new2etcoming \n'


#---------------------------------- no link till now
for i in range(len(fh)) :
    if fh[i].startswith('RT') == True :
        fh[i] = fh[i][2 : ]
    else :
        continue

fhMerged = ''
for i in range(len(fh)) :
    fhMerged = fhMerged + fh[i]

#-------------------------------------- no RT till now


with open('2etnwcnlnrt.txt', 'a', ) as myfile :
    myfile.write(fhMerged + '\n')


with open('2et.txt', 'w', ) as myfile :
    myfile.write('')
