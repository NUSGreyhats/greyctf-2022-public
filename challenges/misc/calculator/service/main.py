#!/usr/bin/python3

import random
import time

FLAG = 'grey{prefix_operation_is_easy_to_evaluate_right_W2MQshAYVpGVJPcw}'

operations = ["add", "mul", "sub", "neg", "inc"]

def op1(op, s):
    return f'{operations[op]} {s}'

def op2(op, s1, s2):
    return f'{operations[op]} {s1} {s2}'

def randnum():
    return random.getrandbits(30)

def gen(depth):
    if (depth == 1):
        a = randnum()
        return a, str(a) 
    
    op = random.randrange(0, len(operations) - 1)        
    
    if (op <= 2):
        if (random.random() < (1 - 1/depth)):
            a1, s1 = gen(depth - 1)
        else:
            a1 = randnum()
            s1 = str(a1)

        if (random.random() < (1 - 1/depth)):
            a2, s2 = gen(depth - 1)
        else:
            a2 = randnum()
            s2 = str(a2)

        if (op == 0):
            return (a1 + a2, op2(op, s1, s2)) 
        if (op == 1):
            return (a1 * a2, op2(op, s1, s2)) 
        if (op == 2):
            return (a1 - a2, op2(op, s1, s2)) 
        
    else:
        if (random.random() < (1 - 1/depth)):
            a1, s1 = gen(depth - 1)
        else:
            a1 = randnum()
            s1 = str(a1)

        if (op == 3):
            return (-a1, op1(op, s1)) 
        if (op == 4):
            return (a1 + 1, op1(op, s1)) 

def menu():
    print('''
           __________                                 
         .'----------`.                              
         | .--------. |                             
         | |########| |       __________              
         | |########| |      /__________\             
.--------| `--------' |------|    --=-- |-------------.
|        `----,-.-----'      |o ======  |             | 
|       ______|_|_______     |__________|             | 
|      /  %%%%%%%%%%%%  \                             | 
|     /  %%%%%%%%%%%%%%  \                            | 
|     ^^^^^^^^^^^^^^^^^^^^                            | 
+-----------------------------------------------------+
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ 
    ''')
    print("How fast are you on calculating basic math expression?")
    print("Answer 100 math questions in 30 seconds to the flag\n")
    print("Operations include: ")
    print("1. add x y -> returns x + y")
    print("2. mul x y -> returns x * y")
    print("3. sub x y -> returns x - y")
    print("4. neg x -> returns -x")
    print("5. inc x -> returns x + 1\n")

    print("Example1: mul add 1 2 sub 5 1")
    print("Ans1: (1 + 2) * (5 - 1) = 12\n")
    print("Example2: add mul sub 3 2 inc 5 3")
    print("Ans2: (3 - 2) * (5 + 1) + 3 = 9\n")
    print("Send START when you are ready!")


if __name__ == "__main__":
    menu()
    s = input()
    if (s == "START"):
        start = time.time()
        for i in range(100):
            if (i < 10):
                a, s = gen(5)
            else:
                a, s = gen(20)
            print(s)
            user = int(input())
            if (a == user):
                print("You got it right!")
            else:
                print(a)
                print("You got it wrong... try again")
                exit(0)
        end = time.time()
        duration = end - start
        print(f'You done it in {duration} seconds!')
        if (duration <= 30):
            print(FLAG)
        else:
            print("That's a little slow... Try again")

    else:
        print("I don't understand what you say")