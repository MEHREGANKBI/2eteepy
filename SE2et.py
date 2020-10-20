import sqlite3
import re
import time

inp = input('Have you fixed the .py dict\'s ENDING and removed dict creation thingy?   ')
if inp == 'yes' :
    pass
else :
    print('well then get your shit together.')
    exit()
#lines off after first run.
#with open('embedFile.py', 'w') as embfile :
    #embfile.write('embedDict = { \n    ')

def retrieveRawEmbedding(word):
    packLine = None
    lineCount = 0
    lineCount2 = 0
    packmin = None
    rawEmbedding = []
    word = word.lower()
    for eachline in open('word2vecTree.txt', encoding = 'UTF-8') :
        eachline = eachline.lower()
        lineCount += 1
        if lineCount == 1 or (lineCount-1)%4 == 0 :
            if len(re.findall('\s' + word + '\s', eachline)) >= 1 :
                packLine = lineCount + 2
                break
            else :
                continue
        else :
            continue

    if packLine == 3 :
        packmin = 0
    elif packLine is None :
        rawEmbedding = []
        return rawEmbedding
    else :
        packmin = ((packLine - 3) / 4) * 1000

    for eachline in open('crawl-300d-2M.vec', encoding = 'UTF-8') :
        lineCount2 += 1
        if lineCount2 > packmin :
            if word == eachline.split()[0].strip() :
                rawEmbedding = eachline.split()[1: ]
                break
    return rawEmbedding

def refineEmbedding(rawEmbedding):
    if len(rawEmbedding) != 300 :
        print('The word embedding is not right.')
        print(len(rawEmbedding))
        exit()
    else :
        pass
    refinedEmbedding = '[ '
    for eachval in rawEmbedding :
        refinedEmbedding = refinedEmbedding + eachval + ' , '
    refinedEmbedding = refinedEmbedding[ : len(refinedEmbedding) - 2] + ']'
    return refinedEmbedding

rawEmbedding = []
refinedEmbedding = None
connection = sqlite3.connect('2etWordDB.sqlite')
cur = connection.cursor()
cur.execute('SELECT word FROM WordEmbeddings WHERE embedding IS NULL')
wordsList = cur.fetchall()
begTime = time.time()
nowTime = time.time()

# A LIST OF TUPLES
wordCounter = 0
for eachword, in wordsList :
    wordCounter += 1
    eachwordRaw = eachword
    rawEmbedding = retrieveRawEmbedding(eachword)
    cur.execute('UPDATE WordEmbeddings SET embedding = ? WHERE word = ?', (1, eachwordRaw))
    connection.commit()
    if len(rawEmbedding) < 1 :
        continue
    refinedEmbedding = refineEmbedding(rawEmbedding)
    eachword = '\'' + eachword + '\''
    with open('embedFile.py', 'a') as embFile :
        embFile.write(eachword + ' : ' + refinedEmbedding + ' ,\n    ')
    if wordCounter % 10 == 0 :
        nowTime = time.time()
        print(nowTime - begTime, ' is time elapsed after ', wordCounter, 'rounds.')

cur.close()
print('==============================')
print('wait. is it done? Really?')
