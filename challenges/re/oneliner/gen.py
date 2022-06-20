import random
from string import ascii_letters, digits

flag = "grey{quite_big_ah}"

def make_true(off):
    r = random.randint(0, 10)

    if r == 0:
        x = random.randint(0, 100000)
        return f"{x} == {x}"
    if r == 1:
        x = random.randint(0, 100000)
        return f"{x} ^ {x} == 0"
    if r == 2:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        return f"{x:#x} ^ {x ^ y:#x} == {y:#x}"
    if r == 3:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        return f"{x:#x} + {y:#x} == {x + y:#x}"
    if r == 4:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        return f"{x:#x} - {y:#x} == {x - y:#x}"
    if r == 5:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        return f"{x:#x} * {y:#x} == {x * y:#x}"
    if r == 6:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        z = random.randint(0, 100000)
        return f"{x:#x} + {y:#x} - {z:#x} == {x + y - z:#x}"
    if r == 7:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        z = random.randint(0, 100000)
        return f"{x:#x} ^ {y:#x} - {z:#x} == {x ^ y - z:#x}"
    if r == 8:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        z = random.randint(0, 4)
        return f"{x:#x} & {y:#x} ** {z:#x} == {x & y ** z:#x}"
    if r == 9:
        x = random.randint(0, 255)
        y = random.randint(0, off-1)
        yc = flag[y]
        return f"{x:#x} ^ {ord(yc):#x} == {x ^ ord(yc):#x}"
    if r == 10:
        x = random.randint(0, 100)
        y = random.randint(0, off-1)
        yc = flag[y]
        return f"{x:#x} ** {ord(yc):#x} == {x ** ord(yc):#x}"

    return "True"

def make_false(off):
    r = random.randint(0, 10)
    bias = random.randint(2, 1000)

    if r == 0:
        x = random.randint(0, 100000)
        return f"{x} == {x + bias}"
    if r == 1:
        x = random.randint(0, 100000)
        return f"{x} ^ {x + bias} == 0"
    if r == 2:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        return f"{x:#x} ^ {x ^ y:#x} == {y ^ bias:#x}"
    if r == 3:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        return f"{x:#x} + {y:#x} == {x + y - bias:#x}"
    if r == 4:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        return f"{x:#x} - {y:#x} == {x - y + bias:#x}"
    if r == 5:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        return f"{x:#x} * {y:#x} == {x * y * bias:#x}"
    if r == 6:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        z = random.randint(0, 100000)
        return f"{x:#x} + {y:#x} - {z:#x} == {x + y - z + bias:#x}"
    if r == 7:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        z = random.randint(0, 100000)
        return f"{x:#x} ^ {y:#x} - {z:#x} == {x ^ y - z + bias:#x}"
    if r == 8:
        x = random.randint(0, 100000)
        y = random.randint(0, 100000)
        z = random.randint(0, 4)
        return f"{x:#x} & {y:#x} ** {z:#x} == {bias & x & y ** z:#x}"
    if r == 9:
        x = random.randint(0, 255)
        y = random.randint(0, off-1)
        yc = flag[y]
        return f"{x:#x} ^ {ord(yc):#x} == {x ^ ord(yc) ^ (bias % 0x100):#x}"
    if r == 10:
        x = random.randint(0, 100)
        y = random.randint(0, off-1)
        yc = flag[y]
        return f"{x:#x} ** {ord(yc):#x} == {x ** ord(yc) * (bias % 0x100):#x}"

    return "False"

def gen1(c, off, n, b):
    code = ""
    r = random.randint(0, n-1)
    for i in range(n):
        if b and i == r:
            code += f"grey[{off}] == '{c}' "
        else:
            code += f"grey[{off}] == '?' "

        if b and i == r:
            code += f"if ({make_true(off)}) else "
        else:
            code += f"if ({make_false(off)}) else "

    code += "False"

    return code

def gen2(s, off, n, b):
    if not b:
        n = random.randint(1, n)

    if len(s) == 1:
        return gen1(s[0], off, n, b)

    code = ""
    r = random.randint(0, n-1)
        # code += gen1(c, i, 4)
    for i in range(n):
        rc = random.choice(ascii_letters)
        while rc in [s[0], "'", "\\"]:
            rc = random.choice(ascii_letters)

        if b and i == r:
            code += f"(grey[{off}] == '{s[0]}') "
        else:
            code += f"(grey[{off}] == '{rc}') "

        if b and i == r:
            code += f"if ({gen2(s[1:], off+1, n, True)}) else ("
        else:
            code += f"if ({gen2(s[1:], off+1, n, False)}) else ("

    code += "False"

    for i in range(n):
        code += ")"

    return code

prog = "grey = input('i will tell you if you know the flag: ')\n"
prog += f"assert(len(grey) == {len(flag)})\n"
prog += "ans = "
# prog += gen1('g', 4)
prog += gen2(flag, 0, 6, True)
prog += "\n"
prog += "print('good' if ans else 'bad')\n"
# print(prog)

print(flag)
open("oneliner.py", "w").write(prog)
