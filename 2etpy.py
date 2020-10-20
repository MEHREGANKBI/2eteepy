import tweepy



#
def write2et(ourNewTweet):
    with open('2et.txt','a') as filehandle :
        text2append = ourNewTweet + '\n' + 'new2etcoming' + '\n'
        filehandle.write(text2append)
        print(text2append)


#-----------------------------------------------------

def oAthuenticate_stuff():
    count = 0
    oAuthFileHandle = open('oAuth.txt')
    for eachline in oAuthFileHandle :
        count += 1
        if count == 1 :
            apiKey = str(eachline)
        elif count == 2 :
            apiSecretKey = str(eachline)
        elif count == 3 :
            access_token = str(eachline)
        elif count == 4 :
            access_token_secret = str(eachline)
    return apiKey, apiSecretKey, access_token, access_token_secret

#---------------------------------------------------

def retrieve_tweets():
    tweets = api.home_timeline()
    return tweets

#--------------------------------------------------
apiKey, apiSecretKey, access_token, access_token_secret = oAthuenticate_stuff()
#AUTH
authentication = tweepy.OAuthHandler(apiKey, apiSecretKey)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication)
#AUTH

#----------------------------------------------------


def ret_2et_full():

    tweetsList = retrieve_tweets()
    for eachtweet in tweetsList :
        write2et(eachtweet)
    print('A total of', len(tweetsList), 'were retrieved and saved to (2et.txt) .')

ret_2et_full()

#------------------------------------------------------------------------
# right after writing twwet to file in 
    print('\n')
    if 'media' in each2et['entities'] :
        print('@' + each2et['entities']['media'][0]['url'])
    elif 'media' not in each2et['entities'] :
        if len(each2et['entities']['urls']) >= 1 :
            print('@' + each2et['entities']['urls'][0]['url'])
        else :
            damUrlsList = re.findall('url": "(https.*)"', str(each2et), re.MULTILINE)
            print(len(damUrlsList), '^^^^^^^^^^')
            if len(damUrlsList) >= 1 :
                print('***********************************')
                print(re.findall('url": "(https.*)"', each2et, re.MULTILINE)[0])
                print('***********************************')
            brokenApi += 1

print('\n')
print ('======================================')
print('brokenAPIs count: ', brokenApi)
