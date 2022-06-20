#!/usr/bin/python3

from Crypto.Util.number import getPrime
import secrets

FLAG = b'grey{The_Answer_To_The_Riddle_Is_"Road"!_ZvBtTpyA4GXuuwjB}'

coeff = []

# Fills in the coeff array
# Post Conditions : 
# 1. len(coeff) > 30
# 2. coeff[len(coeff) - 1] == 1
# 3. There exists at least one input x, where 0 < x < 2**70 and eval(input) == 0
def fillCoeff():
    global coeff
    n = 40 + secrets.randbelow(10)
    root = getPrime(64)
    p = [sign() * secrets.randbits(192) for _ in range(n - 2)]
    coeff = [0 for _ in range(n)]
    p[0] = sign() * getPrime(64) * getPrime(64) * getPrime(64)
    p.append(1)
    coeff[0] = root * p[0] * -1
    for i in range(1, n - 1):
        coeff[i] = p[i - 1] - p[i] * root
    coeff[n - 1] = 1
    assert isCitizen(root)
    assert len(coeff) > 30
    assert coeff[len(coeff) - 1] == 1

def sign():
    if (secrets.randbits(1)):
        return 1
    return -1

def eval(userInput):
    s = 0
    for i in range(len(coeff)):
        s += coeff[i] * (userInput**i)
    return s

def isCitizen(userInput):
    if not (0 < userInput < 2**70):
        return False
    return eval(userInput) == 0

def welcome():
    print('''
                             -|             |-
         -|                  [-_-_-_-_-_-_-_-]                  |-
         [-_-_-_-_-]          |             |          [-_-_-_-_-]
          | o   o |           [  0   0   0  ]           | o   o |
           |     |    -|       |           |       |-    |     |
           |     |_-___-___-___-|         |-___-___-___-_|     |
           |  o  ]              [    0    ]              [  o  |
           |     ]   o   o   o  [ _______ ]  o   o   o   [     | ----__________
_____----- |     ]              [ ||||||| ]              [     |
           |     ]              [ ||||||| ]              [     |
       _-_-|_____]--------------[_|||||||_]--------------[_____|-_-_
      ( (__________------------_____________-------------_________) )
''')
    print("Welcome to The Root Kingdom!!!")
    print("Only citizen of Root are allowed to enter the country.")
    print("Choose the action that you wish to perform.")
    print("1. Have a taste of our beetroot.")
    print("2. Prove that you are a citizen of Root by solving the riddle")

if __name__ == "__main__":
    welcome()
    fillCoeff()
    for i in range(5):
        option = int(input("Option: "))
        if (option == 1):
            x = int(input("How much beetroot do you want?\n"))
            print(f"Here you go! {eval(x)}")
        elif (option == 2):
            x = int(input("What goes through cities and fields, but never moves?\n"))
            if (isCitizen(x)):
                print(f'Welcome Home! {FLAG}')
            else:
                print("Are you sure that you live here?")
        else:
            print("What you say?")
