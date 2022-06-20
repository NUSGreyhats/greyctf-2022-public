#!/usr/bin/python3

from secrets import randbits
from hashlib import shake_256
from Crypto.Util.number import isPrime
import point

FLAG = 'grey{HyperSphereCanBeUsedForKeyExchangeToo!(JustProbablyNotThatSecure)_33JxCZjzQQ7dVGvT}'

p = 7489556970112255858194339343279932810383717284810081135153576286807813194468553481550905061983955290055856497097494238457954616159153509677256329469498187
ga = 2258050144523952547356167241343623076013743172411353499204671793264857719189919436799943033376317821578765115886815403845812363461384417662956951961353685
gb = 1069914179693951322883111467335954654818815798644770440034358650042824371401982086159904675631799159962201142170062814585463048527613494928890992373946863
gc = 11133097852046797355391346851525395533946845181651405581054631571635854160968086
gd = 7489556970112255858194339343279932810383717284810081135153576286807813194460592232877165912462810721221949401180338198644010019265640599992748426319034311

h = 512

g = point.Point(ga, gb, gc, gd, p)

def encrypt(msg : bytes, key : str) -> str:
    otp = shake_256(key.encode()).digest(len(msg))
    return xor(otp, msg).hex()

def xor(a : bytes, b : bytes) -> bytes:
    return bytes([ x ^ y for x, y in zip(a, b)])

def welcome():
    print('''
        _____
    ,-:` \;',`'-, 
  .'-;_,;  ':-;_,'.
 /;   '/    ,  _`.-\\
| '`. (`     /` ` \`|
|:.  `\`-.   \_   / |
|     (   `,  .`\ ;'|
 \     | .'     `-'/
  `.   ;/        .'
jgs `'-._____.
    ''')
    print("Let's do Key Exchange using HyperSphere ヽ(o＾▽＾o)ノ\n", flush=True)

def checkPrime(prime : int) -> bool:
    return prime.bit_length() >= 512 and isPrime(prime)

def checkPoint(ta : int, tb : int, tc : int, td : int) -> bool:
    cond1 = 10 < ta < p - 2
    cond2 = 10 < tb < p - 2
    cond3 = 10 < tc < p - 2
    cond4 = 10 < td < p - 2
    cond5 = (ta * ta + tb * tb + tc * tc + td * td) % p == 1
    return cond1 and cond2 and cond3 and cond4 and cond5

def change():
    global p
    global g
    userIn = input("Do you wish to change the prime number and point? Y/N\n")
    if (userIn == "Y"):
        userPrime = int(input("New Prime: "))
        if (not checkPrime(userPrime)):
            print("Your prime is not suitable!")
            exit(0)
        p = userPrime

        userPoint = input("New Point (split by space): ").split()
        ta = int(userPoint[0])
        tb = int(userPoint[1])
        tc = int(userPoint[2])
        td = int(userPoint[3])
        if (not checkPoint(ta, tb, tc, td)):
            print("Your point is not suitable!")
            exit(0)
        g = point.Point(ta, tb, tc, td, p)
    

if __name__ == '__main__':
    welcome()
    print(f"Prime : {p}")
    print(f"Point : {g}")
    change()
    
    a = randbits(h); b = randbits(h)
    A = g ** a; B = g ** b
    S = A ** b
    key = str(S)
    msg = str(randbits(h)).encode()

    print(f"p = {p}"); print(f"g = ({g})"); print(f"A = ({A})"); print(f"B = ({B})"); 

    print(f"c = {encrypt(msg, key)}\n")

    ans = input("What's the msg?\n")
    if (ans.encode() == msg):
        print("Congratulations! Here's your flag (๑˃ᴗ˂)ﻭ")
        print(FLAG)
    else:
        print("You got it wrong... (＞ｍ＜) Try again!")
    