

# This file was *autogenerated* from the file solve.sage
from sage.all_cmdline import *   # import sage library

_sage_const_7 = Integer(7); _sage_const_2 = Integer(2); _sage_const_512 = Integer(512); _sage_const_1 = Integer(1); _sage_const_0 = Integer(0)
from secrets import randbits
from Crypto.Util.number import getStrongPrime

n = _sage_const_7 
nn = n * _sage_const_2 
bits = _sage_const_512 

pp = int(getStrongPrime(bits))
p = GF(pp)
F = GF(pp ** n, names=('x',)); (x,) = F._first_ngens(1)
mod = F.modulus()

F = p['x']; (x,) = F._first_ngens(1)
mod = mod.polynomial(x) ** _sage_const_2 

g = F.random_element(_sage_const_2  * n - _sage_const_1 )

print(p)
print(mod)
print(g)

def power(a, b, mod):
    res = _sage_const_1 
    while b > _sage_const_0 :
        if b & _sage_const_1 :
            res = res * a % mod
        b >>= _sage_const_1 
        a = a * a % mod
    return res

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

    return (mat, [originalVar[i] for i in range(deg)])

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

def dlpMatrix(A, G):
    n = int(len(list(A)))
    print("Initiailizing Field... ")
    R = GF(pp ** nn, names=('k',)); (k,) = R._first_ngens(1)
    print("Calculating Answer...")
    RR = R['z']; (z,) = RR._first_ngens(1)
    v = vector([_sage_const_1  for _ in range(n)])
    G = Matrix(R, G)
    lam = RR(G.charpoly()(x = z)).roots()[_sage_const_0 ][_sage_const_0 ]
    ff = G.charpoly()(x = z)/((z - lam)**_sage_const_2 )
    v1 = (G - R(lam) * identity_matrix(R, n)) * ff(z = G) * v
    v2 = ff(z = G) * v
    Q = Matrix(R, [[R(i) for i in v1], [R(i) for i in v2]])
    B = list(Q.right_kernel().basis())
    Q = list(Q)
    for v in B:
        Q.append(v)
    Q = Matrix(R, Q)
    Q = Q.transpose()
    res = Q**(-_sage_const_1 ) * A * Q
    return lam * res[_sage_const_0 ][_sage_const_1 ] * res[_sage_const_0 ][_sage_const_0 ] ** (-_sage_const_1 )


def solve(A, g, P):
    print("generating skeleton...")
    skele, vars = homSkele(P)
    print("generating homomorphism...")
    A = hom(skele, vars, A % P)
    g = hom(skele, vars, g % P)
    print("solving DLP...")
    return dlpMatrix(A, g)
    
a = randbits(bits - _sage_const_1 )
b = randbits(bits - _sage_const_1 )
A = power(g, a, mod)
B = power(g, b, mod)

print(a)

print(solve(A, g, mod))


# Naive solution

tempMod = factor(mod)[_sage_const_0 ][_sage_const_0 ]
F = GF(pp ** tempMod.degree(), name='z', modulus=tempMod, impl='pari_ffelt', names=('z',)); (z,) = F._first_ngens(1)
nA = A(x = z)
ng = g(x = z)
print(nA.log(ng))

# s = crt(vals, mods)

# print(power(B, s, mod))
# print(power(A, b, mod))

