#!/usr/bin/python3

import subprocess, random, sys

def test(binary, ans):
    ret = subprocess.run([binary], input= ans.encode())
    return ret.returncode == 0

def main():
    
    print ("Unauthorized access detected.")
    print ("Decontamination in 10 minutes")
    print ("Do you wish to override? (y/n)")

    if (input() != 'y'):
        print ("Good bye")
        sys.exit(1)


    challenges = random.sample([line for line in open("challenges.txt", "r")], 5)
    
    for challenge in challenges:
        binary = challenge.split(",")[0]
        print ("Password required for challenge code: " + binary)
        answer = input()
        if (test("bin/{}".format(binary), answer)):
            pass
        else:
            print ("Authorization failed. System locking down")
            sys.exit(1)
    
    print(open("flag.txt", "r").read())

if __name__ == "__main__":
    main()
