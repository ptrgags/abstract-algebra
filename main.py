#!/usr/bin/env python
from modular import ModularInt
from polynomial import Polynomial

if __name__ == "__main__":
    modulo = 5
    zero = ModularInt.zero(modulo)

    coeffs_f = [ModularInt(x, modulo) for x in [1, 4, 5, -14, 2]]
    coeffs_g = [ModularInt(x, modulo) for x in [2, 5, 6]]

    print(coeffs_f)
    print(coeffs_g)

    f = Polynomial(*coeffs_f, zero=zero)
    g = Polynomial(*coeffs_g, zero=zero)

    print(f)
    print(g)
    print(f + g)

    print(f(ModularInt(3, modulo)))
