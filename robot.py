from weapon import Weapon

#weapons_list = ["Sword", "Laser", "Acid"]

class Robot:
    def __init__(self,name):
        self.name = name
        self.health = 30
        self.weapon = Weapon("laser")

    def attack(self,dinosaur):
        self.health -= self.attack 
        print(f'{self.dinosaur} was attacked by {self.name} and did {self.attack_power} massive damage leaving the dinosaur with {dinosaur.health} health')
  