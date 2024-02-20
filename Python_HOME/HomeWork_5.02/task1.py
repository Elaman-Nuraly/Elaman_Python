class Device:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def turn_on(self):
        print(f"{self.brand} {self.model}: Включено")

    def turn_off(self):
        print(f"{self.brand} {self.model}: Выключено")

class CoffeeMachine(Device):

    def __init__(self, brand, model, water_capacity):
        super().__init__(brand, model)
        self.water_capacity = water_capacity

    def make_coffee(self):
        print(f"{self.brand} {self.model}: Готовим кофе")

    def refill_water(self, amount):
        print(f"{self.brand} {self.model}: Добавляем {amount} мл воды")

class Blender(Device):

    def __init__(self, brand, model, speed_levels):
        super().__init__(brand, model)
        self.speed_levels = speed_levels

    def blend(self):
        print(f"{self.brand} {self.model}: Мешаем ингредиенты")

    def change_speed(self, speed):
        print(f"{self.brand} {self.model}: Устанавливаем скорость {speed}")

class MeatGrinder(Device):

    def __init__(self, brand, model, power):
        super().__init__(brand, model)
        self.power = power

    def grind_meat(self):
        print(f"{self.brand} {self.model}: Измельчаем мясо")

    def change_power(self, power):
        print(f"{self.brand} {self.model}: Устанавливаем мощность {power}")


coffee_machine = CoffeeMachine("Braun", "CM550", 1000)
coffee_machine.turn_on()
coffee_machine.refill_water(200)
coffee_machine.make_coffee()
coffee_machine.turn_off()

blender = Blender("Philips", "HR3655", 10)
blender.turn_on()
blender.blend()
blender.change_speed(5)
blender.turn_off()

meat_grinder = MeatGrinder("Bosch", "MFW45020", 800)
meat_grinder.turn_on()
meat_grinder.grind_meat()
meat_grinder.change_power(900)
meat_grinder.turn_off()
