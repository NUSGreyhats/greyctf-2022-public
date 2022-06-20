

# This file was *autogenerated* from the file gen2.sage
from sage.all_cmdline import *   # import sage library

_sage_const_10 = Integer(10); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2)
from secrets import randbits
from Crypto.Util.number import getPrime

while True:
    n = _sage_const_10 

    pp = int(getPrime(n))
    F = GF(pp)

    M = [[getPrime(n) if i == j else _sage_const_0  for j in range(n)] for i in range(n)]

    M[_sage_const_0 ][_sage_const_1 ] = _sage_const_1 
    M[_sage_const_1 ][_sage_const_1 ] = M[_sage_const_0 ][_sage_const_0 ]

    M = Matrix(F, M)

    P = random_matrix(F, n, algorithm='unimodular')
    A = P * M * P**(-_sage_const_1 )

    R = F['x']; (x,) = R._first_ngens(1)
    b = _sage_const_1  + x + x**_sage_const_2 

    g = R.random_element(n - _sage_const_1 )
    t1 = b * g
    t2 = _sage_const_2  * b

    poly = _sage_const_1 

    for i in factor(t1 - t2):
        if (i[_sage_const_1 ] >= _sage_const_2 ):
            poly *= i[_sage_const_0 ] ** i[_sage_const_1 ]
            continue
        if (i[_sage_const_0 ].degree() == _sage_const_1 ):
            continue
        poly *= i[_sage_const_0 ]


    if (poly.degree() == n):
        print(pp)
        print(i[_sage_const_0 ])
        print(g)
        print(t1 % i[_sage_const_0 ])
        print(t2 % i[_sage_const_0 ])
        exit()

