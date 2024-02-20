class Wheels:

    def __init__(self, number_of_wheels):
        self.number_of_wheels = number_of_wheels

    def display_wheels_info(self):
        print(f"This car has {self.number_of_wheels} wheels.")

class Engine:

    def __init__(self, horsepower):
        self.horsepower = horsepower

    def display_engine_info(self):
        print(f"This car has an engine with {self.horsepower} horsepower.")

class Doors:

    def __init__(self, number_of_doors):
        self.number_of_doors = number_of_doors

    def display_doors_info(self):
        print(f"This car has {self.number_of_doors} doors.")

class Car(Wheels, Engine, Doors):

    def __init__(self, number_of_wheels, horsepower, number_of_doors):
        Wheels.__init__(self, number_of_wheels)
        Engine.__init__(self, horsepower)
        Doors.__init__(self, number_of_doors)

    def display_car_info(self):
        self.display_wheels_info()
        self.display_engine_info()
        self.display_doors_info()

my_car = Car(4, 200, 2)
my_car.display_car_info()
