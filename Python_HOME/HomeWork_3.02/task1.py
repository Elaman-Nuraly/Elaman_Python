class MainClass:

    def __init__(self, text):
        self._text = text

    def set_text(self, new_text=None):
        if new_text is not None:
            self._text = new_text
        else:
            self._text = input("Введите новый текст: ")

    def get_text(self):
        return self._text

class SubClass(MainClass):

    def __init__(self, text, number):
        super().__init__(text)
        self._number = number

    def set_number(self, new_number):
        self._number = new_number

    def get_number(self):
        return self._number

main_obj = MainClass("Hello")
print("Текст в главном классе:", main_obj.get_text())
sub_obj = SubClass("Python", 42)
print("Текст в классе-потомке:", sub_obj.get_text())
print("Число в классе-потомке:", sub_obj.get_number())
main_obj.set_text("Goodbay")
sub_obj.set_number(123)
print("Новый текст в главном классе:", main_obj.get_text())
print("Новое число в классе-потомке:", sub_obj.get_number())
