class Dinosaur:
    def __init__(self,name):
        self.name = name
        self.attack_power = 15
        self.health = 30

    def attack(self,robot):
        robot.health -= self.attack_power
        print(f'{robot.name} was attacked by {self.name} and did {self.attack_power} damaged leaving  the robot with {robot.health} health')