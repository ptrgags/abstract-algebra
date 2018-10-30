#!/usr/bin/env python

class Polynomial(object):
    """
    Polynomial where the coefficients can be from
    any field
    """
    # TODO: add `one` for pretty printing
    def __init__(self, *coeffs, zero=0):
        """
        Initialize a polynomial.

        Coefficients must be given for degree 0, degree 1, etc.
        Insert a zero wherever there is no coefficient.

        Example:

        Polynomial(1, 0, 3, 2) = 2x^3 + 3x^2 + 1
        """
        self.coeffs = list(coeffs)
        while self.coeffs and self.coeffs[-1] == zero:
            self.coeffs = self.coeffs[:-1]

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
        deg = self.degree + other.degree
        result = [self.zero] * (deg + 1)

        # Combine polynomials
        for i, a in enumerate(self.coeffs):
            for j, b in enumerate(other.coeffs):
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
        
        Note: this returns -1 for constant polynomials
        """
        return len(self.coeffs) - 1

    @property
    def leading_coeff(self):
        """
        Return the leading coefficient of the polynomial
        """
        return self.coeffs[self.degree]

    def format_terms(self):
        """
        Pretty print each term as a generator
        """
        for i, a in enumerate(self.coeffs):
            if not a:
                continue

            if i == 0:
                yield "({})".format(a)
            else:
                yield "({})x^{}".format(a, i)

    def __repr__(self):
        terms = reversed(list(self.format_terms()))
        return " + ".join(terms)

    def __divmod__(self, other):
        """
        Find the quotient and remainder when f(x) // g(x)
        using long division.

        (see the class method below for implementation)

        This returns (q, r) where q is the quotient, r is the
        remainder
        """
        return Polynomial.divmod(self, other)

    def __floordiv__(self, other):
        """
        Compute the quotient when f(x) // g(x)

        Note that I use f // g and not f / g because
        polynomial division is closer to integer division
        (quotient, remainder) than real division (quotient only)
        """
        q, _ = divmod(self, other, self.zero)
        return q

    def __mod__(self, other):
        """
        Compute the remainder when f(x) // g(x)
        """
        _, r = divmod(self, other, self.zero)
        return r

    @classmethod
    def divmod(cls, dividend, divisor, zero=0):
        """
        Compute the quotient and remainder when polynomial
        f is divided by g using recursive long division

        returns (q, r) where q is the quotient, r is the remainder
        """
        if dividend.degree < divisor.degree:
            # Base case: deg(f) < deg(g) so g does not divide f
            # so return f as the remainder with quotient 0
            return (Polynomial(*[], zero=zero), dividend)
        else:
            # Recursive case: compute one term of the quotient
            # and subtract a multiple of the divisor

            # Compute the leading term
            coeff = dividend.leading_coeff / divisor.leading_coeff
            degree = dividend.degree - divisor.degree 
            
            # Construct a Polynomial object
            term_as_array = [zero] * degree + [coeff]
            quotient_term = Polynomial(*term_as_array, zero=zero)

            # subtract q * g from our dividend f for the next round
            # of calculations
            new_remainder = dividend - quotient_term * divisor

            # Recursively compute the quotient of what's left
            # until we find the remainder of f / g
            q, r = cls.divmod(new_remainder, divisor, zero)

            # we need to add our quotient term to the quotient:
            return (quotient_term + q, r)


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


    # TODO: Division won't work until I get
    # multiplication to work
    h = Polynomial(1.0, 0.0, 3.0, 4.0, zero=0.0)
    i = Polynomial(4.0, 1.0, 3.0, 2.0, zero=0.0)
    q, r = divmod(h, i)
    print(h)
    print(i)
    print(q)
    print(r)
    print(q * i + r)

    j = Polynomial(-3.0, 2.0, zero=0.0)
    print(j)
    print(divmod(h, j))

