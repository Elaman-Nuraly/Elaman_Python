class Roman:
    
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return Roman(self.value + other.value)

    def __sub__(self, other):
        return Roman(self.value - other.value)
    
    def __mul__(self, other):
        return Roman(self.value * other.value)

    def __truediv__(self, other):
        return Roman(self.value / other.value)

if __name__ == "__main__":
    roman1 = Roman(10)
    roman2 = Roman(5)

    result_add = roman1 + roman2
    print(result_add.value)

    result_sub = roman1 - roman2
    print(result_sub.value)

    result_mul = roman1 * roman2
    print(result_mul.value)

    result_div = roman1 / roman2
    print(result_div.value)
