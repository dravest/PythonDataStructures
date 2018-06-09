"""
    Name: Thomas Draves
    Date: 06-09-2019
    File Name: calculator.py
    Description: For now this calculator can only handle
    two integers and one operator. My goal is to eventually
    add in multiple ints and operators and be able to give
    the correct answer. The original purpose of this
    program was to refresh my python knowledge before
    continuing on to more complicated python projects.
"""

import sys

add = False
sub = False
mult = False
div = False

while(True):
    x = input('Enter an equation')
    if (x == 'exit') or (x == 'Exit') or (x == 'EXIT'):
        sys.exit()
    """
        Here is where the input is checked for invalid characters
        After that the operator that was given is set to true as
        to use in the computation stage.
    """
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

    """
    These next four if statements are where the computation occurs.
    At this point the input has been checked as valid input, the
    operator that was given was choosen. 
    """
    if (add == True):
        x = x.split('+')
        x = int(x[0]) + int(x[1])
        print('Answer:', x)
        add = False
    
    elif (sub == True):
        x = x.split('-')
        x = int(x[0]) - int(x[1])
        print('Answer:', x)
        sub = False
    
    elif (mult == True):
        x = x.split('*')
        x = int(x[0]) * int(x[1])
        print('Answer', x)
        mult = False
    
    elif (div == True):
        x = x.split('/')
        x = int(x[0]) / int(x[1])
        print('Answer', x)
        div = False
