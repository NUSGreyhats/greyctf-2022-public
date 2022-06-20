c = '982e47b0840b47a59c334facab3376a19a1b50ac861f43bdbc2e5bb98b3375a68d3046e8de7d03b4'

c = bytes.fromhex(c)

def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])

key = xor(c[:4], b'grey')

m = b''
for i in range(0, 40, 4):
    m += xor(bytes(c[i : i + 4]), key)

print(m)