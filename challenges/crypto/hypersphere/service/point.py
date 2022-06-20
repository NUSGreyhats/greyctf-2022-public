# Quaternion

class Point():
    def __init__(self, a, b, c, d, p):
        assert (a * a + b * b + c * c + d * d) % p == 1
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.p = p

    def __str__(self):
        return f'{self.a}, {self.b}, {self.c}, {self.d}'

    def __mul__(self, other):
        assert self.p == other.p
        na = (self.a * other.a - self.b * other.b - self.c * other.c - self.d * other.d) % self.p
        nb = (self.a * other.b + self.b * other.a + self.c * other.d - self.d * other.c) % self.p
        nc = (self.a * other.c - self.b * other.d + self.c * other.a + self.d * other.b) % self.p
        nd = (self.a * other.d + self.b * other.c - self.c * other.b + self.d * other.a) % self.p
        return Point(na, nb, nc, nd, self.p)

    def __pow__(self, a):
        res = Point(1, 0, 0, 0, self.p)
        g = Point(self.a, self.b, self.c, self.d, self.p)
        while (a > 0):
            if (a & 1): res = res * g
            g = g * g
            a //= 2
        return res
