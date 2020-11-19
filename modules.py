
'''

MODULES

They are tools that contain some functions and attributes that enable us to perform some functions easily.
It provides the opportunity to use these functions it hosts in different files and programs over and over again.
Thanks to the modules, Python has become a much more useful and easy-to-implement.

In order to use any module in Python, we first need to 'import' it.
Importing means making functions and attributes within one module available from within another program.

'''

import random as rnd
secret = rnd.randint(1,10)

check = False

for x in range(5):
    guess = int(input("Please enter your guess: "))
    if guess == secret:
        print("Congrats!")
        check = True
        break
    elif guess < secret:
        print("Please enter greater number!")
    else:
        print("Please enter smaller number!")

if not check:
    print("The number was: ", secret)