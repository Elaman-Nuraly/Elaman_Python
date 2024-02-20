class Car:
    
    def __init__(self, model, year, manufacturer, engine_capacity, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_capacity = engine_capacity
        self.color = color
        self.price = price

    def input_data(self):
        self.model = input("Введите название модели: ")
        self.year = input("Введите год выпуска: ")
        self.manufacturer = input("Введите производителя: ")
        self.engine_capacity = input("Введите объем двигателя: ")
        self.color = input("Введите цвет машины: ")
        self.price = input("Введите цену: ")

    def output_data(self):
        print("Название модели:", self.model)
        print("Год выпуска:", self.year)
        print("Производитель:", self.manufacturer)
        print("Объем двигателя:", self.engine_capacity)
        print("Цвет машины:", self.color)
        print("Цена:", self.price)

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_manufacturer(self):
        return self.manufacturer

    def get_engine_capacity(self):
        return self.engine_capacity

    def get_color(self):
        return self.color

    def get_price(self):
        return self.price

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def set_engine_capacity(self, engine_capacity):
        self.engine_capacity = engine_capacity

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price

if __name__ == "__main__":
    car1 = Car("BMW", "2018", "BMW", "3.0L", "черный", "35000$")
    car1.output_data()
    print("\nИзменение цены машины:")
    car1.set_price("25000$")
    print("Новая цена:", car1.get_price())
