from secrets import randbits
from Crypto.Util.number import getStrongPrime

n = 7
nn = n * 2
bits = 512

pp = int(getStrongPrime(bits))
p = GF(pp)
F.<x> = GF(pp ^ n)
mod = F.modulus()

F.<x> = p[]
mod = mod.polynomial(x) ^ 2

g = F.random_element(2 * n - 1)

print(p)
print(mod)
print(g)

def power(a, b, mod):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a % mod
        b >>= 1
        a = a * a % mod
    return res

def homSkele(P):
    deg = P.degree()
    R = PolynomialRing(p, 'a', deg * 2 + 1)
    originalVar = R.gens()
    x = originalVar[deg * 2]
    I = R.ideal([P(x)])
    R = R.quotient(I)
    vars = R.gens()
    x = vars[deg * 2]
    a = [vars[i] for i in range(deg)]
    b = [vars[i + deg] for i in range(deg)]
    g = 0
    f = 0
    for i in range(deg):
        g += a[i] * x ^ i

    for i in range(deg):
        f += b[i] * x ^ i

    h = (g * f).lift()
    mat = [[0 for _ in range(deg)] for _ in range(deg)]
    for i in range(deg):
        for j in range(deg):
            mat[i][j] = h.coefficient({b[j]:1, x: i})

    return (mat, [originalVar[i] for i in range(deg)])

def hom(skele, vars, g):
    subDic = {}
    coeff = g.list()
    n = len(skele)
    for i in range(n):
        subDic[vars[i]] = coeff[i] if i < len(coeff) else 0

    mat = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            mat[i][j] = skele[i][j].subs(subDic)

    return Matrix(p, mat)

def dlpMatrix(A, G):
    n = int(len(list(A)))
    print("Initiailizing Field... ")
    R.<k> = GF(pp ^ nn)
    print("Calculating Answer...")
    RR.<z> = R[]
    v = vector([1 for _ in range(n)])
    G = Matrix(R, G)
    lam = RR(G.charpoly()(x = z)).roots()[0][0]
    ff = G.charpoly()(x = z)/((z - lam)^2)
    v1 = (G - R(lam) * identity_matrix(R, n)) * ff(z = G) * v
    v2 = ff(z = G) * v
    Q = Matrix(R, [[R(i) for i in v1], [R(i) for i in v2]])
    B = list(Q.right_kernel().basis())
    Q = list(Q)
    for v in B:
        Q.append(v)
    Q = Matrix(R, Q)
    Q = Q.transpose()
    res = Q^(-1) * A * Q
    return lam * res[0][1] * res[0][0] ^ (-1)


def solve(A, g, P):
    print("generating skeleton...")
    skele, vars = homSkele(P)
    print("generating homomorphism...")
    A = hom(skele, vars, A % P)
    g = hom(skele, vars, g % P)
    print("solving DLP...")
    return dlpMatrix(A, g)
    
a = randbits(bits - 1)
b = randbits(bits - 1)
A = power(g, a, mod)
B = power(g, b, mod)

print(a)

print(solve(A, g, mod))


# Naive solution

tempMod = factor(mod)[0][0]
F.<z> = GF(pp ^ tempMod.degree(), name='z', modulus=tempMod, impl='pari_ffelt')
nA = A(x = z)
ng = g(x = z)
print(nA.log(ng))

# s = crt(vals, mods)

# print(power(B, s, mod))
# print(power(A, b, mod))