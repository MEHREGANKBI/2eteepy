def weirdCharFinder():
    authorizedCharsList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    fh = open('2et.txt', encoding = 'UTF-8').read()
    weirdCharsList = []
    tweetsList = fh.split('new2etcoming')
    for each2et in tweetsList :
        each2et = each2et.strip()
        each2et = each2et.split()
        for eachWord in each2et :
            for i in range(len(eachWord)) :
                if eachWord[i] not in authorizedCharsList :
                    if eachWord[i] not in weirdCharsList :
                        weirdCharsList.append(eachWord[i])
    return weirdCharsList

    
weirdCharFinder()
