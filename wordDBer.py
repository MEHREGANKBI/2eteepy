import sqlite3

input1 = input('Have you run 2etDBer before running this?   ')
if input1 == 'yes' :
    pass
elif input1 == 'no' :
    print('\n')
    print('well then fucking run 2etDBer again you idiot!!!')
    exit()
else :
    print('\n')
    print('invalid response. run the program again')
    exit()

fh = open('2etnwcnlnrt.txt').read()
connection = sqlite3.connect('2etWordDB.sqlite')
cur = connection.cursor()

fh = fh.replace('\n', ' ')
tweetsList = fh.split('new2etcoming')

for each2et in tweetsList :
    each2et = each2et.strip()
    tweetWordList = each2et.split()
    for eachWord in tweetWordList :
        eachWord = eachWord.strip()
        if len(eachWord) > 1 :
            cur.execute('''INSERT OR IGNORE INTO WordEmbeddings (word) VALUES (?)''', (eachWord,))
            connection.commit()
        else:
            pass
cur.close()

input2 = input('Wanna delete 2etnwcnlnrt.txt ?  ')
if input2 == 'yes' :
    with open('2et_failSafe.txt', 'a') as failFile :
        failFile.write(fh + '\n \n new2etpackagecoming \n \n')
    with open('2etnwcnlnrt.txt', 'w') as myfile :
        myfile.write('')
else :
    print('invalid response. you can manually empty 2etnwcnlnrt.txt ')
