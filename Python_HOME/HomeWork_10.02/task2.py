class Airplane:

    def __init__(self, model, max_passengers, current_passengers):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = current_passengers

    def __eq__(self, other):
        return self.model == other.model

    def __gt__(self, other):
        return self.max_passengers > other.max_passengers

    def __lt__(self, other):
        return self.max_passengers < other.max_passengers

    def __le__(self, other):
        return self.max_passengers <= other.max_passengers

    def __ge__(self, other):
        return self.max_passengers >= other.max_passengers

    def __add__(self, value):
        self.current_passengers += value
        return self

    def __sub__(self, value):
        self.current_passengers -= value
        return self

    def __iadd__(self, value):
        self.current_passengers += value
        return self

    def __isub__(self, value):
        self.current_passengers -= value
        return self

plane1 = Airplane("Boeing 747", 400, 200)
plane2 = Airplane("Airbus A380", 500, 300)
print(plane1 == plane2) 
print(plane1 > plane2)  

plane1 += 50 
print(plane1.current_passengers)

plane2 -= 100
print(plane2.current_passengers)
