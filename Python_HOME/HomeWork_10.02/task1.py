class Circle:

    def __init__(self, radius):
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __gt__(self, other):
        return self.radius > other.radius

    def __lt__(self, other):
        return self.radius < other.radius

    def __le__(self, other):
        return self.radius <= other.radius

    def __ge__(self, other):
        return self.radius >= other.radius

    def __add__(self, value):
        return Circle(self.radius + value)

    def __sub__(self, value):
        return Circle(self.radius - value)

    def __iadd__(self, value):
        self.radius += value
        return self

    def __isub__(self, value):
        self.radius -= value
        return self

if __name__ == "__main__":

    circle1 = Circle(7)
    circle2 = Circle(4)
    print(circle1 == circle2)  
    print(circle1 < circle2)
    print(circle1 <= circle2)
    print(circle1 >= circle2)

    circle1 += 2 
    print(circle1.radius)

    circle2 -= 1 
    print(circle2.radius)
    