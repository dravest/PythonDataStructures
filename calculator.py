
import sys

add = False
sub = False
mult = False
div = False

while(True):
    x = input()
    if (x == 'exit') or (x == 'Exit') or (x == 'EXIT'):
        sys.exit()

    for i in range(len(x)):
        if (65 <= ord(x[i]) <= 90) or (97 <= ord(x[i]) <= 122):
            print('ERROR: Invalid Input')
            sys.exit()
        elif (ord(x[i]) == 43):
            add = True
        elif (ord(x[i]) == 45):
            sub = True
        elif (ord(x[i]) == 42):
            mult = True
        elif (ord(x[i]) == 47):
            div = True

    if (add == True):
        x = x.split('+')
        x = int(x[0]) + int(x[1])
        print(x)
        add = False
    
    elif (sub == True):
        x = x.split('-')
        x = int(x[0]) - int(x[1])
        print(x)
        sub = False
    
    elif (mult == True):
        x = x.split('*')
        x = int(x[0]) * int(x[1])
        print(x)
        mult = False
    
    elif (div == True):
        x = x.split('/')
        x = int(x[0]) / int(x[1])
        print(x)
        div = False
