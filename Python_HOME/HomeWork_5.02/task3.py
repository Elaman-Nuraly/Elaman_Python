class Square:
    
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

    def perimeter(self):
        return 4 * self.side_length

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius

class InscribedCircleInSquare(Square, Circle):

    def __init__(self, side_length):
        Square.__init__(self, side_length)
        Circle.__init__(self, side_length / 2)

    def info(self):
        print(f"Окружность, вписанная в квадрат со стороной {self.side_length}:")
        print(f"Площадь квадрата: {self.area()}")
        print(f"Периметр квадрата: {self.perimeter()}")
        print(f"Площадь вписанной окружности: {self.area()}")
        print(f"Длина окружности: {self.circumference()}")

inscribed_circle = InscribedCircleInSquare(8)
inscribed_circle.info()
