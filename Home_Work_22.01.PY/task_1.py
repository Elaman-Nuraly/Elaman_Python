class Human:
    """
    Class Human
    """
    def __init__(
        self: object, fl_name: str, birth_date: str, phone: str, city: str, country: str) -> None:
        self.fl_name = fl_name
        self.__birth_date = birth_date
        self.phone = phone
        self.city = city
        self.country = country

    def get_class_attributies(self):
        return f"{self.fl_name}\n{self.get_birthday}\n{self.city}\n{self.country}\n{self.phone}"

    def set_class_attributies(self, country, city, phone):
        self.country = country
        self.city = city
        self.phone = phone

    def set_class_attributies(self, country):
        self.country = country

    def set_class_attributies(self, city):
        self.city = city

    def set_class_attributies(self, phone):
        self.phone = phone

    def set_class_attributies(self, fl_name):
        self.fl_name

    def set_birthday(self, birthday):
        self.__birth_date = birthday

    def get_birthday(self):
        return self.__birth_date

    def __str__(self):
        return f"{self.get_birthday} - {self.fl_name}"

if __name__ == "__main__":
    HUMAN_ATTRIBUTES = {
        "fl_name": "Иван Иванов",
        "birth_date": "01.01.1990",
        "phone": "+79001234567",
        "city": "Москва",
        "country": "Россия",
    }
    ELAMAN_ATTRIBUTES = {
        "fl_name": "Еламан Нуралы",
        "birth_date": "28.08.2004",
        "phone": "+7 777 297 94 907",
        "city": "Алматы",
        "country": "Казахстан", 
    }

    ELAMAN_CLASS = Human(**ELAMAN_ATTRIBUTES)
    HUMAN_CLASS = Human(**HUMAN_ATTRIBUTES)
    print(HUMAN_CLASS.get_class_attributies())
    print(HUMAN_CLASS.get_class_attributies())

    print("-" * 50, end="\n")

    HUMAN_CLASS.set_class_attributies(
        country="Казахстан", city="Алматы", phone="+7 777 297 94 967")
    print(HUMAN_CLASS.get_class_attributies())

    HUMAN_CLASS.city = "Астана"
    print("-" * 50, end="\n")
    print(HUMAN_CLASS.get_class_attributies())
