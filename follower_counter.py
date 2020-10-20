count = 0
while True :
    inp = input('     Hit Enter:    ')
    if len(inp) < 1 :
        count += 1
        print(count)
    elif inp == 'done' or inp == 'Done' or inp == 'DONE' :
        print('A total of ',count, ' accounts has been followed during this session.')
        break
