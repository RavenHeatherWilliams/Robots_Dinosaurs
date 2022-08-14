from weapon import Weapon

#weapons_list = ["Sword", "Laser", "Acid"]

class Robot:
    def __init__(self,name):
        self.name = name
        self.health = 30
        self.weapon = Weapon("laser")

    def attack(self,dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f'{dinosaur.name} was attacked by {self.name} and did {self.weapon.attack_power} massive damage leaving the dinosaur with {dinosaur.health} health')
  