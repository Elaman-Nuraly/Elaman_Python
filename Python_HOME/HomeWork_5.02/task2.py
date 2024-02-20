class Ship:
    
    def __init__(self, name, length, displacement):
        self.name = name
        self.length = length
        self.displacement = displacement

    def sail(self):
        print(f"{self.name}: Корабль отправился в плавание")

    def anchor(self):
        print(f"{self.name}: Корабль опустил якорь")

class Frigate(Ship):

    def __init__(self, name, length, displacement, missile_capacity):
        super().__init__(name, length, displacement)
        self.missile_capacity = missile_capacity

    def fire_missiles(self):
        print(f"{self.name}: Фрегат выпустил ракеты")

    def reload_missiles(self):
        print(f"{self.name}: Фрегат перезаряжает ракеты")

class Destroyer(Ship):

    def __init__(self, name, length, displacement, cannon_caliber):
        super().__init__(name, length, displacement)
        self.cannon_caliber = cannon_caliber

    def fire_cannons(self):
        print(f"{self.name}: Эсминец открыл огонь из пушек")

    def repair(self):
        print(f"{self.name}: Эсминец находится на ремонте")

class Cruiser(Ship):

    def __init__(self, name, length, displacement, missile_capacity, cannon_caliber):
        super().__init__(name, length, displacement)
        self.missile_capacity = missile_capacity
        self.cannon_caliber = cannon_caliber

    def fire_missiles(self):
        print(f"{self.name}: Крейсер выпустил ракеты")

    def fire_cannons(self):
        print(f"{self.name}: Крейсер открыл огонь из пушек")


frigate = Frigate("Адмирал Григорович", 125, 3800, 32)
frigate.sail()
frigate.fire_missiles()
frigate.anchor()

destroyer = Destroyer("Североморск", 160, 5600, 130)
destroyer.sail()
destroyer.fire_cannons()
destroyer.repair()

cruiser = Cruiser("Петр Великий", 250, 28000, 192, 130)
cruiser.sail()
cruiser.fire_missiles()
cruiser.fire_cannons()