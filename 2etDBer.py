import sqlite3

fh = open('2etnwcnlnrt.txt').read()
if len(fh) < 1 :
    print('\n')
    print('wait. why is 2etnwcnlnrt.txt empty? ')
    print('\n \n')
    print('exiting due to technical difficulties.')
else :
    pass
connection = sqlite3.connect('2etDB.sqlite')
cur = connection.cursor()


fh = fh.replace('\n', ' ')
tweetsList = fh.split('new2etcoming')
for each2et in tweetsList :
    each2et = each2et.strip()

    cur.execute('''INSERT OR IGNORE INTO Tweets (tweet) VALUES (?) ''', (each2et,))
    connection.commit()

cur.close()
