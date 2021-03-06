

# This file was *autogenerated* from the file gen.sage
from sage.all_cmdline import *   # import sage library

_sage_const_10 = Integer(10); _sage_const_599 = Integer(599); _sage_const_2 = Integer(2); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)
from secrets import randbits
from Crypto.Util.number import getPrime

n = _sage_const_10 
pp = _sage_const_599 
p = GF(pp)
F = GF(pp**(n-_sage_const_2 ), names=('x',)); (x,) = F._first_ngens(1)
mod = F.modulus()

F = p['x']; (x,) = F._first_ngens(1)
mod = mod.polynomial(x) ** _sage_const_2 
g = F.random_element(n - _sage_const_1 )

def homSkele(P):
    deg = P.degree()
    R = PolynomialRing(p, 'a', deg * _sage_const_2  + _sage_const_1 )
    originalVar = R.gens()
    x = originalVar[deg * _sage_const_2 ]
    I = R.ideal([P(x)])
    R = R.quotient(I)
    vars = R.gens()
    x = vars[deg * _sage_const_2 ]
    a = [vars[i] for i in range(deg)]
    b = [vars[i + deg] for i in range(deg)]
    g = _sage_const_0 
    f = _sage_const_0 
    for i in range(deg):
        g += a[i] * x ** i

    for i in range(deg):
        f += b[i] * x ** i

    h = (g * f).lift()
    mat = [[_sage_const_0  for _ in range(deg)] for _ in range(deg)]
    for i in range(deg):
        for j in range(deg):
            mat[i][j] = h.coefficient({b[j]:_sage_const_1 , x: i})

    return (mat, [originalVar[i] for i in range(deg)], R)

def hom(skele, vars, g):
    subDic = {}
    coeff = g.list()
    n = len(skele)
    for i in range(n):
        subDic[vars[i]] = coeff[i] if i < len(coeff) else _sage_const_0 

    mat = [[_sage_const_0  for _ in range(n)] for _ in range(n)]

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

