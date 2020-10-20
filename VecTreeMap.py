vh = open('crawl-300d-2M.vec', encoding = 'UTF-8')

def mergeListVals(listName) :
    writeList =''
    for eachval in listName :
        writeList = writeList + ' ' + eachval
    return writeList

appendList = []
count = 0
for eachline in vh :
    count += 1
    word = eachline.split()[0]
    appendList.append(word)
    if count % 1000 == 0 :
        with open('word2vecTree.txt', 'a', encoding = 'UTF-8') as myfile :
            myfile.write(mergeListVals(appendList) + '\n \n' + 'from '+ str((count/1000) - 1) +'K to ' + str(count/1000) + 'K \n \n')
            appendList = []

with open('word2vecTree.txt', 'a') as urfile :
    urfile.write('from ' + str(int(count/1000)) + 'K to ' + str(count))
