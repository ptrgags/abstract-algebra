#!/usr/bin/env python
def gcd(a, b, zero=0):
    """
    Greatest common divisor of a, b
    """
    if b == zero:
        return a
    else:
        return gcd(b, a % b)

def xgcd(a, b, zero=0, one=1):
    r0 = a
    x0 = one
    y0 = zero
    r1 = b
    x1 = zero
    y1 = one

    while r1 != zero:
        q = r0 // r1
        r0, r1 = r1, r0 - q * r1
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    # The previous row stores the gcd (the remainder) and the two
    # coefficients
    return (r0, x0, y0)

if __name__ == "__main__":
    print(gcd(12, 3))

    g, x, y = xgcd(12, 5)
    print("{} = {} * {} + {} * {}".format(g, x, 12, y, 5))
