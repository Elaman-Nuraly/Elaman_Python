class City:
    def __init__(self: object, city_name: str, region_name: str, country_name: str, population_city: str, population_country: str, postal_code: str, phone_code: str) -> None:
        self.city_name = "Аламаты"
        self.region_name = "Алматинская область"
        self.country_name = "Казахстан"
        self.population_city = 2000000 
        self.population_country = 19000000
        self.postal_code = "050010"
        self.phone_code = "+7 (7273) xxxx"

    def input_data(self):
        self.city_name = input("Введите название города: ")
        self.region_name = input("Введите название региона: ")
        self.country_name = input("Введите название страны: ")
        self.population_city = int(input("Введите количество жителей в городе: "))
        self.population_country = int(input("Введите количество жителей в стране: "))
        self.postal_code = input("Введите почтовый код: ")
        self.phone_code = input("ВВедите телефонный код: ")

    def display_data(self):
        print("Название города:", self.city_name)
        print("Название региона:", self.region_name)
        print("Название страны:", self.country_name)
        print("Кол-во жителей в городе:", self.population_city)
        print("Кол-во жителей в стране:", self.population_country)

    def get_city_name(self):
        return self.city_name

    def get_region_name(self):
        return self.region_names

    def get_country_name(self):
        return self.country_name

    def get_population_city(self):
        return self.population_city

    def get_population_country(self):
        return self.population_country

if __name__ == "__main__":
    