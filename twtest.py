import urllib.request, urllib.parse, urllib.error
from twurl import augment
import ssl
import json
import re

# https://apps.twitter.com/
# Create App and get the four strings, put them in hidden.py
countforparam = input('how many tweets?  ')
print('* Calling Twitter...')
url = augment('https://api.twitter.com/1.1/statuses/home_timeline.json',
              {'count': countforparam , 'tweet_mode' : 'extended'})
print(url)



#----------------------------------------------
def write2et(ourNewTweet):
    with open('2et.txt','a', encoding="UTF-8") as filehandle :
        text2append = ourNewTweet + '\n' + 'new2etcoming' + '\n \n'
        filehandle.write(text2append)

    with open('2etFull.txt','a', encoding="UTF-8") as filehandle :
        text2append = ourNewTweet + '\n' + 'new2etcoming' + '\n \n'
        filehandle.write(text2append)

#----------------------------------------------




# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

print ('======================================')
print ('======================================')
print ('======================================')


connection = urllib.request.urlopen(url, context=ctx)
data = connection.read().decode(encoding='UTF-8',errors='ignore')
jsonhandle = json.loads(data)

headers = dict(connection.getheaders())
print(headers['x-rate-limit-remaining'])
#--------------------------------------

#--------------------------------------

count = 0
brokenTweet = 0
for each2et in jsonhandle :
    count += 1
    try:
        write2et(each2et['full_text'])
        print(count, each2et['full_text'] + '\n \n')
    except:
        brokenTweet += 1
        print('Tweet is crazy. moving on to next tweet.', brokenTweet)
        continue
print('Tweet is crazy. moving on to next tweet.', brokenTweet)
