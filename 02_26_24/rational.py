class Rational(object):
    """represents a rational number."""
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self._reduce()
    def __str__(self):
        """Returns the string representation of the number."""
        return str(self.numer) + "/" + str(self.denom)
    def numerator(self):
        """Returns the numerator."""
        return self.numer
    def denominator(self):
        """Returns the denominatior."""
        return self.denom
    def _gcd(self,a,b):
        """Euclid's algorithm for greatest common divisor (hacker's version)."""
        (a,b) = (max(a,b),min(a,b))
        while b > 0:
            (a,b) = (b, a % b)
        return a
    def _reduce(self):
        """Helper to reduce the number to lowest terms."""
        divisor = self._gcd(self.numer, self.denom)
        self.numer = self.numer // divisor
        self.denom = self.denom // divisor
    def __add__(self,other):
        """Returns the sum of the numbers. Self is the left operand and other is the right operand."""
        newNumer = self.numer * other.denom + other.numer * self.denom
        newDenom = self.denom * other.denom
        return Rational(newNumer, newDenom)
    def __sub__(self, other):
        """Returns the difference of the numbers. Self is the left operand and other is the right operand."""
        newNumer = self.numer * other.denom - other.numer * self.denom
        newDenom = self.denom * other.denom
        return Rational(newNumer, newDenom)
    def __mul__(self,other):
        """Returns the product of the numbers. Self is the left operand and other is the right operand."""
        newNumer = self.numer * other.numer
        newDenom = self.denom * other.denom
        return Rational(newNumer, newDenom)
    def __truediv__(self,other):
        """Returns the division of the numbers. Self is the left operand and other is the right operand."""
        newNumer = self.numer * other.denom
        newDenom = self.denom * other.numer
        return Rational(newNumer, newDenom)
    def __eq__(self,other):
        if self is other: 
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.numer == other.numer and self.denom == other.denom
    def __lt__(self,other):
        extremes = self.numer * other.denom
        means = other.numer * self.denom
        return extremes < means
    def __le__(self,other):
        return self < other or self == other
    def __ne__(self,other):
        return not(self == other)