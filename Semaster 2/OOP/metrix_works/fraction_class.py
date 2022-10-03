class cFraction:
    def __init__(self, numerator, denominator):
        if (denominator == 0):
            raise ZeroDivisionError
        if (denominator < 0):
            denominator *=  -1
            numerator *= -1
        self.numerator = numerator
        self.denominator = denominator
        self.simplify()

    def __str__(self):
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, f2):
        if not(isinstance(f2, cFraction)):
            f2 = cFraction(f2, 1)
        denominator = self.denominator*f2.denominator
        numerator = self.numerator * f2.denominator + f2.numerator * self.denominator
        result = cFraction(numerator, denominator)
        self.simplify()
        return result

    def __mul__(self, f2):
        if not(isinstance(f2, cFraction)):
            f2 = cFraction(f2, 1)
        numerator = self.numerator * f2.numerator
        denominator = self.denominator * f2.denominator
        result = cFraction(numerator, denominator)
        result.simplify()
        return result

    def __sub__(self, f2):
        if not(isinstance(f2, cFraction)):
            f2 = cFraction(f2, 1)
        f2.numerator = f2.numerator * -1
        return self + f2

    def __truediv__(self, f2):
        if not(isinstance(f2, cFraction)):
            return self * cFraction(1, f2)
        return self * cFraction(f2.denominator, f2.numerator)


    def __lt__(self, f2):
        if not(isinstance(f2, cFraction)):
            f2 = cFraction(f2, 1)
        a, b = self.__getNumeAfterMakingDenoSame(f2)
        return a < b
    
    def __gt__(self, f2):
        return f2 < self

    def __eq__(self, f2):
        if not(isinstance(f2, cFraction)):
            f2 = cFraction(f2, 1)
        a, b = self.__getNumeAfterMakingDenoSame(f2)
        return a == b

    def __ne__(self, f2):
        return not(self == f2)

    def __ge__(self, f2):
        return (self == f2) or (self > f2)

    def __le__(self, f2):
        return (self == f2) or (self < f2)

    def __getNumeAfterMakingDenoSame(self, f2):
        if (self.denominator != f2.denominator):
            denominator = self.denominator * f2.denominator
            a = denominator / self.denominator
            b = denominator / f2.denominator
            return self.numerator * a, f2.numerator * b
        return self.numerator, f2.numerator

    def inverse(self):
        self.numerator, self.denominator = self.denominator, self.numerator

    def simplify(self):
        def gcd(m, n):
            if (n == 0):
                return m
            return gcd(n, m%n)
        greatestDivisor = gcd(self.numerator, self.denominator)      
        self.numerator = int(self.numerator/greatestDivisor)
        self.denominator = int(self.denominator/greatestDivisor)

f1 = cFraction(4, 7)
f2 = cFraction(2, 8)
print(f1+f2)