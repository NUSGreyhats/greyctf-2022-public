from secrets import randbits
from Crypto.Util.number import getPrime

n = 10
pp = 599
p = GF(pp)
F.<x> = GF(pp^(n-2))
mod = F.modulus()

F.<x> = p[]
mod = mod.polynomial(x) ^ 2
g = F.random_element(n - 1)

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

    return (mat, [originalVar[i] for i in range(deg)], R)

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


print("generating skeleton...")
skele, vars, R = homSkele(mod)
g = hom(skele, vars, g % mod)
print(g.eigenvalues())

# while True:
#     print("Trying...")
#     g = x + 1
#     g = hom(skele, vars, g % mod)
#     print(g)
#     roots = g.charpoly().roots()
#     if (len(roots) != 0):
#         print(g)
#         break
#     else:
#         print("Failed")