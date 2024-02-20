class Stadium:
    
    def __init__(self, name, opening_date, country, city, capacity):
        self.name = name
        self.opening_date = opening_date
        self.country = country
        self.city = city
        self.capacity = capacity

    def input_data(self):
        self.name = input("Введите название стадиона: ")
        self.opening_date = input("Введите дату открытия стадиона: ")
        self.country = input("Введите страну: ")
        self.city = input("Введите город: ")
        self.capacity = input("Введите вместимость стадиона: ")

    def output_data(self):
        print("Название стадиона:", self.name)
        print("Дата открытия:", self.opening_date)
        print("Страна:", self.country)
        print("Город:", self.city)
        print("Вместимость:", self.capacity)

    def get_name(self):
        return self.name

    def get_opening_date(self):
        return self.opening_date

    def get_country(self):
        return self.country

    def get_city(self):
        return self.city

    def get_capacity(self):
        return self.capacity

    def set_name(self, name):
        self.name = name

    def set_opening_date(self, opening_date):
        self.opening_date = opening_date

    def set_country(self, country):
        self.country = country

    def set_city(self, city):
        self.city = city

    def set_capacity(self, capacity):
        self.capacity = capacity

if __name__ == "___main__":
    stadium1 = Stadium("Camp Nou", "24 сентября 1957 года", "Испания", "Барселона", "99 354 человека")
    stadium1.output_data()
print("\nИзменение вместимости стадиона:")
stadium1.set_capacity("100 000 человек")
print("Новая вместимость:", stadium1.get_capacity())
