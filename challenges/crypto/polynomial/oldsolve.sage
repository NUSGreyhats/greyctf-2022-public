from secrets import randbits
from Crypto.Util.number import getPrime

pp = int(12625803040683422737419121862921765179117467231218406881413843802954269461448551645774337768115511283344078849985537509719962591658462577276196012004429087)
p = GF(pp)
F.<x> = p[]
mod = x^20 + 9*x^19 + 12625803040683422737419121862921765179117467231218406881413843802954269461448551645774337768115511283344078849985537509719962591658462577276196012004429079*x^18 + 12625803040683422737419121862921765179117467231218406881413843802954269461448551645774337768115511283344078849985537509719962591658462577276196012004428763*x^17 + 12625803040683422737419121862921765179117467231218406881413843802954269461448551645774337768115511283344078849985537509719962591658462577276196012004428306*x^16 + 3484*x^15 + 18883*x^14 + 9714*x^13 + 12625803040683422737419121862921765179117467231218406881413843802954269461448551645774337768115511283344078849985537509719962591658462577276196012004307410*x^12 + 12625803040683422737419121862921765179117467231218406881413843802954269461448551645774337768115511283344078849985537509719962591658462577276196012004120033*x^11 + 12625803040683422737419121862921765179117467231218406881413843802954269461448551645774337768115511283344078849985537509719962591658462577276196012004358300*x^10 + 924378*x^9 + 2063540*x^8 + 2733487*x^7 + 3575886*x^6 + 5196393*x^5 + 6773246*x^4 + 6827390*x^3 + 4799570*x^2 + 2111300*x + 531005

g = F.random_element(20)

def power(a, b, mod):
    if b == 0:
        return 1
    elif b % 2 == 0:
        return power(a, b // 2, mod) ** 2 % mod
    else:
        return a * power(a, b - 1, mod) % mod

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
    n = len(list(A))
    g = Matrix(p, G).charpoly()

    MOD = []
    ans = []

    for i in factor(g):
        deg = i[0].degree()
        R = GF(pp ^ deg)
        F.<x> = R[]
        root = F(i[0](x = x)).roots()[0][0]
        Q = Matrix(R, list((Matrix(R, G) - root * identity_matrix(R, n)).right_kernel().basis()))
        B = list(Q.right_kernel().basis())
        Q = list(Q)
        for v in B:
            Q.append(v)
        Q = Matrix(R, Q)
        target = Q * Matrix(R, A) * Q^(-1)
        if (deg >= 2):
            F.<x> = FiniteField(pp ^ deg, modulus=R.modulus(), impl='pari_ffelt')
            tt = target[0][0].polynomial()(x)
            kk = root.polynomial()(x)
            MOD.append(kk.multiplicative_order())
            ans.append(tt.log(kk))
        else:
            F = GF(pp)
            tt = F(target[0][0])
            kk = F(root)
            if (tt == 0):
                continue
            MOD.append(kk.multiplicative_order())
            ans.append(tt.log(kk))

    return CRT(ans, MOD), lcm(MOD)


def solve(A, g, P):
    print("generating skeleton...")
    skele, vars = homSkele(P)
    print(skele)
    print("generating homomorphism...")
    # A = hom(skele, vars, A % P)
    #g = hom(skele, vars, g % P)
    #print(g)
    #print(g.charpoly().roots())
    #return dlpMatrix(A, g)
    
    
a = randbits(512)
b = randbits(512)
A = power(g, a, mod)
B = power(g, b, mod)

factors = factor(mod)

vals = []
mods = []

for i in factors:
    tempMod = i[0] ^ i[1]
    solve(A, g, tempMod)
    # x, y = solve(A, g, tempMod)
    # vals.append(x)
    # mods.append(y)

# Naive solution

# for i in factors:
#     tempMod = i[0] ^ i[1]
#     print(tempMod)
#     if (tempMod.degree() < 2):
#         F.<z> = GF(pp ^ tempMod.degree(), name='z', modulus=tempMod)
#         nA = A(x = z)
#         ng = g(x = z)
#         vals.append(discrete_log(nA, ng))
#         mods.append(ng.multiplicative_order())
#     else:
#         F.<z> = GF(pp ^ tempMod.degree(), name='z', modulus=tempMod, impl='pari_ffelt')
#         nA = A(x = z)
#         ng = g(x = z)
#         if (nA == 0):
#             continue
#         vals.append(nA.log(ng))
#         mods.append(ng.multiplicative_order())

# s = crt(vals, mods)

# print(power(B, s, mod))
# print(power(A, b, mod))