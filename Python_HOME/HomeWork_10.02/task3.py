class Complex:

    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        divisor = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / divisor
        imag = (self.imag * other.real - self.real * other.imag) / divisor
        return Complex(real, imag)

# Здесь указан пример
c1 = Complex(4, 9)
c2 = Complex(7, 6)

print("Сложение:", c1 + c2)
print("Вычитание:", c1 - c2)
print("Умножение:", c1 * c2)
print("Деление:", c1 / c2)
