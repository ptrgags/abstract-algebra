#!/usr/bin/env python
from modular import ModularInt
from polynomial import Polynomial
from euclidean_algo import gcd, xgcd

if __name__ == "__main__":
    modulo = 5
    zero = ModularInt.zero(modulo)
    one = ModularInt.one(modulo)

    coeffs_f = [ModularInt(x, modulo) for x in [1, 4, 5, -14, 2]]
    coeffs_g = [ModularInt(x, modulo) for x in [2, 5, 6]]

    f = Polynomial(*coeffs_f, zero=zero)
    g = Polynomial(*coeffs_g, zero=zero)

    print("f =", f)
    print("g =", g)
    print("f / g = {} with remainder {}".format(f, g, f // g, f % g))

    poly_zero = Polynomial.zero(zero)
    poly_one = Polynomial.one(one, zero)
    d = gcd(f, g, zero=poly_zero)
    print("gcd(f, g) = {}".format(d))
    
    # TODO: Need to debug thhis more
    #d, x, y = xgcd(f, g, zero=poly_zero, one=poly_one) 
    #print("({}) * ({}) + ({}) * ({}) = {}".format(x, f, y, g, d))
