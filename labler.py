import sqlite3
connection = sqlite3.connect('2etDB.sqlite')
cur = connection.cursor()
cur.execute('SELECT tweet FROM Tweets WHERE label IS NULL')
tweetsList = cur.fetchall()


def labelify(tweet):
    print(tweet)
    print('\n')
    label = input('Enter the label for this tweet or type help:  ')
    if label == '0' or label == '1' or label == '2' or label == '3' :
        pass
    elif label == 'done' :
        exit()
    elif label == 'help' or label == 'HELP' or label == 'Help' :
        print('''labels are as follows:\n \n0 for medicine/science\n1 for politics\n2 for sports\n3 for others.\n\nDO NOT ENTER HELP AGAIN AT LEAST TILL NEXT TWEET\n\n''')
        label = input('Enter the label for this tweet:  ')
    else :
        print('Invalid response. Program will terminate and you\'ll have to run it again.\nit will continue the process with no adverse effects.')
        exit()
        if label == '0' or label == '1' or label == '2' or label == '3' :
            pass
        else :
            print('Invalid response. Program will terminate and you have to run it again.\nit will continue the process with no adverse effects.')
            exit()
    print('=============================================================')
    print('\n\n\n')
    return(int(label))
# List of Tuples
for eachTweet, in tweetsList :
    label = labelify(eachTweet)
    cur.execute('UPDATE Tweets SET label = ? WHERE tweet = ? ', (label, eachTweet))
    connection.commit()

cur.close()
