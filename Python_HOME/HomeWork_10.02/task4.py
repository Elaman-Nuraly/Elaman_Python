class Flat:
    
    def __init__(self, apartment, price):
        self.apartment = apartment
        self.price = price

    def __eq__(self, other):
        return self.apartment == other.apartment

    def __ne__(self, other):
        return self.apartment != other.apartment

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price

    def __ge__(self, other):
        return self.price >= other.price

    def __le__(self, other):
        return self.price <= other.price

if __name__ == "__main__":
    apartment1 = Flat(85, 12000000)
    apartment2 = Flat(56, 8000000)

    print(apartment1 == apartment2)
    print(apartment1 != apartment2)
    print(apartment1 > apartment2)
    print(apartment1 < apartment2)
    print(apartment1 >= apartment2)
    print(apartment1 <= apartment2)
