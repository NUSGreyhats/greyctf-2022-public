from pwn import *

operations = ["add", "mul", "sub", "neg", "inc"]

r = remote("35.247.145.55", 15521)

r.recvuntil("ready!\n")
r.sendline("START")

def run(st):
    i = st[-1]
    if (i not in operations):
        if (len(st) > 1):
            if (st[-2] == "neg"):
                k = int(st.pop())
                st.pop()
                st.append(-k)
                return run(st)
            if (st[-2] == "inc"):
                k = int(st.pop())
                st.pop()
                st.append(k + 1)
                return run(st)
        if (len(st) > 2 and st[-2] not in operations):
            if (st[-3] == "add"):
                x = int(st.pop())
                y = int(st.pop())
                st.pop()
                st.append(x + y)
                return run(st)
            if (st[-3] == "mul"):
                x = int(st.pop())
                y = int(st.pop())
                st.pop()
                st.append(x * y)
                return run(st)
            if (st[-3] == "sub"):
                y = int(st.pop())
                x = int(st.pop())
                st.pop()
                st.append(x - y)
                return run(st)

for i in range(100):
    p = r.recvline().strip()
    ls = p.split(b" ")
    st = []
    for i in ls:
        i = i.decode()
        st.append(i)
        run(st)
        
    ans = st.pop()
    r.sendline(str(ans))
    r.recvline()

print(r.recvall())
