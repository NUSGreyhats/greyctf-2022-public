from secrets import randbits
from Crypto.Util.number import getPrime

while True:
    n = 10

    pp = int(getPrime(n))
    F = GF(pp)

    M = [[getPrime(n) if i == j else 0 for j in range(n)] for i in range(n)]

    M[0][1] = 1
    M[1][1] = M[0][0]

    M = Matrix(F, M)

    P = random_matrix(F, n, algorithm='unimodular')
    A = P * M * P^(-1)

    R.<x> = F[]
    b = 1 + x + x^2

    g = R.random_element(n - 1)
    t1 = b * g
    t2 = 2 * b

    poly = 1

    for i in factor(t1 - t2):
        if (i[1] >= 2):
            poly *= i[0] ^ i[1]
            continue
        if (i[0].degree() == 1):
            continue
        poly *= i[0]


    if (poly.degree() == n):
        print(pp)
        print(i[0])
        print(g)
        print(t1 % i[0])
        print(t2 % i[0])
        exit()
