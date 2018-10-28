#!/usr/bin/env python

class Polynomial(object):
    """
    Polynomial where the coefficients can be from
    any field
    """
    def __init__(self, *coeffs, zero=0):
        """
        Initialize a polynomial.

        Coefficients must be given for degree 0, degree 1, etc.
        Insert a zero wherever there is no coefficient.

        Example:

        Polynomial(1, 0, 3, 2) = 2x^3 + 3x^2 + 1
        """
        self.coeffs = coeffs

        # For custom types, store the additive identity
        # since this is needed for summing values
        self.zero = zero

    def __eq__(self, other):
        # Make sure we have the same number of coefficients
        if self.degree != other.degree:
            return False

        # Compare the coefficients
        for c1, c2 in zip(self.coeffs, other.coeffs):
            if c1 != c2:
                return False
        return True

    def __ne__(self, other):
        return not (self == other)

    def __getitem__(self, deg):
        """
        Get one of the coefficients from the polynomial..
        If the degree is too big, just return 0
        """
        if deg <= self.degree: 
            return self.coeffs[deg]
        else:
            return self.zero

    def __add__(self, other):
        results = []
        max_deg = max(self.degree, other.degree)

        # Pair up the coefficients add add
        for i in range(max_deg + 1):
            results.append(self[i] + other[i])
        return Polynomial(*results, zero=self.zero)

    def __neg__(self):
        negated = [-a for a in self.coeffs]
        return Polynomial(*negated, zero=self.zero)

    def __sub__(self, other):
        return self + (-other)

    def __mul__(self, other):
        deg = self.degree * other.degree
        result = [self.zero] * (deg + 1)

        # Combine polynomials
        for i, a in enumerate(self.coeffs):
            for j, b in enumerate(self.coeffs):
                result[i + j] += a * b

        return Polynomial(*result, self.zero)

    def __call__(self, x):
        """
        Evaluate the polynomial for a given x.
        the types of the coefficients and x must match
        """
        result = self.zero
        for i, a in enumerate(self.coeffs):
            result += a * x ** i
        return result 

    @property
    def degree(self):
        """
        Get the degree of the polynomial
        """
        return len(self.coeffs) - 1

    def format_terms(self):
        """
        Pretty print each term as a generator
        """
        for i, a in enumerate(self.coeffs):
            if not a:
                continue

            if i == 0:
                yield str(a)
            else:
                yield "{}x^{}".format(a, i)

    def __repr__(self):
        terms = reversed(list(self.format_terms()))
        return " + ".join(terms)


if __name__ == "__main__":
    f = Polynomial(1, 0, 3, 2)
    print(f)
    print(f.degree)

    g = Polynomial(4, 1, 3, 2)
    print(g)

    print(f == f)
    print(f == g)
    print(f + g)
    print(-f)
    print(f - g)
    print(f * g)

    print(f(2))
