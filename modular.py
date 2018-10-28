#!/usr/bin/env python
class ModularInt(object):
    """
    Represent a modular arithmetic equivalence
    class. The value is stored as the remainder
    mod m.
    """
    def __init__(self, x, m):
        self.val = x % m
        self.modulo = m

    def __repr__(self):
        return "[{}]_{}".format(self.val, self.modulo)

    def __add__(self, other):
        if other.modulo != self.modulo:
            raise ValueError("+: Moduli must match!")

        new_val = self.val + other.val
        return ModularInt(new_val, self.modulo)

    def __sub__(self, other):
        if other.modulo != self.modulo:
            raise ValueError("-: Moduli must match!")

        new_val = self.val - other.val
        return ModularInt(new_val, self.modulo)

    def __mul__(self, other):
        if other.modulo != self.modulo:
            raise ValueError("*: Moduli must match!")
        
        new_val = self.val * other.val
        return ModularInt(new_val,  self.modulo)

    def __eq__(self, other):
        return self.modulo == other.modulo and self.val == other.val

    def __ne__(self, other):
        return not (self == other)

if __name__ == "__main__":
    a = ModularInt(10, 5)
    b = ModularInt(20, 5)
    print(a)
    print(b)
    print(a + b)
    print(a * b)

    print(a == b)
    print(a * b == a)
    print(a * b == b)
    print(a - b)
