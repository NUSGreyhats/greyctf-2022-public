import os, jinja2, tempfile, uuid, string, random, subprocess, hashlib, sys

def scramble(a, i, k):
    return chr((ord(a) * i % k + (ord(a)+i))%73 + ord("0"))


def c_string(st):
    s = "{"
    for c in st:
        s += str(ord(c)) + ","
    
    s = s.rstrip(",")
    s += "};"
    return s

def test(binary, ans):
    ret = subprocess.run([binary], input= ans.encode())
    return ret.returncode == 0

def build(src):
    with tempfile.NamedTemporaryFile(delete=True, suffix=".c", mode="w") as tempsrc:
        tempsrc.write(src)
        tempsrc.seek(0)
        binary = "bin/"+str(uuid.uuid4())
        os.system("cc -fno-pie -no-pie -s -o {} {}".format(binary, tempsrc.name))
        newName =  "bin/" + h(binary)
        os.system("mv {} {}".format(binary, newName))
        return newName

"""
    Build a random binary with an answer, returns (sha256(binary), answer)
"""
def generate():
    template = jinja2.Template(open("challenge.jinja", 'r').read())
    
    size = random.randint(25, 31)
    k = random.randint(1001, 3001)
    ans = "".join(random.choices(string.ascii_lowercase+string.digits, k=size))
    expected = "".join([scramble(c, i, k) for i,c in enumerate(ans)])
    expected2 = "".join([scramble(c, ord(expected[i]), k) for i,c in enumerate(ans)])
    print (ans, expected, expected2)
    
    code = template.render(
        expected = c_string(expected),
        expected2 = c_string(expected2),
        size=size,
        ans=ans,
        k=k,
    )

    binary = build(code)
    
    # sometimes the generated answer does not match. idk why, just catching it here.
    assert(test(binary, ans))
    
    return (h(binary), ans, expected, expected2)

def h(binary):
    data = open(binary, "rb").read()
    return hashlib.sha256(data).hexdigest()

def main():
    print ("This will overwrite existing challenges. Do you wish to proceed? (y/n)")
    if (input() != 'y'):
        sys.exit(0)

    challenges = []
    
    for i in range(100):
        challenges.append(generate())

    f = open("challenges.txt", "w")
    for hchallenge, ans, e1, e2 in challenges:
        f.write(hchallenge + ", " + ans + ", " + e1 + ", " + e2 + "\n")

if __name__ == "__main__":
    main()
