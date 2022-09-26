class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        self.simplify()
        if self.denominator == 1:
            return str(self.numerator)
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, f2):
        denominator = self.denominator*f2.denominator
        a = int(denominator/self.denominator)*self.numerator
        b = int(denominator/f2.denominator)*f2.numerator
        numerator = a + b
        return Fraction(numerator, denominator)

    def __mul__(self, f2):
        numerator = self.numerator * f2.numerator
        denominator = self.denominator * f2.denominator
        return Fraction(numerator,denominator)

    def __sub__(self, f2):
        denominator = self.denominator * f2.denominator
        a = int(denominator/self.denominator)*self.numerator
        b = int(denominator/f2.denominator)*f2.numerator
        numerator = a - b
        return Fraction(numerator, denominator)

    def __truediv__(self, f2):
        f2.inverse()
        return self * f2

    def inverse(self):
        numerator = self.numerator
        denominator = self.denominator
        self.numerator = denominator
        self.denominator = numerator

    def simplify(self):
        for i in range(self.denominator, 1, -1):
            if (self.numerator % i == 0) and (self.denominator % i == 0):
                self.numerator = int(self.numerator / i)
                self.denominator = int(self.denominator / i)
            


f1 = Fraction(45, 2)
f2 = Fraction(98, 8)
addAns = f1 + f2
mulAns = f1 * f2
subAns = f1 - f2
divAns = f1 / f2
print(addAns)
print(mulAns)
print(subAns)
print(divAns)