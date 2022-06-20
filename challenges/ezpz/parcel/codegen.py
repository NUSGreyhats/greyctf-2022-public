from string import ascii_letters

hf = open("all.h", "w")
cf = open("all.c", "w")

for c in ascii_letters:
    for i in range(100):
        hf.write(f"void {c}{i}();\n")
        cf.write(f"void {c}{i}(){{}}\n")

hf.close()
cf.close()