FLAG = <REDACTED>

coeff = []

# Fills in the coeff array
# Post Conditions : 
# 1. len(coeff) > 30
# 2. coeff[len(coeff) - 1] == 1
# 3. There exists at least one input x, where 0 < x < 2**70 and eval(input) == 0
def fillCoeff():
    # Implementation hidden
    ...
    assert len(coeff) > 30
    assert coeff[len(coeff) - 1] == 1

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