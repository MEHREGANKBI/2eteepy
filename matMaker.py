import numpy as np
import sqlite3
import time

connection = sqlite3.connect('2etDB.sqlite')
cur = connection.cursor()
cur.execute('SELECT tweet, label FROM Tweets WHERE label IS NOT NULL')
tweetsList = cur.fetchall()
cur.close()
m = len(tweetsList[:2000])
print(m)
n = 300
t = 0
c = 4
for eachTweet,itsLabel in tweetsList :
    eachTweetList = eachTweet.split()
    if len(eachTweetList) > t :
        t = len(eachTweetList)

inputMat = np.zeros((m,t,n))
outputMat = np.zeros((m,c))

def lenEqualize(tweet, nonsensicalTerm = 'thisIsNonesenseCuzisaySo'):
    if len(tweet.split()) < t :
        for i in range(t - len(tweet.split())) :
            tweet = tweet + ' ' + nonsensicalTerm
    else :
        pass
    return tweet
#--------------------------------------------

def oneHot(label, c = 4):
    oneHotVer = np.zeros((c,))
    oneHotVer[label] = 1
    return oneHotVer
#--------------------------------------------

for i in range(m) :
    tweet,label = tweetsList[i]
    tweet = lenEqualize(tweet)
    outputMat[i, :] = oneHot(label = label)



    for j in range(t) :
        word = tweet[j]
        inputMat[i,j, :] = np.zeros((300,))
randList = []
def randomize(grSize):
    matrixA = np.zeros((grSize,t,n))
    matrixB = np.zeros((grSize,c))
    for i in range(grSize) :
        randomNum = np.random.randint(low = 0, high = m)
        if randomNum not in randList :
            randList.append(randomNum)
            matrixA[i, :, :] = inputMat[randomNum, :, :]
            matrixB[i,:] = outputMat[randomNum, :]
    return matrixA, matrixB

input_train, output_train = randomize(int(m * 0.7))
input_cv, output_cv = randomize(int(m * 0.15))
input_test, output_test = randomize(int(m * 0.15))


for i in range(300) :
    print(output_test[i])
    time.sleep(1)
